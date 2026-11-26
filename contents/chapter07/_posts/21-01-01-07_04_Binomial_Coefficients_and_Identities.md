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


Khai triển đa thức $$(a+b)^5$$ cho dãy hệ số `1, 5, 10, 10, 5, 1`; đếm số tập con theo kích thước của tập 5 phần tử cũng ra đúng `1, 5, 10, 10, 5, 1`; đếm số đường đi ngắn nhất trên lưới ô vuông cũng chạm lại đúng hàng số ấy. **Hệ số nhị thức $$\binom{n}{k}$$** là sợi dây kỳ diệu nối liền đại số đa thức với tư duy tổ hợp—nơi nhiều đồng nhất thức tưởng như phức tạp bỗng trở nên trong suốt chỉ bằng một câu chuyện đếm hai cách.

Ở mục trước, chúng ta đã học nguyên lý bù trừ. Mục này giới thiệu **hệ số nhị thức** và các **đồng nhất thức tổ hợp** — cầu nối trực tiếp giữa đại số và phép đếm.

Biểu thức $$(a+b)^n$$ thoạt nhìn có vẻ thuần đại số, nhưng phía sau nó là một câu chuyện đếm rất rõ ràng: ở mỗi thừa số $$(a+b)$$, ta chọn lấy $$a$$ hoặc lấy $$b$$, rồi đếm xem một hạng tử cụ thể xuất hiện bao nhiêu lần. Khi nắm được ý nghĩa tổ hợp của hệ số nhị thức, nhiều đồng nhất thức sẽ trở nên tự nhiên và dễ nhớ hơn vì ta có thể chứng minh chúng bằng cách đếm cùng một đối tượng theo hai cách khác nhau.

## Kiến thức cần nhớ: Bốn trụ cột của Hệ số Nhị thức và Đồng nhất thức Tổ hợp

1. **Định lý Nhị thức $$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k}b^k$$**:
   Khi nhân $$n$$ dấu ngoặc $$(a+b)(a+b)\cdots(a+b)$$, mỗi số hạng $$a^{n-k}b^k$$ xuất hiện đúng bằng số cách chọn $$k$$ ngoặc lấy $$b$$ (và $$n-k$$ ngoặc còn lại lấy $$a$$), tức $$\binom{n}{k}$$.

2. **Hệ thức truy hồi Pascal $$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$**:
   Cố định một phần tử đặc biệt $$x$$: mọi tập con $$k$$ phần tử hoặc *chứa $$x$$* ($$\binom{n-1}{k-1}$$ cách), hoặc *không chứa $$x$$* ($$\binom{n-1}{k}$$ cách). Trong lập trình, công thức này cho phép tính $$\binom{n}{k}$$ bằng quy hoạch động $$O(nk)$$ chỉ dùng phép cộng, tránh tràn số khi tính $$n!$$.

3. **Nghệ thuật "Đếm hai cách" (Double Counting)**:
   Thay vì khai triển giai thừa dài dòng, ta nghĩ ra một bài toán đếm rồi giải theo hai góc nhìn khác nhau—nhờ đó các đồng nhất thức như **Tổng hàng ($$2^n$$)**, **Tổng xen kẽ ($$0$$)**, **Cây gậy khúc côn cầu** và **Vandermonde** hiện lên đầy trực giác.

4. **Cầu nối sang Xác suất, Đồ thị và Thuật toán**:
   Hệ số nhị thức là trái tim của phân phối nhị thức $$B(n, p)$$, đếm số đường đi đơn điệu trên lưới $$(0,0) \to (m,n)$$, và phân tích độ phức tạp thuật toán chia để trị.

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

<p class="textbook-figure-caption" data-figure="7.16">Hệ số nhị thức $\binom{n}{k}$ đếm số cách chọn $k$ phần tử từ $n$ phần tử, không xét thứ tự.</p>

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

<p class="textbook-figure-caption" data-figure="7.17">Mỗi hạng tử trong khai triển $(x+y)^n$ tương ứng với một cách chọn $k$ vị trí lấy $y$ từ $n$ ngoặc.</p>
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

<p class="textbook-figure-caption" data-figure="7.19">Khai triển $(a+b)^n$ — hệ số của mỗi hạng tử chính là $\binom{n}{k}$ nằm ở hàng thứ $n$ của tam giác Pascal.</p>
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

![Tam giác Pascal mở rộng](/discrete-mathematics-for-computer-science-iuh/img/course/Pascal_triangle_extended.svg)

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

### Từ tam giác Pascal ra $$\pi$$

Tam giác Pascal chỉ gồm các phép cộng số nguyên, vậy mà từ nó ta lấy ra được $$\pi$$. Đoạn video dưới đây (4 phút 18 giây, có lời dẫn) đi từng bước: dựng tam giác, nhìn các đường chéo, lấy cách một số trên đường chéo thứ ba, ghép thành một chuỗi, chứng minh chuỗi đó bằng $$\pi$$ rồi xem nó hội tụ nhanh đến đâu.

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/pascal-to-pi.mp4"></video>
</div>

**Ý chính.** Đường chéo thứ ba của tam giác Pascal gồm các số $$\binom{n}{3}$$: $$1, 4, 10, 20, 35, 56, 84, 120, 165, 220, \ldots$$. Nếu chỉ lấy cách một số, ta được $$\binom{4}{3}, \binom{6}{3}, \binom{8}{3}, \ldots = 4, 20, 56, 120, 220, \ldots$$ Lấy nghịch đảo của các số này rồi cộng trừ xen kẽ, kết quả tiến về $$\pi$$.

**Vì sao $$\binom{2k+2}{3}$$?** Đường chéo thứ nhất là $$\binom{n}{1}=n$$, đường chéo thứ hai là các số tam giác $$\binom{n}{2}$$, còn đường chéo thứ ba là $$\binom{n}{3}$$. Theo đồng nhất thức hình gậy khúc côn cầu, mỗi số trên đường chéo này bằng tổng các số liền trước của đường chéo bên cạnh, chẳng hạn $$20=\binom{6}{3}=1+3+6+10$$. Lấy hàng $$n=2k+2$$ (hàng $$4, 6, 8, \ldots$$) thì

<div class="textbook-equation" markdown="1">
$$
\binom{2k+2}{3}=\frac{(2k+2)(2k+1)(2k)}{6}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tích ba số nguyên liên tiếp $$2k,\,2k+1,\,2k+2$$ xuất hiện đúng ở mẫu số của chuỗi Nilakantha. Đó là lý do tam giác Pascal "nhìn thấy" chuỗi này: $$\dfrac{4}{2k(2k+1)(2k+2)}=\dfrac{2}{3}\cdot\dfrac{1}{\binom{2k+2}{3}}$$.

<div class="textbook-theorem" markdown="1">
**Định lý (chuỗi Nilakantha)**: Chuỗi sau hội tụ về $$\pi$$:

<div class="textbook-equation" markdown="1">
$$
\pi = 3+\frac{4}{2\cdot 3\cdot 4}-\frac{4}{4\cdot 5\cdot 6}+\frac{4}{6\cdot 7\cdot 8}-\cdots = 3+\frac{2}{3}\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{\binom{2k+2}{3}}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

Chuỗi này do Nilakantha Somayaji (Ấn Độ, thế kỷ 15) tìm ra. Hãy tính vài số hạng đầu. Cột "Số hạng" là $$\dfrac{4}{2k(2k+1)(2k+2)}$$ với dấu $$(-1)^{k+1}$$, cột $$S_k$$ là tổng riêng $$3+$$ (tổng $$k$$ số hạng đầu).

| $$k$$ | $$\binom{2k+2}{3}$$ | Số hạng | $$S_k$$ | $$\vert S_k-\pi\vert$$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 4 | $$+\tfrac{1}{6}$$ | 3,166667 | 0,0251 |
| 2 | 20 | $$-\tfrac{1}{30}$$ | 3,133333 | 0,0083 |
| 3 | 56 | $$+\tfrac{1}{84}$$ | 3,145238 | 0,0037 |
| 4 | 120 | $$-\tfrac{1}{180}$$ | 3,139683 | 0,0019 |
| 5 | 220 | $$+\tfrac{1}{330}$$ | 3,142713 | 0,0011 |
| 6 | 364 | $$-\tfrac{1}{546}$$ | 3,140881 | 0,00071 |
| 7 | 560 | $$+\tfrac{1}{840}$$ | 3,142072 | 0,00048 |
| 8 | 816 | $$-\tfrac{1}{1224}$$ | 3,141255 | 0,00034 |
| 9 | 1140 | $$+\tfrac{1}{1710}$$ | 3,141840 | 0,00025 |
| 10 | 1540 | $$-\tfrac{1}{2310}$$ | 3,141407 | 0,00019 |

Các tổng riêng nhảy lên xuống quanh $$\pi \approx 3{,}14159265$$ và biên độ giảm rất nhanh, vì $$\pi$$ luôn nằm giữa hai tổng riêng liên tiếp.

<div class="textbook-proof" markdown="1">
**Chứng minh**: Đặt $$m=2k$$ và tách phân thức:

<div class="textbook-equation" markdown="1">
$$
\frac{4}{m(m+1)(m+2)}=\frac{2}{m}-\frac{4}{m+1}+\frac{2}{m+2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Thử với $$m=2$$: vế trái bằng $$\tfrac{4}{24}=\tfrac{1}{6}$$, vế phải bằng $$1-\tfrac{4}{3}+\tfrac{1}{2}=\tfrac{1}{6}$$. Thay $$m=2k$$ rồi nhân dấu $$(-1)^{k+1}$$, tổng của chuỗi gồm hai phần.

*Phần chẵn* $$\dfrac{2}{2k}+\dfrac{2}{2k+2}=\dfrac{1}{k}+\dfrac{1}{k+1}$$. Tổng xen dấu của phần này là

<div class="textbook-equation" markdown="1">
$$
\left(1+\tfrac{1}{2}\right)-\left(\tfrac{1}{2}+\tfrac{1}{3}\right)+\left(\tfrac{1}{3}+\tfrac{1}{4}\right)-\cdots = 1,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

vì các số hạng triệt tiêu từng cặp (tổng riêng thứ $$n$$ bằng $$1\pm\frac{1}{n+1}$$ nên tiến về $$1$$).

*Phần lẻ* $$-\dfrac{4}{2k+1}$$. Theo chuỗi Leibniz $$1-\tfrac{1}{3}+\tfrac{1}{5}-\cdots=\tfrac{\pi}{4}$$, ta có $$\tfrac{1}{3}-\tfrac{1}{5}+\tfrac{1}{7}-\cdots=1-\tfrac{\pi}{4}$$. Do đó

<div class="textbook-equation" markdown="1">
$$
-4\left(\tfrac{1}{3}-\tfrac{1}{5}+\tfrac{1}{7}-\cdots\right)=-4\left(1-\tfrac{\pi}{4}\right)=\pi-4.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Cộng hai phần: $$1+(\pi-4)=\pi-3$$, nên $$3+(\pi-3)=\pi$$. $$\blacksquare$$
</div>

**Hội tụ nhanh đến đâu?** Đây là chuỗi đan dấu có số hạng giảm dần về $$0$$, nên sai số nhỏ hơn số hạng kế tiếp, khoảng $$\dfrac{1}{2k^3}$$. Tính chính xác hơn, sai số xấp xỉ $$\dfrac{1}{4k^3}$$. Bảng trên khớp với công thức này: ở $$k=10$$ có $$\frac{1}{4\cdot 10^3}=0{,}00025$$, so với sai số thật $$0{,}00019$$.

Chuỗi Leibniz có sai số cỡ $$\dfrac{1}{k}$$, nên mỗi chữ số thập phân đúng thêm đòi hỏi nhiều gấp $$10$$ lần số hạng. Với Nilakantha, nhân số hạng lên $$10$$ lần thì sai số giảm $$10^3$$ lần, tức được thêm $$3$$ chữ số:

| Số hạng $$k$$ | Sai số Leibniz | Sai số Nilakantha |
|:---:|:---:|:---:|
| 10 | $$\approx 10^{-1}$$ | $$\approx 10^{-4}$$ |
| 100 | $$\approx 10^{-2}$$ | $$\approx 10^{-7}$$ |
| 1000 | $$\approx 10^{-3}$$ | $$\approx 10^{-10}$$ |

Muốn đúng $$10$$ chữ số thập phân cần $$k=1709$$ số hạng. Con số này nhanh hơn Leibniz rất nhiều, nhưng vẫn kém xa các công thức hiện đại như chuỗi của Ramanujan hay Chudnovsky. Mục đích của ví dụ này là thấy một con số liên hệ với tam giác Pascal, không phải tìm cách tính $$\pi$$ hiệu quả nhất.

### Giải thích: Tìm tay hệ số của $$x^3$$ trong $$(2x - 1)^5$$ và kiểm chứng số đồng nhất thức Vandermonde

**Phần A — Tìm hệ số của $$x^3$$ trong khai triển $$(2x - 1)^5$$**

Áp dụng Định lý Nhị thức với $$a = 2x$$, $$b = -1$$, $$n = 5$$:
$$(2x - 1)^5 = \sum_{k=0}^{5} \binom{5}{k}(2x)^{5-k}(-1)^k.$$
Để thu được bậc $$x^3$$, ta cần $$5 - k = 3 \implies k = 2$$. Thay $$k = 2$$ vào số hạng tổng quát:
$$\binom{5}{2}(2x)^3(-1)^2 = \frac{5 \times 4}{2} \cdot (8x^3) \cdot (+1) = 10 \cdot 8x^3 = \mathbf{80x^3}.$$
*(Chú ý lỗi hay gặp: quên lũy thừa hệ số `2` thành $$2^3 = 8$$, hoặc quên dấu $$(-1)^k$$ khi $$k$$ lẻ!)*

**Phần B — Kiểm chứng bằng số & trực giác "Đếm hai cách" cho đồng nhất thức Vandermonde**

Đề bài: Một nhóm gồm $$m = 4$$ nam và $$n = 3$$ nữ (tổng $$7$$ người). Có bao nhiêu cách chọn ra một đội gồm $$r = 3$$ người?
- **Cách 1 (chọn trực tiếp từ cả 7 người)**:
  $$\binom{4 + 3}{3} = \binom{7}{3} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = \mathbf{35}\text{ cách}.$$
- **Cách 2 (chia trường hợp theo số bạn nữ $$k \in \{0, 1, 2, 3\}$$ trong đội)**:
  - $$k = 0$$ nữ, $$3$$ nam: $$\binom{4}{3}\binom{3}{0} = 4 \times 1 = 4$$.
  - $$k = 1$$ nữ, $$2$$ nam: $$\binom{4}{2}\binom{3}{1} = 6 \times 3 = 18$$.
  - $$k = 2$$ nữ, $$1$$ nam: $$\binom{4}{1}\binom{3}{2} = 4 \times 3 = 12$$.
  - $$k = 3$$ nữ, $$0$$ nam: $$\binom{4}{0}\binom{3}{3} = 1 \times 1 = 1$$.
  - Tổng cộng: $$4 + 18 + 12 + 1 = \mathbf{35}\text{ cách}$$.

Cả hai cách cùng đếm đúng một tập hợp nên luôn bằng nhau: $$\sum_{k=0}^{r} \binom{m}{r-k}\binom{n}{k} = \binom{m+n}{r}$$—không cần biến đổi một dòng đại số nào!

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
<p>Công cụ này tính $C(n,k)$, tô sáng vị trí tương ứng trong tam giác Pascal và hiển thị khai triển $(a+b)^n$.</p>
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

Vì số mũ của $y$ là $3$, hệ số cần tìm là:

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

Tổng tất cả $\binom{n}{k}$ với $k$ từ $0$ đến $n$ bằng $2^n$ (tổng số tập con của một tập $n$ phần tử). Hạng tử $k=0$ ứng với tập rỗng ($\binom{n}{0} = 1$). Bỏ tập rỗng đi, ta còn lại $2^n-1$ tập con khác rỗng.

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
Kết quả này trùng với cách chọn trực tiếp $\binom{9}{3}=84$.

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
