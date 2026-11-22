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
