---
layout: post
title: "Giải Quan hệ Truy hồi Tuyến tính"
categories: chapter10
date: 2021-01-01
order: 2
required: true
lang: vi
excerpt: "Phương trình đặc trưng, nghiệm phân biệt/kép/phức, số phức (dạng đại số–cực–De Moivre), và công thức đóng của truy hồi tuyến tính thuần nhất hệ số hằng."
---

Ở mục trước chúng ta đã định nghĩa quan hệ truy hồi và phân loại theo tính tuyến tính, thuần nhất, và bậc. Mục này tập trung vào **quan hệ truy hồi tuyến tính thuần nhất hệ số hằng** — lớp bài toán cho phép tìm công thức tường minh $$a_n$$ hoặc ít nhất mô tả rõ cấu trúc tăng trưởng của dãy, thay vì tính lần lượt từng bước. Từ số phép gọi đệ quy, số cấu hình ở mỗi mức, đến độ phức tạp của thuật toán chia để trị, nhiều bài toán quy về giải đúng một truy hồi tuyến tính. Chúng ta học kỹ thuật **phương trình đặc trưng** và các dạng nghiệm (phân biệt, bội, phức). Khi biệt thức âm, nghiệm đặc trưng là số phức: bạn sẽ ôn nhanh **số phức**, **ba cách biểu diễn**, và **De Moivre** để viết được dạng sin–cos thực của dãy.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Viết** phương trình đặc trưng cho truy hồi tuyến tính thuần nhất hệ số hằng bậc $$k$$.
- **Giải** các trường hợp nghiệm **phân biệt**, **kép**, và **phức liên hợp**.
- **Biểu diễn** số phức dưới dạng đại số, hình học (Argand) và cực / mũ; dùng **De Moivre** để tính $$z^n$$.
- **Chuyển** cặp nghiệm $$r = \rho e^{\pm i\theta}$$ thành dạng thực $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$ và xác định $$A,B$$ từ điều kiện đầu.
- **Đọc** hành vi dãy theo mô-đun $$\rho$$: tắt ($$\rho < 1$$), chu kỳ ($$\rho = 1$$), phình ($$\rho > 1$$).

**Từ khóa**: phương trình đặc trưng (characteristic equation), nghiệm phân biệt / bội / phức, số phức (complex number), mô-đun, argument, dạng cực, De Moivre, công thức Binet.

</div>

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

<div class="textbook-example" markdown="1">

**Ví dụ (nghiệm bội $$r=1$$ — dãy số lẻ).**  
Xét $$X_n = 2X_{n-1} - X_{n-2}$$ với $$X_0=1$$, $$X_1=3$$.  
Thay $$X_n=r^n$$: $$r^2=2r-1$$ tức $$(r-1)^2=0$$ — nghiệm bội $$r=1$$.  
**Không** được viết $$X_n=A\cdot 1^n+B\cdot 1^n=A+B$$ (hằng số): điều kiện $$X_0=1$$, $$X_1=3$$ mâu thuẫn với dãy hằng.  
Dạng đúng: $$X_n=(A_1+A_2 n)\,1^n=A_1+A_2 n$$.  
$$n=0$$: $$A_1=1$$; $$n=1$$: $$1+A_2=3\Rightarrow A_2=2$$.  
Vậy $$X_n=1+2n$$. Kiểm: $$1,3,5,7,9,\ldots$$ và $$2\cdot 3-1=5$$, $$2\cdot 5-3=7$$.

</div>


## 5. Nghiệm phức và kiến thức số phức

Với truy hồi bậc hai hệ số thực

<div class="textbook-equation" markdown="1">
$$
a_n = c_1 a_{n-1} + c_2 a_{n-2},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

phương trình đặc trưng là $$r^2 - c_1 r - c_2 = 0$$. Biệt thức

<div class="textbook-equation" markdown="1">
$$
\Delta = c_1^2 + 4c_2
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

quyết định loại nghiệm: $$\Delta > 0$$ phân biệt thực, $$\Delta = 0$$ kép, $$\Delta < 0$$ **hai nghiệm phức liên hợp**. Khi $$\Delta < 0$$, nghiệm không nằm trên trục thực; để viết $$r^n$$ và dạng **thực** của dãy $$a_n$$, bạn cần số phức và các cách biểu diễn của chúng.

<div class="content-box insight-box textbook-block" markdown="1">
**Lưu ý quan trọng.** Dãy $$a_n$$ trong bài toán thường là **số thực** (số lần gọi đệ quy, biên độ tín hiệu, …). Nghiệm đặc trưng có thể phức, nhưng công thức đóng cuối cùng nên viết bằng $$\rho^n$$, $$\cos$$, $$\sin$$ với hệ số thực — không “bỏ qua” phần ảo một cách tùy tiện.
</div>

### 5.1. Định nghĩa số phức

<div class="textbook-definition" markdown="1">

**Định nghĩa**: Một **số phức** (complex number) $$z \in \mathbb{C}$$ có **dạng đại số**

$$
z = a + bi,\qquad a,b \in \mathbb{R},\quad i^2 = -1.
$$

- $$a = \operatorname{Re}(z)$$ — **phần thực** (real part);
- $$b = \operatorname{Im}(z)$$ — **phần ảo** (imaginary part);
- $$i$$ — **đơn vị ảo** (imaginary unit).

Hai số phức bằng nhau khi và chỉ khi phần thực **và** phần ảo bằng nhau:

$$
a + bi = c + di \iff (a = c \;\text{và}\; b = d).
$$

</div>

Các trường hợp đặc biệt:

- $$b = 0$$: $$z$$ là số **thực** — $$\mathbb{R} \subset \mathbb{C}$$;
- $$a = 0$$, $$b \neq 0$$: $$z$$ **thuần ảo** (pure imaginary).

<div class="textbook-example" markdown="1">

**Ví dụ**: Đọc phần thực và phần ảo.

| $$z$$ | $$\operatorname{Re}(z)$$ | $$\operatorname{Im}(z)$$ |
|:---|:---:|:---:|
| $$3 + 2i$$ | 3 | 2 |
| $$-1$$ | $$-1$$ | 0 |
| $$i$$ | 0 | 1 |
| $$1 - i$$ | 1 | $$-1$$ |

</div>

### 5.2. Liên hợp phức

<div class="textbook-definition" markdown="1">

**Định nghĩa**: **Liên hợp** (complex conjugate) của $$z = a + bi$$ là

$$
\overline{z} = a - bi.
$$

</div>

Tính chất hay dùng (kiểm tra trực tiếp từ định nghĩa):

- $$z + \overline{z} = 2a$$ (luôn thực);
- $$z - \overline{z} = 2bi$$ (thuần ảo);
- $$z \cdot \overline{z} = a^2 + b^2$$ (thực, $$\ge 0$$);
- $$\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$$;
- $$\overline{z_1 z_2} = \overline{z_1}\, \overline{z_2}$$;
- $$\overline{\overline{z}} = z$$.

**Vai trò với truy hồi.** Đa thức đặc trưng có **hệ số thực** thì nếu $$r$$ là nghiệm phức thì $$\overline{r}$$ cũng là nghiệm. Do đó nghiệm phức luôn xuất hiện **theo cặp liên hợp** — đây là lý do dạng sin–cos có đúng hai hằng số tự do $$A,B$$ cho mỗi cặp.

### 5.3. Ba cách biểu diễn

| Dạng | Công thức | Khi dùng |
|:---|:---|:---|
| **Đại số** | $$z = a + bi$$ | cộng, trừ, so sánh, liên hợp |
| **Hình học (Argand)** | điểm $$(a,b)$$ / vector $$\overrightarrow{Oz}$$ | trực giác, khoảng cách, góc |
| **Cực / mũ** | $$z = \rho(\cos\theta + i\sin\theta) = \rho e^{i\theta}$$ | **nhân** và **lũy thừa** $$z^n$$ |

### 5.4. Dạng đại số — phép toán cơ bản

Với $$z_1 = a + bi$$, $$z_2 = c + di$$:

**Cộng / trừ** (theo tọa độ):

<div class="textbook-equation" markdown="1">
$$
z_1 \pm z_2 = (a \pm c) + (b \pm d)i.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Nhân** (dùng $$i^2 = -1$$):

<div class="textbook-equation" markdown="1">
$$
z_1 z_2 = (ac - bd) + (ad + bc)i.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Chia** (nhân liên hợp mẫu số, $$z_2 \neq 0$$):

<div class="textbook-equation" markdown="1">
$$
\frac{z_1}{z_2} = \frac{z_1 \overline{z_2}}{\lvert z_2 \rvert^2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

### 5.5. Biểu diễn hình học — mặt phẳng phức

Mỗi $$z = a + bi$$ tương ứng **một điểm** $$(a,b)$$ trên **mặt phẳng phức** (complex plane / Argand diagram):

- trục ngang: **Re** (phần thực);
- trục đứng: **Im** (phần ảo);
- gốc $$O$$: số $$0$$;
- đoạn $$\overrightarrow{Oz}$$: vector biểu diễn $$z$$.

![Mặt phẳng phức — dạng đại số](/discrete-mathematics-for-computer-science-iuh/img/course/Complex_plane_algebraic.svg)

<p class="textbook-figure-caption" data-figure="10.8a">Số phức $$z = a + bi$$ tương ứng điểm $$(a,b)$$ trên mặt phẳng Argand. Ví dụ $$z = 3 + 2i$$.</p>

### 5.6. Mô-đun và argument

<div class="textbook-definition" markdown="1">

**Định nghĩa**: Với $$z = a + bi$$,

- **Mô-đun** (modulus / absolute value):

$$
\lvert z \rvert = \rho = \sqrt{a^2 + b^2}
$$

là khoảng cách từ gốc $$O$$ tới điểm $$(a,b)$$.

- **Argument** (đối số, góc): $$\theta = \operatorname{arg}(z)$$ là góc từ trục Re dương tới vector $$\overrightarrow{Oz}$$ (thường lấy trong khoảng mở-đóng $$(-\pi,\pi]$$).

Khi $$a > 0$$: $$\theta = \arctan\left(\frac{b}{a}\right)$$. Khi $$a < 0$$ cần cộng thêm $$\pi$$ (hoặc $$-\pi$$) để đúng góc phần tư (vì $$\arctan$$ chỉ trả giá trị trong $$(-\pi/2,\pi/2)$$).

</div>

Tính chất mô-đun:

- $$\lvert z \rvert \ge 0$$; $$\lvert z \rvert = 0 \iff z = 0$$;
- $$\lvert \overline{z} \rvert = \lvert z \rvert$$;
- $$\lvert z_1 z_2 \rvert = \lvert z_1 \rvert\,\lvert z_2 \rvert$$ và $$\lvert z^n \rvert = \lvert z \rvert^n$$;
- bất đẳng thức tam giác: $$\lvert z_1 + z_2 \rvert \le \lvert z_1 \rvert + \lvert z_2 \rvert$$.

<div class="content-box insight-box textbook-block" markdown="1">
**Với HTTH**: $$\rho = \lvert r \rvert$$ của nghiệm đặc trưng quyết định hành vi dãy khi $$n \to \infty$$ — tắt ($$\rho < 1$$), biên độ ổn định / chu kỳ ($$\rho = 1$$), hoặc phình ($$\rho > 1$$). Đây là cầu nối sang phân tích ổn định hệ tuyến tính rời rạc và bộ lọc tín hiệu.
</div>

### 5.7. Dạng cực và dạng mũ

<div class="textbook-definition" markdown="1">

**Định nghĩa (dạng cực)**: Nếu $$\rho = \lvert z \rvert$$ và $$\theta = \operatorname{arg}(z)$$ thì

$$
z = \rho\bigl(\cos\theta + i\sin\theta\bigr).
$$

**Dạng mũ** (Euler): $$e^{i\theta} = \cos\theta + i\sin\theta$$, nên

$$
z = \rho e^{i\theta}.
$$

</div>

Chuyển đổi hai chiều:

| Chiều | Công thức |
|:---|:---|
| Đại số $$\to$$ cực | $$\rho = \sqrt{a^2 + b^2}$$, $$\theta = \arctan\left(\frac{b}{a}\right)$$ ($$a > 0$$) |
| Cực $$\to$$ đại số | $$a = \rho\cos\theta$$, $$b = \rho\sin\theta$$ |

Liên hợp trong dạng cực: $$\overline{z} = \rho\bigl(\cos\theta - i\sin\theta\bigr) = \rho e^{-i\theta}$$ (cùng mô-đun, góc đổi dấu).

![Dạng cực của số phức](/discrete-mathematics-for-computer-science-iuh/img/course/Complex_plane_polar.svg)

<p class="textbook-figure-caption" data-figure="10.8b">Dạng cực: bán kính $$\rho = \lvert z \rvert$$ và góc $$\theta = \operatorname{arg}(z)$$; tọa độ $$(a,b) = (\rho\cos\theta,\ \rho\sin\theta)$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ**: Chuyển $$z = 1 + i$$ sang dạng cực và dạng mũ.

1. $$\rho = \sqrt{1^2 + 1^2} = \sqrt{2}$$;
2. $$\theta = \arctan\left(\frac{1}{1}\right) = \arctan(1) = \frac{\pi}{4}$$;
3. cực: $$z = \sqrt{2}\bigl(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\bigr)$$;
4. mũ: $$z = \sqrt{2}\, e^{i\pi/4}$$.

Kiểm tra ngược: $$\sqrt{2}\cdot \frac{\sqrt{2}}{2} + i\sqrt{2}\cdot\frac{\sqrt{2}}{2} = 1 + i$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ**: Các điểm trên đường tròn đơn vị ($$\rho = 1$$).

| $$z$$ | $$\rho$$ | $$\theta$$ | Dạng cực |
|:---|:---:|:---:|:---|
| $$-1$$ | 1 | $$\pi$$ | $$\cos\pi + i\sin\pi$$ |
| $$i$$ | 1 | $$\pi/2$$ | $$\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}$$ |
| $$-i$$ | 1 | $$-\pi/2$$ | $$\cos(-\frac{\pi}{2}) + i\sin(-\frac{\pi}{2})$$ |

</div>

### 5.8. Định lý De Moivre

<div class="textbook-theorem" markdown="1">

**Định lý (De Moivre)**: Nếu $$z = \rho(\cos\theta + i\sin\theta)$$ thì với mọi số nguyên $$n$$,

$$
z^n = \rho^n\bigl(\cos n\theta + i\sin n\theta\bigr).
$$

Tương đương: $$(\rho e^{i\theta})^n = \rho^n e^{in\theta}$$.

</div>

**Đọc hình học**: lũy thừa $$z^n$$ **nhân góc** với $$n$$ và **nâng mô-đun** lên lũy thừa $$n$$.

![De Moivre — lũy thừa trên mặt phẳng phức](/discrete-mathematics-for-computer-science-iuh/img/course/Complex_de_moivre.svg)

<p class="textbook-figure-caption" data-figure="10.8c">De Moivre: $$z^n$$ quay vector thêm góc $$(n-1)\theta$$ (tổng góc $$n\theta$$) và đổi độ dài thành $$\rho^n$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ**: Tính $$(1+i)^4$$ bằng De Moivre.

$$1+i = \sqrt{2}\, e^{i\pi/4}$$, nên

$$
(1+i)^4 = (\sqrt{2})^4 e^{i\pi} = 4(\cos\pi + i\sin\pi) = 4(-1) = -4.
$$

</div>

### 5.9. Từ nghiệm phức đến dạng sin–cos (giải thích từng bước)

Mục này trả lời hai câu hỏi liên tiếp:

1. Từ $$a_n = C r^n + D\, \overline{r}^{n}$$ với $$C,D$$ phức chưa biết, vì sao **bắt buộc** $$D = \overline{C}$$ khi $$a_n$$ thực?
2. Từ đó, vì sao được $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$, và vì sao công thức cuối **không còn số phức**?

#### Ý chính (đọc trước, nhớ sau)

1. Nghiệm đặc trưng phức đi **cặp** $$r$$ và $$\overline{r}$$.
2. Từ $$a_n$$ thực, **chứng minh** (không giả định) rằng $$D = \overline{C}$$.
3. Lũy thừa $$r^n$$ viết bằng **cos / sin** (De Moivre).
4. Cộng hai số **liên hợp nhau** → phần ảo **hủy**; còn lại chỉ cos và sin với hệ số **thực** $$A,B$$.
5. Làm bài: **không** cần tính $$C$$ — viết thẳng dạng sin–cos rồi tìm $$A,B$$ từ điều kiện đầu.

#### Bước 0 — Có gì trong tay?

Đặc trưng bậc 2, $$\Delta < 0$$, hệ số thực:

$$
r = \alpha + i\beta,\qquad \overline{r} = \alpha - i\beta \quad (\beta \neq 0).
$$

Chuyển sang dạng cực (đã học):

$$
r = \rho\bigl(\cos\theta + i\sin\theta\bigr),\qquad
\rho = \lvert r \rvert,\quad
\theta = \operatorname{arg}(r).
$$

De Moivre (công thức lũy thừa):

$$
r^n = \rho^n\bigl(\cos n\theta + i\sin n\theta\bigr),
$$

$$
\overline{r}^{n} = \rho^n\bigl(\cos n\theta - i\sin n\theta\bigr).
$$

**Chú ý:** hai vế chỉ khác **dấu** trước $$i\sin n\theta$$. Đó chính là “cặp liên hợp”.

#### Bước 1 — Dạng nghiệm tổng quát (chưa lo “thực”)

Vì có **hai** nghiệm phân biệt, nghiệm tổng quát luôn có **hai** hằng số:

$$
a_n = C\, r^n + D\, \overline{r}^{n}.
$$

Ở đây $$C$$ và $$D$$ là hằng số (có thể phức). Đây chỉ là “khung” đại số — giống $$\alpha r_1^n + \beta r_2^n$$ khi nghiệm thực, nhưng giờ $$r_1,r_2$$ phức.

#### Bước 2 — Chứng minh: $$a_n$$ thực $$\Rightarrow$$ $$D = \overline{C}$$

Ở Bước 1 ta **chỉ** biết

<div class="textbook-equation" markdown="1">
$$
a_n = C\, r^n + D\, \overline{r}^{n},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

với $$C,D \in \mathbb{C}$$ **chưa biết**. Ta **chưa** được phép kết luận $$D = \overline{C}$$. Việc chọn $$D = \overline{C}$$ **không phải giả định** — đó là **hệ quả bắt buộc** khi dãy $$a_n$$ thực.

**Giả thiết.** Hệ số truy hồi thực và điều kiện đầu thực ⇒ mọi $$a_n$$ **thực**.

**Hệ quả của số thực.** Một số $$z$$ thực khi và chỉ khi $$z = \overline{z}$$. Do đó với mọi $$n$$:

$$
a_n = \overline{a_n}.
$$

**Lấy liên hợp hai vế** của $$a_n = C r^n + D\, \overline{r}^{n}$$. Dùng tính chất $$\overline{zw} = \overline{z}\,\overline{w}$$ và $$\overline{\overline{r}} = r$$:

{% raw %}
$$
\begin{aligned}
\overline{a_n}
&= \overline{C\, r^n + D\, \overline{r}^{n}} \\
&= \overline{C}\, \overline{r}^{n} + \overline{D}\, r^{n}.
\end{aligned}
$$
{% endraw %}

(Lưu ý: $$\overline{r^{n}} = \overline{r}^{n}$$ và $$\overline{\overline{r}^{n}} = r^{n}$$.)

**So sánh hai biểu thức** của cùng một dãy. Vì $$a_n = \overline{a_n}$$:

<div class="textbook-equation" markdown="1">
$$
C\, r^n + D\, \overline{r}^{n}
=
\overline{D}\, r^n + \overline{C}\, \overline{r}^{n}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Đưa về một vế:

$$
\bigl(C - \overline{D}\bigr)\, r^n
+
\bigl(D - \overline{C}\bigr)\, \overline{r}^{n}
= 0
\quad\text{với mọi } n.
$$

**Độc lập tuyến tính.** Vì $$r \neq \overline{r}$$ (nghiệm không thuần thực, $$\beta \neq 0$$), hai dãy hàm $$n \mapsto r^n$$ và $$n \mapsto \overline{r}^{n}$$ **độc lập tuyến tính** trên $$\mathbb{C}$$. Hệ quả: tổ hợp tuyến tính bằng 0 với mọi $$n$$ chỉ khi **cả hai hệ số triệt tiêu**:

$$
C - \overline{D} = 0,\qquad
D - \overline{C} = 0.
$$

Tức

$$
C = \overline{D},\qquad
D = \overline{C}.
$$

Hai đẳng thức **tương đương** (lấy liên hợp vế này được vế kia). Vậy

<div class="textbook-equation" markdown="1">
$$
D = \overline{C}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

là **kết luận bắt buộc**, không phải lựa chọn tùy ý.

**Hệ quả.** Nghiệm tổng quát của dãy **thực** phải có dạng

$$
a_n = C\, r^n + \overline{C}\, \overline{r}^{n}.
$$

**Kiểm tra ngược (đủ).** Nếu $$D = \overline{C}$$ và đặt $$w = C r^n$$ thì $$a_n = w + \overline{w} = 2\operatorname{Re}(w) \in \mathbb{R}$$. Vậy điều kiện $$D = \overline{C}$$ cũng **đủ** để $$a_n$$ thực.

<div class="content-box insight-box textbook-block" markdown="1">
**Tóm Bước 2.**  
$$a_n$$ thực $$\Rightarrow$$ $$a_n = \overline{a_n}$$ $$\Rightarrow$$ so sánh hệ số của $$r^n$$ và $$\overline{r}^{n}$$ (độc lập tuyến tính) $$\Rightarrow$$ $$D = \overline{C}$$.  
Chiều ngược: $$D = \overline{C}$$ $$\Rightarrow$$ $$a_n = w + \overline{w}$$ thực.
</div>

#### Bước 3 — Ví dụ số cụ thể (trước khi tổng quát)

Lấy $$r = i$$ (thường gặp với $$a_n = -a_{n-2}$$). Khi đó $$\rho = 1$$, $$\theta = \pi/2$$, và

$$
i^n = \cos\frac{n\pi}{2} + i\sin\frac{n\pi}{2},\qquad
(-i)^n = \cos\frac{n\pi}{2} - i\sin\frac{n\pi}{2}.
$$

Chọn một hệ số đơn giản $$C = \dfrac{1}{2}$$ (thực; liên hợp $$\overline{C} = \dfrac{1}{2}$$):

$$
a_n
= \frac{1}{2}\, i^n + \frac{1}{2}\, (-i)^n
= \frac{1}{2}\Bigl(
  \cos\frac{n\pi}{2} + i\sin\frac{n\pi}{2}
  + \cos\frac{n\pi}{2} - i\sin\frac{n\pi}{2}
\Bigr).
$$

Hai số hạng $$+i\sin$$ và $$-i\sin$$ **hủy nhau**:

$$
a_n = \frac{1}{2}\cdot 2\cos\frac{n\pi}{2} = \cos\frac{n\pi}{2}.
$$

Nhìn lại: đây **đúng** dạng

$$
a_n = \rho^n\bigl(A\cos n\theta + B\sin n\theta\bigr)
= 1^n\Bigl(1\cdot\cos\frac{n\pi}{2} + 0\cdot\sin\frac{n\pi}{2}\Bigr)
$$

với $$A = 1$$, $$B = 0$$. **Không còn $$i$$** trong đáp án.

Kiểm tra vài số hạng: $$n=0 \to 1$$; $$n=1 \to 0$$; $$n=2 \to -1$$; $$n=3 \to 0$$ — dãy thực, đúng như mong đợi.

#### Bước 4 — Trường hợp tổng quát: đặt $$C = p + qi$$

Mọi số phức $$C$$ viết được

$$
C = p + qi,\qquad p,q \in \mathbb{R}
$$

(tức $$p = \operatorname{Re}(C)$$, $$q = \operatorname{Im}(C)$$). Khi đó $$\overline{C} = p - qi$$.

Thay vào công thức và **rút** $$\rho^n$$ ra ngoài:

$$
a_n = \rho^n \cdot \Bigl[
  (p+qi)\,(\cos n\theta + i\sin n\theta)
  +
  (p-qi)\,(\cos n\theta - i\sin n\theta)
\Bigr].
$$

**Nhân số phức ở ngoặc thứ nhất** (dùng $$i^2 = -1$$):

$$
(p+qi)(\cos n\theta + i\sin n\theta)
=
\bigl(p\cos n\theta - q\sin n\theta\bigr)
+
i\bigl(p\sin n\theta + q\cos n\theta\bigr).
$$

**Nhân ở ngoặc thứ hai:**

$$
(p-qi)(\cos n\theta - i\sin n\theta)
=
\bigl(p\cos n\theta - q\sin n\theta\bigr)
-
i\bigl(p\sin n\theta + q\cos n\theta\bigr).
$$

**Cộng hai kết quả:** phần ảo $$+i(\ldots)$$ và $$-i(\ldots)$$ triệt tiêu; phần thực **cộng đôi**:

$$
(p+qi)(\cos n\theta + i\sin n\theta)
+
(p-qi)(\cos n\theta - i\sin n\theta)
=
2\bigl(p\cos n\theta - q\sin n\theta\bigr).
$$

Vậy

$$
a_n = \rho^n \cdot 2\bigl(p\cos n\theta - q\sin n\theta\bigr)
= \rho^n\bigl(A\cos n\theta + B\sin n\theta\bigr),
$$

trong đó ta **đặt tên lại** (chỉ là đổi tên cho gọn):

$$
A = 2p,\qquad B = -2q.
$$

Vì $$p,q$$ tùy ý thực, $$A,B$$ cũng là **hai hằng số thực tùy ý**. Không mất tính tổng quát.

<div class="textbook-equation" markdown="1">
$$
a_n = \rho^n\bigl(A\cos n\theta + B\sin n\theta\bigr),\qquad A,B \in \mathbb{R}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

#### Bước 5 — Bảng “cái gì biến thành cái gì?”

| Trong công thức phức | Trong công thức thực |
|:---|:---|
| Cặp $$r,\ \overline{r}$$ | Hai số thực $$\rho$$ và $$\theta$$ |
| Hằng số phức $$C = p+qi$$ | Hai hằng số thực $$A,B$$ |
| $$C r^n + \overline{C}\,\overline{r}^{n}$$ | $$\rho^n(A\cos n\theta + B\sin n\theta)$$ |
| Phần ảo | **Biến mất** (cộng liên hợp) |
| Điều kiện đầu $$a_0,a_1$$ | Hệ 2 phương trình cho $$A,B$$ |

#### Bước 6 — Làm bài thì làm thế nào? (quan trọng nhất)

Bạn **không cần** tìm $$C$$, $$p$$, $$q$$ khi giải bài tập.

1. Tìm $$r = \alpha \pm i\beta$$ từ đặc trưng.
2. Tính $$\rho = \sqrt{\alpha^2+\beta^2}$$, $$\theta = \operatorname{arg}(r)$$.
3. **Viết thẳng**

   $$
   a_n = \rho^n\bigl(A\cos n\theta + B\sin n\theta\bigr).
   $$

4. Thay $$n=0$$ và $$n=1$$ (điều kiện đầu) → giải $$A,B$$.
5. Kiểm tra một số hạng bằng truy hồi gốc.

Số phức chỉ dùng ở bước 1–2 (tìm $$\rho,\theta$$). Từ bước 3 trở đi toàn **số thực**.

<div class="content-box insight-box textbook-block" markdown="1">
**Tóm tắt siêu ngắn.**  
$$C r^n$$ là một số phức; cộng thêm liên hợp $$\overline{C}\,\overline{r}^{n}$$ → chỉ còn phần thực.  
Phần thực đó, nhờ De Moivre, chính là tổ hợp $$\rho^n(A\cos n\theta + B\sin n\theta)$$.
</div>

<div class="textbook-theorem" markdown="1">

**Quy trình khi gặp nghiệm phức (bậc 2)**

1. Viết đặc trưng; kiểm tra $$\Delta < 0$$.
2. Tìm $$r = \alpha \pm i\beta$$ → $$\rho$$, $$\theta$$.
3. Viết $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$ (bỏ qua $$C$$).
4. Dùng $$a_0,a_1$$ giải $$A,B$$.
5. Kiểm tra bằng truy hồi.

</div>

### 5.10. Các ví dụ giải HTTH với nghiệm phức

<div class="textbook-example" markdown="1">

**Ví dụ 0 (từ giáo trình: $$r=2\pm i$$).**  
Giải $$X_n=4X_{n-1}-5X_{n-2}$$, $$X_0=1$$, $$X_1=2$$.  
Đặc trưng: $$r^2-4r+5=0$$ → $$r=2\pm i$$.  
$$\rho=\sqrt{4+1}=\sqrt{5}$$, $$\theta=\arctan(1/2)$$ (vì $$a=2>0$$).  
Dạng thực: $$X_n=(\sqrt{5})^n\bigl(A\cos n\theta+B\sin n\theta\bigr)$$.  
$$n=0$$: $$A=1$$.  
$$n=1$$: $$\sqrt{5}\bigl(A\cos\theta+B\sin\theta\bigr)=2$$ với $$\cos\theta=2/\sqrt{5}$$, $$\sin\theta=1/\sqrt{5}$$:  
$$\sqrt{5}\bigl(2/\sqrt{5}+B/\sqrt{5}\bigr)=2\Rightarrow 2+B=2\Rightarrow B=0$$.  
Vậy $$X_n=(\sqrt{5})^n\cos\bigl(n\arctan\tfrac12\bigr)$$.  
(So sánh: nếu $$X_1=1$$ thì $$B=-1$$ — bài tập trong slide tiết 25.)

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1** (chu kỳ 4, $$\rho = 1$$): Giải $$a_n = -a_{n-2}$$, $$a_0 = 1$$, $$a_1 = 0$$.

Đặc trưng: $$r^2 + 1 = 0 \Rightarrow r = \pm i$$. Vậy $$\rho = 1$$, $$\theta = \pi/2$$.

$$
a_n = A\cos\frac{n\pi}{2} + B\sin\frac{n\pi}{2}.
$$

$$a_0 = 1 \Rightarrow A = 1$$; $$a_1 = 0 \Rightarrow B = 0$$. Do đó

$$
a_n = \cos\frac{n\pi}{2}.
$$

Dãy: $$1, 0, -1, 0, 1, 0, \ldots$$ — **chu kỳ 4**, khớp trực tiếp với truy hồi.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2** (biên độ phình, $$\rho > 1$$): Giải $$a_n = 2a_{n-1} - 2a_{n-2}$$, $$a_0 = 1$$, $$a_1 = 2$$.

Đặc trưng: $$r^2 - 2r + 2 = 0$$, $$\Delta = 4 - 8 = -4$$, $$r = 1 \pm i$$.

$$\rho = \sqrt{2}$$, $$\theta = \pi/4$$.

$$
a_n = (\sqrt{2})^n\Bigl(A\cos\frac{n\pi}{4} + B\sin\frac{n\pi}{4}\Bigr).
$$

$$a_0 = 1 \Rightarrow A = 1$$. Với $$a_1 = 2$$:

$$
\sqrt{2}\Bigl(A\cos\frac{\pi}{4} + B\sin\frac{\pi}{4}\Bigr) = 2
\Rightarrow A + B = 2 \Rightarrow B = 1.
$$

Vậy

$$
a_n = (\sqrt{2})^n\Bigl(\cos\frac{n\pi}{4} + \sin\frac{n\pi}{4}\Bigr).
$$

Kiểm tra: $$a_2 = 2\cdot 2 - 2\cdot 1 = 2$$; công thức cho $$n = 2$$: $$2(0 + 1) = 2$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 3** (chu kỳ 3 — căn bậc ba của đơn vị): Giải $$a_n = -a_{n-1} - a_{n-2}$$, $$a_0 = 2$$, $$a_1 = -1$$.

Đặc trưng: $$r^2 + r + 1 = 0$$, $$\Delta = -3$$,

$$
r = \frac{-1 \pm i\sqrt{3}}{2}.
$$

Đây là các căn bậc ba của đơn vị khác $$1$$: $$\rho = 1$$, $$\theta = 2\pi/3$$.

$$
a_n = A\cos\frac{2n\pi}{3} + B\sin\frac{2n\pi}{3}.
$$

$$a_0 = 2 \Rightarrow A = 2$$; thay $$a_1 = -1$$ suy ra $$B = 0$$. Do đó

$$
a_n = 2\cos\frac{2n\pi}{3}.
$$

Dãy: $$2, -1, -1, 2, -1, -1, \ldots$$ — **chu kỳ 3**.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4** (dao động tắt, $$\rho < 1$$): Giải $$a_n = a_{n-1} - \frac{1}{2} a_{n-2}$$, $$a_0 = 1$$, $$a_1 = 0$$.

Đặc trưng: $$r^2 - r + \frac{1}{2} = 0$$, $$\Delta = -1$$, $$r = \frac{1}{2} \pm i\frac{1}{2}$$.

$$\rho = \frac{\sqrt{2}}{2} < 1$$, $$\theta = \pi/4$$.

$$
a_n = \Bigl(\frac{\sqrt{2}}{2}\Bigr)^n\Bigl(A\cos\frac{n\pi}{4} + B\sin\frac{n\pi}{4}\Bigr).
$$

Từ điều kiện đầu: $$A = 1$$, $$B = -1$$. Vì $$\rho < 1$$, $$a_n \to 0$$ khi $$n \to \infty$$ (dao động **tắt dần**).

</div>

### 5.11. Bảng so sánh ba trường hợp (bậc 2)

| $$\Delta$$ | Nghiệm đặc trưng | Dạng $$a_n$$ |
|:---:|:---|:---|
| $$> 0$$ | $$r_1 \neq r_2$$ thực | $$\alpha r_1^n + \beta r_2^n$$ |
| $$= 0$$ | $$r$$ kép | $$(\alpha + \beta n)r^n$$ |
| $$< 0$$ | $$\rho e^{\pm i\theta}$$ | $$\rho^n(A\cos n\theta + B\sin n\theta)$$ |

| $$\rho = \lvert r \rvert$$ | Hành vi dãy (thành phần phức) |
|:---:|:---|
| $$\rho < 1$$ | tắt dần |
| $$\rho = 1$$ | biên độ ổn định / thường chu kỳ |
| $$\rho > 1$$ | biên độ phình |

![Tỷ lệ vàng — nghiệm của Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Golden_ratio_line.svg)

<p class="textbook-figure-caption" data-figure="10.8">Nhắc lại: Fibonacci thuộc trường hợp nghiệm **thực** phân biệt với tỷ lệ vàng $$\varphi = (1+\sqrt{5})/2$$ — đối lập với các ví dụ phức ở trên, nhưng cùng khung phương trình đặc trưng.</p>

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

### Bài tập 2b (nghiệm bội từ giáo trình)

Giải $$X_n = 2X_{n-1} - X_{n-2}$$, $$X_0=1$$, $$X_1=3$$. Vì sao không được dùng dạng $$A r_1^n + B r_2^n$$ với $$r_1=r_2=1$$?

<details>
<summary>Đáp án</summary>

Đặc trưng $$(r-1)^2=0$$. $$X_n=A+Bn$$; $$A=1$$, $$B=2$$ → $$X_n=1+2n$$.  
Dạng hai nghiệm phân biệt suy biến thành hằng $$A+B$$, mâu thuẫn $$X_0\neq X_1$$.

</details>

### Bài tập 3

Giải $$a_n = a_{n-1} + a_{n-2}$$, $$a_0 = 0$$, $$a_1 = 1$$ (Fibonacci). Viết dạng tường minh qua nghiệm đặc trưng (không cần rút gọn số).

<details>
<summary>Đáp án</summary>

$$r^2 = r + 1 \Rightarrow r = \frac{1 \pm \sqrt{5}}{2}$$. $$a_n = \alpha r_1^n + \beta r_2^n$$ với $$\alpha, \beta$$ từ $$a_0, a_1$$ (công thức Binet: $$F_n = (\varphi^n - \hat\varphi^n)/\sqrt{5}$$).

</details>

### Bài tập 4 — Số phức: chuyển dạng

Viết $$z = -1 + i\sqrt{3}$$ dưới **dạng cực** và **dạng mũ**. Tính $$\lvert z \rvert$$ và $$\operatorname{arg}(z)$$.

<details>
<summary>Đáp án</summary>

$$\rho = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1+3} = 2$$.

Vì phần thực $$a = -1 < 0$$ (góc phần tư II):

$$
\theta = \pi + \arctan\left(\frac{\sqrt{3}}{-1}\right) = \pi + \arctan(-\sqrt{3}) = \pi - \frac{\pi}{3} = \frac{2\pi}{3}.
$$

Cực: $$z = 2\bigl(\cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3}\bigr)$$.

Mũ: $$z = 2 e^{i 2\pi/3}$$.

</details>

### Bài tập 5 — De Moivre

Dùng De Moivre tính $$(1+i)^6$$.

<details>
<summary>Đáp án</summary>

$$1+i = \sqrt{2}\, e^{i\pi/4}$$, nên

$$
(1+i)^6 = (\sqrt{2})^6 e^{i 6\pi/4} = 8\, e^{i 3\pi/2} = 8\bigl(\cos\frac{3\pi}{2} + i\sin\frac{3\pi}{2}\bigr) = 8\bigl(0 + i(-1)\bigr) = -8i.
$$

</details>

### Bài tập 6 — HTTH nghiệm phức (chu kỳ)

Giải $$a_n = -a_{n-2}$$, $$a_0 = 0$$, $$a_1 = 1$$. Viết dạng $$\rho^n(A\cos n\theta + B\sin n\theta)$$ và sáu số hạng đầu.

<details>
<summary>Đáp án</summary>

$$r^2 + 1 = 0 \Rightarrow r = \pm i$$, $$\rho = 1$$, $$\theta = \pi/2$$.

$$a_n = A\cos\frac{n\pi}{2} + B\sin\frac{n\pi}{2}$$.

$$a_0 = 0 \Rightarrow A = 0$$; $$a_1 = 1 \Rightarrow B = 1$$. Vậy $$a_n = \sin\frac{n\pi}{2}$$.

Dãy: $$0, 1, 0, -1, 0, 1, \ldots$$ (chu kỳ 4).

</details>

### Bài tập 7 — HTTH nghiệm phức (phình)

Giải $$a_n = 2a_{n-1} - 2a_{n-2}$$, $$a_0 = 1$$, $$a_1 = 2$$. Tìm $$\rho$$, $$\theta$$ và công thức đóng.

<details>
<summary>Đáp án</summary>

$$r = 1 \pm i$$, $$\rho = \sqrt{2}$$, $$\theta = \pi/4$$.

$$a_n = (\sqrt{2})^n\bigl(\cos\frac{n\pi}{4} + \sin\frac{n\pi}{4}\bigr)$$
(đã tính $$A = 1$$, $$B = 1$$ trong Ví dụ 2).

</details>

### Bài tập 8 (thách thức) — Dao động tắt

Với $$a_n = a_{n-1} - \frac{1}{2} a_{n-2}$$, $$a_0 = 1$$, $$a_1 = 0$$ (Ví dụ 4): giải thích vì sao $$a_n \to 0$$ và ước lượng cận thô cho $$\lvert a_{10} \rvert$$.

<details>
<summary>Đáp án</summary>

$$\rho = \frac{\sqrt{2}}{2} \approx 0.707 < 1$$ nên nhân tử $$\rho^n \to 0$$.

$$\lvert a_n \rvert \le \left(\frac{\sqrt{2}}{2}\right)^n \cdot \sqrt{2}$$
(vì $$\lvert \cos\theta - \sin\theta \rvert \le \sqrt{2}$$).

$$\lvert a_{10} \rvert \le 2^{-5}\sqrt{2} = \frac{\sqrt{2}}{32} \approx 0.044$$.

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=T647CGsuOVU">Complex numbers: Introduction</a> — 3Blue1Brown (trực giác mặt phẳng phức)
- <a href="https://www.youtube.com/watch?v=fReOvGlhIDw">e^(iπ) in 3.14 minutes</a> — Mathologer (Euler / De Moivre)
- <a href="https://www.youtube.com/watch?v=uhxtUt_-GyM">Solving Linear Recurrence Relations</a> — Trefor Bazett

## Tóm tắt

- Quan hệ truy hồi tuyến tính thuần nhất bậc $$k$$: $$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k}$$.
- Giả sử nghiệm dạng $$r^n$$ dẫn tới **phương trình đặc trưng** bậc $$k$$.
- Nghiệm phân biệt $$r_1, r_2$$: $$a_n = \alpha r_1^n + \beta r_2^n$$; nghiệm kép: $$a_n = (\alpha + \beta n)r^n$$.
- **Số phức**: $$z = a + bi$$; biểu diễn **đại số / Argand / cực** $$z = \rho e^{i\theta}$$; **De Moivre** $$z^n = \rho^n(\cos n\theta + i\sin n\theta)$$.
- Nghiệm phức liên hợp (hệ số thực) cho dạng $$a_n = \rho^n(A\cos n\theta + B\sin n\theta)$$; hành vi theo $$\rho < 1$$, $$\rho = 1$$ hoặc $$\rho > 1$$.
- Bậc cao hơn: mỗi nghiệm đóng góp hạng $$r_i^n$$ (và nhân tử đa thức nếu nghiệm bội).

Trong bài tiếp theo, chúng ta mở rộng sang **quan hệ truy hồi không thuần nhất** — khi có thêm thành phần $$f(n)$$ bên ngoài.
