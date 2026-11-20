---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Đồ thị — Đường đi, Euler, Hamilton

**Toán Rời Rạc**

Tiết 37 (45 phút) — Paths & Graph Traversal

---

## Mục tiêu tiết học

- Phân biệt đường đi Euler và chu trình Hamilton
- Áp dụng điều kiện tồn tại chu trình/đường Euler
- Hiểu BFS và DFS — ý tưởng và độ phức tạp
- Ứng dụng duyệt đồ thị trong routing và scheduling
- Mô hình hóa bài toán thực tế bằng đồ thị

---

## Ôn — Đường đi và Chu trình

**Walk**: Dãy đỉnh-cạnh (có thể lặp).

**Trail**: Walk không lặp **cạnh**.

**Path**: Trail không lặp **đỉnh**.

**Cycle**: Path đóng ($$v_0 = v_k$$).

**Độ dài**: Số cạnh trên đường đi.

---

## Đường đi Euler

**Đường Euler**: Đi qua **mỗi cạnh đúng một lần**.

**Chu trình Euler**: Đường Euler đóng (quay về đỉnh xuất phát).

**Ví dụ cổ điển**: Bài toán 7 cầu Königsberg (Euler, 1736) — sơ khai lý thuyết đồ thị.

**Ứng dụng**: Kiểm tra mạch, vẽ một nét, routing trùng cạnh.

---

## Định lý — Chu trình Euler

**Đồ thị vô hướng liên thông** có chu trình Euler **iff** mọi đỉnh có bậc **chẵn**.

**Đường Euler** (không đóng): Liên thông và **đúng 2** đỉnh bậc lẻ.

**Chứng minh ý tưởng**:
- Cần: Mỗi lần vào/ra đỉnh tiêu thụ 2 bậc → bậc chẵn
- Đủ: Xây dựng bằng Hierholzer's algorithm

---

## Ví dụ Euler

Đồ thị: 4 đỉnh, bậc (2, 2, 2, 2) — tất cả chẵn → **có** chu trình Euler.

Đồ thị: bậc (3, 3, 2, 2) — hai đỉnh bậc lẻ → **có đường** Euler, **không có** chu trình.

**Königsberg**: 4 đỉnh, bậc (3, 3, 3, 5) — 4 đỉnh bậc lẻ → **không** có đường Euler.

---

## Chu trình Hamilton

**Chu trình Hamilton**: Đi qua **mỗi đỉnh đúng một lần** rồi quay về.

**Đường Hamilton**: Đi qua mỗi đỉnh đúng một lần (không đóng).

**Ví dụ**: Người đưa thư (Traveling Salesman) — tìm tour ngắn nhất qua mọi thành phố.

**Khác Euler**: Euler = cạnh; Hamilton = **đỉnh**.

---

## Hamilton vs Euler — So sánh

| | Euler | Hamilton |
|:---|:---|:---|
| Đối tượng | Mỗi **cạnh** 1 lần | Mỗi **đỉnh** 1 lần |
| Điều kiện | Bậc chẵn (dễ kiểm tra) | **Không** có điều kiện đơn giản |
| Độ khó | $$O(E)$$ — thuật toán | **NP-hard** (tổng quát) |
| Ứng dụng | Vẽ một nét, kiểm tra mạch | TSP, lập lịch, DNA sequencing |

---

## BFS — Breadth-First Search

**Ý tưởng**: Duyệt theo **tầng** — queue (FIFO).

**Ứng dụng**:
- Đường đi **ngắn nhất** (không trọng số)
- Kiểm tra liên thông
- Tìm đỉnh gần nhất

**Độ phức tạp**: $$O(V + E)$$ với danh sách kề.

---

## DFS — Depth-First Search

**Ý tưởng**: Đi **sâu** trước — stack hoặc đệ quy.

**Ứng dụng**:
- Phát hiện **chu trình**
- **Sắp xếp topo** (DAG)
- Thành phần liên thông
- Maze solving

**Độ phức tạp**: $$O(V + E)$$.

---

## BFS vs DFS

| | BFS | DFS |
|:---|:---|:---|
| Cấu trúc | Queue | Stack / đệ quy |
| Đường ngắn nhất | **Có** (không trọng số) | Không đảm bảo |
| Bộ nhớ | $$O(V)$$ — rộng hơn | $$O(V)$$ — sâu hơn |
| Topo sort | Không | **Có** |
| Chu trình | Phát hiện được | Phát hiện được |

---

## Code — BFS và DFS

```python
from collections import deque

def bfs(graph, start):
    visited, queue = {start}, deque([start])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for u in graph[start]:
        if u not in visited:
            dfs(graph, u, visited)
    return visited
```

---

## Sắp xếp Topo (Topological Sort)

**DAG** (Directed Acyclic Graph): Đồ thị có hướng **không chu trình**.

**Topo sort**: Thứ tự đỉnh sao cho mọi cạnh $$(u,v)$$: $$u$$ đứng trước $$v$$.

**Ứng dụng**:
- Lịch trình task phụ thuộc (build system, Makefile)
- Thứ tự học môn học
- Pipeline compiler

**Thuật toán**: DFS hoặc BFS (Kahn) — $$O(V+E)$$.

---

## Ứng dụng trong CNTT

- **Routing**: BFS/Dijkstra tìm đường ngắn nhất mạng
- **Social network**: BFS tìm "6 degrees of separation"
- **Web crawling**: DFS/BFS duyệt trang
- **Deadlock detection**: Chu trình trong đồ thị chờ
- **GPS / Maps**: Hamilton/TSP (xấp xỉ heuristic)

---

## Đường ngắn nhất — Giới thiệu

**Không trọng số**: BFS → đường ít cạnh nhất.

**Có trọng số không âm**: **Dijkstra** — $$O((V+E)\log V)$$ với heap.

**Có trọng số âm**: **Bellman-Ford** — phát hiện chu trình âm.

**Edge case**: Đồ thị không liên thông → không có đường giữa một số cặp.

---

## Thực hành 1

Đồ thị vô hướng: đỉnh A–E, cạnh (A,B), (B,C), (C,D), (D,E), (E,A), (A,C).

1. Có chu trình Euler không? (tính bậc)
2. Có chu trình Hamilton không? (thử vẽ)

---

## Thực hành 2

Cho DAG task: A→B, A→C, B→D, C→D.

1. Vẽ đồ thị
2. Tìm một topo sort hợp lệ
3. BFS từ A — thứ tự duyệt?

---

## Tóm tắt Tiết 37

- **Euler**: mỗi cạnh 1 lần — điều kiện bậc chẵn
- **Hamilton**: mỗi đỉnh 1 lần — NP-hard tổng quát
- **BFS**: tầng, đường ngắn nhất, $$O(V+E)$$
- **DFS**: sâu, topo sort, phát hiện chu trình
- Đồ thị là **mô hình** cho routing, scheduling, web

---

## Liên hệ

**Định lý chính**: Điều kiện Euler (bậc chẵn) — chứng minh đủ bằng Hierholzer.

**Edge case**: Đồ thị không liên thông; DAG vs có chu trình; trọng số âm.

**Liên hệ**: Đồ thị (tiết 36) ↔ Thuật toán Big-O (tiết 38) ↔ Cây (tiết 44).

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Phân biệt đường Euler và chu trình Hamilton.

2. **Euler**: Đồ thị 5 đỉnh, bậc (2,2,2,3,3). Có đường Euler không?

3. **BFS/DFS**: Nêu ứng dụng chính của mỗi thuật toán.

---

## Bài tập ôn tập (2/2)

4. **Topo sort**: Cho DAG 4 task: P→Q, P→R, Q→S, R→S. Liệt kê mọi topo sort.

5. **Bài 5**: Chứng minh: nếu đồ thị vô hướng liên thông có đúng 2 đỉnh bậc lẻ thì có đường Euler (không đóng). Gợi ý: đỉnh bậc lẻ là điểm bắt đầu/kết thúc.
