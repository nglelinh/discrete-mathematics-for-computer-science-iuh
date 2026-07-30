---
layout: post
title: "Subset Construction: NFA ≡ DFA"
categories: chapter18
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Định lý tương đương; chứng minh L(D)=L(N); bound 2^|Q|; reachable only."
---


<div class="textbook-epigraph" markdown="1">

"Powerset construction trades nondeterminism for exponentially many states."

<span class="epigraph-attribution">— Rabin–Scott</span>

</div>

![Subset](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_subset_construction.svg)

<p class="textbook-figure-caption" data-figure="18.3">Trạng thái DFA = tập trạng thái NFA.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Xây** DFA từ NFA (có/không ε).
- **Chứng minh** $$L(D)=L(N)$$.
- **Nêu** bound $$2^{\lvert Q\rvert}$$.

</div>

## 1. Construction (không ε)

$$Q_D=\mathcal{P}(Q_N)$$ (hoặc chỉ reachable).  
$$q_{D0}=\{q_0\}$$.  
$$\delta_D(S,a)=\bigcup_{q\in S}\delta_N(q,a)$$.  
$$F_D=\{S:S\cap F_N\neq\emptyset\}$$.

**Có ε:** $$q_{D0}=E(\{q_0\})$$; $$\delta_D(S,a)=E(\bigcup\delta_N(q,a))$$.

## 2. Định lý

<div class="textbook-theorem" markdown="1">

**Định lý** (Rabin–Scott). Với mọi NFA $$N$$ tồn tại DFA $$D$$: $$L(D)=L(N)$$ và $$\lvert Q_D\rvert\le 2^{\lvert Q_N\rvert}$$.

</div>

**Chứng minh.**  
Bất biến: sau đọc $$w$$, trạng thái $$D$$ là $$\hat\delta_N(\{q_0\},w)$$ (hoặc closure). Quy nạp độ dài $$w$$.  
Chấp nhận ⇔ giao $$F\neq\emptyset$$ ⇔ $$w\in L(N)$$.  
Số tập con $$\le 2^{\lvert Q\rvert}$$. $$\square$$

## 3. State explosion

Tồn tại family ngôn ngữ DFA tối tiểu $$\Omega(2^n)$$ trong khi NFA $$O(n)$$ (ví dụ “ký tự thứ $$n$$ từ cuối là 1”).

## Bài tập

1. Chạy subset trên NFA ends-01; liệt kê reachable.  
2. Chứng minh chỉ cần reachable subset.  
3. Tìm example explosion (Sipser).

## Đọc

Sipser §1.2; Hopcroft–Ullman.

## Tóm tắt

Powerset · $$L$$ bảo toàn · $$2^n$$ bound.

**Tiếp:** Mealy/Moore.
