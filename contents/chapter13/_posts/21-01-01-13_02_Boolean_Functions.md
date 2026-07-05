---

layout: post
title: "Hàm Boole và Các Dạng Chuẩn"
categories: chapter13
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã xây dựng các quy tắc nền của đại số Boole và các hằng đẳng thức biến đổi biểu thức. Mục này giới thiệu hàm Boole — ánh xạ từ…"
---

Ở mục trước chúng ta đã xây dựng các quy tắc nền của đại số Boole và các hằng đẳng thức biến đổi biểu thức. Mục này giới thiệu **hàm Boole** — ánh xạ từ $\{0,1\}^n$ sang $\{0,1\}$ — cùng hai dạng chuẩn tắc quan trọng: tổng các tích (SOP/DNF) và tích các tổng (POS/CNF). Các dạng chuẩn này là công cụ thiết yếu cho thiết kế mạch, kiểm chứng logic và các hệ thống suy luận tự động.

![Hàm Boolean và cổng logic](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

<p class="textbook-figure-caption" data-figure="13.6">Mỗi hàm Boolean $f:\{0,1\}^n\to\{0,1\}$ tương ứng một mạch logic.</p>
![Bảng chân trị](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.7">Bảng chân trị liệt kê mọi tổ hợp đầu vào — không gian quyết định $2^n$ dòng.</p>
![Mạch Half Adder](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.8">Half Adder minh họa cách xây hàm Boolean từ bảng chân trị sang mạch.</p>
![Biểu thức SOP và POS](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

<p class="textbook-figure-caption" data-figure="13.9">Dạng tổng các tích (SOP) và tích các tổng (POS) — hai cách chuẩn biểu diễn hàm Boole.</p>
![Biểu đồ Venn AND](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-AND.png)

<p class="textbook-figure-caption" data-figure="13.10">Phép AND tương ứng vùng giao trên biểu đồ Venn — trực giác cho hàm Boolean.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** hàm Boole với $$n$$ biến và biểu diễn bằng bảng chân trị.
- **Viết** hàm Boole dưới dạng tổng các tích chuẩn (SOP) và tích các tổng chuẩn (POS).
- **Chuyển đổi** giữa các dạng biểu diễn khác nhau của hàm Boole.
- **Xây dựng** biểu thức Boole từ bảng chân trị.
- **Tính toán** số lượng hàm Boole với $$n$$ biến.

**Từ khóa**: Hàm Boole (Boolean function), dạng tổng các tích (SOP - Sum of Products), dạng tích các tổng (POS - Product of Sums), minterm, maxterm, dạng chuẩn tắc (canonical form).
</div>

## Định nghĩa Hàm Boole

### Hàm Boole $$n$$ biến

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **hàm Boole** $$n$$ biến là một ánh xạ:
</div>

## Dạng Tổng các Tích Chuẩn (Canonical SOP)

### Minterm

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **minterm** (tích chuẩn) của $$n$$ biến là tích (AND) của $$n$$ biến, trong đó mỗi biến xuất hiện đúng một lần, ở dạng nguyên hoặc dạng bù.
</div>

Với hai biến $$x, y$$:

| $$x$$ | $$y$$ | Minterm | Ký hiệu |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x'y'$$ | $$m_0$$ |
| 0 | 1 | $$x'y$$ | $$m_1$$ |
| 1 | 0 | $$xy'$$ | $$m_2$$ |
| 1 | 1 | $$xy$$ | $$m_3$$ |

**Quy tắc**: Biến được gán 0 thì lấy dạng bù, biến được gán 1 thì lấy dạng nguyên.

### Xây dựng dạng SOP từ bảng chân trị

Để viết hàm Boole dưới dạng tổng các tích chuẩn:

1. Xác định các hàng có đầu ra $$F = 1$$.
2. Với mỗi hàng đó, viết minterm tương ứng.
3. Lấy tổng (OR) tất cả các minterm đó.

<div class="textbook-example" markdown="1">
**Ví dụ**: Xét hàm $$F(x, y, z)$$ với bảng chân trị:

| $$x$$ | $$y$$ | $$z$$ | $$F$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

Các hàng $$F = 1$$ ở các tổ hợp: $$001, 010, 100, 111$$

<div class="textbook-equation" markdown="1">
$$F(x, y, z) = x'y'z + x'yz' + xy'z' + xyz$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Viết gọn: $$F(x, y, z) = m_1 + m_2 + m_4 + m_7 = \sum m(1, 2, 4, 7)$$
</div>

<div class="content-box example-box textbook-block" markdown="1">
**Quy ước ký hiệu**:
- $$\sum m(1, 2, 4, 7)$$: dạng tổng các minterm
- $$m_1$$ ứng với tổ hợp nhị phân 001
- Đây là cách viết gọn của dạng SOP chuẩn tắc
</div>

## Dạng Tích các Tổng Chuẩn (Canonical POS)

### Maxterm

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **maxterm** (tổng chuẩn) của $$n$$ biến là tổng (OR) của $$n$$ biến, trong đó mỗi biến xuất hiện đúng một lần, ở dạng nguyên hoặc dạng bù.
</div>

Với hai biến $$x, y$$:

| $$x$$ | $$y$$ | Maxterm | Ký hiệu |
|:---:|:---:|:---|:---:|
| 0 | 0 | $$x + y$$ | $$M_0$$ |
| 0 | 1 | $$x + y'$$ | $$M_1$$ |
| 1 | 0 | $$x' + y$$ | $$M_2$$ |
| 1 | 1 | $$x' + y'$$ | $$M_3$$ |

**Quy tắc**: Biến được gán 1 thì lấy dạng bù, biến được gán 0 thì lấy dạng nguyên (ngược với minterm).

### Xây dựng dạng POS từ bảng chân trị

Để viết hàm Boole dưới dạng tích các tổng chuẩn:

1. Xác định các hàng có đầu ra $$F = 0$$.
2. Với mỗi hàng đó, viết maxterm tương ứng.
3. Lấy tích (AND) tất cả các maxterm đó.

Với cùng hàm $$F$$ ở ví dụ trên, các hàng $$F = 0$$ ở: $$000, 011, 101, 110$$

<div class="textbook-equation" markdown="1">
$$F(x, y, z) = (x + y + z)(x + y' + z')(x' + y + z')(x' + y' + z)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Viết gọn: $$F(x, y, z) = M_0 \cdot M_3 \cdot M_5 \cdot M_6 = \prod M(0, 3, 5, 6)$$

<div class="content-box insight-box textbook-block" markdown="1">
**Mối liên hệ SOP và POS**: Hai dạng này bổ sung cho nhau:
- SOP: tổng các minterm nơi $$F = 1$$
- POS: tích các maxterm nơi $$F = 0$$
- Chúng liên hệ qua luật De Morgan: một dạng là phủ định của dạng kia

Nếu đã có dạng SOP, hãy lấy các hàng còn lại (nơi $$F = 0$$), viết maxterm, thì thu được dạng POS ngay lập tức.
</div>

## Chuyển đổi giữa SOP và POS

### Phương pháp 1: Dùng bảng chân trị

Cho dạng SOP $$F = \sum m(1, 2, 4, 7)$$, suy ra dạng POS:
- Các tổ hợp còn lại là $$\{0, 3, 5, 6\}$$
- $$F = \prod M(0, 3, 5, 6)$$

### Phương pháp 2: Dùng De Morgan

Cho $$F = x'y'z + x'yz' + xy'z' + xyz$$:

<div class="textbook-equation" markdown="1">
$$F' = x'y'z' + x'yz + xy'z + xyz'$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Áp dụng De Morgan: $$F = (F')' = (x'y'z' + x'yz + xy'z + xyz')'$$

<div class="textbook-equation" markdown="1">
$$F = (x + y + z)(x + y' + z')(x' + y + z')(x' + y' + z)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
## Các Hàm Boole Cơ bản với 2 Biến

Có 16 hàm Boole 2 biến. Dưới đây là các hàm quan trọng:

| Tên hàm | Biểu thức | Ký hiệu | Ý nghĩa |
|:---|:---|:---:|:---|
| Hằng 0 | $$F = 0$$ | 0 | Luôn sai |
| AND | $$F = xy$$ | $$x \wedge y$$ | Cả hai đúng |
| OR | $$F = x + y$$ | $$x \vee y$$ | Ít nhất một đúng |
| XOR | $$F = x'y + xy'$$ | $$x \oplus y$$ | Khác nhau |
| NAND | $$F = (xy)'$$ | $$x \uparrow y$$| Phủ định AND |
| NOR | $$F = (x + y)'$$ | $$x \downarrow y$$ | Phủ định OR |
| XNOR | $$F = xy + x'y'$$ | $$x \odot y$$ | Giống nhau |
| Hằng 1 | $$F = 1$$ | 1 | Luôn đúng |
| Bù x | $$F = x'$$ | $$\overline{x}$$ | Phủ định x |
| Bù y | $$F = y'$$ | $$\overline{y}$$ | Phủ định y |

<div class="content-box info-box textbook-block" markdown="1">
**Tính đầy đủ của các cổng**: Bất kỳ hàm Boole nào cũng có thể được biểu diễn chỉ bằng ba cổng AND, OR, NOT (từ dạng SOP hoặc POS). Hơn nữa, chỉ riêng cổng NAND (hoặc NOR) cũng đủ để biểu diễn mọi hàm Boole.
</div>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Cần chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Các dạng chuẩn SOP và POS là nền tảng của **thiết kế mạch số** (digital circuit design). Mọi chip máy tính đều được tổng hợp từ các biểu thức Boole. Phần mềm CAD (Computer-Aided Design) tự động chuyển đổi bảng chân trị thành mạch logic, và các kỹ thuật tối thiểu hóa (mà chúng ta sẽ học ở các bài sau) là trái tim của công cụ đó.

Một ứng dụng ít ngờ tới: các **cơ sở dữ liệu quan hệ** dùng đại số Boole để tối ưu hóa truy vấn. Khi người lập trình viết `SELECT * FROM employees WHERE (dept = 'IT' AND salary > 50000) OR (dept = 'HR' AND salary > 40000)`, trình tối ưu hóa truy vấn chuyển nó thành một biểu thức Boole, tìm dạng chuẩn tắc, và chọn kế hoạch thực thi nhanh nhất.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Xây dựng Hàm Boole từ Bảng Chân trị</h3>
<p>Nhập bảng chân trị cho hàm Boole và công cụ sẽ tự động sinh ra dạng SOP và POS chuẩn tắc. Quan sát cách minterm và maxterm được xây dựng. <strong>Gợi ý thực hành:</strong> Tạo hàm majority (đầu ra 1 khi có >= 2 biến đầu vào bằng 1) và xem cả hai dạng chuẩn.</p>
<div data-demo="boolean-expression-evaluator"></div>
</div>
<script src="{{ '/public/js/boolean-expression-evaluator.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1: Viết dạng SOP

Cho bảng chân trị:

| $$x$$ | $$y$$ | $$z$$ | $$F$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

a) Viết dạng SOP chuẩn tắc.
b) Viết dạng POS chuẩn tắc.

<details>
<summary>Đáp án</summary>

a) Các hàng $$F = 1$$: $$010, 011, 101, 111$$
   $$F = x'yz' + x'yz + xy'z + xyz$$
   $$F = \sum m(2, 3, 5, 7)$$

b) Các hàng $$F = 0$$: $$000, 001, 100, 110$$
   $$F = (x + y + z)(x + y + z')(x' + y + z)(x' + y' + z)$$
   $$F = \prod M(0, 1, 4, 6)$$

</details>

### Bài tập 2: Xây dựng hàm từ mô tả

Một phòng họp có 3 cảm biến $$A, B, C$$. Đèn tự động bật khi có ít nhất 2 trong 3 cảm biến kích hoạt.

a) Lập bảng chân trị.
b) Viết hàm Boole dạng SOP.
c) Đơn giản hóa biểu thức nếu có thể.

<details>
<summary>Đáp án</summary>

a) Bảng chân trị:

| $$A$$ | $$B$$ | $$C$$ | $$F$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

b) $$F = A'BC + AB'C + ABC' + ABC = \sum m(3, 5, 6, 7)$$

c) Dùng đại số:
<div class="textbook-equation" markdown="1">
$$F = A'BC + AB'C + ABC' + ABC$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$F = BC(A' + A) + AB'C + ABC'$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$F = BC + AB'C + ABC'$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$F = BC + AC(B' + B) + ABC'$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$F = BC + AC + ABC'$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$F = BC + AC + AB$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy $$F = AB + BC + AC$$

</details>

### Bài tập 3: Chuyển đổi SOP sang POS

Cho hàm $$F(x, y, z) = \sum m(0, 2, 5, 7)$$. Hãy viết dạng POS.

<details>
<summary>Đáp án</summary>

Các minterm có mặt: $$\{0, 2, 5, 7\}$$
Các minterm vắng mặt: $$\{1, 3, 4, 6\}$$

Dạng POS: $$F = \prod M(1, 3, 4, 6)$$

<div class="textbook-equation" markdown="1">
$$F = (x + y + z')(x + y' + z')(x' + y + z)(x' + y' + z)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 4: Tư duy

Có bao nhiêu hàm Boole 3 biến mà đầu ra luôn bằng 0 tại các tổ hợp có số bit 1 chẵn? (Gợi ý: các tổ hợp có số bit 1 chẵn là 000, 011, 101, 110)

<details>
<summary>Đáp án</summary>

Có 8 tổ hợp đầu vào. Trong đó, 4 tổ hợp có số bit 1 chẵn (000, 011, 101, 110) bị buộc phải bằng 0. Còn 4 tổ hợp có số bit 1 lẻ (001, 010, 100, 111) có thể tự do chọn 0 hoặc 1. Vậy có $$2^4 = 16$$ hàm thỏa mãn điều kiện.

Đây là ví dụ về việc đếm số hàm Boole với ràng buộc — một bài toán xuất hiện trong thiết kế mạch có điều kiện.
</details>

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Hàm Boole** $$F: \{0,1\}^n \to \{0,1\}$$. Có $$2^{2^n}$$ hàm Boole $$n$$ biến.
- **Dạng SOP chuẩn tắc**: tổng các minterm (tích chuẩn) tại các hàng $$F = 1$$.
- **Dạng POS chuẩn tắc**: tích các maxterm (tổng chuẩn) tại các hàng $$F = 0$$.
- **Minterm**: tích của $$n$$ biến (biến = 0 lấy bù, biến = 1 lấy nguyên).
- **Maxterm**: tổng của $$n$$ biến (biến = 1 lấy bù, biến = 0 lấy nguyên).
- Hai dạng SOP và POS liên hệ qua bảng chân trị hoặc luật De Morgan.

Trong bài tiếp theo, chúng ta sẽ học về mạng các cổng logic và cách tối thiểu hóa hàm Boole.
