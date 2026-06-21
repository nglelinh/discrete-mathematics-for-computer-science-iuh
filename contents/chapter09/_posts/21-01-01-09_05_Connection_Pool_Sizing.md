---
layout: post
title: "Connection pool sizing: Đếm kết nối với Little's Law"
categories: chapter09
date: 2021-01-01
order: 5
required: false
lang: en
---

Thứ Sáu, 14 giờ 30 — demo cho khách hàng enterprise.

API login của startup fintech **vừa được báo** “10.000 user đồng thời”. CTO gửi Slack: *“Tăng HikariCP lên 200 mỗi pod cho chắc. User đông mà.”*

DevOps lead Dũng mở Grafana. PostgreSQL `active_connections` đã chạm **180** trên máy **8 core + 1 SSD**. P99 query từ 12 ms nhảy lên **340 ms**. Log app:

```text
HikariPool-1 - Connection is not available, request timed out after 30000ms
```

Nghịch lý khiến Dũng dừng tay trước khi sửa config: pool **lớn hơn** → DB **chậm hơn** → request **chờ lâu hơn** → timeout nhiều hơn. Khách enterprise vẫn đang chờ trong phòng họp; CTO vẫn tin rằng “càng nhiều connection càng an toàn”.

Brett Wooldridge, tác giả **HikariCP**, viết wiki [About Pool Sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) dựa trên queuing theory và benchmark PostgreSQL: pool quá lớn làm throughput **giảm** vì context switch và lock contention. Câu trả lời không nằm trong cảm giác “càng nhiều càng tốt” — nằm trong **Little's Law** và một công thức đếm mà Dũng đã gặp ở chương hàng đợi.

---

## User đồng thời ≠ connection DB

Hai tầng “đồng thời” hay bị nhầm khi tranh luận pool size. **Concurrent users** là số người mở app cùng lúc — họ có thể đọc dashboard, gõ form, hoặc chờ mạng chậm mà **không** giữ kết nối tới PostgreSQL suốt phiên đó. **Concurrent DB connections** là số session TCP và backend process PostgreSQL đang **thực sự giữ** tại một thời điểm: đang chạy query, đang trong transaction, hoặc đang chờ lock.

Một user đọc dashboard 30 giây chỉ **giữ connection vài millisecond** mỗi lần API gọi xuống DB. Mười nghìn user online không có nghĩa mười nghìn connection — đây là bài toán **đếm có điều kiện**: chỉ đếm request đang *active* trên DB, không đếm toàn bộ session HTTP hay số tab trình duyệt đang mở.

**Connection pool** giữ $$N$$ connection mở sẵn, cho thread mượn khi cần, trả lại sau khi xong. $$N$$ quá nhỏ thì request xếp hàng chờ trong app; $$N$$ quá lớn thì chính DB bị quá tải vì mỗi connection là một process riêng tranh CPU và shared buffer.

![Database connection pool — concept](/discrete-mathematics-for-computer-science-iuh/img/course/Client-server-model.svg)

*Hình 9.12: Nhiều client chia sẻ ít connection DB qua pool — không phải 1:1 user:connection.*

Dũng nhớ incident tuần trước: marketing đếm **DAU** (daily active users), SRE đếm **RPS** (request per second), CTO đếm **concurrent browser tab**. Ba con số, ba quyết định pool khác nhau — chỉ một trong số đó đúng cho PostgreSQL. Pool size không trả lời câu hỏi “bao nhiêu người đang online”; nó trả lời “bao nhiêu query đang chạy đồng thời trên DB”.

---

## Little's Law — công thức hàng đợi cứu demo

Trong hệ ổn định (steady state), **Little's Law** nối ba đại lượng:

$$L = \lambda \times W$$

Ở đây $$L$$ là số “khách” trung bình đang ở trong hệ — với connection pool, đó là số connection **busy** trung bình. $$\lambda$$ là tốc độ vào, throughput: bao nhiêu query hoàn thành mỗi giây. $$W$$ là thời gian trung bình một query ở trong hệ — từ lúc bắt đầu cho tới lúc trả connection về pool.

Ví dụ đơn giản: nếu DB xử lý $$\lambda = 1000$$ query/s và mỗi query mất trung bình $$W = 0{,}01$$ s (10 ms), thì trung bình có $$L = 10$$ connection busy cùng lúc. Để ít khi chờ khi có biến động spike, người ta đặt pool:

$$N \geq \lceil L \rceil + \text{buffer}$$

Buffer nhỏ cho đỉnh ngắn — **không** nhân đôi user count hay DAU.

Dũng lấy số liệu demo thật từ Grafana và APM. Peak **500 request/s** tới API login. Mỗi request trung bình **2 query** xuống DB. Mỗi query mất **5 ms** trên PostgreSQL khi pool còn hợp lý. Tính throughput query:

$$\lambda = 500 \times 2 = 1000 \text{ query/s}$$

Thời gian ở trong hệ:

$$W = 0{,}005 \text{ s}$$

Số connection busy trung bình:

$$L = 1000 \times 0{,}005 = 5$$

Trung bình chỉ **5 connection busy** — pool **10–15** là hợp lý cho một pod. Không phải 200. Dũng gửi lại Slack với bảng tính: “10k user” mà marketing nói có thể là DAU cả ngày; concurrent thực tế lúc peak chỉ vài trăm RPS, và Little's Law cho ra con số đếm được.

<div class="content-box insight-box" markdown="1">
**Điểm Chương 9:** Incident “10k user” thường là nhầm **DAU**, **concurrent user**, hay **RPS**. Chỉ $$\lambda \times W$$ mới trả lời pool — đó là phép đếm có điều kiện trên workload thật, không phải trên headline marketing.
</div>

---

## Công thức HikariCP — vì sao 200 connection chậm hơn 20

Wiki HikariCP tóm tắt benchmark từ [PostgreSQL Wiki — Number of connections](https://wiki.postgresql.org/wiki/Number_Of_Database_Connections). Công thức khởi đầu cho OLTP trên **một** instance PostgreSQL:

$$\text{connections} = \text{core\_count} \times 2 + \text{effective\_spindle\_count}$$

**core_count** là số CPU core **của máy chạy PostgreSQL** — không phải số core trên app server hay số pod Kubernetes. **effective_spindle_count** là số ổ đĩa vật lý (spindle); với **một SSD** người ta thường lấy **1**.

DB server demo của Dũng: 8 core + 1 SSD:

$$\text{pool} = 8 \times 2 + 1 = 17$$

Khuyến nghị wiki: **không** đặt 200 “cho chắc”. PostgreSQL mỗi connection là một **backend process** cộng thêm memory riêng. Quá nhiều process → tranh CPU (context switch), lock trên shared buffer, checkpoint và IO contention. Đồ thị benchmark trên wiki cho thấy throughput đạt đỉnh ở pool **nhỏ**, rồi **giảm** khi tăng connection — đúng những gì Dũng thấy: P99 từ 12 ms nhảy 340 ms khi `active_connections` chạm 180.

Dũng so sánh hai con số: Little's Law cho workload login ra $$L \approx 5$$ busy trung bình; công thức HikariCP cho **giới hạn trên** tổng connection tới một DB instance là khoảng 17. Hai công thức trả lời hai câu hỏi khác nhau — “cần bao nhiêu cho traffic này?” và “DB chịu được bao nhiêu trước khi tự làm chậm mình?” — nhưng cùng chỉ ra rằng 200 là xa cả hai.

<div class="content-box warning-box" markdown="1">
Công thức $$2 \times \text{cores} + \text{spindles}$$ là **điểm xuất phát** cho OLTP trên **một** DB instance — workload analytics, replica đọc nặng, hoặc nhiều database trên cùng máy cần profiling riêng. Đừng copy số từ blog sang production mà không đo $$\lambda$$ và $$W$$ trên hệ của bạn.
</div>

---

## Nhiều app server và PgBouncer

Startup có **3 instance** API. Nếu mỗi instance đặt pool HikariCP **10**, tổng **30 connection** tới PostgreSQL — vẫn trong `max_connections` mặc định 100, nhưng đã vượt công thức 17 cho một DB 8 core. Khi scale thêm pod, tổng connection client tăng tuyến tính theo số replica; DB thì không scale theo cùng tốc độ.

**PgBouncer** là lớp trung gian multiplex: nhiều connection từ app được ghép xuống ít connection thật trên PostgreSQL. Hình dung luồng: hàng nghìn thread app → mỗi app giữ pool 50 → PgBouncer gom lại → chỉ ~17 backend process thật trên Postgres. Toán vẫn là Little's Law — chỉ thêm một hàng đợi trung gian; $$W$$ có thể tăng nhẹ nếu PgBouncer transaction mode không khớp pattern giữ connection lâu trong app.

Trong thread incident chiều thứ Sáu, Dũng đề xuất: HikariCP **15 mỗi pod** (3 pod → 45 connection phía client), PgBouncer chạy transaction mode với `default_pool_size=17` — ghép xuống khoảng 17 backend Postgres, sát công thức HikariCP. Redeploy xong, P99 query về lại dưới 20 ms, timeout biến mất. Demo pass. CTO reply: “Ừ. User không bằng connection. Anh nhầm cả đời.”

Dũng ghi vào runbook ba câu: **concurrent user** đếm người, **$$\lambda$$** đếm query/giây, **pool** đếm connection busy — ba lớp khác nhau. Pool lớn hơn không luôn nhanh hơn; đôi khi chậm hơn rõ rệt vì DB tranh nhau thay vì phục vụ.

**Đọc thêm**: [HikariCP — About Pool Sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) · [PostgreSQL Wiki — Number of connections](https://wiki.postgresql.org/wiki/Number_Of_Database_Connections)

---

## Bài tập thực hành

### Bài tập 1

API checkout xử lý peak **200 request/s**. Mỗi request gọi trung bình **3 query** DB, mỗi query mất **8 ms**. Dùng Little's Law, tính $$L$$ (số connection busy trung bình) và gợi ý pool size $$N$$ với buffer 5.

<details>
<summary>Đáp án</summary>

Throughput query:

$$\lambda = 200 \times 3 = 600 \text{ query/s}$$

Thời gian trong hệ:

$$W = 0{,}008 \text{ s}$$

Little's Law:

$$L = 600 \times 0{,}008 = 4{,}8$$

Trung bình khoảng **4,8** connection busy. Với buffer 5:

$$N \geq \lceil 4{,}8 \rceil + 5 = 5 + 5 = 10$$

Gợi ý pool **10** cho một instance app phục vụ workload này — không nhân theo “số user online”.

</details>

### Bài tập 2

PostgreSQL chạy trên máy **16 core**, **2 SSD** (đếm effective spindle = 2). Áp dụng công thức HikariCP, tính số connection khuyến nghị cho **một** DB instance. Nếu có **4 pod** API, mỗi pod pool 20, tổng bao nhiêu? So sánh với giới hạn công thức.

<details>
<summary>Đáp án</summary>

Công thức HikariCP:

$$\text{pool} = 16 \times 2 + 2 = 34$$

Khuyến nghị tổng connection tới DB instance: khoảng **34**.

Bốn pod, mỗi pod pool 20:

$$4 \times 20 = 80 \text{ connection}$$

**80 > 34** — vượt gần gấp đôi điểm benchmark. DB có thể vẫn “chạy được” dưới `max_connections`, nhưng throughput và latency thường xấu hơn pool nhỏ hơn. Cần giảm pool mỗi pod (ví dụ ~8–10) hoặc dùng **PgBouncer** để multiplex 80 client xuống ~34 backend thật.

</details>

### Bài tập 3

Marketing báo **50.000 DAU**. SRE đo peak **800 RPS** lúc 20h. DevOps đặt HikariCP = 500 “vì user đông”. Phân tích vì sao ba con số này không thay thế được nhau, và đại lượng nào đi vào Little's Law.

<details>
<summary>Đáp án</summary>

**DAU** đếm người dùng khác nhau trong **cả ngày** — không phải số người online cùng lúc lúc peak, cũng không phải RPS. **800 RPS** là throughput HTTP tới app — cần nhân thêm số query mỗi request mới ra $$\lambda$$ (query/s) cho Little's Law. **Pool = 500** nhầm “nhiều user” với “nhiều connection DB”; không có $$W$$ (latency query) trong phép tính.

Little's Law cần $$\lambda$$ (query hoàn thành/giây) và $$W$$ (giây/query) trên **DB**, không cần DAU. Ví dụ nếu 800 RPS × 2 query × $$W = 6$$ ms thì $$L = 1600 \times 0{,}006 = 9{,}6$$ — pool ~15–20 hợp lý hơn 500, và vẫn phải so với công thức $$2 \times \text{cores} + \text{spindles}$$ của máy DB.

</details>

### Bài tập 4

Hệ thống: **5 pod** API, mỗi pod HikariCP **12** → 60 connection client. PgBouncer `default_pool_size=20` xuống PostgreSQL 8 core + 1 SSD. Giải thích vai trò PgBouncer trong bài toán đếm và tại sao 60 ≠ 20 không mâu thuẫn.

<details>
<summary>Đáp án</summary>

**60** là tổng connection từ app tới PgBouncer (hoặc trực tiếp tới DB nếu không có proxy) — mỗi pod giữ pool riêng để thread không chờ acquire quá lâu. **20** là số backend connection thật PgBouncer mở tới PostgreSQL; multiplex nhiều client ngắn trên ít server connection dài.

Little's Law áp dụng ở **tầng DB**: $$\lambda$$ và $$W$$ đo trên query hoàn thành tại Postgres; $$L$$ busy trung bình nên xấp xỉ 20 (giới hạn pool PgBouncer), không phải 60. Công thức HikariCP cho 8 core + 1 SSD cho **~17** — `default_pool_size=20` gần đúng; nếu không có PgBouncer, 60 connection thẳng vào Postgres sẽ vượt xa 17 và dễ gặy latency như incident Dũng.

</details>

---

## Tóm tắt

Connection pool sizing là bài toán **đếm** — không phải cảm giác an toàn. **Concurrent users** và **DAU** mô tả người dùng; **$$\lambda$$** mô tả query/giây; **pool** mô tả connection DB đang busy hoặc sẵn sàng cho thread. Ba lớp không map 1:1.

**Little's Law** $$L = \lambda \times W$$ cho biết trung bình cần bao nhiêu connection busy: nhân throughput với latency query, cộng buffer nhỏ cho spike. **Công thức HikariCP** $$2 \times \text{cores} + \text{spindles}$$ cho giới hạn trên hợp lý cho một PostgreSQL instance — pool lớn hơn có thể làm DB **chậm hơn**, không nhanh hơn. Khi nhiều app server scale ngang, **PgBouncer** multiplex để tổng backend vẫn sát công thức.

Incident demo của Dũng là mẫu điển hình: nhầm “10k user” với “10k connection”, tăng pool, rồi timeout vì DB quá tải. Sửa bằng số — Little's Law cho workload, HikariCP cho máy DB, PgBouncer cho kiến trúc nhiều pod.

Bài sau: **combinatorial explosion** trong QA — [testRigor](https://testrigor.com/blog/what-is-combinatorial-testing/) và cách giảm 324 cấu hình browser–OS–device xuống khoảng 15 test pairwise mà vẫn cover mọi **cặp** tham số, không bỏ sót tương tác hai chiều hay nhầm “test ít” với “test mù”.