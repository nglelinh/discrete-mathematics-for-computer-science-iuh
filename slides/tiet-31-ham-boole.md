---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Hàm Boole và Dạng chuẩn

**Toán Rời Rạc** · Chương 13 · Bài 13.2

Tiết 31 (45 phút)

---

## Mục tiêu tiết học

- Định nghĩa hàm Boole; đếm $$2^{2^{n}}$$
- Bảng chân trị
- Minterm, maxterm
- **SOP (tổng các tích)** / **POS (tích các tổng)** chuẩn
- Chuyển SOP ↔ POS; majority

---

## 1. Hàm Boole

$$
F:\{0,1\}^{n}\to\{0,1\}
$$

Hai hàm bằng nhau  
⟺ cùng giá trị trên **mọi** bộ đầu vào

---

## Đếm số hàm

Số hàm Boole $$n$$ biến:

$$
2^{2^{n}}
$$

| $$n$$ | Số hàm |
|:---:|:---:|
| 2 | 16 |
| 3 | 256 |
| 4 | > 65 000 |

---

## Ba cách biểu diễn

1. **Bảng chân trị** — $$2^{n}$$ dòng  
2. **Biểu thức đại số** — $$+$$, $$\cdot$$, $$'$$  
3. **Dạng chuẩn** — SOP / POS đầy đủ  

Biểu thức = cách **nén** bảng

---

## Thuật ngữ (1)

| Tên | Nghĩa |
|:---|:---|
| **Từ đơn** | Litera $$x$$ / $$\bar x$$ |
| **Đơn thức** | Tích các từ đơn |
| **Từ tối tiểu** | Minterm (đúng $$n$$ litera) |

---

## Thuật ngữ (2)

| Tên | Nghĩa |
|:---|:---|
| **Công thức đa thức** | SOP, chưa nhất thiết chuẩn |
| **Dạng nối rời chính tắc** | SOP chuẩn = $$các hàng $$F=1$$ |
| **Công thức đa thức tối tiểu** | SOP gọn nhất |

---

## 2. Minterm

**Minterm** $$m_{k}$$: tích đúng $$n$$ litera  
= **1** đúng **một** hàng

**Quy tắc từ hàng:**

- biến = **0** → **bù**
- biến = **1** → **nguyên**
- AND tất cả

---

## Bảng minterm 2 biến

| $$x$$ | $$y$$ | Minterm | |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x'y'$$ | $$m_{0}$$ |
| 0 | 1 | $$x'y$$ | $$m_{1}$$ |
| 1 | 0 | $$xy'$$ | $$m_{2}$$ |
| 1 | 1 | $$xy$$ | $$m_{3}$$ |

---

## SOP (tổng các tích) chuẩn

Hàng $$F=1$$ → minterm → OR

SOP chuẩn = tổng các minterm tại hàng $$F=1$$

Còn gọi: *dạng nối rời chính tắc* / DNF đầy đủ

---

## Ví dụ SOP — 3 biến

$$F=1$$ tại $$001$$, $$010$$, $$100$$, $$111$$:

$$F$$ bằng **1** tại hàng **1, 2, 4, 7**

$$
=x'y'z+x'yz'+xy'z'+xyz
$$

---

## Hai cách lập SOP chuẩn

**Cách A — từ bảng**  
Hàng $$F=1$$ → minterm → OR

**Cách B — khai triển**  
Đơn thức thiếu $$x_{i}$$ → nhân $$(x_{i}+\bar x_{i})$$

---

## Ví dụ Cách B

$$f(x,y)=x+\bar y$$

- $$x(y+\bar y)=xy+x\bar y$$
- $$\bar y(x+\bar x)=x\bar y+\bar x\bar y$$
- Gộp: hàng **0, 2, 3**

---

## 3. Maxterm

**Maxterm** $$M_{k}$$: tổng đúng $$n$$ litera  
= **0** đúng **một** hàng

**Quy tắc** (ngược minterm):

- biến = **1** → **bù**
- biến = **0** → **nguyên**
- OR tất cả

---

## Bảng maxterm 2 biến

| $$x$$ | $$y$$ | Maxterm | |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x+y$$ | $$M_{0}$$ |
| 0 | 1 | $$x+y'$$ | $$M_{1}$$ |
| 1 | 0 | $$x'+y$$ | $$M_{2}$$ |
| 1 | 1 | $$x'+y'$$ | $$M_{3}$$ |

---

## POS (tích các tổng) chuẩn

Hàng $$F=0$$ → maxterm → AND

$$
POS chuẩn = tích các maxterm tại hàng $$F=0$$
$$

---

## Ví dụ POS

Cùng $$F$$ bằng **1** tại hàng **1, 2, 4, 7**  
→ hàng 0: $$0,3,5,6$$

$$
POS: maxterm tại hàng **0, 3, 5, 6**
$$

$$
=(x+y+z)(x+y'+z')(x'+y+z')(x'+y'+z)
$$

---

## SOP vs POS

| | SOP | POS |
|:---|:---|:---|
| Nhìn | chỗ $$F=1$$ | chỗ $$F=0$$ |
| Khối | minterm | maxterm |
| Mạch | AND–OR | OR–AND |

Hai dạng **cùng một hàm**

---

## Chuyển SOP ↔ POS

**Cách 1 — chỉ số**

Các hàng $$F=1$$ → các hàng $$F=0$$ là phần còn lại (POS = tích maxterm)

**Cách 2 — phủ định**

SOP của $$F'$$ + De Morgan → POS của $$F$$

---

## 4. Majority (bỏ phiếu)

3 phiếu: $$f=1$$ khi **≥ 2** phiếu = 1

$$f$$ bằng **1** tại hàng **3, 5, 6, 7**

Sau rút gọn: $$f=xy+xz+yz$$

---

## Bảng majority (tóm)

| Số bit 1 | $$f$$ |
|:---:|:---:|
| 0, 1 | 0 |
| 2, 3 | 1 |

Hàng $$f=1$$: 011, 101, 110, 111

---

## Hàm 2 biến quen thuộc

| Hàm | Biểu thức |
|:---|:---|
| AND / OR | $$xy$$, $$x+y$$ |
| XOR | $$x'y+xy'$$ |
| XNOR | $$xy+x'y'$$ |
| NAND / NOR | $$(xy)'$$, $$(x+y)'$$ |

---

## 5. SOP chuẩn → tối tiểu

SOP chuẩn **đúng** nhưng thường **dài**

**Công thức đa thức tối tiểu**  
= ít hạng / ít litera, cùng bảng chân trị

---

## Quy trình rút gọn

1. Lập SOP chuẩn (bảng hoặc Cách B)
2. Rút: đại số · K-map · QM
3. Kiểm lại bảng

→ tiết 32–34

---

## Ứng dụng ngắn

```python
def majority(a, b, c):
    return (a and b) or (b and c) or (a and c)
```

`if` / SQL `WHERE` = hàm Boole  
→ chuẩn hóa rồi tối ưu

---

## Thực hành 1

$$F=1$$ tại $$(0,1)$$ và $$(1,0)$$

a) SOP chuẩn  
b) POS chuẩn  
c) Hàm nào?

---

## Thực hành 2

≥ 2 trong 3 cảm biến $$A,B,C$$ bật

Bảng → $$các hàng $$F=1$$ → $$AB+BC+AC$$

---

## Tóm tắt Tiết 31

- $$F:\{0,1\}^{n}\to\{0,1\}$$; $$2^{2^{n}}$$ hàm
- Minterm → **SOP chuẩn**
- Maxterm → **POS chuẩn**
- Chuyển SOP ↔ POS
- Majority → $$xy+xz+yz$$

---

## Liên hệ

**Edge case**: hàng $$00$$ = $$x'y'$$, không phải $$xy$$

**Tiết 32** — cổng + rút đại số  
**Tiết 33–34** — K-map, QM

---

## Bài tập ôn (1)

1. Số hàm Boole 3 biến?
2. Hàng **2, 3, 5, 7**: viết SOP + POS
3. Hàng $$F=1$$: **0, 2, 5, 7** — viết POS chuẩn

---

## Bài tập ôn (2)

4. Nhiệt cao **và** (cửa mở **hoặc** quạt tắt)
5. Số hàm 3 biến luôn 0 trên hàng bit 1 **chẵn**?
6. *(Tuỳ chọn)* $$f=\bar x+\bar y z$$ → SOP chuẩn (Cách B)
