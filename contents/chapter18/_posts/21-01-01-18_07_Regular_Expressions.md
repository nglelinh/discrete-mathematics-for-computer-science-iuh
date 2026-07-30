---
layout: post
title: "Biểu thức Chính quy"
categories: chapter18
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Định nghĩa đệ quy regex; L(r); ví dụ; liên hệ ngôn ngữ."
---


<div class="textbook-epigraph" markdown="1">

"Regular expressions are the algebra of finite automata."

<span class="epigraph-attribution">— Kleene</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** regex và $$L(r)$$.
- **Dịch** mô tả ngôn ngữ ↔ regex đơn giản.

</div>

## Định nghĩa

**Cơ sở:** $$\emptyset$$, $$\varepsilon$$, $$a\in\Sigma$$.  
**Toán tử:** $$r+s$$ (hợp), $$rs$$ (ghép), $$r^*$$ (sao).

$$L(\emptyset)=\emptyset,\quad L(\varepsilon)=\{\varepsilon\},\quad L(a)=\{a\}.$$

$$L(r+s)=L(r)\cup L(s),\quad L(rs)=L(r)L(s),\quad L(r^*)=\bigcup_{k\ge 0}L(r)^k.$$

*(Tránh align nếu build lỗi — dùng bullet nếu cần.)*

## Ví dụ

$$(0+1)^*$$, $$0^*1^*$$, $$(0+1)^*01$$, $$(01)^*$$.

## Bài tập

1. Regex: chẵn số 0 (trên $$\{0,1\}$$) — khó hơn nghĩ; dùng DFA trước.  
2. Chứng minh $$L(r^*)=L(\varepsilon+rr^*)$$.  
3. Phân biệt regex lý thuyết vs PCRE (backref).

## Đọc

Sipser §1.3.

## Tóm tắt

Algebra · $$L(r)$$ · ba toán tử.

**Tiếp:** Kleene theorem.
