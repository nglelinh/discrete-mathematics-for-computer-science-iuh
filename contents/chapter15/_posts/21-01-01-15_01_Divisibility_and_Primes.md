---
layout: post
title: "Tính chia hết và Số nguyên tố"
categories: chapter15
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Định lý chia, số nguyên tố, định lý cơ bản số học, sàng Eratosthenes, GCD và thuật toán Euclid — nền cho đồng dư và mật mã."
---

<div class="textbook-epigraph" markdown="1">

"Mathematics is the queen of the sciences and number theory is the queen of mathematics."

<span class="epigraph-attribution">— Carl Friedrich Gauss</span>

</div>

**Lý thuyết số** nghiên cứu tính chất của số nguyên: chia hết, số nguyên tố, ước chung. Trong khoa học máy tính, các cấu trúc này xuất hiện khi sinh khóa, kiểm tra modulo, phân tích thừa số và nhiều giao thức bảo mật. Mục này đặt nền: định lý chia, số nguyên tố, định lý cơ bản, GCD và thuật toán Euclid.

![Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid.jpg)

<p class="textbook-figure-caption" data-figure="15.1">Euclid (~300 TCN) — thuật toán GCD và chứng minh vô hạn số nguyên tố.</p>

![Phân tích thừa số nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/PrimeDecompositionExample.svg)

<p class="textbook-figure-caption" data-figure="15.2">Định lý cơ bản: mọi số nguyên $$n>1$$ phân tích duy nhất (không kể thứ tự) thành tích lũy thừa nguyên tố.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** định lý chia: $$a = dq + r$$ với $$0 \le r < d$$.
- **Phân biệt** số nguyên tố và hợp số; nêu định lý cơ bản số học.
- **Tính** $$\gcd(a,b)$$ bằng thuật toán Euclid và nêu đồng nhất thức Bézout.
- **Mô tả** sàng Eratosthenes và độ phức tạp $$O(n\log\log n)$$.
- **Liên hệ** GCD / Euclid với nghịch đảo modulo và mật mã (các mục sau).

**Từ khóa**: chia hết (divisibility), số nguyên tố (prime), GCD, thuật toán Euclid, định lý cơ bản số học, Bézout.

</div>

## 1. Tính chia hết

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho $$a, b \in \mathbb{Z}$$ với $$b \neq 0$$. Ta nói $$b$$ **chia hết** $$a$$, ký hiệu $$b \mid a$$, nếu tồn tại $$c \in \mathbb{Z}$$ sao cho $$a = bc$$. Nếu không, viết $$b \nmid a$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.**

- $$3 \mid 12$$ vì $$12 = 3 \cdot 4$$.
- $$7 \nmid 20$$.
- $$1 \mid n$$ với mọi $$n$$; $$n \mid 0$$ với mọi $$n \neq 0$$.

</div>

### Định lý chia

<div class="textbook-theorem" markdown="1">

**Định lý** (Division algorithm). Cho $$a \in \mathbb{Z}$$ và $$d \in \mathbb{Z}^+$$. Tồn tại **duy nhất** cặp số nguyên $$q$$ (thương) và $$r$$ (số dư) sao cho

$$
a = dq + r, \qquad 0 \le r < d.
$$

Ký hiệu thường dùng: $$a \operatorname{div} d = q$$, $$a \bmod d = r$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.**

- $$a = 17$$, $$d = 5$$: $$17 = 5 \cdot 3 + 2$$ → $$q=3$$, $$r=2$$.
- $$a = -17$$, $$d = 5$$: $$-17 = 5 \cdot (-4) + 3$$ → $$q=-4$$, $$r=3$$ (số dư **không âm**).

Trong Python, `(-17) % 5` bằng $$3$$ — khớp định nghĩa toán. Một số ngôn ngữ (C/C++ với chia hướng 0) có thể cho số dư âm; khi cài đặt cần thống nhất quy ước.

</div>

## 2. Số nguyên tố

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Số nguyên $$p > 1$$ là **số nguyên tố** (*prime*) nếu các ước dương duy nhất của nó là $$1$$ và $$p$$. Số $$n > 1$$ không nguyên tố gọi là **hợp số** (*composite*). Số $$1$$ **không** là nguyên tố cũng **không** là hợp số.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Nguyên tố: $$2,3,5,7,11,\ldots$$. Hợp số: $$4,6,8,9,10,\ldots$$. Số chẵn duy nhất nguyên tố là $$2$$.

</div>

### Định lý cơ bản của số học

<div class="textbook-theorem" markdown="1">

**Định lý** (Fundamental theorem of arithmetic). Mọi số nguyên $$n > 1$$ biểu diễn **duy nhất** (không kể thứ tự nhân tử) dưới dạng

$$
n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k},
$$

với $$p_1 < p_2 < \cdots < p_k$$ nguyên tố và $$e_i \ge 1$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4.** $$60 = 2^2 \cdot 3 \cdot 5$$; $$84 = 2^2 \cdot 3 \cdot 7$$; $$1001 = 7 \cdot 11 \cdot 13$$.

</div>

Tính duy nhất là lý do gọi số nguyên tố là “nguyên tử” của số học: mọi $$n>1$$ có “công thức” thừa số cố định. Nhiều cấu trúc đại số khác **không** có tính duy nhất tương tự.

### Sàng Eratosthenes

Tìm mọi số nguyên tố $$\le n$$:

```text
Sàng-Eratosthenes(n)
1. Đánh dấu mọi k ∈ {2..n} là “ứng viên”
2. FOR i ← 2 TO ⌊√n⌋ DO
3.     IF i còn là ứng viên THEN
4.         FOR j ← i², i²+i, i²+2i, … (≤ n) DO
5.             loại j khỏi ứng viên
6. RETURN các ứng viên còn lại
```

Bắt đầu gạch từ $$i^2$$ vì các bội $$2i,\ldots,(i-1)i$$ đã bị gạch bởi các số nguyên tố nhỏ hơn $$i$$. Độ phức tạp thời gian cổ điển là $$O(n \log\log n)$$.

## 3. Ước chung lớn nhất (GCD)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho $$a, b \in \mathbb{Z}$$ không đồng thời bằng 0. **Ước chung lớn nhất** $$\gcd(a,b)$$ là số nguyên dương lớn nhất $$d$$ sao cho $$d \mid a$$ và $$d \mid b$$. Nếu $$\gcd(a,b)=1$$, ta nói $$a$$ và $$b$$ **nguyên tố cùng nhau** (*coprime*, *relatively prime*).

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 5.** $$\gcd(12,18)=6$$; $$\gcd(17,23)=1$$; $$\gcd(0,5)=5$$. Cặp $$(0,0)$$ không định nghĩa GCD theo quy ước trên.

</div>

### Thuật toán Euclid

<div class="textbook-theorem" markdown="1">

**Định lý** (Euclid). Với $$b > 0$$,

$$
\gcd(a,b) = \gcd(b,\, a \bmod b).
$$

Lặp đến khi số dư bằng 0; GCD là số còn lại khác 0.

</div>

![Euclid từng bước](/discrete-mathematics-for-computer-science-iuh/img/course/Number_euclid_steps.svg)

<p class="textbook-figure-caption" data-figure="15.3">Các bước Euclid cho $$\gcd(252,105)=21$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 6.** $$\gcd(252,105)$$:

| Bước | $$a$$ | $$b$$ | $$a \bmod b$$ |
|:---:|:---:|:---:|:---:|
| 1 | 252 | 105 | 42 |
| 2 | 105 | 42 | 21 |
| 3 | 42 | 21 | 0 |

Kết quả: $$\gcd = 21$$.

</div>

Số bước thuộc $$O(\log \min(|a|,|b|))$$ — đủ nhanh cho số hàng nghìn bit trong thư viện mật mã.

### Đồng nhất thức Bézout

<div class="textbook-theorem" markdown="1">

**Định lý** (Bézout). Tồn tại $$s,t \in \mathbb{Z}$$ sao cho

$$
\gcd(a,b) = sa + tb.
$$

</div>

Thuật toán **Euclid mở rộng** tính đồng thời $$s,t$$ và GCD — công cụ then chốt để tìm **nghịch đảo modulo** khi $$\gcd(a,n)=1$$ (Mục 15.2) và bước tạo khóa RSA (Mục 15.3).

## 4. Thử nghiệm tương tác

Máy tính modulo cơ bản và thuật toán Euclid từng bước (kèm hệ số Bézout):

<div class="interactive-demo" markdown="1">
<div data-demo="modular-calculator"></div>
</div>
<script src="{{ '/public/js/modular-calculator.js' | relative_url }}"></script>

<div class="interactive-demo" markdown="1">
<div data-demo="euclidean-algorithm"></div>
</div>
<script src="{{ '/public/js/euclidean-algorithm.js' | relative_url }}"></script>

## 5. Liên hệ khoa học máy tính

- **RSA / Diffie–Hellman**: cần số nguyên tố lớn, GCD, Euclid mở rộng.
- **Checksum / ISBN**: tổ hợp tuyến tính modulo $$m$$.
- **HTTPS**: trình duyệt thực hiện hàng loạt phép modulo và Euclid khi bắt tay TLS — các phép thuộc lớp thuật toán của mục này và mục 15.2–15.3.

## Bài tập

### Bài tập 1

Tìm thương $$q$$ và số dư $$r$$ của $$a = -45$$ chia cho $$d = 7$$.

<details>
<summary>Đáp án</summary>

Cần $$-45 = 7q + r$$ với $$0 \le r < 7$$. Thử $$q = -7$$: $$7\cdot(-7) = -49$$, $$-45 - (-49) = 4$$. Vậy $$q=-7$$, $$r=4$$.

</details>

### Bài tập 2

Dùng sàng Eratosthenes, liệt kê mọi số nguyên tố $$\le 30$$.

<details>
<summary>Đáp án</summary>

$$2,3,5,7,11,13,17,19,23,29$$.

</details>

### Bài tập 3

Tính $$\gcd(12345, 54321)$$ bằng Euclid (ghi vài bước chính).

<details>
<summary>Đáp án</summary>

$$54321 = 4\cdot 12345 + 4941$$,  
$$12345 = 2\cdot 4941 + 2463$$,  
$$4941 = 2\cdot 2463 + 15$$,  
$$2463 = 164\cdot 15 + 3$$,  
$$15 = 5\cdot 3 + 0$$.  
$$\gcd = 3$$.

</details>

### Bài tập 4

Phân tích $$360$$ và $$504$$ ra thừa số nguyên tố.

<details>
<summary>Đáp án</summary>

$$360 = 2^3 \cdot 3^2 \cdot 5$$,  
$$504 = 2^3 \cdot 3^2 \cdot 7$$.

</details>

### Bài tập 5

Chứng minh có vô hạn số nguyên tố (định lý Euclid).

<details>
<summary>Đáp án</summary>

Giả sử chỉ có hữu hạn số nguyên tố $$p_1,\ldots,p_k$$. Đặt

$$
N = p_1 p_2 \cdots p_k + 1.
$$

Thì $$N > 1$$ nên $$N$$ có ước nguyên tố $$p$$. Nếu $$p = p_i$$ thì $$p \mid N$$ và $$p \mid p_1\cdots p_k$$, suy ra $$p \mid 1$$ — vô lý. Vậy giả sử sai: có vô hạn số nguyên tố.

</details>

## Tóm tắt

1. **Chia hết** $$b\mid a$$ và **định lý chia** với $$0\le r < d$$.
2. **Nguyên tố / hợp số**; **định lý cơ bản** — phân tích duy nhất.
3. **Sàng Eratosthenes** liệt kê nguyên tố $$\le n$$.
4. **GCD** qua Euclid; **Bézout** mở đường cho nghịch đảo modulo.

Trong bài tiếp theo: **đồng dư**, phép toán modulo, nghịch đảo, CRT và lũy thừa modulo nhanh.
