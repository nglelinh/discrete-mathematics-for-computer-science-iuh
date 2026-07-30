---
layout: post
title: "Bảng chữ cái, Chuỗi và Ngôn ngữ"
categories: chapter19
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Σ, w, ε, Σ*; định nghĩa L; ghép chuỗi."
---


<div class="textbook-epigraph" markdown="1">

"A language is a set of strings over an alphabet."

<span class="epigraph-attribution">— Formal language theory</span>

</div>

![Σ*](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_sigma_star.svg)

<p class="textbook-figure-caption" data-figure="19.1">$$L\subseteq\Sigma^*$$.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** alphabet, string, language.
- **Chứng minh** đẳng thức cơ bản về ghép/độ dài.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

$$\Sigma$$ hữu hạn ≠∅.  
Chuỗi: dãy hữu hạn; $$\varepsilon$$; $$\lvert w\rvert$$.  
$$\Sigma^*=\bigcup_{k\ge 0}\Sigma^k$$, $$\Sigma^0=\{\varepsilon\}$$.  
**Ngôn ngữ:** $$L\subseteq\Sigma^*$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** $$\lvert xy\rvert=\lvert x\rvert+\lvert y\rvert$$; $$(xy)z=x(yz)$$; $$w\varepsilon=\varepsilon w=w$$.

</div>

**Chứng minh.** Theo định nghĩa dãy hữu hạn / nối. $$\square$$

## Bài tập

1. Liệt kê $$\Sigma^{\le 2}$$ với $$\Sigma=\{a,b\}$$.  
2. Chứng minh $$\lvert w^R\rvert=\lvert w\rvert$$.  
3. $$\emptyset$$ vs $$\{\varepsilon\}$$.

## Đọc

Sipser §0–1; Hopcroft §1.

## Tóm tắt

Σ · chuỗi · $$L\subseteq\Sigma^*$$.

**Tiếp:** phép toán ngôn ngữ.
