---
layout: post
title: "Đại số Boole"
categories: chapter13
date: 2021-01-01
order: 1
required: true
lang: en
---

Mỗi lần CPU đánh giá một điều kiện, mạch số mở hoặc đóng transistor, hay chương trình ghép các cờ trạng thái bằng `and`, `or`, `not`, ta đang đứng trên cùng một nền toán học: **đại số Boole**.

Đại số Boole nối logic với phần cứng và tối ưu biểu thức, vì vậy phần này vừa có ý nghĩa toán học vừa rất gần với thiết kế mạch và điều kiện trong code.
Nếu logic mệnh đề cho ta ngôn ngữ đúng và sai, thì đại số Boole cho ta cách thao tác có hệ thống trên các biểu thức đó như một dạng đại số thật sự. Đây là cây cầu nối rất đẹp giữa suy luận logic và thiết kế mạch số.

Chủ đề này quan trọng vì nó cho phép ta đơn giản hóa biểu thức, chứng minh hai mạch tương đương, và chuẩn bị nền cho việc tối thiểu hóa hàm Boole ở các bài sau. Trong hardware lẫn software, biểu thức gọn hơn thường đồng nghĩa với hệ thống rõ hơn và đôi khi nhanh hơn.

Trong bài này, chúng ta sẽ xây những quy tắc nền tảng của đại số Boole và nhìn chúng dưới cả hai góc độ, toán học và ứng dụng số.

![George Boole](https://commons.wikimedia.org/wiki/Special:FilePath/George_Boole.jpg?width=640)

*Hình 13.1: George Boole (1815–1864) — người đặt nền móng cho đại số logic dùng trong máy tính hiện đại.*

![Cấu trúc đại số Boole](https://commons.wikimedia.org/wiki/Special:FilePath/Boolean_algebra.svg?width=640)

*Hình 13.2: Đại số Boole trên $\{0,1\}$ với phép OR, AND và phần bù — nền tảng thiết kế mạch số.*

![Các cổng logic](https://commons.wikimedia.org/wiki/Special:FilePath/Logic_Gates.svg?width=640)

*Hình 13.3: Các cổng logic Boolean (NOT, AND, OR, XOR…) — hiện thân phần cứng của biểu thức Boole.*

![Cổng AND](https://commons.wikimedia.org/wiki/Special:FilePath/AND_ANSI_Labelled.svg?width=640)

*Hình 13.4: Cổng AND — chỉ cho kết quả 1 khi cả hai đầu vào đều 1, tương ứng phép nhân logic.*

![Cổng NOT](https://commons.wikimedia.org/wiki/Special:FilePath/NOT_ANSI_Labelled.svg?width=640)

*Hình 13.5: Cổng NOT — phủ định giá trị logic, tương ứng phần bù trong đại số Boole.*

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Phát biểu** định nghĩa đại số Boole và các tiên đề cơ bản.
- **Nhận biết** các hằng đẳng thức quan trọng và áp dụng chúng.
- **Chứng minh** các định lý đại số Boole bằng phương pháp đại số.
- **Giải thích** mối quan hệ giữa đại số Boole và logic mệnh đề.
- **Áp dụng** nguyên lý đối ngẫu (duality principle) để sinh ra các hằng đẳng thức mới.

**Từ khóa**: Đại số Boole (Boolean algebra), phần tử bù (complement), phép cộng logic (OR), phép nhân logic (AND), nguyên lý đối ngẫu (duality principle).

## Định nghĩa Đại số Boole

### Khái niệm Trực quan

Đại số Boole làm việc trên một tập hợp gồm **hai phần tử**: 0 (sai, false) và 1 (đúng, true), cùng với ba phép toán cơ bản:

- **Phép cộng logic (OR)**: ký hiệu $$+$$ hoặc $$\vee$$
  - $$0 + 0 = 0$$
  - $$0 + 1 = 1$$
  - $$1 + 0 = 1$$
  - $$1 + 1 = 1$$

- **Phép nhân logic (AND)**: ký hiệu $$\cdot$$ hoặc $$\wedge$$
  - $$0 \cdot 0 = 0$$
  - $$0 \cdot 1 = 0$$
  - $$1 \cdot 0 = 0$$
  - $$1 \cdot 1 = 1$$

- **Phép bù (NOT)**: ký hiệu $$x'$$ hoặc $$\overline{x}$$
  - $$0' = 1$$
  - $$1' = 0$$

<div class="content-box insight-box" markdown="1">
**Điểm khác biệt so với đại số thông thường**: Trong đại số Boole, $$1 + 1 = 1$$ (trong đại số thường, $$1 + 1 = 2$$). Đây là hệ quả của việc các phép toán làm việc trên giá trị logic, không phải số học. Sinh viên thường nhầm lẫn ở điểm này trong các bài kiểm tra đầu tiên.
</div>

### Định nghĩa Hình thức

**Định nghĩa**: Một **đại số Boole** là một bộ $$(B, +, \cdot, ', 0, 1)$$, trong đó:

- $$B$$ là một tập hợp chứa ít nhất hai phần tử
- $$+$$ và $$\cdot$$ là các phép toán hai ngôi trên $$B$$
- $$'$$ là phép toán một ngôi trên $$B$$
- $$0, 1 \in B$$ là các phần tử đặc biệt

thỏa mãn **6 tiên đề Huntington** sau đây:

### Sáu Tiên đề của Đại số Boole

**Tiên đề 1 - Tính đóng**: Với mọi $$x, y \in B$$:
- $$x + y \in B$$
- $$x \cdot y \in B$$

**Tiên đề 2 - Phần tử trung hòa**: Tồn tại các phần tử $$0, 1 \in B$$ sao cho:
- $$x + 0 = x$$ (0 là phần tử trung hòa của phép +)
- $$x \cdot 1 = x$$ (1 là phần tử trung hòa của phép $$\cdot$$)

**Tiên đề 3 - Tính giao hoán**:
- $$x + y = y + x$$
- $$x \cdot y = y \cdot x$$

**Tiên đề 4 - Tính phân phối**:
- $$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$$
- $$x + (y \cdot z) = (x + y) \cdot (x + z)$$

**Tiên đề 5 - Phần tử bù**: Với mỗi $$x \in B$$, tồn tại $$x' \in B$$ sao cho:
- $$x + x' = 1$$
- $$x \cdot x' = 0$$

**Tiên đề 6 - Tính không suy biến**: $$0 \neq 1$$

<div class="content-box warning-box" markdown="1">
**Chú ý**: Tiên đề 4 khác với đại số thông thường. Trong đại số Boole, phép $$+$$ cũng phân phối với phép $$\cdot$$, không chỉ chiều ngược lại. Đây là điểm mạnh của đại số Boole và cũng là nguồn gốc của nhiều sai lầm khi sinh viên mới làm quen.
</div>

## Các Hằng đẳng thức Cơ bản

Từ 6 tiên đề trên, ta có thể chứng minh nhiều hằng đẳng thức quan trọng:

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

<div class="content-box theorem-box" markdown="1">
**Định lý**: Mọi hằng đẳng thức trong đại số Boole đều có thể được chứng minh bằng hai cách:
1. **Phương pháp đại số**: biến đổi từ vế này sang vế kia dùng các tiên đề và định lý đã biết.
2. **Phương pháp bảng chân trị**: liệt kê tất cả $$2^n$$ tổ hợp giá trị và so sánh hai vế.
</div>

## Chứng minh Các Hằng đẳng thức

### Ví dụ 1: Chứng minh $$x + x = x$$

**Phương pháp đại số**:

$$
\begin{aligned}
x + x &= (x + x) \cdot 1 & \text{(tiên đề 2)} \\
     &= (x + x)(x + x') & \text{(tiên đề 5)} \\
     &= x + xx' & \text{(tiên đề 4 - phân phối)} \\
     &= x + 0 & \text{(tiên đề 5)} \\
     &= x & \text{(tiên đề 2)}
\end{aligned}
$$

### Ví dụ 2: Chứng minh $$x + xy = x$$ (Luật Hấp thụ)

$$
\begin{aligned}
x + xy &= x \cdot 1 + xy & \text{(tiên đề 2)} \\
       &= x(1 + y) & \text{(tiên đề 4)} \\
       &= x \cdot 1 & \text{(luật nuốt: } 1 + y = 1) \\
       &= x & \text{(tiên đề 2)}
\end{aligned}
$$

### Ví dụ 3: Chứng minh $$(x + y)' = x' \cdot y'$$ (De Morgan)

Dùng phương pháp bảng chân trị:

| $$x$$ | $$y$$ | $$x + y$$ | $$(x + y)'$$ | $$x'$$ | $$y'$$ | $$x' \cdot y'$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

Hai cột $$(x + y)'$$ và $$x' \cdot y'$$ giống nhau, vậy hằng đẳng thức đúng.

### Một Sai lầm Phổ biến

Sinh viên thường nhầm rằng $$(x + y)' = x' + y'$$. Hãy nhớ: luật De Morgan **đảo ngược** phép toán — phủ định của tổng là tích của các phủ định. Câu thần chú: "Đảo dấu, đảo biến."

## Nguyên lý Đối ngẫu (Duality Principle)

**Nguyên lý**: Mọi hằng đẳng thức trong đại số Boole vẫn đúng nếu ta thay:
- $$+$$ bằng $$\cdot$$ và $$\cdot$$ bằng $$+$$
- 0 bằng 1 và 1 bằng 0

Ví dụ, từ $$x + xy = x$$, đối ngẫu cho ta: $$x(x + y) = x$$.

<div class="content-box example-box" markdown="1">
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

Ngoài ba phép toán cơ bản AND, OR, NOT, trên $$B = \{0, 1\}$$ ta còn định nghĩa các phép toán hai ngôi khác:

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

<div class="content-box insight-box" markdown="1">
**Tính đầy đủ của NAND và NOR**: Chỉ riêng cổng NAND (hoặc NOR) cũng đủ để biểu diễn mọi hàm Boole. Đây là lý do trong thiết kế mạch số, người ta thường dùng cổng NAND làm cổng cơ sở — chip NAND rẻ hơn, nhanh hơn, và chiếm ít diện tích hơn chip AND.
</div>

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Trình xây dựng Bảng Chân trị</h3>
<p>Sinh viên có thể sử dụng công cụ trực quan dưới đây để tự động tạo bảng chân trị cho bất kỳ biểu thức Boole nào. Nhập biểu thức như <code>(A + B)'</code> hoặc <code>A.B + C</code> và xem kết quả ngay lập tức. <strong>Hãy thử:</strong> So sánh bảng chân trị của <code>A + B.C</code> và <code>(A+B).(A+C)</code> để kiểm chứng luật phân phối.</p>
<div data-demo="boolean-algebra-checker"></div>
</div>
<script src="{{ '/public/js/boolean-algebra-checker.js' | relative_url }}"></script>

## Đại số Boole và Logic Mệnh đề

Đại số Boole có mối liên hệ mật thiết với logic mệnh đề ở Chương 1:

| Logic Mệnh đề | Đại số Boole |
|:---|:---|
| Mệnh đề $$p$$ | Biến Boole $$x$$ |
| Đúng (T) | 1 |
| Sai (F) | 0 |
| Phép hội $$\wedge$$ | Phép nhân $$\cdot$$ |
| Phép tuyển $$\vee$$ | Phép cộng $$+$$ |
| Phủ định $$\neg$$ | Phần tử bù $$'$$ |
| Hằng đúng (Tautology) | Biểu thức bằng 1 |

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Đại số Boole là nền tảng của toàn bộ ngành khoa học máy tính hiện đại. Dưới đây là một số ứng dụng tiêu biểu:

- **Thiết kế vi xử lý**: Mọi lệnh trong CPU đều được thực thi bởi các mạch Boole. Một phép cộng hai số 64-bit đơn giản cần hàng nghìn cổng logic phối hợp.
- **Truy vấn cơ sở dữ liệu**: Các điều kiện WHERE trong SQL (AND, OR, NOT) là ứng dụng trực tiếp của đại số Boole.
- **Mạng nơ-ron nhân tạo**: Một perceptron (nơ-ron đơn giản nhất) thực chất là một hàm Boole với đầu vào và trọng số.
- **Xử lý ảnh và đồ họa**: Phép toán Boole trên bitmask dùng để che, lọc, và kết hợp hình ảnh.
- **Bảo mật và kiểm soát truy cập**: Các luật ACL (Access Control List) được đánh giá bằng biểu thức Boole.

<div class="content-box example-box" markdown="1">
**Ví dụ thực tế**: Khi bạn gõ "cat AND dog NOT fish" vào Google, công cụ tìm kiếm chuyển truy vấn này thành một biểu thức Boole trên hàng tỷ trang web để tìm kết quả phù hợp. Mỗi trang web là một "biến" với giá trị 1 (nếu chứa từ khóa) hoặc 0 (nếu không).
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

$$x(x' + y) = xx' + xy = 0 + xy = xy$$

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
$$
\begin{aligned}
x + x'y &= (x + x')(x + y) \\
        &= 1 \cdot (x + y) \\
        &= x + y
\end{aligned}
$$

b) 
$$
\begin{aligned}
xy + x'y' &= (xy + x')(xy + y') \\
          &= (x + x')(y + x')(x + y')(y + y') \\
          &= 1 \cdot (y + x') \cdot (x + y') \cdot 1 \\
          &= (x' + y)(x + y')
\end{aligned}
$$

</details>

### Bài tập 4: Tư duy phản biện

Có hai sinh viên tranh luận: "Mọi hàm Boole 2 biến đều có thể biểu diễn bằng chỉ OR và NOT." Người thứ nhất nói đúng, người thứ hai nói sai. Ai đúng? Giải thích.

<details>
<summary>Đáp án</summary>

Người thứ nhất đúng. Bộ {OR, NOT} là một tập đầy đủ vì AND có thể được biểu diễn qua OR và NOT: $$x \cdot y = (x' + y')'$$ (luật De Morgan). Tương tự, NAND, NOR và mọi hàm khác đều có thể xây dựng từ OR và NOT. Trong thiết kế mạch, điều này cho phép dùng chỉ một loại cổng để xây dựng toàn bộ hệ thống.
</details>

## Tóm tắt

- **Đại số Boole** làm việc trên hai giá trị $$\{0, 1\}$$ với ba phép toán: $$+$$ (OR), $$\cdot$$ (AND), $$'$$ (NOT).
- **6 tiên đề Huntington** định nghĩa đại số Boole: đóng, trung hòa, giao hoán, phân phối, phần tử bù, không suy biến.
- **Hằng đẳng thức**: lũy đẳng, nuốt, bù, De Morgan, hấp thụ — là công cụ biến đổi biểu thức.
- **Nguyên lý đối ngẫu**: mỗi hằng đẳng thức cho một hằng đẳng thức "đối xứng".
- **Tính đầy đủ**: NAND và NOR tự chúng đã đủ để biểu diễn mọi hàm Boole.
- **Ứng dụng**: từ thiết kế CPU và mạch số đến truy vấn cơ sở dữ liệu và mạng nơ-ron.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu về hàm Boole và hai dạng chuẩn tắc quan trọng — tổng các tích (SOP) và tích các tổng (POS).

## Tài liệu Tham khảo

1. George Boole, *An Investigation of the Laws of Thought*, 1854.
2. Claude E. Shannon, *A Symbolic Analysis of Relay and Switching Circuits*, MIT, 1937 — luận văn thạc sĩ đặt nền móng cho thiết kế mạch số.
3. M. Morris Mano, *Digital Design*, Pearson, các chương 1-2.
