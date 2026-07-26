---
layout: post
title: "Mạch Cộng, Mạch Nhân và Các Mạch Tổ hợp Cơ bản"
categories: chapter13
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Half/full adder, bộ cộng lan truyền mang n-bit, nhân không dấu bằng partial product, cùng MUX, decoder và comparator."
---

<div class="textbook-epigraph" markdown="1">

"An ALU is not magic — it is a carefully arranged forest of adders, multiplexers, and Boolean glue."

<span class="epigraph-attribution">— Digital design classroom wisdom</span>

</div>

Các mục trước đã xây dựng hàm Boolean, cổng logic và tối thiểu hóa. Mục này **ghép** các thành phần đó thành các khối số học và tổ hợp cơ bản:

1. **Bộ cộng** — half adder, full adder, bộ cộng $$n$$-bit.
2. **Bộ nhân** — partial product và cộng theo cột.
3. **MUX, decoder, comparator** — chọn nguồn, giải mã và so sánh.

Mọi khối tuân theo cùng lộ trình:

**bảng chân trị → biểu thức Boolean → sơ đồ cổng.**

Phép `a + b` hay `a * b` trong ngôn ngữ lập trình được hiện thực bằng **mạng cổng** trên bit **0**/**1**. Chuỗi half adder → full adder → bộ cộng $$n$$-bit → nhân nối biểu thức $$x \oplus y$$ với datapath nhiều bit.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây** half adder và full adder từ bảng chân trị và cổng (XOR, AND, OR).
- **Ghép** full adder thành bộ cộng $$n$$-bit kiểu lan truyền mang và ước lượng trễ mang.
- **Mô tả** nhân không dấu bằng partial products và cộng theo cột.
- **Viết** hàm Boole cho MUX 2-to-1, decoder 2-to-4 và comparator 1-bit.
- **Liên hệ** các khối này với ALU và lệnh số học.

**Từ khóa**: half adder, full adder, ripple-carry, partial product, MUX, decoder, comparator, mạch tổ hợp.

</div>

## 1. Mạch tổ hợp

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Mạch **tổ hợp** (combinational) có đầu ra tại thời điểm $$t$$ chỉ phụ thuộc **đầu vào tại $$t$$** (cùng độ trễ lan truyền qua cổng), **không** mang trạng thái nhớ bên trong. Mạch **tuần tự** (sequential) thêm flip-flop hay thanh ghi — chủ đề automata / FSM.

</div>

Các khối cộng, nhân, MUX, decoder và so sánh trong mục này đều là mạch tổ hợp: đầu ra chỉ phụ thuộc đầu vào hiện tại (sau độ trễ lan truyền qua cổng).

![Cổng XOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_XOR.svg)

<p class="textbook-figure-caption" data-figure="13.35a">Cổng XOR — bit tổng của half adder.</p>

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.35b">Cổng AND — bit nhớ của half adder.</p>

## 2. Half adder (bộ nửa cộng) — cộng hai bit, không có nhớ vào

### 2.1. Bảng chân trị

**Bộ nửa cộng** (half adder): cộng hai bit $$A, B \in \{0,1\}$$, **không** xét nhớ từ phép cộng cột trước.

$$
A + B = 2 \cdot C + S,
$$

trong đó $$S$$ là **bit tổng** (sum), $$C$$ là **bit nhớ** (carry).

| $$A$$ | $$B$$ | $$S$$ | $$C$$ | Ý nghĩa |
|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 0 | 0 | $$0 + 0 = 0$$ |
| 0 | 1 | 1 | 0 | $$0 + 1 = 1$$ |
| 1 | 0 | 1 | 0 | $$1 + 0 = 1$$ |
| 1 | 1 | 0 | 1 | $$1 + 1 = 2 = 10_2$$ |

(Hàng bảng có thể sắp theo thứ tự bất kỳ; quan trọng là bốn tổ hợp đủ.)

### 2.2. Biểu thức Boole

Đọc SOP (tổng các tích) từ bảng:

- Cột $$S$$ bằng **1** khi $$A$$ và $$B$$ **khác nhau** → **XOR**.
- Cột $$C$$ bằng **1** khi **cả hai** bằng **1** → **AND**.

<div class="textbook-equation" markdown="1">
$$
S = A \oplus B = \bar A B + A \bar B,\qquad
C = A \cdot B.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Half adder** = “nửa” bộ cộng: **không** có nhớ vào (Cin). Đủ để cộng 2 bit; **chưa** đủ để ghép thành bộ cộng $$n$$-bit (các cột giữa cần Cin).

![Half adder](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.36">Half adder: XOR cho sum, AND cho carry.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** $$A = 1$$, $$B = 1$$ → $$S = 0$$, $$C = 1$$.  
Trong nhị phân: kết quả 2-bit là $$CS = 10_2$$.

</div>

## 3. Full adder (bộ cộng đầy đủ) — cộng ba bit (A, B, Cin)

### 3.1. Vì sao cần full adder?

Khi cộng $$n$$-bit, cột thứ $$i$$ nhận:

- bit $$A_i$$, $$B_i$$,
- **carry** từ cột $$i - 1$$ (gọi $$C_i$$ hoặc Cin).

Mỗi cột phải cộng **ba** bit → **full adder** / **bộ cộng đầy đủ** (FA).

### 3.2. Bảng chân trị (8 dòng)

| $$A$$ | $$B$$ | $$C_{in}$$ | $$C_{out}$$ | $$S$$ | Tổng $$A + B + C_{in}$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 2 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 2 |
| 1 | 1 | 0 | 1 | 0 | 2 |
| 1 | 1 | 1 | 1 | 1 | 3 |

Quan hệ số học:

$$
A + B + C_{in} = 2 \cdot C_{out} + S.
$$

### 3.3. Biểu thức

$$S$$ là **XOR ba ngõ** (tổng modulo 2):

<div class="textbook-equation" markdown="1">
$$
S = A \oplus B \oplus C_{in}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

$$C_{out} = 1$$ khi **ít nhất hai** trong ba bit bằng **1** (**majority**):

<div class="textbook-equation" markdown="1">
$$
C_{out} = AB + A C_{in} + B C_{in}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

(Tương đương $$C_{out} = AB + (A \oplus B)C_{in}$$ — hữu ích khi ghép hai half adder.)

### 3.4. Hiện thực bằng hai half adder

1. HA1: đầu vào $$A, B$$ → $$S_1 = A \oplus B$$, $$C_1 = AB$$.
2. HA2: đầu vào $$S_1$$, $$C_{in}$$ → $$S = S_1 \oplus C_{in}$$, $$C_2 = S_1 \cdot C_{in}$$.
3. $$C_{out} = C_1 + C_2$$ (OR).

![Full adder — khối](/discrete-mathematics-for-computer-science-iuh/img/course/Full_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.37">Full adder: ba đầu vào, sum và carry-out — đơn vị lặp lại trong bộ cộng $$n$$-bit.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** $$A = 1$$, $$B = 1$$, $$C_{in} = 1$$ → tổng 3 → $$S = 1$$, $$C_{out} = 1$$ (nhị phân $$11_2$$).  
Kiểm: $$S = 1 \oplus 1 \oplus 1 = 1$$, $$C_{out} = 1$$.

</div>

## 4. Bộ cộng lan truyền mang (ripple-carry) — cộng $$n$$ bit

### 4.1. Cấu trúc

Cho hai số không dấu $$n$$-bit $$A = (A_{n-1} \ldots A_0)_2$$, $$B = (B_{n-1} \ldots B_0)_2$$. Đặt $$C_0 = 0$$. Với $$i = 0, \ldots, n - 1$$:

$$
(S_i, C_{i+1}) = \mathrm{FA}(A_i, B_i, C_i).
$$

Tổng $$S = (S_{n-1} \ldots S_0)_2$$; $$C_n$$ là carry ra (có thể xem như bit tổng thứ $$n$$ nếu cần $$n+1$$ bit).

![Ripple-carry 4-bit](/discrete-mathematics-for-computer-science-iuh/img/course/Ripple_Carry_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.38">Bốn full adder nối tiếp: mang “gợn sóng” từ bit thấp sang bit cao.</p>

### 4.2. Mẫu 3-bit: half adder + hai full adder

Khi $$C_0 = 0$$ cố định, cột bit thấp chỉ cần **half adder** (không có mang vào). Các cột sau dùng **full adder**:

| Cột | Khối | Đầu vào | Đầu ra |
|:---|:---|:---|:---|
| 0 (thấp) | **HA** | $$x_0, y_0$$ | $$s_0$$, $$c_0$$ |
| 1 | **FA** | $$x_1, y_1, c_0$$ | $$s_1$$, $$c_1$$ |
| 2 (cao) | **FA** | $$x_2, y_2, c_1$$ | $$s_2$$, $$c_2 = s_3$$ |

Tổng 4 bit: $$(s_3 s_2 s_1 s_0)_2$$ với $$s_3 = c_2$$.

![Cộng 3-bit HA+FA+FA](/discrete-mathematics-for-computer-science-iuh/img/course/Ripple_3bit_HA_FA.svg)

<p class="textbook-figure-caption" data-figure="13.38b">Hai số 3-bit: bộ nửa cộng ở bit thấp, rồi hai bộ cộng đầy đủ — mang lan $$c_0 \to c_1 \to c_2$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ số.** $$x = (x_2 x_1 x_0) = 101_2 = 5$$, $$y = (y_2 y_1 y_0) = 011_2 = 3$$.

| Cột | Khối | Vào | $$s$$ | $$c$$ ra |
|:---:|:---|:---|:---:|:---:|
| 0 | HA | $$1+1$$ | $$0$$ | $$1$$ |
| 1 | FA | $$0+1+1$$ | $$0$$ | $$1$$ |
| 2 | FA | $$1+0+1$$ | $$0$$ | $$1$$ |

→ $$(s_3 s_2 s_1 s_0) = 1000_2 = 8$$. Đúng $$5+3=8$$.

</div>

### 4.3. Ví dụ số 4-bit (toàn full adder)

Cộng $$A = 0101_2 = 5$$ và $$B = 0011_2 = 3$$ (kỳ vọng $$8 = 1000_2$$), với $$C_0 = 0$$ và bốn FA (FA bit 0 tương đương HA vì Cin = 0):

| Cột $$i$$ | $$A_i$$ | $$B_i$$ | $$C_i$$ | $$S_i$$ | $$C_{i+1}$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 2 | 1 | 0 | 1 | 0 | 1 |
| 3 | 0 | 0 | 1 | 1 | 0 |

→ $$S = 1000_2 = 8$$, $$C_4 = 0$$. Đúng.

### 4.4. Trễ và hạn chế

Gọi $$t_{FA}$$ là thời gian một full adder tạo ra carry-out ổn định. Mang phải ổn định **tuần tự** từ bit thấp đến bit cao:

$$
t_{\mathrm{RCA}} \approx n \cdot t_{FA}.
$$

Với $$n$$ lớn (ví dụ 64), bộ cộng lan truyền mang **chậm**. CPU thật dùng các kỹ thuật nhanh hơn (carry-lookahead, …) — ngoài phạm vi bài, nhưng **động lực** xuất phát từ công thức trên.

<div class="textbook-definition" markdown="1">

**Tính đúng.** Mỗi FA bảo toàn $$A_i + B_i + C_i = 2C_{i+1} + S_i$$. Ghép $$n$$ tầng suy ra $$A + B + C_0 = S + 2^n C_n$$ — có thể chứng minh bằng quy nạp theo $$n$$.

</div>

## 5. Mạch nhân — partial products và array

### 5.1. Ý tưởng

Nhân hai số không dấu $$n$$-bit tương tự nhân tay:

$$
A \times B = \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} (A_i B_j)\, 2^{i+j}.
$$

Mỗi $$A_i B_j$$ là **một AND** (partial product). Các bit cùng trọng số $$2^k$$ được **cộng** bằng half/full adder — đó là **array multiplier**.

### 5.2. Trường hợp 2×2

$$A = a_1 a_0$$, $$B = b_1 b_0$$. Tích 4 bit $$p_3 p_2 p_1 p_0$$:

| Partial product | Công thức |
|:---|:---|
| hàng $$b_0$$ | $$a_1 b_0$$, $$a_0 b_0$$ |
| hàng $$b_1$$ (dịch trái 1) | $$a_1 b_1$$, $$a_0 b_1$$ |

{% raw %}
$$
\begin{align*}
p_0 &= a_0 b_0,\\
p_1 &= a_1 b_0 \oplus a_0 b_1
\quad (\text{carry } c_1 = a_1 b_0 \cdot a_0 b_1),\\
p_2,\, p_3 &\text{ từ cộng cột cao hơn.}
\end{align*}
$$
{% endraw %}

![Nhân 2×2](/discrete-mathematics-for-computer-science-iuh/img/course/Array_Multiplier_2x2.svg)

<p class="textbook-figure-caption" data-figure="13.39">Nhân 2×2: AND tạo partial products; half/full adder cộng theo cột.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** $$A = 3 = 11_2$$, $$B = 3 = 11_2$$ → $$9 = 1001_2$$.  
Partial: $$11 \times 1 = 11$$, $$11 \times 1$$ dịch trái = $$110$$; cộng $$011 + 110 = 1001$$.

</div>

### 5.3. Độ phức tạp (định tính)

- Số AND: $$n^2$$ (mỗi cặp bit).
- Số adder: bậc $$\Theta(n^2)$$ trong array cổ điển.
- Độ rộng tích: $$2n$$ bit (không dấu).

## 6. Các mạch tổ hợp cơ bản khác

### 6.1. Multiplexer (MUX) 2-to-1

**Chọn** một trong hai nguồn theo bit điều khiển $$S$$:

<div class="textbook-equation" markdown="1">
$$
Y = I_0 \bar S + I_1 S.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

| $$S$$ | $$Y$$ |
|:---:|:---|
| 0 | $$I_0$$ |
| 1 | $$I_1$$ |

Trong ALU: MUX chọn giữa kết quả cộng, AND, OR, … theo mã lệnh. Đó chính là `if–else` phần cứng.

![MUX 2-to-1](/discrete-mathematics-for-computer-science-iuh/img/course/Mux_2to1.svg)

<p class="textbook-figure-caption" data-figure="13.40">MUX 2-to-1: $$Y = S\,?\, I_1 : I_0$$.</p>

**Tổng quát:** MUX $$2^k$$-to-1 có $$k$$ bit chọn; mỗi đầu ra là SOP (tổng các tích) các minterm của bit chọn nhân với đầu vào tương ứng.

### 6.2. Decoder 2-to-4

Hai bit địa chỉ $$A_1 A_0$$ kích **đúng một** trong bốn đường $$Y_0, \ldots, Y_3$$:

$$
Y_i = 1 \iff (A_1 A_0)_2 = i.
$$

Tức $$Y_i$$ chính là **minterm** $$m_i$$:

{% raw %}
$$
\begin{align*}
Y_0 &= \bar A_1 \bar A_0,\\
Y_1 &= \bar A_1 A_0,\\
Y_2 &= A_1 \bar A_0,\\
Y_3 &= A_1 A_0.
\end{align*}
$$
{% endraw %}

![Decoder 2-to-4](/discrete-mathematics-for-computer-science-iuh/img/course/Decoder_2to4.svg)

<p class="textbook-figure-caption" data-figure="13.41">Decoder 2-to-4 — mỗi tổ hợp đầu vào bật đúng một đầu ra (one-hot).</p>

**Ứng dụng:** chọn thanh ghi, giải mã opcode thô, xây ROM đơn giản.

### 6.3. Comparator 1-bit

| Đầu ra | Biểu thức |
|:---|:---|
| $$A = B$$ | $$\overline{A \oplus B} = AB + \bar A \bar B$$ |
| $$A > B$$ | $$A \bar B$$ |
| $$A < B$$ | $$\bar A B$$ |

Ghép theo bit (từ MSB) cho comparator $$n$$-bit — tương tự “ripple” quyết định bất đẳng thức.

### 6.4. Từ các khối đến ALU

- Chuỗi full adder thực hiện **ADD**.
- Muốn **trừ** trong bù 2: đảo bit của $$B$$, đặt $$C_0 = 1$$, rồi cộng.
- AND/OR/XOR bitwise đi song song trên từng cặp bit.
- MUX chọn phép (hoặc nguồn toán hạng) theo opcode.
- Comparator cấp cờ cho lệnh nhảy có điều kiện.
- Array multiplier phục vụ **MUL**.
- Decoder chọn thanh ghi hoặc góp phần giải mã lệnh.

ALU là mạng cổng được tổ chức từ các khối half/full adder, MUX, comparator và các phép bitwise.

## 7. Liên hệ với tối thiểu hóa

Half adder và full adder thường đã ở dạng gọn (XOR và majority). MUX và decoder dạng SOP (tổng các tích) chuẩn ánh xạ tự nhiên sang LUT trên FPGA, vì mỗi LUT lưu một bảng chân trị (Mục 13.6). Khi chỉ được dùng NAND, biểu thức chuyển qua De Morgan và các phương pháp rút gọn ở Mục 13.3–13.5.

## Bài tập

### Bài tập 1

Lập bảng và viết $$S$$, $$C$$ cho half adder. Hiện thực $$S$$ chỉ bằng AND, OR, NOT (không XOR).

<details>
<summary>Đáp án</summary>

$$S = \bar A B + A \bar B$$, $$C = AB$$.  
$$S$$: 2 NOT, 2 AND, 1 OR.

</details>

### Bài tập 2

Với $$A = 1$$, $$B = 0$$, $$C_{in} = 1$$, tính $$S$$, $$C_{out}$$ từ công thức và từ bảng.

<details>
<summary>Đáp án</summary>

$$S = 1 \oplus 0 \oplus 1 = 0$$, $$C_{out} = 1$$.  
Tổng số học $$1 + 0 + 1 = 2$$ → $$CS = 10_2$$.

</details>

### Bài tập 3

Cộng $$A = 0110_2$$ (6) và $$B = 0001_2$$ (1) bằng chuỗi FA ($$C_0 = 0$$). Ghi $$S$$ và các carry trung gian.

<details>
<summary>Đáp án</summary>

Cột 0: $$0+1+0 \to S_0 = 1$$, $$C_1 = 0$$.  
Cột 1: $$1+0+0 \to S_1 = 1$$, $$C_2 = 0$$.  
Cột 2: $$1+0+0 \to S_2 = 1$$, $$C_3 = 0$$.  
Cột 3: $$0+0+0 \to S_3 = 0$$, $$C_4 = 0$$.  
$$S = 0111_2 = 7$$.

</details>

### Bài tập 4

Giả sử mỗi full adder trễ mang $$2\,\mathrm{ns}$$, trễ bit tổng $$3\,\mathrm{ns}$$. Ước lượng thời gian tối thiểu để $$S_{31}$$ ổn định trên bộ cộng 32-bit: mang phải chạy từ bit thấp đến bit cao, rồi mới ra $$S_{31}$$.

<details>
<summary>Đáp án</summary>

Carry qua 31 FA trước FA31: $$31 \times 2 = 62\,\mathrm{ns}$$, rồi sum FA31: $$+3 \approx 65\,\mathrm{ns}$$ (mô hình thô).

</details>

### Bài tập 5

Tính partial products và tích của $$A = 10_2$$ (2) và $$B = 11_2$$ (3).

<details>
<summary>Đáp án</summary>

Tích $$6 = 0110_2$$.

```
      1 0          A
    × 1 1          B
    -----
      1 0          A × b0
    1 0            A × b1, dịch trái 1
    -----
    0 1 1 0        = 6
```

</details>

### Bài tập 6

Chứng minh bằng bảng: $$Y = I_0\bar S + I_1 S$$ cho đúng hành vi 2-to-1. Viết $$Y$$ nếu cần chọn giữa $$A \oplus B$$ và $$AB$$ theo $$S$$.

<details>
<summary>Đáp án</summary>

Khi $$S = 0$$, $$Y = I_0$$; khi $$S = 1$$, $$Y = I_1$$.  
$$Y = (A \oplus B)\bar S + (AB)S$$.

</details>

### Bài tập 7

Viết minterm cho $$Y_2$$ của decoder 2-to-4. Decoder 3-to-8 có bao nhiêu đầu ra? Bao nhiêu đầu ra = **1** tại một thời điểm (enable luôn bật)?

<details>
<summary>Đáp án</summary>

$$Y_2 = A_1 \bar A_0$$.  
3-to-8: 8 đầu ra; đúng **một** đầu ra = **1**.

</details>

### Bài tập 8

Giải thích cách dùng bộ cộng để tính $$A - B$$ trong bù 2: gợi ý $$A + \bar B + 1$$. $$C_0$$ ban đầu bằng bao nhiêu?

<details>
<summary>Đáp án</summary>

Bù 2 của $$B$$ là $$\bar B + 1$$. Đưa $$\bar B$$ vào ngõ B, đặt $$C_0 = 1$$. Kết quả là $$A - B$$ trong bù 2 (đủ bit).

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=RTKQMuWHqG4">Binary addition</a> — half/full adder trực quan
- <a href="https://www.youtube.com/watch?v=YHUCmHvCMlY">How computers do math</a> — bối cảnh ALU
- <a href="https://www.youtube.com/watch?v=ZRCeGwZEd_g">Multiplexers</a> — MUX và ứng dụng

## Tóm tắt

1. Half adder: $$S = A \oplus B$$, $$C = AB$$ (không mang vào).  
2. Full adder: $$S = A \oplus B \oplus C_{in}$$, $$C_{out} = AB + AC_{in} + BC_{in}$$.  
3. Bộ cộng $$n$$-bit kiểu ripple-carry: chuỗi full adder; trễ mang tỉ lệ $$n$$.  
4. Nhân không dấu: $$n^2$$ AND (partial products) kết hợp mạng cộng theo cột.  
5. MUX, decoder và comparator thực hiện chọn nguồn, giải mã one-hot và so sánh trong datapath.

Các khối trên cấu thành lõi số học tổ hợp cơ bản trên nền đại số Boolean.
