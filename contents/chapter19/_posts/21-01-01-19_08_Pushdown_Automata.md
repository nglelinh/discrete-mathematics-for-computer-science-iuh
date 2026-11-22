---
layout: post
title: "Automat Đẩy xuống (PDA)"
categories: chapter19
date: 2021-01-01
order: 8
required: true
lang: en
excerpt: "Định nghĩa hình thức ô-tô-mát đẩy xuống (PDA), mô tả tức thời (ID), hai chế độ chấp nhận (ngăn xếp rỗng và trạng thái kết thúc) cùng ví dụ aⁿbⁿ."
---

<div class="textbook-epigraph" markdown="1">

"A stack is exactly the memory context-free languages need."

<span class="epigraph-attribution">— PDA</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** ô-tô-mát đẩy xuống (*Pushdown Automaton*, PDA).
- **Mô phỏng** quá trình PDA nhận dạng ngôn ngữ $$\{a^nb^n\}$$.
- **Phân biệt** hai chế độ chấp nhận: theo ngăn xếp rỗng (*empty stack*) và theo trạng thái kết thúc (*final state*).

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Một ô-tô-mát đẩy xuống (PDA) là bộ bảy

$$P=(Q,\Sigma,\Gamma,\delta,q_0,Z_0,F),$$

với hàm chuyển $$\delta:Q\times(\Sigma\cup\{\varepsilon\})\times\Gamma\to\mathcal{P}(Q\times\Gamma^*)$$ (có tập ảnh hữu hạn cho mỗi bộ đầu vào).

**Mô tả tức thời (ID)** $$(q,w,\gamma)$$ ghi lại toàn bộ cấu hình của máy tại một thời điểm: trạng thái hiện tại $$q$$, phần chuỗi đầu vào còn lại $$w$$ và nội dung ngăn xếp $$\gamma$$.

</div>

## Ví dụ ngôn ngữ $$a^nb^n$$

Để nhận dạng chuỗi $$a^nb^n$$, máy đẩy một ký hiệu $$A$$ vào ngăn xếp cho mỗi ký tự $$a$$ đọc được, sau đó lấy ra (*pop*) một ký hiệu $$A$$ cho mỗi ký tự $$b$$ tương ứng, và chấp nhận khi ngăn xếp rỗng hoặc đạt trạng thái kết thúc.

## Sự tương đương giữa hai chế độ chấp nhận

Hai chế độ chấp nhận — theo ngăn xếp rỗng và theo trạng thái kết thúc — có sức mạnh hoàn toàn tương đương nhau (có thể chuyển đổi qua lại bằng phép dựng chuẩn trong Hopcroft hoặc Sipser).

### Minh họa PDA: ngăn xếp từng bước

Theo dõi từng nhánh tính toán của PDA với chuỗi đầu vào, trạng thái và nội dung ngăn xếp thay đổi qua mỗi bước chuyển (bao gồm ví dụ không đơn định $$ww^R$$):

<div class="interactive-demo" markdown="1">
<div data-demo="pda-explainer" data-preset="anbn"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. Xây dựng PDA nhận ngôn ngữ các chuỗi ngoặc cân bằng.
2. Giải thích vì sao DFA không đủ khả năng nhận dạng ngôn ngữ $$a^nb^n$$ như PDA.
3. Thảo luận vai trò của tính không đơn định (*nondeterminism*) trong PDA — khác gì so với DFA/NFA?

## Tài liệu đọc thêm

Sipser §2.2; Hopcroft–Ullman.

## Tóm tắt

PDA mở rộng ô-tô-mát hữu hạn bằng một ngăn xếp không giới hạn, cho phép nhận dạng các cấu trúc lồng nhau như $$a^nb^n$$.

**Bài tiếp theo:** Tương đương giữa CFG và PDA.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=4ejIAmp_Atw">Pushdown Automata (Introduction)</a> — Neso Academy, tiếng Anh. Giới thiệu trực quan về PDA: bộ điều khiển trạng thái kết hợp ngăn xếp.
- <a href="https://www.youtube.com/watch?v=JtRyd7Svlew">Pushdown Automata (Formal Definition)</a> — Neso Academy, tiếng Anh. Định nghĩa hình thức tương ứng với bộ bảy trong bài.
- <a href="https://www.youtube.com/watch?v=eY7fwj5jvC4">Pushdown Automata (Graphical Notation)</a> — Neso Academy, tiếng Anh. Cách đọc sơ đồ chuyển của PDA cùng ví dụ dạng $$a^n b^n$$.
