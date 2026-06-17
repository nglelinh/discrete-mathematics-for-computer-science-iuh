---
layout: post
title: "Lý thuyết Tập hợp trong Cơ sở Dữ liệu và Lập trình"
categories: chapter04
date: 2021-01-01
order: 5
required: false
lang: en
---

Nhiều sinh viên gặp lý thuyết tập hợp và nghĩ rằng đó là phần “rất toán”,
khá xa thực tế phần mềm.
Nhưng nếu nhìn kỹ,
ta sẽ thấy set theory nằm ngay dưới chân database,
trong cấu trúc dữ liệu,
trong type systems,
trong hashing,
và cả trong cách ngôn ngữ lập trình hiểu “một tập các giá trị hợp lệ”.

Từ Cantor và những cuộc tranh cãi dữ dội ở thế kỷ XIX,
qua Russell’s paradox,
đến SQL joins,
Python sets,
Bloom filters,
và type theory,
bài học này cho thấy tập hợp không phải phần mở đầu khô khan.
Nó là một lớp tư duy tổ chức thế giới số.

---

## Phần 1: Lịch sử — Cantor, vô hạn, và nghịch lý

### 1.1. Cantor làm điều tưởng như không thể

Georg Cantor bước vào lịch sử toán học khi ông dám đối đầu với khái niệm vô hạn.
Ông không chỉ nói “vô hạn tồn tại”.
Ông hỏi:
liệu các loại vô hạn có kích thước khác nhau không?

Đó là câu hỏi làm rung chuyển nền tảng toán học.
Khi Cantor định nghĩa tập hợp một cách hệ thống,
ông biến set theory thành ngôn ngữ chung để nói về số,
hàm,
quan hệ,
và cấu trúc toán học.

![Georg Cantor — cha đẻ lý thuyết tập hợp](https://commons.wikimedia.org/wiki/Special:FilePath/Georg_Cantor_1894.jpg?width=300)

*Hình 4.31: Georg Cantor (1845–1918) — người đặt nền móng cho lý thuyết tập hợp hiện đại và khái niệm về các loại vô hạn.*

### 1.2. Tranh cãi không chỉ học thuật

Nhiều nhà toán học đương thời phản đối Cantor.
Họ cho rằng làm việc với vô hạn theo kiểu đó là nguy hiểm,
thậm chí phi lý.

Nhưng chính sự táo bạo này lại mở ra khả năng mô hình hóa mọi đối tượng toán học như những tập hợp có cấu trúc.
Sau này,
khoa học máy tính thừa hưởng trực tiếp ngôn ngữ đó.

### 1.3. Russell’s paradox và bài học về thiết kế hệ thống

Sau Cantor,
Bertrand Russell nêu nghịch lý nổi tiếng:
xét tập hợp của mọi tập hợp không chứa chính nó.
Liệu tập hợp này có chứa chính nó không?

Nếu có,
thì theo định nghĩa nó không được chứa chính nó.
Nếu không,
thì theo định nghĩa nó phải chứa chính nó.

Đây không chỉ là cú sốc cho logic.
Nó còn là lời cảnh báo rất hiện đại:
thiết kế hệ thống khái niệm mà không kiểm soát tự tham chiếu dễ dẫn tới mâu thuẫn.

![Bertrand Russell — nghịch lý tập hợp](https://commons.wikimedia.org/wiki/Special:FilePath/Bertrand_Russell_photo.jpg?width=400)

*Hình 4.32: Bertrand Russell (1872–1970) — nghịch lý Russell cảnh báo nguy hiểm của tự tham chiếu trong định nghĩa tập hợp.*

---

## Phần 2: Set operations sống trong SQL mỗi ngày

### 2.1. SELECT-FROM-WHERE là cách chọn tập con

![Cơ sở dữ liệu quan hệ](https://commons.wikimedia.org/wiki/Special:FilePath/Database.svg?width=500)

*Hình 4.33: Mô hình quan hệ — mỗi bảng là một tập các bộ (tuple); truy vấn SQL là phép chọn tập con.*

Một bảng database có thể được xem như tập các bộ dữ liệu (tuples).
Khi bạn viết query,
bạn đang chọn ra tập con thỏa điều kiện.

```sql
SELECT *
FROM Employees
WHERE department = 'IT';
```

Về bản chất,
đây là phép **selection** trên một tập.

### 2.2. UNION, INTERSECT, EXCEPT

SQL hiện đại hỗ trợ trực tiếp các phép set operations:

```sql
SELECT email FROM Customers
UNION
SELECT email FROM Leads;
```

Ở đây,
`UNION` lấy hợp của hai tập kết quả.

Tương tự,
`INTERSECT` là giao,
`EXCEPT` là hiệu.

Điều thú vị là:
nhiều tối ưu hóa query trong database engine
thực chất dựa vào các đẳng thức kiểu đại số tập hợp.

### 2.3. JOIN nhìn như quan hệ, nhưng tư duy tập hợp vẫn ở lõi

Một phép `JOIN` thường được giải thích bằng relational algebra,
nhưng trực giác set theory vẫn rất mạnh:

- mỗi bảng là tập bộ,
- join tạo tập các bộ kết hợp phù hợp,
- điều kiện join đóng vai trò bộ lọc trên tích Descartes.

![Phép JOIN trong SQL](https://commons.wikimedia.org/wiki/Special:FilePath/Square_join.png?width=500)

*Hình 4.34: Phép JOIN — kết hợp hai bảng theo khóa khớp, tư duy tập hợp giúp hiểu cấu trúc phía sau cú pháp.*

```sql
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON e.course_id = c.id;
```

Nếu không có tư duy tập hợp,
nhiều sinh viên chỉ thấy đây là cú pháp.
Khi có tư duy tập hợp,
họ thấy được cấu trúc phía sau.

---

## Phần 3: Python sets, dictionaries, Bloom filters

### 3.1. `set` trong Python là lý thuyết tập hợp ở dạng thực dụng

Python có kiểu `set` rất quen thuộc:

```python
visited = {"A", "B", "C"}
visited.add("D")

if "B" in visited:
    print("Seen")
```

Các phép toán như:

- `|` cho union,
- `&` cho intersection,
- `-` cho difference,
- `in` cho membership,

đều phản chiếu gần như trực tiếp từ set theory.

![Python set và các phép toán tập hợp](https://source.unsplash.com/800x600/?python,programming,code)

*Hình 4.35: Kiểu `set` trong Python — union `|`, intersection `&`, difference `-` ánh xạ trực tiếp từ lý thuyết tập hợp.*

### 3.2. Dictionary và membership

Dictionary không phải tập hợp thuần túy,
nhưng nó dựa mạnh vào tư duy key uniqueness và membership checking.

Khi bạn hỏi:

```python
if user_id in cache:
    ...
```

đó là câu hỏi:
phần tử này có thuộc tập key đã lưu không?

### 3.3. Bloom filter: chấp nhận sai số để đổi lấy tốc độ

Bloom filter là cấu trúc dữ liệu rất đẹp:

- kiểm tra membership cực nhanh,
- dùng rất ít bộ nhớ,
- cho false positives,
- nhưng không cho false negatives.

Nó không lưu trọn tập hợp theo nghĩa thông thường.
Nó lưu “dấu vết” để trả lời gần đúng câu hỏi thuộc-tập.

Ứng dụng của Bloom filter có trong:

- cache systems,
- distributed databases,
- web crawlers,
- networking,
- storage engines.

![Bloom filter — kiểm tra membership xác suất](https://commons.wikimedia.org/wiki/Special:FilePath/Bloom_filter.svg?width=640)

*Hình 4.36: Bloom filter — cấu trúc xác suất kiểm tra "phần tử có thuộc tập không" với ít bộ nhớ, chấp nhận false positive.*

---

## Phần 4: Hashing, indexing, và tổ chức dữ liệu lớn

### 4.1. Hash table như cách tổ chức tập các phần tử

Hash table cho phép tra cứu rất nhanh bằng cách biến key thành vị trí lưu trữ.
Đây là lý do dictionary,
set,
cache,
và nhiều index in-memory hoạt động hiệu quả.

Ở mức trừu tượng,
ta vẫn đang làm việc với:

- tập keys,
- ánh xạ keys sang buckets,
- kiểm tra membership,
- xử lý va chạm.

![Hash table — tra cứu membership nhanh](https://commons.wikimedia.org/wiki/Special:FilePath/Hash_table_simple_999.svg?width=640)

*Hình 4.37: Hash table — ánh xạ key sang bucket để tra cứu O(1) trung bình; nền tảng của `dict`, `set`, và cache.*

### 4.2. Database indexing

Trong database,
index giúp hệ quản trị không phải quét cả bảng.

Khi truy vấn:

```sql
SELECT * FROM Orders WHERE customer_id = 42;
```

index giúp lấy ra tập rất nhỏ các bản ghi liên quan,
thay vì duyệt toàn bộ tập orders.

Tập hợp ở đây không còn chỉ là khái niệm sách giáo khoa.
Nó là vấn đề chi phí I/O,
latency,
và tiền vận hành thật.

---

## Phần 5: Type systems và tập các giá trị hợp lệ

### 5.1. Mỗi type có thể xem như một tập giá trị

Trong nhiều ngôn ngữ lập trình,
ta có thể hiểu một type như tập hợp các giá trị hợp lệ của nó.

Ví dụ:

- `bool` là tập `{true, false}`,
- `int` là tập các số nguyên trong miền biểu diễn,
- `string` là tập các chuỗi hợp lệ,
- `Option<T>` là tập `{None} ∪ T`.

Góc nhìn này rất mạnh,
vì nó làm rõ tại sao type checking lại giống bài toán membership:
giá trị này có thuộc tập giá trị mà type cho phép hay không?

### 5.2. Union types và intersection types

Trong các ngôn ngữ hiện đại như TypeScript,
ta gặp:

- union types,
- intersection types,
- subtype relations.

Những ý tưởng này rất tự nhiên nếu ta nghĩ bằng ngôn ngữ tập hợp.

![Union type — hợp của hai tập giá trị](https://commons.wikimedia.org/wiki/Special:FilePath/Union_of_sets_A_and_B.svg?width=500)

*Hình 4.38: Union type `string | number` trong TypeScript — hợp của hai tập giá trị hợp lệ, tư duy tập hợp trong type system.*

Ví dụ:

```ts
type ID = string | number;
```

đó là hợp của hai tập giá trị.

### 5.3. Set theory như lớp trực giác cho semantics

Nhiều lĩnh vực sâu hơn như denotational semantics,
domain theory,
hay type theory
không phải lúc nào cũng là set theory thuần túy.
Nhưng trực giác tập hợp vẫn giúp sinh viên bước vào những vùng này dễ hơn nhiều.

---

## Phần 6: Tương lai — dữ liệu lớn nhưng cấu trúc vẫn cần rõ

Khi hệ thống ngày càng lớn,
ta càng cần mô hình hóa dữ liệu rõ ràng.

Set theory vẫn sống trong:

- query optimizers,
- data pipelines,
- access control policies,
- static type systems,
- distributed caches,
- probabilistic data structures.

Điều thay đổi chỉ là quy mô.
Nguyên lý nền thì rất cũ,
và rất bền.

---

## Kết luận

Lý thuyết tập hợp không chỉ là phần “căn bản để học tiếp”.
Nó là ngôn ngữ tổ chức dữ liệu,
điều kiện,
kiểu,
và membership trong gần như mọi hệ thống tính toán.

Từ Cantor đến SQL,
từ Russell’s paradox đến Bloom filters,
từ hợp-giao-hiệu đến union types,
tập hợp đã đi từ tranh luận triết học sang hạ tầng của software hiện đại.

Nếu hiểu tập hợp thật sâu,
ta không chỉ giải bài toán tốt hơn.
Ta còn nhìn được cấu trúc ẩn sau rất nhiều công nghệ quen thuộc.

---

## Bài tập thực hành

### Bài tập 1: Viết truy vấn tập hợp

Viết câu SQL dùng UNION, INTERSECT, EXCEPT để tìm sinh viên học cả hai môn "DM" và "DB" nhưng không học "AI".

<details>
<summary>Đáp án</summary>

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI')
```

</details>

### Bài tập 2: Python set operations

Cho hai tập `A = {1,2,3,4}` và `B = {3,4,5,6}`, tính:
- `A | B`
- `A & B`
- `A - B`

<details>
<summary>Đáp án</summary>

- Union: `{1,2,3,4,5,6}`
- Intersection: `{3,4}`
- Difference: `{1,2}`

</details>

### Bài tập 3: Mô hình hóa dữ liệu

Mô tả quan hệ giữa các bảng `students`, `courses`, `enrollments` dưới dạng tập hợp và quan hệ.

<details>
<summary>Đáp án</summary>

- `students`, `courses` là hai tập.
- `enrollments` là một quan hệ (relation) giữa hai tập (bảng nối).

</details>

## Tóm tắt

Tập hợp đã đi từ tranh luận triết học sang hạ tầng của software hiện đại. Nếu hiểu tập hợp thật sâu, ta không chỉ giải bài toán tốt hơn mà còn nhìn được cấu trúc ẩn sau rất nhiều công nghệ quen thuộc.
