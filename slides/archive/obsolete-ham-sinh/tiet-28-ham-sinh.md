---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Hàm sinh — Giới thiệu

**Toán Rời Rạc**

Tiết 28 (45 phút) — Generating Functions

---

## Mục tiêu tiết học

- Định nghĩa hàm sinh thông thường (ordinary GF)
- Hiểu chuỗi lũy thừa hình thức và ký hiệu hệ số
- Thao tác cơ bản: cộng, nhân, dịch chỉ số
- Dùng hàm sinh để đếm dãy và cấu hình
- Chuẩn bị nền cho giải hệ thức truy hồi (tiết 29)

---

## Ý tưởng cốt lõi

**Hàm sinh** (Generating Function) **gói cả dãy** $$a_0, a_1, a_2, \ldots$$ vào **một biểu thức** duy nhất.

**Tư duy CS**: Đổi biểu diễn — giống chọn cấu trúc dữ liệu phù hợp trước khi xử lý.

**Euler** (thế kỷ XVIII) tiên phong dùng chuỗi lũy thừa trong tổ hợp.

---

## Định nghĩa — Hàm sinh thông thường

Cho dãy $$\{a_n\}_{n \ge 0}$$. **Hàm sinh thông thường** (ordinary GF):

$$G(x) = \sum_{n=0}^{\infty} a_n x^{n} = a_0 + a_1 x + a_2 x^{2} + \cdots$$

**Ký hiệu hệ số**: $$[x^{n}]G(x) = a_n$$ — hệ số của $$x^{n}$$ trong khai triển.

---

## Chuỗi lũy thừa hình thức

Trong toán rời rạc, ta xem $$G(x)$$ là **chuỗi lũy thừa hình thức** (formal power series).

**Quan trọng**: Không cần xét miền hội tụ — chỉ quan tâm **quy tắc trên hệ số**.

**Ví dụ hội tụ** (tham khảo): $$1 + x + x^{2} + \cdots = \frac{1}{1-x}$$ khi $$|x| < 1$$.

---

## Ví dụ 1: Dãy hằng

Dãy $$a_n = 2$$ với mọi $$n \ge 0$$:

$$G(x) = 2 + 2x + 2x^{2} + \cdots = 2\sum_{n \ge 0} x^{n} = \frac{2}{1-x}$$

**Đọc ngược**: Hệ số của $$x^{n}$$ trong $$\frac{2}{1-x}$$ là 2.

---

## Ví dụ 2: Dãy tự nhiên

Dãy $$a_n = n$$ ($$n \ge 1$$), $$a_0 = 0$$:

$$\sum_{n \ge 1} n x^{n} = \frac{x}{(1-x)^{2}}$$

**Ý nghĩa**: Công thức chuẩn cho dãy $$0, 1, 2, 3, \ldots$$

---

## Ví dụ 3: Dãy nhị phân

Dãy $$1, 1, 1, 1, \ldots$$ (mọi hệ số bằng 1):

$$G(x) = \frac{1}{1-x}$$

**Liên hệ**: Mỗi lần chọn 0 hoặc 1 đơn vị → tương ứng nhân thừa số $$(1 + x)$$.

---

## Phép toán cơ bản (1)

**Cộng**: Nếu $$F(x) = \sum a_n x^{n}$$, $$G(x) = \sum b_n x^{n}$$ thì

$$F(x) + G(x) = \sum (a_n + b_n) x^{n}$$

**Nhân hằng số**: $$c \cdot G(x) = \sum (c \cdot a_n) x^{n}$$

**Ứng dụng**: Gộp nhiều cách đếm thành một hàm sinh.

---

## Phép toán cơ bản (2)

**Dịch chỉ số** — nhân với $$x^{k}$$:

$$x^{k} \cdot G(x) = \sum_{n \ge k} a_{n-k} x^{n}$$

**Ý nghĩa**: $$a_{n-1}$$, $$a_{n-2}$$ trong truy hồi → nhân $$x$$, $$x^{2}$$ trên $$G(x)$$.

**Đạo hàm hình thức**: $$G'(x) = \sum_{n \ge 1} n a_n x^{n-1}$$.

---

## Định lý — Nhân chuỗi và đếm

Nếu $$A(x) = \sum a_n x^{n}$$, $$B(x) = \sum b_n x^{n}$$ thì

$$A(x) \cdot B(x) = \sum_{n \ge 0} \left(\sum_{k=0}^{n} a_k b_{n-k}\right) x^{n}$$

**Hệ số của $$x^{n}$$** = số cách đạt tổng $$n$$ từ hai nguồn độc lập.

---

## Ứng dụng đếm — Chọn không giới hạn

Mỗi loại vật chọn **0, 1, 2, …** lần → hàm sinh:

$$1 + x + x^{2} + \cdots = \frac{1}{1-x}$$

**$$n$$ loại** độc lập:

$$\left(\frac{1}{1-x}\right)^{n} = \frac{1}{(1-x)^{n}}$$

Hệ số $$x^{k}$$: số cách chọn tổng $$k$$ vật (có lặp, không phân biệt thứ tự).

---

## Ví dụ đếm — Phân phối tiền xu

Có xu 1₫ và 2₫, đếm số cách đổi đúng $$n$$₫:

$$\frac{1}{1-x} \cdot \frac{1}{1-x^{2}}$$

Hệ số của $$x^{n}$$ trong tích = số cách phân rã $$n$$.

**Tư duy**: Mỗi thừa số mã hóa một lựa chọn.

---

## Ứng dụng trong CNTT

```python
def coeffs(seq, n=5):
    terms = [f"{a}x^{i}" if i else str(a)
             for i, a in enumerate(seq[:n])]
    return " + ".join(terms)

print(coeffs([1, 1, 1, 1]))  # → 1 + 1x^{1} + 1x^{2} + 1x^{3}
```

**Ứng dụng**: Phân tích thuật toán, sinh cấu hình, mô hình xác suất rời rạc.

---

## Thực hành 1

Tìm hàm sinh của các dãy:

1. $$a_n = 3^{n}$$
2. $$a_n = (-1)^{n}$$
3. $$a_n = 1$$ nếu $$n$$ chẵn, $$a_n = 0$$ nếu $$n$$ lẻ

**Gợi ý**: Dùng $$\frac{1}{1-rx}$$ và tách chẵn/lẻ.

---

## Thực hành 2

Có 3 loại tem (1₫, 2₫, 5₫), chọn không giới hạn.

Viết hàm sinh tổng giá trị $$n$$ và giải thích hệ số $$x^{10}$$.

---

## Tóm tắt Tiết 28

- **Hàm sinh**: $$G(x) = \sum a_n x^{n}$$, $$[x^{n}]G(x) = a_n$$
- **Chuỗi hình thức**: thao tác hệ số, không cần hội tụ
- **Cộng, nhân, dịch** phản ánh cấu trúc đếm và truy hồi
- **Nhân chuỗi** = tích tổ hợp (convolution) — cốt lõi bài đếm

---

## Liên hệ

**Định lý chính**: Hệ số của $$x^{n}$$ trong tích các GF = số cách ghép cấu hình.

**Edge case**: Chuỗi vô hạn hình thức — chỉ thao tác hệ số hữu hạn.

**Liên hệ**: Hàm sinh ↔ Truy hồi (tiết 29) ↔ Tổ hợp ↔ Phân tích thuật toán.

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Định nghĩa hàm sinh thông thường và giải thích $$[x^{n}]$$.

2. **Tính toán**: Tìm GF của $$a_n = 5 \cdot 2^{n}$$.

3. **Đếm**: Viết GF cho số cách chọn $$k$$ quả từ 2 loại táo (có lặp).

---

## Bài tập ôn tập (2/2)

4. **Chứng minh**: Giải thích vì sao nhân $$G(x)$$ với $$x$$ tương ứng dịch dãy sang phải.

5. **Bài 5**: Dùng GF đếm số nghiệm không âm của $$x_1 + x_2 + x_3 = 7$$.
