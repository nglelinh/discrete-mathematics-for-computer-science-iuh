---
layout: post
title: "Case study: Thiết kế đăng nhập scale với toán rời rạc"
categories: chapter09
date: 2021-01-01
order: 10
required: false
lang: en
excerpt: "Tổng hợp Chương 9 qua tình huống sự cố đăng nhập trên hệ thống TaskFlow (~1 triệu DAU), kết nối định cỡ connection pool, kiểm thử pairwise, nghịch lý sinh nhật, UTF-8 và cardinality."
---

Trong các môn học lý thuyết, từng khái niệm toán rời rạc thường đứng gọn gàng ở từng chương riêng biệt. Nhưng khi một hệ thống thật chạm mốc 1 triệu người dùng mỗi ngày (DAU), năm khái niệm tưởng chừng chẳng liên quan — lý thuyết hàng đợi, quy tắc nhân, nghịch lý sinh nhật, mã hóa ký tự và lực lượng tập hợp — có thể **cùng lúc vỡ trận tại duy nhất một endpoint `/login`**.

**Mạch bài học:** Chẩn đoán đồng thời **5 sự cố thực chiến** trên hệ thống đăng nhập TaskFlow $$\longrightarrow$$ truy vết từng sự cố về đúng công cụ toán rời rạc gốc $$\longrightarrow$$ hợp nhất thành bản thiết kế kiến trúc chịu tải bền vững.

## Bản đồ kiến thức nền: Năm trụ cột toán rời rạc hội tụ trong một luồng đăng nhập

- **Hàng đợi & Tổ hợp cấu hình (Queueing & Combinatorics):** Định luật Little ($$L = \lambda W$$) định cỡ pool kết nối DB thay vì đoán theo DAU; còn kiểm thử Pairwise cắt bùng nổ tổ hợp $$N = \prod v_i$$ của ma trận trình duyệt–OS–ngôn ngữ–OAuth xuống tập ca kiểm thử chạy kịp trong CI/CD.
- **Xác suất va chạm & Mã hóa nhị phân (Birthday Bound & Encoding):** Ngưỡng va chạm $$\approx 1{,}177\sqrt{D}$$ bác bỏ việc dùng `INT32` cho `session_id` (buộc dùng 128-bit/UUID v4); còn chuẩn mã hóa **UTF-8 đồng nhất end-to-end** chặn đứng lỗi `????` khi chuỗi đa ngôn ngữ đi qua nhiều tầng ứng dụng–CSDL.
- **Lực lượng tập hợp trong giám sát (Cardinality Control):** Kiểm soát $$\vert V_C \vert$$ trên nhãn metric Prometheus (tránh gắn `user_id` hay `session_id` làm label) để giữ bộ nhớ chuỗi thời gian ở mức $$O(1)$$ thay vì tăng tuyến tính theo số người dùng.

Mục này **tổng hợp** toàn bộ Chương 9 qua một tình huống thực tế: buổi sáng hệ thống đăng nhập của **TaskFlow** (ứng dụng quản lý công việc khoảng 1 triệu DAU) gặp đồng thời năm sự cố. Mỗi sự cố tương ứng với một bài học trước đó: định cỡ connection pool (Little's Law), kiểm thử tổ hợp (pairwise), nghịch lý sinh nhật (session ID), Unicode/encoding (email tiếng Nhật) và cardinality (metric Prometheus). Bài viết không bổ sung công thức mới mà cho thấy các mảnh toán rời rạc cùng hội tụ tại một điểm vào hệ thống thực tế như thế nào.

Ngay khi **TaskFlow** chạm mốc 1 triệu DAU, kênh `#incidents` liên tục báo lỗi: đăng nhập timeout, email hiển thị `????`, lỗi OAuth trên Safari và Prometheus tràn bộ nhớ (OOM).

Minh, kỹ sư backend có hai năm kinh nghiệm, mở máy và thấy bốn tin nhắn đến gần như cùng lúc:

> **SRE:** Đăng nhập timeout trên toàn region. Chỉ số `active_connections` của PostgreSQL đã chạm trần 200.
>
> **Support (tiếng Nhật):** メールが文字化けしています — email xác nhận hiển thị toàn dấu `????`.
>
> **QA:** Có lỗi OAuth trên production, dù trước đó đã kiểm thử trên Chrome Windows.
>
> **SRE (lần 2):** Prometheus vừa OOM. Có ai gắn nhãn `user_id` vào metric đăng nhập không?

Đây không phải một lỗi đơn lẻ mà là nhiều sự cố độc lập cùng bộc lộ dưới tải lớn — và tất cả đều có thể phòng tránh nếu ngay từ tuần trước nhóm chịu ngồi xuống **đếm có hệ thống** thay vì xem phần “API đăng nhập và phiên” là chi tiết phụ.

Các bài học từ đầu chương — Joel Spolsky và email tiếng Nhật, endianness, Year 2038, máy tính 8-bit của Ben Eater, HikariCP, kiểm thử tổ hợp, nghịch lý sinh nhật, công thức Matt Might và DNS của Cloudflare — mỗi bài là một mảnh ghép. Tình huống dưới đây nối toàn bộ các mảnh ghép đó vào cùng một cổng đăng nhập.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/OSI_Model_v1.svg"
       alt="Mô hình OSI 7 tầng — mỗi request đăng nhập đi qua nhiều lớp xử lý"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.10a: Một yêu cầu đăng nhập đi qua nhiều tầng hệ thống — năm sự cố tương ứng với năm bài học trước cùng bộc lộ trong một buổi sáng tại TaskFlow (nguồn: <a href="https://commons.wikimedia.org/wiki/File:OSI_Model_v1.svg">Wikimedia Commons</a>, CC BY-SA 4.0).</figcaption>
</p>
</figure>

---

## TaskFlow và lý do luồng đăng nhập dễ phát sinh sự cố

TaskFlow phục vụ các nhóm nhỏ và doanh nghiệp với bảng Kanban, bình luận và tệp đính kèm. Hệ thống hỗ trợ đăng nhập bằng email/mật khẩu lẫn OAuth (Google, Microsoft). Người dùng Việt nhập tên có dấu, người dùng Nhật nhận email chào mừng bằng chữ Kanji, và ứng dụng chạy trên trình duyệt máy tính, trình duyệt di động lẫn WebView.

Bề ngoài, luồng đăng nhập chỉ gồm sáu bước: client gửi `POST /api/v1/auth/login`, máy chủ tra cứu tài khoản, kiểm tra mật khẩu bằng bcrypt, tạo phiên (session), ghi nhật ký kiểm toán (audit) và trả về JWT. Tuy nhiên, mỗi bước đều động chạm đến **chuỗi byte**, **biểu diễn số nguyên**, **tổ hợp môi trường** hoặc **đếm kết nối** — những quyết định thiết kế mang tính nền tảng chứ không chỉ là chi tiết cài đặt.

Kiến trúc tại thời điểm xảy ra sự cố:

```
Browser ──HTTPS JSON──► Load Balancer ──► 6 app server (K8s)
                                              │
                                              └── HikariCP ──► PgBouncer ──► PostgreSQL 8-core
```

![Luồng client–server](/discrete-mathematics-for-computer-science-iuh/img/course/Client-server-model.svg)

<p class="textbook-figure-caption" data-figure="9.17">Luồng đăng nhập nhìn như một mũi tên đơn giản nhưng thực chất là chuỗi nhiều quyết định định lượng.</p>

---

## Sự cố 1: “Một triệu người dùng có cần một triệu kết nối không?”

Lúc 7:52, biểu đồ Grafana chuyển đỏ, độ trễ P99 của đăng nhập vượt quá 8 giây và nhật ký ứng dụng ghi liên tục:

```text
HikariPool-1 - Connection is not available, request timed out after 30000ms
```

Tech lead Tuấn đề xuất: “Tăng pool lên 50 mỗi pod vì lượng người dùng đang cao.”

Minh mở bảng tính năng lực (capacity) đã chuẩn bị từ tuần trước:

- DAU: 1.000.000 (số người dùng trong cả ngày, không phải 1 triệu request/giây).
- Tải đăng nhập lúc cao điểm: khoảng 3.000 request/giây (kịch bản giả định 0,3% DAU cùng đăng nhập trong một khung cao điểm buổi sáng).
- Mỗi lượt đăng nhập thành công thực hiện 4 truy vấn DB (tra cứu người dùng, ghi nhận xác thực, tạo phiên, ghi audit).
- Độ trễ truy vấn trung vị (p50): 8 ms.

Áp dụng **Little's Law** từ bài HikariCP:

<div class="textbook-equation" markdown="1">
$$L = \lambda \times W$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Đại lượng cần tính không phải số người đang trực tuyến mà là **số truy vấn đang thực thi đồng thời trên DB**:

<div class="textbook-equation" markdown="1">
$$\lambda = 3000 \times 4 = 12{,}000 \text{ query/giây}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$W = 0{,}008 \text{ giây}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$L = 12{,}000 \times 0{,}008 = 96$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trên toàn cụm chỉ có trung bình **96 kết nối đang bận** — không phải hàng trăm nghìn hay một triệu. Những người đã đăng nhập từ trước đang thao tác kéo thả thẻ Kanban bằng cookie hiện có và không giữ kết nối PostgreSQL.

Chia đều cho 6 máy chủ ứng dụng, mỗi instance cần khoảng **16** kết nối bận; cộng thêm khoản đệm cho đỉnh tải ngắn, cấu hình pool **20–25/pod** là đủ (tổng phía client tối đa ~150).

Nguyên nhân gây timeout là tuần trước nhóm đặt `maximumPoolSize=50` cho **mỗi** pod “cho chắc”, đẩy hàng trăm tiến trình backend xuống máy chủ PostgreSQL chỉ có **8 lõi CPU + 1 SSD**. Theo công thức tham chiếu của HikariCP, số kết nối backend tối ưu trên máy chủ này chỉ quanh mức:

<div class="textbook-equation" markdown="1">
$$2 \times 8 + 1 = 17 \text{ kết nối thật}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Pool quá lớn khiến CPU tiêu tốn thời gian chuyển ngữ cảnh (context switch), tranh chấp khóa trên `shared_buffers` và nghẽn checkpoint — càng nhiều kết nối, DB càng chậm.

Minh đề xuất phương án xử lý trong kênh sự cố và cập nhật vào tài liệu thiết kế:

- Đặt HikariCP ở mức **25 kết nối/pod** theo tính toán Little's Law thay vì 50.
- Cấu hình **PgBouncer** ở chế độ `transaction mode` với `default_pool_size=20` để ghép ~150 kết nối từ ứng dụng xuống khoảng 20 tiến trình backend trên PostgreSQL, sát ngưỡng 17.
- Khi xảy ra timeout, ưu tiên đo và tối ưu truy vấn chậm thay vì tăng pool.

<div class="content-box insight-box textbook-block" markdown="1">
Các sự cố “10.000” hay “1 triệu người dùng” thường xuất phát từ việc nhầm lẫn giữa **DAU**, **người dùng đồng thời** và **RPS**. Chỉ tích $$\lambda \times W$$ mới xác định đúng kích thước pool cần thiết.
</div>

---

## Sự cố 2: Safari, tiếng Việt, OAuth — và 144 cấu hình kiểm thử

Trong lúc DB đang hồi phục, QA Hương báo lỗi OAuth chỉ xảy ra trên **Safari ở iPhone, ngôn ngữ `vi`, đăng nhập bằng Google**, trong khi kiểm thử trên Chrome Windows đều vượt qua.

Product Owner thắc mắc vì sao không kiểm thử toàn bộ mọi tổ hợp. Hương đưa ra bảng tính tổ hợp: 4 trình duyệt × 3 hệ điều hành × 3 thiết bị × 2 ngôn ngữ × 2 phương thức đăng nhập:

<div class="textbook-equation" markdown="1">
$$4 \times 3 \times 3 \times 2 \times 2 = 144 \text{ cấu hình}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Mỗi cấu hình cần 10 bước kiểm tra (biểu mẫu, `redirect_uri`, cookie `SameSite`, thông báo lỗi…):

<div class="textbook-equation" markdown="1">
$$144 \times 10 = 1{,}440 \text{ bước}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nếu thêm trạng thái “tài khoản đã tồn tại / đăng nhập OAuth lần đầu”, khối lượng còn tăng gấp đôi hoặc gấp bốn, vượt xa khả năng chạy thủ công trong một sprint hai tuần. Đây chính là **bùng nổ tổ hợp (combinatorial explosion)** đã phân tích theo testRigor và Optivem Journal.

Cách tiếp cận tiêu chuẩn là **kiểm thử pairwise**: thay vì vét cạn 144 bộ năm tham số, chỉ cần đảm bảo mọi **cặp** giá trị giữa hai tham số bất kỳ đều xuất hiện ít nhất một lần. Công cụ như PICT hoặc Hexawise thường rút gọn còn khoảng **12–18** ca kiểm thử.

Khi Hương chạy PICT trên mô hình này, dòng thứ ba cho ra:

| TC | Browser | OS | Device | Locale | Method |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | Safari | iOS | Mobile | vi | OAuth |

Chỉ cần chạy bộ pairwise này trước khi phát hành, tương tác giữa `Safari + vi` và `Safari + OAuth` đã được kiểm tra từ sớm. Nhóm thống nhất đặt kiểm thử pairwise tại **điểm vào API** (`POST /login`, `GET /oauth/callback`) — thay vì gắn chặt vào từng lớp như `PasswordValidator` vốn dễ vỡ khi tái cấu trúc — kết hợp thêm một vài ca kiểm thử mục tiêu cho cookie trên Safari.

---

## Sự cố 3: `session_id` 32-bit và ảo giác “4 tỷ giá trị là đủ lớn”

Buổi chiều, trong phiên rà soát bảo mật, thực tập sinh Trung đề xuất sinh `session_id = Random.nextInt()` (số nguyên 32-bit) vì nghĩ 4 tỷ giá trị là quá rộng để trùng lặp.

Minh dẫn lại phân tích từ [tomarcher.io](https://tomarcher.io/posts/birthday-paradox/) về **nghịch lý sinh nhật trong production**: va chạm không đợi đến khi dùng gần hết 4 tỷ giá trị mà phụ thuộc vào số **cặp** so sánh. Ngưỡng xác suất va chạm 50% của không gian 32-bit chỉ nằm ở:

<div class="textbook-equation" markdown="1">
$$n_{0.5} \approx 1{,}177 \sqrt{2^{32}} \approx 77{,}000$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Với TaskFlow (khoảng 2 phiên/người dùng/ngày), chỉ vài chục nghìn người dùng hoạt động là hệ thống đã bước vào vùng rủi ro cao; hai phiên trùng ID có thể khiến người dùng A truy cập nhầm dữ liệu của người dùng B — một lỗ hổng nghiêm trọng.

Minh ghi bảng đối chiếu lên bảng trắng:

| Chiến lược định danh | Ngưỡng ~50% va chạm tại $$n$$ |
|:---|:---:|
| INT32 ngẫu nhiên | ~77.000 |
| INT64 ngẫu nhiên | ~$$5 \times 10^9$$ |
| UUID v4 | ~$$2{,}7 \times 10^{18}$$ |

Nhóm chốt sử dụng **UUID v4** (122 bit ngẫu nhiên), cho phép từng pod sinh định danh độc lập mà không cần dịch vụ điều phối trung tâm.

Khi Trung hỏi thêm về việc băm `user_agent` vào các bucket cho nhật ký kiểm toán, Minh chỉ ra đây là một câu hỏi khác — bài toán **kỳ vọng số lần trùng** của Matt Might: $$E = n - D + D((D-1)/D)^n$$, không phải bài toán đảm bảo tính duy nhất của phiên đăng nhập, nên cần tách thành hai mục riêng trong tài liệu thiết kế.

Đồng thời, trường `expires_at` được lưu bằng **BIGINT** tính theo mili giây thay vì INT32 tính theo giây để tránh sự cố tràn số **Year 2038** vào ngày 19/01/2038.

---

## Sự cố 4: Email tiếng Nhật hiển thị `????` — bài học của Joel từ năm 2003

Phiếu hỗ trợ từ khách hàng Nhật đính kèm ảnh chụp màn hình: tên `田中太郎` trong email chào mừng biến thành `????`.

Kiểm tra mẫu email HTML, Minh thấy nội dung mã nguồn hoàn toàn đúng, nhưng thông điệp gửi qua SMTP lại thiếu tiêu đề `charset=UTF-8`. Ứng dụng email phía người nhận buộc phải đoán bảng mã (như ISO-2022-JP hoặc Latin-1), tái hiện đúng vấn đề mà Joel Spolsky từng mô tả trên FogBUGZ năm 2003: *There Ain't No Such Thing As Plain Text*.

Cách khắc phục đòi hỏi sự nhất quán trên toàn bộ đường ống:

- API: `Content-Type: application/json; charset=utf-8`
- Cơ sở dữ liệu PostgreSQL: encoding `UTF8`
- Email MIME: `Content-Type: text/html; charset=UTF-8`
- Tệp nhật ký (log): ghi UTF-8 thay vì phụ thuộc bảng mã mặc định của máy chủ

Với JWT, payload JSON Unicode được mã hóa thành UTF-8 rồi chuyển sang Base64URL trên đường truyền; tránh đưa dữ liệu nhị phân phụ thuộc thứ tự byte (endianness) vào claim.

```json
{
  "sub": "550e8400-e29b-41d4-a716-446655440000",
  "email": "tanaka@example.jp",
  "name": "田中太郎",
  "exp": 1893456000000
}
```

---

## Sự cố 5: Prometheus OOM vì gắn nhãn có cardinality quá cao

Một bản cập nhật mới gộp tối Chủ nhật đã thêm metric:

```text
login_requests_total{user_id="88421", email="minh@taskflow.vn", status="ok"}
```

Vì mỗi giá trị `user_id` và `email` tạo ra một chuỗi thời gian (time series) riêng, với 1 triệu DAU số series lập tức vọt lên hàng triệu và khiến Prometheus hết bộ nhớ (OOM) vào sáng thứ Hai.

Đây chính là bài học từ hệ thống phân tích DNS của Cloudflare: tổng hợp theo `query_name` (cardinality cao) không thể nén hiệu quả như `response_code` (khoảng 12 giá trị). Đưa `user_id` vào nhãn metric tạo ra hệ quả tương tự.

Nhóm giới hạn nhãn metric ở các chiều có lực lượng nhỏ như `status`, `method`, `region` (vài chục tổ hợp). Khi cần truy vết một người dùng cụ thể, kỹ sư tra cứu **trace ID** trong nhật ký JSON lấy mẫu 1%; còn khi cần đếm số người dùng duy nhất theo giờ, hệ thống dùng tác vụ tổng hợp theo lô (batch) hoặc **HyperLogLog** thay vì Prometheus. Sau khi SRE sửa lại thành `login_requests_total{status, method}`, mức dùng RAM của Prometheus trở lại ổn định.

---

## Tổng kết tài liệu thiết kế sau sự cố

Cuối ngày, Minh tóm lược lại các quyết định định lượng thành tài liệu thiết kế cho toàn nhóm:

**TaskFlow Auth — các chuẩn thiết kế rút ra từ sự cố:**

- **Connection pool:** Cao điểm 3.000 login/giây × 4 truy vấn = 12.000 truy vấn/giây. Theo Little's Law cần ~96 kết nối bận; cấu hình 25 kết nối/pod kết hợp PgBouncer 20 kết nối backend thay vì mở 200 kết nối trực tiếp vào PostgreSQL 8 lõi.
- **Kiểm thử QA:** Không chạy vét cạn 144 cấu hình; dùng ~15 ca kiểm thử pairwise trên API đăng nhập/OAuth cộng thêm 5 ca mục tiêu cho Safari/iOS.
- **Phiên đăng nhập:** Dùng UUID v4 cho `session_id` và `BIGINT` (mili giây) cho `expires_at`; không dùng INT32 ngẫu nhiên (ngưỡng 50% va chạm chỉ ~77.000).
- **Encoding:** Thống nhất UTF-8 xuyên suốt API, cơ sở dữ liệu, tiêu đề MIME email và tệp log.
- **Giám sát (metrics):** Tuyệt đối không đưa `user_id` hay `email` vào nhãn metric; giữ lực lượng nhãn ở mức thấp và có kiểm soát.

Một triệu DAU không đòi hỏi một triệu lời giải phức tạp — nó đòi hỏi không bỏ qua những phép đếm nền tảng: nhân tham số kiểm thử, tính $$\lambda \times W$$, ước lượng $$\sqrt{d}$$ cho không gian định danh, khai báo bảng mã cho từng luồng byte và kiểm soát lực lượng nhãn giám sát.

---

## Ví dụ tính tay cầm tay chỉ việc: Bảng kiểm toán 5 thông số cho TaskFlow (1.000.000 DAU)

Trước khi triển khai bản vá lên production, một kỹ sư trưởng sẽ kiểm tra nhanh bằng 5 phép tính nhẩm trong 2 phút:

1. **Pool DB (Định luật Little):** Giả sử giờ cao điểm có $$\lambda = 400$$ lượt đăng nhập/giây, mỗi lượt chạy truy vấn mất $$W = 10\text{ ms} = 0{,}01\text{s}$$. Số kết nối bận trung bình:
   $$L = 400 \times 0{,}01 = 4\text{ kết nối.}$$
   Với máy chủ DB 8 lõi CPU, pool tổng ~16–20 kết nối (qua PgBouncer) thừa sức gánh tải gấp 4 lần đỉnh mà không gây nghẽn đổi ngữ cảnh.
2. **Ma trận test đăng nhập (Quy tắc nhân vs. Pairwise):** 3 trình duyệt $$\times$$ 3 OS $$\times$$ 4 ngôn ngữ $$\times$$ 2 chế độ OAuth $$\times$$ 2 mạng = $$3 \times 3 \times 4 \times 2 \times 2 = 144$$ cấu hình vét cạn; dùng Pairwise chỉ cần khoảng **16–18 ca** là phủ 100% mọi cặp tương tác (như Safari + OAuth).
3. **Định danh phiên (Nghịch lý Sinh nhật):** Ở mức 200.000 phiên đang hoạt động song song, `INT32` ($$n_{0.5} \approx 77\,136$$) có xác suất va chạm:
   $$P \approx 1 - \exp\!\left(-\frac{200\,000^2}{2 \times 2^{32}}\right) \approx 1 - e^{-4{,}66} \approx 99{,}05\%\text{ (chắc chắn nổ!).}$$
   Chuyển sang UUID v4 (122 bit ngẫu nhiên) giảm xác suất va chạm xuống $$\approx \frac{4\times 10^{10}}{2 \times 5{,}3\times 10^{36}} \approx 3{,}8 \times 10^{-27}$$.
4. **Chuỗi tiếng Nhật UTF-8:** 1 ký tự Kanji như `東` (U+6771) chiếm **3 byte** trong UTF-8 (`E6 9D B1`); nếu cột MySQL dùng `latin1` (1 byte/ký tự) thay vì `utf8mb4`, dữ liệu bị cắt hỏng thành `???`.
5. **Cardinality của Prometheus:** Gắn nhãn `user_id` cho 1 triệu DAU tạo ra $$1\,000\,000$$ time-series riêng lẻ (tốn hàng GB RAM); đổi sang nhãn `auth_method` (3 giá trị) $$\times$$ `status_code` (4 giá trị) chỉ tạo tối đa $$3 \times 4 = 12$$ time-series!

### Khung giải thích: Tư duy kiến trúc hệ thống bằng toán rời rạc (nên đọc chậm)

1. **Bước 1 — Mọi sự cố vận hành đều có "chữ ký toán học":** Độ trễ tăng khi tăng pool là chữ ký của tranh chấp hàng đợi; lỗi lặp khóa bất ngờ là chữ ký của $$\sqrt{D}$$; RAM tăng đều theo lượng người dùng là chữ ký của cardinality không chặn.
2. **Bước 2 — Tính bậc độ lớn trước khi viết code:** Chỉ cần 5 phép tính nháp ($$L=\lambda W$$, $$\prod v_i$$, $$1{,}177\sqrt{D}$$, số byte/ký tự, $$\prod \vert V_i \vert$$) đã loại bỏ được phần lớn lỗi kiến trúc ngay trên giấy.
3. **Bước 3 — Hệ thống bền vững nhờ chặn cận trên:** Mọi tài nguyên hữu hạn (kết nối DB, số ca CI, bộ nhớ metric) phải được chặn bằng các đại lượng có cận trên tường minh thay vì để tăng tự do theo lưu lượng người dùng.

$$\text{TaskFlow Login} = \underbrace{L=\lambda W}_{\text{Pool}} + \underbrace{\text{Pairwise}}_{\text{QA}} + \underbrace{\text{UUIDv4}}_{\sqrt{D}} + \underbrace{\text{UTF-8}}_{\text{Bytes}} + \underbrace{\vert V_C\vert \le 12}_{\text{Metrics}}.$$

## Bài tập thực hành

### Bài tập 1

Hệ thống **FlowBoard** (kiến trúc tương tự TaskFlow) đạt **800.000 DAU**. SRE đo tải đăng nhập cao điểm **2.500 request/s** lúc 8 giờ sáng. Mỗi lượt đăng nhập thành công thực hiện **5 truy vấn** DB với độ trễ p50 là **10 ms**. Hạ tầng gồm **8 pod** ứng dụng và máy chủ PostgreSQL **12 lõi CPU + 2 SSD**, chưa dùng PgBouncer. DevOps đề xuất `maximumPoolSize=60` mỗi pod.

(a) Tính $$L$$ theo Little's Law ở tầng DB. (b) Đề xuất kích thước pool mỗi pod (có khoản đệm nhỏ). (c) Tính tổng số kết nối nếu mỗi pod đặt 60 và so sánh với công thức HikariCP cho máy chủ DB. (d) Giải thích ngắn gọn vì sao con số 800.000 DAU không xuất hiện trong phép tính pool.

<details>
<summary>Đáp án</summary>

(a) Thông lượng truy vấn:

<div class="textbook-equation" markdown="1">
$$\lambda = 2{,}500 \times 5 = 12{,}500 \text{ query/s}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$W = 0{,}010 \text{ s}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$L = 12{,}500 \times 0{,}010 = 125$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trung bình có **125** kết nối đang bận trên toàn cụm.

(b) Chia cho 8 pod: $$125 / 8 \approx 15{,}6$$ kết nối bận/pod. Cộng thêm khoản đệm cho đỉnh tải ngắn, mức **20–25 kết nối/pod** là hợp lý.

(c) Với 8 pod × 60 = **480** kết nối từ ứng dụng. Trong khi đó, công thức HikariCP cho máy chủ DB 12 lõi + 2 SSD là:

<div class="textbook-equation" markdown="1">
$$2 \times 12 + 2 = 26$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Mức **480** vượt gần 20 lần ngưỡng 26, dễ gây tranh chấp CPU và khóa trên DB. Cần giảm pool mỗi pod kết hợp đặt **PgBouncer** phía trước để ghép xuống khoảng 20–26 kết nối backend thật.

(d) **DAU** là tổng số người dùng riêng biệt trong cả ngày; phần lớn người dùng không thực thi truy vấn DB tại cùng một thời điểm. Kích thước pool phụ thuộc vào thông lượng truy vấn lúc cao điểm ($$\lambda$$) và thời gian xử lý truy vấn ($$W$$).

</details>

### Bài tập 2

Nhóm QA của FlowBoard có ma trận kiểm thử đăng nhập gồm: **5** trình duyệt × **4** hệ điều hành × **3** thiết bị × **3** ngôn ngữ × **2** phương thức xác thực; mỗi cấu hình gồm **8** bước kiểm tra API.

(a) Tính tổng số cấu hình vét cạn và tổng số bước kiểm thử thủ công. (b) Nếu mỗi bước tốn 2 phút, một sprint hai tuần (10 ngày làm việc × 6 giờ/ngày) có đủ cho một QA thực hiện không? (c) Giải thích vì sao bộ kiểm thử pairwise (~15 ca) phát hiện được lỗi **Safari + iOS + vi + OAuth** mà kiểm thử chỉ trên Chrome bỏ sót. (d) Đề xuất bộ kiểm thử tối thiểu để phát hành an toàn.

<details>
<summary>Đáp án</summary>

(a) Tổng số cấu hình:

<div class="textbook-equation" markdown="1">
$$5 \times 4 \times 3 \times 3 \times 2 = 360$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tổng số bước:

<div class="textbook-equation" markdown="1">
$$360 \times 8 = 2{,}880 \text{ bước}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

(b) Tổng thời gian:

<div class="textbook-equation" markdown="1">
$$2{,}880 \times 2 = 5{,}760 \text{ phút} = 96 \text{ giờ}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Quỹ thời gian sprint là $$10 \times 6 = 60$$ giờ/người — **không đủ**, chưa tính các kiểm thử hồi quy khác.

(c) Pairwise bảo đảm mọi **cặp** tham số (`Safari + vi`, `Safari + OAuth`, `vi + OAuth`…) đều xuất hiện ít nhất một lần trong bảng khoảng 15 ca kiểm thử, giúp lộ lỗi cookie `SameSite` trên Safari ngôn ngữ Việt — điều mà việc chỉ chạy trên Chrome không thể phủ tới.

(d) Đề xuất: **12–18 ca kiểm thử pairwise** tại điểm vào `POST /login` và `GET /oauth/callback`, cộng **3–5 ca kiểm thử mục tiêu** cho Safari/iOS (cookie, `redirect_uri`) và bộ smoke test trên môi trường staging tương đương production.

</details>

### Bài tập 3

Một thực tập sinh đề xuất bảng phiên đăng nhập của FlowBoard như sau:

```sql
session_id   INT,          -- Random.nextInt()
expires_at   INT,          -- Unix giây
user_agent   VARCHAR(64)   -- hash bucket cho audit
```

Hệ thống dự kiến tạo **120.000 phiên mới mỗi ngày** và duy trì lược đồ này trong **10 năm**.

(a) Ước lượng ngưỡng $$n_{0.5}$$ cho `session_id` kiểu INT32 và so sánh với tốc độ 120.000 phiên/ngày. (b) Vì sao `expires_at` kiểu INT (giây) là rủi ro dài hạn dù hệ thống chạy tốt vào năm 2026? (c) Đề xuất kiểu thay thế cho hai cột số nguyên và phân biệt ngắn gọn bài toán “tính duy nhất của session” với bài toán “kỳ vọng số lần trùng bucket kiểm toán” (Matt Might).

<details>
<summary>Đáp án</summary>

(a) Ngưỡng 50% va chạm của không gian 32-bit là $$n_{0.5} \approx 1{,}177\sqrt{2^{32}} \approx 77{,}000$$. Với tốc độ 120.000 phiên/ngày, nếu các phiên tích lũy trong cùng không gian thì chỉ **chưa tới 1 ngày** đã vượt ngưỡng 77.000; kể cả khi có TTL làm giảm số phiên đồng thời, xác suất va chạm vẫn sớm đạt mức nguy hiểm trong vài ngày đến vài tuần. Cần đổi sang **UUID v4** hoặc **INT64**.

(b) Kiểu INT 32-bit có dấu lưu Unix giây sẽ tràn vào ngày **19/01/2038** (Year 2038), kéo `expires_at` quay về năm 1901 và làm hỏng logic kiểm tra hết hạn phiên. Với vòng đời thiết kế 10 năm tính từ 2026, hệ thống sẽ chạm mốc này trong tương lai gần.

(c) Thay thế: `session_id UUID` và `expires_at BIGINT` (mili giây kể từ epoch). Việc băm `user_agent` vào $$D$$ bucket kiểm toán thuộc bài toán **kỳ vọng số lần trùng** $$E = n - D + D((D-1)/D)^n$$ (trả lời trung bình có bao nhiêu bản ghi rơi vào bucket đã có dữ liệu), hoàn toàn khác với bài toán xác suất trùng định danh phiên $$P(\text{collision})$$.

</details>

### Bài tập 4

Một pull request cuối tuần gộp hai thay đổi: (1) thêm metric `login_requests_total{user_id, email, status}`; (2) gửi email HTML chào mừng không khai báo `charset` và trả JSON không có tiêu đề `charset`. Sáng thứ Hai, Prometheus gặp OOM và khách hàng Nhật báo lỗi tên Kanji hiển thị thành `????`.

(a) Ước lượng quy mô time series trên Prometheus nếu có **500.000 DAU** (mỗi người đăng nhập trung bình 2 lần/ngày) khi gắn `user_id` làm nhãn. (b) So sánh với cấu hình chỉ giữ các nhãn `status`, `method`, `region` (tổng $$\vert V\vert \approx 30$$ tổ hợp). (c) Liệt kê bốn lớp trong đường ống cần thống nhất UTF-8. (d) Viết hai nhận xét ngắn gọn để từ chối cả hai thay đổi trong PR.

<details>
<summary>Đáp án</summary>

(a) Với 500.000 DAU, mỗi người đăng nhập 2 lần/ngày tạo ra:

<div class="textbook-equation" markdown="1">
$$500{,}000 \times 2 = 1{,}000{,}000 \text{ lượt đăng nhập/ngày}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Vì mỗi `user_id` (kèm `email`) sinh một chuỗi thời gian riêng, tổng số time series sẽ lên tới **hàng trăm nghìn đến hàng triệu** (tùy số trạng thái `status` nhân thêm), khiến Prometheus hết RAM.

(b) Giữ tập nhãn cardinality thấp (~30 tổ hợp `status × method × region`) giúp số chuỗi thời gian cố định ở mức vài chục, ổn định bộ nhớ mà vẫn đáp ứng đầy đủ giám sát SLA — tương tự sự khác biệt giữa `response_code` và `query_name` tại Cloudflare.

(c) Bốn lớp cần thống nhất UTF-8: (1) **HTTP API** (`Content-Type: application/json; charset=utf-8`), (2) **PostgreSQL** (`UTF8`), (3) **Email MIME** (`Content-Type: text/html; charset=UTF-8`) và (4) **tệp log** (UTF-8).

(d) Ví dụ nhận xét PR:
- *Metric*: “Nhãn `user_id`/`email` có cardinality ngang với DAU, tạo ra hàng trăm nghìn đến hàng triệu time series và gây OOM cho Prometheus; hãy dùng trace ID trong log JSON để gỡ lỗi và dùng batch/HyperLogLog khi cần đếm người dùng duy nhất.”
- *Encoding*: “Thiếu khai báo `charset` khiến ứng dụng người nhận tự đoán bảng mã và gây lỗi hiển thị Kanji/tiếng Việt; cần khai báo thống nhất UTF-8 ở cả API, DB, MIME email và log.”

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Tình huống sáng thứ Hai tại TaskFlow cho thấy năm bài toán của Chương 9 cùng hội tụ tại một luồng đăng nhập:

- **Sự cố 1 (Connection pool):** Phân biệt DAU, người dùng đồng thời và RPS; Little's Law cho ~96 kết nối bận (pool 25/pod + PgBouncer 20 backend) thay vì mở 200 kết nối thẳng vào PostgreSQL 8 lõi (ngưỡng HikariCP là 17).
- **Sự cố 2 (Kiểm thử tổ hợp):** $$4 \times 3 \times 3 \times 2 \times 2 = 144$$ cấu hình × 10 bước = 1.440 bước vượt quỹ thời gian sprint; kiểm thử pairwise (~15 ca) phủ đủ tương tác cặp như `Safari + vi + OAuth`.
- **Sự cố 3 (Nghịch lý sinh nhật & Y2038):** INT32 ngẫu nhiên chạm ngưỡng 50% va chạm quanh 77.000 phiên; cần chuyển sang UUID v4 và `expires_at` kiểu `BIGINT` (mili giây), đồng thời tách biệt với bài toán kỳ vọng trùng bucket của Matt Might.
- **Sự cố 4 (Encoding):** Thiếu `charset=UTF-8` trong MIME và API gây lỗi hiển thị `????` cho chữ Kanji; cần thống nhất UTF-8 xuyên suốt hệ thống.
- **Sự cố 5 (Cardinality):** Nhãn `user_id` làm bùng nổ hàng triệu time series gây OOM cho Prometheus; chỉ dùng nhãn có lực lượng thấp trên metric.

Sau Chương 9, **Chương 10: Quan hệ truy hồi** sẽ cung cấp công cụ mô hình hóa sự tăng trưởng theo thời gian — giúp dự báo tải hệ thống không chỉ ở một thời điểm hiện tại mà qua nhiều chu kỳ tăng trưởng tiếp theo.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=fYjiS2ogcoE">Little&#x27;s Law Explained | L = λ × W | Queueing Theory &amp; System Design</a> — Industry Ready Coder, tiếng Anh. Ôn lại định luật Little cho sự cố connection pool trong tình huống đăng nhập.
- <a href="https://www.youtube.com/watch?v=MijmeoH9LT4">Characters, Symbols and the Unicode Miracle - Computerphile</a> — Computerphile, tiếng Anh. Nhắc lại Unicode và encoding, gắn với sự cố hiển thị email tiếng Nhật.
- <a href="https://www.youtube.com/watch?v=lKTsv6iVxV4">Binary: Plusses &amp; Minuses (Why We Use Two&#x27;s Complement) - Computerphile</a> — Computerphile, tiếng Anh. Cơ chế bù hai và tràn số nguyên 32-bit liên quan đến trường `expires_at`.
