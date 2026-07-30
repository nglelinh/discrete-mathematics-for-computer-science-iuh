---
layout: post
title: "Đường đi, Chu trình và Liên thông"
categories: chapter12
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Walk, trail, path, cycle; liên thông vô hướng; liên thông yếu/mạnh trên digraph; thành phần liên thông, DAG và phụ thuộc vòng."
---

<div class="textbook-epigraph" markdown="1">

"Connectivity is the global shape of a graph; paths are how that shape is experienced locally."

<span class="epigraph-attribution">— Tinh thần lý thuyết đồ thị</span>

</div>

Biểu diễn đồ thị cho biết **ai kề ai**. Nhiều câu hỏi thực tế đòi hỏi thêm cấu trúc toàn cục: hai máy có thông được không, module có phụ thuộc vòng không, tập trang web có tách thành các cụm rời không. Các khái niệm **đường đi**, **chu trình** và **liên thông** trả lời các câu hỏi đó một cách hình thức và là nền cho BFS, DFS, Union–Find, cũng như phát hiện circular dependency trong hệ thống build.

![Walk, path và cycle](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_path_cycle_walk.svg)

<p class="textbook-figure-caption" data-figure="12.6">Cùng một đồ thị: path không lặp đỉnh; cycle là path đóng; walk cho phép lặp đỉnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** walk, trail, path và cycle theo ràng buộc lặp đỉnh/cạnh.
- **Định nghĩa** đồ thị liên thông (vô hướng) và liên thông yếu / mạnh (có hướng).
- **Xác định** thành phần liên thông và nêu vai trò trong phân tích mạng.
- **Giải thích** DAG và hệ quả của chu trình trên dependency graph.

**Từ khóa**: walk, trail, path, cycle, liên thông (connected), thành phần liên thông (connected component), DAG.

</div>

## 1. Walk, trail, path, cycle

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho đồ thị $$G = (V,E)$$ (tạm thời vô hướng; biến thể có hướng đọc cạnh theo hướng).

- **Walk** (*đi bộ*): dãy đỉnh $$v_0, v_1, \ldots, v_k$$ ($$k \ge 0$$) sao cho mỗi cặp liên tiếp $$\{v_i, v_{i+1}\}$$ là cạnh. Đỉnh và cạnh **được phép lặp**.
- **Trail**: walk **không lặp cạnh**.
- **Path** (*đường đi đơn*): walk **không lặp đỉnh** (do đó cũng không lặp cạnh).
- **Cycle** (*chu trình*): dãy $$v_0, v_1, \ldots, v_k$$ với $$k \ge 3$$, $$v_0 = v_k$$, các đỉnh $$v_0,\ldots,v_{k-1}$$ đôi một khác nhau, và mỗi cặp liên tiếp là cạnh.

**Độ dài** của walk/path/cycle là số cạnh trên dãy (bằng $$k$$ trong ký hiệu trên).

</div>

Thứ tự ràng buộc tăng dần:

$$
\text{walk} \;\supset\; \text{trail} \;\supset\; \text{path};
$$

cycle là dạng đóng của path (với độ dài tối thiểu 3 trên đồ thị đơn vô hướng).

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Trên Hình 12.6:

- $$A\text{–}B\text{–}C\text{–}D$$ là **path** độ dài 3;
- $$B\text{–}C\text{–}F\text{–}E\text{–}B$$ là **cycle** độ dài 4;
- $$A\text{–}B\text{–}E\text{–}F\text{–}C\text{–}B\text{–}D$$ là **walk** nhưng không phải path vì đỉnh $$B$$ xuất hiện hai lần.

</div>

Trên **đồ thị có hướng**, định nghĩa tương tự với cạnh $$(v_i, v_{i+1})$$ theo đúng hướng. Khi đó path và cycle đều mang hướng; không được “đi ngược” cạnh.

## 2. Liên thông trên đồ thị vô hướng

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Đồ thị vô hướng $$G$$ **liên thông** (*connected*) nếu với mọi cặp đỉnh $$u, v \in V$$ tồn tại một path nối $$u$$ và $$v$$.

**Thành phần liên thông** (*connected component*) là tập con đỉnh tối đại sao cho đồ thị con cảm sinh trên tập đó liên thông. Nói cách khác: các thành phần phân hoạch $$V$$; trong mỗi thành phần mọi cặp đỉnh nối được bằng path, và không có cạnh nào nối hai thành phần khác nhau.

</div>

![Thành phần liên thông](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_connected_components.svg)

<p class="textbook-figure-caption" data-figure="12.7">Ba thành phần liên thông: không tồn tại đường đi giữa các cụm khác nhau.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Đồ thị với cạnh $$AB$$, $$BC$$, $$CD$$ có đúng **một** thành phần $$\{A,B,C,D\}$$ — đây là đồ thị đường (*path graph*) liên thông.

Nếu thêm đỉnh cô lập $$E$$ (không cạnh), số thành phần tăng lên 2: $$\{A,B,C,D\}$$ và $$\{E\}$$.

</div>

Kiểm tra liên thông / liệt kê thành phần được thực hiện bằng BFS hoặc DFS từ một đỉnh, rồi lặp trên các đỉnh chưa thăm (Mục 12.4). Cấu trúc Union–Find (*disjoint-set*) xử lý cùng bài toán khi cạnh được thêm dần (ví dụ Kruskal).

## 3. Liên thông trên đồ thị có hướng

Bỏ hướng cạnh tạo ra một đồ thị vô hướng nền. Từ đó có hai mức liên thông:

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho digraph $$G$$:

- $$G$$ **liên thông yếu** nếu đồ thị vô hướng thu được khi bỏ hướng mọi cạnh là liên thông.
- $$G$$ **liên thông mạnh** nếu với mọi cặp $$u, v$$ tồn tại path **có hướng** từ $$u$$ đến $$v$$ **và** từ $$v$$ đến $$u$$.

**Thành phần liên thông mạnh** (SCC — *strongly connected component*) là tập đỉnh tối đại cảm sinh đồ thị con liên thông mạnh.

</div>

Liên thông mạnh $$\implies$$ liên thông yếu; chiều ngược lại sai.

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Digraph với cạnh $$1\to 2$$, $$2\to 3$$, $$1\to 3$$:

- **Liên thông yếu**: có — bỏ hướng vẫn là đường/tam giác mở liên thông.
- **Liên thông mạnh**: **không** — không có path có hướng từ 3 về 1 (hay về 2).

</div>

## 4. DAG và chu trình phụ thuộc

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **DAG** (*Directed Acyclic Graph*) là đồ thị có hướng **không chứa chu trình** có hướng.

</div>

DAG là mô hình chuẩn cho:

- thứ tự biên dịch / build khi không có circular dependency;
- task scheduling với ràng buộc “việc $$A$$ trước việc $$B$$”;
- một số lược đồ dữ liệu và pipeline xử lý.

Trên DAG luôn tồn tại **thứ tự tôpô** (*topological order*): đánh số đỉnh sao cho mọi cạnh đi từ chỉ số nhỏ hơn sang lớn hơn. Ngược lại, nếu có chu trình thì không tồn tại thứ tự tôpô — hệ thống build báo lỗi phụ thuộc vòng.

<div class="textbook-example" markdown="1">

**Ví dụ 4** (CS). Nếu dependency graph chứa cạnh

$$
A \to B \to C \to A,
$$

thì ba module tạo thành chu trình có hướng. Không có thứ tự build hợp lệ: mỗi module đòi hỏi một module khác trong vòng đã được build trước. Đây là lỗi kiến trúc, không chỉ lỗi cú pháp.

</div>

## 5. Đồ thị con và clique

**Đồ thị con** $$G' = (V', E')$$ của $$G$$ thỏa $$V' \subseteq V$$ và $$E' \subseteq E$$, đồng thời mọi cạnh trong $$E'$$ chỉ nối các đỉnh thuộc $$V'$$.

**Clique** là tập đỉnh trong đó mọi cặp phân biệt đều có cạnh — đồ thị con cảm sinh là $$K_r$$ với $$r$$ bằng lực lượng tập. Clique xuất hiện trong phân cụm quan hệ chặt (nhóm bạn bè đầy đủ, module gọi nhau đầy đủ theo nghĩa vô hướng hóa).

## 6. Thử nghiệm tương tác

Bật/tắt cạnh và quan sát ma trận kề. Khi một đỉnh có cả hàng và cột toàn 0, đỉnh đó là thành phần cô lập. Khi đồ thị tách thành nhiều cụm, các khối 1 trên ma trận (sau hoán vị đỉnh) phản ánh thành phần liên thông.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-adjacency-builder"></div>
</div>
<script src="{{ '/public/js/graph-adjacency-builder.js' | relative_url }}"></script>


## Bài tập

### Bài tập 1

Đồ thị vô hướng với các cạnh $$AB$$, $$BC$$, $$CD$$. Có bao nhiêu thành phần liên thông? Liệt kê.

<details>
<summary>Đáp án</summary>

Một thành phần: $$\{A,B,C,D\}$$. Mọi cặp đỉnh nối được bằng path dọc theo đường.

</details>

### Bài tập 2

Phân biệt walk và path. Walk $$A \to B \to C \to B \to D$$ có phải path không?

<details>
<summary>Đáp án</summary>

Không. Đỉnh $$B$$ lặp, nên đây là walk (thậm chí có thể là trail nếu không lặp cạnh) nhưng **không** phải path đơn.

</details>

### Bài tập 3

Digraph: $$1\to 2$$, $$2\to 3$$, $$1\to 3$$. Liên thông mạnh? Liên thông yếu?

<details>
<summary>Đáp án</summary>

**Yếu**: có. **Mạnh**: không — thiếu đường về từ 3 (và từ 2 về 1).

</details>

### Bài tập 4

Chứng minh ngắn: trên đồ thị vô hướng, quan hệ “có path nối $$u$$ và $$v$$” (kể cả path độ dài 0 khi $$u=v$$) là quan hệ tương đương trên $$V$$. Các lớp tương đương là gì?

<details>
<summary>Đáp án</summary>

- Phản xạ: path độ dài 0 tại mỗi đỉnh.
- Đối xứng: đảo dãy đỉnh của path (vô hướng).
- Bắc cầu: nối hai path tại đỉnh chung.

Các lớp tương đương chính là **thành phần liên thông**.

</details>

### Bài tập 5

Hệ thống có cạnh phụ thuộc `app→ui`, `app→api`, `ui→core`, `api→core`, `core→app`. Đây có phải DAG không? Vì sao?

<details>
<summary>Đáp án</summary>

Không phải DAG. Ví dụ chu trình: $$\mathrm{app}\to\mathrm{ui}\to\mathrm{core}\to\mathrm{app}$$.

</details>

## Tóm tắt

1. **Walk / trail / path / cycle** siết dần điều kiện không lặp; độ dài = số cạnh.
2. Đồ thị vô hướng **liên thông** khi mọi cặp đỉnh có path; **thành phần liên thông** phân hoạch tập đỉnh.
3. Trên digraph: **liên thông yếu** (bỏ hướng) và **liên thông mạnh** (đi hai chiều theo hướng cạnh).
4. **DAG** không chu trình có hướng — điều kiện cần cho thứ tự tôpô và build không vòng.

Trong bài tiếp theo, ta xét hai kiểu “đi hết” đặc biệt — **Euler** (cạnh) và **Hamilton** (đỉnh) — cùng hai thuật toán duyệt nền tảng **BFS** và **DFS**.
