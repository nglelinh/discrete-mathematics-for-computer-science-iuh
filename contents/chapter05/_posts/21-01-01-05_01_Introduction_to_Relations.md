---
layout: post
title: "Giới thiệu Quan hệ"
categories: chapter05
date: 2021-01-01
order: 1
required: true
lang: en
---

Trong dữ liệu và hệ thống, các đối tượng hiếm khi tồn tại một mình. Sinh viên học môn học, người dùng theo dõi người dùng khác, tiến trình phụ thuộc tài nguyên, hai node có kết nối với nhau. Điều quan trọng không chỉ là có những phần tử nào, mà còn là chúng **liên hệ** với nhau ra sao.


Khi đọc phần này, hãy nghĩ đến các liên kết giữa đối tượng trong cơ sở dữ liệu, đồ thị và hệ thống phân quyền, vì quan hệ chính là cách ta mô tả những liên kết đó.
**Quan hệ** là công cụ để mô hình hóa chính xác các liên kết đó. Từ góc nhìn toán học, quan hệ là tập con của tích Descartes. Từ góc nhìn khoa học máy tính, nó là nền tảng của cơ sở dữ liệu quan hệ, ma trận kề, mô hình trạng thái, hệ thống phân quyền và rất nhiều cấu trúc khác.

Một khi đã nhìn bài toán dưới dạng quan hệ, ta có thể đặt ra những câu hỏi sâu hơn: quan hệ này có đối xứng không, có phản xạ không, có cho phép suy ra quan hệ mới hay không? Những câu hỏi đó sẽ dẫn thẳng đến các chương sau về thứ tự, tương đương và đồ thị.

Bài này sẽ đặt nền cho toàn bộ phần đó bằng cách giới thiệu định nghĩa quan hệ, cách biểu diễn và cách đọc ý nghĩa của quan hệ trong ngữ cảnh thực tế.

## Định nghĩa Quan hệ

Phần này đặt lại ngôn ngữ chung của bài học. Nắm chắc định nghĩa trước sẽ giúp các ví dụ và định lý phía sau trở nên dễ theo dõi hơn.

**Định nghĩa**: Quan hệ R từ tập hợp A đến tập hợp B là một tập con của tích Cartesian A × B.

**Ký hiệu**: 
- R ⊆ A × B
- Nếu (a, b) ∈ R, ta viết aRb hoặc R(a, b)
- Nếu (a, b) ∉ R, ta viết a R̸ b

### Tích Cartesian

**Định nghĩa**: A × B = {(a, b) | a ∈ A và b ∈ B}

**Ví dụ**:
- A = {1, 2}, B = {x, y}
- A × B = {(1, x), (1, y), (2, x), (2, y)}
- |A × B| = |A| × |B| = 2 × 2 = 4

<div class="content-box insight-box" markdown="1">
**Tích Cartesian trong CS**: Tích Cartesian là nền tảng của phép JOIN trong SQL. Khi bạn viết `SELECT * FROM A, B`, bạn nhận được tích Cartesian A × B. Thực tế, phép `CROSS JOIN` trong SQL chính là tích Cartesian.
</div>

### Quan hệ trên một tập hợp

Khi A = B, ta nói R là **quan hệ trên A** (R ⊆ A × A). Đây là trường hợp quan trọng nhất -- chúng ta sẽ tập trung vào loại quan hệ này.

**Ví dụ**: Quan hệ "≤" trên ℝ là quan hệ trên tập số thực. Quan hệ "⊆" trên tập lũy thừa của S là quan hệ trên 𝒫(S).

## Các cách biểu diễn quan hệ

### 1. Liệt kê các cặp
**Ví dụ**: R = {(1, 2), (2, 3), (3, 1)} trên tập {1, 2, 3}

### 2. Mô tả bằng tính chất
**Ví dụ**: R = {(x, y) | x < y} trên tập số thực

### 3. Ma trận quan hệ
Cho A = {a₁, a₂, ..., aₘ}, B = {b₁, b₂, ..., bₙ}

Ma trận M_R có M_R[i][j] = 1 nếu (aᵢ, bⱼ) ∈ R, ngược lại = 0

**Ví dụ**: A = {1, 2, 3}, R = {(1, 1), (2, 3), (3, 2)}

```
    1  2  3
1 [ 1  0  0 ]
2 [ 0  0  1 ]
3 [ 0  1  0 ]
```

### 4. Đồ thị có hướng (Digraph)
- Đỉnh: các phần tử của tập hợp
- Cung (mũi tên): các cặp trong quan hệ

#### Minh họa trực quan: Ma trận quan hệ

**Quy tắc nhanh**:
- **Hàng** = phần tử nguồn (từ A)
- **Cột** = phần tử đích (đến B)
- Nếu A = B → ma trận **vuông**

![Đồ thị có hướng](https://commons.wikimedia.org/wiki/Special:FilePath/Example_of_simple_directed_graph.svg?width=400)

*Hình 5.1: Biểu diễn quan hệ bằng đồ thị có hướng — mỗi cung thể hiện một cặp (a, b) ∈ R.*

## Ứng dụng trong Khoa học Máy tính

### 1. Cơ sở dữ liệu quan hệ
Mô hình quan hệ (relational model) do Edgar Codd đề xuất năm 1970 là nền tảng của hầu hết cơ sở dữ liệu hiện đại. Mỗi bảng (table) là một quan hệ, mỗi hàng là một bộ (tuple), và mỗi cột là một thuộc tính.

Trong cách nhìn này, lược đồ `Enrollments(student_id, course_id)` được xây từ tích Cartesian `Students × Courses`, còn quan hệ thật sự chỉ lấy những cặp có nghĩa như `(S01, CS101)`. Quan hệ one-to-many xuất hiện ở `Departments × Students`, còn many-to-many xuất hiện ở `Students × Courses`.

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

```python
students = {"S01", "S02"}
courses = {"CS101", "MATH101"}
enrollments = {("S01", "CS101"), ("S01", "MATH101"), ("S02", "CS101")}
cs_only = {sid for (sid, cid) in enrollments if cid == "CS101"}
```

Đoạn mã trên biểu diễn quan hệ như một tập các bộ. Đây là cách rất gần với định nghĩa toán học `R ⊆ A × B`.

### 2. Đồ thị và mạng xã hội
Quan hệ "bạn bè" trên Facebook là quan hệ hai ngôi. Đồ thị có hướng của quan hệ giúp phân tích mạng xã hội: ai là người có ảnh hưởng, ai kết nối các nhóm.

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

## Tóm tắt

- **Quan hệ** R từ A đến B là tập con của A × B
- Biểu diễn: **liệt kê**, **mô tả**, **ma trận**, **đồ thị có hướng**
- **Quan hệ trên A**: R ⊆ A × A
- **Tích Cartesian**: A × B, lực lượng |A| × |B|
- Ứng dụng: cơ sở dữ liệu quan hệ (SQL JOIN), đồ thị, mạng xã hội

Trong bài tiếp theo, chúng ta sẽ xem xét bốn tính chất cơ bản của quan hệ: phản xạ, đối xứng, phản đối xứng, và bắc cầu -- chìa khóa để phân loại quan hệ.
