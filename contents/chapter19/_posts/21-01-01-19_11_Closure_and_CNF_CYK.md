---
layout: post
title: "Đóng CFL, CNF và CYK"
categories: chapter19
date: 2021-01-01
order: 11
required: true
lang: en
excerpt: "Đóng hợp ghép star; không đóng giao/bù; CNF; thuật toán CYK + đúng đắn khung."
---


<div class="textbook-epigraph" markdown="1">

"CFLs are closed under union, not under intersection."

<span class="epigraph-attribution">— Classic contrast with regular</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** đóng ∪, ·, * cho CFL.
- **Chứng minh** không đóng ∩ (dùng $$a^nb^nc^n$$).
- **Mô tả** CNF và CYK $$O(n^3)$$.

</div>

## Đóng

**∪ · *:** construction grammar (start mới).  
**Homomorphism, reverse:** có.  

<div class="textbook-theorem" markdown="1">

**Định lý.** CFL **không** đóng với ∩ và bù.

</div>

**Chứng minh.** $$L_1=\{a^nb^nc^m\}$$, $$L_2=\{a^nb^mc^m\}$$ CFL nhưng $$L_1\cap L_2=\{a^nb^nc^n\}$$ không CFL.  
Bù: nếu đóng bù và ∪ thì đóng ∩. $$\square$$

## CNF

$$A\to BC$$ hoặc $$A\to a$$ (Sipser transform).

## CYK

DP $$X_{i,j}$$ nonterminal sinh $$w_{i..i+j-1}$$.  
Thời gian $$O(n^3\lvert P\rvert)$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** CYK đúng: $$S\in X_{1,n}\Leftrightarrow w\in L(G)$$ ($$G$$ CNF).

</div>

**Ý:** quy nạp độ dài substring. $$\square$$

## Bài tập

1. Chứng minh không đóng ∩ đầy đủ.  
2. Chạy CYK trên ví dụ nhỏ.  
3. Vì sao regular đóng ∩ mà CFL không?

## Đọc

Sipser §2.3; Hopcroft CYK; Grune parsing.

## Tóm tắt

Đóng/không đóng · CNF · CYK ∈ P.

**Tiếp:** compiler.
