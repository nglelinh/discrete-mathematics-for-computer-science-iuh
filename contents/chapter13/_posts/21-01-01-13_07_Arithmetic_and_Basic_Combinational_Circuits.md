---
layout: post
title: "Mạch Cộng, Mạch Nhân và Các Mạch Tổ hợp Cơ bản"
categories: chapter13
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Xây dựng half adder, full adder, bộ cộng lan truyền nhớ (ripple-carry) n-bit, mạch nhân không dấu bằng tích riêng phần, cùng các khối tổ hợp MUX, decoder và comparator."
---

<div class="textbook-epigraph" markdown="1">

"An ALU is not magic — it is a carefully arranged forest of adders, multiplexers, and Boolean glue."

<span class="epigraph-attribution">— Digital design classroom wisdom</span>

</div>

Các mục trước đã trình bày hàm Boole, cổng logic và các kỹ thuật tối thiểu hóa. Mục này kết hợp các thành phần đó để xây dựng những khối mạch số học và mạch tổ hợp cơ bản:

1. **Bộ cộng**: half adder, full adder và bộ cộng $$n$$-bit.
2. **Bộ nhân**: tạo các tích riêng phần (partial products) và cộng theo cột.
3. **MUX, decoder và comparator**: chọn nguồn dữ liệu, giải mã địa chỉ và so sánh.

Mọi khối mạch đều được xây dựng theo cùng một lộ trình:

**bảng chân trị → biểu thức Boole → sơ đồ cổng.**

Các phép toán `a + b` hay `a * b` trong ngôn ngữ lập trình được hiện thực ở mức phần cứng bằng **mạng cổng** thao tác trên bit **0**/**1**. Chuỗi half adder → full adder → bộ cộng $$n$$-bit → bộ nhân kết nối trực tiếp biểu thức $$x \oplus y$$ với đường dữ liệu (datapath) nhiều bit.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** half adder và full adder từ bảng chân trị bằng các cổng XOR, AND, OR.
- **Ghép nối** các full adder thành bộ cộng $$n$$-bit lan truyền nhớ và ước lượng độ trễ nhớ.
- **Mô tả** cơ chế nhân số không dấu bằng tích riêng phần và mạng cộng theo cột.
- **Viết** biểu thức Boole cho MUX 2-to-1, decoder 2-to-4 và comparator 1-bit.
- **Liên hệ** các khối tổ hợp này với cấu trúc khối số học–logic (ALU).

**Từ khóa**: half adder, full adder, ripple-carry, partial product, MUX, decoder, comparator, mạch tổ hợp.

</div>

## Mạch tổ hợp

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Mạch tổ hợp** (*combinational circuit*) là mạch có đầu ra tại thời điểm $$t$$ chỉ phụ thuộc vào **đầu vào tại thời điểm $$t$$** (sau độ trễ lan truyền qua các cổng) và **không** chứa phần tử nhớ trạng thái bên trong. Ngược lại, **mạch tuần tự** (*sequential circuit*) bổ sung thêm flip-flop hoặc thanh ghi — nội dung thuộc chủ đề automata và máy trạng thái hữu hạn (FSM).

</div>

Toàn bộ các khối cộng, nhân, MUX, decoder và so sánh xét trong bài này đều là mạch tổ hợp.

![Cổng XOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_XOR.svg)

<p class="textbook-figure-caption" data-figure="13.35a">Cổng XOR tạo bit tổng của half adder.</p>

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.35b">Cổng AND tạo bit nhớ của half adder.</p>

## Half adder (bộ nửa cộng) — cộng hai bit, không có nhớ vào

### Bảng chân trị

**Bộ nửa cộng** (*half adder*) thực hiện cộng hai bit $$A, B \in \{0,1\}$$ mà **không** có bit nhớ từ cột trước:

$$
A + B = 2 \cdot C + S,
$$

trong đó $$S$$ là **bit tổng** (*sum*) và $$C$$ là **bit nhớ** (*carry*).

| $$A$$ | $$B$$ | $$S$$ | $$C$$ | Ý nghĩa |
|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 0 | 0 | $$0 + 0 = 0$$ |
| 0 | 1 | 1 | 0 | $$0 + 1 = 1$$ |
| 1 | 0 | 1 | 0 | $$1 + 0 = 1$$ |
| 1 | 1 | 0 | 1 | $$1 + 1 = 2 = 10_2$$ |

### Biểu thức Boole

Đọc trực tiếp dạng SOP từ bảng chân trị:

- Cột $$S$$ bằng **1** khi $$A$$ và $$B$$ **khác nhau** → cổng **XOR**.
- Cột $$C$$ bằng **1** khi **cả hai** đều bằng **1** → cổng **AND**.

<div class="textbook-equation" markdown="1">
$$
S = A \oplus B = \bar A B + A \bar B,\qquad
C = A \cdot B.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tên gọi **half adder** (“nửa” bộ cộng) xuất phát từ việc mạch **không** có ngõ nhớ vào ($$C_{in}$$). Khối này đủ để cộng 2 bit độc lập hoặc cột bit thấp nhất, nhưng chưa đủ cho các cột giữa trong bộ cộng $$n$$-bit.

![Half adder](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.36">Half adder: cổng XOR cho bit tổng và cổng AND cho bit nhớ.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** Với $$A = 1$$ và $$B = 1$$, ta được $$S = 0$$ và $$C = 1$$, tương ứng kết quả 2 bit là $$CS = 10_2$$.

</div>

## Full adder (bộ cộng đầy đủ) — cộng ba bit ($$A, B, C_{in}$$)

### Vì sao cần full adder?

Khi cộng hai số $$n$$-bit, mỗi cột thứ $$i$$ cần cộng đồng thời **ba** bit: hai bit toán hạng $$A_i, B_i$$ và **bit nhớ** truyền từ cột $$i - 1$$ sang (ký hiệu $$C_i$$ hoặc $$C_{in}$$). Khối thực hiện phép cộng 3 bit này là **full adder** (*bộ cộng đầy đủ*, viết tắt FA).

### Bảng chân trị (8 dòng)

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

### Biểu thức Boole

Bit tổng $$S$$ là phép **XOR ba ngõ vào** (tổng modulo 2):

<div class="textbook-equation" markdown="1">
$$
S = A \oplus B \oplus C_{in}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Bit nhớ ra $$C_{out}$$ bằng **1** khi **ít nhất hai** trong ba bit đầu vào bằng **1** (hàm đa số — majority):

<div class="textbook-equation" markdown="1">
$$
C_{out} = AB + A C_{in} + B C_{in}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Biểu thức này tương đương với $$C_{out} = AB + (A \oplus B)C_{in}$$, thuận tiện khi ghép từ hai half adder.

### Hiện thực bằng hai half adder

1. **HA1**: nhận $$A, B$$ → tạo $$S_1 = A \oplus B$$ và $$C_1 = AB$$.
2. **HA2**: nhận $$S_1, C_{in}$$ → tạo $$S = S_1 \oplus C_{in}$$ và $$C_2 = S_1 \cdot C_{in}$$.
3. Dùng một cổng OR để lấy $$C_{out} = C_1 + C_2$$.

![Full adder — khối](/discrete-mathematics-for-computer-science-iuh/img/course/Full_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.37">Full adder gồm ba ngõ vào, một bit tổng và một bit nhớ ra — đơn vị cơ bản lặp lại trong bộ cộng $$n$$-bit.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** Với $$A = 1$$, $$B = 1$$, $$C_{in} = 1$$, tổng bằng 3 nên $$S = 1$$ và $$C_{out} = 1$$ (nhị phân $$11_2$$). Kiểm tra bằng công thức: $$S = 1 \oplus 1 \oplus 1 = 1$$ và $$C_{out} = 1$$.

</div>

## Bộ cộng lan truyền nhớ (ripple-carry) — cộng $$n$$ bit

### Cấu trúc

Cho hai số không dấu $$n$$-bit $$A = (A_{n-1} \ldots A_0)_2$$ và $$B = (B_{n-1} \ldots B_0)_2$$. Đặt $$C_0 = 0$$; với từng cột $$i = 0, \ldots, n - 1$$:

$$
(S_i, C_{i+1}) = \mathrm{FA}(A_i, B_i, C_i).
$$

Kết quả gồm $$n$$ bit tổng $$S = (S_{n-1} \ldots S_0)_2$$ và bit nhớ ra cuối cùng $$C_n$$ (có thể coi là bit thứ $$n$$ nếu biểu diễn tổng bằng $$n+1$$ bit).

![Ripple-carry 4-bit](/discrete-mathematics-for-computer-science-iuh/img/course/Ripple_Carry_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.38">Bốn full adder mắc nối tiếp: bit nhớ lan truyền tuần tự từ bit thấp sang bit cao.</p>

### Mẫu 3-bit: một half adder và hai full adder

Vì cột bit thấp nhất có $$C_0 = 0$$ cố định, ta có thể dùng **half adder** ở cột 0 và **full adder** cho các cột cao hơn:

| Cột | Khối | Đầu vào | Đầu ra |
|:---|:---|:---|:---|
| 0 (thấp) | **HA** | $$x_0, y_0$$ | $$s_0$$, $$c_0$$ |
| 1 | **FA** | $$x_1, y_1, c_0$$ | $$s_1$$, $$c_1$$ |
| 2 (cao) | **FA** | $$x_2, y_2, c_1$$ | $$s_2$$, $$c_2 = s_3$$ |

Tổng 4 bit thu được là $$(s_3 s_2 s_1 s_0)_2$$ với $$s_3 = c_2$$.

![Cộng 3-bit HA+FA+FA](/discrete-mathematics-for-computer-science-iuh/img/course/Ripple_3bit_HA_FA.svg)

<p class="textbook-figure-caption" data-figure="13.38b">Cộng hai số 3-bit: half adder ở bit thấp nhất, theo sau là hai full adder với bit nhớ lan truyền $$c_0 \to c_1 \to c_2$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ số.** Cộng $$x = 101_2 = 5$$ và $$y = 011_2 = 3$$:

| Cột | Khối | Phép cộng | $$s$$ | $$c$$ ra |
|:---:|:---|:---|:---:|:---:|
| 0 | HA | $$1+1$$ | $$0$$ | $$1$$ |
| 1 | FA | $$0+1+1$$ | $$0$$ | $$1$$ |
| 2 | FA | $$1+0+1$$ | $$0$$ | $$1$$ |

Kết quả: $$(s_3 s_2 s_1 s_0) = 1000_2 = 8$$, khớp với $$5+3=8$$.

</div>

### Ví dụ số 4-bit (dùng toàn bộ full adder)

Cộng $$A = 0101_2 = 5$$ và $$B = 0011_2 = 3$$ với $$C_0 = 0$$ bằng bốn FA (FA ở bit 0 hoạt động như HA do $$C_0 = 0$$):

| Cột $$i$$ | $$A_i$$ | $$B_i$$ | $$C_i$$ | $$S_i$$ | $$C_{i+1}$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 2 | 1 | 0 | 1 | 0 | 1 |
| 3 | 0 | 0 | 1 | 1 | 0 |

Thu được $$S = 1000_2 = 8$$ và $$C_4 = 0$$.

### Độ trễ và hạn chế

Gọi $$t_{FA}$$ là thời gian một full adder tạo ra bit nhớ $$C_{out}$$ ổn định. Vì bit nhớ phải lan truyền tuần tự qua tất cả $$n$$ tầng từ bit thấp đến bit cao:

$$
t_{\mathrm{RCA}} \approx n \cdot t_{FA}.
$$

Khi $$n$$ lớn (ví dụ 64 bit), độ trễ của bộ cộng lan truyền nhớ trở nên đáng kể. Đó là lý do các bộ xử lý thực tế áp dụng các kiến trúc cộng nhanh hơn như *carry-lookahead* (ngoài phạm vi bài này).

<div class="textbook-definition" markdown="1">

**Tính đúng đắn.** Mỗi full adder bảo toàn đẳng thức $$A_i + B_i + C_i = 2C_{i+1} + S_i$$. Ghép $$n$$ tầng và quy nạp theo $$n$$ cho $$A + B + C_0 = S + 2^n C_n$$.

</div>

### Thử nghiệm: lan truyền nhớ trong bộ cộng ripple-carry

Quan sát bộ cộng 4 bit gồm bốn full adder nối tiếp: theo dõi bit nhớ lan qua từng tầng, thử phép cộng/trừ bù hai và hiện tượng tràn số.

<div class="interactive-demo" markdown="1">
<div data-demo="adder-explainer" data-a="11" data-b="6"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Mạch nhân — tích riêng phần và mạch mảng

### Ý tưởng

Phép nhân hai số không dấu $$n$$-bit có thể viết theo khai triển nhị phân giống cách nhân đặt tính bằng tay:

$$
A \times B = \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} (A_i B_j)\, 2^{i+j}.
$$

Mỗi tích bit $$A_i B_j$$ được tạo bằng **một cổng AND** (gọi là tích riêng phần — *partial product*). Sau đó, các bit có cùng trọng số $$2^k$$ được cộng lại bằng mạng half adder và full adder, tạo thành **mạch nhân mảng** (*array multiplier*).

### Trường hợp 2×2 bit

Với $$A = a_1 a_0$$ và $$B = b_1 b_0$$, tích 4 bit $$p_3 p_2 p_1 p_0$$ được tạo từ các tích riêng phần:

| Tích riêng phần | Công thức |
|:---|:---|
| hàng $$b_0$$ | $$a_1 b_0$$, $$a_0 b_0$$ |
| hàng $$b_1$$ (dịch trái 1 vị trí) | $$a_1 b_1$$, $$a_0 b_1$$ |

{% raw %}
$$
\begin{align*}
p_0 &= a_0 b_0,\\
p_1 &= a_1 b_0 \oplus a_0 b_1
\quad (\text{nhớ } c_1 = a_1 b_0 \cdot a_0 b_1),\\
p_2,\, p_3 &\text{ thu được từ phép cộng ở các cột cao hơn.}
\end{align*}
$$
{% endraw %}

![Nhân 2×2](/discrete-mathematics-for-computer-science-iuh/img/course/Array_Multiplier_2x2.svg)

<p class="textbook-figure-caption" data-figure="13.39">Mạch nhân 2×2: các cổng AND tạo tích riêng phần, các bộ cộng cộng dồn theo từng cột.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** Với $$A = 3 = 11_2$$ và $$B = 3 = 11_2$$, các tích riêng phần là $$11 \times 1 = 11$$ và $$11 \times 1$$ dịch trái thành $$110$$; cộng lại cho $$011 + 110 = 1001_2 = 9$$.

</div>

### Độ phức tạp (định tính)

- Số cổng AND: $$n^2$$ (một cổng cho mỗi cặp bit).
- Số bộ cộng: bậc $$\Theta(n^2)$$ trong mạch mảng cổ điển.
- Độ rộng kết quả: $$2n$$ bit (đối với số nguyên không dấu).

## Các mạch tổ hợp cơ bản khác

### Bộ chọn kênh (Multiplexer — MUX) 2-to-1

MUX 2-to-1 chọn một trong hai tín hiệu đầu vào $$I_0, I_1$$ đưa ra ngõ ra $$Y$$ theo bit điều khiển $$S$$:

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

Trong ALU, MUX chọn giữa kết quả của phép cộng, AND, OR… dựa theo mã lệnh — đóng vai trò tương tự cấu trúc `if–else` ở mức phần cứng.

![MUX 2-to-1](/discrete-mathematics-for-computer-science-iuh/img/course/Mux_2to1.svg)

<p class="textbook-figure-caption" data-figure="13.40">MUX 2-to-1 thực hiện lựa chọn $$Y = S\,?\, I_1 : I_0$$.</p>

**Tổng quát:** MUX $$2^k$$-to-1 sử dụng $$k$$ bit chọn; biểu thức đầu ra là tổng các tích giữa từng minterm của $$k$$ bit chọn với ngõ vào dữ liệu tương ứng.

### Bộ giải mã (Decoder) 2-to-4

Hai bit địa chỉ $$A_1 A_0$$ kích hoạt **đúng một** trong bốn ngõ ra $$Y_0, \ldots, Y_3$$:

$$
Y_i = 1 \iff (A_1 A_0)_2 = i.
$$

Mỗi ngõ ra $$Y_i$$ chính là **minterm** $$m_i$$:

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

<p class="textbook-figure-caption" data-figure="13.41">Decoder 2-to-4: mỗi tổ hợp đầu vào kích hoạt đúng một đường đầu ra (mã one-hot).</p>

**Ứng dụng:** chọn thanh ghi trong tập thanh ghi, giải mã mã lệnh (opcode) và xây dựng bộ nhớ ROM đơn giản.

### Bộ so sánh (Comparator) 1-bit

| Đầu ra | Biểu thức |
|:---|:---|
| $$A = B$$ | $$\overline{A \oplus B} = AB + \bar A \bar B$$ |
| $$A > B$$ | $$A \bar B$$ |
| $$A < B$$ | $$\bar A B$$ |

Để so sánh hai số $$n$$-bit, ta ghép các tầng so sánh từ bit cao nhất (MSB) xuống thấp dần.

### Ghép các khối thành ALU

- Chuỗi full adder thực hiện phép cộng (**ADD**).
- Phép **trừ** trong biểu diễn bù 2 thực hiện bằng cách đảo bit của $$B$$, đặt $$C_0 = 1$$ rồi đưa vào bộ cộng.
- Các phép AND/OR/XOR theo từng bit chạy song song trên mỗi cặp bit tương ứng.
- MUX chọn kết quả phép toán đầu ra theo mã lệnh (opcode).
- Comparator cung cấp các cờ trạng thái cho lệnh rẽ nhánh có điều kiện.
- Mạch nhân mảng thực hiện phép nhân (**MUL**).
- Decoder chọn thanh ghi và tham gia giải mã lệnh.

Như vậy, khối ALU là một mạng cổng tổ hợp có cấu trúc gồm các bộ cộng, bộ nhân, MUX, comparator và các mạch bitwise.

## Liên hệ với tối thiểu hóa

Half adder và full adder vốn đã có biểu thức gọn (XOR và hàm đa số). Các mạch MUX và decoder ở dạng SOP chuẩn ánh xạ trực tiếp sang các bảng tra cứu LUT trên FPGA (Mục 13.6). Khi cần hiện thực chỉ bằng cổng NAND, ta biến đổi biểu thức qua luật De Morgan và các kỹ thuật tối thiểu hóa ở Mục 13.3–13.5.

## Bài tập

### Bài tập 1

Lập bảng chân trị và viết biểu thức cho $$S$$, $$C$$ của half adder. Hiện thực $$S$$ chỉ bằng các cổng AND, OR và NOT (không dùng XOR).

<details>
<summary>Đáp án</summary>

$$S = \bar A B + A \bar B$$ và $$C = AB$$.  
Mạch tạo $$S$$ không dùng XOR gồm 2 cổng NOT, 2 cổng AND và 1 cổng OR.

</details>

### Bài tập 2

Với $$A = 1$$, $$B = 0$$, $$C_{in} = 1$$, tính $$S$$ và $$C_{out}$$ của full adder bằng công thức và kiểm tra lại theo bảng chân trị.

<details>
<summary>Đáp án</summary>

$$S = 1 \oplus 0 \oplus 1 = 0$$ và $$C_{out} = 1\cdot 0 + 1\cdot 1 + 0\cdot 1 = 1$$.  
Tổng số học $$1 + 0 + 1 = 2 = 10_2$$, khớp với $$(C_{out}, S) = (1, 0)$$.

</details>

### Bài tập 3

Cộng $$A = 0110_2$$ (6) và $$B = 0001_2$$ (1) bằng chuỗi 4 full adder với $$C_0 = 0$$. Ghi rõ các bit tổng $$S_i$$ và bit nhớ trung gian $$C_{i+1}$$.

<details>
<summary>Đáp án</summary>

Cột 0: $$0+1+0 \to S_0 = 1$$, $$C_1 = 0$$.  
Cột 1: $$1+0+0 \to S_1 = 1$$, $$C_2 = 0$$.  
Cột 2: $$1+0+0 \to S_2 = 1$$, $$C_3 = 0$$.  
Cột 3: $$0+0+0 \to S_3 = 0$$, $$C_4 = 0$$.  
Kết quả: $$S = 0111_2 = 7$$.

</details>

### Bài tập 4

Giả sử mỗi full adder có độ trễ tạo bit nhớ là $$2\,\mathrm{ns}$$ và độ trễ tạo bit tổng là $$3\,\mathrm{ns}$$. Ước lượng thời gian tối thiểu để bit $$S_{31}$$ ổn định trong bộ cộng ripple-carry 32-bit.

<details>
<summary>Đáp án</summary>

Bit nhớ phải đi qua 31 tầng FA trước khi tới FA31, tốn $$31 \times 2 = 62\,\mathrm{ns}$$; sau đó FA31 mất thêm $$3\,\mathrm{ns}$$ để tạo $$S_{31}$$. Tổng thời gian ước lượng là $$65\,\mathrm{ns}$$.

</details>

### Bài tập 5

Tính các tích riêng phần và tích cuối cùng của $$A = 10_2$$ (2) và $$B = 11_2$$ (3).

<details>
<summary>Đáp án</summary>

Tích bằng $$6 = 0110_2$$:

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

Kiểm tra bằng bảng chân trị rằng $$Y = I_0\bar S + I_1 S$$ thực hiện đúng chức năng MUX 2-to-1. Viết biểu thức $$Y$$ khi cần chọn giữa $$A \oplus B$$ và $$AB$$ theo bit chọn $$S$$.

<details>
<summary>Đáp án</summary>

Khi $$S = 0$$, $$Y = I_0\cdot 1 + I_1\cdot 0 = I_0$$; khi $$S = 1$$, $$Y = I_0\cdot 0 + I_1\cdot 1 = I_1$$.  
Với hai nguồn đã cho: $$Y = (A \oplus B)\bar S + (AB)S$$.

</details>

### Bài tập 7

Viết minterm ứng với ngõ ra $$Y_2$$ của decoder 2-to-4. Một decoder 3-to-8 có bao nhiêu ngõ ra, và có bao nhiêu ngõ ra bằng **1** tại cùng một thời điểm (khi ngõ enable luôn bật)?

<details>
<summary>Đáp án</summary>

$$Y_2 = A_1 \bar A_0$$.  
Decoder 3-to-8 có 8 ngõ ra, và tại mỗi thời điểm có đúng **một** ngõ ra bằng **1**.

</details>

### Bài tập 8

Giải thích cách dùng bộ cộng $$n$$-bit để tính $$A - B$$ trong biểu diễn bù 2 dựa trên đẳng thức $$A - B = A + \bar B + 1$$. Khi đó $$C_0$$ cần đặt bằng bao nhiêu?

<details>
<summary>Đáp án</summary>

Số đối của $$B$$ trong biểu diễn bù 2 là $$\bar B + 1$$. Do đó, ta đảo toàn bộ các bit của $$B$$ thành $$\bar B$$ đưa vào ngõ vào thứ hai của bộ cộng và đặt bit nhớ đầu vào $$C_0 = 1$$; tổng thu được chính là $$A - B$$ trong biểu diễn bù 2.

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=RTKQMuWHqG4">Binary addition</a> — minh họa trực quan half/full adder
- <a href="https://www.youtube.com/watch?v=YHUCmHvCMlY">How computers do math</a> — bối cảnh hoạt động của ALU
- <a href="https://www.youtube.com/watch?v=ZRCeGwZEd_g">Multiplexers</a> — nguyên lý và ứng dụng của MUX

## Tóm tắt

1. Half adder: $$S = A \oplus B$$, $$C = AB$$ (không có bit nhớ vào).  
2. Full adder: $$S = A \oplus B \oplus C_{in}$$, $$C_{out} = AB + AC_{in} + BC_{in}$$.  
3. Bộ cộng $$n$$-bit lan truyền nhớ (ripple-carry) ghép nối tiếp $$n$$ tầng full adder, có độ trễ nhớ tỉ lệ tuyến tính theo $$n$$.  
4. Mạch nhân mảng không dấu dùng $$n^2$$ cổng AND tạo tích riêng phần kết hợp mạng cộng theo cột.  
5. MUX, decoder và comparator thực hiện các chức năng chọn kênh, giải mã one-hot và so sánh trong datapath.

Các khối tổ hợp này tạo nên phần lõi số học cơ bản dựa trên đại số Boole.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=wvJc9CZcvBc">Learn how computers add numbers and build a 4 bit adder circuit</a> — Ben Eater, tiếng Anh. Minh họa phép cộng nhị phân và lắp dựng mạch cộng 4 bit thực tế.
- <a href="https://www.youtube.com/watch?v=aLUY-s7LSns">Half Adder</a> — Neso Academy, tiếng Anh. Xây dựng half adder từ bảng chân trị.
- <a href="https://www.youtube.com/watch?v=FKvnmxte98A">Introduction to Multiplexers | MUX Basic</a> — Neso Academy, tiếng Anh. Giới thiệu nguyên lý bộ chọn kênh (MUX).
