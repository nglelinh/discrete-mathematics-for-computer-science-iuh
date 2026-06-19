---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 1500
enableTimeBar: true
---

# Bài kiểm tra nhỏ

**Toán Rời Rạc cho Khoa học Máy tính — IUH**

Tiết 1, 2, 3 — Thời gian: **25 phút**

---

# Thông tin bài kiểm tra

- **Thời gian làm bài:** 25 phút
- **Hình thức:** Tự luận ngắn (viết trên giấy)
- **Không được sử dụng:** tài liệu, điện thoại, máy tính
- **Tổng điểm:** 10 điểm

---

# Hướng dẫn

- Đọc kỹ đề trước khi làm
- Viết rõ ràng, dùng ký hiệu logic chuẩn ($p, q, \land, \lor, \to, \neg ...$)
- Khi làm bảng chân trị: liệt kê theo thứ tự nhị phân
- Kiểm tra lại đáp án trước khi nộp

**Phân bổ thời gian gợi ý:** ~4–6 phút / câu

---

# Phạm vi kiến thức

**Tiết 1**
- Giới thiệu Toán rời rạc & vai trò trong CNTT
- Logic và suy luận hình thức

**Tiết 2**
- Định nghĩa mệnh đề
- Mệnh đề sơ cấp vs phức hợp
- Giá trị chân lý T / F
- Gödel (tổng quát)

**Tiết 3**
- 6 phép toán logic
- Bảng chân trị
- Tautology, Contradiction, Contingency
- Tương đương logic & luật (De Morgan, Bù, Phân phối...)

---

# Câu 1 (2 điểm)

Xác định câu nào **là mệnh đề**. Nếu là mệnh đề, cho biết giá trị chân lý (T hoặc F) khi có thể xác định được:

a) "Hà Nội là thủ đô của Việt Nam."

b) "Hãy nộp bài tập vào cuối tuần!"

c) "$x^2 + 1 = 0$" (với $x$ là biến chưa gán giá trị)

d) "Mọi số nguyên tố lớn hơn 2 đều là số lẻ."

---

# Câu 2 (2 điểm)

Đặt ký hiệu cho các mệnh đề sơ cấp rồi viết biểu thức logic:

> "Hệ thống cho phép người dùng tải tài liệu nếu **đã đăng nhập** và (**tài khoản còn hạn** hoặc **có quyền đặc biệt**)."

---

# Câu 3 (2 điểm)

Cho $p = \text{T}$, $q = \text{F}$, $r = \text{T}$. Tính giá trị chân lý:

a) $\neg q \lor (p \land r)$

b) $(p \to q) \leftrightarrow \neg r$

c) $\neg (p \lor q) \to r$

---

# Câu 4 (2 điểm)

Lập **bảng chân trị đầy đủ** (8 dòng) cho biểu thức sau:

$$(p \lor q) \to (\neg p \lor r)$$

Yêu cầu:
- Liệt kê $p, q, r$ theo thứ tự nhị phân (000 → 111)
- Tính từng cột trung gian nếu cần
- Cột cuối cùng là kết quả

---

# Câu 5 (2 điểm)

a) Biểu thức $p \lor \neg p$ thuộc loại nào?  
   (Tautology / Contradiction / Contingency). Giải thích ngắn gọn.

b) Dùng luật **De Morgan**, viết biểu thức tương đương (không có phủ định ở ngoài):

$$\neg \bigl( p \land (q \lor r) \bigr)$$

c) Chứng minh (bằng bảng chân trị ngắn hoặc giải thích):

$$p \to q \equiv \neg p \lor q$$

---

# Hết giờ

**Dừng làm bài và nộp ngay.**

Kiểm tra lại:
- Họ tên, lớp, MSSV
- Số thứ tự câu hỏi
- Đáp án rõ ràng

---

# Chúc các bạn làm bài tốt!

**Kết thúc bài kiểm tra nhỏ - Tiết 1, 2, 3**

---

# ĐÁP ÁN THAM KHẢO

**(Dành cho giảng viên — chỉ xem sau khi thu bài)**

---

# Đáp án Câu 1

a) **Là mệnh đề** → **T**

b) **Không phải** (mệnh lệnh / câu cảm thán)

c) **Không phải** (phụ thuộc biến $x$ chưa gán)

d) **Là mệnh đề** → **T**

---

# Đáp án Câu 2

**Ký hiệu:**

- $p$: đã đăng nhập
- $q$: tài khoản còn hạn
- $r$: có quyền đặc biệt

**Biểu thức logic:** $p \land (q \lor r)$

---

# Đáp án Câu 3

Cho $p = \text{T}$, $q = \text{F}$, $r = \text{T}$:

a) $\neg q \lor (p \land r)$  
   $= \text{T} \lor (\text{T} \land \text{T}) = \text{T} \lor \text{T} = \textbf{T}$

b) $(p \to q) \leftrightarrow \neg r$  
   $= (\text{F}) \leftrightarrow (\text{F}) = \textbf{T}$

c) $\neg (p \lor q) \to r$  
   $= \text{F} \to \text{T} = \textbf{T}$

---

# Đáp án Câu 4

Biểu thức: $(p \lor q) \to (\neg p \lor r)$

Tương đương: $\neg(p \lor q) \lor (\neg p \lor r) \equiv \neg p \lor \neg q \lor r$

**Kết quả cột cuối (p q r → kết quả):**

| p | q | r | Kết quả |
|:---:|:---:|:---:|:---:|
| F | F | F | T |
| F | F | T | T |
| F | T | F | T |
| F | T | T | T |
| T | F | F | T |
| T | F | T | T |
| T | T | F | **F** |
| T | T | T | T |

---

# Đáp án Câu 5

a) **Tautology** (luôn đúng với mọi gán giá trị). Phủ định của nó là contradiction.

b) $\neg p \lor (\neg q \land \neg r)$  
   hoặc $\neg p \lor \neg q \lor \neg r$

c) Bảng chân trị chứng minh:

| $p$ | $q$ | $p \to q$ | $\neg p \lor q$ |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

Hai cột **giống hệt nhau** → tương đương.

---

# Kết thúc chữa bài

**Bài kiểm tra nhỏ hoàn tất.**