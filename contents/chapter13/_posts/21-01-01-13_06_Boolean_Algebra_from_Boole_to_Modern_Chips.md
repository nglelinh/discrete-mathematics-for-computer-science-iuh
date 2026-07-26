---
layout: post
title: "Đại số Boole: Từ Boole đến Chip Hiện đại"
categories: chapter13
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Tổng hợp chương 13: Boole–Shannon, mạng công tắc, năm bước thiết kế mạch, tối thiểu hóa và số cổng, half/full adder, SAT và FPGA."
---

<div class="textbook-epigraph" markdown="1">

"It has been found that the symbolism of Algebra is capable of indicating… the laws of those mental operations which are involved in reasoning."

<span class="epigraph-attribution">— George Boole, *An Investigation of the Laws of Thought* (1854)</span>

</div>

Các mục 13.1–13.5 xây dựng lần lượt đại số Boole, hàm và dạng chuẩn, cổng logic, cùng các phương pháp tối thiểu hóa. Mục này đặt các công cụ đó vào một khung thống nhất: cùng một hệ ký hiệu logic, từ thế kỷ XIX, đã trở thành ngôn ngữ mô tả và tối ưu **mạch số**. Mỗi bước rút gọn biểu thức không chỉ gọn trên giấy mà còn làm giảm số cổng, rút ngắn đường tín hiệu và tạo điều kiện cho kiểm chứng.

| Giai đoạn | Nội dung | Mục |
|:---:|:---|:---|
| 1 | Đại số Boole | 13.1 |
| 2 | Hàm, bảng chân trị, SOP / POS | 13.2 |
| 3 | Cổng và tối thiểu hóa đại số | 13.3 |
| 4 | K-map và Quine–McCluskey | 13.4–13.5 |
| 5 | Bối cảnh lịch sử và ứng dụng | **13.6** |
| 6 | Mạch cộng, MUX, decoder | 13.7 |

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tóm tắt** đóng góp của Boole và Shannon; liên hệ công tắc nối tiếp / song song với AND / OR.
- **Mô tả** quy trình thiết kế năm bước từ yêu cầu đến mạng cổng.
- **Phân tích** các ví dụ tổ hợp: ba công tắc–đèn, majority, half/full adder.
- **Giải thích** quan hệ giữa rút gọn biểu thức và số cổng.
- **Liên hệ** SAT với kiểm tra tương đương mạch; mô tả FPGA/LUT như bảng chân trị cấu hình được.

**Từ khóa**: đại số Boole, Claude Shannon, mạng công tắc, thiết kế tổ hợp, tối thiểu hóa, half/full adder, SAT, FPGA, LUT.

</div>

## 1. Hai bước nhảy lịch sử: Boole và Shannon

### 1.1. George Boole — đại số hóa suy luận

George Boole (1815–1864) không thiết kế máy tính. Trong *The Laws of Thought* (1854), ông biểu diễn thao tác trên mệnh đề và lớp bằng ký hiệu đại số — cộng, nhân, bù — với các quy luật riêng, chẳng hạn $$1 + 1 = 1$$ trong ngữ cảnh logic.

Đóng góp then chốt đối với tin học là suy luận được viết thành **biểu thức** biến đổi được theo quy tắc hình thức, thay vì chỉ diễn đạt bằng ngôn ngữ tự nhiên.

![George Boole](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="13.26">George Boole (1815–1864) — đặt nền đại số cho logic.</p>

### 1.2. Claude Shannon — Boole khớp với mạch đóng/mở

Năm **1937**, luận văn thạc sĩ của Claude Shannon thiết lập sự tương ứng giữa đại số Boole và mạch chuyển mạch:

| Logic / Boole | Mạch chuyển mạch (rơ-le / công tắc) |
|:---|:---|
| **0** / **1** | hở / đóng (hoặc hai mức điện áp) |
| AND | **nối tiếp**: chỉ dẫn khi mọi công tắc đóng |
| OR | **song song**: dẫn khi ít nhất một công tắc đóng |
| NOT | tiếp điểm đảo (bù) |

![Nối tiếp và song song](/discrete-mathematics-for-computer-science-iuh/img/course/Switch_series_parallel.svg)

<p class="textbook-figure-caption" data-figure="13.27a">Nối tiếp tương ứng AND; song song tương ứng OR.</p>

Cùng một biểu thức Boole vừa mô tả suy luận vừa mô tả mạng công tắc. Thiết kế mạch số nhờ đó có thể dựa trên biến đổi đại số có quy tắc, thay vì chỉ thử–sai trên sơ đồ.

<div class="textbook-example" markdown="1">

**Ví dụ.** Nhánh trên gồm $$x$$ nối tiếp với $$(y$$ song song $$z)$$; nhánh dưới gồm $$\bar z$$ nối tiếp $$\bar x$$; hai nhánh song song rồi nối tiếp $$t$$. Hàm dẫn:

$$
f(x,y,z,t)=\bigl[x(y+z)+\bar z\,\bar x\bigr]t = xyt + xzt + \bar x\,\bar z\, t.
$$

Biểu thức thu được đã ở dạng **SOP** (tổng các tích), có thể hiện thực bằng mạng AND–OR–NOT hoặc ánh xạ sang LUT.

</div>

![Claude Shannon](/discrete-mathematics-for-computer-science-iuh/img/course/ClaudeShannon_MFO3807.jpg)

<p class="textbook-figure-caption" data-figure="13.27">Claude Shannon (1916–2001) — ánh xạ đại số Boole lên mạch rơ-le (1937).</p>

<div class="textbook-definition" markdown="1">

**Phân biệt mốc lịch sử.** Boole (thế kỷ XIX) xây dựng đại số logic. Shannon (1937) **ánh xạ** đại số đó lên mạch điện. Transistor và mạch tích hợp về sau là **hiện thực vật lý** của các cổng; khung logic vẫn là đại số Boole.

</div>

<div class="textbook-definition" markdown="1">

**Mạch và cổng.**  
- *Mạch chuyển mạch* gồm công tắc và dây dẫn; đại lượng quan tâm là có hay không có dòng.  
- Mỗi **công tắc** tương ứng một **biến Boole**.  
- **Cổng logic** là khối có một hoặc nhiều ngõ vào và một ngõ ra theo bảng chân trị cố định (AND, OR, NOT, NAND, NOR, XOR, XNOR; xem 13.3).

</div>

## 2. Từ yêu cầu đến mạng cổng

Một chức năng số — ví dụ cộng hai bit — có thể mô tả ở nhiều lớp **tương đương về hành vi**:

| Lớp | Nội dung | Ví dụ cộng một bit |
|:---|:---|:---|
| 1. Bảng chân trị | Ánh xạ đầu vào → đầu ra | $$(1,1)\mapsto (c,s)=(1,0)$$ |
| 2. Biểu thức Boole | SOP / POS | $$s=x\oplus y$$, $$c=xy$$ |
| 3. Mạng cổng | Sơ đồ AND/OR/NOT/XOR | 1 XOR + 1 AND |
| 4. Hiện thực | Linh kiện hoặc FPGA | transistor; LUT |

![Bảng chân trị](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.28">Bảng chân trị đặc tả hành vi trước khi viết biểu thức hay vẽ cổng.</p>

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.29">Cổng AND.</p>

![Cổng OR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_OR.svg)

<p class="textbook-figure-caption" data-figure="13.29b">Cổng OR.</p>

![Cổng NOT](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.29c">Cổng NOT.</p>

![Transistor CMOS (mô hình)](/discrete-mathematics-for-computer-science-iuh/img/course/transistor.svg)

<p class="textbook-figure-caption" data-figure="13.30">Transistor là phần tử vật lý cấu thành cổng logic trên silicon.</p>

### 2.1. Quy trình thiết kế năm bước

Từ mô tả bằng lời đến mạng cổng (và tiếp đến silicon hoặc FPGA) có thể tóm tắt thành năm bước:

| Bước | Nội dung |
|:---:|:---|
| 1 | Đặt biến vào/ra và quy ước **0**/**1** |
| 2 | Lập bảng chân trị đầy đủ |
| 3 | Viết biểu thức (thường SOP từ các dòng $$Y=1$$) |
| 4 | Rút gọn (đại số, K-map hoặc Quine–McCluskey) |
| 5 | Hiện thực bằng mạng cổng và đánh giá số cổng / số tầng |

![Bước 1 — Đặt biến](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_1.svg)

<p class="textbook-figure-caption" data-figure="13.30a">Bước 1: đặt biến và quy ước 0–1.</p>

![Bước 5 — Vẽ mạch](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_5.svg)

<p class="textbook-figure-caption" data-figure="13.30b">Bước 5: từ biểu thức đã rút gọn đến mạng cổng.</p>

Hai thao tác ngược chiều bổ trợ nhau: từ sơ đồ suy ra biểu thức, và từ biểu thức dựng sơ đồ. Ví dụ đọc mạch:

$$
Y = (\bar A + B)(A + B + C)\bar C.
$$

![Đọc mạch ra biểu thức](/discrete-mathematics-for-computer-science-iuh/img/course/Circuit_to_expression.svg)

<p class="textbook-figure-caption" data-figure="13.30c">Gán nhãn từng lớp cổng để suy ra biểu thức.</p>

### 2.2. Ví dụ: ba công tắc và đèn

<div class="textbook-example" markdown="1">

**Ví dụ.** Ba công tắc $$A,B,C$$; đèn $$Y$$ sáng khi cả ba hở, hoặc khi công tắc 1 và 2 đóng còn công tắc 3 hở. Quy ước: đóng = **1**, hở = **0**; sáng = **1**.

$$Y=1$$ chỉ tại $$(0,0,0)$$ và $$(1,1,0)$$, nên

$$
Y = \bar A\bar B\bar C + AB\bar C = \bar C\,(\bar A\bar B + AB) = \bar C\,(A \odot B),
$$

trong đó $$A \odot B$$ là phép **XNOR**. Hiện thực gọn gồm một XNOR và một AND với $$\bar C$$.

</div>

![Bảng ba công tắc](/discrete-mathematics-for-computer-science-iuh/img/course/Three_switch_truth_table.svg)

<p class="textbook-figure-caption" data-figure="13.30d">Bảng chân trị của hàm ba công tắc–đèn.</p>

![Mạch ba công tắc–đèn](/discrete-mathematics-for-computer-science-iuh/img/course/Three_switch_lamp.svg)

<p class="textbook-figure-caption" data-figure="13.30e">Mạng cổng cho $$Y=\bar C(A\odot B)$$.</p>

### 2.3. Majority và half / full adder

Hàm **majority** ba biến $$f = xy + xz + yz$$ bằng **1** khi ít nhất hai trong ba ngõ bằng **1**. Cùng biểu thức xuất hiện như bit mang ra $$C_{out}$$ của full adder.

![Majority](/discrete-mathematics-for-computer-science-iuh/img/course/Majority_circuit.svg)

<p class="textbook-figure-caption" data-figure="13.30f">Mạng majority $$xy+xz+yz$$.</p>

**Half adder** (bộ nửa cộng) nhận hai bit $$x,y$$ và sinh tổng $$s$$ cùng mang $$c$$, không có mang vào:

| $$x$$ | $$y$$ | $$s$$ | $$c$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$$
s = \bar x y + x \bar y = x \oplus y,\qquad
c = x y.
$$

![Half adder](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.31">Half adder: $$s = x \oplus y$$, $$c = xy$$.</p>

**Full adder** (bộ cộng đầy đủ) nhận thêm $$C_{in}$$: $$S = x \oplus y \oplus C_{in}$$ và $$C_{out}$$ là majority của ba bit. Ghép half adder với hai full adder cho phép cộng hai số ba bit theo kiểu lan truyền mang (*ripple-carry*); chi tiết và các khối liên quan ở Mục 13.7.

![Cộng 3-bit HA+FA+FA](/discrete-mathematics-for-computer-science-iuh/img/course/Ripple_3bit_HA_FA.svg)

<p class="textbook-figure-caption" data-figure="13.31b">Cấu trúc cộng ba bit: half adder ở bit thấp, full adder ở các bit cao hơn.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** Hiện thực $$s = \bar x y + x \bar y$$ bằng AND/OR/NOT cần khoảng năm cổng; nếu dùng XOR có sẵn thì chỉ cần một XOR và một AND cho cặp $$(s,c)$$ của half adder. Cùng bảng chân trị có thể tương ứng nhiều sơ đồ khác nhau về số cổng.

</div>

### 2.4. Vai trò của tối thiểu hóa

Hai biểu thức cùng bảng chân trị:

$$
f_1 = xy + x\bar y + \bar x y,\qquad
f_2 = x + y.
$$

| | $$f_1$$ | $$f_2$$ |
|:---|:---:|:---:|
| AND 2-ngõ (ước lượng) | 3 | 0 |
| OR 2-ngõ | 2 | 1 |
| NOT | 2 | 0 |
| Tổng cổng thô | **7** | **1** |

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = xyz + x\bar y z$$ bằng **1** tại $$111$$ và $$101$$.  
Dạng SOP chưa rút gọn cần hai AND ba ngõ, một OR và một NOT. Sau rút gọn:

$$
F = xz(y+\bar y) = xz,
$$

chỉ còn một AND hai ngõ.

</div>

![Hai cách sau rút gọn](/discrete-mathematics-for-computer-science-iuh/img/course/Minimize_two_ways.svg)

<p class="textbook-figure-caption" data-figure="13.31c">Hai hiện thực của cùng hàm: $$xyz + x\bar y z$$ và $$xz$$.</p>

Ít cổng hơn thường đồng nghĩa với sơ đồ đơn giản hơn và, trên phần cứng, ít linh kiện hơn cũng như đường trễ ngắn hơn. K-map và Quine–McCluskey cung cấp quy trình có hệ thống để chuyển từ dạng như $$f_1$$ sang dạng như $$f_2$$.

Về mặt thư viện cổng, NAND (và NOR) là tập đầy đủ: mọi hàm Boolean đều hiện thực được chỉ bằng một loại cổng (Sheffer / Peirce; Mục 13.1, 13.3). Thông thường nên rút gọn biểu thức trước, rồi mới ánh xạ sang NAND hoặc NOR.

## 3. Các mức phương pháp tối thiểu hóa

| Phương pháp | Phạm vi điển hình | Đặc trưng |
|:---|:---|:---|
| Đại số (13.3) | Ít biến | Nhanh khi cấu trúc biểu thức rõ |
| K-map (13.4) | 2–4 biến | Trực quan trên lưới |
| Quine–McCluskey (13.5) | Nhiều biến hơn | Bảng, thuật toán hóa được |
| Phần mềm hỗ trợ | Quy mô lớn | Cùng khung hạng nguyên tố và phủ |

![Bản đồ Karnaugh](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

<p class="textbook-figure-caption" data-figure="13.32">Bản đồ Karnaugh cho hàm số biến nhỏ.</p>

![Quine–McCluskey](/discrete-mathematics-for-computer-science-iuh/img/course/quine_mccluskey.svg)

<p class="textbook-figure-caption" data-figure="13.33">Quine–McCluskey: rút gọn bằng bảng.</p>

<div class="textbook-definition" markdown="1">

**Thông điệp của Chương 13.** Ba hướng rút gọn hàm Boolean bổ sung cho nhau ở các mức độ khác nhau. **Bản đồ Karnaugh (K-map)** rèn luyện khả năng nhận biết các nhóm có thể gộp trên lưới; **thuật toán Quine–McCluskey** cung cấp quy trình rút gọn có hệ thống, thực hiện được bằng máy tính; **các công cụ phần mềm** mở rộng cùng tư duy đó cho mạch có nhiều biến và quy mô lớn. Dù khác nhau về cách tiếp cận và phạm vi áp dụng, cả ba đều dựa trên nền tảng **đại số Boole**.

</div>

## 4. SAT và kiểm chứng logic

### 4.1. Bài toán SAT

<div class="textbook-definition" markdown="1">

**SAT** (*Boolean satisfiability*): cho một công thức logic, thường ở dạng CNF (tích các tuyển), hỏi có tồn tại phép gán **0**/**1** cho các biến sao cho toàn công thức bằng **1** hay không.

</div>

SAT là bài toán NP-đầy đủ kinh điển; đồng thời, các bộ giải thực tế vẫn xử lý được nhiều công thức có kích thước lớn.

### 4.2. Kiểm tra tương đương hai mạch

Cho hai mạch tổ hợp $$f$$ và $$g$$ cùng số ngõ vào, mỗi mạch một ngõ ra. Câu hỏi tương đương hành vi tương đương với:

> Có tồn tại đầu vào sao cho $$f \neq g$$ không?  
> Tức là công thức $$f \oplus g$$ có thỏa được (bằng **1**) hay không?

- Nếu không tồn tại đầu vào làm $$f \oplus g = 1$$ thì $$f$$ và $$g$$ tương đương.  
- Nếu tồn tại, vector tìm được là phản chứng.

Như vậy, mạng cổng **tính** hàm Boolean, còn SAT **tìm kiếm** trong không gian gán biến — hai vai trò khác nhau trên cùng nền đại số Boole.

![Cây tìm kiếm](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="13.34">Minh họa tìm kiếm theo nhánh gán biến trong không gian Boolean.</p>

### 4.3. Liên hệ với CNF / POS

Nhiều bộ giải SAT nhận đầu vào dạng CNF. Dạng POS (tích các tổng) / CNF ở Mục 13.2 vì vậy gắn trực tiếp với ngôn ngữ đặc tả ràng buộc cho kiểm chứng.

<div class="textbook-example" markdown="1">

**Ví dụ.** Ràng buộc “không bật đồng thời ghi và xóa” viết $$\lnot(w \land e)$$, tương đương $$\bar w \lor \bar e$$. Tập hợp nhiều mệnh đề kiểu này tạo thành một CNF.

</div>

## 5. FPGA và LUT

Hai hướng hiện thực mạch số có thể đối chiếu như sau:

| | **ASIC** | **FPGA** |
|:---|:---|:---|
| Sau chế tạo | Logic cố định | Cấu hình lại bằng bitstream |
| Ưu điểm | Mật độ và hiệu năng cao | Linh hoạt, chu kỳ thử nhanh |
| Liên hệ Boole | Mạng cổng cố định | Mỗi **LUT** $$k$$ ngõ ≈ bảng chân trị $$k$$ biến |

**LUT** (*lookup table*) lưu cột đầu ra của bảng chân trị. Về mặt toán học, đây chính là đối tượng hàm Boolean đã xét ở Mục 13.2; khác biệt chỉ là bảng nằm trong bộ nhớ cấu hình. Số LUT cần dùng phụ thuộc số biến và số hàm; rút gọn biểu thức trước khi ánh xạ vẫn làm giảm độ phức tạp cấu hình.

## 6. Tổng kết cấu trúc chương

| Mục | Nội dung chính |
|:---|:---|
| 13.1 | Đại số $$+, \cdot, '$$ |
| 13.2 | Hàm, SOP / POS |
| 13.3 | Cổng, tối thiểu hóa đại số, NAND/NOR đầy đủ |
| 13.4 | K-map |
| 13.5 | Quine–McCluskey |
| **13.6** | Lịch sử, thiết kế tổ hợp, silicon, SAT, FPGA |
| 13.7 | Half/full adder, ripple, nhân, MUX, decoder |

<div class="textbook-definition" markdown="1">

**Kết luận.** Máy tính số thực hiện các ánh xạ $$\{0,1\}^n \to \{0,1\}^m$$ trên mức điện áp. Đại số Boole là toán học của các ánh xạ đó — từ mạng công tắc đến LUT trên FPGA.

</div>

## Bài tập

### Bài tập 1

Nêu tương ứng Shannon cho: (a) $$x \cdot y$$, (b) $$x + y$$, (c) $$x'$$. Giải thích vì sao AND tương ứng nối tiếp.

<details>
<summary>Đáp án</summary>

(a) Hai switch nối tiếp — chỉ dẫn khi cả hai đóng.  
(b) Song song — dẫn khi ít nhất một đóng.  
(c) Tiếp điểm đảo.  
AND = nối tiếp vì *cả hai* điều kiện đóng phải thỏa đồng thời.

</details>

### Bài tập 2

Cho $$f = ab + a\bar b$$.

1. Chứng minh $$f = a$$.  
2. Ước lượng số cổng AND/OR/NOT của $$ab + a\bar b$$ so với hiện thực chỉ bằng $$a$$.  
3. Nêu một hệ quả về tối thiểu hóa.

<details>
<summary>Đáp án</summary>

1. $$ab + a\bar b = a(b + \bar b) = a$$.  
2. Dạng dài ≈ 1 NOT + 2 AND + 1 OR; dạng rút: 0 cổng.  
3. Biểu thức tương đương có thể khác nhau **rất xa** về số cổng.

</details>

### Bài tập 3

Với hàm ba công tắc–đèn ở Mục 2.2: lập bảng tám dòng, viết SOP chuẩn và dạng có XNOR; so sánh số khối (đếm XNOR như một cổng).

<details>
<summary>Đáp án</summary>

$$Y(0,0,0)=Y(1,1,0)=1$$; $$Y=\bar A\bar B\bar C+AB\bar C=\bar C(A\odot B)$$.  
SOP thô: 2 AND 3-ngõ + 1 OR + 3 NOT; dạng XNOR: 1 XNOR + 1 NOT + 1 AND.

</details>

### Bài tập 4

1. Từ bảng half adder, viết SOP cho $$s$$ và $$c$$; mô tả mạng cổng khi được dùng XOR.  
2. Viết majority ba biến dạng SOP và liên hệ với $$C_{out}$$ của full adder.

<details>
<summary>Đáp án</summary>

1. $$s=\bar x y+x\bar y$$ hoặc $$x\oplus y$$; $$c=xy$$; có XOR: 1 XOR + 1 AND.  
2. $$xy+xz+yz$$ = majority = $$C_{out}$$ khi ba ngõ là $$A,B,C_{in}$$.

</details>

### Bài tập 5

$$F=xyz+x\bar y z$$. Rút gọn và so sánh số cổng của SOP ban đầu với dạng rút gọn (không dùng XOR).

<details>
<summary>Đáp án</summary>

$$F=xz$$. Thô ≈ 2 AND 3-ngõ + 1 OR + 1 NOT; rút ≈ 1 AND 2-ngõ.

</details>

### Bài tập 6

Với hàm ba biến, phương pháp tối thiểu hóa nào thường phù hợp? Với hàm mười hai biến, vì sao K-map không còn thực tế?

<details>
<summary>Đáp án</summary>

Ba biến: K-map hoặc biến đổi đại số.  
Mười hai biến: $$2^{12}=4096$$ minterm; lưới tay không khả thi — dùng Quine–McCluskey hoặc phần mềm.

</details>

### Bài tập 7

Giải thích cách dùng SAT để kiểm tra hai mạch một ngõ ra $$f$$ và $$g$$ có tương đương hay không. Gợi ý: xét $$f\oplus g$$.

<details>
<summary>Đáp án</summary>

Hỏi có đầu vào làm $$f\neq g$$ không, tức $$f\oplus g=1$$.  
Không thỏa được → $$f\equiv g$$; thỏa được → model là phản chứng.

</details>

### Bài tập 8

Một LUT bốn ngõ lưu bao nhiêu bit cấu hình cho một hàm Boolean bốn biến tùy ý? Liên hệ với bảng chân trị.

<details>
<summary>Đáp án</summary>

$$2^4=16$$ dòng bảng → **16 bit** cho mỗi LUT bốn ngõ (chưa kể định tuyến).

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=zPNdj_Qth_Q">How transistors work</a>
- <a href="https://www.youtube.com/watch?v=dJsguV1PaPQ">Karnaugh maps</a>
- Mục 13.3 — cổng và tối thiểu hóa đại số  
- Mục 13.7 — full adder, ripple, MUX, decoder  

## Tóm tắt

1. Boole xây dựng đại số logic; Shannon ánh xạ đại số đó lên mạch chuyển mạch (nối tiếp–AND, song song–OR).  
2. Quy trình năm bước: biến, bảng chân trị, biểu thức, rút gọn, mạng cổng.  
3. Cùng hành vi có thể mô tả bằng bảng, biểu thức, sơ đồ cổng và hiện thực vật lý (silicon, LUT).  
4. Tối thiểu hóa làm giảm số cổng; NAND và NOR là tập đầy đủ.  
5. SAT phục vụ kiểm tra tương đương; FPGA/LUT hiện thực bảng chân trị có cấu hình.

Đại số Boole vì vậy là sợi liên tục từ mô hình công tắc đến các khối trên chip.
