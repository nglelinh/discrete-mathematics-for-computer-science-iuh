---
layout: post
title: "Hàm Boole và Các Dạng Chuẩn"
categories: chapter13
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Hàm Boole, bảng chân trị, minterm, maxterm, dạng chuẩn SOP và POS, cách chuyển đổi giữa hai dạng, bài toán đa số (majority) và khái niệm công thức đa thức tối tiểu."
---

> **Câu chuyện mở đầu:** Mọi bộ vi xử lý hiện đại — từ chiếc điện thoại trên tay bạn đến siêu máy tính huấn luyện AI — thực chất chỉ làm đúng một việc: tính giá trị của các **hàm Boole** nhận đầu vào $$0/1$$ và trả ra $$0/1$$. Với $$n$$ biến đầu vào có tới $$2^{2^n}$$ hàm khác nhau (chỉ riêng $$n = 4$$ đã có **65.536** hàm!). Làm sao biểu diễn **mọi** hàm Boole một cách chuẩn mực, duy nhất và dễ biến thành mạch điện? Câu trả lời nằm ở **dạng chuẩn SOP (tổng các minterm)** và **POS (tích các maxterm)**!

<div class="textbook-epigraph" markdown="1">

"A Boolean function is completely determined by its truth table — the algebra only rewrites that table more compactly."

<span class="epigraph-attribution">— Tinh thần thiết kế logic</span>

</div>

Sau đại số trên tập $$\{0,1\}$$ với các phép AND, OR, NOT, đối tượng tiếp theo là **hàm Boole** — ánh xạ từ một bộ bit đầu vào sang một bit đầu ra.

Bài học này trình bày bốn nội dung chính:

1. mô tả hàm Boole bằng **bảng chân trị**;
2. xây dựng dạng **SOP** chuẩn (tổng các tích / *Sum of Products*);
3. xây dựng dạng **POS** chuẩn (tích các tổng / *Product of Sums*);
4. chuyển đổi giữa hai dạng chuẩn trước khi thực hiện tối thiểu hóa và thiết kế mạch.

Một biểu thức điều kiện trong lập trình, chẳng hạn `if ((x && !y) || z)`, chính là một hàm $$F : \{0,1\}^n \to \{0,1\}$$. Khi $$n$$ nhỏ, bảng chân trị mô tả trọn vẹn hàm; khi $$n$$ lớn hơn, các dạng chuẩn vẫn cung cấp biểu diễn đầy đủ làm điểm xuất phát cho bước rút gọn.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** hàm Boole $$n$$ biến và lập bảng chân trị tương ứng.
- **Viết** minterm, maxterm và dạng chuẩn SOP (tổng các tích) / POS (tích các tổng) từ bảng chân trị.
- **Chuyển đổi** giữa hai dạng chuẩn SOP và POS.
- **Đếm** số hàm Boole $$n$$ biến và giải thích công thức $$2^{2^n}$$.
- **Mô hình hóa** các yêu cầu logic cơ bản (chẳng hạn hàm đa số — majority) thành hàm Boole.

**Từ khóa**: hàm Boole, minterm, maxterm, SOP (sum of products / tổng các tích), POS (product of sums / tích các tổng), dạng chuẩn tắc (canonical form).

</div>

## Bản đồ kiến thức nền: Hàm Boole và Dạng chuẩn nằm ở đâu trong Khoa học Máy tính?

### 1. Đại số Boole trên $$\{0, 1\}^n$$
- **Bản chất:** Một hàm Boole $$f: \{0, 1\}^n \to \{0, 1\}$$ được xác định hoàn toàn bởi bảng chân trị gồm $$2^n$$ dòng.
- **Số lượng hàm:** Vì mỗi dòng có 2 lựa chọn ($$0$$ hoặc $$1$$), tồn tại đúng $$2^{2^n}$$ hàm Boole $$n$$ biến.

### 2. Minterm (SOP chuẩn) và Maxterm (POS chuẩn)
- **Minterm $$m_i$$:** Tích đủ $$n$$ biến (nguyên hoặc đảo) chỉ nhận giá trị $$1$$ tại đúng **1 dòng duy nhất** $$i$$. Mọi hàm Boole là tổng (OR) của đúng các minterm nơi $$f = 1$$ (**Dạng tổng các tích chuẩn — Canonical SOP**).
- **Maxterm $$M_i$$:** Tổng đủ $$n$$ biến chỉ nhận giá trị $$0$$ tại đúng **1 dòng duy nhất** $$i$$. Mọi hàm Boole là tích (AND) của các maxterm nơi $$f = 0$$ (**Canonical POS**).

### 3. Tính Đầy đủ Hàm (Functional Completeness)
- **Bản chất:** Nhờ dạng SOP chuẩn, bộ ba cổng $$\{\text{AND}, \text{OR}, \text{NOT}\}$$ biểu diễn được **mọi** hàm Boole. Thậm chí chỉ riêng cổng **NAND** (hoặc chỉ riêng **NOR**) cũng đủ xây dựng toàn bộ CPU!

## Ví dụ tính tay cầm tay chỉ việc: Hàm Đa số 3 biến (Majority Function)

Xét mạch biểu quyết 3 cảm biến $$f(x, y, z) = 1$$ khi và chỉ khi có ít nhất **2 trong 3** biến bằng $$1$$:
1. **Liệt kê các dòng mà $$f = 1$$** (theo chỉ số nhị phân $$(x,y,z)_2$$):
   - $$(0, 1, 1) \to m_3 = \bar{x}yz$$
   - $$(1, 0, 1) \to m_5 = x\bar{y}z$$
   - $$(1, 1, 0) \to m_6 = xy\bar{z}$$
   - $$(1, 1, 1) \to m_7 = xyz$$
2. **Dạng SOP chuẩn:** $$f(x, y, z) = \sum m(3, 5, 6, 7) = \bar{x}yz + x\bar{y}z + xy\bar{z} + xyz$$.
3. **Rút gọn đại số bằng tay** (nhân bản $$xyz = xyz + xyz + xyz$$ nhờ luật lũy đẳng $$a + a = a$$!):
   $$
   f = (\bar{x}yz + xyz) + (x\bar{y}z + xyz) + (xy\bar{z} + xyz) = yz + xz + xy!
   $$
   Từ 4 minterm (12 cổng/đầu vào) rút xuống còn đúng 3 tích 2 biến!
4. **Dạng POS chuẩn:** Các dòng $$f = 0$$ là $$0, 1, 2, 4 \implies f = \prod M(0, 1, 2, 4)$$.

### Khung giải thích: Từ Bảng chân trị sang Biểu thức Chuẩn (nên đọc chậm)

#### Bước 1: Đọc chỉ số nhị phân từng dòng bảng chân trị
Mỗi tổ hợp $$n$$ bit $$(x_{n-1}\dots x_0)$$ ứng với một số nguyên $$i \in \{0, \dots, 2^n-1\}$$.

#### Bước 2: Dùng minterm chọn các dòng $$f = 1$$ (SOP) hoặc maxterm loại các dòng $$f = 0$$ (POS)
Trong minterm: bit $$1$$ giữ nguyên biến, bit $$0$$ lấy phủ định. Trong maxterm: ngược lại hoàn toàn (bit $$0$$ giữ nguyên, bit $$1$$ lấy phủ định).

#### Bước 3: Chuyển đổi tức thì SOP $$\leftrightarrow$$ POS nhờ tập bù
Nếu $$f = \sum m(S)$$ thì lập tức $$f = \prod M(\{0,\dots,2^n-1\} \setminus S)$$ — không cần tính lại bảng chân trị!

#### Bước 4: Tối ưu hóa trước khi chế tạo phần cứng
Dạng chuẩn luôn tồn tại và duy nhất, nhưng thường cồng kềnh; các bài tiếp theo (tối thiểu hóa đại số, K-map, Quine–McCluskey) sẽ nén dạng chuẩn thành mạch điện ít cổng nhất.

$$
\text{Bảng chân trị }2^n\text{ dòng}
\;\xrightarrow{\;\text{Minterm / Maxterm}\;}\;
\text{SOP }\sum m(S) \;\&\; \text{POS }\prod M(\bar{S})
\;\xrightarrow{\;\text{Rút gọn}\;}\;
\text{Mạch logic tối ưu}.
$$

## Hàm Boole và bảng chân trị

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Một **hàm Boole** $$n$$ biến là một ánh xạ

$$
F : \{0,1\}^n \to \{0,1\}.
$$

Hai hàm Boole bằng nhau khi và chỉ khi chúng cho cùng giá trị đầu ra trên mọi bộ đầu vào $$(x_1, \ldots, x_n) \in \{0,1\}^n$$.

</div>

Tập nguồn có đúng $$2^n$$ phần tử và mỗi phần tử có 2 lựa chọn giá trị đầu ra (0 hoặc 1). Do đó, tổng số hàm Boole $$n$$ biến là

$$
2^{(2^n)}.
$$

Với $$n = 2$$ có $$16$$ hàm; với $$n = 3$$ có $$256$$ hàm; với $$n = 4$$ con số đã vượt $$65\,000$$. Dù không thể liệt kê hết mọi hàm khi $$n$$ lớn, ta luôn có thể mô tả một hàm cụ thể bằng bảng chân trị hoặc công thức đại số.

![Bảng chân trị](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.7">Bảng chân trị.</p>

### Thuật ngữ

| Thuật ngữ | Nghĩa |
|:---|:---|
| **Từ đơn (litera)** | Biến ở dạng nguyên $$x_i$$ hoặc dạng bù $$\bar x_i$$ |
| **Đơn thức** | Tích AND của các từ đơn (không chứa đồng thời cả $$x_i$$ và $$\bar x_i$$); **bậc** là số từ đơn khác nhau |
| **Từ tối tiểu / tiểu hạng (minterm)** | Đơn thức chứa đầy đủ $$n$$ biến |
| **Công thức đa thức (SOP)** | Tổng OR của các đơn thức, không nhất thiết ở dạng chuẩn |
| **Dạng nối rời chính tắc (SOP chuẩn)** | Tổng OR của các từ tối tiểu (còn gọi là DNF đầy đủ) |
| **Công thức đa thức tối tiểu** | Dạng SOP gọn nhất về số hạng và số litera (mục tiêu của rút gọn đại số và K-map) |

<div class="textbook-example" markdown="1">

**Ví dụ (thuật ngữ).** Với 3 biến $$x,y,z$$: $$x$$ và $$\bar y$$ là các từ đơn; $$xy$$ và $$yz$$ là các đơn thức; $$xy\bar z$$ là một từ tối tiểu (minterm); $$E = xy + yz$$ là công thức đa thức; $$F = xyz + \bar x\bar y\bar z$$ là dạng nối rời chính tắc gồm hai minterm.

</div>

### Ví dụ bỏ phiếu theo đa số (majority)

<div class="textbook-example" markdown="1">

**Ví dụ (hàm đa số 3 phiếu).** Mỗi phiếu biểu diễn bằng một biến $$x,y,z \in \{0,1\}$$ (1 là tán thành). Hàm $$f$$ bằng **1** (thông qua) khi **đa số** tán thành, tức có **ít nhất hai** phiếu bằng **1**.

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

Dạng SOP chuẩn: $$f = m_3 + m_5 + m_6 + m_7$$ (ứng với các hàng **3, 5, 6, 7**).  
Sau khi rút gọn (xem bài 13.3–13.4): $$f = xy + xz + yz$$ — đây là **mạch bỏ phiếu theo đa số** (majority).

</div>

## Minterm (từ tối tiểu) và dạng SOP chuẩn

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Minterm** (*từ tối tiểu* / *tiểu hạng*) của $$n$$ biến là tích AND của đúng $$n$$ litera, trong đó mỗi biến xuất hiện đúng một lần ở dạng nguyên hoặc dạng bù. Ký hiệu $$m_k$$ ứng với hàng thứ $$k$$ khi đọc bộ giá trị nhị phân của các biến.

</div>

**Quy tắc viết minterm từ một hàng của bảng chân trị:**

1. Biến nhận giá trị **0** → viết ở dạng **bù** (ví dụ $$x'$$).
2. Biến nhận giá trị **1** → viết ở dạng **nguyên** (ví dụ $$x$$).
3. Lấy tích (AND) tất cả các litera thu được.

Với hai biến $$x$$ và $$y$$:

| $$x$$ | $$y$$ | Minterm | Ký hiệu |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x'y'$$ | $$m_0$$ |
| 0 | 1 | $$x'y$$ | $$m_1$$ |
| 1 | 0 | $$xy'$$ | $$m_2$$ |
| 1 | 1 | $$xy$$ | $$m_3$$ |

Mỗi minterm $$m_k$$ nhận giá trị **1** tại đúng **một** hàng thứ $$k$$ và bằng **0** tại mọi hàng còn lại. Do đó, nếu hàm $$F$$ bằng **1** đúng trên các hàng $$k_1, \ldots, k_r$$ thì

$$
F = m_{k_1} + m_{k_2} + \cdots + m_{k_r}
$$

là biểu diễn đầy đủ của $$F$$, gọi là **dạng tổng các tích chuẩn** (canonical SOP / dạng nối rời chính tắc).

<div class="textbook-example" markdown="1">

**Ví dụ.** Cho hàm $$F(x, y, z)$$ bằng **1** tại các tổ hợp $$001$$, $$010$$, $$100$$, $$111$$ (và bằng **0** ở các hàng còn lại). Các minterm tương ứng là $$x'y'z$$, $$x'yz'$$, $$xy'z'$$, $$xyz$$, suy ra:

$$
F = x'y'z + x'yz' + xy'z' + xyz
$$

(tương ứng các hàng **1, 2, 4, 7**).

</div>

Cách làm thực hành luôn có hệ thống: duyệt cột $$F$$, lấy tất cả các hàng có giá trị **1**, viết minterm cho từng hàng rồi nối chúng bằng phép OR mà không cần đoán công thức.

![Half adder — SOP](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.9">Bit tổng của mạch cộng nửa (half adder) là phép XOR: gồm hai minterm $$A'B + AB'$$ ở dạng SOP chuẩn.</p>

### Hai cách lập dạng nối rời chính tắc (SOP chuẩn)

**Cách A — từ bảng chân trị** (phổ biến nhất trong bài tập): xác định các hàng có $$F=1$$, viết minterm tương ứng rồi lấy tổng OR.

**Cách B — khai triển từ công thức đa thức** (khi đã có biểu thức nhưng chưa ở dạng chuẩn):

1. Biến đổi $$F$$ về tổng các đơn thức (dùng luật phân phối nếu cần).
2. Với mỗi đơn thức **thiếu** biến $$x_i$$, nhân thêm nhân tử $$(x_i + \bar x_i)$$ (vì $$x_i + \bar x_i = 1$$).
3. Khai triển và loại bỏ các hạng trùng lặp để thu được tổng các minterm.

<div class="textbook-example" markdown="1">

**Ví dụ (Cách B).** Đưa $$f(x,y) = x + \bar y$$ về dạng SOP chuẩn:

- Đơn thức $$x$$ thiếu biến $$y$$: $$x(y+\bar y) = xy + x\bar y$$.
- Đơn thức $$\bar y$$ thiếu biến $$x$$: $$\bar y(x+\bar x) = x\bar y + \bar x\bar y$$.
- Gộp hai kết quả và bỏ hạng trùng $$x\bar y$$: $$f = xy + x\bar y + \bar x\bar y$$.

Đối chiếu với bảng chân trị: $$f=1$$ tại $$(0,0), (1,0), (1,1)$$, đúng với các hàng **0, 2, 3**.

</div>

## Maxterm và dạng POS chuẩn

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Maxterm** (tổng chuẩn) của $$n$$ biến là tổng OR của đúng $$n$$ litera, trong đó mỗi biến xuất hiện đúng một lần ở dạng nguyên hoặc dạng bù. Ký hiệu là $$M_k$$.

</div>

**Quy tắc viết maxterm** (ngược lại với minterm):

1. Biến nhận giá trị **1** → viết ở dạng **bù**.
2. Biến nhận giá trị **0** → viết ở dạng **nguyên**.
3. Lấy tổng (OR) tất cả các litera thu được.

Nhờ quy tắc này, maxterm $$M_k$$ nhận giá trị **0** tại đúng hàng $$k$$ và bằng **1** ở mọi hàng còn lại. Với hai biến $$x, y$$:

| $$x$$ | $$y$$ | Maxterm | Ký hiệu |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x + y$$ | $$M_0$$ |
| 0 | 1 | $$x + y'$$ | $$M_1$$ |
| 1 | 0 | $$x' + y$$ | $$M_2$$ |
| 1 | 1 | $$x' + y'$$ | $$M_3$$ |

Nếu $$F$$ bằng **0** đúng trên các hàng $$\ell_1, \ldots, \ell_s$$ thì

$$
F = M_{\ell_1} \cdot M_{\ell_2} \cdots M_{\ell_s}
$$

là **dạng tích các tổng chuẩn** (canonical POS).

Với ví dụ trên ($$F=1$$ tại các hàng **1, 2, 4, 7**), các hàng có $$F = 0$$ là **0, 3, 5, 6**, nên:

$$
F = (x + y + z)(x + y' + z')(x' + y + z')(x' + y' + z).
$$

Hai dạng chuẩn cùng mô tả một hàm duy nhất nhưng theo hai góc nhìn bù nhau:

- **SOP** (tổng các tích) tập trung vào các hàng có $$F = 1$$.
- **POS** (tích các tổng) tập trung vào các hàng có $$F = 0$$.

SOP thuận tiện cho kiến trúc mạch hai tầng AND–OR, còn POS thuận tiện cho mạch OR–AND. Trong logic mệnh đề, dạng chuẩn hội (CNF) có cùng cấu trúc với POS.

## Chuyển đổi giữa SOP và POS

**Cách 1 — thông qua tập chỉ số hàng.** Nếu biết các hàng có $$F=1$$ thì các hàng có $$F=0$$ chính là phần bù trong $$\{0,1,\ldots,2^n-1\}$$; từ đó lập POS chuẩn bằng tích các maxterm tại các hàng $$F=0$$.

**Cách 2 — thông qua phủ định.** Viết SOP chuẩn cho hàm phủ định $$F'$$ (gồm các minterm ứng với hàng $$F = 0$$), rồi áp dụng luật De Morgan cho $$(F')'$$ để thu được POS chuẩn của $$F$$.

Cả hai cách đều cho cùng một kết quả và có thể dùng để kiểm tra chéo lẫn nhau.

## Một số hàm hai biến quen thuộc

Trong số $$16$$ hàm Boole hai biến, các hàm sau xuất hiện phổ biến nhất:

| Hàm | Biểu thức | Tên gọi |
|:---|:---|:---|
| Hằng | $$0$$, $$1$$ | Hàm hằng |
| AND / OR | $$xy$$, $$x + y$$ | Phép hội / tuyển |
| XOR | $$x \oplus y = x'y + xy'$$ | Tuyển loại trừ |
| NAND / NOR | $$(xy)'$$, $$(x + y)'$$ | Phủ định của AND / OR |
| XNOR | $$xy + x'y'$$ | Tương đương |

Tập $$\{\text{AND}, \text{OR}, \text{NOT}\}$$ đủ để biểu diễn mọi hàm Boole (nhờ dạng SOP). Riêng phép NAND cũng đủ chức năng như đã trình bày ở bài 13.1.

![Venn AND](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-AND.png)

<p class="textbook-figure-caption" data-figure="13.10">Phép AND tương ứng với phép giao hai tập hợp, còn phép OR tương ứng với phép hợp.</p>

## Từ SOP chuẩn đến công thức đa thức tối tiểu

Dạng SOP **chuẩn** luôn chính xác nhưng thường khá **dài**. Các bài tiếp theo hướng tới **công thức đa thức tối tiểu**: một biểu thức SOP ngắn gọn hơn (ít hạng tử và ít litera hơn) nhưng có **cùng bảng chân trị** với hàm ban đầu.

Hai biểu thức $$F$$ và $$G$$ được so sánh dựa trên số hạng tử và tổng số litera. $$F$$ gọi là **tối tiểu** nếu không tồn tại biểu thức tương đương $$G$$ nào đơn giản hơn $$F$$; một hàm Boole có thể có nhiều dạng tối tiểu tương đương nhau.

Quy trình làm việc chuẩn gồm ba bước:

1. Lập dạng SOP chuẩn từ bảng chân trị (hoặc bằng cách khai triển).  
2. Rút gọn bằng biến đổi đại số (13.3), **bản đồ Karnaugh** (13.4) hoặc phương pháp Quine–McCluskey (13.5).  
3. Kiểm chứng lại kết quả bằng bảng chân trị.

## Ứng dụng trong lập trình và cơ sở dữ liệu

Trong lập trình và hệ quản trị cơ sở dữ liệu, quy trình xử lý biểu thức điều kiện cũng đi theo tư duy tương tự: biểu diễn chính xác rồi tối ưu hóa. Trình tối ưu truy vấn SQL chuyển điều kiện `WHERE` thành cây biểu thức logic để rút gọn và sắp xếp thứ tự đánh giá các phép AND/OR. Việc nắm vững minterm giúp liên kết trực tiếp từng tổ hợp đầu vào trong bảng chân trị với hành vi của điều kiện trong mã nguồn.

Các bài 13.3–13.5 tiếp tục đi sâu vào bước rút gọn biểu thức, trước khi bài **13.6** chuyển sang thiết kế mạch logic thực tế.

<div class="interactive-demo" markdown="1">
Thử xây dựng dạng SOP (tổng các tích) và POS (tích các tổng) từ bảng chân trị bằng công cụ tương tác dưới đây.
<div data-demo="boolean-expression-evaluator"></div>
</div>
<script src="{{ '/public/js/boolean-expression-evaluator.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Cho hàm $$F(x,y,z) = 1$$ tại các tổ hợp $$010, 011, 101, 111$$ (các hàng còn lại bằng $$0$$). Viết dạng SOP chuẩn (tổng các minterm) và POS chuẩn (tích các maxterm) kèm khai triển.

<details>
<summary>Đáp án</summary>

Các hàng có $$F=1$$ là **2, 3, 5, 7**, nên dạng SOP chuẩn là:  
$$F = x'yz' + x'yz + xy'z + xyz$$.  
Các hàng có $$F=0$$ là **0, 1, 4, 6** (ứng với `000`, `001`, `100`, `110`), nên dạng POS chuẩn là:  
$$F = M_0 M_1 M_4 M_6 = (x+y+z)(x+y+z')(x'+y+z)(x'+y'+z)$$.

</details>

### Bài tập 2

Một đèn báo sáng khi **ít nhất hai** trong ba cảm biến $$A, B, C$$ kích hoạt. Lập bảng chân trị, viết dạng SOP chuẩn và rút gọn về $$AB + BC + AC$$.

<details>
<summary>Đáp án</summary>

Các hàng có $$F=1$$ là **3, 5, 6, 7**.  
Rút gọn: $$A'BC + AB'C + ABC' + ABC = BC + AC + AB$$ (hàm đa số — majority).

</details>

### Bài tập 3

Cho hàm $$F$$ nhận giá trị **1** tại các hàng **0, 2, 5, 7**. Viết dạng POS chuẩn của $$F$$.

<details>
<summary>Đáp án</summary>

Các hàng có $$F=0$$ là **1, 3, 4, 6**.  
Do đó $$F = M_1 \cdot M_3 \cdot M_4 \cdot M_6$$.

</details>

### Bài tập 4

Có bao nhiêu hàm Boole 3 biến luôn nhận giá trị **0** tại mọi hàng có số bit **1** là số chẵn?

<details>
<summary>Đáp án</summary>

Trong 8 hàng của bảng chân trị 3 biến, 4 hàng có số bit 1 chẵn (000, 011, 101, 110) bị cố định bằng **0**; 4 hàng còn lại có thể chọn tự do 0 hoặc 1, nên có $$2^4 = 16$$ hàm.

</details>

### Bài tập 5

Đưa hàm $$f(x,y,z) = \bar x + \bar y z$$ về dạng nối rời chính tắc bằng **Cách B** (nhân bổ sung $$x_i + \bar x_i$$), rồi đối chiếu với bảng chân trị.

<details>
<summary>Đáp án</summary>

Khai triển $$\bar x(y+\bar y)(z+\bar z)$$ thu được 4 minterm có $$x=0$$; khai triển $$\bar y z(x+\bar x)$$ thu được $$x\bar y z + \bar x\bar y z$$ (trong đó $$\bar x\bar y z$$ bị trùng nên gộp lại).  
Kết quả gồm các hàng có $$x=0$$ cùng với tổ hợp $$(1,0,1)$$, tức là các hàng **0, 1, 2, 3, 5**.

</details>

## Xem thêm

- Mục 13.1 — luật De Morgan và các hằng đẳng thức cơ bản.
- Mục 13.3 — cổng logic và tối thiểu hóa đại số.

## Tóm tắt

1. Hàm Boole là ánh xạ $$\{0,1\}^n \to \{0,1\}$$, được xác định duy nhất bởi bảng chân trị của nó.
2. **Minterm** (từ tối tiểu) bằng 1 tại đúng một hàng; tổng các minterm tại các hàng $$F=1$$ tạo nên **dạng SOP chuẩn** (dạng nối rời chính tắc).
3. **Maxterm** bằng 0 tại đúng một hàng; tích các maxterm tại các hàng $$F=0$$ tạo nên **dạng POS chuẩn**.
4. SOP và POS tương đương nhau và có thể chuyển đổi qua phần bù tập chỉ số hàng hoặc luật De Morgan.
5. Dạng SOP chuẩn là điểm xuất phát để rút gọn thành **công thức đa thức tối tiểu** bằng đại số hoặc bản đồ Karnaugh.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=xnLBbOYYnHM">Sum of Products (Part 1) | SOP Form</a> — Neso Academy, tiếng Anh. Giới thiệu dạng tổng các tích (SOP).
- <a href="https://www.youtube.com/watch?v=nXsiLPJfDZ4">Product of Sums (Part 1) | POS Form</a> — Neso Academy, tiếng Anh. Trình bày dạng tích các tổng (POS) và maxterm.
- <a href="https://www.youtube.com/watch?v=d-amzrRVhfE">Minterms, Maxterms, and Canonical Boolean Expressions</a> — EngMicroLectures, tiếng Anh. Cách lập minterm, maxterm và biểu thức chính tắc từ bảng chân trị.
