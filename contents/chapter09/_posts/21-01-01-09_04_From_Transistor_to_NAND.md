---
layout: post
title: "Từ transistor đến NAND: Xây CPU từ logic rời rạc"
categories: chapter09
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Đi từ transistor đến cổng logic NAND, latch, flip-flop và mạch cộng ALU trên breadboard, cho thấy đại số Boole trực tiếp tạo nên phần cứng máy tính."
---

Mỗi khi bạn gõ `c = a + b` trong C hay Python, phép cộng trông trừu tượng như một dòng chữ trên màn hình. Nhưng sâu bên dưới hệ điều hành và trình biên dịch, toàn bộ phép tính ấy chỉ là hàng tỷ công tắc điện tử siêu nhỏ bật–tắt ở tốc độ gigahertz, ghép thành một loại cổng duy nhất là **NAND**.

**Mạch bài học:** Từ **transistor** đóng vai công tắc vật lý $$\longrightarrow$$ tính đầy đủ hàm của cổng **NAND** $$\longrightarrow$$ mạch nhớ tuần tự (**SR latch / flip-flop**) $$\longrightarrow$$ bộ cộng **half-adder / full-adder** biến đại số Boole thành phép cộng số học.

## Kiến thức cần nhớ: Kiến trúc mạch số nối toán rời rạc với silicon ra sao?

- **Tính đầy đủ hàm (Functional Completeness):** Một tập cổng logic được gọi là đầy đủ nếu mọi hàm Boole $$f:\{0,1\}^k \to \{0,1\}$$ đều biểu diễn được từ tập đó. Cổng **NAND** ($$\overline{A \cdot B}$$) tự một mình đã đủ dựng nên `NOT`, `AND`, `OR`, `XOR` và mọi mạch tổ hợp phức tạp.
- **Mạch tổ hợp vs. Mạch tuần tự (Combinational vs. Sequential Logic):** Mạch tổ hợp (như bộ cộng) cho đầu ra chỉ phụ thuộc đầu vào hiện tại; còn mạch tuần tự (latch, flip-flop, RAM) có vòng phản hồi (feedback loop) nên **ghi nhớ được trạng thái quá khứ** — nền tảng của bộ nhớ và thanh ghi CPU.
- **Số học nhị phân trên phần cứng (Binary Arithmetic Circuits):** Cách tách phép cộng hai số $$n$$-bit thành chuỗi các bộ cộng toàn phần (full-adder) nối tiếp bit nhớ (ripple-carry), dùng chung một mạch cho cả cộng lẫn trừ bù hai.

Ở bài Year 2038, chúng ta đã phân tích phép **cộng 1** trên số 32-bit có dấu ở mức công thức; vậy phép cộng đó thực sự diễn ra ở đâu bên trong máy tính? Mục này trả lời câu hỏi đó bằng cách đi từng tầng phần cứng từ **transistor** đến cổng logic, latch, flip-flop và mạch cộng ALU trên breadboard theo loạt video của Ben Eater. Mục tiêu là thấy rõ đại số Boole (Chương 1, Chương 13) hiện diện trực tiếp trong **phần cứng silicon**: mọi câu lệnh `if (x && y)` và mọi phép cộng bù hai cuối cùng đều được thực hiện bởi transistor và cổng NAND. Ben Eater dùng breadboard cùng đèn LED hiển thị từng bit để xây dựng một [**máy tính 8-bit hoàn chỉnh**](https://eater.net/8bit/) gồm program counter, thanh ghi (register), ALU, RAM và khối điều khiển (control unit), rồi chạy chương trình tính dãy Fibonacci bằng mã lệnh assembly thực thụ.

Khi xem [video lập trình máy tính 8-bit](https://www.youtube.com/watch?v=9PPrrSyubG0) lần đầu, người học dễ nhận ra rằng phép `a + b` trong C thực chất là hàng chục cổng logic đang chuyển trạng thái cùng lúc — chỉ khác là trên máy tính cá nhân ta không nhìn thấy đèn LED. Nếu Chương 13 trình bày đại số Boole và bìa Karnaugh trên giấy, thì dự án của Ben Eater cho thấy các biểu thức Boole đó vận hành trực tiếp trên mạch vật lý như thế nào.

![Ben Eater 8-bit computer](/discrete-mathematics-for-computer-science-iuh/img/course/maxresdefault.jpg)

<p class="textbook-figure-caption" data-figure="9.7">Máy tính 8-bit trên breadboard — mỗi đèn LED biểu thị trạng thái của một bit (YouTube / Ben Eater).</p>

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/transistor.svg"
       alt="Ký hiệu transistor BJT — công tắc điện tử của bit"
       width="45%" height="45%">
  <figcaption style="text-align: center;">Hình 9.4a: Từ transistor đến phép `a + b` trong C — hiện tượng tràn số Year 2038 diễn ra ngay bên trong mạch ALU (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Transistor.svg">sventeeuwen / Wikimedia Commons</a>, public domain).</figcaption>
</p>
</figure>

---

## Transistor: công tắc của bit

Mọi mạch số đều khởi đầu từ một linh kiện cơ bản là **transistor**. Trong mạch kỹ thuật số, transistor đóng vai trò một **công tắc điện tử**: mức điện áp cao (HIGH, 1) cho dòng điện đi qua, còn mức điện áp thấp (LOW, 0) ngắt dòng. Logic rời rạc chỉ làm việc với hai trạng thái ổn định này chứ không xét trạng thái trung gian. Hàng tỷ transistor trên các bộ xử lý hiện đại như Apple M1, M2 hay AMD Ryzen đều dựa trên cùng nguyên lý đóng/mở này, chỉ được thu nhỏ kích thước và tăng tốc độ chuyển mạch lên rất nhiều lần.

![Transistor symbol — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/transistor.svg)

<p class="textbook-figure-caption" data-figure="9.8">Transistor đóng vai trò công tắc — nền tảng của mọi cổng logic.</p>

Điện áp liên tục trong tự nhiên được **lượng tử hóa** thành hai mức rời rạc — đây là cơ sở vật lý cho mọi bit 0 và 1. Ben Eater xây dựng từng lớp theo trình tự chặt chẽ: [chất bán dẫn (semiconductor)](https://www.youtube.com/watch?v=33vbFFFn04k) → [transistor](https://www.youtube.com/watch?v=DXvAlwMAxiA) → [cổng logic](https://www.youtube.com/watch?v=sTu3LwpF6XI) → [latch / flip-flop](https://www.youtube.com/watch?v=YW-_GkUguMM). Mỗi tầng dựa trực tiếp lên tầng ngay dưới nó, giúp người học hiểu mạch hoạt động thay vì xem phần cứng như hộp đen.

<div class="content-box insight-box textbook-block" markdown="1">
Trong toán rời rạc, mỗi bit là một biến Boole $$x \in \{0,1\}$$. Transistor là linh kiện **hiện thực hóa** biến đó ở tầng vật lý bằng hai trạng thái điện áp ổn định mà mạch có thể đọc chính xác.
</div>

---

## Cổng logic và tính đầy đủ của cổng NAND

Ghép một vài transistor lại với nhau, ta thu được các **cổng logic** cơ bản như NOT, AND, OR — chính là các phép toán Boole đã học ở Chương 1 và Chương 13. Trên breadboard của Ben Eater, trạng thái sáng hoặc tắt của đèn LED tương ứng trực tiếp với từng dòng trong bảng chân trị, không còn khoảng cách giữa công thức trên giấy và mạch điện thật.

![Logic gates — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

<p class="textbook-figure-caption" data-figure="9.9">Ký hiệu cổng logic chuẩn — đồng nhất với sơ đồ mạch của Ben Eater.</p>

Cổng **NAND** (phép Sheffer) có biểu thức $$y = (xz)'$$: đầu ra chỉ bằng 0 khi cả hai đầu vào cùng bằng 1. Một tính chất quan trọng của NAND là **tính đầy đủ hàm** (functional completeness): chỉ cần dùng duy nhất cổng NAND cũng đủ xây dựng mọi hàm Boole. Cụ thể, phép phủ định viết là $$x' = (x \uparrow x)$$ (ký hiệu NAND), còn phép OR suy ra từ định luật De Morgan: $$x + z = (x' \cdot z')'$$. Trong sản xuất chip thực tế, các xưởng đúc vẫn kết hợp nhiều loại cổng khác nhau để tối ưu hiệu năng, nhưng về mặt lý thuyết, toàn bộ CPU có thể quy về tổ hợp của các cổng NAND.

Trên phần cứng, mạch NAND thường gọn, nhanh và tiết kiệm diện tích hơn so với việc ghép nhiều loại cổng riêng lẻ. Vì vậy, việc rút gọn biểu thức Boole bằng bìa Karnaugh ở Chương 13 mang ý nghĩa kỹ thuật trực tiếp: **ít cổng logic hơn** đồng nghĩa với **ít transistor hơn**, giúp chip tiêu thụ ít điện năng và tỏa ít nhiệt hơn.

---

## Latch và flip-flop — ghi nhớ một bit

Các cổng logic tổ hợp thuần túy chỉ tính đầu ra theo đầu vào hiện tại mà không lưu giữ trạng thái cũ. Để tạo ra **bộ nhớ**, mạch cần có **vòng phản hồi** (feedback) đưa đầu ra quay ngược trở lại đầu vào. Ghép chéo hai cổng logic tạo thành **SR latch** với hai trạng thái ổn định, giữ nguyên giá trị một bit cho đến khi tín hiệu điều khiển yêu cầu thay đổi.

**D flip-flop** bổ sung khả năng đồng bộ theo xung nhịp: nó lấy mẫu giá trị đầu vào tại **cạnh xung clock** rồi giữ cố định giá trị đó cho đến cạnh xung kế tiếp. Một thanh ghi (register) 8-bit trên máy Ben Eater đơn giản là tám flip-flop đặt song song, cùng nhận một xung clock. Tương tự, mã lệnh (opcode) 4-bit trên máy này cho phép tối đa $$2^4 = 16$$ lệnh máy khác nhau; mở rộng độ rộng opcode nghĩa là tăng số bit lưu trạng thái điều khiển trong phần cứng.

Khi gỡ lỗi tràn số kiểu `int` trong C, ta đang dựa vào hoạt động chính xác của **chuỗi nhớ** (carry chain) lan truyền từ bit thấp lên bit cao bên trong chip. Trên breadboard, Ben Eater gắn đèn LED cho từng bit nhớ để người xem quan sát trực tiếp, còn trên CPU hiện đại quá trình đó diễn ra trong vài nano giây.

---

## Half-adder: phép cộng thực chất là logic

Phép cộng hai bit đơn $$a$$ và $$b$$ hoàn toàn là một bài toán logic Boole: nếu cả hai bằng 0 thì tổng bằng 0 và nhớ 0; nếu đúng một bit bằng 1 thì tổng bằng 1 và nhớ 0; nếu cả hai cùng bằng 1 thì tổng bằng 0 và bit **nhớ** (carry) bằng 1. Do đó, tổng chính là phép XOR: $$\text{Sum} = a \oplus b$$, còn bit nhớ là phép AND: $$\text{Carry} = a \cdot b$$. Ở tầng transistor không tồn tại “phép cộng số học” tách biệt — chỉ có các cổng AND, OR, NOT (hoặc NAND) nối theo đúng cấu trúc.

![Half adder — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Half-adder.svg)

<p class="textbook-figure-caption" data-figure="9.10">Cổng XOR kết hợp cổng AND tạo nên mạch bán cộng (half-adder) — nền tảng của ALU 8-bit.</p>

Mạch **full-adder** (mạch cộng đầy đủ) bổ sung thêm đầu vào carry-in từ cột bit đứng trước; ghép nối tiếp tám full-adder tạo thành **bộ cộng 8-bit** có bit nhớ lan truyền dọc theo chuỗi. Do thời gian lan truyền tăng theo số bit, CPU 64-bit cần các kỹ thuật thiết kế mạch tiên tiến hơn thay vì cộng nối tiếp đơn thuần. Trong video so sánh [ngôn ngữ C với mã máy](https://www.youtube.com/watch?v=yOyaJXpAYZQ), Ben Eater chỉ rõ một vòng `for` ở bậc cao thực chất được dịch thành chuỗi thao tác tăng program counter, nạp dữ liệu (load), cộng (add) và lưu lại (store) lặp đi lặp lại trên mạch thật theo từng opcode.

<div data-demo="logic-gates-builder"></div>

<script src="{{ '/public/js/logic-gates-builder.js' | relative_url }}"></script>

---

## Từ breadboard đến bù hai (two's complement)

Ở bài Year 2038, chúng ta đã xét bù hai trên công thức: cộng 1 vào cực đại 32-bit có dấu khiến timestamp lùi về năm 1901. Trên breadboard, Ben Eater dùng số **không dấu** để người xem dễ theo dõi chuỗi bit nhớ lan truyền qua các đèn LED từ bit thấp lên bit cao. CPU thực tế dùng **chính mạch cộng không dấu đó**; khác biệt nằm ở tầng tập lệnh (ISA), nơi CPU diễn giải bit cao nhất là bit dấu và bật cờ tràn (overflow flag) khi cộng hai số dương mà kết quả lại mang bit dấu 1.

Xét ví dụ 8-bit để thấy rõ: cực đại không dấu là `11111111` (255), cộng 1 cho ra `00000000` (0) và bỏ bit nhớ ra ngoài. Với mẫu bit `01111111` (127), cộng thêm 1 cho ra `10000000`: nếu đọc **không dấu** thì giá trị là 128, nhưng nếu đọc theo **bù hai** thì đó là −128. **Cùng một mạch cộng nhưng khác quy ước đọc** — đây là cầu nối trực tiếp giữa đèn LED trên breadboard và rủi ro Year 2038 trên firmware PLC mà Lan ghi vào sổ quản lý rủi ro.

Khi xem lại video về ALU của Ben Eater sau khi đọc bài viết trên Planet Mainframe, Lan nhận ra sự kiện phần cứng đằng sau bài `09_03`: hai số dương cộng với nhau làm bit dấu bật từ 0 lên 1. Mạch silicon không biết đến khái niệm “năm 2038”; nó chỉ thực hiện đúng quy tắc lan truyền bit nhớ.

---

## Ví dụ tính tay làm từng bước: Dựng NOT, AND, OR chỉ từ NAND và cộng nhị phân 2-bit

**Phần A — Chứng minh bằng bảng chân trị rằng NAND sinh được NOT và AND:**
Định nghĩa $$\text{NAND}(A, B) = \overline{A \cdot B}$$.

1. **Tạo `NOT(A)`:** Nối hai đầu vào của NAND vào cùng tín hiệu $$A$$:
   $$\text{NAND}(A, A) = \overline{A \cdot A} = \overline{A}.$$
   Kiểm tra: nếu $$A=0 \Rightarrow \overline{0\cdot 0}=1$; nếu $$A=1 \Rightarrow \overline{1\cdot 1}=0$.
2. **Tạo `AND(A, B)`:** Đưa đầu ra của $$\text{NAND}(A, B)$$ qua một cổng `NOT` làm từ NAND:
   $$\text{NAND}\big(\text{NAND}(A, B),\, \text{NAND}(A, B)\big) = \overline{\overline{A \cdot B}} = A \cdot B.$$
3. **Tạo `OR(A, B)` nhờ định luật De Morgan:** Đảo từng đầu vào bằng NAND rồi đưa vào NAND thứ ba:
   $$\text{NAND}(\overline{A}, \overline{B}) = \overline{\overline{A} \cdot \overline{B}} = A + B.$$

**Phần B — Chạy tay bộ cộng 2-bit cho phép tính $$3 + 2 = 5$$ ($$11_2 + 10_2$$):**
Gọi $$A = a_1 a_0 = 11_2$$, $$B = b_1 b_0 = 10_2$$.
- **Bit 0 (Half-Adder):**
  - Tổng $$s_0 = a_0 \oplus b_0 = 1 \oplus 0 = 1$$.
  - Bit nhớ $$c_1 = a_0 \cdot b_0 = 1 \cdot 0 = 0$$.
- **Bit 1 (Full-Adder nhận $$a_1=1, b_1=1, c_1=0$$):**
  - Tổng $$s_1 = a_1 \oplus b_1 \oplus c_1 = 1 \oplus 1 \oplus 0 = 0$$.
  - Bit nhớ ra $$c_2 = (a_1 \cdot b_1) + c_1 \cdot (a_1 \oplus b_1) = (1 \cdot 1) + 0 = 1$$.
- **Kết quả ghép lại:** $$c_2 s_1 s_0 = 101_2 = 4 + 0 + 1 = 5$$. Hoàn toàn khớp với số học thông thường!

### Giải thích: Cầu nối 4 tầng từ vật lý đến chương trình máy tính
1. **Bước 1 — Vật lý rời rạc hóa điện áp:** Transistor biến điện áp tương tự (0V / 5V) thành hai ký hiệu rời rạc `0` và `1`, giúp loại bỏ nhiễu nhỏ ở mỗi tầng mạch.
2. **Bước 2 — Đại số Boole tạo khối tính toán:** Nhờ tính đầy đủ hàm của NAND, mọi bảng chân trị hữu hạn — kể cả bộ cộng `Sum = A XOR B` và `Carry = A AND B` — đều đóng gói được thành mạch tổ hợp.
3. **Bước 3 — Vòng phản hồi tạo ra trí nhớ:** Khi nối đầu ra cổng NAND quay ngược về đầu vào cổng bên cạnh (SR latch), mạch giữ nguyên bit `0` hoặc `1` ngay cả khi tín hiệu kích đã ngắt — biến mạch logic thành thanh ghi và RAM.
4. **Bước 4 — Đồng hồ nhịp (clock) điều phối toàn CPU:** Kết hợp thanh ghi + ALU + xung clock, máy tính đọc lệnh từ RAM, cộng/trừ trên thanh ghi rồi ghi kết quả ngược lại, biến lý thuyết đại số Boole thành bộ vi xử lý thực thụ.

$$\text{Transistor} \;\xrightarrow{\text{đóng/ngắt}}\; \text{NAND} \;\xrightarrow{\text{De Morgan}}\; \text{ALU \& Latch} \;\xrightarrow{\text{Clock}}\; \text{CPU chạy mã máy.}$$

## Bài tập thực hành

### Bài tập 1

Chỉ sử dụng cổng NAND, hãy biểu diễn phép phủ định $$x'$$ của một biến $$x$$.

<details>
<summary>Đáp án</summary>

Nối cả hai đầu vào của một cổng NAND vào cùng biến $$x$$: $$x' = x \uparrow x = (xx)' = x'$$. Đây là bước đầu tiên để chứng minh tập chỉ gồm cổng NAND đủ để xây dựng mọi hàm Boole.

</details>

### Bài tập 2

Một mạch half-adder nhận đầu vào $$a = 1$$ và $$b = 1$$. Tính giá trị của Sum và Carry.

<details>
<summary>Đáp án</summary>

$$\text{Sum} = 1 \oplus 1 = 0$$ và $$\text{Carry} = 1 \cdot 1 = 1$$. Hai bit 1 cộng lại cho tổng 0 ở cột hiện tại và nhớ 1 sang cột kế tiếp, khớp với phép cộng nhị phân $$1 + 1 = 10_2$$.

</details>

### Bài tập 3

Một thanh ghi 8-bit trên máy tính của Ben Eater cần bao nhiêu flip-flop? Nếu opcode rộng 4 bit, máy hỗ trợ tối đa bao nhiêu lệnh máy khác nhau?

<details>
<summary>Đáp án</summary>

Thanh ghi 8-bit cần **8 flip-flop** (mỗi flip-flop lưu 1 bit). Opcode 4-bit tạo ra $$2^4 = 16$$ tổ hợp khác nhau, tương ứng tối đa **16 lệnh máy** nếu mỗi mã ứng với một lệnh riêng.

</details>

### Bài tập 4

Trên 8 bit, lấy mẫu `01111111` (127) cộng thêm 1 thu được `10000000`. Giải thích vì sao kết quả là 128 khi đọc không dấu nhưng lại là −128 khi đọc theo bù hai, và liên hệ với tràn số có dấu.

<details>
<summary>Đáp án</summary>

Mạch cộng thực hiện cùng một thao tác: bit nhớ lan truyền qua bảy bit 1 ở các vị trí thấp, làm bit cao nhất chuyển từ 0 sang 1. Khi đọc **không dấu** (unsigned), `10000000` bằng $$2^7 = 128$$. Khi đọc theo **bù hai** 8-bit, bit dấu bằng 1 nên giá trị là $$-2^7 = -128$$. Đây là tràn số có dấu dạng “dương + dương → âm”, có cùng cơ chế với sự cố Year 2038 ở quy mô 32-bit khi `0111…111` + 1 biến thành `1000…000`.

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Dự án máy tính 8-bit trên breadboard của Ben Eater cho thấy rõ mối liên hệ giữa lý thuyết và phần cứng: **mọi lệnh trong chương trình cuối cùng đều quy về cổng logic, và mọi cổng logic đều cấu tạo từ transistor**. Transistor trong mạch số đóng vai trò công tắc hai trạng thái; từ đó xây dựng các cổng NOT, AND, OR và đặc biệt là NAND — cổng có tính đầy đủ để tạo mọi hàm Boole. Bổ sung vòng phản hồi cho ra latch và flip-flop để **lưu bit**; ghép flip-flop thành thanh ghi và ghép các bộ cộng half-adder/full-adder theo chuỗi nhớ tạo nên **mạch cộng ALU**.

Bài `09_03` phân tích bù hai và Year 2038 ở mức biểu diễn số học, còn bài này cho thấy **chính một mạch cộng** đứng sau cả số không dấu lẫn số có dấu: CPU cộng bit như nhau rồi dùng quy ước tập lệnh (ISA) để đọc bit dấu và bật cờ tràn. Bìa Karnaugh và tối ưu biểu thức Boole ở Chương 13 gắn trực tiếp với kỹ thuật chip: giảm số cổng đồng nghĩa với giảm transistor, điện năng và nhiệt lượng.

**Đọc thêm:** [Ben Eater — 8-bit computer](https://eater.net/8bit/) · [Video series — từ transistor đến CPU](https://www.youtube.com/playlist?list=PLowKtXNTBypGqPEN6Wkuy-gv1SFmc-KH8)

Bài tiếp theo rời khỏi tầng silicon để chuyển sang **bài toán hàng đợi trên máy chủ**: wiki [HikariCP](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) của Brett Wooldridge — vì sao “một triệu người dùng trực tuyến” không tương đương “một triệu kết nối PostgreSQL”, và vì sao cấu hình connection pool quá lớn lại khiến cơ sở dữ liệu **chậm đi**.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=33vbFFFn04k">How semiconductors work</a> — Ben Eater, tiếng Anh. Giới thiệu nguyên lý chất bán dẫn, lớp vật lý nền trước khi đi vào transistor.
- <a href="https://www.youtube.com/watch?v=DXvAlwMAxiA">How a transistor works</a> — Ben Eater, tiếng Anh. Minh họa hoạt động của transistor như một công tắc biểu diễn bit.
- <a href="https://www.youtube.com/watch?v=sTu3LwpF6XI">Making logic gates from transistors</a> — Ben Eater, tiếng Anh. Cách ghép transistor thành các cổng logic, tiến tới cổng NAND có tính đầy đủ.
