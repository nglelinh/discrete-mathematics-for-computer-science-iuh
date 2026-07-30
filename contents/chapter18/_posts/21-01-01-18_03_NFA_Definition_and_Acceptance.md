---
layout: post
title: "NFA: Định nghĩa và Chấp nhận"
categories: chapter18
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "δ đa trị; đường chạy; L(N); so sánh DFA; ví dụ ends-with."
---


<div class="textbook-epigraph" markdown="1">

"Nondeterminism is a design convenience with a deterministic cost."

<span class="epigraph-attribution">— Automata theory</span>

</div>

![NFA](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_nfa_ends_01.svg)

<p class="textbook-figure-caption" data-figure="18.2">NFA kết thúc bằng 01: đoán khi bắt đầu khớp.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** NFA và $$L(N)$$.
- **Chứng minh** $$L$$ NFA đơn giản bằng tồn tại đường.

</div>

## 1. Định nghĩa

<div class="textbook-definition" markdown="1">

**NFA:** $$N=(Q,\Sigma,\delta,q_0,F)$$ với $$\delta:Q\times\Sigma\to\mathcal{P}(Q)$$.

**Chấp nhận** $$w$$: ∃ dãy trạng thái $$q_0,q_1,\ldots,q_n$$ với $$q_{i}\in\delta(q_{i-1},a_i)$$ và $$q_n\in F$$.

$$L(N)=\{w:\text{được chấp nhận}\}.$$

</div>

## 2. Mở rộng $$\hat\delta$$ tập

$$\hat\delta(S,\varepsilon)=S$$, $$\hat\delta(S,a)=\bigcup_{q\in S}\delta(q,a)$$, mở rộng chuỗi.  
$$w\in L(N)\Leftrightarrow\hat\delta(\{q_0\},w)\cap F\neq\emptyset$$.

## 3. Vì sao NFA “gọn”

Mẫu “kết thúc bằng $$x$$” / “chứa một trong nhiều pattern”: NFA đoán điểm bắt đầu; DFA nhớ hậu tố (có thể nhiều trạng thái hơn trước khi tối tiểu).

## Bài tập

1. Chứng minh $$1101\in L$$ NFA ends-01 bằng một đường.  
2. Viết $$\delta$$ đầy đủ bảng.  
3. So sánh số trạng thái NFA vs DFA tối tiểu (thảo luận).

## Đọc

Sipser §1.2.

## Tóm tắt

Đa trị · tồn tại đường · $$L(N)$$.

**Tiếp:** ε-NFA.
