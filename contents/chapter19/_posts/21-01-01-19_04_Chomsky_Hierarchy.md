---
layout: post
title: "Phân cấp Chomsky"
categories: chapter19
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Type 0–3; dạng production; máy tương ứng; bao hàm."
---


<div class="textbook-epigraph" markdown="1">

"Four types of rules, four kinds of machines."

<span class="epigraph-attribution">— Chomsky hierarchy</span>

</div>

![Chomsky](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_chomsky_nested.svg)

<p class="textbook-figure-caption" data-figure="19.2">Type-3 ⊂ Type-2 ⊂ Type-1 ⊂ Type-0.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phân loại** production theo type.
- **Nêu** máy nhận tương ứng.
- **Phát biểu** bao hàm.

</div>

## Bảng

| Type | Tên | Quy tắc (ý) | Máy |
|:---:|:---|:---|:---|
| 3 | Regular | $$A\to aB$$ / $$A\to a$$ | DFA/NFA |
| 2 | CF | $$A\to\alpha$$ | PDA |
| 1 | CS | $$\lvert\alpha\rvert\le\lvert\beta\rvert$$ | LBA |
| 0 | RE | tự do | TM |

<div class="textbook-theorem" markdown="1">

**Định lý** (bao hàm cổ điển).  
$$\mathcal{L}_3\subset\mathcal{L}_2\subset\mathcal{L}_1\subset\mathcal{L}_0$$ (với xử lý ε-rule chuẩn).

</div>

## Bài tập

1. Xếp grammar $$S\to aS\mid b$$.  
2. Vì sao $$a^nb^nc^n$$ không Type-2 (preview pump CFL)?  
3. Liên hệ Ch.18 regular.

## Đọc

Sipser; Hopcroft; Chomsky 1956/1959 historical.

## Tóm tắt

4 type · máy · lồng nhau.

**Tiếp:** regular grammar.
