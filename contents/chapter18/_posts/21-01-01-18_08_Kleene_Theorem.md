---
layout: post
title: "Định lý Kleene"
categories: chapter18
date: 2021-01-01
order: 8
required: true
lang: en
excerpt: "Regex ≡ ε-NFA ≡ NFA ≡ DFA; Thompson; state elimination (khung chứng minh)."
---


<div class="textbook-epigraph" markdown="1">

"Three notations, one class: regular languages."

<span class="epigraph-attribution">— Kleene’s theorem</span>

</div>

![Kleene](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_kleene_triangle.svg)

<p class="textbook-figure-caption" data-figure="18.5">Ba biểu diễn tương đương.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** định lý Kleene.
- **Mô tả** Thompson và state elimination.
- **Chứng minh** khung hai chiều.

</div>

## Định lý

<div class="textbook-theorem" markdown="1">

**Định lý (Kleene).** Các lớp sau trùng nhau:  
(1) $$L(r)$$ cho regex $$r$$;  
(2) $$L(N)$$ cho ε-NFA/NFA;  
(3) $$L(M)$$ cho DFA.

</div>

## Chiều regex → ε-NFA (Thompson)

Quy nạp cấu trúc: mẫu NFA cho $$\emptyset,\varepsilon,a$$; hợp/nối/star bằng ε.  
$$O(\lvert r\rvert)$$ trạng thái.

**Tính đúng:** quy nạp $$L(N_r)=L(r)$$.

## Chiều NFA → DFA

Subset construction (bài 18.5).

## Chiều DFA → regex

Loại bỏ trạng thái / hệ phương trình Arden:  
$$X=A X+B\Rightarrow X=A^*B$$ (nếu $$\varepsilon\notin L(A)$$ hoặc xử lý cẩn thận).

## Bài tập

1. Thompson cho $$(0+1)^*01$$.  
2. DFA 2 trạng thái → regex bằng elimination.  
3. Đọc Arden lemma statement.

## Đọc

Sipser; Kozen; Hopcroft.

## Tóm tắt

Kleene · Thompson · powerset · elimination.

**Tiếp:** pumping lemma.
