---
layout: post
title: "Văn phạm Phi ngữ cảnh (CFG)"
categories: chapter19
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "Định nghĩa văn phạm phi ngữ cảnh (CFG), dẫn xuất trái nhất, ví dụ chuỗi ngoặc cân bằng, biểu thức số học và chứng minh L(G)={aⁿbⁿ}."
---

<div class="textbook-epigraph" markdown="1">

"One nonterminal rewrite at a time — that is context-free."

<span class="epigraph-attribution">— CFG</span>

</div>

![CFG](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_cfg_parens.svg)

<p class="textbook-figure-caption" data-figure="19.3">Ngôn ngữ ngoặc cân bằng — ví dụ kinh điển của văn phạm phi ngữ cảnh.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** văn phạm phi ngữ cảnh (*Context-Free Grammar*, CFG).
- **Viết** dẫn xuất trái nhất (*leftmost derivation*) cho một chuỗi cho trước.
- **Chứng minh** $$L(G)=\{a^nb^n\}$$ đối với văn phạm chuẩn.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Văn phạm $$G=(V,\Sigma,P,S)$$ là **văn phạm phi ngữ cảnh (CFG)** nếu mọi luật sinh đều có dạng $$A\to\alpha$$, trong đó vế trái là đúng một ký hiệu không kết thúc $$A\in V$$ và vế phải $$\alpha\in(V\cup\Sigma)^*$$.

</div>

## Ví dụ

- Văn phạm ngoặc cân bằng: $$S\to(S)S\mid\varepsilon$$.
- Văn phạm $$S\to aSb\mid\varepsilon$$ sinh ra ngôn ngữ $$\{a^nb^n : n \ge 0\}$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** Văn phạm $$G: S\to aSb\mid\varepsilon$$ sinh ra đúng ngôn ngữ $$L(G)=\{a^nb^n:n\ge 0\}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.**  
Chiều ($$\subseteq$$): Quy nạp theo số bước dẫn xuất: mỗi lần áp dụng luật $$S\to aSb$$ đều thêm đồng thời một ký tự $$a$$ bên trái và một ký tự $$b$$ bên phải, sau cùng kết thúc bằng $$S\to\varepsilon$$.  
Chiều ($$\supseteq$$): Để sinh chuỗi $$a^nb^n$$ bất kỳ, áp dụng $$n$$ lần luật $$S\to aSb$$ rồi áp dụng một lần luật $$S\to\varepsilon$$.

</div>

## Bài tập

1. Viết dẫn xuất cho chuỗi $$()(())$$ bằng văn phạm ngoặc cân bằng.
2. Xét văn phạm biểu thức $$E\to E+E\mid E*E\mid(E)\mid\mathrm{id}$$ và chỉ ra hiện tượng mơ hồ (*ambiguity*).
3. Giải thích vì sao ngôn ngữ $$\{a^nb^n\}$$ là phi ngữ cảnh nhưng không chính quy.

## Tài liệu đọc thêm

Sipser §2.1.

## Tóm tắt

Văn phạm phi ngữ cảnh cho phép viết lại độc lập từng ký hiệu không kết thúc, đủ sức biểu diễn các cấu trúc lồng nhau như ngoặc cân bằng và $$a^nb^n$$.

**Bài tiếp theo:** Cây phân tích và sự mơ hồ.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=5_tfVe7ED3g">Context Free Grammar &amp; Context Free Language</a> — Neso Academy, tiếng Anh. Giới thiệu văn phạm và ngôn ngữ phi ngữ cảnh.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Hướng dẫn dẫn xuất trái nhất và phải nhất từ các luật sinh.
- <a href="https://www.youtube.com/watch?v=htoFbcwES28">Method to find whether a String belongs to a Grammar or not</a> — Neso Academy, tiếng Anh. Cách kiểm tra một chuỗi có thuộc ngôn ngữ sinh bởi văn phạm hay không.
