---
layout: post
title: "ε-NFA và Epsilon-closure"
categories: chapter18
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Chuyển ε; định nghĩa E(S); thuật toán tính closure; chấp nhận."
---


<div class="textbook-epigraph" markdown="1">

"ε-moves stitch machines together — Kleene’s algebra becomes automata."

<span class="epigraph-attribution">— Thompson construction spirit</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** ε-NFA và $$E(S)$$.
- **Chứng minh** tính chất closure.
- **Tính** $$E(S)$$ bằng DFS/BFS trên cạnh ε.

</div>

## 1. Định nghĩa

$$\delta:Q\times(\Sigma\cup\{\varepsilon\})\to\mathcal{P}(Q)$$.

<div class="textbook-definition" markdown="1">

**Epsilon-closure** $$E(S)$$: mọi trạng thái tới được từ $$S$$ chỉ bằng cạnh ε (gồm $$S$$).

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** $$E(E(S))=E(S)$$; $$S\subseteq E(S)$$; $$S\subseteq T\Rightarrow E(S)\subseteq E(T)$$.

</div>

**Chứng minh.** Tính chất bao đóng phản xạ-bắc cầu của quan hệ “có đường ε”. $$\square$$

## 2. Chấp nhận

Đọc $$a$$: $$S' = E\bigl(\bigcup_{q\in S}\delta(q,a)\bigr)$$.  
Bắt đầu $$E(\{q_0\})$$; chấp nhận nếu giao $$F\neq\emptyset$$.

## 3. Thuật toán

Stack/queue từ $$S$$, đi theo cạnh ε, đánh dấu visited — $$O(\lvert Q\rvert+\lvert E_\varepsilon\rvert)$$.

## Bài tập

1. Chứng minh ba tính chất $$E$$.  
2. Vẽ ε-NFA hợp hai DFA bằng ε từ start mới.  
3. Vì sao ε không tăng sức mạnh? (preview subset)

## Đọc

Sipser; Hopcroft ε-removal.

## Tóm tắt

$$E(S)$$ · chấp nhận có ε · ghép máy.

**Tiếp:** subset construction.
