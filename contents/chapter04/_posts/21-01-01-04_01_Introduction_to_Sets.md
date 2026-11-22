---

layout: post
title: "Giới thiệu Tập hợp"
categories: chapter04
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Giới thiệu các khái niệm nền tảng của lý thuyết tập hợp: phần tử, cách biểu diễn tập hợp, tập con, lực lượng, tập lũy thừa và cách biểu diễn tập trên máy tính."
---

<div class="textbook-epigraph" markdown="1">

"A set is a many that allows itself to be thought of as a one."

<span class="epigraph-attribution">— Georg Cantor</span>

</div>

Trong chương này, chúng ta xây dựng **lý thuyết tập hợp** — nền tảng của toán học rời rạc và khoa học máy tính. Khi viết truy vấn SQL, lọc người dùng theo vai trò, lưu danh sách các nút đã duyệt trong thuật toán, hay mô tả tập ký tự hợp lệ của trình phân tích cú pháp, ta đều đang làm việc với cùng một khái niệm: **tập hợp**. Tập hợp giúp xác định rạch ròi phần tử nào thuộc nhóm và phần tử nào không — đó là ngôn ngữ cơ sở của dữ liệu, quan hệ, hàm số, xác suất và đồ thị. Nếu thiếu tư duy tập hợp, các phát biểu kỹ thuật dễ trở nên mơ hồ; hai điều kiện trông tương tự nhau có thể cho kết quả khác hẳn chỉ vì miền giá trị khác nhau. Mục 4.1 bắt đầu từ khái niệm phần tử, ký hiệu, cách biểu diễn và các loại tập hợp quen thuộc.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** khái niệm tập hợp và phần tử của tập hợp.
- **Sử dụng** chính xác các ký hiệu: $$\in$$, $$\notin$$, $$\subseteq$$, $$\emptyset$$.
- **Biểu diễn** tập hợp bằng ba cách: liệt kê, mô tả tính chất và ký hiệu khoảng.
- **Phân biệt** các tập hợp số cơ bản: $$\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$$.
- **Xác định** quan hệ tập con, hai tập hợp bằng nhau và lực lượng tập hợp.
- **Áp dụng** khái niệm tập hợp trong lập trình Python và biểu diễn bằng xâu bit.
</div>

## Định nghĩa Tập hợp

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Tập hợp là một tập trung các đối tượng phân biệt, được gọi là các **phần tử** (elements) của tập hợp.
</div>


> Georg Cantor mô tả tập hợp một cách trực quan: "Một tập hợp là sự kết hợp thành một tổng thể của những đối tượng xác định, phân biệt thuộc trực giác hay tư duy của chúng ta."

![Georg Cantor — cha đẻ lý thuyết tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Georg_Cantor_1894.jpg)

<p class="textbook-figure-caption" data-figure="4.1">Georg Cantor (1845–1918), nhà toán học người Đức, người đặt nền móng cho lý thuyết tập hợp hiện đại.</p>
### Ký hiệu cơ bản

- Tập hợp: $$A, B, C, \ldots$$ (chữ cái in hoa).
- Phần tử: $$a, b, c, \ldots$$ (chữ cái thường).
- Quan hệ thuộc: $$a \in A$$ ($$a$$ là phần tử của $$A$$).
- Quan hệ không thuộc: $$a \notin A$$ ($$a$$ không thuộc $$A$$).

## Cách biểu diễn tập hợp

### Liệt kê (Roster Method)

Ta liệt kê tất cả các phần tử bên trong cặp dấu ngoặc nhọn. Cách này trực quan và thuận tiện khi tập hợp có ít phần tử.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$A = \{1, 2, 3, 4, 5\}$$
- $$B = \{a, e, i, o, u\}$$ (tập các nguyên âm tiếng Anh)
- $$C = \{\text{đỏ}, \text{xanh}, \text{vàng}\}$$

![Các phần tử riêng biệt trong một tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="4.2">Phương pháp liệt kê — mỗi phần tử trong tập hợp là riêng biệt và được ghi trong cặp dấu ngoặc nhọn.</p>
</div>

### Mô tả tính chất (Set-Builder Notation)

Ta xác định tập hợp thông qua tính chất đặc trưng của các phần tử. Cách này đặc biệt hữu ích khi tập hợp có rất nhiều phần tử hoặc là tập vô hạn.

**Cú pháp**: `{x | P(x)}` hoặc `{x : P(x)}`, đọc là "tập hợp các $$x$$ sao cho $$P(x)$$ đúng".

![Biểu đồ Venn 3 tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="4.3">Biểu đồ Venn minh họa quan hệ giữa 3 tập hợp cùng các vùng giao (intersection) và hợp (union).</p>
<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$A = \{x \mid x \text{ là số nguyên và } 1 \le x \le 5\}$$
- $$B = \{x \mid x^2 = 4\}$$
- $$C = \{n \in \mathbb{N} \mid n \text{ là số chẵn}\}$$
</div>


### Sử dụng khoảng (cho tập con của số thực)

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$[0, 1] = \{x \in \mathbb{R} \mid 0 \le x \le 1\}$$
- $$(0, 1) = \{x \in \mathbb{R} \mid 0 < x < 1\}$$
- $$[0, \infty) = \{x \in \mathbb{R} \mid x \ge 0\}$$

![Ký hiệu khoảng trên trục số thực](/discrete-mathematics-for-computer-science-iuh/img/course/Interval.svg)

<p class="textbook-figure-caption" data-figure="4.4">Minh họa khoảng đóng [a, b], khoảng mở (a, b) và khoảng nửa mở trên trục số thực.</p>
</div>

### Tập hợp con (Subset)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A \subseteq B$$ nếu mọi phần tử của $$A$$ đều thuộc $$B$$.
</div>


**Ký hiệu**:
- $$A \subseteq B$$: $$A$$ là tập con của $$B$$.
- $$A \subset B$$: $$A$$ là tập con thực sự của $$B$$ ($$A \subseteq B$$ và $$A \ne B$$).

**Tính chất**:
- $$\emptyset \subseteq A$$ với mọi tập hợp $$A$$.
- $$A \subseteq A$$ với mọi tập hợp $$A$$.
- Nếu $$A \subseteq B$$ và $$B \subseteq C$$ thì $$A \subseteq C$$ (tính bắc cầu).

![Biểu đồ Venn: A là tập con của B](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_subset_B.svg)

<p class="textbook-figure-caption" data-figure="4.5">Khi A ⊆ B, mọi phần tử của A đều nằm bên trong vùng biểu diễn của B trên biểu đồ Venn.</p>
![Ký hiệu tập rỗng ∅](/discrete-mathematics-for-computer-science-iuh/img/course/Empty_set.svg)

<p class="textbook-figure-caption" data-figure="4.6">Tập rỗng ∅ — tập hợp không chứa phần tử nào, đồng thời là tập con của mọi tập hợp.</p>
<div class="content-box example-box textbook-block" markdown="1">
**Ví dụ minh họa**: Cho $$A = \{a, b\}$$, liệt kê tất cả các tập con của $$A$$.

Các tập con gồm: $$\emptyset, \{a\}, \{b\}, \{a, b\}$$ (tổng cộng 4 tập con).

Trong Python:
```python
A = {'a', 'b'}
# Kiểm tra quan hệ tập con:
print({'a'}.issubset(A))  # True
print({'c'}.issubset(A))  # False
```
</div>

### Tập hợp bằng nhau

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A = B$$ khi và chỉ khi $$A \subseteq B$$ và $$B \subseteq A$$.
</div>


Đây cũng là phương pháp phổ biến nhất để chứng minh hai tập hợp bằng nhau: chứng minh từng chiều bao hàm $$A \subseteq B$$ và $$B \subseteq A$$.

### Lực lượng (Cardinality)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Số phần tử của tập hữu hạn $$A$$ được gọi là **lực lượng** của $$A$$, ký hiệu $$\lvert A \rvert$$ hoặc $$\#A$$.
</div>


<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$\lvert \{1, 2, 3\} \rvert = 3$$
- $$\lvert \emptyset \rvert = 0$$
- $$\lvert \mathbb{N} \rvert = \infty$$ (vô hạn đếm được — sẽ học chi tiết ở mục 4.3)
</div>


<div class="content-box insight-box textbook-block" markdown="1">
**Lực lượng trong khoa học máy tính**: Hàm `len(set([1, 2, 3]))` trong Python trả về `3` — chính là lực lượng của tập hợp. Trong cơ sở dữ liệu, truy vấn `SELECT COUNT(*) FROM table` cũng tính lực lượng của bảng.
</div>

### Minh họa tương tác

Bấm vào từng vùng trên biểu đồ Venn để thêm hoặc bớt phần tử, hoặc nhập biểu thức tập hợp để quan sát vùng tương ứng được tô màu.

<div class="interactive-demo" markdown="1">
<div data-demo="venn-explainer" data-sets="2" data-expr="A ∪ B"></div>
</div>
<script src="{{ '/public/js/explainers/venn-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Nhận diện phần tử

Cho $$A = \{1, 3, 5, 7, 9\}$$. Xác định tính đúng sai của các khẳng định sau:

a) $$3 \in A$$  
b) $$2 \in A$$  
c) $$6 \notin A$$  
d) $$\emptyset \in A$$

<details>
<summary>Đáp án</summary>

a) Đúng, vì 3 là một phần tử của $$A$$.  
b) Sai, vì 2 không nằm trong $$A$$.  
c) Đúng, vì 6 không thuộc $$A$$.  
d) Sai, vì $$\emptyset$$ (tập rỗng) không phải là phần tử của $$A$$ (các phần tử của $$A$$ đều là số nguyên, không phải tập hợp; tuy nhiên $$\emptyset \subseteq A$$ thì đúng).
</details>

### Bài tập 2: Biểu diễn tập hợp

Viết các tập hợp sau dưới dạng liệt kê và dạng mô tả tính chất:

a) Tập các số tự nhiên chẵn nhỏ hơn 10.  
b) Tập các ước nguyên dương của 12.

<details>
<summary>Đáp án</summary>

a) Liệt kê: $$\{0, 2, 4, 6, 8\}$$.  
   Mô tả: $$A = \{n \in \mathbb{N}_0 \mid n \text{ là số chẵn và } n < 10\}$$ hoặc $$A = \{2k \mid k \in \mathbb{N}_0,\, 2k < 10\}$$.

b) Liệt kê: $$\{1, 2, 3, 4, 6, 12\}$$.  
   Mô tả: $$B = \{n \in \mathbb{N} \mid n \ge 1 \text{ và } 12 \text{ chia hết cho } n\}$$.
</details>

### Bài tập 3: Quan hệ tập con

Cho $$A = \{1, 2, 3, 4\}$$. Tìm tất cả các tập con của $$A$$ có đúng 2 phần tử.

<details>
<summary>Đáp án</summary>

Có 6 tập con: $$\{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\}$$.

Tổng quát, với tập có $$\lvert A \rvert = n$$, số tập con gồm đúng $$k$$ phần tử là $$C(n,k) = \frac{n!}{k!(n-k)!}$$. Ở đây $$C(4,2) = \frac{4!}{2!2!} = 6$$.
</details>

### Bài tập 4: Lập trình

Viết hàm Python `is_subset(A, B)` kiểm tra xem tập `A` có phải là tập con của `B` hay không.

<details>
<summary>Đáp án</summary>

```python
def is_subset(A, B):
    """Kiểm tra A có phải tập con của B không"""
    for element in A:
        if element not in B:
            return False
    return True

# Kiểm tra
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(is_subset(A, B))  # True

# Cách ngắn hơn với phương thức tích hợp:
print(A.issubset(B))  # True
```
</details>

### Bài tập 5: Tập lũy thừa (Power Set)

**A.2** Tập lũy thừa của một tập hợp $$S$$ là $$\text{pow}(S) = \{T : T \subseteq S\}$$ — tập hợp tất cả các tập con của $$S$$. Ví dụ, $$\text{pow}(\{1, 2, 3\}) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}$$.

(a) Liệt kê tất cả các phần tử của $$\text{pow}(\text{pow}(\{1\}))$$.

(b) Khẳng định $$S \cap T \in \text{pow}(S) \cap \text{pow}(T)$$ có đúng với mọi tập hợp $$S$$ và $$T$$ không? Giải thích.

(c) Khẳng định $$S \cup T \in \text{pow}(S) \cup \text{pow}(T)$$ có đúng với mọi tập hợp $$S$$ và $$T$$ không? Giải thích.

<details>
<summary>Đáp án</summary>

(a) Ta có $$\text{pow}(\{1\}) = \{\emptyset, \{1\}\}$$. Do đó:
$$\text{pow}(\text{pow}(\{1\})) = \{\emptyset, \{\emptyset\}, \{\{1\}\}, \{\emptyset, \{1\}\}\}$$.

(b) **Đúng.** Vì $$S \cap T \subseteq S$$ nên theo định nghĩa tập lũy thừa, $$S \cap T \in \text{pow}(S)$$. Tương tự, vì $$S \cap T \subseteq T$$ nên $$S \cap T \in \text{pow}(T)$$. Do đó, $$S \cap T \in \text{pow}(S) \cap \text{pow}(T)$$.

(c) **Sai.** Lấy phản ví dụ $$S = \{1\}$$ và $$T = \{2\}$$. Khi đó $$S \cup T = \{1, 2\} \notin \text{pow}(S) \cup \text{pow}(T)$$ vì $$\{1, 2\}$$ không phải tập con của $$S$$ và cũng không phải tập con của $$T$$.

</details>

## Định lý: Số tập con của một tập hợp hữu hạn

![Sơ đồ tập lũy thừa (power set)](/discrete-mathematics-for-computer-science-iuh/img/course/Powerset.svg)

<p class="textbook-figure-caption" data-figure="4.7">Tập lũy thừa P(S) gồm tất cả các tập con của S — nếu |S| = n thì |P(S)| = 2ⁿ.</p>
<div class="textbook-theorem" markdown="1">
**Định lý**: Một tập hợp hữu hạn $$A$$ có đúng $$2^{\vert A\vert }$$ tập con (bao gồm cả $$\emptyset$$ và $$A$$).
</div>


<div class="textbook-proof" markdown="1">
**Chứng minh**:

Giả sử $$A = \{a_1, a_2, \dots, a_n\}$$ với $$\vert A\vert = n$$.

1. Mỗi tập con $$B \subseteq A$$ được xác định duy nhất bằng cách quyết định có chọn từng phần tử $$a_i$$ hay không.
2. Với mỗi $$a_i$$, có đúng 2 lựa chọn: $$a_i \in B$$ hoặc $$a_i \notin B$$.
3. Theo nguyên lý nhân, tổng số tập con của $$A$$ là:
   $$
   2 \times 2 \times \cdots \times 2 \quad (n \text{ lần}) = 2^n.
   $$
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả**:
- $$\vert A\vert = 0$$ (tập rỗng): có $$2^0 = 1$$ tập con (chính là $$\emptyset$$).
- $$\vert A\vert = 1$$: có 2 tập con.
- $$\vert A\vert = 10$$: có $$2^{10} = 1024$$ tập con.
- $$\vert A\vert = 20$$: có $$2^{20} = 1{,}048{,}576$$ tập con (hơn 1 triệu).
</div>

**Ý nghĩa trong khoa học máy tính**:
- Không gian trạng thái của một hệ thống $$n$$ bit gồm $$2^n$$ trạng thái.
- Tập con xuất hiện trực tiếp trong nhiều bài toán thuật toán (tổng tập con, bài toán cái túi), cơ sở dữ liệu và chọn đặc trưng (feature selection) trong học máy.

### Tập lũy thừa và tính chất

Cho tập $$X$$, tập hợp tất cả các tập con của $$X$$ được gọi là **tập lũy thừa**, ký hiệu $$P(X)$$ (hoặc $$\mathcal{P}(X)$$). Ví dụ, với $$X = \{0, 1, 2\}$$:

$$P(X) = \{\emptyset, \{0\}, \{1\}, \{2\}, \{0,1\}, \{0,2\}, \{1,2\}, \{0,1,2\}\}.$$

**Tính chất:**
- Nếu $$X \subset Y$$ thì $$P(X) \subset P(Y)$$.
- Nếu $$\lvert X \rvert = n$$ thì $$\lvert P(X) \rvert = 2^n$$.

### Biểu diễn tập hợp trên máy tính bằng xâu bit

Khi tập vũ trụ $$U$$ là hữu hạn, một cách biểu diễn tập hợp hiệu quả trên máy tính là dùng **xâu bit** (bit vector). Giả sử các phần tử của $$U = \{a_1, a_2, \ldots, a_n\}$$ được sắp theo một thứ tự cố định. Mỗi tập con $$A \subseteq U$$ được biểu diễn bằng một xâu bit độ dài $$n$$, trong đó bit thứ $$i$$ bằng `1` nếu $$a_i \in A$$ và bằng `0` nếu $$a_i \notin A$$.

**Ví dụ:** Với $$U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$$ xếp tăng dần:
- $$A = \{1, 2, 3, 4, 5\} \rightarrow \text{11111 00000}$$
- $$B = \{1, 3, 5, 7, 9\} \rightarrow \text{10101 01010}$$

Khi đó các phép toán tập hợp trở thành phép toán bit trực tiếp:
- Hợp $$A \cup B$$ tương ứng phép `OR` theo từng bit: `11111 00000 ∨ 10101 01010 = 11111 01010` $$\rightarrow \{1, 2, 3, 4, 5, 7, 9\}$$.
- Giao $$A \cap B$$ tương ứng phép `AND` theo từng bit: `11111 00000 ∧ 10101 01010 = 10101 00000` $$\rightarrow \{1, 3, 5\}$$.

Trong cách biểu diễn này, tập rỗng $$\emptyset$$ ứng với xâu toàn bit `0`, còn tập vũ trụ $$U$$ ứng với xâu toàn bit `1`. Kỹ thuật này được dùng phổ biến trong lập trình với bitmask và các cấu trúc như Bloom filter.

## Các tập hợp số quan trọng

Trong toán học và khoa học máy tính, các tập số cơ bản lồng nhau theo thứ tự sau:

![Sơ đồ các tập hợp số ℕ, ℤ, ℚ, ℝ, ℂ](/discrete-mathematics-for-computer-science-iuh/img/course/Euler_diagram_of_number_sets.svg)

<p class="textbook-figure-caption" data-figure="4.8">Quan hệ bao hàm giữa các tập số: số tự nhiên ℕ ⊂ số nguyên ℤ ⊂ số hữu tỷ ℚ ⊂ số thực ℝ ⊂ số phức ℂ.</p>
## Xem thêm / Video gợi ý

- [Set Theory — Cardinality and Infinity](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Numberphile (Hilbert's Hotel)
- [Introduction to Sets](https://www.youtube.com/watch?v=4l7L9v0p0Q) — Khan Academy (Basics + notation)

## Tóm tắt

- **Tập hợp** là tập trung các phần tử phân biệt, không xét thứ tự hay số lần lặp.
- Ba cách biểu diễn phổ biến: **liệt kê**, **mô tả tính chất** và **ký hiệu khoảng**.
- **Tập rỗng** $$\emptyset$$ không chứa phần tử nào và là tập con của mọi tập hợp.
- **Tập con** $$A \subseteq B$$ nghĩa là mọi phần tử của $$A$$ đều thuộc $$B$$; tập hữu hạn có $$n$$ phần tử có đúng $$2^n$$ tập con.
- **Lực lượng** $$\lvert A \rvert$$ là số phần tử của tập hữu hạn $$A$$.
- Quan hệ các tập số cơ bản: $$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu các phép toán trên tập hợp: hợp, giao, hiệu, phần bù và hiệu đối xứng.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=tyDKR4FG3Yw">INTRODUCTION to SET THEORY - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu ký hiệu tập hợp, phần tử và các ví dụ mở đầu.
- <a href="https://www.youtube.com/watch?v=B1v2-nGXNzs">Intro to Sets | Examples, Notation &amp; Properties</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày cách liệt kê và các tính chất cơ bản của tập hợp.
- <a href="https://www.youtube.com/watch?v=H5D6EAezsXQ">SUBSETS AND POWER SETS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu tập con và tập lũy thừa, làm nền cho nội dung lực lượng ở mục sau.
