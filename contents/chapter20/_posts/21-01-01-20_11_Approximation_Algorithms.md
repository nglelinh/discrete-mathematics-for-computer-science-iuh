---
layout: post
title: "Thuật toán Xấp xỉ"
categories: chapter20
date: 2021-01-01
order: 11
required: true
lang: en
excerpt: "Định nghĩa tỉ số xấp xỉ, PTAS và FPTAS; chứng minh thuật toán xấp xỉ tỉ lệ 2 cho Vertex Cover; thuật toán Christofides 3/2 cho Metric TSP và giới hạn không xấp xỉ được."
---

<div class="textbook-epigraph" markdown="1">

"If you cannot solve it exactly in poly-time, solve it approximately — with a proof."

<span class="epigraph-attribution">— Approximation algorithms</span>

</div>

Tính NP-complete loại trừ khả năng giải chính xác trong thời gian đa thức (dưới giả thuyết $$P\neq NP$$). **Thuật toán xấp xỉ** tiếp cận theo hướng khác: chấp nhận lời giải gần tối ưu trong thời gian đa thức nhưng có **bảo đảm chặt chẽ về tỉ lệ sai số**.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** tỉ số xấp xỉ (*approximation ratio*), PTAS và FPTAS.
- **Chứng minh** thuật toán APPROX-VC đạt tỉ lệ xấp xỉ 2.
- **Phát biểu** định lý Christofides cho Metric TSP và tính khó xấp xỉ của TSP tổng quát.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

Đối với bài toán tối thiểu hóa, một thuật toán đạt **tỉ số xấp xỉ** $$\rho \ge 1$$ nếu với mọi thể hiện đầu vào $$I$$, giá trị lời giải $$A(I)$$ thỏa $$A(I)\le\rho\cdot\mathrm{OPT}(I)$$.

- **PTAS** (*Polynomial-Time Approximation Scheme*): với mọi $$\varepsilon>0$$ cố định, cho lời giải tỉ lệ $$1+\varepsilon$$ trong thời gian đa thức theo $$n$$ (số mũ có thể phụ thuộc vào $$1/\varepsilon$$).
- **FPTAS** (*Fully PTAS*): thời gian chạy là đa thức theo cả $$n$$ lẫn $$1/\varepsilon$$.

</div>

## Thuật toán xấp xỉ tỉ lệ 2 cho Vertex Cover

```text
while còn cạnh:
  chọn e={u,v}; thêm u,v vào C; xóa mọi cạnh kề u hoặc v
```

<div class="textbook-theorem" markdown="1">

**Định lý.** Tập đỉnh $$C$$ trả về là một phủ đỉnh hợp lệ và thỏa mãn $$\lvert C\rvert\le 2\,\mathrm{OPT}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.**  
- *Hợp lệ:* mọi cạnh đều chỉ bị xóa sau khi ít nhất một đầu mút của nó được đưa vào $$C$$, nên $$C$$ phủ toàn bộ cạnh của đồ thị.  
- *Tỉ số 2:* gọi $$M$$ là tập các cạnh $$e=\{u,v\}$$ đã được chọn trong vòng lặp. Vì sau mỗi bước ta xóa toàn bộ cạnh kề với $$u$$ và $$v$$, tập $$M$$ là một ghép cặp (*matching*) không chung đỉnh, do đó $$\lvert C\rvert=2\lvert M\rvert$$. Mặt khác, mọi phủ đỉnh tối ưu đều phải chọn ít nhất một đầu mút cho mỗi cạnh trong $$M$$, suy ra $$\mathrm{OPT}\ge\lvert M\rvert$$, và từ đó $$\lvert C\rvert\le 2\,\mathrm{OPT}$$.

</div>

### Thử nghiệm: xấp xỉ gấp đôi cho Vertex Cover

Chọn dần từng cạnh chưa được phủ và thêm cả hai đầu mút vào tập phủ, rồi đối chiếu với phủ đỉnh tối ưu để quan sát tỉ lệ luôn $$\le 2$$:

<div class="interactive-demo" markdown="1">
<div data-demo="reduction-explainer" data-tab="approx"></div>
</div>
<script src="{{ '/public/js/explainers/complexity-explainer.js' | relative_url }}"></script>

## Bài toán Metric TSP

<div class="textbook-theorem" markdown="1">

**Định lý** (Christofides–Serdyukov). Bài toán Metric TSP (trọng số thỏa bất đẳng thức tam giác) có thuật toán xấp xỉ tỉ lệ $$3/2$$ chạy trong thời gian đa thức.

</div>

Ý tưởng thuật toán kết hợp cây khung nhỏ nhất (MST), ghép cặp trọng số nhỏ nhất trên tập các đỉnh bậc lẻ và kỹ thuật đi tắt (*shortcutting*, xem Vazirani Chương 3).

## Giới hạn không thể xấp xỉ (*Inapproximability*)

Với TSP tổng quát (không thỏa bất đẳng thức tam giác), không tồn tại thuật toán xấp xỉ với bất kỳ tỉ số hằng số nào trừ khi $$P=NP$$ (Sahni–Gonzalez). Định lý PCP còn mở đường cho nhiều kết quả giới hạn xấp xỉ sâu hơn đối với MAX-3SAT, CLIQUE và nhiều bài toán tối ưu khác (xem Arora–Barak).

## Bài tập

1. Tự trình bày lại chứng minh thuật toán xấp xỉ tỉ lệ 2 cho Vertex Cover mà không xem tài liệu.
2. Chứng minh rằng tập các đầu mút của **bất kỳ** ghép cặp cực đại theo quan hệ bao hàm (*maximal matching*) nào cũng tạo thành một phủ đỉnh có kích thước $$\le 2\,\mathrm{OPT}$$.
3. Đọc phác thảo chứng minh thuật toán Christofides–Serdyukov.

## Tài liệu đọc thêm

Vazirani; Williamson–Shmoys; Arora–Barak (phần giới thiệu định lý PCP).

## Tóm tắt

Thuật toán xấp xỉ cung cấp bảo đảm định lượng chặt chẽ cho các bài toán NP-hard — tiêu biểu là tỉ lệ 2 cho Vertex Cover và tỉ lệ $$3/2$$ cho Metric TSP — đồng thời gắn liền với lý thuyết giới hạn không thể xấp xỉ.

**Bài tiếp theo:** 20.12 — Độ phức tạp tham số hóa và lớp FPT.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=6t8luYUjw88">Vertex Cover Approximation</a> — Computational Thinking, tiếng Anh. Giới thiệu thuật toán xấp xỉ phủ đỉnh, ví dụ trọng tâm của bài.
- <a href="https://www.youtube.com/watch?v=nwZjiQra0EA">Approximation Algorithms: Introduction by the Example of Vertex Cover</a> — Algorithms Lab, tiếng Anh. Phân tích tỉ số xấp xỉ trên bài toán Vertex Cover.
- <a href="https://www.youtube.com/watch?v=xyqIXdUXeU0">Approximation Algorithms 1 - Introduction and  Vertex Cover Problem</a> — Learn@Home, tiếng Anh. Khung lý thuyết thuật toán xấp xỉ trước khi đi vào chứng minh chi tiết.
