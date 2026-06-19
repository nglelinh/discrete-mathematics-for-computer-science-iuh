---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Ôn tập + Lý thuyết Tập hợp

**Toán Rời Rạc — IUH**

Tiết 8 (45 phút)

---

# Mục tiêu tiết học

- Ôn lại kiến thức logic và chứng minh
- Hiểu định nghĩa tập hợp
- Thực hiện các phép toán trên tập hợp
- Biểu diễn tập hợp trong máy tính
- Liên hệ với CSDL và lập trình

---

# Ôn nhanh: Logic mệnh đề & Vị từ

- Mệnh đề = câu có giá trị T/F
- 6 phép toán + bảng chân trị
- DNF/CNF
- Quy tắc suy diễn (MP, MT, Tam đoạn luận)
- Phản chứng
- Vị từ + ∀, ∃

**Bài tập nhanh**: Phủ định ∀x ∃y (x > y)

---

# Định nghĩa Tập hợp

**Tập hợp (Set)**: Là một tập hợp các đối tượng phân biệt (không có thứ tự, không lặp).

**Ký hiệu**:
- \( A = \{1, 2, 3\} \)
- \( x \in A \): x thuộc A
- \( x \notin A \): x không thuộc A

**Mô tả**:
- Liệt kê: \{a, b, c\}
- Đặc trưng: \{ x | P(x) \}

---

# Các tập hợp đặc biệt

| Ký hiệu | Tên | Ý nghĩa |
|---------|-----|---------|
| ∅ hoặc {} | Tập rỗng | Không chứa phần tử nào |
| U | Tập vũ trụ | Tập chứa mọi đối tượng đang xét |
| ℕ | Số tự nhiên | 1,2,3,... (hoặc 0,1,2...) |
| ℤ | Số nguyên | ...,-2,-1,0,1,2,... |
| ℚ | Số hữu tỷ | Phân số |
| ℝ | Số thực | |

---

# Phép toán trên tập hợp

**1. Hợp (Union)**: \( A \cup B = \{x \mid x \in A \lor x \in B\} \)

**2. Giao (Intersection)**: \( A \cap B = \{x \mid x \in A \land x \in B\} \)

**3. Hiệu (Difference)**: \( A \setminus B = \{x \mid x \in A \land x \notin B\} \)

**4. Bù (Complement)**: \( A^c = U \setminus A \)

**5. Tích Descartes**: \( A \times B = \{(a,b) \mid a \in A, b \in B\} \)

---

# Tính chất quan trọng

- Giao hoán, kết hợp, phân phối
- Luật De Morgan cho tập hợp:
  \( (A \cup B)^c = A^c \cap B^c \)
  \( (A \cap B)^c = A^c \cup B^c \)

- Tập con: \( A \subseteq B \)

---

# Biểu diễn tập hợp trong máy tính

**Python**:
```python
A = {1, 2, 3}
B = {3, 4, 5}
A | B          # union
A & B          # intersection
A - B          # difference
A ^ B          # symmetric difference
```

**SQL**: Biểu diễn qua bảng (mỗi hàng là phần tử), JOIN, UNION, INTERSECT.

---

# Thực hành (10 phút)

Cho:
- A = {1,2,3,4}
- B = {3,4,5,6}
- U = {1..10}

Tính:
1. A ∪ B
2. A ∩ B
3. (A ∪ B)^c
4. A × B (một số cặp)

---

# Tóm tắt

- Tập hợp là nền tảng mô hình hóa dữ liệu
- Các phép toán hợp, giao, hiệu, bù, tích Descartes
- Liên hệ trực tiếp với SQL và cấu trúc dữ liệu

---

# Chiều sâu & Liên hệ (1)

**Định lý**: |A ∪ B| = |A| + |B| - |A ∩ B| (chứng minh bằng đếm).

**Edge case**: Tập rỗng, tập vũ trụ.

---

# Chiều sâu & Liên hệ (2)

**Liên hệ**:
- Tập hợp ↔ Quan hệ (Cartesian).
- Tập hợp ↔ Logic (Boolean ops).

**Ứng dụng nâng cao**:
- Relational algebra.
- HashSet, Bloom Filter.
- Cardinality analysis.

---

# Bài tập ôn tập (1/2)

1. Chứng minh: \( A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \)
2. Tìm tập con đúng của {1,2,3,4}

---

# Bài tập ôn tập (2/2)

3. Viết biểu thức: "Sinh viên học Toán rời rạc hoặc Lập trình"
4. Python code kiểm tra A ⊆ B
5. Tại sao quan hệ CSDL là tập hợp?

---

# Tiết sau

**Phương pháp đếm + Nguyên lý chuồng bồ câu**

---

# Câu hỏi?