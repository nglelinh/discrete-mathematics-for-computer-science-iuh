---
layout: post
title: "Connection pool sizing: Đếm kết nối với Little's Law"
categories: chapter09
date: 2021-01-01
order: 5
required: false
lang: en
excerpt: "Áp dụng định luật Little (Little's Law) và công thức HikariCP để tính kích thước connection pool cho cơ sở dữ liệu, phân biệt rõ số người dùng đồng thời với số kết nối DB thực sự bận."
---

Một trong những phản xạ tốn kém nhất khi hệ thống chậm là "vặn lớn mọi thông số cấu hình" — thấy 10.000 người dùng online liền tăng connection pool lên 200 kết nối mỗi server. Kết quả thường ngược hẳn kỳ vọng: độ trễ P99 vọt lên gấp 20 lần và cơ sở dữ liệu ngạt thở vì đổi ngữ cảnh (context switching). Đằng sau nghịch lý đó là một công thức cực gọn của lý thuyết hàng đợi: **Định luật Little (Little's Law)**.

**Mạch bài học:** Tách bạch **người dùng đồng thời** với **kết nối DB đang bận** $$\longrightarrow$$ **Định luật Little** $$L = \lambda W$$ $$\longrightarrow$$ công thức thực nghiệm **HikariCP** $$\longrightarrow$$ mở rộng nhiều pod bằng **PgBouncer**.

## Kiến thức cần nhớ: Lý thuyết hàng đợi và hệ thống CSDL đứng sau connection pool là gì?

- **Lý thuyết hàng đợi & Định luật Little (Queueing Theory):** Nghiên cứu mối quan hệ trạng thái dừng giữa tốc độ đến trung bình $$\lambda$$ (requests/giây), thời gian phục vụ trung bình $$W$$ (giây), và số lượng yêu cầu đang nằm trong hệ thống $$L = \lambda W$$ — đúng cho mọi phân phối đến/phục vụ ổn định.
- **Tranh chấp tài nguyên & Đổi ngữ cảnh (Contention & Context Switching):** Khi số kết nối DB đang chạy song song vượt xa số lõi CPU và băng thông I/O của máy chủ DB, nhân hệ điều hành phải liên tục chuyển luồng và tranh khóa (lock contention), làm $$W$$ tăng phi tuyến và đẩy thông lượng đi xuống.
- **Ghép kênh kết nối (Connection Multiplexing):** Kỹ thuật đặt bộ trung gian như PgBouncer ở chế độ *transaction pooling* để hàng trăm kết nối ứng dụng nhàn rỗi chia sẻ hiệu quả một nhóm nhỏ kết nối vật lý tới PostgreSQL.

Ở bài transistor và ALU, chúng ta đã quan sát bit và phép cộng ở tầng phần cứng. Mục này chuyển sang **bài toán hàng đợi** ở tầng hệ thống: **connection pool sizing** — tính toán số kết nối cơ sở dữ liệu bằng **định luật Little (Little's Law)** và công thức tham chiếu của HikariCP. Một tình huống rất phổ biến: khi bộ phận marketing báo “10.000 người dùng đồng thời”, CTO đề xuất tăng HikariCP lên 200 kết nối mỗi pod. Tuy nhiên, **người dùng đồng thời** (concurrent users) không đồng nghĩa với **kết nối DB đang bận** (busy connections), và đặt pool quá lớn thậm chí có thể khiến PostgreSQL **chậm hơn**.

Dũng, trưởng nhóm DevOps, mở Grafana và thấy chỉ số `active_connections` của PostgreSQL đã chạm **180** trên máy chủ **8 lõi CPU + 1 SSD**, trong khi độ trễ P99 của truy vấn tăng vọt từ 12 ms lên **340 ms**. Nhật ký ứng dụng liên tục báo lỗi:

```text
HikariPool-1 - Connection is not available, request timed out after 30000ms
```

Một nghịch lý xuất hiện khiến Dũng dừng tay trước khi tăng thêm cấu hình: pool **lớn hơn** → DB **chậm hơn** → yêu cầu **chờ lâu hơn** → lỗi timeout **nhiều hơn**. Dù khách hàng doanh nghiệp đang chờ buổi demo và CTO vẫn cho rằng “nhiều kết nối hơn sẽ an toàn hơn”, số liệu thực tế lại chỉ ra điều ngược lại.

Brett Wooldridge, tác giả **HikariCP**, đã tổng hợp trong bài viết [About Pool Sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) dựa trên lý thuyết hàng đợi và các bài đo hiệu năng PostgreSQL: pool quá lớn làm giảm thông lượng (throughput) vì chi phí chuyển ngữ cảnh (context switch) và tranh chấp khóa (lock contention). Thay vì ước lượng theo cảm tính, câu trả lời nằm ở **Little's Law** và công thức định cỡ kết nối dựa trên năng lực phần cứng.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Client-server-model.svg"
       alt="Mô hình client–server — nhiều client chia sẻ tài nguyên server qua pool kết nối"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.5a: “10.000 người dùng” không tương đương 10.000 kết nối DB — chỉ công thức $$L = \lambda \times W$$ mới cho biết cần bao nhiêu kết nối thực sự bận (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Client-server-model.svg">Wikimedia Commons</a>, CC BY-SA 3.0).</figcaption>
</p>
</figure>

---

## Người dùng đồng thời khác với kết nối cơ sở dữ liệu

Khi bàn về kích thước pool, người ta thường nhầm lẫn hai mức độ “đồng thời”. **Người dùng đồng thời** (concurrent users) là số người đang mở ứng dụng cùng lúc — phần lớn thời gian họ đang đọc giao diện, điền biểu mẫu hoặc chờ mạng mà **không** giữ kết nối tới PostgreSQL. Trong khi đó, **kết nối DB đồng thời** (concurrent DB connections) là số phiên TCP và tiến trình backend PostgreSQL đang **thực sự bận** tại một thời điểm: đang thực thi truy vấn, đang trong giao dịch (transaction) hoặc đang chờ khóa.

Một người dùng đọc bảng điều khiển suốt 30 giây thực chất chỉ **giữ kết nối DB trong vài mili giây** mỗi lần API gửi truy vấn. Vì vậy, 10.000 người dùng trực tuyến không đồng nghĩa với 10.000 kết nối. Đây là bài toán **đếm có điều kiện**: ta chỉ đếm các truy vấn đang thực sự *hoạt động* trên cơ sở dữ liệu, không đếm số phiên HTTP hay số thẻ trình duyệt đang mở.

**Connection pool** duy trì sẵn $$N$$ kết nối, cấp cho luồng ứng dụng mượn khi cần và thu hồi ngay khi truy vấn kết thúc. Nếu $$N$$ quá nhỏ, yêu cầu phải xếp hàng chờ ở phía ứng dụng; nhưng nếu $$N$$ quá lớn, bản thân cơ sở dữ liệu sẽ quá tải vì mỗi kết nối PostgreSQL là một tiến trình riêng cạnh tranh CPU và bộ đệm dùng chung (`shared_buffers`).

![Database connection pool — concept](/discrete-mathematics-for-computer-science-iuh/img/course/Client-server-model.svg)

<p class="textbook-figure-caption" data-figure="9.12">Nhiều client chia sẻ một số lượng nhỏ kết nối DB thông qua connection pool thay vì ánh xạ 1:1 giữa người dùng và kết nối.</p>

Dũng nhớ lại sự cố tuần trước: marketing đếm **DAU** (số người dùng hoạt động hằng ngày), SRE đếm **RPS** (số yêu cầu mỗi giây), còn CTO đếm **số thẻ trình duyệt mở đồng thời**. Ba đại lượng dẫn đến ba đề xuất kích thước pool khác nhau, nhưng chỉ có số liệu ở tầng truy vấn DB mới phù hợp để định cỡ PostgreSQL. Kích thước pool không trả lời câu hỏi “bao nhiêu người đang trực tuyến” mà trả lời “bao nhiêu truy vấn đang chạy đồng thời trên DB”.

---

## Little's Law — công thức hàng đợi giúp tính đúng kích thước pool

Ở trạng thái ổn định (steady state), **định luật Little (Little's Law)** liên kết ba đại lượng:

<div class="textbook-equation" markdown="1">
$$L = \lambda \times W$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trong đó, $$L$$ là số đơn vị trung bình đang ở trong hệ thống (với connection pool, đó là số kết nối **đang bận** trung bình); $$\lambda$$ là tốc độ đến hay thông lượng (số truy vấn hoàn thành mỗi giây); và $$W$$ là thời gian trung bình một truy vấn lưu lại trong hệ thống (từ lúc mượn kết nối cho đến khi trả về pool).

Ví dụ, nếu DB xử lý $$\lambda = 1000$$ truy vấn/giây và mỗi truy vấn tốn trung bình $$W = 0{,}01$$ giây (10 ms), số kết nối bận trung bình là $$L = 10$$. Để hạn chế tình trạng chờ khi lưu lượng dao động ngắn hạn, kích thước pool thường được chọn theo công thức:

<div class="textbook-equation" markdown="1">
$$N \geq \lceil L \rceil + \text{buffer}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Khoản đệm (buffer) nhỏ chỉ dùng để hấp thụ các đỉnh tải ngắn hạn, không phải để nhân theo số lượng người dùng hay DAU.

Dũng lấy số liệu đo thực tế từ Grafana và APM: giờ cao điểm có **500 request/s** gửi tới API đăng nhập, mỗi request thực hiện trung bình **2 truy vấn** xuống DB, và mỗi truy vấn mất **5 ms** khi pool còn ở mức hợp lý. Thông lượng truy vấn là:

<div class="textbook-equation" markdown="1">
$$\lambda = 500 \times 2 = 1000 \text{ query/s}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Thời gian trung bình trong hệ thống:

<div class="textbook-equation" markdown="1">
$$W = 0{,}005 \text{ s}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Số kết nối bận trung bình:

<div class="textbook-equation" markdown="1">
$$L = 1000 \times 0{,}005 = 5$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trung bình chỉ có **5 kết nối bận**, nên cấu hình pool khoảng **10–15** cho một pod là hợp lý, thay vì 200. Dũng gửi bảng tính lên Slack giải thích rằng con số “10.000 người dùng” của marketing có thể là DAU cả ngày, còn tải đỉnh thực tế chỉ vài trăm RPS và Little's Law cho ra con số định lượng rõ ràng.

<div class="content-box insight-box textbook-block" markdown="1">
Các sự cố “10.000 người dùng” thường bắt nguồn từ việc nhầm lẫn giữa **DAU**, **người dùng đồng thời** và **RPS**. Chỉ tích $$\lambda \times W$$ mới xác định đúng số kết nối cần thiết dựa trên khối lượng truy vấn thực tế.
</div>

---

### Thử nghiệm: hàng đợi và định luật Little

Điều chỉnh tốc độ đến, thời gian phục vụ và số kết nối để quan sát độ dài hàng đợi, thời gian chờ và quan hệ $$L = \lambda W$$.

<div class="interactive-demo" markdown="1">
<div data-demo="sim-explainer" data-tab="queue"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Công thức HikariCP — vì sao 200 kết nối chậm hơn 20

Wiki của HikariCP tóm lược các kết quả đo hiệu năng từ [PostgreSQL Wiki — Number of connections](https://wiki.postgresql.org/wiki/Number_Of_Database_Connections) thành công thức khởi điểm cho tải giao dịch (OLTP) trên **một** máy chủ PostgreSQL:

<div class="textbook-equation" markdown="1">
$$\text{connections} = \text{core\_count} \times 2 + \text{effective\_spindle\_count}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Ở đây, **core_count** là số lõi CPU **của máy chủ chạy PostgreSQL** (không phải số lõi của máy chủ ứng dụng hay số pod Kubernetes), còn **effective_spindle_count** là số ổ đĩa vật lý (với **một ổ SSD**, giá trị thường lấy là **1**).

Với máy chủ DB của Dũng gồm 8 lõi CPU và 1 SSD:

<div class="textbook-equation" markdown="1">
$$\text{pool} = 8 \times 2 + 1 = 17$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Khuyến nghị kỹ thuật rất rõ ràng: **không** đặt 200 kết nối “cho chắc”. Trên PostgreSQL, mỗi kết nối tương ứng với một **tiến trình backend** kèm bộ nhớ riêng. Khi số tiến trình vượt quá khả năng xử lý đồng thời của phần cứng, hệ thống tiêu tốn tài nguyên vào việc chuyển ngữ cảnh CPU, tranh chấp khóa trên `shared_buffers`, checkpoint và tắc nghẽn I/O. Biểu đồ đo hiệu năng trên wiki HikariCP cho thấy thông lượng đạt đỉnh ở kích thước pool **nhỏ** rồi **suy giảm** khi tiếp tục tăng số kết nối — khớp với hiện tượng P99 tăng từ 12 ms lên 340 ms lúc `active_connections` chạm 180.

Đối chiếu hai kết quả: Little's Law cho tải đăng nhập cần trung bình $$L \approx 5$$ kết nối bận, còn công thức HikariCP chỉ ra giới hạn hiệu quả cho toàn bộ máy chủ DB là khoảng 17 kết nối. Hai công thức trả lời hai câu hỏi khác nhau — “lưu lượng hiện tại cần bao nhiêu?” và “máy chủ DB xử lý tối ưu khoảng bao nhiêu trước khi tự chậm lại?” — nhưng cả hai đều khẳng định mức 200 là quá lớn.

<div class="content-box warning-box textbook-block" markdown="1">
Công thức $$2 \times \text{cores} + \text{spindles}$$ chỉ là **điểm xuất phát** cho tải OLTP trên **một** instance DB. Các hệ thống thiên về phân tích dữ liệu (analytics), bản sao chỉ đọc (read replica) hoặc máy chủ chạy nhiều cơ sở dữ liệu cần đo đạc (profiling) riêng. Luôn đo $$\lambda$$ và $$W$$ trên hệ thống thực tế trước khi chốt cấu hình production.
</div>

---

## Nhiều máy chủ ứng dụng và vai trò của PgBouncer

Khi hệ thống chạy **3 instance** API và mỗi instance đặt pool HikariCP là **10**, tổng số kết nối tới PostgreSQL sẽ là **30** — vẫn thấp hơn giới hạn mặc định `max_connections = 100`, nhưng đã vượt mức tối ưu 17 của máy chủ 8 lõi. Khi mở rộng thêm pod ứng dụng, tổng số kết nối từ phía client tăng tuyến tính theo số replica, trong khi năng lực xử lý của DB đơn lẻ không tăng theo.

**PgBouncer** giải quyết vấn đề này bằng cơ chế ghép kênh (multiplexing) ở lớp trung gian: nhiều kết nối từ ứng dụng được gom lại và dùng chung một số lượng nhỏ kết nối thật tới PostgreSQL. Luồng hoạt động trở thành: nhiều luồng ứng dụng → mỗi instance giữ pool 50 kết nối tới PgBouncer → PgBouncer phân phối xuống khoảng 17 tiến trình backend thật trên PostgreSQL. Quy luật toán học vẫn là Little's Law với một hàng đợi trung gian; độ trễ $$W$$ có thể tăng rất nhẹ nếu ứng dụng giữ giao dịch lâu không phù hợp với chế độ `transaction mode` của PgBouncer.

Trong kênh xử lý sự cố chiều thứ Sáu, Dũng đề xuất cấu hình HikariCP **15 kết nối mỗi pod** (3 pod tạo 45 kết nối phía client) kết hợp PgBouncer ở chế độ transaction mode với `default_pool_size=17`, sát với công thức HikariCP. Sau khi triển khai lại, độ trễ P99 giảm về dưới 20 ms, lỗi timeout chấm dứt và buổi demo diễn ra suôn sẻ.

Dũng ghi ba ý chính vào tài liệu vận hành (runbook): **người dùng đồng thời** đếm người, **$$\lambda$$** đếm truy vấn/giây, còn **pool** đếm kết nối DB đang bận — ba đại lượng hoàn toàn khác nhau. Pool lớn hơn không phải lúc nào cũng nhanh hơn; vượt ngưỡng phần cứng sẽ khiến cơ sở dữ liệu chậm đi rõ rệt do tranh chấp tài nguyên.

**Đọc thêm**: [HikariCP — About Pool Sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) · [PostgreSQL Wiki — Number of connections](https://wiki.postgresql.org/wiki/Number_Of_Database_Connections)

---

## Ví dụ tính tay làm từng bước: Áp dụng Định luật Little và công thức HikariCP cho 10.000 người dùng

Giả sử ứng dụng web của bạn đang có **10.000 người dùng đồng thời**, trung bình mỗi người bấm một thao tác gọi API mỗi **20 giây** (think time = 20s). Mỗi request API thực hiện **2 truy vấn SQL**, mỗi truy vấn mất trung bình **5 ms** ($$0{,}005$$ giây) trên máy chủ PostgreSQL có **8 lõi CPU** và **1 ổ SSD**.

1. **Tính tốc độ truy vấn đến DB ($$\lambda$$):**
   - Số request API mỗi giây: $$\lambda_{\text{API}} = \frac{10\,000}{20} = 500\text{ req/s}$$.
   - Vì mỗi request chạy 2 truy vấn SQL: $$\lambda_{\text{SQL}} = 500 \times 2 = 1\,000\text{ queries/s}$$.
2. **Tính số kết nối DB thực sự bận trung bình ($$L$$) bằng Định luật Little:**
   $$L = \lambda_{\text{SQL}} \cdot W = 1\,000 \times 0{,}005 = 5\text{ kết nối bận!}$$
   Con số này khác một trời một vực so với ảo giác "10.000 người dùng nên cần vài trăm kết nối".
3. **Tính trần khuyến nghị theo công thức HikariCP:**
   $$\text{connections} = (\text{core\_count} \times 2) + \text{effective\_spindle\_count} = (8 \times 2) + 1 = 17 \approx 16\text{–}20\text{ kết nối.}$$
4. **Phân bổ cho cụm 4 pod ứng dụng:**
   - Nếu không có PgBouncer, chia đều trần 20 kết nối cho 4 pod $$\Rightarrow$$ mỗi pod chỉ nên đặt `maximumPoolSize = 5` (thay vì `50` hay `200`).
   - Kiểm tra hệ số tải trung bình: $$L / 20 = 5 / 20 = 25\%$$, đủ khoảng đệm gấp 4 lần cho các đợt tăng đột biến (burst) mà vẫn giữ CPU DB ở vùng thông lượng tối ưu.

### Giải thích: Vì sao pool nhỏ hơn lại chạy nhanh hơn
1. **Bước 1 — Đếm đúng đại lượng:** Phần lớn thời gian trong một phiên, người dùng đang đọc màn hình chứ không giữ kết nối DB. Đại lượng quyết định kích thước pool là $$L = \lambda W$$, không phải tổng số người đang mở trình duyệt.
2. **Bước 2 — Giới hạn vật lý nằm ở CPU và đĩa của DB:** Máy chủ 8 lõi tại một thời điểm chỉ thực thi tối đa 8 luồng CPU. Mở 180 kết nối đồng thời không tạo thêm lõi CPU nào — nó chỉ bắt PostgreSQL tốn chu kỳ đổi ngữ cảnh, đẩy cache CPU (L1/L2) bị xóa liên tục và kéo dài $$W$$.
3. **Bước 3 — Vòng xoáy tích cực khi giữ pool gọn:** Khi xếp hàng ở tầng ứng dụng (pool size $$\approx 16\text{–}20$$), mỗi truy vấn vào DB được phục vụ nhanh gọn trong vài mili-giây ($$W$$ nhỏ), nên hàng đợi xả cực nhanh và độ trễ P99 giảm mạnh.
4. **Bước 4 — Tách bài toán ngang bằng PgBouncer:** Khi cần scale lên 20 pod ứng dụng, dùng PgBouncer ở giữa để gom hàng trăm kết nối logic vào đúng ~20 kết nối vật lý tới PostgreSQL.

$$10\,000\text{ users} \;\xrightarrow{\text{think time } 20\text{s}}\; \lambda = 1\,000\text{ qps} \;\xrightarrow{W = 5\text{ ms}}\; L = 5 \ll 200.$$

## Bài tập thực hành

### Bài tập 1

API thanh toán (checkout) xử lý lúc cao điểm **200 request/s**. Mỗi request gọi trung bình **3 truy vấn** DB, mỗi truy vấn mất **8 ms**. Áp dụng Little's Law, tính $$L$$ (số kết nối bận trung bình) và đề xuất kích thước pool $$N$$ với khoản đệm (buffer) là 5.

<details>
<summary>Đáp án</summary>

Thông lượng truy vấn:

<div class="textbook-equation" markdown="1">
$$\lambda = 200 \times 3 = 600 \text{ query/s}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Thời gian trung bình trong hệ thống:

<div class="textbook-equation" markdown="1">
$$W = 0{,}008 \text{ s}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Áp dụng Little's Law:

<div class="textbook-equation" markdown="1">
$$L = 600 \times 0{,}008 = 4{,}8$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trung bình có **4,8** kết nối bận. Cộng thêm buffer bằng 5:

<div class="textbook-equation" markdown="1">
$$N \geq \lceil 4{,}8 \rceil + 5 = 5 + 5 = 10$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nên đặt pool khoảng **10** cho một instance ứng dụng phục vụ tải này, không tính theo số người dùng trực tuyến.

</details>

### Bài tập 2

Một máy chủ PostgreSQL có **16 lõi CPU** và **2 SSD** (lấy effective spindle = 2). Áp dụng công thức HikariCP, tính số kết nối khuyến nghị cho **một** DB instance. Nếu có **4 pod** API, mỗi pod đặt pool bằng 20, tổng số kết nối là bao nhiêu và so với ngưỡng công thức như thế nào?

<details>
<summary>Đáp án</summary>

Theo công thức HikariCP:

<div class="textbook-equation" markdown="1">
$$\text{pool} = 16 \times 2 + 2 = 34$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tổng số kết nối khuyến nghị tới DB instance là khoảng **34**.

Với 4 pod, mỗi pod 20 kết nối:

<div class="textbook-equation" markdown="1">
$$4 \times 20 = 80 \text{ connection}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Vì **80 > 34** (vượt hơn gấp đôi ngưỡng tham chiếu), dù vẫn dưới `max_connections`, thông lượng và độ trễ có thể kém hơn so với pool nhỏ. Nên giảm pool mỗi pod xuống khoảng 8–10 hoặc đặt **PgBouncer** phía trước để gom 80 kết nối client xuống khoảng 34 kết nối backend thật.

</details>

### Bài tập 3

Bộ phận marketing báo **50.000 DAU**, SRE đo được cao điểm **800 RPS** lúc 20 giờ, còn DevOps đặt HikariCP = 500 vì “người dùng đông”. Phân tích vì sao ba con số này không thể thay thế cho nhau và đại lượng nào mới được đưa vào Little's Law.

<details>
<summary>Đáp án</summary>

**DAU** đếm tổng số người dùng riêng biệt trong **cả ngày**, không phản ánh số người thao tác đồng thời tại giờ cao điểm hay tốc độ truy vấn. **800 RPS** là tốc độ yêu cầu HTTP tới máy chủ ứng dụng — cần nhân với số truy vấn DB trung bình trên mỗi yêu cầu mới ra thông lượng truy vấn $$\lambda$$ (query/s). Cấu hình **pool = 500** nhầm lẫn giữa quy mô người dùng và số kết nối DB, đồng thời bỏ qua hoàn toàn độ trễ truy vấn $$W$$.

Little's Law chỉ dùng $$\lambda$$ (truy vấn/giây) và $$W$$ (giây/truy vấn) đo trên **DB**. Ví dụ, nếu 800 RPS × 2 truy vấn × $$W = 6$$ ms thì $$L = 1600 \times 0{,}006 = 9{,}6$$ — mức pool khoảng 15–20 hợp lý hơn nhiều so với 500, và vẫn cần đối chiếu với ngưỡng $$2 \times \text{cores} + \text{spindles}$$ của máy chủ DB.

</details>

### Bài tập 4

Một hệ thống gồm **5 pod** API, mỗi pod cấu hình HikariCP **12** (tổng 60 kết nối client). PgBouncer đặt `default_pool_size=20` kết nối xuống máy chủ PostgreSQL 8 lõi CPU + 1 SSD. Giải thích vai trò của PgBouncer trong bài toán đếm và vì sao hai con số 60 và 20 không mâu thuẫn nhau.

<details>
<summary>Đáp án</summary>

**60** là tổng số kết nối từ các pod ứng dụng tới PgBouncer, giúp mỗi pod giữ đủ kết nối chờ để luồng xử lý không bị nghẽn khi mượn kết nối. **20** là số kết nối backend thật mà PgBouncer duy trì tới PostgreSQL bằng cách ghép nhiều giao dịch ngắn của client lên ít kết nối server hơn.

Little's Law ở **tầng DB** áp dụng cho các truy vấn thực thi tại PostgreSQL, nơi số kết nối bận thực tế bị giới hạn bởi mức 20 của PgBouncer chứ không phải 60. Công thức HikariCP cho máy 8 lõi + 1 SSD cho kết quả **17**, nên `default_pool_size=20` nằm rất gần ngưỡng tối ưu; nếu bỏ PgBouncer và mở thẳng 60 kết nối vào PostgreSQL, hệ thống dễ gặp tăng độ trễ tương tự sự cố của Dũng.

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Định cỡ connection pool là một bài toán **đếm định lượng**, không phải ước lượng theo cảm tính. **Người dùng đồng thời** và **DAU** đo quy mô người dùng, **$$\lambda$$** đo số truy vấn mỗi giây, còn **pool** đo số kết nối DB đang bận hoặc sẵn sàng phục vụ — ba đại lượng này không tương ứng 1:1.

**Little's Law** $$L = \lambda \times W$$ xác định số kết nối bận trung bình cần thiết từ thông lượng và độ trễ truy vấn, cộng thêm một khoản đệm nhỏ cho đỉnh tải. **Công thức HikariCP** $$2 \times \text{cores} + \text{spindles}$$ cung cấp mốc khởi điểm cho một máy chủ PostgreSQL để tránh tình trạng pool quá lớn làm DB chậm lại. Khi mở rộng theo chiều ngang với nhiều pod ứng dụng, **PgBouncer** giúp ghép kênh để tổng số kết nối backend luôn giữ gần ngưỡng tối ưu.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu hiện tượng **bùng nổ tổ hợp (combinatorial explosion)** trong kiểm thử phần mềm theo phân tích của [testRigor](https://testrigor.com/blog/what-is-combinatorial-testing/) — cách rút gọn 324 cấu hình trình duyệt–hệ điều hành–thiết bị xuống khoảng 15 ca kiểm thử pairwise mà vẫn phủ hết mọi **cặp** tham số.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=fYjiS2ogcoE">Little&#x27;s Law Explained | L = λ × W | Queueing Theory &amp; System Design</a> — Industry Ready Coder, tiếng Anh. Trình bày trực quan định luật Little $$L = \lambda W$$, nền tảng cho công thức định cỡ pool trong bài.
- <a href="https://www.youtube.com/watch?v=2Lx7QtaPDKw">Little’s Law In Queuing Theory</a> — Explified Labs, tiếng Anh. Giải thích vai trò của định luật Little trong hàng đợi, liên kết số người dùng đồng thời với số kết nối thực tế.
- <a href="https://www.youtube.com/watch?v=Cp-aFYHLiCw">Database Connection Pool Sizing - Demystified! by Jasmin Fluri</a> — Devoxx, tiếng Anh. Phân tích định cỡ connection pool trên tải thực tế, tương ứng trực tiếp với tình huống HikariCP.
