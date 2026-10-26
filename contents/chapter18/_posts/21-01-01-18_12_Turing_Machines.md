---
layout: post
title: "Máy Turing"
categories: chapter18
date: 2021-01-01
order: 12
required: true
lang: en
excerpt: "Định nghĩa TM; cấu hình; ví dụ; so FSM/PDA; Church–Turing."
---


<div class="textbook-epigraph" markdown="1">

"We may compare a man in the process of computing … to a machine."

<span class="epigraph-attribution">— A. M. Turing, 1936</span>

</div>

![TM](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_turing_tape.svg)

<p class="textbook-figure-caption" data-figure="18.6">Băng R/W vô hạn — bộ nhớ không bị chặn như DFA.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** TM bộ 7.
- **Mô tả** cấu hình và bước $$\vdash$$.
- **So sánh** DFA / PDA / TM.

</div>

## Định nghĩa

$$M=(Q,\Sigma,\Gamma,\delta,q_0,q_A,q_R)$$,  
$$\delta:(Q\setminus\{q_A,q_R\})\times\Gamma\to Q\times\Gamma\times\{L,R\}$$.

**Cấu hình** $$uqv$$: băng $$uv$$, đầu tại đầu $$v$$, trạng thái $$q$$.

## Sức mạnh

| Mô hình | Bộ nhớ | Ví dụ ngoài |
|:---|:---|:---|
| DFA | hữu hạn | $$0^n1^n$$ |
| PDA | stack | $$a^nb^nc^n$$ |
| TM | băng | — (mọi decidable) |

## Church–Turing

Thuật toán hiệu quả ≈ TM (hoặc mô hình tương đương).

## Bài tập

1. TM nhận $$0^n1^n$$ (ý gạch).  
2. So sánh một bước DFA vs TM.  
3. Đọc Turing 1936 excerpt.

## Đọc

Sipser §3; Arora–Barak §1.

## Tóm tắt

TM · cấu hình · phổ quát.

**Tiếp:** decidable vs RE.

## Video tham khảo

- **xem trước** <a href="https://www.youtube.com/watch?v=dNRDvLACg5Q">Turing Machines Explained - Computerphile</a> — Computerphile, tiếng Anh. Xem trước máy Turing: băng, đầu đọc và trạng thái.
- <a href="https://www.youtube.com/watch?v=PvLaPKPzq2I">Turing Machine - Introduction (Part 1)</a> — Neso Academy, tiếng Anh. Giới thiệu từng bộ phận trước định nghĩa bộ bảy.
- <a href="https://www.youtube.com/watch?v=yFEdBR-rP9g">Turing Machine (Formal Definition)</a> — Neso Academy, tiếng Anh. Định nghĩa hình thức, đúng mục định nghĩa của bài.
