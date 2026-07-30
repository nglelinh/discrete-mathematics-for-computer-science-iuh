---
layout: post
title: "Biểu diễn Đồ thị"
categories: chapter12
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Ma trận kề và danh sách kề: xây dựng, độ phức tạp kiểm tra cạnh và duyệt láng giềng, lựa chọn theo đồ thị thưa hay dày."
---

<div class="textbook-epigraph" markdown="1">

"Data structures are not an implementation detail of graphs — they are the graphs that algorithms actually see."

<span class="epigraph-attribution">— Tinh thần cấu trúc dữ liệu đồ thị</span>

</div>

Ở mục trước, đồ thị được định nghĩa trừu tượng dưới dạng $$G = (V, E)$$. Để thuật toán chạy được, cấu trúc đó phải được **lưu trữ** và **truy vấn** trên máy tính. Hai biểu diễn chuẩn là **ma trận kề** (*adjacency matrix*) và **danh sách kề** (*adjacency list*). Chúng mã hóa cùng thông tin kề, nhưng khác nhau về bộ nhớ và thời gian các thao tác — kiểm tra có cạnh hay không, liệt kê láng giềng, duyệt toàn bộ đồ thị.

Mục này xây dựng hai biểu diễn, so sánh độ phức tạp, và nêu nguyên tắc chọn theo mật độ cạnh.

![Ma trận kề và danh sách kề](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_adjacency_matrix_list.svg)

<p class="textbook-figure-caption" data-figure="12.5">Cùng một đồ thị bốn đỉnh: ma trận $$n\times n$$ và danh sách các láng giềng theo từng đỉnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** ma trận kề cho đồ thị vô hướng, có hướng và có trọng số.
- **Xây dựng** danh sách kề tương ứng.
- **So sánh** chi phí kiểm tra cạnh, duyệt láng giềng và bộ nhớ.
- **Chọn** biểu diễn phù hợp đồ thị thưa (*sparse*) hay dày (*dense*).

**Từ khóa**: ma trận kề (adjacency matrix), danh sách kề (adjacency list), đồ thị thưa (sparse), đồ thị dày (dense).

</div>

## 1. Ma trận kề

Giả sử các đỉnh được đánh số $$0, 1, \ldots, n-1$$ với $$n = |V|$$.

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Ma trận kề** của $$G$$ là ma trận $$A$$ kích thước $$n \times n$$ xác định bởi

$$
A[i][j] =
\begin{cases}
1 & \text{nếu } (i,j) \in E \text{ (hoặc } \{i,j\} \in E \text{ khi vô hướng)}, \\
0 & \text{ngược lại}.
\end{cases}
$$

Với đồ thị **có trọng số**, thay $$1$$ bằng trọng số $$w(i,j)$$ (và quy ước một giá trị đặc biệt, ví dụ $$0$$ hoặc $$\infty$$, cho cặp không có cạnh — tùy bài toán).

</div>

Tính chất trực tiếp:

- Đồ thị **vô hướng** $$\implies$$ $$A$$ **đối xứng**: $$A[i][j] = A[j][i]$$.
- Đồ thị **không khuyên** $$\implies$$ đường chéo toàn $$0$$.
- Với đồ thị vô hướng đơn, $$\deg(i) = \sum_{j=0}^{n-1} A[i][j]$$ (tổng hàng $$i$$).

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Đồ thị vô hướng bốn đỉnh với cạnh $$\{0,1\}$$, $$\{0,2\}$$, $$\{1,2\}$$, $$\{2,3\}$$:

|  | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 0 | 1 | 0 |
| **2** | 1 | 1 | 0 | 1 |
| **3** | 0 | 0 | 1 | 0 |

Ma trận đối xứng; $$\deg(2) = 3$$ bằng tổng hàng 2.

</div>

| Thao tác | Độ phức tạp (ma trận kề) |
|:---|:---|
| Kiểm tra có cạnh $$(i,j)$$ | $$O(1)$$ |
| Liệt kê mọi láng giềng của $$i$$ | $$O(n)$$ (duyệt cả hàng) |
| Bộ nhớ | $$O(n^2)$$ |

## 2. Danh sách kề

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Danh sách kề** là một bảng (mảng hoặc map) gồm $$n$$ mục; mục thứ $$i$$ chứa danh sách các đỉnh $$j$$ sao cho $$(i,j) \in E$$ (hoặc các cặp $$(j,w)$$ nếu cạnh mang trọng số).

</div>

Với đồ thị vô hướng, mỗi cạnh $$\{u,v\}$$ xuất hiện hai lần: $$v$$ trong danh sách của $$u$$ và $$u$$ trong danh sách của $$v$$.

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Cùng đồ thị Ví dụ 1:

```python
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2],
}
```

Tổng độ dài các danh sách bằng $$2|E| = 8$$ trên đồ thị vô hướng (mỗi cạnh được lưu hai chiều).

</div>

| Thao tác | Độ phức tạp (danh sách kề) |
|:---|:---|
| Kiểm tra có cạnh $$(i,j)$$ | $$O(\deg(i))$$ (duyệt list của $$i$$; hoặc $$O(1)$$ trung bình nếu dùng set) |
| Duyệt láng giềng của $$i$$ | $$O(\deg(i))$$ |
| Bộ nhớ | $$O(n + m)$$ với $$m = |E|$$ (vô hướng: $$O(n + 2m)$$ chỗ lưu chiều) |

## 3. So sánh và nguyên tắc chọn

| Tiêu chí | Ma trận kề | Danh sách kề |
|:---|:---|:---|
| Bộ nhớ | $$O(n^2)$$ — cố định theo số đỉnh | $$O(n+m)$$ — tỉ lệ số cạnh |
| Kiểm tra cạnh | $$O(1)$$ | $$O(\deg)$$ |
| Duyệt toàn bộ cạnh (BFS/DFS) | Phải quét tới $$O(n^2)$$ ô | Chỉ đi đúng các cạnh: $$O(n+m)$$ |
| Đồ thị $$n = 10^6$$, $$m \approx 3\cdot 10^6$$ | Hàng terabyte — không khả thi | Cỡ chục megabyte + overhead |
| Thuật toán kiểu nhân ma trận | Tự nhiên trên $$A$$ (hoặc CSR thưa) | Cần chuyển đổi |

<div class="textbook-definition" markdown="1">

**Định nghĩa** (mật độ). Đồ thị được gọi là **dày** khi $$m$$ cùng bậc với $$n^2$$ (ví dụ gần $$K_n$$). Đồ thị **thưa** khi $$m \ll n^2$$ — điển hình $$m = O(n)$$ hoặc $$O(n \log n)$$ như nhiều mạng thực tế.

</div>

**Nguyên tắc chọn.**

1. Đồ thị **thưa** (mạng xã hội, web, dependency quy mô lớn) → **danh sách kề** là lựa chọn mặc định.
2. Đồ thị **dày** hoặc thuật toán cần kiểm tra cạnh liên tục theo chỉ số $$(i,j)$$ → ma trận kề có thể hợp lý khi $$n$$ nhỏ (vài nghìn đỉnh).
3. BFS, DFS, Dijkstra trên đồ thị lớn gần như luôn giả định danh sách kề để đạt $$O(n+m)$$ hoặc $$O(m + n\log n)$$.

<div class="textbook-example" markdown="1">

**Ví dụ 3** (ước lượng bộ nhớ). Giả sử mỗi phần tử ma trận 1 byte và mỗi entry danh sách kề khoảng 8 byte (chỉ số đỉnh).

- Ma trận: $$n=10^4$$ $$\implies$$ khoảng $$100$$ MB; $$n=10^6$$ $$\implies$$ khoảng $$1$$ TB.
- Danh sách với $$m=3\cdot 10^6$$ cạnh vô hướng: khoảng $$2m$$ entry $$\approx 48$$ MB cộng mảng con trỏ $$n$$ — vẫn trong tầm máy trạm.

</div>

## 4. Biến thể và lưu ý triển khai

- **Digraph**: danh sách kề chỉ lưu cạnh ra; nếu cần cạnh vào, có thể giữ thêm *in-list* hoặc xây từ cạnh ra khi tiền xử lý.
- **Đa đồ thị / khuyên**: ma trận có thể lưu số cạnh thay vì bit 0/1; danh sách lưu lặp hoặc cấu trúc có bội số.
- **Ma trận thưa** (CSR, CSC): trung gian giữa hai cực — lưu hiệu quả gần danh sách kề nhưng vẫn hỗ trợ phép nhân ma trận–vector (PageRank, phổ đồ thị).
- **Thứ tự đỉnh**: đánh số $$0..n-1$$ là quy ước thuật toán; map từ nhãn thực (tên module, user id) sang chỉ số là bước tiền xử lý.

```python
def has_edge_matrix(A, u, v):
    return A[u][v] != 0  # O(1)

def has_edge_adj_list(graph, u, v):
    return v in graph.get(u, [])  # O(deg(u)) với list
```

## 5. Thử nghiệm tương tác

Xây ma trận kề bằng cách bật/tắt cạnh; so sánh với danh sách kề suy ra từ các hàng khác 0.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-adjacency-builder"></div>
</div>
<script src="{{ '/public/js/graph-adjacency-builder.js' | relative_url }}"></script>


## Bài tập

### Bài tập 1

Viết ma trận kề cho đồ thị có hướng với các cạnh $$(0,1)$$, $$(1,2)$$, $$(2,0)$$, $$(2,3)$$.

<details>
<summary>Đáp án</summary>

$$
A =
\begin{bmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Các vị trí khác bằng 0. Ma trận **không** đối xứng.

</details>

### Bài tập 2

Đồ thị $$n$$ đỉnh, $$m$$ cạnh. Bỏ qua hằng số, khi nào danh sách kề tiết kiệm bộ nhớ hơn ma trận kề?

<details>
<summary>Đáp án</summary>

Khi $$O(n+m)$$ nhỏ hơn $$O(n^2)$$ theo bậc lớn, tức $$m \ll n^2$$ — đồ thị thưa. Thực tế còn phụ thuộc kích thước từng phần tử lưu trữ, nhưng ngưỡng định tính là mật độ cạnh.

</details>

### Bài tập 3

Cho danh sách kề vô hướng:

```text
0: 1, 2
1: 0, 2, 3
2: 0, 1
3: 1
```

(a) Viết ma trận kề. (b) Tính $$\deg(1)$$. (c) Ước lượng chi phí liệt kê láng giềng của mọi đỉnh bằng từng biểu diễn.

<details>
<summary>Đáp án</summary>

(a)

|  | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 0 | 0 |
| 3 | 0 | 1 | 0 | 0 |

(b) $$\deg(1) = 3$$.

(c) Danh sách kề: tổng thời gian $$O(n+m) = O(4+4)$$ (đếm cạnh vô hướng $$m=4$$). Ma trận: $$O(n^2)=O(16)$$ vì mỗi hàng duyệt đủ 4 cột.

</details>

### Bài tập 4

Cài đặt `neighbors(graph, u)` cho danh sách kề và nêu độ phức tạp khi sau đó duyệt in mọi láng giềng.

<details>
<summary>Đáp án</summary>

```python
def neighbors(graph, u):
    return graph.get(u, [])
```

Trả về tham chiếu danh sách: $$O(1)$$. Duyệt in các láng giềng: $$O(\deg(u))$$.

</details>

## Tóm tắt

1. **Ma trận kề** cho phép kiểm tra cạnh $$O(1)$$ với chi phí bộ nhớ $$O(n^2)$$.
2. **Danh sách kề** dùng bộ nhớ $$O(n+m)$$ và duyệt láng giềng đúng bằng bậc — phù hợp đồ thị thưa và BFS/DFS.
3. Việc chọn biểu diễn là quyết định **độ phức tạp**, không chỉ chi tiết cài đặt.
4. Trên digraph và đồ thị có trọng số, cùng hai khuôn mẫu được mở rộng bằng hướng cạnh và cặp $$(j,w)$$.

Trong bài tiếp theo, với biểu diễn đã chọn, ta định nghĩa **đường đi**, **chu trình** và **liên thông** — các khái niệm trả lời câu hỏi “đi từ đâu đến đâu được không?”.
