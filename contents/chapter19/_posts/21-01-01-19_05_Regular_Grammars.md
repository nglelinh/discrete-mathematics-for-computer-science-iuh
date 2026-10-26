---
layout: post
title: "Văn phạm Chính quy ≡ Ngôn ngữ Chính quy"
categories: chapter19
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Right-linear grammar; chứng minh khung ≡ NFA; liên hệ Ch.18."
---


<div class="textbook-epigraph" markdown="1">

"Right-linear rules are finite automata in disguise."

<span class="epigraph-attribution">— Grammar–automaton bridge</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** right/left linear.
- **Chứng minh khung** regular grammar ≡ NFA.

</div>

## Định nghĩa

Right-linear: $$A\to wB$$ hoặc $$A\to w$$ ($$w\in\Sigma^*$$).  
(Thường $$w$$ single symbol sau chuẩn hóa.)

## Định lý

<div class="textbook-theorem" markdown="1">

**Định lý.** $$L$$ regular ⇔ $$L=L(G)$$ với right-linear $$G$$.

</div>

**Ý chứng minh.**  
Grammar→NFA: nonterminal = state; $$A\to aB$$ cạnh $$a$$.  
NFA→grammar: ngược. $$\square$$

## Bài tập

1. Grammar từ DFA parity.  
2. Chứng minh chi tiết một chiều.  
3. Left-linear cũng regular.

## Đọc

Hopcroft; Sipser exercises.

## Tóm tắt

Type-3 ≡ Ch.18 regular.

**Tiếp:** CFG.

## Video tham khảo

- **xem trước** <a href="https://www.youtube.com/watch?v=WgEsPTAL55Q">Regular Grammar</a> — Neso Academy, tiếng Anh. Xem trước văn phạm chính quy và dạng luật.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Dẫn xuất một xâu từ văn phạm.
- <a href="https://www.youtube.com/watch?v=upu_TeZImN0">Regular Expression</a> — Neso Academy, tiếng Anh. Biểu thức chính quy, ngôn ngữ cùng lớp với văn phạm chính quy.
