---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Đại số Boole — Cơ bản

**Toán Rời Rạc** · Chương 13 · Bài 13.1

Tiết 30 (45 phút)

---

## Mục tiêu tiết học

- Làm việc trên $$B=\{0,1\}$$ và **10 hằng đẳng thức**
- Định nghĩa đại số Boole + tiên đề Huntington
- Ví dụ $$P(U)$$, $$B^{n}$$
- Chứng minh: đại số **hoặc** bảng chân trị
- Phép dẫn xuất: XOR, NAND, NOR, …

---

## Bối cảnh

**George Boole** (1815–1864): đại số hóa logic

**Claude Shannon** (1937): Boole ↔ mạch relay

Mỗi lần `if` / `WHERE` / CPU đánh giá điều kiện  
→ đang dùng **đại số Boole**

---

## 1. Đại số logic $$B=\{0,1\}$$

Ba phép cơ bản:

| Phép | Ký hiệu |
|:---|:---|
| **OR** (tổng) | $$x+y$$, $$x\lor y$$ |
| **AND** (tích) | $$xy$$, $$x\land y$$ |
| **NOT** (bù) | $$x'$$, $$\bar x$$ |

---

## Ý nghĩa ba phép

| Phép | Ra **1** / **0** khi… |
|:---|:---|
| OR | ra **1** nếu ≥ 1 ngõ = **1** |
| AND | ra **0** nếu ≥ 1 ngõ = **0** |
| NOT | đảo: $$\bar 0=1$$, $$\bar 1=0$$ |

**Khác số học**: $$1+1=1$$ (OR, không phải cộng số)

---

## Bảng OR và AND

| $$x$$ | $$y$$ | $$x+y$$ | $$xy$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 |

---

## Bảng NOT

| $$x$$ | $$x'$$ |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

---

## 10 hằng đẳng thức — nhóm A

| # | Tên | Ví dụ |
|:---:|:---|:---|
| 1 | Giao hoán | $$x+y=y+x$$ |
| 2 | Kết hợp | $$(x+y)+z=x+(y+z)$$ |
| 3 | Phân phối | $$x(y+z)=xy+xz$$ |
| 4 | Bù kép | $$(x')'=x$$ |
| 5 | De Morgan | $$(x+y)'=x'y'$$ |

---

## Phân phối **hai chiều**

$$
x(y+z)=xy+xz
$$

$$
x+(yz)=(x+y)(x+z)
$$

Chiều thứ hai **không** có trong số học thường  
→ vừa sức mạnh, vừa bẫy

---

## 10 hằng đẳng thức — nhóm B

| # | Tên | Ví dụ |
|:---:|:---|:---|
| 6 | Lũy đẳng | $$x+x=x$$ |
| 7 | Trung hòa | $$x+0=x$$, $$x\cdot1=x$$ |
| 8 | Phần tử bù | $$x+x'=1$$, $$xx'=0$$ |
| 9 | Nuốt | $$x+1=1$$, $$x\cdot0=0$$ |
| 10 | Hấp thụ | $$x+xy=x$$ |

---

## 2. Định nghĩa đại số Boole

Bộ $$(A, +, \cdot, ', 0, 1)$$ thỏa  
**6 tiên đề Huntington**

$$A$$ có ít nhất hai phần tử; $$0,1\in A$$

---

## Tiên đề Huntington (1–3)

1. **Đóng**: $$x+y$$, $$xy\in A$$
2. **Trung hòa**: $$x+0=x$$, $$x\cdot1=x$$
3. **Giao hoán**: $$x+y=y+x$$, $$xy=yx$$

---

## Tiên đề Huntington (4–6)

4. **Phân phối hai chiều**
5. **Phần tử bù**: $$x+x'=1$$, $$xx'=0$$
6. **Không suy biến**: $$0\neq1$$

*(Kết hợp thường suy được — vẫn dùng thoải mái khi biến đổi.)*

---

## Ví dụ: $$P(U)$$

| Phép | Tập hợp |
|:---|:---|
| $$\land$$ | $$\cap$$ |
| $$\lor$$ | $$\cup$$ |
| bù | $$U\setminus X$$ |
| 0 / 1 | $$\emptyset$$ / $$U$$ |

$$U$$ 1 phần tử → đẳng cấu $$B=\{0,1\}$$

---

## $$B^{n}$$ — vector bit

Phép **từng bit** trên $$\{0,1\}^{n}$$

$$B^{n}$$ là đại số Boole  
= **không gian đầu vào** hàm $$n$$ biến (bài 13.2)

---

## 3. De Morgan

$$
(x+y)'=x'y'
$$

$$
(xy)'=x'+y'
$$

**Thần chú**: *Đảo dấu, đảo biến*

---

## Sai lầm phổ biến

**Sai**: $$(x+y)'=x'+y'$$

**Đúng**: $$(x+y)'=x'y'$$

Phủ định **đảo phép**, không chỉ đảo biến.

---

## Hấp thụ — chứng minh nhanh

$$
\begin{aligned}
x+xy &= x\cdot1+xy \\
     &= x(1+y) \\
     &= x\cdot1 = x
\end{aligned}
$$

---

## Hai phương pháp chứng minh

1. **Đại số** — biến đổi từ tiên đề / định lý
2. **Bảng chân trị** — so $$2^{n}$$ tổ hợp

Ví dụ De Morgan $$n=2$$ → bảng 4 dòng

---

## Nguyên lý đối ngẫu

Đổi:

- $$+\leftrightarrow\cdot$$
- $$0\leftrightarrow1$$

Hằng đẳng thức vẫn đúng.

---

## Bảng đối ngẫu (mẫu)

| Gốc | Đối ngẫu |
|:---|:---|
| $$x+0=x$$ | $$x\cdot1=x$$ |
| $$x+xy=x$$ | $$x(x+y)=x$$ |
| $$(x+y)'=x'y'$$ | $$(xy)'=x'+y'$$ |

Chứng một nửa → “anh em sinh đôi”

---

## 4. Phép dẫn xuất

| Phép | Công thức |
|:---|:---|
| XOR | $$x\oplus y=x'y+xy'$$ |
| Kéo theo | $$x\to y=x'+y$$ |
| XNOR | $$xy+x'y'$$ |

---

## NAND và NOR

| Phép | Công thức |
|:---|:---|
| NAND | $$x\mid y=(xy)'$$ |
| NOR | $$x\downarrow y=(x+y)'$$ |

Mỗi cái **đầy đủ** — đủ xây mọi hàm Boole  
(chi tiết mạch: tiết 32)

---

## Bảng XOR và XNOR

| $$x$$ | $$y$$ | $$\oplus$$ | XNOR |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

XOR = **khác**; XNOR = **giống**

---

## Bảng NAND và NOR

| $$x$$ | $$y$$ | NAND | NOR |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

---

## 5. Liên hệ logic mệnh đề

| Logic (ch1) | Boole |
|:---|:---|
| Mệnh đề $$p$$ | Biến $$x$$ |
| T / F | 1 / 0 |
| $$\wedge$$ / $$\vee$$ / $$\neg$$ | $$\cdot$$ / $$+$$ / $$'$$ |

Tautology ↔ biểu thức $$=1$$

---

## Ứng dụng ngắn

- Điều kiện `if` / `while` / bitmask
- SQL `WHERE` (AND, OR, NOT)
- Nền **cổng logic** (tiết 32)

---

## Thực hành 1

Đơn giản hóa:

1. $$(A+B)(A+C)$$
2. $$A+AB+AC$$
3. $$(A'B)'$$

---

## Thực hành 2

Chứng minh $$x+yz=(x+y)(x+z)$$

- **Cách 1**: đại số  
- **Cách 2**: bảng chân trị  

---

## Tóm tắt Tiết 30

- $$B=\{0,1\}$$ + 10 hằng đẳng thức
- 6 tiên đề Huntington; $$1+1=1$$
- De Morgan, hấp thụ, đối ngẫu
- Phép dẫn xuất: XOR, NAND, NOR, …
- Cầu nối logic mệnh đề (ch1)

---

## Liên hệ lộ trình

**Tiết 31** — Hàm Boole, SOP/POS  
**Tiết 32** — Cổng + tối thiểu hóa  
**Tiết 33–34** — K-map, Quine–McCluskey

---

## Bài tập ôn (1)

1. Liệt kê 6 tiên đề Huntington
2. Đơn giản hóa $$AB+A'B+AB'$$
3. Đơn giản hóa $$(x+yz)'$$

---

## Bài tập ôn (2)

4. Chứng minh $$x(x'+y)=xy$$
5. Viết XOR bằng AND/OR/NOT
6. *(Tuỳ chọn)* Vì sao $$P(U)$$, $$B^{n}$$ là đại số Boole?
