---
layout: post
title: "Rút gọn SAT ≤ₚ 3SAT"
categories: chapter20
date: 2021-01-01
order: 8
required: true
lang: en
excerpt: "Chứng minh đầy đủ SAT≤ₚ3SAT: pad mệnh đề 1, 2, ≥4 literal; 3SAT NP-complete."
---

<div class="textbook-epigraph" markdown="1">

"3SAT is the workhorse source problem for combinatorial reductions."

<span class="epigraph-attribution">— Karp style</span>

</div>

Mọi hardness graph thường đi từ **3SAT**. Mục này chứng minh $$3\mathrm{SAT}$$ NP-complete từ Cook–Levin.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Xây** $$f$$ poly-time: CNF → 3CNF bảo toàn thỏa được.
- **Chứng minh** từng trường hợp độ dài mệnh đề.
- **Kết luận** $$3\mathrm{SAT}$$ NPC.

</div>

## 1. $$3\mathrm{SAT}\in NP$$

Certificate = gán. Verifier đánh giá: poly. $$\square$$

## 2. Construction

Cho $$\varphi=C_1\land\cdots\land C_m$$. Xử lý từng $$C$$:

### $$\lvert C\rvert=3$$
Giữ nguyên.

### $$\lvert C\rvert=1$$: $$C=(\ell)$$
Biến mới $$u,v$$:

$$
(\ell\lor u\lor v)\land(\ell\lor u\lor\neg v)\land(\ell\lor\neg u\lor v)\land(\ell\lor\neg u\lor\neg v).
$$

**Bổ đề.** Thỏa ⇔ $$\ell$$ true.  
*Chứng minh.* $$\ell$$ true ⇒ ok. $$\ell$$ false ⇒ bốn mệnh đề yêu cầu mọi tổ hợp $$u,v$$ — mâu thuẫn. $$\square$$

### $$\lvert C\rvert=2$$: $$(\ell_1\lor\ell_2)$$
Biến $$u$$: $$(\ell_1\lor\ell_2\lor u)\land(\ell_1\lor\ell_2\lor\neg u)$$.  
Thỏa ⇔ $$\ell_1\lor\ell_2$$.

### $$\lvert C\rvert=k\ge 4$$: $$(\ell_1\lor\cdots\lor\ell_k)$$
Biến $$y_1,\ldots,y_{k-3}$$:

$$
(\ell_1\lor\ell_2\lor y_1)
\land(\neg y_1\lor\ell_3\lor y_2)
\land\cdots
\land(\neg y_{k-3}\lor\ell_{k-1}\lor\ell_k).
$$

**Bổ đề.** Thỏa ⇔ ∃ $$\ell_j$$ true.  
*(⇒)* Mọi $$\ell$$ false buộc dây $$y_i$$ dẫn mâu thuẫn cuối.  
*(⇐)* Gán $$y$$ “prefix true đến trước literal đúng”. $$\square$$

## 3. Tổng hợp

$$f(\varphi)$$ = hội mọi mệnh đề 3-literal sau pad.  
Poly-time (tuyến tính).  
$$\varphi$$ sat ⇔ $$f(\varphi)$$ sat.

<div class="textbook-theorem" markdown="1">

**Định lý.** $$\mathrm{SAT}\le_p 3\mathrm{SAT}$$. Kết hợp Cook–Levin: $$3\mathrm{SAT}$$ NP-complete.

</div>

## Bài tập

1. Chứng minh đủ pad $$k=5$$ bằng bảng gán.  
2. Ước số biến mới theo $$\sum(\lvert C_j\rvert)$$.  
3. Vì sao 2SAT ∈ P không mâu thuẫn? (2SAT không NPC trừ P=NP)

## Đọc

Sipser; CLRS NPC; Garey–Johnson.

## Tóm tắt

Pad mệnh đề · 3SAT NPC · nguồn rút gọn đồ thị.

**Tiếp:** 20.9 — IS, CLIQUE, VC.
