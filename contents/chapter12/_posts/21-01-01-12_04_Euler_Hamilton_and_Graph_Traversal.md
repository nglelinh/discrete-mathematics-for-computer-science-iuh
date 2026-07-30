---
layout: post
title: "Euler, Hamilton và Duyệt Đồ thị"
categories: chapter12
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Đường/chu trình Euler và điều kiện bậc; đường/chu trình Hamilton; BFS và DFS với độ phức tạp O(V+E); phân biệt bài toán P và NP-hard."
---

<div class="textbook-epigraph" markdown="1">

"The Königsberg bridge problem is an example of a problem that could be solved only by means of graph theory."

<span class="epigraph-attribution">— Leonhard Euler</span>

</div>

Năm 1736, Euler trả lời câu hỏi thực tế: tại Königsberg, có thể đi qua mỗi cây cầu đúng một lần rồi về điểm xuất phát không? Câu trả lời phụ thuộc **bậc** các đỉnh trên mô hình đồ thị — không phụ thuộc cách vẽ bản đồ. Cùng tinh thần “đi hết” nhưng đổi đối tượng từ cạnh sang đỉnh dẫn tới **chu trình Hamilton** và bài toán người du lịch (TSP), vốn khó về mặt tính toán. Cuối mục, **BFS** và **DFS** là hai khuôn mẫu duyệt mọi đỉnh/cạnh đạt được trong thời gian tuyến tính theo kích thước biểu diễn.

![Leonhard Euler](/discrete-mathematics-for-computer-science-iuh/img/course/Leonhard_Euler.jpg)

<p class="textbook-figure-caption" data-figure="12.8">Leonhard Euler (1707–1783) — bài toán 7 cầu Königsberg mở đầu lý thuyết đồ thị.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** đường/chu trình Euler và đường/chu trình Hamilton.
- **Áp dụng** điều kiện bậc cho sự tồn tại đường và chu trình Euler.
- **Mô tả** BFS và DFS, nêu độ phức tạp $$O(V+E)$$ trên danh sách kề.
- **Giải thích** vì sao Euler thuộc lớp bài toán đa thức trong khi tối ưu Hamilton/TSP là NP-hard.

**Từ khóa**: Euler path/cycle, Hamilton path/cycle, BFS, DFS, Hierholzer, NP-hard.

</div>

## 1. Đường đi và chu trình Euler

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **Đường Euler** (*Eulerian path*): trail đi qua **mỗi cạnh** của $$G$$ **đúng một lần**.
- **Chu trình Euler** (*Eulerian circuit*): đường Euler đóng — bắt đầu và kết thúc cùng một đỉnh.

</div>

Đối tượng được “phủ” là **cạnh**. Đỉnh có thể (và thường phải) được thăm nhiều lần.

<div class="textbook-theorem" markdown="1">

**Định lý** (Euler, dạng vô hướng). Cho $$G$$ vô hướng. Giả sử mọi cạnh nằm trong một thành phần liên thông (các đỉnh cô lập có thể bỏ qua). Khi đó:

- $$G$$ có **chu trình Euler** khi và chỉ khi mọi đỉnh có bậc **chẵn**;
- $$G$$ có **đường Euler** (không nhất thiết đóng) khi và chỉ khi số đỉnh bậc **lẻ** bằng **0** hoặc **2**.

  - 0 đỉnh bậc lẻ: đường Euler đóng (tức chu trình Euler);
  - đúng 2 đỉnh bậc lẻ: đường Euler mở, bắt đầu tại một đỉnh bậc lẻ và kết thúc tại đỉnh bậc lẻ còn lại.

</div>

*Ý tưởng.* Mỗi lần trail đi vào rồi ra khỏi một đỉnh “giữa đường” dùng hai “nửa” bậc. Ở đỉnh xuất phát/kết thúc của đường mở, còn dư đúng một hướng. Thuật toán **Hierholzer** xây chu trình Euler trong thời gian $$O(|E|)$$ khi điều kiện thỏa: luôn nối các chu trình con dọc theo cạnh chưa dùng.

![Mô hình 7 cầu Königsberg](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_konigsberg_euler.svg)

<p class="textbook-figure-caption" data-figure="12.9">Bốn vùng đất và bảy cầu: mô hình đa đồ thị với bốn đỉnh bậc lẻ — không có đường Euler.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1** (Königsberg). Bốn đỉnh với bậc lẻ (thực tế cả bốn đều lẻ). Số đỉnh bậc lẻ $$= 4 \neq 0,2$$. Theo định lý, **không** tồn tại đường Euler — không thể đi qua mỗi cầu đúng một lần, bất kể điểm xuất phát.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Đồ thị liên thông với dãy bậc $$2,2,4,4$$: mọi bậc chẵn $$\implies$$ có **chu trình Euler**.

Dãy $$3,3,2,2$$: đúng hai đỉnh bậc lẻ $$\implies$$ có **đường Euler** mở, **không** có chu trình Euler.

</div>

## 2. Đường đi và chu trình Hamilton

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **Đường Hamilton**: path đi qua **mỗi đỉnh** đúng một lần.
- **Chu trình Hamilton**: cycle đi qua mọi đỉnh đúng một lần rồi trở về đỉnh xuất phát.

</div>

Đối tượng phủ là **đỉnh**. Không yêu cầu dùng hết cạnh.

![Euler so với Hamilton](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_euler_vs_hamilton.svg)

<p class="textbook-figure-caption" data-figure="12.10">Trái: chu trình Euler nhấn mạnh phủ cạnh. Phải: chu trình Hamilton nhấn mạnh phủ đỉnh.</p>

| | Euler | Hamilton |
|:---|:---|:---|
| Đối tượng | Cạnh | Đỉnh |
| Điều kiện cổ điển | Bậc chẵn / đúng 0 hoặc 2 bậc lẻ | Không có điều kiện bậc đơn giản tương đương |
| Thuật toán | Hierholzer $$O(E)$$ | Không có thuật toán đa thức tổng quát cho quyết định/tối ưu |
| Biến thể tối ưu | Ít gặp trong giáo trình cơ sở | TSP — tìm chu trình Hamilton trọng số nhỏ nhất |

**TSP** (*Traveling Salesman Problem*): trên đồ thị đầy đủ có trọng số, tìm chu trình Hamilton có tổng trọng số nhỏ nhất. Bài toán tối ưu này (và nhiều biến thể quyết định liên quan) là **NP-hard** — xem thêm Chương 20. Trong thực tế người ta dùng heuristic và xấp xỉ; điều đó **không** mâu thuẫn với việc chu trình Euler vẫn giải được nhanh.

## 3. BFS — duyệt theo bề rộng

**BFS** (*Breadth-First Search*) mở rộng đồ thị theo **tầng** khoảng cách từ đỉnh nguồn $$s$$. Cấu trúc hỗ trợ là **hàng đợi** (*queue*).

![BFS theo tầng](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_bfs_layers.svg)

<p class="textbook-figure-caption" data-figure="12.11">BFS từ $$s$$: tầng $$k$$ gồm các đỉnh có đường ngắn nhất (theo số cạnh) độ dài $$k$$.</p>

**Tính chất quan trọng.** Trên đồ thị **không trọng số** (mọi cạnh độ dài 1), lần đầu BFS thăm đỉnh $$v$$ chính là thời điểm phát hiện đường đi từ $$s$$ tới $$v$$ với **số cạnh tối thiểu**.

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    dist = {start: 0}
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                dist[v] = dist[u] + 1
                queue.append(v)
    return order, dist
```

## 4. DFS — duyệt theo chiều sâu

**DFS** (*Depth-First Search*) luôn cố gắng đi tiếp theo một cạnh tới đỉnh chưa thăm trước khi quay lui. Cấu trúc hỗ trợ là **ngăn xếp** (*stack*) tường minh hoặc stack gọi hàm khi viết đệ quy.

![Thứ tự DFS](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_dfs_order.svg)

<p class="textbook-figure-caption" data-figure="12.12">DFS ưu tiên nhánh sâu; cạnh ngược trên rừng DFS dùng để phát hiện chu trình.</p>

Ứng dụng điển hình:

- phát hiện chu trình (vô hướng và có hướng);
- **topological sort** trên DAG;
- tính thành phần liên thông (và biến thể SCC trên digraph);
- sinh không gian trạng thái trong backtracking.

```python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for v in graph.get(start, []):
        if v not in visited:
            dfs(graph, v, visited, order)
    return order
```

## 5. Độ phức tạp chung

<div class="textbook-theorem" markdown="1">

**Định lý** (chi phí duyệt). Với biểu diễn **danh sách kề**, cả BFS và DFS chạy trong thời gian $$O(|V| + |E|)$$ và dùng bộ nhớ phụ $$O(|V|)$$ cho tập đã thăm cùng hàng đợi hoặc ngăn xếp.

</div>

*Lý do.* Mỗi đỉnh vào hàng đợi/stack tối đa một lần; mỗi danh sách kề được quét đúng một lần khi đỉnh chủ được xử lý — tổng độ dài các danh sách là $$\Theta(|E|)$$ (hoặc $$2|E|$$ vô hướng, cùng bậc lớn).

Trên **ma trận kề**, cùng logic duyệt láng giềng mất $$O(|V|)$$ mỗi đỉnh, dẫn tới $$O(|V|^2)$$ — kém hơn rõ khi đồ thị thưa.

| Thuật toán | Cấu trúc | Khoảng cách / ứng dụng chính |
|:---|:---|:---|
| BFS | Queue | Đường ngắn nhất theo số cạnh; tầng; kiểm tra hai phía |
| DFS | Stack / đệ quy | Chu trình; topo sort; SCC; backtracking |

<div class="textbook-example" markdown="1">

**Ví dụ 3** (ứng dụng).

- BFS từ máy chủ gốc trong mạng hop-count: số tầng = số bước chuyển tối thiểu.
- DFS trên dependency graph: nếu gặp cạnh ngược tới đỉnh đang nằm trên stack đệ quy thì tồn tại chu trình — báo circular dependency trước khi build.

</div>

## 6. Thử nghiệm tương tác

### 6.1. Euler và Hamilton

Bật/tắt cạnh, kiểm tra điều kiện bậc cho chu trình Euler và tìm một chu trình Hamilton (nếu có) trên đồ thị nhỏ.

<div class="interactive-demo" markdown="1">
<div data-demo="euler-hamilton-checker"></div>
</div>
<script src="{{ '/public/js/euler-hamilton-checker.js' | relative_url }}"></script>

### 6.2. BFS / DFS từng bước

Chạy BFS hoặc DFS từng bước: theo dõi hàng đợi / ngăn xếp, thứ tự thăm và khoảng cách $$d$$ (số cạnh từ nguồn trong BFS).

<div class="interactive-demo" markdown="1">
<div data-demo="bfs-dfs-visualizer"></div>
</div>
<script src="{{ '/public/js/bfs-dfs-visualizer.js' | relative_url }}"></script>


## Bài tập

### Bài tập 1

Đồ thị vô hướng liên thông, bậc các đỉnh: $$2, 2, 4, 4$$. Có chu trình Euler không?

<details>
<summary>Đáp án</summary>

Mọi bậc chẵn và đồ thị liên thông $$\implies$$ **có** chu trình Euler.

</details>

### Bài tập 2

Bậc: $$3, 3, 2, 2$$. Có đường Euler? Có chu trình Euler?

<details>
<summary>Đáp án</summary>

Đúng hai đỉnh bậc lẻ $$\implies$$ **có đường Euler** mở, **không** có chu trình Euler.

</details>

### Bài tập 3

Vì sao BFS cho đường đi ngắn nhất theo số cạnh trên đồ thị không trọng số?

<details>
<summary>Đáp án</summary>

BFS xử lý đỉnh theo thứ tự khoảng cách không giảm từ nguồn. Lần đầu gặp $$v$$, mọi đỉnh ở tầng nhỏ hơn đã được xét; không tồn tại path tới $$v$$ ngắn hơn tầng hiện tại.

</details>

### Bài tập 4

Phân loại độ khó: (a) tìm chu trình Euler; (b) tìm chu trình Hamilton có tổng trọng số nhỏ nhất (TSP). Thuộc P hay NP-hard (theo hiểu biết giáo trình)?

<details>
<summary>Đáp án</summary>

(a) Euler: giải được đa thức (Hierholzer) — thuộc **P**.  
(b) TSP tối ưu: **NP-hard**.

</details>

### Bài tập 5

Cho danh sách kề

```text
0: 1, 2
1: 0, 3
2: 0, 3
3: 1, 2
```

(a) Chạy BFS từ 0 — một thứ tự thăm hợp lệ và khoảng cách tới từng đỉnh.  
(b) Đồ thị có chu trình Euler không?

<details>
<summary>Đáp án</summary>

(a) Một BFS hợp lệ: thăm $$0$$, rồi $$1,2$$ (tầng 1), rồi $$3$$ (tầng 2).  
$$\mathrm{dist}(0)=0$$, $$\mathrm{dist}(1)=\mathrm{dist}(2)=1$$, $$\mathrm{dist}(3)=2$$.

(b) Bậc: $$\deg(0)=\deg(1)=\deg(2)=\deg(3)=2$$ — mọi bậc chẵn, liên thông $$\implies$$ **có** chu trình Euler (ví dụ đi quanh chu trình 4 đỉnh).

</details>

## Tóm tắt

1. **Euler** phủ **cạnh**: điều kiện bậc chẵn (chu trình) hoặc đúng 0/2 đỉnh bậc lẻ (đường); thuật toán đa thức.
2. **Hamilton** phủ **đỉnh**: không có tiêu chuẩn bậc đơn giản tương đương; tối ưu TSP là NP-hard.
3. **BFS** duyệt theo tầng — đường ngắn nhất không trọng số.
4. **DFS** duyệt sâu — chu trình, topo sort, SCC; cả hai đạt $$O(V+E)$$ trên danh sách kề.

Chương 12 dừng ở tầng đồ thị cơ bản. **Chương 16** (Cây) và **Chương 17** (Đồ thị nâng cao) mở rộng sang cây khung, MST và các thuật toán trên đồ thị có trọng số.
