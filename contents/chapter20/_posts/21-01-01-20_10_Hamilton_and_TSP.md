---
layout: post
title: "Hamilton Cycle và TSP Quyết định"
categories: chapter20
date: 2021-01-01
order: 10
required: true
lang: en
excerpt: "HC∈NP; HC≤ₚTSP-DEC chứng minh đầy đủ; cấu trúc rút gọn 3SAT→HC; liên hệ Ch.12."
---

<div class="textbook-epigraph" markdown="1">

"Euler is easy; Hamilton is hard — the difference is edges versus vertices."

<span class="epigraph-attribution">— Graph algorithms folklore</span>

</div>

Ch.12: Euler đa thức, Hamilton khó. Mục này đặt vào khung NPC.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** HC, TSP-DEC ∈ NP.
- **Chứng minh** $$\mathrm{HC}\le_p\mathrm{TSP\text{-}DEC}$$.
- **Mô tả** cấu trúc chứng minh $$3\mathrm{SAT}\le_p\mathrm{HC}$$ (gadget — đọc Garey–Johnson).

</div>

## 1. Thuộc NP

**HC:** certificate = hoán vị; kiểm $$n$$ cạnh.  
**TSP-DEC:** certificate = tour; cộng trọng số so $$K$$. $$\square$$

## 2. $$\mathrm{HC}\le_p\mathrm{TSP\text{-}DEC}$$ (đầy đủ)

**Construction.** Từ $$G=(V,E)$$, $$\lvert V\rvert=n$$, dựng $$K_n$$:

$$
w(e)=\begin{cases}1&e\in E\\2&e\notin E.\end{cases}
$$

Hỏi: có tour độ dài $$\le n$$?

**Tính đúng.**  
Tour Hamilton trong $$G$$ ⇒ $$n$$ cạnh weight 1 ⇒ tổng $$n$$.  
Tour TSP tổng $$\le n$$: mọi cạnh weight $$\ge 1$$ ⇒ phải đúng $$n$$ cạnh weight 1 ⇒ chu trình trong $$G$$.

Poly-time. $$\square$$

## 3. $$3\mathrm{SAT}\le_p\mathrm{HC}$$ (cấu trúc)

Gadget đỉnh/cạnh mô phỏng literal và mệnh đề (Garey–Johnson; Sipser optional).  
**Seminar:** đọc một nguồn, vẽ gadget, viết Yes⇔Yes 2 trang — *không* tự bịa gadget.

<div class="textbook-theorem" markdown="1">

**Định lý.** HC và TSP-DEC NP-complete (HC từ literature gadget + TSP từ §2).

</div>

## Bài tập

1. Viết đủ chứng minh HC→TSP-DEC.  
2. Vì sao weight $$2$$ đủ lớn? (tổng $$\ge n+1$$ nếu một cạnh “giả”)  
3. Euler vs Hamilton: đối chiếu certificate/thuật toán.

## Đọc

Garey–Johnson (Hamilton); Vazirani (metric TSP xấp xỉ — 20.11).

## Tóm tắt

HC NPC · TSP-DEC NPC · cầu Ch.12 ↔ complexity.

**Tiếp:** 20.11 — xấp xỉ.
