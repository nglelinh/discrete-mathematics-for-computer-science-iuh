---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Nguyên lý Bao hàm - Loại trừ

**Toán Rời Rạc — IUH**

Tiết 12 (45 phút)

---

# Mục tiêu

- Nắm công thức bao hàm-loại trừ cho 2 và 3 tập
- Áp dụng vào đếm và xác suất
- Liên hệ với SQL JOIN và tích Descartes

---

# Công thức

**2 tập**:
\[ |A \cup B| = |A| + |B| - |A \cap B| \]

**3 tập**:
\[ |A \cup B \cup C| = |A| + |B| + |C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B \cap C| \]

---

# Ứng dụng

- Đếm số sinh viên học ít nhất 1 trong 3 môn
- Số phần tử thỏa ít nhất 1 điều kiện
- Tính xác suất union events

**Ví dụ SQL**:
Tích Descartes A × B tương ứng với CROSS JOIN.
Các phép giao/hợp liên hệ với INNER/OUTER JOIN.

---

# Thực hành

Tính |A ∪ B ∪ C| với số liệu cho trước.

---

# Chiều sâu & Liên hệ

**Định lý** (Inclusion-Exclusion cho n tập):
Công thức tổng quát xen kẽ dấu + và - .

**Chứng minh ý tưởng**:
Mỗi phần tử được đếm đúng số tập nó thuộc vào.

**Edge case**:
Các tập rời nhau → giảm về nguyên lý cộng.

**Liên hệ**:
- Bao hàm-loại trừ ↔ Xác suất.
- Bao hàm-loại trừ ↔ Đồ thị (đếm với điều kiện).

**Ứng dụng nâng cao**:
- Đếm số user thỏa ít nhất k chính sách.
- Tối ưu query CSDL với UNION/EXCEPT.
- Trong bảo mật: đếm khả năng vi phạm.

---

# Bài tập ôn tập

1. Trong lớp 100 SV, 40 học Toán, 30 học Lý, 25 học Hóa. Biết 10 học cả 3. Tính số SV học ít nhất 1 môn.
2. Ứng dụng vào kiểm đếm user có ít nhất 1 quyền.
3. (Thách thức) Mở rộng cho 4 tập và giải thích công thức.

---

# Tiết sau

Ôn tập đếm + Review.

---

# Câu hỏi?