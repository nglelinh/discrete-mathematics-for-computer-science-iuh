---
layout: post
title: "Cardinality và analytics: Bài học từ 1M DNS queries/giây của Cloudflare"
categories: chapter09
date: 2021-01-01
order: 9
required: false
lang: en
---

Thứ Hai, dashboard DNS analytics màu xanh. Thứ Ba, một datacenter latency đỏ — nhưng **chỉ** trên một subset query name mà aggregate zone-level che mất.

Khoa, engineer analytics tại team DNS, đọc lại [How Cloudflare analyzes 1M DNS queries per second](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/) (Marek Vavruša, 2017) trong lúc debug. Cloudflare xử lý **hơn 1 triệu truy vấn DNS mỗi giây**. Mỗi query ghi: zone, response code, **query name**, thời gian, kích thước…

Bài trước (09_08) đếm **va chạm** trong không gian hữu hạn $$D$$ bucket. Bài này gặp biến thể production khác: không hỏi “có trùng không?” mà hỏi “**có bao nhiêu giá trị distinct** trên một cột?” — và câu trả lời quyết định aggregate có **nén** được hay không.

Một bài toán toán rời rạc nổi lên ngay:

> Aggregate theo cột **độ cao cardinality** (nhiều giá trị unique) có thể **không giảm** số dòng — đôi khi **tăng** so với raw log.

**Response code** chỉ có khoảng 12 giá trị → aggregate theo phút **giảm** mạnh số dòng. **Query name** có thể **hàng triệu** domain khác nhau → reduction **0–60×**, không ổn định. Cardinality không phải buzzword BI — là **|tập giá trị distinct|** quyết định aggregate có **nén** được hay không.

---

## Triệu query/giây — metadata, không full payload

Con số blog 2017 là **hơn 1 triệu queries/s** toàn cầu; con số thực tế hôm nay còn lớn hơn. Mỗi log chỉ khoảng **150 byte** telemetry — không phải full DNS message — nhưng nhân với throughput đó vẫn là **terabyte/tháng** nếu ship mọi thứ về warehouse mà không lọc.

![Cloudflare DNS analytics — blog header](/discrete-mathematics-for-computer-science-iuh/img/course/how-cloudflare-analyzes-1m-dns-queries-per-second.png)

*Hình 9.15: DNS analytics quy mô triệu query/giây — đếm và tổng hợp là vấn đề hạ tầng (nguồn: [Cloudflare Blog](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/)).*

Pipeline Cloudflare mô tả trong blog: edge server log **Cap'n Proto** → multiplexer → Kafka → warehouse (ClickHouse). Insight quan trọng không nằm ở tên công nghệ mà ở chỗ xử lý **metadata tại edge**, không ship full DNS message — giảm bandwidth vì đếm byte có chủ đích. Khoa nhớ lại bài `09_01`: không có “plain text”, chỉ có byte và quy ước; ở đây không có “raw log thuần”, chỉ có **schema telemetry** và quyết định cột nào đáng lưu.

---

## Vì sao aggregate “theo qname” không scale

Gọi $$R$$ là số dòng raw log trong một phút. Khi aggregate theo chiều $$C$$ với cardinality $$|V_C|$$ giá trị unique trong cửa sổ thời gian, số dòng sau aggregate phụ thuộc vào **|tập giá trị distinct|**, không phụ thuộc vào tên cột trên dashboard.

Với **response code**, $$|V| \approx 12$$. Một triệu query trong phút, phân bố đều qua các mã, mỗi bucket thời gian tối đa **12 dòng/phút** — reduction lý tưởng khoảng 83.000×. Cacheable queries lặp nhiều lần cùng mã `NOERROR` hay `NXDOMAIN` nên aggregate thực tế còn gọn hơn nữa.

Với **query name**, $$|V|$$ có thể tiệm cận hàng triệu: typo, subdomain ngẫu nhiên, random subdomain attacks. Blog Cloudflare ghi reduction chỉ **0–60×** — không ổn định. Worst case: mỗi query name unique → **1M dòng/phút**, reduction **1×**, không giảm gì so với raw.

<div class="content-box warning-box" markdown="1">
Khi $$|V|$$ gần $$R$$, mỗi dòng aggregate gần như một unique key → **không nén được**. Nhiều chiều cardinality cao nhân với nhau — **explosion** ô aggregate.
</div>

Khi aggregate theo $$k$$ cột với cardinality $$c_1, \ldots, c_k$$ trong cùng cửa sổ:

$$R' \leq \min\left(R,\; \prod_{i=1}^{k} c_i'\right)$$

Ví dụ zone (10.000 giá trị) × qname (1M unique trong giờ) → upper bound lý thuyết **10 tỷ** ô; thực tế sparsity giảm nhưng vẫn đủ gây **explosion** storage và query cost. Khoa gặp đúng pattern này khi materialized view `zone + qname + minute` phình to nhanh hơn raw log sampled — vì mỗi ô aggregate vẫn phải lưu key đủ dài.

---

## Incident — aggregate tiết kiệm tiền, raw cứu root cause

Cloudflare mô tả latency spike tại một datacenter. Trên **aggregated** zone-level, dashboard chỉ thấy xu hướng thô: “zone X chậm hơn trung bình”. Trên **unaggregated** log, team thấy **subset query name** cụ thể chậm → truy ra **firewall rule** sai áp lên pattern qname.

Khoa gặp biến thể nhỏ hơn nhưng cùng bản chất. Materialized view theo `zone + response_code` đủ cho SLA dashboard hàng ngày; debug incident cần sampled log giữ dimension **qname** — vì latency không đỏ trên toàn zone, chỉ đỏ trên vài tên miền lạ.

**Bài học** Khoa ghi vào post-mortem: aggregate tiết kiệm storage và query trend; raw (hoặc sampled) cần cho root cause — trade-off **đếm** vs **lưu trữ**, giống chọn encoding (bài `09_01`): không có schema “một size fits all”. Dashboard zone-level trả lời “có chuyện gì đang xảy ra?”; log giữ qname trả lời “**cái gì** đang xảy ra?”.

---

## HyperLogLog — đếm distinct mà không lưu từng key

Câu hỏi analytics hay gặp: “Bao nhiêu **query name khác nhau** trong 1 giờ?” Chạy `COUNT(DISTINCT qname)` trên terabyte log → cực chậm, bộ nhớ lớn, vì engine phải giữ set key hoặc sort toàn bộ.

**HyperLogLog (HLL)** ước lượng **cardinality** với sai số khoảng 1–2%, mỗi row state chỉ **20–100 byte** (đã nén) thay vì lưu full key. Counter tổng (sum) chỉ cần khoảng 8 byte mỗi row (1 byte nếu nén); HLL sketch đắt hơn nhưng vẫn **cố định** theo độ chính xác, không tăng tuyến tính theo số distinct thực tế.

Merge HLL từ phút → giờ → ngày qua materialized view ClickHouse — cùng ý tưởng merge set trong ch04 nhưng **xấp xỉ**, chấp nhận sai số nhỏ để đổi lấy bộ nhớ cố định.

![HyperLogLog concept — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/hyperloglog.svg)

*Hình 9.16: HyperLogLog — đếm gần đúng số phần tử distinct với bộ nhớ cố định (nguồn: Wikimedia Commons).*

Cloudflare **bỏ stream processor** riêng — ingestion + materialized view đủ cho trend API. ClickHouse merge segment khi insert → đồng thời update bảng aggregate (counters, uniques, quantiles). Khoa không cần nhớ chi tiết thuật toán HLL; anh cần nhớ **khi nào** dùng: câu hỏi “bao nhiêu unique?” trên cột cardinality cao, không cần liệt kê từng key.

**Primary key** là quyết định đếm thứ hai. Sort theo `zone` trước `timestamp` → query một zone đọc contiguous trên disk, nhanh cho dashboard per-customer. Query toàn cầu all zones → scan lớn → cần bảng pre-aggregated hoặc sampled. Chọn primary key = chọn **một** thứ tự sắp xếp; không tối ưu mọi query cùng lúc — giống endianness (bài `09_02`): một quy ước, nhiều workload đọc theo chiều khác nhau.

---

## Epilogue

Khoa sửa firewall rule, latency xanh lại. Post-mortem: thêm sampled qname log 1% traffic cho debug — chi phí storage chấp nhận được so với terabyte aggregate vô dụng theo `zone × qname`.

Cardinality quyết định aggregate có **nén** được không. Low cardinality (`response_code`) → dashboard rẻ; high cardinality (`qname`) → cần HLL, sampling, hoặc chấp nhận không aggregate. Cả aggregate lẫn raw đều cần — trend vs root cause.

**Đọc thêm**: [Cloudflare — 1M DNS queries/sec](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/) · [HyperLogLog — Wikipedia](https://en.wikipedia.org/wiki/HyperLogLog)

---

## Bài tập thực hành

### Bài tập 1

Trong một phút có **900.000** dòng raw DNS log. Aggregate theo `response_code` với $$|V| = 12$$ giá trị distinct, phân bố đều. Ước lượng số dòng sau aggregate và reduction factor (so với raw).

<details>
<summary>Đáp án</summary>

Phân bố đều qua 12 mã → tối đa **12 dòng/phút** mỗi bucket thời gian (mỗi mã một dòng).

Reduction:

$$\frac{900{,}000}{12} = 75{,}000$$

Tức reduction khoảng **75.000×** trong trường hợp lý tưởng. Thực tế có thể ít hơn nếu một vài mã chiếm đa số traffic, nhưng vẫn là low-cardinality aggregate — đúng pattern dashboard SLA.

</details>

### Bài tập 2

Cùng **900.000** dòng/phút, nhưng mỗi `query_name` là unique (worst case attack subdomain ngẫu nhiên). Aggregate theo `query_name` + `minute` cho ra bao nhiêu dòng? Reduction factor là bao nhiêu?

<details>
<summary>Đáp án</summary>

Mỗi qname unique → **900.000 dòng/phút** sau aggregate (mỗi key một dòng).

Reduction:

$$\frac{900{,}000}{900{,}000} = 1$$

Reduction **1×** — không nén được. Đây là lý do Cloudflare blog ghi reduction 0–60× cho qname: worst case gần 1×; best case vẫn xa so với response_code.

</details>

### Bài tập 3

Materialized view aggregate theo `zone` ($$c_1 = 5{,}000$$) × `query_name` ($$c_2 = 200{,}000$$ unique trong giờ) × `response_code` ($$c_3 = 12$$). Dùng công thức upper bound, tính $$\prod c_i$$ và giải thích vì sao storage có thể “nổ” dù raw log trong giờ chỉ 50 triệu dòng.

<details>
<summary>Đáp án</summary>

Upper bound lý thuyết:

$$5{,}000 \times 200{,}000 \times 12 = 12 \times 10^{12}$$

Tức **12 nghìn tỷ** ô aggregate tối đa — vượt xa 50 triệu dòng raw. Công thức $$R' \leq \min(R, \prod c_i')$$ cho **trần**; thực tế sparsity làm ít ô được điền, nhưng vẫn đủ lớn để warehouse và merge cost phình to. Ba chiều cardinality cao **nhân** nhau — không cộng — nên một chiều qname đã đủ phá schema aggregate.

</details>

### Bài tập 4

Dashboard zone-level báo latency bình thường; sampled log 1% giữ `qname` cho thấy 0,3% traffic tới pattern `*.bad-sub.example.com` chậm gấp 10 lần. Giải thích vì sao aggregate zone-level che mất signal, và đề xuất hai lớp dữ liệu (không cần chi tiết triển khai).

<details>
<summary>Đáp án</summary>

Aggregate zone-level **cộng trung bình** (hoặc percentile) latency trên toàn zone — 0,3% traffic chậm bị **dilute** bởi 99,7% traffic nhanh, nên metric zone vẫn xanh. Đây là hạn chế của aggregate theo chiều **low cardinality** khi root cause nằm ở chiều **high cardinality** (qname).

Hai lớp hợp lý: (1) **pre-aggregated** `zone + response_code` (và có thể HLL trên qname) cho trend và SLA — rẻ, nhanh; (2) **sampled raw** hoặc log giữ `qname` cho incident debug — đắt hơn nhưng cứu root cause. Giống incident Cloudflare: aggregate thấy “zone chậm”; unaggregated thấy “**subset qname** chậm”.

</details>

---

## Tóm tắt

Cardinality là **|tập giá trị distinct|** trên một cột — đại lượng toán rời rạc quyết định aggregate có nén được log hay không. Cloudflare xử lý **hơn 1 triệu DNS queries/giây**; mỗi log ~150 byte metadata vẫn thành terabyte/tháng nếu không thiết kế schema đếm có chủ đích.

**Low cardinality** (`response_code`, ~12 giá trị) → aggregate giảm mạnh số dòng, dashboard rẻ. **High cardinality** (`query_name`, có thể hàng triệu) → reduction 0–60×, worst case 1×; nhiều chiều cao nhân theo $$\prod c_i$$ và gây explosion. **HyperLogLog** trả lời “bao nhiêu unique?” với bộ nhớ cố định và sai số nhỏ, thay cho `COUNT(DISTINCT)` trên terabyte.

Aggregate và raw không thay thế nhau: aggregate cho **trend** và chi phí storage; raw hoặc sampled log cho **root cause** khi signal nằm ở subset high-cardinality — như incident firewall rule Cloudflare mà Khoa gặp lại ở quy mô nhỏ hơn. Chọn primary key và materialized view = chọn **một** thứ tự đếm; không schema nào tối ưu mọi câu hỏi cùng lúc.

Bài cuối chương: **case study tổng hợp TaskFlow** — một buổi sáng login sập, và cách pool sizing, pairwise test, birthday paradox, cardinality cùng đổ vào một cửa (`09_10`).