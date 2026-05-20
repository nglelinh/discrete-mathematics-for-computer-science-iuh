---
layout: post
title: "Hàm Boole và Các Dạng Chuẩn"
categories: chapter13
date: 2021-01-01
order: 2
required: true
lang: en
---

# Hàm Boole và Các Dạng Chuẩn

Sau khi có các luật cơ bản của đại số Boole, câu hỏi tự nhiên tiếp theo là: làm sao biến chúng thành một “hàm” nhận đầu vào 0/1 và tạo ra đầu ra 0/1? Đây không còn là chuyện ký hiệu trên giấy nữa; đây là cách máy tính ra quyết định, cách mạch số phản ứng với tín hiệu, và cách một bảng chân trị được hiện thực hóa thành hành vi cụ thể.

**Hàm Boole** là mô hình của mọi khối quyết định nhị phân trong phần cứng và nhiều hệ thống logic trong phần mềm. Hiểu cách biểu diễn, đọc và biến đổi hàm Boole sẽ giúp ta chuẩn bị trực tiếp cho thiết kế mạch, tối thiểu hóa biểu thức và các kỹ thuật tối ưu hóa ở những bài sau.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Định nghĩa** hàm Boole với $$n$$ biến và biểu diễn bằng bảng chân trị.
- **Viết** hàm Boole dưới dạng tổng các tích chuẩn (SOP) và tích các tổng chuẩn (POS).
- **Chuyển đổi** giữa các dạng biểu diễn khác nhau của hàm Boole.
- **Xây dựng** biểu thức Boole từ bảng chân trị.
- **Tính toán** số lượng hàm Boole với $$n$$ biến.

**Từ khóa**: Hàm Boole (Boolean function), dạng tổng các tích (SOP - Sum of Products), dạng tích các tổng (POS - Product of Sums), minterm, maxterm, dạng chuẩn tắc (canonical form).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter13/boolean_function_mapping.svg" alt="Ánh xạ từ đầu vào nhị phân sang đầu ra trong hàm Boole n biến" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 13.2 — Hàm Boole $$F: \{0,1\}^n \to \{0,1\}$$ ánh xạ mỗi tổ hợp đầu vào thành một giá trị đầu ra.</figcaption>
</p>
</figure>

## Định nghĩa Hàm Boole

### Hàm Boole $$n$$ biến

**Định nghĩa**: Một **hàm Boole** $$n$$ biến là một ánh xạ:

$$F: \{0,1\}^n \to \{0,1\}$$

Mỗi tổ hợp giá trị đầu vào $$(x_1, x_2, \ldots, x_n)$$ cho một giá trị đầu ra duy nhất $$F(x_1, x_2, \ldots, x_n)$$.

<div class="content-box info-box" markdown="1">
**Số lượng hàm Boole $$n$$ biến**: Vì có $$2^n$$ tổ hợp đầu vào và mỗi tổ hợp cho 1 trong 2 giá trị đầu ra, tổng số hàm Boole $$n$$ biến là $$2^{2^n}$$.

Ví dụ:
- $$n = 1$$: có $$2^{2^1} = 4$$ hàm 1 biến
- $$n = 2$$: có $$2^{2^2} = 16$$ hàm 2 biến
- $$n = 3$$: có $$2^{2^3} = 256$$ hàm 3 biến
- $$n = 4$$: có $$2^{2^4} = 65536$$ hàm 4 biến

Con số này tăng cực kỳ nhanh. Với $$n = 6$$, đã có $$2^{64} \approx 1.8 \times 10^{19}$$ hàm — nhiều hơn số giọt nước trong tất cả các đại dương!
</div>

### Biểu diễn Hàm Boole

Hàm Boole có thể được biểu diễn bằng:

1. **Bảng chân trị**: liệt kê tất cả tổ hợp đầu vào và đầu ra tương ứng.
2. **Biểu thức đại số**: dùng các phép toán $$+$$, $$\cdot$$, $$'$$.
3. **Dạng chuẩn tắc**: SOP hoặc POS.

### Dạng chuẩn tắc SOP và POS

**Dạng tổng các tích chuẩn (DNF - Disjunctive Normal Form)**:
Mỗi số hạng là một **minterm** (tích của tất cả các biến hoặc phần bù của chúng). Hàm được viết thành tổng (OR) các minterm tương ứng với các tổ hợp đầu vào có $$F = 1$$.

**Dạng tích các tổng chuẩn (CNF - Conjunctive Normal Form)**:
Mỗi thừa số là một **maxterm** (tổng của tất cả các biến hoặc phần bù của chúng). Hàm được viết thành tích các maxterm tương ứng với các tổ hợp đầu vào có $$F = 0$$.

**Quy tắc xây dựng minterm và maxterm**:

| Đầu vào $$x_i$$ | Minterm | Maxterm |
|:---:|:---------|:---------|
| 1 | $$x_i$$ | $$x_i'$$ |
| 0 | $$x_i'$$ | $$x_i$$ |

**Ví dụ**: Với hàm 2 biến:

| $$x$$ | $$y$$ | $$F$$ | Minterm | Maxterm |
|:---:|:---:|:---:|:---------|:---------|
| 0 | 0 | 1 | $$x'y'$$ | - |
| 0 | 1 | 0 | - | $$x + y'$$ |
| 1 | 0 | 1 | $$xy'$$ | - |
| 1 | 1 | 0 | - | $$x' + y$$ |

Dạng DNF: $$F = x'y' + xy'$$
Dạng CNF: $$F = (x + y')(x' + y)$$

### Ví dụ: Hàm 2 biến

Xét hàm $$F(x, y) = x + y'$$:

| $$x$$ | $$y$$ | $$y'$$ | $$F = x + y'$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |

<div class="content-box insight-box" markdown="1">
**Sai lầm thường gặp**: Nhiều sinh viên viết minterm cho hàng $$x=0, y=0$$ là $$xy$$ thay vì $$x'y'$$. Hãy nhớ: minterm là *tích*, và để tích bằng 1, **biến 0 phải lấy bù**. 
</div>

## Dạng Tổng các Tích Chuẩn (Canonical SOP)

### Minterm

**Định nghĩa**: Một **minterm** (tích chuẩn) của $$n$$ biến là tích (AND) của $$n$$ biến, trong đó mỗi biến xuất hiện đúng một lần, ở dạng nguyên hoặc dạng bù.

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

$$F(x, y, z) = x'y'z + x'yz' + xy'z' + xyz$$

Viết gọn: $$F(x, y, z) = m_1 + m_2 + m_4 + m_7 = \sum m(1, 2, 4, 7)$$

<div class="content-box example-box" markdown="1">
**Quy ước ký hiệu**:
- $$\sum m(1, 2, 4, 7)$$: dạng tổng các minterm
- $$m_1$$ ứng với tổ hợp nhị phân 001
- Đây là cách viết gọn của dạng SOP chuẩn tắc
</div>

## Dạng Tích các Tổng Chuẩn (Canonical POS)

### Maxterm

**Định nghĩa**: Một **maxterm** (tổng chuẩn) của $$n$$ biến là tổng (OR) của $$n$$ biến, trong đó mỗi biến xuất hiện đúng một lần, ở dạng nguyên hoặc dạng bù.

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

$$F(x, y, z) = (x + y + z)(x + y' + z')(x' + y + z')(x' + y' + z)$$

Viết gọn: $$F(x, y, z) = M_0 \cdot M_3 \cdot M_5 \cdot M_6 = \prod M(0, 3, 5, 6)$$

<div class="content-box insight-box" markdown="1">
**Mối liên hệ SOP và POS**: Hai dạng này bổ sung cho nhau:
- SOP: tổng các minterm nơi $$F = 1$$
- POS: tích các maxterm nơi $$F = 0$$
- Chúng liên hệ qua luật De Morgan: một dạng là phủ định của dạng kia

Nếu bạn có dạng SOP, hãy lấy các hàng còn lại (nơi $$F = 0$$), viết maxterm, và bạn có POS ngay lập tức.
</div>

## Chuyển đổi giữa SOP và POS

### Phương pháp 1: Dùng bảng chân trị

Cho dạng SOP $$F = \sum m(1, 2, 4, 7)$$, suy ra dạng POS:
- Các tổ hợp còn lại là $$\{0, 3, 5, 6\}$$
- $$F = \prod M(0, 3, 5, 6)$$

### Phương pháp 2: Dùng De Morgan

Cho $$F = x'y'z + x'yz' + xy'z' + xyz$$:

$$F' = x'y'z' + x'yz + xy'z + xyz'$$

Áp dụng De Morgan: $$F = (F')' = (x'y'z' + x'yz + xy'z + xyz')'$$

$$F = (x + y + z)(x + y' + z')(x' + y + z')(x' + y' + z)$$

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

<div class="content-box info-box" markdown="1">
**Tính đầy đủ của các cổng**: Bất kỳ hàm Boole nào cũng có thể được biểu diễn chỉ bằng ba cổng AND, OR, NOT (từ dạng SOP hoặc POS). Hơn nữa, chỉ riêng cổng NAND (hoặc NOR) cũng đủ để biểu diễn mọi hàm Boole.
</div>

## Ứng dụng trong Khoa học Máy tính

Các dạng chuẩn SOP và POS là nền tảng của **thiết kế mạch số** (digital circuit design). Mọi chip máy tính đều được tổng hợp từ các biểu thức Boole. Phần mềm CAD (Computer-Aided Design) tự động chuyển đổi bảng chân trị thành mạch logic, và các kỹ thuật tối thiểu hóa (mà chúng ta sẽ học ở các bài sau) là trái tim của công cụ đó.

Một ứng dụng ít ngờ tới: các **cơ sở dữ liệu quan hệ** dùng đại số Boole để tối ưu hóa truy vấn. Khi bạn viết `SELECT * FROM employees WHERE (dept = 'IT' AND salary > 50000) OR (dept = 'HR' AND salary > 40000)`, trình tối ưu hóa truy vấn chuyển nó thành một biểu thức Boole, tìm dạng chuẩn tắc, và chọn kế hoạch thực thi nhanh nhất.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Xây dựng Hàm Boole từ Bảng Chân trị</h3>
<p>Nhập bảng chân trị cho hàm Boole và công cụ sẽ tự động sinh ra dạng SOP và POS chuẩn tắc. Quan sát cách minterm và maxterm được xây dựng. <strong>Hãy thử:</strong> Tạo hàm majority (đầu ra 1 khi có >= 2 biến đầu vào bằng 1) và xem cả hai dạng chuẩn.</p>
</div>

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
$$F = A'BC + AB'C + ABC' + ABC$$
$$F = BC(A' + A) + AB'C + ABC'$$
$$F = BC + AB'C + ABC'$$
$$F = BC + AC(B' + B) + ABC'$$
$$F = BC + AC + ABC'$$
$$F = BC + AC + AB$$

Vậy $$F = AB + BC + AC$$

</details>

### Bài tập 3: Chuyển đổi SOP sang POS

Cho hàm $$F(x, y, z) = \sum m(0, 2, 5, 7)$$. Hãy viết dạng POS.

<details>
<summary>Đáp án</summary>

Các minterm có mặt: $$\{0, 2, 5, 7\}$$
Các minterm vắng mặt: $$\{1, 3, 4, 6\}$$

Dạng POS: $$F = \prod M(1, 3, 4, 6)$$

$$F = (x + y + z')(x + y' + z')(x' + y + z)(x' + y' + z)$$

</details>

### Bài tập 4: Tư duy

Có bao nhiêu hàm Boole 3 biến mà đầu ra luôn bằng 0 tại các tổ hợp có số bit 1 chẵn? (Gợi ý: các tổ hợp có số bit 1 chẵn là 000, 011, 101, 110)

<details>
<summary>Đáp án</summary>

Có 8 tổ hợp đầu vào. Trong đó, 4 tổ hợp có số bit 1 chẵn (000, 011, 101, 110) bị buộc phải bằng 0. Còn 4 tổ hợp có số bit 1 lẻ (001, 010, 100, 111) có thể tự do chọn 0 hoặc 1. Vậy có $$2^4 = 16$$ hàm thỏa mãn điều kiện.

Đây là ví dụ về việc đếm số hàm Boole với ràng buộc — một bài toán xuất hiện trong thiết kế mạch có điều kiện.
</details>

## Tóm tắt

- **Hàm Boole** $$F: \{0,1\}^n \to \{0,1\}$$. Có $$2^{2^n}$$ hàm Boole $$n$$ biến.
- **Dạng SOP chuẩn tắc**: tổng các minterm (tích chuẩn) tại các hàng $$F = 1$$.
- **Dạng POS chuẩn tắc**: tích các maxterm (tổng chuẩn) tại các hàng $$F = 0$$.
- **Minterm**: tích của $$n$$ biến (biến = 0 lấy bù, biến = 1 lấy nguyên).
- **Maxterm**: tổng của $$n$$ biến (biến = 1 lấy bù, biến = 0 lấy nguyên).
- Hai dạng SOP và POS liên hệ qua bảng chân trị hoặc luật De Morgan.

Trong bài tiếp theo, chúng ta sẽ học về mạng các cổng logic và cách tối thiểu hóa hàm Boole.
