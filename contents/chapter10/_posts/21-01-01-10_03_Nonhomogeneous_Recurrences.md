---

layout: post
title: "Quan hệ Truy hồi Không Thuần nhất và Ứng dụng"
categories: chapter10
date: 2021-01-01
order: 3
required: true
lang: vi
excerpt: "Ở mục trước chúng ta đã giải quan hệ truy hồi tuyến tính thuần nhất bằng phương trình đặc trưng. Mục này mở rộng sang quan hệ truy hồi không thuần nhất — khi…"
---

Ở mục trước chúng ta đã giải quan hệ truy hồi **tuyến tính thuần nhất** bằng phương trình đặc trưng. Mục này mở rộng sang **quan hệ truy hồi không thuần nhất** — khi ngoài các số hạng $$a_{n-i}$$ còn có thêm thành phần $$f(n)$$ (hằng số, đa thức, $$b^n$$, …). Dạng này mô tả nhiều quá trình thực tế hơn: mỗi bước vừa kế thừa trạng thái cũ vừa nhận tác động bên ngoài (chi phí cố định, dữ liệu mới, yêu cầu phát sinh). Trong phân tích thuật toán, ví dụ điển hình là $$T(n)=2T(n/2)+n$$ của merge sort — thuần nhất về cấu trúc đệ quy nhưng có thành phần công việc $$f(n)=n$$ ở mỗi mức. Chúng ta học **nguyên lý chồng chất** và **phương pháp hệ số bất định**, kể cả trường hợp **cộng hưởng** khi dạng nghiệm thử trùng nghiệm thuần nhất.

## 1. Dạng tổng quát

Quan hệ truy hồi tuyến tính không thuần nhất bậc $k$ có dạng

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}+f(n),
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó $f(n)$ không đồng nhất bằng 0.

Quan hệ thuần nhất liên kết là

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
## 2. Nguyên lý chồng chất

Nghiệm tổng quát có dạng

<div class="textbook-equation" markdown="1">
$$
a_n=a_n^{(h)}+a_n^{(p)},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó:

- $a_n^{(h)}$ là nghiệm tổng quát của quan hệ thuần nhất liên kết.
- $a_n^{(p)}$ là một nghiệm riêng của quan hệ không thuần nhất.

**Chứng minh**: Nếu $L$ là toán tử tuyến tính tương ứng với vế trái sau khi chuyển hết về một phía, thì quan hệ có dạng $L(a)=f$. Nếu $L(h)=0$ và $L(p)=f$, thì $L(h+p)=L(h)+L(p)=f$. Do đó tổng của nghiệm thuần nhất và một nghiệm riêng là nghiệm của bài toán đầy đủ.

![Nguyên lý chồng chất — nghiệm tổng quát](/discrete-mathematics-for-computer-science-iuh/img/course/Constant-recursive-sequences.svg)

<p class="textbook-figure-caption" data-figure="10.11">Nghiệm tổng quát = nghiệm thuần nhất + nghiệm riêng — nguyên lý chồng chất mở rộng kỹ thuật giải truy hồi.</p>
## 3. Phương pháp hệ số bất định

Khi $f(n)$ có dạng quen thuộc, ta đoán nghiệm riêng cùng “họ” với $f(n)$.

| Dạng $f(n)$ | Dạng thử cho $a_n^{(p)}$ |
|------------|---------------------------|
| Hằng số $d$ | $A$ |
| Đa thức bậc $m$ | đa thức bậc $m$ |
| $b^n$ | $Ab^n$ |
| $n^m b^n$ | đa thức bậc $m$ nhân $b^n$ |

Nếu dạng thử trùng với nghiệm thuần nhất, nhân thêm $n$ đủ số lần để độc lập tuyến tính.

![Phương pháp hệ số bất định](/discrete-mathematics-for-computer-science-iuh/img/course/Recursive_problem_solving.svg)

<p class="textbook-figure-caption" data-figure="10.12">Đoán nghiệm riêng cùng "họ" với $f(n)$ — hằng số, đa thức, hoặc $b^n$ — rồi xác định hệ số bằng thế.</p>
## 4. Ví dụ với hằng số

Khi $f(n)$ là hằng số, theo bảng ở mục 3 ta đoán nghiệm riêng $a_n^{(p)}=A$, thế vào quan hệ để xác định $A$, rồi ghép với nghiệm thuần nhất và điều kiện ban đầu.

Giải

<div class="textbook-equation" markdown="1">
$$
a_n=2a_{n-1}+3,\quad a_0=1.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Phần thuần nhất: $a_n^{(h)}=C2^n$.

Thử nghiệm riêng hằng $a_n^{(p)}=A$. Thay vào:

<div class="textbook-equation" markdown="1">
$$
A=2A+3\Rightarrow A=-3.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy $a_n=C2^n-3$. Từ $a_0=1$, $C-3=1$ nên $C=4$. Do đó

<div class="textbook-equation" markdown="1">
$$
a_n=4\cdot2^n-3.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
## 5. Ví dụ với đa thức

Với $f(n)$ là đa thức bậc $m$, ta chọn nghiệm riêng cùng bậc; nếu dạng thử trùng nghiệm thuần nhất thì tăng bậc một để đảm bảo độc lập tuyến tính.

Giải dạng tổng quát:

<div class="textbook-equation" markdown="1">
$$
a_n=a_{n-1}+n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Phần thuần nhất có nghiệm $C$. Vì $f(n)=n$ là đa thức bậc 1, thử $a_n^{(p)}=An^2+Bn$. Thay vào:

<div class="textbook-equation" markdown="1">
$$
An^2+Bn=A(n-1)^2+B(n-1)+n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
So sánh hệ số cho $A=\frac12$. Ta có thể chọn $B=\frac12$, khi đó

<div class="textbook-equation" markdown="1">
$$
a_n^{(p)}=\frac{n(n+1)}2.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đây chính là tổng $1+2+\cdots+n$.

![Dãy số học — tổng $1+2+\cdots+n$](/discrete-mathematics-for-computer-science-iuh/img/course/Arithmetic_progression.svg)

<p class="textbook-figure-caption" data-figure="10.13">Truy hồi $a_n = a_{n-1} + n$ có nghiệm riêng bậc hai — chính là công thức tổng Gauss.</p>
## 6. Trường hợp cộng hưởng

Xét

<div class="textbook-equation" markdown="1">
$$
a_n=2a_{n-1}+2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Phần thuần nhất có nghiệm $C2^n$. Nếu thử $A2^n$, nó trùng với nghiệm thuần nhất nên không thể xác định $A$. Ta phải thử

<div class="textbook-equation" markdown="1">
$$
a_n^{(p)}=An2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đây gọi là hiện tượng **cộng hưởng**: tác động ngoài có cùng dạng với nghiệm tự nhiên của hệ.

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học chọn dạng $f(n)$ và nghiệm đặc trưng. Công cụ đề xuất dạng nghiệm riêng, cảnh báo khi xảy ra cộng hưởng và tự nhân thêm $n$.
<div data-demo="characteristic-solver"></div>
</div>
<script src="{{ '/public/js/characteristic-solver.js' | relative_url }}"></script>

## 7. Ứng dụng phân tích thuật toán

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Phần này liên hệ khái niệm toán học với bài toán thực tế trong lập trình và hệ thống.

Quan hệ

<div class="textbook-equation" markdown="1">
$$
T(n)=2T(n/2)+n
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
mô tả nhiều thuật toán chia để trị như merge sort. Đây không phải truy hồi tuyến tính theo chỉ số $n-1$, nhưng tư tưởng vẫn giống: nghiệm gồm phần do đệ quy và phần chi phí ngoài $n$ ở mỗi mức. Kết quả $T(n)=\Theta(n\log n)$ cho thấy thành phần không thuần nhất quyết định đáng kể độ phức tạp.

![Dãy hình học — thành phần $f(n)$ trong truy hồi](/discrete-mathematics-for-computer-science-iuh/img/course/Geometric_sequence.svg)

<p class="textbook-figure-caption" data-figure="10.14">Thành phần $f(n)$ trong truy hồi không thuần nhất mô tả tác động bên ngoài — chi phí cố định, dữ liệu mới, hoặc công việc phụ mỗi bước.</p>
Với truy hồi tuyến tính, ví dụ số phép gán trong một vòng lặp tích lũy có thể thỏa

<div class="textbook-equation" markdown="1">
$$
a_n=a_{n-1}+2n+1,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
và nghiệm riêng bậc hai cho ta tổng chi phí bậc $\Theta(n^2)$.

## Bài tập

### Bài tập 1

Giải $$a_n = 2a_{n-1} + 3$$, $$a_0 = 0$$ bằng phương pháp hệ số bất định.

<details>
<summary>Đáp án</summary>

Thuần nhất: $$a_n^{(h)} = c \cdot 2^n$$. Thử riêng $$a_n^{(p)} = A$$ (hằng). Thay: $$A = 2A + 3 \Rightarrow A = -3$$. $$a_n = c \cdot 2^n - 3$$, $$a_0 = 0 \Rightarrow c = 3$$. Vậy $$a_n = 3 \cdot 2^n - 3$$.

</details>

### Bài tập 2

Giải $$a_n = a_{n-1} + 2n$$, $$a_0 = 1$$.

<details>
<summary>Đáp án</summary>

$$a_n^{(h)} = c$$. Thử $$a_n^{(p)} = An + B$$. Thay: $$An + B = A(n-1) + B + 2n \Rightarrow A = 2$$. $$a_n = c + 2n$$, $$a_0 = 1 \Rightarrow c = 1$$. $$a_n = 1 + 2n$$.

</details>

### Bài tập 3

Giải thích **cộng hưởng**: vì sao với $$a_n = 2a_{n-1} + 2^n$$ ta thử $$a_n^{(p)} = A n 2^n$$ thay vì $$A 2^n$$?

<details>
<summary>Đáp án</summary>

$$2^n$$ là nghiệm thuần nhất của phương trình đặc trưng $$r - 2 = 0$$. Thử $$A 2^n$$ cho riêng sẽ triệt tiêu — phải nhân thêm $$n$$ (hoặc $$n^s$$ nếu nghiệm bội).

</details>

---

## Xem thêm / Video gợi ý

- [Solving Recurrence Relations](https://www.youtube.com/watch?v=7jZ5n8k0p0Q) — MIT OCW (Master theorem + examples)


## Tóm tắt

- Quan hệ không thuần nhất: $$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k} + f(n)$$.
- **Nguyên lý chồng chất**: $$a_n = a_n^{(h)} + a_n^{(p)}$$ — nghiệm thuần nhất cộng một nghiệm riêng.
- **Phương pháp hệ số bất định**: đoán $$a_n^{(p)}$$ cùng “họ” với $$f(n)$$ (hằng số, đa thức, $$b^n$$).
- **Cộng hưởng**: khi dạng thử trùng nghiệm thuần nhất, nhân thêm $$n$$ (hoặc $$n^s$$).
- Ứng dụng: phân tích thuật toán chia để trị ($$T(n)=2T(n/2)+n$$) và truy hồi tuyến tính với $$f(n)$$ đa thức.

Trong bài tiếp theo, chúng ta tổng hợp ứng dụng quan hệ truy hồi trong thuật toán và hệ thống thực tế.
