---
layout: post
title: "Case study: Thiết kế đăng nhập scale với toán rời rạc"
categories: chapter09
date: 2021-01-01
order: 10
required: false
lang: en
---

# Một triệu người dùng, và buổi sáng login sập

Thứ Hai, 7 giờ 45 — đúng giờ cao điểm mà mọi startup mơ ước.

**TaskFlow**, app quản lý việc làm kiểu Trello cho thị trường Việt Nam và Nhật, vừa được báo đăng vì chạm **một triệu DAU**. Trên banner trang chủ, confetti digital bay lung tung. Trong Slack channel `#incidents`, màu đỏ cũng bay lung tung — nhưng không ai muốn.

Minh, backend engineer hai năm kinh nghiệm, vừa mở laptop thì thấy bốn tin nhắn chồng lên nhau:

> **SRE:** Login timeout toàn region. Postgres `active_connections` chạm trần 200.
>
> **Support (tiếng Nhật):** メールが文字化けしています — email xác nhận toàn dấu `????`.
>
> **QA:** Production bug OAuth. Em test Chrome Windows rồi mà?
>
> **SRE (lần 2):** Prometheus OOM. Ai gắn `user_id` vào metric login thế?

Minh thở dài. Không phải một bug. Bốn bug. Và cả bốn đều có thể đã được **tránh** nếu tuần trước họ ngồi xuống đếm — thật sự đếm — thay vì viết “API login + session” rồi ship.

Chương 9 của khóa học này đã dạy từng mảnh: Joel và email Nhật, endianness, Y2038, Ben Eater và bit trên silicon, HikariCP, combinatorial testing, birthday paradox, Matt Might, Cloudflare DNS. Bài cuối không thêm công thức lạ. Bài cuối kể **một ngày** mà tất cả các mảnh đó cùng đổ vào một cửa — cửa đăng nhập.

---

## TaskFlow là gì, và vì sao login là nơi nguy hiểm nhất

TaskFlow bán cho team nhỏ và doanh nghiệp: board Kanban, comment, file đính kèm. Đăng nhập hỗ trợ email/mật khẩu và OAuth (Google, Microsoft). User Việt gõ tên có dấu; user Nhật nhận email chào mừng bằng kanji. Có web, mobile web, và app bọc WebView.

Luồng đăng nhập nghe đơn giản: client gửi `POST /api/v1/auth/login`, server tra user, verify bcrypt, tạo session, ghi audit, trả JWT. Sáu bước. Nhưng mỗi bước chạm **chuỗi byte**, **số nguyên**, **tổ hợp môi trường**, hoặc **đếm connection** — và Minh tuần trước coi đó là “chi tiết implementation”, không phải “thiết kế”.

Kiến trúc lúc incident:

```
Browser ──HTTPS JSON──► Load Balancer ──► 6 app server (K8s)
                                              │
                                              └── HikariCP ──► PgBouncer ──► PostgreSQL 8-core
```

![Luồng client–server](/discrete-mathematics-for-computer-science-iuh/img/course/Client-server-model.svg)

*Hình 9.17: Đăng nhập trông như một mũi tên; thực ra là chuỗi quyết định đếm.*

---

## Incident 1: “Một triệu user thì cần một triệu connection chứ?”

Grafana nhảy đỏ lúc 7:52. P99 login vượt 8 giây. Log app:

```text
HikariPool-1 - Connection is not available, request timed out after 30000ms
```

Tech lead Tuấn nhắn: “Tăng pool lên 50 mỗi pod đi, user đông mà.”

Minh mở spreadsheet capacity — may mắn là tuần trước anh đã lười chưa xóa. Trên đó ghi:

- DAU: 1.000.000 — milestone PR, không phải 1M request/s.
- Peak login: ~3.000 request/s — giả định 0,3% DAU cùng đăng nhập trong một phút buổi sáng (cực đoan, nhưng đúng kiểu incident review).
- Mỗi login thành công: 4 query DB (lookup user, side-effect verify, insert session, audit).
- Latency query p50: 8 ms.

Anh nhớ bài HikariCP và **Little's Law** — công thức hàng đợi mà nghe phí thời gian học, giờ cứu mạng:

$$L = \lambda \times W$$

Không phải “bao nhiêu user online”, mà **bao nhiêu query đang chạy trên DB**:

$$\lambda = 3000 \times 4 = 12{,}000 \text{ query/giây}$$

$$W = 0{,}008 \text{ giây}$$

$$L = 12{,}000 \times 0{,}008 = 96$$

Ninety-six. Chỉ **96 connection busy trung bình** trên cả cluster — không phải 96 người, chắc chắn không phải một triệu. User đã login từ sáng sớm đang kéo card Kanban bằng cookie cũ; họ không giữ connection PostgreSQL.

Chia cho 6 app server: mỗi instance cần khoảng **16** connection busy, cộng buffer cho spike → pool **20–25** là đủ. Tổng client tối đa ~150.

Vậy tại sao timeout?

Vì tuần trước họ set `maximumPoolSize=50` trên **mỗi** pod “cho chắc”, và Postgres nhận **hàng trăm backend process** trong khi máy DB chỉ **8 core + 1 SSD**. Wiki HikariCP (và thực nghiệm PostgreSQL) gợi ý throughput tối đa quanh:

$$2 \times 8 + 1 = 17 \text{ connection thật}$$

Pool **quá lớn** không làm DB nhanh hơn — nó làm CPU đánh nhau context switch, lock `shared_buffers`, checkpoint giẫm lên nhau. Nhiều connection **chậm hơn** ít connection. Đó là điều trái trực giác mà chỉ đếm mới thấy.

Giải pháp Minh đề xuất trong thread incident (và sau đó ghi design doc):

- HikariCP **25/pod** — đủ theo Little's Law, không phải 50.
- **PgBouncer** transaction mode, `default_pool_size=20` — 150 client app ghép xuống ~20 backend Postgres, sát công thức 17.
- Khi timeout: **đừng** tăng pool — profile slow query trước.

Tuấn im một lúc, rồi reply: “Ừ. DAU không bằng connection. Anh nhầm cả đời.”

<div class="content-box insight-box" markdown="1">
**Điểm Chương 9:** Incident “10k user” thường là nhầm **DAU**, **concurrent user**, hay **RPS**. Chỉ $$ \lambda \times W $$ mới trả lời pool.
</div>

---

## Incident 2: Safari, tiếng Việt, OAuth — và 144 cách để sai

Trong lúc DB hồi phục, QA Hương ping: bug chỉ lên **Safari trên iPhone, locale vi, đăng nhập Google**. Chrome Windows pass hết.

Product owner: “Sao không test hết combination?”

Hương không giận — cô đưa spreadsheet. Browser 4 × OS 3 × device 3 × locale 2 × auth method 2:

$$4 \times 3 \times 3 \times 2 \times 2 = 144 \text{ cấu hình}$$

Mỗi cấu hình 10 bước kiểm tra (form, redirect URI, cookie `SameSite`, thông báo lỗi…):

$$144 \times 10 = 1{,}440 \text{ bước}$$

Thêm trạng thái “đã có account / lần đầu OAuth” — nhân đôi hoặc nhân tư. Sprint hai tuần không có 1.440 bước manual. Đây là **combinatorial explosion** mà testRigor và Optivem Journal mô tả: không phải QA lười, là **không gian tổ hợp** lớn hơn thời gian con người.

Cách industry làm: **pairwise testing**. Không cần chạy cả 144 bộ năm tham số cùng lúc — chỉ cần mọi **cặp** tham số (browser–OS, browser–locale, …) xuất hiện ít nhất một lần. PICT hoặc Hexawise thường sinh **12–18** test.

Hương chạy PICT, dán kết quả vào thread. Dòng thứ ba:

| TC | Browser | OS | Device | Locale | Method |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | Safari | iOS | Mobile | vi | OAuth |

“Đây,” cô nói. “Nếu chạy bảng này tuần trước, bug không lên production. Chrome-only không cover cặp Safari + vi.”

Minh gật. Test **entry point** API `POST /login` và `GET /oauth/callback` — hành vi hệ thống — không test từng class `PasswordValidator` riêng lẻ (Optivem: test class = fragile khi refactor). Pairwise trên API + vài test **targeted** Safari cookie — đủ cho ship, không đủ cho math olympiad.

---

## Incident 3: Intern và bốn tỷ số “đủ lớn rồi”

Security review lúc chiều. Intern Trung trình bày slide đẹp: `session_id = Random.nextInt()` — INT32, “có 4 tỷ giá trị, chắc không trùng.”

Minh nhớ bài [tomarcher.io](https://tomarcher.io/posts/birthday-paradox/) — **birthday paradox trong production**. Bạn không cần lấp đầy 4 tỷ ô mới trùng. Bạn chỉ cần đủ **cặp** so sánh. Ngưỡng 50% collision với INT32:

$$n_{0.5} \approx 1{,}177 \sqrt{2^{32}} \approx 77{,}000$$

Bảy mươi bảy nghìn session — không phải bốn tỷ. TaskFlow ~2 session/user/ngày → vài chục nghìn user là vào vùng rủi ro. Hai session trùng ID → user A có thể thấy board user B. Critical.

Trên whiteboard Minh viết:

| Chiến lược | ~50% collision tại |
|:---|:---:|
| INT32 random | ~77.000 |
| INT64 random | ~5 × 10⁹ |
| UUID v4 | ~2.7 × 10¹⁸ |

“Chúng ta dùng UUID v4,” anh nói. “122 bit random, sinh được trên mỗi pod không cần coordinator.”

Trung hỏi: “Còn audit log hash user-agent trùng bucket thì sao?”

Khác câu hỏi — đó là **kỳ vọng số match** của Matt Might: $$E = n - D + D((D-1)/D)^n$$, không phải uniqueness session. Design doc cần hai dòng riêng, không gộp chung cho nghe pro.

`expires_at` ghi **BIGINT** milliseconds — Planet Mainframe và Y2038 đã dạy: INT32 giây +1 vào 2038-01-19 nhảy về 1901. Session schema sống lâu hơn intern.

---

## Incident 4: メール — Joel đã cảnh báo từ 2003

Ticket support Nhật gắn screenshot: `????` thay vì `田中太郎`.

Minh mở template email welcome. HTML đẹp. Nhưng SMTP gửi **byte** không header `charset=UTF-8`. Client Nhật đoán ISO-2022-JP hoặc Latin-1 — Joel Spolsky gọi đây là thế giới không có **plain text**: *There Ain't No Such Thing As Plain Text.*

FogBUGZ năm 2003 cùng bệnh: email tiếng Nhật, thư viện MIME decode sai, phải undo/redo conversion. Hai mươi năm sau, TaskFlow tái hiện.

Fix không khó về code — khó về **thói quen**:

- API: `Content-Type: application/json; charset=utf-8`
- DB PostgreSQL: encoding UTF8
- Email: `Content-Type: text/html; charset=UTF-8`
- Log file: UTF-8, không mặc định Latin-1 trên server

JWT payload JSON Unicode → Base64URL trên wire. Không nhét binary endian-sensitive vào claim (bài endianness — UCS-2 `Hello` là `00 48` hay `48 00` tùy máy; JWT không phải chỗ để thử).

```json
{
  "sub": "550e8400-e29b-41d4-a716-446655440000",
  "email": "tanaka@example.jp",
  "name": "田中太郎",
  "exp": 1893456000000
}
```

---

## Incident 5: Prometheus chết vì đếm nhầm thứ cần đếm

Metric mới merge tối Chủ nhật:

```text
login_requests_total{user_id="88421", email="minh@taskflow.vn", status="ok"}
```

Mỗi user một time series. Một triệu DAU → **triệu series**. Prometheus OOM sáng Thứ Hai.

Minh nhớ Cloudflare DNS analytics: aggregate theo `query_name` (high **cardinality**) không nén được như `response_code` (12 giá trị). Gắn `user_id` làm label giống gắn **domain name** làm label metric — đẹp lúc demo, chết lúc scale.

Label được phép: `status`, `method`, `region` — vài chục giá trị. Debug user cụ thể: **trace ID** trong log JSON, sample 1%. Đếm unique user/giờ: rollup batch hoặc HyperLogLog — không Prometheus.

SRE gỡ PR, viết lại `login_requests_total{status, method}`. RAM trở lại. Incident đóng.

---

## Buổi chiều: design doc thật, không slide

7 giờ tối. Channel `#incidents` vàng trở lại. Minh paste doc — không phải checklist Phần 0–8, mà đoạn team sẽ đọc tuần sau:

---

**TaskFlow Auth — những gì sáng nay dạy chúng ta**

Peak 3.000 login/s × 4 query = 12.000 query/s. Little's Law → ~96 connection busy. Pool 25/pod + PgBouncer 20 backend — không 200 connection thẳng vào Postgres 8-core.

QA: 144 exhaustive → từ chối. 15 pairwise trên API login/OAuth + 5 test Safari targeted.

Session: UUID v4, `expires_at` BIGINT ms. INT32 random đạt 50% collision ~77k — không dùng.

Encoding: UTF-8 end-to-end; MIME charset email. Không plain text.

Metrics: không label `user_id` / `email`. Cardinality có giới hạn.

---

CTO reply một dòng: “Lẽ ra đọc trước khi lên báo.” Cả team im — vì đúng.

Minh tắt laptop. Một triệu DAU không phải một triệu bài toán; là **vài câu đếm** bị bỏ qua vì trông quá đơn giản: nhân vài tham số test, nhân λ với W, căn sqrt của không gian ID, đếm label metric thay vì đếm user.

Đó là toán rời rạc trong CNTT — không nằm trong đề thi cuối kỳ, nằm trong Slack lúc 7:45 sáng.

---

## Bài tập thực hành

### Bài tập 1

Startup **FlowBoard** (mô hình giống TaskFlow) vừa đạt **800.000 DAU**. SRE đo peak login **2.500 request/s** lúc 8h sáng. Mỗi login thành công gọi **5 query** DB, latency p50 **10 ms**. Kiến trúc: **8 pod** app, PostgreSQL **12 core + 2 SSD**, chưa có PgBouncer. DevOps đề xuất `maximumPoolSize=60` mỗi pod “vì gần một triệu user”.

(a) Tính $$L$$ theo Little's Law trên tầng DB. (b) Gợi ý pool mỗi pod (có buffer nhỏ). (c) Tính tổng connection nếu mỗi pod pool 60 và so với công thức HikariCP cho DB instance. (d) Một câu giải thích vì sao 800.000 DAU không đi vào phép tính pool.

<details>
<summary>Đáp án</summary>

(a) Throughput query:

$$\lambda = 2{,}500 \times 5 = 12{,}500 \text{ query/s}$$

$$W = 0{,}010 \text{ s}$$

$$L = 12{,}500 \times 0{,}010 = 125$$

Trung bình **125** connection busy trên cluster — không phải 800.000.

(b) Chia cho 8 pod: $$125 / 8 \approx 15{,}6$$ busy/pod. Cộng buffer spike → pool **20–25/pod** hợp lý (gần incident TaskFlow: 25/pod).

(c) Tám pod × 60 = **480** connection client. Công thức HikariCP:

$$2 \times 12 + 2 = 26$$

**480 ≫ 26** — vượt gần 20 lần điểm benchmark. DB sẽ context-switch và lock contention trước khi “đủ connection cho user”. Cần giảm pool/pod hoặc thêm **PgBouncer** multiplex xuống ~20–26 backend.

(d) **DAU** đếm người khác nhau trong cả ngày; nhiều người đã login từ sáng sớm không giữ connection DB. Pool cần $$\lambda$$ (query/s lúc peak) và $$W$$ (latency query) — hai đại lượng throughput, không phải headcount marketing.

</details>

### Bài tập 2

Team QA của FlowBoard kế thừa ma trận test login: browser **5** × OS **4** × device **3** × locale **3** × auth method **2**, mỗi cấu hình **8** bước kiểm tra API. Product yêu cầu “chạy exhaustive trước release”.

(a) Tính số cấu hình và tổng bước manual. (b) Nếu mỗi bước mất 2 phút, sprint hai tuần (10 ngày làm × 6 giờ/ngày) đủ không? (c) Giải thích vì sao pairwise ~15 test vẫn bắt được bug **Safari + iOS + vi + OAuth** mà test Chrome-only bỏ sót. (d) Đề xuất bộ test tối thiểu (số lượng + nguyên tắc) cho ship an toàn.

<details>
<summary>Đáp án</summary>

(a) Cấu hình:

$$5 \times 4 \times 3 \times 3 \times 2 = 360$$

Bước:

$$360 \times 8 = 2{,}880 \text{ bước}$$

(b) Thời gian:

$$2{,}880 \times 2 = 5{,}760 \text{ phút} \approx 96 \text{ giờ}$$

Sprint có $$10 \times 6 = 60$$ giờ/người — **không đủ** cho một QA, chưa kể regression khác. Đây là combinatorial explosion incident 2.

(c) Pairwise đảm bảo mọi **cặp** tham số (browser–locale, browser–method, locale–method, …) xuất hiện ít nhất một test. Cặp **Safari + vi** và **Safari + OAuth** và **vi + OAuth** đều được cover trong bảng 15 dòng — bug cookie `SameSite` trên Safari locale Việt lộ ra. Chrome-only không tạo cặp Safari–vi nào.

(d) Gợi ý: **12–18 test pairwise** trên entry point `POST /login` và `GET /oauth/callback` + **3–5 test targeted** Safari/iOS (cookie, redirect URI) + smoke trên production-like staging. Tổng ~20 test thay vì 2.880 bước — đủ cover tương tác hai chiều, không đủ cho olympiad năm tham số.

</details>

### Bài tập 3

Intern đề xuất schema session FlowBoard:

```sql
session_id   INT,          -- Random.nextInt()
expires_at   INT,          -- Unix giây
user_agent   VARCHAR(64)   -- hash bucket cho audit
```

Hệ thống dự kiến **120.000 session mới/ngày**, lưu schema **10 năm**. Security review hỏi ba câu: collision session, Y2038, và hash bucket audit.

(a) Ước lượng $$n_{0.5}$$ cho `session_id` INT32 và so sánh với 120k session/ngày — sau bao lâu vào vùng rủi ro 50%? (b) Vì sao `expires_at` INT giây là rủi ro dài hạn dù login chạy tốt năm 2026? (c) Đề xuất thay thế hai cột số và một dòng phân biệt “uniqueness session” với “kỳ vọng match hash bucket” (Matt Might).

<details>
<summary>Đáp án</summary>

(a) $$n_{0.5} \approx 1{,}177\sqrt{2^{32}} \approx 77{,}000$$ session trong cùng không gian random — chưa cần 4 tỷ.

Với 120.000 session/ngày, nếu coi như tích lũy ID active trong window ngắn, **< 1 ngày** đã vượt 77k nếu không rotate không gian; trong thực tế TTL session làm giảm $$n$$ đồng thời, nhưng 120k/ngày vẫn đưa hệ vào vùng $$P(\text{collision})$$ đáng kể trong vài ngày–tuần — đủ lộ bug “user A thấy board user B”. Nên dùng **UUID v4** (122 bit random) hoặc INT64.

(b) INT32 giây overflow **2038-01-19** (Y2038): `expires_at` +1 có thể nhảy về 1901, session hết hạn sớm hoặc sống mãi tùy so sánh. Schema “sống 10 năm” vẫn chạm mốc 2038 trước khi hết hạn thiết kế. Dùng **BIGINT milliseconds** (như JWT `exp` trong incident 4).

(c) Thay thế: `session_id UUID`, `expires_at BIGINT` (ms since epoch). Hash `user_agent` vào bucket audit là bài **kỳ vọng số match** $$E = n - D + D((D-1)/D)^n$$ với $$D$$ bucket — trả lời “trung bình bao nhiêu log cùng bucket”, không trả lời “hai session có trùng ID không”. Design doc cần hai dòng riêng; gộp chung là lỗi incident 3.

</details>

### Bài tập 4

PR cuối tuần gộp hai thay đổi: (1) metric `login_requests_total{user_id, email, status}`; (2) email welcome HTML không khai `charset`, API trả JSON không header charset. Thứ Hai: Prometheus OOM và ticket Nhật `????` cho tên kanji.

(a) Ước lượng số time series Prometheus nếu **500.000 DAU** mỗi người tạo trung bình **2** login/ngày và mỗi `user_id` là label riêng. (b) So sánh với metric chỉ label `status`, `method`, `region` ($$|V| \approx 30$$). (c) Liệt kê bốn lớp pipeline encoding cần thống nhất UTF-8 (từ incident 4). (d) Viết đoạn review PR từ chối cả hai thay đổi — mỗi thay đổi một câu lý do toán rời rạc.

<details>
<summary>Đáp án</summary>

(a) Mỗi `user_id` distinct → một series cho mỗi tổ hợp label khác. Cỡ đơn hàng:

$$500{,}000 \times 2 = 1{,}000{,}000 \text{ login/ngày}$$

Nếu mỗi user_id là label, số series theo user_id có thể lên **hàng trăm nghìn đến triệu** (tùy cardinality `status` nhân vào) — Prometheus OOM như incident 5. Cardinality của label = số giá trị distinct, không phải “chỉ khi debug”.

(b) Label tập nhỏ (~30 tổ hợp `status × method × region`) → **vài chục đến vài trăm** series cố định, RAM ổn định, dashboard SLA vẫn đọc được. Reduction từ triệu series xuống ~30 là khác biệt **đếm** — giống Cloudflare `response_code` vs `query_name`.

(c) Bốn lớp: **HTTP API** `Content-Type: application/json; charset=utf-8`; **PostgreSQL** encoding UTF8; **email SMTP** `Content-Type: text/html; charset=UTF-8` trên MIME part; **log file** UTF-8 (không Latin-1 mặc định server). JWT payload Unicode → Base64URL trên wire; không nhét binary endian-sensitive vào claim.

(d) Ví dụ review:

- Metric: “Label `user_id`/`email` có cardinality ~DAU → triệu time series, vi phạm nguyên tắc low-cardinality metrics; debug bằng trace ID trong log JSON, aggregate user/giờ bằng batch hoặc HLL.”
- Encoding: “Không có charset = client đoán bảng mã → mojibake kanji/Việt; byte không có ‘plain text’ (Joel) — UTF-8 end-to-end trên API, DB, email, log.”

</details>

---

## Tóm tắt

Sáng Thứ Hai của TaskFlow không phải một bug — là **năm** bài đếm cùng đổ vào cửa login. **Incident 1** nhắc DAU, concurrent user, và RPS là ba con số khác nhau: Little's Law $$L = \lambda \times W$$ với peak 3.000 login/s × 4 query cho ~96 connection busy, trong khi pool 50/pod × 6 pod vượt xa công thức HikariCP $$2 \times 8 + 1 = 17$$ — pool quá lớn làm Postgres **chậm hơn**, không nhanh hơn. **Incident 2** là combinatorial explosion: $$4 \times 3 \times 3 \times 2 \times 2 = 144$$ cấu hình × 10 bước = 1.440 bước không fit sprint; pairwise ~15 test vẫn cover cặp Safari + vi + OAuth mà Chrome-only bỏ sót.

**Incident 3** đưa birthday paradox vào schema: INT32 random đạt 50% collision quanh **77.000** session, không phải 4 tỷ; UUID v4 và `expires_at` BIGINT ms tránh cả va chạm ID lẫn Y2038. Hash audit bucket là câu hỏi Matt Might (kỳ vọng match), không gộp với uniqueness session. **Incident 4** tái hiện Joel 2003: email và API gửi **byte** không khai charset → `????` thay vì `田中太郎`; UTF-8 thống nhất từ HTTP, DB, MIME email đến log. **Incident 5** là cardinality trên metric: label `user_id` tạo ~triệu time series, Prometheus OOM — cùng logic Cloudflare khi aggregate theo chiều high-cardinality thay vì `status`/`region` vài chục giá trị.

Case study không thêm công thức lạ; nó chứng minh các mảnh Chương 9 **cộng lại** ở một entry point thực tế. Minh tắt laptop với design doc đếm được: pool theo $$\lambda \times W$$, test theo cặp tham số, ID theo $$\sqrt{d}$$, byte theo charset, metric theo $$|V|$$ label. Một triệu DAU không phải một triệu bài toán — là vài phép nhân bị bỏ qua vì trông quá đơn giản.

Sau đó, **Chương 10: Quan hệ truy hồi** sẽ dạy cách mô hình hóa tăng trưởng theo thời gian — dự báo không chỉ snapshot 7:45 sáng, mà cả quý sau khi DAU đôi lên.