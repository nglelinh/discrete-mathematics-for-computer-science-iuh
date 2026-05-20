---
layout: post
title: "Mật mã học Cơ bản"
categories: chapter15
date: 2021-01-01
order: 3
required: true
lang: en
---

# Mật mã học Cơ bản

Mỗi lần bạn đăng nhập ngân hàng, gửi tin nhắn mã hóa hay truy cập một trang web có biểu tượng ổ khóa, đằng sau đó là một lời hứa rất lớn: dữ liệu nhạy cảm phải đi qua môi trường công khai mà vẫn an toàn. Câu hỏi là làm sao một thông tin ai cũng có thể chặn được trên đường truyền lại chỉ người nhận hợp lệ mới đọc được?

**Mật mã học** trả lời câu hỏi ấy bằng cách kết hợp toán học với engineering. Và điều thú vị là rất nhiều ý tưởng cốt lõi của nó quay về lý thuyết số, modulo và số nguyên tố. Bài mở đầu này cho thấy vì sao một chủ đề từng bị xem là bí thuật quân sự nay lại là hạ tầng mặc định của internet hiện đại.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Giải thích** sự khác biệt giữa mã hóa đối xứng và bất đối xứng.
- **Mã hóa và giải mã** bằng Caesar cipher, affine cipher, và RSA.
- **Thực hiện** trao đổi khóa Diffie-Hellman.
- **Phân tích** tại sao RSA an toàn (dựa trên bài toán phân tích thừa số).
- **Hiểu** vai trò của mật mã trong bảo mật hiện đại.

**Từ khóa**: Mã hóa (encryption), giải mã (decryption), khóa công khai (public key), khóa riêng (private key), RSA, Diffie-Hellman, Caesar cipher.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter15/encryption_decryption.svg" alt="Sơ đồ quá trình mã hóa và giải mã với khóa" width="80%" height="80%">
  <figcaption style="text-align: center;">Hình 15.3 — Quá trình mã hóa và giải mã: bản rõ → thuật toán mã hóa + khóa → bản mã → thuật toán giải mã + khóa → bản rõ.</figcaption>
</p>
</figure>

## 1. Mã hóa Cổ điển

### Caesar Cipher

Dịch mỗi ký tự đi $$k$$ vị trí:

- **Mã hóa**: $$E(x) = (x + k) \bmod 26$$
- **Giải mã**: $$D(y) = (y - k) \bmod 26$$

<div class="content-box example-box" markdown="1">
Với $$k = 3$$, "HELLO" → "KHOOR".
</div>

### Affine Cipher

Tổng quát hơn: $$E(x) = (ax + b) \bmod 26$$, với $$\gcd(a, 26) = 1$$.

Giải mã cần nghịch đảo modulo: $$D(y) = a^{-1} \cdot (y - b) \bmod 26$$.

<div class="content-box example-box" markdown="1">
Với $$a = 5, b = 8$$: "A" (x=0) → $$5(0) + 8 = 8$$ → "I"
Giải mã: $$a^{-1} \bmod 26 = 21$$
"I" (y=8) → $$21(8-8) \bmod 26 = 0$$ → "A"
</div>

<div class="content-box warning-box" markdown="1">
**Lưu ý**: Các hệ mã cổ điển dễ bị phá bằng phân tích tần suất (frequency analysis). Trong thực tế, không dùng để bảo mật — chỉ có giá trị minh họa.
</div>

## 2. Mã hóa Khóa Công khai và RSA

### Vấn đề của Mã hóa Đối xứng

Trong mã hóa đối xứng, cả hai bên dùng **cùng một khóa** để mã hóa và giải mã. Vấn đề: làm sao trao đổi khóa an toàn qua kênh không an toàn?

### Ý tưởng Khóa Công khai

- Mỗi người có **khóa công khai** (public key) — ai cũng biết
- Và **khóa riêng** (private key) — chỉ mình biết
- Mã hóa bằng khóa công khai, giải mã bằng khóa riêng

### Thuật toán RSA (Rivest-Shamir-Adleman, 1977)

**Tạo khóa**:
1. Chọn hai số nguyên tố lớn $$p, q$$
2. Tính $$n = p \times q$$, $$\phi(n) = (p-1)(q-1)$$
3. Chọn $$e$$ sao cho $$\gcd(e, \phi(n)) = 1$$ (thường $$e = 65537$$)
4. Tính $$d = e^{-1} \bmod \phi(n)$$ (bằng Euclid mở rộng)
5. **Khóa công khai**: $$(n, e)$$ — **Khóa riêng**: $$d$$

**Mã hóa**: Cho thông điệp $$M < n$$: $$C = M^e \bmod n$$

**Giải mã**: $$M = C^d \bmod n$$

**Tại sao đúng?** Vì $$C^d \equiv (M^e)^d = M^{ed} \equiv M \pmod{n}$$ nhờ Định lý Euler: $$M^{\phi(n)} \equiv 1 \pmod{n}$$ khi $$\gcd(M, n) = 1$$.

<div class="content-box example-box" markdown="1">
**Ví dụ RSA với số nhỏ**:

- Chọn $$p = 61, q = 53$$ → $$n = 3233$$, $$\phi(n) = 3120$$
- Chọn $$e = 17$$ ($$\gcd(17, 3120) = 1$$)
- Tính $$d = 17^{-1} \bmod 3120 = 2753$$

Mã hóa $$M = 123$$: $$C = 123^{17} \bmod 3233 = 855$$
Giải mã $$C = 855$$: $$M = 855^{2753} \bmod 3233 = 123$$ ✓
</div>

**Tại sao RSA an toàn?** Để tính $$d$$ từ $$(n, e)$$, cần biết $$\phi(n)$$. Để tính $$\phi(n)$$, cần biết $$p$$ và $$q$$ — tức cần phân tích $$n$$ ra thừa số. Với $$n$$ 2048-bit (~617 chữ số), bài toán này bất khả thi với công nghệ hiện tại.

<div class="content-box insight-box" markdown="1">
**Một sự thật đáng kinh ngạc**: RSA dựa trên giả định rằng "nhân hai số nguyên tố lớn thì dễ, nhưng phân tích tích của chúng ra thừa số thì khó". Đây là một trong những ví dụ đẹp nhất về việc dùng *độ khó tính toán* làm công cụ bảo mật. Nếu một ngày nào đó ai đó tìm ra thuật toán phân tích thừa số nhanh (hoặc xây dựng được máy tính lượng tử đủ mạnh), RSA sẽ sụp đổ.
</div>

## 3. Trao đổi Khóa Diffie-Hellman

Cho phép hai bên thỏa thuận một khóa bí mật chung qua kênh công khai, không cần gặp nhau trước.

**Giao thức**:
1. Công khai: số nguyên tố lớn $$p$$, phần tử sinh $$g$$
2. Alice chọn bí mật $$a$$, gửi $$A = g^a \bmod p$$ cho Bob
3. Bob chọn bí mật $$b$$, gửi $$B = g^b \bmod p$$ cho Alice
4. Alice tính $$K = B^a \bmod p = g^{ba} \bmod p$$
5. Bob tính $$K = A^b \bmod p = g^{ab} \bmod p$$ → cùng $$K$$

<div class="content-box example-box" markdown="1">
Chọn $$p = 23, g = 5$$. Alice chọn $$a = 6$$, Bob chọn $$b = 15$$.

Alice gửi $$A = 5^6 \bmod 23 = 8$$
Bob gửi $$B = 5^{15} \bmod 23 = 19$$

Alice tính $$K = 19^6 \bmod 23 = 2$$
Bob tính $$K = 8^{15} \bmod 23 = 2$$ ✓
</div>

<div class="content-box insight-box" markdown="1">
**Tại sao an toàn?** Kẻ nghe lén biết $$p, g, A, B$$ nhưng không biết $$a, b$$ riêng. Để tính $$K$$, hắn cần tìm $$a$$ từ $$g^a \bmod p$$ — đây là **bài toán logarit rời rạc** (discrete logarithm), được tin là khó không kém phân tích thừa số.
</div>

## 4. Ứng dụng trong Thực tế

- **HTTPS/TLS**: Mọi website có ổ khóa xanh đều dùng Diffie-Hellman (hoặc RSA) để thiết lập kết nối an toàn.
- **Chữ ký số**: Xác thực danh tính người gửi — dùng RSA "ngược" (ký bằng khóa riêng, xác minh bằng khóa công khai).
- **Mã hóa đầu cuối**: WhatsApp, Signal dùng mật mã để đảm bảo chỉ người gửi và người nhận đọc được tin nhắn.
- **Bitcoin/Ethereum**: Ví tiền mã hóa dùng ECDSA (biến thể của mật mã đường cong elliptic, dựa trên ý tưởng từ số học modulo).

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Mô phỏng RSA</h3>
<p>Công cụ này mô phỏng toàn bộ quá trình RSA: chọn p, q, tính n và phi(n), tạo khóa, mã hóa và giải mã. Quan sát từng bước và hiểu cách các phép toán kết nối với nhau. <strong>Hãy thử:</strong> Chọn p=17, q=19, e=5 và mã hóa số 42. Kiểm tra xem giải mã có cho kết quả đúng không.</p>
</div>

## Bài tập

1. Mã hóa "MATH" bằng Caesar cipher với $$k = 5$$.
2. Trong Affine cipher với $$a = 7, b = 3$$, mã hóa "YES". Tìm công thức giải mã.
3. Với $$p = 3, q = 11, e = 7$$, tạo khóa RSA và mã hóa $$M = 5$$.
4. Trong Diffie-Hellman với $$p = 29, g = 2$$, Alice chọn $$a = 12$$, Bob chọn $$b = 8$$. Tính khóa chung.
5. **Thử thách**: Giả sử Eve có thể chặn được bản mã RSA $$C = 15$$, với khóa công khai $$(n, e) = (33, 7)$$. Hãy phân tích $$n$$, tính $$d$$, và giải mã.

<details>
<summary>Hướng dẫn bài 5</summary>

Phân tích 33: $$33 = 3 \times 11$$. Vậy $$p = 3, q = 11$$.

$$\phi(33) = (3-1)(11-1) = 2 \times 10 = 20$$.

$$d = e^{-1} \bmod 20 = 7^{-1} \bmod 20 = 3$$ (vì $$7 \times 3 = 21 \equiv 1 \pmod{20}$$).

Giải mã: $$M = C^d \bmod n = 15^3 \bmod 33$$.
$$15^2 = 225 \equiv 225 - 6 \times 33 = 225 - 198 = 27 \pmod{33}$$
$$15^3 = 15^2 \times 15 \equiv 27 \times 15 = 405 \equiv 405 - 12 \times 33 = 405 - 396 = 9 \pmod{33}$$

Vậy thông điệp gốc là $$M = 9$$.

Bài tập này cho thấy: với n nhỏ (33), việc phá RSA rất dễ. Trong thực tế, n phải có ít nhất 2048 bit để đảm bảo an toàn.
</details>

## Tóm tắt

- **Mã hóa cổ điển**: Caesar dịch chuyển, Affine mở rộng với nhân.
- **Mã hóa đối xứng**: cùng khóa cho mã hóa và giải mã — vấn đề trao đổi khóa.
- **RSA**: bảo mật dựa trên độ khó phân tích thừa số nguyên tố.
- **Diffie-Hellman**: trao đổi khóa qua kênh công khai, dựa trên logarit rời rạc.
- **Lũy thừa modulo nhanh**: thuật toán cốt lõi của mọi hệ thống mật mã hiện đại.

Trong bài tiếp theo, chúng ta sẽ khám phá thêm các ứng dụng khác của lý thuyết số.

## Tài liệu Tham khảo

1. R.L. Rivest, A. Shamir, L. Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems," *Communications of the ACM*, 1978 — bài báo RSA gốc.
2. W. Diffie, M. Hellman, "New Directions in Cryptography," *IEEE Transactions on Information Theory*, 1976 — bài báo Diffie-Hellman gốc.
3. Bruce Schneier, *Applied Cryptography*, Wiley — tài liệu tham khảo toàn diện.
4. Simon Singh, *The Code Book* — lịch sử mật mã học dễ đọc.
