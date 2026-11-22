---

layout: post
title: "Hệ số Nhị thức và Đồng nhất thức Tổ hợp"
categories: chapter07
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Hệ số nhị thức, định lý nhị thức, tam giác Pascal và các đồng nhất thức tổ hợp quan trọng — cầu nối giữa đại số và phép đếm."
---

Ở mục trước, chúng ta đã học nguyên lý bù trừ. Mục này giới thiệu **hệ số nhị thức** và các **đồng nhất thức tổ hợp** — cầu nối trực tiếp giữa đại số và phép đếm.

Biểu thức $$(a+b)^n$$ thoạt nhìn có vẻ thuần đại số, nhưng phía sau nó là một câu chuyện đếm rất rõ ràng: ở mỗi thừa số $$(a+b)$$, ta chọn lấy $$a$$ hoặc lấy $$b$$, rồi đếm xem một hạng tử cụ thể xuất hiện bao nhiêu lần. Khi nắm được ý nghĩa tổ hợp của hệ số nhị thức, nhiều đồng nhất thức sẽ trở nên tự nhiên và dễ nhớ hơn vì ta có thể chứng minh chúng bằng cách đếm cùng một đối tượng theo hai cách khác nhau.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Sử dụng** tam giác Pascal và định lý nhị thức để khai triển biểu thức.
- **Chứng minh** các đồng nhất thức tổ hợp cơ bản bằng phương pháp đại số và phương pháp đếm hai cách.
- **Áp dụng** hệ số nhị thức trong xác suất, kiểm thử và thiết kế thuật toán.

**Từ khóa**: hệ số nhị thức, tam giác Pascal, định lý nhị thức, đồng nhất thức tổ hợp.
</div>

## Hệ số nhị thức

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với $$0\le k\le n$$, hệ số nhị thức $$\binom{n}{k}$$ là số cách chọn $$k$$ phần tử từ một tập gồm $$n$$ phần tử mà không xét thứ tự.
</div>

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Quy ước $$\binom{n}{k}=0$$ nếu $$k<0$$ hoặc $$k>n$$.

![Hệ số nhị thức — n chọn k](/discrete-mathematics-for-computer-science-iuh/img/course/Combination.svg)

<p class="textbook-figure-caption" data-figure="7.16">Hệ số nhị thức $$\binom{n}{k}$$ đếm số cách chọn $$k$$ phần tử từ $$n$$ phần tử, không xét thứ tự.</p>
**Ký hiệu**: $$\binom{n}{k}$$ đọc là “$$n$$ chọn $$k$$”. Trong nhiều tài liệu, ký hiệu $$C(n,k)$$ hoặc $$C_n^k$$ cũng được dùng tương đương.

<div class="content-box example-box textbook-block" markdown="1">
<div class="textbook-example" markdown="1">
**Ví dụ**: Từ 10 sinh viên chọn 3 sinh viên lập nhóm thuyết trình:

<div class="textbook-equation" markdown="1">
$$
\binom{10}{3}=\frac{10\cdot 9\cdot 8}{3\cdot 2\cdot 1}=120.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>
</div>

## Định lý nhị thức

<div class="textbook-theorem" markdown="1">
**Định lý**: Với mọi số nguyên không âm $$n$$,

<div class="textbook-equation" markdown="1">
$$
(x+y)^n=\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh tổ hợp**: Khi khai triển tích

<div class="textbook-equation" markdown="1">
$$
(x+y)^n=(x+y)(x+y)\cdots(x+y),
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
mỗi hạng tử được tạo thành bằng cách chọn $$x$$ hoặc $$y$$ từ từng ngoặc. Để thu được hạng tử $$x^{n-k}y^k$$, ta phải chọn $$y$$ từ đúng $$k$$ trong tổng số $$n$$ ngoặc (và chọn $$x$$ từ $$n-k$$ ngoặc còn lại). Vì có $$\binom{n}{k}$$ cách chọn $$k$$ ngoặc đó nên hệ số của $$x^{n-k}y^k$$ chính là $$\binom{n}{k}$$.
</div>

![Trực quan định lý nhị thức](/discrete-mathematics-for-computer-science-iuh/img/course/Binomial_theorem_visualisation.svg)

<p class="textbook-figure-caption" data-figure="7.17">Mỗi hạng tử trong khai triển $$(x+y)^n$$ tương ứng với một cách chọn $$k$$ vị trí lấy $$y$$ từ $$n$$ ngoặc.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**:

<div class="textbook-equation" markdown="1">
$$
(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

## Tam giác Pascal và hệ thức truy hồi cơ bản

Tam giác Pascal được xây dựng theo quy tắc mỗi số ở bên trong bằng tổng hai số đứng ngay phía trên nó:

```text
n=0:        1
n=1:       1 1
n=2:      1 2 1
n=3:     1 3 3 1
n=4:    1 4 6 4 1
n=5:   1 5 10 10 5 1
```

![Tam giác Pascal](/discrete-mathematics-for-computer-science-iuh/img/course/Pascal_triangle.svg)

<p class="textbook-figure-caption" data-figure="7.18">Tam giác Pascal — mỗi hệ số bằng tổng hai hệ số ngay phía trên theo đồng nhất thức Pascal.</p>
**Đồng nhất thức Pascal**:

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh tổ hợp**: Xét bài toán chọn $$k$$ người từ $$n$$ người và cố định một người tên An. Mọi nhóm được chọn chia thành hai trường hợp rời nhau: nhóm có mặt An (cần chọn thêm $$k-1$$ người từ $$n-1$$ người còn lại, có $$\binom{n-1}{k-1}$$ cách) và nhóm không có mặt An (cần chọn đủ $$k$$ người từ $$n-1$$ người còn lại, có $$\binom{n-1}{k}$$ cách). Hai trường hợp này bao phủ toàn bộ khả năng nên ta thu được đẳng thức trên.

![Khai triển nhị thức và tam giác Pascal](/discrete-mathematics-for-computer-science-iuh/img/course/Binomial_expansion_with_Pascal_s_triangle.svg)

<p class="textbook-figure-caption" data-figure="7.19">Khai triển $$(a+b)^n$$ — hệ số của mỗi hạng tử chính là $$\binom{n}{k}$$ nằm ở hàng thứ $$n$$ của tam giác Pascal.</p>
<div class="interactive-demo" markdown="1">
**Demo tương tác**: Nhập $$n, k$$ để công cụ tô màu hai ô $$\binom{n-1}{k-1}$$ và $$\binom{n-1}{k}$$ trong tam giác Pascal, rồi hiển thị tổng của chúng bằng $$\binom{n}{k}$$.
</div>

### Minh hoạ tam giác Pascal: cộng từ đỉnh xuống

Quan sát tam giác Pascal được xây dựng từng hàng từ đỉnh: với mỗi ô, hai ô cha ngay phía trên sẽ sáng lên và cộng lại (ví dụ 1 + 2 = 3). Công cụ hỗ trợ Play/Dừng, tiến/lùi từng bước, chỉnh tốc độ, chọn số hàng (0–14), chuyển đổi giữa giá trị số và ký hiệu C(n,k), tô màu chẵn/lẻ (Sierpiński), cùng các thẻ minh họa tổng hàng $$2^n$$, tính đối xứng và đồng nhất thức cây gậy khúc côn cầu.

<div class="interactive-demo" markdown="1">
<div data-demo="pascal-explainer" data-rows="6"></div>
</div>
<script src="{{ '/public/js/explainers/counting-explainer.js' | relative_url }}"></script>

## Các đồng nhất thức quan trọng

### Tính đối xứng

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k}=\binom{n}{n-k}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Chọn $$k$$ phần tử để giữ lại tương đương với chọn $$n-k$$ phần tử để bỏ đi.

### Tổng một hàng

<div class="textbook-equation" markdown="1">
$$
\sum_{k=0}^{n}\binom{n}{k}=2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh**: Vế trái đếm tất cả các tập con của một tập $$n$$ phần tử theo từng kích thước $$k$$. Vế phải đếm trực tiếp theo từng phần tử: mỗi phần tử có đúng 2 lựa chọn (thuộc hoặc không thuộc tập con).

### Tổng xen kẽ

<div class="textbook-equation" markdown="1">
$$
\sum_{k=0}^{n}(-1)^k\binom{n}{k}=0 \quad (n\ge 1).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Thay $$x=1, y=-1$$ vào định lý nhị thức, ta thu được $$(1-1)^n=0$$.

### Đồng nhất thức “cây gậy khúc côn cầu”

<div class="textbook-equation" markdown="1">
$$
\sum_{i=r}^{n}\binom{i}{r}=\binom{n+1}{r+1}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Trực giác**: Đếm số cách chọn $$r+1$$ phần tử từ tập $$\{1,2,\ldots,n+1\}$$. Nếu phần tử lớn nhất được chọn là $$i+1$$ (với $$r \le i \le n$$), ta cần chọn thêm $$r$$ phần tử từ $$i$$ phần tử nhỏ hơn nó, có $$\binom{i}{r}$$ cách. Cộng theo mọi giá trị của $$i$$ cho vế trái.

### Đồng nhất thức Vandermonde

<div class="textbook-equation" markdown="1">
$$
\sum_{i=0}^{r}\binom{m}{i}\binom{n}{r-i}=\binom{m+n}{r}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh tổ hợp**: Xét bài toán chọn $$r$$ người từ một lớp gồm $$m$$ nam và $$n$$ nữ. Nếu chọn đúng $$i$$ nam và $$r-i$$ nữ thì có $$\binom{m}{i}\binom{n}{r-i}$$ cách. Cộng theo mọi $$i$$ từ $$0$$ đến $$r$$ cho tổng số cách bằng việc chọn trực tiếp $$r$$ người từ $$m+n$$ người.

### Video ngắn: Từ tam giác Pascal ra $$\pi$$

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/pascal-to-pi.mp4"></video>
</div>

Chuỗi Nilakantha $$\pi = 3 + \sum_{k\ge 1} (-1)^{k+1}\dfrac{4}{2k(2k+1)(2k+2)}$$ có thể viết lại thành $$\pi = 3 + \tfrac{2}{3}\sum_{k\ge 1} \dfrac{(-1)^{k+1}}{\binom{2k+2}{3}}$$. Các mẫu số $$\binom{4}{3}, \binom{6}{3}, \binom{8}{3}, \ldots = 4, 20, 56, 120, 220, \ldots$$ chính là các số nằm trên đường chéo thứ ba của tam giác Pascal, lấy cách một số.

## Ứng dụng trong Khoa học Máy tính

![Blaise Pascal — nhà toán học Pháp](/discrete-mathematics-for-computer-science-iuh/img/course/Blaise_Pascal_Versailles.JPG)

<p class="textbook-figure-caption" data-figure="7.20">Blaise Pascal (1623–1662) — cùng Fermat đặt nền móng cho lý thuyết xác suất và tổ hợp hiện đại.</p>
Hệ số nhị thức xuất hiện trong phân tích thuật toán chia để trị, xác suất Bernoulli, mã sửa lỗi, học máy và bài toán sinh ngẫu nhiên tập con. Trong kiểm thử phần mềm, nếu cần chọn mọi tập con gồm $$k$$ tính năng từ $$n$$ tính năng để kiểm tra tương tác, số nhóm cần xét là $$\binom{n}{k}$$.

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

### Minh hoạ tương tác

Minh hoạ tam giác Pascal tương tác: chọn một ô bất kỳ để xem hệ thức Pascal và tổng hàng $$2^n$$.

<div class="interactive-demo" markdown="1">
<div data-demo="counting-explainer" data-tab="pascal"></div>
</div>
<!-- Script counting-explainer.js đã được nạp ở khối Pascal phía trên (một bản runtime cho cả hai explainer). -->

## Bài tập thực hành

### Bài tập 1: Khai triển

Tìm hệ số của $$x^7y^3$$ trong khai triển $$(x+y)^{10}$$.

<details>
<summary>Đáp án</summary>

Vì số mũ của $$y$$ là $$3$$, hệ số cần tìm là:

<div class="textbook-equation" markdown="1">
$$
\binom{10}{3}=120.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2: Chứng minh bằng tổ hợp

Chứng minh $$\binom{n}{1}+\binom{n}{2}+\cdots+\binom{n}{n}=2^n-1$$.

<details>
<summary>Đáp án</summary>

Tổng tất cả $$\binom{n}{k}$$ với $$k$$ từ $$0$$ đến $$n$$ bằng $$2^n$$ (tổng số tập con của một tập $$n$$ phần tử). Hạng tử $$k=0$$ ứng với tập rỗng ($$\binom{n}{0} = 1$$). Bỏ tập rỗng đi, ta còn lại $$2^n-1$$ tập con khác rỗng.

</details>

### Bài tập 3: Vandermonde

Một đội gồm 5 sinh viên CNTT và 4 sinh viên Toán. Có bao nhiêu cách chọn 3 người từ đội này?

<details>
<summary>Đáp án</summary>

Áp dụng đồng nhất thức Vandermonde:

<div class="textbook-equation" markdown="1">
$$
\binom{5}{0}\binom{4}{3}+\binom{5}{1}\binom{4}{2}+\binom{5}{2}\binom{4}{1}+\binom{5}{3}\binom{4}{0}
=4+30+40+10=84.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Kết quả này trùng với cách chọn trực tiếp $$\binom{9}{3}=84$$.

</details>

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **Hệ số nhị thức** $$\binom{n}{k}$$ đếm số cách chọn $$k$$ phần tử từ $$n$$ phần tử mà không xét thứ tự.
- **Định lý nhị thức** kết nối phép đếm tổ hợp với khai triển đại số của $$(x+y)^n$$.
- **Tam giác Pascal** trực quan hóa hệ thức truy hồi $$\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}$$.
- **Đồng nhất thức tổ hợp** thường có thể chứng minh bằng hai cách: biến đổi đại số hoặc đếm hai cách.
- **Ứng dụng trong Khoa học Máy tính**: kiểm thử tổ hợp, xác suất, sinh tập con và phân tích thuật toán.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu hoán vị và tổ hợp mở rộng.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=stfqYC13bSY">[Discrete Mathematics] Binomial Theorem and Pascal&#x27;s Triangle</a> — TrevTutor, tiếng Anh. Giới thiệu định lý nhị thức và tam giác Pascal.
- <a href="https://www.youtube.com/watch?v=XMriWTvPXHI">The mathematical secrets of Pascal’s triangle - Wajdi Mohamed Ratemi</a> — TED-Ed, tiếng Anh. Giải thích các quy luật thú vị ẩn trong tam giác Pascal.
