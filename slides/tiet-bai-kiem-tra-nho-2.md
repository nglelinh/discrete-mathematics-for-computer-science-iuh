---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 1500
enableTimeBar: true
---

# Bài kiểm tra nhỏ - Đề 2

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

**Tiết 3**
- 6 phép toán logic
- Bảng chân trị
- Tautology, Contradiction, Contingency
- Tương đương logic & luật (De Morgan, Bù, Phân phối, Hấp thụ...)

---

# Câu 1 (2 điểm)

Xác định câu nào **là mệnh đề**. Nếu là mệnh đề, cho biết giá trị chân lý (T hoặc F) khi có thể xác định được:

a) "5 chia hết cho 2."

b) "Bạn tên là gì?"

c) "Mọi chương trình Java đều có hàm main."

d) "Số n chia hết cho 5." (với n là biến chưa biết)

---

# Câu 2 (2 điểm)

Đặt ký hiệu cho các mệnh đề sơ cấp rồi viết biểu thức logic:

> "Cho phép cập nhật hồ sơ nếu tài khoản **đã được xác thực** và (**là tài khoản premium** hoặc **đã bật xác thực 2FA**)."

---

# Câu 3 (2 điểm)

Cho $p = \text{T}$, $q = \text{T}$, $r = \text{F}$. Tính giá trị chân lý:

a) $(p \land \neg q) \to r$

b) $p \leftrightarrow (q \lor \neg r)$

c) $\neg p \lor (q \to r)$

---

# Câu 4 (2 điểm)

Lập **bảng chân trị đầy đủ** (8 dòng) cho biểu thức sau:

$$ (p \to q) \lor (\neg q \to r) $$

Yêu cầu:
- Liệt kê $p, q, r$ theo thứ tự nhị phân (000 → 111)
- Tính từng cột trung gian nếu cần
- Cột cuối cùng là kết quả

---

# Câu 5 (2 điểm)

a) Biểu thức $p \land \neg p$ thuộc loại nào?  
   (Tautology / Contradiction / Contingency). Giải thích ngắn gọn.

b) Dùng luật **De Morgan**, viết biểu thức tương đương (không có phủ định ở ngoài):

$$ \neg (p \lor (q \land r)) $$

c) Chứng minh (bằng bảng chân trị ngắn hoặc giải thích):

$$ p \to q \equiv \neg q \to \neg p $$

---

# Hết giờ

**Dừng làm bài và nộp ngay.**

Kiểm tra lại:
- Họ tên, lớp, MSSV
- Số thứ tự câu hỏi
- Đáp án rõ ràng

---

# Chúc các bạn làm bài tốt!

**Kết thúc bài kiểm tra nhỏ - Đề 2**

---

# ĐÁP ÁN THAM KHẢO

**(Dành cho giảng viên — chỉ xem sau khi thu bài)**

---

# Đáp án Câu 1

a) **Là mệnh đề** → **F**

b) **Không phải** (câu hỏi)

c) **Là mệnh đề** → **T**

d) **Không phải** (phụ thuộc biến n)

---

# Đáp án Câu 2

**Ký hiệu:**

- $p$: tài khoản đã được xác thực
- $q$: là tài khoản premium
- $r$: đã bật xác thực 2FA

**Biểu thức logic:** $p \land (q \lor r)$

---

# Đáp án Câu 3

Cho $p = \text{T}$, $q = \text{T}$, $r = \text{F}$:

a) $(p \land \neg q) \to r$  
   $= (T \land \neg T) \to F = (F) \to F = \textbf{T}$

b) $p \leftrightarrow (q \lor \neg r)$  
   $= T \leftrightarrow (T \lor \neg F) = T \leftrightarrow T = \textbf{T}$

c) $\neg p \lor (q \to r)$  
   $= F \lor (T \to F) = F \lor F = \textbf{F}$

---

# Đáp án Câu 4

Biểu thức: $(p \to q) \lor (\neg q \to r)$

Tương đương: $\neg p \lor q \lor r$

**Kết quả cột cuối (p q r → kết quả):**

| p | q | r | Kết quả |
|:---:|:---:|:---:|:---:|
| F | F | F | T |
| F | F | T | T |
| F | T | F | T |
| F | T | T | T |
| T | F | F | **F** |
| T | F | T | T |
| T | T | F | T |
| T | T | T | T |

→**Giải thích**: Sai khi cả hai phép kéo theo đều sai:
- $p \to q$ sai khi $p=T$, $q=F$
- $\neg q \to r$ sai khi $q=F$, $r=F$

→ Chỉ xảy ra tại **p=T, q=F, r=F**.

---

# Đáp án Câu 5

a) **Contradiction** (luôn sai với mọi gán). Đây là phủ định của tautology.

b) $\neg p \land \neg(q \land r)$  
   = $\neg p \land (\neg q \lor \neg r)$

c) Bảng chứng minh tương đương (Contrapositive):

| $p$ | $q$ | $p \to q$ | $\neg q \to \neg p$ |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

Hai cột **giống hệt nhau** → tương đương.

---

# Kết thúc chữa bài

**Bài kiểm tra nhỏ Đề 2 hoàn tất.**