---
layout: post
title: "coNP và Hệ quả Cấu trúc"
categories: chapter20
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Định nghĩa coNP; P⊆NP∩coNP; nếu NPC thuộc coNP thì NP=coNP; factoring và NP∩coNP."
---

<div class="textbook-epigraph" markdown="1">

"coNP is about short proofs of NO."

<span class="epigraph-attribution">— Structural complexity</span>

</div>

$$NP$$: chứng chỉ cho **Yes**. $$\mathrm{coNP}$$: chứng chỉ cho **No**. Cấu trúc $$NP$$ vs $$\mathrm{coNP}$$ tinh hơn $$P$$ vs $$NP$$ và liên quan mật mã.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** $$\mathrm{coNP}$$.
- **Chứng minh** $$P\subseteq NP\cap\mathrm{coNP}$$.
- **Phát biểu** hệ quả nếu có NPC trong $$\mathrm{coNP}$$.
- **Thảo luận** factoring ∈ NP∩coNP (ý).

</div>

## 1. Định nghĩa

<div class="textbook-definition" markdown="1">

**Định nghĩa.** $$\mathrm{coNP}=\{L:\overline{L}\in NP\}$$.

Tương đương: No-instance có chứng chỉ ngắn kiểm đa thức.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ.** TAUTOLOGY (công thức luôn đúng): “No” = không tautology = có gán làm false — chứng chỉ gán → liên hệ $$\mathrm{coNP}$$.

</div>

## 2. Định lý

<div class="textbook-theorem" markdown="1">

**Định lý.** $$P\subseteq\mathrm{coNP}$$.

</div>

**Chứng minh.** $$L\in P\Rightarrow\overline{L}\in P$$ (đảo output) $$\Rightarrow\overline{L}\in NP$$ $$\Rightarrow L\in\mathrm{coNP}$$. $$\square$$

<div class="textbook-theorem" markdown="1">

**Định lý.** $$P\subseteq NP\cap\mathrm{coNP}$$.

</div>

**Chứng minh.** Kết hợp $$P\subseteq NP$$ và định lý trên. $$\square$$

<div class="textbook-theorem" markdown="1">

**Định lý** (cấu trúc). Nếu tồn tại $$L$$ NP-complete mà $$L\in\mathrm{coNP}$$ thì $$NP=\mathrm{coNP}$$.

</div>

**Ý chứng minh.** Mọi $$A\in NP$$ có $$A\le_p L$$; membership $$\mathrm{coNP}$$ “kéo” theo rút gọn (Arora–Barak). Chiều kia đối xứng. $$\square$$

## 3. Factoring (cảnh báo NCS)

Integer factoring (dạng quyết định chuẩn) được lập luận thuộc $$NP\cap\mathrm{coNP}$$ nhưng **không** biết NPC.  
→ RSA **không** dựa trên “factoring NP-complete”.

## Bài tập

1. Chứng minh $$P\subseteq\mathrm{coNP}$$ từng dòng.  
2. Nếu $$NP=\mathrm{coNP}$$ thì sao với chứng minh độ dài ngắn? (thảo luận)  
3. Đọc một đoạn Arora–Barak về $$NP$$ vs $$\mathrm{coNP}$$.

## Đọc

Arora–Barak §2; Goldreich conceptual notes.

## Tóm tắt

coNP · $$P\subseteq NP\cap\mathrm{coNP}$$ · NPC∩coNP ⇒ sụp hierarchy.

**Tiếp:** 20.5 — rút gọn $$\le_p$$.
