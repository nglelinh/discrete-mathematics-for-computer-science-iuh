---
layout: post
title: "Mạng các Cổng Logic và Tối thiểu hóa Hàm Boole"
categories: chapter13
date: 2021-01-01
order: 3
required: true
lang: en
---

# Mạng các Cổng Logic và Tối thiểu hóa Hàm Boole

Một biểu thức logic không chỉ nằm trên giấy. Trong mạch số, nó phải được hiện thực bằng các **cổng logic** thật, với chi phí phần cứng, độ trễ và độ phức tạp kết nối cụ thể.


Đại số Boole nối logic với phần cứng và tối ưu biểu thức, vì vậy phần này vừa có ý nghĩa toán học vừa rất gần với thiết kế mạch và điều kiện trong code.
Vì vậy, việc tối thiểu hóa hàm Boole không phải chuyện thẩm mỹ ký hiệu. Biểu thức gọn hơn có thể dẫn đến mạch ít cổng hơn, ít tầng hơn, dễ kiểm thử hơn và đôi khi tiết kiệm năng lượng hơn. Đây là điểm giao rất rõ giữa toán rời rạc và kiến trúc máy tính.

Khi đã nhìn biểu thức như một mạng cổng, nhiều câu hỏi trở nên rất thực tế: có thể thay thế cấu trúc này bằng cấu trúc gọn hơn không, hai mạch có tương đương không, đâu là điểm dư thừa?

Trong bài này, chúng ta sẽ nối logic đại số với mạch số, rồi học cách đơn giản hóa hàm Boole theo góc nhìn triển khai thực tế.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Nhận biết** các cổng logic cơ bản: AND, OR, NOT, NAND, NOR, XOR.
- **Vẽ** sơ đồ mạch logic từ biểu thức Boole và ngược lại.
- **Áp dụng** các phương pháp đại số để tối thiểu hóa hàm Boole.
- **Tính toán** độ phức tạp của mạch (số cổng, số tầng).
- **Xây dựng** mạch tổ hợp từ bảng chân trị.

**Từ khóa**: Cổng logic (logic gate), mạch tổ hợp (combinational circuit), tối thiểu hóa (minimization), đa thức tối tiểu (minimal polynomial), độ phức tạp mạch (circuit complexity).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter13/logic_gates_symbols.svg" alt="Ký hiệu chuẩn của các cổng logic AND, OR, NOT, NAND, NOR, XOR" width="80%" height="80%">
  <figcaption style="text-align: center;">Hình 13.3 — Ký hiệu IEEE chuẩn cho sáu cổng logic cơ bản.</figcaption>
</p>
</figure>

## Các Cổng Logic Cơ bản

### Cổng AND

Đầu ra là 1 khi và chỉ khi **tất cả** đầu vào bằng 1.

| Đầu vào | Đầu ra |
|:---:|:---:|
| 0, 0 | 0 |
| 0, 1 | 0 |
| 1, 0 | 0 |
| 1, 1 | 1 |

<div class="content-box example-box" markdown="1">
**Ký hiệu mạch**: Cổng AND có dạng hình chữ D với hai đầu vào và một đầu ra. Biểu thức: $$F = A \cdot B$$. Với 3 đầu vào: $$F = A \cdot B \cdot C$$.
</div>

### Cổng OR

Đầu ra là 1 khi **ít nhất một** đầu vào bằng 1.

| Đầu vào | Đầu ra |
|:---:|:---:|
| 0, 0 | 0 |
| 0, 1 | 1 |
| 1, 0 | 1 |
| 1, 1 | 1 |

### Cổng NOT (Inverter)

Đầu ra là phủ định của đầu vào.

| Đầu vào | Đầu ra |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

### Cổng NAND

Kết hợp AND và NOT: $$F = (A \cdot B)'$$.

| $$A$$ | $$B$$ | $$A \cdot B$$ | $$(A \cdot B)'$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

### Cổng NOR

Kết hợp OR và NOT: $$F = (A + B)'$$.

| $$A$$ | $$B$$ | $$A + B$$ | $$(A + B)'$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 |

### Cổng XOR (Exclusive OR)

Đầu ra là 1 khi hai đầu vào **khác nhau**.

| $$A$$ | $$B$$ | $$A \oplus B$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<div class="content-box insight-box" markdown="1">
**Cổng phổ dụng**: Cổng NAND và NOR được gọi là **cổng phổ dụng** vì chỉ riêng chúng cũng đủ để xây dựng mọi hàm Boole. Trong thực tế, chip NAND thường rẻ hơn và nhanh hơn chip AND. Bạn có biết? Toàn bộ CPU trong điện thoại của bạn có thể được xây dựng chỉ từ cổng NAND!
</div>

## Từ Biểu thức đến Sơ đồ Mạch

### Ví dụ 1: Mạch so sánh 2 bit

Xây dựng mạch cho hàm $$F = A'B + AB'$$ (XOR):

1. Biểu thức có hai số hạng: $$A'B$$ và $$AB'$$
2. Mỗi số hạng cần: NOT, AND
3. Hai số hạng kết hợp bằng OR

Sơ đồ mạch:
- Đầu vào $$A$$ và $$B$$
- $$A$$ qua NOT được $$A'$$, kết hợp AND với $$B$$ được $$A'B$$
- $$B$$ qua NOT được $$B'$$, kết hợp AND với $$A$$ được $$AB'$$
- $$A'B$$ và $$AB'$$ qua OR được đầu ra

### Ví dụ 2: Mạch đa số (Majority Circuit)

Xây dựng mạch cho hàm đa số 3 biến: $$F = AB + AC + BC$$

Sơ đồ mạch:
- Ba cổng AND 2 đầu vào: $$AB$$, $$AC$$, $$BC$$
- Một cổng OR 3 đầu vào kết hợp các tích

### Ví dụ 3: Mạch từ dạng SOP

Cho $$F(x, y, z) = x'y'z + x'yz' + xy'z' + xyz$$

Sơ đồ mạch dạng hai tầng (two-level circuit):
- **Tầng 1**: các cổng AND thực hiện các tích chuẩn
- **Tầng 2**: một cổng OR kết hợp các tích

<div class="content-box info-box" markdown="1">
**Cấu trúc hai tầng**: Dạng SOP và POS đều có thể thực thi bằng mạch hai tầng (AND-OR hoặc OR-AND). Đây là cấu trúc phổ biến vì độ trễ thấp (chỉ hai tầng cổng) — tín hiệu chỉ đi qua đúng hai cổng từ đầu vào đến đầu ra.
</div>

### Sự Thật Thú vị về Độ Trễ

Trong thực tế, mỗi cổng logic mất vài pico-giây để chuyển trạng thái. Một mạch 2 tầng có độ trễ ~2 × 10 ps = 20 ps. Với CPU 4 GHz (mỗi chu kỳ = 250 ps), toàn bộ phép tính Boole chỉ mất chưa đầy 10% chu kỳ xung nhịp!

## Tối thiểu hóa Hàm Boole

### Tại sao cần tối thiểu hóa?

Một hàm Boole dạng SOP chuẩn tắc thường có nhiều số hạng hơn cần thiết. Tối thiểu hóa giúp:

1. **Giảm số cổng logic** trong mạch
2. **Giảm chi phí** sản xuất
3. **Giảm năng lượng** tiêu thụ
4. **Tăng tốc độ** xử lý (ít tầng cổng hơn)

### Kỹ thuật 1: Kết hợp các số hạng

Sử dụng hằng đẳng thức: $$xy + xy' = x$$

Ví dụ: $$F = xyz + xyz' = xy(z + z') = xy$$

### Kỹ thuật 2: Hấp thụ

Sử dụng: $$x + xy = x$$ và $$x + x'y = x + y$$

Ví dụ: $$F = AB + ABC = AB(1 + C) = AB$$

### Kỹ thuật 3: Thêm số hạng trung gian

Đôi khi cần thêm $$x + x'$$ vào một số hạng để kết hợp với số hạng khác:

$$F = AB' + A'B + AB$$

$$F = AB' + A'B + AB + AB$$ (thêm AB - luật lũy đẳng)

$$F = A(B' + B) + B(A' + A) = A + B$$

<div class="content-box example-box" markdown="1">
**Ví dụ tổng hợp**: Tối thiểu hóa $$F = x'y'z + x'yz + xy'z + xyz$$

$$
\begin{aligned}
F &= x'z(y' + y) + xz(y' + y) \\
  &= x'z + xz \\
  &= z(x' + x) \\
  &= z
\end{aligned}
$$

Kết quả: từ 4 số hạng xuống còn 1 biến duy nhất! Đây là một ví dụ ấn tượng cho thấy sức mạnh của tối thiểu hóa.
</div>

## Độ phức tạp của mạch

### Các thước đo

1. **Số cổng logic**: tổng số cổng trong mạch
2. **Độ sâu (depth)**: số tầng cổng lớn nhất từ đầu vào đến đầu ra
3. **Số đầu vào (fan-in)**: tổng số chân đầu vào

### Ví dụ so sánh

Xét hàm $$F = AB + AC + BC$$:

| Thước đo | Dạng SOP chuẩn tắc | Dạng tối thiểu |
|:---|---:|---:|
| Số cổng | 4 (3 AND + 1 OR) | 4 (3 AND + 1 OR) |
| Số đầu vào | 9 | 9 |

Trong trường hợp này, dạng SOP đã là tối thiểu.

Xét hàm $$F = x'y'z + x'yz + xy'z + xyz$$:

| Thước đo | Dạng SOP chuẩn tắc | Dạng tối thiểu ($$z$$) |
|:---|---:|---:|
| Số cổng | 5 (4 AND + 1 OR) | 0 (dây nối trực tiếp) |
| Số đầu vào | 13 | 0 |

## Mạch Tổ hợp (Combinational Circuits)

**Định nghĩa**: Mạch tổ hợp là mạch có đầu ra chỉ phụ thuộc vào đầu vào hiện tại (không có bộ nhớ).

### Ví dụ: Bộ cộng nửa (Half Adder)

Cộng hai bit $$A$$ và $$B$$, cho tổng $$S$$ và số nhớ $$C_{out}$$:

| $$A$$ | $$B$$ | $$S$$ | $$C_{out}$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Hàm Boole: $$S = A \oplus B$$, $$C_{out} = AB$$

Mạch: một cổng XOR và một cổng AND.

### Ví dụ: Bộ cộng đầy đủ (Full Adder)

Cộng hai bit $$A, B$$ và số nhớ đầu vào $$C_{in}$$, cho tổng $$S$$ và số nhớ đầu ra $$C_{out}$$:

| $$A$$ | $$B$$ | $$C_{in}$$ | $$S$$ | $$C_{out}$$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

$$S = A \oplus B \oplus C_{in}$$

$$C_{out} = AB + AC_{in} + BC_{in}$$

<div class="content-box insight-box" markdown="1">
**Ứng dụng**: Bộ cộng đầy đủ là khối xây dựng cơ bản của ALU (Arithmetic Logic Unit) trong mọi bộ vi xử lý. Một CPU 64-bit dùng 64 bộ cộng đầy đủ để thực hiện phép cộng. Khi bạn gõ `1 + 1` trong Python, hàng chục ngàn cổng logic đã làm việc để cho bạn kết quả `2`.
</div>

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Mô phỏng Cổng Logic</h3>
<p>Một mô phỏng trực quan cho phép bạn kéo-thả các cổng AND, OR, NOT, NAND, NOR, XOR để xây dựng mạch. Bật/tắt đầu vào để xem tín hiệu lan truyền qua các cổng như thế nào. <strong>Hãy thử:</strong> Xây dựng bộ cộng nửa (half adder) và kiểm tra với cả 4 tổ hợp đầu vào.</p>
<div data-demo="logic-gates-builder"></div>
</div>
<script src="{{ '/public/js/logic-gates-builder.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1: Từ biểu thức sang mạch

Vẽ sơ đồ mạch cho các hàm sau và tính số cổng:

a) $$F = A'B'C + A'BC + ABC$$

b) $$F = (A + B)(A + C)(B + C)$$

<details>
<summary>Đáp án</summary>

a) Biểu thức có 3 số hạng. Tối thiểu hóa:
$$F = A'C(B' + B) + ABC = A'C + ABC = C(A' + AB) = C(A' + B)$$
Số cổng sau tối thiểu: 3 (NOT, AND, OR). Số đầu vào: 5.

b) $$F = (A + B)(A + C)(B + C)$$
Đây là dạng POS. Có thể triển khai:
$$F = (A + BC)(B + C) = AB + AC + BC$$
Số cổng: 4 (3 AND + 1 OR). Số đầu vào: 9.

</details>

### Bài tập 2: Tối thiểu hóa

Tối thiểu hóa các hàm sau:

a) $$F = xyz + xyz' + xy'z + x'yz$$

b) $$F = ABCD + ABC'D + AB'CD + A'BCD$$

<details>
<summary>Đáp án</summary>

a) 
$$
\begin{aligned}
F &= xyz + xyz' + xy'z + x'yz \\
  &= xy(z + z') + z(xy' + x'y) \\
  &= xy + z(x \oplus y)
\end{aligned}
$$

b) 
$$
\begin{aligned}
F &= ABCD + ABC'D + AB'CD + A'BCD \\
  &= ABD(C + C') + BCD(A + A') \\
  &= ABD + BCD \\
  &= BD(A + C)
\end{aligned}
$$

</details>

### Bài tập 3: Thiết kế mạch

Thiết kế mạch phát hiện số lẻ cho 3 bit đầu vào $$A, B, C$$. Đầu ra $$F = 1$$ nếu số bit 1 trong đầu vào là lẻ (hàm parity lẻ).

<details>
<summary>Đáp án</summary>

Bảng chân trị:

| $$A$$ | $$B$$ | $$C$$ | $$F$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

$$F = A'B'C + A'BC' + AB'C' + ABC = A \oplus B \oplus C$$

Mạch: hai cổng XOR nối tiếp. Đây là mạch parity dùng trong phát hiện lỗi truyền dữ liệu. Hệ thống RAM máy tính dùng mạch parity để phát hiện lỗi bit.

</details>

### Bài tập 4: Tư duy thiết kế

Một bãi đỗ xe có 4 chỗ (A, B, C, D). Thiết kế mạch hiển thị số chỗ trống trên đèn LED 7 đoạn. Đầu vào mỗi chỗ là 1 nếu có xe. Mạch cần tính tổng số chỗ trống (4 - số xe). Mô tả cách bạn sẽ thiết kế mạch này.

<details>
<summary>Đáp án hướng dẫn</summary>

Bài toán này lớn hơn so với các ví dụ trên. Cách tiếp cận:
1. Xác định đầu ra: cần 3 bit để hiển thị số 0-4
2. Xây dựng bảng chân trị 4 biến đầu vào, 3 biến đầu ra
3. Tối thiểu hóa từng hàm đầu ra riêng biệt
4. Vẽ mạch tổng hợp

Đây là bài toán xuất hiện trong các kỳ thi thiết kế mạch số thực tế. Kỹ thuật tương tự được dùng trong máy tính tiền, máy bán hàng tự động, và hệ thống kiểm soát ra vào.
</details>

## Tóm tắt

- **Cổng logic cơ bản**: AND, OR, NOT, NAND, NOR, XOR.
- **Mạch hai tầng**: dạng SOP (AND-OR) và POS (OR-AND).
- **Tối thiểu hóa đại số**: dùng các hằng đẳng thức để rút gọn biểu thức.
- **Độ phức tạp**: đo bằng số cổng, độ sâu, số đầu vào.
- **Mạch tổ hợp**: đầu ra chỉ phụ thuộc đầu vào hiện tại.

Trong bài tiếp theo, chúng ta sẽ học phương pháp trực quan hơn: bản đồ Karnaugh.

## Tài liệu Tham khảo

1. M. Morris Mano, *Digital Design*, Pearson, chương 3.
2. Charles H. Roth Jr., *Fundamentals of Logic Design*, các chương 1-3 về mạch tổ hợp.
3. Tài liệu về họ chip 7400 — họ cổng logic TTL tiêu chuẩn, đã được sản xuất hàng tỷ đơn vị từ những năm 1960.
