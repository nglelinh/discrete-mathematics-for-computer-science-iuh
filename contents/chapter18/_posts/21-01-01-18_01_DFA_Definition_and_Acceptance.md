---
layout: post
title: "Định nghĩa DFA và Ngôn ngữ Chấp nhận"
categories: chapter18
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Bộ năm DFA; δ̂; L(M); sơ đồ/bảng; acceptor."
---


<div class="textbook-epigraph" markdown="1">

"A finite automaton is a mathematical model of computation with a finite amount of memory."

<span class="epigraph-attribution">— Hopcroft & Ullman spirit</span>

</div>

Máy hữu hạn trạng thái là mô hình tính toán với **bộ nhớ hữu hạn** (tập trạng thái). Mục này cố định định nghĩa **DFA** và ngôn ngữ nó nhận — nền cho cả chương automata.

![DFA chẵn 1](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_dfa_even_ones.svg)

<p class="textbook-figure-caption" data-figure="18.1">DFA parity: chấp nhận chuỗi nhị phân có chẵn số bit 1.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** $$M=(Q,\Sigma,\delta,q_0,F)$$.
- **Mở rộng** $$\hat\delta$$ và định nghĩa $$L(M)$$.
- **Chứng minh** tính duy nhất đường chạy trên DFA.

</div>

## 1. Định nghĩa

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **DFA** là bộ năm $$M=(Q,\Sigma,\delta,q_0,F)$$ với $$Q,\Sigma$$ hữu hạn khác rỗng; $$\delta:Q\times\Sigma\to Q$$ **toàn phần**; $$q_0\in Q$$; $$F\subseteq Q$$.

</div>

## 2. Hàm chuyển mở rộng

<div class="textbook-definition" markdown="1">

**Định nghĩa.** $$\hat\delta:Q\times\Sigma^*\to Q$$:

$$
\hat\delta(q,\varepsilon)=q,\qquad
\hat\delta(q,wa)=\delta\bigl(\hat\delta(q,w),a\bigr).
$$

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (đường chạy duy nhất). Với mọi $$q,w$$ tồn tại duy nhất dãy trạng thái khi đọc $$w$$ từ $$q$$ trên DFA.

</div>

**Chứng minh.** Quy nạp $$\lvert w\rvert$$: bước $$\delta$$ xác định duy nhất. $$\square$$

## 3. Ngôn ngữ

<div class="textbook-definition" markdown="1">

$$L(M)=\{w\in\Sigma^*:\hat\delta(q_0,w)\in F\}.$$  
Ngôn ngữ **chính quy** nếu $$L=L(M)$$ với một DFA $$M$$ (sẽ mở rộng tương đương NFA/regex).

</div>

## 4. Biểu diễn

Sơ đồ: vòng đôi = $$F$$; mũi tên vào $$q_0$$.  
Bảng: hàng trạng thái, cột ký hiệu.

## Bài tập

1. Chứng minh $$\hat\delta(q,xy)=\hat\delta\bigl(\hat\delta(q,x),y\bigr)$$.  
2. DFA parity: chứng minh bằng bất biến “trạng thái = parity số 1 đã đọc”.  
3. Vì sao $$\delta$$ phải total trên DFA chuẩn?

## Đọc

Sipser §1.1; Hopcroft–Ullman; Kozen *Automata*.

## Tóm tắt

DFA · $$\hat\delta$$ · $$L(M)$$ · duy nhất đường chạy.

**Tiếp:** 18.2 thiết kế DFA + chứng minh đúng.
