---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Ôn tập Đếm + Quy nạp + Chuồng bồ câu

**Toán Rời Rạc — IUH**

Tiết 10 (45 phút)

---

# Mục tiêu

- Củng cố kỹ năng đếm và quy nạp
- Làm quen nguyên lý chuồng bồ câu
- Áp dụng vào password, phân quyền, test case

---

# Các quy tắc đếm cơ bản

**Nguyên lý cộng**:
|A ∪ B| = |A| + |B| - |A ∩ B|

**Nguyên lý nhân**:
Số cách tuần tự = tích lựa chọn.

---

# Công thức đếm cơ bản

**Hoán vị** P(n,k) = n! / (n-k)!

**Tổ hợp** C(n,k) = n! / (k!(n-k)!)

**Hoán vị lặp**: n! / (n1! n2! ...)

**Tổ hợp lặp**: C(k + n - 1 , k)

---

# Nguyên lý chuồng bồ câu (Pigeonhole Principle)

**Định lý cơ bản**:
Nếu n con bồ câu vào m chuồng (n > m), thì ít nhất một chuồng có ≥ 2 bồ câu.

**Dạng tổng quát**:
Nếu n vật được chia vào m nhóm, thì có ít nhất một nhóm chứa ít nhất \(\lceil n/m \rceil\) vật.

**Ví dụ**:
Trong 13 người, ít nhất 2 người sinh cùng tháng.

---

# Ứng dụng CNTT

- Password: Nếu có ít hơn số lượng mật khẩu có thể, thì có collision (sinh nhật paradox).
- Hash table: Nếu nhiều key hơn bucket → collision.
- Phân quyền: Nếu số user > số quyền → ít nhất 2 user có cùng quyền (nếu phân theo pigeonhole).

---

# Quy nạp toán học (Toán học quy nạp)

**Cấu trúc**:
1. **Bước cơ sở** (Base case): Chứng minh cho n = n0 (thường n=1 hoặc 0)
2. **Giả thiết quy nạp**: Giả sử đúng cho k = n
3. **Bước quy nạp**: Chứng minh đúng cho k = n+1

**Ví dụ**: Chứng minh tổng 1 + 2 + ... + n = n(n+1)/2

---

# Thực hành

1. Tính số hoán vị của 5 phần tử.
2. Áp dụng pigeonhole: Trong lớp 40 SV, chứng minh ít nhất 4 SV sinh cùng quý.
3. Chứng minh quy nạp: \(1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}\)

---

# Chiều sâu & Liên hệ

**Định lý chính**: Nguyên lý chuồng bồ câu và quy nạp toán học.

**Liên hệ**:
- Đếm ↔ Truy hồi.
- Pigeonhole ↔ Xác suất (Birthday paradox trong hash).

**Ứng dụng nâng cao**:
- Hash collision.
- Worst-case analysis.
- Resource scheduling.

---

# Bài tập ôn tập

1. Chứng minh bằng quy nạp: \(2^n > n\) với n ≥ 1
2. Tìm số cách chọn 3 người từ 10 người.
3. Password dài 8 ký tự (chữ + số): Ít nhất bao nhiêu người để chắc chắn có 2 người trùng password?
4. Ứng dụng pigeonhole trong thiết kế hash function.
5. (Thách thức) Chứng minh trong n+1 số từ 1 đến 2n luôn có 2 số chia hết cho nhau.

---

# Tiết sau

Lý thuyết tổ hợp chi tiết.

---

# Câu hỏi?