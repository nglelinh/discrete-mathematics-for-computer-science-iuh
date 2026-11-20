---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Hàm ngược & Hàm hợp

**Toán Rời Rạc**

Tiết 15 (45 phút) — ch06 `06_03`

---

## Mục tiêu tiết học

- Tính hàm hợp $$g \circ f$$ và hiểu thứ tự thực hiện
- Nắm tính kết hợp và vai trò hàm đồng nhất
- Điều kiện tồn tại hàm nghịch đảo
- Tìm $$f^{-1}$$ khi $$f$$ song ánh
- Áp dụng pipeline, mã hóa, serialization trong CNTT

---

## Hàm hợp (Composition)

Cho $$f: A \to B$$, $$g: B \to C$$. **Hàm hợp**:

$$(g \circ f)(x) = g(f(x))$$

Đọc: **"g sau f"** — tính $$f$$ trước, rồi $$g$$.

**Ví dụ**: $$f(x) = 2x + 1$$, $$g(x) = x^{2}$$

- $$(g \circ f)(x) = (2x+1)^{2}$$
- $$(f \circ g)(x) = 2x^{2} + 1$$

Hai biểu thức **thường khác nhau** — phép hợp **không giao hoán**.

---

## Điều kiện để Hợp được

Để $$g \circ f$$ xác định:

$$f(A) \subseteq \operatorname{dom}(g)$$

Mọi giá trị $$f(x)$$ phải nằm trong domain của $$g$$.

**Ví dụ**: $$f(x) = x^{2}$$ có ảnh $$[0,\infty)$$; nếu $$g(x) = \sqrt{x}$$ chỉ xác định trên $$[0,\infty)$$ thì $$g \circ f$$ hợp lệ.

**Liên hệ tiết 13**: Hàm hợp tương ứng hợp thành quan hệ giữa đồ thị ánh xạ.

---

## Tính kết hợp

Nếu các hàm hợp xác định:

$$h \circ (g \circ f) = (h \circ g) \circ f$$

**Chứng minh ý tưởng**: Với mọi $$x$$:

$$[h \circ (g \circ f)](x) = h(g(f(x))) = [(h \circ g) \circ f](x)$$

Phép hợp **có tính kết hợp** nhưng **không giao hoán**.

---

## Hàm đồng nhất

**Định nghĩa**: $$id_A: A \to A$$, $$id_A(x) = x$$

**Tính chất** (phần tử trung hòa):

$$f \circ id_A = f,\quad id_B \circ f = f$$

với $$f: A \to B$$.

**Ví dụ**: $$id_{\mathbb{R}}(x) = x$$ — "không làm gì", nhưng quan trọng trong định nghĩa nghịch đảo.

---

## Hàm nghịch đảo

$$g: B \to A$$ là **nghịch đảo** của $$f: A \to B$$ nếu:

$$g \circ f = id_A \quad \text{và} \quad f \circ g = id_B$$

Ký hiệu: $$g = f^{-1}$$.

**Định lý**: $$f$$ có nghịch đảo hai phía **⟺** $$f$$ **song ánh**.

**Ý nghĩa**: Biến đổi không mất thông tin — có thể "undo" chính xác.

---

## Tìm Hàm nghịch đảo

**Ví dụ**: $$f(x) = 3x - 2$$. Đặt $$y = 3x - 2$$, giải theo $$x$$:

$$x = \frac{y + 2}{3} \Rightarrow f^{-1}(y) = \frac{y + 2}{3}$$

Đổi biến: $$f^{-1}(x) = \frac{x + 2}{3}$$

**Kiểm tra**: $$f(f^{-1}(x)) = 3 \cdot \frac{x+2}{3} - 2 = x$$ ✓

---

## Khi nào không có Nghịch đảo?

$$f(x) = x^{2}$$ trên $$\mathbb{R} \to \mathbb{R}$$:

- Không đơn ánh: $$f(2) = f(-2) = 4$$
- Không thể đảo ngược duy nhất

**Giải pháp**: Hạn chế domain → $$f: [0,\infty) \to [0,\infty)$$ song ánh, $$f^{-1}(x) = \sqrt{x}$$.

**Bài học**: Nghịch đảo phụ thuộc domain/codomain (như tiết 14).

---

## Ứng dụng trong CNTT

**Pipeline dữ liệu** = chuỗi hàm hợp:

```python
def clean(s):
    return s.strip().lower()

def tokenize(s):
    return s.split()

result = tokenize(clean("  Discrete Math  "))
# ['discrete', 'math']
```

- **Mật mã**: encrypt/decrypt là cặp nghịch đảo
- **Serialization**: `decode(encode(x)) = x`
- **Functional programming**: ghép hàm nhỏ → chương trình lớn

```python
def compose(f, g):
    return lambda x: f(g(x))
```

---

## Thực hành 1

Cho $$f(x) = 2x$$, $$g(x) = x + 3$$.

1. Tính $$(f \circ g)(x)$$ và $$(g \circ f)(x)$$
2. Tính $$(f \circ g)(5)$$ và $$(g \circ f)(5)$$
3. Phép hợp có giao hoán không?

---

## Thực hành 2

Cho $$f(x) = 3x + 1$$ trên $$\mathbb{R} \to \mathbb{R}$$.

1. Chứng minh $$f$$ song ánh
2. Tìm $$f^{-1}(x)$$
3. Kiểm tra: $$f(f^{-1}(x)) = x$$ và $$f^{-1}(f(x)) = x$$

---

## Thực hành 3

Mô tả pipeline xử lý ảnh:

`resize` → `normalize` → `predict`

1. Viết dạng hàm hợp
2. Nếu chỉ `normalize` và `resize` có nghịch đảo, pipeline có undo hoàn toàn không?
3. Liên hệ với mã hóa AES (encrypt/decrypt).

---

## Tóm tắt Tiết 15

- **Hàm hợp**: $$(g \circ f)(x) = g(f(x))$$ — thứ tự quan trọng
- **Kết hợp**: có; **giao hoán**: không
- **Hàm đồng nhất**: phần tử trung hòa của phép hợp
- **Nghịch đảo**: tồn tại ⟺ song ánh
- **CNTT**: pipeline, encode/decode, undo

---

## Liên hệ

**Điểm then chốt**: $$f \circ g \neq g \circ f$$ — đổi thứ tự = đổi kết quả.

**Liên hệ**:
- Tiết 13: $$S \circ R$$ trên quan hệ
- Tiết 14: song ánh là điều kiện nghịch đảo
- Neural network: composition of layers

**Edge case**: Hàm nghịch đảo một phía (decode có thể mất metadata).

---

## Bài tập ôn tập (1/2)

1. **Bài 1**: $$f(x) = x - 1$$, $$g(x) = x^{2}$$. Tính $$f \circ g$$, $$g \circ f$$, $$(f \circ g)(3)$$.

2. **Bài 2**: Tìm $$f^{-1}$$ nếu $$f(x) = \frac{2x + 1}{3}$$ trên $$\mathbb{R} \to \mathbb{R}$$.

---

## Bài tập ôn tập (2/2)

4. **Bài 4**: $$h(x) = |x|$$ trên $$\mathbb{R} \to [0,\infty)$$. Có nghịch đảo không? Nếu hạn chế domain thì sao?

5. **Bài 5**: Cho pipeline `hash → mod n` trong bảng băm. Giải thích tại sao không thể có nghịch đảo hoàn toàn và ảnh hưởng đến collision.
