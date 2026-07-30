---
layout: post
title: "Cây Phân tích và Sự Mơ hồ"
categories: chapter19
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Parse tree; quan hệ derivation; ambiguous grammar; if-else."
---


<div class="textbook-epigraph" markdown="1">

"Ambiguity is multiple stories for one string."

<span class="epigraph-attribution">— Parsing theory</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Vẽ** parse tree.
- **Định nghĩa** ambiguous grammar.
- **Chứng minh** grammar cụ thể mơ hồ.

</div>

## Parse tree

Nút trong = nonterminal; con = vế phải; lá = terminal/ε.  
Yield = chuỗi.

<div class="textbook-theorem" markdown="1">

**Định lý** (tinh thần). Leftmost derivations ↔ parse trees (1–1 với cây).

</div>

## Ambiguity

<div class="textbook-definition" markdown="1">

$$G$$ **mơ hồ** nếu ∃ $$w$$ có ≥2 leftmost derivation (hoặc ≥2 parse tree).

</div>

**Ví dụ.** $$E\to E+E\mid\mathrm{id}$$: $$id+id+id$$ hai cây.  
**Dangling else:** cổ điển C/Java.

## Bài tập

1. Hai tree cho $$id+id*id$$ với * và + không ưu tiên.  
2. Viết grammar không mơ hồ cho + * trái kết hợp.  
3. Inherent ambiguity (khái niệm).

## Đọc

Aho–Sethi–Ullman Dragon book; Sipser.

## Tóm tắt

Tree · ambiguity · ưu tiên.

**Tiếp:** PDA.
