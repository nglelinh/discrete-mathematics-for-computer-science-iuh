---
layout: post
title: "Xây dựng tập con: NFA ≡ DFA"
categories: chapter18
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Định lý tương đương Rabin–Scott giữa NFA và DFA, chứng minh L(D)=L(N), cận trên 2^|Q| trạng thái và tối ưu chỉ xét các tập con đạt được."
---

<div class="textbook-epigraph" markdown="1">

"Powerset construction trades nondeterminism for exponentially many states."

<span class="epigraph-attribution">— Rabin–Scott</span>

</div>

![Subset](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_subset_construction.svg)

<p class="textbook-figure-caption" data-figure="18.3">Mỗi trạng thái của DFA tương ứng với một tập con các trạng thái của NFA.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Xây dựng** DFA tương đương từ một NFA (có hoặc không có chuyển ε).
- **Chứng minh** đẳng thức ngôn ngữ $$L(D)=L(N)$$.
- **Nêu** cận trên số trạng thái $$2^{\lvert Q\rvert}$$ và hiện tượng bùng nổ trạng thái.

</div>

## Phép xây dựng tập con (không có ε)

Từ NFA $$N=(Q_N,\Sigma,\delta_N,q_0,F_N)$$, ta xây dựng DFA $$D$$ như sau: tập trạng thái $$Q_D=\mathcal{P}(Q_N)$$ (trong thực tế chỉ cần giữ các tập con đạt được từ trạng thái đầu), trạng thái khởi đầu $$q_{D0}=\{q_0\}$$, hàm chuyển $$\delta_D(S,a)=\bigcup_{q\in S}\delta_N(q,a)$$, và tập trạng thái kết thúc $$F_D=\{S \in Q_D : S\cap F_N\neq\emptyset\}$$.

**Trường hợp có chuyển ε:** ta đặt $$q_{D0}=E(\{q_0\})$$ và $$\delta_D(S,a)=E\bigl(\bigcup_{q\in S}\delta_N(q,a)\bigr)$$.

### Video ngắn: Từ NFA sang DFA

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/nfa-to-dfa-subset-construction.mp4"></video>
</div>

Video dài khoảng 2 phút 56 giây: xét NFA nhận các chuỗi bắt đầu bằng 1 và kết thúc bằng 01, theo dõi tập trạng thái đang hoạt động khi đọc chuỗi, lập bảng chuyển DFA từng hàng, xử lý trạng thái chết $$\varnothing$$, chạy thử DFA thu được và giải thích vì sao số trạng thái có thể tăng đến $$2^n$$.

## Định lý tương đương

<div class="textbook-theorem" markdown="1">

**Định lý** (Rabin–Scott). Với mọi NFA $$N$$, luôn tồn tại một DFA $$D$$ sao cho $$L(D)=L(N)$$ và $$\lvert Q_D\rvert\le 2^{\lvert Q_N\rvert}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.**  
Bất biến: sau khi đọc bất kỳ chuỗi $$w \in \Sigma^*$$, trạng thái hiện tại của DFA $$D$$ chính là tập trạng thái $$\hat\delta_N(\{q_0\},w)$$ (hoặc phiên bản có bao đóng ε). Bất biến này được chứng minh trực tiếp bằng quy nạp theo độ dài chuỗi $$w$$.  
Do đó, $$D$$ chấp nhận $$w$$ khi và chỉ khi tập trạng thái kết thúc có giao khác rỗng với $$F_N$$, tức là khi và chỉ khi $$w\in L(N)$$. Vì mỗi trạng thái của $$D$$ là một tập con của $$Q_N$$ nên số trạng thái tối đa là $$2^{\lvert Q_N\rvert}$$.

</div>

## Bùng nổ trạng thái (*state explosion*)

Cận trên hàm mũ là chặt: tồn tại những họ ngôn ngữ mà DFA tối tiểu bắt buộc phải có $$\Omega(2^n)$$ trạng thái trong khi NFA chỉ cần $$O(n)$$ trạng thái (chẳng hạn ngôn ngữ “ký tự thứ $$n$$ tính từ cuối là 1”).

### Minh họa tương tác

Theo dõi phép xây dựng tập con từng bước để thấy bảng chuyển và sơ đồ DFA hiện dần (một NFA 4 trạng thái tạo ra DFA 8 trạng thái):

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa3" data-tab="subset"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Áp dụng phép xây dựng tập con lên NFA nhận chuỗi kết thúc bằng `01` và liệt kê các trạng thái đạt được.
2. Chứng minh rằng việc loại bỏ các tập con không đạt được từ $$q_{D0}$$ không làm thay đổi ngôn ngữ $$L(D)$$.
3. Tìm thêm một ví dụ về hiện tượng bùng nổ trạng thái (tham khảo Sipser).

## Tài liệu đọc thêm

Sipser §1.2; Hopcroft–Ullman.

## Tóm tắt

Phép xây dựng tập con (*powerset construction*) chứng minh NFA và DFA có cùng sức mạnh biểu diễn ngôn ngữ, với chi phí tối đa $$2^{\lvert Q\rvert}$$ trạng thái.

**Bài tiếp theo:** Máy Mealy và máy Moore.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=--CSVsFIDng">Conversion of NFA to DFA</a> — Neso Academy, tiếng Anh. Giới thiệu cách dựng DFA từ các tập con trạng thái của NFA.
- <a href="https://www.youtube.com/watch?v=pnyXgIXpKnc">Conversion of NFA to DFA (Example 1)</a> — Neso Academy, tiếng Anh. Ví dụ thứ nhất về phép xây dựng tập con.
- <a href="https://www.youtube.com/watch?v=i-fk9o46oVY">Conversion of NFA to DFA (Example 2)</a> — Neso Academy, tiếng Anh. Ví dụ thứ hai giúp đối chiếu với chứng minh tương đương.
