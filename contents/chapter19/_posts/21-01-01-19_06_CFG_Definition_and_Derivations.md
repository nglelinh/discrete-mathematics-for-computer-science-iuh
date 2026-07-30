---
layout: post
title: "Văn phạm Phi ngữ cảnh (CFG)"
categories: chapter19
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "A→α; leftmost derivation; ví dụ ngoặc và biểu thức."
---


<div class="textbook-epigraph" markdown="1">

"One nonterminal rewrite at a time — that is context-free."

<span class="epigraph-attribution">— CFG</span>

</div>

![CFG](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_cfg_parens.svg)

<p class="textbook-figure-caption" data-figure="19.3">Ngoặc cân bằng — CFG cổ điển.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** CFG.
- **Viết** leftmost derivation.
- **Chứng minh** $$L(G)=\{a^nb^n\}$$ cho grammar chuẩn.

</div>

## Định nghĩa

Mọi production $$A\to\alpha$$, $$A\in V$$, $$\alpha\in(V\cup\Sigma)^*$$.

## Ví dụ

$$S\to(S)S\mid\varepsilon$$.  
$$S\to aSb\mid\varepsilon$$ ⇒ $$\{a^nb^n\}$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** $$G: S\to aSb\mid\varepsilon$$ có $$L(G)=\{a^nb^n:n\ge 0\}$$.

</div>

**Chứng minh.**  
(⊆) Quy nạp dẫn xuất: mỗi lần $$aSb$$ thêm cặp.  
(⊇) $$a^nb^n$$: $$n$$ lần $$aSb$$ rồi ε. $$\square$$

## Bài tập

1. Derivation $$()(() )$$.  
2. CFG biểu thức $$E\to E+E\mid E*E\mid(E)\mid\mathrm{id}$$ — ambiguity.  
3. So $$a^nb^n$$ vs regular.

## Đọc

Sipser §2.1.

## Tóm tắt

CFG · derivation · $$a^nb^n$$.

**Tiếp:** parse tree & ambiguity.
