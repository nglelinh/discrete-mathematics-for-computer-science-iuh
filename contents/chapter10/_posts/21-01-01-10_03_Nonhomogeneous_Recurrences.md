---
layout: post
title: "Quan hệ Truy hồi Không Thuần nhất và Ứng dụng"
categories: chapter10
date: 2021-01-01
order: 3
required: true
lang: vi
excerpt: "Truy hồi tuyến tính không thuần nhất: nguyên lý a=a_h+a_p, hệ số bất định, cộng hưởng, ví dụ bậc 1–2 (2x+1, tổng n^2, +3^n) và liên hệ thuật toán."
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

**Chứng minh (phác).** Gọi $$L$$ là toán tử tuyến tính “chuyển vế trái”:  
$$L(a)_n = a_n - c_1 a_{n-1} - \cdots - c_k a_{n-k}$$.  
Quan hệ không thuần nhất là $$L(a)=f$$. Nếu $$a^{(p)}$$ thỏa $$L(a^{(p)})=f$$ và $$b$$ là **một** nghiệm bất kỳ của cùng phương trình, thì  

$$
L(b-a^{(p)}) = L(b)-L(a^{(p)}) = f-f = 0,
$$

nên $$b-a^{(p)}$$ là nghiệm của quan hệ **thuần nhất** liên kết — ký hiệu $$a^{(h)}$$. Vậy mọi nghiệm có dạng $$b = a^{(p)} + a^{(h)}$$. (Ngược lại: nếu $$L(h)=0$$ và $$L(p)=f$$ thì $$L(h+p)=f$$.)

## 3. Phương pháp hệ số bất định

Khi $f(n)$ có dạng quen thuộc, ta đoán nghiệm riêng cùng “họ” với $f(n)$.

| Dạng $f(n)$ | Dạng thử cho $a_n^{(p)}$ |
|------------|---------------------------|
| Hằng số $d$ | $A$ |
| Đa thức bậc $m$ | đa thức bậc $m$ |
| $b^n$ | $Ab^n$ |
| $n^m b^n$ | đa thức bậc $m$ nhân $b^n$ |

Nếu dạng thử trùng với nghiệm thuần nhất, nhân thêm $n$ đủ số lần để độc lập tuyến tính.

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

<div class="textbook-example" markdown="1">

**Ví dụ (bậc 1 — kiểu Tháp Hà Nội / “gấp đôi rồi cộng 1”).**  
Giải $$x_n = 2x_{n-1} + 1$$, $$x_1 = 1$$.  
Thuần nhất: $$x_n^{(h)} = A\cdot 2^n$$.  
Thử riêng hằng $$x_n^{(p)}=C$$: $$C=2C+1\Rightarrow C=-1$$.  
Tổng quát: $$x_n = A\cdot 2^n - 1$$.  
$$x_1=1$$: $$2A-1=1\Rightarrow A=1$$.  
Vậy $$x_n = 2^n - 1$$ (đúng $$1,3,7,15,\ldots$$).

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

<div class="textbook-example" markdown="1">

**Ví dụ (tổng bình phương — cộng hưởng đa thức).**  
Đặt $$a_n = 1^2 + 2^2 + \cdots + n^2$$ ($$n\ge 1$$), $$a_0=0$$. Khi đó  
$$a_n = a_{n-1} + n^2.$$  
Thuần nhất: $$a_n^{(h)}=C$$ (nghiệm $$r=1$$). Vì $$f(n)=n^2$$ là đa thức bậc 2 và **hằng số đã là nghiệm thuần nhất**, thử riêng  
$$a_n^{(p)} = n(qn^2 + sn + t) = qn^3 + sn^2 + tn$$  
(bậc 3). Thế vào $$a_n - a_{n-1} = n^2$$ và đồng nhất hệ số (hoặc nhớ công thức) cho  
$$a_n^{(p)} = \frac{n(n+1)(2n+1)}{6}.$$  
Với $$a_0=0$$ thì $$C=0$$, nên  
$$a_n = \frac{n(n+1)(2n+1)}{6}.$$

</div>

## 5b. Ví dụ bậc 2 không thuần nhất

<div class="textbook-example" markdown="1">

**Ví dụ ($$f(n)=3^n$$, thuần nhất có nghiệm bội $$r=1$$).**  
$$X_n = 2X_{n-1} - X_{n-2} + 3^n$$, $$X_0=1$$, $$X_1=3$$.

**Thuần nhất.** Đặc trưng $$r^2-2r+1=(r-1)^2=0$$ → $$X_n^{(h)}=A+Bn$$.

**Riêng.** Thử $$X_n^{(p)}=C\cdot 3^n$$ ($$3$$ không phải nghiệm $$r=1$$):  
$$C\cdot 3^n = 2C\cdot 3^{n-1} - C\cdot 3^{n-2} + 3^n.$$  
Chia $$3^{n-2}$$: $$9C = 6C - C + 9 \Rightarrow 4C=9 \Rightarrow C=\dfrac{9}{4}$$.  
Vậy $$X_n^{(p)}=\dfrac{9}{4}\,3^n$$.

**Tổng quát + điều kiện đầu.**  
$$X_n = A + Bn + \dfrac{9}{4}\,3^n.$$  
$$n=0$$: $$A+\dfrac{9}{4}=1 \Rightarrow A=-\dfrac{5}{4}$$.  
$$n=1$$: $$-\dfrac{5}{4}+B+\dfrac{27}{4}=3 \Rightarrow B=-\dfrac{5}{2}$$.  
$$X_n = -\dfrac{5}{4} - \dfrac{5}{2}n + \dfrac{9}{4}\,3^n.$$  
Kiểm $$n=2$$: truy hồi $$X_2=2\cdot 3-1+9=14$$; công thức $$-5/4-5+(9/4)\cdot 9=14$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ ($$f(n)=n^2$$, bậc 2).**  
$$a_n = 2a_{n-1} + a_{n-2} + n^2.$$  
Thuần nhất: $$r^2-2r-1=0$$ → $$r=1\pm\sqrt{2}$$,  
$$a_n^{(h)}=C_1(1+\sqrt{2})^n + C_2(1-\sqrt{2})^n.$$  
Vì $$1$$ không phải nghiệm đặc trưng, thử $$a_n^{(p)}=An^2+Bn+C$$.  
Thế $$a_n-2a_{n-1}-a_{n-2}=n^2$$, khai $$(n-1)^2$$, $$(n-2)^2$$ và so hệ số:  
$$A=-\dfrac12,\quad B=-2,\quad C=-\dfrac52.$$  
Vậy  
$$a_n = C_1(1+\sqrt{2})^n + C_2(1-\sqrt{2})^n - \dfrac{n^2}{2} - 2n - \dfrac{5}{2},$$  
với $$C_1,C_2$$ từ điều kiện đầu (nếu đề cho).

</div>

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

### Bài tập 4 (từ giáo trình — bậc 1)

Giải $$x_n = 2x_{n-1} + 1$$, $$x_1 = 1$$. Viết công thức đóng và $$x_5$$.

<details>
<summary>Đáp án</summary>

$$x_n = 2^n - 1$$; $$x_5 = 31$$.

</details>

### Bài tập 5 (tổng bình phương)

Đặt $$a_n = a_{n-1} + n^2$$, $$a_0=0$$. Giải bằng hệ số bất định (nhắc: cộng hưởng với $$r=1$$) và đối chiếu công thức $$\sum_{k=1}^n k^2$$.

<details>
<summary>Đáp án</summary>

$$a_n = \dfrac{n(n+1)(2n+1)}{6}$$.

</details>

### Bài tập 6 (bậc 2 + $$3^n$$)

Giải $$X_n = 2X_{n-1} - X_{n-2} + 3^n$$, $$X_0=1$$, $$X_1=3$$ (làm đủ ba bước: thuần nhất, riêng, điều kiện đầu).

<details>
<summary>Đáp án</summary>

$$X_n = -\dfrac{5}{4} - \dfrac{5}{2}n + \dfrac{9}{4}\,3^n$$  
(xem ví dụ 5b trong bài).

</details>

### Bài tập 7 (thách thức)

Giải $$a_n = 2a_{n-1} + a_{n-2} + n^2$$ với $$a_0=0$$, $$a_1=1$$ (dùng dạng riêng ở ví dụ 5b, rồi tìm $$C_1,C_2$$).

<details>
<summary>Đáp án</summary>

$$a_n^{(p)} = -\dfrac{n^2}{2}-2n-\dfrac{5}{2}$$.  
$$a_n = C_1(1+\sqrt{2})^n + C_2(1-\sqrt{2})^n + a_n^{(p)}$$.  
Từ $$a_0,a_1$$ giải hệ tuyến tính cho $$C_1,C_2$$ (tính số: $$n=0$$: $$C_1+C_2-5/2=0$$; $$n=1$$: $$C_1(1+\sqrt{2})+C_2(1-\sqrt{2})-1/2-2-5/2=1$$).

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=ghSnXV4RHiI">Solving non-homogeneous recurrence relations</a> — worked examples
- Tài liệu gốc khóa: `material/Chuong 3. He Thuc Hoi Quy.pdf` (bậc 1–2, nghiệm bội / phức / không thuần nhất)

## Tóm tắt

- Quan hệ không thuần nhất: $$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k} + f(n)$$.
- **Nguyên lý chồng chất**: $$a_n = a_n^{(h)} + a_n^{(p)}$$ — mọi nghiệm = một riêng + thuần nhất tổng quát.
- **Hệ số bất định**: đoán $$a_n^{(p)}$$ cùng họ $$f(n)$$ (hằng, đa thức, $$b^n$$).
- **Cộng hưởng**: dạng thử trùng nghiệm thuần nhất → nhân $$n$$ (hoặc $$n^s$$); với $$a_n-a_{n-1}=n^2$$ nhận công thức tổng bình phương.
- Ví dụ chuẩn: $$2x_{n-1}+1$$, $$+3^n$$ với $$(r-1)^2$$, $$+n^2$$ bậc 2.
- Ứng dụng: chia để trị $$T(n)=2T(n/2)+n$$.

Trong bài tiếp theo, chúng ta tổng hợp ứng dụng quan hệ truy hồi trong thuật toán và hệ thống thực tế.
