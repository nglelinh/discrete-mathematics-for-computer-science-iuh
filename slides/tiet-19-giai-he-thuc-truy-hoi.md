---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Giải Hệ thức Truy hồi Tuyến tính

**Toán Rời Rạc — IUH**

Tiết 19 (45 phút)

---

# Mục tiêu

- Giải hệ thức truy hồi tuyến tính thuần nhất
- Tìm nghiệm tổng quát
- Ứng dụng vào dãy số và thuật toán

---

# Phương trình đặc trưng + Chứng minh

Đối với \( a_n = c_1 a_{n-1} + c_2 a_{n-2} \)

**Phương trình đặc trưng**: \( r^2 - c_1 r - c_2 = 0 \)

Nghiệm r1, r2 → nghiệm tổng quát \( a_n = A r1^n + B r2^n \)

**Ý tưởng chứng minh**:
- Giả sử nghiệm có dạng \( r^n \), thay vào phương trình → ra đặc trưng.
- Tổng quát là tổ hợp tuyến tính của nghiệm (vì tuyến tính).

**Trường hợp nghiệm kép**:
Nếu r1 = r2 = r, thì \( a_n = (A + B n) r^n \)

---

# Ví dụ Fibonacci (chi tiết)

\( F_n = F_{n-1} + F_{n-2} \), F0=0, F1=1

Nghiệm: \( r = \frac{1 \pm \sqrt{5}}{2} \) (φ và hat φ)

\( F_n = A \phi^n + B \hat{\phi}^n \)

Sử dụng F0, F1 giải A, B → công thức Binet.

**Ứng dụng**: Phân tích độ phức tạp đệ quy, số lần gọi hàm.

---

# Bài tập ôn tập

Giải các hệ thức cho trước và tìm công thức đóng.

---

# Tiết sau

Hệ thức không thuần nhất.

---

# Câu hỏi?