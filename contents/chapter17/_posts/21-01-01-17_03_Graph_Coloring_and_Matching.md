---
layout: post
title: "Tô màu Đồ thị và Ghép cặp"
categories: chapter17
date: 2021-01-01
order: 3
required: false
lang: en
excerpt: "Tô màu đỉnh, số sắc χ(G), greedy coloring; matching bipartite; liên hệ scheduling, register allocation và NP-hard."
---

<div class="textbook-epigraph" markdown="1">

"Color so that neighbors disagree — match so that no two edges share a vertex."

<span class="epigraph-attribution">— Tinh thần tô màu và matching</span>

</div>

Xếp lịch thi: hai môn trùng sinh viên không cùng ca. Gán thanh ghi: hai biến sống đồng thời không dùng chung register. Cả hai mô hình bằng **tô màu đỉnh**. Ghép job–máy hoặc mentor–mentee là **matching** trên đồ thị hai phía. Mục tùy chọn này giới thiệu hai họ bài toán và chỗ chúng đứng so với Dijkstra / topo (đa thức) và TSP / tô màu tối ưu (NP-hard — Ch.20).

![Tô màu](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_coloring_example.svg)

<p class="textbook-figure-caption" data-figure="17.3">Tô màu: hai đỉnh kề khác màu; số màu tối thiểu là số sắc $$\chi(G)$$.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** tô màu đỉnh và số sắc $$\chi(G)$$.
- **Áp dụng** greedy coloring; nêu $$\chi$$ cho cây, $$C_n$$, $$K_n$$.
- **Định nghĩa** matching và matching lớn nhất trên đồ thị hai phía.
- **Đặt** các bài toán vào phổ độ khó (đa thức vs NP-hard).

**Từ khóa**: graph coloring, chromatic number, greedy coloring, bipartite matching, NP-hard.

</div>

## 1. Tô màu đỉnh

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Tô màu đỉnh** gán mỗi đỉnh một màu sao cho hai đỉnh **kề nhau** không cùng màu. **Số sắc** $$\chi(G)$$ là số màu **ít nhất** đủ để tô $$G$$ hợp lệ.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1** (lịch thi). Môn = đỉnh; cạnh nối hai môn có sinh viên chung. Mỗi **màu** = một **ca thi**. $$\chi(G)$$ = số ca tối thiểu (lý thuyết).

</div>

**Greedy coloring.** Duyệt đỉnh theo một thứ tự; gán màu dương nhỏ nhất chưa dùng bởi các hàng xóm đã tô. Luôn cho tô hợp lệ với $$\le \Delta(G)+1$$ màu ($$\Delta$$ = bậc lớn nhất), nhưng **không** luôn đạt $$\chi$$.

| Lớp đồ thị | $$\chi$$ |
|:---|:---|
| Cây có cạnh | $$2$$ |
| Chu trình $$C_n$$ | $$2$$ nếu $$n$$ chẵn; $$3$$ nếu $$n$$ lẻ |
| Đầy đủ $$K_n$$ | $$n$$ |
| Hai phía (có cạnh) | $$2$$ |

<div class="textbook-theorem" markdown="1">

**Định lý** (Brooks — ý). Nếu $$G$$ liên thông, không phải $$K_n$$ và không phải chu trình lẻ, thì $$\chi(G)\le \Delta(G)$$. Việc tính $$\chi(G)$$ tối ưu trên đồ thị tổng quát là **NP-hard**.

</div>

**Ứng dụng CS:** register allocation (interference graph), xếp kênh tần số, map coloring cổ điển.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-coloring-interactive"></div>
</div>
<script src="{{ '/public/js/graph-coloring-interactive.js' | relative_url }}"></script>

## 2. Đồ thị hai phía và ghép cặp

![Matching](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_bipartite_matching.svg)

<p class="textbook-figure-caption" data-figure="17.4">Matching: tập cạnh không chung đỉnh; trên bipartite tìm matching lớn nhất trong thời gian đa thức.</p>

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **Đồ thị hai phía**: $$V=L\cup R$$, mọi cạnh nối $$L$$–$$R$$.
- **Matching**: tập cạnh **không** hai cạnh nào chung đỉnh.
- **Matching lớn nhất**: matching có lực lượng cực đại (trên bipartite: thuật toán đường tăng / Hopcroft–Karp $$O(E\sqrt{V})$$).

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** $$L=\{1,2\}$$, $$R=\{a,b,c\}$$; cạnh $$1a,1b,2b,2c$$. Matching size 2: ví dụ $$\{1a,2c\}$$.

</div>

Ứng dụng: gán task–worker, matching sinh viên–đề tài, assignment.

## 3. Bản đồ độ khó (chương 12–17)

| Bài toán | Lớp điển hình | Độ khó (giáo trình) |
|:---|:---|:---|
| BFS / DFS / topo / Euler | Đồ thị / DAG | **P** (đa thức) |
| Dijkstra ($$w\ge 0$$) | Trọng số không âm | **P** |
| Matching max bipartite | Hai phía | **P** |
| MST | Vô hướng có trọng số | **P** |
| Tô màu tối ưu $$\chi$$ | Vô hướng tổng quát | **NP-hard** |
| Hamilton / TSP | Vô hướng / tối ưu | **NP-hard** (Ch.12, Ch.20) |

Chương 17 bổ sung thuật toán **đa thức** quan trọng (shortest path, topo) và **preview** các bài NP-hard qua tô màu / Hamilton.

## 4. Tổng quan Chương 17

1. **Shortest path** — Dijkstra, routing.  
2. **Topo sort** — DAG, build, scheduling.  
3. **Coloring / matching** — tài nguyên hữu hạn, ghép cặp.

## Bài tập

### Bài tập 1

$$\chi(C_5)=?$$ Greedy theo thứ tự vòng có thể dùng bao nhiêu màu?

<details>
<summary>Đáp án</summary>

$$\chi(C_5)=3$$ (chu trình lẻ). Greedy theo vòng thường dùng 3 màu — đạt tối ưu trên ví dụ này; trên đồ thị khác greedy có thể dùng thừa màu.

</details>

### Bài tập 2

Ba môn A,B,C: cạnh A–B, B–C (trùng SV); không cạnh A–C. Số ca tối thiểu?

<details>
<summary>Đáp án</summary>

Đường A–B–C: $$\chi=2$$ (A và C cùng ca; B ca khác).

</details>

### Bài tập 3

Matching lớn nhất trên ví dụ mục 2 có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

**2** (ví dụ $$1a$$ và $$2c$$).

</details>

### Bài tập 4

Vì sao tô màu tối ưu “khó hơn” matching bipartite trong giáo trình này?

<details>
<summary>Đáp án</summary>

Matching max bipartite có thuật toán đa thức. Tính $$\chi(G)$$ tổng quát là NP-hard — không kỳ vọng thuật toán đa thức đơn giản như Dijkstra/topo.

</details>

## Tóm tắt

1. **Tô màu**: hàng xóm khác màu; $$\chi$$; greedy; tối ưu NP-hard.
2. **Matching bipartite**: ghép không chung đỉnh; max matching ∈ P.
3. Ch.17: thuật toán đa thức + cửa sổ sang NP-hard (Ch.20).

Chương 18 trở đi: **mô hình tính toán** — automata và ngôn ngữ hình thức.
