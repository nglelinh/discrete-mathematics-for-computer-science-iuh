---
layout: post
title: "Phương pháp Quine-McCluskey"
categories: chapter13
date: 2021-01-01
order: 5
required: true
lang: en
---

# Phương pháp Quine-McCluskey

Khi số biến tăng lên, bản đồ Karnaugh bắt đầu mất lợi thế. Những gì còn trực quan với 3 hoặc 4 biến sẽ nhanh chóng trở nên rối. Lúc đó, ta cần một quy trình có hệ thống hơn để tối thiểu hóa hàm Boole.


Đại số Boole nối logic với phần cứng và tối ưu biểu thức, vì vậy phần này vừa có ý nghĩa toán học vừa rất gần với thiết kế mạch và điều kiện trong code.
**Phương pháp Quine, McCluskey** chính là phiên bản mang tính thuật toán của bài toán đó. Nó đặc biệt quan trọng vì có thể cơ giới hóa, rất phù hợp với tư duy lập trình và các công cụ thiết kế mạch tự động.

Thay vì dựa vào trực giác hình ảnh, phương pháp này làm việc bằng cách nhóm, rút gọn và chọn các implicant thiết yếu theo từng bước rõ ràng. Nó cho thấy một bài toán logic có thể được chuyển thành quy trình tính toán cụ thể như thế nào.

Trong bài này, chúng ta sẽ học quy trình Quine, McCluskey và hiểu khi nào nó phù hợp hơn các phương pháp trực quan như Karnaugh.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Mô tả** các bước của thuật toán Quine-McCluskey.
- **Áp dụng** thuật toán để tìm tất cả implicant nguyên tố.
- **Sử dụng** bảng phủ (covering table) để chọn implicant tối ưu.
- **Xử lý** các hàm với don't-care conditions.
- **So sánh** Quine-McCluskey với K-map về ưu nhược điểm.

**Từ khóa**: Quine-McCluskey, implicant nguyên tố (prime implicant), bảng phủ (covering table), Petrick's method, biểu thức tối tiểu.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter13/qm_algorithm_flowchart.svg" alt="Sơ đồ khối thuật toán Quine-McCluskey hai pha" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 13.5 — Hai pha của thuật toán Quine-McCluskey: tìm implicant nguyên tố và chọn implicant tối ưu.</figcaption>
</p>
</figure>

## Giới thiệu

### Khi nào dùng Quine-McCluskey?

- **K-map**: hiệu quả cho 2-4 biến, trực quan.
- **Quine-McCluskey**: hiệu quả cho 5+ biến, có thể lập trình.
- Cả hai đều cho kết quả tối tiểu giống nhau.

### Ý tưởng chính

Thuật toán gồm hai pha:

1. **Pha 1 - Tìm tất cả implicant nguyên tố**: Lặp đi lặp lại việc kết hợp các minterm khác nhau đúng 1 bit để tạo ra các tích lớn hơn.
2. **Pha 2 - Chọn implicant**: Dùng bảng phủ để chọn implicant nguyên tố phủ tất cả minterm ban đầu với chi phí tối thiểu.

## Pha 1: Tìm Implicant Nguyên tố

### Biểu diễn nhị phân

Mỗi minterm được biểu diễn bằng số nhị phân tương ứng với tổ hợp đầu vào.

Ví dụ: với 4 biến $$w, x, y, z$$:
- $$m_0 = w'x'y'z'$$ = 0000
- $$m_5 = w'xy'z$$ = 0101
- $$m_{15} = wxyz$$ = 1111

### Nhóm theo số bit 1

Các minterm được nhóm theo số lượng bit 1 trong biểu diễn nhị phân.

### Quy tắc kết hợp

Hai minterm có thể kết hợp nếu:
- Chúng khác nhau đúng 1 bit.
- Bit khác nhau được thay bằng dấu "-" (don't-care).
- Kết quả là tích đã đơn giản hóa.

Kết quả kết hợp tiếp tục được kết hợp với nhau cho đến khi không còn cặp nào kết hợp được.

<div class="content-box insight-box" markdown="1">
**Cơ sở toán học**: Hai minterm khác nhau đúng 1 bit tương ứng với hằng đẳng thức $$xy + xy' = x$$. Bit khác nhau bị loại bỏ, các bit còn lại giữ nguyên. Quá trình kết hợp nhiều lần chính là áp dụng liên tiếp luật này.
</div>

### Ví dụ 1: Tìm Implicant Nguyên tố

Cho hàm $$F(w, x, y, z) = \sum m(0, 1, 2, 5, 6, 7, 8, 9, 10, 14)$$.

**Bước 1: Nhóm minterm theo số bit 1**

| Nhóm | Minterm | Nhị phân |
|:---:|:---:|:---:|
| 0 bit 1 | 0 | 0000 |
| 1 bit 1 | 1, 2, 8 | 0001, 0010, 1000 |
| 2 bit 1 | 5, 6, 9, 10 | 0101, 0110, 1001, 1010 |
| 3 bit 1 | 7, 14 | 0111, 1110 |

**Bước 2: Kết hợp lần 1**

Kết hợp các minterm trong nhóm $$k$$ với nhóm $$k+1$$:

- 0 (0000) - 1 (0001) = 000- (0, 1)
- 0 (0000) - 2 (0010) = 00-0 (0, 2)
- 0 (0000) - 8 (1000) = -000 (0, 8)
- 1 (0001) - 5 (0101) = 0-01 (1, 5)
- 1 (0001) - 9 (1001) = -001 (1, 9)
- 2 (0010) - 6 (0110) = 0-10 (2, 6)
- 2 (0010) - 10 (1010) = -010 (2, 10)
- 5 (0101) - 7 (0111) = 01-1 (5, 7)
- 6 (0110) - 7 (0111) = 011- (6, 7)
- 6 (0110) - 14 (1110) = -110 (6, 14)
- 8 (1000) - 9 (1001) = 100- (8, 9)
- 8 (1000) - 10 (1010) = 10-0 (8, 10)

Đánh dấu các minterm đã được dùng (sẽ không là implicant nguyên tố).

**Bước 3: Kết hợp lần 2**

Kết hợp các tích 2 minterm với nhau:

| Tích | Nhị phân |
|:---:|:---:|
| (0, 1) | 000- |
| (0, 2) | 00-0 |
| (0, 8) | -000 |
| (1, 5) | 0-01 |
| (1, 9) | -001 |
| (2, 6) | 0-10 |
| (2, 10) | -010 |
| (5, 7) | 01-1 |
| (6, 7) | 011- |
| (6, 14) | -110 |
| (8, 9) | 100- |
| (8, 10) | 10-0 |

Kết hợp:
- (0, 1) và (8, 9): 000- và 100- khác 1 bit = -00- (0, 1, 8, 9)
- (0, 2) và (8, 10): 00-0 và 10-0 khác 1 bit = -0-0 (0, 2, 8, 10)
- (2, 6) và (10, 14): 0-10 và -110 khác 1 bit = --10 (2, 6, 10, 14)

**Bước 4: Lặp lại**

Kết hợp lần 3:
- (0, 1) và (8, 9) đã tạo (-00-)
- (0, 2) và (8, 10) đã tạo (-0-0)
- Các tích còn lại không kết hợp được nữa

**Các implicant nguyên tố** (tích không được đánh dấu):

| Implicant | Phủ các minterm | Biểu thức |
|:---|:---:|:---|
| $$P_1$$ = -00- | 0, 1, 8, 9 | $$x'z'$$ |
| $$P_2$$ = -0-0 | 0, 2, 8, 10 | $$x'y'$$ |
| $$P_3$$ = --10 | 2, 6, 10, 14 | $$yz'$$ |
| $$P_4$$ = 0-01 | 1, 5 | $$w'x'z$$ |
| $$P_5$$ = 01-1 | 5, 7 | $$w'xy$$ |
| $$P_6$$ = 011- | 6, 7 | $$w'xy$$ |

<div class="content-box insight-box" markdown="1">
**Lưu ý**: $$P_5$$ và $$P_6$$ đều phủ minterm 7 và có biểu thức khác nhau. Trong bước chọn implicant, chúng ta sẽ cần quyết định implicant nào thực sự cần thiết.
</div>

## Pha 2: Bảng phủ

### Xây dựng bảng phủ

| Minterm \ Implicant | 0 | 1 | 2 | 5 | 6 | 7 | 8 | 9 | 10 | 14 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $$P_1 = x'z'$$ | X | X | | | | | X | X | | |
| $$P_2 = x'y'$$ | X | | X | | | | X | | X | |
| $$P_3 = yz'$$ | | | X | | X | | | | X | X |
| $$P_4 = w'x'z$$ | | X | | X | | | | | | |
| $$P_5 = w'xy$$ | | | | X | | X | | | | |
| $$P_6 = w'xy'$$ | | | | | X | X | | | | |

### Xác định implicant cốt yếu

Một implicant là **cốt yếu** nếu nó là implicant duy nhất phủ một minterm nào đó.

Xét từng minterm:
- Minterm 0: được phủ bởi $$P_1, P_2$$ (không cốt yếu ngay)
- Minterm 1: được phủ bởi $$P_1, P_4$$
- Minterm 2: được phủ bởi $$P_2, P_3$$
- Minterm 5: được phủ bởi $$P_4, P_5$$
- Minterm 7: chỉ được phủ bởi $$P_5$$ và $$P_6$$
- Minterm 14: chỉ được phủ bởi $$P_3$$

Implicant cốt yếu:
- $$P_3$$ (duy nhất phủ minterm 14)
- $$P_5$$ hoặc $$P_6$$ — vì minterm 7 chỉ được phủ bởi hai implicant này

Sau khi chọn $$P_3$$ và $$P_5$$, các minterm còn lại cần phủ: 0, 1, 2, 8, 9, 10.

Chọn thêm $$P_1$$ (phủ 0, 1, 8, 9) và $$P_3$$ đã chọn ở trên phủ 2, 10. Còn minterm nào chưa phủ? 10 đã phủ bởi $$P_3$$.

Kết quả: $$F = P_1 + P_3 + P_5 = x'z' + yz' + w'xy$$

<div class="content-box example-box" markdown="1">
**Nhận xét**: Quá trình chọn implicant trên bảng phủ giống như chọn các hình ghép trong trò chơi domino. Mỗi implicant là một miếng ghép phủ một số minterm. Mục tiêu là phủ tất cả minterm với số miếng ghép ít nhất.
</div>

## Xử lý Don't-care

Khi có don't-care, ta coi chúng như minterm trong pha 1 (tìm implicant nguyên tố), nhưng không yêu cầu phủ chúng trong pha 2 (bảng phủ).

### Ví dụ 2: Tối thiểu hóa với Don't-care

Cho $$F(w, x, y, z) = \sum m(0, 2, 4, 6, 8) + d(10, 12, 14)$$.

**Pha 1**: Thêm các don't-care (10, 12, 14) vào danh sách minterm để tìm implicant.

- Nhóm 0: 0 (0000)
- Nhóm 1: 2 (0010), 4 (0100), 8 (1000)
- Nhóm 2: 6 (0110), 10 (1010), 12 (1100)
- Nhóm 3: 14 (1110)

Kết hợp lần 1 và lần 2, ta có các implicant:

| Implicant | 0 | 2 | 4 | 6 | 8 |
|:---|:---:|:---:|:---:|:---:|:---:|
| $$Q_1 = 0--0$$ | X | X | X | X | |
| $$Q_2 = -0-0$$ | X | X | | | X |
| $$Q_3 = --00$$ | X | | X | | X |
| $$Q_4 = --10$$ | | X | | X | |
| $$Q_5 = 1--0$$ | | | | | X |

**Pha 2**: Bảng phủ chỉ cho các minterm thực (không tính don't-care).

Implicant cốt yếu:
- Minterm 6 chỉ được phủ bởi $$Q_4$$. Chọn $$Q_4$$.
- Sau khi chọn $$Q_4$$, minterm 2 được phủ.
- Minterm 4 chỉ được phủ bởi $$Q_1$$ và $$Q_3$$.
- Chọn $$Q_1$$ (phủ 0, 2, 4, 6) và $$Q_5$$ (phủ 8).

Kết quả: $$F = Q_1 + Q_4 + Q_5$$

Trong đó:
- $$Q_1 = 0--0 = x'y'$$ 
- $$Q_4 = --10 = yz'$$
- $$Q_5 = 1--0 = wx'$$

Vậy: $$F = x'y' + yz' + wx'$$

## So sánh K-map và Quine-McCluskey

| Tiêu chí | Bản đồ Karnaugh | Quine-McCluskey |
|:---|:---|:---|
| Số biến tối đa | 4-6 (khó cho 5+) | Không giới hạn về lý thuyết |
| Tính trực quan | Cao | Thấp |
| Dễ lập trình | Thấp | Cao |
| Độ chính xác | Phụ thuộc người dùng | Thuật toán đảm bảo |
| Tốc độ | Nhanh (với ít biến) | Chậm với nhiều biến |
| Don't-care | Dễ xử lý | Phức tạp hơn |

<div class="content-box insight-box" markdown="1">
**Cải tiến của Quine-McCluskey**: Với hàm nhiều biến (trên 6), thuật toán Quine-McCluskey cơ bản có thể chậm do số implicant tăng theo cấp số nhân. Các cải tiến như **Espresso** (dùng trong CAD) sử dụng heuristic để xử lý hiệu quả các mạch với hàng trăm biến. Hầu hết các công cụ tổng hợp logic thương mại đều dùng các biến thể của Espresso.
</div>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Thuật toán Quine-McCluskey và các biến thể của nó là nền tảng của:

- **Tổng hợp logic (logic synthesis)**: Các công cụ như Synopsys, Cadence, Yosys dùng các thuật toán tối thiểu hóa để thiết kế chip.
- **Thiết kế FPGA**: Khi bạn viết Verilog hoặc VHDL, công cụ tổng hợp tự động tối thiểu hóa các hàm Boole trước khi ánh xạ lên chip.
- **Hệ thống nhúng**: Tối ưu hóa mạch điều khiển trong thiết bị IoT, ô tô, máy bay.
- **Khai thác dữ liệu**: Các thuật toán tìm luật kết hợp (association rule mining) có nguyên lý tương tự Quine-McCluskey — tìm các tổ hợp tối thiểu phủ dữ liệu.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Mô phỏng Quine-McCluskey</h3>
<p>Công cụ này thực hiện từng bước của thuật toán Quine-McCluskey trên hàm bạn nhập. Quan sát cách các minterm được nhóm, kết hợp, và cuối cùng chọn implicant tối ưu. <strong>Hãy thử:</strong> So sánh kết quả của Quine-McCluskey trên một hàm 4 biến với kết quả từ K-map ở bài trước.</p>
<div data-demo="quine-mccluskey-simplifier"></div>
</div>
<script src="{{ '/public/js/quine-mccluskey-simplifier.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1: Quine-McCluskey cơ bản

Dùng phương pháp Quine-McCluskey để tối thiểu hóa:

$$F(a, b, c, d) = \sum m(0, 2, 3, 5, 7, 8, 10, 11, 13, 15)$$

<details>
<summary>Đáp án</summary>

Nhóm minterm:
- 0 bit 1: 0 (0000)
- 1 bit 1: 2 (0010), 8 (1000)
- 2 bit 1: 3 (0011), 5 (0101), 10 (1010)
- 3 bit 1: 7 (0111), 11 (1011), 13 (1101)
- 4 bit 1: 15 (1111)

Kết hợp lần 1 → các tích 2 minterm, kết hợp lần 2 được:

Implicant nguyên tố:
- $$P_1 = --11$$ (3, 7, 11, 15): $$cd$$
- $$P_2 = -1-1$$ (5, 7, 13, 15): $$bd$$
- $$P_3 = -0-0$$ (0, 2, 8, 10): $$b'd'$$
- $$P_4 = 00-0$$ (0, 2): $$a'b'd'$$
- $$P_5 = 10-0$$ (8, 10): $$ab'd'$$

Bảng phủ:
- Các minterm 3, 5, 7, 11, 13 được phủ bởi $$P_1$$ hoặc $$P_2$$
- Các minterm 0, 2, 8, 10 được phủ bởi $$P_3$$

Implicant cốt yếu: $$P_3$$ (phủ 0, 2, 8, 10) là duy nhất phủ các minterm này.

Chọn $$P_1$$ hoặc $$P_2$$. Cả hai đều tối ưu, chọn $$P_1 = cd$$.

Kết quả: $$F = cd + b'd'$$

</details>

### Bài tập 2: Quine-McCluskey với Don't-care

Tối thiểu hóa: $$F(a, b, c) = \sum m(1, 2, 5) + d(0, 7)$$

<details>
<summary>Đáp án</summary>

Nhóm (gồm cả don't-care):
- 0 bit 1: 0 (000)
- 1 bit 1: 1 (001), 2 (010)
- 2 bit 1: 5 (101)
- 3 bit 1: 7 (111)

Kết hợp:
- (0, 1) = 00-
- (0, 2) = 0-0
- (1, 5) = -01
- (5, 7) = 1-1

Kết hợp lần 2: không có cặp nào khác đúng 1 bit.

Implicant nguyên tố:
- $$P_1$$ = 00- (phủ 0, 1) tức $$a'b'$$
- $$P_2$$ = 0-0 (phủ 0, 2) tức $$a'c'$$
- $$P_3$$ = -01 (phủ 1, 5) tức $$b'c$$
- $$P_4$$ = 1-1 (phủ 5, 7) tức $$ac$$

Bảng phủ (chỉ cho minterm thực: 1, 2, 5):

| Implicant | 1 | 2 | 5 |
|:---|:---:|:---:|:---:|
| $$P_1 = a'b'$$ | X | | |
| $$P_2 = a'c'$$ | | X | |
| $$P_3 = b'c$$ | X | | X |
| $$P_4 = ac$$ | | | X |

Implicant cốt yếu:
- Minterm 2: chỉ phủ bởi $$P_2$$. Chọn $$P_2 = a'c'$$.
- Minterm 5: phủ bởi $$P_3, P_4$$.
- Minterm 1: phủ bởi $$P_1, P_3$$.

Sau khi chọn $$P_2$$, còn cần phủ 1 và 5. Chọn $$P_3 = b'c$$ phủ cả 1 và 5.

Kết quả: $$F = a'c' + b'c$$

</details>

### Bài tập 3: So sánh K-map và Quine-McCluskey

Cho hàm $$F(x, y, z) = \sum m(0, 1, 4, 5, 6)$$.

a) Tối thiểu hóa bằng K-map.
b) Tối thiểu hóa bằng Quine-McCluskey.
c) So sánh kết quả.

<details>
<summary>Đáp án</summary>

a) K-map:

| $$xy$$ \ $$z$$ | $$0$$ | $$1$$ |
|:---:|:---:|:---:|
| $$00$$ | 1 | 1 |
| $$01$$ | 0 | 0 |
| $$11$$ | 1 | 0 |
| $$10$$ | 1 | 1 |

Nhóm 1: hàng $$xy = 00$$ và $$xy = 10$$, cột $$z = 0, 1$$: $$y'$$
Nhóm 2: ô (11, 0) và (10, 0) hoặc nhóm cột $$z = 0$$: $$z'$$

Kết quả: $$F = y' + xz'$$

b) Quine-McCluskey:

Nhóm:
- 0 bit 1: 0 (000)
- 1 bit 1: 1 (001), 4 (100)
- 2 bit 1: 5 (101), 6 (110)

Kết hợp lần 1:
- (0, 1) = 00-
- (0, 4) = -00
- (1, 5) = -01
- (4, 5) = 10-
- (4, 6) = 1-0

Kết hợp lần 2:
- (0, 1) và (4, 5): -0- (phủ 0, 1, 4, 5)

Implicant nguyên tố:
- $$P_1 = -0-$$ (phủ 0, 1, 4, 5): $$y'$$
- $$P_2 = 1-0$$ (phủ 4, 6): $$xz'$$

Bảng phủ:
- Minterm 6: chỉ phủ bởi $$P_2$$. Cốt yếu.
- $$P_1$$ phủ 0, 1, 4, 5.

Kết quả: $$F = y' + xz'$$

c) Hai phương pháp cho kết quả giống hệt nhau. K-map nhanh hơn cho 3 biến, nhưng Quine-McCluskey dễ lập trình hóa.

</details>

## Tóm tắt

- **Quine-McCluskey**: thuật toán có hệ thống cho tối thiểu hóa hàm Boole.
- **Pha 1**: kết hợp các minterm để tìm implicant nguyên tố.
  - Nhóm minterm theo số bit 1.
  - Kết hợp các cặp khác nhau đúng 1 bit.
  - Lặp đến khi không kết hợp được nữa.
- **Pha 2**: dùng bảng phủ để chọn implicant.
  - Xác định implicant cốt yếu.
  - Chọn implicant bổ sung để phủ các minterm còn lại.
- **Don't-care**: dùng trong pha 1, bỏ qua trong pha 2.
- **So sánh**: K-map trực quan; Quine-McCluskey có hệ thống và lập trình được.
- **Công cụ thực tế**: Espresso và các biến thể được dùng trong thiết kế chip.

Bài này kết thúc chương về Đại số Boole. Chương tiếp theo sẽ chuyển sang một chủ đề mới: thuật toán và độ phức tạp.

## Tài liệu Tham khảo

1. W.V. Quine, "A Way to Simplify Truth Functions," *The American Mathematical Monthly*, 1955.
2. E.J. McCluskey, "Minimization of Boolean Functions," *Bell System Technical Journal*, 1956.
3. Robert K. Brayton et al., *Logic Minimization Algorithms for VLSI Synthesis*, Kluwer, 1984 — về thuật toán Espresso.
