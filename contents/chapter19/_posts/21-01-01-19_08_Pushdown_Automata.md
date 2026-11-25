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

Nếu bạn trao cho một máy trạng thái hữu hạn (NFA) đúng một công cụ bổ sung duy nhất — một chiếc **ngăn xếp (stack)** chỉ cho phép đẩy vào và lấy ra ở đỉnh — sức mạnh của chiếc máy lập tức nhảy vọt từ ngôn ngữ chính quy lên toàn bộ ngôn ngữ phi ngữ cảnh. Chiếc máy đó chính là **Automat đẩy xuống (Pushdown Automaton — PDA)**, mô hình toán học đứng sau mọi bộ phân tích cú pháp (parser) trong trình biên dịch.

## Bản đồ kiến thức nền: Ba trụ cột của Automat Đẩy xuống (PDA)

1. **Hàm chuyển bộ ba $$\delta(q, a, X) \ni (p, \gamma)$$**:
   Tại trạng thái $$q$$, đọc ký hiệu vào $$a$$ (hoặc $$\varepsilon$$) và lấy ký hiệu $$X$$ trên đỉnh ngăn xếp, PDA chuyển sang trạng thái $$p$$ rồi đẩy chuỗi $$\gamma$$ thay vào đỉnh ngăn xếp ($$\gamma = \varepsilon$$ nghĩa là *pop* thuần túy).
2. **Hai chế độ chấp nhận tương đương (Trạng thái cuối vs. Ngăn xếp rỗng)**:
   PDA có thể chấp nhận khi kết thúc chuỗi ở trạng thái $$q \in F$$ hoặc khi ngăn xếp trống rỗng hoàn toàn. Hai cơ chế này có sức mạnh hoàn toàn tương đương trên lớp CFL (có thể chuyển đổi qua lại).
3. **Bất đối xứng quan trọng: DPDA $$\subsetneq$$ NPDA**:
   Khác hẳn DFA = NFA, với PDA tính không đơn định thực sự **làm tăng sức mạnh**: ngôn ngữ đối xứng không có dấu giữa $$L = \{ww^R \mid w \in \{a,b\}^*\}$$ được nhận bởi NPDA (đoán điểm giữa), nhưng không có DPDA nào nhận được!

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

### Khung giải thích (nên đọc chậm): Chạy tay ngăn xếp PDA trên chuỗi `aabb`

Xét PDA nhận $$L = \{a^n b^n \mid n \ge 1\}$$ với ký hiệu đáy ngăn xếp $$Z_0$$:
- Ở $$q_0$$: gặp `a` thì đẩy `A` lên đỉnh ngăn xếp.
- Khi gặp `b` đầu tiên (đỉnh là `A`): xóa `A` và chuyển sang $$q_1$$.
- Ở $$q_1$$: mỗi `b` xóa 1 ký hiệu `A`; khi hết chuỗi và thấy lại đáy $$Z_0$$, chuyển sang trạng thái chấp nhận $$q_f$$.

Theo dõi từng cấu hình $$(q, \text{phần chuỗi còn lại}, \text{ngăn xếp từ đỉnh xuống đáy})$$ với đầu vào `aabb`:

| Bước | Trạng thái | Chuỗi còn lại | Ngăn xếp (đỉnh bên trái) | Thao tác |
| :---: | :---: | :---: | :---: | :--- |
| 0 | $$q_0$$ | `aabb` | $$Z_0$$ | Khởi đầu |
| 1 | $$q_0$$ | `abb` | $$A Z_0$$ | Đọc `a`, đẩy `A` |
| 2 | $$q_0$$ | `bb` | $$A A Z_0$$ | Đọc `a`, đẩy `A` |
| 3 | $$q_1$$ | `b` | $$A Z_0$$ | Đọc `b`, xóa `A`, sang $$q_1$$ |
| 4 | $$q_1$$ | $$\varepsilon$$ | $$Z_0$$ | Đọc `b`, xóa `A` |
| 5 | $$q_f$$ | $$\varepsilon$$ | $$Z_0$$ | Chuyển $$\varepsilon$$ khi gặp $$Z_0$$ → **Chấp nhận!** |

Nếu đầu vào là `aab`, bước 4 hết chuỗi nhưng ngăn xếp vẫn còn `A Z_0` (chưa thấy $$Z_0$$), nên máy từ chối!

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
