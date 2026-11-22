---
layout: post
title: "Đại số Boole: Từ Boole đến Chip Hiện đại"
categories: chapter13
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Tổng hợp Chương 13: từ đại số Boole và mạng công tắc của Shannon đến quy trình năm bước thiết kế mạch tổ hợp, mối liên hệ giữa rút gọn biểu thức và số cổng, bộ giải SAT và FPGA/LUT."
---

<div class="textbook-epigraph" markdown="1">

"It has been found that the symbolism of Algebra is capable of indicating… the laws of those mental operations which are involved in reasoning."

<span class="epigraph-attribution">— George Boole, *An Investigation of the Laws of Thought* (1854)</span>

</div>

Các mục 13.1–13.5 đã lần lượt trình bày đại số Boole, hàm và dạng chuẩn, cổng logic cùng các phương pháp tối thiểu hóa. Mục này kết nối các công cụ đó trong một bức tranh thống nhất: từ hệ ký hiệu logic thế kỷ XIX, đại số Boole đã trở thành ngôn ngữ mô tả và tối ưu hóa **mạch số**. Mỗi bước rút gọn biểu thức không chỉ làm công thức ngắn hơn trên giấy mà còn giúp giảm số cổng, rút ngắn độ trễ tín hiệu và hỗ trợ kiểm chứng thiết kế.

| Giai đoạn | Nội dung | Mục |
|:---:|:---|:---|
| 1 | Đại số Boole | 13.1 |
| 2 | Hàm Boole, bảng chân trị, SOP / POS | 13.2 |
| 3 | Cổng logic và tối thiểu hóa đại số | 13.3 |
| 4 | K-map và Quine–McCluskey | 13.4–13.5 |
| 5 | Bối cảnh lịch sử và ứng dụng | **13.6** |
| 6 | Mạch cộng, MUX, decoder | 13.7 |

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tóm tắt** đóng góp của George Boole và Claude Shannon, đồng thời liên hệ công tắc nối tiếp/song song với phép AND/OR.
- **Mô tả** quy trình năm bước thiết kế mạch tổ hợp từ yêu cầu đến mạng cổng.
- **Phân tích** các ví dụ mạch tổ hợp tiêu biểu: ba công tắc–đèn, hàm đa số (majority), half adder và full adder.
- **Giải thích** mối liên hệ giữa việc rút gọn biểu thức và số lượng cổng logic.
- **Liên hệ** bài toán SAT với kiểm tra tương đương mạch và mô tả FPGA/LUT như bảng chân trị có thể cấu hình.

**Từ khóa**: đại số Boole, Claude Shannon, mạng công tắc, thiết kế tổ hợp, tối thiểu hóa, half/full adder, SAT, FPGA, LUT.

</div>

## Hai bước ngoặt lịch sử: Boole và Shannon

### George Boole — đại số hóa suy luận

George Boole (1815–1864) không thiết kế máy tính. Trong tác phẩm *The Laws of Thought* (1854), ông mô tả các phép suy luận trên mệnh đề bằng ký hiệu đại số — cộng, nhân và bù — tuân theo những quy luật riêng như $$1 + 1 = 1$$ trong ngữ cảnh logic.

Đóng góp cốt lõi của ông đối với khoa học máy tính là cho thấy suy luận có thể viết thành **biểu thức hình thức** và biến đổi theo quy tắc đại số, thay vì chỉ diễn đạt bằng ngôn ngữ tự nhiên.

![George Boole](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="13.26">George Boole (1815–1864), người đặt nền móng đại số cho logic.</p>

### Claude Shannon — nối đại số Boole với mạch chuyển mạch

Năm **1937**, luận văn thạc sĩ của Claude Shannon thiết lập mối tương ứng chính xác giữa đại số Boole và mạch chuyển mạch điện:

| Đại số Boole | Mạch chuyển mạch (rơ-le / công tắc) |
|:---|:---|
| **0** / **1** | hở / đóng (hoặc hai mức điện áp) |
| AND | **mắc nối tiếp**: mạch chỉ dẫn khi mọi công tắc đều đóng |
| OR | **mắc song song**: mạch dẫn khi ít nhất một công tắc đóng |
| NOT | tiếp điểm đảo (bù) |

![Nối tiếp và song song](/discrete-mathematics-for-computer-science-iuh/img/course/Switch_series_parallel.svg)

<p class="textbook-figure-caption" data-figure="13.27a">Mắc nối tiếp tương ứng phép AND; mắc song song tương ứng phép OR.</p>

Nhờ sự tương ứng này, một biểu thức Boole vừa mô tả suy luận logic vừa mô tả cấu trúc một mạng công tắc, giúp việc thiết kế mạch số dựa trên biến đổi đại số có hệ thống thay vì thử–sai thủ công.

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét mạch có nhánh trên gồm $$x$$ nối tiếp với $$(y$$ song song $$z)$$, nhánh dưới gồm $$\bar z$$ nối tiếp $$\bar x$$; hai nhánh mắc song song với nhau rồi nối tiếp với $$t$$. Hàm dẫn điện của mạch là:

$$
f(x,y,z,t)=\bigl[x(y+z)+\bar z\,\bar x\bigr]t = xyt + xzt + \bar x\,\bar z\, t.
$$

Biểu thức sau khai triển đã ở dạng **SOP** (tổng các tích), có thể hiện thực bằng mạng AND–OR–NOT hoặc ánh xạ sang LUT.

</div>

![Claude Shannon](/discrete-mathematics-for-computer-science-iuh/img/course/ClaudeShannon_MFO3807.jpg)

<p class="textbook-figure-caption" data-figure="13.27">Claude Shannon (1916–2001), người ánh xạ đại số Boole lên mạch chuyển mạch rơ-le năm 1937.</p>

<div class="textbook-definition" markdown="1">

**Phân biệt các mốc lịch sử.** Boole (thế kỷ XIX) xây dựng đại số logic; Shannon (1937) ánh xạ đại số đó lên mạch điện; transistor và mạch tích hợp về sau là **công nghệ hiện thực vật lý** cho các cổng logic, trong khi cơ sở toán học vẫn là đại số Boole.

</div>

<div class="textbook-definition" markdown="1">

**Mạch và cổng.**  
- *Mạch chuyển mạch* gồm công tắc và dây dẫn, chỉ xét hai trạng thái có hoặc không có dòng điện.  
- Mỗi **công tắc** tương ứng với một **biến Boole**.  
- **Cổng logic** là phần tử có một hoặc nhiều ngõ vào và một ngõ ra tuân theo bảng chân trị cố định (AND, OR, NOT, NAND, NOR, XOR, XNOR; xem mục 13.3).

</div>

## Từ yêu cầu đến mạng cổng

Một chức năng số — chẳng hạn phép cộng hai bit — có thể được mô tả ở bốn tầng **tương đương về hành vi**:

| Tầng | Nội dung | Ví dụ cộng một bit |
|:---|:---|:---|
| 1. Bảng chân trị | Ánh xạ đầu vào → đầu ra | $$(1,1)\mapsto (c,s)=(1,0)$$ |
| 2. Biểu thức Boole | Dạng SOP / POS | $$s=x\oplus y$$, $$c=xy$$ |
| 3. Mạng cổng | Sơ đồ AND/OR/NOT/XOR | 1 cổng XOR + 1 cổng AND |
| 4. Hiện thực vật lý | Linh kiện rời hoặc FPGA | transistor, LUT |

![Bảng chân trị](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.28">Bảng chân trị đặc tả hành vi đầy đủ trước khi viết biểu thức hay vẽ sơ đồ cổng.</p>

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.29">Cổng AND.</p>

![Cổng OR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_OR.svg)

<p class="textbook-figure-caption" data-figure="13.29b">Cổng OR.</p>

![Cổng NOT](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.29c">Cổng NOT.</p>

![Transistor CMOS (mô hình)](/discrete-mathematics-for-computer-science-iuh/img/course/transistor.svg)

<p class="textbook-figure-caption" data-figure="13.30">Transistor là linh kiện vật lý cơ bản cấu thành cổng logic trên chip silicon.</p>

### Quy trình thiết kế năm bước

Quá trình chuyển từ đặc tả bằng lời sang mạng cổng (và tiếp đến chip silicon hoặc FPGA) gồm năm bước chuẩn:

| Bước | Nội dung |
|:---:|:---|
| 1 | Đặt tên biến đầu vào/đầu ra và quy ước ý nghĩa **0**/**1** |
| 2 | Lập bảng chân trị đầy đủ |
| 3 | Viết biểu thức Boole (thường ở dạng SOP từ các dòng $$Y=1$$) |
| 4 | Rút gọn biểu thức bằng đại số, K-map hoặc Quine–McCluskey |
| 5 | Vẽ mạng cổng và đánh giá số cổng, số tầng trễ |

![Bước 1 — Đặt biến](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_1.svg)

<p class="textbook-figure-caption" data-figure="13.30a">Bước 1: đặt biến và quy ước giá trị 0–1.</p>

![Bước 5 — Vẽ mạch](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_5.svg)

<p class="textbook-figure-caption" data-figure="13.30b">Bước 5: chuyển biểu thức đã rút gọn thành mạng cổng logic.</p>

Hai kỹ năng ngược chiều luôn bổ trợ nhau: đọc sơ đồ mạch để suy ra biểu thức, và từ biểu thức dựng nên sơ đồ mạch. Ví dụ đọc biểu thức từ sơ đồ:

$$
Y = (\bar A + B)(A + B + C)\bar C.
$$

![Đọc mạch ra biểu thức](/discrete-mathematics-for-computer-science-iuh/img/course/Circuit_to_expression.svg)

<p class="textbook-figure-caption" data-figure="13.30c">Gán nhãn đầu ra từng tầng cổng để suy ra biểu thức tổng của mạch.</p>

### Ví dụ: ba công tắc và đèn

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét ba công tắc $$A,B,C$$ điều khiển một bóng đèn $$Y$$: đèn sáng khi cả ba công tắc đều hở, hoặc khi công tắc 1 và 2 đóng còn công tắc 3 hở. Quy ước đóng = **1**, hở = **0** và đèn sáng = **1**.

Ta có $$Y=1$$ chỉ tại hai tổ hợp $$(0,0,0)$$ và $$(1,1,0)$$, nên:

$$
Y = \bar A\bar B\bar C + AB\bar C = \bar C\,(\bar A\bar B + AB) = \bar C\,(A \odot B),
$$

trong đó $$A \odot B$$ là phép **XNOR**. Mạch rút gọn chỉ cần một cổng XNOR, một cổng NOT và một cổng AND.

</div>

![Bảng ba công tắc](/discrete-mathematics-for-computer-science-iuh/img/course/Three_switch_truth_table.svg)

<p class="textbook-figure-caption" data-figure="13.30d">Bảng chân trị của mạch ba công tắc–đèn.</p>

![Mạch ba công tắc–đèn](/discrete-mathematics-for-computer-science-iuh/img/course/Three_switch_lamp.svg)

<p class="textbook-figure-caption" data-figure="13.30e">Sơ đồ mạng cổng cho $$Y=\bar C(A\odot B)$$.</p>

### Majority và half / full adder

Hàm **đa số** (majority) ba biến $$f = xy + xz + yz$$ nhận giá trị **1** khi có ít nhất hai trong ba ngõ vào bằng **1**. Chính biểu thức này là bit nhớ ra $$C_{out}$$ của bộ cộng đầy đủ (full adder).

![Majority](/discrete-mathematics-for-computer-science-iuh/img/course/Majority_circuit.svg)

<p class="textbook-figure-caption" data-figure="13.30f">Mạng cổng cho hàm đa số $$xy+xz+yz$$.</p>

**Half adder** (bộ nửa cộng) cộng hai bit $$x,y$$ (không có bit nhớ vào) để tạo ra bit tổng $$s$$ và bit nhớ $$c$$:

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

<p class="textbook-figure-caption" data-figure="13.31">Half adder với $$s = x \oplus y$$ và $$c = xy$$.</p>

**Full adder** (bộ cộng đầy đủ) nhận thêm bit nhớ vào $$C_{in}$$, cho $$S = x \oplus y \oplus C_{in}$$ và $$C_{out}$$ là hàm đa số của ba bit. Khi ghép một half adder với hai full adder, ta thu được bộ cộng hai số 3-bit theo cơ chế lan truyền nhớ (*ripple-carry*); chi tiết được trình bày ở Mục 13.7.

![Cộng 3-bit HA+FA+FA](/discrete-mathematics-for-computer-science-iuh/img/course/Ripple_3bit_HA_FA.svg)

<p class="textbook-figure-caption" data-figure="13.31b">Mạch cộng 3 bit: dùng half adder ở bit thấp nhất và full adder cho các bit cao hơn.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** Nếu hiện thực $$s = \bar x y + x \bar y$$ chỉ bằng cổng AND, OR và NOT thì cần 5 cổng; nhưng nếu dùng sẵn cổng XOR thì toàn bộ half adder cho cặp $$(s,c)$$ chỉ cần 1 cổng XOR và 1 cổng AND. Cùng một bảng chân trị có thể tương ứng nhiều sơ đồ với số cổng khác nhau.

</div>

### Vai trò của tối thiểu hóa

Xét hai biểu thức có cùng bảng chân trị:

$$
f_1 = xy + x\bar y + \bar x y,\qquad
f_2 = x + y.
$$

| Loại cổng | $$f_1$$ | $$f_2$$ |
|:---|:---:|:---:|
| AND 2 ngõ vào (ước lượng) | 3 | 0 |
| OR 2 ngõ vào | 2 | 1 |
| NOT | 2 | 0 |
| Tổng số cổng thô | **7** | **1** |

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét $$F = xyz + x\bar y z$$ (bằng **1** tại $$111$$ và $$101$$). Dạng chưa rút gọn cần hai cổng AND 3 ngõ vào, một cổng OR và một cổng NOT. Sau khi rút gọn:

$$
F = xz(y+\bar y) = xz,
$$

mạch chỉ còn duy nhất một cổng AND 2 ngõ vào.

</div>

![Hai cách sau rút gọn](/discrete-mathematics-for-computer-science-iuh/img/course/Minimize_two_ways.svg)

<p class="textbook-figure-caption" data-figure="13.31c">So sánh hai hiện thực của cùng một hàm: $$xyz + x\bar y z$$ và $$xz$$.</p>

Số cổng ít hơn thường kéo theo sơ đồ đơn giản hơn, ít linh kiện hơn và độ trễ lan truyền tín hiệu nhỏ hơn trên phần cứng. K-map và Quine–McCluskey cung cấp quy trình có hệ thống để rút gọn biểu thức từ dạng như $$f_1$$ sang $$f_2$$.

Trong thư viện phần cứng, NAND và NOR đều là tập cổng đầy đủ (Mục 13.1, 13.3): ta thường rút gọn biểu thức trước rồi mới chuyển đổi sang mạng chỉ gồm cổng NAND hoặc chỉ gồm cổng NOR.

## Các mức phương pháp tối thiểu hóa

| Phương pháp | Phạm vi phù hợp | Đặc trưng |
|:---|:---|:---|
| Biến đổi đại số (13.3) | Ít biến | Nhanh khi cấu trúc biểu thức rõ ràng |
| Bản đồ Karnaugh (13.4) | 2–4 biến | Trực quan trên lưới |
| Quine–McCluskey (13.5) | Nhiều biến hơn | Dạng bảng, dễ thuật toán hóa |
| Công cụ phần mềm EDA | Quy mô lớn | Mở rộng cùng khung hạng nguyên tố và phủ |

![Bản đồ Karnaugh](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

<p class="textbook-figure-caption" data-figure="13.32">Bản đồ Karnaugh dùng cho hàm có số biến nhỏ.</p>

![Quine–McCluskey](/discrete-mathematics-for-computer-science-iuh/img/course/quine_mccluskey.svg)

<p class="textbook-figure-caption" data-figure="13.33">Phương pháp bảng Quine–McCluskey.</p>

<div class="textbook-definition" markdown="1">

**Thông điệp của Chương 13.** Các phương pháp rút gọn hàm Boole bổ trợ cho nhau theo quy mô bài toán: **bản đồ Karnaugh (K-map)** giúp nhận diện trực quan các nhóm gộp; **Quine–McCluskey** chuẩn hóa quy trình thành thuật toán bảng; còn **các công cụ phần mềm** mở rộng cùng nguyên lý cho mạch nhiều biến. Tất cả đều dựa trên nền tảng chung là **đại số Boole**.

</div>

## SAT và kiểm chứng logic

### Bài toán SAT

<div class="textbook-definition" markdown="1">

**SAT** (*Boolean satisfiability*): cho một công thức logic (thường viết ở dạng chuẩn hội CNF — tích các tuyển), hỏi có tồn tại một phép gán giá trị **0**/**1** cho các biến sao cho toàn bộ công thức nhận giá trị **1** hay không.

</div>

SAT là bài toán NP-đầy đủ kinh điển, nhưng các bộ giải hiện đại vẫn xử lý hiệu quả nhiều công thức quy mô lớn trong thực tế công nghiệp.

### Kiểm tra tương đương hai mạch

Cho hai mạch tổ hợp $$f$$ và $$g$$ có cùng tập ngõ vào và mỗi mạch một ngõ ra. Bài toán kiểm tra xem hai mạch có tương đương hành vi hay không được quy về câu hỏi:

> Có tồn tại tổ hợp đầu vào nào làm $$f \neq g$$ (tức $$f \oplus g = 1$$) hay không?

- Nếu công thức $$f \oplus g$$ **không thỏa được** (UNSAT), hai mạch $$f$$ và $$g$$ tương đương nhau trên mọi đầu vào.  
- Nếu **thỏa được** (SAT), phép gán tìm được chính là phản chứng chỉ ra nơi hai mạch khác nhau.

Như vậy, mạng cổng thực hiện việc **tính** giá trị hàm Boole, còn bộ giải SAT thực hiện việc **tìm kiếm** trong không gian gán biến — hai ứng dụng bổ sung nhau trên cùng nền tảng đại số Boole.

![Cây tìm kiếm](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="13.34">Minh họa cây tìm kiếm theo các nhánh gán giá trị biến trong không gian Boole.</p>

### Liên hệ với CNF / POS

Phần lớn bộ giải SAT nhận đầu vào ở dạng CNF. Vì vậy, dạng POS (tích các tổng) ở Mục 13.2 gắn trực tiếp với ngôn ngữ mô tả ràng buộc trong kiểm chứng tự động.

<div class="textbook-example" markdown="1">

**Ví dụ.** Ràng buộc “không cho phép bật đồng thời tín hiệu ghi $$w$$ và xóa $$e$$” được viết là $$\lnot(w \land e)$$, tương đương $$\bar w \lor \bar e$$. Kết hợp nhiều mệnh đề ràng buộc như vậy tạo thành một công thức CNF.

</div>

## FPGA và LUT

Hai hướng hiện thực mạch số phổ biến có thể so sánh như sau:

| Tiêu chí | **ASIC** | **FPGA** |
|:---|:---|:---|
| Sau chế tạo | Cấu trúc logic cố định | Có thể cấu hình lại bằng bitstream |
| Ưu điểm | Mật độ tích hợp và hiệu năng cao | Linh hoạt, chu kỳ thử nghiệm nhanh |
| Liên hệ đại số Boole | Mạng cổng cố định | Mỗi **LUT** $$k$$ ngõ vào tương ứng một bảng chân trị $$k$$ biến |

**LUT** (*lookup table*) lưu trực tiếp cột giá trị đầu ra của bảng chân trị trong bộ nhớ cấu hình. Về mặt toán học, đó chính là hàm Boole ở Mục 13.2; việc rút gọn biểu thức trước khi ánh xạ vẫn giúp giảm số LUT và tài nguyên định tuyến cần dùng.

## Tổng kết cấu trúc chương

| Mục | Nội dung chính |
|:---|:---|
| 13.1 | Đại số Boole với $$+, \cdot, '$$ |
| 13.2 | Hàm Boole, dạng SOP và POS |
| 13.3 | Cổng logic, tối thiểu hóa đại số, tính đầy đủ của NAND/NOR |
| 13.4 | Bản đồ Karnaugh (K-map) |
| 13.5 | Phương pháp Quine–McCluskey |
| **13.6** | Bối cảnh lịch sử, thiết kế tổ hợp, silicon, SAT và FPGA |
| 13.7 | Half/full adder, bộ cộng ripple-carry, mạch nhân, MUX và decoder |

<div class="textbook-definition" markdown="1">

**Kết luận.** Máy tính số thực thi các ánh xạ $$\{0,1\}^n \to \{0,1\}^m$$ trên các mức điện áp, và đại số Boole là cơ sở toán học xuyên suốt từ mạng công tắc cho đến các khối LUT trên FPGA.

</div>

## Bài tập

### Bài tập 1

Nêu quy tắc tương ứng của Shannon cho: (a) $$x \cdot y$$, (b) $$x + y$$, (c) $$x'$$. Giải thích vì sao phép AND tương ứng với cách mắc nối tiếp.

<details>
<summary>Đáp án</summary>

(a) Hai công tắc mắc nối tiếp: mạch chỉ dẫn điện khi cả hai công tắc đều đóng.  
(b) Hai công tắc mắc song song: mạch dẫn điện khi có ít nhất một công tắc đóng.  
(c) Tiếp điểm đảo (thường đóng).  
Phép AND tương ứng mắc nối tiếp vì *cả hai* điều kiện đóng mạch phải thỏa mãn đồng thời.

</details>

### Bài tập 2

Cho $$f = ab + a\bar b$$.

1. Chứng minh $$f = a$$.  
2. So sánh số cổng AND/OR/NOT cần thiết cho $$ab + a\bar b$$ và cho $$a$$.  
3. Nêu ý nghĩa của kết quả này đối với tối thiểu hóa mạch.

<details>
<summary>Đáp án</summary>

1. $$ab + a\bar b = a(b + \bar b) = a \cdot 1 = a$$.  
2. Dạng chưa rút gọn cần khoảng 1 NOT, 2 AND và 1 OR (4 cổng); dạng rút gọn $$f = a$$ không cần cổng nào (nối dây trực tiếp).  
3. Hai biểu thức tương đương về mặt logic có thể chênh lệch rất lớn về chi phí phần cứng.

</details>

### Bài tập 3

Với bài toán ba công tắc–đèn ở phần *Ví dụ: ba công tắc và đèn*: lập bảng chân trị 8 dòng, viết dạng SOP chuẩn và dạng dùng XNOR, sau đó so sánh số cổng (coi XNOR là một cổng).

<details>
<summary>Đáp án</summary>

$$Y(0,0,0)=Y(1,1,0)=1$$, nên $$Y=\bar A\bar B\bar C+AB\bar C=\bar C(A\odot B)$$.  
Dạng SOP chuẩn cần 2 cổng AND 3 ngõ vào, 1 cổng OR và 3 cổng NOT; dạng dùng XNOR chỉ cần 1 cổng XNOR, 1 cổng NOT và 1 cổng AND.

</details>

### Bài tập 4

1. Từ bảng chân trị half adder, viết dạng SOP cho $$s$$ và $$c$$, đồng thời mô tả mạng cổng khi được dùng XOR.  
2. Viết hàm đa số (majority) ba biến ở dạng SOP và nêu liên hệ với $$C_{out}$$ của full adder.

<details>
<summary>Đáp án</summary>

1. $$s=\bar x y+x\bar y = x\oplus y$$ và $$c=xy$$; khi dùng cổng XOR, mạch gồm 1 cổng XOR và 1 cổng AND.  
2. Hàm đa số $$xy+xz+yz$$ chính là bit nhớ ra $$C_{out}$$ của full adder với ba ngõ vào $$A, B, C_{in}$$.

</details>

### Bài tập 5

Cho $$F=xyz+x\bar y z$$. Rút gọn biểu thức và so sánh số cổng giữa dạng SOP ban đầu và dạng rút gọn (không dùng XOR).

<details>
<summary>Đáp án</summary>

$$F=xz$$. Dạng ban đầu cần 2 cổng AND 3 ngõ vào, 1 cổng OR và 1 cổng NOT; dạng rút gọn chỉ cần 1 cổng AND 2 ngõ vào.

</details>

### Bài tập 6

Với hàm 3 biến, phương pháp tối thiểu hóa nào phù hợp? Với hàm 12 biến, vì sao K-map không còn khả thi?

<details>
<summary>Đáp án</summary>

Với 3 biến, có thể dùng K-map hoặc biến đổi đại số. Với 12 biến, bảng chân trị có tới $$2^{12}=4096$$ minterm nên không thể vẽ lưới bằng tay; khi đó cần dùng thuật toán Quine–McCluskey hoặc công cụ phần mềm chuyên dụng.

</details>

### Bài tập 7

Giải thích cách dùng bộ giải SAT để kiểm tra hai mạch tổ hợp một ngõ ra $$f$$ và $$g$$ có tương đương nhau hay không (gợi ý: xét biểu thức $$f\oplus g$$).

<details>
<summary>Đáp án</summary>

Đặt câu hỏi SAT xem có tồn tại đầu vào nào làm $$f \oplus g = 1$$ (tức $$f \neq g$$) hay không. Nếu bài toán không thỏa được (UNSAT) thì $$f \equiv g$$; nếu thỏa được (SAT) thì phép gán tìm được là phản chứng chứng tỏ hai mạch khác nhau.

</details>

### Bài tập 8

Một LUT 4 ngõ vào cần lưu bao nhiêu bit cấu hình để biểu diễn một hàm Boole 4 biến tùy ý? Giải thích mối liên hệ với bảng chân trị.

<details>
<summary>Đáp án</summary>

Bảng chân trị 4 biến có $$2^4=16$$ dòng, nên mỗi LUT 4 ngõ vào lưu đúng **16 bit** (ứng với cột giá trị đầu ra của bảng chân trị, chưa tính phần định tuyến).

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=zPNdj_Qth_Q">How transistors work</a>
- <a href="https://www.youtube.com/watch?v=dJsguV1PaPQ">Karnaugh maps</a>
- Mục 13.3 — cổng logic và tối thiểu hóa đại số  
- Mục 13.7 — full adder, bộ cộng ripple-carry, MUX và decoder  

## Tóm tắt

1. Boole xây dựng đại số logic; Shannon thiết lập tương ứng với mạch chuyển mạch (nối tiếp ứng với AND, song song ứng với OR).  
2. Quy trình thiết kế mạch tổ hợp gồm năm bước: đặt biến, lập bảng chân trị, viết biểu thức, rút gọn và vẽ mạng cổng.  
3. Một chức năng logic có thể biểu diễn tương đương qua bảng chân trị, biểu thức, sơ đồ cổng và hiện thực phần cứng (silicon, LUT).  
4. Tối thiểu hóa biểu thức giúp giảm số cổng và độ trễ; NAND và NOR đều là tập cổng đầy đủ.  
5. Bộ giải SAT hỗ trợ kiểm tra tương đương mạch, còn FPGA/LUT hiện thực trực tiếp bảng chân trị có thể cấu hình lại.

Đại số Boole là sợi dây xuyên suốt kết nối mô hình công tắc cổ điển với các vi mạch hiện đại.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=7ckEQ91E6F8">How George Boole and Claude Shannon Created Computer Circuits</a> — Hypatia Arduino Lab, tiếng Anh. Giới thiệu cách Boole và Shannon đưa đại số vào thiết kế mạch chuyển mạch.
- <a href="https://www.youtube.com/watch?v=aLUY-s7LSns">Half Adder</a> — Neso Academy, tiếng Anh. Minh họa mạch tổ hợp half adder.
- <a href="https://www.youtube.com/watch?v=fxpa4le_bXQ">FPGA Introduction Part 1 | LUT Basics and FPGA Building Blocks</a> — My Embedded School , tiếng Anh. Giải thích nguyên lý LUT trên FPGA khi hiện thực hàm Boole bằng bảng.
