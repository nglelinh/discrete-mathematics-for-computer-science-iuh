---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Logic Vị từ

**Toán Rời Rạc — IUH**

Tiết 7 (45 phút) — Lượng từ ∀ và ∃

---

# Mục tiêu tiết học

- Hiểu hạn chế của logic mệnh đề
- Định nghĩa vị từ và miền xác định
- Sử dụng lượng từ ∀ (với mọi) và ∃ (tồn tại)
- Viết và phủ định đúng mệnh đề lượng hóa
- Áp dụng vị từ vào lập trình và CSDL

---

# Hạn chế của Logic Mệnh đề

Logic mệnh đề chỉ làm việc với câu khẳng định đã hoàn chỉnh (có giá trị T/F).

**Ví dụ không xử lý được tốt**:
- "Tất cả sinh viên đều học toán rời rạc"
- "Có ít nhất một sinh viên giỏi lập trình"
- "Với mọi x > 5 thì x² > 25"

Logic mệnh đề không thể phân tích cấu trúc bên trong → không thể suy luận "An là sinh viên ⇒ An học toán rời rạc".

**Giải pháp**: Logic vị từ (Predicate Logic / First-order Logic).

---

# Định nghĩa Vị từ

**Vị từ (Predicate)**: Là một hàm trả về giá trị chân lý, mô tả tính chất hoặc quan hệ của đối tượng.

**Ký hiệu**: P(x), Q(x,y), ...

**Ví dụ**:
- P(x): "x là sinh viên"
- Q(x,y): "x lớn hơn y"
- R(x): "x là số chẵn"

**Vị từ + giá trị cụ thể** = Mệnh đề

Ví dụ: P(An) = "An là sinh viên" → mệnh đề (có thể đúng/sai).

---

# Miền xác định (Domain)

**Miền xác định (Domain / Universe)**: Tập hợp các giá trị mà biến có thể nhận.

**Ví dụ**:
- Domain = tập sinh viên IUH
- Domain = tập số nguyên ℤ
- Domain = tập người dùng trong hệ thống

Khi viết lượng từ, phải chỉ rõ miền nếu cần.

---

# Lượng từ (Quantifiers)

**1. Lượng từ phổ dụng ∀** ("Với mọi", "Tất cả")

$$\forall x \in D, P(x)$$
Đọc: "Với mọi x thuộc D, P(x) đúng."

**Ví dụ**:
- ∀x ∈ ℤ, x + 0 = x
- ∀ sinh viên x, x phải đóng học phí

**2. Lượng từ tồn tại ∃** ("Có ít nhất một", "Tồn tại")

$$\exists x \in D, P(x)$$
Đọc: "Tồn tại x thuộc D sao cho P(x) đúng."

**Ví dụ**:
- ∃x ∈ ℤ, x² = 4
- ∃ sinh viên x, x có điểm 10 môn Toán rời rạc

---

# Phủ định lượng từ

**Quy tắc quan trọng**:

$$\neg (\forall x, P(x)) \equiv \exists x, \neg P(x)$$

$$\neg (\exists x, P(x)) \equiv \forall x, \neg P(x)$$

**Ví dụ**:
- Phủ định "Tất cả sinh viên đều học bài" = "Có sinh viên không học bài"
- Phủ định "Có sinh viên đạt điểm 10" = "Tất cả sinh viên đều không đạt điểm 10"

---

# Lượng từ lồng nhau (quan trọng - tăng chiều sâu)

**Ví dụ**:
- ∀x ∃y (x + y = 0) — Với mọi x tồn tại y...
- ∃y ∀x (x + y = 0) — Tồn tại một y mà với mọi x...

**Sự khác biệt**:
Thứ tự lượng từ quyết định ý nghĩa logic. Đổi chỗ có thể thay đổi hoàn toàn chân trị.

**Trong lập trình & CSDL (nâng cao)**:
- ∀x ∃y : "Mọi user có ít nhất một session" → dùng EXISTS trong subquery.
- ∃y ∀x : Rất mạnh, thường xuất hiện trong "có một cấu hình áp dụng cho tất cả".

```python
# ∀ user ∃ permission
all(any(u.has_perm(p) for p in permissions) for u in users)
```

**Chứng minh / Phủ định phức tạp**:
Khi phủ định lượng từ lồng, phải đổi tất cả lượng từ và phủ định vị từ.

---

# Ứng dụng trong CSDL

**SQL** sử dụng lượng từ ngầm:

```sql
-- ∀ sinh viên có điểm >= 5
SELECT * FROM students WHERE score >= 5;

-- ∃ sinh viên có điểm 10
SELECT * FROM students WHERE score = 10;
```

**Phủ định trong SQL**:
- `NOT EXISTS` thường dùng để diễn đạt ∀ không tồn tại.

---

# Thực hành 1 (8 phút)

Viết vị từ và lượng từ:

1. "Tất cả số chẵn đều chia hết cho 2"
2. "Có một số nguyên tố lớn hơn 100"
3. "Với mọi x, nếu x > 0 thì tồn tại y sao cho y = 1/x"

---

# Thực hành 2 (10 phút)

Phủ định các mệnh đề sau:

1. ∀x (P(x) → Q(x))
2. ∃x (P(x) ∧ ¬Q(x))
3. ∀x ∃y (x + y > 0)

---

# Tóm tắt Tiết 7

- Vị từ = hàm chân lý có biến
- ∀ = với mọi | ∃ = tồn tại
- Phủ định lượng từ: đổi lượng từ + phủ định vị từ
- Thứ tự lượng từ ảnh hưởng ý nghĩa
- Rất mạnh trong mô hình hóa yêu cầu phần mềm và truy vấn CSDL

---

# Bài tập ôn tập (1/2)

1. Viết: "Mọi hàm liên tục trên đoạn đóng đều đạt cực đại."

2. Phủ định: "Tồn tại thuật toán sắp xếp O(1)."

3. Viết vị từ + lượng từ: "Mọi user active có ít nhất 1 quyền."

---

# Bài tập ôn tập (2/2)

4. Phân tích khác biệt: ∀x ∃y P(x,y) vs ∃y ∀x P(x,y)

5. Viết SQL: "Không có sinh viên điểm dưới 0."

---

# Tiết sau

**Ôn tập + Tập hợp**

- Ôn lại logic + chứng minh
- Lý thuyết tập hợp cơ bản
- Biểu diễn tập hợp
- Phép toán trên tập hợp

---

# Câu hỏi?

**Tiết 8**: Ôn + Tập hợp + Phương pháp đếm