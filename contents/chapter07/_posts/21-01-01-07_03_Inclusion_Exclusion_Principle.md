---
layout: post
title: "Nguyên lý Bù trừ"
categories: chapter07
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã học hoán vị và tổ hợp. Mục này giới thiệu nguyên lý bù trừ — công cụ sửa sai có hệ thống khi nhiều điều kiện chồng lấn."
---

Ở mục trước chúng ta đã học hoán vị và tổ hợp. Mục này giới thiệu **nguyên lý bù trừ** — công cụ sửa sai có hệ thống khi nhiều điều kiện chồng lấn.

Khi nhiều điều kiện chồng lên nhau, việc đếm bằng trực giác rất dễ sai: cộng số phần tử của từng nhóm riêng lẻ rồi vô tình đếm lặp những phần tử thuộc nhiều nhóm cùng lúc. Nguyên lý bù trừ cho phép cộng những gì cần có, trừ phần đã đếm trùng, và tiếp tục cộng trừ theo nhịp đúng khi có nhiều lớp chồng lấn phức tạp hơn.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** công thức IE cho 2, 3 tập và dạng đơn giản.
- **Đếm** phần tử không vi phạm ràng buộc (dạng bù).
- **Nhận biện** khi cộng thẳng $$|A_i|$$ gây đếm trùng.

**Từ khóa**: bao hàm–loại trừ, giao tập, đếm có điều kiện.
</div>

## 1. Đếm hợp của hai tập hợp

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với hai tập hữu hạn $A$ và $B$, **hợp** $A \cup B$ gồm các phần tử thuộc ít nhất một trong hai tập. **Giao** $A \cap B$ gồm các phần tử thuộc cả hai tập.
</div>

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $A$ và $B$ hữu hạn thì
</div>

<div class="textbook-equation" markdown="1">
$$
\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh**: Khi tính $$\lvert A \rvert + \lvert B \rvert$$, mỗi phần tử chỉ thuộc $$A$$ hoặc chỉ thuộc $$B$$ được đếm đúng một lần. Mỗi phần tử thuộc $$A \cap B$$ được đếm hai lần: một lần trong $$\lvert A \rvert$$ và một lần trong $$\lvert B \rvert$$. Vì trong hợp chúng ta chỉ muốn đếm nó một lần, chúng ta trừ đi $$\lvert A \cap B \rvert$$. Do đó công thức đúng.

![Phép hợp hai tập — nguyên lý bù trừ](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_union_B.svg)

<p class="textbook-figure-caption" data-figure="7.11">$$\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$$ — trừ phần giao để không đếm trùng.</p>
<div class="content-box example-box textbook-block" markdown="1">
<div class="textbook-example" markdown="1">
**Ví dụ**: Trong một lớp có 50 sinh viên, 30 sinh viên học tiếng Anh, 20 sinh viên học tiếng Pháp, 10 sinh viên học cả hai. Số sinh viên học ít nhất một ngoại ngữ là

<div class="textbook-equation" markdown="1">
$$
30 + 20 - 10 = 40.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Không thể trả lời $50$ chỉ vì $30+20=50$; con số $10$ ở phần giao là thông tin bắt buộc.
</div>
</div>

## 2. Nguyên lý bù trừ cho ba tập hợp

Với ba tập $A,B,C$, công thức là

<div class="textbook-equation" markdown="1">
{% raw %}$$
\begin{aligned}
\lvert A \cup B \cup C \rvert
&= \lvert A \rvert + \lvert B \rvert + \lvert C \rvert \\
&\quad - \lvert A \cap B \rvert - \lvert A \cap C \rvert - \lvert B \cap C \rvert \\
&\quad + \lvert A \cap B \cap C \rvert.
\end{aligned}
$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Tại sao phải cộng lại giao ba?** Một phần tử nằm trong cả ba tập được đếm $3$ lần ở bước cộng tập đơn, bị trừ $3$ lần ở bước trừ giao đôi, nên tổng tạm thời là $0$. Chúng ta phải cộng lại một lần để nó được đếm đúng một lần.

![Nguyên lý bù trừ — ba tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="7.12">Công thức bù trừ cho ba tập — cộng tập đơn, trừ giao đôi, cộng lại giao ba.</p>
<div class="interactive-tool" data-demo="inclusion-exclusion-toggle" markdown="1">
**Mô phỏng tương tác đề xuất**: Một bảng có ba công tắc `A`, `B`, `C`. Khi chọn vị trí của một phần tử trong sơ đồ Venn, công cụ hiển thị phần tử đó được cộng/trừ bao nhiêu lần trong công thức bù trừ.
</div>

<script src="{{ '/public/js/inclusion-exclusion-toggle.js' | relative_url }}"></script>

## 3. Công thức tổng quát cho $n$ tập hợp

Cho $A_1,A_2,\ldots,A_n$ là các tập hữu hạn. Khi đó

<div class="textbook-equation" markdown="1">
{% raw %}$$
\begin{aligned}
\left\lvert\bigcup_{i=1}^{n} A_i\right\rvert
&= \sum_i \lvert A_i \rvert \\
&\quad - \sum_{i<j}\lvert A_i\cap A_j \rvert \\
&\quad + \sum_{i<j<k}\lvert A_i\cap A_j\cap A_k \rvert \\
&\quad - \cdots \\
&\quad + (-1)^{n+1}\lvert A_1\cap\cdots\cap A_n \rvert.
\end{aligned}
$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Dạng compact hơn:

<div class="textbook-equation" markdown="1">
{% raw %}$$
\left\lvert\bigcup_{i=1}^{n} A_i\right\rvert
= \sum_{\emptyset \neq I \subseteq \{1,2,\ldots,n\}} (-1)^{\lvert I \rvert+1}\left\lvert\bigcap_{i\in I} A_i\right\rvert.
$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Khối chứng minh**: Xét một phần tử $x$ thuộc đúng $r$ trong $n$ tập. Trong vế phải, $x$ đóng góp

<div class="textbook-equation" markdown="1">
$$
\binom{r}{1}-\binom{r}{2}+\binom{r}{3}-\cdots+(-1)^{r+1}\binom{r}{r}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Theo khai triển nhị thức,

<div class="textbook-equation" markdown="1">
$$
(1-1)^r = \binom{r}{0}-\binom{r}{1}+\binom{r}{2}-\cdots+(-1)^r\binom{r}{r}=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Suy ra tổng xen kẽ không có hạng $\binom{r}{0}$ bằng $1$. Vậy mỗi phần tử thuộc hợp được đếm đúng một lần.

![Phép giao hai tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_intersect_B.svg)

<p class="textbook-figure-caption" data-figure="7.13">Mỗi giao $$\lvert A_i \cap A_j \rvert$$ trong công thức tổng quát đại diện phần bị đếm trùng.</p>
## 4. Dạng bù: đếm phần tử không vi phạm điều kiện nào

Nhiều bài toán dễ hơn nếu đếm số đối tượng **vi phạm ít nhất một điều kiện**, rồi lấy tổng trừ đi số đó.

Nếu $U$ là không gian tất cả đối tượng và $A_i$ là tập các đối tượng vi phạm điều kiện thứ $i$, thì số đối tượng hợp lệ là

<div class="textbook-equation" markdown="1">
$$
\lvert U \rvert-\left\lvert\bigcup_i A_i\right\rvert.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Có bao nhiêu số từ $1$ đến $100$ không chia hết cho $2$, $3$, hoặc $5$?

Gọi $A_2,A_3,A_5$ lần lượt là các số chia hết cho $2,3,5$. Chúng ta có

<div class="textbook-equation" markdown="1">
$$
\lvert A_2 \rvert=50,\quad \lvert A_3 \rvert=33,\quad \lvert A_5 \rvert=20,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$
\lvert A_2\cap A_3 \rvert=16,\quad \lvert A_2\cap A_5 \rvert=10,\quad \lvert A_3\cap A_5 \rvert=6,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$
\lvert A_2\cap A_3\cap A_5 \rvert=3.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Do đó số bị loại là $50+33+20-16-10-6+3=74$. Số hợp lệ là $100-74=26$.

![Biểu đồ Venn ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="7.14">Dạng bù đếm các số không chia hết cho 2, 3 hoặc 5 — loại phần vi phạm ít nhất một điều kiện.</p>
![Birthday paradox — va chạm sớm hơn trực giác](/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg)

<p class="textbook-figure-caption" data-figure="7.15">Nguyên lý bù trừ cũng xuất hiện khi đếm xác suất hợp nhiều biến cố — tương tự birthday paradox.</p>
</div>

## 6. Ứng dụng trong Khoa học Máy tính
Trong cơ sở dữ liệu, truy vấn `OR` giữa nhiều điều kiện có thể tạo ra bản ghi trùng. Hệ quản trị phải loại trùng tương tự nguyên lý bù trừ. Trong bảo mật, khi đếm số mật khẩu thỏa các điều kiện “có chữ hoa”, “có chữ số”, “có ký tự đặc biệt”, cách hiệu quả là đếm phần bù: mật khẩu thiếu ít nhất một loại ký tự. Trong thuật toán, bù trừ xuất hiện trong sàng số nguyên tố, tính xác suất lỗi của hệ thống nhiều thành phần và phân tích các cấu hình bị cấm.

```python
from itertools import combinations

def inclusion_exclusion(sizes):
    # sizes[k] chứa tổng kích thước các giao của đúng k tập, k bắt đầu từ 1
    return sum(((-1) ** (k + 1)) * value for k, value in sizes.items())

print(inclusion_exclusion({1: 50 + 33 + 20, 2: 16 + 10 + 6, 3: 3}))
```

## Bài tập thực hành

### Bài tập 1: Ba câu lạc bộ

Một lớp có 80 sinh viên. Có 35 sinh viên tham gia CLB Lập trình, 30 tham gia CLB Toán, 25 tham gia CLB Robot. Có 12 sinh viên tham gia cả Lập trình và Toán, 10 tham gia cả Lập trình và Robot, 8 tham gia cả Toán và Robot, và 5 tham gia cả ba. Hỏi có bao nhiêu sinh viên tham gia ít nhất một CLB?

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$
35+30+25-12-10-8+5=65.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Có 65 sinh viên tham gia ít nhất một CLB.

</details>

### Bài tập 2: Mật khẩu

Có bao nhiêu chuỗi nhị phân độ dài 8 chứa ít nhất một số 0 và ít nhất một số 1?

<details>
<summary>Đáp án</summary>

Tổng số chuỗi là $2^8=256$. Chuỗi không có số 0 chỉ có một chuỗi `11111111`; chuỗi không có số 1 chỉ có một chuỗi `00000000`. Vậy số cần tìm là $256-2=254$.

</details>

### Bài tập 3: Chia hết

Tìm số nguyên dương không vượt quá $1000$ chia hết cho $3$ hoặc $5$ hoặc $7$.

<details>
<summary>Đáp án</summary>

Các số lượng đơn: $333,200,142$. Giao đôi: chia hết cho $15,21,35$ lần lượt là $66,47,28$. Giao ba: chia hết cho $105$ là $9$. Do đó

<div class="textbook-equation" markdown="1">
$$
333+200+142-66-47-28+9=543.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 4: Mật khẩu nhiều loại ký tự

**A.15** Suppose passwords are strings where the alphabet has 10 digits, 26 lower-case letters, 26 upper-case letters, and 15 special symbols.

(a) How many length-$$n$$ passwords contain at least two of the four types of characters?

(b) How many length-$$n$$ passwords have no two adjacent identical characters?

(c) How many length-$$n$$ passwords contain at least two of the four types of characters **and** have no two adjacent identical characters?

<details>
<summary>Đáp án</summary>

Đặt các loại ký tự: D = digit (10), L = lower (26), U = upper (26), S = special (15). Tổng bảng chữ: $$10+26+26+15 = 77$$.

(a) Dùng bù trừ. Tổng số password độ dài $$n$$: $$77^n$$.

Số password chỉ dùng **một** loại: $$10^n + 26^n + 26^n + 15^n = 10^n + 2 \cdot 26^n + 15^n$$.

Số password chỉ dùng đúng **hai** loại: Có $$C(4,2) = 6$$ cặp. Với mỗi cặp có kích thước $$a,b$$, số password chỉ từ hai loại đó là $$(a+b)^n - a^n - b^n$$. Tổng cộng:

<div class="textbook-equation" markdown="1">
{% raw %}$$
\begin{aligned}
S_2 &= (10+26)^n - 10^n - 26^n && \text{(D,L)} \\
&\quad + (10+26)^n - 10^n - 26^n && \text{(D,U)} \\
&\quad + (10+15)^n - 10^n - 15^n && \text{(D,S)} \\
&\quad + (26+26)^n - 26^n - 26^n && \text{(L,U)} \\
&\quad + (26+15)^n - 26^n - 15^n && \text{(L,S)} \\
&\quad + (26+15)^n - 26^n - 15^n && \text{(U,S)} \\
&= 2(36^n - 10^n - 26^n) + (25^n - 10^n - 15^n) \\
&\quad + (52^n - 2\cdot 26^n) + 2(41^n - 26^n - 15^n)
\end{aligned}
$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Yêu cầu "ít nhất hai loại" = Total - một loại - hai loại = $$77^n - (10^n + 2\cdot 26^n + 15^n) - S_2$$.

(b) Password không có hai ký tự kề giống nhau: ký tự đầu có 77 cách chọn, mỗi ký tự sau có 76 cách (khác ký tự trước). Vậy số lượng = $$77 \times 76^{n-1}$$.

(c) Kết hợp cả hai điều kiện. Gọi A = có ít nhất hai loại ký tự, B = không có hai ký tự kề giống nhau. Chúng ta cần $$\lvert A \cap B \rvert = \lvert B \rvert - \lvert\bar{A} \cap B \rvert$$, với $$\bar{A}$$ = chỉ dùng 0 hoặc 1 loại ký tự.

Tính $$\lvert\bar{A} \cap B \rvert$$: số password chỉ dùng 1 loại và không có ký tự kề giống nhau. Với mỗi loại có $$k$$ ký tự, số lượng là $$k \times (k-1)^{n-1}$$ ($$k \ge 2$$) hoặc $$k$$ nếu $$k=1$$. Vậy:

- Chỉ digit: $$10 \times 9^{n-1}$$ ($$k=10$$)
- Chỉ lower: $$26 \times 25^{n-1}$$
- Chỉ upper: $$26 \times 25^{n-1}$$
- Chỉ special: $$15 \times 14^{n-1}$$

Tổng $$\lvert\bar{A} \cap B \rvert = 10 \times 9^{n-1} + 2 \cdot 26 \times 25^{n-1} + 15 \times 14^{n-1}$$.

Vậy kết quả: $$\lvert A \cap B \rvert = 77 \times 76^{n-1} - \big(10 \times 9^{n-1} + 52 \times 25^{n-1} + 15 \times 14^{n-1}\big)$$.

</details>

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **Nguyên lý bù trừ** sửa sai cho việc đếm trùng trong hợp các tập hợp.
- **Dấu xen kẽ**: cộng tập đơn, trừ giao đôi, cộng giao ba, và tiếp tục như vậy.
- **Dạng bù** đặc biệt hữu ích khi đếm các đối tượng không vi phạm điều kiện nào.
- **Chứng minh phần tử** cho thấy mỗi phần tử thuộc hợp được đếm đúng một lần.
- **Ứng dụng CS** gồm truy vấn dữ liệu, kiểm tra mật khẩu, sàng số, xác suất lỗi và phân tích cấu hình bị cấm.

Trong bài tiếp theo, chúng ta sẽ học về hệ số nhị thức và các đồng nhất thức tổ hợp.
