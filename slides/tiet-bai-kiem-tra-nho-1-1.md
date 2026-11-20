---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 1500
enableTimeBar: true
---

## Bài kiểm tra nhỏ - Đề 1

**Toán Rời Rạc cho Khoa học Máy tính**

Tiết 1, 2, 3 — Thời gian: **25 phút**

---

## Thông tin bài kiểm tra

- **Thời gian làm bài:** 25 phút
- **Hình thức:** Tự luận ngắn (viết trên giấy)
- **Không được sử dụng:** tài liệu, điện thoại, máy tính
- **Tổng điểm:** 10 điểm

---

## Hướng dẫn

- Đọc kỹ đề trước khi làm
- Viết rõ ràng, dùng ký hiệu logic chuẩn ($p, q, \land, \lor, \to, \neg ...$)
- Khi làm bảng chân trị: liệt kê theo thứ tự nhị phân
- Kiểm tra lại đáp án trước khi nộp

**Phân bổ thời gian gợi ý:** ~4–6 phút / câu

---

## Phạm vi kiến thức

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

## Câu 1 (2 điểm)

Xác định câu nào **là mệnh đề**. Nếu là mệnh đề, cho biết giá trị chân lý (T hoặc F) khi có thể xác định được:

a) "Hà Nội là thủ đô của Việt Nam."
b) "Hãy nộp bài tập vào cuối tuần!"
c) "$x^{2} + 1 = 0$" (với $x$ là biến chưa gán giá trị)
d) "Mọi số nguyên tố lớn hơn 2 đều là số lẻ."

---

## Câu 2 (2 điểm)

Đặt ký hiệu cho các mệnh đề sơ cấp rồi viết biểu thức logic:

> "Hệ thống cho phép người dùng tải tài liệu nếu **đã đăng nhập** và (**tài khoản còn hạn** hoặc **có quyền đặc biệt**)."

---

## Câu 3 (2 điểm)

Cho $p = \text{T}$, $q = \text{F}$, $r = \text{T}$. Tính giá trị chân lý:

a) $\neg q \lor (p \land r)$

b) $(p \to q) \leftrightarrow \neg r$

c) $\neg (p \lor q) \to r$

---

## Câu 4 (2 điểm)

Lập **bảng chân trị đầy đủ** (8 dòng) cho biểu thức sau:

$$(p \lor q) \to (\neg p \lor r)$$

Yêu cầu:
- Liệt kê $p, q, r$ theo thứ tự nhị phân (000 → 111)
- Tính từng cột trung gian nếu cần
- Cột cuối cùng là kết quả

---

## Câu 5 (2 điểm)

a) Biểu thức $p \lor \neg p$ thuộc loại nào?  
   (Tautology / Contradiction / Contingency). Giải thích ngắn gọn.

b) Dùng luật **De Morgan**, viết biểu thức tương đương (không có phủ định ở ngoài):

$$\neg \bigl( p \land (q \lor r) \bigr)$$

c) Chứng minh tương đương logic bằng **các phép biến đổi** (ghi rõ tên luật ở mỗi bước; **không** dùng bảng chân trị):

$$ (p \land q) \to r \equiv p \to (q \to r) $$

---

## Hết giờ

**Dừng làm bài và nộp ngay.**

Kiểm tra lại:
- Họ tên, lớp, MSSV
- Số thứ tự câu hỏi
- Đáp án rõ ràng

---

## Chúc các bạn làm bài tốt!

**Kết thúc bài kiểm tra nhỏ - Đề 1**

---

## ĐÁP ÁN THAM KHẢO

**(Dành cho giảng viên — chỉ xem sau khi thu bài)**

---

## Đáp án Câu 1

a) **Mệnh đề** → **T**

b) **Không** (mệnh lệnh)

c) **Không** (phụ thuộc biến $x$)

d) **Mệnh đề** → **T**

---

## Đáp án Câu 2

- $p$: đã đăng nhập
- $q$: tài khoản còn hạn
- $r$: có quyền đặc biệt

**Biểu thức:** $p \land (q \lor r)$

---

## Đáp án Câu 3

$p=\text{T}$, $q=\text{F}$, $r=\text{T}$:

a) $\neg q \lor (p \land r) = \text{T} \lor \text{T} = \textbf{T}$

b) $(p \to q) \leftrightarrow \neg r = \text{F} \leftrightarrow \text{F} = \textbf{T}$

c) $\neg(p \lor q) \to r = \text{F} \to \text{T} = \textbf{T}$

---

## Đáp án Câu 4

$(p \lor q) \to (\neg p \lor r) \equiv \neg p \lor \neg q \lor r$

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

→ Sai duy nhất tại **p=T, q=T, r=F**.

---

## Đáp án Câu 5

a) **Tautology** — luôn đúng vì $p$ và $\neg p$ không thể cùng sai.

b) $\neg p \lor (\neg q \land \neg r)$

c) Vế trái:

$(p \land q) \to r = \neg(p \land q) \lor r$ *(kéo theo)*

$= (\neg p \lor \neg q) \lor r$ *(De Morgan)*

$= \neg p \lor \neg q \lor r$ *(kết hợp)*

Vế phải:

$p \to (q \to r) = \neg p \lor (\neg q \lor r)$ *(kéo theo ×2)*

$= \neg p \lor \neg q \lor r$ *(kết hợp)*

→ **Tương đương**.

---

## Kết thúc chữa bài

**Bài kiểm tra nhỏ Đề 1 hoàn tất.**
