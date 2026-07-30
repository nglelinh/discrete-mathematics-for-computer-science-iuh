---
layout: post
title: "Đường đi Ngắn nhất và Thuật toán Dijkstra"
categories: chapter17
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Shortest path: BFS (không trọng số), Dijkstra (trọng số ≥ 0), Bellman–Ford (cạnh âm); relax, heap O((V+E) log V); khác MST."
---

<div class="textbook-epigraph" markdown="1">

"The shortest path is not always the path with the fewest edges."

<span class="epigraph-attribution">— Tinh thần đường đi có trọng số</span>

</div>

GPS và routing mạng trả lời: từ $$s$$ đến $$t$$, đường nào **rẻ nhất** (km, độ trễ, chi phí)? Khi mọi cạnh có độ dài 1, **BFS** (Ch.12) đủ. Khi cạnh mang **trọng số không âm**, cần **Dijkstra**. Mục này định nghĩa single-source shortest path, mô tả Dijkstra, và nêu Bellman–Ford khi có cạnh âm.

![Dijkstra](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_dijkstra_example.svg)

<p class="textbook-figure-caption" data-figure="17.1">Ví dụ Dijkstra từ $$A$$: chốt đỉnh theo dist tăng dần; relax cạnh kề cập nhật ứng viên.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** shortest path không trọng số (BFS) và có trọng số (Dijkstra / Bellman–Ford).
- **Mô tả** Dijkstra: extract-min, **relax**, mảng `parent`.
- **Nêu** độ phức tạp với binary heap $$O((V+E)\log V)$$.
- **Giải thích** vì sao trọng số âm phá Dijkstra; vai trò Bellman–Ford.
- **So sánh** shortest path với **MST** (Ch.16).

**Từ khóa**: single-source shortest path, Dijkstra, relax, priority queue, Bellman–Ford, chu trình âm.

</div>

## 1. Bài toán đường đi ngắn nhất

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho đồ thị $$G=(V,E)$$ (có hướng hoặc vô hướng) với trọng số $$w(e)$$ trên cạnh, và đỉnh nguồn $$s$$. **Khoảng cách ngắn nhất** $$\mathrm{dist}(s,v)$$ là **tổng trọng số nhỏ nhất** trên mọi path từ $$s$$ đến $$v$$. Nếu không có path: $$\mathrm{dist}(s,v)=\infty$$.

</div>

| Loại trọng số | Thuật toán điển hình | Độ phức tạp (tiêu biểu) |
|:---|:---|:---|
| Mọi cạnh độ dài 1 (hoặc không trọng số) | **BFS** | $$O(V+E)$$ |
| $$w(e)\ge 0$$ | **Dijkstra** | $$O((V+E)\log V)$$ (binary heap) |
| Có $$w(e)<0$$ (không chu trình âm, hoặc cần phát hiện) | **Bellman–Ford** | $$O(VE)$$ |

**Khác MST.** MST tối ưu **tập cạnh** nối mọi đỉnh thành cây. Shortest path tối ưu **một path** từ nguồn đến từng đỉnh — cây các cạnh `parent` là *shortest-path tree*, **không** nhất thiết là MST.

## 2. Thuật toán Dijkstra

**Ý tưởng greedy.** Duy trì ước lượng `dist[v]` (ban đầu $$\infty$$, `dist[s]=0`). Lặp: **chốt** đỉnh $$u$$ chưa chốt có `dist` nhỏ nhất; với mỗi cạnh $$(u,v)$$, **relax**:

$$
\text{nếu } \mathrm{dist}[u]+w(u,v) < \mathrm{dist}[v]
\text{ thì } \mathrm{dist}[v] \leftarrow \mathrm{dist}[u]+w(u,v),\ \mathrm{parent}[v]\leftarrow u.
$$

```text
DIJKSTRA(G, w, s):
  dist[v] ← ∞ với mọi v; dist[s] ← 0
  Q ← priority queue chứa các v, key = dist[v]
  while Q ≠ ∅:
    u ← EXTRACT-MIN(Q)
    for mỗi cạnh (u, v) với trọng số w(u,v):
      if dist[u] + w(u,v) < dist[v]:
        dist[v] ← dist[u] + w(u,v)
        parent[v] ← u
        DECREASE-KEY(Q, v)
```

<div class="textbook-theorem" markdown="1">

**Định lý.** Nếu mọi trọng số **không âm**, thì ngay sau khi $$u$$ bị extract-min, $$\mathrm{dist}[u]$$ bằng khoảng cách ngắn nhất thực sự từ $$s$$ đến $$u$$.

</div>

*Phác thảo.* Giả sử $$u$$ là đỉnh chốt sai đầu tiên. Path tối ưu tới $$u$$ phải rời tập đã chốt qua một cạnh; nhờ $$w\ge 0$$, không path nào “đi vòng” rẻ hơn ước lượng đã có khi chốt — mâu thuẫn.

**Độ phức tạp.** Binary heap: $$O((V+E)\log V)$$. Fibonacci heap (lý thuyết): $$O(E + V\log V)$$.

<div class="textbook-example" markdown="1">

**Ví dụ.** Cạnh $$(A,B,1)$$, $$(A,C,4)$$, $$(B,C,2)$$, $$(B,D,6)$$, $$(C,D,1)$$. Từ $$A$$:

- Chốt $$A$$ (0); relax → $$B=1$$, $$C=4$$.
- Chốt $$B$$ (1); relax $$C=\min(4,1+2)=3$$, $$D=7$$.
- Chốt $$C$$ (3); relax $$D=\min(7,3+1)=4$$.
- Chốt $$D$$ (4).

Path tối ưu $$A\to B\to C\to D$$, tổng 4.

</div>

<div class="interactive-demo" markdown="1">
<div data-demo="dijkstra-visualizer"></div>
</div>
<script src="{{ '/public/js/dijkstra-visualizer.js' | relative_url }}"></script>

## 3. Bellman–Ford và trọng số âm

<div class="textbook-theorem" markdown="1">

**Định lý / quan sát.** Nếu tồn tại **chu trình âm** reachable từ $$s$$, khoảng cách ngắn nhất **không bị chặn dưới** (đi vòng vô hạn). **Bellman–Ford** thực hiện $$|V|-1$$ vòng relax mọi cạnh; vòng thứ $$|V|$$ còn cải thiện được $$\implies$$ có chu trình âm.

</div>

**Dijkstra sai** khi có cạnh âm: đỉnh có thể bị chốt quá sớm. Đồ thị **không liên thông** (từ $$s$$): một số `dist` vẫn $$\infty$$ — hợp lệ.

## 4. Ứng dụng

- Routing (mô hình chi phí liên kết); OSPF kiểu shortest path.
- Pathfinding game / lưới có chi phí (A\* = Dijkstra + heuristic admissible).
- Mạng quan hệ với trọng số (không chỉ số hop BFS).

## Bài tập

### Bài tập 1

Với ví dụ mục 2, $$\mathrm{dist}(A,D)=?$$ Path?

<details>
<summary>Đáp án</summary>

$$\mathrm{dist}(A,D)=4$$; path $$A\to B\to C\to D$$ (1+2+1).

</details>

### Bài tập 2

Vì sao BFS không đúng khi cạnh có trọng số 1 và 10?

<details>
<summary>Đáp án</summary>

BFS tối ưu **số cạnh**, không tổng trọng số. Path 2 cạnh tổng 2 có thể rẻ hơn path 1 cạnh trọng số 10 — BFS có thể chọn path “ít hop” đắt hơn.

</details>

### Bài tập 3

Có cạnh $$(A,B,-1)$$. Dùng Dijkstra từ $$A$$ có an toàn không? Thuật toán nào?

<details>
<summary>Đáp án</summary>

Không an toàn. Dùng **Bellman–Ford**; nếu phát hiện chu trình âm reachable thì báo không có shortest path hữu hạn.

</details>

### Bài tập 4

Nêu một khác biệt cốt lõi giữa Dijkstra và Kruskal.

<details>
<summary>Đáp án</summary>

Dijkstra tối ưu path từ nguồn; Kruskal (MST) tối ưu tổng trọng số cây phủ mọi đỉnh, không quan tâm path từ một $$s$$ cố định.

</details>

## Tóm tắt

1. **BFS**: ít cạnh nhất — $$O(V+E)$$.
2. **Dijkstra**: $$w\ge 0$$; greedy + relax + heap.
3. **Bellman–Ford**: cạnh âm; phát hiện chu trình âm.
4. Shortest path ≠ MST.

Trong bài tiếp theo: **sắp xếp topo** trên DAG.
