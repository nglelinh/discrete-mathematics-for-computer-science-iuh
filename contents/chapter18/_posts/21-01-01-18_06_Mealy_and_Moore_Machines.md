---
layout: post
title: "Máy Mealy và Moore"
categories: chapter18
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "Transducer; λ(q) vs ω(q,a); độ dài ra; tương đương sức mạnh (ý+chứng minh khung)."
---


<div class="textbook-epigraph" markdown="1">

"Moore outputs on states; Mealy on edges."

<span class="epigraph-attribution">— Sequential machine theory</span>

</div>

![Mealy Moore](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_mealy_moore.svg)

<p class="textbook-figure-caption" data-figure="18.4">Hai kiểu transducer hữu hạn trạng thái.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** Moore/Mealy.
- **Tính** chuỗi ra.
- **Phác** chuyển Moore↔Mealy.

</div>

## 1. Moore

$$M=(Q,\Sigma,\Delta,\delta,\lambda,q_0)$$, $$\lambda:Q\to\Delta$$.  
Vào $$a_1\ldots a_n$$ → ra $$\lambda(q_0)\ldots\lambda(q_n)$$ độ dài $$n+1$$.

## 2. Mealy

$$\omega:Q\times\Sigma\to\Delta$$.  
Ra $$\omega(q_0,a_1)\ldots\omega(q_{n-1},a_n)$$ độ dài $$n$$.

## 3. Tương đương (khung)

<div class="textbook-theorem" markdown="1">

**Định lý** (tinh thần). Mọi Mealy có Moore tương đương “trễ 1” và ngược lại (mở rộng trạng thái nhớ output).

</div>

**Ý.** Mealy→Moore: trạng thái $$(q,\mathrm{last\_out})$$ hoặc gán $$\lambda$$ theo cạnh vào.  
Moore→Mealy: $$\omega(q,a)=\lambda(\delta(q,a))$$ (bỏ $$\lambda(q_0)$$ đầu nếu chuẩn hóa).

## Bài tập

1. Mealy đảo bit; chứng minh ra = bù từng bit.  
2. So sánh latency phần cứng.  
3. Thiết kế phát hiện `aab` (Mealy hoặc Moore).

## Đọc

Kohavi switching; Hopcroft applications.

## Tóm tắt

Transducer · độ dài ra · mô phỏng.

**Tiếp:** regex.
