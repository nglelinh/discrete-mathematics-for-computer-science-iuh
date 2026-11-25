---
layout: post
title: "Đại số Boole"
categories: chapter13
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Đại số logic trên {0,1}, hệ tiên đề Huntington, các hằng đẳng thức cơ bản, nguyên lý đối ngẫu, các phép toán dẫn xuất (XOR, NAND, NOR) và ví dụ đại số Boole như P(U) và B^n."
---

<div class="textbook-epigraph" markdown="1">

"Boolean algebra is the algebra of truth values — the mathematics of 0 and 1."

<span class="epigraph-attribution">— George Boole (paraphrased)</span>

</div>


Năm 1854, George Boole xuất bản cuốn *The Laws of Thought* với tham vọng biến suy luận logic thành phép tính đại số — khi ấy chưa ai nghĩ đến máy tính điện tử. Gần một thế kỷ sau (1937), chàng sinh viên 21 tuổi Claude Shannon nhận ra trong luận văn thạc sĩ của mình rằng toàn bộ hệ tiên đề khô khan của Boole lại mô tả **chính xác từng công tắc rơ-le đóng–mở** của mạch điện số. Từ đó, đại số Boole trở thành nền móng toán học trực tiếp của mọi bộ vi xử lý trên Trái Đất.

**Mạch bài học:** Đại số logic nhị phân $$B = \{0, 1\}$$ $$\longrightarrow$$ định nghĩa tiên đề của **Đại số Boole trừu tượng** $$\longrightarrow$$ bộ **hằng đẳng thức rút gọn** (hấp thụ, De Morgan, phân phối kép) $$\longrightarrow$$ **Nguyên lý Đối ngẫu (Duality Principle)** nhân đôi mọi định lý miễn phí và cầu nối sang mạch logic.

## Kiến thức cần nhớ: Đại số Boole trừu tượng khác gì đại số số thực thông thường?

- **Tính phân phối kép (Dual Distributivity):** Trong số thực, phép nhân phân phối qua phép cộng ($$a(b+c)=ab+ac$$) nhưng phép cộng **không** phân phối qua phép nhân. Trong đại số Boole, **cả hai chiều đều đúng**: $$x + (y \cdot z) = (x + y)(x + z)$$ — nguồn gốc của nhiều phép rút gọn mạch kỳ diệu!
- **Nguyên lý Đối ngẫu (Duality Principle):** Nếu một đẳng thức đúng trong mọi đại số Boole, thì khi ta hoán đổi đồng thời $$+ \leftrightarrow \cdot$$ và $$0 \leftrightarrow 1$$, đẳng thức mới thu được **tự động đúng mà không cần chứng minh lại**!
- **Đẳng cấu giữa ba thế giới (Logic – Tập hợp – Mạch số):** Đại số mệnh đề ($$\lor, \land, \neg, F, T$$), đại số tập hợp ($$\cup, \cap, \overline{\cdot}, \emptyset, U$$) và mạch cổng số ($$\text{OR}, \text{AND}, \text{NOT}, 0, 1$$) thực chất là **cùng một cấu trúc đại số Boole** khoác ba chiếc áo ký hiệu khác nhau.

Đại số Boole là nền tảng toán học của logic số, thiết kế mạch và tối ưu hóa biểu thức điều kiện. Mọi phép đánh giá điều kiện trong chương trình máy tính cũng như mọi mạch công tắc hay cổng logic đều vận hành trên cùng một cấu trúc đại số với hai giá trị $$0$$ và $$1$$. Bài học này trình bày đại số logic $$B=\{0,1\}$$, định nghĩa hình thức của đại số Boole, hệ tiên đề Huntington và các hằng đẳng thức cơ bản.

![George Boole](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="13.1">George Boole (1815–1864), người đặt nền móng đại số cho logic.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thao tác** trên đại số logic $$B=\{0,1\}$$ với các phép OR, AND, NOT và mười hằng đẳng thức cơ bản.
- **Phát biểu** định nghĩa đại số Boole và hệ tiên đề Huntington.
- **Nhận biết** các ví dụ đại số Boole quan trọng như $$P(U)$$ và $$B^n$$.
- **Chứng minh** và kiểm tra hằng đẳng thức bằng biến đổi đại số hoặc bảng chân trị.
- **Áp dụng** nguyên lý đối ngẫu và sử dụng các phép toán dẫn xuất (XOR, kéo theo, tương đương, NAND, NOR).
- **Giải thích** mối liên hệ giữa đại số Boole và logic mệnh đề (Chương 1).

**Từ khóa**: đại số logic $$B$$, đại số Boole, hằng đẳng thức, phần tử bù, đối ngẫu, XOR, NAND, NOR.
</div>

## Đại số logic $$B = \{0,1\}$$

Trước khi xét định nghĩa “đại số Boole” trừu tượng, ta làm quen với **đại số logic** trên tập hai giá trị $$B = \{0,1\}$$, đại diện cho **sai/đúng** hoặc **tắt/bật**.

### Ba phép toán cơ bản

| Phép toán | Ký hiệu thường dùng | Quy tắc |
|:---|:---|:---|
| **Tổng Boole** (OR) | $$x + y$$, $$x \lor y$$ | $$0+0=0$$; bằng **1** nếu có ít nhất một toán hạng bằng **1** |
| **Tích Boole** (AND) | $$xy$$, $$x \land y$$ | $$1\cdot1=1$$; bằng **0** nếu có ít nhất một toán hạng bằng **0** |
| **Bù** (NOT) | $$x'$$, $$\bar x$$, $$\lnot x$$ | $$\bar 0=1$$, $$\bar 1=0$$ |

Các biến nhận giá trị trong $$B$$ được gọi là **biến logic** hoặc **biến Boole**.

<div class="content-box insight-box textbook-block" markdown="1">
**Khác biệt với đại số số học**: Trong đại số Boole, $$1 + 1 = 1$$ (không phải 2), vì ký hiệu $$+$$ biểu thị phép **OR**, không phải phép cộng số nguyên.
</div>

### Mười hằng đẳng thức cơ bản trên $$B$$

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

Ở phần sau, chúng ta sẽ chứng minh một số hằng đẳng thức tiêu biểu từ các tiên đề.

## Định nghĩa đại số Boole (trừu tượng)

### Định nghĩa hình thức

<div class="textbook-definition" markdown="1">
**Định nghĩa.** Một **đại số Boole** là một bộ $$(A, +, \cdot, ', 0, 1)$$ (còn viết $$(A,\lor,\land,/,0,1)$$), trong đó $$A$$ là tập hợp có ít nhất hai phần tử, $$+$$ và $$\cdot$$ là hai phép toán hai ngôi, $$'$$ là phép toán một ngôi, $$0, 1 \in A$$, thỏa mãn các tiên đề dưới đây.
</div>

### Các tiên đề

**Tiên đề 1 — Tính đóng.** Với mọi $$x, y \in A$$: $$x + y \in A$$ và $$x \cdot y \in A$$.

**Tiên đề 2 — Phần tử trung hòa.** Tồn tại hai phần tử $$0, 1 \in A$$ sao cho với mọi $$x \in A$$:
- $$x + 0 = x$$ (0 là phần tử trung hòa của phép $$+$$)
- $$x \cdot 1 = x$$ (1 là phần tử trung hòa của phép $$\cdot$$)

**Tiên đề 3 — Giao hoán.** $$x + y = y + x$$ và $$x \cdot y = y \cdot x$$.

**Tiên đề 4 — Phân phối (cả hai chiều).**
- $$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$$
- $$x + (y \cdot z) = (x + y) \cdot (x + z)$$

**Tiên đề 5 — Phần tử bù.** Với mỗi $$x \in A$$, tồn tại $$x' \in A$$ sao cho $$x + x' = 1$$ và $$x \cdot x' = 0$$.

**Tiên đề 6 — Không suy biến.** $$0 \neq 1$$.

*(Một số tài liệu liệt kê thêm tính **kết hợp** như một tiên đề độc lập; trong hệ tiên đề Huntington, tính kết hợp có thể suy ra từ các tiên đề trên, nên ta vẫn sử dụng tính kết hợp bình thường khi biến đổi.)*

<div class="content-box warning-box textbook-block" markdown="1">
**Chú ý.** Khác với số học thông thường, Tiên đề 4 cho phép phép $$+$$ **cũng** phân phối qua phép $$\cdot$$. Đây là quy tắc rất hữu ích nhưng dễ gây nhầm lẫn khi mới chuyển từ đại số số học sang đại số Boole.
</div>

### Ví dụ quan trọng: họ tập con $$P(U)$$

<div class="textbook-example" markdown="1">

**Ví dụ (đại số Boole trên tập hợp).**  
Cho tập vũ trụ $$U$$ bất kỳ và đặt $$A = P(U)$$ (tập lũy thừa gồm mọi tập con của $$U$$). Định nghĩa các phép toán và hằng phần tử như sau:

| Phép toán trên $$A$$ | Ý nghĩa tập hợp |
|:---|:---|
| $$X \land Y$$ | $$X \cap Y$$ |
| $$X \lor Y$$ | $$X \cup Y$$ |
| $$X'$$ | $$U \setminus X$$ (phần bù trong $$U$$) |
| $$0$$ | $$\emptyset$$ |
| $$1$$ | $$U$$ |

Khi đó $$(P(U), \cap, \cup, {}^c, \emptyset, U)$$ là một **đại số Boole**.  
Trường hợp nhỏ nhất có ý nghĩa thực tế là khi $$U$$ gồm đúng một phần tử: $$P(U)$$ chỉ có hai phần tử và đẳng cấu với đại số logic $$B = \{0,1\}$$.

</div>

### Tích Descartes và $$B^n$$

Nếu $$A$$ và $$C$$ là hai đại số Boole thì tích Descartes $$A \times C$$ cũng là một đại số Boole với các phép toán xác định **theo từng thành phần**:

$$
(a_1,c_1) \land (a_2,c_2) = (a_1\land a_2,\, c_1\land c_2),
$$

tương tự cho phép $$\lor$$ và phép lấy bù $$(a,c)'=(a',c')$$; phần tử 0 là $$(0,0)$$ và phần tử 1 là $$(1,1)$$.

Đặc biệt, $$B^n = \{0,1\}^n$$ (tập các vector bit độ dài $$n$$) là một đại số Boole — đây chính là miền xác định của **hàm Boole $$n$$ biến** ở bài 13.2.

## Các hằng đẳng thức cơ bản

Từ 6 tiên đề trên, ta có thể suy ra nhiều hằng đẳng thức thường dùng:

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
**Định lý**: Mọi hằng đẳng thức trong đại số Boole đều có thể chứng minh bằng một trong hai cách:
1. **Phương pháp đại số**: biến đổi từ vế này sang vế kia nhờ các tiên đề và định lý đã biết.
2. **Phương pháp bảng chân trị**: liệt kê đầy đủ $$2^n$$ tổ hợp giá trị đầu vào và so sánh cột giá trị của hai vế.
</div>
</div>

## Chứng minh các hằng đẳng thức

<div class="textbook-example" markdown="1">
**Ví dụ 1**: Chứng minh $$x + x = x$$ bằng phương pháp đại số:

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
**Ví dụ 2**: Chứng minh $$x + xy = x$$ (Luật Hấp thụ):

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
**Ví dụ 3**: Chứng minh $$(x + y)' = x' \cdot y'$$ (Luật De Morgan) bằng bảng chân trị:

| $$x$$ | $$y$$ | $$x + y$$ | $$(x + y)'$$ | $$x'$$ | $$y'$$ | $$x' \cdot y'$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

Hai cột $$(x + y)'$$ và $$x' \cdot y'$$ hoàn toàn trùng khớp, nên hằng đẳng thức được chứng minh.
</div>

### Một sai lầm phổ biến

Sai lầm thường gặp là viết $$(x + y)' = x' + y'$$. Luật De Morgan **đảo cả phép toán lẫn biến**: phủ định của tổng là tích các phủ định, và phủ định của tích là tổng các phủ định. Quy tắc ghi nhớ ngắn gọn: “Đảo dấu, đảo biến.”

## Nguyên lý Đối ngẫu (Duality Principle)

**Nguyên lý**: Mọi hằng đẳng thức đúng trong đại số Boole vẫn giữ nguyên tính đúng đắn khi ta đồng thời hoán đổi:
- phép $$+$$ với phép $$\cdot$$;
- hằng $$0$$ với hằng $$1$$.

Chẳng hạn, từ luật hấp thụ $$x + xy = x$$, nguyên lý đối ngẫu cho ngay $$x(x + y) = x$$.

<div class="content-box example-box textbook-block" markdown="1">
**Bảng đối ngẫu các hằng đẳng thức:**

| Hằng đẳng thức gốc | Hằng đẳng thức đối ngẫu |
|:---|:---|
| $$x + 0 = x$$ | $$x \cdot 1 = x$$ |
| $$x + x' = 1$$ | $$x \cdot x' = 0$$ |
| $$x + xy = x$$ | $$x(x + y) = x$$ |
| $$(x + y)' = x'y'$$ | $$(xy)' = x' + y'$$ |

**Nhận xét**: Nguyên lý đối ngẫu phản ánh tính đối xứng trong hệ tiên đề đại số Boole. Khi chứng minh xong một đẳng thức, ta có ngay đẳng thức đối ngẫu tương ứng mà không cần chứng minh lại từ đầu.
</div>

## Các phép toán dẫn xuất trên đại số logic $$B$$

Ngoài ba phép toán cơ bản AND, OR, NOT, trên $$B = \{0, 1\}$$ còn có các phép toán hai ngôi quan trọng sau:

| Phép toán | Ký hiệu | Công thức | Ý nghĩa |
|:----------|:-------:|:-----------|:--------|
| XOR (tổng mod 2) | $$x \oplus y$$ | $$x'y + xy'$$ | Bằng 1 khi hai biến khác nhau |
| Kéo theo (Implication) | $$x \to y$$ | $$x' + y$$ | Bằng 1 trừ trường hợp $$x=1, y=0$$ |
| Tương đương (Equivalence) | $$x \leftrightarrow y$$ | $$xy + x'y'$$ | Bằng 1 khi hai biến bằng nhau |
| NOR (Vebb) | $$x \downarrow y$$ | $$(x + y)'$$ | Phủ định của OR |
| NAND (Sheffer) | $$x \mid y$$ | $$(xy)'$$ | Phủ định của AND |

**Bảng chân trị của các phép toán dẫn xuất**:

| $$x$$ | $$y$$ | $$x \oplus y$$ | $$x \to y$$ | $$x \leftrightarrow y$$ | $$x \downarrow y$$ | $$x \mid y$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 | 0 | 0 |

<div class="textbook-definition" markdown="1">

**Tính đầy đủ chức năng của NAND và NOR.** Chỉ riêng phép NAND (hoặc chỉ riêng phép NOR) đã đủ để biểu diễn mọi hàm Boole. Nhờ tính chất này, NAND thường được chọn làm cổng cơ sở trong thiết kế mạch số.

</div>

<div class="interactive-demo" markdown="1">
<div data-demo="boolean-algebra-checker"></div>
</div>
<script src="{{ '/public/js/boolean-algebra-checker.js' | relative_url }}"></script>

## Đại số Boole và logic mệnh đề

Đại số Boole tương ứng trực tiếp với logic mệnh đề ở Chương 1:

| Logic Mệnh đề | Đại số Boole |
|:---|:---|
| Mệnh đề $$p$$ | Biến Boole $$x$$ |
| Đúng (T) | 1 |
| Sai (F) | 0 |
| Phép hội $$\wedge$$ | Phép nhân $$\cdot$$ |
| Phép tuyển $$\vee$$ | Phép cộng $$+$$ |
| Phủ định $$\neg$$ | Phần tử bù $$'$$ |
| Hằng đúng (Tautology) | Biểu thức đồng nhất bằng 1 |

## Ứng dụng trong khoa học máy tính

Đại số Boole xuất hiện ở nhiều tầng của hệ thống máy tính:

- **Mạch số và CPU**: các bộ cộng, bộ so sánh và mạch điều khiển đều được xây dựng từ mạng cổng logic.
- **Truy vấn dữ liệu**: mệnh đề `WHERE` trong SQL kết hợp các điều kiện lọc bằng AND, OR, NOT.
- **Bitmask và xử lý bit**: các phép toán bit AND, OR, NOT dùng để bật, tắt và kiểm tra cờ trạng thái.
- **Kiểm soát truy cập**: chính sách ACL (*Access Control List*) đánh giá quyền hạn như các biểu thức logic trên thuộc tính của chủ thể và tài nguyên.

<div class="textbook-example" markdown="1">

**Ví dụ.** Truy vấn tìm kiếm dạng “cat AND dog NOT fish” là một biểu thức Boole trên tập tài liệu, trong đó mỗi tài liệu được gán giá trị **1** hoặc **0** tùy vào việc có chứa từng từ khóa hay không.

</div>

## Ví dụ tính tay làm từng bước: Rút gọn biểu thức Boole bằng đại số & kiểm tra bằng đối ngẫu

**Phần A — Rút gọn biểu thức mạch $$F(x, y, z) = x y + \bar{x} z + y z$$ (Định lý đồng thuận — Consensus Theorem):**
Ta muốn chứng minh số hạng thừa $$y z$$ có thể **xóa bỏ hoàn toàn** (tiết kiệm 1 cổng AND và 1 đầu vào OR trên chip!):
1. **Nhân thêm $$1 = x + \bar{x}$$ vào số hạng $$yz$$:**
   $$F = x y + \bar{x} z + (x + \bar{x}) y z = x y + \bar{x} z + x y z + \bar{x} y z.$$
2. **Gom nhóm theo $$xy$$ và $$\bar{x}z$$:**
   $$F = x y (1 + z) + \bar{x} z (1 + y).$$
3. **Dùng luật thống trị $$1 + z = 1$$ và $$1 + y = 1$$:**
   $$F = x y \cdot 1 + \bar{x} z \cdot 1 = x y + \bar{x} z.$$
- **Kiểm chứng nhanh tại $$x=1, y=1, z=1$$:** Gốc cho $$1 + 0 + 1 = 1$$; rút gọn cho $$1 + 0 = 1$$. Tại $$x=0, y=1, z=1$$: gốc cho $$0 + 1 + 1 = 1$$; rút gọn cho $$0 + 1 = 1$$. Chính xác!

**Phần B — Áp dụng Nguyên lý Đối ngẫu để nhận ngay định lý thứ hai miễn phí:**
Từ đẳng thức vừa chứng minh $$x y + \bar{x} z + y z = x y + \bar{x} z$$, hoán đổi toàn bộ $$+ \leftrightarrow \cdot$$:
$$(x + y)(\bar{x} + z)(y + z) = (x + y)(\bar{x} + z).$$
Không tốn thêm một dòng chứng minh nào, ta thu ngay thêm một luật rút gọn dạng tích các tổng (POS)!

### Giải thích: Bốn mẹo đại số để rút gọn biểu thức Boole nhanh và không sót
1. **Bước 1 — Đẩy dấu phủ định vào tận biến đơn bằng De Morgan trước tiên:** Biến $$\overline{x + y} = \bar{x}\bar{y}$$ và $$\overline{xy} = \bar{x} + \bar{y}$$ để giải phóng ngoặc lớn.
2. **Bước 2 — Tìm cặp bù $$A + \bar{A} = 1$$ và luật hấp thụ $$A + AB = A$$:** Mọi số hạng chứa thừa một nhân tử đã có mặt độc lập đều biến mất ngay lập tức.
3. **Bước 3 — Dùng "chiêu chèn $$1 = x + \bar{x}$$" khi thấy thiếu biến:** Như ví dụ Định lý đồng thuận ở trên, nhân thêm $$(x + \bar{x})$$ giúp tạo nhân tử chung để triệt tiêu số hạng dư.
4. **Bước 4 — Kiểm tra chéo trên vài bộ giá trị $$(0, 1)$$:** Với 3 biến chỉ có $$2^3 = 8$$ tổ hợp; thay nhanh 2–3 tổ hợp biên là đủ phát hiện ngay nếu lỡ sai dấu phủ định!

$$(\mathcal{B}, +, \cdot, \bar{\phantom{x}}, 0, 1) \;\xleftrightarrow{\text{Đối ngẫu}}\; (+ \leftrightarrow \cdot,\; 0 \leftrightarrow 1) \;\Longrightarrow\; \text{Logic} \cong \text{Tập hợp} \cong \text{Mạch số.}$$

## Bài tập

### Bài tập 1: Kiểm tra hằng đẳng thức

Kiểm tra các hằng đẳng thức sau bằng bảng chân trị hoặc biến đổi đại số:

a) $$x + yz = (x + y)(x + z)$$

b) $$x(x' + y) = xy$$

<details>
<summary>Đáp án</summary>

**a)** Lập bảng chân trị:

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

Hai cột $$x + yz$$ và $$(x+y)(x+z)$$ trùng nhau trên mọi dòng, nên hằng đẳng thức đúng.

**b)** Biến đổi đại số:

<div class="textbook-equation" markdown="1">
$$x(x' + y) = xx' + xy = 0 + xy = xy$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2: Áp dụng luật De Morgan

Đơn giản hóa các biểu thức sau bằng luật De Morgan:

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

Chứng minh các hằng đẳng thức sau bằng biến đổi đại số:

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

Hai sinh viên tranh luận về nhận định: “Mọi hàm Boole 2 biến đều có thể biểu diễn chỉ bằng OR và NOT.” Người thứ nhất cho rằng đúng, người thứ hai cho rằng sai. Ai đúng? Giải thích.

<details>
<summary>Đáp án</summary>

Người thứ nhất đúng. Tập phép toán {OR, NOT} là tập đầy đủ chức năng vì phép AND có thể biểu diễn qua OR và NOT theo luật De Morgan: $$x \cdot y = (x' + y')'$$. Từ đó, NAND, NOR và mọi hàm Boole khác đều xây dựng được chỉ từ OR và NOT.
</details>


### Bài tập 5: $$P(U)$$ và $$B^n$$

(a) Với $$U=\{a,b\}$$, liệt kê 4 phần tử của $$P(U)$$ và tính $$\{a\}\cup\{b\}$$, $$\{a\}\cap\{b\}$$, phần bù của $$\{a\}$$.  
(b) Vì sao $$B^2$$ có 4 phần tử? Phép OR từng bit của $$(1,0)$$ và $$(0,1)$$ cho kết quả nào?

<details>
<summary>Đáp án</summary>

(a) Các phần tử của $$P(U)$$ là $$\emptyset, \{a\}, \{b\}, \{a,b\}$$; hợp $$\{a\}\cup\{b\}=\{a,b\}$$; giao $$\{a\}\cap\{b\}=\emptyset$$; phần bù của $$\{a\}$$ là $$\{b\}$$.  
(b) Vì mỗi vị trí có 2 lựa chọn (0 hoặc 1) nên có $$2^2=4$$ vector bit; phép OR từng bit của $$(1,0)$$ và $$(0,1)$$ là $$(1,1)$$.

</details>

## Xem thêm

- [Boolean Algebra and Karnaugh Maps](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Neso Academy (Gate level + minimization)

## Tóm tắt

1. **Đại số logic** $$B=\{0,1\}$$ gồm các phép OR, AND, NOT cùng mười hằng đẳng thức cơ bản (lưu ý $$1+1=1$$).
2. **Đại số Boole** trừu tượng được xác định bởi hệ tiên đề Huntington, với các ví dụ tiêu biểu là $$P(U)$$ và $$B^n$$.
3. Hằng đẳng thức có thể chứng minh bằng **biến đổi đại số** hoặc **bảng chân trị**; **nguyên lý đối ngẫu** giúp suy ra ngay cặp đẳng thức tương ứng.
4. Các phép toán dẫn xuất gồm XOR, kéo theo, tương đương và hai phép đầy đủ chức năng là **NAND** và **NOR**.
5. Bài tiếp theo sẽ trình bày về hàm Boole, minterm và dạng nối rời chính tắc (SOP chuẩn).

## Tài liệu Tham khảo

1. George Boole, *An Investigation of the Laws of Thought*, 1854.
2. Claude E. Shannon, *A Symbolic Analysis of Relay and Switching Circuits*, MIT, 1937 — luận văn thạc sĩ đặt nền móng cho thiết kế mạch số.
3. M. Morris Mano, *Digital Design*, Pearson, các chương 1-2.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=WW-NPtIzHwk">Introduction to Boolean Algebra (Part 1)</a> — Neso Academy, tiếng Anh. Giới thiệu đại số Boole trên {0,1} và các hằng đẳng thức cơ bản.
- <a href="https://www.youtube.com/watch?v=OjWmVCG8PLA">Introduction to Boolean Algebra (Part 2)</a> — Neso Academy, tiếng Anh. Trình bày tiếp các luật đại số Boole và ví dụ chứng minh đẳng thức.
- <a href="https://www.youtube.com/watch?v=imPCCJDyCAs">Toán rời rạc 30. Giới thiệu về đại số Boole</a> — TITV, tiếng Việt. Bài giảng giới thiệu đại số Boole bằng tiếng Việt.
