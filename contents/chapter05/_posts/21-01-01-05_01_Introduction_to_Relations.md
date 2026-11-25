---

layout: post
title: "Giới thiệu Quan hệ"
categories: chapter05
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Giới thiệu khái niệm quan hệ như tập con của tích Descartes, các cách biểu diễn bằng liệt kê, ma trận và đồ thị có hướng, cùng ứng dụng trong cơ sở dữ liệu và mạng xã hội."
---


Một danh sách sinh viên và một danh sách môn học đứng tách rời nhau chỉ là hai tập hợp vô hồn; hệ thống đào tạo chỉ thực sự "sống dậy" khi ta nối chúng lại bằng các cặp có thứ tự *(sinh viên $$a$$, môn học $$b$$)*. Từ bảng ghi danh trong SQL, mạng lưới người theo dõi trên mạng xã hội cho đến sơ đồ gọi hàm giữa các microservice, mọi sự kết nối có cấu trúc trong khoa học máy tính đều quy về một khái niệm duy nhất: **Quan hệ (Relation)**.

<div class="textbook-epigraph" markdown="1">

"Order is the shape upon which beauty depends."

<span class="epigraph-attribution">— Pearl S. Buck</span>

</div>

Trong chương này, chúng ta nghiên cứu **quan hệ** — cấu trúc toán học mô tả cách các đối tượng liên kết với nhau. Trong cơ sở dữ liệu, đồ thị hay hệ thống phân quyền, điều quan trọng không chỉ là tập hợp có những phần tử nào, mà còn là chúng **liên hệ** với nhau ra sao. Mục 5.1 giới thiệu định nghĩa quan hệ như tập con của tích Descartes, các cách biểu diễn cơ bản và những ứng dụng trực tiếp trong khoa học máy tính.

Dưới góc nhìn toán học, quan hệ hai ngôi là một tập con của tích Descartes $$A \times B$$; dưới góc nhìn khoa học máy tính, đây là nền tảng của mô hình cơ sở dữ liệu quan hệ, ma trận kề, mô hình trạng thái và hệ thống phân quyền. Khi đã biểu diễn bài toán dưới dạng quan hệ, ta có thể phân tích các tính chất như phản xạ, đối xứng, bắc cầu và suy diễn thêm các liên kết mới ở các mục tiếp theo.

## Kiến thức cần nhớ: Bốn góc nhìn cốt lõi về Quan hệ Hai ngôi

1. **Tích Descartes $$A \times B$$ — Không gian mọi liên kết có thể xảy ra**:
   Trước khi xét quan hệ, ta tạo tập tất cả các cặp có thứ tự $$(a, b)$$ với $$a \in A, b \in B$$. Khác với tập hợp, thứ tự trong cặp rất quan trọng: $$(a, b) \neq (b, a)$$ khi $$a \neq b$$, và $$\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$$.

2. **Quan hệ $$R \subseteq A \times B$$ — Chọn lọc những liên kết thực sự tồn tại**:
   Một quan hệ hai ngôi từ $$A$$ đến $$B$$ đơn giản là một **tập con** của $$A \times B$$. Ta viết $$aRb$$ (hoặc $$(a, b) \in R$$) để khẳng định $$a$$ có quan hệ $$R$$ với $$b$$. Nếu $$A = B$$, ta gọi là quan hệ **trên tập $$A$$**.

3. **Bốn cách biểu diễn tương đương (chọn đúng công cụ cho đúng bài toán)**:
   - *Liệt kê cặp* và *Mô tả tính chất*: gọn gàng cho tư duy toán học và chứng minh.
   - *Ma trận quan hệ $$M_R$$ (0–1)*: tối ưu cho máy tính, phép nhân Boolean và thuật toán đồ thị dày.
   - *Đồ thị có hướng (Digraph)*: trực quan nhất để nhìn đường đi, chu trình và khuyên (self-loop).

4. **Quy mô bùng nổ tổ hợp ($$2^{\lvert A \rvert\cdot\lvert B \rvert}$$)**:
   Vì mỗi cặp trong $$A \times B$$ có 2 lựa chọn (thuộc $$R$$ hoặc không), nên trên tập $$A$$ gồm $$n$$ phần tử có tới $$2^{n^2}$$ quan hệ khác nhau—ngay cả với $$n = 4$$ đã có $$2^{16} = 65{,}536$$ quan hệ!

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** quan hệ như một tập con của tích Descartes $$A \times B$$.
- **Biểu diễn** quan hệ bằng cách liệt kê cặp, mô tả tính chất, ma trận 0-1 và đồ thị có hướng.
- **Phân biệt** quan hệ giữa hai tập hợp với quan hệ trên một tập hợp.
- **Áp dụng** khái niệm quan hệ để lý giải bảng trong cơ sở dữ liệu, truy vấn SQL và đồ thị mạng xã hội.

**Từ khóa**: quan hệ (relation), tích Descartes (Cartesian product), miền (domain), tầm (range), ma trận quan hệ.
</div>

## Định nghĩa Quan hệ
<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **quan hệ** (hai ngôi) $$R$$ từ tập hợp $$A$$ đến tập hợp $$B$$ là một tập con của tích Descartes $$A \times B$$.
</div>

**Ký hiệu**:
- $$R \subseteq A \times B$$.
- Nếu $$(a, b) \in R$$, ta viết $$aRb$$ hoặc $$R(a, b)$$ (đọc là "$$a$$ có quan hệ $$R$$ với $$b$$").
- Nếu $$(a, b) \notin R$$, ta viết $$a \not R b$$.

### Tích Descartes (Cartesian Product)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A \times B = \{(a, b) \mid a \in A \text{ và } b \in B\}$$
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$A = \{1, 2\}$$, $$B = \{x, y\}$$.
- $$A \times B = \{(1, x), (1, y), (2, x), (2, y)\}$$.
- $$\lvert A \times B \rvert = \lvert A \rvert \times \lvert B \rvert = 2 \times 2 = 4$$.
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Tích Descartes trong khoa học máy tính**: Tích Descartes là cơ sở của phép `JOIN` trong SQL. Câu lệnh `SELECT * FROM A, B` (hay `CROSS JOIN`) tạo ra đúng tích Descartes $$A \times B$$.
</div>

### Quan hệ trên một tập hợp

Khi $$A = B$$, ta gọi $$R$$ là một **quan hệ trên $$A$$** ($$R \subseteq A \times A$$). Đây là trường hợp trọng tâm sẽ được nghiên cứu xuyên suốt các mục tiếp theo.

<div class="textbook-example" markdown="1">
**Ví dụ**: Quan hệ "$$\le$$" trên $$\mathbb{R}$$ là một quan hệ trên tập số thực; quan hệ "$$\subseteq$$" trên tập lũy thừa $$\mathcal{P}(S)$$ là một quan hệ trên $$\mathcal{P}(S)$$.
</div>

## Các cách biểu diễn quan hệ

### Liệt kê các cặp
<div class="textbook-example" markdown="1">
**Ví dụ**: $$R = \{(1, 2), (2, 3), (3, 1)\}$$ trên tập $$\{1, 2, 3\}$$.
</div>

### Mô tả bằng tính chất
<div class="textbook-example" markdown="1">
**Ví dụ**: $$R = \{(x, y) \mid x < y\}$$ trên tập số thực $$\mathbb{R}$$.
</div>

### Ma trận quan hệ
Cho $$A = \{a_1, a_2, \ldots, a_m\}$$ và $$B = \{b_1, b_2, \ldots, b_n\}$$. Ma trận quan hệ $$M_R$$ có kích thước $$m \times n$$ với $$M_R[i][j] = 1$$ nếu $$(a_i, b_j) \in R$$ và bằng $$0$$ nếu ngược lại.

<div class="textbook-example" markdown="1">
**Ví dụ**: Với $$A = \{1, 2, 3\}$$ và $$R = \{(1, 1), (2, 3), (3, 2)\}$$:

```
    1  2  3
1 [ 1  0  0 ]
2 [ 0  0  1 ]
3 [ 0  1  0 ]
```
</div>

### Đồ thị có hướng (Digraph)
- **Đỉnh**: tương ứng với các phần tử của tập hợp.
- **Cung (mũi tên)**: mỗi cặp $$(a, b) \in R$$ được vẽ thành một cung có hướng từ $$a$$ đến $$b$$.

#### Minh họa trực quan: Quy tắc đọc ma trận quan hệ

- **Hàng** tương ứng với phần tử nguồn (thuộc $$A$$).
- **Cột** tương ứng với phần tử đích (thuộc $$B$$).
- Khi $$A = B$$, ma trận quan hệ là **ma trận vuông**.

![Đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.1">Biểu diễn quan hệ bằng đồ thị có hướng — mỗi cung biểu diễn một cặp (a, b) ∈ R.</p>
![Tích Cartesian A × B](/discrete-mathematics-for-computer-science-iuh/img/course/Cartesian_Product_qtl1.svg)

<p class="textbook-figure-caption" data-figure="5.2">Tích Descartes A × B — mỗi cặp (a, b) ghép một phần tử từ A với một phần tử từ B.</p>

### Giải thích: Biểu diễn quan hệ chia hết trên $$A = \{1, 2, 3, 4\}$$ theo đủ 4 cách

Xét tập $$A = \{1, 2, 3, 4\}$$ và quan hệ $$R$$ trên $$A$$ định nghĩa bởi $$aRb \iff a \mid b$$ ($$a$$ là ước của $$b$$).

1. **Cách 1 — Mô tả bằng tính chất**:
   $$R = \{(a, b) \in A \times A \mid b \bmod a = 0\}.$$
2. **Cách 2 — Liệt kê từng cặp có thứ tự** (duyệt từng hàng $$a = 1, 2, 3, 4$$):
   - $$a = 1$$ chia hết mọi phần tử: $$(1,1), (1,2), (1,3), (1,4)$$ (4 cặp).
   - $$a = 2$$ chia hết $$2$$ và $$4$$: $$(2,2), (2,4)$$ (2 cặp).
   - $$a = 3$$ chỉ chia hết $$3$$: $$(3,3)$$ (1 cặp).
   - $$a = 4$$ chỉ chia hết $$4$$: $$(4,4)$$ (1 cặp).
   Tổng cộng $$\lvert R \rvert = 4 + 2 + 1 + 1 = \mathbf{8}$$ cặp trên tổng số $$\lvert A \times A \rvert = 4 \times 4 = 16$$ cặp khả dĩ.
3. **Cách 3 — Ma trận quan hệ $$M_R$$ ($$4 \times 4$$)** (hàng là $$a$$, cột là $$b$$; ghi `1` nếu $$a \mid b$$, ngược lại `0`):
   $$M_R = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$
   *Mẹo đọc nhanh*: Đường chéo chính toàn số `1` (mọi số đều chia hết chính nó), và toàn bộ nửa dưới đường chéo đều là `0` (vì số lớn không bao giờ chia hết số nhỏ hơn trong tập dương).
4. **Cách 4 — Đồ thị có hướng (Digraph)**:
   Vẽ 4 đỉnh `1, 2, 3, 4`. Có **4 khuyên** tại chính mỗi đỉnh (`1→1, 2→2, 3→3, 4→4`) và **4 mũi tên nối hai đỉnh khác nhau** (`1→2, 1→3, 1→4, 2→4`). Đếm lại: $$4 + 4 = 8$$ cung, khớp hoàn toàn với số phần tử `1` trong ma trận $$M_R$$!

## Ứng dụng trong Khoa học Máy tính

### Cơ sở dữ liệu quan hệ
Mô hình quan hệ (relational model) do Edgar F. Codd đề xuất năm 1970 là nền tảng của đa số hệ quản trị cơ sở dữ liệu hiện đại. Trong mô hình này, mỗi bảng (table) là một quan hệ, mỗi hàng là một bộ (tuple) và mỗi cột là một thuộc tính.

Chẳng hạn, bảng `Enrollments(student_id, course_id)` là một tập con của tích Descartes `Students × Courses`, chỉ lưu các cặp thực sự tồn tại như `(S01, CS101)`. Quan hệ một–nhiều (one-to-many) xuất hiện giữa `Departments` và `Students`, còn quan hệ nhiều–nhiều (many-to-many) xuất hiện giữa `Students` và `Courses`.

![Biểu tượng cơ sở dữ liệu quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="5.3">Mô hình quan hệ — mỗi bảng là một quan hệ, mỗi hàng là một bộ (tuple).</p>
### Quan hệ và truy vấn SQL
Các mệnh đề quen thuộc của SQL tương ứng trực tiếp với các phép toán trên quan hệ: `SELECT` thực hiện phép chiếu thuộc tính, `WHERE` lọc các bộ thỏa điều kiện, và `JOIN` ghép các quan hệ dựa trên thuộc tính chung.

```sql
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON c.id = e.course_id
WHERE c.department = 'CS';
```

Trong câu lệnh trên, `JOIN` liên kết các bộ tương ứng giữa ba bảng, `WHERE` giữ lại các bản ghi thuộc khoa `CS`, và `SELECT` chỉ chiếu ra hai thuộc tính cần hiển thị.

![Phép JOIN trong SQL](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

<p class="textbook-figure-caption" data-figure="5.4">Phép JOIN ghép hai quan hệ qua thuộc tính chung — tương đương lọc tích Descartes theo điều kiện khớp khóa.</p>
```python
students = {"S01", "S02"}
courses = {"CS101", "MATH101"}
enrollments = {("S01", "CS101"), ("S01", "MATH101"), ("S02", "CS101")}
cs_only = {sid for (sid, cid) in enrollments if cid == "CS101"}
```

Đoạn mã Python trên biểu diễn quan hệ trực tiếp dưới dạng một tập các cặp, phản ánh sát định nghĩa toán học $$R \subseteq A \times B$$.

### Đồ thị và mạng xã hội
Quan hệ "bạn bè" trên Facebook hay "theo dõi" trên mạng xã hội đều là các quan hệ hai ngôi. Biểu diễn chúng bằng đồ thị giúp phân tích cấu trúc mạng xã hội như xác định nút trung tâm hay các cộng đồng liên kết chặt.

![Đồ thị có hướng minh họa quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.5">Đồ thị có hướng — mỗi cung có hướng biểu diễn một cặp thuộc quan hệ.</p>
![Phân tích mạng xã hội](/discrete-mathematics-for-computer-science-iuh/img/course/Social_Network_Analysis_Visualization.png)

<p class="textbook-figure-caption" data-figure="5.6">Mạng xã hội là đồ thị quan hệ quy mô lớn — phân tích liên kết giúp nhận diện nhóm, mức độ ảnh hưởng và cấu trúc cộng đồng.</p>
### Lý thuyết đồ thị
Mọi đồ thị có hướng đơn đều tương ứng với một quan hệ hai ngôi trên tập đỉnh, còn đồ thị vô hướng tương ứng với quan hệ đối xứng.


## Công cụ tương tác

Bật hoặc tắt các ô của ma trận quan hệ trên tập $$\{1,2,3\}$$ để xem tập cặp tương ứng.
<div class="interactive-demo" markdown="1">
<div data-demo="relation-matrix-toggle"></div>
</div>
<script src="{{ '/public/js/relation-matrix-toggle.js' | relative_url }}"></script>

### Minh họa tương tác

Chỉnh sửa ma trận hoặc đồ thị của một quan hệ trên tập nhỏ để quan sát các tính chất và phản ví dụ tương ứng.

<div class="interactive-demo" markdown="1">
<div data-demo="relation-explainer" data-preset="mod2"></div>
</div>
<script src="{{ '/public/js/explainers/relation-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Tích Descartes

Cho $$A = \{1, 2, 3\}$$ và $$B = \{a, b\}$$. Hãy liệt kê $$A \times B$$ và tính $$\lvert A \times B \rvert$$.

<details>
<summary>Đáp án</summary>

$A \times B = \{(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)\}$

$\lvert A \times B \rvert = 3 \times 2 = 6$
</details>

### Bài tập 2: Ma trận quan hệ

Viết ma trận quan hệ cho $$R = \{(1, 2), (2, 1), (1, 3)\}$$ trên $$A = \{1, 2, 3\}$$.

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

Cho ma trận quan hệ sau trên $$A = \{a, b, c\}$$:
```
   a  b  c
a [1 0 1]
b [0 1 0]
c [0 1 1]
```

Liệt kê các cặp thuộc $$R$$.

<details>
<summary>Đáp án</summary>

$R = \{(a, a), (a, c), (b, b), (c, b), (c, c)\}$
</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Quan hệ** $$R$$ từ $$A$$ đến $$B$$ là một tập con của $$A \times B$$.
- Bốn cách biểu diễn thông dụng: **liệt kê cặp**, **mô tả tính chất**, **ma trận 0-1** và **đồ thị có hướng**.
- **Quan hệ trên $$A$$** là trường hợp đặc biệt $$R \subseteq A \times A$$.
- **Tích Descartes** $$A \times B$$ có lực lượng $$\lvert A \rvert \times \lvert B \rvert$$.
- Ứng dụng thực tế: cơ sở dữ liệu quan hệ (SQL `JOIN`), lý thuyết đồ thị và phân tích mạng xã hội.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu bốn tính chất cơ bản của quan hệ: phản xạ, đối xứng, phản đối xứng và bắc cầu — cơ sở để phân loại các lớp quan hệ quan trọng.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=FI6j5QZNVx0">RELATIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu quan hệ như tập con của tích Descartes.
- <a href="https://www.youtube.com/watch?v=0dzNlrNJYdc">Relations between two sets | Definition + First Examples</a> — Dr. Trefor Bazett, tiếng Anh. Ví dụ quan hệ giữa hai tập và cách liệt kê các cặp.
- <a href="https://www.youtube.com/watch?v=cQiyDUiIcOQ">Relations and their Inverses</a> — Dr. Trefor Bazett, tiếng Anh. Giới thiệu quan hệ ngược, nội dung sẽ dùng lại ở mục phép toán và bao đóng.
