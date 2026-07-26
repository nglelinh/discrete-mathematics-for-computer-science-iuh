---
layout: post
title: "Đại số Boole"
categories: chapter13
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Đại số logic trên {0,1}, tiên đề Huntington, hằng đẳng thức, đối ngẫu, phép dẫn xuất (XOR, NAND, NOR), và ví dụ đại số Boole (P(U), B^n)."
---

<div class="textbook-epigraph" markdown="1">

"Boolean algebra is the algebra of truth values — the mathematics of 0 and 1."

<span class="epigraph-attribution">— George Boole (paraphrased)</span>

</div>

Đại số Boole là nền tảng toán học của logic số, thiết kế mạch và tối ưu biểu thức điều kiện. Mọi phép đánh giá điều kiện trong chương trình, mọi mạng công tắc hay cổng logic đều vận hành trên cùng cấu trúc đại số với hai giá trị $$0$$ và $$1$$. Mục này trình bày đại số logic $$B=\{0,1\}$$, định nghĩa hình thức, tiên đề Huntington và các hằng đẳng thức cơ bản.

![George Boole](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="13.1">George Boole (1815–1864) — đặt nền đại số cho logic.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Làm việc** trên đại số logic $$B=\{0,1\}$$ với OR, AND, NOT và mười hằng đẳng thức cơ bản.
- **Phát biểu** định nghĩa đại số Boole và các tiên đề (Huntington).
- **Nhận biết** ví dụ $$P(U)$$ và $$B^n$$ là đại số Boole.
- **Chứng minh** / kiểm hằng đẳng thức bằng đại số hoặc bảng chân trị.
- **Áp dụng** nguyên lý đối ngẫu; dùng XOR, kéo theo, XNOR, NAND, NOR.
- **Giải thích** mối quan hệ với logic mệnh đề (Chương 1).

**Từ khóa**: đại số logic $$B$$, đại số Boole, hằng đẳng thức, phần tử bù, đối ngẫu, XOR, NAND, NOR.
</div>

## 1. Đại số logic $$B = \{0,1\}$$

Trước khi định nghĩa “đại số Boole” trừu tượng, ta làm việc trên **đại số logic** $$B = \{0,1\}$$ — hai giá trị **sai / đúng** (hoặc **tắt / bật**).

### 1.1. Ba phép cơ bản

| Phép | Ký hiệu thường dùng | Bảng tóm tắt |
|:---|:---|:---|
| **Tổng Boole** (OR) | $$x + y$$, $$x \lor y$$ | $$0+0=0$$; ra **1** nếu có ngõ **1** |
| **Tích Boole** (AND) | $$xy$$, $$x \land y$$ | $$1\cdot1=1$$; ra **0** nếu có ngõ **0** |
| **Bù** (NOT) | $$x'$$, $$\bar x$$, $$\lnot x$$ | $$\bar 0=1$$, $$\bar 1=0$$ |

Biến nhận giá trị trong $$B$$ gọi là **biến logic** / **biến Boole**.

<div class="content-box insight-box textbook-block" markdown="1">
**Khác đại số số học**: $$1 + 1 = 1$$ (không phải 2). Phép $$+$$ là **OR**, không phải cộng số nguyên.
</div>

### 1.2. Mười hằng đẳng thức cơ bản trên $$B$$

| # | Tên | Dạng điển hình |
|:---:|:---|:---|
| 1 | **Giao hoán** | $$x+y=y+x$$, $$xy=yx$$ |
| 2 | **Kết hợp** | $$(x+y)+z=x+(y+z)$$, $$(xy)z=x(yz)$$ |
| 3 | **Phân phối** | $$x(y+z)=xy+xz$$ **và** $$x+(yz)=(x+y)(x+z)$$ |
| 4 | **Bù kép** | $$(x')'=x$$ |
| 5 | **De Morgan** | $$(x+y)'=x'y'$$, $$(xy)'=x'+y'$$ |
| 6 | **Lũy đẳng** | $$x+x=x$$, $$xx=x$$ |
| 7 | **Trung hòa** | $$x+0=x$$, $$x\cdot 1=x$$ |
| 8 | **Phần tử bù** | $$x+x'=1$$, $$xx'=0$$ |
| 9 | **Thống trị (nuốt)** | $$x+1=1$$, $$x\cdot 0=0$$ |
| 10 | **Hấp thụ** | $$x+xy=x$$, $$x(x+y)=x$$ |

Phần sau chứng minh một số đẳng thức từ **tiên đề**.

## 2. Định nghĩa đại số Boole (trừu tượng)

### 2.1. Định nghĩa hình thức

<div class="textbook-definition" markdown="1">
**Định nghĩa.** Một **đại số Boole** là một bộ $$(A, +, \cdot, ', 0, 1)$$ (cũng viết $$(A,\lor,\land,/,0,1)$$), trong đó $$A$$ có ít nhất hai phần tử; $$+$$, $$\cdot$$ hai ngôi; $$'$$ một ngôi; $$0,1\in A$$ — thỏa các tiên đề dưới đây.
</div>

### 2.2. Các tiên đề

**Tiên đề 1 — Tính đóng.** Với mọi $$x, y \in A$$: $$x + y \in A$$, $$x \cdot y \in A$$.

**Tiên đề 2 — Phần tử trung hòa.** Tồn tại $$0, 1 \in A$$ sao cho:
- $$x + 0 = x$$ (0 trung hòa của $$+$$)
- $$x \cdot 1 = x$$ (1 trung hòa của $$\cdot$$)

**Tiên đề 3 — Giao hoán.** $$x + y = y + x$$, $$x \cdot y = y \cdot x$$.

**Tiên đề 4 — Phân phối (cả hai chiều).**
- $$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$$
- $$x + (y \cdot z) = (x + y) \cdot (x + z)$$

**Tiên đề 5 — Phần tử bù.** Với mỗi $$x \in A$$ tồn tại $$x' \in A$$ sao cho $$x + x' = 1$$ và $$x \cdot x' = 0$$.

**Tiên đề 6 — Không suy biến.** $$0 \neq 1$$.

*(Một số tài liệu ghi thêm **kết hợp** như tiên đề; trên đại số Boole chuẩn, kết hợp suy được từ các tiên đề Huntington — ta vẫn dùng kết hợp thoải mái khi biến đổi.)*

<div class="content-box warning-box textbook-block" markdown="1">
**Chú ý.** Tiên đề 4 khác đại số số học: phép $$+$$ **cũng** phân phối với $$\cdot$$. Đây vừa là sức mạnh vừa là bẫy khi mới chuyển từ số học.
</div>

### 2.3. Ví dụ quan trọng: họ tập con $$P(U)$$

<div class="textbook-example" markdown="1">

**Ví dụ (đại số Boole trên tập).**  
Cho $$U$$ bất kỳ, đặt $$A = P(U)$$ (tập các tập con của $$U$$). Định nghĩa:

| Phép trên $$A$$ | Ý nghĩa tập hợp |
|:---|:---|
| $$X \land Y$$ | $$X \cap Y$$ |
| $$X \lor Y$$ | $$X \cup Y$$ |
| $$X'$$ | $$U \setminus X$$ (bù trong $$U$$) |
| $$0$$ | $$\emptyset$$ |
| $$1$$ | $$U$$ |

Khi đó $$(P(U), \cap, \cup, {}^c, \emptyset, U)$$ là một **đại số Boole**.  
Trường hợp “nhỏ nhất hữu ích” trong máy tính: $$U$$ một phần tử → $$P(U)$$ chỉ có hai tập, đẳng cấu với $$B = \{0,1\}$$.

</div>

### 2.4. Tích Descartes và $$B^n$$

Nếu $$A$$ và $$C$$ là hai đại số Boole thì $$A \times C$$ cũng là đại số Boole với phép **từng thành phần**:

$$
(a_1,c_1) \land (a_2,c_2) = (a_1\land a_2,\, c_1\land c_2),
$$

tương tự $$\lor$$ và bù $$(a,c)'=(a',c')$$; phần tử 0 là $$(0,0)$$, 1 là $$(1,1)$$.

Đặc biệt, $$B^n = \{0,1\}^n$$ (vector bit độ dài $$n$$) là đại số Boole — đúng không gian đầu vào của **hàm Boole $$n$$ biến** (bài 13.2).

## 3. Các hằng đẳng thức cơ bản (chứng minh)

Từ 6 tiên đề trên, chúng ta có thể chứng minh nhiều hằng đẳng thức quan trọng:

### Nhóm 1: Luật Lũy đẳng (Idempotent Laws)
- $$x + x = x$$
- $$x \cdot x = x$$

### Nhóm 2: Luật Nuốt (Domination Laws)
- $$x + 1 = 1$$
- $$x \cdot 0 = 0$$

### Nhóm 3: Luật Bù (Complement Laws)
- $$(x')' = x$$ (luật phủ định kép)
- $$x + x'y = x + y$$
- $$x(x' + y) = xy$$

### Nhóm 4: Luật De Morgan
- $$(x + y)' = x' \cdot y'$$
- $$(x \cdot y)' = x' + y'$$

### Nhóm 5: Luật Hấp thụ (Absorption Laws)
- $$x + xy = x$$
- $$x(x + y) = x$$

<div class="content-box theorem-box textbook-block" markdown="1">
<div class="textbook-theorem" markdown="1">
**Định lý**: Mọi hằng đẳng thức trong đại số Boole đều có thể được chứng minh bằng hai cách:
1. **Phương pháp đại số**: biến đổi từ vế này sang vế kia dùng các tiên đề và định lý đã biết.
2. **Phương pháp bảng chân trị**: liệt kê tất cả $$2^n$$ tổ hợp giá trị và so sánh hai vế.
</div>
</div>

## Chứng minh Các Hằng đẳng thức

<div class="textbook-example" markdown="1">
**Ví dụ** 1: Chứng minh $$x + x = x$$:

**Phương pháp đại số**:

<div class="textbook-equation" markdown="1">
$$
\begin{aligned}
x + x &= (x + x) \cdot 1 & \text{(tiên đề 2)} \\
     &= (x + x)(x + x') & \text{(tiên đề 5)} \\
     &= x + xx' & \text{(tiên đề 4 - phân phối)} \\
     &= x + 0 & \text{(tiên đề 5)} \\
     &= x & \text{(tiên đề 2)}
\end{aligned}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** 2: Chứng minh $$x + xy = x$$ (Luật Hấp thụ):

<div class="textbook-equation" markdown="1">
$$
\begin{aligned}
x + xy &= x \cdot 1 + xy & \text{(tiên đề 2)} \\
       &= x(1 + y) & \text{(tiên đề 4)} \\
       &= x \cdot 1 & \text{(luật nuốt: } 1 + y = 1) \\
       &= x & \text{(tiên đề 2)}
\end{aligned}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** 3: Chứng minh $$(x + y)' = x' \cdot y'$$ (De Morgan):

Dùng phương pháp bảng chân trị:

| $$x$$ | $$y$$ | $$x + y$$ | $$(x + y)'$$ | $$x'$$ | $$y'$$ | $$x' \cdot y'$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

Hai cột $$(x + y)'$$ và $$x' \cdot y'$$ giống nhau, vậy hằng đẳng thức đúng.
</div>

### Một Sai lầm Phổ biến

Lỗi phổ biến: $$(x + y)' = x' + y'$$. Luật De Morgan **đảo ngược** phép toán — phủ định của tổng là tích của các phủ định. Quy tắc ghi nhớ: "Đảo dấu, đảo biến."

## Nguyên lý Đối ngẫu (Duality Principle)

**Nguyên lý**: Mọi hằng đẳng thức trong đại số Boole vẫn đúng nếu chúng ta thay:
- $$+$$ bằng $$\cdot$$ và $$\cdot$$ bằng $$+$$
- 0 bằng 1 và 1 bằng 0

Ví dụ, từ $$x + xy = x$$, đối ngẫu cho chúng ta: $$x(x + y) = x$$.

<div class="content-box example-box textbook-block" markdown="1">
**Bảng đối ngẫu các hằng đẳng thức:**

| Hằng đẳng thức gốc | Hằng đẳng thức đối ngẫu |
|:---|:---|
| $$x + 0 = x$$ | $$x \cdot 1 = x$$ |
| $$x + x' = 1$$ | $$x \cdot x' = 0$$ |
| $$x + xy = x$$ | $$x(x + y) = x$$ |
| $$(x + y)' = x'y'$$ | $$(xy)' = x' + y'$$ |

**Ý nghĩa sâu xa**: Nguyên lý đối ngẫu cho thấy cấu trúc đại số Boole có tính "đối xứng" tự nhiên. Mỗi định lý đều có một "người anh em sinh đôi" — chỉ cần chứng minh một nửa, nửa kia tự động đúng.
</div>

## Các phép toán dẫn xuất trên đại số logic B

Ngoài ba phép toán cơ bản AND, OR, NOT, trên $$B = \{0, 1\}$$ chúng ta còn định nghĩa các phép toán hai ngôi khác:

| Phép toán | Ký hiệu | Công thức | Ý nghĩa |
|:----------|:-------:|:-----------|:--------|
| XOR (tổng mod 2) | $$x \oplus y$$ | $$x'y + xy'$$ | 1 khi hai biến khác nhau |
| Kéo theo (Implication) | $$x \to y$$ | $$x' + y$$ | 1 trừ khi $$x=1, y=0$$ |
| Tương đương (Equivalence) | $$x \leftrightarrow y$$ | $$xy + x'y'$$ | 1 khi hai biến bằng nhau |
| NOR (Vebb) | $$x \downarrow y$$ | $$(x + y)'$$ | Phủ định của OR |
| NAND (Sheffer) | $$x \mid y$$ | $$(xy)'$$ | Phủ định của AND |

**Bảng chân trị các phép toán dẫn xuất**:

| $$x$$ | $$y$$ | $$x \oplus y$$ | $$x \to y$$ | $$x \leftrightarrow y$$ | $$x \downarrow y$$ | $$x \mid y$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 | 0 | 0 |

<div class="textbook-definition" markdown="1">

**Tính đầy đủ của NAND và NOR.** Chỉ NAND (hoặc chỉ NOR) đủ biểu diễn mọi hàm Boolean. Do đó NAND thường được chọn làm cổng cơ sở trong thư viện mạch số.

</div>

<div class="interactive-demo" markdown="1">
<div data-demo="boolean-algebra-checker"></div>
</div>
<script src="{{ '/public/js/boolean-algebra-checker.js' | relative_url }}"></script>

## Đại số Boole và logic mệnh đề

Đại số Boole liên hệ trực tiếp với logic mệnh đề (Chương 1):

| Logic Mệnh đề | Đại số Boole |
|:---|:---|
| Mệnh đề $$p$$ | Biến Boole $$x$$ |
| Đúng (T) | 1 |
| Sai (F) | 0 |
| Phép hội $$\wedge$$ | Phép nhân $$\cdot$$ |
| Phép tuyển $$\vee$$ | Phép cộng $$+$$ |
| Phủ định $$\neg$$ | Phần tử bù $$'$$ |
| Hằng đúng (Tautology) | Biểu thức bằng 1 |

## Ứng dụng trong khoa học máy tính

Đại số Boolean xuất hiện ở nhiều lớp của hệ thống tính toán:

- **Mạch số và CPU**: phép cộng, so sánh và điều khiển điều kiện được hiện thực bằng mạng cổng.
- **Truy vấn dữ liệu**: điều kiện `WHERE` trong SQL tổ hợp bằng AND, OR, NOT.
- **Bitmask và đồ họa**: phép AND/OR/NOT trên bit dùng để che, lọc và kết hợp mặt nạ.
- **Kiểm soát truy cập**: chính sách ACL (*Access Control List*) được đánh giá như biểu thức Boolean trên thuộc tính chủ thể và đối tượng.

<div class="textbook-example" markdown="1">

**Ví dụ.** Truy vấn tìm kiếm dạng “cat AND dog NOT fish” tương ứng một biểu thức Boolean trên tập tài liệu: mỗi tài liệu được gán **1** hoặc **0** theo sự hiện diện của từng từ khóa.

</div>

## Bài tập

### Bài tập 1: Kiểm tra hằng đẳng thức

Dùng bảng chân trị kiểm tra các hằng đẳng thức sau:

a) $$x + yz = (x + y)(x + z)$$

b) $$x(x' + y) = xy$$

<details>
<summary>Đáp án</summary>

**a)** Bảng chân trị:

| $$x$$ | $$y$$ | $$z$$ | $$yz$$ | $$x + yz$$ | $$x + y$$ | $$x + z$$ | $$(x+y)(x+z)$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Hai cột cuối giống nhau, hằng đẳng thức đúng.

**b)** Dùng biến đổi đại số:

<div class="textbook-equation" markdown="1">
$$x(x' + y) = xx' + xy = 0 + xy = xy$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2: Áp dụng De Morgan

Đơn giản hóa các biểu thức sau dùng luật De Morgan:

a) $$(x' + y)'$$

b) $$(x'y')'$$

c) $$(x + yz)'$$

<details>
<summary>Đáp án</summary>

a) $$(x' + y)' = (x')' \cdot y' = x \cdot y'$$

b) $$(x'y')' = (x')' + (y')' = x + y$$

c) $$(x + yz)' = x' \cdot (yz)' = x'(y' + z')$$

</details>

### Bài tập 3: Chứng minh bằng đại số

Chứng minh các hằng đẳng thức sau bằng phương pháp đại số:

a) $$x + x'y = x + y$$

b) $$xy + x'y' = (x + y')(x' + y)$$

<details>
<summary>Đáp án</summary>

a) 
<div class="textbook-equation" markdown="1">
$$
\begin{aligned}
x + x'y &= (x + x')(x + y) \\
        &= 1 \cdot (x + y) \\
        &= x + y
\end{aligned}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
b) 
<div class="textbook-equation" markdown="1">
$$
\begin{aligned}
xy + x'y' &= (xy + x')(xy + y') \\
          &= (x + x')(y + x')(x + y')(y + y') \\
          &= 1 \cdot (y + x') \cdot (x + y') \cdot 1 \\
          &= (x' + y)(x + y')
\end{aligned}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 4: Tư duy phản biện

Có hai sinh viên tranh luận: "Mọi hàm Boole 2 biến đều có thể biểu diễn bằng chỉ OR và NOT." Người thứ nhất nói đúng, người thứ hai nói sai. Ai đúng? Giải thích.

<details>
<summary>Đáp án</summary>

Người thứ nhất đúng. Bộ {OR, NOT} là một tập đầy đủ vì AND có thể được biểu diễn qua OR và NOT: $$x \cdot y = (x' + y')'$$ (luật De Morgan). Tương tự, NAND, NOR và mọi hàm khác đều có thể xây dựng từ OR và NOT. Trong thiết kế mạch, điều này cho phép dùng chỉ một loại cổng để xây dựng toàn bộ hệ thống.
</details>


### Bài tập 5: $$P(U)$$ và $$B^n$$

(a) Với $$U=\{a,b\}$$, liệt kê 4 phần tử của $$P(U)$$ và tính $$\{a\}\cup\{b\}$$, $$\{a\}\cap\{b\}$$, bù của $$\{a\}$$.  
(b) Vì sao $$B^2$$ có 4 phần tử? Phép OR từng bit của $$(1,0)$$ và $$(0,1)$$ là gì?

<details>
<summary>Đáp án</summary>

(a) $$\emptyset,\{a\},\{b\},\{a,b\}$$; hợp $$=\{a,b\}$$; giao $$=\emptyset$$; bù $$\{a\}=\{b\}$$.  
(b) $$2^2=4$$ vector bit; OR từng bit $$(1,1)$$.

</details>

## Xem thêm

- [Boolean Algebra and Karnaugh Maps](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Neso Academy (Gate level + minimization)

## Tóm tắt

1. **Đại số logic** $$B=\{0,1\}$$: OR, AND, NOT và mười hằng đẳng thức cơ bản; lưu ý $$1+1=1$$.
2. **Đại số Boole** trừu tượng: tiên đề Huntington; ví dụ $$P(U)$$ (tập con) và $$B^n$$.
3. Chứng minh bằng **đại số** hoặc **bảng chân trị**; **đối ngẫu** nhân đôi số đẳng thức.
4. Phép dẫn xuất: XOR, kéo theo, tương đương, **NAND/NOR** (đầy đủ chức năng).
5. Mục tiếp theo: hàm Boole, minterm và dạng nối rời chính tắc (SOP chuẩn).

## Tài liệu Tham khảo

1. George Boole, *An Investigation of the Laws of Thought*, 1854.
2. Claude E. Shannon, *A Symbolic Analysis of Relay and Switching Circuits*, MIT, 1937 — luận văn thạc sĩ đặt nền móng cho thiết kế mạch số.
3. M. Morris Mano, *Digital Design*, Pearson, các chương 1-2.
