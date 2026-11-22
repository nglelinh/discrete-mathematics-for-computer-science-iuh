---
layout: post
title: "Euler, Hamilton và Duyệt Đồ thị"
categories: chapter12
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Đường đi và chu trình Euler với điều kiện bậc đỉnh; đường đi và chu trình Hamilton; thuật toán duyệt BFS và DFS có độ phức tạp O(V+E); phân biệt lớp bài toán P và NP-hard."
---

<div class="textbook-epigraph" markdown="1">

"The Königsberg bridge problem is an example of a problem that could be solved only by means of graph theory."

<span class="epigraph-attribution">— Leonhard Euler</span>

</div>

Năm 1736, Leonhard Euler giải quyết một bài toán thực tế tại Königsberg: liệu có thể đi qua mỗi cây cầu đúng một lần rồi quay về điểm xuất phát hay không? Câu trả lời hoàn toàn phụ thuộc vào **bậc** của các đỉnh trong mô hình đồ thị, không phụ thuộc vào hình vẽ địa lý. Khi đổi mục tiêu từ đi qua mọi cạnh sang đi qua mọi đỉnh đúng một lần, ta gặp bài toán **chu trình Hamilton** và bài toán người du lịch (TSP), vốn có độ khó tính toán cao hơn nhiều. Cuối bài, ta tìm hiểu **BFS** và **DFS** — hai thuật toán duyệt đồ thị cơ bản có thời gian chạy tuyến tính theo kích thước danh sách kề.

![Leonhard Euler](/discrete-mathematics-for-computer-science-iuh/img/course/Leonhard_Euler.jpg)

<p class="textbook-figure-caption" data-figure="12.8">Leonhard Euler (1707–1783) và bài toán bảy cây cầu Königsberg — khởi nguồn của lý thuyết đồ thị.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** đường đi/chu trình Euler và đường đi/chu trình Hamilton.
- **Áp dụng** điều kiện về bậc đỉnh để kiểm tra sự tồn tại đường đi và chu trình Euler.
- **Mô tả** cơ chế hoạt động của BFS và DFS, đồng thời giải thích độ phức tạp $$O(V+E)$$ trên danh sách kề.
- **Giải thích** vì sao bài toán Euler giải được trong thời gian đa thức (lớp P) trong khi tối ưu Hamilton/TSP thuộc lớp NP-hard.

**Từ khóa**: Euler path/cycle, Hamilton path/cycle, BFS, DFS, Hierholzer, NP-hard.

</div>

## Đường đi và chu trình Euler

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **Đường đi Euler** (*Eulerian path*): trail đi qua **mỗi cạnh** của $$G$$ **đúng một lần**.
- **Chu trình Euler** (*Eulerian circuit*): đường đi Euler khép kín, có đỉnh bắt đầu và đỉnh kết thúc trùng nhau.

</div>

Đối tượng cần đi qua hết ở đây là **cạnh**; các đỉnh có thể (và thường phải) được thăm nhiều lần.

<div class="textbook-theorem" markdown="1">

**Định lý** (Euler, trường hợp vô hướng). Cho đồ thị vô hướng $$G$$ mà mọi cạnh đều nằm trong cùng một thành phần liên thông (có thể bỏ qua các đỉnh cô lập). Khi đó:

- $$G$$ có **chu trình Euler** khi và chỉ khi mọi đỉnh đều có bậc **chẵn**;
- $$G$$ có **đường đi Euler** (không nhất thiết khép kín) khi và chỉ khi số đỉnh bậc **lẻ** bằng **0** hoặc **2**:

  - nếu có 0 đỉnh bậc lẻ: đường đi Euler khép kín (chính là chu trình Euler);
  - nếu có đúng 2 đỉnh bậc lẻ: đường đi Euler mở, xuất phát tại một đỉnh bậc lẻ và kết thúc tại đỉnh bậc lẻ còn lại.

</div>

*Ý tưởng chứng minh.* Mỗi lần hành trình đi vào rồi rời khỏi một đỉnh trung gian, nó sử dụng đúng 2 cạnh kề với đỉnh đó. Riêng tại hai đầu mút của đường đi mở, số cạnh sử dụng bị lẻ đi 1. Khi điều kiện tồn tại được thỏa mãn, thuật toán **Hierholzer** xây dựng chu trình Euler trong thời gian $$O(\vert E\vert )$$ bằng cách liên tục ghép các chu trình con dọc theo các cạnh chưa đi qua.

![Mô hình 7 cầu Königsberg](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_konigsberg_euler.svg)

<p class="textbook-figure-caption" data-figure="12.9">Bốn khu đất và bảy cây cầu được mô hình hóa thành đa đồ thị có 4 đỉnh bậc lẻ, nên không tồn tại đường đi Euler.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1** (Königsberg). Mô hình đa đồ thị có 4 đỉnh và cả 4 đỉnh đều có bậc lẻ. Vì số đỉnh bậc lẻ là $$4 \neq 0,2$$, theo định lý Euler, **không** tồn tại đường đi Euler — không thể đi qua mỗi cây cầu đúng một lần dù xuất phát từ đâu.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Một đồ thị vô hướng liên thông có dãy bậc $$2,2,4,4$$ có tất cả bậc chẵn $$\implies$$ tồn tại **chu trình Euler**.

Với dãy bậc $$3,3,2,2$$, đồ thị có đúng hai đỉnh bậc lẻ $$\implies$$ tồn tại **đường đi Euler** mở nhưng **không** có chu trình Euler.

</div>

### Video ngắn: Bảy cây cầu Königsberg

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/konigsberg-bridges.mp4"></video>
</div>

Euler mô hình hóa bốn khu đất thành 4 đỉnh và bảy cây cầu thành 7 cạnh, thu được dãy bậc $$3,5,3,3$$ — cả bốn đỉnh đều bậc lẻ. Theo định lý Euler, một hành trình đi qua mỗi cầu đúng một lần chỉ tồn tại khi số đỉnh bậc lẻ là $$0$$ hoặc $$2$$, nên không thể tìm ra lộ trình thỏa mãn yêu cầu.

## Đường đi và chu trình Hamilton

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **Đường đi Hamilton**: đường đi đơn (path) đi qua **mỗi đỉnh** của đồ thị đúng một lần.
- **Chu trình Hamilton**: chu trình (cycle) đi qua mọi đỉnh đúng một lần rồi quay lại đỉnh xuất phát.

</div>

Đối tượng cần đi qua hết ở đây là **đỉnh**; không bắt buộc phải đi qua toàn bộ các cạnh.

![Euler so với Hamilton](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_euler_vs_hamilton.svg)

<p class="textbook-figure-caption" data-figure="12.10">Trái: chu trình Euler yêu cầu đi qua mọi cạnh đúng một lần. Phải: chu trình Hamilton yêu cầu đi qua mọi đỉnh đúng một lần.</p>

| | Euler | Hamilton |
|:---|:---|:---|
| Đối tượng phủ | Cạnh | Đỉnh |
| Điều kiện kiểm tra | Dựa trực tiếp trên bậc chẵn/lẻ | Không có điều kiện bậc đơn giản tương đương |
| Thuật toán | Hierholzer trong $$O(E)$$ | Chưa biết thuật toán thời gian đa thức tổng quát cho bài toán quyết định hoặc tối ưu |
| Biến thể tối ưu | Ít gặp trong giáo trình cơ sở | TSP — tìm chu trình Hamilton có tổng trọng số nhỏ nhất |

**TSP** (*Traveling Salesman Problem*): trên đồ thị đầy đủ có trọng số, tìm chu trình Hamilton có tổng trọng số nhỏ nhất. Bài toán tối ưu này (và nhiều biến thể quyết định liên quan) thuộc lớp **NP-hard** (xem thêm Chương 20). Trong thực tế, người ta thường dùng thuật toán heuristic hoặc xấp xỉ để giải TSP; điều này không mâu thuẫn với việc chu trình Euler vẫn giải được nhanh chóng trong thời gian tuyến tính.

### Video ngắn: BFS và DFS

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/bfs-vs-dfs.mp4"></video>
</div>

Video dài khoảng 3 phút 6 giây: chạy BFS (hàng đợi) và DFS (ngăn xếp/đệ quy) trên cùng một đồ thị 7 đỉnh với thứ tự duyệt đỉnh kề theo bảng chữ cái như mã nguồn trong bài; minh họa khoảng cách theo lớp và đường đi ngắn nhất $$A \to B \to D \to G$$ trên cây BFS; chỉ ra cạnh ngược $$C$$–$$A$$ trong DFS tạo chu trình $$A$$–$$B$$–$$E$$–$$C$$–$$A$$; cho thấy sự khác biệt khi đổi `popleft()` thành `pop()`; cùng bảng so sánh và ứng dụng đếm thành phần liên thông với độ phức tạp $$O(V + E)$$.

## BFS — duyệt theo chiều rộng

**BFS** (*Breadth-First Search*) duyệt đồ thị theo từng **tầng** khoảng cách tăng dần tính từ đỉnh nguồn $$s$$, sử dụng cấu trúc dữ liệu **hàng đợi** (*queue*).

![BFS theo tầng](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_bfs_layers.svg)

<p class="textbook-figure-caption" data-figure="12.11">BFS xuất phát từ $$s$$: tầng $$k$$ gồm các đỉnh có đường đi ngắn nhất (tính theo số cạnh) bằng $$k$$.</p>

**Tính chất quan trọng.** Trên đồ thị **không trọng số** (mỗi cạnh có độ dài 1), lần đầu tiên BFS chạm tới đỉnh $$v$$ cũng chính là lúc tìm ra đường đi từ $$s$$ đến $$v$$ với **số cạnh ít nhất**.

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

## DFS — duyệt theo chiều sâu

**DFS** (*Depth-First Search*) ưu tiên đi sâu theo một nhánh tới các đỉnh chưa thăm trước khi quay lui, sử dụng **ngăn xếp** (*stack*) tường minh hoặc ngăn xếp gọi hàm khi cài đặt bằng đệ quy.

![Thứ tự DFS](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_dfs_order.svg)

<p class="textbook-figure-caption" data-figure="12.12">DFS mở rộng theo nhánh sâu trước; cạnh ngược trên cây/rừng DFS giúp phát hiện chu trình.</p>

Các ứng dụng điển hình của DFS:

- phát hiện chu trình (trên cả đồ thị vô hướng và có hướng);
- sắp xếp tôpô (**topological sort**) trên DAG;
- tìm thành phần liên thông và thành phần liên thông mạnh (SCC) trên đồ thị có hướng;
- duyệt không gian trạng thái trong kỹ thuật quay lui (backtracking).

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

## Độ phức tạp chung

<div class="textbook-theorem" markdown="1">

**Định lý** (chi phí duyệt). Khi đồ thị được biểu diễn bằng **danh sách kề**, cả BFS và DFS đều có thời gian chạy $$O(\vert V\vert  + \vert E\vert )$$ và bộ nhớ phụ $$O(\vert V\vert )$$ để lưu tập đỉnh đã thăm cùng hàng đợi hoặc ngăn xếp.

</div>

*Giải thích.* Mỗi đỉnh được đưa vào hàng đợi hoặc ngăn xếp tối đa một lần, và danh sách kề của mỗi đỉnh chỉ được duyệt đúng một lần khi xử lý đỉnh đó. Tổng độ dài các danh sách kề là $$\Theta(\vert E\vert )$$ (hoặc $$2\vert E\vert $$ đối với đồ thị vô hướng, cùng bậc tăng trưởng).

Nếu dùng **ma trận kề**, thao tác tìm các láng giềng của mỗi đỉnh tốn $$O(\vert V\vert )$$, làm tổng thời gian tăng lên $$O(\vert V\vert ^2)$$ — kém hiệu quả rõ rệt trên đồ thị thưa.

| Thuật toán | Cấu trúc hỗ trợ | Ứng dụng chính |
|:---|:---|:---|
| BFS | Hàng đợi (Queue) | Đường đi ngắn nhất theo số cạnh; phân tầng; kiểm tra đồ thị hai phía |
| DFS | Ngăn xếp (Stack) / Đệ quy | Phát hiện chu trình; sắp xếp tôpô; tìm SCC; quay lui |

<div class="textbook-example" markdown="1">

**Ví dụ 3** (ứng dụng).

- Chạy BFS từ máy chủ gốc trong mạng đo theo số bước nhảy (hop-count): chỉ số tầng chính là số bước chuyển tiếp tối thiểu.
- Chạy DFS trên đồ thị phụ thuộc: nếu gặp cạnh ngược trỏ về một đỉnh đang nằm trên ngăn xếp đệ quy thì đồ thị chứa chu trình — hệ thống có thể báo lỗi phụ thuộc vòng trước khi build.

</div>

## Thử nghiệm tương tác

### Euler và Hamilton

Bật/tắt cạnh trên đồ thị nhỏ để kiểm tra điều kiện bậc của chu trình Euler và tìm một chu trình Hamilton (nếu tồn tại).

<div class="interactive-demo" markdown="1">
<div data-demo="euler-hamilton-checker"></div>
</div>
<script src="{{ '/public/js/euler-hamilton-checker.js' | relative_url }}"></script>

### BFS / DFS từng bước

Chạy mô phỏng BFS hoặc DFS từng bước để theo dõi trạng thái hàng đợi/ngăn xếp, thứ tự thăm đỉnh và khoảng cách $$d$$ (số cạnh tính từ đỉnh nguồn trong BFS).

<div class="interactive-demo" markdown="1">
<div data-demo="bfs-dfs-visualizer"></div>
</div>
<script src="{{ '/public/js/bfs-dfs-visualizer.js' | relative_url }}"></script>


### Minh họa thuật toán đồ thị (BFS / DFS)

Sử dụng khung minh họa tương tác (hỗ trợ chỉnh sửa đồ thị trên canvas SVG, chạy từng bước và tô sáng giả mã) để so sánh trực tiếp BFS và DFS trên cùng một đồ thị.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-explainer" data-algorithm="bfs"></div>
</div>
<script src="{{ '/public/js/explainers/graph-explainer.js' | relative_url }}"></script>



## Bài tập

### Bài tập 1

Một đồ thị vô hướng liên thông có bậc các đỉnh là $$2, 2, 4, 4$$. Đồ thị này có chu trình Euler không?

<details>
<summary>Đáp án</summary>

Mọi đỉnh đều có bậc chẵn và đồ thị liên thông $$\implies$$ **có** chu trình Euler.

</details>

### Bài tập 2

Một đồ thị vô hướng liên thông có dãy bậc $$3, 3, 2, 2$$. Đồ thị có đường đi Euler không? Có chu trình Euler không?

<details>
<summary>Đáp án</summary>

Đồ thị có đúng hai đỉnh bậc lẻ $$\implies$$ **có đường đi Euler** mở nhưng **không** có chu trình Euler.

</details>

### Bài tập 3

Vì sao BFS tìm được đường đi ngắn nhất theo số cạnh trên đồ thị không trọng số?

<details>
<summary>Đáp án</summary>

BFS duyệt các đỉnh theo thứ tự khoảng cách không giảm tính từ đỉnh nguồn. Do đó, vào thời điểm đỉnh $$v$$ được phát hiện lần đầu tiên, tất cả các đỉnh ở các tầng gần hơn đã được xét hết, nên không thể tồn tại đường đi nào tới $$v$$ có ít cạnh hơn tầng hiện tại.

</details>

### Bài tập 4

Phân loại độ khó của hai bài toán sau (thuộc P hay NP-hard): (a) tìm chu trình Euler; (b) tìm chu trình Hamilton có tổng trọng số nhỏ nhất (TSP).

<details>
<summary>Đáp án</summary>

(a) Tìm chu trình Euler giải được trong thời gian đa thức (thuật toán Hierholzer) — thuộc lớp **P**.  
(b) Bài toán tối ưu TSP thuộc lớp **NP-hard**.

</details>

### Bài tập 5

Cho đồ thị vô hướng biểu diễn bằng danh sách kề:

```text
0: 1, 2
1: 0, 3
2: 0, 3
3: 1, 2
```

(a) Chạy BFS từ đỉnh 0: nêu một thứ tự thăm hợp lệ và khoảng cách tới từng đỉnh.  
(b) Đồ thị có chu trình Euler không?

<details>
<summary>Đáp án</summary>

(a) Một thứ tự duyệt BFS hợp lệ là: thăm $$0$$, tiếp theo là $$1, 2$$ (tầng 1), rồi đến $$3$$ (tầng 2).  
Khoảng cách tương ứng: $$\mathrm{dist}(0)=0$$, $$\mathrm{dist}(1)=\mathrm{dist}(2)=1$$, $$\mathrm{dist}(3)=2$$.

(b) Bậc các đỉnh là $$\deg(0)=\deg(1)=\deg(2)=\deg(3)=2$$ — mọi đỉnh đều có bậc chẵn và đồ thị liên thông $$\implies$$ **có** chu trình Euler (chẳng hạn $$0 \to 1 \to 3 \to 2 \to 0$$).

</details>

## Tóm tắt

1. **Euler** xét việc đi qua mọi **cạnh**: điều kiện là mọi đỉnh bậc chẵn (chu trình) hoặc đúng 0 hay 2 đỉnh bậc lẻ (đường đi), giải được trong thời gian đa thức.
2. **Hamilton** xét việc đi qua mọi **đỉnh**: không có điều kiện bậc đơn giản tương đương; phiên bản tối ưu TSP thuộc lớp NP-hard.
3. **BFS** duyệt theo tầng, tìm đường đi ngắn nhất trên đồ thị không trọng số.
4. **DFS** duyệt theo chiều sâu, phục vụ phát hiện chu trình, sắp xếp tôpô và tìm SCC; cả BFS và DFS đều có độ phức tạp $$O(V+E)$$ trên danh sách kề.

Chương 12 dừng ở các khái niệm đồ thị cơ bản. **Chương 16** (Cây) và **Chương 17** (Đồ thị nâng cao) sẽ mở rộng sang cây khung, cây khung nhỏ nhất (MST) và các thuật toán trên đồ thị có trọng số.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=dSK5jTEe-AM">Euler Paths &amp; the 7 Bridges of Konigsberg | Graph Theory</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày đường đi Euler qua bài toán bảy cây cầu Königsberg.
- <a href="https://www.youtube.com/watch?v=t_6VByupc1U">[Discrete Mathematics] Hamilton Cycles</a> — TrevTutor, tiếng Anh. Giới thiệu chu trình Hamilton.
- <a href="https://www.youtube.com/watch?v=pcKY4hjDrxk">5.1 Graph Traversals - BFS &amp; DFS -Breadth First Search and Depth First Search</a> — Abdul Bari, tiếng Anh. Trình bày chi tiết hai thuật toán duyệt đồ thị BFS và DFS.
