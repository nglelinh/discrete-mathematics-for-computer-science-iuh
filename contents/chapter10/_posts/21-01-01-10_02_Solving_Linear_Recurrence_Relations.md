---
layout: post
title: "Giải Quan hệ Truy hồi Tuyến tính"
categories: chapter10
date: 2021-01-01
order: 2
required: true
lang: vi
excerpt: "Giải quan hệ truy hồi tuyến tính thuần nhất hệ số hằng bằng phương trình đặc trưng: nghiệm phân biệt, nghiệm bội, nghiệm phức liên hợp, công thức De Moivre và dạng thực sin–cos."
---

Ở bài trước, chúng ta đã làm quen với định nghĩa và cách phân loại quan hệ truy hồi theo bậc, tính tuyến tính và tính thuần nhất. Bài học này tập trung vào lớp bài toán quan trọng bậc nhất: **quan hệ truy hồi tuyến tính thuần nhất có hệ số hằng**. Với lớp truy hồi này, thay vì phải tính lần lượt từng số hạng từ đầu, ta có thể tìm được công thức đóng tường minh cho $$a_n$$ hoặc đánh giá trực tiếp tốc độ tăng trưởng của dãy.

Trong khoa học máy tính, từ số lời gọi đệ quy, số cấu hình tổ hợp đến phân tích thuật toán chia để trị, rất nhiều bài toán đều quy về giải một quan hệ truy hồi tuyến tính. Công cụ chủ đạo ở đây là **phương trình đặc trưng**, dẫn đến ba trường hợp nghiệm: nghiệm thực phân biệt, nghiệm bội và nghiệm phức liên hợp. Để xử lý trọn vẹn trường hợp biệt thức âm, bài học cũng hệ thống lại ngắn gọn các kiến thức nền về **số phức**, **ba cách biểu diễn** và **định lý De Moivre**, giúp bạn chuyển đổi nghiệm phức sang dạng thực chứa $$\cos$$ và $$\sin$$ một cách chắc chắn.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Lập** phương trình đặc trưng cho quan hệ truy hồi tuyến tính thuần nhất hệ số hằng bậc $$k$$.
- **Giải** đầy đủ ba trường hợp nghiệm: nghiệm thực **phân biệt**, nghiệm **bội** và nghiệm **phức liên hợp**.
- **Biểu diễn** số phức dưới dạng đại số, hình học (mặt phẳng Argand) và dạng cực / mũ; vận dụng **định lý De Moivre** để tính lũy thừa $$z^n$$.
- **Chuyển đổi** cặp nghiệm phức $$r = \rho e^{\pm i\theta}$$ thành công thức thực $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$ và xác định $$A, B$$ từ điều kiện đầu.
- **Phân tích** hành vi dài hạn của dãy số dựa vào mô-đun $$\rho$$: tắt dần ($$\rho < 1$$), dao động ổn định / tuần hoàn ($$\rho = 1$$) hoặc tăng trưởng bùng nổ ($$\rho > 1$$).

**Từ khóa**: phương trình đặc trưng (characteristic equation), nghiệm phân biệt, nghiệm bội, nghiệm phức, số phức (complex number), mô-đun, argument, dạng cực, định lý De Moivre, công thức Binet.

</div>

## Dạng tổng quát

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ truy hồi tuyến tính thuần nhất hệ số hằng bậc $$k$$ có dạng tổng quát
</div>

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k},\quad c_k\ne0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Các đặc điểm nhận diện của lớp truy hồi này gồm:

- **Tuyến tính**: các số hạng $$a_{n-i}$$ chỉ xuất hiện ở bậc nhất, không có tích hay lũy thừa giữa chúng.
- **Thuần nhất**: không có thành phần tự do chỉ phụ thuộc vào $$n$$ (tức $$f(n) \equiv 0$$).
- **Hệ số hằng**: các hệ số $$c_1, c_2, \dots, c_k$$ là hằng số, không phụ thuộc vào $$n$$.
- **Điều kiện đầu**: cần đúng $$k$$ giá trị khởi tạo để xác định duy nhất một dãy số.

<div class="textbook-example" markdown="1">
**Ví dụ**: Dãy Fibonacci thỏa mãn $$F_n = F_{n-1} + F_{n-2}$$ với điều kiện đầu $$F_0 = 0, F_1 = 1$$. Đây là truy hồi tuyến tính thuần nhất hệ số hằng bậc 2.

![Dãy truy hồi tuyến tính hệ số hằng](/discrete-mathematics-for-computer-science-iuh/img/course/Constant-recursive-sequences.svg)

<p class="textbook-figure-caption" data-figure="10.6">Nghiệm tổng quát của quan hệ truy hồi tuyến tính thuần nhất bậc $$k$$ được xây dựng từ tổ hợp tuyến tính các hạng tử dạng $$r_i^n$$.</p>
</div>

## Ý tưởng nghiệm dạng $$r^n$$ và phương trình đặc trưng

Xét quan hệ truy hồi bậc hai:

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Ta thử tìm nghiệm có dạng hàm mũ $$a_n = r^n$$ với $$r \ne 0$$. Thay vào quan hệ trên, ta thu được:

<div class="textbook-equation" markdown="1">
$$
r^n=c_1r^{n-1}+c_2r^{n-2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Chia cả hai vế cho $$r^{n-2}$$ (do $$r \ne 0$$) rồi chuyển vế, ta có:

<div class="textbook-equation" markdown="1">
$$
r^2-c_1r-c_2=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Phương trình đại số này được gọi là **phương trình đặc trưng** (characteristic equation) của quan hệ truy hồi.

Vì quan hệ truy hồi có tính tuyến tính và thuần nhất, mọi tổ hợp tuyến tính của các nghiệm riêng biệt cũng đều là nghiệm. Cụ thể, ở bậc hai: nếu phương trình đặc trưng có hai nghiệm phân biệt $$r_1, r_2$$ thì nghiệm tổng quát có dạng $$a_n = \alpha r_1^n + \beta r_2^n$$; nếu có nghiệm kép $$r$$ thì nghiệm tổng quát có dạng $$a_n = (\alpha + \beta n)r^n$$.

![Giải bài toán đệ quy — phương trình đặc trưng](/discrete-mathematics-for-computer-science-iuh/img/course/Recursive_problem_solving.svg)

<p class="textbook-figure-caption" data-figure="10.7">Phương trình đặc trưng $$r^k - c_1 r^{k-1} - \cdots - c_k = 0$$ quyết định hoàn toàn cấu trúc nghiệm của truy hồi tuyến tính thuần nhất.</p>

<div class="content-box insight-box textbook-block" markdown="1">
**Trực giác**: Khi một dãy số tăng trưởng theo quy luật nhân lặp lại, tỷ số giữa hai số hạng liên tiếp $$a_n / a_{n-1}$$ thường tiến dần về một hằng số $$r$$. Chính vì vậy, dạng hàm mũ $$a_n = r^n$$ là ứng viên tự nhiên nhất cho các hệ tuyến tính có hệ số hằng.
</div>

## Trường hợp 1: Nghiệm thực phân biệt

Nếu phương trình đặc trưng bậc hai có hai nghiệm thực phân biệt $$r_1 \neq r_2$$, thì nghiệm tổng quát của quan hệ truy hồi là:

<div class="textbook-equation" markdown="1">
$$
a_n=\alpha r_1^n+\beta r_2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Hai hằng số $$\alpha, \beta$$ được xác định duy nhất bằng cách giải hệ phương trình sinh ra từ hai điều kiện đầu.

<div class="textbook-example" markdown="1">
**Ví dụ**: Giải quan hệ truy hồi $$a_n = 5a_{n-1} - 6a_{n-2}$$ với $$a_0 = 2$$ và $$a_1 = 5$$.

Phương trình đặc trưng:

<div class="textbook-equation" markdown="1">
$$
r^2-5r+6=(r-2)(r-3)=0 \implies r_1 = 2,\; r_2 = 3.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nghiệm tổng quát có dạng:

<div class="textbook-equation" markdown="1">
$$
a_n=\alpha \cdot 2^n+\beta \cdot 3^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Thay các điều kiện đầu vào biểu thức:

- Với $$n = 0$$: $$\alpha + \beta = 2$$.
- Với $$n = 1$$: $$2\alpha + 3\beta = 5$$.

Giải hệ phương trình trên, ta được $$\alpha = 1$$ và $$\beta = 1$$. Do đó công thức đóng là:

<div class="textbook-equation" markdown="1">
$$
a_n=2^n+3^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

### Video ngắn: Fibonacci và tỷ lệ vàng

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/fibonacci-golden-ratio.mp4"></video>
</div>

Dãy Fibonacci $$F_{n+1} = F_n + F_{n-1}$$ có phương trình đặc trưng $$r^2 - r - 1 = 0$$ với hai nghiệm thực phân biệt là $$\varphi = \frac{1+\sqrt{5}}{2}$$ và $$\psi = \frac{1-\sqrt{5}}{2}$$. Vì $$\lvert \psi \rvert < 1$$ nên khi $$n$$ đủ lớn, thành phần $$\psi^n$$ tiến nhanh về $$0$$, kéo theo tỷ số $$F_{n+1}/F_n \to \varphi \approx 1{,}618$$ — chính là tỷ lệ vàng như minh họa trong video.

## Trường hợp 2: Nghiệm bội

Nếu phương trình đặc trưng bậc hai có nghiệm kép $$r$$, ta không thể chỉ lấy hai hạng tử $$r^n$$ vì chúng phụ thuộc tuyến tính với nhau. Khi đó, nghiệm tổng quát có dạng:

<div class="textbook-equation" markdown="1">
$$
a_n=(\alpha+\beta n)r^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tổng quát hơn, với truy hồi bậc $$k$$, nếu $$r$$ là nghiệm bội $$m$$ của phương trình đặc trưng thì nó đóng góp $$m$$ thành phần độc lập tuyến tính vào nghiệm tổng quát:

<div class="textbook-equation" markdown="1">
$$
r^n,\; nr^n,\; n^2r^n,\ldots,n^{m-1}r^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 1**: Tìm nghiệm tổng quát của $$a_n = 4a_{n-1} - 4a_{n-2}$$.

Phương trình đặc trưng là:

<div class="textbook-equation" markdown="1">
$$
r^2-4r+4=(r-2)^2=0,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

có nghiệm kép $$r = 2$$. Suy ra nghiệm tổng quát là:

<div class="textbook-equation" markdown="1">
$$
a_n=(\alpha+\beta n)2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2 (nghiệm kép $$r = 1$$ — dãy số lẻ):**  
Giải $$X_n = 2X_{n-1} - X_{n-2}$$ với $$X_0 = 1$$ và $$X_1 = 3$$.

Thay $$X_n = r^n$$, ta được phương trình đặc trưng $$r^2 - 2r + 1 = (r - 1)^2 = 0$$, có nghiệm kép $$r = 1$$.

Lưu ý rằng ta **không thể** viết $$X_n = A \cdot 1^n + B \cdot 1^n = A + B$$ vì biểu thức này chỉ là một hằng số, mâu thuẫn với điều kiện đầu $$X_0 = 1 \neq X_1 = 3$$. Dạng nghiệm tổng quát đúng phải là:

$$X_n = (A_1 + A_2 n) \cdot 1^n = A_1 + A_2 n.$$

Thay điều kiện đầu:
- Với $$n = 0$$: $$A_1 = 1$$.
- Với $$n = 1$$: $$1 + A_2 = 3 \Rightarrow A_2 = 2$$.

Vậy $$X_n = 1 + 2n$$. Kiểm tra vài số hạng đầu ta được $$1, 3, 5, 7, 9, \dots$$, hoàn toàn khớp với hệ thức $$2 \cdot 3 - 1 = 5$$ và $$2 \cdot 5 - 3 = 7$$.

</div>

## Trường hợp 3: Nghiệm phức và kiến thức nền về số phức

Xét quan hệ truy hồi bậc hai có hệ số thực:

<div class="textbook-equation" markdown="1">
$$
a_n = c_1 a_{n-1} + c_2 a_{n-2},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

với phương trình đặc trưng $$r^2 - c_1 r - c_2 = 0$$. Biệt thức:

<div class="textbook-equation" markdown="1">
$$
\Delta = c_1^2 + 4c_2
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

quyết định bản chất nghiệm: $$\Delta > 0$$ cho hai nghiệm thực phân biệt, $$\Delta = 0$$ cho nghiệm kép, và $$\Delta < 0$$ cho **hai nghiệm phức liên hợp**. Khi $$\Delta < 0$$, nghiệm không nằm trên trục số thực; để tính $$r^n$$ và đưa công thức của dãy $$a_n$$ về dạng **thực**, ta cần ôn nhanh về số phức và các cách biểu diễn của chúng.

<div class="content-box insight-box textbook-block" markdown="1">
**Lưu ý quan trọng**: Trong các bài toán thực tế, dãy $$a_n$$ thường là dãy **số thực** (chẳng hạn số bước tính toán hay biên độ tín hiệu). Dù phương trình đặc trưng có nghiệm phức, công thức đóng cuối cùng vẫn cần được viết lại bằng $$\rho^n$$, $$\cos$$ và $$\sin$$ với hệ số thực — tuyệt đối không được tùy tiện "bỏ qua" phần ảo.
</div>

### Định nghĩa số phức

<div class="textbook-definition" markdown="1">

**Định nghĩa**: Một **số phức** (complex number) $$z \in \mathbb{C}$$ ở **dạng đại số** được viết là:

$$
z = a + bi,\qquad a,b \in \mathbb{R},\quad i^2 = -1.
$$

Trong đó:
- $$a = \operatorname{Re}(z)$$ là **phần thực** (real part).
- $$b = \operatorname{Im}(z)$$ là **phần ảo** (imaginary part).
- $$i$$ là **đơn vị ảo** (imaginary unit).

Hai số phức bằng nhau khi và chỉ khi phần thực và phần ảo của chúng lần lượt bằng nhau:

$$
a + bi = c + di \iff (a = c \;\text{và}\; b = d).
$$

</div>

Hai trường hợp đặc biệt cần nhớ:

- Khi $$b = 0$$: $$z$$ là số **thực** (nên $$\mathbb{R} \subset \mathbb{C}$$).
- Khi $$a = 0$$ và $$b \neq 0$$: $$z$$ là số **thuần ảo** (pure imaginary).

<div class="textbook-example" markdown="1">

**Ví dụ**: Xác định phần thực và phần ảo của các số phức sau:

| $$z$$ | $$\operatorname{Re}(z)$$ | $$\operatorname{Im}(z)$$ |
|:---|:---:|:---:|
| $$3 + 2i$$ | 3 | 2 |
| $$-1$$ | $$-1$$ | 0 |
| $$i$$ | 0 | 1 |
| $$1 - i$$ | 1 | $$-1$$ |

</div>

### Số phức liên hợp

<div class="textbook-definition" markdown="1">

**Định nghĩa**: **Số phức liên hợp** (complex conjugate) của $$z = a + bi$$ là:

$$
\overline{z} = a - bi.
$$

</div>

Một số tính chất thường dùng (có thể kiểm chứng trực tiếp từ định nghĩa):

- $$z + \overline{z} = 2a$$ (luôn là số thực).
- $$z - \overline{z} = 2bi$$ (luôn là số thuần ảo).
- $$z \cdot \overline{z} = a^2 + b^2$$ (luôn là số thực không âm).
- $$\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$$ và $$\overline{z_1 z_2} = \overline{z_1}\,\overline{z_2}$$.
- $$\overline{\overline{z}} = z$$.

**Ý nghĩa đối với quan hệ truy hồi**: Khi đa thức đặc trưng có hệ số thực, nếu $$r$$ là một nghiệm phức thì liên hợp $$\overline{r}$$ chắc chắn cũng là nghiệm. Vì nghiệm phức luôn đi theo cặp liên hợp, mỗi cặp sẽ ứng với đúng hai hằng số thực tự do $$A, B$$ trong công thức dạng $$\cos$$–$$\sin$$.

### Ba cách biểu diễn số phức

| Dạng biểu diễn | Công thức | Ứng dụng thuận tiện nhất |
|:---|:---|:---|
| **Đại số** | $$z = a + bi$$ | Cộng, trừ, so sánh và lấy liên hợp |
| **Hình học (Argand)** | Điểm $$(a,b)$$ hoặc vector $$\overrightarrow{Oz}$$ | Hình dung trực quan về khoảng cách và góc quay |
| **Cực / mũ** | $$z = \rho(\cos\theta + i\sin\theta) = \rho e^{i\theta}$$ | **Nhân**, **chia** và tính **lũy thừa** $$z^n$$ |

### Các phép toán cơ bản ở dạng đại số

Với $$z_1 = a + bi$$ và $$z_2 = c + di$$:

- **Cộng và trừ** (thực hiện theo từng thành phần):

<div class="textbook-equation" markdown="1">
$$
z_1 \pm z_2 = (a \pm c) + (b \pm d)i.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

- **Nhân** (khai triển phân phối và thay $$i^2 = -1$$):

<div class="textbook-equation" markdown="1">
$$
z_1 z_2 = (ac - bd) + (ad + bc)i.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

- **Chia** (nhân cả tử và mẫu với liên hợp của mẫu số, với $$z_2 \neq 0$$):

<div class="textbook-equation" markdown="1">
$$
\frac{z_1}{z_2} = \frac{z_1 \overline{z_2}}{\lvert z_2 \rvert^2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

### Biểu diễn hình học trên mặt phẳng phức

Mỗi số phức $$z = a + bi$$ tương ứng duy nhất với điểm $$(a, b)$$ trên **mặt phẳng phức** (còn gọi là mặt phẳng Argand):

- Trục hoành **Re** biểu diễn phần thực.
- Trục tung **Im** biểu diễn phần ảo.
- Gốc tọa độ $$O$$ tương ứng với số $$0$$.
- Vector $$\overrightarrow{Oz}$$ biểu diễn vị trí của số phức $$z$$.

![Mặt phẳng phức — dạng đại số](/discrete-mathematics-for-computer-science-iuh/img/course/Complex_plane_algebraic.svg)

<p class="textbook-figure-caption" data-figure="10.8a">Số phức $$z = a + bi$$ tương ứng với điểm $$(a,b)$$ trên mặt phẳng Argand (minh họa với $$z = 3 + 2i$$).</p>

### Mô-đun và argument

<div class="textbook-definition" markdown="1">

**Định nghĩa**: Cho số phức $$z = a + bi$$.

- **Mô-đun** (modulus / độ lớn):
$$
\lvert z \rvert = \rho = \sqrt{a^2 + b^2}
$$
chính là khoảng cách từ gốc tọa độ $$O$$ đến điểm $$(a,b)$$.

- **Argument** (góc cực): $$\theta = \operatorname{arg}(z)$$ là góc định hướng tính từ chiều dương trục thực Re đến vector $$\overrightarrow{Oz}$$ (thường chuẩn hóa trong nửa khoảng $$(-\pi, \pi]$$).

Khi $$a > 0$$, ta tính trực tiếp $$\theta = \arctan\left(\frac{b}{a}\right)$$. Khi $$a < 0$$, do hàm $$\arctan$$ chỉ nhận giá trị trong $$(-\pi/2, \pi/2)$$, cần cộng thêm $$\pi$$ (nếu $$b \ge 0$$) hoặc trừ đi $$\pi$$ (nếu $$b < 0$$) để đưa góc về đúng góc phần tư.

</div>

Các tính chất quan trọng của mô-đun:

- $$\lvert z \rvert \ge 0$$, và $$\lvert z \rvert = 0 \iff z = 0$$.
- $$\lvert \overline{z} \rvert = \lvert z \rvert$$.
- $$\lvert z_1 z_2 \rvert = \lvert z_1 \rvert\,\lvert z_2 \rvert$$ và $$\lvert z^n \rvert = \lvert z \rvert^n$$.
- Bất đẳng thức tam giác: $$\lvert z_1 + z_2 \rvert \le \lvert z_1 \rvert + \lvert z_2 \rvert$$.

<div class="content-box insight-box textbook-block" markdown="1">
**Liên hệ với hệ thức truy hồi**: Mô-đun $$\rho = \lvert r \rvert$$ của nghiệm đặc trưng quyết định trực tiếp dáng điệu của dãy khi $$n \to \infty$$ — tắt dần về 0 nếu $$\rho < 1$$, giữ biên độ ổn định nếu $$\rho = 1$$, và phình to ra vô hạn nếu $$\rho > 1$$. Đây cũng là nền tảng để phân tích tính ổn định của hệ tuyến tính rời rạc và bộ lọc tín hiệu số.
</div>

### Dạng cực và dạng mũ

<div class="textbook-definition" markdown="1">

**Định nghĩa**: Với $$\rho = \lvert z \rvert$$ và $$\theta = \operatorname{arg}(z)$$:

- **Dạng cực** (polar form):
$$
z = \rho\bigl(\cos\theta + i\sin\theta\bigr).
$$

- **Dạng mũ** (exponential form, theo công thức Euler $$e^{i\theta} = \cos\theta + i\sin\theta$$):
$$
z = \rho e^{i\theta}.
$$

</div>

Bảng chuyển đổi giữa dạng đại số và dạng cực:

| Chiều chuyển đổi | Công thức |
|:---|:---|
| Đại số $$\to$$ cực | $$\rho = \sqrt{a^2 + b^2}$$, $$\theta = \arctan\left(\frac{b}{a}\right)$$ (với $$a > 0$$) |
| Cực $$\to$$ đại số | $$a = \rho\cos\theta$$, $$b = \rho\sin\theta$$ |

Ở dạng cực và dạng mũ, số phức liên hợp giữ nguyên mô-đun và chỉ đổi dấu góc: $$\overline{z} = \rho(\cos\theta - i\sin\theta) = \rho e^{-i\theta}$$.

![Dạng cực của số phức](/discrete-mathematics-for-computer-science-iuh/img/course/Complex_plane_polar.svg)

<p class="textbook-figure-caption" data-figure="10.8b">Biểu diễn cực gồm bán kính $$\rho = \lvert z \rvert$$ và góc $$\theta = \operatorname{arg}(z)$$, liên hệ với tọa độ đại số qua $$(a,b) = (\rho\cos\theta,\ \rho\sin\theta)$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1**: Viết số phức $$z = 1 + i$$ dưới dạng cực và dạng mũ.

1. Mô-đun: $$\rho = \sqrt{1^2 + 1^2} = \sqrt{2}$$.
2. Argument (vì $$a = 1 > 0$$): $$\theta = \arctan\left(\frac{1}{1}\right) = \frac{\pi}{4}$$.
3. Dạng cực: $$z = \sqrt{2}\bigl(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\bigr)$$.
4. Dạng mũ: $$z = \sqrt{2}\,e^{i\pi/4}$$.

Kiểm tra ngược: $$\sqrt{2}\cdot\frac{\sqrt{2}}{2} + i\sqrt{2}\cdot\frac{\sqrt{2}}{2} = 1 + i$$ ✓.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2**: Một số điểm đặc biệt trên đường tròn đơn vị ($$\rho = 1$$):

| $$z$$ | $$\rho$$ | $$\theta$$ | Dạng cực |
|:---|:---:|:---:|:---|
| $$-1$$ | 1 | $$\pi$$ | $$\cos\pi + i\sin\pi$$ |
| $$i$$ | 1 | $$\pi/2$$ | $$\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}$$ |
| $$-i$$ | 1 | $$-\pi/2$$ | $$\cos\bigl(-\frac{\pi}{2}\bigr) + i\sin\bigl(-\frac{\pi}{2}\bigr)$$ |

</div>

### Định lý De Moivre

<div class="textbook-theorem" markdown="1">

**Định lý (De Moivre)**: Nếu $$z = \rho(\cos\theta + i\sin\theta)$$ thì với mọi số nguyên $$n$$, ta có:

$$
z^n = \rho^n\bigl(\cos n\theta + i\sin n\theta\bigr).
$$

Viết theo dạng mũ, đẳng thức này trở nên rất gọn: $$(\rho e^{i\theta})^n = \rho^n e^{in\theta}$$.

</div>

**Ý nghĩa hình học**: Khi nâng số phức $$z$$ lên lũy thừa bậc $$n$$, ta chỉ cần **nâng mô-đun lên lũy thừa $$n$$** và **nhân góc cực lên $$n$$ lần**.

![De Moivre — lũy thừa trên mặt phẳng phức](/discrete-mathematics-for-computer-science-iuh/img/course/Complex_de_moivre.svg)

<p class="textbook-figure-caption" data-figure="10.8c">Theo định lý De Moivre, phép tính $$z^n$$ xoay vector tới góc tổng $$n\theta$$ và thay đổi độ dài thành $$\rho^n$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ**: Tính $$(1+i)^4$$ bằng định lý De Moivre.

Vì $$1 + i = \sqrt{2}\,e^{i\pi/4}$$, áp dụng công thức De Moivre ta được:

$$
(1+i)^4 = (\sqrt{2})^4 e^{i\pi} = 4(\cos\pi + i\sin\pi) = 4(-1) = -4.
$$

</div>

### Từ nghiệm phức đến dạng thực sin–cos

Phần này giải đáp trọn vẹn hai câu hỏi mấu chốt khi gặp nghiệm phức:

1. Xuất phát từ công thức tổng quát $$a_n = C r^n + D\,\overline{r}^{n}$$ (với $$C, D \in \mathbb{C}$$), vì sao điều kiện dãy $$a_n$$ nhận giá trị thực lại **bắt buộc** $$D = \overline{C}$$?
2. Từ hệ thức $$D = \overline{C}$$, làm thế nào ta rút gọn được thành $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$ mà hoàn toàn không còn đơn vị ảo $$i$$?

#### Tóm lược ý tưởng

1. Nghiệm phức của đa thức đặc trưng hệ số thực luôn xuất hiện theo **cặp liên hợp** $$r$$ và $$\overline{r}$$.
2. Từ giả thiết $$a_n$$ là số thực với mọi $$n$$, ta **chứng minh** được $$D = \overline{C}$$ (chứ không phải giả định tùy ý).
3. Áp dụng định lý De Moivre để viết $$r^n$$ và $$\overline{r}^{n}$$ qua $$\cos n\theta$$ và $$\sin n\theta$$.
4. Khi cộng hai số phức liên hợp, phần ảo tự động triệt tiêu, chỉ còn tổ hợp thực của $$\cos n\theta$$ và $$\sin n\theta$$.
5. Khi làm bài tập, bạn không cần tìm $$C$$ — chỉ cần viết thẳng dạng thực rồi giải hệ tìm $$A, B$$ từ điều kiện đầu.

#### Bước 0: Xuất phát điểm

Với phương trình đặc trưng bậc hai hệ số thực có $$\Delta < 0$$, hai nghiệm phức liên hợp có dạng:

$$
r = \alpha + i\beta,\qquad \overline{r} = \alpha - i\beta \quad (\beta \neq 0).
$$

Chuyển sang dạng cực với $$\rho = \lvert r \rvert$$ và $$\theta = \operatorname{arg}(r)$$:

$$
r = \rho\bigl(\cos\theta + i\sin\theta\bigr),\qquad \overline{r} = \rho\bigl(\cos\theta - i\sin\theta\bigr).
$$

Áp dụng định lý De Moivre cho cả hai nghiệm:

$$
r^n = \rho^n\bigl(\cos n\theta + i\sin n\theta\bigr),
$$

$$
\overline{r}^{n} = \rho^n\bigl(\cos n\theta - i\sin n\theta\bigr).
$$

Hai biểu thức này chỉ khác nhau ở dấu của thành phần $$i\sin n\theta$$, tức là chúng tiếp tục tạo thành một cặp liên hợp.

#### Bước 1: Viết dạng nghiệm tổng quát trên trường số phức

Vì $$r \neq \overline{r}$$, nghiệm tổng quát có dạng tổ hợp tuyến tính với hai hằng số phức $$C, D \in \mathbb{C}$$:

$$
a_n = C\, r^n + D\, \overline{r}^{n}.
$$

Cấu trúc đại số ở đây hoàn toàn tương tự công thức $$\alpha r_1^n + \beta r_2^n$$ ở trường hợp nghiệm thực phân biệt.

#### Bước 2: Chứng minh $$a_n$$ thực kéo theo $$D = \overline{C}$$

Ở Bước 1, $$C$$ và $$D$$ vẫn là hai hằng số phức bất kỳ. Để thấy $$D = \overline{C}$$ là **hệ quả tất yếu** của việc dãy $$a_n$$ thực, ta lập luận như sau:

Vì hệ số truy hồi và điều kiện đầu đều là số thực nên mọi số hạng $$a_n$$ đều là số thực. Một số phức là số thực khi và chỉ khi nó bằng liên hợp của chính nó, tức là với mọi $$n$$:

$$
a_n = \overline{a_n}.
$$

Lấy liên hợp hai vế của biểu thức $$a_n = C r^n + D\,\overline{r}^{n}$$ (sử dụng $$\overline{zw} = \overline{z}\,\overline{w}$$ và $$\overline{\overline{r}} = r$$):

{% raw %}
$$
\begin{aligned}
\overline{a_n}
&= \overline{C\, r^n + D\, \overline{r}^{n}} \\
&= \overline{C}\, \overline{r}^{n} + \overline{D}\, r^{n}.
\end{aligned}
$$
{% endraw %}

*(Lưu ý rằng $$\overline{r^{n}} = \overline{r}^{n}$$ và $$\overline{\overline{r}^{n}} = r^{n}$$.)*

Cho hai biểu thức của $$a_n$$ và $$\overline{a_n}$$ bằng nhau:

<div class="textbook-equation" markdown="1">
$$
C\, r^n + D\, \overline{r}^{n}
=
\overline{D}\, r^n + \overline{C}\, \overline{r}^{n}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Chuyển tất cả sang một vế:

$$
\bigl(C - \overline{D}\bigr)\, r^n
+
\bigl(D - \overline{C}\bigr)\, \overline{r}^{n}
= 0
\quad\text{với mọi } n.
$$

Do $$r \neq \overline{r}$$ (vì $$\beta \neq 0$$), hai dãy hàm $$n \mapsto r^n$$ và $$n \mapsto \overline{r}^{n}$$ **độc lập tuyến tính** trên $$\mathbb{C}$$. Vì vậy, tổ hợp tuyến tính của chúng đồng nhất bằng 0 khi và chỉ khi cả hai hệ số đều bằng 0:

$$
C - \overline{D} = 0,\qquad D - \overline{C} = 0.
$$

Hai phương trình này tương đương với nhau và đều dẫn đến kết luận bắt buộc:

<div class="textbook-equation" markdown="1">
$$
D = \overline{C}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả**: Nghiệm tổng quát của dãy số thực phải có dạng
</div>

$$
a_n = C\, r^n + \overline{C}\, \overline{r}^{n}.
$$

**Chiều ngược lại (điều kiện đủ)**: Nếu đặt $$w = C r^n$$ thì $$a_n = w + \overline{w} = 2\operatorname{Re}(w) \in \mathbb{R}$$. Như vậy $$D = \overline{C}$$ là điều kiện cần và đủ để dãy $$a_n$$ hoàn toàn thực.

<div class="content-box insight-box textbook-block" markdown="1">
**Tóm lược Bước 2**:  
- Chiều thuận: $$a_n \in \mathbb{R} \Rightarrow a_n = \overline{a_n} \Rightarrow$$ đồng nhất hệ số của hai dãy độc lập tuyến tính $$r^n$$ và $$\overline{r}^{n} \Rightarrow D = \overline{C}$$.  
- Chiều đảo: $$D = \overline{C} \Rightarrow a_n = w + \overline{w} = 2\operatorname{Re}(w) \in \mathbb{R}$$.
</div>

#### Bước 3: Minh họa bằng ví dụ số cụ thể

Xét $$r = i$$ (nghiệm đặc trưng của $$a_n = -a_{n-2}$$). Khi đó $$\rho = 1$$, $$\theta = \pi/2$$ và:

$$
i^n = \cos\frac{n\pi}{2} + i\sin\frac{n\pi}{2},\qquad
(-i)^n = \cos\frac{n\pi}{2} - i\sin\frac{n\pi}{2}.
$$

Chọn thử $$C = \dfrac{1}{2}$$ (khi đó $$\overline{C} = \dfrac{1}{2}$$):

$$
a_n
= \frac{1}{2}\, i^n + \frac{1}{2}\, (-i)^n
= \frac{1}{2}\Bigl(
  \cos\frac{n\pi}{2} + i\sin\frac{n\pi}{2}
  + \cos\frac{n\pi}{2} - i\sin\frac{n\pi}{2}
\Bigr).
$$

Hai số hạng $$+i\sin\frac{n\pi}{2}$$ và $$-i\sin\frac{n\pi}{2}$$ triệt tiêu nhau, chỉ còn lại:

$$
a_n = \cos\frac{n\pi}{2} = 1^n\Bigl(1\cdot\cos\frac{n\pi}{2} + 0\cdot\sin\frac{n\pi}{2}\Bigr).
$$

Công thức cuối cùng không còn chứa $$i$$, và tạo ra dãy số thực $$1, 0, -1, 0, 1, \dots$$ ứng với $$n = 0, 1, 2, 3, 4, \dots$$

#### Bước 4: Biến đổi trong trường hợp tổng quát

Viết hằng số phức $$C$$ dưới dạng đại số $$C = p + qi$$ với $$p, q \in \mathbb{R}$$, suy ra $$\overline{C} = p - qi$$. Thay vào biểu thức $$a_n = C r^n + \overline{C}\,\overline{r}^{n}$$ và đặt $$\rho^n$$ làm nhân tử chung:

$$
a_n = \rho^n \cdot \Bigl[
  (p+qi)\,(\cos n\theta + i\sin n\theta)
  +
  (p-qi)\,(\cos n\theta - i\sin n\theta)
\Bigr].
$$

Khai triển từng tích (lưu ý $$i^2 = -1$$):

$$
(p+qi)(\cos n\theta + i\sin n\theta)
=
\bigl(p\cos n\theta - q\sin n\theta\bigr)
+
i\bigl(p\sin n\theta + q\cos n\theta\bigr),
$$

$$
(p-qi)(\cos n\theta - i\sin n\theta)
=
\bigl(p\cos n\theta - q\sin n\theta\bigr)
-
i\bigl(p\sin n\theta + q\cos n\theta\bigr).
$$

Khi cộng hai biểu thức này, hai phần ảo đối dấu nhau triệt tiêu hoàn toàn, còn phần thực được nhân đôi:

$$
a_n = \rho^n \cdot 2\bigl(p\cos n\theta - q\sin n\theta\bigr)
= \rho^n\bigl(A\cos n\theta + B\sin n\theta\bigr),
$$

trong đó ta đặt $$A = 2p$$ và $$B = -2q$$. Vì $$p, q$$ là hai số thực tùy ý nên $$A, B$$ cũng là hai hằng số thực tùy ý mà không làm mất tính tổng quát.

<div class="textbook-equation" markdown="1">
$$
a_n = \rho^n\bigl(A\cos n\theta + B\sin n\theta\bigr),\qquad A,B \in \mathbb{R}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

#### Bước 5: Bảng đối chiếu giữa dạng phức và dạng thực

| Thành phần ở dạng phức | Thành phần tương ứng ở dạng thực |
|:---|:---|
| Cặp nghiệm liên hợp $$r,\ \overline{r}$$ | Mô-đun $$\rho$$ và góc cực $$\theta$$ |
| Hằng số phức $$C = p + qi$$ | Hai hằng số thực $$A, B$$ |
| $$C r^n + \overline{C}\,\overline{r}^{n}$$ | $$\rho^n(A\cos n\theta + B\sin n\theta)$$ |
| Phần ảo | Tự triệt tiêu khi cộng hai số liên hợp |
| Điều kiện đầu $$a_0, a_1$$ | Hệ hai phương trình tuyến tính xác định $$A, B$$ |

#### Bước 6: Quy trình thực hành khi giải bài tập

Khi giải bài tập thực tế, bạn **không cần** đi qua các hằng số trung gian $$C, p, q$$. Hãy thực hiện trực tiếp theo 5 bước:

1. Lập phương trình đặc trưng và giải tìm cặp nghiệm phức $$r = \alpha \pm i\beta$$.
2. Tính mô-đun $$\rho = \sqrt{\alpha^2 + \beta^2}$$ và argument $$\theta = \operatorname{arg}(r)$$.
3. Viết ngay dạng nghiệm thực:
   $$
   a_n = \rho^n\bigl(A\cos n\theta + B\sin n\theta\bigr).
   $$
4. Thay điều kiện đầu (thường là $$n = 0$$ và $$n = 1$$) để giải tìm $$A$$ và $$B$$.
5. Kiểm tra lại một số hạng kế tiếp (như $$a_2$$) bằng quan hệ truy hồi gốc.

Như vậy, số phức chỉ xuất hiện ở hai bước đầu để xác định $$\rho$$ và $$\theta$$; từ bước 3 trở đi, toàn bộ phép tính đều diễn ra trên tập số thực.

<div class="content-box insight-box textbook-block" markdown="1">
**Ghi nhớ nhanh**: Biểu thức $$C r^n + \overline{C}\,\overline{r}^{n}$$ là tổng của hai số phức liên hợp nên kết quả luôn thực. Nhờ định lý De Moivre, phần thực đó luôn viết gọn thành $$\rho^n(A\cos n\theta + B\sin n\theta)$$.
</div>

<div class="textbook-theorem" markdown="1">

**Tóm tắt quy trình giải truy hồi bậc hai có nghiệm phức**

1. Lập phương trình đặc trưng và kiểm tra $$\Delta < 0$$.
2. Tìm nghiệm $$r = \alpha \pm i\beta$$, từ đó suy ra $$\rho$$ và $$\theta$$.
3. Viết trực tiếp công thức $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$.
4. Sử dụng điều kiện đầu $$a_0, a_1$$ để tìm $$A, B$$.
5. Đối chiếu kết quả bằng cách thử lại với quan hệ truy hồi ban đầu.

</div>

### Các ví dụ giải hệ thức truy hồi có nghiệm phức

<div class="textbook-example" markdown="1">

**Ví dụ 0 (nghiệm $$r = 2 \pm i$$):**  
Giải $$X_n = 4X_{n-1} - 5X_{n-2}$$ với $$X_0 = 1$$ và $$X_1 = 2$$.

- **Phương trình đặc trưng**: $$r^2 - 4r + 5 = 0 \implies r = 2 \pm i$$.
- **Mô-đun và góc cực**: $$\rho = \sqrt{2^2 + 1^2} = \sqrt{5}$$ và $$\theta = \arctan(1/2)$$ (vì phần thực $$a = 2 > 0$$).
- **Dạng nghiệm thực**: $$X_n = (\sqrt{5})^n\bigl(A\cos n\theta + B\sin n\theta\bigr)$$.
- **Xác định $$A, B$$**:
  - Với $$n = 0$$: $$A = 1$$.
  - Với $$n = 1$$: vì $$\cos\theta = \frac{2}{\sqrt{5}}$$ và $$\sin\theta = \frac{1}{\sqrt{5}}$$, ta có:
    $$\sqrt{5}\left(\frac{2}{\sqrt{5}} + B\cdot\frac{1}{\sqrt{5}}\right) = 2 \implies 2 + B = 2 \implies B = 0.$$

Vậy công thức đóng là $$X_n = (\sqrt{5})^n \cos\bigl(n\arctan\tfrac{1}{2}\bigr)$$. *(Ghi chú: Nếu đổi điều kiện đầu thành $$X_1 = 1$$ thì sẽ thu được $$B = -1$$.)*

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1 (tuần hoàn chu kỳ 4, $$\rho = 1$$):**  
Giải $$a_n = -a_{n-2}$$ với $$a_0 = 1$$ và $$a_1 = 0$$.

Phương trình đặc trưng $$r^2 + 1 = 0$$ cho hai nghiệm $$r = \pm i$$, tương ứng với $$\rho = 1$$ và $$\theta = \pi/2$$.

Nghiệm tổng quát dạng thực:

$$
a_n = A\cos\frac{n\pi}{2} + B\sin\frac{n\pi}{2}.
$$

Thay $$a_0 = 1 \Rightarrow A = 1$$ và $$a_1 = 0 \Rightarrow B = 0$$. Do đó:

$$
a_n = \cos\frac{n\pi}{2}.
$$

Các số hạng đầu là $$1, 0, -1, 0, 1, 0, \dots$$ — tạo thành dãy tuần hoàn với **chu kỳ 4**, khớp hoàn toàn với quan hệ truy hồi ban đầu.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2 (dao động có biên độ tăng dần, $$\rho > 1$$):**  
Giải $$a_n = 2a_{n-1} - 2a_{n-2}$$ với $$a_0 = 1$$ và $$a_1 = 2$$.

Phương trình đặc trưng $$r^2 - 2r + 2 = 0$$ có $$\Delta = 4 - 8 = -4$$, suy ra $$r = 1 \pm i$$. Do đó $$\rho = \sqrt{2}$$ và $$\theta = \pi/4$$.

Nghiệm tổng quát:

$$
a_n = (\sqrt{2})^n\Bigl(A\cos\frac{n\pi}{4} + B\sin\frac{n\pi}{4}\Bigr).
$$

Từ $$a_0 = 1$$ ta có $$A = 1$$. Thay $$a_1 = 2$$:

$$
\sqrt{2}\Bigl(A\cos\frac{\pi}{4} + B\sin\frac{\pi}{4}\Bigr) = 2
\implies A + B = 2 \implies B = 1.
$$

Vậy:

$$
a_n = (\sqrt{2})^n\Bigl(\cos\frac{n\pi}{4} + \sin\frac{n\pi}{4}\Bigr).
$$

Kiểm tra với $$n = 2$$: truy hồi cho $$a_2 = 2\cdot 2 - 2\cdot 1 = 2$$, còn công thức cho $$(\sqrt{2})^2(0 + 1) = 2$$ ✓.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 3 (tuần hoàn chu kỳ 3 — căn bậc ba của đơn vị):**  
Giải $$a_n = -a_{n-1} - a_{n-2}$$ với $$a_0 = 2$$ và $$a_1 = -1$$.

Phương trình đặc trưng $$r^2 + r + 1 = 0$$ có $$\Delta = -3$$, cho hai nghiệm:

$$
r = \frac{-1 \pm i\sqrt{3}}{2}.
$$

Đây chính là hai căn bậc ba phức của đơn vị, có $$\rho = 1$$ và $$\theta = 2\pi/3$$. Suy ra:

$$
a_n = A\cos\frac{2n\pi}{3} + B\sin\frac{2n\pi}{3}.
$$

Từ $$a_0 = 2 \Rightarrow A = 2$$; thay $$a_1 = -1$$ ta giải được $$B = 0$$. Vậy:

$$
a_n = 2\cos\frac{2n\pi}{3}.
$$

Dãy thu được là $$2, -1, -1, 2, -1, -1, \dots$$ — tuần hoàn với **chu kỳ 3**.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4 (dao động tắt dần, $$\rho < 1$$):**  
Giải $$a_n = a_{n-1} - \frac{1}{2} a_{n-2}$$ với $$a_0 = 1$$ và $$a_1 = 0$$.

Phương trình đặc trưng $$r^2 - r + \frac{1}{2} = 0$$ có $$\Delta = -1$$, cho nghiệm $$r = \frac{1}{2} \pm i\frac{1}{2}$$. Suy ra $$\rho = \frac{\sqrt{2}}{2} < 1$$ và $$\theta = \pi/4$$.

Nghiệm tổng quát:

$$
a_n = \Bigl(\frac{\sqrt{2}}{2}\Bigr)^n\Bigl(A\cos\frac{n\pi}{4} + B\sin\frac{n\pi}{4}\Bigr).
$$

Áp dụng điều kiện đầu ta tìm được $$A = 1$$ và $$B = -1$$. Do $$\rho < 1$$, biên độ $$\rho^n$$ giảm nhanh về 0 nên $$a_n \to 0$$ khi $$n \to \infty$$ (dao động **tắt dần**).

</div>

### Bảng tổng hợp ba trường hợp nghiệm (bậc 2)

| Biệt thức $$\Delta$$ | Nghiệm đặc trưng | Dạng nghiệm tổng quát $$a_n$$ |
|:---:|:---|:---|
| $$\Delta > 0$$ | Hai nghiệm thực phân biệt $$r_1 \neq r_2$$ | $$\alpha r_1^n + \beta r_2^n$$ |
| $$\Delta = 0$$ | Một nghiệm thực kép $$r$$ | $$(\alpha + \beta n)r^n$$ |
| $$\Delta < 0$$ | Cặp nghiệm phức liên hợp $$\rho e^{\pm i\theta}$$ | $$\rho^n(A\cos n\theta + B\sin n\theta)$$ |

Ảnh hưởng của mô-đun $$\rho = \lvert r \rvert$$ đến dáng điệu dãy khi có nghiệm phức:

| Giá trị $$\rho = \lvert r \rvert$$ | Hành vi dài hạn của dãy |
|:---:|:---|
| $$\rho < 1$$ | Dao động tắt dần về 0 |
| $$\rho = 1$$ | Biên độ ổn định (thường tuần hoàn theo chu kỳ) |
| $$\rho > 1$$ | Dao động với biên độ tăng trưởng bùng nổ |

![Tỷ lệ vàng — nghiệm của Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Golden_ratio_line.svg)

<p class="textbook-figure-caption" data-figure="10.8">Dãy Fibonacci thuộc trường hợp nghiệm thực phân biệt với tỷ lệ vàng $$\varphi = (1+\sqrt{5})/2$$, nằm trong cùng khung phương pháp phương trình đặc trưng với các ví dụ nghiệm phức ở trên.</p>

## Mở rộng cho truy hồi bậc cao hơn

Với quan hệ truy hồi tuyến tính thuần nhất bậc $$k$$:

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+\cdots+c_ka_{n-k},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

phương trình đặc trưng tương ứng là đa thức bậc $$k$$:

<div class="textbook-equation" markdown="1">
$$
r^k-c_1r^{k-1}-c_2r^{k-2}-\cdots-c_k=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Mỗi nghiệm đơn $$r_i$$ đóng góp một hạng tử $$\alpha_i r_i^n$$; mỗi nghiệm bội $$m$$ đóng góp các hạng tử nhân thêm đa thức bậc $$m-1$$ theo $$n$$; và mỗi cặp nghiệm phức liên hợp đóng góp một thành phần $$\rho^n(A\cos n\theta + B\sin n\theta)$$.

![Merge Sort — truy hồi chia để trị](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

<p class="textbook-figure-caption" data-figure="10.9">Việc phân tích các thuật toán đệ quy thường dẫn về quan hệ truy hồi — tiêu biểu như $$T(n) = 2T(n/2) + n$$ của Merge Sort.</p>

![Master Theorem — giải truy hồi chia để trị](/discrete-mathematics-for-computer-science-iuh/img/course/Master_theorem.png)

<p class="textbook-figure-caption" data-figure="10.10">Định lý Thợ (Master Theorem) giúp giải nhanh dạng $$T(n) = aT(n/b) + f(n)$$ trong phân tích thuật toán thực tế.</p>

<div class="interactive-demo" markdown="1">
**Công cụ tương tác**: Nhập hệ số $$c_1, c_2$$ cùng điều kiện đầu để quan sát vị trí các nghiệm đặc trưng trên trục thực hoặc mặt phẳng phức và theo dõi các số hạng đầu tiên của dãy.
<div data-demo="linear-recurrence-solver"></div>
</div>
<script src="{{ '/public/js/linear-recurrence-solver.js' | relative_url }}"></script>

### Minh hoạ tương tác

Khám phá mối liên hệ giữa đa thức đặc trưng, các loại nghiệm (phân biệt, kép, phức) và công thức đóng sinh ra qua công cụ tương tác dưới đây:

<div class="interactive-demo" markdown="1">
<div data-demo="recurrence-explainer" data-mode="linear" data-preset="complex"></div>
</div>
<script src="{{ '/public/js/explainers/recurrence-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Giải $$a_n = 5a_{n-1}$$ với điều kiện đầu $$a_0 = 3$$.

<details>
<summary>Đáp án</summary>

Phương trình đặc trưng là $$r = 5$$. Suy ra công thức đóng: $$a_n = 3 \cdot 5^n$$.

</details>

### Bài tập 2

Giải $$a_n = 4a_{n-1} - 4a_{n-2}$$ với $$a_0 = 1$$ và $$a_1 = 4$$.

<details>
<summary>Đáp án</summary>

Phương trình đặc trưng $$r^2 - 4r + 4 = (r - 2)^2 = 0$$ có nghiệm kép $$r = 2$$, nên $$a_n = (\alpha + \beta n)2^n$$. Thay điều kiện đầu ta tìm được $$\alpha = 1$$ và $$\beta = 1$$. Vậy $$a_n = (1 + n)2^n$$.

</details>

### Bài tập 2b (nghiệm bội)

Giải $$X_n = 2X_{n-1} - X_{n-2}$$ với $$X_0 = 1$$, $$X_1 = 3$$. Giải thích vì sao không thể dùng công thức dạng $$A r_1^n + B r_2^n$$ khi $$r_1 = r_2 = 1$$.

<details>
<summary>Đáp án</summary>

Phương trình đặc trưng $$(r - 1)^2 = 0$$ có nghiệm kép $$r = 1$$, nên $$X_n = A + Bn$$. Từ $$X_0 = 1, X_1 = 3$$ suy ra $$A = 1, B = 2$$, tức $$X_n = 1 + 2n$$. Nếu viết $$A \cdot 1^n + B \cdot 1^n$$, biểu thức suy biến thành hằng số $$A + B$$ nên không thể thỏa mãn đồng thời hai điều kiện đầu khác nhau $$X_0 \neq X_1$$.

</details>

### Bài tập 3

Giải quan hệ truy hồi Fibonacci $$a_n = a_{n-1} + a_{n-2}$$ với $$a_0 = 0$$, $$a_1 = 1$$. Viết công thức đóng theo các nghiệm đặc trưng.

<details>
<summary>Đáp án</summary>

Phương trình đặc trưng $$r^2 - r - 1 = 0$$ cho hai nghiệm $$\varphi = \frac{1 + \sqrt{5}}{2}$$ và $$\hat\varphi = \frac{1 - \sqrt{5}}{2}$$. Từ $$a_n = \alpha\varphi^n + \beta\hat\varphi^n$$ kết hợp điều kiện đầu $$a_0 = 0, a_1 = 1$$, ta thu được công thức Binet: $$F_n = \frac{\varphi^n - \hat\varphi^n}{\sqrt{5}}$$.

</details>

### Bài tập 4 — Chuyển đổi dạng số phức

Viết số phức $$z = -1 + i\sqrt{3}$$ dưới **dạng cực** và **dạng mũ**, đồng thời tính $$\lvert z \rvert$$ và $$\operatorname{arg}(z)$$.

<details>
<summary>Đáp án</summary>

Mô-đun: $$\rho = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = 2$$.

Vì phần thực $$a = -1 < 0$$ và phần ảo $$b = \sqrt{3} > 0$$ (điểm nằm ở góc phần tư thứ II):

$$
\theta = \pi + \arctan\left(\frac{\sqrt{3}}{-1}\right) = \pi - \frac{\pi}{3} = \frac{2\pi}{3}.
$$

- **Dạng cực**: $$z = 2\bigl(\cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3}\bigr)$$.
- **Dạng mũ**: $$z = 2e^{i 2\pi/3}$$.

</details>

### Bài tập 5 — Ứng dụng định lý De Moivre

Sử dụng định lý De Moivre để tính $$(1 + i)^6$$.

<details>
<summary>Đáp án</summary>

Vì $$1 + i = \sqrt{2}\,e^{i\pi/4}$$, ta có:

$$
(1+i)^6 = (\sqrt{2})^6 e^{i 6\pi/4} = 8\,e^{i 3\pi/2} = 8\bigl(\cos\frac{3\pi}{2} + i\sin\frac{3\pi}{2}\bigr) = 8(0 - i) = -8i.
$$

</details>

### Bài tập 6 — Truy hồi nghiệm phức (tuần hoàn)

Giải $$a_n = -a_{n-2}$$ với $$a_0 = 0$$, $$a_1 = 1$$. Viết nghiệm ở dạng $$\rho^n(A\cos n\theta + B\sin n\theta)$$ và liệt kê sáu số hạng đầu tiên.

<details>
<summary>Đáp án</summary>

Phương trình đặc trưng $$r^2 + 1 = 0 \Rightarrow r = \pm i$$, nên $$\rho = 1$$ và $$\theta = \pi/2$$.

$$a_n = A\cos\frac{n\pi}{2} + B\sin\frac{n\pi}{2}.$$

Thay $$a_0 = 0 \Rightarrow A = 0$$ và $$a_1 = 1 \Rightarrow B = 1$$. Vậy $$a_n = \sin\frac{n\pi}{2}$$.

Sáu số hạng đầu tiên: $$0, 1, 0, -1, 0, 1$$ (tuần hoàn chu kỳ 4).

</details>

### Bài tập 7 — Truy hồi nghiệm phức (biên độ tăng)

Giải $$a_n = 2a_{n-1} - 2a_{n-2}$$ với $$a_0 = 1$$, $$a_1 = 2$$. Xác định $$\rho$$, $$\theta$$ và công thức đóng.

<details>
<summary>Đáp án</summary>

Nghiệm đặc trưng là $$r = 1 \pm i$$, suy ra $$\rho = \sqrt{2}$$ và $$\theta = \pi/4$$.

Từ điều kiện đầu (tương tự Ví dụ 2), ta tìm được $$A = 1, B = 1$$, do đó:

$$a_n = (\sqrt{2})^n\Bigl(\cos\frac{n\pi}{4} + \sin\frac{n\pi}{4}\Bigr).$$

</details>

### Bài tập 8 (thử thách) — Dao động tắt dần

Xét quan hệ truy hồi ở Ví dụ 4: $$a_n = a_{n-1} - \frac{1}{2}a_{n-2}$$ với $$a_0 = 1$$, $$a_1 = 0$$. Hãy giải thích vì sao $$a_n \to 0$$ khi $$n \to \infty$$ và ước lượng một cận trên đơn giản cho $$\lvert a_{10} \rvert$$.

<details>
<summary>Đáp án</summary>

Vì $$\rho = \frac{\sqrt{2}}{2} \approx 0{,}707 < 1$$, nhân tử $$\rho^n$$ tiến về 0 khi $$n \to \infty$$, kéo theo $$a_n \to 0$$.

Do $$\lvert \cos\alpha - \sin\alpha \rvert \le \sqrt{2}$$ với mọi $$\alpha$$, ta có đánh giá:

$$\lvert a_n \rvert \le \left(\frac{\sqrt{2}}{2}\right)^n \cdot \sqrt{2}.$$

Thay $$n = 10$$:

$$\lvert a_{10} \rvert \le 2^{-5}\sqrt{2} = \frac{\sqrt{2}}{32} \approx 0{,}044.$$

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=T647CGsuOVU">Complex numbers: Introduction</a> — 3Blue1Brown (Trực giác về số phức và mặt phẳng Argand).
- <a href="https://www.youtube.com/watch?v=fReOvGlhIDw">e^(iπ) in 3.14 minutes</a> — Mathologer (Giải thích công thức Euler và De Moivre).
- <a href="https://www.youtube.com/watch?v=uhxtUt_-GyM">Solving Linear Recurrence Relations</a> — Trefor Bazett (Tổng hợp cách giải truy hồi tuyến tính).

## Tóm tắt

- **Quan hệ truy hồi tuyến tính thuần nhất hệ số hằng bậc $$k$$**: $$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k}$$.
- Giả sử nghiệm có dạng $$r^n$$ dẫn tới **phương trình đặc trưng** bậc $$k$$.
- Với bậc hai: nghiệm thực phân biệt cho $$a_n = \alpha r_1^n + \beta r_2^n$$; nghiệm kép cho $$a_n = (\alpha + \beta n)r^n$$.
- **Số phức**: viết dưới dạng đại số $$z = a + bi$$, hình học (mặt phẳng Argand) và cực / mũ $$z = \rho e^{i\theta}$$; **định lý De Moivre** cho $$z^n = \rho^n(\cos n\theta + i\sin n\theta)$$.
- Cặp nghiệm phức liên hợp cho dạng nghiệm thực $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$, với dáng điệu dài hạn phụ thuộc vào $$\rho < 1$$, $$\rho = 1$$ hay $$\rho > 1$$.
- Ở bậc cao hơn, nghiệm tổng quát là tổng đóng góp của tất cả các nghiệm đơn, nghiệm bội và cặp nghiệm phức liên hợp.

Trong bài tiếp theo, chúng ta sẽ mở rộng sang **quan hệ truy hồi không thuần nhất** — trường hợp phương trình có thêm thành phần tác động bên ngoài $$f(n)$$.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=7mhvA5L7KqY">HOMOGENEOUS RECURRENCE RELATIONS - Discrete Mathematics</a> — TrevTutor (tiếng Anh). Giới thiệu phương pháp lập và giải phương trình đặc trưng.
- <a href="https://www.youtube.com/watch?v=Otj2ypYXn0Q">[Discrete Mathematics] Homogeneous Recurrence Relations Examples</a> — TrevTutor (tiếng Anh). Minh họa chi tiết cách giải nghiệm phân biệt và thay điều kiện đầu.
- <a href="https://www.youtube.com/watch?v=T647CGsuOVU">Imaginary Numbers Are Real [Part 1: Introduction]</a> — Welch Labs (tiếng Anh). Ôn tập trực quan về số phức và mặt phẳng Argand, bổ trợ cho phần nghiệm phức và định lý De Moivre.
