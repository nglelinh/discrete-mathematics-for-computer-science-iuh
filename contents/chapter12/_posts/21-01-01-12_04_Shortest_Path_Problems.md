---
layout: post
title: "Bài toán Đường đi Ngắn nhất"
categories: chapter12
date: 2021-01-01
order: 4
required: true
lang: vi
---

# Bài toán Đường đi Ngắn nhất

Trong bản đồ số, mạng máy tính hay hệ thống giao hàng, câu hỏi “có đường đi không?” chỉ là bước khởi động. Câu hỏi thật sự có giá trị là: đi **đường nào ngắn nhất**, rẻ nhất hoặc nhanh nhất? Khi dữ liệu có hàng triệu đỉnh và cạnh, chọn sai đường không chỉ lãng phí vài phút mà có thể kéo theo chi phí vận hành khổng lồ.

Bài toán **đường đi ngắn nhất** vì thế là một trong những bài toán cốt lõi nhất của khoa học máy tính ứng dụng. Nó nối lý thuyết đồ thị với thuật toán, tối ưu và thiết kế hệ thống. Học phần này là học cách biến một mạng liên kết phức tạp thành quyết định tốt nhất theo tiêu chí rõ ràng.

## 1. Phát biểu bài toán

Cho đồ thị có trọng số $G=(V,E,w)$, trong đó $w(e)$ là trọng số của cạnh $e$. Với đỉnh nguồn $s$, cần tìm khoảng cách ngắn nhất

$$
d(s,v)=\min\{\text{tổng trọng số của đường đi từ }s\text{ đến }v\}
$$

cho mọi $v\in V$.

Nếu đồ thị không trọng số, ta xem mỗi cạnh có trọng số 1 và dùng BFS để tìm đường đi ít cạnh nhất.

## 2. Relaxation

**Relaxation** là thao tác cốt lõi của hầu hết thuật toán đường đi ngắn nhất. Với cạnh $(u,v)$, nếu ta đã biết đường từ $s$ đến $u$, thì đường từ $s$ đến $v$ qua $u$ có độ dài $dist[u]+w(u,v)$.

Nếu

$$
dist[u]+w(u,v)<dist[v],
$$

thì cập nhật

$$
dist[v]=dist[u]+w(u,v).
$$

## 3. Thuật toán Dijkstra

**Điều kiện**: Mọi trọng số cạnh không âm.

**Ý tưởng**: Mỗi bước chọn đỉnh chưa xử lý có khoảng cách tạm thời nhỏ nhất. Vì trọng số không âm, một khi đỉnh được chọn, khoảng cách của nó là tối ưu.

```text
Dijkstra(G, s):
    dist[s] = 0
    dist[v] = ∞ với mọi v ≠ s
    Q = hàng đợi ưu tiên chứa các đỉnh
    while Q không rỗng:
        u = extract_min(Q)
        for mỗi cạnh (u, v):
            relax(u, v)
```

**Độ phức tạp**: $O((V+E)\log V)$ với heap nhị phân.

## 4. Vì sao Dijkstra không dùng cho cạnh âm?

Dijkstra dựa vào giả định rằng khi một đỉnh có khoảng cách tạm thời nhỏ nhất được chọn, không có đường nào sau này làm nó ngắn hơn. Cạnh âm phá vỡ giả định này: một đường đi qua đỉnh chưa xử lý có thể quay lại làm giảm khoảng cách đã “chốt”.

<div class="content-box warning-box" markdown="1">
**Cảnh báo**: Không dùng Dijkstra nếu đồ thị có cạnh âm. Nếu có cạnh âm nhưng không có chu trình âm, dùng Bellman-Ford.
</div>

## 5. Bellman-Ford

Bellman-Ford lặp relaxation trên tất cả cạnh $|V|-1$ lần. Lý do: mọi đường đi đơn ngắn nhất có nhiều nhất $|V|-1$ cạnh.

```text
BellmanFord(G, s):
    dist[s] = 0
    dist[v] = ∞ với mọi v ≠ s
    repeat |V|-1 lần:
        for mỗi cạnh (u, v):
            relax(u, v)
    kiểm tra chu trình âm
```

**Độ phức tạp**: $O(VE)$.

**Ưu điểm**: Xử lý cạnh âm và phát hiện chu trình âm.

## 6. Chu trình âm

Nếu tồn tại chu trình có tổng trọng số âm và có thể đi tới từ nguồn, thì không tồn tại đường đi ngắn nhất hữu hạn: ta có thể đi quanh chu trình đó nhiều lần để giảm chi phí vô hạn.

## 7. Floyd-Warshall

Nếu cần đường đi ngắn nhất giữa mọi cặp đỉnh, Floyd-Warshall là một thuật toán quy hoạch động với độ phức tạp $O(V^3)$.

Ý tưởng:

$$
d_{ij}^{(k)}=\min(d_{ij}^{(k-1)}, d_{ik}^{(k-1)}+d_{kj}^{(k-1)}).
$$

Nghĩa là đường từ $i$ đến $j$ có thể không đi qua $k$, hoặc đi qua $k$.

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học chọn từng bước của Dijkstra; công cụ tô màu đỉnh đã chốt, cạnh được relaxation và bảng `dist` hiện tại.
</div>

## 8. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- BFS chỉ cho đường đi ngắn nhất khi mọi cạnh có trọng số bằng nhau.
- Dijkstra không xử lý cạnh âm.
- Bellman-Ford không “sửa” chu trình âm; nó phát hiện rằng bài toán không có nghiệm hữu hạn.
- Đường đi ngắn nhất không nhất thiết là đường có ít cạnh nhất.
</div>

## 9. Ứng dụng trong Khoa học Máy tính

Đường đi ngắn nhất xuất hiện trong định tuyến Internet, hệ thống bản đồ, logistics, robot, game pathfinding, phân tích phụ thuộc phần mềm và tối ưu chi phí trong mạng. Trong AI game, A* mở rộng Dijkstra bằng heuristic để tìm đường nhanh hơn khi có thông tin hình học.

```python
import heapq

def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

## Bài tập thực hành

### Bài tập 1

Vì sao BFS tìm đường ngắn nhất trong đồ thị không trọng số?

<details>
<summary>Đáp án</summary>

BFS thăm các đỉnh theo từng lớp khoảng cách: trước hết khoảng cách 0, rồi 1, rồi 2, v.v. Khi một đỉnh được thăm lần đầu, đó là bằng số cạnh ít nhất từ nguồn.

</details>

### Bài tập 2

Dijkstra có áp dụng được cho đồ thị có cạnh trọng số 0 không?

<details>
<summary>Đáp án</summary>

Có. Điều kiện của Dijkstra là trọng số không âm, nên cạnh trọng số 0 được phép.

</details>

### Bài tập 3

Nếu Bellman-Ford vẫn relaxation được sau $|V|-1$ vòng, điều đó nghĩa là gì?

<details>
<summary>Đáp án</summary>

Có chu trình âm có thể đi tới từ nguồn.

</details>

## Tóm tắt

- Đường đi ngắn nhất tối thiểu hóa tổng trọng số cạnh.
- Relaxation là thao tác cập nhật khoảng cách trung tâm.
- BFS dùng cho đồ thị không trọng số; Dijkstra dùng cho trọng số không âm.
- Bellman-Ford xử lý cạnh âm và phát hiện chu trình âm.
- Ứng dụng trải rộng từ bản đồ số, định tuyến mạng đến game AI và logistics.
