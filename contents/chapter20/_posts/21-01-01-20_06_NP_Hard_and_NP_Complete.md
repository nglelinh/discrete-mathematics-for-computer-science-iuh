---
layout: post
title: "NP-hard và NP-complete"
categories: chapter20
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "Định nghĩa NP-hard/NPC; chứng minh: một NPC trong P ⇒ P=NP; checklist chứng minh hardness; Ladner."
---

<div class="textbook-epigraph" markdown="1">

"NP-complete problems are the hardest problems in NP — under polynomial reductions."

<span class="epigraph-attribution">— Garey & Johnson spirit</span>

</div>

![P NP](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_p_np_sets.svg)

<p class="textbook-figure-caption" data-figure="20.4">NPC “khó nhất” trong NP theo $$\le_p$$.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** NP-hard, NP-complete.
- **Chứng minh** các hệ quả chuẩn.
- **Áp dụng** checklist 2 bước chứng minh NPC.

</div>

## 1. Định nghĩa

<div class="textbook-definition" markdown="1">

- $$B$$ **NP-hard:** $$\forall A\in NP$$, $$A\le_p B$$.  
- $$B$$ **NP-complete:** NP-hard và $$B\in NP$$.

</div>

## 2. Định lý then chốt

<div class="textbook-theorem" markdown="1">

**Định lý.** Cho $$B$$ NP-complete.

1. $$B\in P\Rightarrow P=NP$$.  
2. $$P\neq NP\Rightarrow B\notin P$$.  
3. Nếu $$A\in NP$$ và $$B\le_p A$$ thì $$A$$ NP-complete.

</div>

**Chứng minh (1).** $$\forall L\in NP$$: $$L\le_p B\in P\Rightarrow L\in P$$. $$\square$$

**Chứng minh (3).** NP-hard: $$L\le_p B\le_p A\Rightarrow L\le_p A$$. $$\square$$

## 3. Checklist chứng minh $$A$$ NPC

1. **$$A\in NP$$:** certificate + verifier poly.  
2. **$$B\le_p A$$** với $$B$$ đã NPC (thường 3SAT).  
3. Chứng minh $$x\in B\Leftrightarrow f(x)\in A$$.  
4. $$f$$ poly-time.

## 4. Ladner

<div class="textbook-theorem" markdown="1">

**Định lý** (Ladner 1975). Nếu $$P\neq NP$$ thì ∃ $$L\in NP\setminus P$$ không NP-complete.

</div>

→ Dưới $$P\neq NP$$ có bài “trung gian”.

## 5. Myth

- NP ≠ “không giải được”.  
- NP-hard ⇏ thuộc NP.  
- Factoring chưa biết NPC.

## Bài tập

1. Viết đủ chứng minh (1) và (3).  
2. Giả sử IS NPC. Suy VC NPC nếu đã có IS≤ₚVC (xem 20.9).  
3. Đọc Ladner sketch (Arora–Barak).

## Đọc

Garey–Johnson; Sipser; Ladner 1975.

## Tóm tắt

NPC = hard + in NP · một poly ⇒ sụp · checklist 2 bước.

**Tiếp:** 20.7 — Cook–Levin.
