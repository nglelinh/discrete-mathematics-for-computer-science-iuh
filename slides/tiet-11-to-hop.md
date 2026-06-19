---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Lý thuyết Tổ hợp

**Toán Rời Rạc — IUH**

Tiết 11 (45 phút) — Hoán vị và Tổ hợp

---

# Mục tiêu

- Tính P(n,k), C(n,k)
- Hoán vị vòng tròn, hoán vị lặp
- Tổ hợp lặp
- Ứng dụng sinh test case, mật mã

---

# Công thức chính + Chứng minh ý tưởng

**Hoán vị**:
P(n, k) = n! / (n - k)!

**Tổ hợp**:
C(n, k) = n! / (k! (n - k)!)

**Chứng minh tổ hợp** (bằng cách đếm):
- Chọn k từ n theo thứ tự: P(n,k)
- Mỗi tập hợp k phần tử được đếm k! lần → chia cho k!

**Công thức nhị thức**:
\((a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k\)

**Chứng minh bằng tổ hợp**:
Hệ số của \(a^{n-k} b^k\) là số cách chọn k vị trí cho b từ n vị trí.

---

# Hoán vị vòng tròn

Số cách xếp n vật quanh bàn tròn (không phân biệt chiều):
\((n-1)!\)

**Lý do**: Cố định một vị trí để loại bỏ sự quay vòng.

---

# Hoán vị với vật giống nhau (lặp)

Nếu có \(n_1\) vật loại 1, \(n_2\) loại 2, ... :
\[
\frac{n!}{n_1! n_2! \dots n_k!}
\]

**Ví dụ**: Số từ khác nhau từ chữ cái "MISSISSIPPI" = 11! / (1! 4! 4! 2!)

---

# Ứng dụng nâng cao trong CNTT

- **Sinh test case**: Số cách chọn tổ hợp tham số đầu vào để bao phủ.
- **Mật mã & Hash**: Số lượng key có thể → birthday attack (liên hệ pigeonhole).
- **Phân tích thuật toán**: Số lần lặp trong brute-force = tổ hợp.
- **Thiết kế hệ thống**: Stars and bars dùng trong phân vùng load balancing, resource allocation.

**Ví dụ thực tế**:
Trong kiểm thử phần mềm, số test case cho 5 tham số mỗi cái 3 giá trị (có lặp) = C(5+3-1, 5).

---

# Tổ hợp lặp (Stars and Bars)

Số cách chọn k vật từ n loại (có lặp):
\[
\binom{k + n - 1}{k}
\]

**Chứng minh ý tưởng**: Đặt k dấu sao (vật) và n-1 dấu gạch (phân cách), đếm số cách bố trí.

**Edge case**: Khi k=0 hoặc n=1.

---

# Thực hành

1. Tính P(10,3) và C(10,3)
2. Xếp 8 người quanh bàn tròn.
3. Số cách chọn 5 quả từ 3 loại trái cây (có lặp).

---

# Bài tập ôn tập

1. Tính số hoán vị của từ "COMPUTER".
2. Chứng minh C(n,k) = C(n, n-k)
3. Ứng dụng: Số cách tạo password 8 ký tự từ 26 chữ cái (có lặp).

---

# Tiết sau

Nguyên lý bao hàm-loại trừ + Tích Descartes.

---

# Câu hỏi?