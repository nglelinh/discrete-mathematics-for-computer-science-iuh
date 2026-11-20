---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Mật mã Cơ bản — RSA

**Toán Rời Rạc**

Tiết 41 (45 phút) — Symmetric vs Asymmetric Cryptography

---

## Mục tiêu tiết học

- Phân biệt mã hóa đối xứng và bất đối xứng
- Hiểu ý tưởng khóa công khai / khóa riêng
- Mô tả thuật toán RSA (tạo khóa, mã hóa, giải mã)
- Giải thích vì sao RSA an toàn (phân tích thừa số khó)
- Liên hệ HTTPS, chữ ký số, blockchain

---

## Mật mã học — Câu hỏi cốt lõi

1. Làm sao **chỉ người nhận** đọc được tin nhắn?
2. Làm sao **xác minh** tin nhắn không bị sửa?
3. Làm sao **trao đổi khóa** trên kênh không an toàn?

**Ba thành phần**:
- **Mã hóa** (encryption) / **Giải mã** (decryption)
- **Khóa** (key)
- **Thuật toán** (algorithm)

---

## Mã hóa Đối xứng (Symmetric)

**Một khóa** $$K$$ dùng cho cả mã hóa và giải mã:

$$E_K(\text{plaintext}) = \text{ciphertext}$$
$$D_K(\text{ciphertext}) = \text{plaintext}$$

**Ví dụ**: AES, ChaCha20, Caesar cipher.

| Ưu điểm | Nhược điểm |
|:---|:---|
| Nhanh | Phải chia sẻ $$K$$ an toàn |
| Hiệu quả cho dữ liệu lớn | $$n$$ người cần $$O(n^{2})$$ khóa |

**Vấn đề**: Làm sao gửi $$K$$ qua Internet mà không bị đánh cắp?

---

## Mã hóa Bất đối xứng (Asymmetric)

**Hai khóa** — cặp khóa toán học liên kết:

- **Khóa công khai** (public key): ai cũng biết → **mã hóa**
- **Khóa riêng** (private key): chỉ mình biết → **giải mã**

$$E_{\text{pub}}(m) = c \quad ; \quad D_{\text{priv}}(c) = m$$

**Ví dụ**: RSA, ECC (Elliptic Curve).

**Ý tưởng**: Gửi khóa công khai công khai; giữ khóa riêng bí mật.

---

## Caesar Cipher — Minh họa cổ điển

Dịch mỗi ký tự đi $$k$$ vị trí:

- **Mã hóa**: $$E(x) = (x + k) \bmod 26$$
- **Giải mã**: $$D(y) = (y - k) \bmod 26$$

**Ví dụ**: $$k = 3$$ → "HELLO" → "KHOOR"

**Yếu**: Chỉ 26 khóa → brute-force. Dễ bị **phân tích tần suất**.

**Bài học**: Mật mã cần không gian khóa **rất lớn** và cấu trúc toán học mạnh.

---

## So sánh Đối xứng vs Bất đối xứng

| | Đối xứng | Bất đối xứng |
|:---|:---|:---|
| Số khóa | 1 | 2 (cặp) |
| Tốc độ | Nhanh | Chậm hơn |
| Trao đổi khóa | Khó | Dễ (gửi public key) |
| Dùng cho | Mã hóa dữ liệu lớn | Trao đổi khóa, chữ ký |
| Ví dụ | AES-256 | RSA-2048, ECDSA |

**Thực tế (HTTPS)**: RSA/ECDHE trao đổi khóa → AES mã hóa session.

---

## Ý tưởng RSA (1977)

**Dựa trên**:
- Nhân hai số nguyên tố lớn: **dễ** ($$O(n^{2})$$)
- Phân tích $$n = p \times q$$ về nguyên tố: **rất khó** (chưa có thuật toán đa thức)

**Asymmetry** (bất đối xứng tính toán):
- Biết $$(p, q)$$ → tính $$\phi(n)$$ dễ
- Chỉ biết $$n$$ → phân tích $$p, q$$ khó

---

## RSA — Tạo khóa

1. Chọn hai số nguyên tố lớn $$p, q$$ (ví dụ 1024-bit mỗi số)
2. Tính $$n = p \times q$$ và $$\phi(n) = (p-1)(q-1)$$
3. Chọn $$e$$ sao cho $$\gcd(e, \phi(n)) = 1$$ (thường $$e = 65537$$)
4. Tính $$d \equiv e^{-1} \pmod{\phi(n)}$$ (Euclid mở rộng)

**Khóa công khai**: $$(e, n)$$

**Khóa riêng**: $$(d, n)$$

---

## RSA — Mã hóa & Giải mã

**Mã hóa** thông điệp $$m$$ ($$0 < m < n$$):

$$c \equiv m^{e} \pmod{n}$$

**Giải mã**:

$$m \equiv c^{d} \pmod{n}$$

**Tính đúng** (ý tưởng): $$c^{d} \equiv m^{ed} \equiv m \pmod{n}$$ (nhờ định lý Euler).

**Lũy thừa modulo nhanh**: $$O(\log e)$$ — khả thi trong thực tế.

---

## Ví dụ RSA nhỏ

$$p = 11, q = 13 \Rightarrow n = 143, \phi(n) = 120$$

Chọn $$e = 7$$ ($$\gcd(7, 120) = 1$$).

Tính $$d$$: $$7d \equiv 1 \pmod{120} \Rightarrow d = 103$$.

**Mã hóa** $$m = 5$$: $$c = 5^{7} \bmod 143 = 78125 \bmod 143 = 71$$

**Giải mã**: $$71^{103} \bmod 143 = 5$$ ✓

---

## Vì sao RSA an toàn?

**Giả thuyết**: Với $$n$$ đủ lớn (2048+ bit), phân tích $$n = pq$$ cần thời gian **siêu đa thức**.

| Kích thước $$n$$ | Thời gian phân tích (ước lượng) |
|:---|:---|
| 512 bit | Đã bị phá (1999) |
| 1024 bit | Không khuyến nghị |
| 2048 bit | Tiêu chuẩn hiện tại |
| 4096 bit | Mức bảo mật cao |

**Lưu ý**: RSA **không** mã hóa trực tiếp file lớn — dùng hybrid (RSA + AES).

---

## Ứng dụng thực tế

- **HTTPS/TLS**: Xác thực server, trao đổi khóa session
- **Chữ ký số**: Ký bằng private key, xác minh bằng public key
- **Email (PGP/GPG)**: Mã hóa end-to-end
- **Blockchain**: ECDSA ký giao dịch
- **JWT**: Ký token bằng RSA/ECDSA

```python
# Minh họa ý tưởng (KHÔNG dùng production!)
c = pow(m, e, n)      # mã hóa
m = pow(c, d, n)      # giải mã
```

---

## Thực hành 1

Với Caesar cipher $$k = 5$$:

1. Mã hóa "DISCRETE"
2. Giải mã "MJQQT"
3. Có bao nhiêu khóa có thể? Tại sao không an toàn?

---

## Thực hành 2

RSA mini: $$p = 3, q = 11, e = 3$$.

1. Tính $$n$$ và $$\phi(n)$$
2. Tìm $$d$$ sao cho $$ed \equiv 1 \pmod{\phi(n)}$$
3. Mã hóa $$m = 4$$, rồi giải mã kiểm tra

---

## Thực hành 3

Phân tích kịch bản:

> Alice gửi email mã hóa cho Bob qua kênh công cộng.

1. Dùng đối xứng thuần — vấn đề gì?
2. Bob công bố public key — Alice mã hóa bằng gì?
3. HTTPS dùng kết hợp như thế nào?

---

## Tóm tắt Tiết 41

- **Đối xứng**: 1 khóa, nhanh, khó trao đổi khóa
- **Bất đối xứng**: cặp khóa, trao đổi dễ, chậm hơn
- **RSA**: $$n = pq$$, $$c = m^{e} \bmod n$$, $$m = c^{d} \bmod n$$
- **Bảo mật**: phân tích thừa số khó
- **Thực tế**: hybrid encryption (RSA + AES)

---

## Liên hệ

**Cốt lõi**: Asymmetry — dễ một chiều, khó chiều ngược.

**Edge case**: $$p = q$$ → $$\phi(n)$$ tính sai, RSA không an toàn; $$m \geq n$$ cần chia block.

**Liên hệ**: Modulo (tiết 40) → RSA (tiết 41) → HTTPS, blockchain.

---

## Bài tập ôn tập (1/2)

1. **So sánh**: Nêu 2 ưu và 2 nhược điểm của mã hóa đối xứng.

2. **RSA mini**: $$p=5, q=7, e=5$$. Tính $$n, \phi(n), d$$. Mã hóa $$m=2$$.

3. **Caesar**: Giải mã "WKHDQ" với $$k$$ không cho — dùng phân tích tần suất (gợi ý: tiếng Anh, 'e' phổ biến nhất).

---

## Bài tập ôn tập (2/2)

4. **Bảo mật**: Giải thích vì sao biết $$e$$ và $$n$$ (public) không đủ để tính $$d$$ nếu phân tích $$n$$ khó.

5. **Bài 5**: Thiết kế kịch bản: 3 người A, B, C trao đổi khóa session an toàn. Dùng RSA cho bước nào? AES cho bước nào?
