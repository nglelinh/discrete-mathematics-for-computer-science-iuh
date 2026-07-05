---

layout: post
title: "Giải Quan hệ Truy hồi Tuyến tính"
categories: chapter10
date: 2021-01-01
order: 2
required: true
lang: vi
excerpt: "Ở mục trước chúng ta đã định nghĩa quan hệ truy hồi và phân loại theo tính tuyến tính, thuần nhất, và bậc. Mục này tập trung vào quan hệ truy hồi tuyến tính…"
---

Ở mục trước chúng ta đã định nghĩa quan hệ truy hồi và phân loại theo tính tuyến tính, thuần nhất, và bậc. Mục này tập trung vào **quan hệ truy hồi tuyến tính thuần nhất hệ số hằng** — lớp bài toán cho phép tìm công thức tường minh $$a_n$$ hoặc ít nhất mô tả rõ cấu trúc tăng trưởng của dãy, thay vì tính lần lượt từng bước. Từ số phép gọi đệ quy, số cấu hình ở mỗi mức, đến độ phức tạp của thuật toán chia để trị, nhiều bài toán quy về giải đúng một truy hồi tuyến tính. Chúng ta học kỹ thuật **phương trình đặc trưng** và các dạng nghiệm (phân biệt, bội, phức).

## 1. Dạng tổng quát

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ truy hồi tuyến tính thuần nhất hệ số hằng bậc $k$ có dạng
</div>


<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k},\quad c_k\ne0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
- **Tuyến tính**: các số hạng $a_{n-i}$ chỉ xuất hiện bậc nhất.
- **Thuần nhất**: không có thành phần ngoài chỉ phụ thuộc vào $n$.
- **Hệ số hằng**: $c_i$ không thay đổi theo $n$.
- Cần $k$ điều kiện đầu để xác định duy nhất dãy.

<div class="textbook-example" markdown="1">
**Ví dụ**: Fibonacci thỏa $F_n=F_{n-1}+F_{n-2}$ với $F_0=0,F_1=1$.

![Dãy truy hồi tuyến tính hệ số hằng](/discrete-mathematics-for-computer-science-iuh/img/course/Constant-recursive-sequences.svg)

<p class="textbook-figure-caption" data-figure="10.6">Truy hồi tuyến tính thuần nhất bậc $k$ — nghiệm là tổng các hạng dạng $r_i^n$.</p>
</div>

## 2. Ý tưởng nghiệm dạng $r^n$

Giả sử $a_n=r^n$ với $r\ne0$. Thay vào truy hồi bậc hai

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
thu được

<div class="textbook-equation" markdown="1">
$$
r^n=c_1r^{n-1}+c_2r^{n-2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Chia cho $r^{n-2}$:

<div class="textbook-equation" markdown="1">
$$
r^2-c_1r-c_2=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đây là **phương trình đặc trưng**.

Nghiệm tổng quát của hệ tuyến tính thuần nhất là tổ hợp tuyến tính các nghiệm đặc trưng: nếu $$r_1, r_2$$ phân biệt thì $$a_n = A r_1^n + B r_2^n$$; nếu nghiệm kép $$r$$ thì $$a_n = (A + Bn)r^n$$. Dãy Fibonacci ($$F_1=1, F_2=1, F_n=F_{n-1}+F_{n-2}$$) là trường hợp khảo sát tiêu biểu.

![Giải bài toán đệ quy — phương trình đặc trưng](/discrete-mathematics-for-computer-science-iuh/img/course/Recursive_problem_solving.svg)

<p class="textbook-figure-caption" data-figure="10.7">Phương trình đặc trưng $r^k - c_1 r^{k-1} - \cdots - c_k = 0$ quyết định cấu trúc nghiệm của truy hồi tuyến tính.</p>
<div class="content-box insight-box textbook-block" markdown="1">
**Trực giác**: Nếu một dãy tăng theo quy luật nhân lặp lại, tỉ số giữa các số hạng liên tiếp gần giống một hằng số. Vì vậy nghiệm mũ $r^n$ là ứng viên tự nhiên cho hệ tuyến tính hệ số hằng.
</div>

## 3. Nghiệm phân biệt

Nếu phương trình đặc trưng bậc hai có hai nghiệm phân biệt $r_1,r_2$, nghiệm tổng quát là

<div class="textbook-equation" markdown="1">
$$
a_n=\alpha r_1^n+\beta r_2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Các hằng số $\alpha,\beta$ được xác định từ điều kiện đầu.

<div class="textbook-example" markdown="1">
**Ví dụ**: Giải $a_n=5a_{n-1}-6a_{n-2}$, $a_0=2,a_1=5$.

Phương trình đặc trưng:

<div class="textbook-equation" markdown="1">
$$
r^2-5r+6=0=(r-2)(r-3).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Nghiệm tổng quát:

<div class="textbook-equation" markdown="1">
$$
a_n=\alpha2^n+\beta3^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Từ $a_0=2$: $\alpha+\beta=2$. Từ $a_1=5$: $2\alpha+3\beta=5$. Suy ra $\beta=1,\alpha=1$. Vậy

<div class="textbook-equation" markdown="1">
$$
a_n=2^n+3^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## 4. Nghiệm bội

Nếu phương trình đặc trưng có nghiệm kép $r$, nghiệm tổng quát là

<div class="textbook-equation" markdown="1">
$$
a_n=(\alpha+\beta n)r^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Tổng quát hơn, nếu $r$ là nghiệm bội $m$, ta có các thành phần

<div class="textbook-equation" markdown="1">
$$
r^n,\; nr^n,\; n^2r^n,\ldots,n^{m-1}r^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Giải $a_n=4a_{n-1}-4a_{n-2}$. Phương trình đặc trưng là

<div class="textbook-equation" markdown="1">
$$
r^2-4r+4=(r-2)^2=0,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
nên

<div class="textbook-equation" markdown="1">
$$
a_n=(\alpha+\beta n)2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## 5. Nghiệm phức

Nếu phương trình đặc trưng có nghiệm phức liên hợp $r=\rho(\cos\theta+i\sin\theta)$ và $\overline r$, nghiệm thực có dạng

<div class="textbook-equation" markdown="1">
$$
a_n=\rho^n(A\cos n\theta+B\sin n\theta).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Trường hợp này xuất hiện trong các mô hình dao động rời rạc, bộ lọc tín hiệu và phân tích hệ thống tuyến tính.

![Tỷ lệ vàng — nghiệm của Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Golden_ratio_line.svg)

<p class="textbook-figure-caption" data-figure="10.8">Nghiệm phức của phương trình đặc trưng Fibonacci liên quan tỷ lệ vàng $\varphi = \frac{1+\sqrt{5}}{2}$.</p>
## 6. Bậc cao hơn

Với truy hồi bậc $k$,

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+\cdots+c_ka_{n-k},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
phương trình đặc trưng là

<div class="textbook-equation" markdown="1">
$$
r^k-c_1r^{k-1}-c_2r^{k-2}-\cdots-c_k=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mỗi nghiệm phân biệt $r_i$ đóng góp một hạng $\alpha_i r_i^n$; nghiệm bội đóng góp thêm các nhân tử đa thức theo $n$.

![Merge Sort — truy hồi chia để trị](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

<p class="textbook-figure-caption" data-figure="10.9">Phân tích thuật toán đệ quy thường quy về truy hồi — ví dụ $T(n) = 2T(n/2) + n$ của merge sort.</p>
![Master Theorem — giải truy hồi chia để trị](/discrete-mathematics-for-computer-science-iuh/img/course/Master_theorem.png)

<p class="textbook-figure-caption" data-figure="10.10">Master Theorem giải nhanh dạng $T(n) = aT(n/b) + f(n)$ — công cụ công nghiệp cho phân tích thuật toán.</p>
<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học nhập hệ số $c_1,c_2$ và điều kiện đầu. Công cụ vẽ nghiệm đặc trưng trên trục số/phức và hiển thị vài số hạng đầu của dãy.
<div data-demo="linear-recurrence-solver"></div>
</div>
<script src="{{ '/public/js/linear-recurrence-solver.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Giải $$a_n = 5a_{n-1}$$, $$a_0 = 3$$.

<details>
<summary>Đáp án</summary>

Phương trình đặc trưng $$r = 5$$. $$a_n = 3 \cdot 5^n$$.

</details>

### Bài tập 2

Giải $$a_n = 4a_{n-1} - 4a_{n-2}$$, $$a_0 = 1$$, $$a_1 = 4$$.

<details>
<summary>Đáp án</summary>

$$r^2 - 4r + 4 = 0 \Rightarrow (r-2)^2 = 0$$ — nghiệm kép $$r = 2$$. $$a_n = (\alpha + \beta n) 2^n$$. Từ điều kiện đầu: $$\alpha = 1$$, $$\beta = 1$$. Vậy $$a_n = (1+n)2^n$$.

</details>

### Bài tập 3

Giải $$a_n = a_{n-1} + a_{n-2}$$, $$a_0 = 0$$, $$a_1 = 1$$ (Fibonacci). Viết dạng tường minh qua nghiệm đặc trưng (không cần rút gọn số).

<details>
<summary>Đáp án</summary>

$$r^2 = r + 1 \Rightarrow r = \frac{1 \pm \sqrt{5}}{2}$$. $$a_n = \alpha r_1^n + \beta r_2^n$$ với $$\alpha, \beta$$ từ $$a_0, a_1$$.

</details>

---

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)


## Tóm tắt

- Quan hệ truy hồi tuyến tính thuần nhất bậc $$k$$: $$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k}$$.
- Giả sử nghiệm dạng $$r^n$$ dẫn tới **phương trình đặc trưng** bậc $$k$$.
- Nghiệm phân biệt $$r_1, r_2$$: $$a_n = \alpha r_1^n + \beta r_2^n$$; nghiệm kép: $$a_n = (\alpha + \beta n)r^n$$.
- Nghiệm phức liên hợp cho dạng $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$.
- Bậc cao hơn: mỗi nghiệm đóng góp hạng $$r_i^n$$ (và nhân tử đa thức nếu nghiệm bội).

Trong bài tiếp theo, chúng ta mở rộng sang **quan hệ truy hồi không thuần nhất** — khi có thêm thành phần $$f(n)$$ bên ngoài.
