---
layout: post
title: "Rút gọn Đồ thị: IS, CLIQUE, Vertex Cover"
categories: chapter20
date: 2021-01-01
order: 9
required: true
lang: en
excerpt: "Chứng minh 3SAT≤ₚIS; IS≡CLIQUE; IS≤ₚVC — đầy đủ tính đúng và poly-time."
---

<div class="textbook-epigraph" markdown="1">

"One careful graph gadget unlocks a family of NP-complete problems."

<span class="epigraph-attribution">— Combinatorial reduction craft</span>

</div>

Ba bài đồ thị “cốt lõi” — nền cho hàng loạt hardness khác.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** $$3\mathrm{SAT}\le_p\mathrm{IS}$$.
- **Chứng minh** IS ≡ CLIQUE qua bù.
- **Chứng minh** $$\mathrm{IS}\le_p\mathrm{VC}$$.

</div>

## 1. $$3\mathrm{SAT}\le_p\mathrm{INDEPENDENT\text{-}SET}$$

**Construction.**  
Mệnh đề $$C_j=\{\ell_{j1},\ell_{j2},\ell_{j3}\}$$.  
Đỉnh $$v_{j,r}$$ ($$3m$$ đỉnh).  
Cạnh: (i) tam giác trong mỗi mệnh đề; (ii) nối literal mâu thuẫn khác mệnh đề.  
$$k=m$$.

**Tính đúng.**  
*Sat ⇒ IS:* mỗi mệnh đề chọn 1 literal true → $$m$$ đỉnh, không mâu thuẫn, không cùng tam giác.  
*IS ⇒ sat:* đúng 1 đỉnh/mệnh đề; gán theo literal chọn; nhất quán vì không cạnh mâu thuẫn.

**Poly-time:** $$O(m^2)$$.  

<div class="textbook-theorem" markdown="1">

**Định lý.** $$3\mathrm{SAT}\le_p\mathrm{IS}$$. Vậy IS NP-complete (IS∈NP rõ).

</div>

## 2. IS ≡ CLIQUE

$$\overline{G}$$: cạnh khi $$G$$ không có.  
$$S$$ IS trong $$G$$ ⇔ $$S$$ clique trong $$\overline{G}$$.  
$$f(G,k)=(\overline{G},k)$$ trong $$O(n^2)$$; khả nghịch.

## 3. IS ≤ₚ VC

**Bổ đề.** $$S$$ IS ⇔ $$V\setminus S$$ vertex cover.

**Chứng minh.** Cạnh không thể nằm trọn trong IS; cover phải chạm mọi cạnh. $$\square$$

**Rút gọn:** $$(G,k)\mapsto(G,n-k)$$.  
IS size $$\ge k$$ ⇔ cover size $$\le n-k$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** VC NP-complete.

</div>

## Bài tập

1. Vẽ gadget 2 mệnh đề $$(x\lor y\lor z)\land(\neg x\lor y\lor w)$$.  
2. Chứng minh bỏ cạnh mâu thuẫn làm construction sai.  
3. Suy CLIQUE NPC từ IS.

## Đọc

Sipser; CLRS; Garey–Johnson.

## Tóm tắt

3SAT→IS→CLIQUE/VC · template hardness đồ thị.

**Tiếp:** 20.10 — Hamilton & TSP.
