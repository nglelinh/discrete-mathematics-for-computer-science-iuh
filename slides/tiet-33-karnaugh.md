---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Karnaugh Maps + Quine-McCluskey

**Toán Rời Rạc — IUH**

Tiết 33 (45 phút) — Tối thiểu hóa nâng cao

---

# Mục tiêu

- Sử dụng bản đồ Karnaugh để tối ưu hàm Boolean
- Xử lý Don't Care
- Phương pháp Quine-McCluskey
- So sánh các phương pháp tối thiểu hóa

---

# Bản đồ Karnaugh

- Biểu diễn hàm Boolean 2,3,4 biến dưới dạng lưới
- Gom nhóm ô 1 (power of 2) để loại biến

**Quy tắc gom nhóm**:
- Số ô trong nhóm phải là lũy thừa của 2
- Các ô phải liền kề (kể cả quấn)

---

# Don't Care

Ký hiệu X hoặc d

Có thể dùng để mở rộng nhóm (làm nhóm lớn hơn), nhưng không bắt buộc phải cover.

---

# Quine-McCluskey

Phương pháp bảng cho số biến lớn (>6).

Bước:
1. Liệt kê minterm
2. Kết hợp theo số bit khác nhau
3. Xây bảng prime implicant
4. Chọn phủ tối ưu

---

# Thực hành

Tối ưu hóa hàm cho trước bằng Karnaugh và Quine-McCluskey.

---

# Chiều sâu & Liên hệ

**Chứng minh / Ý tưởng**:
K-map dựa trên mã Gray (chỉ đổi 1 bit liền kề) để gom nhóm hợp lệ.

**Edge case**:
Don't Care cho nhiều lời giải tối ưu khác nhau; cần chọn lời giải tốt nhất.

**Liên hệ**:
- Boolean ↔ Thiết kế phần cứng (giảm cổng = giảm diện tích, công suất).
- Karnaugh ↔ Tối ưu compiler.

**Ứng dụng nâng cao**:
- Thiết kế mạch ASIC/FPGA.
- Tối ưu biểu thức trong ngôn ngữ lập trình.
- Quine-McCluskey cho >6 biến.

---

# Bài tập ôn tập

1. Tối ưu hóa hàm 4 biến bằng K-map.
2. Sử dụng Don't Care để tối ưu hơn.
3. (Thách thức) So sánh độ phức tạp K-map vs Quine-McCluskey.

---

# Tiết sau

Review Boolean.

---

# Câu hỏi?