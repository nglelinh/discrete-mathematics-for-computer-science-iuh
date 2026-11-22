---
layout: post
title: "Biểu diễn Đồ thị"
categories: chapter12
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Ma trận kề và danh sách kề: cách xây dựng, độ phức tạp khi kiểm tra cạnh và duyệt láng giềng, cùng nguyên tắc lựa chọn theo mật độ cạnh."
---

<div class="textbook-epigraph" markdown="1">

"Data structures are not an implementation detail of graphs — they are the graphs that algorithms actually see."

<span class="epigraph-attribution">— Tinh thần cấu trúc dữ liệu đồ thị</span>

</div>

Ở mục trước, đồ thị được định nghĩa trừu tượng dưới dạng $$G = (V, E)$$. Để thuật toán có thể xử lý, cấu trúc này cần được **lưu trữ** và **truy vấn** trong bộ nhớ máy tính. Hai cách biểu diễn tiêu chuẩn là **ma trận kề** (*adjacency matrix*) và **danh sách kề** (*adjacency list*). Cả hai cùng mã hóa thông tin về quan hệ kề, nhưng khác nhau rõ rệt về chi phí bộ nhớ và thời gian thực hiện các thao tác cơ bản như kiểm tra cạnh, liệt kê láng giềng hay duyệt toàn bộ đồ thị.

Bài học này trình bày cách xây dựng hai biểu diễn, so sánh độ phức tạp và nêu nguyên tắc lựa chọn tùy theo mật độ cạnh.

![Ma trận kề và danh sách kề](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_adjacency_matrix_list.svg)

<p class="textbook-figure-caption" data-figure="12.5">Cùng một đồ thị 4 đỉnh biểu diễn bằng ma trận $$n\times n$$ và bằng danh sách láng giềng của từng đỉnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** ma trận kề cho đồ thị vô hướng, có hướng và có trọng số.
- **Xây dựng** danh sách kề tương ứng.
- **So sánh** chi phí kiểm tra cạnh, duyệt láng giềng và dung lượng bộ nhớ của hai biểu diễn.
- **Lựa chọn** biểu diễn phù hợp cho đồ thị thưa (*sparse*) và đồ thị dày (*dense*).

**Từ khóa**: ma trận kề (adjacency matrix), danh sách kề (adjacency list), đồ thị thưa (sparse), đồ thị dày (dense).

</div>

## Ma trận kề

Giả sử các đỉnh được đánh số từ $$0, 1, \ldots, n-1$$ với $$n = \vert V\vert $$.

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Ma trận kề** của $$G$$ là ma trận $$A$$ kích thước $$n \times n$$ xác định bởi:

$$
A[i][j] =
\begin{cases}
1 & \text{nếu } (i,j) \in E \text{ (hoặc } \{i,j\} \in E \text{ khi vô hướng)}, \\
0 & \text{ngược lại}.
\end{cases}
$$

Với đồ thị **có trọng số**, giá trị $$1$$ được thay bằng trọng số $$w(i,j)$$, còn cặp đỉnh không có cạnh được quy ước bằng một giá trị đặc biệt (ví dụ $$0$$ hoặc $$\infty$$ tùy bài toán).

</div>

Một số tính chất trực tiếp của ma trận kề:

- Với đồ thị **vô hướng**, $$A$$ là ma trận **đối xứng**: $$A[i][j] = A[j][i]$$.
- Với đồ thị **không có khuyên**, đường chéo chính gồm toàn số $$0$$.
- Với đồ thị vô hướng đơn, $$\deg(i) = \sum_{j=0}^{n-1} A[i][j]$$ (tổng các phần tử trên hàng $$i$$).

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Xét đồ thị vô hướng 4 đỉnh với các cạnh $$\{0,1\}$$, $$\{0,2\}$$, $$\{1,2\}$$, $$\{2,3\}$$:

|  | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 0 | 1 | 0 |
| **2** | 1 | 1 | 0 | 1 |
| **3** | 0 | 0 | 1 | 0 |

Ma trận đối xứng qua đường chéo chính, và $$\deg(2) = 3$$ bằng tổng hàng 2.

</div>

| Thao tác | Độ phức tạp (ma trận kề) |
|:---|:---|
| Kiểm tra có cạnh $$(i,j)$$ | $$O(1)$$ |
| Liệt kê mọi láng giềng của $$i$$ | $$O(n)$$ (phải duyệt toàn bộ hàng $$i$$) |
| Bộ nhớ | $$O(n^2)$$ |

## Danh sách kề

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Danh sách kề** là một mảng (hoặc bảng ánh xạ) gồm $$n$$ mục; mục thứ $$i$$ lưu danh sách các đỉnh $$j$$ sao cho $$(i,j) \in E$$ (hoặc các cặp $$(j,w)$$ nếu cạnh có trọng số).

</div>

Với đồ thị vô hướng, mỗi cạnh $$\{u,v\}$$ được lưu hai lần: $$v$$ nằm trong danh sách của $$u$$ và $$u$$ nằm trong danh sách của $$v$$.

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Với cùng đồ thị ở Ví dụ 1, danh sách kề trong Python là:

```python
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2],
}
```

Tổng độ dài tất cả các danh sách bằng $$2\vert E\vert  = 8$$ do mỗi cạnh vô hướng được lưu ở cả hai đầu mút.

</div>

| Thao tác | Độ phức tạp (danh sách kề) |
|:---|:---|
| Kiểm tra có cạnh $$(i,j)$$ | $$O(\deg(i))$$ (duyệt danh sách của $$i$$; hoặc $$O(1)$$ trung bình nếu dùng tập băm) |
| Duyệt láng giềng của $$i$$ | $$O(\deg(i))$$ |
| Bộ nhớ | $$O(n + m)$$ với $$m = \vert E\vert $$ (đồ thị vô hướng dùng $$O(n + 2m)$$ đơn vị lưu trữ) |

## So sánh và nguyên tắc chọn

| Tiêu chí | Ma trận kề | Danh sách kề |
|:---|:---|:---|
| Bộ nhớ | $$O(n^2)$$ — cố định theo số đỉnh | $$O(n+m)$$ — tỉ lệ với số đỉnh và số cạnh |
| Kiểm tra cạnh | $$O(1)$$ | $$O(\deg)$$ |
| Duyệt toàn bộ đồ thị (BFS/DFS) | Quét tới $$O(n^2)$$ ô | Chỉ xét đúng các cạnh hiện có: $$O(n+m)$$ |
| Đồ thị $$n = 10^6$$, $$m \approx 3\cdot 10^6$$ | Hàng terabyte — không khả thi | Cỡ vài chục megabyte cộng chi phí quản lý |
| Thuật toán dựa trên nhân ma trận | Tự nhiên trên $$A$$ (hoặc dạng thưa CSR) | Cần chuyển đổi biểu diễn |

<div class="textbook-definition" markdown="1">

**Định nghĩa** (mật độ). Đồ thị được gọi là **dày** (*dense*) khi $$m$$ cùng bậc với $$n^2$$ (chẳng hạn gần với $$K_n$$), và là **thưa** (*sparse*) khi $$m \ll n^2$$ — thường gặp $$m = O(n)$$ hoặc $$O(n \log n)$$ trong các mạng thực tế.

</div>

**Nguyên tắc chọn.**

1. Với đồ thị **thưa** (mạng xã hội, liên kết web, đồ thị phụ thuộc quy mô lớn), **danh sách kề** là lựa chọn mặc định.
2. Với đồ thị **dày** hoặc thuật toán cần kiểm tra cạnh liên tục theo chỉ số $$(i,j)$$, ma trận kề tỏ ra phù hợp khi $$n$$ nhỏ (vài nghìn đỉnh).
3. Các thuật toán như BFS, DFS hay Dijkstra trên đồ thị lớn hầu như luôn dùng danh sách kề để đạt độ phức tạp $$O(n+m)$$ hoặc $$O(m + n\log n)$$.

<div class="textbook-example" markdown="1">

**Ví dụ 3** (ước lượng bộ nhớ). Giả sử mỗi phần tử ma trận chiếm 1 byte và mỗi phần tử trong danh sách kề chiếm khoảng 8 byte (chỉ số đỉnh).

- Ma trận kề: khi $$n=10^4$$ cần khoảng $$100$$ MB; khi $$n=10^6$$ cần khoảng $$1$$ TB.
- Danh sách kề với $$m=3\cdot 10^6$$ cạnh vô hướng: khoảng $$2m$$ phần tử $$\approx 48$$ MB cộng mảng con trỏ kích thước $$n$$ — hoàn toàn khả thi trên máy trạm thông thường.

</div>

## Biến thể và lưu ý triển khai

- **Đồ thị có hướng (Digraph)**: danh sách kề mặc định chỉ lưu các cạnh ra; nếu cần truy vấn cạnh vào, ta có thể duy trì thêm *in-list* hoặc xây dựng từ danh sách cạnh ra ở bước tiền xử lý.
- **Đa đồ thị và khuyên**: ma trận kề có thể lưu số lượng cạnh thay vì chỉ 0/1; danh sách kề có thể cho phép lặp phần tử hoặc lưu kèm bội số.
- **Ma trận thưa** (CSR, CSC): là dạng trung gian, tiết kiệm bộ nhớ tương đương danh sách kề nhưng vẫn hỗ trợ tốt phép nhân ma trận–vector (như trong PageRank hay lý thuyết phổ đồ thị).
- **Đánh số đỉnh**: chỉ số $$0..n-1$$ là quy ước phục vụ thuật toán; ánh xạ giữa nhãn thực tế (tên mô-đun, mã người dùng) và chỉ số nguyên thường được thực hiện ở bước tiền xử lý.

```python
def has_edge_matrix(A, u, v):
    return A[u][v] != 0  # O(1)

def has_edge_adj_list(graph, u, v):
    return v in graph.get(u, [])  # O(deg(u)) với list
```

## Thử nghiệm tương tác

Xây dựng ma trận kề bằng cách bật/tắt các cạnh, sau đó đối chiếu với danh sách kề suy ra từ các vị trí khác 0 trên từng hàng.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-adjacency-builder"></div>
</div>
<script src="{{ '/public/js/graph-adjacency-builder.js' | relative_url }}"></script>


## Bài tập

### Bài tập 1

Viết ma trận kề cho đồ thị có hướng gồm 4 đỉnh $$0, 1, 2, 3$$ với các cạnh $$(0,1)$$, $$(1,2)$$, $$(2,0)$$, $$(2,3)$$.

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

Các vị trí không có cạnh đều bằng 0. Do đồ thị có hướng nên ma trận **không** đối xứng.

</details>

### Bài tập 2

Với đồ thị có $$n$$ đỉnh và $$m$$ cạnh (bỏ qua hằng số), khi nào danh sách kề tiết kiệm bộ nhớ hơn ma trận kề?

<details>
<summary>Đáp án</summary>

Khi $$O(n+m)$$ nhỏ hơn $$O(n^2)$$ về bậc tăng trưởng, tức là $$m \ll n^2$$ (đồ thị thưa). Trên thực tế, ngưỡng chuyển đổi cụ thể còn phụ thuộc kích thước mỗi phần tử lưu trữ, nhưng yếu tố quyết định vẫn là mật độ cạnh.

</details>

### Bài tập 3

Cho danh sách kề của một đồ thị vô hướng:

```text
0: 1, 2
1: 0, 2, 3
2: 0, 1
3: 1
```

(a) Viết ma trận kề. (b) Tính $$\deg(1)$$. (c) Ước lượng chi phí liệt kê láng giềng của tất cả các đỉnh theo từng biểu diễn.

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

(c) Với danh sách kề, tổng thời gian là $$O(n+m) = O(4+4)$$ (số cạnh vô hướng $$m=4$$). Với ma trận kề, chi phí là $$O(n^2)=O(16)$$ vì mỗi hàng đều phải duyệt đủ 4 cột.

</details>

### Bài tập 4

Cài đặt hàm `neighbors(graph, u)` trên danh sách kề và nêu độ phức tạp khi duyệt in tất cả láng giềng của đỉnh `u`.

<details>
<summary>Đáp án</summary>

```python
def neighbors(graph, u):
    return graph.get(u, [])
```

Thao tác trả về tham chiếu đến danh sách mất $$O(1)$$; việc duyệt và in toàn bộ láng giềng mất $$O(\deg(u))$$.

</details>

## Tóm tắt

1. **Ma trận kề** cho phép kiểm tra cạnh trong $$O(1)$$ với chi phí bộ nhớ $$O(n^2)$$.
2. **Danh sách kề** chiếm bộ nhớ $$O(n+m)$$ và duyệt láng giềng tỉ lệ với bậc đỉnh, phù hợp cho đồ thị thưa và các thuật toán duyệt như BFS/DFS.
3. Lựa chọn biểu diễn ảnh hưởng trực tiếp đến **độ phức tạp thuật toán**, không chỉ là chi tiết cài đặt.
4. Với đồ thị có hướng và có trọng số, cả hai biểu diễn đều mở rộng tự nhiên bằng cách giữ đúng hướng cạnh và lưu thêm cặp $$(j,w)$$.

Trong bài tiếp theo, ta sẽ định nghĩa **đường đi**, **chu trình** và **tính liên thông** — những khái niệm trả lời câu hỏi khả năng kết nối giữa các đỉnh trong đồ thị.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=5hPfm_uqXmw">6.1 Graph Representation in Data Structure(Graph Theory)|Adjacency Matrix and Adjacency List</a> — Jenny&#x27;s Lectures CS IT, tiếng Anh. Giới thiệu ma trận kề và danh sách kề.
- <a href="https://www.youtube.com/watch?v=7AhHGp7EzZ8">Graph Representation with an Adjacency Matrix | Graph Theory, Adjaceny Matrices</a> — Wrath of Math, tiếng Anh. Minh họa cách lập ma trận kề từ một đồ thị cho trước.
- <a href="https://www.youtube.com/watch?v=ze-poffnS1E">Adjacency Matrix versus Adjacency List</a> — Professor Kevin Wortman, tiếng Anh. So sánh khi nào nên dùng ma trận kề và khi nào nên dùng danh sách kề.
