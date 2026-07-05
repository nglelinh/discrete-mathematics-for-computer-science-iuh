---
layout: post
title: "Đường đi Ngắn nhất và Thuật toán Dijkstra"
categories: chapter17
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Mục 17.1 phân biệt shortest path không trọng số (BFS) và có trọng số không âm (Dijkstra), cùng độ phức tạp O((V+E) log V) và ứng dụng routing mạng."
---

GPS và router mạng đều trả lời cùng một câu hỏi: từ điểm A đến B, đường nào **rẻ nhất** (ít km, ít độ trễ, ít hop)? Khi cạnh có **trọng số không âm**, BFS không đủ — ta cần **Dijkstra**. Mục 17.1 xây dựng bài toán shortest path và thuật toán kinh điển năm 1959.

![Đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="17.1">Đồ thị có trọng số — mỗi cạnh mang chi phí; shortest path tối thiểu tổng trọng số.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** shortest path không trọng số (BFS) và có trọng số (Dijkstra, Bellman-Ford).
- **Mô tả** thuật toán Dijkstra với priority queue.
- **Phân tích** độ phức tạp $$O((V+E)\log V)$$ với binary heap.
- **Giải thích** vì sao trọng số âm phá vỡ Dijkstra.

**Từ khóa**: single-source shortest path, Dijkstra, relax, priority queue, Bellman-Ford.
</div>

## Bài toán đường đi ngắn nhất

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho đồ thị $$G = (V, E)$$ với trọng số $$w(e) \geq 0$$ trên mỗi cạnh và đỉnh nguồn $$s$$. **Khoảng cách ngắn nhất** $$\text{dist}(s, v)$$ là tổng trọng số nhỏ nhất trên mọi đường đi từ $$s$$ đến $$v$$. Nếu không có đường đi, $$\text{dist}(s,v) = \infty$$.
</div>

| Loại đồ thị | Thuật toán | Độ phức tạp |
|:---|:---|:---|
| Không trọng số (hoặc bằng 1) | **BFS** | $$O(V+E)$$ |
| Trọng số không âm | **Dijkstra** | $$O((V+E)\log V)$$ |
| Có trọng số âm | **Bellman-Ford** | $$O(VE)$$ |

**Khác MST** (Ch.16): Shortest path tối ưu **một** đường giữa hai đỉnh; MST tối ưu **tập cạnh** nối mọi đỉnh thành cây.

## Thuật toán Dijkstra

**Ý tưởng greedy**: Luôn **chốt** đỉnh chưa xử lý có `dist` nhỏ nhất; **relax** các cạnh kề.

```
DIJKSTRA(G, w, s):
    dist[v] ← ∞ cho mọi v; dist[s] ← 0
    Q ← priority queue chứa mọi v, key = dist[v]
    while Q không rỗng:
        u ← EXTRACT-MIN(Q)
        for mỗi cạnh (u,v) với trọng số w(u,v):
            if dist[u] + w(u,v) < dist[v]:
                dist[v] ← dist[u] + w(u,v)
                parent[v] ← u
```

<div class="textbook-theorem" markdown="1">
**Định lý**: Với trọng số **không âm**, sau khi `u` được extract-min, $$\text{dist}[u]$$ là khoảng cách ngắn nhất thực sự từ $$s$$ đến $$u$$.
</div>

**Độ phức tạp**: Với binary heap: $$O((V+E)\log V)$$. Với Fibonacci heap: $$O(E + V \log V)$$ (lý thuyết).

<div class="interactive-demo" markdown="1">
<div data-demo="dijkstra-visualizer"></div>
</div>
<script src="{{ '/public/js/dijkstra-visualizer.js' | relative_url }}"></script>

## Bellman-Ford và trọng số âm

<div class="textbook-definition" markdown="1">
**Định lý**: Nếu đồ thị có **chu trình âm** (tổng trọng số < 0), khoảng cách ngắn nhất **không xác định** (có thể giảm vô hạn). **Bellman-Ford** relax mọi cạnh $$V-1$$ lần; lần thứ $$V$$ phát hiện chu trình âm.
</div>

**Edge case**: Dijkstra **sai** khi có cạnh âm — đỉnh chốt sớm có thể chưa tối ưu. Đồ thị **không liên thông**: một số cặp đỉnh có dist = ∞.

## Ứng dụng

- **Routing** (OSPF, một số mô hình): tìm đường ít chi phí.
- **Game AI**: pathfinding trên lưới có trọng số (A* là mở rộng heuristic của Dijkstra).
- **Social network**: khoảng cách theo trọng số quan hệ (không phải số hop BFS).

## Bài tập

### Bài tập 1

Đồ thị 4 đỉnh: cạnh (A,B,1), (A,C,4), (B,C,2), (B,D,6), (C,D,1). Chạy Dijkstra từ A. dist đến D?

<details>
<summary>Đáp án</summary>

dist[A]=0, dist[B]=1, dist[C]=3 (qua B), dist[D]=4 (A→B→C→D: 1+2+1=4).

</details>

### Bài tập 2

Vì sao BFS không đúng khi cạnh có trọng số 1 và 10?

<details>
<summary>Đáp án</summary>

BFS tối ưu **số cạnh**, không tổng trọng số. Đường 2 cạnh tổng 20 có thể tệ hơn đường 1 cạnh trọng số 5.

</details>

### Bài tập 3

Cho cạnh (A,B,-1). Dijkstra từ A có đáng tin không? Thuật toán nào dùng?

<details>
<summary>Đáp án</summary>

Không — trọng số âm. Dùng **Bellman-Ford**; nếu phát hiện chu trình âm thì báo lỗi.

</details>

## Tóm tắt

- **BFS**: ít cạnh nhất, không trọng số — $$O(V+E)$$.
- **Dijkstra**: trọng số không âm, greedy + heap — $$O((V+E)\log V)$$.
- **Bellman-Ford**: trọng số âm, phát hiện chu trình âm.

Bài tiếp theo: **sắp xếp topo** trên DAG — ứng dụng DFS/BFS cho lịch task và pipeline build.