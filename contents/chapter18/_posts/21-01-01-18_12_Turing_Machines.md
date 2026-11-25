---
layout: post
title: "Máy Turing"
categories: chapter18
date: 2021-01-01
order: 12
required: true
lang: en
excerpt: "Định nghĩa hình thức máy Turing bộ 7, cấu hình và bước chuyển, so sánh sức mạnh giữa DFA/PDA/TM và luận đề Church–Turing."
---

<div class="textbook-epigraph" markdown="1">

"We may compare a man in the process of computing … to a machine."

<span class="epigraph-attribution">— A. M. Turing, 1936</span>

</div>

![TM](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_turing_tape.svg)

<p class="textbook-figure-caption" data-figure="18.6">Băng đọc/ghi vô hạn cung cấp bộ nhớ không bị giới hạn như ở DFA.</p>

Năm 1936, khi máy tính điện tử còn chưa ra đời, Alan Turing ngồi tự hỏi: *"Một người tính toán cầm bút chì và cuốn vở kẻ ô có thể làm được những phép tính nào?"* Để trả lời câu hỏi đó, ông rút gọn toàn bộ hành động tính toán của con người thành một thiết bị cực kỳ tối giản: một cuộn băng giấy dài vô hạn chia thành từng ô, một đầu đọc/ghi chỉ di chuyển từng ô sang trái hoặc phải, và một bảng quy tắc hữu hạn. Điều kỳ diệu là mô hình tưởng chừng thô sơ ấy lại mạnh ngang ngửa với mọi siêu máy tính hiện đại ngày nay.

## Bản đồ kiến thức nền: Ba trụ cột của Máy Turing

1. **Bộ nhớ đọc/ghi không giới hạn (Băng vô hạn)**:
   Khác với DFA (chỉ nhớ trạng thái hữu hạn) hay PDA (chỉ chạm được đỉnh ngăn xếp LIFO), máy Turing có thể đi tới đi lui tùy ý trên băng, ghi đè kết quả trung gian và dùng chính băng làm bộ nhớ nháp không giới hạn.
2. **Cấu hình (Configuration) và Quan hệ bước chuyển $$\vdash$$**:
   Toàn bộ trạng thái của một máy tính đang chạy được chụp gọn thành một chuỗi $$uqv$$: phần bên trái đầu đọc là $$u$$, trạng thái hiện tại là $$q$$, và ký hiệu ngay dưới đầu đọc là ký tự đầu tiên của $$v$$. Một tính toán chỉ là dãy bước chuyển $$C_0 \vdash C_1 \vdash \cdots \vdash C_k$$.
3. **Luận đề Church–Turing (Chuẩn mực phổ quát của thuật toán)**:
   Mọi mô hình tính toán vật lý hợp lý (máy nhiều băng, RAM, phép tính $$\lambda$$, Python, C++) đều tính được đúng cùng một lớp hàm như máy Turing đơn định 1 băng — chỉ khác nhau về tốc độ chứ không khác về *khả năng tính được*.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** máy Turing (TM) bằng bộ bảy thành phần.
- **Mô tả** cấu hình của máy và quan hệ bước chuyển $$\vdash$$.
- **So sánh** sức mạnh biểu diễn giữa DFA, PDA và máy Turing.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Một máy Turing đơn định là bộ bảy

$$M=(Q,\Sigma,\Gamma,\delta,q_0,q_A,q_R),$$

với hàm chuyển $$\delta:(Q\setminus\{q_A,q_R\})\times\Gamma\to Q\times\Gamma\times\{L,R\}$$.

**Cấu hình** $$uqv$$ biểu diễn trạng thái toàn cục của máy tại một bước: nội dung băng là $$uv$$, máy đang ở trạng thái $$q$$ và đầu đọc/ghi đặt tại ký hiệu đầu tiên của $$v$$.

</div>

## So sánh sức mạnh các mô hình

| Mô hình | Bộ nhớ | Ví dụ ngôn ngữ nằm ngoài lớp |
|:---|:---|:---|
| DFA | Hữu hạn | $$0^n1^n$$ |
| PDA | Ngăn xếp (*stack*) | $$a^nb^nc^n$$ |
| Máy Turing (TM) | Băng đọc/ghi vô hạn | — (nhận mọi ngôn ngữ quyết định được) |

## Luận đề Church–Turing

Theo luận đề Church–Turing, khái niệm trực giác về “thuật toán tính toán hiệu quả” tương đương với khả năng thực thi trên một máy Turing (hoặc bất kỳ mô hình tính toán tương đương nào).

### Minh họa máy Turing: băng, đầu đọc và trạng thái

Chạy thử máy Turing từng bước để xem quá trình đọc ký hiệu, ghi đè, dịch chuyển đầu đọc và chuyển trạng thái trên các ví dụ: cộng 1 nhị phân, nhận dạng $$0^n1^n$$ và phép cộng đơn phân:

<div class="interactive-demo" markdown="1">
<div data-demo="tm-explainer" data-preset="inc"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

### Khung giải thích (nên đọc chậm): Chạy tay máy Turing cộng 1 vào số nhị phân `1011`

Để thấy máy Turing thực sự "tính toán" ra sao mà không cần CPU phức tạp, ta thiết kế máy cộng 1 vào số nhị phân (đầu đọc bắt đầu ở bit đầu tiên bên trái):
- **Trạng thái $$q_{\text{right}}$$**: Đi sang phải (`R`) qua mọi ký tự `0`, `1` cho đến khi gặp ô trống $$\sqcup$$, thì quay sang trái (`L`) và chuyển sang $$q_{\text{carry}}$$.
- **Trạng thái $$q_{\text{carry}}$$**: Nếu gặp `1` thì đổi thành `0` và đi tiếp sang trái (`L`, giữ nhớ 1); nếu gặp `0` (hoặc $$\sqcup$$) thì đổi thành `1` và chuyển sang trạng thái dừng chấp nhận $$q_A$$.

Theo dõi từng cấu hình $$uqv$$ với đầu vào `1011` (giá trị thập phân $$11$$):

| Bước | Cấu hình $$uqv$$ | Ký hiệu đọc | Hành động của $$\delta$$ | Giải thích trực quan |
| :---: | :--- | :---: | :--- | :--- |
| 0 | $$q_{\text{right}} 1011$$ | `1` | Ghi `1`, đi `R`, giữ $$q_{\text{right}}$$ | Bỏ qua để tìm bit cuối |
| 1–3 | $$1011 q_{\text{right}} \sqcup$$ | $$\sqcup$$ | Ghi $$\sqcup$$, đi `L`, sang $$q_{\text{carry}}$$ | Đã tới cuối chuỗi, quay lại cộng 1 |
| 4 | $$101 q_{\text{carry}} 1$$ | `1` | Ghi `0`, đi `L`, giữ $$q_{\text{carry}}$$ | $$1 + 1 = 0$$ nhớ 1 |
| 5 | $$10 q_{\text{carry}} 10$$ | `1` | Ghi `0`, đi `L`, giữ $$q_{\text{carry}}$$ | $$1 + 1 = 0$$ nhớ 1 |
| 6 | $$1 q_{\text{carry}} 000$$ | `0` | Ghi `1`, đi `R`, sang $$q_A$$ | $$0 + 1 = 1$$, hết nhớ → **Dừng!** |

Kết quả trên băng là `1100` (giá trị $$12$$). Chỉ với 2 trạng thái làm việc, máy Turing đã thực hiện hoàn chỉnh phép cộng nhớ nhị phân cho chuỗi dài tùy ý!

## Bài tập

1. Mô tả máy Turing nhận ngôn ngữ $$0^n1^n$$ bằng ý tưởng gạch chéo từng cặp ký tự `0` và `1`.
2. So sánh một bước tính toán của DFA với một bước tính toán của máy Turing.
3. Đọc trích đoạn công trình gốc năm 1936 của Alan Turing.

## Tài liệu đọc thêm

Sipser §3; Arora–Barak §1.

## Tóm tắt

Máy Turing mở rộng mô hình tính toán bằng băng đọc/ghi không giới hạn, tạo nên chuẩn mực phổ quát cho khái niệm thuật toán.

**Bài tiếp theo:** Ngôn ngữ quyết định được (Decidable), đệ quy liệt kê (RE) và bài toán dừng.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=dNRDvLACg5Q">Turing Machines Explained - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu trực quan về máy Turing: băng, đầu đọc và bảng trạng thái.
- <a href="https://www.youtube.com/watch?v=PvLaPKPzq2I">Turing Machine - Introduction (Part 1)</a> — Neso Academy, tiếng Anh. Giới thiệu từng thành phần trước khi đi vào định nghĩa bộ bảy.
- <a href="https://www.youtube.com/watch?v=yFEdBR-rP9g">Turing Machine (Formal Definition)</a> — Neso Academy, tiếng Anh. Định nghĩa hình thức của máy Turing, sát với phần định nghĩa trong bài.
