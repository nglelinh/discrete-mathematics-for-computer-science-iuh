---
layout: post
title: "Tập hợp trong CSDL và lập trình: Từ Russell đến Bloom filter"
categories: chapter09
date: 2021-01-01
order: 11
required: false
lang: en
---

Thứ Tư, 9 giờ sáng — campaign email “khách hàng VIP” gửi **hai lần** cho cùng một địa chỉ.

Linh, data engineer tại startup e-commerce, mở query mà intern viết đêm qua:

```sql
SELECT email FROM newsletter_subscribers
UNION ALL
SELECT email FROM loyalty_vip;
```

PM đếm: 48.000 email unique trong CRM, nhưng SendGrid báo **61.000** recipients. Không phải bug ESP — là bug **tập hợp**. `UNION ALL` giữ **mọi bản sao**; `UNION` mới là **hợp** (dedup). Intern hiểu SQL như cú pháp ghép chuỗi, không hiểu như phép toán trên tập.

Bài trước (`09_10`) kể một buổi sáng TaskFlow sập vì đếm sai connection, cardinality metric, và UUID — tất cả qua cửa login. Bài này là **lời kết Chương 9**: quay lại lý thuyết tập hợp từ chương 4, nhưng đặt ngay dưới chân PostgreSQL, Redis, TypeScript, và câu hỏi `if user_id in cache`. Từ tranh cãi Cantor thế kỷ XIX, qua nghịch lý Russell, đến Bloom filter trong crawler — cùng một ngôn ngữ: **phần tử có thuộc tập không**, **hợp–giao–hiệu** ra sao.

Nhiều sinh viên học ch04 rồi nghĩ tập hợp “rất toán”, xa production. Thực tế set theory nằm dưới chân mọi thứ Chương 9 đã chạm: cardinality analytics (`09_09`), hash collision (`09_07`–`08`), connection pool đếm session (`09_05`). Linh sửa campaign không cần thêm công thức lạ — chỉ cần nhớ `UNION` là hợp hai tập kết quả, không phải nối hai danh sách.

---

## Russell và bài học về tự tham chiếu

Georg Cantor dám hỏi: các loại vô hạn có kích thước khác nhau không? Ông biến set theory thành ngôn ngữ chung cho số, hàm, quan hệ — nền mà khoa học máy tính thừa hưởng. Khi bạn viết `SELECT DISTINCT`, bạn đang yêu cầu engine loại phần tử trùng trong một tập tuple; khi bạn khai báo `type ID = string | number`, bạn đang mô tả hợp hai tập giá trị hợp lệ. Cantor không viết PostgreSQL, nhưng mọi phép “có thuộc tập không” trong code đều mượn trực giác ông đặt nền.

![Georg Cantor](/discrete-mathematics-for-computer-science-iuh/img/course/Georg_Cantor_1894.jpg)

*Hình 9.18: Georg Cantor (1845–1918) — nền móng lý thuyết tập hợp hiện đại.*

Bertrand Russell sau đó nêu nghịch lý: xét tập hợp của mọi tập hợp **không** chứa chính nó. Tập đó có chứa chính nó không? Có → theo định nghĩa không được chứa; không → theo định nghĩa phải chứa. Logic bế tắc — không phải trò đố vui.

![Bertrand Russell](/discrete-mathematics-for-computer-science-iuh/img/course/Bertrand_Russell_photo.jpg)

*Hình 9.19: Bertrand Russell — cảnh báo nguy hiểm của tự tham chiếu trong định nghĩa tập.*

Đây không chỉ là cú sốc triết học. Đó là lời nhắc hiện đại: schema “tập hợp mọi thứ” không kiểm soát tự tham chiếu dễ mâu thuẫn — giống JSON lồng vô hạn, hay foreign key vòng `A → B → A`. E. F. Codd (1970) đặt nền **mô hình quan hệ** trên tập hợp có cấu trúc (tuple, domain), tránh “tập của mọi tập” kiểu naive. Mỗi bảng là tập các bộ có kiểu; mỗi cột thuộc một domain — không phải “mọi giá trị có thể tưởng tượng”.

---

## SQL mỗi ngày — SELECT là chọn tập con

![Cơ sở dữ liệu quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

*Hình 9.20: Mỗi bảng là tập các bộ (tuple); truy vấn là phép chọn tập con.*

Một bảng = tập các tuple. `WHERE` = **selection** — lấy tập con thỏa điều kiện:

```sql
SELECT *
FROM Employees
WHERE department = 'IT';
```

Kết quả không phải “danh sách” theo nghĩa thứ tự quan trọng; về mặt đại số quan hệ, đó là tập (hoặc bag nếu bạn bật `DISTINCT` tắt và cho phép trùng). Linh sửa campaign query:

```sql
SELECT email FROM newsletter_subscribers
UNION          -- không phải UNION ALL
SELECT email FROM loyalty_vip;
```

`UNION` = hợp hai tập kết quả, loại trùng. `INTERSECT` = giao. `EXCEPT` = hiệu (phần tử thuộc tập trái nhưng không thuộc tập phải). Ba phép này map trực tiếp từ ch04; SQL chỉ thêm cú pháp và optimizer.

Ví dụ sinh viên học cả DM và DB nhưng không học AI:

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

Đọc bằng ngôn ngữ tập: lấy tập sinh viên đăng ký DM, giao với tập đăng ký DB, rồi bỏ những ai cũng học AI. Query optimizer PostgreSQL thường rewrite nested subquery thành các phép tương đương đại số tập — biết set semantics giúp đọc `EXPLAIN`, không chỉ viết SQL cho đúng cú pháp.

Incident email của Linh là case **hợp** sai: `UNION ALL` không dedup, nên cùng một `email` xuất hiện hai lần trong bag kết quả, SendGrid gửi hai thư. Đổi sang `UNION` là đủ — không cần `DISTINCT` bọc ngoài nếu hai nhánh đã là tập email.

### JOIN — tích Descartes có bộ lọc

`JOIN` được dạy bằng relational algebra, nhưng trực giác tập hợp vẫn mạnh: mỗi bảng là tập bộ; join tạo tập bộ kết hợp thỏa điều kiện khóa.

![Phép JOIN trong SQL](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

*Hình 9.21: JOIN — kết hợp hai bảng theo khóa khớp.*

```sql
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON e.course_id = c.id;
```

Về bản chất, đây là tích Descartes của `Students × Enrollments × Courses`, rồi **lọc** những bộ mà `s.id = e.student_id` và `e.course_id = c.id`. Incident email là case **hợp** sai; incident chậm query tuần trước của Linh là case **tích** phình — `JOIN` thiếu điều kiện `ON`, Cartesian product 10⁶ dòng trước khi `WHERE` kịp cắt. Cùng chương tập hợp, hai thảm họa khác nhau: một thừa phần tử, một nhân phần tử.

<div class="content-box warning-box" markdown="1">
`INNER JOIN` ≈ giao có điều kiện trên khóa; `LEFT JOIN` giữ cả phần tử “mồ côi” bên trái. Nhầm hai phép → mất dòng hoặc nhân dòng — không phải lỗi cú pháp, lỗi **tập**.
</div>

---

## Python `set` — hợp giao hiệu trong ETL

Pipeline nightly của Linh dedup `user_id` trước khi sync warehouse:

```python
newsletter = {"u1", "u2", "u3"}
vip = {"u2", "u4"}

all_reach = newsletter | vip      # union
both = newsletter & vip           # intersection
only_newsletter = newsletter - vip  # difference

if "u2" in vip:
    ...
```

`|`, `&`, `-`, `in` — ánh xạ trực tiếp từ ch04. Dictionary không phải tập thuần (key–value), nhưng `if user_id in cache` là câu hỏi **membership** trên tập key — cùng câu hỏi Cantor đặt nền, chỉ khác là bạn trả lời bằng hash lookup thay vì suy luận trên giấy.

Linh dùng set trong ETL vì dedup trong RAM nhanh hơn `SELECT DISTINCT` trên staging table khi dataset vừa phải. Khi scale lên hàng chục triệu `user_id`, set Python không còn vừa RAM — lúc đó Bloom filter hoặc `UNION` trong SQL trên warehouse mới là lựa chọn đúng.

---

## Bloom filter — tập xấp xỉ khi bộ nhớ là tiền

Redis layer trước PostgreSQL của Linh dùng **Bloom filter** để trả lời nhanh: “`user_id` này đã từng mua chưa?” Câu hỏi membership xuất hiện hàng triệu lần mỗi đêm; quét bảng `Orders` mỗi lần là đốt I/O và tiền RDS.

Bloom filter không lưu trọn tập; nó lưu “dấu vết” bit qua vài hàm hash để trả lời gần đúng. Kiểm tra membership cực nhanh, ít RAM. **False positive** có thể — filter nghĩ user đã mua, query DB thừa một lần. **False negative** không có — không bỏ sót người thật sự đã mua. Đó là trade-off có chủ đích: chấp nhận query thừa để đổi RAM và latency.

![Bloom filter](/discrete-mathematics-for-computer-science-iuh/img/course/Bloom_filter.svg)

*Hình 9.22: Bloom filter — membership xác suất, chấp nhận false positive để đổi RAM.*

Liên hệ bài `09_07`–`08`: hash vào $$D$$ bucket, xác suất va chạm — cùng họ tư duy **đếm membership** dưới quy mô lớn. Bloom filter là tập **xấp xỉ**; bài `09_09` Cloudflare cũng chấp nhận xấp xỉ (HyperLogLog) thay vì đếm distinct chính xác trên terabyte log. Ứng dụng thực tế: cache negative lookup, distributed DB, web crawler (“URL đã crawl chưa?”), storage engine — mọi nơi cần trả lời “có trong tập không?” mà không mang cả tập theo.

---

## Hash table, index — tổ chức tập để tra cứu

Hash table: tập keys, ánh xạ key → bucket, xử lý collision khi hai key cùng bucket. Nền của `dict`, `set`, in-memory cache — và của Bloom filter phía trên.

![Hash table](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

*Hình 9.23: Hash table — tra cứu membership trung bình O(1).*

Trong PostgreSQL, **index** trên `customer_id` giúp:

```sql
SELECT * FROM Orders WHERE customer_id = 42;
```

lấy **tập con nhỏ** thay vì quét toàn bộ `Orders`. Index không phải “tập hợp” theo nghĩa toán học thuần — nó là cấu trúc dữ liệu sắp xếp lại phần tử để membership và range query rẻ hơn. Nhưng trực giác vẫn là tập: toàn bộ bảng là universe; điều kiện `WHERE` chọn subset; index giúp engine không phải duyệt universe.

Tập hợp ở đây là chi phí I/O và tiền RDS — không còn bài tập sách. Linh nhớ incident TaskFlow (`09_10`): pool connection và cardinality metric là đếm khác; index và Bloom filter là đếm membership khác — cùng một chương “đếm có chủ đích”.

---

## Type system — mỗi type là một tập giá trị

TypeScript:

```ts
type ID = string | number;
```

`string | number` = **hợp** hai tập giá trị hợp lệ. `bool` = $$\{\text{true}, \text{false}\}$$. `Option<T>` trong Rust hoặc `Maybe` trong Haskell = $$\{\text{None}\} \cup T$$ — thêm phần tử “không có giá trị” vào domain.

![Union of sets](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

*Hình 9.24: Union type — hợp tập giá trị trong type system.*

Type checker hỏi: giá trị runtime có **thuộc** tập mà type cho phép không? Cùng câu hỏi membership với `IN` trong SQL và `in` trong Python — ba tầng, một trực giác. Khi bạn viết `function process(id: string | number)`, compiler từ chối `process(true)` vì `true` không thuộc hợp `{string} ∪ {number}`.

Discriminated union (`type Result = { ok: true, data: T } | { ok: false, error: string }`) là cách type system mô tả **phân hoạch** tập kết quả — mỗi nhánh là tập con disjoint, hợp lại là toàn bộ không gian lỗi/thành công. Đó là set partition trong ch04, chỉ đổi tên thành “algebraic data type”.

---

## Epilogue

Linh sửa `UNION ALL` → `UNION`, rerun campaign — 48.012 recipients, khớp CRM. Intern viết post-mortem một dòng: *“SQL là đại số tập, không phải nối chuỗi.”*

Case study TaskFlow (`09_10`) cho thấy một buổi sáng login có thể sập vì đếm sai connection, cardinality metric, UUID collision — tất cả qua một cửa. Bài này bổ sung **lớp tập hợp** dưới SQL, cache, và type system mà case study giả định bạn đã cảm được: mỗi `UNION` là hợp, mỗi `JOIN` là tích có lọc, mỗi Bloom filter là membership xấp xỉ, mỗi `string | number` là hợp tập giá trị.

Cantor và Russell không viết PostgreSQL. Nhưng mỗi lần bạn chọn `UNION` hay `UNION ALL`, đặt Bloom filter trước DB, hay khai báo union type, bạn đang vận hành set theory đã được kiểm chứng — trên dữ liệu thật, tiền thật, email trùng thật.

**Đọc thêm**: [PostgreSQL — UNION, INTERSECT, EXCEPT](https://www.postgresql.org/docs/current/queries-union.html) · [Use The Index, Luke — Anatomy of an Index](https://use-the-index-luke.com/sql/anatomy) · [Wikipedia — Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter)

Chương 9 kết tại đây. **Chương 10: Quan hệ truy hồi** sẽ dạy cách mô hình hóa tăng trưởng theo thời gian — dự báo không chỉ snapshot sáng Thứ Tư với 48.012 email, mà cả quý sau khi subscriber đôi lên và campaign chạy mỗi tuần.

---

## Bài tập thực hành

### Bài tập 1

Bảng `newsletter_subscribers` có 30.000 email distinct. Bảng `loyalty_vip` có 22.000 email distinct. Giao hai tập có **4.000** email trùng. `UNION ALL` cho ra bao nhiêu dòng? `UNION` cho ra bao nhiêu? Giải thích chênh lệch với con số 61.000 trong incident của Linh nếu hai bảng thực tế lớn hơn ví dụ này.

<details>
<summary>Đáp án</summary>

`UNION ALL` giữ mọi bản sao:

$$30{,}000 + 22{,}000 = 52{,}000 \text{ dòng}$$

`UNION` loại trùng (hợp tập):

$$30{,}000 + 22{,}000 - 4{,}000 = 48{,}000 \text{ email distinct}$$

Chênh lệch:

$$52{,}000 - 48{,}000 = 4{,}000$$

— đúng bằng số email nằm trong cả hai tập (bị đếm hai lần khi dùng `UNION ALL`). Incident 61.000 recipients với CRM 48.000 unique cho thấy overlap hoặc nguồn dữ liệu còn nhiều hơn hai bảng đơn giản — có thể thêm nhánh query, staging trùng, hoặc `UNION ALL` nhiều lần — nhưng **cơ chế** giống nhau: bag lớn hơn set vì không dedup.

</details>

### Bài tập 2

Cho ba tập (theo `student_id`):

- $$A$$: đăng ký môn DM — $$|A| = 120$$
- $$B$$: đăng ký môn DB — $$|B| = 95$$
- $$C$$: đăng ký môn AI — $$|C| = 40$$
- $$|A \cap B| = 50$$, $$|A \cap C| = 10$$, $$|B \cap C| = 8$$, $$|A \cap B \cap C| = 5$$

Tính $$|(A \cap B) \setminus C|$$ — tức sinh viên học cả DM và DB nhưng không học AI. Viết SQL tương đương dùng `INTERSECT` và `EXCEPT`.

<details>
<summary>Đáp án</summary>

Học cả DM và DB: $$|A \cap B| = 50$$. Trong đó có 5 người cũng học AI, nên:

$$|(A \cap B) \setminus C| = 50 - 5 = 45$$

SQL:

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

`INTERSECT` = giao; `EXCEPT` = hiệu — map trực tiếp $$(A \cap B) \setminus C$$.

</details>

### Bài tập 3

Bloom filter với $$m = 10{,}000$$ bit và $$k = 3$$ hàm hash. Ước lượng false positive rate khi đã insert $$n = 1{,}000$$ phần tử (dùng xấp xỉ $$p \approx (1 - e^{-kn/m})^k$$). Nếu chấp nhận tối đa 1% false positive, bạn nên làm gì khi $$n$$ tăng lên 5.000 — tăng $$m$$, tăng $$k$$, hay query DB bỏ filter?

<details>
<summary>Đáp án</summary>

Với $$n = 1{,}000$$:

$$\frac{kn}{m} = \frac{3 \times 1{,}000}{10{,}000} = 0.3$$

$$p \approx (1 - e^{-0.3})^3 \approx (1 - 0.741)^3 \approx 0.017$$

— khoảng **1,7%** false positive.

Khi $$n = 5{,}000$$, $$\frac{kn}{m} = 1.5$$ → $$p$$ tăng mạnh (có thể vài chục %). Để giữ ~1% FP:

- **Tăng $$m$$** (nhiều bit hơn) — cách chuẩn; công thức gợi ý $$m \approx -kn/\ln p$$.
- **Tăng $$k$$** có giới hạn — quá nhiều hash làm cả FP và thời gian insert tăng; thường chọn $$k$$ tối ưu theo $$m/n$$.
- **Bỏ filter, query DB mỗi lần** — đúng nhưng đắt I/O; không phải lựa chọn scale.

Bloom filter không bao giờ tạo false negative cho phần tử đã insert — chỉ FP khi chưa insert. Khi FP quá cao, filter vẫn “an toàn” về correctness (chỉ thừa query), nhưng lợi ích cache giảm.

</details>

### Bài tập 4

TypeScript:

```ts
type PaymentId = string;
type LegacyId = number;
type OrderRef = PaymentId | LegacyId;

function charge(ref: OrderRef): void { ... }
```

Python tương đương:

```python
newsletter = {"u1", "u2"}
vip = {"u2", "u3"}
```

(a) `charge(42)` và `charge("pay_abc")` — cái nào hợp lệ? (b) `newsletter | vip` và `newsletter & vip` cho tập nào? (c) Nối ba câu hỏi membership: SQL `IN`, Python `in`, TypeScript type check — điểm chung là gì?

<details>
<summary>Đáp án</summary>

(a) `OrderRef = string ∪ number`. `charge(42)` hợp lệ ($$42 \in \mathbb{Z}$$ subset giá trị number). `charge("pay_abc")` hợp lệ ($$\text{"pay\_abc"} \in \text{string}$$). `charge(true)` **không** hợp lệ — `bool` không thuộc hợp.

(b) `newsletter | vip` = $$\{\text{u1}, \text{u2}, \text{u3}\}$$ (hợp). `newsletter & vip` = $$\{\text{u2}\}$$ (giao).

(c) Cả ba đều hỏi **membership**: giá trị có thuộc tập cho phép không? SQL `WHERE id IN (SELECT ...)` — thuộc tập con kết quả subquery. Python `"u2" in vip` — thuộc tập `vip`. TypeScript từ chối compile khi đối số không thuộc union type — kiểm tra tĩnh trước runtime. Khác thời điểm (compile vs query vs runtime), cùng trực giác tập từ ch04.

</details>

---

## Tóm tắt

Set theory từ Cantor và Russell không nằm trên giấy thi — nó nằm dưới SQL, cache, và type system. **Cantor** đặt nền “phần tử thuộc tập”; **Russell** cảnh báo tự tham chiếu trong định nghĩa tập naive — song song JSON vòng và FK vòng. **Codd** đặt CSDL quan hệ trên tập tuple có cấu trúc.

Trong SQL, mỗi bảng là tập bộ; `WHERE` chọn tập con; `UNION` là hợp (dedup), `UNION ALL` là bag (giữ trùng) — incident email Linh là nhầm hai phép. `INTERSECT` và `EXCEPT` là giao và hiệu; `JOIN` là tích Descartes có lọc khóa — thiếu `ON` là nhân phình dòng, nhầm `INNER`/`LEFT` là mất hoặc thừa phần tử. Python `set` map trực tiếp `|`, `&`, `-`, `in`. **Bloom filter** trả lời membership xấp xỉ: không false negative, có thể false positive — đổi RAM lấy query thừa, cùng họ tư duy hash (`09_07`–`08`) và cardinality xấp xỉ (`09_09`). **Hash table** và **index** tổ chức tập để tra cứu O(1) hoặc range rẻ. **Union type** TypeScript là hợp tập giá trị hợp lệ — type checker là membership tĩnh.

Case study TaskFlow (`09_10`) gom Chương 9 qua cửa login; bài này khép lại bằng lớp tập hợp dưới chân. **Chương 10: Quan hệ truy hồi** sẽ mô hình tăng trưởng theo thời gian — từ snapshot 48.012 email sang dự báo quý sau khi subscriber và campaign scale.