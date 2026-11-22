---
layout: post
title: "Văn phạm Tổng quát"
categories: chapter19
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Định nghĩa văn phạm G=(V,Σ,P,S), quan hệ dẫn xuất, ngôn ngữ sinh ra L(G) và góc nhìn đối ngẫu giữa sinh chuỗi và nhận dạng."
---

<div class="textbook-epigraph" markdown="1">

"Grammars generate; automata recognize."

<span class="epigraph-attribution">— Formal languages dual view</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** văn phạm hình thức (*grammar*) và ngôn ngữ sinh ra $$L(G)$$.
- **Thực hiện** các bước dẫn xuất chuỗi mẫu từ tập luật sinh.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

Một **văn phạm hình thức** là bộ bốn $$G=(V,\Sigma,P,S)$$, gồm tập ký hiệu không kết thúc (*nonterminal*) $$V$$, tập ký hiệu kết thúc (*terminal*) $$\Sigma$$, tập luật sinh $$P$$ dạng $$\alpha\to\beta$$ (trong đó $$\alpha$$ chứa ít nhất một ký hiệu không kết thúc) và ký hiệu khởi đầu $$S \in V$$.

Ta viết $$u\Rightarrow v$$ nếu $$v$$ thu được từ $$u$$ bằng cách thay thế một lần xuất hiện của vế trái $$\alpha$$ bằng vế phải $$\beta$$ theo một luật trong $$P$$. Ngôn ngữ sinh bởi $$G$$ là

$$L(G)=\{w\in\Sigma^*:S\Rightarrow^* w\}.$$

</div>

## Ví dụ

Văn phạm với luật sinh $$S\to aSb\mid\varepsilon$$ (thuộc lớp CFG) sinh ra đúng ngôn ngữ $$\{a^nb^n : n \ge 0\}$$.

## Bài tập

1. Viết đầy đủ các bước dẫn xuất chuỗi $$aaabbb$$ từ văn phạm ví dụ trên.
2. Phác thảo một văn phạm (loại 1 hoặc loại 0) sinh ra ngôn ngữ $$\{a^nb^n c^n : n \ge 1\}$$.
3. So sánh góc nhìn “sinh chuỗi” của văn phạm với góc nhìn “nhận dạng chuỗi” của ô-tô-mát.

## Tài liệu đọc thêm

Sipser §2; Hopcroft §5.

## Tóm tắt

Văn phạm mô tả ngôn ngữ bằng tập luật sinh và phép dẫn xuất từ ký hiệu khởi đầu $$S$$ đến các chuỗi gồm toàn ký hiệu kết thúc.

**Bài tiếp theo:** Phân cấp Chomsky.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu vị trí của văn phạm loại 0 trong phân cấp Chomsky.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Minh họa thao tác dẫn xuất chuỗi từ tập luật sinh của văn phạm.
- <a href="https://www.youtube.com/watch?v=5_tfVe7ED3g">Context Free Grammar &amp; Context Free Language</a> — Neso Academy, tiếng Anh. Văn phạm phi ngữ cảnh như một trường hợp hạn chế của văn phạm tổng quát để đối chiếu.
