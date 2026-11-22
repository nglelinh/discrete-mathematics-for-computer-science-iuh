---
layout: post
title: "Cổng Logic và Tối thiểu hóa Đại số"
categories: chapter13
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Bảy cổng logic cơ bản (AND, OR, NOT, NAND, NOR, XOR, XNOR) qua bảng chân trị, các kỹ thuật tối thiểu hóa hàm Boole bằng đại số và tính đầy đủ chức năng của NAND/NOR."
---

<div class="textbook-epigraph" markdown="1">

"Boolean algebra is the algebra of truth values — and each gate is one truth table made concrete."

<span class="epigraph-attribution">— Tinh thần bài 13.3</span>

</div>

Sau khi tìm hiểu đại số và hàm Boole (bảng chân trị, SOP và POS), ta gắn từng phép toán logic với một **cổng logic** tương ứng. Bài học này trình bày bảng chân trị của bảy cổng cơ bản (NOT, AND, OR, NAND, NOR, XOR, XNOR) cùng các kỹ thuật **tối thiểu hóa đại số** như đồng nhất, hấp thụ, gom nhân tử và luật De Morgan.

Quy trình thiết kế mạch từ đặc tả bằng lời, đếm số cổng và các mạch số học sẽ được trình bày ở Mục 13.6–13.7; trọng tâm của bài này là nhận diện cổng logic và rút gọn biểu thức đại số.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nhận biết** bảy cổng logic cơ bản và đọc đúng bảng chân trị của từng cổng.
- **Viết** công thức Boole tương ứng với XOR, XNOR, NAND và NOR.
- **Áp dụng** các kỹ thuật tối thiểu hóa đại số: đồng nhất, hấp thụ, gom nhân tử, De Morgan và thêm hạng tử phụ.
- **Kiểm chứng** sự tương đương giữa hai biểu thức bằng bảng chân trị.
- **Giải thích** vì sao chỉ riêng NAND (hoặc chỉ riêng NOR) đã đủ biểu diễn mọi hàm Boole.

**Từ khóa**: cổng logic, bảng chân trị, XOR, XNOR, NAND, NOR, tối thiểu hóa đại số, hấp thụ, De Morgan, đầy đủ chức năng.

</div>

## Cổng logic là gì?

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Cổng logic** (logic gate) là phần tử cơ bản nhận **một hoặc nhiều** tín hiệu nhị phân (**0** hoặc **1**) ở ngõ vào và tạo ra **một** tín hiệu ở ngõ ra theo một **bảng chân trị cố định**.

</div>

Ba phép toán cơ bản của đại số Boole tương ứng trực tiếp với ba cổng sau:

| Phép toán | Cổng | Quy tắc hoạt động |
|:---|:---|:---|
| $$+$$ (OR) | OR | Ngõ ra bằng **1** nếu có **ít nhất 1** ngõ vào bằng **1** |
| $$\cdot$$ (AND) | AND | Ngõ ra bằng **1** chỉ khi **mọi** ngõ vào bằng **1** |
| $$'$$ / $$\bar{\phantom{x}}$$ | NOT | Đảo giá trị ngõ vào: $$\bar 0=1$$, $$\bar 1=0$$ |

Lưu ý rằng $$1+1=1$$ theo phép OR logic, không phải phép cộng số học.

Phần hiện thực vật lý (công tắc, mạch tích hợp, sơ đồ mạch) sẽ được xét ở **bài 13.6**; trong bài này, mỗi cổng được xem qua **bảng chân trị và công thức**.

## Bảy cổng logic cơ bản

### NOT (cổng đảo)

Ngõ ra đảo ngược giá trị của ngõ vào: $$Y = A'$$ (còn viết $$\bar A$$).

| $$A$$ | $$Y$$ |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

![Cổng NOT](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.11">Cổng NOT (inverter).</p>

### AND

Ngõ ra bằng **1** khi và chỉ khi **mọi** ngõ vào đều bằng **1**.

| $$A$$ | $$B$$ | $$AB$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.12">Cổng AND.</p>

### OR

Ngõ ra bằng **1** khi có **ít nhất một** ngõ vào bằng **1**.

| $$A$$ | $$B$$ | $$A+B$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

![Cổng OR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_OR.svg)

<p class="textbook-figure-caption" data-figure="13.13">Cổng OR.</p>

### NAND và NOR

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

### XOR và XNOR

| Cổng | Ngõ ra bằng **1** khi… | Công thức |
|:---|:---|:---|
| **XOR** | hai ngõ vào **khác nhau** | $$A\oplus B = A'B + AB'$$ |
| **XNOR** | hai ngõ vào **giống nhau** | $$A\odot B = AB + A'B' = (A\oplus B)'$$ |

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

### Bảng tổng hợp bảy cổng

| Cổng | Ngõ ra bằng **1** khi… | Công thức (2 ngõ vào) |
|:---|:---|:---|
| NOT | ngõ vào = **0** | $$A'$$ |
| AND | **mọi** ngõ vào = **1** | $$AB$$ |
| OR | có **≥ 1** ngõ vào = **1** | $$A+B$$ |
| NAND | **không** phải cả hai ngõ vào đều bằng **1** | $$(AB)'$$ |
| NOR | **mọi** ngõ vào = **0** | $$(A+B)'$$ |
| XOR | hai ngõ vào **khác nhau** | $$A\oplus B$$ |
| XNOR | hai ngõ vào **giống nhau** | $$A\odot B$$ |

## Tối thiểu hóa đại số

Hai biểu thức Boole là **tương đương** nếu chúng có cùng bảng chân trị. Trong số các biểu thức tương đương, ta ưu tiên dạng có **ít hạng tử** và **ít litera** hơn để dễ đọc, dễ tính toán và tốn ít cổng hơn khi thiết kế mạch (bài 13.6).

Tối thiểu hóa đại số là chuỗi biến đổi dựa trên các tiên đề và hằng đẳng thức ở bài 13.1. Phương pháp này không có một quy trình máy móc duy nhất, nhưng có các kỹ thuật chủ chốt thường dùng trước khi chuyển sang bản đồ Karnaugh (13.4) hoặc Quine–McCluskey (13.5).

### Đồng nhất và lũy đẳng

$$
x+x'=1,\quad xx'=0,\quad x+x=x,\quad xx=x,
$$
$$
x+0=x,\quad x\cdot 1=x,\quad x+1=1,\quad x\cdot 0=0.
$$

<div class="textbook-example" markdown="1">

**Ví dụ 1.** $$F = xy + x\bar y = x(y+\bar y) = x$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.**  
$$F = xyz + x\bar y z = xz(y+\bar y) = xz$$.  
Hai biểu thức có cùng bảng chân trị, nhưng dạng sau gọn hơn rõ rệt.

</div>

### Hấp thụ

$$
x + xy = x, \qquad x(x+y) = x.
$$

Một hệ quả thường dùng khác là:

$$
x + \bar x\, y = x + y
$$

(chứng minh: $$x + \bar x y = (x+\bar x)(x+y) = 1\cdot(x+y) = x+y$$).

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = a + ab + ac = a(1+b+c) = a$$.

</div>

### Phân phối và gom nhân tử

Đặt nhân tử chung để xuất hiện dạng $$y+\bar y = 1$$ rồi triệt tiêu biến.

<div class="textbook-example" markdown="1">

**Ví dụ.**  
$$F = xy + x\bar y + \bar x y = x + \bar x y = x + y$$.

</div>

### Luật De Morgan

$$
(x+y)' = x'y', \qquad (xy)' = x' + y'.
$$

**Lưu ý ghi nhớ:** đảo dấu, đảo biến — không viết nhầm $$(x+y)'=x'+y'$$.

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = (x'+y)' + xy = xy' + xy = x$$.

</div>

### Thêm hạng tử phụ bằng luật lũy đẳng

Vì $$t+t=t$$, đôi khi ta có thể lặp lại một hạng tử sẵn có để tạo thêm cặp gộp mới:

$$
xy + x\bar y + \bar x y
= (xy + x\bar y) + (\bar x y + xy) = x + y.
$$

### Chiến lược rút gọn và kiểm chứng

**Thứ tự ưu tiên khi biến đổi:**

1. Áp dụng luật hấp thụ và lũy đẳng để loại bỏ hạng tử thừa.  
2. Tìm các cặp hạng tử chỉ khác nhau đúng **một** litera (nguyên và bù) để gộp.  
3. Áp dụng luật De Morgan khi gặp dấu phủ định bao ngoài ngoặc.  
4. Dùng luật phân phối hoặc gom nhân tử chung.  
5. Dừng lại khi không còn bước rút gọn rõ ràng, rồi **kiểm chứng** kết quả.

**Kiểm chứng:** đối chiếu bảng chân trị của hai biểu thức (khi $$n$$ nhỏ) hoặc thử trực tiếp trên một số tổ hợp giá trị làm $$F=1$$ và $$F=0$$.

<div class="textbook-example" markdown="1">

**Ví dụ tổng hợp.**  
$$F = ab' + ac + a'b + bc$$.  
Gom nhóm: $$F = (ab' + a'b) + c(a+b) = (a\oplus b) + c(a+b)$$.  
Ta có thể kiểm tra lại bằng cách thay một vài bộ giá trị $$(a,b,c)$$ vào cả hai biểu thức.

</div>

## Tính đầy đủ chức năng của NAND và NOR

Chỉ riêng cổng **NAND** (hoặc chỉ riêng cổng **NOR**) đủ để biểu diễn mọi hàm Boole, vì từ chúng có thể xây dựng lại cả ba phép cơ bản NOT, AND và OR:

| Phép toán | Chỉ dùng NAND ($$\mid$$) | Chỉ dùng NOR ($$\downarrow$$) |
|:---|:---|:---|
| NOT | $$x' = (x \mid x)$$ | $$x' = (x \downarrow x)$$ |
| AND | $$xy = ((x \mid y) \mid (x \mid y))$$ | $$xy = x' \downarrow y'$$ |
| OR | $$x+y = (x' \mid y')$$ | $$x+y = ((x \downarrow y) \downarrow (x \downarrow y))$$ |

Trong thực hành, ta thường rút gọn biểu thức đại số trước rồi mới chuyển đổi sang mạng chỉ gồm cổng NAND hoặc chỉ gồm cổng NOR khi hiện thực mạch.

## Liên hệ trong chương

| Bài | Nội dung chính |
|:---|:---|
| **13.3 (bài này)** | Bảy cổng logic cơ bản và rút gọn bằng đại số |
| **13.4–13.5** | Bản đồ Karnaugh (K-map) và phương pháp Quine–McCluskey |
| **13.6** | Công tắc, quy trình năm bước thiết kế mạch, đếm cổng và ứng dụng |
| **13.7** | Mạch cộng nửa/đầy đủ (half/full adder), MUX và decoder |


## Công cụ tương tác

Chọn cổng AND, OR, NOT, NAND hoặc XOR, thay đổi công tắc đầu vào và quan sát bảng chân trị đầu ra.
<div class="interactive-demo" markdown="1">
<div data-demo="logic-gates-builder"></div>
</div>
<script src="{{ '/public/js/logic-gates-builder.js' | relative_url }}"></script>


### Minh họa liên kết: từ cổng logic đến K-map

Quan sát mạch SOP (AND–OR, vòng tròn nhỏ biểu thị đảo tín hiệu) của một hàm Boole, đồng bộ với bảng chân trị và bản đồ Karnaugh; công cụ này tự động dựng mạch tối tiểu từ biểu thức đã nhập.

<div class="interactive-demo" markdown="1">
<div data-demo="boolean-explainer" data-vars="3" data-focus="circuit" data-expr="p ⊕ q ⊕ r"></div>
</div>
<script src="{{ '/public/js/explainers/boolean-explainer.js' | relative_url }}"></script>


## Bài tập

### Bài tập 1

Viết bảng chân trị 2 ngõ vào cho XOR và XNOR, đồng thời biểu diễn XOR bằng AND, OR và NOT.

<details>
<summary>Đáp án</summary>

Theo thứ tự $$(A,B) = (0,0), (0,1), (1,0), (1,1)$$: XOR cho đầu ra $$0, 1, 1, 0$$; XNOR cho đầu ra $$1, 0, 0, 1$$.  
Công thức: $$A\oplus B = A'B + AB'$$.

</details>

### Bài tập 2

Rút gọn các biểu thức sau bằng biến đổi đại số (nêu rõ quy tắc sử dụng):

(a) $$ab + ab' + a'b$$  
(b) $$xy + x'z + yz$$  
(c) $$(x'+y)' + x$$

<details>
<summary>Đáp án</summary>

(a) $$ab + ab' + a'b = a(b+b') + a'b = a + a'b = a + b$$.  
(b) Theo định lý đồng thuận (consensus): $$xy + x'z + yz = xy + x'z + yz(x+x') = xy(1+z) + x'z(1+y) = xy + x'z$$.  
(c) $$(x'+y)' + x = xy' + x = x$$ (De Morgan rồi hấp thụ).

</details>

### Bài tập 3

Giải thích vì sao chỉ riêng NAND đủ để xây dựng NOT, AND và OR (viết rõ công thức). Làm tương tự với NOR.

<details>
<summary>Đáp án</summary>

Với NAND: $$x'=(x\mid x)$$; $$xy=((x\mid y)\mid(x\mid y))$$; $$x+y=(x'\mid y')$$.  
Với NOR: $$x'=(x\downarrow x)$$; $$x+y=((x\downarrow y)\downarrow(x\downarrow y))$$; $$xy = (x' \downarrow y')$$ theo luật De Morgan.

</details>

### Bài tập 4

Cho $$F = ab'c + abc' + a'bc + abc$$.  
Rút gọn biểu thức về dạng $$ab + bc + ca$$ (hàm đa số) và kiểm tra tại hai tổ hợp $$(1,1,0)$$ và $$(1,0,0)$$.

<details>
<summary>Đáp án</summary>

Nhân bản hạng $$abc$$ bằng luật lũy đẳng rồi gom thành ba cặp: $$(ab'c + abc) + (abc' + abc) + (a'bc + abc) = ac + ab + bc$$.  
Kiểm tra: tại $$(1,1,0)$$, cả hai biểu thức đều bằng **1**; tại $$(1,0,0)$$, cả hai đều bằng **0**.

</details>

### Bài tập 5

Cho hàm Boole $$F(x,y,z)$$ bằng **1** chỉ khi $$(x,y,z)=(1,1,1)$$ hoặc $$(1,0,1)$$.

1. Viết dạng SOP chuẩn.  
2. Rút gọn biểu thức bằng đại số.

<details>
<summary>Đáp án</summary>

1. $$F = xyz + x\bar y z$$.  
2. $$F = xz(y+\bar y) = xz$$.

</details>

### Bài tập 6

Xét biểu thức $$F = x'y'z + x'yz' + xy'z' + xyz$$. Đếm số hạng tử và số litera ở dạng SOP hiện tại, và nhận xét xem có thể rút gọn thêm ở dạng SOP hay không.

<details>
<summary>Đáp án</summary>

Ở dạng SOP hiện tại, $$F$$ có 4 hạng tử, mỗi hạng gồm 3 litera (tổng cộng 12 litera). Biểu thức này **không thể rút gọn thêm ở dạng SOP** vì không có hai minterm nào chỉ khác nhau đúng 1 biến (đây chính là hàm parity 3 biến). Nếu sử dụng phép XOR, biểu thức viết gọn thành $$F = x \oplus y \oplus z$$ (3 litera).

</details>

## Xem thêm

- Mục 13.1 — hằng đẳng thức và các phép toán dẫn xuất NAND/NOR.  
- Mục 13.2 — minterm, dạng SOP và POS chuẩn.  
- Mục 13.4–13.5 — bản đồ Karnaugh và phương pháp Quine–McCluskey.  
- Mục 13.6–13.7 — thiết kế mạch tổ hợp và mạch số học.

## Tóm tắt

1. Cổng logic hiện thực các phép toán Boole theo bảng chân trị cố định: NOT, AND, OR, NAND, NOR, XOR và XNOR.  
2. Cổng XOR cho đầu ra **1** khi hai ngõ vào khác nhau; cổng XNOR cho đầu ra **1** khi hai ngõ vào giống nhau.  
3. Tối thiểu hóa đại số kết hợp các luật đồng nhất, hấp thụ, gom nhân tử và De Morgan, sau đó kiểm chứng bằng bảng chân trị.  
4. Cả NAND và NOR đều là các phép toán đầy đủ chức năng.  
5. Thiết kế mạch tổ hợp và các khối số học được trình bày ở Mục 13.6–13.7.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=vJO-5gY0wpk">How Do Computers Make Decisions? Logic Gates and Boolean Logic Explained.</a> — Basics Explained, H3Vtux, tiếng Anh. Giới thiệu cổng logic và bảng chân trị của các phép toán cơ bản.
- <a href="https://www.youtube.com/watch?v=ChtmE09BSy0">NAND Gate as Universal Gate (Part 1)</a> — Neso Academy, tiếng Anh. Giải thích tính đầy đủ chức năng của cổng NAND.
- <a href="https://www.youtube.com/watch?v=sTu3LwpF6XI">Making logic gates from transistors</a> — Ben Eater, tiếng Anh. Minh họa cách lắp dựng cổng logic từ transistor, kết nối công thức với phần cứng.
