---
layout: post
title: "Số học Modulo và Đồng dư"
categories: chapter15
date: 2021-01-01
order: 2
required: true
lang: en
---

# Số học Modulo và Đồng dư

Đồng hồ chỉ 14 giờ rồi quay về 2 giờ; checksum cộng đến một mức nào đó rồi lấy phần dư; rất nhiều thuật toán mã hóa và băm hoạt động không phải trên số nguyên “thẳng”, mà trên số nguyên theo chu kỳ. Nếu chưa quen, kiểu tính toán này có cảm giác như toán học đang tự bẻ luật của chính nó.

Thực ra đó là **số học modulo** — một trong những công cụ hữu ích nhất của lý thuyết số ứng dụng. Nó giúp ta làm việc với phần dư có quy tắc, rút gọn phép tính lớn, và xây nền cho mật mã, hashing, randomization cùng nhiều kỹ thuật tối ưu trong khoa học máy tính.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Thực hiện** phép cộng, trừ, nhân trong modulo $$n$$.
- **Giải** phương trình đồng dư tuyến tính dạng $$ax \equiv b \pmod{n}$$.
- **Tính** nghịch đảo modulo bằng thuật toán Euclid mở rộng.
- **Áp dụng** Định lý Số dư Trung Hoa (CRT) cho hệ đồng dư.
- **Tính** lũy thừa modulo nhanh (fast modular exponentiation).

**Từ khóa**: Đồng dư (congruence), modulo, nghịch đảo modulo (modular inverse), CRT, lũy thừa modulo, $$a^{-1} \bmod n$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter15/modular_clock.svg" alt="Minh họa đồng hồ modulo 12 — các số quay vòng sau 12" width="60%" height="60%">
  <figcaption style="text-align: center;">Hình 15.2 — Đồng hồ modulo 12: $$13 \equiv 1 \pmod{12}$$, $$17 \equiv 5 \pmod{12}$$.</figcaption>
</p>
</figure>

## 1. Đồng dư

**Định nghĩa**: Cho $$a, b \in \mathbb{Z}$$, $$n \in \mathbb{Z}^+$$. Ta nói $$a$$ **đồng dư** với $$b$$ modulo $$n$$, ký hiệu:

$$a \equiv b \pmod{n}$$

nếu $$n \mid (a - b)$$, tức $$a$$ và $$b$$ có cùng số dư khi chia cho $$n$$.

<div class="content-box example-box" markdown="1">
- $$17 \equiv 5 \pmod{12}$$ vì $$17 - 5 = 12$$ chia hết cho 12
- $$-8 \equiv 2 \pmod{5}$$ vì $$-8 - 2 = -10$$ chia hết cho $$5$$
- $$15 \equiv 0 \pmod{5}$$ vì $$15$$ chia hết cho $$5$$
</div>

### Phép toán Modulo

Nếu $$a \equiv b \pmod{n}$$ và $$c \equiv d \pmod{n}$$ thì:

- $$a + c \equiv b + d \pmod{n}$$
- $$a - c \equiv b - d \pmod{n}$$
- $$a \times c \equiv b \times d \pmod{n}$$

<div class="content-box example-box" markdown="1">
Tính $$(23 \times 17) \bmod 5$$:

$$23 \equiv 3 \pmod{5},\quad 17 \equiv 2 \pmod{5}$$
$$23 \times 17 \equiv 3 \times 2 = 6 \equiv 1 \pmod{5}$$
</div>

<div class="content-box warning-box" markdown="1">
**Cảnh báo**: Phép chia trong modulo KHÔNG đơn giản như trong số học thông thường. $$a \equiv b \pmod{n}$$ KHÔNG suy ra $$a/c \equiv b/c \pmod{n}$$. Để "chia" trong modulo, ta cần dùng **nghịch đảo modulo** (sẽ học ở phần 3).
</div>

## 2. Phương trình Đồng dư Tuyến tính

Bài toán: giải $$ax \equiv b \pmod{n}$$, tìm $$x$$.

**Định lý**: Phương trình có nghiệm khi và chỉ khi $$d = \gcd(a, n) \mid b$$. Khi đó, có đúng $$d$$ nghiệm modulo $$n$$, không đồng dư với nhau.

<div class="content-box example-box" markdown="1">
**Ví dụ**: Giải $$6x \equiv 3 \pmod{9}$$.

$$\gcd(6, 9) = 3$$ và $$3 \mid 3$$ → có 3 nghiệm.

Chia cả hai vế cho 3: $$2x \equiv 1 \pmod{3}$$ → $$x \equiv 2 \pmod{3}$$.

Các nghiệm modulo 9: $$x \equiv 2, 5, 8 \pmod{9}$$.
</div>

## 3. Nghịch đảo Modulo

**Định nghĩa**: Nghịch đảo modulo của $$a$$ modulo $$n$$ là số $$\bar{a}$$ sao cho:

$$a \cdot \bar{a} \equiv 1 \pmod{n}$$

Tồn tại khi và chỉ khi $$\gcd(a, n) = 1$$.

### Thuật toán Euclid Mở rộng

```
THUẬT TOÁN: Euclid-Mở-rộng(a, n)   // tìm nghịch đảo của a mod n
Đầu vào: a, n với gcd(a, n) = 1
Đầu ra: nghịch đảo x sao cho a·x ≡ 1 (mod n)

1. old_r, r ← a, n
2. old_s, s ← 1, 0
3. WHILE r ≠ 0 DO
4.     q ← old_r DIV r
5.     old_r, r ← r, old_r - q*r
6.     old_s, s ← s, old_s - q*s
7. END WHILE
8. RETURN old_s MOD n   // đảm bảo kết quả dương
```

<div class="content-box example-box" markdown="1">
Tìm nghịch đảo của 7 modulo 26:

| Bước | old_r | r | q | old_s | s |
|:------|:-------|:---|---:|:-------|:---|
| 1 | 7 | 26 | 0 | 1 | 0 |
| 2 | 26 | 7 | 3 | 0 | 1 |
| 3 | 7 | 5 | 1 | 1 | -3 |
| 4 | 5 | 2 | 2 | -3 | 4 |
| 5 | 2 | 1 | 2 | 4 | -11 |
| 6 | 1 | 0 | - | -11 | — |

Kết quả: $$-11 \bmod 26 = 15$$. Kiểm tra: $$7 \times 15 = 105 \equiv 1 \pmod{26}$$ ✓
</div>

## 4. Định lý Số dư Trung Hoa (CRT)

**Định lý**: Cho $$n_1, n_2, \ldots, n_k$$ là các số nguyên dương đôi một nguyên tố cùng nhau. Hệ đồng dư:

$$x \equiv a_1 \pmod{n_1}$$
$$x \equiv a_2 \pmod{n_2}$$
$$\cdots$$
$$x \equiv a_k \pmod{n_k}$$

có nghiệm duy nhất modulo $$N = n_1 \cdot n_2 \cdots n_k$$.

<div class="content-box example-box" markdown="1">
**Ví dụ**: Giải hệ:
$$x \equiv 2 \pmod{3}$$
$$x \equiv 3 \pmod{5}$$
$$x \equiv 2 \pmod{7}$$

$$N = 3 \times 5 \times 7 = 105$$.
$$N_1 = 105/3 = 35$$, $$y_1 = 35^{-1} \bmod 3 = 2^{-1} \bmod 3 = 2$$
$$N_2 = 105/5 = 21$$, $$y_2 = 21^{-1} \bmod 5 = 1^{-1} \bmod 5 = 1$$
$$N_3 = 105/7 = 15$$, $$y_3 = 15^{-1} \bmod 7 = 1^{-1} \bmod 7 = 1$$

$$x = 2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1 = 140 + 63 + 30 = 233$$
$$x \equiv 233 \bmod 105 \equiv 23 \pmod{105}$$

Kiểm tra: $$23 \bmod 3 = 2$$, $$23 \bmod 5 = 3$$, $$23 \bmod 7 = 2$$ ✓
</div>

<div class="content-box insight-box" markdown="1">
**CRT trong lịch sử**: Định lý này được biết đến từ thế kỷ thứ 3 ở Trung Quốc, trong cuốn sách "Tôn Tử Toán Kinh" (Sunzi Suan Jing). Bài toán gốc: "Tìm số biết rằng chia 3 dư 2, chia 5 dư 3, chia 7 dư 2." Đáp số 23 — giống hệt ví dụ trên!
</div>

## 5. Lũy thừa Modulo Nhanh

Tính $$b^e \bmod n$$ với $$e$$ rất lớn (hàng trăm chữ số — như trong RSA):

```
THUẬT TOÁN: Lũy-thừa-Modulo-Nhanh(b, e, n)
1. result ← 1
2. base ← b MOD n
3. WHILE e > 0 DO
4.     IF e lẻ THEN result ← (result * base) MOD n
5.     base ← (base * base) MOD n
6.     e ← e DIV 2
7. END WHILE
8. RETURN result
```

Độ phức tạp: $$O(\log e)$$ — thay vì $$O(e)$$ nếu nhân tuần tự!

<div class="content-box example-box" markdown="1">
**Ví dụ**: Tính $$3^{13} \bmod 7$$.

$$13_{10} = 1101_2$$. Các bit: 1, 1, 0, 1 (từ LSB đến MSB).

| Bit | base | result |
|:---|:---|:---:|
| - | 3 | 1 |
| 1 (LSB) | $$3^2=9\equiv2$$ | $$1\times3=3$$ |
| 0 | $$2^2=4$$ | 3 |
| 1 | $$4^2=16\equiv2$$ | $$3\times2=6\equiv6$$ |
| 1 (MSB) | $$2^2=4$$ | $$6\times4=24\equiv3$$ |

Kết quả: $$3^{13} \bmod 7 = 3$$. Kiểm tra: $$3^{13} = 1594323 = 7 \times 227760 + 3$$ ✓
</div>

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Máy tính Modulo</h3>
<p>Công cụ này thực hiện các phép tính modulo cơ bản: cộng, trừ, nhân, nghịch đảo, lũy thừa. Quan sát từng bước của thuật toán Euclid mở rộng. <strong>Hãy thử:</strong> Tính $$5^{17} \bmod 23$$ bằng lũy thừa modulo nhanh — đây là phép tính cốt lõi trong Diffie-Hellman!</p>
</div>

## Ứng dụng trong Khoa học Máy tính

Số học modulo xuất hiện trong: băm (hash maps), kiểm tra tính nguyên tố (Miller-Rabin), sinh số ngẫu nhiên (LGC), mã hóa RSA và ElGamal, chữ ký số DSA, và giao thức trao đổi khóa Diffie-Hellman.

Lũy thừa modulo nhanh là một trong những thuật toán được gọi nhiều nhất trong mọi hệ thống bảo mật web (TLS/HTTPS). Mỗi khi bạn truy cập một trang web có ổ khóa xanh, trình duyệt của bạn đã thực hiện hàng chục phép lũy thừa modulo với số mũ hàng trăm chữ số!

## Bài tập

1. Tính $$(47 \times 93) \bmod 13$$ bằng cách rút gọn modulo.
2. Giải $$4x \equiv 5 \pmod{9}$$.
3. Tìm nghịch đảo modulo của 11 trong modulo 26.
4. Dùng CRT giải: $$x \equiv 1 \pmod{3}, x \equiv 2 \pmod{5}, x \equiv 3 \pmod{7}$$.
5. **Thử thách**: Viết chương trình (pseudocode) tính $$a^b \bmod n$$ bằng lũy thừa modulo nhanh, và ước tính số phép nhân cần thiết khi $$b$$ có 2048 bit (như trong RSA).

<details>
<summary>Hướng dẫn bài 5</summary>

Số phép nhân cần thiết: với số mũ 2048 bit, thuật toán thực hiện đúng 2048 vòng lặp. Mỗi vòng thực hiện tối đa 2 phép nhân modulo (một cho base, một cho result nếu bit là 1). Vậy tối đa ~4096 phép nhân.

So sánh với nhân tuần tự: cần $$2^{2048}$$ phép nhân — một con số lớn hơn tổng số nguyên tử trong vũ trụ!

Đây là lý do tại sao lũy thừa modulo nhanh là một trong những thuật toán quan trọng nhất trong mật mã học.
</details>

## Tóm tắt

- **Đồng dư**: $$a \equiv b \pmod{n}$$ nếu $$n \mid (a - b)$$.
- **Phép toán modulo**: cộng, trừ, nhân giữ nguyên modulo.
- **Phương trình $$ax \equiv b \pmod{n}$$**: có nghiệm ⇔ $$\gcd(a,n) \mid b$$.
- **Nghịch đảo modulo**: tồn tại ⇔ $$\gcd(a, n) = 1$$, tính bằng Euclid mở rộng.
- **Định lý Số dư Trung Hoa**: giải hệ phương trình đồng dư với các modulo nguyên tố cùng nhau.
- **Lũy thừa modulo nhanh**: $$O(\log e)$$ thay vì $$O(e)$$.

Trong bài tiếp theo, chúng ta sẽ áp dụng những kiến thức này vào mật mã học.

## Tài liệu Tham khảo

1. Kenneth H. Rosen, *Elementary Number Theory and Its Applications*, Chương 4-5.
2. Tôn Tử, *Tôn Tử Toán Kinh*, ~thế kỷ 3 — nguồn gốc của CRT.
3. Carl Friedrich Gauss, *Disquisitiones Arithmeticae*, 1801 — hệ thống hóa số học modulo hiện đại.
