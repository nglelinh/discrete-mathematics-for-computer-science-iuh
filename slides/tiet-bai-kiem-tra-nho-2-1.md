---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 1500
enableTimeBar: true
---

## Bài kiểm tra nhỏ số 2

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

a) Mật khẩu gồm **2 ký tự**: ký tự 1 là **chữ cái in hoa** (26 chữ), ký tự 2 là **chữ số** (0–9). Cho phép lặp. Có bao nhiêu mật khẩu?

b) Chọn **một** món: hoặc 1 trong **4** món khai vị, hoặc 1 trong **5** món chính. Có bao nhiêu cách chọn?

---

## Câu 2 (2 điểm)

**Hoán vị & Tổ hợp** (tiết 17)

a) Tính $$P(9, 3)$$.

b) Tính $$C(9, 3)$$.

c) Không tính số, chỉ **giải thích ngắn** tại sao $$C(9, 3) = C(9, 6)$$.

---

## Câu 3 (2 điểm)

**Tổ hợp & Nhị thức** (tiết 17, 20)

Có bao nhiêu **xâu nhị phân** độ dài 10 có **đúng 4** bit 1?

- Ghi công thức dùng
- Tính kết quả cuối cùng

---

## Câu 4 (2 điểm)

**Hoán vị vòng tròn & Tổ hợp lặp** (tiết 17, 18)

a) Có bao nhiêu **cách xếp 8 người quanh bàn tròn**? *(Không phân biệt vị trí quay vòng.)*

b) Phân phối **6 viên kẹo** vào **3 hộp** *(có lặp, hộp có thể rỗng)*. Có bao nhiêu cách?

---

## Câu 5 (2 điểm)

**Bao hàm–loại trừ, Chuồng bồ câu & Nhị thức** (tiết 19–21)

a) **Nguyên lý chuồng bồ câu:** Trong 25 người, chứng minh ít nhất 3 người sinh cùng tháng. *(Ghi số chuồng, số bồ câu, và kết luận.)*

b) Trong lớp 100 sinh viên: 40 học Toán, 35 học Lý, 30 học Hóa. Biết 15 học cả Toán–Lý, 10 học cả Toán–Hóa, 8 học cả Lý–Hóa, 5 học cả ba môn. Tính số SV học **ít nhất một** môn.

c) Tìm **hệ số** của $$x^{4} y^{2}$$ trong khai triển $$(x + y)^{6}$$.

---

## Hết giờ

**Dừng làm bài và nộp ngay.**

Kiểm tra lại:
- Họ tên, lớp, MSSV
- Số thứ tự câu hỏi
- Đáp án rõ ràng

---

## Chúc các bạn làm bài tốt!

**Kết thúc bài kiểm tra nhỏ số 2 — Đề 1**

---

## ĐÁP ÁN THAM KHẢO

**(Dành cho giảng viên — chỉ xem sau khi thu bài)**

---

## Đáp án Câu 1

a) Nhân: $$26 \times 10 = \mathbf{260}$$

b) Cộng: $$4 + 5 = \mathbf{9}$$

---

## Đáp án Câu 2

a) $$P(9,3) = \dfrac{9!}{6!} = 9 \times 8 \times 7 = \mathbf{504}$$

b) $$C(9,3) = \dfrac{9!}{3!\,6!} = \mathbf{84}$$

c) Chọn 3 phần tử để **lấy** tương đương chọn 6 phần tử để **bỏ**; mỗi tập 3 phần tử tương ứng duy nhất một tập 6 phần tử bù.

---

## Đáp án Câu 3

Chọn vị trí đặt 4 bit 1 trong 10 vị trí:

$$C(10, 4) = \dfrac{10!}{4!\,6!} = \mathbf{210}$$

---

## Đáp án Câu 4

a) Hoán vị vòng tròn: $$(8-1)! = 7! = \mathbf{5040}$$

b) Stars and bars:

$$\binom{6 + 3 - 1}{6} = \binom{8}{6} = \binom{8}{2} = \mathbf{28}$$

---

## Đáp án Câu 5

a) 12 tháng = 12 chuồng, 25 bồ câu → $$\lceil 25/12 \rceil = 3$$. Ít nhất một tháng có $$\geq 3$$ người.

b) $$|T \cup L \cup H| = 40 + 35 + 30 - 15 - 10 - 8 + 5 = \mathbf{77}$$

c) Hệ số $$x^{4} y^{2}$$: chọn 2 vị trí cho $$y$$ (hoặc 4 cho $$x$$):

$$\binom{6}{2} = \mathbf{15}$$

---

## Kết thúc chữa bài

**Bài kiểm tra nhỏ số 2 — Đề 1 hoàn tất.**
