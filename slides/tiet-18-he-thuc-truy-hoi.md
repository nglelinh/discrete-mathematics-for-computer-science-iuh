---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Hệ thức Truy hồi

**Toán Rời Rạc — IUH**

Tiết 18 (45 phút)

---

# Mục tiêu

- Định nghĩa hệ thức truy hồi
- Giải hệ thức truy hồi tuyến tính
- Ứng dụng trong phân tích thuật toán

---

# Định nghĩa

**Hệ thức truy hồi**: Công thức định nghĩa dãy số trong đó mỗi phần tử được xác định từ các phần tử trước.

**Ví dụ**:
- Fibonacci: \( F_n = F_{n-1} + F_{n-2} \), F0=0, F1=1
- Giai thừa: n! = n × (n-1)!

---

# Giải hệ thức tuyến tính thuần nhất

Dạng: \( a_n + c_1 a_{n-1} + \dots + c_k a_{n-k} = 0 \)

**Bước**:
1. Tìm phương trình đặc trưng
2. Tìm nghiệm
3. Viết nghiệm tổng quát
4. Dùng điều kiện đầu để tìm hằng số

---

# Ứng dụng

- Phân tích độ phức tạp đệ quy (Merge sort, Tower of Hanoi)
- Số lần gọi hàm đệ quy

---

# Chiều sâu & Liên hệ (1)

**Định lý**: Nghiệm tổng quát = tổ hợp tuyến tính nghiệm đặc trưng.

**Chứng minh ý tưởng**:
Giả sử r^n, thay vào → ra đặc trưng.

**Edge case**:
Nghiệm kép → nhân thêm n.

---

# Chiều sâu & Liên hệ (2)

**Liên hệ**:
- Truy hồi ↔ Đếm.
- Truy hồi ↔ Đồ thị.
- Truy hồi ↔ Master Theorem.

**Ứng dụng nâng cao**:
- Merge Sort Θ(n log n)
- Hanoi Θ(2^n)
- DP + memoization.

---

# Bài tập ôn tập (1/2)

1. Giải hệ: \( a_n = 3 a_{n-1} + 2 \), a0=1. Tìm công thức đóng.

2. Tìm độ phức tạp Tower of Hanoi + chứng minh quy nạp.

---

# Bài tập ôn tập (2/2)

3. (Thách thức) Phân tích tìm kiếm nhị phân bằng truy hồi.

---

# Tiết sau

Quan hệ và ánh xạ.

---

# Câu hỏi?