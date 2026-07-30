---
layout: post
title: "Thuật toán Xấp xỉ"
categories: chapter20
date: 2021-01-01
order: 11
required: true
lang: en
excerpt: "Ratio xấp xỉ; chứng minh VC ratio 2; metric TSP 3/2 (phát biểu); inapproximability và PCP (định hướng)."
---

<div class="textbook-epigraph" markdown="1">

"If you cannot solve it exactly in poly-time, solve it approximately — with a proof."

<span class="epigraph-attribution">— Approximation algorithms</span>

</div>

NPC chặn exact poly-time (nếu $$P\neq NP$$). **Xấp xỉ** hỏi: poly-time với **bảo đảm tỉ lệ**?

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** ratio, PTAS, FPTAS.
- **Chứng minh** APPROX-VC ratio 2.
- **Phát biểu** Christofides và hardness TSP không metric.

</div>

## 1. Định nghĩa

<div class="textbook-definition" markdown="1">

Minimization: $$A(I)\le\rho\cdot\mathrm{OPT}(I)$$, $$\rho\ge 1$$.  
**PTAS:** mọi $$\varepsilon>0$$, ratio $$1+\varepsilon$$, thời gian poly (mũ có thể phụ thuộc $$1/\varepsilon$$).  
**FPTAS:** poly cả $$n$$ và $$1/\varepsilon$$.

</div>

## 2. Vertex Cover ratio 2

```text
while còn cạnh:
  chọn e={u,v}; thêm u,v vào C; xóa cạnh kề u hoặc v
```

<div class="textbook-theorem" markdown="1">

**Định lý.** $$C$$ là cover và $$\lvert C\rvert\le 2\mathrm{OPT}$$.

</div>

**Chứng minh.**  
Cover: mọi cạnh bị xóa khi một đầu đã vào $$C$$.  
$$M$$ = cạnh được chọn: matching. $$\lvert C\rvert=2\lvert M\rvert$$.  
$$\mathrm{OPT}\ge\lvert M\rvert$$ (phủ matching). $$\square$$

## 3. Metric TSP

<div class="textbook-theorem" markdown="1">

**Định lý** (Christofides–Serdyukov). Metric TSP: ratio $$3/2$$ poly-time.

</div>

MST + matching đỉnh bậc lẻ + shortcut (Vazirani Ch.3).

## 4. Không xấp xỉ

TSP không metric: không ratio hằng trừ $$P=NP$$ (Sahni–Gonzalez).  
PCP ⇒ inapproximability MAX-3SAT, CLIQUE, … (Arora–Barak).

## Bài tập

1. Viết lại chứng minh VC 2 không nhìn tài liệu.  
2. Chứng minh mọi maximal matching cho cover $$2\mathrm{OPT}$$.  
3. Đọc Christofides proof outline.

## Đọc

Vazirani; Williamson–Shmoys; Arora–Barak (PCP intro).

## Tóm tắt

Ratio · VC-2 · metric TSP · hardness xấp xỉ.

**Tiếp:** 20.12 — FPT.
