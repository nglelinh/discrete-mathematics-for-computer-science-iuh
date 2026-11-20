---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Hàm số — Định nghĩa & Tính chất

**Toán Rời Rạc**

Tiết 14 (45 phút) — ch06 `06_01`, `06_02`

---

## Mục tiêu tiết học

- Định nghĩa hàm từ tập hợp; phân biệt domain, codomain, range
- Nhận biết hàm như quan hệ đặc biệt (tồn tại + duy nhất)
- Kiểm tra đơn ánh, toàn ánh, song ánh
- Hiểu vai trò domain/codomain khi xét tính chất
- Áp dụng vào API, hash, mã hóa, ML

---

## Định nghĩa Hàm số

Cho $$A, B$$. Hàm $$f: A \to B$$ gán mỗi $$x \in A$$ **đúng một** $$y \in B$$.

**Ký hiệu**:
- $$A$$: **domain** (miền xác định)
- $$B$$: **codomain** (miền đích)
- $$f(A) = \{f(x) \mid x \in A\}$$: **range** (ảnh / tập giá trị)

**Nguyên tắc**: Cùng đầu vào → cùng đầu ra. Không được "một input, nhiều output".

---

## Hàm như Quan hệ Đặc biệt

Quan hệ $$R \subseteq A \times B$$ là hàm khi:

1. **Tồn tại**: $$\forall a \in A,\ \exists b \in B,\ (a,b) \in R$$
2. **Duy nhất**: $$(a,b_1) \in R \land (a,b_2) \in R \Rightarrow b_1 = b_2$$

**Ví dụ hợp lệ**: $$R = \{(1,a),(2,b),(3,b)\}$$

**Không phải hàm**: $$S = \{(1,a),(1,b),(2,b)\}$$ — input 1 có hai output.

---

## Domain, Codomain, Range

**Ví dụ**: $$f: \mathbb{Z} \to \mathbb{Z}$$, $$f(n) = 2n$$

| Khái niệm | Giá trị |
|-----------|---------|
| Domain | $$\mathbb{Z}$$ |
| Codomain | $$\mathbb{Z}$$ |
| Range | tập số chẵn |

---

## Các cách Biểu diễn

**Công thức**: $$f(x) = 3x + 1$$

**Bảng**:

| $$x$$ | 1 | 2 | 3 |
|---:|---:|---:|---:|
| $$f(x)$$ | 4 | 7 | 10 |

**Tập cặp**: $$f = \{(1,4),(2,7),(3,10)\}$$

**Code**:
```python
def f(x):
    return 3 * x + 1
```

---

## Đơn ánh (Injective)

$$f: A \to B$$ **đơn ánh** nếu hai đầu vào khác nhau cho hai đầu ra khác nhau:

$$x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2)$$

**Dạng chứng minh**: $$f(x_1) = f(x_2) \Rightarrow x_1 = x_2$$

**Ví dụ**: $$f(x) = 2x + 3$$ trên $$\mathbb{R}$$ — đơn ánh.

**Phản ví dụ**: $$g(x) = x^{2}$$ trên $$\mathbb{R}$$ — $$g(2) = g(-2) = 4$$.

---

## Toàn ánh (Surjective)

$$f: A \to B$$ **toàn ánh** nếu mọi phần tử codomain đều có tiền ảnh:

$$\forall y \in B,\ \exists x \in A,\ f(x) = y$$

**Ví dụ**: $$f(x) = x^{3}$$ trên $$\mathbb{R} \to \mathbb{R}$$ — toàn ánh (chọn $$x = \sqrt[3]{y}$$).

**Phản ví dụ**: $$g(x) = x^{2}$$ trên $$\mathbb{R} \to \mathbb{R}$$ — không có $$x$$ cho $$g(x) = -1$$.

---

## Song ánh (Bijective)

$$f$$ **song ánh** ⟺ vừa đơn ánh vừa toàn ánh.

Thiết lập ghép cặp **một-một** giữa $$A$$ và $$B$$.

**Ví dụ**: $$f(x) = x + 5$$ trên $$\mathbb{R} \to \mathbb{R}$$

- Đơn ánh: $$x_1 + 5 = x_2 + 5 \Rightarrow x_1 = x_2$$
- Toàn ánh: với $$y$$ bất kỳ, chọn $$x = y - 5$$

---

## Domain/Codomain quyết định Tính chất

Cùng công thức $$f(x) = x^{2}$$, khác domain/codomain → khác tính chất:

| Domain → Codomain | Đơn ánh? | Toàn ánh? |
|-------------------|:--------:|:---------:|
| $$\mathbb{R} \to \mathbb{R}$$ | ✗ | ✗ |
| $$\mathbb{R} \to [0,\infty)$$ | ✗ | ✓ |
| $$[0,\infty) \to [0,\infty)$$ | ✓ | ✓ |

**Bài học**: Luôn nêu rõ domain và codomain khi kiểm tra tính chất.

---

## Định lý: Số hàm hữu hạn

**Định lý**: Số hàm từ tập $$A$$ ($$|A| = n$$) sang $$B$$ ($$|B| = m$$) là $$m^{n}$$.

**Chứng minh ý tưởng**: Mỗi $$a \in A$$ chọn độc lập một trong $$m$$ giá trị ở $$B$$ → quy tắc nhân.

---

**Hệ quả**:
- Hàm Boolean $$n$$ biến: $$2^{2^{n}}$$
- Hàm từ tập $$n$$ phần tử sang chính nó: $$n^{n}$$ (hoán vị chỉ là $$n!$$)

---

## Ứng dụng trong CNTT

- API request - response
- **Hash function**: thường **không** đơn ánh (collision)
- **Primary key**: đơn ánh từ bản ghi → khóa
- **Mã hóa khả nghịch**: cần **song ánh** (encode/decode không mất dữ liệu)
- **ML**: mô hình là hàm $$f: \text{features} \to \text{prediction}$$

---

## Thực hành 1

Xét quan hệ $$R = \{(1,2),(2,4),(3,6),(1,3)\}$$.

1. $$R$$ có phải hàm không? Giải thích.
2. Nếu bỏ $$(1,3)$$, xác định domain, codomain, range.

---

## Thực hành 2

Với $$f: \mathbb{R} \to \mathbb{R}$$, $$f(x) = 3x - 2$$:

1. Chứng minh $$f$$ đơn ánh
2. Chứng minh $$f$$ toàn ánh
3. Kết luận: $$f$$ song ánh?

---

## Thực hành 3

Giải thích ngắn:

1. Tại sao hash function tốt nên **gần** đơn ánh?
2. Tại sao serialization cần gần song ánh?
3. Một REST endpoint trả về kết quả khác nhau cho cùng request — vi phạm tính chất nào của hàm?

---

## Tóm tắt Tiết 14

- Hàm = quan hệ **tồn tại + duy nhất**
- **Đơn ánh**: không gộp hai input khác nhau
- **Toàn ánh**: phủ hết codomain
- **Song ánh**: cả hai → có thể đảo ngược (tiết 15)
- Domain/codomain **thay đổi** tính chất của cùng một công thức

---

## Liên hệ

**Điểm then chốt**: Kiểm tra đơn ánh bằng $$f(x_1)=f(x_2) \Rightarrow x_1=x_2$$.

**Liên hệ**:
- Tiết 13: hàm là quan hệ đặc biệt
- Tiết 15: song ánh ⟺ có hàm nghịch đảo

**Edge case**: Hàm lập trình có exception/I/O — không phải hàm toán học thuần túy.

---

## Bài tập ôn tập (1/2)

1. **Bài 1**: $$f: \mathbb{N} \to \mathbb{N}$$, $$f(x) = x^{2} + 1$$. Xác định range. $$f$$ có đơn ánh trên $$\mathbb{N}$$ không?

2. **Bài 2**: Tìm một hàm song ánh từ $$\{1,2,3,4\}$$ sang $$\{a,b,c,d\}$$.

3. **Bài 3**: Có bao nhiêu hàm từ $$\{1,2,3\}$$ sang $$\{0,1\}$$?

---

## Bài tập ôn tập (2/2)

4. **Bài 4**: $$g: \mathbb{Z} \to \mathbb{Z}$$, $$g(n) = n \bmod 5$$. Đơn ánh? Toàn ánh? Giải thích.

5. **Bài 5**: Thiết kế hàm băm đơn giản từ chuỗi → số nguyên. Thảo luận tại sao khó đạt song ánh trên tập chuỗi vô hạn.
