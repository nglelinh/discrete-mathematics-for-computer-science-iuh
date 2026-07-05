---

layout: post
title: "Giới thiệu Quan hệ"
categories: chapter05
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Trong chương này chúng ta nghiên cứu quan hệ — cấu trúc mô tả cách các đối tượng liên kết với nhau. Trong cơ sở dữ liệu, đồ thị và hệ thống phân quyền, điều…"
---

<div class="textbook-epigraph" markdown="1">

"Order is the shape upon which beauty depends."

<span class="epigraph-attribution">— Pearl S. Buck</span>

</div>

Trong chương này chúng ta nghiên cứu **quan hệ** — cấu trúc mô tả cách các đối tượng liên kết với nhau. Trong cơ sở dữ liệu, đồ thị và hệ thống phân quyền, điều quan trọng không chỉ là có những phần tử nào, mà còn là chúng **liên hệ** với nhau ra sao. Mục 5.1 này bắt đầu từ định nghĩa quan hệ như tập con của tích Descartes, các cách biểu diễn và ứng dụng trong khoa học máy tính.

Từ góc nhìn toán học, quan hệ là tập con của tích Cartesian $$A \times B$$; từ góc nhìn khoa học máy tính, nó là nền tảng của mô hình quan hệ, ma trận kề, mô hình trạng thái và hệ thống phân quyền. Một khi đã nhìn bài toán dưới dạng quan hệ, chúng ta có thể đặt các câu hỏi về tính phản xạ, đối xứng, bắc cầu và khả năng suy diễn quan hệ mới — những chủ đề sẽ được phát triển ở các mục tiếp theo.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** quan hệ như tập con của tích Cartesian $$A \times B$$.
- **Biểu diễn** quan hệ bằng bảng, ma trận và đồ thị có hướng.
- **Tính** miền, tầm và thặng dư của quan hệ.
- **Áp dụng** quan hệ trong CSDL, đồ thị và mô hình trạng thái.

**Từ khóa**: quan hệ (relation), tích Cartesian, miền (domain), tầm (range), ma trận quan hệ.
</div>

## Định nghĩa Quan hệ
<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ R từ tập hợp A đến tập hợp B là một tập con của tích Cartesian A × B.
</div>

**Ký hiệu**: 
- R ⊆ A × B
- Nếu (a, b) ∈ R, chúng ta viết aRb hoặc R(a, b)
- Nếu (a, b) ∉ R, chúng ta viết a R̸ b

### Tích Cartesian

<div class="textbook-definition" markdown="1">
**Định nghĩa**: A × B = {(a, b) | a ∈ A và b ∈ B}
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- A = {1, 2}, B = {x, y}
- A × B = {(1, x), (1, y), (2, x), (2, y)}
- |A × B| = |A| × |B| = 2 × 2 = 4
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Tích Cartesian trong CS**: Tích Cartesian là nền tảng của phép JOIN trong SQL. Khi chúng ta viết `SELECT * FROM A, B`, chúng ta nhận được tích Cartesian A × B. Thực tế, phép `CROSS JOIN` trong SQL chính là tích Cartesian.
</div>

### Quan hệ trên một tập hợp

Khi A = B, chúng ta nói R là **quan hệ trên A** (R ⊆ A × A). Đây là trường hợp quan trọng nhất -- chúng ta sẽ tập trung vào loại quan hệ này.

<div class="textbook-example" markdown="1">
**Ví dụ**: Quan hệ "≤" trên ℝ là quan hệ trên tập số thực. Quan hệ "⊆" trên tập lũy thừa của S là quan hệ trên 𝒫(S).
</div>

## Các cách biểu diễn quan hệ

### 1. Liệt kê các cặp
<div class="textbook-example" markdown="1">
**Ví dụ**: R = {(1, 2), (2, 3), (3, 1)} trên tập {1, 2, 3}
</div>

### 2. Mô tả bằng tính chất
<div class="textbook-example" markdown="1">
**Ví dụ**: R = {(x, y) | x < y} trên tập số thực
</div>

### 3. Ma trận quan hệ
Cho A = {a₁, a₂, ..., aₘ}, B = {b₁, b₂, ..., bₙ}

Ma trận M_R có M_R[i][j] = 1 nếu (aᵢ, bⱼ) ∈ R, ngược lại = 0

<div class="textbook-example" markdown="1">
**Ví dụ**: A = {1, 2, 3}, R = {(1, 1), (2, 3), (3, 2)}

```
    1  2  3
1 [ 1  0  0 ]
2 [ 0  0  1 ]
3 [ 0  1  0 ]
```
</div>

### 4. Đồ thị có hướng (Digraph)
- Đỉnh: các phần tử của tập hợp
- Cung (mũi tên): các cặp trong quan hệ

#### Minh họa trực quan: Ma trận quan hệ

**Quy tắc nhanh**:
- **Hàng** = phần tử nguồn (từ A)
- **Cột** = phần tử đích (đến B)
- Nếu A = B → ma trận **vuông**

![Đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.1">Biểu diễn quan hệ bằng đồ thị có hướng — mỗi cung thể hiện một cặp (a, b) ∈ R.</p>
![Tích Cartesian A × B](/discrete-mathematics-for-computer-science-iuh/img/course/Cartesian_Product_qtl1.svg)

<p class="textbook-figure-caption" data-figure="5.2">Tích Cartesian A × B — mỗi cặp (a, b) ghép một phần tử từ A với một phần tử từ B.</p>
## Ứng dụng trong Khoa học Máy tính

### 1. Cơ sở dữ liệu quan hệ
Mô hình quan hệ (relational model) do Edgar Codd đề xuất năm 1970 là nền tảng của hầu hết cơ sở dữ liệu hiện đại. Mỗi bảng (table) là một quan hệ, mỗi hàng là một bộ (tuple), và mỗi cột là một thuộc tính.

Trong cách nhìn này, lược đồ `Enrollments(student_id, course_id)` được xây từ tích Cartesian `Students × Courses`, còn quan hệ thật sự chỉ lấy những cặp có nghĩa như `(S01, CS101)`. Quan hệ one-to-many xuất hiện ở `Departments × Students`, còn many-to-many xuất hiện ở `Students × Courses`.

![Biểu tượng cơ sở dữ liệu quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="5.3">Mô hình quan hệ — mỗi bảng là một quan hệ, mỗi hàng là một bộ (tuple).</p>
### 2. Quan hệ và truy vấn SQL
Các phép SQL quen thuộc chính là cách thao tác trên quan hệ: `SELECT` gần với phép chiếu thuộc tính, `WHERE` lọc những bộ thỏa điều kiện, còn `JOIN` ghép các quan hệ qua thuộc tính chung.

```sql
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON c.id = e.course_id
WHERE c.department = 'CS';
```

Ở đây, `JOIN` nối các cặp liên hệ, `WHERE` giữ lại các bộ thuộc khoa `CS`, và `SELECT` chỉ chiếu ra hai thuộc tính cần xem.

![Phép JOIN trong SQL](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

<p class="textbook-figure-caption" data-figure="5.4">Phép JOIN ghép hai quan hệ qua thuộc tính chung — tương đương lọc tích Cartesian theo điều kiện khớp khóa.</p>
```python
students = {"S01", "S02"}
courses = {"CS101", "MATH101"}
enrollments = {("S01", "CS101"), ("S01", "MATH101"), ("S02", "CS101")}
cs_only = {sid for (sid, cid) in enrollments if cid == "CS101"}
```

Đoạn mã trên biểu diễn quan hệ như một tập các bộ. Đây là cách rất gần với định nghĩa toán học `R ⊆ A × B`.

### 2. Đồ thị và mạng xã hội
Quan hệ "chúng ta bè" trên Facebook là quan hệ hai ngôi. Đồ thị có hướng của quan hệ giúp phân tích mạng xã hội: ai là người có ảnh hưởng, ai kết nối các nhóm.

![Đồ thị có hướng minh họa quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.5">Đồ thị có hướng — mỗi cung (mũi tên) biểu diễn một cặp có trong quan hệ.</p>
![Phân tích mạng xã hội](/discrete-mathematics-for-computer-science-iuh/img/course/Social_Network_Analysis_Visualization.png)

<p class="textbook-figure-caption" data-figure="5.6">Mạng xã hội thực tế là đồ thị quan hệ quy mô lớn — phân tích liên kết giúp tìm nhóm, ảnh hưởng và cấu trúc cộng đồng.</p>
### 3. Lý thuyết đồ thị
Mọi đồ thị có hướng đều biểu diễn một quan hệ. Đồ thị vô hướng biểu diễn quan hệ đối xứng.

## Bài tập thực hành

### Bài tập 1: Tích Cartesian

Cho A = {1, 2, 3} và B = {a, b}. Tính A × B và |A × B|.

<details>
<summary>Đáp án</summary>

A × B = {(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)}

|A × B| = 3 × 2 = 6
</details>

### Bài tập 2: Ma trận quan hệ

Viết ma trận quan hệ cho R = {(1, 2), (2, 1), (1, 3)} trên A = {1, 2, 3}.

<details>
<summary>Đáp án</summary>

```
    1  2  3
1 [ 0  1  1 ]
2 [ 1  0  0 ]
3 [ 0  0  0 ]
```
</details>

### Bài tập 3: Tìm quan hệ từ ma trận

Cho ma trận quan hệ sau trên A = {a, b, c}:
```
   a  b  c
a [1 0 1]
b [0 1 0]
c [0 1 1]
```

Liệt kê các cặp của R.

<details>
<summary>Đáp án</summary>

R = {(a, a), (a, c), (b, b), (c, b), (c, c)}
</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Quan hệ** R từ A đến B là tập con của A × B
- Biểu diễn: **liệt kê**, **mô tả**, **ma trận**, **đồ thị có hướng**
- **Quan hệ trên A**: R ⊆ A × A
- **Tích Cartesian**: A × B, lực lượng |A| × |B|
- Ứng dụng: cơ sở dữ liệu quan hệ (SQL JOIN), đồ thị, mạng xã hội

Trong bài tiếp theo, chúng ta sẽ xem xét bốn tính chất cơ bản của quan hệ: phản xạ, đối xứng, phản đối xứng, và bắc cầu -- chìa khóa để phân loại quan hệ.
