---
layout: post
title: "Xây dựng tập con: NFA ≡ DFA"
categories: chapter18
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Định lý tương đương; chứng minh L(D)=L(N); bound 2^|Q|; reachable only."
---


<div class="textbook-epigraph" markdown="1">

"Powerset construction trades nondeterminism for exponentially many states."

<span class="epigraph-attribution">— Rabin–Scott</span>

</div>

![Subset](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_subset_construction.svg)

<p class="textbook-figure-caption" data-figure="18.3">Trạng thái DFA = tập trạng thái NFA.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Xây** DFA từ NFA (có/không ε).
- **Chứng minh** $$L(D)=L(N)$$.
- **Nêu** bound $$2^{\lvert Q\rvert}$$.

</div>

## Construction (không ε)

$$Q_D=\mathcal{P}(Q_N)$$ (hoặc chỉ reachable).  
$$q_{D0}=\{q_0\}$$.  
$$\delta_D(S,a)=\bigcup_{q\in S}\delta_N(q,a)$$.  
$$F_D=\{S:S\cap F_N\neq\emptyset\}$$.

**Có ε:** $$q_{D0}=E(\{q_0\})$$; $$\delta_D(S,a)=E(\bigcup\delta_N(q,a))$$.

### Video ngắn: Từ NFA sang DFA

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/nfa-to-dfa-subset-construction.mp4"></video>
</div>

Video dài khoảng 2 phút 56 giây: NFA nhận các chuỗi bắt đầu bằng 1 và kết thúc bằng 01, theo dõi tập trạng thái đang bật khi đọc chuỗi, lập bảng chuyển DFA từng hàng, trạng thái chết $$\varnothing$$, chạy thử DFA thu được, và vì sao số trạng thái có thể lên tới $$2^n$$.

## Định lý

<div class="textbook-theorem" markdown="1">

**Định lý** (Rabin–Scott). Với mọi NFA $$N$$ tồn tại DFA $$D$$: $$L(D)=L(N)$$ và $$\lvert Q_D\rvert\le 2^{\lvert Q_N\rvert}$$.

</div>

<div class="textbook-proof" markdown="1">
**Chứng minh.**  
Bất biến: sau đọc $$w$$, trạng thái $$D$$ là $$\hat\delta_N(\{q_0\},w)$$ (hoặc closure). Quy nạp độ dài $$w$$.  
Chấp nhận ⇔ giao $$F\neq\emptyset$$ ⇔ $$w\in L(N)$$.  
Số tập con $$\le 2^{\lvert Q\rvert}$$.
</div>

## State explosion

Tồn tại family ngôn ngữ DFA tối tiểu $$\Omega(2^n)$$ trong khi NFA $$O(n)$$ (ví dụ “ký tự thứ $$n$$ từ cuối là 1”).

### Minh hoạ tương tác

Minh hoạ otomat: xây dựng tập con từng bước, thấy bảng chuyển và DFA hiện dần; NFA 4 trạng thái cho DFA 8 trạng thái. Các widget có sẵn bên trên vẫn giữ nguyên.

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa3" data-tab="subset"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chạy subset trên NFA ends-01; liệt kê reachable.  
2. Chứng minh chỉ cần reachable subset.  
3. Tìm example explosion (Sipser).

## Đọc

Sipser §1.2; Hopcroft–Ullman.

## Tóm tắt

Powerset · $$L$$ bảo toàn · $$2^n$$ bound.

**Tiếp:** Mealy/Moore.

## Video tham khảo

- **xem trước** <a href="https://www.youtube.com/watch?v=--CSVsFIDng">Conversion of NFA to DFA</a> — Neso Academy, tiếng Anh. Xem trước dựng DFA từ tập con trạng thái của NFA.
- <a href="https://www.youtube.com/watch?v=pnyXgIXpKnc">Conversion of NFA to DFA (Example 1)</a> — Neso Academy, tiếng Anh. Ví dụ subset construction thứ nhất.
- <a href="https://www.youtube.com/watch?v=i-fk9o46oVY">Conversion of NFA to DFA (Example 2)</a> — Neso Academy, tiếng Anh. Ví dụ thứ hai, đối chiếu với chứng minh tương đương.
