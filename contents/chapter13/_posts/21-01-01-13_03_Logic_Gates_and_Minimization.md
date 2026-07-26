---
layout: post
title: "Cổng Logic và Tối thiểu hóa Đại số"
categories: chapter13
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Bảy cổng logic (AND, OR, NOT, NAND, NOR, XOR, XNOR) qua bảng chân trị; tối thiểu hóa hàm Boole bằng đại số (hấp thụ, De Morgan, đồng nhất); NAND/NOR đầy đủ chức năng. Thiết kế mạch → bài 13.6."
---

<div class="textbook-epigraph" markdown="1">

"Boolean algebra is the algebra of truth values — and each gate is one truth table made concrete."

<span class="epigraph-attribution">— Tinh thần bài 13.3</span>

</div>

Sau đại số và hàm Boolean (bảng chân trị, SOP / POS), mỗi phép được gắn với một **cổng logic**. Mục này trình bày bảng chân trị của NOT, AND, OR, NAND, NOR, XOR, XNOR cùng các kỹ thuật **tối thiểu hóa đại số** (đồng nhất, hấp thụ, gom nhân tử, De Morgan).

Quy trình thiết kế mạch từ yêu cầu bằng lời, đếm cổng và các khối số học được triển khai ở Mục 13.6–13.7. Ở đây trọng tâm là nhận diện cổng và rút gọn biểu thức.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nhận biết** bảy cổng cơ bản và đọc đúng bảng chân trị (0/1).
- **Viết** công thức Boole của XOR, XNOR, NAND, NOR.
- **Áp dụng** tối thiểu hóa đại số: đồng nhất, hấp thụ, gom nhân tử, De Morgan, thêm hạng phụ.
- **Kiểm** hai biểu thức tương đương bằng bảng chân trị.
- **Giải thích** vì sao chỉ NAND (hoặc chỉ NOR) đủ biểu diễn mọi hàm Boole (công thức).

**Từ khóa**: cổng logic, bảng chân trị, XOR, XNOR, NAND, NOR, tối thiểu hóa đại số, hấp thụ, De Morgan, đầy đủ chức năng.

</div>

## 1. Cổng logic là gì?

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Cổng logic** (logic gate) là khối nhận **một hoặc nhiều** tín hiệu **0**/**1** và phát ra **một** tín hiệu theo **bảng chân trị cố định**.

</div>

Ba phép cơ bản của đại số Boole tương ứng ba cổng:

| Phép | Cổng | Ý nghĩa nhanh |
|:---|:---|:---|
| $$+$$ (OR) | OR | Ra **1** nếu **≥ 1** ngõ = **1** |
| $$\cdot$$ (AND) | AND | Ra **1** chỉ khi **mọi** ngõ = **1** |
| $$'$$ / $$\bar{\phantom{x}}$$ | NOT | Đảo: $$\bar 0=1$$, $$\bar 1=0$$ |

Nhớ: $$1+1=1$$ (OR logic, không phải cộng số).

Phần cứng (công tắc, chip, vẽ sơ đồ) → **bài 13.6**. Ở đây cổng = **bảng + công thức**.

## 2. Bảy cổng cơ bản

Mỗi cổng: **một câu tiếng Việt + bảng 0/1 + hình ký hiệu**.

### 2.1. NOT (đảo)

$$Y = A'$$ (cũng viết $$\bar A$$).

| $$A$$ | $$Y$$ |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

![Cổng NOT](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.11">Cổng NOT (inverter).</p>

### 2.2. AND

Ra **1** khi **mọi** ngõ vào = **1**.

| $$A$$ | $$B$$ | $$AB$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.12">Cổng AND.</p>

### 2.3. OR

Ra **1** khi **ít nhất một** ngõ = **1**.

| $$A$$ | $$B$$ | $$A+B$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

![Cổng OR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_OR.svg)

<p class="textbook-figure-caption" data-figure="13.13">Cổng OR.</p>

### 2.4. NAND và NOR

| Cổng | Định nghĩa | Ý nghĩa |
|:---|:---|:---|
| **NAND** | $$Y=(AB)'$$ | Phủ định của AND |
| **NOR** | $$Y=(A+B)'$$ | Phủ định của OR |

| $$A$$ | $$B$$ | NAND | NOR |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

![Cổng NAND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NAND.svg)

<p class="textbook-figure-caption" data-figure="13.14">Cổng NAND.</p>

![Cổng NOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOR.svg)

<p class="textbook-figure-caption" data-figure="13.15">Cổng NOR.</p>

### 2.5. XOR và XNOR

| Cổng | Ra **1** khi… | Công thức |
|:---|:---|:---|
| **XOR** | hai ngõ **khác** nhau | $$A\oplus B = A'B + AB'$$ |
| **XNOR** | hai ngõ **giống** nhau | $$A\odot B = AB + A'B' = (A\oplus B)'$$ |

| $$A$$ | $$B$$ | XOR | XNOR |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

![Cổng XOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_XOR.svg)

<p class="textbook-figure-caption" data-figure="13.16">Cổng XOR.</p>

![Cổng XNOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_XNOR.svg)

<p class="textbook-figure-caption" data-figure="13.17">Cổng XNOR.</p>

### 2.6. Tóm tắt bảy cổng

| Cổng | Ra **1** khi… | Công thức (2 ngõ) |
|:---|:---|:---|
| NOT | vào = **0** | $$A'$$ |
| AND | **mọi** vào = **1** | $$AB$$ |
| OR | **≥ 1** vào = **1** | $$A+B$$ |
| NAND | **không** phải cả hai = **1** | $$(AB)'$$ |
| NOR | **mọi** vào = **0** | $$(A+B)'$$ |
| XOR | hai vào **khác** | $$A\oplus B$$ |
| XNOR | hai vào **giống** | $$A\odot B$$ |

## 3. Tối thiểu hóa đại số

Hai biểu thức **tương đương** nếu cùng bảng chân trị. Trong lớp biểu thức tương đương, ta ưa dạng **ít hạng** và **ít litera** hơn — dễ đọc, dễ làm bài, và (khi sang 13.6) dễ vẽ mạch hơn.

Tối thiểu hóa đại số = chuỗi biến đổi hợp lệ từ tiên đề / hằng đẳng thức bài 13.1. Không có “một thuật toán máy móc duy nhất”; có **các kỹ thuật** hay dùng trước K-map (13.4) và Quine–McCluskey (13.5).

### 3.1. Đồng nhất và lũy đẳng

$$
x+x'=1,\quad xx'=0,\quad x+x=x,\quad xx=x,
$$
$$
x+0=x,\quad x\cdot 1=x,\quad x+1=1,\quad x\cdot 0=0.
$$

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = xy + x\bar y = x(y+\bar y) = x$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ (vì sao phải rút).**  
$$F = xyz + x\bar y z = xz(y+\bar y) = xz$$.  
Cùng bảng chân trị; dạng sau ngắn hơn rõ rệt.

</div>

### 3.2. Hấp thụ

$$
x + xy = x, \qquad x(x+y) = x.
$$

Mở rộng hay dùng:

$$
x + \bar x\, y = x + y
$$

(vì $$x + \bar x y = (x+\bar x)(x+y) = x+y$$).

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = a + ab + ac = a(1+b+c) = a$$.

</div>

### 3.3. Phân phối và gom nhân tử

Kéo nhân tử chung hoặc tạo cặp $$y+\bar y$$.

<div class="textbook-example" markdown="1">

**Ví dụ.**  
$$F = xy + x\bar y + \bar x y = x + \bar x y = x + y$$.

</div>

### 3.4. De Morgan

$$
(x+y)' = x'y', \qquad (xy)' = x' + y'.
$$

**Thần chú:** đảo dấu, đảo biến — **không** viết $$(x+y)'=x'+y'$$.

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = (x'+y)' + xy = xy' + xy = x$$.

</div>

### 3.5. Thêm hạng phụ (đôi khi)

Vì $$t+t=t$$, đôi khi **viết thêm** một hạng để tạo cặp gộp:

$$
xy + x\bar y + \bar x y
= (xy + x\bar y) + (\bar x y + xy) = x + y.
$$

### 3.6. Chiến lược và kiểm chứng

**Khi làm bài:**

1. Ưu tiên hấp thụ và lũy đẳng.  
2. Tìm cặp chỉ khác **một** litera bù.  
3. De Morgan khi có ngoặc phủ định.  
4. Phân phối / gom nhân tử.  
5. **Dừng** khi không còn cắt rõ — rồi **kiểm**.

**Kiểm chứng:** so bảng chân trị hai biểu thức ($$n$$ nhỏ), hoặc thử vài vector nơi $$F=1$$ và $$F=0$$.

<div class="textbook-example" markdown="1">

**Ví dụ tổng hợp.**  
$$F = ab' + ac + a'b + bc$$.  
Gom: $$F = (ab' + a'b) + c(a+b) = (a\oplus b) + c(a+b)$$.  
Kiểm nhanh vài bộ $$(a,b,c)$$ — hai dạng phải trùng.

</div>

## 4. NAND và NOR đầy đủ chức năng

Chỉ riêng **NAND** (hoặc chỉ **NOR**) đủ biểu diễn mọi hàm Boole — vì từ chúng dựng được NOT, AND, OR.

| Phép | Chỉ NAND ($$\mid$$) | Chỉ NOR ($$\downarrow$$) |
|:---|:---|:---|
| NOT | $$x' = (x \mid x)$$ | $$x' = (x \downarrow x)$$ |
| AND | $$xy = ((x \mid y) \mid (x \mid y))$$ | $$xy = x' \downarrow y'$$ |
| OR | $$x+y = (x' \mid y')$$ | $$x+y = ((x \downarrow y) \downarrow (x \downarrow y))$$ |

Thông thường rút gọn biểu thức trước (mục 3), rồi mới ánh xạ sang mạng chỉ NAND hoặc chỉ NOR khi yêu cầu hiện thực.

## 5. Liên hệ lộ trình

| Bài | Nội dung |
|:---|:---|
| **13.3 (bài này)** | Cổng + bảng; rút gọn **đại số** |
| **13.4–13.5** | K-map, Quine–McCluskey |
| **13.6** | Công tắc, năm bước thiết kế, đếm cổng, ứng dụng |
| **13.7** | Half/full adder, MUX, decoder |

## Bài tập

### Bài tập 1

Viết bảng chân trị 2 ngõ cho XOR và XNOR. Viết XOR bằng AND/OR/NOT.

<details>
<summary>Đáp án</summary>

XOR: 0,1,1,0 theo $$(A,B)=(00,01,10,11)$$; XNOR: 1,0,0,1.  
$$A\oplus B = A'B + AB'$$.

</details>

### Bài tập 2

Rút gọn bằng đại số (ghi rõ đẳng thức):

(a) $$ab + ab' + a'b$$  
(b) $$xy + x'z + yz$$  
(c) $$(x'+y)' + x$$

<details>
<summary>Đáp án</summary>

(a) $$ab + ab' + a'b = a + a'b = a + b$$.  
(b) Có thể đưa về $$xy + x'z$$ (kiểm bảng 8 dòng).  
(c) $$(x'+y)' + x = xy' + x = x$$.

</details>

### Bài tập 3

Giải thích vì sao chỉ NAND đủ xây NOT, AND, OR (viết công thức). Tương tự NOR cho NOT và OR.

<details>
<summary>Đáp án</summary>

NAND: $$x'=(x\mid x)$$; $$xy=((x\mid y)\mid(x\mid y))$$; $$x+y=(x'\mid y')$$.  
NOR: $$x'=(x\downarrow x)$$; $$x+y=((x\downarrow y)\downarrow(x\downarrow y))$$; AND qua De Morgan.

</details>

### Bài tập 4

Cho $$F = ab'c + abc' + a'bc + abc$$.  
Rút gọn về $$ab + bc + ca$$ (majority). Kiểm tại $$(1,1,0)$$ và $$(1,0,0)$$.

<details>
<summary>Đáp án</summary>

Gom dần về majority (ít nhất hai trong ba biến = **1**).  
Tại $$110$$: cả hai dạng **1**; tại $$100$$: cả hai **0**.

</details>

### Bài tập 5

Hàm bằng **1** chỉ khi $$(x,y,z)=(1,1,1)$$ hoặc $$(1,0,1)$$.

1. Viết SOP chuẩn.  
2. Rút gọn bằng đại số.

<details>
<summary>Đáp án</summary>

1. $$F = xyz + x\bar y z$$.  
2. $$F = xz$$.

</details>

### Bài tập 6

So sánh số **hạng** và số **litera** của $$F = x'y'z + x'yz' + xy'z' + xyz$$ với một dạng rút (nếu có). Không cần vẽ mạch.

<details>
<summary>Đáp án</summary>

SOP thô: 4 hạng, mỗi hạng 3 litera. Sau rút (tùy cách) số hạng/litera giảm — đối bảng 8 dòng để chắc tương đương.

</details>

## Xem thêm

- Mục 13.1 — hằng đẳng thức; NAND/NOR như phép dẫn xuất.  
- Mục 13.2 — minterm, SOP / POS chuẩn.  
- Mục 13.4–13.5 — K-map và Quine–McCluskey.  
- Mục 13.6–13.7 — thiết kế tổ hợp và mạch số học.

## Tóm tắt

1. Cổng logic hiện thực phép Boolean theo bảng chân trị cố định: NOT, AND, OR, NAND, NOR, XOR, XNOR.  
2. XOR bằng **1** khi hai ngõ khác nhau; XNOR bằng **1** khi hai ngõ giống nhau.  
3. Tối thiểu hóa đại số dựa trên đồng nhất, hấp thụ, gom nhân tử và De Morgan, sau đó kiểm chứng bằng bảng chân trị.  
4. NAND và NOR mỗi cái là tập đầy đủ chức năng.  
5. Thiết kế mạch tổ hợp và các khối số học được trình bày ở Mục 13.6–13.7.
