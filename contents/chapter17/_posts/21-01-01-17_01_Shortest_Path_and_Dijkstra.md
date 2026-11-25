---
layout: post
title: "Đường đi Ngắn nhất và Thuật toán Dijkstra"
categories: chapter17
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Bài toán đường đi ngắn nhất: BFS (không trọng số), Dijkstra (trọng số ≥ 0), Bellman–Ford (có cạnh âm); phép relax, binary heap O((V+E) log V) và phân biệt với MST."
---

> **Câu chuyện mở đầu:** Năm 1956, Edsger W. Dijkstra ngồi uống cà phê ở Amsterdam cùng vợ sắp cưới để nghĩ một bài toán trình diễn cho chiếc máy tính ARMAC mới lắp: tìm tuyến đường ngắn nhất nối hai thành phố Hà Lan. Chỉ trong **20 phút** không dùng giấy bút, ông đã phát minh ra thuật toán mang tên mình — và ngày nay, **thuật toán Dijkstra** đang chạy hàng tỷ lần mỗi ngày trong Google Maps, định tuyến Internet (OSPF) và trò chơi điện tử!

<div class="textbook-epigraph" markdown="1">

"The shortest path is not always the path with the fewest edges."

<span class="epigraph-attribution">— Tinh thần đường đi có trọng số</span>

</div>

Hệ thống dẫn đường GPS và định tuyến mạng đều cần giải bài toán: từ đỉnh $$s$$ đến đỉnh $$t$$, đường đi nào có **chi phí nhỏ nhất** (theo quãng đường, độ trễ hoặc cước phí)? Khi mọi cạnh có cùng độ dài bằng 1, thuật toán **BFS** (Chương 12) là đủ. Khi các cạnh mang **trọng số không âm**, ta cần **thuật toán Dijkstra**. Bài học này định nghĩa bài toán đường đi ngắn nhất từ một nguồn, trình bày Dijkstra và giới thiệu Bellman–Ford cho trường hợp đồ thị có cạnh trọng số âm.

![Dijkstra](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_dijkstra_example.svg)

<p class="textbook-figure-caption" data-figure="17.1">Minh họa Dijkstra xuất phát từ $$A$$: chốt dần các đỉnh theo giá trị khoảng cách tăng dần và dùng phép relax trên cạnh kề để cập nhật ứng viên.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** bài toán đường đi ngắn nhất không trọng số (BFS) và có trọng số (Dijkstra, Bellman–Ford).
- **Mô tả** cơ chế của Dijkstra gồm thao tác trích cực tiểu (*extract-min*), phép **relax** và mảng `parent`.
- **Nêu** độ phức tạp $$O((V+E)\log V)$$ khi cài đặt bằng binary heap.
- **Giải thích** vì sao cạnh trọng số âm làm sai thuật toán Dijkstra và vai trò của Bellman–Ford.
- **So sánh** bài toán đường đi ngắn nhất với bài toán **cây khung nhỏ nhất (MST)** ở Chương 16.

**Từ khóa**: single-source shortest path, Dijkstra, relax, priority queue, Bellman–Ford, chu trình âm.

</div>

## Bản đồ kiến thức nền: Đường đi Ngắn nhất & Điều kiện Sống còn của Dijkstra

### 1. Phép Nới lỏng Cạnh (Edge Relaxation)
- **Bản chất:** Mọi thuật toán đường đi ngắn nhất đều xoay quanh một thao tác sơ cấp: nếu đi tới $$u$$ mất $$d[u]$$ và có cạnh $$(u, v)$$ nặng $$w(u, v)$$ sao cho $$d[u] + w(u, v) < d[v]$$, ta lập tức cập nhật $$d[v] \leftarrow d[u] + w(u, v)$$!

### 2. Bất biến Tham lam của Dijkstra (Chỉ đúng khi $$w(u, v) \ge 0$$!)
- **Bản chất:** Tại mỗi bước, Dijkstra chọn đỉnh $$u$$ chưa chốt có $$d[u]$$ **nhỏ nhất** trong Min-Heap và tuyên bố $$d[u]$$ đã là **khoảng cách ngắn nhất cuối cùng**! Điều này đúng 100% **chỉ vì mọi cạnh đều không âm**: không thể đi vòng qua đỉnh khác lớn hơn rồi cộng thêm số dương mà lại nhỏ hơn $$d[u]$$ được!

### 3. Bản đồ chọn Thuật toán theo Trọng số
- **Không trọng số:** BFS ($$O(V + E)$$).
- **Trọng số không âm ($$w \ge 0$$):** **Dijkstra + Min-Heap** ($$O((V + E)\log V)$$).
- **Có trọng số âm (không có chu trình âm):** **Bellman–Ford** ($$O(VE)$$, nới lỏng toàn bộ cạnh $$V - 1$$ lần).

## Ví dụ tính tay cầm tay chỉ việc: Chạy Dijkstra & Phản ví dụ Cạnh âm

### Ví dụ 1: Theo vết bảng Dijkstra trên đồ thị 4 đỉnh $$S, A, B, T$$
Các cạnh có hướng: $$(S, A)=1,\; (S, B)=4,\; (A, B)=2,\; (A, T)=6,\; (B, T)=1$$. Khởi tạo $$d = (0, \infty, \infty, \infty)$$:
1. **Chốt $$S$$ ($$d[S]=0$$):** Nới lỏng $$(S,A), (S,B) \implies d[A] = 1,\; d[B] = 4,\; d[T] = \infty$$.
2. **Chốt $$A$$ (nhỏ nhất: $$d[A]=1$$):** Nới lỏng $$(A,B)$$ cho $$1 + 2 = 3 < 4 \implies d[B] = 3$$; nới lỏng $$(A,T)$$ cho $$1 + 6 = 7 \implies d[T] = 7$$.
3. **Chốt $$B$$ (nhỏ nhất: $$d[B]=3$$):** Nới lỏng $$(B,T)$$ cho $$3 + 1 = 4 < 7 \implies d[T] = 4$$!
4. **Chốt $$T$$ ($$d[T]=4$$):** Kết thúc! Đường đi ngắn nhất là $$S \to A \to B \to T$$ với tổng độ dài **$$1 + 2 + 1 = 4$$**!

### Ví dụ 2: Vì sao 1 cạnh âm duy nhất làm Dijkstra trả kết quả SAI?
Xét 3 đỉnh $$S, A, B$$ với các cạnh: $$(S, A) = 2,\; (S, B) = 5,\; (B, A) = -4$$!
- Dijkstra thấy $$d[A] = 2 < 5 = d[B]$$ nên **chốt vĩnh viễn $$d[A] = 2$$** ngay bước 1 — bỏ lỡ hoàn toàn đường đi $$S \to B \to A$$ có độ dài thực là **$$5 + (-4) = 1 < 2$$**!

### Khung giải thích: 4 bước nắm chắc chứng minh Tính đúng của Dijkstra (nên đọc chậm)

#### Bước 1: Giả sử phản chứng tại đỉnh đầu tiên $$u$$ bị chốt sai
Gọi $$u$$ là đỉnh đầu tiên được rút khỏi Min-Heap mà $$d[u] > \delta(S, u)$$ (khoảng cách ngắn nhất thật).

#### Bước 2: Lần theo đường đi ngắn nhất thật từ $$S$$ tới $$u$$
Đường đi thật này bắt đầu trong tập đã chốt $$S_{\text{done}}$$ và kết thúc ở $$u \notin S_{\text{done}}$$, nên phải có cạnh đầu tiên $$(x, y)$$ vượt ranh giới từ $$x \in S_{\text{done}}$$ sang $$y \notin S_{\text{done}}$$.

#### Bước 3: Dùng tính không âm của trọng số để tạo mâu thuẫn
Vì $$x$$ đã chốt đúng trước $$u$$, sau khi nới lỏng $$(x, y)$$ ta có $$d[y] = \delta(S, y)$$. Mà mọi cạnh phía sau $$y$$ đến $$u$$ đều **không âm** nên $$d[y] = \delta(S, y) \le \delta(S, u) < d[u]$$ — mâu thuẫn với việc Dijkstra vừa chọn $$u$$ là đỉnh có $$d$$ nhỏ nhất!

#### Bước 4: Tối ưu thực tế bằng Thuật toán $$A^*$$
Trong bản đồ GPS thực tế, cộng thêm hàm ước lượng khoảng cách chim bay $$h(v)$$ (heuristic chấp nhận được) vào độ ưu tiên của Dijkstra tạo ra **thuật toán $$A^*$$**, thu hẹp vùng tìm kiếm hàng chục lần mà vẫn giữ nguyên độ chính xác!

$$
\text{Trọng số }w \ge 0
\;\xrightarrow{\;\text{Min-Heap + Relaxation}\;}\;
\text{Dijkstra }O((V+E)\log V)
\;\xrightarrow{\;+\text{ heuristic }h(v)\;}\;
\text{Thuật toán }A^*.
$$

## Bài toán đường đi ngắn nhất

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho đồ thị $$G=(V,E)$$ (có hướng hoặc vô hướng) với trọng số $$w(e)$$ trên mỗi cạnh và một đỉnh nguồn $$s$$. **Khoảng cách ngắn nhất** $$\mathrm{dist}(s,v)$$ là **tổng trọng số nhỏ nhất** trong tất cả các đường đi từ $$s$$ đến $$v$$. Nếu không tồn tại đường đi từ $$s$$ đến $$v$$, ta quy ước $$\mathrm{dist}(s,v)=\infty$$.

</div>

| Loại trọng số | Thuật toán tiêu biểu | Độ phức tạp (tiêu biểu) |
|:---|:---|:---|
| Mọi cạnh có độ dài 1 (không trọng số) | **BFS** | $$O(V+E)$$ |
| Trọng số không âm $$w(e)\ge 0$$ | **Dijkstra** | $$O((V+E)\log V)$$ (binary heap) |
| Có cạnh âm $$w(e)<0$$ (không có chu trình âm, hoặc cần phát hiện) | **Bellman–Ford** | $$O(VE)$$ |

**Phân biệt với MST.** Cây khung nhỏ nhất (MST) tối ưu tổng trọng số của **tập cạnh** phủ toàn bộ đỉnh. Ngược lại, bài toán đường đi ngắn nhất tối ưu **từng đường đi** xuất phát từ đỉnh nguồn $$s$$ — tập các cạnh `parent` tạo thành *cây đường đi ngắn nhất* (*shortest-path tree*), và cây này **không** nhất thiết trùng với MST.

## Thuật toán Dijkstra

**Ý tưởng tham lam.** Duy trì ước lượng khoảng cách `dist[v]` (khởi tạo $$\infty$$ với mọi đỉnh, riêng `dist[s]=0`). Ở mỗi bước, **chốt** đỉnh $$u$$ chưa được chốt có `dist[u]` nhỏ nhất; sau đó với mỗi cạnh $$(u,v)$$ đi ra từ $$u$$, thực hiện phép **relax**:

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

**Định lý.** Nếu mọi cạnh của đồ thị đều có trọng số **không âm**, thì ngay tại thời điểm đỉnh $$u$$ được lấy ra bởi thao tác extract-min, giá trị $$\mathrm{dist}[u]$$ chính là khoảng cách ngắn nhất thực sự từ $$s$$ đến $$u$$.

</div>

*Phác thảo chứng minh.* Giả sử $$u$$ là đỉnh đầu tiên bị chốt với giá trị khoảng cách sai. Đường đi tối ưu từ $$s$$ đến $$u$$ phải rời khỏi tập đỉnh đã chốt qua một cạnh nào đó; do mọi trọng số đều $$w \ge 0$$, không thể tồn tại đường đi vòng qua các đỉnh chưa chốt mà có tổng độ dài nhỏ hơn ước lượng tại thời điểm chọn $$u$$ — dẫn tới mâu thuẫn.

**Độ phức tạp.** Khi dùng binary heap, thuật toán chạy trong $$O((V+E)\log V)$$; với Fibonacci heap (về mặt lý thuyết) là $$O(E + V\log V)$$.

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét đồ thị có các cạnh $$(A,B,1)$$, $$(A,C,4)$$, $$(B,C,2)$$, $$(B,D,6)$$, $$(C,D,1)$$. Chạy Dijkstra từ đỉnh nguồn $$A$$:

- Chốt $$A$$ (0); relax các cạnh kề được $$B=1$$, $$C=4$$.
- Chốt $$B$$ (1); relax được $$C=\min(4,1+2)=3$$ và $$D=7$$.
- Chốt $$C$$ (3); relax được $$D=\min(7,3+1)=4$$.
- Chốt $$D$$ (4).

Đường đi ngắn nhất từ $$A$$ đến $$D$$ là $$A\to B\to C\to D$$ với tổng trọng số bằng 4.

</div>

<div class="interactive-demo" markdown="1">
<div data-demo="dijkstra-visualizer"></div>
</div>
<script src="{{ '/public/js/dijkstra-visualizer.js' | relative_url }}"></script>

Minh họa đồ thị dùng chung: chọn **Dijkstra** để theo dõi nhãn $$d(v)$$, tập đỉnh đã chốt $$S$$ và phép relax trên từng cạnh.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-explainer" data-algorithm="dijkstra"></div>
</div>
<script src="{{ '/public/js/explainers/graph-explainer.js' | relative_url }}"></script>

### Video ngắn: Dijkstra từng bước

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/dijkstra-shortest-path.mp4"></video>
</div>

Video dài khoảng 2 phút 58 giây: chạy Dijkstra từng bước trên đồ thị có hướng 6 đỉnh, theo dõi nhãn $$d[v]$$, phép relax và hàng đợi ưu tiên; dựng cây đường đi ngắn nhất (cho thấy đường 5 cạnh có tổng trọng số 8 vẫn ngắn hơn đường 3 cạnh tổng 10); giải thích vì sao bước chốt đúng khi trọng số không âm và nêu ví dụ cạnh âm khiến Dijkstra trả về kết quả sai.

## Bellman–Ford và trọng số âm

<div class="textbook-theorem" markdown="1">

**Định lý.** Nếu tồn tại một **chu trình âm** có thể đi tới từ đỉnh nguồn $$s$$, thì khoảng cách ngắn nhất **không bị chặn dưới** (có thể đi vòng vô hạn để giảm tổng trọng số). Thuật toán **Bellman–Ford** thực hiện $$\vert V\vert -1$$ lượt relax toàn bộ các cạnh; nếu ở lượt thứ $$\vert V\vert $$ vẫn còn cạnh có thể cải thiện khoảng cách thì đồ thị tồn tại chu trình âm.

</div>

**Dijkstra cho kết quả sai** khi có cạnh âm vì một đỉnh có thể bị chốt quá sớm trước khi đường đi vòng qua cạnh âm được xét đến. Với đồ thị **không liên thông** từ $$s$$, các đỉnh không thể đi tới vẫn giữ giá trị `dist` bằng $$\infty$$, đây là kết quả hợp lệ.

## Ứng dụng

- Định tuyến mạng theo chi phí liên kết (như giao thức OSPF dựa trên đường đi ngắn nhất).
- Tìm đường trên bản đồ hoặc lưới trò chơi có chi phí (thuật toán A\* mở rộng Dijkstra bằng một hàm heuristic chấp nhận được).
- Phân tích mạng quan hệ có trọng số, thay vì chỉ đếm số bước nhảy như BFS.

## Bài tập

### Bài tập 1

Trong ví dụ ở mục Thuật toán Dijkstra, hãy cho biết $$\mathrm{dist}(A,D)$$ và đường đi ngắn nhất tương ứng.

<details>
<summary>Đáp án</summary>

$$\mathrm{dist}(A,D)=4$$ theo đường đi $$A\to B\to C\to D$$ (tổng $$1+2+1$$).

</details>

### Bài tập 2

Vì sao BFS không cho kết quả đúng khi đồ thị có các cạnh trọng số 1 và 10?

<details>
<summary>Đáp án</summary>

BFS chỉ tối ưu **số cạnh** chứ không tối ưu tổng trọng số. Một đường đi gồm 2 cạnh với tổng trọng số bằng 2 có thể ngắn hơn đường đi 1 cạnh trọng số 10, nhưng BFS sẽ ưu tiên chọn đường ít cạnh hơn dù tổng chi phí lớn hơn.

</details>

### Bài tập 3

Nếu đồ thị có cạnh $$(A,B,-1)$$, dùng thuật toán Dijkstra xuất phát từ $$A$$ có đảm bảo đúng không? Nên dùng thuật toán nào?

<details>
<summary>Đáp án</summary>

Không đảm bảo đúng vì có cạnh trọng số âm. Trong trường hợp này cần dùng **Bellman–Ford**; nếu thuật toán phát hiện chu trình âm đi tới được từ $$A$$ thì kết luận không tồn tại đường đi ngắn nhất hữu hạn.

</details>

### Bài tập 4

Nêu một điểm khác biệt cốt lõi giữa thuật toán Dijkstra và thuật toán Kruskal.

<details>
<summary>Đáp án</summary>

Dijkstra tìm đường đi ngắn nhất xuất phát từ một đỉnh nguồn cố định $$s$$ đến các đỉnh còn lại, trong khi Kruskal tìm cây khung có tổng trọng số nhỏ nhất phủ toàn bộ tập đỉnh mà không phụ thuộc vào đỉnh nguồn.

</details>

## Tóm tắt

1. **BFS** tìm đường đi ít cạnh nhất trong $$O(V+E)$$.
2. **Dijkstra** áp dụng cho đồ thị có trọng số không âm ($$w\ge 0$$), kết hợp chọn tham lam, phép relax và hàng đợi ưu tiên.
3. **Bellman–Ford** xử lý được cạnh trọng số âm và phát hiện chu trình âm.
4. Cây đường đi ngắn nhất khác với cây khung nhỏ nhất (MST).

Trong bài tiếp theo, ta sẽ học về **sắp xếp topo** trên đồ thị có hướng không chu trình (DAG).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=_lHSawdgXpI">Dijkstra&#x27;s algorithm in 3 minutes</a> — Michael Sambol, tiếng Anh. Giới thiệu nhanh cơ chế của Dijkstra trước khi đi vào chứng minh chi tiết.
- <a href="https://www.youtube.com/watch?v=GazC3A4OQTE">Dijkstra&#x27;s Algorithm - Computerphile</a> — Computerphile, tiếng Anh. Giải thích trực giác vì sao thuật toán luôn chọn đỉnh có nhãn khoảng cách nhỏ nhất.
- <a href="https://www.youtube.com/watch?v=XB4MIexjvY0">3.6 Dijkstra Algorithm - Single Source Shortest Path - Greedy Method</a> — Abdul Bari, tiếng Anh. Minh họa đầy đủ một ví dụ Dijkstra kèm bảng cập nhật khoảng cách.
