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

## Định nghĩa

$$P=(Q,\Sigma,\Gamma,\delta,q_0,Z_0,F)$$,  
$$\delta:Q\times(\Sigma\cup\{\varepsilon\})\times\Gamma\to\mathcal{P}(Q\times\Gamma^*)$$ (hữu hạn ảnh).

**ID** $$(q,w,\gamma)$$: trạng thái, input còn, stack.

## Ví dụ $$a^nb^n$$

Đẩy $$A$$ cho mỗi $$a$$; pop cho mỗi $$b$$; accept empty/final.

## Tương đương chấp nhận

Empty stack ≡ final state (construction chuẩn Hopcroft/Sipser).

## Bài tập

1. PDA ngoặc.  
2. Vì sao DFA không đủ.  
3. Nondeterminism trong PDA quan trọng?

## Đọc

Sipser §2.2; Hopcroft.

## Tóm tắt

Stack · ID · $$a^nb^n$$.

**Tiếp:** CFG ≡ PDA.
