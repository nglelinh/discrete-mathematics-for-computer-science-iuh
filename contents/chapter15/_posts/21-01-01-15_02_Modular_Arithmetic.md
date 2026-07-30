---
layout: post
title: "Số học Modulo và Đồng dư"
categories: chapter15
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Đồng dư a ≡ b (mod n), phép toán modulo, phương trình tuyến tính, nghịch đảo và Euclid mở rộng, CRT, lũy thừa modulo nhanh, Fermat và Euler."
---

<div class="textbook-epigraph" markdown="1">

"Disquisitiones Arithmeticae made congruence the everyday language of number theory."

<span class="epigraph-attribution">— Tinh thần Gauss (1801)</span>

</div>

Ở mục trước đã có định lý chia, GCD và Euclid. **Số học modulo** chỉ giữ lại số dư khi chia cho modulus cố định $$n$$. Khung này là công cụ trung tâm của RSA, hàm băm, sinh số giả ngẫu nhiên và nhiều thuật toán bảo mật.

![Đồng dư modulo](/discrete-mathematics-for-computer-science-iuh/img/course/Number_congruence_clock.svg)

<p class="textbook-figure-caption" data-figure="15.4">Đồng dư modulo $$n$$: hai số cùng số dư khi chia cho $$n$$ — hình ảnh “đồng hồ số học”.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** $$a \equiv b \pmod n$$ và thực hiện cộng, trừ, nhân modulo $$n$$.
- **Giải** $$ax \equiv b \pmod n$$ khi điều kiện GCD thỏa.
- **Tính** nghịch đảo modulo bằng Euclid mở rộng.
- **Áp dụng** Định lý số dư Trung Hoa (CRT) cho hệ đồng dư.
- **Tính** $$b^e \bmod n$$ bằng lũy thừa modulo nhanh; nêu Fermat / Euler.

**Từ khóa**: đồng dư (congruence), modulo, nghịch đảo modulo, CRT, lũy thừa modulo, định lý Fermat nhỏ, định lý Euler.

</div>

## 1. Đồng dư

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho $$a,b \in \mathbb{Z}$$ và $$n \in \mathbb{Z}^+$$. Ta nói $$a$$ **đồng dư** với $$b$$ modulo $$n$$, ký hiệu

$$
a \equiv b \pmod n,
$$

khi và chỉ khi $$n \mid (a-b)$$ — tức $$a$$ và $$b$$ có cùng số dư khi chia cho $$n$$.

</div>

Đồng dư theo modulus cố định là quan hệ **tương đương** trên $$\mathbb{Z}$$. Các lớp tương đương là

$$
[0],[1],\ldots,[n-1]
$$

(với $$[r] = \{ \ldots, r-n, r, r+n, \ldots \}$$).

<div class="textbook-theorem" markdown="1">

**Định lý** (tương thích phép toán). Nếu $$a \equiv b \pmod n$$ và $$c \equiv d \pmod n$$ thì

$$
a+c \equiv b+d, \qquad a-c \equiv b-d, \qquad ac \equiv bd \pmod n.
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** $$15 \equiv 3 \pmod{12}$$ vì $$15-3=12$$.  
$$(47 \cdot 93) \bmod 13$$: $$47 \equiv 8$$, $$93 \equiv 2 \pmod{13}$$ nên $$47\cdot 93 \equiv 8\cdot 2 = 16 \equiv 3 \pmod{13}$$.

</div>

## 2. Phương trình đồng dư tuyến tính

Bài toán: tìm $$x$$ thỏa $$ax \equiv b \pmod n$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** Đặt $$d = \gcd(a,n)$$. Phương trình $$ax \equiv b \pmod n$$ có nghiệm khi và chỉ khi $$d \mid b$$. Khi đó có đúng $$d$$ nghiệm không đồng dư modulo $$n$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Giải $$6x \equiv 3 \pmod 9$$.

$$\gcd(6,9)=3$$ và $$3\mid 3$$ → có 3 nghiệm. Chia phương trình cho 3 (modulus chia cho 3):

$$
2x \equiv 1 \pmod 3.
$$

Nhân với nghịch đảo của 2 modulo 3 (là 2, vì $$2\cdot 2=4\equiv 1$$): $$x \equiv 2 \pmod 3$$.  
Các nghiệm modulo 9: $$x \equiv 2,5,8 \pmod 9$$.

</div>

## 3. Nghịch đảo modulo

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Nghịch đảo modulo** của $$a$$ modulo $$n$$ là số $$\bar a$$ sao cho

$$
a \cdot \bar a \equiv 1 \pmod n.
$$

Nghịch đảo tồn tại khi và chỉ khi $$\gcd(a,n)=1$$. Ký hiệu thường gặp: $$a^{-1} \bmod n$$.

</div>

### Euclid mở rộng

Từ Bézout: nếu $$\gcd(a,n)=1$$ thì tồn tại $$s,t$$ với $$sa + tn = 1$$, suy ra $$s \equiv a^{-1} \pmod n$$.

```text
Euclid-Mở-rộng(a, n)   // giả sử gcd(a,n)=1
old_r, r ← a, n
old_s, s ← 1, 0
WHILE r ≠ 0 DO
    q ← old_r DIV r
    (old_r, r) ← (r, old_r − q·r)
    (old_s, s) ← (s, old_s − q·s)
RETURN old_s MOD n   // đưa về {0..n−1}
```

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Nghịch đảo của $$7$$ modulo $$26$$: Euclid mở rộng cho $$-11$$, và $$-11 \bmod 26 = 15$$. Kiểm tra: $$7\cdot 15 = 105 = 4\cdot 26 + 1 \equiv 1 \pmod{26}$$.

</div>

## 4. Định lý số dư Trung Hoa (CRT)

<div class="textbook-theorem" markdown="1">

**Định lý** (Chinese Remainder Theorem). Cho $$n_1,\ldots,n_k$$ đôi một nguyên tố cùng nhau. Hệ

$$
x \equiv a_i \pmod{n_i}, \quad i=1,\ldots,k
$$

có nghiệm duy nhất modulo $$N = n_1 n_2 \cdots n_k$$.

Công thức: $$x = \sum_{i=1}^{k} a_i N_i y_i$$ với $$N_i = N/n_i$$ và $$y_i = N_i^{-1} \bmod n_i$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4** (bài toán Tôn Tử). Giải

$$
x \equiv 2 \pmod 3,\quad
x \equiv 3 \pmod 5,\quad
x \equiv 2 \pmod 7.
$$

$$N=105$$; $$N_1=35$$, $$y_1=2$$; $$N_2=21$$, $$y_2=1$$; $$N_3=15$$, $$y_3=1$$.

$$
x = 2\cdot 35\cdot 2 + 3\cdot 21\cdot 1 + 2\cdot 15\cdot 1 = 233 \equiv 23 \pmod{105}.
$$

Kiểm tra: $$23 \bmod 3=2$$, $$23 \bmod 5=3$$, $$23 \bmod 7=2$$.

</div>

## 5. Lũy thừa modulo nhanh

Tính $$b^e \bmod n$$ với $$e$$ lớn (hàng trăm–nghìn bit trong RSA):

```text
ModExp(b, e, n)
result ← 1; base ← b MOD n
WHILE e > 0 DO
    IF e lẻ THEN result ← (result · base) MOD n
    base ← (base · base) MOD n
    e ← e DIV 2
RETURN result
```

Độ phức tạp $$O(\log e)$$ phép nhân modulo — thay vì $$O(e)$$ nhân tuần tự.

<div class="textbook-example" markdown="1">

**Ví dụ 5.** $$3^{13} \bmod 7$$. $$13 = 1101_2$$. Theo từng bit (LSB trước): kết quả $$3$$. Kiểm tra: $$3^{13} = 1594323 = 7\cdot 227760 + 3$$.

</div>

## 6. Định lý Fermat nhỏ và Euler

<div class="textbook-theorem" markdown="1">

**Định lý** (Fermat nhỏ). Nếu $$p$$ nguyên tố và $$p \nmid a$$ thì

$$
a^{p-1} \equiv 1 \pmod p.
$$

Tương đương: $$a^p \equiv a \pmod p$$ với mọi $$a$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Euler). Nếu $$\gcd(a,n)=1$$ thì

$$
a^{\varphi(n)} \equiv 1 \pmod n,
$$

trong đó $$\varphi$$ là **hàm Euler totient** (số các số trong $$\{1,\ldots,n-1\}$$ nguyên tố cùng nhau với $$n$$). Khi $$n=p$$ nguyên tố, $$\varphi(p)=p-1$$ — khôi phục Fermat.

</div>

Hai định lý này là nền **tính đúng RSA**: nếu $$ed \equiv 1 \pmod{\varphi(n)}$$ thì $$M^{ed} \equiv M \pmod n$$ trong các điều kiện chuẩn (Mục 15.3).

## 7. Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="modular-arithmetic-calc"></div>
</div>
<script src="{{ '/public/js/modular-arithmetic-calc.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Tính $$(47 \times 93) \bmod 13$$ bằng rút gọn modulo.

<details>
<summary>Đáp án</summary>

$$47\equiv 8$$, $$93\equiv 2 \pmod{13}$$ → $$8\cdot 2=16\equiv 3 \pmod{13}$$.

</details>

### Bài tập 2

Giải $$4x \equiv 5 \pmod 9$$.

<details>
<summary>Đáp án</summary>

$$\gcd(4,9)=1\mid 5$$. Nghịch đảo của 4 modulo 9: $$4\cdot 7=28\equiv 1$$ nên $$4^{-1}\equiv 7$$.  
$$x \equiv 5\cdot 7 = 35 \equiv 8 \pmod 9$$.

</details>

### Bài tập 3

Tìm nghịch đảo của 11 modulo 26.

<details>
<summary>Đáp án</summary>

$$\gcd(11,26)=1$$. Euclid mở rộng: $$11\cdot 19 = 209 = 8\cdot 26 + 1$$ → $$11^{-1}\equiv 19 \pmod{26}$$.

</details>

### Bài tập 4

CRT: $$x\equiv 1\pmod 3$$, $$x\equiv 2\pmod 5$$, $$x\equiv 3\pmod 7$$.

<details>
<summary>Đáp án</summary>

$$N=105$$. Công thức CRT cho $$x \equiv 52 \pmod{105}$$ (kiểm tra: $$52\bmod 3=1$$, $$52\bmod 5=2$$, $$52\bmod 7=3$$).

</details>

### Bài tập 5

Với số mũ 2048 bit, lũy thừa modulo nhanh cần cỡ bao nhiêu phép nhân modulo? So với nhân tuần tự?

<details>
<summary>Đáp án</summary>

Khoảng $$2048$$ vòng; mỗi vòng $$\le 2$$ nhân modulo → cỡ vài nghìn phép. Nhân tuần tự cần $$\Theta(2^{2048})$$ — không khả thi.

</details>

## Tóm tắt

1. $$a\equiv b\pmod n \iff n\mid(a-b)$$; cộng/trừ/nhân tương thích.
2. $$ax\equiv b\pmod n$$ có nghiệm $$\iff \gcd(a,n)\mid b$$.
3. Nghịch đảo tồn tại $$\iff \gcd(a,n)=1$$ — Euclid mở rộng.
4. **CRT** ghép hệ đồng dư modulus nguyên tố cùng nhau.
5. **ModExp** $$O(\log e)$$; **Fermat / Euler** nền RSA.

Trong bài tiếp theo: mật mã cổ điển, **RSA** và **Diffie–Hellman**.
