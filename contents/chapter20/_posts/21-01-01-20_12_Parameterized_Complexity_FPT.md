---
layout: post
title: "Parameterized Complexity và FPT"
categories: chapter20
date: 2021-01-01
order: 12
required: true
lang: en
excerpt: "FPT; chứng minh VC search tree 2ᵏn; kernel (ý); W[1] và Clique; treewidth (định hướng)."
---

<div class="textbook-epigraph" markdown="1">

"n is large, k is small — that is the FPT contract."

<span class="epigraph-attribution">— Downey & Fellows spirit</span>

</div>

Tham số hóa: thời gian $$f(k)n^{O(1)}$$ chấp nhận $$f$$ mũ theo $$k$$ nếu $$k$$ nhỏ (solution size, treewidth, …).

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** FPT.
- **Chứng minh** VC-FPT $$O(2^k n^{O(1)})$$.
- **Phân biệt** FPT vs XP; nêu W[1]-hard.

</div>

## 1. Định nghĩa

<div class="textbook-definition" markdown="1">

**FPT:** thời gian $$f(k)\cdot n^{O(1)}$$, $$f$$ chỉ phụ thuộc $$k$$.  
**XP:** $$n^{g(k)}$$ — yếu hơn (số mũ phụ thuộc $$k$$).

</div>

## 2. Vertex Cover — search tree

```text
VC(G,k):
  if k<0: No
  if no edges: Yes
  if k=0 and edges remain: No
  pick edge {u,v}
  return VC(G-u,k-1) OR VC(G-v,k-1)
```

<div class="textbook-theorem" markdown="1">

**Định lý.** Thuật toán đúng và chạy $$O(2^k\cdot\mathrm{poly}(n))$$.

</div>

**Đúng:** cover phải chứa $$u$$ hoặc $$v$$; quy nạp.  
**Thời gian:** $$\le 2^{k+1}$$ lá; mỗi node poly. $$\square$$

## 3. Kernel (ý)

Buss: đỉnh bậc $$>k$$ buộc vào cover; sau giảm, instance size $$O(k^2)$$ (hoặc tốt hơn bằng LP).  
→ Preprocess đa thức còn instance chỉ phụ thuộc $$k$$.

## 4. W[1] và Clique

Clique tham số $$k$$: **W[1]-complete** — không FPT trừ FPT=W[1].  
Đọc: Cygan et al.; Downey–Fellows.

## 5. Treewidth (định hướng)

Nhiều bài MSO trên treewidth $$w$$: $$f(w)n$$ (Courcelle) — hằng số lớn; DP thực dụng $$2^{O(w)}n^{O(1)}$$.

## Bài tập

1. Chứng minh VC-FPT đầy đủ.  
2. Phân tích nếu nhánh 3 theo đỉnh bậc ≥3 (tùy biến).  
3. Đọc 1 kernel proof (Buss).

## Đọc

Cygan et al. *Parameterized Algorithms*; IPEC papers.

## Tóm tắt

FPT · VC $$2^k$$ · kernel · W[1].

**Tiếp:** 20.13 — ETH, fine-grained, average-case.
