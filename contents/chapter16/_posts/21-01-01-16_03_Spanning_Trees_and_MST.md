---
layout: post
title: "Cây khung và Cây khung Nhỏ nhất"
categories: chapter16
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Cây khung, cây khung nhỏ nhất (MST), tính chất tham lam (cut property), thuật toán Kruskal (Union–Find) và Prim (hàng đợi ưu tiên), độ phức tạp và ứng dụng mạng."
---

> **Câu chuyện mở đầu:** Công ty điện lực cần kéo cáp quang kết nối $$n$$ thành phố với **tổng chi phí thấp nhất**. Họ không cần mọi cặp thành phố đều có đường nối trực tiếp — chỉ cần tất cả thông suốt với nhau (một **cây khung nhỏ nhất — MST**). Kỳ diệu thay, dù phần lớn các bài toán tối ưu trên đồ thị đều rất khó, với MST thì **chiến lược tham lam (Greedy)** lại cho ra **đáp án tối ưu toàn cục 100%** nhờ hai thuật toán kinh điển **Kruskal** và **Prim**!

<div class="textbook-epigraph" markdown="1">

"A minimum spanning tree is the cheapest way to keep a network connected."

<span class="epigraph-attribution">— Tinh thần thuật toán greedy trên đồ thị</span>

</div>

Bài toán kết nối toàn bộ các trạm với **tổng chi phí cáp nhỏ nhất** sao cho mạng vẫn **liên thông** được mô hình hóa bằng **cây khung nhỏ nhất** (*Minimum Spanning Tree*, **MST**). Khác với bài toán đường đi ngắn nhất (tối ưu đường đi từ một đỉnh nguồn), MST tối ưu **tập cạnh** tạo thành một cây phủ toàn bộ tập đỉnh. Bài học này trình bày định nghĩa MST và hai thuật toán tham lam kinh điển: Kruskal và Prim.

![MST](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_mst_example.svg)

<p class="textbook-figure-caption" data-figure="16.4">MST gồm $$n-1$$ cạnh (nét đậm), không có chu trình và có tổng trọng số nhỏ nhất trong mọi cây khung.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** cây khung và cây khung nhỏ nhất (MST) trên đồ thị vô hướng liên thông có trọng số.
- **Mô tả** thuật toán Kruskal (sắp xếp cạnh kết hợp Union–Find) và Prim (mở rộng dần từ một tập đỉnh).
- **Nêu** độ phức tạp tiêu biểu $$O(E\log E)$$ của Kruskal và $$O(E\log V)$$ của Prim.
- **Áp dụng** ý tưởng MST vào bài toán thiết kế mạng và phân cụm sơ cấp.

**Từ khóa**: spanning tree, MST, Kruskal, Prim, Union–Find, greedy.

</div>

## Bản đồ kiến thức nền: Cây khung Nhỏ nhất (MST) và Tính chất Lát cắt (Cut Property)

### 1. Vì sao Tham lam lại đúng tuyệt đối trên MST? — Tính chất Lát cắt
- **Định lý Lát cắt (Cut Property):** Chia tập đỉnh $$V$$ thành hai nhóm bất kỳ $$(S, V\setminus S)$$. Cạnh có **trọng số nhỏ nhất** bắc ngang qua hai nhóm đó **chắc chắn thuộc về một cây khung nhỏ nhất**! (Chứng minh bằng phép tráo đổi cạnh: nếu MST không dùng cạnh nhẹ nhất $$e$$, thêm $$e$$ vào tạo chu trình cắt qua lát cắt thêm một cạnh $$e'$$ nặng hơn $$\implies$$ đổi $$e'$$ lấy $$e$$ giảm tổng trọng số!)

### 2. Hai chiến lược Tham lam: Kruskal (theo cạnh) vs. Prim (theo đỉnh)
- **Kruskal:** Sắp xếp mọi cạnh tăng dần theo trọng số; lần lượt nhặt cạnh nhỏ nhất **không tạo chu trình** (kiểm tra cực nhanh trong $$O(\alpha(V))$$ bằng cấu trúc **Disjoint Set Union — DSU**). Tổng thời gian: $$O(E \log E)$$, cực mạnh trên **đồ thị thưa**!
- **Prim:** Xuất phát từ 1 đỉnh gốc, mỗi bước mở rộng cây bằng cạnh nhẹ nhất nối từ cây hiện tại sang đỉnh chưa thăm (dùng **Min-Heap**). Tổng thời gian: $$O(E \log V)$$ (hoặc $$O(V^2)$$ trên đồ thị dày đặc).

## Ví dụ tính tay cầm tay chỉ việc: Chạy Kruskal trên đồ thị 4 đỉnh $$A, B, C, D$$

Cho đồ thị vô hướng 4 đỉnh với 5 cạnh có trọng số:
$$(A, B) = 1,\quad (B, C) = 2,\quad (A, C) = 3,\quad (C, D) = 4,\quad (B, D) = 5.$$
Ta cần chọn đúng $$V - 1 = 3$$ cạnh theo thứ tự trọng số tăng dần:
1. Xét $$(A, B) = 1$$: $$A$$ và $$B$$ ở hai tập rời nhau $$\implies$$ **CHỌN** (nhóm: $$\{A,B\}, \{C\}, \{D\}$$).
2. Xét $$(B, C) = 2$$: $$B$$ và $$C$$ ở hai tập rời nhau $$\implies$$ **CHỌN** (nhóm: $$\{A,B,C\}, \{D\}$$).
3. Xét $$(A, C) = 3$$: $$A$$ và $$C$$ đã chung nhóm $$\{A,B,C\}$$ (thêm vào sẽ tạo chu trình $$A-B-C$$!) $$\implies$$ **BỎ QUA**!
4. Xét $$(C, D) = 4$$: $$C$$ và $$D$$ ở hai tập rời nhau $$\implies$$ **CHỌN** (nhóm: $$\{A,B,C,D\}$$).

Đủ $$3$$ cạnh $$\implies$$ **DỪNG!** MST gồm $$\{(A,B), (B,C), (C,D)\}$$ với tổng trọng số tối ưu bằng **$$1 + 2 + 4 = 7$$**!

### Khung giải thích: Phân biệt rạch ròi Cây MST với Cây Đường đi ngắn nhất (Dijkstra) (nên đọc chậm)

#### Bước 1: Đừng nhầm MST với Dijkstra!
MST tối ưu **tổng chi phí toàn bộ mạng cáp**, không hề cam kết đường đi từ $$A$$ đến $$D$$ là ngắn nhất! (Ví dụ tam giác cạnh $$5, 5, 8$$: MST dùng hai cạnh $$5+5=10$$ nên đường giữa hai đỉnh kia dài $$10$$ thay vì cạnh trực tiếp $$8$$!)

#### Bước 2: Dùng DSU (Path Compression + Union by Rank) cho Kruskal
Nhờ DSU, kiểm tra chu trình tốn gần như $$O(1)$$ mỗi cạnh; nút thắt duy nhất của Kruskal là bước sắp xếp cạnh $$O(E\log E)$$.

#### Bước 3: Xử lý cạnh trọng số trùng nhau
Nếu mọi trọng số đôi một khác nhau, MST là **duy nhất**. Nếu có cạnh bằng nhau, có thể có nhiều MST khác nhau nhưng **tổng trọng số nhỏ nhất luôn duy nhất**!

#### Bước 4: Ứng dụng ngoài hạ tầng mạng — Gom cụm (Single-Linkage Clustering)
Chạy Kruskal dừng sớm trước $$k - 1$$ cạnh cuối cùng sẽ tự động chia dữ liệu thành đúng $$k$$ cụm có khoảng cách liên cụm lớn nhất!

$$
\text{Đồ thị có trọng số }G=(V,E,w)
\;\xrightarrow{\;\text{Cut Property}\;}\;
\begin{cases}
\text{Kruskal + DSU: } O(E\log E) \\
\text{Prim + Heap: } O(E\log V)
\end{cases}
\;\implies\;
\text{MST tối ưu toàn cục}.
$$

## Cây khung và MST

Nhắc lại: **cây khung** của đồ thị liên thông $$G$$ là một cây con chứa tất cả các đỉnh của $$G$$.

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho đồ thị vô hướng **liên thông** $$G=(V,E)$$ với trọng số $$w(e)$$ trên mỗi cạnh. **Cây khung nhỏ nhất** (MST) là một cây khung $$T\subseteq E$$ sao cho tổng trọng số

$$
\sum_{e\in T} w(e)
$$

đạt giá trị **nhỏ nhất** trong số mọi cây khung của $$G$$.

</div>

Nếu trọng số của các cạnh đôi một khác nhau thì MST là **duy nhất**. Khi có các cạnh trùng trọng số, đồ thị có thể có nhiều MST khác nhau nhưng có cùng tổng trọng số.

<div class="textbook-theorem" markdown="1">

**Định lý** (Tính chất lát cắt / *cut property*). Xét một phân hoạch bất kỳ $$V = S \cup (V\setminus S)$$ với $$S \neq \emptyset$$ và $$S \neq V$$. Nếu $$e$$ là cạnh có trọng số **nhỏ nhất** nối một đỉnh thuộc $$S$$ với một đỉnh ngoài $$S$$, thì tồn tại ít nhất một MST chứa cạnh $$e$$.

</div>

Nhờ tính chất lát cắt, một chiến lược tham lam luôn chọn cạnh “an toàn” theo từng lát cắt hoặc theo thứ tự trọng số tăng dần toàn cục vẫn đảm bảo tìm ra MST tối ưu.

## Thuật toán Kruskal

1. Sắp xếp tất cả các cạnh theo trọng số **tăng dần**.
2. Khởi tạo rừng ban đầu gồm các cây đơn lẻ: mỗi đỉnh là một thành phần riêng (quản lý bằng Union–Find).
3. Duyệt lần lượt từng cạnh $$(u,v)$$: nếu $$u$$ và $$v$$ thuộc **hai thành phần khác nhau**, **thêm** cạnh vào MST và **hợp nhất** hai thành phần; nếu đã cùng thành phần thì **bỏ qua** để tránh tạo chu trình.
4. Dừng khi đã chọn đủ $$\vert V\vert -1$$ cạnh.

**Độ phức tạp:** bước sắp xếp tốn $$O(E\log E)$$, còn các thao tác Union–Find (với nén đường đi và hợp nhất theo hạng) tốn gần như tuyến tính $$O(E\,\alpha(V))$$.

<div class="interactive-demo" markdown="1">
<div data-demo="kruskal-algorithm"></div>
</div>
<script src="{{ '/public/js/kruskal-algorithm.js' | relative_url }}"></script>

## Thuật toán Prim

1. Chọn một đỉnh xuất phát $$s$$ và khởi tạo tập đỉnh đã phủ $$S=\{s\}$$.
2. Lặp cho đến khi $$\vert S\vert =\vert V\vert $$: chọn cạnh **nhẹ nhất** nối một đỉnh trong $$S$$ với một đỉnh ngoài $$S$$; thêm cạnh đó vào MST và bổ sung đỉnh mới vào $$S$$.
3. Cấu trúc dữ liệu hỗ trợ: hàng đợi ưu tiên (binary heap hoặc Fibonacci heap).

**Độ phức tạp:** với binary heap, thuật toán có độ phức tạp $$O(E\log V)$$.

| Tiêu chí | Kruskal | Prim |
|:---|:---|:---|
| Chiến lược tham lam | Xét cạnh toàn cục (đã sắp xếp) | Xét cạnh đi ra khỏi tập $$S$$ |
| Cấu trúc dữ liệu | Union–Find | Hàng đợi ưu tiên (*priority queue*) |
| Thường phù hợp | Đồ thị **thưa** | Đồ thị **dày** hoặc mở rộng từ một gốc |

Dùng minh họa đồ thị dưới đây (chọn **Kruskal** hoặc **Prim**, điều chỉnh trọng số và chạy từng bước) để quan sát cạnh nào được thêm vào MST và cạnh nào bị loại vì tạo chu trình:

<div class="interactive-demo" markdown="1">
<div data-demo="graph-explainer" data-algorithm="kruskal"></div>
</div>
<script src="{{ '/public/js/explainers/graph-explainer.js' | relative_url }}"></script>

### Minh họa Prim: mở rộng dần từ một đỉnh

Minh họa riêng cho thuật toán Prim để đối chiếu với Kruskal ở trên: tập $$S$$ lớn dần từ đỉnh xuất phát, ở mỗi bước chọn cạnh nhẹ nhất đi ra khỏi $$S$$.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-explainer" data-algorithm="prim"></div>
</div>

### Video ngắn: Kruskal và Prim

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/mst-kruskal-prim.mp4"></video>
</div>

Video dài khoảng 2 phút 50 giây: chạy lần lượt Kruskal và Prim trên cùng một đồ thị 6 đỉnh, chỉ rõ các cạnh bị loại do tạo chu trình, xác nhận cả hai thuật toán cùng tạo ra cây khung tổng trọng số 20 và giải thích tính tối ưu bằng tính chất lát cắt cùng phép đổi cạnh.

## Ví dụ tính tay

<div class="textbook-example" markdown="1">

**Ví dụ.** Cho đồ thị gồm 4 đỉnh $$A,B,C,D$$ với các cạnh:  
$$(A,B,1)$$, $$(B,D,2)$$, $$(A,D,4)$$, $$(B,C,5)$$, $$(C,D,6)$$.

Chạy thuật toán Kruskal: chọn $$AB(1)$$, chọn $$BD(2)$$, bỏ qua $$AD(4)$$ (vì $$A$$ và $$D$$ đã cùng thành phần $$A$$–$$B$$–$$D$$), sau đó chọn $$BC(5)$$.  
Cây khung nhỏ nhất thu được là $$\{AB,BD,BC\}$$ với tổng trọng số $$1+2+5=8$$.

</div>

## Ứng dụng

- Thiết kế mạng LAN hoặc hệ thống đường dây nhằm đảm bảo liên thông với chi phí thấp nhất.
- Phân cụm dữ liệu (*clustering*) sơ cấp bằng cách bỏ đi các cạnh nặng nhất trong MST để tách thành các cụm.
- Làm bước khởi tạo cho thuật toán xấp xỉ ở một số bài toán mạng nâng cao.

**Lưu ý phân biệt với đường đi ngắn nhất (Dijkstra):** MST tối ưu tổng chi phí của toàn bộ cây, nên không đảm bảo đường đi trên MST giữa hai đỉnh $$s$$ và $$t$$ là đường đi ngắn nhất.

## Bài tập

### Bài tập 1

Trong ví dụ tính tay ở trên, tổng trọng số MST là bao nhiêu? Nếu đổi trọng số cạnh $$BC$$ thành 6 và cạnh $$CD$$ thành 5 thì MST thay đổi thế nào và tổng trọng số bằng bao nhiêu?

<details>
<summary>Đáp án</summary>

Tổng trọng số MST ban đầu là **8**. Khi đổi $$BC=6$$ và $$CD=5$$, Kruskal sẽ chọn các cạnh $$AB, BD, CD$$ với tổng trọng số $$1+2+5=8$$. Tập cạnh của MST thay đổi nhưng tổng trọng số tối ưu vẫn bằng 8.

</details>

### Bài tập 2

Vì sao thuật toán Kruskal loại bỏ các cạnh tạo thành chu trình?

<details>
<summary>Đáp án</summary>

Một cây khung có đúng $$\vert V\vert -1$$ cạnh và không được chứa chu trình. Cạnh nối hai đỉnh đã thuộc cùng một thành phần liên thông sẽ tạo ra chu trình và không giúp kết nối thêm đỉnh mới nào cho rừng đang xây dựng.

</details>

### Bài tập 3

MST của một đồ thị liên thông gồm $$n$$ đỉnh có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

Có đúng $$n-1$$ cạnh.

</details>

### Bài tập 4

Một đồ thị không liên thông có MST hay không?

<details>
<summary>Đáp án</summary>

Không, vì theo định nghĩa MST phải phủ tất cả các đỉnh bằng **một** cây duy nhất. Với đồ thị không liên thông, ta tìm **rừng khung nhỏ nhất** gồm các MST trên từng thành phần liên thông.

</details>

## Tóm tắt

1. **MST** là cây khung có tổng trọng số cạnh nhỏ nhất trên đồ thị vô hướng liên thông.
2. **Tính chất lát cắt (*cut property*)** là cơ sở chứng minh tính đúng đắn của các thuật toán tham lam tìm MST.
3. **Kruskal** dùng sắp xếp cạnh và Union–Find; **Prim** mở rộng tập đỉnh $$S$$ bằng hàng đợi ưu tiên.
4. MST ứng dụng trong thiết kế mạng và phân cụm, khác về mục tiêu tối ưu so với bài toán đường đi ngắn nhất.

Trong bài tùy chọn tiếp theo, ta sẽ tìm hiểu **mã hóa Huffman** và **cây tìm kiếm nhị phân (BST)**.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=4ZlRH0eK-qQ">3.5 Prims and Kruskals Algorithms - Greedy Method</a> — Abdul Bari, tiếng Anh. Trình bày tổng quan thuật toán Prim và Kruskal cho bài toán cây khung nhỏ nhất.
- <a href="https://www.youtube.com/watch?v=cplfcGZmX7I">Prim&#x27;s algorithm in 2 minutes</a> — Michael Sambol, tiếng Anh. Minh họa nhanh thuật toán Prim trên ví dụ ngắn.
- <a href="https://www.youtube.com/watch?v=71UQH7Pr9kU">Kruskal&#x27;s algorithm in 2 minutes</a> — Michael Sambol, tiếng Anh. Minh họa nhanh thuật toán Kruskal để đối chiếu với Prim.
