---
layout: post
title: "Phép toán trên Ngôn ngữ"
categories: chapter19
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Hợp giao bù ghép star; chứng minh đẳng thức; ví dụ."
---


<div class="textbook-epigraph" markdown="1">

"Language operations are set operations with concatenation structure."

<span class="epigraph-attribution">— Algebra of languages</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Thực hiện** ∪ ∩ ¯ · *.
- **Chứng minh** một số đẳng thức.

</div>

## Định nghĩa

$$L_1L_2=\{xy:x\in L_1,y\in L_2\}$$,  
$$L^*=\bigcup_{k\ge 0}L^k$$, $$L^0=\{\varepsilon\}$$, $$L^+=LL^*$$.

## Định lý

<div class="textbook-theorem" markdown="1">

**Định lý.**  
(1) $$L\emptyset=\emptyset L=\emptyset$$.  
(2) $$L\{\varepsilon\}=\{\varepsilon\}L=L$$.  
(3) $$(L_1\cup L_2)L_3=L_1L_3\cup L_2L_3$$.  
(4) $$(L^*)^*=L^*$$.

</div>

**Chứng minh (4).** $$L^*\subseteq(L^*)^*$$ vì $$A\subseteq A^*$$.  
$$(L^*)^*\subseteq L^*$$: phần tử là ghép các từ trong $$L^*$$, mỗi từ là ghép từ $$L$$ ⇒ thuộc $$L^*$$. $$\square$$

## Bài tập

1. Chứng minh (3).  
2. Đưa phản ví dụ $$(L_1L_2)^*=L_1^*L_2^*$$ (sai).  
3. $$L^+$$ vs $$L^*$$ khi $$\varepsilon\in L$$.

## Đọc

Sipser; Hopcroft.

## Tóm tắt

Đại số ngôn ngữ · star lũy đẳng.

**Tiếp:** grammar.
