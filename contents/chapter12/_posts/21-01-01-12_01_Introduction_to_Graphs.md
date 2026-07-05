---
layout: post
title: "Giới thiệu Đồ thị"
categories: chapter12
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Chương này giới thiệu lý thuyết đồ thị — mô hình toán học cho mạng, quan hệ và phụ thuộc. Mục 12.1 định nghĩa đồ thị G = (V, E), các loại đồ thị, bậc đỉnh và định lý bắt tay."
---

<div class="textbook-epigraph" markdown="1">

"The Königsberg bridge problem is an example of a problem that could be solved only by means of graph theory."

<span class="epigraph-attribution">— Leonhard Euler</span>

</div>

Trong Chương 5 chúng ta đã học **quan hệ** như tập cặp có thứ tự. **Đồ thị** (graph) là cách trực quan hóa quan hệ: đỉnh là đối tượng, cạnh là liên kết. Mạng xã hội, sơ đồ phụ thuộc module, routing Internet, call graph và dependency graph trong CI/CD đều là đồ thị trong thực tế. Mục 12.1 này đặt nền tảng định nghĩa và phân loại.

![Đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="12.1">Đồ thị có hướng: cạnh $(u,v)$ biểu diễn quan hệ một chiều — ví dụ quyền truy cập hoặc luồng dữ liệu.</p>
![Đồ thị vô hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="12.2">Đồ thị vô hướng: cạnh $\{u,v\}$ — quan hệ hai chiều, ví dụ kết bạn trên mạng xã hội.</p>
![Ví dụ đồ thị đơn giản](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="12.3">Đồ thị đơn giản: tập đỉnh và tập cạnh hữu hạn — mô hình cơ bản cho thuật toán đồ thị.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** đồ thị $$G = (V, E)$$ và phân loại vô hướng / có hướng / có trọng số.
- **Tính** bậc đỉnh và áp dụng **định lý bắt tay**.
- **Nhận biết** đồ thị đơn, đa đồ thị, đồ thị đầy đủ $$K_n$$, đồ thị hai phía.
- **Mô hình hóa** bài toán CNTT bằng đồ thị (mạng, phụ thuộc, luồng điều khiển).

**Từ khóa**: đồ thị (graph), đỉnh (vertex), cạnh (edge), bậc (degree), định lý bắt tay (handshaking lemma), đồ thị hai phía (bipartite).
</div>

## Định nghĩa đồ thị

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **đồ thị** là bộ đôi $$G = (V, E)$$ trong đó:

- $$V$$: tập **đỉnh** (vertices / nodes) hữu hạn, không rỗng.
- $$E$$: tập **cạnh** (edges) — mỗi cạnh nối một hoặc hai đỉnh.

**Đồ thị vô hướng**: $$E$$ là tập các cặp không thứ tự $$\{u, v\}$$ với $$u, v \in V$$.

**Đồ thị có hướng** (digraph): $$E$$ là tập các cặp có thứ tự $$(u, v)$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (mô hình hóa):

| Bài toán | Đỉnh $$V$$ | Cạnh $$E$$ |
|:---|:---|:---|
| Mạng xã hội | Người dùng | Quan hệ bạn bè |
| Dependency graph | Module / package | `A` phụ thuộc `B` |
| Call graph | Hàm | `f` gọi `g` |
| Trang web | URL | Link hypertext |
</div>

## Các loại đồ thị

| Loại | Đặc điểm |
|:---|:---|
| **Đơn đồ thị** | Tối đa một cạnh giữa hai đỉnh; không khuyên $$(v,v)$$ |
| **Đa đồ thị** | Cho phép nhiều cạnh song song |
| **Có trọng số** | Mỗi cạnh có cost / weight |
| **Đồ thị đầy đủ** $$K_n$$ | $$n$$ đỉnh, mọi cặp khác nhau có cạnh; $$|E| = \binom{n}{2}$$ (vô hướng) |
| **Đồ thị hai phía** | $$V = A \cup B$$, cạnh chỉ nối $$A$$–$$B$$ |

## Bậc đỉnh và định lý bắt tay

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong đồ thị **vô hướng**, **bậc** $$\deg(v)$$ của đỉnh $$v$$ là số cạnh incident với $$v$$. Trong đồ thị **có hướng**: **bậc ra** $$\deg^+(v)$$, **bậc vào** $$\deg^-(v)$$.
</div>

<div class="textbook-theorem" markdown="1">
**Định lý** (Handshaking Lemma): Với đồ thị vô hướng $$G = (V,E)$$,

$$\sum_{v \in V} \deg(v) = 2|E|$$

**Hệ quả**: Số đỉnh có bậc lẻ là **số chẵn**.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Đồ thị có 5 đỉnh, tổng bậc = 12. Suy ra $$|E| = 12/2 = 6$$.
</div>

![Control flow graph](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

<p class="textbook-figure-caption" data-figure="12.4">Control-flow graph — đỉnh là basic block, cạnh là nhánh điều khiển; nền tảng phân tích chương trình.</p>
## Bài tập

### Bài tập 1

Đồ thị vô hướng có 8 đỉnh, mỗi đỉnh bậc 3. Có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

$$\sum \deg = 8 \cdot 3 = 24 = 2|E|$$ → $$|E| = 12$$.

</details>

### Bài tập 2

$$K_5$$ có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

$$\binom{5}{2} = 10$$.

</details>

### Bài tập 3

Cho danh sách bậc: 3, 3, 2, 2, 2, 2. Có thể là đồ thị vô hướng đơn không? Tính $$|E|$$.

<details>
<summary>Đáp án</summary>

Tổng bậc = 14 → $$|E| = 7$$. Số đỉnh bậc lẻ = 2 (chẵn) — **có thể** tồn tại (cần thêm điều kiện đồ thị thực sự, nhưng handshaking không cấm).

</details>

## Tóm tắt

- **Đồ thị** $$G=(V,E)$$: mô hình mạng và quan hệ.
- Phân loại: vô hướng / có hướng / có trọng số; đơn / đa; $$K_n$$; hai phía.
- **Handshaking**: $$\sum \deg(v) = 2|E|$$; số đỉnh bậc lẻ chẵn.
- Ứng dụng CS: social graph, dependency, CFG, routing.

Trong bài tiếp theo, chúng ta học **biểu diễn đồ thị** bằng ma trận kề và danh sách kề — quyết định hiệu năng thuật toán.