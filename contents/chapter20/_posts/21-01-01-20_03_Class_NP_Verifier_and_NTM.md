---
layout: post
title: "Lớp NP: Verifier và NTM"
categories: chapter20
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Định nghĩa NP qua verifier và NTIME; chứng minh tương đương; chứng minh P⊆NP; ví dụ certificate."
---

<div class="textbook-epigraph" markdown="1">

"NP is the class of problems with short, efficiently checkable proofs of YES answers."

<span class="epigraph-attribution">— Verifier view of NP</span>

</div>

Trực giác TSP: **kiểm** tour dễ, **tìm** tour khó. $$NP$$ hình thức hóa “Yes có chứng chỉ ngắn”.

![Verifier](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_verifier.svg)

<p class="textbook-figure-caption" data-figure="20.2">$$x\in L$$ ⇔ ∃ chứng chỉ $$c$$ ngắn, $$V(x,c)=\mathrm{Yes}$$.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** $$NP$$ hai cách và **chứng minh** tương đương.
- **Chứng minh** $$P\subseteq NP$$.
- **Viết** certificate + verifier cho SAT, HC, 3-Color.

</div>

## 1. Verifier

<div class="textbook-definition" markdown="1">

**Định nghĩa.** $$L\in NP$$ nếu ∃ đa thức $$p$$ và TM tất định $$V$$:

1. $$V(x,c)$$ chạy trong thời gian $$\mathrm{poly}(\lvert x\rvert)$$ (từ chối nếu $$\lvert c\rvert>p(\lvert x\rvert)$$).  
2. $$x\in L\Rightarrow\exists c$$: $$V(x,c)=1$$.  
3. $$x\notin L\Rightarrow\forall c$$: $$V(x,c)=0$$.

</div>

## 2. NTM

<div class="textbook-definition" markdown="1">

**Định nghĩa.** $$NP=\bigcup_k\mathrm{NTIME}(n^k)$$: NTM chấp nhận $$L$$ trong thời gian đa thức (tồn tại nhánh Yes).

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (tương đương). Verifier ⇔ NTM.

</div>

**Chứng minh.**

*NTM → verifier.* $$c$$ = dãy lựa chọn/cấu hình nhánh; $$V$$ mô phỏng tất định nhánh, kiểm tra hợp lệ $$\delta$$ và accept.

*Verifier → NTM.* Đoán $$c$$ không tất định, chạy $$V(x,c)$$. $$\square$$

## 3. $$P\subseteq NP$$

<div class="textbook-theorem" markdown="1">

**Định lý.** $$P\subseteq NP$$.

</div>

**Chứng minh.** $$L\in P$$ với thuật toán $$A$$. Đặt $$V(x,c):=A(x)$$ (bỏ $$c$$). Đầy đủ/âm thanh/thời gian rõ. $$\square$$

## 4. Bảng certificate

| Bài | $$c$$ | $$V$$ kiểm |
|:---|:---|:---|
| SAT | gán biến | đánh giá công thức |
| Hamilton | hoán vị | $$n$$ cạnh (+ đóng) |
| 3-Color | tô $$\{1,2,3\}^V$$ | mọi cạnh khác màu |
| Subset Sum | tập con | tổng = target |

## Bài tập

1. Viết verifier giả mã cho HC; phân tích thời gian.  
2. Chứng minh $$P\subseteq NP$$ không suy ra gì về $$NP\subseteq P$$.  
3. Composite: certificate? (thừa số)

## Đọc

Sipser (NP); Arora–Barak §2.1.

## Tóm tắt

NP = short proofs · $$P\subseteq NP$$ · hai định nghĩa tương đương.

**Tiếp:** 20.4 — $$\mathrm{coNP}$$.
