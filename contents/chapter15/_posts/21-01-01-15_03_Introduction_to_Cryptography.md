---
layout: post
title: "Mật mã học Cơ bản"
categories: chapter15
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã nắm số học modulo và các phép toán đồng dư. Mục này giới thiệu mật mã học ở mức nhập môn — cách dùng các cấu trúc số học để bảo vệ…"
---

Ở mục trước chúng ta đã nắm số học modulo và các phép toán đồng dư. Mục này giới thiệu **mật mã học** ở mức nhập môn — cách dùng các cấu trúc số học để bảo vệ tính bí mật, toàn vẹn và xác thực của thông tin trong hệ thống số.

![Sơ đồ RSA](/discrete-mathematics-for-computer-science-iuh/img/course/Public_key_encryption_keys.svg)

<p class="textbook-figure-caption" data-figure="15.11">RSA: mã hóa bằng khóa công khai $(e,n)$, giải mã bằng khóa riêng $(d,n)$.</p>
![Sinh khóa RSA](/discrete-mathematics-for-computer-science-iuh/img/course/rsa_key_generation.svg)

<p class="textbook-figure-caption" data-figure="15.12">Chọn hai số nguyên tố lớn $p,q$ — nhân dễ, phân tích khó tạo asymmetry bảo mật.</p>
![Độ khó phân tích thừa số](/discrete-mathematics-for-computer-science-iuh/img/course/PrimeDecompositionExample.svg)

<p class="textbook-figure-caption" data-figure="15.13">Bảo mật RSA dựa trên giả thuyết phân tích tích hai số nguyên tố lớn là khó.</p>
![Mũ modulo](/discrete-mathematics-for-computer-science-iuh/img/course/modular_arithmetic.svg)

<p class="textbook-figure-caption" data-figure="15.14">Mã hóa RSA dùng $c \equiv m^e \pmod n$ — số học mô-đun ở lõi mật mã.</p>
![Lịch sử mật mã](/discrete-mathematics-for-computer-science-iuh/img/course/Carl_Friedrich_Gauss.jpg)

<p class="textbook-figure-caption" data-figure="15.15">Từ Gauss đến Diffie–Hellman và RSA — lý thuyết số thuần trở thành hạ tầng Internet.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** sự khác biệt giữa mã hóa đối xứng và bất đối xứng.
- **Mã hóa và giải mã** bằng Caesar cipher, affine cipher, và RSA.
- **Thực hiện** trao đổi khóa Diffie-Hellman.
- **Phân tích** tại sao RSA an toàn (dựa trên bài toán phân tích thừa số).
- **Hiểu** vai trò của mật mã trong bảo mật hiện đại.

**Từ khóa**: Mã hóa (encryption), giải mã (decryption), khóa công khai (public key), khóa riêng (private key), RSA, Diffie-Hellman, Caesar cipher.
</div>

## 1. Khái niệm Mật mã học

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Hệ mật mã** gồm thuật toán **mã hóa** $$E$$ và **giải mã** $$D$$ trên tập thông điệp (plaintext) và bản mã (ciphertext). **Khóa** $$K$$ (hoặc cặp khóa) điều khiển biến đổi; mục tiêu: chỉ người có khóa hợp lệ đọc được nội dung.
</div>

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **Mã hóa đối xứng** (symmetric): cùng khóa bí mật $$K$$ cho $$E_K$$ và $$D_K$$ (AES, ChaCha20).
- **Mã hóa bất đối xứng** (asymmetric): cặp khóa $$(K_{pub}, K_{priv})$$; mã hóa bằng công khai, giải mã bằng riêng (RSA).
</div>

**Ba mục tiêu bảo mật** (CIA triad trong mật mã):

| Mục tiêu | Ý nghĩa |
|:---|:---|
| **Confidentiality** (bí mật) | Kẻ ngoài không đọc được |
| **Integrity** (toàn vẹn) | Phát hiện sửa đổi (hash, MAC) |
| **Authentication** (xác thực) | Xác minh người gửi (chữ ký số) |

## 2. Mã hóa Cổ điển

<div class="textbook-definition" markdown="1">
**Định nghĩa** (Caesar cipher): Ánh xạ mỗi chữ cái (mã hóa 0–25) dịch chuyển vòng $$k$$ vị trí:

- **Mã hóa**: $$E(x) = (x + k) \bmod 26$$
- **Giải mã**: $$D(y) = (y - k) \bmod 26$$
</div>

<div class="textbook-definition" markdown="1">
**Định nghĩa** (Affine cipher): $$E(x) = (ax + b) \bmod 26$$ với $$\gcd(a, 26) = 1$$. Giải mã: $$D(y) = a^{-1}(y - b) \bmod 26$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Caesar với $$k = 3$$: "HELLO" → "KHOOR". Chỉ có 26 khóa — **brute-force** tức thì; minh họa vì sao cần không gian khóa lớn.
</div>

## 3. Mã hóa Khóa Công khai và RSA

<div class="textbook-definition" markdown="1">
**Vấn đề trao đổi khóa**: Mã hóa đối xứng cần Alice và Bob **cùng biết** $$K$$ trước khi mã hóa — nhưng kênh truyền có thể bị nghe lén (Eve). **Khóa công khai** công bố $$K_{pub}$$; chỉ chủ sở hữu giữ $$K_{priv}$$.
</div>

<div class="textbook-definition" markdown="1">
**Định nghĩa** (RSA — Rivest, Shamir, Adleman, 1977): Hệ mật mã bất đối xứng dựa trên độ khó **phân tích thừa số**. Khóa công khai $$(n, e)$$; khóa riêng $$d$$ với $$ed \equiv 1 \pmod{\phi(n)}$$.
</div>

**Tạo khóa**:
1. Chọn hai số nguyên tố lớn $$p, q$$
2. Tính $$n = p \times q$$, $$\phi(n) = (p-1)(q-1)$$
3. Chọn $$e$$ sao cho $$\gcd(e, \phi(n)) = 1$$ (thường $$e = 65537$$)
4. Tính $$d = e^{-1} \bmod \phi(n)$$ (bằng Euclid mở rộng)
5. **Khóa công khai**: $$(n, e)$$ — **Khóa riêng**: $$d$$

**Mã hóa**: Cho thông điệp $$M < n$$: $$C = M^e \bmod n$$

**Giải mã**: $$M = C^d \bmod n$$

<div class="textbook-theorem" markdown="1">
**Định lý** (tính đúng RSA): Với $$ed \equiv 1 \pmod{\phi(n)}$$, ta có $$C^d \equiv M^{ed} \equiv M \pmod{n}$$ khi $$\gcd(M, n) = 1$$, nhờ **Định lý Euler**: $$M^{\phi(n)} \equiv 1 \pmod{n}$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ RSA với số nhỏ**:

- Chọn $$p = 61, q = 53$$ → $$n = 3233$$, $$\phi(n) = 3120$$
- Chọn $$e = 17$$ ($$\gcd(17, 3120) = 1$$)
- Tính $$d = 17^{-1} \bmod 3120 = 2753$$

Mã hóa $$M = 123$$: $$C = 123^{17} \bmod 3233 = 855$$
Giải mã $$C = 855$$: $$M = 855^{2753} \bmod 3233 = 123$$ ✓
</div>

<div class="textbook-definition" markdown="1">
**Giả thuyết bảo mật RSA**: Từ $$(n, e)$$ công khai, tính $$d$$ tương đương phân tích $$n = pq$$ — bài toán **phân tích thừa số** được tin là khó với $$n \geq$$ 2048 bit. Máy tính lượng tử (Shor) có thể phá RSA trong tương lai — xem 15.4 (post-quantum).
</div>

## 4. Trao đổi Khóa Diffie-Hellman

<div class="textbook-definition" markdown="1">
**Định nghĩa** (Diffie–Hellman, 1976): Giao thức trao đổi khóa qua kênh công khai. Hai bên thỏa thuận khóa chung $$K = g^{ab} \bmod p$$ mà không truyền $$a, b$$ — dựa trên giả thuyết **logarit rời rạc** (DLP) khó.
</div>

**Giao thức**:
1. Công khai: số nguyên tố lớn $$p$$, phần tử sinh $$g$$
2. Alice chọn bí mật $$a$$, gửi $$A = g^a \bmod p$$ cho Bob
3. Bob chọn bí mật $$b$$, gửi $$B = g^b \bmod p$$ cho Alice
4. Alice tính $$K = B^a \bmod p = g^{ba} \bmod p$$
5. Bob tính $$K = A^b \bmod p = g^{ab} \bmod p$$ → cùng $$K$$

<div class="textbook-example" markdown="1">
Chọn $$p = 23, g = 5$$. Alice chọn $$a = 6$$, Bob chọn $$b = 15$$.

Alice gửi $$A = 5^6 \bmod 23 = 8$$
Bob gửi $$B = 5^{15} \bmod 23 = 19$$

Alice tính $$K = 19^6 \bmod 23 = 2$$
Bob tính $$K = 8^{15} \bmod 23 = 2$$ ✓
</div>

**Tại sao an toàn?** Eve biết $$p, g, A, B$$ nhưng tính $$a$$ từ $$A = g^a \bmod p$$ là **bài toán logarit rời rạc** — được tin khó tương đương phân tích thừa số.

## 5. Chữ ký số

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Chữ ký số** dùng khóa **riêng** để ký $$S = \text{Sign}(M, K_{priv})$$; mọi người **xác minh** bằng $$K_{pub}$$. Khác mã hóa: ký = chứng minh **nguồn gốc** và **toàn vẹn**, không nhất thiết giữ bí mật nội dung.
</div>

RSA ký: $$S = M^d \bmod n$$; xác minh: kiểm tra $$S^e \equiv M \pmod{n}$$. Thực tế ký **hash** của tài liệu (SHA-256), không ký trực tiếp file lớn.

## 6. Ứng dụng trong Thực tế

- **HTTPS/TLS**: Mọi website có ổ khóa xanh đều dùng Diffie-Hellman (hoặc RSA) để thiết lập kết nối an toàn.
- **Chữ ký số**: Xác thực danh tính người gửi — dùng RSA "ngược" (ký bằng khóa riêng, xác minh bằng khóa công khai).
- **Mã hóa đầu cuối**: WhatsApp, Signal dùng mật mã để đảm bảo chỉ người gửi và người nhận đọc được tin nhắn.
- **Bitcoin/Ethereum**: Ví tiền mã hóa dùng ECDSA (biến thể của mật mã đường cong elliptic, dựa trên ý tưởng từ số học modulo).

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Mô phỏng RSA</h3>
<p>Công cụ này mô phỏng toàn bộ quá trình RSA: chọn p, q, tính n và phi(n), tạo khóa, mã hóa và giải mã. Quan sát từng bước và hiểu cách các phép toán kết nối với nhau. <strong>Gợi ý thực hành:</strong> Chọn p=17, q=19, e=5 và mã hóa số 42. Kiểm tra xem giải mã có cho kết quả đúng không.</p>
<div data-demo="rsa-simulator"></div>
</div>
<script src="{{ '/public/js/rsa-simulator.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Mã hóa "MATH" bằng Caesar cipher với $$k = 5$$.

<details>
<summary>Đáp án</summary>

M→R, A→F, T→Y, H→M → **"RFYM"**.
</details>

### Bài tập 2

Affine cipher $$a = 7, b = 3$$: mã hóa "YES". Công thức giải mã?

<details>
<summary>Đáp án</summary>

$$7^{-1} \equiv 15 \pmod{26}$$. $$D(y) = 15(y - 3) \bmod 26$$.
</details>

### Bài tập 3

$$p = 3, q = 11, e = 7$$: tạo khóa RSA, mã hóa $$M = 5$$.

<details>
<summary>Gợi ý</summary>

$$n = 33$$, $$\phi = 20$$, $$d = 3$$, $$C = 5^7 \bmod 33$$.
</details>

### Bài tập 4

Diffie-Hellman: $$p = 29, g = 2$$, $$a = 12$$, $$b = 8$$. Khóa chung?

<details>
<summary>Đáp án</summary>

$$A = 2^{12} \bmod 29$$, $$B = 2^8 \bmod 29$$; $$K = B^{12} \equiv A^8 \pmod{29}$$.
</details>

### Bài tập 5

Eve chặn $$C = 15$$, khóa công khai $$(n, e) = (33, 7)$$. Phân tích $$n$$, tính $$d$$, giải mã.

<details>
<summary>Đáp án</summary>

Phân tích 33: $$33 = 3 \times 11$$. Vậy $$p = 3, q = 11$$.

$$\phi(33) = (3-1)(11-1) = 2 \times 10 = 20$$.

$$d = e^{-1} \bmod 20 = 7^{-1} \bmod 20 = 3$$ (vì $$7 \times 3 = 21 \equiv 1 \pmod{20}$$).

Giải mã: $$M = C^d \bmod n = 15^3 \bmod 33$$.
<div class="textbook-equation" markdown="1">
$$15^2 = 225 \equiv 225 - 6 \times 33 = 225 - 198 = 27 \pmod{33}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$15^3 = 15^2 \times 15 \equiv 27 \times 15 = 405 \equiv 405 - 12 \times 33 = 405 - 396 = 9 \pmod{33}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy thông điệp gốc là $$M = 9$$.

Bài tập này cho thấy: với n nhỏ (33), việc phá RSA rất dễ. Trong thực tế, n phải có ít nhất 2048 bit để đảm bảo an toàn.
</details>

## Xem thêm / Video gợi ý

- [RSA Encryption](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Why it works)

## Tóm tắt

- **Hệ mật mã**: plaintext/ciphertext, khóa; đối xứng vs bất đối xứng.
- **Cổ điển**: Caesar, Affine — không gian khóa nhỏ, dễ phá.
- **RSA**: $$(n,e)$$ công khai; bảo mật từ phân tích thừa số; Euler chứng minh tính đúng.
- **Diffie-Hellman**: khóa chung $$g^{ab}$$; an toàn từ DLP.
- **Chữ ký số**: ký bằng khóa riêng, xác minh bằng công khai.

Trong bài tiếp theo, chúng ta sẽ khám phá thêm các ứng dụng khác của lý thuyết số.

## Tài liệu Tham khảo

1. R.L. Rivest, A. Shamir, L. Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems," *Communications of the ACM*, 1978 — bài báo RSA gốc.
2. W. Diffie, M. Hellman, "New Directions in Cryptography," *IEEE Transactions on Information Theory*, 1976 — bài báo Diffie-Hellman gốc.
3. Bruce Schneier, *Applied Cryptography*, Wiley — tài liệu tham khảo toàn diện.
4. Simon Singh, *The Code Book* — lịch sử mật mã học dễ đọc.
