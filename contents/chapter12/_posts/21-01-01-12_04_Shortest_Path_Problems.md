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

Khi dùng bản đồ số, tối ưu route giao hàng, tìm đường truyền dữ liệu ít trễ nhất, hay chọn chuỗi phụ thuộc có chi phí thấp nhất, ta đang hỏi cùng một câu: từ điểm xuất phát đến đích, đâu là con đường tốt nhất theo một tiêu chí nào đó?


Đồ thị là mô hình chuẩn cho mạng, phụ thuộc và đường đi, nên mỗi khái niệm ở đây đều có thể nối trực tiếp sang bài toán thực tế trong phần mềm.
Trong lý thuyết đồ thị, đó là **bài toán đường đi ngắn nhất**. "Ngắn nhất" có thể là ít cạnh nhất, tổng trọng số nhỏ nhất, thời gian nhỏ nhất, hay chi phí thấp nhất. Chỉ cần mô hình đúng, rất nhiều tình huống thực tế đều rơi vào khuôn mẫu này.

Đây là một chủ đề cực kỳ quan trọng trong khoa học máy tính vì nó đứng sau định tuyến mạng, navigation, tối ưu logistics và nhiều bài toán AI cổ điển. Đồng thời, nó cũng cho thấy cách một mô hình toán học trừu tượng có thể đi thẳng vào ứng dụng.

Trong bài này, chúng ta sẽ học cách phát biểu bài toán, phân biệt các trường hợp thường gặp và chuẩn bị nền cho các thuật toán giải tương ứng.

## 1. Phát biểu bài toán

Trước khi giải, ta cần phát biểu bài toán thật chính xác. Chỉ cần sai mô hình hoặc sai giả thiết, toàn bộ lời giải phía sau sẽ lệch hướng.

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

Ở phần này, đừng chỉ nhớ các bước. Hãy chú ý điều kiện áp dụng, thông tin được duy trì sau mỗi bước và lý do thuật toán cho kết quả đúng.

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
<div data-demo="dijkstra-visualizer"></div>
</div>
<script src="{{ '/public/js/dijkstra-visualizer.js' | relative_url }}"></script>

## 8. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- BFS chỉ cho đường đi ngắn nhất khi mọi cạnh có trọng số bằng nhau.
- Dijkstra không xử lý cạnh âm.
- Bellman-Ford không “sửa” chu trình âm; nó phát hiện rằng bài toán không có nghiệm hữu hạn.
- Đường đi ngắn nhất không nhất thiết là đường có ít cạnh nhất.
</div>

## 9. Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

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
