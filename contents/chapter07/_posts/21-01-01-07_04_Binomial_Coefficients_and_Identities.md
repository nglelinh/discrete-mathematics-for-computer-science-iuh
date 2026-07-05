---

layout: post
title: "Hệ số Nhị thức và Đồng nhất thức Tổ hợp"
categories: chapter07
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã học nguyên lý bù trừ. Mục này giới thiệu hệ số nhị thức và các đồng nhất thức tổ hợp — cầu nối giữa đại số và tổ hợp."
---

Ở mục trước chúng ta đã học nguyên lý bù trừ. Mục này giới thiệu **hệ số nhị thức** và các **đồng nhất thức tổ hợp** — cầu nối giữa đại số và tổ hợp.

Biểu thức $$(a+b)^n$$ nhìn có vẻ thuần đại số, nhưng phía sau là câu chuyện đếm rất rõ: ở mỗi lần nhân, chúng ta chọn lấy $$a$$ hay $$b$$, rồi xem một hạng tử cụ thể xuất hiện bao nhiêu lần. Khi đã hiểu ý nghĩa đếm của hệ số nhị thức, nhiều đồng nhất thức trở nên dễ nhớ hơn vì có thể được chứng minh bằng hai cách đếm cùng một đối tượng.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Sử dụng** tam giác Pascal và định lý nhị thức.
- **Chứng minh** các đẳng thức tổ hợp cơ bản.
- **Áp dụng** hệ số nhị thức trong xác suất và thuật toán.

**Từ khóa**: hệ số nhị thức, tam giác Pascal, định lý nhị thức, đồng nhất tổ hợp.
</div>

## 1. Hệ số nhị thức

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với $0\le k\le n$, hệ số nhị thức $\binom{n}{k}$ là số cách chọn $k$ phần tử từ một tập có $n$ phần tử, không xét thứ tự.
</div>

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Quy ước $\binom{n}{k}=0$ nếu $k<0$ hoặc $k>n$.

![Hệ số nhị thức — n chọn k](/discrete-mathematics-for-computer-science-iuh/img/course/Combination.svg)

<p class="textbook-figure-caption" data-figure="7.16">Hệ số nhị thức $\binom{n}{k}$ đếm số cách chọn $k$ phần tử từ $n$ phần tử, không xét thứ tự.</p>
**Ký hiệu**: $\binom{n}{k}$ đọc là “$n$ chọn $k$”. Trong một số tài liệu cũ, ký hiệu $C(n,k)$ hoặc $C_n^k$ cũng được dùng.

<div class="content-box example-box textbook-block" markdown="1">
<div class="textbook-example" markdown="1">
**Ví dụ**: Từ 10 sinh viên chọn 3 sinh viên làm nhóm thuyết trình:

<div class="textbook-equation" markdown="1">
$$
\binom{10}{3}=\frac{10\cdot 9\cdot 8}{3\cdot 2\cdot 1}=120.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>
</div>

## 2. Định lý nhị thức

<div class="textbook-theorem" markdown="1">
**Định lý**: Với $n$ là số nguyên không âm,
</div>

<div class="textbook-equation" markdown="1">
$$
(x+y)^n=\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh tổ hợp**: Khi nhân

<div class="textbook-equation" markdown="1">
$$
(x+y)^n=(x+y)(x+y)\cdots(x+y),
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
mỗi hạng tử trong khai triển được tạo bằng cách chọn từ mỗi ngoặc một $x$ hoặc một $y$. Để nhận được hạng $x^{n-k}y^k$, chúng ta phải chọn $y$ từ đúng $k$ trong $n$ ngoặc. Có $\binom{n}{k}$ cách chọn các ngoặc đó. Vì vậy hệ số của $x^{n-k}y^k$ là $\binom{n}{k}$.

![Trực quan định lý nhị thức](/discrete-mathematics-for-computer-science-iuh/img/course/Binomial_theorem_visualisation.svg)

<p class="textbook-figure-caption" data-figure="7.17">Mỗi hạng trong khai triển $(x+y)^n$ tương ứng một cách chọn $k$ vị trí lấy $y$ từ $n$ ngoặc.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**:

<div class="textbook-equation" markdown="1">
$$
(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

## 3. Tam giác Pascal và truy hồi cơ bản

Tam giác Pascal được xây dựng bằng quy tắc mỗi số bằng tổng của hai số ngay phía trên nó:

```text
n=0:        1
n=1:       1 1
n=2:      1 2 1
n=3:     1 3 3 1
n=4:    1 4 6 4 1
n=5:   1 5 10 10 5 1
```

![Tam giác Pascal](/discrete-mathematics-for-computer-science-iuh/img/course/Pascal_triangle.svg)

<p class="textbook-figure-caption" data-figure="7.18">Tam giác Pascal — mỗi hệ số bằng tổng hai hệ số ngay phía trên theo quy tắc Pascal.</p>
**Đồng nhất thức Pascal**:

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh tổ hợp**: Chọn $k$ người từ $n$ người. Cố định một người đặc biệt tên An. Mọi nhóm được chia thành hai loại: nhóm có An, khi đó chọn thêm $k-1$ người từ $n-1$ người; nhóm không có An, khi đó chọn $k$ người từ $n-1$ người. Hai loại rời nhau và bao phủ toàn bộ khả năng.

![Khai triển nhị thức và tam giác Pascal](/discrete-mathematics-for-computer-science-iuh/img/course/Binomial_expansion_with_Pascal_s_triangle.svg)

<p class="textbook-figure-caption" data-figure="7.19">Khai triển $(a+b)^n$ — hệ số mỗi hạng chính là $\binom{n}{k}$ ở hàng thứ $n$ của tam giác Pascal.</p>
<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học nhập $n,k$, công cụ tô màu hai ô $\binom{n-1}{k-1}$ và $\binom{n-1}{k}$ trong tam giác Pascal, rồi hiển thị tổng bằng $\binom{n}{k}$.
</div>

## 4. Các đồng nhất thức quan trọng

### 4.1. Đối xứng

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k}=\binom{n}{n-k}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Chọn $k$ phần tử để lấy tương đương với chọn $n-k$ phần tử để bỏ lại.

### 4.2. Tổng một hàng

<div class="textbook-equation" markdown="1">
$$
\sum_{k=0}^{n}\binom{n}{k}=2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh**: Vế trái đếm tất cả tập con của một tập $n$ phần tử theo kích thước. Vế phải đếm trực tiếp: mỗi phần tử có hai lựa chọn, thuộc hoặc không thuộc tập con.

### 4.3. Tổng xen kẽ

<div class="textbook-equation" markdown="1">
$$
\sum_{k=0}^{n}(-1)^k\binom{n}{k}=0 \quad (n\ge 1).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Thay $x=1,y=-1$ vào định lý nhị thức chúng ta được $(1-1)^n=0$.

### 4.4. Đồng nhất thức “cây gậy khúc côn cầu”

<div class="textbook-equation" markdown="1">
$$
\sum_{i=r}^{n}\binom{i}{r}=\binom{n+1}{r+1}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Trực giác**: Đếm số cách chọn $r+1$ phần tử từ $\{1,2,\ldots,n+1\}$. Nếu phần tử lớn nhất là $i+1$, chúng ta chọn $r$ phần tử còn lại từ $i$ phần tử nhỏ hơn, có $\binom{i}{r}$ cách.

### 4.5. Đồng nhất thức Vandermonde

<div class="textbook-equation" markdown="1">
$$
\sum_{i=0}^{r}\binom{m}{i}\binom{n}{r-i}=\binom{m+n}{r}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh tổ hợp**: Chọn $r$ người từ một lớp gồm $m$ nam và $n$ nữ. Nếu chọn đúng $i$ nam thì có $\binom{m}{i}\binom{n}{r-i}$ cách. Cộng trên mọi $i$ cho kết quả bằng cách chọn trực tiếp $r$ người từ $m+n$ người.

## 6. Ứng dụng trong Khoa học Máy tính

![Blaise Pascal — nhà toán học Pháp](/discrete-mathematics-for-computer-science-iuh/img/course/Blaise_Pascal_Versailles.JPG)

<p class="textbook-figure-caption" data-figure="7.20">Blaise Pascal (1623–1662) — cùng Fermat đặt nền móng cho xác suất và tổ hợp hiện đại.</p>
Hệ số nhị thức xuất hiện trong phân tích thuật toán chia để trị, xác suất Bernoulli, mã sửa lỗi, học máy và sinh ngẫu nhiên tập con. Trong kiểm thử phần mềm, nếu cần chọn mọi tập con gồm $k$ tính năng từ $n$ tính năng để kiểm tra tương tác, số ca kiểm thử là $\binom{n}{k}$.

```python
from math import comb

n = 20
for k in range(0, 6):
    print(k, comb(n, k))
```

<div class="interactive-tool" markdown="1">
<h3>🔬 Công cụ Tương tác: Máy tính Hệ số Nhị thức</h3>
<p>Công cụ này tính $$C(n,k)$$, tô sáng vị trí tương ứng trong tam giác Pascal và hiển thị khai triển $$(a+b)^n$$.</p>
<div data-demo="binomial-coefficient-calc"></div>
</div>
<script src="{{ '/public/js/binomial-coefficient-calc.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Khai triển

Tìm hệ số của $x^7y^3$ trong $(x+y)^{10}$.

<details>
<summary>Đáp án</summary>

Vì số mũ của $y$ là $3$, hệ số là

<div class="textbook-equation" markdown="1">
$$
\binom{10}{3}=120.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2: Chứng minh bằng tổ hợp

Chứng minh $\binom{n}{1}+\binom{n}{2}+\cdots+\binom{n}{n}=2^n-1$.

<details>
<summary>Đáp án</summary>

Tổng tất cả $\binom{n}{k}$ từ $k=0$ đến $n$ là $2^n$. Hạng $k=0$ đếm tập rỗng. Bỏ tập rỗng còn $2^n-1$ tập con không rỗng.

</details>

### Bài tập 3: Vandermonde

Một đội gồm 5 sinh viên CNTT và 4 sinh viên Toán. Có bao nhiêu cách chọn 3 người?

<details>
<summary>Đáp án</summary>

Theo Vandermonde:

<div class="textbook-equation" markdown="1">
$$
\binom{5}{0}\binom{4}{3}+\binom{5}{1}\binom{4}{2}+\binom{5}{2}\binom{4}{1}+\binom{5}{3}\binom{4}{0}
=4+30+40+10=84.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cũng bằng $\binom{9}{3}=84$.

</details>

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **Hệ số nhị thức** $\binom{n}{k}$ đếm số cách chọn $k$ phần tử từ $n$ phần tử.
- **Định lý nhị thức** liên hệ tổ hợp với khai triển đại số của $(x+y)^n$.
- **Tam giác Pascal** biểu diễn truy hồi $\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}$.
- **Đồng nhất thức tổ hợp** thường có hai kiểu chứng minh: đại số và đếm hai cách.
- **Ứng dụng CS** gồm kiểm thử tổ hợp, xác suất, sinh tập con và phân tích thuật toán.

Trong bài tiếp theo, chúng ta sẽ học về hoán vị và tổ hợp mở rộng.
