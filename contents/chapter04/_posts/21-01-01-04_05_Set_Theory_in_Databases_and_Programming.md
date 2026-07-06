---
layout: post
title: "Tập hợp trong CSDL và Lập trình"
categories: chapter04
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Từ Cantor và Russell đến PostgreSQL, Python set và Bloom filter — mỗi lớp đều hỏi cùng một câu: phần tử có thuộc tập không, và hợp–giao–hiệu ra sao khi dữ liệu…"
---

<div class="textbook-epigraph" markdown="1">

"The essence of mathematics is not to make simple things complicated, but to make complicated things simple."

<span class="epigraph-attribution">— Stanislaw Ulam</span>

</div>

Sau bốn mục lý thuyết — định nghĩa tập, phép toán, lực lượng, tích Descartes — chúng ta đặt cùng một câu hỏi dưới chân **PostgreSQL**, **Python**, **Redis** và **TypeScript**: phần tử có **thuộc** tập không? Hợp, giao, hiệu ra sao khi dữ liệu chạy thật trên production?

Một lỗi kinh điển: campaign email gửi **hai lần** cho cùng địa chỉ vì dùng `UNION ALL` thay vì `UNION`. Không phải bug ESP — là nhầm **hợp tập** (loại trùng) với **nối bag** (giữ mọi bản sao). Bài học này khép Chương 4 bằng cách nối lý thuyết tập hợp với công cụ bạn dùng hàng ngày.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Ánh xạ** `UNION`, `INTERSECT`, `EXCEPT` trong SQL sang hợp, giao, hiệu tập.
- **Phân biệt** `UNION` và `UNION ALL`, `JOIN` và `CROSS JOIN`.
- **Sử dụng** `set` Python cho hợp, giao, hiệu và membership.
- **Giải thích** ý nghĩa Bloom filter và hash table như cấu trúc membership.
- **Nhận diện** union type trong type system là hợp tập giá trị hợp lệ.

**Từ khóa**: membership, `UNION`/`INTERSECT`/`EXCEPT`, Bloom filter, hash table, union type.
</div>

## Cantor, Russell và bài học về định nghĩa tập

Georg Cantor đặt nền lý thuyết tập hợp hiện đại — mọi câu hỏi "có thuộc tập không" trong code đều mượn trực giác ông xây dựng. Khi viết `SELECT DISTINCT`, engine loại phần tử trùng trong một tập bộ; khi khai báo `type ID = string | number`, ta mô tả **hợp** hai tập giá trị hợp lệ.

![Georg Cantor](/discrete-mathematics-for-computer-science-iuh/img/course/Georg_Cantor_1894.jpg)

<p class="textbook-figure-caption" data-figure="4.21">Georg Cantor (1845–1918) — nền móng lý thuyết tập hợp.</p>

Bertrand Russell chỉ ra **nghịch lý**: xét tập mọi tập **không** chứa chính nó. Tập đó có chứa chính nó không? Có → theo định nghĩa không được chứa; không → theo định nghĩa phải chứa. Logic bế tắc.

![Bertrand Russell](/discrete-mathematics-for-computer-science-iuh/img/course/Bertrand_Russell_photo.jpg)

<p class="textbook-figure-caption" data-figure="4.22">Bertrand Russell — cảnh báo nguy hiểm của tự tham chiếu trong định nghĩa tập naive.</p>

Đây không chỉ là tranh luận triết học. Schema "tập mọi thứ" không kiểm soát **tự tham chiếu** dễ mâu thuẫn — giống JSON lồng vô hạn, hay khóa ngoại vòng `A → B → A`. E. F. Codd (1970) đặt **mô hình quan hệ** trên tập bộ có cấu trúc (tuple, domain), tránh "tập của mọi tập" kiểu naive. Mỗi bảng là tập các bộ có kiểu; mỗi cột thuộc một domain cố định.

## SQL — mỗi bảng là một tập

![Cơ sở dữ liệu quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="4.23">Mỗi bảng là tập các bộ (tuple); truy vấn là phép chọn tập con.</p>

Một bảng = tập các tuple. `WHERE` = **selection** — lấy tập con thỏa điều kiện:

```sql
SELECT *
FROM Employees
WHERE department = 'IT';
```

### Hợp, giao, hiệu trong SQL

```sql
-- Hợp (loại trùng) — đúng semantics tập hợp
SELECT email FROM newsletter_subscribers
UNION
SELECT email FROM loyalty_vip;

-- Bag: giữ mọi bản sao — KHÔNG phải hợp tập
SELECT email FROM newsletter_subscribers
UNION ALL
SELECT email FROM loyalty_vip;
```

`INTERSECT` = giao. `EXCEPT` = hiệu (phần tử thuộc tập trái nhưng không thuộc tập phải).

<div class="textbook-example" markdown="1">
**Ví dụ**:

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

Đọc bằng ngôn ngữ tập: sinh viên học cả DM và DB, nhưng không học AI.
</div>

![Biểu đồ Venn ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="4.24">Hợp, giao, hiệu — cùng hình ảnh trên giấy và trong SQL.</p>

### JOIN — tích Descartes có bộ lọc

`JOIN` kết hợp hai bảng theo khóa khớp — xem thêm mục 4.4. Thiếu điều kiện `ON` tương đương `CROSS JOIN`: tích Descartes phình to trước khi `WHERE` kịp cắt.

```sql
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON e.course_id = c.id;
```

<div class="textbook-definition" markdown="1">
**Lưu ý**: `INNER JOIN` ≈ giao có điều kiện trên khóa; `LEFT JOIN` giữ phần tử "mồ côi" bên trái. Nhầm hai phép → mất dòng hoặc nhân dòng — lỗi **tập**, không phải lỗi cú pháp.
</div>

## Python `set` — hợp giao hiệu trong ETL

Pipeline dedup `user_id` trước khi sync warehouse:

```python
newsletter = {"u1", "u2", "u3"}
vip = {"u2", "u4"}

all_reach = newsletter | vip       # hợp
both = newsletter & vip            # giao
only_newsletter = newsletter - vip # hiệu

if "u2" in vip:
    ...
```

`|`, `&`, `-`, `in` — ánh xạ trực tiếp từ mục 4.2. Dictionary không phải tập thuần (key–value), nhưng `if user_id in cache` là câu hỏi **membership** trên tập key.

## Bloom filter — tập xấp xỉ khi bộ nhớ là tiền

Redis layer trước PostgreSQL có thể dùng **Bloom filter** để trả lời nhanh: "`user_id` này đã từng mua chưa?" Bloom filter không lưu trọn tập; nó lưu dấu vết bit qua vài hàm hash.

- **False positive** có thể — filter nghĩ user đã mua, query DB thừa một lần.
- **False negative** không có — không bỏ sót người thật sự đã mua.

![Bloom filter](/discrete-mathematics-for-computer-science-iuh/img/course/Bloom_filter.svg)

<p class="textbook-figure-caption" data-figure="4.25">Bloom filter — membership xác suất, đổi RAM lấy false positive có kiểm soát.</p>

Ứng dụng: cache negative lookup, web crawler ("URL đã crawl chưa?"), storage engine — mọi nơi cần trả lời "có trong tập không?" mà không mang cả tập theo.

## Hash table và index — tổ chức tập để tra cứu

Hash table: tập keys, ánh xạ key → bucket, xử lý collision. Nền của `dict`, `set`, in-memory cache.

![Hash table](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="4.26">Hash table — tra cứu membership trung bình O(1).</p>

Index trên `customer_id` trong PostgreSQL giúp:

```sql
SELECT * FROM Orders WHERE customer_id = 42;
```

lấy **tập con nhỏ** thay vì quét toàn bộ bảng. Trực giác vẫn là tập: toàn bộ bảng là universe; `WHERE` chọn subset; index giúp engine không duyệt universe.

## Type system — mỗi type là một tập giá trị

TypeScript:

```ts
type ID = string | number;
```

`string | number` = **hợp** hai tập giá trị hợp lệ. `bool` = $$\{\text{true}, \text{false}\}$$. Type checker hỏi: giá trị runtime có **thuộc** tập mà type cho phép không?

![Hợp hai tập](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

<p class="textbook-figure-caption" data-figure="4.27">Union type — hợp tập giá trị trong type system.</p>

Discriminated union (`{ ok: true, data: T } | { ok: false, error: string }`) mô tả **phân hoạch** tập kết quả — mỗi nhánh là tập con rời nhau, hợp lại là toàn bộ không gian lỗi/thành công. Đó là phân hoạch tập từ mục 4.1, chỉ đổi tên thành "algebraic data type".

## Bài tập thực hành

### Bài tập 1: UNION vs UNION ALL

Bảng `newsletter_subscribers` có 30.000 email distinct. Bảng `loyalty_vip` có 22.000 email distinct. Giao hai tập có **4.000** email trùng. `UNION ALL` cho ra bao nhiêu dòng? `UNION` cho ra bao nhiêu?

<details>
<summary>Đáp án</summary>

`UNION ALL`: $$30{,}000 + 22{,}000 = 52{,}000$$ dòng (giữ trùng).

`UNION`: $$30{,}000 + 22{,}000 - 4{,}000 = 48{,}000$$ email distinct (nguyên lý bao hàm–loại trừ, mục 4.3).

Chênh lệch 4.000 = số email bị đếm hai lần khi dùng `UNION ALL`.

</details>

### Bài tập 2: INTERSECT và EXCEPT

Cho $$|A|=120$$, $$|B|=95$$, $$|C|=40$$, $$|A \cap B|=50$$, $$|A \cap C|=10$$, $$|B \cap C|=8$$, $$|A \cap B \cap C|=5$$. Tính $$|(A \cap B) \setminus C|$$. Viết SQL tương đương.

<details>
<summary>Đáp án</summary>

$$|(A \cap B) \setminus C| = 50 - 5 = 45$$.

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

</details>

### Bài tập 3: Python set

```python
dm = {"s1", "s2", "s3"}
db = {"s2", "s4"}
ai = {"s3", "s5"}
```

Tính `(dm | db) - ai` và `dm & db & ai` bằng ký hiệu tập.

<details>
<summary>Đáp án</summary>

`dm | db` = $$\{\text{s1}, \text{s2}, \text{s3}, \text{s4}\}$$; trừ `ai` → $$\{\text{s1}, \text{s2}, \text{s4}\}$$.

`dm & db & ai` = $$\{\text{s3}\}$$ (chỉ s3 thuộc cả ba tập).

</details>

### Bài tập 4: Membership ba tầng

So sánh ba câu hỏi membership: SQL `WHERE id IN (SELECT ...)`, Python `"u2" in vip`, TypeScript từ chối `charge(true)` khi `OrderRef = string | number`. Điểm chung là gì?

<details>
<summary>Đáp án</summary>

Cả ba đều hỏi: giá trị có **thuộc** tập cho phép không? Khác thời điểm (compile time vs query vs runtime), cùng trực giác tập từ Chương 4.

</details>

## Xem thêm / Video gợi ý

- [PostgreSQL — UNION, INTERSECT, EXCEPT](https://www.postgresql.org/docs/current/queries-union.html)
- [Use The Index, Luke — Anatomy of an Index](https://use-the-index-luke.com/sql/anatomy)
- [Wikipedia — Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter)

## Tóm tắt

- **Cantor** đặt nền membership; **Russell** cảnh báo tự tham chiếu; **Codd** đặt CSDL quan hệ trên tập tuple có cấu trúc.
- SQL: bảng = tập bộ; `WHERE` = chọn tập con; `UNION` = hợp (dedup), `UNION ALL` = bag; `INTERSECT`/`EXCEPT` = giao/hiệu; `JOIN` = tích có lọc.
- Python `set`: `|`, `&`, `-`, `in` map trực tiếp phép toán tập.
- **Bloom filter** và **hash table** trả lời membership với trade-off bộ nhớ/thời gian.
- **Union type** là hợp tập giá trị hợp lệ — type checker là membership tĩnh.

Chương 4 kết tại đây. **Chương 5: Quan hệ** sẽ phát triển tích Descartes (mục 4.4) thành công cụ mô hình hóa liên kết giữa đối tượng — từ CSDL đến đồ thị và hệ thống phân quyền.