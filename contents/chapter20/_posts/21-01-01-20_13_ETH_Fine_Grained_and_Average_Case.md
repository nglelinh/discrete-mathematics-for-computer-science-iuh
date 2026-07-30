---
layout: post
title: "ETH, Fine-grained và Average-case"
categories: chapter20
date: 2021-01-01
order: 13
required: true
lang: en
excerpt: "ETH và hệ quả; fine-grained (SETH, 3SUM); Impagliazzo five worlds; mật mã vs worst-case NPC."
---

<div class="textbook-epigraph" markdown="1">

"Not all hardness is NP-completeness — some is fine-grained, some is average-case."

<span class="epigraph-attribution">— Modern complexity map</span>

</div>

Ba lớp công cụ **tinh** hơn NPC: giả thuyết thời gian mũ, lower bound trong $$P$$, độ khó trung bình (crypto).

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** ETH/SETH và một hệ quả.
- **Mô tả** fine-grained hardness (ý).
- **Giải thích** five worlds và vì sao crypto ≠ NPC worst-case.

</div>

## 1. ETH

<div class="textbook-definition" markdown="1">

**ETH** (Impagliazzo–Paturi–Zane): 3SAT không có thuật toán $$2^{o(n)}$$ ($$n$$ biến).

</div>

**Hệ quả điển hình:** nhiều bài không $$2^{o(n+m)}$$; FPT $$2^{o(k)}n^{O(1)}$$ bị loại cho một số bài.  
Dùng trong paper: “assuming ETH, our $$2^{\Theta(k)}$$ is tight”.

**SETH:** dạng mạnh hơn cho $$k$$-SAT khi $$k\to\infty$$ — nền edit distance, etc.

## 2. Fine-grained complexity

Hỏi *trong* $$P$$: APSP có $$O(n^{3-\varepsilon})$$? 3SUM có $$O(n^{2-\varepsilon})$$?  
Rút gọn **fine-grained** dưới SETH/3SUM/APSP hypotheses (V. Vassilevska Williams surveys).

**Đối với NCS:** hướng “hot” nếu thích lower bound điều kiện + thuật toán.

## 3. Average-case và five worlds

Impagliazzo (1995):

| World | Tinh thần |
|:---|:---|
| Algorithmica | $$P=NP$$ (kể average) |
| Heuristica | worst hard, average easy |
| Pessiland | average hard, no OWF |
| Minicrypt | OWF, limited PKE |
| Cryptomania | rich public-key crypto |

**Bài học:** NP-complete worst-case **không** tự cho one-way function.  
Crypto: LWE, factoring, DLOG — giả thuyết *riêng*, average-preserving reductions (Goldreich).

## 4. Randomness

BPP, derandomization dưới circuit lower bounds — Arora–Barak.  
#P counting (Valiant permanent) — nhánh riêng.

## Bài tập

1. Viết 1 trang: ETH dùng để chứng minh tightness thế nào (ví dụ).  
2. Bảng 5 worlds đủ 5 dòng hệ quả.  
3. Vì sao “TSP hard ⇒ crypto” là suy luận sai?

## Đọc

Impagliazzo 1995; IPZ ETH; Williams fine-grained survey; Goldreich crypto foundations.

## Tóm tắt

ETH · fine-grained · average-case · crypto tách worst-case NPC.

**Tiếp:** 20.14 — bắt tay nghiên cứu.
