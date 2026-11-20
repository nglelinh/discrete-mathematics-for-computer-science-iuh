---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 1500
enableTimeBar: true
---

## Bài kiểm tra nhỏ số 2 — Đề 2

**Toán Rời Rạc cho Khoa học Máy tính**

Tiết 16, 17, 18, 19, 20, 21, 22 — Thời gian: **25 phút**

---

## Thông tin bài kiểm tra

- **Thời gian làm bài:** 25 phút
- **Hình thức:** Tự luận ngắn (viết trên giấy)
- **Không được sử dụng:** tài liệu, điện thoại, máy tính
- **Tổng điểm:** 10 điểm

---

## Hướng dẫn

- Đọc kỹ đề trước khi làm
- Viết rõ công thức ($$P(n,k)$$, $$C(n,k)$$, bù trừ, chuồng bồ câu) trước khi thay số
- Ghi giải thích ngắn khi đề yêu cầu
- Kiểm tra lại đáp án trước khi nộp

**Phân bổ thời gian gợi ý:** ~4–6 phút / câu

---

## Phạm vi kiến thức

**Tiết 16** — Nguyên lý cộng, nhân; tích Descartes; đếm cơ bản

**Tiết 17** — Hoán vị $$P(n,k)$$, tổ hợp $$C(n,k)$$, hoán vị vòng tròn

**Tiết 18** — Hoán vị lặp, tổ hợp lặp, stars and bars

**Tiết 19** — Nguyên lý bao hàm–loại trừ (2 và 3 tập)

**Tiết 20** — Hệ số nhị thức, tam giác Pascal, định lý nhị thức Newton

**Tiết 21** — Nguyên lý chuồng bồ câu (Dirichlet)

**Tiết 22** — Đếm ứng dụng CNTT (mật khẩu, collision, kiểm thử)

---

## Câu 1 (2 điểm)

**Nguyên lý cộng & nhân** (tiết 16)

a) Mã sản phẩm gồm **3 ký tự**: 2 chữ số đầu (0–9, có lặp) và 1 chữ cái in hoa cuối (26 chữ). Có bao nhiêu mã?

b) Chọn **một** cuốn sách: hoặc 1 trong **5** sách Toán, hoặc 1 trong **6** sách Lý. Có bao nhiêu cách chọn?

---

## Câu 2 (2 điểm)

**Hoán vị & Tổ hợp** (tiết 17)

a) Tính $$P(10, 4)$$.

b) Tính $$C(10, 4)$$.

c) Tính $$C(10, 6)$$ và so sánh với $$C(10, 4)$$.

---

## Câu 3 (2 điểm)

**Tổ hợp** (tiết 17)

Có bao nhiêu **xâu nhị phân** độ dài 8 có **đúng 3** bit 1?

- Ghi công thức dùng
- Tính kết quả cuối cùng

---

## Câu 4 (2 điểm)

**Hoán vị vòng tròn & Tổ hợp lặp** (tiết 17, 18)

a) Có bao nhiêu **cách xếp 7 người quanh bàn tròn**? *(Không phân biệt vị trí quay vòng.)*

b) Chọn **5 viên bi** từ **4 loại màu** *(có lặp, chỉ phân biệt loại)*. Có bao nhiêu cách?

---

## Câu 5 (2 điểm)

**Bao hàm–loại trừ, Chuồng bồ câu & Nhị thức** (tiết 19–21)

a) **Nguyên lý chuồng bồ câu:** Trong 10 người, chứng minh ít nhất 2 người sinh cùng ngày trong tuần. *(Ghi số chuồng, số bồ câu.)*

b) Trong lớp 90 sinh viên: 35 học CS, 28 học Toán, 22 học Anh. Biết 12 học cả CS–Toán, 8 học cả CS–Anh, 6 học cả Toán–Anh, 4 học cả ba môn. Tính số SV học **ít nhất một** môn.

c) Tìm **hệ số** của $$x^{2}$$ trong khai triển $$(3x + 1)^{4}$$.

---

## Hết giờ

**Dừng làm bài và nộp ngay.**

Kiểm tra lại:
- Họ tên, lớp, MSSV
- Số thứ tự câu hỏi
- Đáp án rõ ràng

---

## Chúc các bạn làm bài tốt!

**Kết thúc bài kiểm tra nhỏ số 2 — Đề 2**

---

## ĐÁP ÁN THAM KHẢO

**(Dành cho giảng viên — chỉ xem sau khi thu bài)**

---

## Đáp án Câu 1

a) Nhân: $$10 \times 10 \times 26 = \mathbf{2600}$$

b) Cộng: $$5 + 6 = \mathbf{11}$$

---

## Đáp án Câu 2

a) $$P(10,4) = \dfrac{10!}{6!} = 10 \times 9 \times 8 \times 7 = \mathbf{5040}$$

b) $$C(10,4) = \dfrac{10!}{4!\,6!} = \mathbf{210}$$

c) $$C(10,6) = \dfrac{10!}{6!\,4!} = \mathbf{210}$$ → **bằng nhau** *(tính chất đối xứng)*

---

## Đáp án Câu 3

Chọn vị trí đặt 3 bit 1 trong 8 vị trí:

$$C(8, 3) = \dfrac{8!}{3!\,5!} = \mathbf{56}$$

---

## Đáp án Câu 4

a) Hoán vị vòng tròn: $$(7-1)! = 6! = \mathbf{720}$$

b) Tổ hợp lặp (stars and bars):

$$\binom{5 + 4 - 1}{5} = \binom{8}{5} = \mathbf{56}$$

---

## Đáp án Câu 5

a) 7 ngày = 7 chuồng, 10 bồ câu → ít nhất một ngày có $$\geq 2$$ người.

b) $$|CS \cup Toán \cup Anh| = 35 + 28 + 22 - 12 - 8 - 6 + 4 = \mathbf{63}$$

c) Số hạng $$x^{2}$$: chọn 2 vị trí cho $$x$$, 2 vị trí còn lại là $$1$$:

$$\binom{4}{2} \cdot 3^{2} \cdot 1^{2} = 6 \times 9 = \mathbf{54}$$

---

## Kết thúc chữa bài

**Bài kiểm tra nhỏ số 2 — Đề 2 hoàn tất.**
