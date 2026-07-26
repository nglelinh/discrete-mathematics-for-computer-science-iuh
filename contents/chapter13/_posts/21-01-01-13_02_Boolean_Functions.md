---
layout: post
title: "Hàm Boole và Các Dạng Chuẩn"
categories: chapter13
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Hàm Boole, minterm (từ tối tiểu), dạng nối rời chính tắc / SOP–POS chuẩn, khai triển (xi+xī), majority, và công thức đa thức tối tiểu."
---

<div class="textbook-epigraph" markdown="1">

"A Boolean function is completely determined by its truth table — the algebra only rewrites that table more compactly."

<span class="epigraph-attribution">— Tinh thần thiết kế logic</span>

</div>

Ở bài 13.1 chúng ta đã có đại số trên tập $$\{0,1\}$$ với AND, OR, NOT. Bài này chuyển từ *phép toán* sang *hàm*: đối tượng quan tâm không còn là một ký hiệu đơn lẻ, mà là một **ánh xạ** từ chuỗi bit đầu vào sang bit đầu ra.

Lộ trình của bài gồm bốn bước:

1. Mô tả hàm bằng **bảng chân trị**.
2. Viết công thức đầy đủ dạng **SOP** (tổng các tích / *Sum of Products*).
3. Viết công thức đầy đủ dạng **POS** (tích các tổng / *Product of Sums*).
4. Chuyển qua lại giữa hai dạng — bước trung gian trước khi rút gọn và vẽ mạch.

Điều kiện trong mã nguồn như `if ((x && !y) || z)` chính là một hàm $$F : \{0,1\}^n \to \{0,1\}$$. Khi $$n$$ nhỏ, bảng liệt kê hết hành vi; khi $$n$$ lớn, dạng chuẩn vẫn cho một **công thức đầy đủ** (có thể dài) trước khi tối thiểu hóa.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** hàm Boole $$n$$ biến và lập bảng chân trị.
- **Viết** minterm, maxterm và dạng chuẩn SOP (tổng các tích) / POS (tích các tổng) từ bảng.
- **Chuyển** giữa SOP (tổng các tích) và POS (tích các tổng).
- **Đếm** số hàm Boole $$n$$ biến và giải thích $$2^{2^n}$$.
- **Mô hình hóa** yêu cầu đơn giản (ví dụ majority) thành hàm Boole.

**Từ khóa**: hàm Boole, minterm, maxterm, SOP (sum of products / tổng các tích), POS (product of sums / tích các tổng), dạng chuẩn tắc (canonical form).

</div>

## 1. Hàm Boole và bảng chân trị

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Một **hàm Boole** $$n$$ biến là ánh xạ

$$
F : \{0,1\}^n \to \{0,1\}.
$$

Hai hàm bằng nhau khi và chỉ khi chúng cho cùng giá trị trên mọi bộ $$(x_1, \ldots, x_n) \in \{0,1\}^n$$.

</div>

Miền có đúng $$2^n$$ phần tử; mỗi phần tử gán được hai giá trị đầu ra. Do đó số hàm Boole $$n$$ biến là

$$
2^{(2^n)}.
$$

Với $$n = 2$$ đã có $$16$$ hàm; với $$n = 3$$ có $$256$$ hàm; với $$n = 4$$ con số vượt $$65\,000$$. Ta không liệt kê hết mọi hàm, nhưng **mô tả** từng hàm bằng bảng hoặc công thức thì luôn làm được.

![Bảng chân trị](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.7">Bảng chân trị liệt kê đủ $$2^n$$ tổ hợp đầu vào; mỗi cột đầu ra định nghĩa một hàm.</p>

Bảng chân trị là “hợp đồng” hành vi: mỗi hàng là một gán biến, cột $$F$$ là kết quả. Mọi biểu thức SOP (tổng các tích) hay POS (tích các tổng) chỉ là cách **nén** bảng đó thành công thức.

### 1.1. Thuật ngữ slide / giáo trình Việt

Trên slide “Đại số Boole” còn dùng các tên sau — **cùng nghĩa** với thuật ngữ quốc tế:

| Thuật ngữ slide | Nghĩa trong bài này |
|:---|:---|
| **Từ đơn** | Litera: $$x_i$$ hoặc $$\bar x_i$$ |
| **Đơn thức** | Tích các từ đơn (không chứa cả $$x_i$$ và $$\bar x_i$$); **bậc** = số từ đơn khác nhau |
| **Từ tối tiểu** / **tiểu hạng** | Đơn thức đúng $$n$$ từ đơn = **minterm** |
| **Công thức đa thức** | Tổng (OR) các đơn thức = **SOP** (tổng các tích), chưa nhất thiết chuẩn |
| **Dạng nối rời chính tắc** | Tổng các từ tối tiểu = **SOP (tổng các tích) chuẩn** / DNF đầy đủ |
| **Công thức đa thức tối tiểu** | SOP “đơn giản nhất” theo số hạng và số litera (mục tiêu rút gọn / K-map) |

<div class="textbook-example" markdown="1">

**Ví dụ (từ vựng).** Với 3 biến $$x,y,z$$: $$x$$, $$\bar y$$ là từ đơn; $$xy$$, $$yz$$ là đơn thức; $$xy\bar z$$ là từ tối tiểu (minterm); $$E = xy + yz$$ là công thức đa thức; $$F = xyz + \bar x\bar y\bar z$$ là dạng nối rời chính tắc (hai minterm).

</div>

### 1.2. Ví dụ bỏ phiếu (majority)

<div class="textbook-example" markdown="1">

**Ví dụ (3 phiếu).** Mỗi phiếu $$x,y,z \in \{0,1\}$$ (1 = tán thành). Hàm $$f$$ = **1** (thông qua) khi **đa số** tán thành — tức **ít nhất hai** phiếu bằng **1**.

| $$x$$ | $$y$$ | $$z$$ | $$f$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | **1** |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | **1** |
| 1 | 1 | 0 | **1** |
| 1 | 1 | 1 | **1** |

SOP (tổng các tích) chuẩn: $$f = \sum m(3,5,6,7)$$.  
Sau rút gọn (bài 13.3–13.4): $$f = xy + xz + yz$$ — **mạch bỏ phiếu theo đa số** (majority).

</div>

## 2. Minterm (từ tối tiểu) và dạng SOP (tổng các tích) chuẩn

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Minterm** (*từ tối tiểu* / *tiểu hạng*) của $$n$$ biến là tích AND của đúng $$n$$ litera, mỗi biến xuất hiện đúng một lần ở dạng nguyên hoặc bù. Ký hiệu $$m_k$$ gắn với hàng thứ $$k$$ khi đọc tổ hợp biến như số nhị phân.

</div>

**Quy tắc viết minterm từ một hàng:**

1. Biến mang giá trị **0** → viết dạng **bù** (ví dụ $$x'$$).
2. Biến mang giá trị **1** → viết dạng **nguyên** (ví dụ $$x$$).
3. Nhân (AND) tất cả các litera đó.

Với hai biến $$x$$, $$y$$:

| $$x$$ | $$y$$ | Minterm | Ký hiệu |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x'y'$$ | $$m_0$$ |
| 0 | 1 | $$x'y$$ | $$m_1$$ |
| 1 | 0 | $$xy'$$ | $$m_2$$ |
| 1 | 1 | $$xy$$ | $$m_3$$ |

Mỗi minterm $$m_k$$ bằng **1** đúng **một** hàng và bằng **0** ở mọi hàng khác. Hệ quả quan trọng: nếu $$F$$ bằng **1** đúng trên các hàng $$k_1, \ldots, k_r$$ thì

$$
F = m_{k_1} + m_{k_2} + \cdots + m_{k_r}
$$

là biểu diễn **đầy đủ** của $$F$$ — gọi là **dạng tổng các tích chuẩn** (canonical SOP). Ký hiệu gọn:

$$
F = \sum m(k_1, \ldots, k_r).
$$

<div class="textbook-example" markdown="1">

**Ví dụ.** Hàm $$F(x, y, z)$$ bằng **1** tại các tổ hợp $$001$$, $$010$$, $$100$$, $$111$$ (các hàng còn lại bằng **0**). Các minterm tương ứng là $$x'y'z$$, $$x'yz'$$, $$xy'z'$$, $$xyz$$, nên

$$
F = x'y'z + x'yz' + xy'z' + xyz = \sum m(1, 2, 4, 7).
$$

</div>

Cách làm thực hành luôn giống nhau: nhìn cột $$F$$, lấy mọi hàng bằng **1**, viết minterm, nối bằng OR. Bảng đã chỉ định hết — không cần “đoán” biểu thức.

![Half adder — SOP](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.9">Bit tổng của half adder là XOR: hai minterm $$A'B + AB'$$ — dạng SOP (tổng các tích) quen thuộc từ bảng cộng 1 bit.</p>

### 2.1. Hai cách lập dạng nối rời chính tắc (SOP chuẩn)

**Cách A — từ bảng chân trị** (phổ biến nhất trên bài tập): các hàng $$F=1$$ → các minterm → OR.

**Cách B — khai triển từ công thức đa thức** (khi đã có biểu thức, chưa chuẩn):

1. Viết $$F$$ thành tổng các đơn thức (phân phối nếu cần).
2. Với mỗi đơn thức **thiếu** biến $$x_i$$, nhân thêm $$(x_i + \bar x_i)$$ (= **1**).
3. Khai triển, bỏ hạng trùng → tổng các minterm = **dạng nối rời chính tắc**.

<div class="textbook-example" markdown="1">

**Ví dụ (Cách B).** $$f(x,y) = x + \bar y$$.

- Đơn thức $$x$$ thiếu $$y$$: $$x(y+\bar y) = xy + x\bar y$$.
- Đơn thức $$\bar y$$ thiếu $$x$$: $$\bar y(x+\bar x) = x\bar y + \bar x\bar y$$.
- Gộp, bỏ trùng: $$f = xy + x\bar y + \bar x\bar y$$.

Đối chiếu bảng: $$f=1$$ tại $$(0,0),(1,0),(1,1)$$ — đúng $$\sum m(0,2,3)$$.

</div>

## 3. Maxterm và dạng POS (tích các tổng) chuẩn

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Maxterm** (tổng chuẩn) của $$n$$ biến là tổng OR của đúng $$n$$ litera, mỗi biến một lần (nguyên hoặc bù). Ký hiệu $$M_k$$.

</div>

**Quy tắc viết maxterm** — **ngược** minterm:

1. Biến mang giá trị **1** → viết dạng **bù**.
2. Biến mang giá trị **0** → viết dạng **nguyên**.
3. Cộng (OR) tất cả các litera đó.

Nhờ vậy maxterm $$M_k$$ bằng **0** đúng tại hàng $$k$$, và bằng **1** ở mọi hàng khác. Với hai biến:

| $$x$$ | $$y$$ | Maxterm | Ký hiệu |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x + y$$ | $$M_0$$ |
| 0 | 1 | $$x + y'$$ | $$M_1$$ |
| 1 | 0 | $$x' + y$$ | $$M_2$$ |
| 1 | 1 | $$x' + y'$$ | $$M_3$$ |

Nếu $$F$$ bằng **0** đúng trên các hàng $$\ell_1, \ldots, \ell_s$$ thì

$$
F = M_{\ell_1} \cdot M_{\ell_2} \cdots M_{\ell_s} = \prod M(\ell_1, \ldots, \ell_s)
$$

là **dạng tích các tổng chuẩn** (canonical POS).

Với cùng ví dụ $$\sum m(1, 2, 4, 7)$$, các hàng $$F = 0$$ là $$0, 3, 5, 6$$, nên

$$
F = \prod M(0, 3, 5, 6) = (x + y + z)(x + y' + z')(x' + y + z')(x' + y' + z).
$$

Hai dạng **cùng mô tả một hàm**:

- **SOP** (tổng các tích) “nhìn” các chỗ hàm bằng **1**.
- **POS** (tích các tổng) “nhìn” các chỗ hàm bằng **0**.

SOP thuận mạch AND–OR; POS thuận mạch OR–AND. Dạng CNF trong logic mệnh đề (tích các tuyển) cùng họ với POS.

## 4. Chuyển SOP (tổng các tích) ↔ POS (tích các tổng)

**Cách 1 — qua tập chỉ số.** Nếu $$F = \sum m(S)$$ trên không gian $$\{0, 1, \ldots, 2^n - 1\}$$ thì

$$
F = \prod M\bigl(\{0, \ldots, 2^n - 1\} \setminus S\bigr).
$$

**Cách 2 — qua phủ định.** Lập SOP (tổng các tích) của $$F'$$ (các minterm ở hàng $$F = 0$$), rồi áp dụng De Morgan để được POS (tích các tổng) của $$F$$.

Cả hai cách phải ra cùng kết quả — hữu ích để tự kiểm.

## 5. Vài hàm hai biến quen thuộc

Trong $$16$$ hàm hai biến, một số xuất hiện liên tục:

| Hàm | Biểu thức | Tên |
|:---|:---|:---|
| Hằng | $$0$$, $$1$$ | — |
| AND / OR | $$xy$$, $$x + y$$ | hội / tuyển |
| XOR | $$x \oplus y = x'y + xy'$$ | loại trừ |
| NAND / NOR | $$(xy)'$$, $$(x + y)'$$ | phủ định AND/OR |
| XNOR | $$xy + x'y'$$ | tương đương |

Bộ $$\{AND, OR, NOT\}$$ đủ biểu diễn mọi hàm (qua SOP). Riêng NAND cũng đủ, như đã nói ở 13.1.

![Venn AND](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-AND.png)

<p class="textbook-figure-caption" data-figure="13.10">Phép AND như giao hai tập — trực giác tập hợp cho tích logic; OR tương ứng hợp.</p>

## 6. Từ SOP chuẩn đến “công thức đa thức tối tiểu”

SOP (tổng các tích) **chuẩn** luôn đúng nhưng thường **dài**. Mục tiêu các bài 13.3–13.5 là tìm **công thức đa thức tối tiểu**: SOP ngắn hơn (ít hạng, ít litera) nhưng **cùng bảng chân trị**.

Trên slide, hai công thức $$F$$, $$G$$ được so **“đơn giản hơn”** bằng cách so số hạng và số từ đơn trong từng hạng. $$F$$ là **tối tiểu** nếu không còn $$G$$ thực sự đơn giản hơn $$F$$ (có thể có **nhiều** dạng tối tiểu “đơn giản như nhau” — K-map sẽ cho thấy).

Quy trình thực hành:

1. Lập SOP (tổng các tích) chuẩn từ bảng (hoặc khai triển).  
2. Rút gọn: đại số (13.3), **K-map** (13.4), hoặc Quine–McCluskey (13.5).  
3. Kiểm lại bằng bảng chân trị.

## 7. Ứng dụng ngắn

Trong lập trình và cơ sở dữ liệu, ta cũng làm việc theo cùng tư duy: viết điều kiện rõ ràng (chuẩn hóa), rồi mới tối ưu. Trình tối ưu SQL biến điều kiện `WHERE` thành cây logic và đẩy các phép AND/OR. Hiểu minterm giúp bạn đọc được vì sao một test case cụ thể bật hay tắt một nhánh `if`.

Ở các bài 13.3–13.5, cùng ý tưởng “chuẩn hóa rồi rút gọn” sẽ áp dụng cho mạch cổng.

<div class="interactive-demo" markdown="1">
Thử dựng SOP (tổng các tích) / POS (tích các tổng) từ bảng chân trị (nếu widget khả dụng).
<div data-demo="boolean-expression-evaluator"></div>
</div>
<script src="{{ '/public/js/boolean-expression-evaluator.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Cho $$F = 1$$ tại $$010, 011, 101, 111$$ (các hàng khác $$0$$). Viết $$\sum m(\ldots)$$ và $$\prod M(\ldots)$$ kèm khai triển.

<details>
<summary>Đáp án</summary>

$$F = \sum m(2, 3, 5, 7) = x'yz' + x'yz + xy'z + xyz$$.  
Hàng $$0$$: $$0, 1, 4, 6$$ → $$F = \prod M(0, 1, 4, 6)$$.

</details>

### Bài tập 2

Đèn bật khi **ít nhất hai** trong ba cảm biến $$A, B, C$$ kích hoạt. Lập bảng, viết SOP (tổng các tích), rút gọn thành $$AB + BC + AC$$.

<details>
<summary>Đáp án</summary>

$$F = \sum m(3, 5, 6, 7)$$.  
Gom: $$A'BC + AB'C + ABC' + ABC = BC + AC + AB$$ (majority).

</details>

### Bài tập 3

$$F = \sum m(0, 2, 5, 7)$$. Viết POS (tích các tổng).

<details>
<summary>Đáp án</summary>

$$F = \prod M(1, 3, 4, 6)$$.

</details>

### Bài tập 4

Có bao nhiêu hàm 3 biến luôn bằng **0** trên mọi hàng có số bit **1** chẵn?

<details>
<summary>Đáp án</summary>

Bốn hàng chẵn bị cố định **0**; bốn hàng lẻ tự do → $$2^4 = 16$$ hàm.

</details>

## Xem thêm

- Ôn De Morgan (bài 13.1) trước khi chuyển SOP ↔ POS bằng phủ định.
- Bài 13.3 — gắn dạng chuẩn với cổng và tối thiểu hóa đại số.

### Bài tập 5 — Khai triển thành SOP chuẩn

Đưa $$f(x,y,z) = \bar x + \bar y z$$ về dạng nối rời chính tắc bằng **Cách B** (bổ sung từ đơn), rồi đối chiếu $$\sum m(\ldots)$$ từ bảng.

<details>
<summary>Đáp án</summary>

$$\bar x(y+\bar y)(z+\bar z)$$ khai triển 4 minterm mang $$\bar x$$; cộng $$\bar y z(x+\bar x)$$ → thêm $$x\bar y z$$, $$\bar x\bar y z$$ (một phần trùng).  
Kết quả: các hàng $$f=1$$ là mọi chỗ $$x=0$$ cộng $$(1,0,1)$$ → $$\sum m(0,1,2,3,5)$$ (kiểm bảng).

</details>

## Tóm tắt

1. Hàm Boole là ánh xạ $$\{0,1\}^n \to \{0,1\}$$; bảng chân trị định nghĩa nó hoàn toàn.
2. **Từ tối tiểu** = minterm; **dạng nối rời chính tắc** = SOP (tổng các tích) chuẩn — lập từ bảng hoặc khai triển $$(x_i+\bar x_i)$$.
3. Maxterm “tắt” đúng một hàng; tích các maxterm nơi $$F = 0$$ cho **POS** (tích các tổng) chuẩn.
4. Hai dạng tương đương và chuyển được qua phần bù chỉ số.
5. SOP chuẩn → **công thức đa thức tối tiểu** qua đại số / K-map / QM; majority $$xy+xz+yz$$ là ví dụ điển hình.
