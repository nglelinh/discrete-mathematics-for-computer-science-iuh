---
layout: post
title: "Thiết kế DFA và Chứng minh Tính đúng"
categories: chapter18
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Phương pháp bất biến; ví dụ ends-with, contains; chứng minh L(M)=L."
---


<div class="textbook-epigraph" markdown="1">

"A correct automaton is a theorem: states are invariants."

<span class="epigraph-attribution">— Design by invariant</span>

</div>

Thiết kế DFA = chọn **bất biến** cho mỗi trạng thái, rồi chứng minh $$L(M)=L$$ hai chiều.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Thiết kế** DFA bằng invariant.
- **Chứng minh** $$L(M)\subseteq L$$ và $$L\subseteq L(M)$$.

</div>

## 1. Quy trình

1. Mô tả $$L\subseteq\Sigma^*$$ bằng tính chất.  
2. Phân lớp tiền tố theo “thông tin cần nhớ” (hữu hạn).  
3. Gán trạng thái = lớp; $$\delta$$ cập nhật bất biến.  
4. $$F$$ = lớp thỏa thuộc $$L$$.  
5. Chứng minh bất biến + kết thúc.

## 2. Ví dụ: kết thúc bằng $$01$$

Trạng thái: $$q_\varepsilon,q_0,q_{01}$$ (và sink reject nếu cần).  
Bất biến: “hậu tố liên quan đến tiền tố của $$01$$”.

<div class="textbook-theorem" markdown="1">

**Định lý.** DFA xây đúng nhận $$L=\{w:w\text{ kết thúc }01\}$$.

</div>

**Chứng minh (khung).**  
(⇒) Bất biến: vào $$q_{01}$$ ⇔ đã đọc …01.  
(⇐) Mọi $$w\in L$$ buộc đường chạy kết thúc $$q_{01}$$. Chi tiết theo quy nạp độ dài. $$\square$$

## 3. Ví dụ: chẵn số $$1$$

$$q_0$$: chẵn; $$q_1$$: lẻ. $$F=\{q_0\}$$.

**Bất biến:** $$\hat\delta(q_0,w)=q_0\Leftrightarrow\#_1(w)$$ chẵn — quy nạp hiển nhiên.

## Bài tập

1. DFA “chứa $$aa$$” + chứng minh.  
2. DFA “độ dài $$\equiv 0\pmod 3$$”.  
3. Chứng minh không cần “đoán”: so với NFA sau.

## Đọc

Sipser exercises 1.1–1.6; Hopcroft design examples.

## Tóm tắt

Invariant · hai chiều $$L(M)=L$$.

**Tiếp:** NFA.
