---
layout: post
title: "Automat Đẩy xuống (PDA)"
categories: chapter19
date: 2021-01-01
order: 8
required: true
lang: en
excerpt: "Định nghĩa PDA; ID; chấp nhận empty stack/final state; ví dụ aⁿbⁿ."
---


<div class="textbook-epigraph" markdown="1">

"A stack is exactly the memory context-free languages need."

<span class="epigraph-attribution">— PDA</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** PDA.
- **Mô phỏng** $$a^nb^n$$.
- **Phân biệt** accept by empty stack vs final state.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">
**Định nghĩa**:

$$P=(Q,\Sigma,\Gamma,\delta,q_0,Z_0,F)$$,  
$$\delta:Q\times(\Sigma\cup\{\varepsilon\})\times\Gamma\to\mathcal{P}(Q\times\Gamma^*)$$ (hữu hạn ảnh).

**ID** $$(q,w,\gamma)$$: trạng thái, input còn, stack.
</div>

## Ví dụ $$a^nb^n$$

Đẩy $$A$$ cho mỗi $$a$$; pop cho mỗi $$b$$; accept empty/final.

## Tương đương chấp nhận

Empty stack ≡ final state (construction chuẩn Hopcroft/Sipser).

### Minh hoạ PDA: ngăn xếp từng bước

Theo dõi một nhánh tính toán của PDA: chuỗi vào, trạng thái và ngăn xếp thay đổi theo từng chuyển tiếp (có ví dụ không tất định wwᴿ).

<div class="interactive-demo" markdown="1">
<div data-demo="pda-explainer" data-preset="anbn"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. PDA ngoặc.  
2. Vì sao DFA không đủ.  
3. Nondeterminism trong PDA quan trọng?

## Đọc

Sipser §2.2; Hopcroft.

## Tóm tắt

Stack · ID · $$a^nb^n$$.

**Tiếp:** CFG ≡ PDA.

## Video tham khảo

- **xem trước** <a href="https://www.youtube.com/watch?v=4ejIAmp_Atw">Pushdown Automata (Introduction)</a> — Neso Academy, tiếng Anh. Xem trước PDA: trạng thái cộng ngăn xếp.
- <a href="https://www.youtube.com/watch?v=JtRyd7Svlew">Pushdown Automata (Formal Definition)</a> — Neso Academy, tiếng Anh. Định nghĩa hình thức, đúng bộ bảy của bài.
- <a href="https://www.youtube.com/watch?v=eY7fwj5jvC4">Pushdown Automata (Graphical Notation)</a> — Neso Academy, tiếng Anh. Đọc sơ đồ chuyển của PDA, gồm ví dụ dạng a^n b^n.
