---

layout: post
title: "Giới thiệu Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 1
required: true
lang: vi
excerpt: "Trong chương này chúng ta giới thiệu hàm sinh (generating function) — công cụ gói cả một dãy vô hạn vào một biểu thức duy nhất để thao tác bằng đại số. Thay…"
---

<div class="textbook-epigraph" markdown="1">

"Generating functions are a bridge between discrete structures and continuous analysis."

<span class="epigraph-attribution">— Herbert Wilf (paraphrased)</span>

</div>

Trong chương này chúng ta giới thiệu **hàm sinh** (generating function) — công cụ gói cả một dãy vô hạn $$a_0, a_1, a_2, \ldots$$ vào một biểu thức duy nhất $$G(x) = \sum_{n\ge 0} a_n x^n$$ để thao tác bằng đại số. Thay vì liệt kê từng số hạng, chúng ta làm việc trên chuỗi lũy thừa hình thức; các phép cộng, nhân, dịch chỉ số và đạo hàm trên $$G(x)$$ phản ánh trực tiếp cấu trúc bài toán đếm hoặc truy hồi phía sau. Từ góc nhìn khoa học máy tính, đây là một cách **đổi biểu diễn** — tương tự việc chọn cấu trúc dữ liệu phù hợp trước khi xử lý — giúp lời giải gọn và có hệ thống hơn.

Mục này làm quen với định nghĩa, ký hiệu hệ số $$[x^n]G(x)$$, và các phép toán cơ bản trên hàm sinh.

![Chuỗi lũy thừa hình thức](/discrete-mathematics-for-computer-science-iuh/img/course/Laurent_series.svg)

<p class="textbook-figure-caption" data-figure="11.1">Chuỗi lũy thừa $G(x)=\sum a_n x^n$ — mỗi hệ số $a_n$ mã hóa một số hạng của dãy.</p>
![Hàm sinh (generating function)](/discrete-mathematics-for-computer-science-iuh/img/course/R._V._Lapshin__Generating_functions_and_squares.png)

<p class="textbook-figure-caption" data-figure="11.2">Hàm sinh gói cả dãy số vào một biểu thức duy nhất để thao tác bằng đại số.</p>
![Leonhard Euler](/discrete-mathematics-for-computer-science-iuh/img/course/Leonhard_Euler.jpg)

<p class="textbook-figure-caption" data-figure="11.3">Leonhard Euler (1707–1783) — nhà toán học tiên phong trong lý thuyết hàm sinh và chuỗi lũy thừa.</p>
![Dãy số học](/discrete-mathematics-for-computer-science-iuh/img/course/Arithmetic_progression.svg)

<p class="textbook-figure-caption" data-figure="11.4">Dãy số học là ví dụ đầu tiên: hệ số tăng tuyến tính tương ứng với cấu trúc đếm đơn giản.</p>
![Ký hiệu tổng Σ](/discrete-mathematics-for-computer-science-iuh/img/course/Sigma_summation_notation.svg)

<p class="textbook-figure-caption" data-figure="11.5">Ký hiệu Σ liên kết hàm sinh với các tổng hữu hạn và vô hạn trong tổ hợp.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** hàm sinh thông thường $$G(x)=\sum a_n x^n$$ và ký hiệu hệ số $$[x^n]G(x)$$.
- **Phân biệt** chuỗi lũy thừa hình thức và chuỗi hội tụ trong ngữ cảnh toán rời rạc.
- **Áp dụng** các phép cộng, nhân, dịch chỉ số và đạo hàm trên hàm sinh.
- **Nhận biết** các hàm sinh chuẩn: hình học, nhị thức, hệ số tổ hợp.
- **Giải thích** vai trò hàm sinh trong đếm, phân tích thuật toán và mô hình trạng thái.

**Từ khóa**: hàm sinh (generating function), chuỗi lũy thừa hình thức (formal power series), hệ số $$[x^n]$$, phép nhân Cauchy, hàm sinh hình học.
</div>

## Định nghĩa hàm sinh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho dãy số $$a_0, a_1, a_2, \ldots$$. **Hàm sinh thông thường** (ordinary generating function, OGF) của dãy là

$$G(x) = \sum_{n=0}^{\infty} a_n x^n = a_0 + a_1 x + a_2 x^2 + \cdots$$

Ký hiệu $$[x^n]G(x) = a_n$$ nghĩa là $$a_n$$ là hệ số của $$x^n$$ trong khai triển của $$G(x)$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Dãy hằng $$1, 1, 1, \ldots$$ có hàm sinh

$$G(x) = 1 + x + x^2 + \cdots = \frac{1}{1-x}$$

(khi xem là chuỗi hình thức hoặc chuỗi hội tụ với $$|x| < 1$$).
</div>

## Chuỗi lũy thừa hình thức

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Chuỗi lũy thừa hình thức** là đối tượng đại số $$G(x) = \sum_{n \ge 0} a_n x^n$$ trong đó ta chỉ quan tâm đến **hệ số** $$a_n$$, không cần xét miền hội tụ của $$x$$.
</div>

Hai chuỗi hình thức bằng nhau khi và chỉ khi mọi hệ số tương ứng trùng nhau. Điều này cho phép ta thao tác đại số (cộng, nhân, đạo hàm) trên dãy mà không lo vấn đề hội tụ.

## Các phép toán cơ bản

| Phép toán trên dãy | Tác động lên $$G(x)$$ |
|:---|:---|
| $$b_n = a_n + c_n$$ | $$B(x) = A(x) + C(x)$$ |
| $$b_n = \sum_{k=0}^{n} a_k c_{n-k}$$ (tích chập) | $$B(x) = A(x) \cdot C(x)$$ |
| $$b_n = a_{n-1}$$ ($$n \ge 1$$), $$b_0 = 0$$ | $$B(x) = x \cdot A(x)$$ |
| $$b_n = (n+1) a_{n+1}$$ | $$B(x) = A'(x)$$ |

<div class="textbook-theorem" markdown="1">
**Định lý** (nhân Cauchy): Nếu $$A(x) = \sum a_n x^n$$ và $$C(x) = \sum c_n x^n$$ thì hệ số của $$A(x) \cdot C(x)$$ tại $$x^n$$ là

$$[x^n](A \cdot C) = \sum_{k=0}^{n} a_k c_{n-k}$$

Đây là công thức **tích chập** — nền của đếm có cấu trúc (chọn $$k$$ từ cấu hình A, $$n-k$$ từ cấu hình C).
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (dịch chỉ số): Dãy Fibonacci thỏa $$F_n = F_{n-1} + F_{n-2}$$. Nhân truy hồi với $$x^n$$ và cộng cho thấy dịch $$F_{n-1}$$ tương ứng nhân $$G(x)$$ với $$x$$, dịch $$F_{n-2}$$ tương ứng nhân $$x^2$$ — chủ đề mục 11.2.
</div>

## Hàm sinh chuẩn

Các công thức sau dùng lặp lại trong mọi bài toán hàm sinh:

| Dãy $$a_n$$ | Hàm sinh $$G(x)$$ |
|:---|:---|
| $$1, 1, 1, \ldots$$ | $$\dfrac{1}{1-x}$$ |
| $$0, 1, 2, 3, \ldots$$ ($$a_n = n$$) | $$\dfrac{x}{(1-x)^2}$$ |
| $$\binom{n+k}{k}$$ | $$\dfrac{1}{(1-x)^{k+1}}$$ |
| $$1, 0, 1, 0, \ldots$$ | $$\dfrac{1}{1-x^2}$$ |

<div class="textbook-example" markdown="1">
**Ví dụ** (đếm cách chia tiền): Có bao nhiêu cách đưa tổng $$n$$ bằng các đồng 1đ và 2đ? Mỗi cách tương ứng một tổ hợp số 1 và 2. Hàm sinh là tích

$$G(x) = \frac{1}{1-x} \cdot \frac{1}{1-x^2}$$

Hệ số $$[x^n]G(x)$$ cho đáp số — không cần liệt kê từng cách.
</div>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Phần này liên hệ khái niệm toán học với bài toán thực tế trong lập trình và hệ thống.

Hàm sinh được dùng để đếm cấu hình, phân tích thuật toán, mô hình hóa trạng thái động và suy ra công thức cho số cách phân rã một đối tượng tổ hợp. Trong lập trình sinh ngẫu nhiên và phân tích ký hiệu, các chuỗi sinh còn cho phép suy ra phân phối kích thước của đối tượng sinh ra.

```python
def coeffs(seq):
    return " + ".join(f"{a}x^{i}" if i else str(a) for i, a in enumerate(seq))

print(coeffs([1, 1, 1, 1]))
```

## Bài tập

### Bài tập 1

Tìm hàm sinh của dãy $$a_n = 2$$ với mọi $$n \ge 0$$.

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$
G(x)=\sum_{n\ge0}2x^n=\frac{2}{1-x}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2

Tìm hàm sinh của dãy $a_n=n$.

<details>
<summary>Đáp án</summary>

Dùng công thức chuẩn:

<div class="textbook-equation" markdown="1">
$$
\sum_{n\ge1}nx^n=\frac{x}{(1-x)^2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 3

Giải thích vì sao dịch chuỗi bằng cách nhân với $x$ lại hữu ích khi làm việc với truy hồi.

<details>
<summary>Đáp án</summary>

Vì các hạng $$a_{n-1}$$, $$a_{n-2}$$ trong truy hồi sẽ trở thành các hệ số của chuỗi sau khi nhân với $$x$$ hoặc $$x^2$$. Nhờ vậy, truy hồi được biến thành phương trình đại số trên hàm sinh.

</details>

### Bài tập 4

Cho $$A(x) = 1 + x$$ và $$C(x) = 1 + x + x^2$$. Tính hệ số $$[x^2](A \cdot C)$$ bằng công thức tích chập.

<details>
<summary>Đáp án</summary>

$$[x^2](A \cdot C) = a_0 c_2 + a_1 c_1 + a_2 c_0 = 1 \cdot 1 + 1 \cdot 1 + 0 \cdot 1 = 2$$. Kiểm tra: $$(1+x)(1+x+x^2) = 1 + 2x + 2x^2 + x^3$$.

</details>

### Bài tập 5

Dãy $$a_n = \binom{n+2}{2}$$ (số tam giác). Tìm hàm sinh $$G(x)$$.

<details>
<summary>Đáp án</summary>

$$\sum_{n \ge 0} \binom{n+2}{2} x^n = \frac{1}{(1-x)^3}$$ — hàm sinh của hệ số nhị thức bậc 2.

</details>

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- Hàm sinh thông thường: $$G(x)=\sum_{n\ge 0} a_n x^n$$; ký hiệu $$[x^n]G(x)=a_n$$.
- Chuỗi lũy thừa **hình thức** cho phép thao tác hệ số mà không cần xét hội tụ.
- Ví dụ chuẩn: $$1+x+x^2+\cdots = 1/(1-x)$$; $$\sum nx^n = x/(1-x)^2$$.
- Phép cộng, nhân, dịch chỉ số và đạo hàm mã hóa thao tác trên dãy.
- Trong CS: đếm cấu hình, phân tích thuật toán, mô hình trạng thái động.

Trong bài tiếp theo, chúng ta dùng hàm sinh để **giải quan hệ truy hồi** bằng phương pháp bốn bước.
