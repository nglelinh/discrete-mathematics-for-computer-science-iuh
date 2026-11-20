---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Phương pháp đơn giản hóa hàm Boole

**Toán Rời Rạc**

Tiết 37 (45 phút) — Algebra · K-map · Quine–McCluskey

---

## Mục tiêu tiết học

- Nêu **mục tiêu** rút gọn: ít hạng, ít litera, ít tầng cổng
- Áp dụng **đại số** (hấp thụ, De Morgan, đồng nhất)
- Dùng **K-map** cho 2–4 biến
- Mô tả ý **Quine–McCluskey** (bảng)
- **Chọn đúng công cụ** theo số biến

---

## Vì sao phải đơn giản hóa?

Hai biểu thức **cùng bảng chân trị** có thể khác **số cổng** rất xa.

Ví dụ:

$$
f_1 = xy + x\bar y + \bar x y
\quad\text{vs}\quad
f_2 = x + y
$$

$$f_1 \equiv f_2$$ nhưng $$f_2$$ vẽ mạch gọn hơn nhiều.

---

## Ba phương pháp (cùng mục tiêu)

| Phương pháp | Ưu | Khi dùng |
|:---|:---|:---|
| **Đại số** | Nhanh, chứng minh được | Vài hạng, tay |
| **K-map** | Trực quan | 2–4 biến |
| **Quine–McCluskey** | Hệ thống, máy làm được | Hiểu thuật toán; $$n$$ vừa |

---

## Phương pháp 1 — Đại số Boole

Dùng hằng đẳng thức (tiết 30 / bài 13.1):

- Đồng nhất: $$x + x' = 1$$, $$xx' = 0$$
- Hấp thụ: $$x + xy = x$$, $$x + x'y = x + y$$
- De Morgan: $$(x+y)' = x'y'$$
- Gom nhân tử: $$xy + xz = x(y+z)$$

**Luôn kiểm** bằng bảng hoặc vài vector.

---

## Ví dụ đại số

$$
F = xy + x\bar y + \bar x y.
$$

$$
F = x(y+\bar y) + \bar x y = x + \bar x y = x + y.
$$

**Các bước**: gom → đồng nhất → hấp thụ mở rộng.

---

## Bài tập nhanh — Đại số

Rút gọn (ghi đẳng thức dùng):

(a) $$ab + ab' + a'b$$  
(b) $$(x'+y)' + x$$  
(c) $$xy + x'z + yz$$

---

## Gợi ý đáp án — Đại số

(a) $$a + b$$  
(b) $$x$$ (De Morgan rồi hấp thụ)  
(c) $$xy + x'z$$ ($$yz$$ bị hấp thụ / kiểm bảng)

---

## Phương pháp 2 — Bản đồ Karnaugh

**Ý tưởng**: sắp bảng chân trị trên lưới **mã Gray**  
→ ô kề = minterm khác **một** bit  
→ gộp = áp dụng $$xy + xy' = x$$ bằng mắt.

---

## Quy tắc khoanh nhóm (K-map)

1. Chỉ khoanh ô **1** (và **X** nếu có)
2. Kích thước $$1,2,4,8,\ldots$$
3. Ưu tiên nhóm **lớn**
4. Được **chồng** nhóm
5. Mọi ô **1** phải được phủ ≥ 1 lần

---

## Ví dụ K-map 2 biến

$$F$$ bằng **1** tại các hàng **0, 1, 3**

- Hàng $$x=0$$ đầy → $$x'$$
- Cột $$y=1$$ → $$y$$

$$
F = x' + y
$$

---

## Ví dụ K-map 3 biến

$$F$$ bằng **1** tại các hàng **0, 2, 4, 5, 6**

Một cover hay gặp:

$$
F = z' + xy'
$$

(Tự vẽ lưới Gray $$xy$$ × $$z$$ rồi khoanh.)

---

## Don't-care trên K-map

Ký **X**: đầu ra **không quan tâm**.

- Được coi **X = 1** để **phình** nhóm
- **Không** bắt buộc phủ **X**

Ví dụ: $$F$$ bằng **1** tại các hàng **0, 1, 3**, don't-care tại **5, 7** có thể gọn hơn nếu dùng **X**.

---

## Phương pháp 3 — Quine–McCluskey

**Pha 1**: gộp mã nhị phân chỉ khác **1 bit**  
→ nguyên nhân nguyên tố (không dán/gộp thêm được).

**Pha 2**: bảng phủ  
→ chọn nguyên tố **cốt yếu** + phủ nốt các minterm bắt buộc.

= K-map viết dưới dạng **thuật toán bảng**.

---

## So sánh nhanh 3 phương pháp

| | Đại số | K-map | QM |
|:---|:---:|:---:|:---:|
| Trực quan | ★★ | ★★★ | ★ |
| Chứng minh | ★★★ | ★★ | ★★★ |
| 5–6 biến tay | khó | chật | nặng |
| Lập trình được | một phần | khó | tốt |

---

## Quy trình làm bài rút gọn (đề thi)

1. Lấy **SOP chuẩn** (hoặc bảng)
2. $$n \le 4$$ → **K-map** (nhanh)
3. Biểu thức đã gần gọn → **đại số** vài bước
4. Đề yêu cầu “bảng / nguyên nhân nguyên tố” → **QM**
5. **Kiểm** 2–3 vector so với dạng gốc

---

## Bài tập lớp 1

Rút gọn bằng **đại số**:

$$
F = ab'c + abc' + a'bc + abc
$$

(Hướng tới majority $$ab + bc + ca$$.)

---

## Bài tập lớp 2

$$F$$ bằng **1** tại các hàng **0, 1, 2, 5, 6, 7** (3 biến).

1. Vẽ K-map
2. Khoanh nhóm
3. Viết SOP tối tiểu

---

## Bài tập lớp 3

So sánh (cùng hàm):

- SOP chuẩn của $$F$$ bằng **1** tại các hàng **0, 2, 5, 7**
- Một dạng rút bạn tìm được

Đếm thô số AND + OR + NOT của hai dạng.

---

## Bài tập ôn tập (mang về)

1. Rút: $$xy + x'z + yz$$ bằng đại số + kiểm bảng.
2. K-map: **1** tại các hàng **0, 2, 4, 5, 6, 7** → SOP tối tiểu.
3. Giải thích 3 câu: khi nào **không** nên K-map tay?
4. QM (phác): liệt kê bước pha 1 cho **1** tại các hàng **0, 1, 2, 3** (2 biến).
5. (Thách thức) $$F$$ bằng **1** tại các hàng **1, 2, 5**, don't-care tại **0, 7** — dùng don't-care.

---

## Liên hệ

- Tiết 32–34: cổng, K-map, QM chi tiết  
- Tiết 36: luyện SOP/POS  
- Tiết 38: **mạch** từ biểu thức đã rút  
- Bài `13_03`–`13_05` trên website

---

## Câu hỏi?
