---
layout: post
title: "Bổ đề Bơm CFL"
categories: chapter19
date: 2021-01-01
order: 10
required: true
lang: en
excerpt: "Phát biểu; ý chứng minh parse tree; aⁿbⁿcⁿ không CFL."
---


<div class="textbook-epigraph" markdown="1">

"Long parse trees repeat a nonterminal on a root-to-leaf path."

<span class="epigraph-attribution">— CFL pumping</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** pumping lemma CFL.
- **Chứng minh** $$\{a^nb^nc^n\}$$ không CFL.
- **Checklist** phản chứng.

</div>

## Định lý

<div class="textbook-theorem" markdown="1">

**Bổ đề bơm CFL.** Nếu $$L$$ CFL thì ∃ $$p$$: mọi $$w\in L$$, $$\lvert w\rvert\ge p$$, $$w=uvxyz$$ với  
(1) $$uv^kxy^kz\in L$$ $$\forall k\ge 0$$;  
(2) $$\lvert vy\rvert\ge 1$$;  
(3) $$\lvert vxy\rvert\le p$$.

</div>

**Ý chứng minh.** CNF grammar; parse tree cao ⇒ lặp nonterminal trên path; bơm subtree. $$\square$$

## Ứng dụng

<div class="textbook-theorem" markdown="1">

**Định lý.** $$L=\{a^nb^nc^n:n\ge 0\}$$ không CFL.

</div>

**Chứng minh.** $$w=a^pb^pc^p$$. $$vxy$$ nằm trong cửa sổ ≤$$p$$ ⇒ không chạm cả 3 khối chữ cái đủ cách; bơm phá cân bằng 3 số. (Chi tiết case analysis Sipser.) $$\square$$

## Bài tập

1. $$\{ww\}$$ không CFL.  
2. So pump regular vs CFL (2 đoạn vs 2 chỗ).  
3. Ogden’s lemma (định hướng).

## Đọc

Sipser §2.3.

## Tóm tắt

Pump CFL · $$a^nb^nc^n$$.

**Tiếp:** đóng CFL.
