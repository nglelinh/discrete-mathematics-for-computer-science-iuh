---
layout: post
title: "Euler, Hamilton và Duyệt Đồ thị"
categories: chapter12
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: 'Mục 12.4 phân biệt đường Euler và chu trình Hamilton, nêu điều kiện tồn tại chu trình Euler, và giới thiệu BFS/DFS — nền tảng duyệt đồ thị trong thuật toán.'
---

Bài toán **7 cầu Königsberg** (Euler, 1736) mở ra lý thuyết đồ thị hiện đại: có thể đi qua mỗi cầu đúng một lần không? Câu hỏi tương tự xuất hiện trong kiểm tra mạch in một nét, routing và lập lịch. Mục 12.4 phân biệt **Euler** (cạnh) và **Hamilton** (đỉnh), rồi giới thiệu **BFS** và **DFS**.

![Leonhard Euler](/discrete-mathematics-for-computer-science-iuh/img/course/Leonhard_Euler.jpg)

<p class="textbook-figure-caption" data-figure="12.9">Leonhard Euler (1707–1783) — bài toán 7 cầu Königsberg là khởi đầu lý thuyết đồ thị.</p>
![Merge sort — tư duy duyệt có cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

<p class="textbook-figure-caption" data-figure="12.10">Duyệt đồ thị có cấu trúc (BFS/DFS) — tương tự chia để trị trong thuật toán.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** đường/chu trình Euler và Hamilton.
- **Áp dụng** điều kiện bậc chẵn cho chu trình Euler.
- **Mô tả** thuật toán BFS và DFS, độ phức tạp $$O(V+E)$$.
- **Giải thích** vì sao Hamilton (tìm optimal) là NP-hard nhưng Euler có thuật toán đa thức.

**Từ khóa**: Euler path/cycle, Hamilton path/cycle, BFS, DFS, Hierholzer, NP-hard.
</div>

## Đường đi và chu trình Euler

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **Đường Euler**: Đi qua **mỗi cạnh đúng một lần**.
- **Chu trình Euler**: Đường Euler đóng (quay về đỉnh xuất phát).
</div>

<div class="textbook-theorem" markdown="1">
**Định lý** (Euler): Đồ thị vô hướng **liên thông** có:

- **Chu trình Euler** ⟺ mọi đỉnh có bậc **chẵn**.
- **Đường Euler** (không đóng) ⟺ liên thông và **đúng 2** đỉnh bậc **lẻ** (điểm đầu và cuối).
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (Königsberg): 4 vùng đất, 7 cầu — mô hình đồ thị có 4 đỉnh bậc lẻ → **không** có đường Euler. Đây là câu trả lời âm của Euler năm 1736.
</div>

## Chu trình Hamilton

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **Đường Hamilton**: Đi qua **mỗi đỉnh đúng một lần**.
- **Chu trình Hamilton**: Đường Hamilton đóng.
</div>

**TSP** (Traveling Salesman Problem) là biến thể tối ưu hóa chu trình Hamilton — **NP-hard** (Ch.20). Không có điều kiện bậc đơn giản như Euler.

| | Euler | Hamilton |
|:---|:---|:---|
| Đối tượng duyệt | Cạnh | Đỉnh |
| Điều kiện cổ điển | Bậc chẵn | Không có kết quả đơn giản |
| Độ khó | Đa thức (Hierholzer) | NP-hard (tìm optimal) |

## BFS và DFS

**BFS** (Breadth-First Search): Duyệt theo **tầng** — dùng hàng đợi (queue). Tìm đường đi **ngắn nhất** (số cạnh) trên đồ thị không trọng số.

**DFS** (Depth-First Search): Đi **sâu** trước — dùng ngăn xếp (stack) hoặc đệ quy. Phát hiện chu trình, topological sort trên DAG.

<div class="textbook-theorem" markdown="1">
**Độ phức tạp**: Với danh sách kề, cả BFS và DFS chạy trong **$$O(V + E)$$** thời gian và **$$O(V)$$** bộ nhớ phụ (visited + queue/stack).
</div>

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order
```

<div class="textbook-example" markdown="1">
**Ví dụ** (ứng dụng): BFS từ node gốc trong CDN — tìm hop tối thiểu. DFS trên dependency graph — phát hiện cycle trước khi build.
</div>

## Bài tập

### Bài tập 1

Đồ thị vô hướng liên thông, bậc các đỉnh: 2, 2, 4, 4. Có chu trình Euler không?

<details>
<summary>Đáp án</summary>

Tất cả bậc chẵn → **có** chu trình Euler.

</details>

### Bài tập 2

Bậc: 3, 3, 2, 2. Có đường Euler? Có chu trình Euler?

<details>
<summary>Đáp án</summary>

Đúng 2 đỉnh bậc lẻ → **có đường** Euler, **không có** chu trình Euler.

</details>

### Bài tập 3

Vì sao BFS cho đường đi ngắn nhất (theo số cạnh) trên đồ thị không trọng số?

<details>
<summary>Đáp án</summary>

BFS mở rộng theo tầng 0, 1, 2, … — lần đầu gặp đỉnh $$v$$ là qua ít cạnh nhất.

</details>

### Bài tập 4

Phân loại: tìm chu trình Euler vs tìm chu trình Hamilton tối thiểu (TSP). Thuộc P hay NP-hard?

<details>
<summary>Đáp án</summary>

Euler: **P** (Hierholzer $$O(E)$$). TSP optimal: **NP-hard**.

</details>

## Tóm tắt

- **Euler**: duyệt cạnh; điều kiện bậc chẵn; giải được đa thức.
- **Hamilton / TSP**: duyệt đỉnh; NP-hard; dùng heuristic trong thực tế.
- **BFS**: tầng, đường ngắn nhất không trọng số, $$O(V+E)$$.
- **DFS**: sâu, cycle detection, topological sort.

Chúng ta đã hoàn thành phần **đồ thị cơ bản** của chương 12. Chương 16 (Cây) và Chương 17 (Đồ thị nâng cao) sẽ mở rộng sang cây khung, MST và thuật toán nâng cao hơn.