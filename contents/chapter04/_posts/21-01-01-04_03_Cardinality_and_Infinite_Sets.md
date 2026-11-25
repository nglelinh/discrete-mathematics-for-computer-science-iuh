---

layout: post
title: "Lực lượng Tập hợp và Nguyên lý Bao hàm - Loại trừ"
categories: chapter04
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Trình bày lực lượng tập hợp, tập lũy thừa, nguyên lý bao hàm–loại trừ cho hai và ba tập, tập đếm được và không đếm được, lập luận đường chéo Cantor và định lý Schröder–Bernstein."
---

Đếm số phần tử của một tập hữu hạn thì dễ—nhưng làm sao so sánh kích thước của hai **tập vô hạn** như tập số tự nhiên $\mathbb{N}$, tập số chẵn, tập số hữu tỉ $\mathbb{Q}$ và tập số thực $\mathbb{R}$? Georg Cantor đã làm rung chuyển toàn bộ nền toán học thế kỷ 19 khi chứng minh rằng **có những cái vô hạn lớn hơn cái vô hạn khác**—và chính kỹ thuật **đường chéo hóa (diagonalization)** của ông sau này đã giúp Alan Turing chứng minh tồn tại những bài toán *không một máy tính nào giải được*!

## Bản đồ kiến thức nền: Bốn trụ cột của Lực lượng (Cardinality) & Tập Vô hạn

1. **So sánh lực lượng bằng Song ánh (Bijection)**:
   Hai tập $A$ và $B$ có cùng lực lượng ($\vert A \vert = \vert B \vert$) khi và chỉ khi tồn tại một ánh xạ 1–1 và lên (song ánh) giữa chúng—một định nghĩa hoạt động mượt mà cho cả tập hữu hạn lẫn vô hạn!

2. **Tập đếm được (Countable — $\aleph_0$)**:
   Một tập vô hạn là **đếm được** nếu ta có thể lập danh sách đánh số $a_1, a_2, a_3, \dots$ khớp 1–1 với $\mathbb{N}$. Điều kỳ diệu: tập số nguyên $\mathbb{Z}$ và cả tập phân số $\mathbb{Q}$ đều **đếm được** (cùng kích thước với $\mathbb{N}$!).

3. **Tập không đếm được (Uncountable) & Lập luận đường chéo Cantor**:
   Tập số thực $\mathbb{R}$ và tập lũy thừa $\mathcal{P}(\mathbb{N})$ là **không đếm được**: mọi nỗ lực lập danh sách toàn bộ chúng đều bỏ sót ít nhất một phần tử mới tạo ra bằng cách lật chữ số/bit trên đường chéo chính.

4. **Hệ quả chấn động cho Khoa học Máy tính**:
   Tập tất cả các chương trình máy tính hợp lệ (chuỗi ký tự hữu hạn) là **đếm được** ($\aleph_0$), nhưng tập tất cả các bài toán quyết định $f: \mathbb{N} \to \{0, 1\}$ là **không đếm được** ($2^{\aleph_0}$) ⇒ **tồn tại vô số bài toán không thể tính toán được (uncomputable)!**

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tính** lực lượng của tập hữu hạn và áp dụng công thức $$\vert \mathcal{P}(A)\vert = 2^{\vert A\vert }$$.
- **Phân biệt** tập vô hạn đếm được và tập không đếm được theo lập luận của Cantor.
- **Áp dụng** nguyên lý bao hàm–loại trừ cho hai và ba tập hợp.

**Từ khóa**: lực lượng (cardinality), tập lũy thừa, tập đếm được, tập không đếm được, lập luận đường chéo (diagonal argument).
</div>

## Lực lượng của tập hợp

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Lực lượng** (cardinality) của một tập hữu hạn $$A$$, ký hiệu $$\lvert A \rvert$$, là số phần tử phân biệt trong $$A$$.
</div>


**Ký hiệu**:

- $$\lvert A \rvert$$: số phần tử của $$A$$.
- $$\emptyset$$: tập rỗng, có lực lượng bằng 0.
- $$A \subseteq B$$: $$A$$ là tập con của $$B$$.

<div class="textbook-example" markdown="1">
**Ví dụ**:

- Nếu $$A=\{1,3,5,7,9\}$$ thì $$\lvert A \rvert=5$$.
- Nếu $$B=\{x\in\mathbb{N}\mid 1\le x\le 100\}$$ thì $$\lvert B \rvert=100$$.
- $$\lvert \emptyset \rvert=0$$.

![Đếm phần tử trong tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Pascal_triangle.svg)

<p class="textbook-figure-caption" data-figure="4.17">Lực lượng $$\lvert A \rvert$$ đo số phần tử phân biệt — nền tảng cho bài toán đếm, thống kê và phân tích quy mô dữ liệu.</p>
**Tính chất cơ bản**:

- Nếu $$A\subseteq B$$ và $$A,B$$ là các tập hữu hạn thì $$\lvert A \rvert\le \lvert B \rvert$$.
- Nếu $$A\cap B=\emptyset$$ thì $$\lvert A\cup B \rvert=\lvert A \rvert+\lvert B \rvert$$.
- Tổng quát, khi hai tập có phần giao khác rỗng, ta không thể cộng trực tiếp lực lượng của từng tập.
</div>


## Tập lũy thừa

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Tập lũy thừa** của $$A$$, ký hiệu $$\mathcal{P}(A)$$, là tập hợp tất cả các tập con của $$A$$.
</div>


<div class="textbook-equation" markdown="1">
$$\mathcal{P}(A)=\{X\mid X\subseteq A\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$\lvert A \rvert=n$$ thì $$\lvert \mathcal{P}(A) \rvert=2^n$$.
</div>


![Sơ đồ tập lũy thừa P(A)](/discrete-mathematics-for-computer-science-iuh/img/course/Powerset.svg)

<p class="textbook-figure-caption" data-figure="4.18">Tập lũy thừa $$\mathcal{P}(A)$$ chứa mọi tập con của $$A$$ — với $$\lvert A \rvert = n$$ thì $$\lvert \mathcal{P}(A) \rvert = 2^n$$.</p>
<div class="textbook-proof" id="chứng-minh" markdown="1">
**Chứng minh**: Để tạo một tập con của $$A$$, mỗi phần tử trong $$A$$ có hai lựa chọn độc lập: được chọn hoặc không được chọn. Với $$n$$ phần tử, tổng số cách chọn là:

<div class="textbook-equation" markdown="1">
$$2\cdot 2\cdots 2 = 2^n.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vì mỗi cách chọn tương ứng với đúng một tập con, suy ra $$\lvert \mathcal{P}(A) \rvert=2^n$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Nếu $$A=\{a,b,c\}$$ thì:

<div class="textbook-equation" markdown="1">
$$\mathcal{P}(A)=\{\emptyset,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Tập này có $$2^3=8$$ phần tử.
</div>


### Khung giải thích (nên đọc chậm): Tự tay dựng số bị bỏ sót bằng Lập luận đường chéo Cantor trên 4 chuỗi nhị phân

Giả sử ai đó tuyên bố đã lập được danh sách đánh số **tất cả** các chuỗi nhị phân vô hạn (tương ứng với các tập con của $\mathbb{N}$), bắt đầu bằng 4 dòng đầu:
- $s_1 = \mathbf{0}\, 1\, 0\, 1\, \dots$
- $s_2 = 1\, \mathbf{1}\, 1\, 0\, \dots$
- $s_3 = 0\, 0\, \mathbf{0}\, 1\, \dots$
- $s_4 = 1\, 0\, 1\, \mathbf{1}\, \dots$

Hãy dựng chuỗi mới $d$ bằng quy tắc: **lấy bit thứ $i$ của chuỗi $s_i$ trên đường chéo chính rồi lật ngược (`0 → 1`, `1 → 0`)**:
- Vị trí 1: $s_1[1] = \mathbf{0} \implies d[1] = \mathbf{1}$ (chắc chắn $d \neq s_1$!).
- Vị trí 2: $s_2[2] = \mathbf{1} \implies d[2] = \mathbf{0}$ (chắc chắn $d \neq s_2$!).
- Vị trí 3: $s_3[3] = \mathbf{0} \implies d[3] = \mathbf{1}$ (chắc chắn $d \neq s_3$!).
- Vị trí 4: $s_4[4] = \mathbf{1} \implies d[4] = \mathbf{0}$ (chắc chắn $d \neq s_4$!).

Vậy $d = 1\, 0\, 1\, 0\, \dots$ **khác mọi chuỗi $s_k$ ở ít nhất vị trí thứ $k$**, nên $d$ không thể xuất hiện ở bất kỳ dòng nào trong danh sách! Mâu thuẫn này chứng minh tập chuỗi nhị phân vô hạn là **không đếm được**.

## Nguyên lý bao hàm - loại trừ cho hai tập

<div class="textbook-theorem" markdown="1">
**Định lý**:


<div class="textbook-equation" markdown="1">
$$\lvert A\cup B \rvert=\lvert A \rvert+\lvert B \rvert-\lvert A\cap B \rvert.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

### Diễn giải

Khi cộng $$\lvert A \rvert+\lvert B \rvert$$, mỗi phần tử thuộc phần giao $$A\cap B$$ bị đếm hai lần. Do đó ta trừ đi $$\lvert A\cap B \rvert$$ một lần để mỗi phần tử trong $$A \cup B$$ chỉ được đếm đúng một lần.

![Nguyên lý bao hàm–loại trừ: hai tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_intersect_B.svg)

<p class="textbook-figure-caption" data-figure="4.19">Vùng giao $$A \cap B$$ bị đếm hai lần khi cộng $$\lvert A \rvert + \lvert B \rvert$$, nên cần trừ $$\lvert A \cap B \rvert$$ để tính đúng $$\lvert A \cup B \rvert$$.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Trong lớp có 40 sinh viên, trong đó 25 sinh viên học Python, 18 sinh viên học Java và 10 sinh viên học cả hai ngôn ngữ. Số sinh viên học ít nhất một trong hai ngôn ngữ là:

<div class="textbook-equation" markdown="1">
$$25+18-10=33.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## Nguyên lý bao hàm - loại trừ cho ba tập

<div class="textbook-theorem" markdown="1">
**Định lý**:


<div class="textbook-equation" markdown="1">
$$\lvert A\cup B\cup C \rvert=\lvert A \rvert+\lvert B \rvert+\lvert C \rvert-\lvert A\cap B \rvert-\lvert A\cap C \rvert-\lvert B\cap C \rvert+\lvert A\cap B\cap C \rvert.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

### Ý tưởng suy luận

- Cộng $$\lvert A \rvert+\lvert B \rvert+\lvert C \rvert$$ khiến các vùng giao đôi bị đếm hai lần và vùng giao ba bị đếm ba lần.
- Trừ đi ba vùng giao đôi giúp sửa phần giao đôi, nhưng lại trừ vùng giao ba đúng ba lần (thành 0 lần).
- Cộng lại $$\lvert A\cap B\cap C \rvert$$ để vùng giao ba được đếm đúng một lần.

![Nguyên lý bao hàm–loại trừ: ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="4.20">Công thức bao hàm–loại trừ cho 3 tập: cộng từng tập, trừ các giao đôi, rồi cộng lại phần giao ba.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Trong nhóm 100 sinh viên, có 50 bạn học Python, 40 bạn học Java, 30 bạn học C++; 20 bạn học Python và Java, 15 bạn học Python và C++, 10 bạn học Java và C++; 5 bạn học cả ba ngôn ngữ. Số sinh viên học ít nhất một ngôn ngữ là:

<div class="textbook-equation" markdown="1">
$$50+40+30-20-15-10+5=80.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## Tập vô hạn đếm được

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một tập hợp $$A$$ được gọi là **đếm được** nếu các phần tử của nó có thể liệt kê thành một dãy $$a_1,a_2,a_3,\ldots$$, tức tồn tại song ánh giữa $$A$$ và một tập con của $$\mathbb{N}$$.
</div>


<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$\mathbb{N}$$ là tập đếm được.
- $$\mathbb{Z}$$ là tập đếm được, vì có thể liệt kê theo thứ tự $$0,1,-1,2,-2,3,-3,\ldots$$
- $$\mathbb{Q}$$ là tập đếm được, mặc dù các số hữu tỷ phân bố dày đặc trên trục số.

![Tập đếm được — liệt kê theo thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Countable.vs.Continuum.svg)

<p class="textbook-figure-caption" data-figure="4.21">Tập đếm được có thể đánh số 1, 2, 3, … — các tập ℕ, ℤ, ℚ đều đếm được với lực lượng ℵ₀.</p>
</div>

### Video ngắn: Đường chéo Cantor

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/cantor-diagonal.mp4"></video>
</div>

Video dài khoảng 2 phút 57 giây: xếp $$\mathbb{Z}$$ thành một hàng $$0, 1, -1, 2, -2, \dots$$, khách sạn Hilbert, đường zigzag liệt kê $$\mathbb{Q}$$ (bỏ qua phân số chưa tối giản), lập luận đường chéo trên bảng các dãy 0/1 để dựng một dãy nằm ngoài mọi danh sách, cùng ý tưởng với số thực trong $$(0,1)$$ để có $$|\mathbb{N}| < |\mathbb{R}|$$ và $$|A| < |\mathcal{P}(A)|$$, rồi bảng chương trình – đầu vào cho thấy bài toán dừng không giải được.

## Tập không đếm được

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một tập hợp là **không đếm được** nếu không thể liệt kê tất cả các phần tử của nó bằng một dãy vô hạn đánh số bởi $$\mathbb{N}$$.
</div>


**Ý tưởng đường chéo Cantor**: Tập các số thực trong khoảng $$(0,1)$$ không đếm được. Nếu giả sử có thể liệt kê hết mọi số thực trong $$(0,1)$$ thành một danh sách đánh số bởi $$1, 2, 3, \ldots$$, ta xây dựng một số thực mới trong $$(0,1)$$ khác số thứ nhất ở chữ số thập phân thứ nhất, khác số thứ hai ở chữ số thập phân thứ hai, và cứ tiếp tục như vậy. Số mới này không thể trùng với bất kỳ số nào trong danh sách, dẫn đến mâu thuẫn.

![Lập luận đường chéo Cantor](/discrete-mathematics-for-computer-science-iuh/img/course/Diagonal_argument.svg)

<p class="textbook-figure-caption" data-figure="4.22">Phương pháp đường chéo Cantor — xây dựng một số mới khác mọi số trong danh sách giả định để chứng minh (0,1) không đếm được.</p>
![Đếm được vs continuum](/discrete-mathematics-for-computer-science-iuh/img/course/Countable.vs.Continuum.svg)

<p class="textbook-figure-caption" data-figure="4.23">So sánh lực lượng — tập đếm được ($$\aleph_0$$) có lực lượng nhỏ hơn lực lượng continuum ($$2^{\aleph_0} = \lvert \mathbb{R} \rvert$$).</p>
### Thử nghiệm: Đường chéo Cantor, khách sạn Hilbert và hàm ghép cặp

Đảo các bit trên đường chéo để tạo một dãy nhị phân không nằm trong danh sách; sắp xếp khách mới vào khách sạn vô hạn; hoặc xem cách ghép cặp $$\mathbb{N} \times \mathbb{N}$$ với $$\mathbb{N}$$.

<div class="interactive-demo" markdown="1">
<div data-demo="infinity-explainer" data-tab="diagonal"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Định lý Schröder–Bernstein

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu tồn tại hai đơn ánh $$f: A \to B$$ và $$g: B \to A$$, thì tồn tại một song ánh giữa $$A$$ và $$B$$. Nói cách khác:


<div class="textbook-equation" markdown="1">
$$
\lvert A \rvert \leq \lvert B \rvert \quad \text{và} \quad \lvert B \rvert \leq \lvert A \rvert \quad \implies \quad \lvert A \rvert = \lvert B \rvert.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Phác thảo chứng minh**:

1. Vì $$f$$ là đơn ánh, $$A$$ có thể nhúng vào $$B$$, nên $$\lvert A \rvert \leq \lvert B \rvert$$.
2. Tương tự, vì $$g$$ là đơn ánh nên $$\lvert B \rvert \leq \lvert A \rvert$$.
3. Ý tưởng chính là xây dựng một song ánh $$h: A \to B$$ bằng cách ghép $$f$$ và $$g^{-1}$$ trên các tập con phù hợp (phân hoạch $$A$$ theo các chuỗi tiền ảnh dưới ánh xạ hợp $$g \circ f$$ rồi chọn $$f$$ hoặc $$g^{-1}$$ trên từng chuỗi).
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả**:

- $$\lvert \mathbb{N} \rvert = \lvert 2\mathbb{N} \rvert = \lvert \mathbb{Z} \rvert = \lvert \mathbb{Q} \rvert = \aleph_0$$ (các tập vô hạn đếm được).
- $$\lvert \mathbb{R} \rvert = \lvert (0,1) \rvert = \lvert [0,1] \rvert = 2^{\aleph_0}$$ (lực lượng continuum).
</div>

**Ý nghĩa trong khoa học máy tính**:
- Cho phép so sánh kích thước của hai không gian trạng thái mà không cần xây dựng trực tiếp một song ánh tường minh.
- Gợi ý cách tư duy so sánh độ khó hai chiều trong lý thuyết độ phức tạp tính toán.

## Ứng dụng trong Khoa học Máy tính

```python
python = {'An', 'Binh', 'Chi'}
java = {'Binh', 'Dung'}
learns_any = python | java
learns_both = python & java
print(len(learns_any))
```

- **Tìm kiếm và lọc dữ liệu**: Các phép toán `COUNT`, `DISTINCT`, `UNION`, `INTERSECT` đều liên quan trực tiếp đến lực lượng tập hợp.
- **Phân tích thuật toán**: Số tập con của một tập $$n$$ phần tử là $$2^n$$, giải thích vì sao các thuật toán vét cạn tập con có độ phức tạp hàm mũ.
- **Kiểm thử phần mềm**: Nguyên lý bao hàm–loại trừ giúp ước lượng số ca kiểm thử phủ nhiều điều kiện giao nhau.
- **Lý thuyết tính toán**: Tập các chương trình (chuỗi ký tự hữu hạn) là đếm được, trong khi tập các hàm từ $$\mathbb{N}$$ vào $$\{0,1\}$$ là không đếm được — từ đó suy ra tồn tại những bài toán không có thuật toán giải.

## Bài tập thực hành

### Bài tập 1: So sánh lực lượng

Chứng minh rằng tập hợp các số tự nhiên $$\mathbb{N}$$ và tập hợp các số chẵn dương có cùng lực lượng.

<details>
<summary>Đáp án</summary>

Với quy ước $$\mathbb{N} = \{1, 2, 3, \ldots\}$$, ánh xạ $$f(n) = 2n$$ là một song ánh từ $$\mathbb{N}$$ lên tập các số chẵn dương $$\{2, 4, 6, \ldots\}$$ (nếu tính $$\mathbb{N} = \{0, 1, 2, \ldots\}$$, ta dùng song ánh $$f(n) = 2n + 2$$). Do đó hai tập có cùng lực lượng $$\aleph_0$$.

</details>

### Bài tập 2: Lực lượng tập lũy thừa

Tính lực lượng của tập hợp tất cả các tập con của $$\{1,2,3\}$$.

<details>
<summary>Đáp án</summary>

Tập có $$2^3 = 8$$ tập con (bao gồm cả tập rỗng và chính tập $$\{1, 2, 3\}$$).

</details>

### Bài tập 3: Ứng dụng bao hàm - loại trừ

Có 50 sinh viên học Python, 40 sinh viên học Java và 30 sinh viên học cả hai ngôn ngữ. Hỏi có bao nhiêu sinh viên học ít nhất một trong hai ngôn ngữ?

<details>
<summary>Đáp án</summary>

$$\lvert P \cup J \rvert = 50 + 40 - 30 = 60$$ sinh viên.

</details>


## Xem thêm / Video gợi ý

- [Set Theory — Cardinality and Infinity](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Numberphile (Hilbert's Hotel)
- [Introduction to Sets](https://www.youtube.com/watch?v=4l7L9v0p0Q) — Khan Academy (Basics + notation)

## Tóm tắt

- **Lực lượng** $$\vert A\vert$$ đo số phần tử; với tập hữu hạn có $$n$$ phần tử, $$\vert \mathcal{P}(A)\vert = 2^n$$.
- **Nguyên lý bao hàm–loại trừ**: $$\vert A \cup B\vert = \vert A\vert + \vert B\vert - \vert A \cap B\vert$$, và mở rộng tương tự cho ba tập hoặc nhiều tập.
- Tập **đếm được** ($$\mathbb{N}, \mathbb{Z}, \mathbb{Q}$$) có thể liệt kê bởi $$\mathbb{N}$$; tập **không đếm được** ($$\mathbb{R}, (0,1)$$) được chứng minh bằng lập luận đường chéo Cantor.
- **Định lý Schröder–Bernstein**: nếu $$\vert A\vert \leq \vert B\vert$$ và $$\vert B\vert \leq \vert A\vert$$ thì $$\vert A\vert = \vert B\vert$$.
- Ứng dụng trong khoa học máy tính: phân tích không gian trạng thái $$2^n$$, đếm ca kiểm thử và lý giải giới hạn khả năng tính toán.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Z_Rr4d-3fFY">Countable and Uncountable Sets - Discrete Mathematics</a> — TrevTutor, tiếng Anh. Giới thiệu lực lượng, tập đếm được và tập không đếm được.
- <a href="https://www.youtube.com/watch?v=Uj3_KqkI9Zo">The Infinite Hotel Paradox - Jeff Dekofsky</a> — TED-Ed, tiếng Anh. Khách sạn Hilbert, minh họa trực giác tập vô hạn có cùng lực lượng với tập con thực sự của nó.
- <a href="https://www.youtube.com/watch?v=GS7dIWA6Hpo">INCLUSION-EXCLUSION PRINCIPLE - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Nguyên lý bao hàm–loại trừ cho bài toán đếm các tập giao nhau.
