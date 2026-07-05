---

layout: post
title: "Lực lượng Tập hợp và Nguyên lý Bao hàm - Loại trừ"
categories: chapter04
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Ở hai mục trước, chúng ta đã định nghĩa tập hợp và các phép toán hợp, giao, hiệu, phần bù. Mục này mở rộng sang lực lượng tập hợp (cardinality) và nguyên lý…"
---

Ở hai mục trước, chúng ta đã định nghĩa tập hợp và các phép toán hợp, giao, hiệu, phần bù. Mục này mở rộng sang **lực lượng tập hợp** (cardinality) và **nguyên lý bao hàm–loại trừ**. Khi hệ thống tăng quy mô, câu hỏi không còn chỉ là "có những phần tử nào" mà còn là "có bao nhiêu phần tử" — số người dùng hoạt động, số trường hợp test, mức chồng lấn giữa hai tập điều kiện đều là bài toán đếm. Lực lượng cho cách đo kích thước tập, kể cả tập vô hạn. Khi các tập giao nhau, cộng riêng từng phần dẫn đến đếm trùng; nguyên lý bao hàm–loại trừ sửa lỗi đó và xuất hiện trong combinatorics, xác suất và phân tích thuật toán.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tính** lực lượng tập hữu hạn và $$|\mathcal{P}(A)| = 2^{|A|}$$.
- **Phân biệt** tập đếm được và không đếm được (Cantor).
- **Áp dụng** bao hàm–loại trừ cơ bản trên tập.

**Từ khóa**: lực lượng (cardinality), tập lũy thừa, đếm được, không đếm được, diagonal argument.
</div>

## 1. Lực lượng của tập hợp

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Lực lượng** (cardinality) của tập hữu hạn $$A$$, ký hiệu $$\lvert A \rvert$$, là số phần tử phân biệt trong $$A$$.
</div>


**Ký hiệu**:

- $$\lvert A \rvert$$: số phần tử của $$A$$.
- $$\emptyset$$: tập rỗng, có lực lượng 0.
- $$A\subseteq B$$: $$A$$ là tập con của $$B$$.

<div class="textbook-example" markdown="1">
**Ví dụ**:

- Nếu $$A=\{1,3,5,7,9\}$$ thì $$\lvert A \rvert=5$$.
- Nếu $$B=\{x\in\mathbb{N}\mid 1\le x\le 100\}$$ thì $$\lvert B \rvert=100$$.
- $$\lvert \emptyset \rvert=0$$.

![Đếm phần tử trong tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Pascal_triangle.svg)

<p class="textbook-figure-caption" data-figure="4.17">Lực lượng $$\lvert A \rvert$$ đo số phần tử phân biệt — nền tảng cho đếm, thống kê và phân tích quy mô dữ liệu.</p>
**Tính chất cơ bản**:

- Nếu $$A\subseteq B$$ và $$A,B$$ hữu hạn thì $$\lvert A \rvert\le \lvert B \rvert$$.
- Nếu $$A\cap B=\emptyset$$ thì $$\lvert A\cup B \rvert=\lvert A \rvert+\lvert B \rvert$$.
- Tổng quát, nếu hai tập chồng lấn, không được cộng đơn giản.
</div>


## 2. Tập lũy thừa

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Tập lũy thừa** của $$A$$, ký hiệu $$\mathcal{P}(A)$$, là tập tất cả các tập con của $$A$$.
</div>


<div class="textbook-equation" markdown="1">
$$\mathcal{P}(A)=\{X\mid X\subseteq A\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$\lvert A \rvert=n$$ thì $$\lvert \mathcal{P}(A) \rvert=2^n$$.
</div>


![Sơ đồ tập lũy thừa P(A)](/discrete-mathematics-for-computer-science-iuh/img/course/Powerset.svg)

<p class="textbook-figure-caption" data-figure="4.18">Tập lũy thừa $$\mathcal{P}(A)$$ chứa mọi tập con — với $$\lvert A \rvert = n$$ thì $$\lvert \mathcal{P}(A) \rvert = 2^n$$.</p>
### Chứng minh

Mỗi phần tử của $$A$$ có hai lựa chọn khi tạo một tập con: hoặc được chọn, hoặc không được chọn. Với $$n$$ phần tử độc lập, số cách chọn là:

<div class="textbook-equation" markdown="1">
$$2\cdot 2\cdots 2 = 2^n.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vì mỗi cách chọn tương ứng đúng một tập con, nên $$\lvert \mathcal{P}(A) \rvert=2^n$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: Nếu $$A=\{a,b,c\}$$ thì:

<div class="textbook-equation" markdown="1">
$$\mathcal{P}(A)=\{\emptyset,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Có $$2^3=8$$ tập con.
</div>


## 3. Nguyên lý bao hàm - loại trừ cho hai tập

<div class="textbook-theorem" markdown="1">
**Định lý**:
</div>


<div class="textbook-equation" markdown="1">
$$\lvert A\cup B \rvert=\lvert A \rvert+\lvert B \rvert-\lvert A\cap B \rvert.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Diễn giải

Khi cộng $$\lvert A \rvert+\lvert B \rvert$$, các phần tử thuộc $$A\cap B$$ bị đếm hai lần. Vì vậy ta phải trừ đi một lần.

![Nguyên lý bao hàm–loại trừ: hai tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_intersect_B.svg)

<p class="textbook-figure-caption" data-figure="4.19">Vùng giao $$A \cap B$$ bị đếm hai lần khi cộng $$\lvert A \rvert + \lvert B \rvert$$ — phải trừ $$\lvert A \cap B \rvert$$ để đếm đúng $$\lvert A \cup B \rvert$$.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Trong lớp có 40 sinh viên, 25 sinh viên học Python, 18 sinh viên học Java, 10 sinh viên học cả hai. Số sinh viên học ít nhất một trong hai ngôn ngữ là:

<div class="textbook-equation" markdown="1">
$$25+18-10=33.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## 4. Nguyên lý bao hàm - loại trừ cho ba tập

<div class="textbook-theorem" markdown="1">
**Định lý**:
</div>


<div class="textbook-equation" markdown="1">
$$\lvert A\cup B\cup C \rvert=\lvert A \rvert+\lvert B \rvert+\lvert C \rvert-\lvert A\cap B \rvert-\lvert A\cap C \rvert-\lvert B\cap C \rvert+\lvert A\cap B\cap C \rvert.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Khối suy luận

- Cộng $$\lvert A \rvert+\lvert B \rvert+\lvert C \rvert$$: vùng giao đôi bị đếm thừa.
- Trừ các giao đôi: vùng giao ba bị trừ quá nhiều.
- Cộng lại $$\lvert A\cap B\cap C \rvert$$ để cân bằng.

![Nguyên lý bao hàm–loại trừ: ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="4.20">Công thức bao hàm–loại trừ cho 3 tập — cộng từng tập, trừ giao đôi, cộng lại giao ba.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Có 100 sinh viên. 50 học Python, 40 học Java, 30 học C++; 20 học Python và Java, 15 học Python và C++, 10 học Java và C++; 5 học cả ba. Số sinh viên học ít nhất một ngôn ngữ là:

<div class="textbook-equation" markdown="1">
$$50+40+30-20-15-10+5=80.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## 5. Tập vô hạn đếm được

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một tập $$A$$ là **đếm được** nếu các phần tử của nó có thể liệt kê thành một dãy $$a_1,a_2,a_3,\ldots$$, tức tồn tại song ánh giữa $$A$$ và một tập con của $$\mathbb{N}$$.
</div>


<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$\mathbb{N}$$ là đếm được.
- $$\mathbb{Z}$$ là đếm được: $$0,1,-1,2,-2,3,-3,\ldots$$.
- $$\mathbb{Q}$$ là đếm được, dù dày đặc trên trục số.

![Tập đếm được — liệt kê theo thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Countable.vs.Continuum.svg)

<p class="textbook-figure-caption" data-figure="4.21">Tập đếm được có thể đánh số 1, 2, 3, … — ví dụ ℕ, ℤ, ℚ đều đếm được (lực lượng ℵ₀).</p>
</div>

## 6. Tập không đếm được

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một tập là **không đếm được** nếu không thể liệt kê tất cả phần tử của nó bằng một dãy vô hạn đánh số bởi $$\mathbb{N}$$.
</div>


**Ý tưởng đường chéo Cantor**: Tập số thực trong đoạn $$(0,1)$$ không đếm được. Nếu giả sử liệt kê được mọi số thực trong $$(0,1)$$, ta có thể tạo một số mới khác số thứ nhất ở chữ số thập phân thứ nhất, khác số thứ hai ở chữ số thứ hai, và cứ thế. Số mới này không nằm trong danh sách, mâu thuẫn.

![Lập luận đường chéo Cantor](/discrete-mathematics-for-computer-science-iuh/img/course/Diagonal_argument.svg)

<p class="textbook-figure-caption" data-figure="4.22">Phương pháp đường chéo Cantor — xây số mới khác mọi số trong danh sách giả định, chứng minh (0,1) không đếm được.</p>
![Đếm được vs continuum](/discrete-mathematics-for-computer-science-iuh/img/course/Countable.vs.Continuum.svg)

<p class="textbook-figure-caption" data-figure="4.23">So sánh lực lượng — tập đếm được ($$\aleph_0$$) nhỏ hơn continuum ($$2^{\aleph_0} = \lvert \R \rvert$$).</p>
## Định lý Schröder–Bernstein

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu tồn tại hai hàm đơn ánh $$f: A \to B$$ và $$g: B \to A$$, thì tồn tại một song ánh giữa $$A$$ và $$B$$. Nói cách khác:
</div>


<div class="textbook-equation" markdown="1">
$$
\lvert A \rvert \leq \lvert B \rvert \quad \text{và} \quad \lvert B \rvert \leq \lvert A \rvert \quad \implies \quad \lvert A \rvert = \lvert B \rvert.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh (phác thảo)**:

1. Vì $$f$$ là đơn ánh, $$A$$ "nhúng" được vào $$B$$, nên $$\lvert A \rvert \leq \lvert B \rvert$$.

2. Tương tự, $$g$$ đơn ánh nên $$\lvert B \rvert \leq \lvert A \rvert$$.

3. Ý tưởng chứng minh: Xây dựng một song ánh $$h: A \to B$$ bằng cách "ghép" $$f$$ và $$g^{-1}$$ trên các tập con thích hợp (dùng chuỗi tiền ảnh dưới $$g \circ f$$).

   (Chi tiết chứng minh thường dùng định lý điểm cố định hoặc phân hoạch $$A$$ thành các chuỗi và chọn $$f$$ hoặc $$g^{-1}$$ trên từng chuỗi.)

**Hệ quả**:

- $$\lvert \N \rvert = \lvert 2\N \rvert = \lvert \Z \rvert = \lvert \Q \rvert = \aleph_0$$ (tập đếm được).
- $$\lvert \R \rvert = \lvert (0,1) \rvert = \lvert [0,1] \rvert = 2^{\aleph_0}$$ (lực lượng continuum).

**Ý nghĩa CS**:
- So sánh độ phức tạp của không gian trạng thái mà không cần xây dựng song ánh tường minh.
- Dùng trong chứng minh một số bài toán NP-đầy đủ có cùng độ khó.

## 9. Ứng dụng trong Khoa học Máy tính

```python
python = {'An', 'Binh', 'Chi'}
java = {'Binh', 'Dung'}
learns_any = python | java
learns_both = python & java
print(len(learns_any))
```

- **Tìm kiếm và lọc dữ liệu**: `COUNT`, `DISTINCT`, `UNION`, `INTERSECT` đều là thao tác lực lượng.
- **Phân tích thuật toán**: số tập con của một tập $$n$$ phần tử là $$2^n$$, dẫn đến thuật toán vét cạn theo cấp số mũ.
- **Kiểm thử phần mềm**: bao hàm - loại trừ giúp ước lượng số ca test phủ nhiều điều kiện.
- **Lý thuyết tính toán**: tính không đếm được giải thích vì sao có nhiều bài toán hơn số chương trình có thể viết.

## Bài tập thực hành

### Bài tập 1: So sánh lực lượng

Chứng minh rằng tập hợp các số tự nhiên $$\N$$ và tập hợp các số chẵn dương có cùng lực lượng.

<details>
<summary>Đáp án</summary>

Ánh xạ $$f: \N \to 2\N$$, $$f(n) = 2n$$ là song ánh. Do đó $$\lvert \N \rvert = \lvert 2\N \rvert = \aleph_0$$.

</details>

### Bài tập 2: Lực lượng tập con

Tính lực lượng của tập hợp tất cả tập con của $$\{1,2,3\}$$.

<details>
<summary>Đáp án</summary>

$$2^3 = 8$$ tập con (bao gồm cả tập rỗng và tập đầy đủ).

</details>

### Bài tập 3: Ứng dụng bao hàm - loại trừ

Có 50 sinh viên học Python, 40 học Java, 30 học cả hai. Hỏi có bao nhiêu sinh viên học ít nhất một ngôn ngữ?

<details>
<summary>Đáp án</summary>

$$\lvert P \cup J \rvert = 50 + 40 - 30 = 60$$.

</details>


## Xem thêm / Video gợi ý

- [Set Theory — Cardinality and Infinity](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Numberphile (Hilbert's Hotel)
- [Introduction to Sets](https://www.youtube.com/watch?v=4l7L9v0p0Q) — Khan Academy (Basics + notation)

## Tóm tắt

- **Lực lượng** $$|A|$$ đo số phần tử; với tập hữu hạn $$n$$ phần tử, $$|\mathcal{P}(A)| = 2^n$$.
- **Nguyên lý bao hàm–loại trừ**: $$|A \cup B| = |A| + |B| - |A \cap B|$$; mở rộng cho ba tập và nhiều tập.
- Tập **đếm được** (ℕ, ℤ, ℚ) có thể liệt kê bởi ℕ; tập **không đếm được** (ℝ, (0,1)) — lập luận đường chéo Cantor.
- **Định lý Schröder–Bernstein**: nếu $$|A| \leq |B|$$ và $$|B| \leq |A|$$ thì $$|A| = |B|$$.
- Ứng dụng CS: phân tích không gian trạng thái $$2^n$$, đếm test case, giới hạn tính toán.
