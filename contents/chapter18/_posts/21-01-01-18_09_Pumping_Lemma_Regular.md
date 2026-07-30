---
layout: post
title: "Bổ đề Bơm cho Ngôn ngữ Chính quy"
categories: chapter18
date: 2021-01-01
order: 9
required: true
lang: en
excerpt: "Phát biểu; chứng minh từ DFA; ứng dụng 0ⁿ1ⁿ; checklist phản chứng."
---


<div class="textbook-epigraph" markdown="1">

"If it is regular, long enough strings pump — use that to kill candidates."

<span class="epigraph-attribution">— Pumping lemma</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** và **chứng minh** pumping lemma.
- **Chứng minh** $$\{0^n1^n\}$$ không chính quy.
- **Áp dụng** checklist phản chứng.

</div>

## Định lý

<div class="textbook-theorem" markdown="1">

**Bổ đề bơm (regular).** Nếu $$L$$ chính quy thì ∃ $$p\ge 1$$: mọi $$w\in L$$, $$\lvert w\rvert\ge p$$, phân hoạch $$w=xyz$$ với  
(1) $$xy^kz\in L$$ $$\forall k\ge 0$$;  
(2) $$\lvert y\rvert\ge 1$$;  
(3) $$\lvert xy\rvert\le p$$.

</div>

**Chứng minh.** Cho DFA $$p=\lvert Q\rvert$$. $$w=a_1\ldots a_n$$, $$n\ge p$$. Dãy $$p+1$$ trạng thái trên tiền tố độ dài $$\le p$$: lặp $$q_i=q_j$$, $$0\le i<j\le p$$.  
$$x$$ đến $$i$$, $$y$$ từ $$i$$ đến $$j$$, $$z$$ còn lại. Bơm = quay vòng. $$\square$$

## Ứng dụng

<div class="textbook-theorem" markdown="1">

**Định lý.** $$L=\{0^n1^n:n\ge 0\}$$ không chính quy.

</div>

**Chứng minh.** Giả sử chính quy, lấy $$p$$. $$w=0^p1^p=xyz$$, $$\lvert xy\rvert\le p\Rightarrow y=0^{t}$$, $$t\ge 1$$. $$k=2$$: $$0^{p+t}1^p\notin L$$. $$\square$$

## Checklist

Chọn $$w$$ phụ thuộc $$p$$ · mọi phân hoạch · một $$k$$ phá.

## Bài tập

1. $$\{ww\}$$ không regular.  
2. $$\{0^{n!}$$} — cẩn thận; dùng Myhill–Nerode tốt hơn.  
3. Pumping là điều kiện **cần** không đủ — ví dụ discussion Sipser.

## Đọc

Sipser §1.4; Hopcroft.

## Tóm tắt

Pump từ chu trình DFA · phản chứng chuẩn.

**Tiếp:** đóng regular.
