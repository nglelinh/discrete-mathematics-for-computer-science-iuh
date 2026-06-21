---
layout: post
title: "Từ transistor đến NAND: Xây CPU từ logic rời rạc"
categories: chapter09
date: 2021-01-01
order: 4
required: false
lang: en
---

Sau buổi học Year 2038, Lan mang về nhà câu hỏi mà cả lớp SCADA đều thấy trừu tượng: **cộng một** trên 32-bit signed thực sự xảy ra ở đâu trong máy? Giáo viên nói “trong ALU”, nhưng ALU là hộp đen. Tối đó Lan xem loạt video của Ben Eater — anh không vẽ ALU lên slide rồi bảo “phần còn lại để sinh viên tự tìm hiểu”. Anh dùng breadboard, transistor thật, LED nhấp nháy từng bit, và xây [**máy tính 8-bit hoàn chỉnh**](https://eater.net/8bit/): program counter, register, ALU, RAM, control unit — rồi chạy Fibonacci bằng opcode assembly thật.

Xem [video lập trình máy](https://www.youtube.com/watch?v=9PPrrSyubG0) lần đầu, nhiều người nghĩ: “Ồ, `a + b` trong C **là** hàng chục cổng logic đang chạy.” Đúng vậy — chỉ là trên laptop bạn không thấy LED. Chương 13 dạy đại số Boole và Karnaugh trên giấy. Ben Eater cho thấy Boole **là silicon** — và mọi `if (x && y)` cuối cùng đứng trên transistor.

![Ben Eater 8-bit computer](/discrete-mathematics-for-computer-science-iuh/img/course/maxresdefault.jpg)

*Hình 9.7: Máy 8-bit trên breadboard — mỗi đèn là một bit (YouTube / Ben Eater).*

---

## Transistor: công tắc của bit

Mọi câu chuyện bắt đầu từ một khối nhỏ hơn móng tay: **transistor**. Trong mạch digital, transistor hoạt động như **công tắc**: điện áp cao (HIGH, 1) cho phép dòng chạy qua, điện áp thấp (LOW, 0) chặn dòng. Không có “một chút mở” trong logic rời rạc — chỉ có hai trạng thái ổn định. Hàng tỷ transistor trên chip M1, M2 hay Ryzen là biến thể thu nhỏ của ý tưởng này: cùng một nguyên lý khóa/mở, chỉ nhỏ hơn và nhanh hơn khủng khiếp.

![Transistor symbol — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/transistor.svg)

*Hình 9.8: Transistor như khóa — nền mọi cổng logic.*

Điện áp liên tục trong thế giới vật lý bị **quantize** thành hai mức — đây là mệnh đề vật lý đằng sau mọi bit: chỉ 0 hoặc 1. Ben Eater đi từng bước, không nhảy cóc: [semiconductor](https://www.youtube.com/watch?v=33vbFFFn04k) → [transistor](https://www.youtube.com/watch?v=DXvAlwMAxiA) → [logic gates](https://www.youtube.com/watch?v=sTu3LwpF6XI) → [latch / flip-flop](https://www.youtube.com/watch?v=YW-_GkUguMM). Mỗi video là một tầng xây dựng; bỏ qua tầng nào thì tầng sau trở thành phép màu.

<div class="content-box insight-box" markdown="1">
Trong toán rời rạc, mỗi bit là biến Boole $$x \in \{0,1\}$$. Transistor là cách **vật lý hóa** biến đó — không phải “gần giống 0 và 1”, mà là hai trạng thái ổn định mà mạch thiết kế để máy đọc chắc chắn.
</div>

---

## Cổng logic và NAND đủ cho mọi thứ

Ghép vài transistor lại, ta có **cổng logic**: NOT, AND, OR — những hàm Boole quen từ chương 1 và chương 13. Trên breadboard của Ben Eater, LED sáng hoặc tắt **chính là** một dòng trong bảng chân trị; không có lớp trừu tượng nào che giữa công thức trên giấy và ánh sáng trên mạch.

![Logic gates — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

*Hình 9.9: Ký hiệu chuẩn — cùng ngôn ngữ với sơ đồ Ben Eater.*

Cổng **NAND** (Sheffer) có công thức $$y = (xz)'$$: chỉ khi cả hai đầu vào đều 1 thì đầu ra mới là 0. Điều kỳ diệu là **chỉ NAND** cũng đủ biểu diễn mọi hàm Boole — tính đầy đủ mà sách giáo khoa gọi là functional completeness. Phủ định một biến: $$x' = (x \uparrow x)$$ với ký hiệu NAND. OR suy ra từ De Morgan: $$x + z = (x' \cdot z')'$$. Trong thực tế, foundry tối ưu hỗn hợp nhiều loại cổng, nhưng câu “CPU chỉ là NAND khổng lồ” vẫn đúng về mặt lý thuyết — và giúp bạn nhớ rằng phần cứng không ma thuật, chỉ là Boole được in lên silicon.

Chip NAND thường rẻ, nhanh, ít tốn diện tích hơn ghép nhiều loại cổng riêng lẻ. Karnaugh map ở chương 13 không phải bài tập trang trí: rút gọn biểu thức Boole nghĩa là **ít cổng hơn**, tức ít transistor hơn, tức ít điện năng và ít nhiệt hơn trên chip thật.

---

## Latch, flip-flop — nhớ một bit

Cổng logic thuần chỉ tính toán: đầu vào đổi thì đầu ra đổi theo, không “nhớ” gì cả. Muốn có **bộ nhớ**, cần **phản hồi** — đầu ra quay ngược về đầu vào. Hai cổng nối chéo tạo **SR latch**: hai trạng thái ổn định, mỗi trạng thái là một bit được giữ cho đến khi tín hiệu điều khiển bắt đổi.

**D flip-flop** tiến thêm một bước: lấy mẫu giá trị đầu vào tại **cạnh clock**, rồi giữ nguyên cho đến cạnh kế tiếp. Register 8-bit trên máy Ben Eater là tám flip-flop xếp cạnh nhau — mỗi ô nhớ một bit, cùng nhịp clock. Opcode 4-bit trên máy đó cho phép $$2^4 = 16$$ lệnh máy khả dĩ; thay đổi độ rộng opcode là thay đổi **số bit nhớ trạng thái điều khiển**, không phải chỉ đổi tên lệnh trên giấy.

Khi bạn debug overflow `int` trong C, bạn đang tin rằng **carry chain** của half-adder trên chip đã propagate đúng từ bit thấp lên bit cao. Ben Eater bật LED từng carry để bạn **nhìn** điều đó — còn trong laptop, chuỗi carry chạy trong nanosecond mà không có đèn nào nhấp nháy.

---

## Half-adder: cộng là logic

Phép cộng hai bit $$a$$ và $$b$$ là bài toán Boole thuần túy. Khi cả hai đều 0, tổng 0 và không nhớ; khi một trong hai là 1, tổng 1 và không nhớ; khi cả hai đều 1, tổng 0 nhưng **carry** (nhớ sang) là 1. Tổng chính là XOR: $$\text{Sum} = a \oplus b$$. Carry là AND: $$\text{Carry} = a \cdot b$$. Không có phép “cộng số học” riêng ở tầng transistor — chỉ có AND, OR, NOT (hoặc NAND) được dây nối đúng cách.

![Half adder — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Half-adder.svg)

*Hình 9.10: XOR + AND — nền ALU 8-bit.*

**Full-adder** thêm đầu vào carry-in từ bit trước; nối tám full-adder thành **8-bit adder** với carry chạy dọc theo chuỗi. Độ trễ tăng theo số bit — đó là lý do CPU 64-bit không “cộng trong một nhịp” theo nghĩa tức thì trên toàn bộ dãy bit. Ben Eater so sánh [C với machine language](https://www.youtube.com/watch?v=yOyaJXpAYZQ): vòng `for` trong ngôn ngữ cao cấp là tăng program counter, load, add, store — lặp đi lặp lại trên mạch thật, từng opcode một.

<div data-demo="logic-gates-builder"></div>

---

## Từ breadboard đến two's complement

Bài trước (09_03) đã thấy two's complement trên giấy: cộng 1 vào giá trị max của 32-bit signed đưa timestamp về năm 1901. Máy Ben Eater dùng số **không dấu** trên breadboard để bạn **nhìn** carry chain từng bit — LED nhấp nháy từ hàng đơn vị lên hàng cao. CPU thật dùng **cùng mạch cộng không dấu**; khác biệt nằm ở tầng ISA: CPU **đọc** bit cao nhất như sign bit và bật cờ overflow khi cộng hai số dương mà ra kết quả âm.

Ví dụ 8-bit cho dễ hình dung: max không dấu là `11111111` (255). Cộng 1 → `00000000` (0) với carry-out bị bỏ qua — wrap-around bình thường. Cùng pattern bit `01111111` (127) cộng 1 thành `10000000`: nếu đọc **không dấu** thì được 128; nếu đọc **two's complement** thì `10000000` là −128. **Cùng mạch cộng, khác quy ước đọc** — đó là cầu nối giữa LED nhấp nháy trên breadboard và Year 2038 trên firmware PLC mà Lan vừa ghi vào risk register.

Lan tua lại video ALU của Ben Eater sau khi đọc Planet Mainframe. Lần này cô không chỉ thấy “cộng bit” — cô thấy **cùng sự kiện vật lý** mà bài 09_03 mô tả bằng công thức: dương cộng dương mà sign bit bật lên 1. Silicon không biết năm 2038; nó chỉ biết carry propagating đúng hay sai.

---

## Bài tập thực hành

### Bài tập 1

Chỉ dùng cổng NAND, biểu diễn phủ định $$x'$$ từ một biến $$x$$.

<details>
<summary>Đáp án</summary>

Nối cả hai đầu vào của một cổng NAND cùng vào $$x$$: $$x' = x \uparrow x = (xx)' = x'$$. Đây là bước cơ bản để chứng minh NAND đủ dựng mọi hàm Boole.

</details>

### Bài tập 2

Half-adder có $$a = 1$$, $$b = 1$$. Sum và Carry là gì?

<details>
<summary>Đáp án</summary>

$$\text{Sum} = 1 \oplus 1 = 0$$. $$\text{Carry} = 1 \cdot 1 = 1$$. Hai bit 1 cộng lại cho tổng 0 tại bit hiện tại và nhớ 1 sang bit kế tiếp — đúng với cộng nhị phân $$1 + 1 = 10_2$$.

</details>

### Bài tập 3

Register 8-bit trên máy Ben Eater cần bao nhiêu flip-flop? Nếu opcode rộng 4 bit, tối đa bao nhiêu lệnh máy khác nhau?

<details>
<summary>Đáp án</summary>

Register 8-bit cần **8 flip-flop** (mỗi flip-flop giữ 1 bit). Opcode 4-bit biểu diễn $$2^4 = 16$$ tổ hợp khác nhau, tức tối đa **16 lệnh máy** nếu mỗi pattern opcode map tới một lệnh riêng.

</details>

### Bài tập 4

Trên 8-bit, pattern `01111111` (127) cộng 1 ra `10000000`. Giải thích vì sao kết quả là 128 nếu đọc không dấu nhưng là −128 nếu đọc two's complement — và liên hệ với overflow signed.

<details>
<summary>Đáp án</summary>

Mạch cộng không đổi: carry chạy qua các bit 1 ở vị trí thấp, làm bit cao nhất từ 0 thành 1. Đọc **unsigned**, `10000000` = $$2^7 = 128$$. Đọc **two's complement** 8-bit, bit sign = 1 nên giá trị = $$-2^7 = -128$$. Đây là overflow signed kiểu “dương + dương → âm” — cùng hiện tượng ở quy mô 32-bit tạo Year 2038 khi `0111…111` + 1 thành `1000…000`.

</details>

---

## Tóm tắt

Ben Eater xây máy tính 8-bit trên breadboard để chứng minh điều mà đại số Boole trên giấy hay nói qua loa: **mọi lệnh trong chương trình cuối cùng là cổng logic, và mọi cổng logic cuối cùng là transistor**. Transistor digital là công tắc hai trạng thái; từ đó ghép NOT, AND, OR, và đặc biệt NAND — cổng đủ để dựng mọi hàm Boole. Thêm phản hồi chéo ta có latch và flip-flop để **nhớ bit**; xếp flip-flop thành register và nối half-adder/full-adder thành chuỗi carry ta có **ALU cộng**.

Bài 09_03 dạy two's complement và Year 2038 trên lớp trừu tượng. Bài này cho thấy **cùng mạch cộng** đứng sau cả hai: CPU không có mạch riêng cho “số âm”; nó cộng bit như không dấu, rồi ISA quy định cách đọc sign bit và khi nào báo overflow. Karnaugh map và tối ưu Boole ở chương 13 không xa rời thực tế — ít cổng hơn nghĩa là ít transistor, ít điện năng, chip chạy nhanh hơn.

**Đọc thêm:** [Ben Eater — 8-bit computer](https://eater.net/8bit/) · [Video series — từ transistor đến CPU](https://www.youtube.com/playlist?list=PLowKtXNTBypGqPEN6Wkuy-gv1SFmc-KH8)

Bài tiếp theo rời khỏi silicon, chuyển sang **hàng đợi** trên server: Brett Wooldridge và wiki [HikariCP](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) — vì sao “một triệu user online” không đồng nghĩa “một triệu connection PostgreSQL”, và pool connection quá lớn có thể làm database **chậm hơn** thay vì nhanh hơn.