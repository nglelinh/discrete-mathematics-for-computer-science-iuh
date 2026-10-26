---
layout: post
title: "CFG ≡ PDA"
categories: chapter19
date: 2021-01-01
order: 9
required: true
lang: en
excerpt: "Hai chiều: grammar→PDA; PDA→grammar; khung chứng minh."
---


<div class="textbook-epigraph" markdown="1">

"CFGs and PDAs define the same languages."

<span class="epigraph-attribution">— Fundamental theorem of CFLs</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Mô tả** hai construction.
- **Chứng minh khung** $$L(G)=L(P)$$.

</div>

## CFG → PDA

PDA đoán production leftmost: stack giữ sentential form; match terminal với input.

## PDA → CFG

Biến $$A_{pq}$$: “từ $$p$$ đến $$q$$, stack height + net 0 từ bottom symbol”.  
Production theo 1 bước PDA (Sipser).

<div class="textbook-theorem" markdown="1">

**Định lý.** $$L$$ CFL ⇔ $$L=L(P)$$ cho PDA $$P$$.

</div>

## Bài tập

1. PDA từ $$S\to aSb\mid\varepsilon$$.  
2. Đọc full proof Sipser một chiều.  
3. Deterministic CFL ⊂ CFL nghiêm.

## Đọc

Sipser §2.2; Hopcroft §6.

## Tóm tắt

Hai construction · CFL = PDA.

**Tiếp:** pumping CFL.

## Video tham khảo

- **xem trước** <a href="https://www.youtube.com/watch?v=FjGrU7vczyg">Equivalence of CFG and PDA (Part 1)</a> — Neso Academy, tiếng Anh. Xem trước một chiều tương đương CFG và PDA.
- <a href="https://www.youtube.com/watch?v=kyvLetfjOhc">Equivalence of CFG and PDA (Part 2a)</a> — Neso Academy, tiếng Anh. Tiếp chứng minh, phần đổi từ văn phạm sang máy hoặc ngược lại.
- <a href="https://www.youtube.com/watch?v=DjbukiTf-48">Equivalence of CFG and PDA (Part 2b)</a> — Neso Academy, tiếng Anh. Nốt phần còn lại của chứng minh tương đương.
