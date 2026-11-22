---
layout: post
title: "Myhill–Nerode và DFA Tối tiểu"
categories: chapter18
date: 2021-01-01
order: 11
required: true
lang: en
excerpt: "Quan hệ tương đương Myhill–Nerode ~L, định lý Myhill–Nerode, chứng minh ngôn ngữ không chính quy và thuật toán tối tiểu hóa DFA."
---

<div class="textbook-epigraph" markdown="1">

"The number of states you need is the number of distinguishable futures."

<span class="epigraph-attribution">— Myhill–Nerode</span>

</div>

Định lý Myhill–Nerode là công cụ **mạnh hơn bổ đề bơm**, vừa cung cấp điều kiện cần và đủ cho tính chính quy vừa xác định chính xác cận dưới số trạng thái của DFA tối tiểu.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** quan hệ tương đương không phân biệt hậu tố $$x\sim_L y$$.
- **Phát biểu** định lý Myhill–Nerode.
- **Áp dụng** định lý để chứng minh ngôn ngữ không chính quy và tìm cận dưới số trạng thái DFA.

</div>

## Quan hệ tương đương Myhill–Nerode

<div class="textbook-definition" markdown="1">

Cho ngôn ngữ $$L \subseteq \Sigma^*$$. Hai chuỗi $$x, y \in \Sigma^*$$ gọi là tương đương theo $$L$$, ký hiệu $$x\sim_L y$$, nếu và chỉ nếu với mọi hậu tố $$z\in\Sigma^*$$:

$$xz\in L\Leftrightarrow yz\in L.$$

</div>

Quan hệ $$\sim_L$$ là một quan hệ tương đương trên $$\Sigma^*$$, phân hoạch tập chuỗi thành các lớp tương đương $$[x]$$.

## Định lý Myhill–Nerode

<div class="textbook-theorem" markdown="1">

**Định lý (Myhill–Nerode).** Ngôn ngữ $$L$$ là chính quy khi và chỉ khi số lớp tương đương của quan hệ $$\sim_L$$ là hữu hạn. Khi đó, DFA tối tiểu nhận $$L$$ có số trạng thái đúng bằng số lớp tương đương này (mỗi lớp ứng với một trạng thái).

</div>

**Ý tưởng chứng minh.**  
Chiều ($$\Rightarrow$$): Nếu có DFA nhận $$L$$, quan hệ “đưa máy về cùng một trạng thái” $$\hat\delta(q_0,x)=\hat\delta(q_0,y)$$ làm mịn quan hệ $$\sim_L$$ (cùng trạng thái thì mọi hậu tố đều cho cùng kết quả), nên số lớp của $$\sim_L$$ không vượt quá $$\lvert Q\rvert$$.  
Chiều ($$\Leftarrow$$): Nếu số lớp hữu hạn, ta dựng trực tiếp DFA trên tập các lớp tương đương với $$\delta([x],a)=[xa]$$ (xác định tốt) và $$F=\{[x]:x\in L\}$$. $$\square$$

## Ứng dụng

Với ngôn ngữ $$L = \{0^n1^n : n \ge 0\}$$, mọi cặp $$0^i$$ và $$0^j$$ ($$i \neq j$$) đều không tương đương vì hậu tố $$z=1^i$$ cho $$0^i1^i \in L$$ nhưng $$0^j1^i \notin L$$. Do đó $$\sim_L$$ có vô hạn lớp tương đương, suy ra $$L$$ không chính quy.

## Tối tiểu hóa DFA

Trong thực hành, ta tối tiểu hóa DFA bằng phương pháp điền bảng (*table-filling*) hoặc tinh chỉnh phân hoạch (*partition refinement*) để gộp các trạng thái không phân biệt được; thuật toán Hopcroft thực hiện việc này trong thời gian $$O(n\log n)$$.

### Minh họa tương tác

Minh họa quá trình tối tiểu hóa DFA bằng cách gộp dần các nhóm trạng thái tương đương:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa101" data-tab="minimize"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chứng minh $$\sim_L$$ là một quan hệ tương đương trên $$\Sigma^*$$.
2. Xác định số lớp tương đương của ngôn ngữ “chuỗi nhị phân có số bit 1 chẵn”.
3. Xét ngôn ngữ $$\{a^ib^jc^k:i=j\text{ hoặc }j=k\}$$ — nên dùng định lý Myhill–Nerode hay bổ đề bơm để chứng minh không chính quy?

## Tài liệu đọc thêm

Sipser (mục bổ sung Myhill–Nerode); Hopcroft (thuật toán tối tiểu hóa); Kozen.

## Tóm tắt

Định lý Myhill–Nerode gắn trực tiếp số trạng thái tối tiểu của DFA với số lớp chuỗi có thể phân biệt bằng hậu tố, đồng thời cung cấp tiêu chuẩn cần và đủ cho tính chính quy.

**Bài tiếp theo:** Máy Turing.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=hOzc4BUIXRk">Minimization of Deterministic Finite Automata (DFA)</a> — Neso Academy, tiếng Anh. Giới thiệu bài toán tối tiểu hóa DFA, ứng dụng trực tiếp của Myhill–Nerode.
- <a href="https://www.youtube.com/watch?v=fWDOqJoKY3k">Myhill-Nerode Theorem for DFA Minimization</a> — Neso Academy, tiếng Anh. Trình bày định lý Myhill–Nerode và quan hệ không phân biệt trạng thái.
- <a href="https://www.youtube.com/watch?v=0XaGAkY09Wc">Minimization of DFA (Example 1)</a> — Neso Academy, tiếng Anh. Ví dụ cụ thể về gộp các trạng thái tương đương.
