---
layout: post
title: "Tích Descartes và Cặp có thứ tự"
categories: chapter04
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Sau hợp, giao và hiệu, bước tiếp theo là kết hợp phần tử từ hai tập thành cặp có thứ tự — nền tảng của quan hệ, bảng SQL và mọi mô hình (người, khóa)…"
---

<div class="textbook-epigraph" markdown="1">

"Each problem that I solved became a rule, which served afterwards to solve other problems."

<span class="epigraph-attribution">— René Descartes</span>

</div>

Ở các mục trước, chúng ta đã làm việc với **tập hợp** — gom phần tử không quan tâm thứ tự. Nhưng trong khoa học máy tính, thứ tự thường **quan trọng**: tọa độ $$(x, y)$$ trên màn hình, cặp `(user_id, role)` trong bảng phân quyền, hay bộ `(sinh_viên, môn_học, điểm)` trong cơ sở dữ liệu. Khi cần kết hợp phần tử từ hai tập theo **cặp có thứ tự**, ta dùng **tích Descartes** (Cartesian product). Đây là cầu nối trực tiếp sang **quan hệ** ở Chương 5: mỗi quan hệ là một tập con của tích Descartes.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** cặp có thứ tự $$(a,b)$$ với tập hai phần tử $$\{a,b\}$$.
- **Định nghĩa** và **tính** tích Descartes $$A \times B$$.
- **Áp dụng** công thức $$\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$$.
- **Chứng minh** một số tính chất cơ bản của tích (giao, phân phối hạn chế).
- **Nhận diện** `CROSS JOIN` trong SQL và mối liên hệ với quan hệ.

**Từ khóa**: cặp có thứ tự (ordered pair), tích Descartes (Cartesian product), quan hệ (relation), `CROSS JOIN`.
</div>

## Cặp có thứ tự

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Cặp có thứ tự** (ordered pair) $$(a,b)$$ gồm hai thành phần theo thứ tự cố định: $$a$$ là **thành phần đầu**, $$b$$ là **thành phần sau**.
</div>

Hai cặp bằng nhau khi và chỉ khi từng thành phần tương ứng bằng nhau:

<div class="textbook-equation" markdown="1">
$$(a,b) = (c,d) \iff a = c \land b = d.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(3, 5) \neq (5, 3)$$ — thứ tự khác nhau.
- $$\{3, 5\} = \{5, 3\}$$ — tập hợp không quan tâm thứ tự.
- Trong Python, `tuple` là cặp/bộ có thứ tự: `(3, 5) != (5, 3)`; `set` thì không.
</div>

Trong lập trình, `dict` dùng cặp khóa–giá trị; `JOIN` trong SQL ghép hai bản ghi thành một bộ có thứ tự cột. Nhầm cặp có thứ tự với tập là nguồn lỗi phổ biến khi mô hình hóa dữ liệu.

## Tích Descartes

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho hai tập $$A$$ và $$B$$. **Tích Descartes** $$A \times B$$ là tập mọi cặp có thứ tự $$(a,b)$$ với $$a \in A$$ và $$b \in B$$:

$$A \times B = \{(a,b) \mid a \in A \land b \in B\}.$$
</div>

![Tích Descartes A × B](/discrete-mathematics-for-computer-science-iuh/img/course/Cartesian_Product_qtl1.svg)

<p class="textbook-figure-caption" data-figure="4.19">Tích Descartes $$A \times B$$ — mỗi điểm tương ứng một cặp $$(a,b)$$.</p>

<div class="textbook-example" markdown="1">
**Ví dụ**: $$A = \{1, 2\}$$, $$B = \{x, y\}$$.

$$A \times B = \{(1,x), (1,y), (2,x), (2,y)\}.$$

$$\lvert A \times B \rvert = 2 \times 2 = 4.$$
</div>

Ký hiệu $$\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$$ là mặt phẳng tọa độ — mỗi điểm $$(x,y)$$ là cặp số thực. Trong UI, vị trí pixel $$(row, col)$$ cũng là phần tử của tích $$\mathbb{N} \times \mathbb{N}$$.

### Lực lượng tích

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$A,B$$ hữu hạn thì

$$\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert.$$
</div>

**Chứng minh (đếm trực tiếp)**: Với mỗi $$a \in A$$ (có $$\lvert A \rvert$$ lựa chọn), ta chọn $$b \in B$$ ($$\lvert B \rvert$$ lựa chọn). Theo nguyên lý nhân, số cặp là $$\lvert A \rvert \cdot \lvert B \rvert$$. ∎

<div class="textbook-example" markdown="1">
**Ví dụ (cảnh báo hiệu năng)**:

- Bảng `Students` có 1.000 dòng, `Courses` có 500 dòng.
- `CROSS JOIN` (tích Descartes đầy đủ) tạo tối đa $$1{,}000 \times 500 = 500{,}000$$ dòng trước khi lọc.
- `JOIN` với điều kiện `ON` là tích Descartes **có lọc** — chỉ giữ cặp khớp khóa.
</div>

## Tính chất quan trọng

### Giao và tích

<div class="textbook-theorem" markdown="1">
**Định lý**: Với mọi tập $$Q,R,S,T$$,

$$(Q \times R) \cap (S \times T) = (Q \cap S) \times (R \cap T).$$
</div>

**Chứng minh**: $$(x,y) \in (Q \times R) \cap (S \times T)$$ ⇔ $$x \in Q, y \in R, x \in S, y \in T$$ ⇔ $$x \in Q \cap S, y \in R \cap T$$ ⇔ $$(x,y) \in (Q \cap S) \times (R \cap T)$$. ∎

### Hợp và tích — không phân phối đơn giản

<div class="textbook-example" markdown="1">
**Cảnh báo**: $$(Q \times R) \cup (S \times T) \neq (Q \cup S) \times (R \cup T)$$ nói chung.

Phản ví dụ: $$Q=\{1\}, R=\{a\}, S=\{2\}, T=\{b\}$$.

- Vế trái: $$\{(1,a), (2,b)\}$$.
- Vế phải: $$\{1,2\} \times \{a,b\} = \{(1,a),(1,b),(2,a),(2,b)\}$$.
</div>

Hiểu điều này giúp tránh suy luận sai khi ghép nhiều nguồn dữ liệu: hợp hai tập cặp **không** bằng tích hai tập hợp thành phần.

### Tích rỗng

Nếu $$A = \emptyset$$ hoặc $$B = \emptyset$$ thì $$A \times B = \emptyset$$. Không có cặp nào được tạo — tương ứng truy vấn `CROSS JOIN` với một bảng rỗng cho kết quả rỗng.

## Tích nhiều tập và quan hệ

Tích $$n$$ tập:

$$A_1 \times A_2 \times \cdots \times A_n = \{(a_1, a_2, \ldots, a_n) \mid a_i \in A_i\}.$$

<div class="textbook-definition" markdown="1">
**Định nghĩa (xem trước Chương 5)**: Cho $$A,B$$ là hai tập. **Quan hệ** $$R$$ từ $$A$$ đến $$B$$ là một tập con của $$A \times B$$:

$$R \subseteq A \times B.$$
</div>

Ví dụ: $$A$$ = tập sinh viên, $$B$$ = tập môn học, $$R$$ = tập các cặp `(sinh_viên, môn)` mà sinh viên đó đã đăng ký. Không phải mọi cặp đều thuộc $$R$$ — quan hệ **chọn** một phần của tích Descartes.

![Phép JOIN trong SQL](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

<p class="textbook-figure-caption" data-figure="4.20">`JOIN` — lọc tích Descartes theo điều kiện khóa khớp.</p>

```sql
-- Tích Descartes đầy đủ (thường tránh trong production)
SELECT * FROM Students CROSS JOIN Courses;

-- Quan hệ có lọc: chỉ cặp (student, course) đã đăng ký
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON e.course_id = c.id;
```

## Bài tập thực hành

### Bài tập 1: Liệt kê tích

Cho $$A = \{0, 1\}$$, $$B = \{a, b, c\}$$. Liệt kê $$A \times B$$ và tính $$\lvert A \times B \rvert$$.

<details>
<summary>Đáp án</summary>

$$A \times B = \{(0,a), (0,b), (0,c), (1,a), (1,b), (1,c)\}$$, $$\lvert A \times B \rvert = 2 \times 3 = 6$$.

</details>

### Bài tập 2: Tính chất giao

Chứng minh $$(Q \times R) \cap (S \times T) = (Q \cap S) \times (R \cap T)$$ bằng phương pháp phần tử.

<details>
<summary>Đáp án</summary>

Xét $$(x,y)$$. Theo định nghĩa tích và giao, chuỗi tương đương trong mục "Giao và tích" ở trên là chứng minh hai chiều. ∎

</details>

### Bài tập 3: SQL và quy mô

Bảng `A` có 2.000 dòng, `B` có 3.000 dòng. Một truy vấn `SELECT * FROM A CROSS JOIN B` tạo tối đa bao nhiêu dòng? Nếu thêm `WHERE A.id = B.a_id` và mỗi `id` khớp trung bình 2 dòng ở `B`, ước lượng số dòng sau lọc.

<details>
<summary>Đáp án</summary>

`CROSS JOIN` tối đa $$2{,}000 \times 3{,}000 = 6{,}000{,}000$$ dòng. Sau lọc khóa, nếu mỗi dòng `A` khớp 2 dòng `B` thì khoảng $$2{,}000 \times 2 = 4{,}000$$ dòng — nhỏ hơn rất nhiều so với tích đầy đủ.

</details>

### Bài tập 4: Quan hệ như tập con

$$S = \{1,2,3\}$$, $$T = \{a,b\}$$. Cho $$R = \{(1,a), (2,b), (3,a)\}$$. (a) Chứng minh $$R \subseteq S \times T$$. (b) $$\lvert S \times T \rvert$$ là bao nhiêu? (c) Tỷ lệ $$\lvert R \rvert / \lvert S \times T \rvert$$ cho biết điều gì?

<details>
<summary>Đáp án</summary>

(a) Mỗi cặp trong $$R$$ có thành phần đầu thuộc $$S$$, thành phần sau thuộc $$T$$.

(b) $$\lvert S \times T \rvert = 3 \times 2 = 6$$.

(c) Tỷ lệ $$3/6 = 1/2$$ — chỉ một nửa cặp khả dĩ thực sự thuộc quan hệ (độ "thưa" của quan hệ).

</details>

## Xem thêm / Video gợi ý

- [Cartesian Product](https://www.youtube.com/watch?v=8tShnKOE-1o) — Khan Academy
- [Relations and Functions](https://www.youtube.com/watch?v=JbEpXyH8Y9s) — giới thiệu quan hệ từ tích Descartes

## Tóm tắt

- **Cặp có thứ tự** $$(a,b)$$ khác tập $$\{a,b\}$$ — thứ tự quan trọng trong dữ liệu và tọa độ.
- **Tích Descartes** $$A \times B$$ gồm mọi cặp $$(a,b)$$ với $$a \in A, b \in B$$; $$\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$$.
- **Giao**: $$(Q \times R) \cap (S \times T) = (Q \cap S) \times (R \cap T)$$; **hợp** không phân phối tương tự.
- **Quan hệ** là tập con của tích Descartes — nền tảng Chương 5 và mô hình bảng SQL.
- `CROSS JOIN` = tích đầy đủ; `JOIN ... ON` = tích có lọc — nhầm hai phép dễ gây truy vấn chậm hoặc kết quả sai.

Trong bài tiếp theo, chúng ta quay lại **ứng dụng** tập hợp trong CSDL, lập trình và cấu trúc dữ liệu — nơi hợp, giao, hiệu và membership xuất hiện mỗi ngày trong production.