---
layout: post
title: "Mật mã học Cơ bản"
categories: chapter15
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Mã hóa đối xứng và bất đối xứng; Caesar, Affine; RSA (tạo khóa, mã/giải); Diffie–Hellman; chữ ký số — gắn với modulo và Euclid."
---

<div class="textbook-epigraph" markdown="1">

"We stand today on the brink of a revolution in cryptography."

<span class="epigraph-attribution">— Diffie & Hellman (1976), tinh thần</span>

</div>

Số học modulo cho phép thao tác trên số dư; **mật mã học** dùng các cấu trúc đó để bảo vệ bí mật, toàn vẹn và xác thực thông tin. Mục này giới thiệu mô hình hệ mật, mã cổ điển (Caesar, Affine), RSA, Diffie–Hellman và chữ ký số — luôn ở mức có thể tính tay với số nhỏ.

![Luồng RSA](/discrete-mathematics-for-computer-science-iuh/img/course/Number_rsa_flow.svg)

<p class="textbook-figure-caption" data-figure="15.5">RSA: khóa công khai $$(n,e)$$, khóa riêng $$d$$; $$C \equiv M^e \pmod n$$, $$M \equiv C^d \pmod n$$.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** mã hóa đối xứng và bất đối xứng.
- **Mã / giải** Caesar, Affine và RSA với số nhỏ.
- **Thực hiện** một vòng Diffie–Hellman số nhỏ.
- **Giải thích** giả thuyết bảo mật RSA (phân tích thừa số) và DLP.
- **Mô tả** chữ ký số RSA ở mức khái niệm.

**Từ khóa**: encryption, public/private key, RSA, Diffie–Hellman, Caesar, Affine, chữ ký số.

</div>

## 1. Hệ mật mã

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Hệ mật mã** gồm thuật toán **mã hóa** $$E$$ và **giải mã** $$D$$ trên plaintext / ciphertext, điều khiển bởi **khóa**. Mục tiêu: chỉ bên có khóa hợp lệ khôi phục nội dung.

- **Đối xứng** (*symmetric*): cùng khóa bí mật $$K$$ cho $$E_K$$ và $$D_K$$ (AES, ChaCha20).
- **Bất đối xứng** (*asymmetric*): cặp $$(K_{\mathrm{pub}}, K_{\mathrm{priv}})$$; thường mã bằng công khai, giải bằng riêng (RSA).

</div>

| Mục tiêu | Ý nghĩa |
|:---|:---|
| **Confidentiality** | Kẻ ngoài không đọc được nội dung |
| **Integrity** | Phát hiện sửa đổi (hash, MAC) |
| **Authentication** | Xác minh nguồn (chữ ký số) |

## 2. Mã hóa cổ điển

<div class="textbook-definition" markdown="1">

**Định nghĩa** (Caesar). Với chữ cái mã hóa $$0..25$$ và khóa $$k$$:

$$
E(x) = (x+k)\bmod 26, \qquad D(y) = (y-k)\bmod 26.
$$

</div>

<div class="textbook-definition" markdown="1">

**Định nghĩa** (Affine). $$E(x)=(ax+b)\bmod 26$$ với $$\gcd(a,26)=1$$;

$$
D(y) = a^{-1}(y-b)\bmod 26.
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Caesar $$k=3$$: HELLO → KHOOR. Chỉ 26 khóa — brute-force tức thì; minh họa vì sao cần không gian khóa lớn.

</div>

## 3. RSA

**Vấn đề trao đổi khóa.** Mã đối xứng cần hai bên đã chia sẻ $$K$$; kênh nghe lén làm việc đó khó. Khóa công khai cho phép công bố $$K_{\mathrm{pub}}$$ và giữ riêng $$K_{\mathrm{priv}}$$.

<div class="textbook-definition" markdown="1">

**Định nghĩa** (RSA — Rivest, Shamir, Adleman, 1977). Hệ bất đối xứng dựa trên độ khó **phân tích thừa số**. Khóa công khai $$(n,e)$$; khóa riêng $$d$$ với $$ed \equiv 1 \pmod{\varphi(n)}$$.

</div>

**Tạo khóa**

1. Chọn hai số nguyên tố lớn $$p,q$$.
2. $$n = pq$$, $$\varphi(n)=(p-1)(q-1)$$.
3. Chọn $$e$$ với $$\gcd(e,\varphi(n))=1$$ (thường $$e=65537$$).
4. $$d = e^{-1} \bmod \varphi(n)$$ (Euclid mở rộng).
5. Công khai $$(n,e)$$; riêng $$d$$ (và thường cả $$p,q$$).

**Mã / giải** (thông điệp $$0 \le M < n$$):

$$
C \equiv M^e \pmod n, \qquad M \equiv C^d \pmod n.
$$

<div class="textbook-theorem" markdown="1">

**Định lý** (tính đúng RSA). Nếu $$ed \equiv 1 \pmod{\varphi(n)}$$ và $$\gcd(M,n)=1$$ thì $$C^d \equiv M^{ed} \equiv M \pmod n$$ nhờ định lý Euler $$M^{\varphi(n)}\equiv 1 \pmod n$$. (Có mở rộng cho mọi $$M$$ khi $$n=pq$$.)

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2** (số nhỏ). $$p=61$$, $$q=53$$ → $$n=3233$$, $$\varphi=3120$$. Chọn $$e=17$$, $$d=2753$$.  
$$M=123$$: $$C = 123^{17}\bmod 3233 = 855$$; giải mã bằng $$855^{2753}\bmod 3233$$ khôi phục $$123$$.

</div>

**Giả thuyết bảo mật.** Từ $$(n,e)$$ công khai, suy $$d$$ về thực chất đòi hỏi phân tích $$n=pq$$ — được tin khó với $$n$$ cỡ 2048 bit trở lên trên máy tính cổ điển. Thuật toán Shor trên máy lượng tử đe dọa RSA (Mục 15.4).

## 4. Diffie–Hellman

![Diffie–Hellman](/discrete-mathematics-for-computer-science-iuh/img/course/Number_diffie_hellman.svg)

<p class="textbook-figure-caption" data-figure="15.6">Hai bên tính cùng $$K = g^{ab}\bmod p$$ mà không gửi $$a$$ hay $$b$$.</p>

<div class="textbook-definition" markdown="1">

**Định nghĩa** (Diffie–Hellman, 1976). Giao thức trao đổi khóa trên kênh công khai. Tham số công khai: nguyên tố $$p$$, phần tử sinh $$g$$. Alice giữ $$a$$, gửi $$A=g^a\bmod p$$; Bob giữ $$b$$, gửi $$B=g^b\bmod p$$; cả hai tính $$K=g^{ab}\bmod p$$. An toàn dựa trên giả thuyết **logarit rời rạc** (DLP) khó.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 3.** $$p=23$$, $$g=5$$; $$a=6$$, $$b=15$$.  
$$A=5^6\bmod 23=8$$, $$B=5^{15}\bmod 23=19$$.  
$$K=19^6\bmod 23=2$$ và $$K=8^{15}\bmod 23=2$$.

</div>

## 5. Chữ ký số

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Chữ ký số**: ký bằng khóa **riêng** $$S=\mathrm{Sign}(M,K_{\mathrm{priv}})$$; xác minh bằng khóa **công khai**. Mục tiêu là **nguồn gốc** và **toàn vẹn**, không nhất thiết che nội dung.

</div>

RSA (mô hình đơn giản): $$S \equiv M^d \pmod n$$; xác minh $$S^e \equiv M \pmod n$$. Thực tế ký **hash** (SHA-256) của tài liệu, không ký trực tiếp file lớn.

## 6. Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="rsa-simulator"></div>
</div>
<script src="{{ '/public/js/rsa-simulator.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Mã hóa MATH bằng Caesar $$k=5$$.

<details>
<summary>Đáp án</summary>

M→R, A→F, T→Y, H→M → **RFYM**.

</details>

### Bài tập 2

Affine $$a=7$$, $$b=3$$: nêu công thức giải mã (nghịch đảo của 7 modulo 26).

<details>
<summary>Đáp án</summary>

$$7\cdot 15=105\equiv 1\pmod{26}$$ → $$a^{-1}\equiv 15$$.  
$$D(y)=15(y-3)\bmod 26$$.

</details>

### Bài tập 3

$$p=3$$, $$q=11$$, $$e=7$$: tính $$n$$, $$\varphi$$, $$d$$; mã hóa $$M=5$$.

<details>
<summary>Đáp án</summary>

$$n=33$$, $$\varphi=20$$, $$d=3$$ (vì $$7\cdot 3\equiv 1\pmod{20}$$).  
$$C=5^7\bmod 33=14$$ (vì $$5^2=25$$, $$5^4=(25)^2=625\equiv 31$$, $$5^6\equiv 31\cdot 25\equiv 26$$, $$5^7\equiv 26\cdot 5=130\equiv 31$$ — tính cẩn thận: $$5^1=5$$, $$5^2=25$$, $$5^3=125\equiv 26$$, $$5^4\equiv 26\cdot 5=130\equiv 31$$, $$5^5\equiv 31\cdot 5=155\equiv 23$$, $$5^6\equiv 23\cdot 5=115\equiv 16$$, $$5^7\equiv 16\cdot 5=80\equiv 14$$).

</details>

### Bài tập 4

Diffie–Hellman: $$p=29$$, $$g=2$$, $$a=12$$, $$b=8$$. Tính $$A$$, $$B$$ và $$K$$.

<details>
<summary>Đáp án</summary>

$$A=2^{12}\bmod 29=7$$; $$B=2^8\bmod 29=24$$.  
$$K=B^{12}\bmod 29=A^8\bmod 29=20$$ (cả hai cùng $$g^{ab}$$).

</details>

### Bài tập 5

Eve chặn $$C=15$$, khóa công khai $$(n,e)=(33,7)$$. Phân tích $$n$$, tìm $$d$$, giải mã.

<details>
<summary>Đáp án</summary>

$$33=3\cdot 11$$, $$\varphi=20$$, $$d=3$$.  
$$M=15^3\bmod 33$$: $$15^2=225\equiv 27$$, $$15^3\equiv 27\cdot 15=405\equiv 9\pmod{33}$$.  
$$M=9$$. Với $$n$$ nhỏ, RSA không an toàn.

</details>

## Tóm tắt

1. Đối xứng vs bất đối xứng; CIA ở mức khái niệm.
2. Caesar / Affine — modulo 26, không gian khóa nhỏ.
3. **RSA**: $$(n,e)$$, $$d$$; Euler bảo đảm tính đúng; an toàn từ factoring.
4. **Diffie–Hellman**: $$g^{ab}\bmod p$$; an toàn từ DLP.
5. **Chữ ký**: khóa riêng ký, công khai xác minh.

Trong bài tiếp theo: hash, PRNG, CRT tăng tốc RSA, ECC và hậu lượng tử.
