---
layout: post
title: "Tích Descartes và Cặp có thứ tự"
categories: chapter04
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Giới thiệu cặp có thứ tự, tích Descartes A × B, các tính chất cơ bản và mối liên hệ trực tiếp với phép JOIN trong SQL và khái niệm quan hệ ở Chương 5."
---

<div class="textbook-epigraph" markdown="1">

"Each problem that I solved became a rule, which served afterwards to solve other problems."

<span class="epigraph-attribution">— René Descartes</span>

</div>

Ở các mục trước, chúng ta làm việc với **tập hợp** — nơi thứ tự các phần tử không quan trọng. Tuy nhiên, trong khoa học máy tính, thứ tự thường mang ý nghĩa quyết định: tọa độ $$(x, y)$$ trên màn hình, cặp `(user_id, role)` trong bảng phân quyền, hay bộ `(sinh_viên, môn_học, điểm)` trong cơ sở dữ liệu. Để kết hợp các phần tử từ nhiều tập hợp theo **cặp có thứ tự**, ta sử dụng **tích Descartes** (Cartesian product). Đây là cầu nối trực tiếp sang **quan hệ** ở Chương 5, vì mỗi quan hệ hai ngôi là một tập con của tích Descartes.

Tập hợp vốn không quan tâm đến thứ tự ($\{1, 2\} = \{2, 1\}$), nhưng thế giới thực lại sống dựa vào thứ tự: tọa độ `(x, y)` khác `(y, x)`, cạnh có hướng `(An → Bình)` khác `(Bình → An)`, và một dòng trong bảng cơ sở dữ liệu `(mssv, ho_ten, diem)` phải giữ đúng vị trí từng cột. **Cặp có thứ tự (Ordered Pair)** và **Tích Descartes (Cartesian Product $A \times B$)** chính là cây cầu đưa cấu trúc thứ tự vào lý thuyết tập hợp.

## Bản đồ kiến thức nền: Bốn ý niệm cốt lõi của Tích Descartes

1. **Cặp có thứ tự $(a, b)$ & Bộ $n$-thành phần ($n$-tuple)**:
   $(a, b) = (c, d) \iff (a = c) \land (b = d)$. Mở rộng ra $n$ chiều, ta có bộ $(a_1, a_2, \dots, a_n)$—chính là một `tuple`/`struct` trong lập trình hay một bản ghi (*row*) trong bảng SQL.

2. **Tích Descartes $A \times B$ và Lực lượng**:
   $A \times B = \{(a, b) \mid a \in A \text{ và } b \in B\}$. Lực lượng luôn thỏa quy tắc nhân: $\vert A \times B \vert = \vert A \vert \cdot \vert B \vert$. Đặc biệt: $A \times B \neq B \times A$ (không giao hoán khi $A \neq B$ và cả hai khác rỗng!), và $A \times \emptyset = \emptyset$.

3. **Liên hệ trực tiếp với `CROSS JOIN` trong SQL và Không gian trạng thái**:
   Lệnh `SELECT * FROM Sizes CROSS JOIN Colors` trong SQL chính là tính tích Descartes $\text{Sizes} \times \text{Colors}$. Trong kiểm thử tự động và thuật toán, không gian trạng thái của hệ thống đa biến là tích Descartes của các miền biến.

4. **Bệ phóng sang Chương 5 (Quan hệ) và Chương 6 (Hàm số)**:
   Mọi quan hệ hai ngôi từ $A$ đến $B$ đơn giản chỉ là một **tập con** $R \subseteq A \times B$, và mọi hàm số $f: A \to B$ là một quan hệ đặc biệt trong $A \times B$!

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** cặp có thứ tự $$(a,b)$$ với tập hai phần tử $$\{a,b\}$$.
- **Định nghĩa** và **tính** tích Descartes $$A \times B$$.
- **Áp dụng** công thức lực lượng $$\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$$.
- **Chứng minh** một số tính chất cơ bản của tích Descartes (như tương tác với phép giao và trường hợp phép hợp).
- **Nhận diện** phép `CROSS JOIN` trong SQL và mối liên hệ với quan hệ.

**Từ khóa**: cặp có thứ tự (ordered pair), tích Descartes (Cartesian product), quan hệ (relation), `CROSS JOIN`.
</div>

## Cặp có thứ tự

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Cặp có thứ tự** (ordered pair) $$(a,b)$$ gồm hai thành phần theo thứ tự cố định: $$a$$ là **thành phần thứ nhất**, $$b$$ là **thành phần thứ hai**.
</div>

Hai cặp có thứ tự bằng nhau khi và chỉ khi từng thành phần tương ứng của chúng bằng nhau:

<div class="textbook-equation" markdown="1">
$$(a,b) = (c,d) \iff a = c \land b = d.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(3, 5) \neq (5, 3)$$ vì thứ tự hai thành phần khác nhau.
- $$\{3, 5\} = \{5, 3\}$$ vì tập hợp không phân biệt thứ tự phần tử.
- Trong Python, `tuple` biểu diễn cặp hoặc bộ có thứ tự nên `(3, 5) != (5, 3)`, còn `set` thì không phân biệt thứ tự.
</div>

Trong lập trình, kiểu từ điển (`dict`) lưu trữ các cặp khóa–giá trị, còn phép `JOIN` trong SQL ghép hai bản ghi thành một bộ có thứ tự cột xác định. Nhầm lẫn giữa cặp có thứ tự và tập hợp là nguyên nhân phổ biến gây sai sót khi mô hình hóa dữ liệu.

## Tích Descartes

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho hai tập hợp $$A$$ và $$B$$. **Tích Descartes** $$A \times B$$ là tập hợp tất cả các cặp có thứ tự $$(a,b)$$ với $$a \in A$$ và $$b \in B$$:

$$A \times B = \{(a,b) \mid a \in A \land b \in B\}.$$
</div>

![Tích Descartes A × B](/discrete-mathematics-for-computer-science-iuh/img/course/Cartesian_Product_qtl1.svg)

<p class="textbook-figure-caption" data-figure="4.19">Tích Descartes $$A \times B$$ — mỗi điểm trên lưới tương ứng với một cặp có thứ tự $$(a,b)$$.</p>

<div class="textbook-example" markdown="1">
**Ví dụ**: Cho $$A = \{1, 2\}$$ và $$B = \{x, y\}$$. Khi đó:

$$A \times B = \{(1,x), (1,y), (2,x), (2,y)\}.$$

Lực lượng của tích là $$\lvert A \times B \rvert = 2 \times 2 = 4$$.
</div>

Mặt phẳng tọa độ được ký hiệu là $$\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$$, trong đó mỗi điểm $$(x,y)$$ là một cặp số thực. Trong lập trình giao diện, tọa độ điểm ảnh `(row, col)` cũng là một phần tử của tích $$\mathbb{N} \times \mathbb{N}$$.

### Lực lượng của tích Descartes

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$A$$ và $$B$$ là hai tập hữu hạn thì:

$$\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert.$$
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh**: Với mỗi phần tử $$a \in A$$ (có $$\lvert A \rvert$$ cách chọn), ta chọn một phần tử $$b \in B$$ (có $$\lvert B \rvert$$ cách chọn). Theo nguyên lý nhân, tổng số cặp có thứ tự tạo thành là $$\lvert A \rvert \cdot \lvert B \rvert$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ (lưu ý về hiệu năng trong SQL)**:

- Giả sử bảng `Students` có 1.000 dòng và bảng `Courses` có 500 dòng.
- Phép `CROSS JOIN` (tích Descartes đầy đủ) tạo ra $$1{,}000 \times 500 = 500{,}000$$ dòng trước khi lọc.
- Phép `JOIN` kèm điều kiện `ON` thực chất là tích Descartes có lọc, chỉ giữ lại các cặp khớp khóa.
</div>

## Tính chất quan trọng

### Tích Descartes và phép giao

<div class="textbook-theorem" markdown="1">
**Định lý**: Với mọi tập hợp $$Q,R,S,T$$,

$$(Q \times R) \cap (S \times T) = (Q \cap S) \times (R \cap T).$$
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh**: $$(x,y) \in (Q \times R) \cap (S \times T) \iff x \in Q \land y \in R \land x \in S \land y \in T \iff x \in Q \cap S \land y \in R \cap T \iff (x,y) \in (Q \cap S) \times (R \cap T)$$.
</div>

### Tích Descartes và phép hợp — không phân phối trực tiếp

<div class="textbook-example" markdown="1">
**Cảnh báo**: Nói chung, $$(Q \times R) \cup (S \times T) \neq (Q \cup S) \times (R \cup T)$$.

Phản ví dụ: Chọn $$Q=\{1\}, R=\{a\}, S=\{2\}, T=\{b\}$$.

- Vế trái: $$\{(1,a), (2,b)\}$$.
- Vế phải: $$\{1,2\} \times \{a,b\} = \{(1,a),(1,b),(2,a),(2,b)\}$$.
</div>

Nắm rõ điểm này giúp tránh suy luận sai khi gộp dữ liệu từ nhiều nguồn: hợp của hai tập các cặp không bằng tích Descartes của hai tập hợp thành phần.

### Tích với tập rỗng

Nếu $$A = \emptyset$$ hoặc $$B = \emptyset$$ thì $$A \times B = \emptyset$$, vì không có cặp nào được tạo ra. Trong SQL, điều này tương ứng với việc `CROSS JOIN` cùng một bảng rỗng luôn trả về kết quả rỗng.

### Khung giải thích (nên đọc chậm): Tính tay kích thước `CROSS JOIN` (Tích Descartes) và tránh bẫy bùng nổ dòng trong SQL

Giả sử cửa hàng áo thun có:
- Tập kích cỡ $S = \{\text{M}, \text{L}\}$ ($\vert S \vert = 2$)
- Tập màu sắc $C = \{\text{Đen}, \text{Trắng}, \text{Xanh}\}$ ($\vert C \vert = 3$)

1. **Liệt kê đầy đủ $S \times C$** ($\vert S \times C \vert = 2 \times 3 = 6$ mã SKU):
   $$S \times C = \{(\text{M}, \text{Đen}), (\text{M}, \text{Trắng}), (\text{M}, \text{Xanh}), (\text{L}, \text{Đen}), (\text{L}, \text{Trắng}), (\text{L}, \text{Xanh})\}.$$
2. **Kiểm tra không giao hoán**: $(\text{M}, \text{Đen}) \in S \times C$, nhưng $(\text{M}, \text{Đen}) \notin C \times S$ (vì phần tử đầu của $C \times S$ phải là màu sắc!).
3. **Cảnh báo thực tế trong SQL**: Nếu bảng `Users` có `10.000` dòng và bảng `Orders` có `50.000` dòng, một câu lệnh `SELECT * FROM Users, Orders` quên mệnh đề `WHERE Users.id = Orders.user_id` sẽ buộc CSDL tính trọn tích Descartes:
   $$10.000 \times 50.000 = \mathbf{500.000.000\text{ dòng}}$$
   —làm treo ngay máy chủ CSDL! Biết công thức $\vert A \times B \vert = \vert A \vert \cdot \vert B \vert$ giúp bạn nhận ra ngay cái bẫy `CROSS JOIN` vô tình.

## Tích nhiều tập và khái niệm quan hệ

Tích Descartes mở rộng cho $$n$$ tập hợp là:

$$A_1 \times A_2 \times \cdots \times A_n = \{(a_1, a_2, \ldots, a_n) \mid a_i \in A_i\}.$$

<div class="textbook-definition" markdown="1">
**Định nghĩa (dẫn nhập Chương 5)**: Cho hai tập hợp $$A$$ và $$B$$. Một **quan hệ** $$R$$ từ $$A$$ đến $$B$$ là một tập con của tích Descartes $$A \times B$$:

$$R \subseteq A \times B.$$
</div>

Ví dụ, với $$A$$ là tập sinh viên và $$B$$ là tập môn học, quan hệ $$R$$ có thể là tập các cặp `(sinh_viên, môn)` mà sinh viên đó đã đăng ký. Không phải mọi cặp trong $$A \times B$$ đều thuộc $$R$$ — quan hệ chọn ra một tập con có ý nghĩa từ tích Descartes.

![Phép JOIN trong SQL](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

<p class="textbook-figure-caption" data-figure="4.20">Phép `JOIN` trong SQL lọc tích Descartes theo điều kiện khớp khóa.</p>

```sql
-- Tích Descartes đầy đủ (thường tránh dùng trên dữ liệu lớn)
SELECT * FROM Students CROSS JOIN Courses;

-- Quan hệ có lọc: chỉ lấy các cặp (student, course) đã đăng ký
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON e.course_id = c.id;
```

## Bài tập thực hành

### Bài tập 1: Liệt kê tích Descartes

Cho $$A = \{0, 1\}$$ và $$B = \{a, b, c\}$$. Liệt kê $$A \times B$$ và tính $$\lvert A \times B \rvert$$.

<details>
<summary>Đáp án</summary>

$$A \times B = \{(0,a), (0,b), (0,c), (1,a), (1,b), (1,c)\}$$, lực lượng $$\lvert A \times B \rvert = 2 \times 3 = 6$$.

</details>

### Bài tập 2: Tính chất giao

Chứng minh $$(Q \times R) \cap (S \times T) = (Q \cap S) \times (R \cap T)$$ bằng phương pháp phần tử.

<details>
<summary>Đáp án</summary>

Xét cặp $$(x,y)$$ bất kỳ. Theo định nghĩa tích Descartes và phép giao, chuỗi tương đương ở mục "Tích Descartes và phép giao" phía trên cho chứng minh cả hai chiều. ∎

</details>

### Bài tập 3: Quy mô truy vấn SQL

Bảng `A` có 2.000 dòng và bảng `B` có 3.000 dòng. Truy vấn `SELECT * FROM A CROSS JOIN B` tạo ra tối đa bao nhiêu dòng? Nếu bổ sung điều kiện `WHERE A.id = B.a_id` và mỗi `id` ở `A` khớp trung bình với 2 dòng ở `B`, hãy ước lượng số dòng kết quả sau khi lọc.

<details>
<summary>Đáp án</summary>

`CROSS JOIN` tạo ra $$2{,}000 \times 3{,}000 = 6{,}000{,}000$$ dòng. Sau khi lọc theo khóa, nếu mỗi dòng của `A` khớp trung bình 2 dòng của `B`, kết quả chỉ còn khoảng $$2{,}000 \times 2 = 4{,}000$$ dòng — nhỏ hơn rất nhiều so với tích Descartes đầy đủ.

</details>

### Bài tập 4: Quan hệ như một tập con

Cho $$S = \{1,2,3\}$$, $$T = \{a,b\}$$ và $$R = \{(1,a), (2,b), (3,a)\}$$.  
(a) Chứng minh $$R \subseteq S \times T$$.  
(b) Tính $$\lvert S \times T \rvert$$.  
(c) Tỷ lệ $$\lvert R \rvert / \lvert S \times T \rvert$$ cho biết điều gì?

<details>
<summary>Đáp án</summary>

(a) Mỗi cặp trong $$R$$ đều có thành phần thứ nhất thuộc $$S$$ và thành phần thứ hai thuộc $$T$$, nên $$R \subseteq S \times T$$.

(b) $$\lvert S \times T \rvert = 3 \times 2 = 6$$.

(c) Tỷ lệ là $$3/6 = 1/2$$, cho biết một nửa số cặp khả dĩ của $$S \times T$$ thuộc quan hệ $$R$$ (phản ánh mật độ của quan hệ).

</details>

## Xem thêm / Video gợi ý

- [Cartesian Product](https://www.youtube.com/watch?v=8tShnKOE-1o) — Khan Academy
- [Relations and Functions](https://www.youtube.com/watch?v=JbEpXyH8Y9s) — giới thiệu quan hệ từ tích Descartes

## Tóm tắt

- **Cặp có thứ tự** $$(a,b)$$ khác với tập hợp $$\{a,b\}$$ vì thứ tự hai thành phần mang ý nghĩa xác định.
- **Tích Descartes** $$A \times B$$ là tập hợp mọi cặp $$(a,b)$$ với $$a \in A, b \in B$$, có lực lượng $$\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$$.
- Tích Descartes phân phối tốt qua phép giao: $$(Q \times R) \cap (S \times T) = (Q \cap S) \times (R \cap T)$$, nhưng không có đẳng thức tương tự cho phép hợp.
- **Quan hệ** là một tập con của tích Descartes — nền tảng cho Chương 5 và mô hình bảng trong SQL.
- `CROSS JOIN` tương ứng tích Descartes đầy đủ, còn `JOIN ... ON` là tích có điều kiện lọc.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu ứng dụng của lý thuyết tập hợp trong cơ sở dữ liệu, lập trình và các cấu trúc dữ liệu thực tế.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=NnEkVooAsxk">CARTESIAN PRODUCTS and ORDERED PAIRS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu cặp có thứ tự và tích Descartes.
- <a href="https://www.youtube.com/watch?v=ufjEv-5nmcA">Cartesian Product of Two Sets A x B</a> — Dr. Trefor Bazett, tiếng Anh. Cách liệt kê và đọc tích $$A \times B$$ trên các ví dụ nhỏ trước khi chuyển sang quan hệ.
- <a href="https://www.youtube.com/watch?v=j5fnaXLOkFk">How to do a PROOF with CARTESIAN PRODUCTS - Discrete Mathematics</a> — TrevTutor, tiếng Anh. Hướng dẫn chứng minh đẳng thức có chứa tích Descartes.
