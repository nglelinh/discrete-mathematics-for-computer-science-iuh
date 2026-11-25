---
layout: post
title: "Tập hợp trong CSDL và Lập trình"
categories: chapter04
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Kết nối lý thuyết tập hợp từ Cantor, Russell và Codd với các công cụ thực tế như PostgreSQL, Python set, Bloom filter, bảng băm và hệ thống kiểu trong TypeScript."
---


Nửa đêm ngày sale lớn, hệ thống thương mại điện tử bất ngờ nghẽn cổ chai vì một câu truy vấn lọc khách hàng chưa nhận mã giảm giá quét qua 10 triệu dòng dữ liệu. Khi kỹ sư trưởng thay vòng lặp lồng nhau bằng một phép hiệu tập hợp (`EXCEPT` / `set` difference) có chỉ mục bảng băm, thời gian chạy tụt từ 45 giây xuống còn 12 mili-giây. Đằng sau cú tăng tốc ngoạn mục đó không phải phép màu phần cứng, mà chính là **Lý thuyết Tập hợp** đang vận hành trực tiếp trong SQL, Python, bảng băm, Bloom filter và hệ thống kiểu dữ liệu.

<div class="textbook-epigraph" markdown="1">

"The essence of mathematics is not to make simple things complicated, but to make complicated things simple."

<span class="epigraph-attribution">— Stanislaw Ulam</span>

</div>

Sau bốn mục lý thuyết về định nghĩa tập hợp, phép toán, lực lượng và tích Descartes, mục này đặt các khái niệm đó vào những công cụ quen thuộc trong thực hành như **PostgreSQL**, **Python**, **Redis** và **TypeScript**. Xuyên suốt các lớp hệ thống này đều là cùng những câu hỏi cốt lõi: một phần tử có thuộc tập hợp hay không, và các phép hợp, giao, hiệu vận hành ra sao trên dữ liệu thực tế?

Một lỗi thường gặp trong thực tế là chiến dịch email gửi hai lần cho cùng một địa chỉ chỉ vì truy vấn dùng `UNION ALL` thay cho `UNION`. Đây không phải lỗi của hệ thống gửi thư, mà là sự nhầm lẫn giữa **phép hợp tập hợp** (loại bỏ bản sao) với **phép nối đa tập** (giữ nguyên mọi bản sao). Bài học này khép lại Chương 4 bằng cách nối lý thuyết tập hợp với các công cụ kỹ thuật hằng ngày.

## Bản đồ kiến thức nền: Bốn hiện thân của Lý thuyết Tập hợp trong Hệ thống Phần mềm

1. **SQL & Đại số quan hệ — Bảng dữ liệu là tập hợp (hoặc đa tập)**:
   Các phép toán `UNION` (hợp khử trùng), `UNION ALL` (hợp đa tập giữ trùng), `INTERSECT` (giao), `EXCEPT` (hiệu) và `JOIN` (tích Descartes kèm điều kiện lọc) ánh xạ 1–1 với các phép toán tập hợp cơ bản.

2. **Kiểu `set` & Bảng băm (Hash Table) — Kiểm tra thuộc tập trong $O(1)$**:
   Thay vì duyệt tuyến tính $O(n)$ trên danh sách, bảng băm ánh xạ phần tử sang vị trí ô nhớ để trả lời câu hỏi $x \in S$ trong thời gian trung bình $O(1)$—chìa khóa để loại bỏ trùng lặp và giao/hiệu dữ liệu lớn.

3. **Bloom Filter — Đánh đổi RAM lấy tập xấp xỉ sai số một phía**:
   Khi tập hợp có hàng trăm triệu phần tử không thể nạp hết vào RAM, Bloom filter dùng mảng bit kết hợp nhiều hàm băm để nén tập hợp cực gọn: đảm bảo **không bao giờ âm tính giả** (báo `False` thì chắc chắn $x \notin S$), chỉ chấp nhận tỷ lệ nhỏ dương tính giả.

4. **Hệ thống kiểu dữ liệu (Type System) — Mỗi kiểu là một tập giá trị**:
   Một kiểu như `bool` chính là tập $\{\text{True}, \text{False}\}$, kiểu hợp (*Union Type* `int | str`) là phép hợp tập hợp, còn kiểu tích (*Tuple / Struct*) là tích Descartes $A \times B$—nhờ đó trình biên dịch bắt lỗi logic ngay trước khi chương trình chạy.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Ánh xạ** các toán tử `UNION`, `INTERSECT`, `EXCEPT` trong SQL sang phép hợp, giao và hiệu tập hợp.
- **Phân biệt** `UNION` với `UNION ALL`, cũng như `JOIN` với `CROSS JOIN`.
- **Sử dụng** kiểu `set` trong Python cho các phép hợp, giao, hiệu và kiểm tra thuộc tập (membership).
- **Giải thích** vai trò của Bloom filter và bảng băm (hash table) trong bài toán kiểm tra phần tử thuộc tập.
- **Nhận diện** kiểu hợp (union type) trong hệ thống kiểu như phép hợp các tập giá trị hợp lệ.

**Từ khóa**: membership, `UNION`/`INTERSECT`/`EXCEPT`, Bloom filter, hash table, union type.
</div>

## Cantor, Russell và bài học về định nghĩa tập hợp

Georg Cantor đặt nền móng cho lý thuyết tập hợp hiện đại, và câu hỏi "phần tử có thuộc tập hay không" xuất hiện khắp nơi trong lập trình. Khi viết `SELECT DISTINCT`, hệ quản trị cơ sở dữ liệu loại bỏ các bản ghi trùng lặp trong một tập bộ; khi khai báo `type ID = string | number`, ta mô tả **hợp** của hai tập giá trị hợp lệ.

![Georg Cantor](/discrete-mathematics-for-computer-science-iuh/img/course/Georg_Cantor_1894.jpg)

<p class="textbook-figure-caption" data-figure="4.21">Georg Cantor (1845–1918) — người đặt nền móng cho lý thuyết tập hợp.</p>

Tuy nhiên, Bertrand Russell đã chỉ ra một **nghịch lý** khi định nghĩa tập hợp một cách tự do không ràng buộc: xét tập hợp tất cả các tập hợp **không** chứa chính nó. Nếu tập hợp này chứa chính nó thì theo định nghĩa nó không được chứa chính nó; ngược lại, nếu nó không chứa chính nó thì theo định nghĩa nó lại phải chứa chính nó, dẫn đến mâu thuẫn logic.

![Bertrand Russell](/discrete-mathematics-for-computer-science-iuh/img/course/Bertrand_Russell_photo.jpg)

<p class="textbook-figure-caption" data-figure="4.22">Bertrand Russell — người chỉ ra nghịch lý tự tham chiếu trong lý thuyết tập hợp ngây thơ.</p>

Vấn đề này cũng có ý nghĩa thực tế trong thiết kế phần mềm: các cấu trúc tự tham chiếu không kiểm soát (như JSON lồng nhau vô hạn hoặc khóa ngoại vòng `A → B → A`) dễ dẫn đến trạng thái không nhất quán. Năm 1970, E. F. Codd xây dựng **mô hình quan hệ** dựa trên tập các bộ có cấu trúc rõ ràng (tuple và domain): mỗi bảng là một tập các bộ có lược đồ xác định, và mỗi cột chỉ nhận giá trị trong một miền dữ liệu cố định.

## SQL — Mỗi bảng là một tập hợp

![Cơ sở dữ liệu quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="4.23">Mỗi bảng là một tập các bộ (tuple); truy vấn là thao tác chọn tập con.</p>

Trong mô hình quan hệ, một bảng là tập các bộ (tuple), còn mệnh đề `WHERE` thực hiện phép **chọn** (selection) để lấy ra tập con thỏa mãn điều kiện:

```sql
SELECT *
FROM Employees
WHERE department = 'IT';
```

### Hợp, giao, hiệu trong SQL

```sql
-- Hợp (loại trùng) — đúng ngữ nghĩa tập hợp
SELECT email FROM newsletter_subscribers
UNION
SELECT email FROM loyalty_vip;

-- Đa tập (bag): giữ nguyên mọi bản sao — KHÔNG phải hợp tập hợp
SELECT email FROM newsletter_subscribers
UNION ALL
SELECT email FROM loyalty_vip;
```

Tương tự, `INTERSECT` biểu diễn phép giao và `EXCEPT` biểu diễn phép hiệu (lấy các phần tử thuộc tập bên trái nhưng không thuộc tập bên phải).

<div class="textbook-example" markdown="1">
**Ví dụ**:

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

Diễn giải theo ngôn ngữ tập hợp: truy vấn này tìm các sinh viên học cả hai môn DM và DB, nhưng không học môn AI.
</div>

![Biểu đồ Venn ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="4.24">Hợp, giao và hiệu giữ nguyên ý nghĩa khi chuyển từ sơ đồ Venn sang truy vấn SQL.</p>

### JOIN — Tích Descartes có điều kiện lọc

Phép `JOIN` kết hợp hai bảng theo điều kiện khớp khóa (xem thêm mục 4.4). Nếu thiếu điều kiện `ON`, truy vấn trở thành `CROSS JOIN`, làm kích thước bảng trung gian tăng theo tích số dòng trước khi mệnh đề `WHERE` lọc lại.

```sql
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON e.course_id = c.id;
```

<div class="textbook-definition" markdown="1">
**Lưu ý**: `INNER JOIN` tương ứng với việc giữ các cặp khớp khóa ở cả hai bảng, còn `LEFT JOIN` giữ thêm các bản ghi bên trái không có bản ghi khớp ở bên phải. Nhầm lẫn giữa hai phép này dẫn đến mất dữ liệu hoặc nhân bản dòng — bản chất là sai lệch về ngữ nghĩa tập hợp chứ không phải lỗi cú pháp.
</div>

## Kiểu `set` trong Python — Hợp, giao, hiệu khi xử lý dữ liệu

Trong quy trình khử trùng lặp `user_id` trước khi đồng bộ vào kho dữ liệu:

```python
newsletter = {"u1", "u2", "u3"}
vip = {"u2", "u4"}

all_reach = newsletter | vip       # hợp
both = newsletter & vip            # giao
only_newsletter = newsletter - vip # hiệu

if "u2" in vip:
    ...
```

Các toán tử `|`, `&`, `-` và `in` tương ứng trực tiếp với các phép toán tập hợp ở mục 4.2. Kiểu từ điển (`dict`) lưu cặp khóa–giá trị thay vì tập thuần túy, nhưng phép kiểm tra `if user_id in cache` vẫn là bài toán kiểm tra phần tử thuộc tập khóa.

## Bloom filter — Tập xấp xỉ tiết kiệm bộ nhớ

Một tầng bộ nhớ đệm Redis đặt trước PostgreSQL có thể sử dụng **Bloom filter** để trả lời nhanh câu hỏi "`user_id` này đã từng mua hàng hay chưa?". Thay vì lưu toàn bộ phần tử của tập, Bloom filter chỉ lưu dấu vết trong một mảng bit thông qua nhiều hàm băm:

- Có thể xảy ra **dương tính giả (false positive)**: bộ lọc báo người dùng đã mua dù thực tế chưa, khiến hệ thống truy vấn cơ sở dữ liệu thêm một lần.
- Không xảy ra **âm tính giả (false negative)**: không bao giờ bỏ sót người dùng thực sự đã mua.

![Bloom filter](/discrete-mathematics-for-computer-science-iuh/img/course/Bloom_filter.svg)

<p class="textbook-figure-caption" data-figure="4.25">Bloom filter — kiểm tra phần tử thuộc tập theo xác suất, giảm dung lượng bộ nhớ đổi lấy tỷ lệ dương tính giả có kiểm soát.</p>

Cấu trúc này được dùng phổ biến trong bộ nhớ đệm chống truy vấn rỗng, trình thu thập dữ liệu web (kiểm tra URL đã duyệt hay chưa) và các hệ lưu trữ cần kiểm tra nhanh sự tồn tại mà không giữ toàn bộ tập hợp trong RAM.

## Bảng băm (Hash table) và chỉ mục (Index) — Tổ chức tập hợp để tra cứu nhanh

Bảng băm tổ chức một tập khóa bằng cách ánh xạ từng khóa vào một ngăn chứa (bucket) qua hàm băm và xử lý va chạm khi cần. Đây là nền tảng của `dict`, `set` và nhiều bộ nhớ đệm trong bộ nhớ chính.

![Hash table](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="4.26">Bảng băm — hỗ trợ kiểm tra phần tử thuộc tập với thời gian trung bình O(1).</p>

Trong PostgreSQL, việc tạo chỉ mục trên cột `customer_id` giúp câu lệnh:

```sql
SELECT * FROM Orders WHERE customer_id = 42;
```

truy xuất trực tiếp một **tập con nhỏ** thay vì quét toàn bộ bảng. Về bản chất tập hợp, cả bảng đóng vai trò tập vũ trụ, mệnh đề `WHERE` xác định tập con cần lấy, còn chỉ mục giúp hệ thống thu hẹp phạm vi tìm kiếm.

## Hệ thống kiểu (Type system) — Mỗi kiểu là một tập giá trị

Trong TypeScript:

```ts
type ID = string | number;
```

Kiểu `string | number` chính là **phép hợp** của hai tập giá trị hợp lệ, còn kiểu `bool` là tập $$\{\text{true}, \text{false}\}$$. Trình kiểm tra kiểu (type checker) thực hiện nhiệm vụ xác minh xem giá trị khi chạy có **thuộc** tập giá trị mà kiểu đó cho phép hay không.

![Hợp hai tập](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

<p class="textbook-figure-caption" data-figure="4.27">Union type — phép hợp các tập giá trị hợp lệ trong hệ thống kiểu.</p>

Kiểu hợp phân biệt (discriminated union) như `{ ok: true, data: T } | { ok: false, error: string }` mô tả một **phân hoạch** của tập kết quả: mỗi nhánh là một tập con rời nhau, và hợp của chúng phủ kín toàn bộ không gian trạng thái thành công và lỗi.

### Khung giải thích (nên đọc chậm): Tính tay phép tập hợp SQL, kích thước `JOIN` và một Bloom Filter 10-bit

**Phần A — So sánh các phép toán SQL trên hai bảng nhỏ**

Giả sử bảng `A` (khách mua sách) có 4 dòng `ID = {1, 2, 2, 3}` (có trùng `2`) và bảng `B` (khách mua khóa học) có 3 dòng `ID = {2, 3, 4}`:
- `SELECT ID FROM A UNION SELECT ID FROM B` → Khử trùng như tập hợp chuẩn: $\{1, 2, 3, 4\}$ (**4 dòng**).
- `SELECT ID FROM A UNION ALL SELECT ID FROM B` → Giữ nguyên đa tập: `[1, 2, 2, 3, 2, 3, 4]` (**7 dòng**).
- `A INTERSECT B` → $\{2, 3\}$ (**2 dòng**); `A EXCEPT B` → $\{1\}$ (**1 dòng**).
- `A CROSS JOIN B` → Tích Descartes có đúng $4 \times 3 = \mathbf{12}$ dòng; khi thêm điều kiện `ON A.ID = B.ID` (`INNER JOIN`), ta chỉ giữ các cặp khớp: `(2,2)` xuất hiện 2 lần (do `A` có hai dòng `ID=2`) và `(3,3)` xuất hiện 1 lần → **3 dòng**.

**Phần B — Mô phỏng bằng tay một Bloom Filter $m = 10$ bit**

Khởi tạo mảng 10 bit toàn `0`: `B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` (chỉ số `0..9`), dùng $k = 2$ hàm băm:
$$h_1(x) = (2x + 1) \bmod 10, \qquad h_2(x) = (3x + 2) \bmod 10.$$
1. **Chèn $x = 4$**: $h_1(4) = 9$, $h_2(4) = 14 \bmod 10 = 4$ → Bật bit `4` và `9`.
2. **Chèn $x = 7$**: $h_1(7) = 15 \bmod 10 = 5$, $h_2(7) = 23 \bmod 10 = 3$ → Bật bit `3` và `5`.
   Mảng bit hiện tại: chỉ số `{3, 4, 5, 9}` bằng `1`, các vị trí còn lại bằng `0`.
3. **Truy vấn $x = 6$ (không có trong tập)**: $h_1(6) = 3$ (bit = `1`), $h_2(6) = 0$ (bit = `0`) → Thấy ngay một bit `0`, kết luận **chắc chắn $6 \notin S$** (âm tính chuẩn xác 100%).
4. **Truy vấn $x = 2$ (không có trong tập)**: $h_1(2) = 5$ (bit = `1`), $h_2(2) = 8$ (bit = `0`) → Chắc chắn $2 \notin S$.
5. **Truy vấn $x = 9$ (không có trong tập)**: $h_1(9) = 19 \bmod 10 = 9$ (bit = `1`), $h_2(9) = 29 \bmod 10 = 9$ (bit = `1`) → Cả hai bit đều tình cờ đã bật từ trước nên bộ lọc báo "có thể thuộc $S$" — đây chính là một **dương tính giả (false positive)** được tạo ra do đụng độ băm trên mảng bit hữu hạn!

## Bài tập thực hành

### Bài tập 1: `UNION` và `UNION ALL`

Bảng `newsletter_subscribers` có 30.000 địa chỉ email phân biệt và bảng `loyalty_vip` có 22.000 địa chỉ email phân biệt. Phần giao giữa hai tập có **4.000** email trùng nhau. Hỏi `UNION ALL` và `UNION` lần lượt trả về bao nhiêu dòng?

<details>
<summary>Đáp án</summary>

`UNION ALL` trả về $$30{,}000 + 22{,}000 = 52{,}000$$ dòng (giữ nguyên các bản sao).

`UNION` trả về $$30{,}000 + 22{,}000 - 4{,}000 = 48{,}000$$ email phân biệt (theo nguyên lý bao hàm–loại trừ ở mục 4.3).

Phần chênh lệch 4.000 dòng chính là số địa chỉ email bị lặp hai lần khi dùng `UNION ALL`.

</details>

### Bài tập 2: `INTERSECT` và `EXCEPT`

Cho $$\vert A\vert =120$$, $$\vert B\vert =95$$, $$\vert C\vert =40$$, $$\vert A \cap B\vert =50$$, $$\vert A \cap C\vert =10$$, $$\vert B \cap C\vert =8$$ và $$\vert A \cap B \cap C\vert =5$$. Tính $$\vert (A \cap B) \setminus C\vert$$ và viết truy vấn SQL tương đương.

<details>
<summary>Đáp án</summary>

$$\vert (A \cap B) \setminus C\vert = \vert A \cap B\vert - \vert A \cap B \cap C\vert = 50 - 5 = 45$$.

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

</details>

### Bài tập 3: Phép toán tập hợp trong Python

```python
dm = {"s1", "s2", "s3"}
db = {"s2", "s4"}
ai = {"s3", "s5"}
```

Tính kết quả của `(dm | db) - ai` và `dm & db & ai` rồi viết lại bằng ký hiệu tập hợp.

<details>
<summary>Đáp án</summary>

- `dm | db` $$= \{\text{s1}, \text{s2}, \text{s3}, \text{s4}\}$$, do đó `(dm | db) - ai` $$= \{\text{s1}, \text{s2}, \text{s4}\}$$.
- `dm & db` $$= \{\text{s2}\}$$, nhưng `"s2"` không thuộc `ai`, nên `dm & db & ai` $$= \emptyset$$ (tập rỗng, không có phần tử nào thuộc cả ba tập).

</details>

### Bài tập 4: Kiểm tra thuộc tập ở ba lớp hệ thống

So sánh ba thao tác kiểm tra thuộc tập sau: câu lệnh SQL `WHERE id IN (SELECT ...)`, biểu thức Python `"u2" in vip`, và việc TypeScript báo lỗi khi gọi `charge(true)` với kiểu tham số `OrderRef = string | number`. Điểm chung giữa chúng là gì?

<details>
<summary>Đáp án</summary>

Cả ba đều kiểm tra cùng một câu hỏi: một giá trị có **thuộc** tập hợp cho phép hay không. Chúng chỉ khác nhau ở thời điểm kiểm tra (lúc biên dịch, lúc truy vấn cơ sở dữ liệu hay lúc thực thi chương trình), nhưng đều dựa trên cùng một khái niệm tập hợp của Chương 4.

</details>

## Xem thêm / Video gợi ý

- [PostgreSQL — UNION, INTERSECT, EXCEPT](https://www.postgresql.org/docs/current/queries-union.html)
- [Use The Index, Luke — Anatomy of an Index](https://use-the-index-luke.com/sql/anatomy)
- [Wikipedia — Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter)

## Tóm tắt

- **Cantor** đặt nền móng cho khái niệm phần tử thuộc tập; **Russell** chỉ ra nguy cơ của tự tham chiếu không kiểm soát; **Codd** xây dựng cơ sở dữ liệu quan hệ dựa trên tập các bộ có cấu trúc.
- Trong SQL: bảng tương ứng tập các bộ; `WHERE` chọn tập con; `UNION` là phép hợp (loại trùng) khác với `UNION ALL` (đa tập); `INTERSECT` và `EXCEPT` là phép giao và hiệu; `JOIN` là tích Descartes có lọc.
- Kiểu `set` trong Python dùng trực tiếp `|`, `&`, `-`, `in` cho các phép toán tập hợp.
- **Bloom filter** và **bảng băm** hỗ trợ kiểm tra phần tử thuộc tập với sự đánh đổi giữa bộ nhớ, tốc độ và độ chính xác.
- **Union type** biểu diễn phép hợp các tập giá trị hợp lệ, giúp trình biên dịch kiểm tra tĩnh tính hợp lệ của dữ liệu.

Chương 4 kết thúc tại đây. **Chương 5: Quan hệ** sẽ phát triển khái niệm tích Descartes (mục 4.4) để mô hình hóa các liên kết giữa đối tượng trong cơ sở dữ liệu, đồ thị và hệ thống phân quyền.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=76v3gRns28U">Basics of Relational Algebra</a> — Neso Academy, tiếng Anh. Giới thiệu mô hình bảng như tập các bộ và các phép đại số quan hệ.
- <a href="https://www.youtube.com/watch?v=4TlCToZZ5gA">SET OPERATIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Các phép hợp, giao, hiệu tương ứng trực tiếp với SQL và kiểu tập trong lập trình.
- <a href="https://www.youtube.com/watch?v=cORV6VX2Jnw">Theory Behind SQL Databases: Relational Algebra</a> — Jacob Schrum, tiếng Anh. Giải thích cơ sở toán học của truy vấn SQL trên nền lý thuyết tập hợp.
