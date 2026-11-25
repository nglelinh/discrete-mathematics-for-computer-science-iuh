---
layout: post
title: "Số học Modulo và Đồng dư"
categories: chapter15
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Đồng dư a ≡ b (mod n), phép toán modulo, phương trình đồng dư tuyến tính, nghịch đảo modulo và Euclid mở rộng, CRT, lũy thừa modulo nhanh, Fermat và Euler."
---

> **Câu chuyện mở đầu:** Nếu bây giờ là 10 giờ tối và 5 tiếng nữa chuông báo thức kêu, bạn không trả lời "15 giờ" — bạn lập tức trả lời **3 giờ sáng**! Bạn vừa thực hiện phép tính $$10 + 5 \equiv 3 \pmod{12}$$ trong **số học đồng hồ (số học modulo)** mà Carl Friedrich Gauss đã hệ thống hóa thành một đại số hoàn chỉnh năm 1801. Từ tìm nghịch đảo modulo, Định lý Fermat nhỏ cho đến **Định lý Số dư Trung Hoa (CRT)** — đây chính là bộ động cơ số học của mật mã học và tính toán phân tán!

<div class="textbook-epigraph" markdown="1">

"Disquisitiones Arithmeticae made congruence the everyday language of number theory."

<span class="epigraph-attribution">— Tinh thần Gauss (1801)</span>

</div>

Ở bài trước, ta đã làm quen với định lý chia, ước chung lớn nhất và thuật toán Euclid. **Số học modulo** tập trung vào phần dư khi chia cho một số nguyên dương cố định gọi là *modulus* $$n$$. Đây là công cụ cốt lõi trong hệ mật RSA, hàm băm, bộ sinh số giả ngẫu nhiên và nhiều thuật toán bảo mật.

![Đồng dư modulo](/discrete-mathematics-for-computer-science-iuh/img/course/Number_congruence_clock.svg)

<p class="textbook-figure-caption" data-figure="15.4">Đồng dư modulo $$n$$: hai số có cùng số dư khi chia cho $$n$$ — hình ảnh “đồng hồ số học”.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** quan hệ $$a \equiv b \pmod n$$ và thực hiện các phép cộng, trừ, nhân theo modulo $$n$$.
- **Giải** phương trình đồng dư tuyến tính $$ax \equiv b \pmod n$$ khi điều kiện GCD thỏa mãn.
- **Tính** nghịch đảo modulo bằng thuật toán Euclid mở rộng.
- **Áp dụng** Định lý số dư Trung Hoa (CRT) để giải hệ đồng dư.
- **Tính** $$b^e \bmod n$$ bằng lũy thừa modulo nhanh, đồng thời phát biểu định lý Fermat nhỏ và định lý Euler.

**Từ khóa**: đồng dư (congruence), modulo, nghịch đảo modulo, CRT, lũy thừa modulo, định lý Fermat nhỏ, định lý Euler.

</div>

## Bản đồ kiến thức nền: Số học Modulo và ba Định lý Trụ cột

### 1. Vành $$\mathbb{Z}_m$$ & Nghịch đảo Modulo
- **Bản chất:** $$a \equiv b \pmod m$$ nghĩa là $$m \mid (a - b)$$. Ta cộng, trừ, nhân tự do theo modulo $$m$$, nhưng **phép chia chỉ tồn tại khi $$\gcd(a, m) = 1$$**: khi đó tồn tại duy nhất nghịch đảo $$a^{-1} \bmod m$$ tìm bằng Thuật toán Euclid mở rộng!

### 2. Định lý Fermat nhỏ & Định lý Euler
- **Fermat nhỏ:** Với $$p$$ nguyên tố và $$p \nmid a$$: $$a^{p-1} \equiv 1 \pmod p$$.
- **Euler tổng quát:** Với $$\gcd(a, n) = 1$$: $$a^{\varphi(n)} \equiv 1 \pmod n$$ — nền tảng trực tiếp chứng minh bước giải mã của RSA!

### 3. Định lý Số dư Trung Hoa (CRT)
- **Bản chất:** Nếu $$m_1, \dots, m_k$$ đôi một nguyên tố cùng nhau, hệ đồng dư $$x \equiv a_i \pmod{m_i}$$ luôn có **nghiệm duy nhất** theo modulo $$M = m_1\cdots m_k$$ — cho phép tách phép tính trên số khổng lồ thành nhiều phép tính song song trên các modulo nhỏ!

## Ví dụ tính tay cầm tay chỉ việc

### Ví dụ 1: Tìm nghịch đảo $$7^{-1} \pmod{26}$$ bằng Euclid mở rộng
Ta cần giải $$7x + 26y = 1$$:
- $$26 = 3 \cdot 7 + 5$$
- $$7 = 1 \cdot 5 + 2$$
- $$5 = 2 \cdot 2 + 1 \implies 1 = 5 - 2\cdot 2 = 5 - 2(7 - 5) = 3\cdot 5 - 2\cdot 7 = 3(26 - 3\cdot 7) - 2\cdot 7 = 3\cdot 26 - 11\cdot 7$$.
Vậy $$7 \cdot (-11) \equiv 1 \pmod{26}$$. Cộng $$26$$ để lấy đại diện dương: $$-11 + 26 = 15$$!
**Kiểm tra:** $$7 \times 15 = 105 = 4 \times 26 + 1 \equiv 1 \pmod{26}$$! ✓

### Ví dụ 2: Giải hệ Định lý Số dư Trung Hoa cổ điển của Tôn Tử
Tìm $$x$$ thỏa: $$x \equiv 2 \pmod 3,\; x \equiv 3 \pmod 5,\; x \equiv 2 \pmod 7$$.
- $$M = 3\cdot 5\cdot 7 = 105$$; các tích phụ: $$M_1 = 35,\; M_2 = 21,\; M_3 = 15$$.
- Tìm nghịch đảo từng tích phụ:
  - $$35 y_1 \equiv 2 y_1 \equiv 1 \pmod 3 \implies y_1 = 2$$.
  - $$21 y_2 \equiv 1 y_2 \equiv 1 \pmod 5 \implies y_2 = 1$$.
  - $$15 y_3 \equiv 1 y_3 \equiv 1 \pmod 7 \implies y_3 = 1$$.
- Công thức CRT: $$x \equiv 2(35)(2) + 3(21)(1) + 2(15)(1) = 140 + 63 + 30 = 233 \equiv 23 \pmod{105}$$!
**Kiểm tra:** $$23 = 7\cdot 3 + 2$$, $$23 = 4\cdot 5 + 3$$, $$23 = 3\cdot 7 + 2$$ — khớp cả 3 phương trình! ✓

### Khung giải thích: 4 bước tính nhanh mọi bài toán Số học Modulo (nên đọc chậm)

#### Bước 1: Luôn rút gọn số dư trước khi nhân hay lũy thừa
Không bao giờ tính $$237^{100}$$ rồi mới chia! Thay cơ số bằng số dư nhỏ nhất và dùng **lũy thừa nhị phân (binary exponentiation)** chỉ tốn $$O(\log e)$$ phép nhân!

#### Bước 2: Dùng Fermat / Euler để hạ số mũ khổng lồ
Muốn tính $$a^k \bmod p$$, chỉ cần lấy số mũ theo modulo $$(p-1)$$ trước!

#### Bước 3: Kiểm tra $$\gcd(a, m)$$ trước khi giải $$ax \equiv b \pmod m$$
Nếu $$d = \gcd(a, m)$$ không chia hết $$b$$ thì vô nghiệm ngay lập tức; nếu $$d \mid b$$ thì chia cả 3 số $$a, b, m$$ cho $$d$$ rồi nhân với nghịch đảo!

#### Bước 4: Dùng CRT để tăng tốc giải mã RSA gấp 4 lần
Trong thực tế, thay vì tính $$C^d \bmod (pq)$$, thư viện OpenSSL tính riêng $$C^d \bmod p$$ và $$C^d \bmod q$$ rồi ghép bằng CRT!

$$
\text{Đồng dư }a \equiv b \pmod m
\;\xrightarrow{\;\text{Euclid mở rộng}\;}\;
a^{-1} \bmod m
\;\xrightarrow{\;\text{Euler + CRT}\;}\;
\text{RSA \& Tính toán song song}.
$$

## Đồng dư

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho $$a,b \in \mathbb{Z}$$ và $$n \in \mathbb{Z}^+$$. Ta nói $$a$$ **đồng dư** với $$b$$ modulo $$n$$, ký hiệu

$$
a \equiv b \pmod n,
$$

khi và chỉ khi $$n \mid (a-b)$$, tức là $$a$$ và $$b$$ có cùng số dư khi chia cho $$n$$.

</div>

Với một modulus $$n$$ cố định, quan hệ đồng dư là một **quan hệ tương đương** trên $$\mathbb{Z}$$. Các lớp tương đương tương ứng là

$$
[0],[1],\ldots,[n-1]
$$

trong đó $$[r] = \{ \ldots, r-n, r, r+n, \ldots \}$$.

<div class="textbook-theorem" markdown="1">

**Định lý** (Tính tương thích với phép toán). Nếu $$a \equiv b \pmod n$$ và $$c \equiv d \pmod n$$ thì

$$
a+c \equiv b+d, \qquad a-c \equiv b-d, \qquad ac \equiv bd \pmod n.
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** $$15 \equiv 3 \pmod{12}$$ vì $$15-3=12$$ chia hết cho $$12$$.  
Để tính $$(47 \cdot 93) \bmod 13$$, ta rút gọn từng thừa số: $$47 \equiv 8 \pmod{13}$$ và $$93 \equiv 2 \pmod{13}$$, suy ra $$47\cdot 93 \equiv 8\cdot 2 = 16 \equiv 3 \pmod{13}$$.

</div>

## Phương trình đồng dư tuyến tính

Xét bài toán tìm số nguyên $$x$$ thỏa mãn $$ax \equiv b \pmod n$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** Đặt $$d = \gcd(a,n)$$. Phương trình $$ax \equiv b \pmod n$$ có nghiệm khi và chỉ khi $$d \mid b$$. Khi có nghiệm, phương trình có đúng $$d$$ nghiệm không đồng dư với nhau theo modulo $$n$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Giải phương trình $$6x \equiv 3 \pmod 9$$.

Ta có $$\gcd(6,9)=3$$ và $$3\mid 3$$, nên phương trình có 3 nghiệm modulo 9. Chia cả hai vế và modulus cho 3, ta được:

$$
2x \equiv 1 \pmod 3.
$$

Nhân hai vế với nghịch đảo của 2 modulo 3 (là 2, vì $$2\cdot 2=4\equiv 1 \pmod 3$$), ta thu được $$x \equiv 2 \pmod 3$$.  
Từ đó, các nghiệm theo modulo 9 là $$x \equiv 2,5,8 \pmod 9$$.

</div>

### Video ngắn: Bảng cửu chương theo modulo

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/modular-times-table.mp4"></video>
</div>

Đặt $$n=100$$ điểm cách đều nhau trên một đường tròn và nối mỗi điểm $$i$$ với điểm $$k\cdot i \bmod n$$. Khi $$k$$ tăng lên, các dây cung tạo thành những đường bao đặc trưng: $$k=2$$ cho hình tim (cardioid), $$k=3$$ cho nephroid, và tổng quát đường bao có $$k-1$$ điểm nhọn. Đây là cách biểu diễn hình học cho phép nhân trong $$\mathbb{Z}_n$$.

## Nghịch đảo modulo

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Nghịch đảo modulo** của $$a$$ theo modulo $$n$$ là số nguyên $$\bar a$$ thỏa mãn

$$
a \cdot \bar a \equiv 1 \pmod n.
$$

Nghịch đảo tồn tại khi và chỉ khi $$\gcd(a,n)=1$$, thường ký hiệu là $$a^{-1} \bmod n$$.

</div>

### Thuật toán Euclid mở rộng

Theo đồng nhất thức Bézout, nếu $$\gcd(a,n)=1$$ thì tồn tại các số nguyên $$s,t$$ sao cho $$sa + tn = 1$$. Lấy modulo $$n$$ hai vế, ta suy ra $$s \equiv a^{-1} \pmod n$$.

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

**Ví dụ 3.** Tìm nghịch đảo của $$7$$ modulo $$26$$: thuật toán Euclid mở rộng cho hệ số $$-11$$, đưa về đoạn không âm ta được $$-11 \bmod 26 = 15$$. Kiểm tra lại: $$7\cdot 15 = 105 = 4\cdot 26 + 1 \equiv 1 \pmod{26}$$.

</div>

## Định lý số dư Trung Hoa (CRT)

<div class="textbook-theorem" markdown="1">

**Định lý** (Chinese Remainder Theorem). Cho các số nguyên dương $$n_1,\ldots,n_k$$ đôi một nguyên tố cùng nhau. Hệ đồng dư

$$
x \equiv a_i \pmod{n_i}, \quad i=1,\ldots,k
$$

có nghiệm duy nhất theo modulo $$N = n_1 n_2 \cdots n_k$$.

Nghiệm được tính theo công thức $$x = \sum_{i=1}^{k} a_i N_i y_i$$, với $$N_i = N/n_i$$ và $$y_i = N_i^{-1} \bmod n_i$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4** (Bài toán Tôn Tử). Giải hệ phương trình đồng dư

$$
x \equiv 2 \pmod 3,\quad
x \equiv 3 \pmod 5,\quad
x \equiv 2 \pmod 7.
$$

Ta có $$N=105$$; $$N_1=35$$, $$y_1=2$$; $$N_2=21$$, $$y_2=1$$; $$N_3=15$$, $$y_3=1$$. Khi đó:

$$
x = 2\cdot 35\cdot 2 + 3\cdot 21\cdot 1 + 2\cdot 15\cdot 1 = 233 \equiv 23 \pmod{105}.
$$

Kiểm tra: $$23 \bmod 3=2$$, $$23 \bmod 5=3$$ và $$23 \bmod 7=2$$.

</div>

### Thử nghiệm: giải hệ đồng dư Trung Hoa

Nhập các phương trình $$x \equiv a_i \pmod{m_i}$$ để quan sát từng số hạng $$a_i \cdot M_i \cdot y_i$$:

<div class="interactive-demo" markdown="1">
<div data-demo="crypto-explainer" data-tab="crt"></div>
</div>

## Lũy thừa modulo nhanh

Để tính $$b^e \bmod n$$ khi số mũ $$e$$ rất lớn (dài hàng trăm đến hàng nghìn bit trong RSA), ta dùng phương pháp bình phương và nhân liên tiếp:

```text
ModExp(b, e, n)
result ← 1; base ← b MOD n
WHILE e > 0 DO
    IF e lẻ THEN result ← (result · base) MOD n
    base ← (base · base) MOD n
    e ← e DIV 2
RETURN result
```

Thuật toán chỉ cần $$O(\log e)$$ phép nhân modulo, thay vì $$O(e)$$ phép nhân tuần tự.

<div class="textbook-example" markdown="1">

**Ví dụ 5.** Tính $$3^{13} \bmod 7$$. Biểu diễn nhị phân của $$13$$ là $$1101_2$$. Thực hiện duyệt từng bit (từ bit thấp nhất LSB trước) cho kết quả bằng $$3$$. Kiểm tra trực tiếp: $$3^{13} = 1594323 = 7\cdot 227760 + 3$$.

</div>

## Định lý Fermat nhỏ và Định lý Euler

<div class="textbook-theorem" markdown="1">

**Định lý** (Fermat nhỏ). Nếu $$p$$ là số nguyên tố và $$p \nmid a$$ thì

$$
a^{p-1} \equiv 1 \pmod p.
$$

Dạng tương đương đúng với mọi số nguyên $$a$$ là $$a^p \equiv a \pmod p$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Euler). Nếu $$\gcd(a,n)=1$$ thì

$$
a^{\varphi(n)} \equiv 1 \pmod n,
$$

trong đó $$\varphi(n)$$ là **hàm phi Euler** (*Euler totient function*), đếm số các số nguyên trong $$\{1,\ldots,n-1\}$$ nguyên tố cùng nhau với $$n$$. Khi $$n=p$$ là số nguyên tố, ta có $$\varphi(p)=p-1$$, khôi phục lại định lý Fermat nhỏ.

</div>

Hai định lý này là cơ sở cho **tính đúng đắn của RSA**: nếu $$ed \equiv 1 \pmod{\varphi(n)}$$ thì $$M^{ed} \equiv M \pmod n$$ dưới các điều kiện tiêu chuẩn (Mục 15.3).

## Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="modular-arithmetic-calc"></div>
</div>
<script src="{{ '/public/js/modular-arithmetic-calc.js' | relative_url }}"></script>

### Minh họa tương tác

Minh họa mặt đồng hồ modulo, bảng cộng/nhân, nghịch đảo modulo và giải phương trình $$a\cdot x \equiv c$$:

<div class="interactive-demo" markdown="1">
<div data-demo="numtheory-explainer" data-tab="modular"></div>
</div>
<script src="{{ '/public/js/explainers/numtheory-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Tính $$(47 \times 93) \bmod 13$$ bằng cách rút gọn theo modulo.

<details>
<summary>Đáp án</summary>

Ta có $$47\equiv 8 \pmod{13}$$ và $$93\equiv 2 \pmod{13}$$, suy ra $$47 \cdot 93 \equiv 8\cdot 2 = 16 \equiv 3 \pmod{13}$$.

</details>

### Bài tập 2

Giải phương trình $$4x \equiv 5 \pmod 9$$.

<details>
<summary>Đáp án</summary>

Vì $$\gcd(4,9)=1\mid 5$$ nên phương trình có nghiệm duy nhất modulo 9. Nghịch đảo của 4 modulo 9 là 7 (vì $$4\cdot 7=28\equiv 1 \pmod 9$$), nên $$4^{-1}\equiv 7 \pmod 9$$.  
Suy ra $$x \equiv 5\cdot 7 = 35 \equiv 8 \pmod 9$$.

</details>

### Bài tập 3

Tìm nghịch đảo của 11 modulo 26.

<details>
<summary>Đáp án</summary>

Ta có $$\gcd(11,26)=1$$. Áp dụng Euclid mở rộng được $$11\cdot 19 = 209 = 8\cdot 26 + 1$$, suy ra $$11^{-1}\equiv 19 \pmod{26}$$.

</details>

### Bài tập 4

Giải hệ đồng dư bằng CRT: $$x\equiv 1\pmod 3$$, $$x\equiv 2\pmod 5$$, $$x\equiv 3\pmod 7$$.

<details>
<summary>Đáp án</summary>

Ta có $$N=105$$. Áp dụng công thức CRT thu được $$x \equiv 52 \pmod{105}$$ (kiểm tra: $$52\bmod 3=1$$, $$52\bmod 5=2$$, $$52\bmod 7=3$$).

</details>

### Bài tập 5

Với số mũ dài 2048 bit, thuật toán lũy thừa modulo nhanh cần khoảng bao nhiêu phép nhân modulo? So sánh với cách nhân tuần tự.

<details>
<summary>Đáp án</summary>

Thuật toán cần khoảng $$2048$$ vòng lặp; mỗi vòng thực hiện tối đa $$2$$ phép nhân modulo, nên tổng cộng chỉ vào cỡ vài nghìn phép nhân. Trong khi đó, nhân tuần tự cần $$\Theta(2^{2048})$$ phép nhân — hoàn toàn không khả thi về mặt tính toán.

</details>

## Tóm tắt

1. Quan hệ đồng dư $$a\equiv b\pmod n \iff n\mid(a-b)$$ tương thích với các phép cộng, trừ, nhân.
2. Phương trình $$ax\equiv b\pmod n$$ có nghiệm khi và chỉ khi $$\gcd(a,n)\mid b$$.
3. Nghịch đảo modulo tồn tại khi và chỉ khi $$\gcd(a,n)=1$$ và được tính bằng thuật toán Euclid mở rộng.
4. **Định lý số dư Trung Hoa (CRT)** cho phép giải hệ đồng dư với các modulus đôi một nguyên tố cùng nhau.
5. **Lũy thừa modulo nhanh** chạy trong $$O(\log e)$$; **định lý Fermat nhỏ và Euler** là nền tảng cho RSA.

Trong bài tiếp theo, ta sẽ tìm hiểu về mật mã cổ điển, **RSA** và giao thức trao đổi khóa **Diffie–Hellman**.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=d-n92Ml1iu0">[Discrete Mathematics] Modular Arithmetic</a> — TrevTutor, tiếng Anh. Giới thiệu về đồng dư và các phép toán modulo.
- <a href="https://www.youtube.com/watch?v=jCUOhbk1O_o">Quotient-Remainder Theorem and Modular Arithmetic</a> — Dr. Trefor Bazett, tiếng Anh. Định lý thương–dư, nền tảng của số học đồng dư.
- <a href="https://www.youtube.com/watch?v=TiV-tXVKPuM">Cơ bản về số học modulo Phần 1, phép Mod, div</a> — Đỗ Văn Đức - ĐH GTVT, tiếng Việt. Giải thích phép mod và div bằng tiếng Việt.
