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

Thay vì xây một chiếc máy để *kiểm tra* một chuỗi có hợp lệ hay không (cách tiếp cận của automata), ta có thể lật ngược góc nhìn: xây một bộ quy tắc thay thế để *sinh ra* toàn bộ các chuỗi hợp lệ. Đó chính là khái niệm **văn phạm hình thức (formal grammar)** do Noam Chomsky đặt nền móng vào năm 1956 — từ loại tổng quát nhất không giới hạn quy tắc (Loại 0) tương đương trọn vẹn với sức mạnh của máy Turing.

## Kiến thức cần nhớ: Ba trụ cột của Văn phạm Tổng quát

1. **Bộ bốn thành phần $$G = (V, T, P, S)$$**:
   Phân biệt rạch ròi ký hiệu không kết thúc (biến $$V$$, đại diện cho cấu trúc ngữ pháp chưa hoàn chỉnh) và ký hiệu kết thúc ($$T$$, các ký tự xuất hiện trong chuỗi đầu ra cuối cùng), bắt đầu từ ký hiệu gốc $$S$$.
2. **Quan hệ dẫn xuất một bước ($$\Rightarrow$$) và nhiều bước ($$\Rightarrow^*$$)**:
   Trong văn phạm không giới hạn (Loại 0), vế trái $$\alpha$$ của quy tắc $$\alpha \to \beta$$ có thể chứa nhiều ký hiệu (miễn có ít nhất một biến), cho phép biểu diễn cả bối cảnh xung quanh lẫn rút gọn độ dài chuỗi.
3. **Ngôn ngữ sinh bởi văn phạm $$L(G)$$ và tương đương với RE**:
   $$L(G) = \{w \in T^* \mid S \Rightarrow^* w\}$$. Mọi ngôn ngữ nhận dạng được bởi máy Turing (RE) đều sinh được bởi một văn phạm Loại 0 và ngược lại.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** văn phạm hình thức (*grammar*) và ngôn ngữ sinh ra $$L(G)$$.
- **Thực hiện** các bước dẫn xuất chuỗi mẫu từ tập luật sinh.

</div>

## Định nghĩa

![Mô hình ngôn ngữ hình thức](/discrete-mathematics-for-computer-science-iuh/img/course/Formal_languages.svg)

<div class="textbook-definition" markdown="1">

Một **văn phạm hình thức** là bộ bốn $$G=(V,\Sigma,P,S)$$, gồm tập ký hiệu không kết thúc (*nonterminal*) $$V$$, tập ký hiệu kết thúc (*terminal*) $$\Sigma$$, tập luật sinh $$P$$ dạng $$\alpha\to\beta$$ (trong đó $$\alpha$$ chứa ít nhất một ký hiệu không kết thúc) và ký hiệu khởi đầu $$S \in V$$.

Ta viết $$u\Rightarrow v$$ nếu $$v$$ thu được từ $$u$$ bằng cách thay thế một lần xuất hiện của vế trái $$\alpha$$ bằng vế phải $$\beta$$ theo một luật trong $$P$$. Ngôn ngữ sinh bởi $$G$$ là

$$L(G)=\{w\in\Sigma^*:S\Rightarrow^* w\}.$$

</div>

## Ví dụ

Văn phạm với luật sinh $$S\to aSb\mid\varepsilon$$ (thuộc lớp CFG) sinh ra đúng ngôn ngữ $$\{a^nb^n : n \ge 0\}$$.

### Giải thích: Dẫn xuất từng bước chuỗi `aabbcc` bằng văn phạm không giới hạn

Ngôn ngữ $$L = \{a^n b^n c^n \mid n \ge 1\}$$ không thể sinh bởi văn phạm phi ngữ cảnh (CFG), nhưng lại sinh gọn gàng bằng quy tắc có ngữ cảnh (hoán vị `CB -> BC`):
- Quy tắc: $$S \to aSBC \mid aBC$$, $$CB \to BC$$, $$aB \to ab$$, $$bB \to bb$$, $$bC \to bc$$, $$cC \to cc$$.

Theo dõi từng bước dẫn xuất chuỗi `aabbcc` ($$n = 2$$):
1. $$S \Rightarrow aSBC$$ (dùng $$S \to aSBC$$)
2. $$\Rightarrow aaBCBC$$ (dùng $$S \to aBC$$)
3. $$\Rightarrow aaBBCC$$ (dùng quy tắc ngữ cảnh $$CB \to BC$$ để gom `B` sang trái, `C` sang phải)
4. $$\Rightarrow aabBCC \Rightarrow aabbCC$$ (chuyển lần lượt `B` thành `b` khi đứng cạnh `a` hoặc `b`)
5. $$\Rightarrow aabbcC \Rightarrow \mathbf{aabbcc}$$ (chuyển lần lượt `C` thành `c`).

Chính khả năng đổi chỗ $$CB \to BC$$ nhờ vế trái có 2 ký hiệu đã cho văn phạm Loại 0/Loại 1 sức mạnh vượt xa CFG!

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
