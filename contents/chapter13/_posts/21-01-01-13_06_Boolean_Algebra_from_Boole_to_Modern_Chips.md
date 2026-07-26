---
layout: post
title: "Đại số Boole: Từ Boole đến Chip Hiện đại"
categories: chapter13
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Tổng hợp chương 13: từ Boole và Shannon đến cổng, tối thiểu hóa, kiểm chứng logic (SAT) và FPGA — giải thích thuật ngữ từng bước."
---

<div class="textbook-epigraph" markdown="1">

"It has been found that the symbolism of Algebra is capable of indicating… the laws of those mental operations which are involved in reasoning."

<span class="epigraph-attribution">— George Boole, *An Investigation of the Laws of Thought* (1854)</span>

</div>

Các bài 13.1–13.5 đã trang bị **công cụ kỹ thuật**: đại số Boole, hàm và dạng chuẩn, cổng logic, K-map, Quine–McCluskey. Bài tổng hợp này trả lời câu hỏi *vì sao những công cụ đó quan trọng*: một hệ ký hiệu thế kỷ XIX trở thành ngôn ngữ chung của mạch số, và mỗi lần rút gọn biểu thức có thể đổi thành **ít cổng hơn, dễ kiểm tra hơn**.

Sợi chỉ xuyên suốt chương:

| Bước | Nội dung | Bài |
|:---:|:---|:---|
| 1 | Đại số Boole (0/1, AND/OR/NOT) | 13.1 |
| 2 | Hàm, bảng, SOP / POS | 13.2 |
| 3 | Cổng và tối thiểu hóa đại số | 13.3 |
| 4 | K-map / Quine–McCluskey | 13.4–13.5 |
| 5 | Bối cảnh ứng dụng rộng | **bài này** |
| 6 | Mạch cộng, MUX, decoder | 13.7 |

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tóm tắt** vai trò của Boole và Shannon trong việc nối logic với mạch chuyển mạch.
- **Mô tả** lộ trình: yêu cầu → bảng chân trị → biểu thức → tối thiểu hóa → mạng cổng.
- **Giải thích** (định tính) vì sao rút gọn biểu thức làm giảm số cổng.
- **Liên hệ** CNF / bài toán SAT với việc kiểm tra hai mạch có cùng hành vi.
- **Nhận biết** FPGA/LUT như “bảng chân trị lập trình được”.

**Từ khóa**: đại số Boole, Claude Shannon, tối thiểu hóa, SAT, FPGA, LUT (lookup table).

</div>

## 1. Hai bước nhảy lịch sử: Boole và Shannon

### 1.1. George Boole — đại số hóa suy luận

George Boole (1815–1864) không thiết kế máy tính. Trong *The Laws of Thought* (1854), ông đề xuất thao tác mệnh đề / lớp bằng ký hiệu đại số — cộng, nhân, bù — với quy luật riêng (ví dụ $$1 + 1 = 1$$ trong ngữ cảnh logic).

Điểm then chốt với tin học sau này: suy luận được viết dưới dạng **biểu thức** có thể biến đổi theo quy tắc, không chỉ là câu tiếng Việt hay tiếng Anh.

![George Boole](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="13.26">George Boole (1815–1864) — đặt nền đại số cho logic.</p>

### 1.2. Claude Shannon — Boole khớp với mạch đóng/mở

Năm **1937**, luận văn thạc sĩ của Claude Shannon chỉ ra sự tương ứng:

| Logic / Boole | Mạch chuyển mạch (rơ-le) |
|:---|:---|
| **0** / **1** | hở / đóng (hoặc hai mức điện áp) |
| AND | nối tiếp |
| OR | song song |
| NOT | tiếp điểm đảo |

Đây là cú ghép quan trọng: **cùng một biểu thức** vừa mô tả suy luận vừa mô tả mạng công tắc. Từ đó, thiết kế mạch số có thể dùng biến đổi đại số thay vì chỉ thử–sai trên sơ đồ.

![Claude Shannon](/discrete-mathematics-for-computer-science-iuh/img/course/ClaudeShannon_MFO3807.jpg)

<p class="textbook-figure-caption" data-figure="13.27">Claude Shannon (1916–2001) — nối đại số Boole với mạch rơ-le (1937).</p>

<div class="textbook-definition" markdown="1">

**Không nhầm mốc.** Boole (thế kỷ XIX) = đại số logic. Shannon (1937) = **ánh xạ** đại số đó lên mạch điện. Transistor và mạch tích hợp sau này chỉ là **hiện thực vật lý** các cổng; khung logic vẫn là Boole.

</div>

## 2. Từ yêu cầu đến mạng cổng — bốn lớp cùng hành vi

Một chức năng số (ví dụ “cộng hai bit”) có thể mô tả ở nhiều lớp **cùng hành vi**:

| Lớp | Câu hỏi | Ví dụ “cộng 1 bit” |
|:---|:---|:---|
| 1. **Bảng chân trị** | Input nào → output nào? | $$(1,1)$$ → carry **1**, sum **0** |
| 2. **Biểu thức Boole** | Công thức SOP / POS? | $$s = x \oplus y$$, $$c = xy$$ |
| 3. **Mạng cổng** | Vẽ AND/OR/NOT/XOR thế nào? | 1 XOR + 1 AND |
| 4. **Hiện thực** | Linh kiện / chip ra sao? | transistor, hoặc LUT trên FPGA |

![Bảng chân trị — điểm xuất phát](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.28">Bảng chân trị — “hợp đồng” hành vi trước khi viết biểu thức hay vẽ cổng.</p>

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.29">Cổng AND — một khối chuẩn trên sơ đồ mạch.</p>

![Cổng OR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_OR.svg)

<p class="textbook-figure-caption" data-figure="13.29b">Cổng OR.</p>

![Cổng NOT](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.29c">Cổng NOT.</p>

![Transistor CMOS (mô hình)](/discrete-mathematics-for-computer-science-iuh/img/course/transistor.svg)

<p class="textbook-figure-caption" data-figure="13.30">Transistor là “gạch” silicon; mỗi cổng logic gồm vài đến hàng chục transistor tùy công nghệ.</p>

### 2.1. Ví dụ xuyên suốt: half adder

Hai bit $$x, y$$. Tổng $$s$$ và nhớ $$c$$:

| $$x$$ | $$y$$ | $$c$$ | $$s$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Dạng SOP (tổng các tích):

$$
s = \bar x y + x \bar y = x \oplus y,\qquad
c = x y.
$$

![Half adder](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.31">Half adder: $$s = x \oplus y$$, $$c = xy$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ (đếm cổng).**  
Hiện thực $$s = \bar x y + x \bar y$$ bằng AND/OR/NOT: khoảng 2 NOT + 2 AND + 1 OR = **5 cổng**.  
Nếu được dùng cổng XOR có sẵn: **1 XOR + 1 AND**.  
Cùng bảng chân trị, **sơ đồ khác nhau rõ rệt** — đó là lý do ta rút gọn biểu thức trước khi vẽ mạch.

</div>

### 2.2. Vì sao rút gọn không chỉ “đẹp trên giấy”

Hai biểu thức **tương đương** (cùng bảng chân trị):

$$
f_1 = xy + x\bar y + \bar x y,\qquad
f_2 = x + y.
$$

| | $$f_1$$ (thừa) | $$f_2$$ (rút gọn) |
|:---|:---:|:---:|
| AND 2-ngõ (ước lượng) | 3 | 0 |
| OR 2-ngõ | 2 | 1 |
| NOT | 2 | 0 |
| **Tổng cổng thô** | **7** | **1** |

Trên bài tập, ít cổng nghĩa là vẽ và kiểm nhanh hơn. Trên phần cứng thật, ít cổng thường nghĩa là ít linh kiện, trễ thấp hơn và tiêu thụ ít hơn. K-map và Quine–McCluskey chính là công cụ biến $$f_1$$ thành $$f_2$$ một cách có hệ thống.

## 3. Ba tầng công cụ tối thiểu hóa

| Công cụ | Quy mô điển hình | Bản chất |
|:---|:---|:---|
| **Đại số** (13.3) | vài biến, làm tay | nhanh, cần kinh nghiệm |
| **K-map** (13.4) | 2–4 biến | trực quan |
| **Quine–McCluskey** (13.5) | vừa, bằng bảng | hệ thống, lập trình được |
| **Phần mềm hỗ trợ** | nhiều biến | máy làm thay; cùng tư duy gộp + phủ |

![Bản đồ Karnaugh](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

<p class="textbook-figure-caption" data-figure="13.32">K-map — tối thiểu hóa bằng mắt cho hàm nhỏ.</p>

![Quine–McCluskey](/discrete-mathematics-for-computer-science-iuh/img/course/quine_mccluskey.svg)

<p class="textbook-figure-caption" data-figure="13.33">Quine–McCluskey — cùng mục tiêu nhưng bằng bảng.</p>

<div class="textbook-definition" markdown="1">

**Thông điệp chương 13.** K-map dạy *nhìn thấy* sự rút gọn; Quine–McCluskey dạy *thuật toán*; phần mềm công nghiệp scale cùng tư duy lên quy mô lớn. Cả ba tầng đều nói ngôn ngữ Boole.

</div>

## 4. SAT: tìm gán biến làm công thức đúng

### 4.1. Bài toán SAT

<div class="textbook-definition" markdown="1">

**SAT** (*Boolean satisfiability*): cho một công thức logic (thường dạng CNF — tích các tuyển), hỏi có tồn tại gán **0**/**1** cho các biến sao cho toàn công thức bằng **1** không?

</div>

Đây là bài NP-đầy đủ kinh điển, nhưng các chương trình giải SAT thực tế vẫn xử lý được nhiều công thức rất lớn.

### 4.2. Liên hệ với kiểm tra hai mạch

Giả sử hai mạch tổ hợp $$f$$ và $$g$$ cùng số ngõ vào, mỗi mạch một ngõ ra. Câu hỏi “$$f$$ và $$g$$ có **cùng hành vi** không?” có thể mã hóa thành:

> Có tồn tại đầu vào sao cho $$f \neq g$$ không?  
> Tức là: công thức $$f \oplus g$$ có thỏa được (bằng **1**) không?

- Nếu **không** có đầu vào nào làm $$f \oplus g = 1$$ → hai mạch tương đương.
- Nếu **có** → vector đó là ví dụ phản chứng (test bắt lỗi).

Nói cách khác: cổng **tính** hàm Boole; SAT **tìm kiếm** trong không gian gán biến. Cùng nền tảng, hai vai trò.

![Cây tìm kiếm](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="13.34">Trực giác tìm kiếm nhánh gán biến. Solver thật tinh vi hơn, nhưng vẫn bám cấu trúc mệnh đề Boole.</p>

### 4.3. Cầu nối với dạng chuẩn

CNF (tích các mệnh đề OR) là dạng đầu vào quen của nhiều chương trình SAT. Vì vậy học POS (tích các tổng) / CNF ở 13.2 không chỉ để thi: khi bạn viết ràng buộc dưới dạng mệnh đề, bạn đã đứng sát ngôn ngữ kiểm chứng.

<div class="textbook-example" markdown="1">

**Ví dụ.** Ràng buộc “không bật đồng thời ghi và xóa”: $$\lnot(w \land e)$$ tương đương $$\bar w \lor \bar e$$.  
Nhiều ràng buộc kiểu này ghép thành CNF lớn.

</div>

## 5. FPGA: bảng chân trị lập trình được

Hai hướng hiện thực mạch số (mức ý tưởng):

| | **ASIC** (chip chuyên dụng) | **FPGA** |
|:---|:---|:---|
| Sau sản xuất | logic “đóng” cố định | nạp lại được bằng bitstream |
| Ưu | mật độ, hiệu năng cao | linh hoạt, thử nhanh |
| Liên hệ Boole | mạng cổng cố định | mỗi **LUT** $$k$$ ngõ ≈ bảng chân trị $$k$$ biến |

**LUT** (*lookup table*) lưu sẵn cột đầu ra của bảng chân trị. Đó đúng là đối tượng đã học ở 13.2 — chỉ khác chỗ bảng nằm trong bộ nhớ cấu hình thay vì trên giấy.

Người hiểu Boole đọc được vì sao một thiết kế “nặng” (nhiều biến, nhiều hàm) cần nhiều LUT hơn, và vì sao rút gọn biểu thức vẫn có ích trước khi nạp FPGA.

## 6. Sợi chỉ xuyên chương 13

| Bài | Đóng góp |
|:---|:---|
| 13.1 | Ngôn ngữ đại số $$+, \cdot, '$$ |
| 13.2 | Hàm, SOP (tổng các tích) / POS (tích các tổng) |
| 13.3 | Cổng và tối thiểu hóa đại số |
| 13.4 | K-map — tối thiểu trực quan |
| 13.5 | Quine–McCluskey — thuật toán bảng |
| **13.6** | **Bối cảnh:** Shannon, silicon, SAT, FPGA |
| 13.7 | Half/full adder, bộ cộng, nhân, MUX, decoder |

<div class="textbook-definition" markdown="1">

**Một câu chốt.** Máy tính số không “hiểu” tiếng Việt; nó chuyển mức điện áp theo hàm $$\{0,1\}^n \to \{0,1\}^m$$. Đại số Boole là toán học của các hàm đó — từ trang vở đến mạch thật.

</div>

## Bài tập

### Bài tập 1 — Shannon map

Nêu tương ứng Shannon (rơ-le) cho: (a) $$x \cdot y$$, (b) $$x + y$$, (c) $$x'$$. Vì sao AND “tự nhiên” là nối tiếp?

<details>
<summary>Đáp án</summary>

(a) Hai switch nối tiếp — chỉ dẫn khi cả hai đóng.  
(b) Song song — dẫn khi ít nhất một đóng.  
(c) Tiếp điểm đảo.  
AND = nối tiếp vì *cả hai* điều kiện đóng phải thỏa đồng thời.

</details>

### Bài tập 2 — Đếm cổng và tương đương

Cho $$f = ab + a\bar b$$.

1. Chứng minh $$f = a$$ bằng đại số.  
2. Ước lượng số cổng AND/OR/NOT nếu hiện thực $$ab + a\bar b$$ so với chỉ dây nối $$a$$.  
3. Kết luận một câu về tối thiểu hóa.

<details>
<summary>Đáp án</summary>

1. $$ab + a\bar b = a(b + \bar b) = a$$.  
2. Dạng dài ≈ 1 NOT + 2 AND + 1 OR; dạng rút: 0 cổng.  
3. Biểu thức tương đương có thể khác nhau **rất xa** về số cổng.

</details>

### Bài tập 3 — Half adder

Từ bảng half adder, viết SOP (tổng các tích) cho $$s$$ và $$c$$. Mô tả mạng cổng nếu được dùng XOR.

<details>
<summary>Đáp án</summary>

$$s = \bar x y + x\bar y$$ hoặc $$s = x \oplus y$$; $$c = xy$$.  
Có XOR: 1 XOR + 1 AND.

</details>

### Bài tập 4 — Chọn công cụ

Hàm 3 biến, làm tay trên lớp → công cụ nào? Hàm 12 biến → vì sao không K-map?

<details>
<summary>Đáp án</summary>

3 biến: K-map hoặc đại số.  
12 biến: $$2^{12} = 4096$$ minterm — K-map tay không khả thi; dùng QM/phần mềm, không vẽ lưới tay.

</details>

### Bài tập 5 — SAT và tương đương

Giải thích trong 3–5 câu: làm sao dùng SAT để kiểm tra hai mạch 1-bit output $$f$$ và $$g$$ có tương đương? (Gợi ý: xét $$f \oplus g$$.)

<details>
<summary>Đáp án</summary>

Hỏi có input làm $$f \neq g$$ không, tức $$f \oplus g = 1$$.  
Nếu **unsat** → không có input phân biệt → $$f \equiv g$$.  
Nếu **sat** → model là counterexample.

</details>

### Bài tập 6 (thách thức) — LUT

LUT 4-input lưu bao nhiêu bit cấu hình cho *một* hàm Boole 4 biến tùy ý? Liên hệ với bảng chân trị.

<details>
<summary>Đáp án</summary>

$$2^4 = 16$$ dòng bảng → **16 bit** cho mỗi LUT 4 ngõ (chưa kể định tuyến).

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=zPNdj_Qth_Q">How transistors work</a> — trực giác vật lý cổng
- <a href="https://www.youtube.com/watch?v=dJsguV1PaPQ">Karnaugh maps</a> — ôn 13.4

## Tóm tắt

1. Boole cho đại số logic; Shannon ánh xạ đại số đó lên mạch đóng/mở.
2. Cùng hành vi có thể mô tả bằng bảng, biểu thức, mạng cổng, rồi hiện thực vật lý.
3. Rút gọn biểu thức giảm số cổng — trên bài tập và trên phần cứng.
4. SAT tìm gán biến; dùng được để kiểm hai mạch có cùng hành vi.
5. FPGA/LUT là bảng chân trị lập trình được — đúng ngôn ngữ chương 13.

Chương khép lại không bằng một công thức mới, mà bằng **bản đồ** từ trang vở đến mạch thật: mỗi lần bạn nhóm ô trên K-map, bạn đang làm cùng loại tối ưu mà hệ thống lớn cũng làm ở quy mô khác.
