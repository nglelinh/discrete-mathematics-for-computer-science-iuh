---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Mục tiêu tiết học

- Luyện viết **minterm / maxterm** từ bảng chân trị
- Viết **SOP** (tổng các tích) và **POS** (tích các tổng) chuẩn
- Chuyển SOP chuẩn $$\leftrightarrow$$ POS chuẩn
- Mô hình hóa yêu cầu thực tế thành hàm Boole
- Kiểm lại bằng vài bộ giá trị (vector)

---

## Ôn nhanh — SOP (tổng các tích)

**SOP chuẩn** = OR các minterm tại hàng $$F = 1$$.

**Quy tắc minterm từ một hàng**:
1. Biến = **0** → viết bù ($$x'$$)
2. Biến = **1** → viết nguyên ($$x$$)
3. AND tất cả litera

SOP chuẩn: tổng các minterm tại hàng $$F=1$$

---

## Ôn nhanh — POS (tích các tổng)

**POS chuẩn** = AND các maxterm tại hàng $$F = 0$$.

**Quy tắc maxterm** (ngược minterm):
1. Biến = **1** → bù
2. Biến = **0** → nguyên
3. OR tất cả litera

POS chuẩn: $$F$$ là tích các maxterm tại hàng $$F=0$$

---

## Ôn nhanh — Chuyển đổi

Nếu biết các hàng $$F=1$$ thì POS chuẩn lấy maxterm tại các hàng $$F=0$$ còn lại.


**Cách 2**: SOP của $$F'$$ rồi De Morgan → POS của $$F$$.

---

## Bài 1 — Minterm (2 biến)

Cho bảng:

| $$x$$ | $$y$$ | $$F$$ |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

Viết từng minterm tại hàng $$F=1$$ và ghi SOP chuẩn.

---

## Bài 1 — Gợi ý đáp án

Hàng $$F=1$$: $$00$$, $$10$$, $$11$$ → $$m_0, m_2, m_3$$.

$$
$$F = x'y' + xy' + xy$$ (hàng **0, 2, 3**).
$$

(Có thể rút sau: $$F = x + y'$$ — tiết sau.)

---

## Bài 2 — POS từ bảng

Cùng bảng Bài 1. Viết POS chuẩn.

---

## Bài 2 — Gợi ý đáp án

Hàng $$F=0$$: chỉ $$01$$ → $$m_1$$ → maxterm $$M_1$$.

$$
Chỉ hàng **1** có $$F=0$$ → $$F = x + y'$$.
$$

Kiểm: tại $$(0,1)$$: $$0 + 0 = 0$$; các hàng khác = 1. ✓

---

## Bài 3 — Ba biến, SOP

$$F(x,y,z) = 1$$ tại $$001, 010, 100, 111$$; còn lại $$0$$.

1. Viết SOP chuẩn (liệt kê hàng $$F=1$$)
2. Khai triển SOP đầy đủ (4 hạng)

---

## Bài 3 — Gợi ý đáp án

$$F$$ bằng **1** tại các hàng **1, 2, 4, 7**

$$
F = x'y'z + x'yz' + xy'z' + xyz.
$$

---

## Bài 4 — Chuyển SOP → POS

Cho $$F$$ bằng **1** tại các hàng **1, 2, 4, 7** (3 biến).

Viết POS chuẩn (tích maxterm tại hàng $$F=0$$) và khai triển một maxterm bất kỳ.

---

## Bài 4 — Gợi ý đáp án

Hàng $$0$$: $$0,3,5,6$$.

$$
Hàng $$F=0$$: **0, 3, 5, 6** → tích các maxterm tương ứng.
$$

Ví dụ $$M_0 = x + y + z$$ (hàng $$000$$).

---

## Bài 5 — Majority 3 biến

Đèn bật khi **ít nhất hai** trong ba cảm biến $$A,B,C$$ = 1.

1. Liệt kê các hàng $$F=1$$
2. Viết SOP chuẩn (liệt kê hàng $$F=1$$)
3. (Tuỳ chọn) đoán dạng rút: $$AB + BC + AC$$

---

## Bài 5 — Gợi ý đáp án

Hàng $$F=1$$: $$011, 101, 110, 111$$ → $$m_3, m_5, m_6, m_7$$.

$$
$$F$$ bằng **1** tại các hàng **3, 5, 6, 7**.
$$

Rút gọn (tiết 37): $$F = AB + BC + AC$$.

---

## Bài 6 — Từ code sang hàm

```python
if (x and not y) or z:
    ...
```

1. Viết biểu thức Boole $$F(x,y,z)$$
2. Lập bảng chân trị 8 dòng
3. Viết SOP chuẩn

---

## Bài 6 — Gợi ý đáp án

$$F = xy' + z$$.

SOP chuẩn: gom mọi hàng $$F=1$$, ví dụ gồm $$m_1, m_3, m_4, m_5, m_7$$ (kiểm từng dòng).

**Lưu ý**: $$xy' + z$$ đã gọn hơn SOP chuẩn — tiết 37.

---

## Bài 7 — Đếm hàm

1. Có bao nhiêu hàm Boole **2** biến?
2. Có bao nhiêu hàm Boole **3** biến luôn bằng **0** trên mọi hàng có số bit 1 **chẵn**?

---

## Bài 7 — Gợi ý đáp án

1. $$2^{2^2} = 2^4 = 16$$ hàm.
2. 4 hàng chẵn cố định $$0$$; 4 hàng lẻ tự do → $$2^4 = 16$$ hàm.

---

## Bài 8 (thách thức) — Tự kiểm

Cho $$F$$ bằng **1** tại các hàng **0, 2, 5, 7** (3 biến).

1. Viết POS
2. Kiểm tại vector $$(1,0,1)$$: cả SOP lẫn POS phải cùng giá trị

---

## Bài 8 — Gợi ý đáp án

Các hàng $$F=0$$: **1, 3, 4, 6** → POS chuẩn là tích các maxterm tương ứng.

Tại $$101$$ ($$m_5$$): SOP có $$m_5$$ → $$F=1$$.  
POS: không nhân $$M_5$$ (vì 5 không trong list 0) → các maxterm tại 101 ≠ 0 → $$F=1$$. ✓

---

## Chiến lược làm bài hàm Boole

1. **Đọc đề** → bảng hay $$các hàng $$F=1$$ / mô tả lời?
2. **Quy ước** 0/1 và thứ tự biến $$(x,y,z)$$
3. **SOP** từ hàng 1; **POS** từ hàng 0
4. **Đối chiếu** chỉ số: $$S$$ và phần bù
5. **Thử 2–3 vector** trước khi chốt

---

## Bài tập ôn tập (mang về)

1. Viết SOP + POS cho $$F$$ bằng **1** tại các hàng **0, 1, 4, 5** (3 biến).
2. Bảng 2 biến: $$F=1$$ chỉ tại $$01$$ và $$10$$. Viết $$F$$ (XOR).
3. Mô tả: “bật khi $$A=B$$” (2 biến) → SOP và tên hàm (XNOR).
4. Từ $$F = (x+y)(x'+z)$$: lập bảng, viết $$các hàng $$F=1$$.
5. (Thách thức) Hàng **1, 2, 4, 7** có phải majority không? (kiểm bảng)

---

## Liên hệ

- Ôn lý thuyết: `tiet-31-ham-boole.md`, bài `13_02`
- Tiết sau: **phương pháp đơn giản hóa** hàm Boole
- Website: `contents/chapter13/`

---

## Câu hỏi?
