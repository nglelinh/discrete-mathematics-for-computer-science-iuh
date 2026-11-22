---
layout: post
title: "Cardinality và analytics: Bài học từ 1M DNS queries/giây của Cloudflare"
categories: chapter09
date: 2021-01-01
order: 9
required: false
lang: en
excerpt: "Phân tích khái niệm cardinality (số giá trị phân biệt trên một cột) qua bài toán xử lý hơn 1 triệu truy vấn DNS mỗi giây của Cloudflare và vai trò của HyperLogLog trong hệ thống phân tích dữ liệu."
---

Ở bài trước, chúng ta đã phân biệt xác suất va chạm $$P(\text{collision})$$ và kỳ vọng số lần trùng $$E[\text{matches}]$$. Mục này xét một đại lượng đếm khác trong hạ tầng dữ liệu: **lực lượng (cardinality)** — $$\vert V_C\vert $$, số giá trị **phân biệt** trên một cột — yếu tố quyết định việc tổng hợp (aggregate) nhật ký có **nén** được dữ liệu hay không. Bài viết trên [Cloudflare Blog](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/) (Vavruša, 2017) mô tả hệ thống xử lý **hơn 1 triệu truy vấn DNS mỗi giây**: tổng hợp theo `response_code` (khoảng 12 giá trị) giảm mạnh số dòng lưu trữ, còn tổng hợp theo `query_name` (có thể lên tới hàng triệu tên miền khác nhau) có mức nén rất thấp và không ổn định (0–60×, trường hợp xấu nhất là 1×). Một sự cố thực tế hay gặp là bảng điều khiển ở mức zone hiển thị hoàn toàn bình thường trong khi một tập con `qname` cụ thể lại có độ trễ rất cao — tín hiệu ở chiều cardinality cao bị làm loãng khi tổng hợp sai chiều.

Bài toán toán rời rạc cốt lõi ở đây có thể tóm gọn như sau:

> Tổng hợp dữ liệu theo một cột có **cardinality cao** (nhiều giá trị phân biệt) có thể **không giảm** số dòng lưu trữ, thậm chí làm tăng chi phí xử lý so với dữ liệu gốc.

Cột **response code** chỉ có khoảng 12 giá trị nên tổng hợp theo phút nén số dòng xuống cực nhỏ. Ngược lại, cột **query name** có thể chứa **hàng triệu** tên miền khác nhau nên tỷ lệ nén chỉ dao động **0–60×**. Cardinality không phải thuật ngữ tiếp thị của BI mà là **số lượng giá trị phân biệt của một tập hợp**, quyết định trực tiếp khả năng nén của bảng tổng hợp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/hyperloglog.svg"
       alt="HyperLogLog — ước lượng số phần tử distinct với bộ nhớ cố định"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.9a: Cardinality (số giá trị phân biệt trên một cột) quyết định khả năng nén của phép tổng hợp — `response_code` nén rất gọn, còn `qname` thì không (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Hyperloglog.svg">Wikimedia Commons</a>, CC BY-SA 4.0).</figcaption>
</p>
</figure>

---

## Hơn một triệu truy vấn mỗi giây — chỉ gửi siêu dữ liệu, không gửi toàn bộ gói tin

Số liệu Cloudflare công bố năm 2017 là **hơn 1 triệu truy vấn/giây** trên toàn cầu (và thực tế hiện nay còn cao hơn nhiều). Dù mỗi bản ghi telemetry chỉ khoảng **150 byte** — không lưu toàn bộ thông điệp DNS — khi nhân với lưu lượng đó, tổng dung lượng vẫn lên tới **hàng terabyte mỗi tháng** nếu chuyển toàn bộ về kho dữ liệu mà không qua bước lọc và tổng hợp.

![Cloudflare DNS analytics — blog header](/discrete-mathematics-for-computer-science-iuh/img/course/how-cloudflare-analyzes-1m-dns-queries-per-second.png)

<p class="textbook-figure-caption" data-figure="9.15">Phân tích DNS ở quy mô triệu truy vấn mỗi giây — bài toán đếm và tổng hợp gắn trực tiếp với chi phí hạ tầng (nguồn: [Cloudflare Blog](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/)).</p>

Đường ống dữ liệu của Cloudflare gồm: máy chủ biên (edge server) ghi log bằng **Cap'n Proto** → bộ ghép kênh (multiplexer) → Kafka → kho dữ liệu ClickHouse. Điểm quan trọng không nằm ở tên công cụ mà ở quyết định **chỉ trích xuất siêu dữ liệu tại tầng biên**, thay vì truyền toàn bộ gói DNS, nhằm kiểm soát băng thông ngay từ đầu. Tương tự bài Unicode (không có “văn bản thuần”, chỉ có byte và quy ước), ở đây không có “nhật ký thô vô hạn” mà luôn là **lược đồ telemetry** gắn với lựa chọn có chủ đích về những cột cần giữ lại.

---

## Vì sao tổng hợp theo `qname` không thể mở rộng

Gọi $$R$$ là số dòng nhật ký thô trong một phút. Khi tổng hợp theo chiều $$C$$ có lực lượng $$\vert V_C\vert $$ giá trị phân biệt trong cửa sổ thời gian đó, số dòng sau tổng hợp phụ thuộc trực tiếp vào **$$\vert V_C\vert $$**.

Với **response code**, $$\vert V\vert \approx 12$$. Ngay cả khi có 1 triệu truy vấn mỗi phút phân bố qua mọi mã phản hồi, mỗi cửa sổ một phút chỉ sinh tối đa **12 dòng** — tỷ lệ nén lý tưởng đạt khoảng 83.000×. Trong thực tế, các mã phổ biến như `NOERROR` hay `NXDOMAIN` chiếm phần lớn lưu lượng nên bảng tổng hợp còn gọn hơn nữa.

Với **query name**, $$\vert V\vert $$ có thể đạt hàng triệu do lỗi gõ tên miền, tên miền phụ sinh tự động hoặc tấn công random subdomain. Cloudflare ghi nhận tỷ lệ nén chỉ khoảng **0–60×** và rất thiếu ổn định; trong trường hợp xấu nhất khi mọi `query_name` đều khác nhau, 1 triệu dòng thô sau tổng hợp vẫn là **1 triệu dòng** (tỷ lệ nén **1×**, không giảm được dòng nào).

<div class="content-box warning-box textbook-block" markdown="1">
Khi $$\vert V\vert $$ tiến gần $$R$$, gần như mỗi dòng tổng hợp ứng với một khóa riêng biệt nên **không nén được**. Khi kết hợp nhiều chiều có cardinality cao cùng lúc, số ô tổng hợp sẽ **bùng nổ** theo tích.
</div>

Nếu tổng hợp đồng thời theo $$k$$ cột có lực lượng lần lượt là $$c_1, \ldots, c_k$$ trong cùng một cửa sổ thời gian, số dòng sau tổng hợp bị chặn trên bởi:

<div class="textbook-equation" markdown="1">
$$R' \leq \min\left(R,\; \prod_{i=1}^{k} c_i'\right)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Ví dụ, kết hợp `zone` (10.000 giá trị) × `qname` (1 triệu giá trị phân biệt mỗi giờ) tạo ra cận trên lý thuyết lên tới **10 tỷ** ô; dù dữ liệu thực tế thưa hơn nhiều, bảng tổng hợp vẫn phình to nhanh chóng và đẩy chi phí lưu trữ lẫn truy vấn lên cao. Khoa từng gặp đúng tình huống này khi materialized view theo `zone + qname + minute` tốn dung lượng lớn hơn cả tập nhật ký thô đã lấy mẫu, vì mỗi ô tổng hợp đều phải lưu khóa tên miền đầy đủ.

---

## Sự cố thực tế — bảng tổng hợp tiết kiệm chi phí, nhật ký chi tiết tìm nguyên nhân gốc

Cloudflare từng ghi nhận một sự cố tăng độ trễ tại một trung tâm dữ liệu. Trên bảng điều khiển **tổng hợp** ở cấp zone, nhóm vận hành chỉ thấy tín hiệu mờ nhạt rằng “zone X chậm hơn trung bình”. Chỉ khi kiểm tra nhật ký **chưa tổng hợp**, họ mới phát hiện một **tập con `query_name`** cụ thể bị chậm bất thường và truy ra một **quy tắc tường lửa** áp dụng sai mẫu tên miền.

Khoa gặp tình huống tương tự ở quy mô nhỏ hơn: materialized view theo `zone + response_code` hoạt động tốt cho bảng theo dõi SLA hằng ngày, nhưng để truy tìm nguyên nhân sự cố, hệ thống vẫn cần nhật ký lấy mẫu giữ lại chiều **`qname`** vì độ trễ chỉ tăng đột biến ở một vài tên miền cụ thể.

Bài học Khoa ghi lại trong báo cáo sau sự cố: dữ liệu tổng hợp giúp tiết kiệm dung lượng và theo dõi xu hướng (trả lời “có bất thường không?”), còn dữ liệu thô hoặc lấy mẫu giúp tìm nguyên nhân gốc (trả lời “**chính xác cái gì** đang bất thường?”). Không có một lược đồ duy nhất đáp ứng tối ưu cho cả hai mục đích.

---

## HyperLogLog — đếm số giá trị phân biệt mà không lưu từng khóa

Một câu hỏi phân tích rất phổ biến là: “Có bao nhiêu **tên miền truy vấn khác nhau** trong 1 giờ qua?” Chạy trực tiếp `COUNT(DISTINCT qname)` trên hàng terabyte nhật ký rất chậm và ngốn RAM vì hệ quản trị phải lưu tập khóa hoặc sắp xếp toàn bộ dữ liệu.

**HyperLogLog (HLL)** giải quyết bài toán này bằng cách ước lượng **cardinality** với sai số khoảng 1–2%, trong khi mỗi trạng thái hàng (row state) sau khi nén chỉ tốn khoảng **20–100 byte** thay vì lưu danh sách khóa đầy đủ. Dù tốn hơn bộ đếm tổng đơn giản (chỉ khoảng 8 byte, hoặc ~1 byte sau nén), kích thước bản phác thảo (sketch) của HLL là **cố định** theo mức sai số yêu cầu và không tăng tuyến tính theo số phần tử phân biệt thực tế.

Một ưu điểm quan trọng khác là có thể **gộp** (merge) các trạng thái HLL từ mức phút → giờ → ngày thông qua materialized view trong ClickHouse — tương tự phép hợp tập hợp ở Chương 4 nhưng ở dạng xấp xỉ, đánh đổi một sai số rất nhỏ để giữ bộ nhớ cố định.

![HyperLogLog concept — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/hyperloglog.svg)

<p class="textbook-figure-caption" data-figure="9.16">HyperLogLog — ước lượng số phần tử phân biệt với dung lượng bộ nhớ cố định (nguồn: Wikimedia Commons).</p>

Nhờ cơ chế hợp nhất phân đoạn ngay khi chèn dữ liệu của ClickHouse (tự động cập nhật bảng tổng hợp gồm bộ đếm, ước lượng duy nhất và phân vị), Cloudflare thậm chí **bỏ hẳn lớp xử lý luồng (stream processor)** riêng cho API xu hướng. Với kỹ sư ứng dụng như Khoa, điều quan trọng nhất là biết **khi nào** nên chọn HLL: khi cần trả lời “có bao nhiêu giá trị duy nhất?” trên cột cardinality cao mà không cần liệt kê từng khóa cụ thể.

Quyết định quan trọng thứ hai là chọn **khóa chính (primary key)**. Sắp xếp dữ liệu theo `zone` trước rồi đến `timestamp` giúp truy vấn một zone đọc liên tục trên đĩa, rất nhanh cho bảng điều khiển của từng khách hàng; nhưng truy vấn tổng hợp trên toàn bộ các zone lại phải quét diện rộng, đòi hỏi bảng tổng hợp sẵn hoặc dữ liệu lấy mẫu. Chọn khóa chính nghĩa là chọn **một** thứ tự sắp xếp duy nhất — không thể tối ưu đồng thời cho mọi kiểu truy vấn.

---

## Kết thúc sự cố

Khoa sửa lại quy tắc tường lửa và độ trễ trở lại mức bình thường. Sau buổi tổng kết, nhóm bổ sung luồng lưu nhật ký lấy mẫu 1% có giữ trường `qname` để phục vụ gỡ lỗi — chi phí lưu trữ hoàn toàn nằm trong tầm kiểm soát so với việc duy trì bảng tổng hợp `zone × qname` khổng lồ.

Tóm lại, cardinality quyết định liệu phép tổng hợp có nén được dữ liệu hay không: cột cardinality thấp (`response_code`) phù hợp cho bảng điều khiển chi phí thấp; cột cardinality cao (`qname`) cần HyperLogLog, lấy mẫu hoặc giữ ở luồng tra cứu riêng. Cả hai lớp dữ liệu tổng hợp và lấy mẫu đều cần thiết cho hai mục tiêu khác nhau: theo dõi xu hướng và tìm nguyên nhân gốc.

**Đọc thêm**: [Cloudflare — 1M DNS queries/sec](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/) · [HyperLogLog — Wikipedia](https://en.wikipedia.org/wiki/HyperLogLog)

---

## Bài tập thực hành

### Bài tập 1

Trong một phút có **900.000** dòng nhật ký DNS thô. Nếu tổng hợp theo `response_code` với $$\vert V\vert = 12$$ giá trị phân biệt phân bố đều, ước lượng số dòng sau tổng hợp và tỷ lệ nén (reduction factor) so với dữ liệu thô.

<details>
<summary>Đáp án</summary>

Với 12 mã phản hồi phân bố đều, mỗi cửa sổ một phút cho ra tối đa **12 dòng** (mỗi mã một dòng).

Tỷ lệ nén:

<div class="textbook-equation" markdown="1">
$$\frac{900{,}000}{12} = 75{,}000$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tỷ lệ nén lý tưởng đạt **75.000×**. Trong thực tế, nếu một vài mã chiếm phần lớn lưu lượng thì số dòng còn có thể ít hơn nữa — đây là đặc trưng của phép tổng hợp theo chiều cardinality thấp cho bảng SLA.

</details>

### Bài tập 2

Với cùng **900.000** dòng/phút, giả sử mọi `query_name` đều khác nhau (trường hợp xấu nhất khi bị tấn công tên miền phụ ngẫu nhiên). Tổng hợp theo `query_name` và `minute` tạo ra bao nhiêu dòng và tỷ lệ nén bằng bao nhiêu?

<details>
<summary>Đáp án</summary>

Vì mọi `query_name` đều phân biệt, bảng sau tổng hợp vẫn có đúng **900.000 dòng/phút** (mỗi khóa một dòng).

Tỷ lệ nén:

<div class="textbook-equation" markdown="1">
$$\frac{900{,}000}{900{,}000} = 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tỷ lệ nén bằng **1×** — không giảm được dòng nào. Điều này lý giải vì sao Cloudflare chỉ đạt tỷ lệ nén 0–60× cho `qname`, kém xa so với `response_code`.

</details>

### Bài tập 3

Một materialized view tổng hợp theo `zone` ($$c_1 = 5{,}000$$) × `query_name` ($$c_2 = 200{,}000$$ giá trị phân biệt mỗi giờ) × `response_code` ($$c_3 = 12$$). Tính tích cận trên $$\prod c_i$$ và giải thích vì sao chi phí lưu trữ vẫn có thể phình to dù nhật ký thô trong giờ chỉ có 50 triệu dòng.

<details>
<summary>Đáp án</summary>

Cận trên lý thuyết của tích các chiều:

<div class="textbook-equation" markdown="1">
$$5{,}000 \times 200{,}000 \times 12 = 12 \times 10^{9}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tức tối đa **12 tỷ** tổ hợp khóa — lớn hơn rất nhiều so với 50 triệu dòng dữ liệu thô. Theo công thức $$R' \leq \min\left(R, \prod c_i'\right)$$, số dòng thực tế sẽ bị chặn bởi 50 triệu dòng thô (và nhỏ hơn nữa do độ thưa), nhưng gần như không nén được so với dữ liệu gốc, khiến dung lượng lưu trữ và chi phí hợp nhất bảng tăng mạnh. Chỉ cần đưa một chiều cardinality cao như `query_name` vào phép nhân nhiều chiều là đủ làm mất hiệu quả nén.

</details>

### Bài tập 4

Bảng điều khiển cấp zone báo độ trễ bình thường, nhưng nhật ký lấy mẫu 1% có giữ trường `qname` lại phát hiện 0,3% lưu lượng gửi tới mẫu `*.bad-sub.example.com` chậm gấp 10 lần. Giải thích vì sao bảng tổng hợp cấp zone che khuất tín hiệu này và đề xuất kiến trúc hai lớp dữ liệu.

<details>
<summary>Đáp án</summary>

Bảng tổng hợp cấp zone tính trung bình hoặc phân vị trên toàn bộ lưu lượng của zone, nên 0,3% yêu cầu chậm bị **làm loãng** bởi 99,7% yêu cầu nhanh còn lại. Đây là giới hạn tự nhiên khi tổng hợp theo chiều cardinality thấp trong khi sự cố nằm ở chiều cardinality cao (`qname`).

Kiến trúc hai lớp hợp lý gồm: (1) lớp **tổng hợp sẵn** theo `zone + response_code` (có thể kết hợp HLL cho số `qname` duy nhất) để theo dõi xu hướng và SLA với chi phí thấp; (2) lớp **nhật ký thô lấy mẫu** có giữ `qname` để truy vết nguyên nhân gốc khi xảy ra sự cố — tương tự bài học từ sự cố tường lửa của Cloudflare.

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Cardinality là **số lượng giá trị phân biệt** trên một cột — đại lượng toán rời rạc quyết định trực tiếp khả năng nén của phép tổng hợp nhật ký. Ở quy mô hơn 1 triệu truy vấn DNS mỗi giây của Cloudflare, ngay cả khi mỗi bản ghi chỉ chứa ~150 byte siêu dữ liệu, tổng dung lượng vẫn lên tới hàng terabyte mỗi tháng nếu không thiết kế lược đồ tổng hợp hợp lý.

Cột **cardinality thấp** (`response_code`, ~12 giá trị) cho tỷ lệ nén rất cao và chi phí bảng điều khiển thấp. Cột **cardinality cao** (`query_name`, hàng triệu giá trị) chỉ nén được 0–60× (xấu nhất là 1×), và khi kết hợp nhiều chiều sẽ bùng nổ theo tích $$\prod c_i$$. **HyperLogLog** cho phép ước lượng số phần tử phân biệt với bộ nhớ cố định và sai số khoảng 1–2%, thay thế cho `COUNT(DISTINCT)` tốn kém. Cuối cùng, dữ liệu tổng hợp và dữ liệu lấy mẫu bổ sung cho nhau: tổng hợp phục vụ theo dõi xu hướng, còn lấy mẫu phục vụ tìm nguyên nhân gốc.

Bài tiếp theo (`09_10`) là **case study tổng hợp về hệ thống đăng nhập của TaskFlow**, nơi các bài toán định cỡ connection pool, kiểm thử pairwise, nghịch lý sinh nhật, encoding và cardinality cùng xuất hiện trong một sự cố thực tế.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=eV1haPUt0NU">Hyperloglog: Facebook&#x27;s algorithm to count distinct elements</a> — Gaurav Sen, tiếng Anh. Giải thích nguyên lý HyperLogLog ước lượng số phần tử phân biệt mà không cần lưu từng khóa.
- <a href="https://www.youtube.com/watch?v=tOsb-tFoPCg">Hyperloglog and Cardinality Estimation</a> — Arpit Bhayani, tiếng Anh. Trình bày bài toán ước lượng lực lượng trên luồng dữ liệu, gắn trực tiếp với hệ thống phân tích.
- <a href="https://www.youtube.com/watch?v=B_PexYrEcEw">HyperLogLog Hit Counter - Computerphile</a> — Computerphile, tiếng Anh. Bản giới thiệu ngắn gọn về HyperLogLog trước khi đọc tình huống DNS của Cloudflare.
