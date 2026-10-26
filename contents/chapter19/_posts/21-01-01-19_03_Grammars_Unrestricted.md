---
layout: post
title: "Văn phạm Tổng quát"
categories: chapter19
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "G=(V,Σ,P,S); dẫn xuất; L(G); ví dụ Type-0."
---


<div class="textbook-epigraph" markdown="1">

"Grammars generate; automata recognize."

<span class="epigraph-attribution">— Formal languages dual view</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** grammar và $$L(G)$$.
- **Viết** dẫn xuất mẫu.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

$$G=(V,\Sigma,P,S)$$: nonterminal $$V$$, terminal $$\Sigma$$, $$P$$ quy tắc $$\alpha\to\beta$$ ($$\alpha$$ chứa nonterminal), start $$S$$.

$$u\Rightarrow v$$ nếu thay một occurrence vế trái.  
$$L(G)=\{w\in\Sigma^*:S\Rightarrow^* w\}$$.

</div>

## Ví dụ

$$S\to aSb\mid\varepsilon$$ sinh $$\{a^nb^n\}$$ (CFG).

## Bài tập

1. Dẫn xuất $$aaabbb$$.  
2. Grammar cho $$\{a^nb^n c^n\}$$ (Type-1/0 ý).  
3. So generate vs recognize.

## Đọc

Sipser §2; Hopcroft §5.

## Tóm tắt

Production · derivation · $$L(G)$$.

**Tiếp:** Chomsky hierarchy.

## Video tham khảo

- **xem trước** <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Xem trước văn phạm loại 0 trên phân cấp Chomsky.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Dẫn xuất từ một văn phạm, thao tác cơ bản của bài.
- <a href="https://www.youtube.com/watch?v=5_tfVe7ED3g">Context Free Grammar &amp; Context Free Language</a> — Neso Academy, tiếng Anh. CFG là hạn chế của văn phạm tổng quát, để đối chiếu.
