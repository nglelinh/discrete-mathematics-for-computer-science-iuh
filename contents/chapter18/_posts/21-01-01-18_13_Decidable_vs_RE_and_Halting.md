---
layout: post
title: "Decidable, RE và Bài toán Dừng"
categories: chapter18
date: 2021-01-01
order: 13
required: true
lang: en
excerpt: "Recursive vs RE; chứng minh khung A_TM RE; Halting undecidable (phác diagonal)."
---


<div class="textbook-epigraph" markdown="1">

"Some problems are not merely hard — they are impossible."

<span class="epigraph-attribution">— Computability</span>

</div>

Nối Ch.18 → Ch.20: không chỉ **khó đa thức**, còn **không quyết định được**.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phân biệt** decidable / RE.
- **Phác** $$A_{\mathrm{TM}}$$ RE nhưng undecidable.
- **Nêu** hệ quả cho verification.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

**Decidable (recursive):** ∃ TM luôn dừng, accept đúng $$L$$.  
**RE (Turing-recognizable):** ∃ TM accept đúng $$L$$ (có thể loop ngoài $$L$$).

</div>

$$\mathrm{decidable}\subsetneq\mathrm{RE}\subsetneq$$ mọi ngôn ngữ.

## $$A_{\mathrm{TM}}$$

$$A_{\mathrm{TM}}=\{\langle M,w\rangle:M\text{ accept }w\}.$$  
**RE:** mô phỏng $$M$$ trên $$w$$.  
**Undecidable:** diagonal / reduction từ $$A_{\mathrm{TM}}$$ (Sipser §4–5).

## Halting

$$\mathrm{HALT}=\{\langle M,w\rangle:M\text{ dừng trên }w\}$$ undecidable.

## Bài tập

1. Chứng minh decidable ⊆ RE.  
2. Nếu $$A_{\mathrm{TM}}$$ decidable thì sao?  
3. Liên hệ “verify program” thực tế.

## Đọc

Sipser §4–5; Davis computability.

## Tóm tắt

Decidable ⊂ RE · halting impossible.

**Tiếp:** lộ trình nghiên cứu automata.
