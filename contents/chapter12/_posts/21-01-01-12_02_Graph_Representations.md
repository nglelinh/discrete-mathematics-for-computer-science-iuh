---
layout: post
title: "Biểu diễn Đồ thị"
categories: chapter12
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Mục 12.2 trình bày hai cách biểu diễn đồ thị trong máy tính — ma trận kề và danh sách kề — cùng so sánh bộ nhớ và độ phức tạp các thao tác cơ bản."
---

Sau khi định nghĩa đồ thị trừu tượng, bước tiếp theo là **cài đặt** trên máy tính. Lựa chọn cấu trúc dữ liệu quyết định thời gian kiểm tra cạnh, duyệt láng giềng và bộ nhớ — đây là quyết định kiến trúc, không chỉ chi tiết triển khai. Mục 12.2 so sánh **ma trận kề** và **danh sách kề**.

![Ma trận kề — đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="12.5">Đồ thị 4 đỉnh — mỗi cấu trúc biểu diễn lưu cùng thông tin nhưng chi phí thao tác khác nhau.</p>
![Hash table — tư duy danh sách kề](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="12.6">Danh sách kề gắn mỗi đỉnh với tập láng giềng — tương tự bucket trong hash table.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** ma trận kề cho đồ thị có hướng / vô hướng / có trọng số.
- **Xây dựng** danh sách kề (adjacency list).
- **So sánh** $$O(1)$$ vs $$O(V)$$ cho kiểm tra cạnh; $$O(V^2)$$ vs $$O(V+E)$$ cho bộ nhớ.
- **Chọn** biểu diễn phù hợp đồ thị thưa hay dày.

**Từ khóa**: ma trận kề (adjacency matrix), danh sách kề (adjacency list), đồ thị thưa (sparse), đồ thị dày (dense).
</div>

## Ma trận kề

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho đồ thị $$G$$ với $$n$$ đỉnh được đánh số $$0, 1, \ldots, n-1$$. **Ma trận kề** $$A$$ là ma trận $$n \times n$$ với:

$$A[i][j] = \begin{cases} 1 & \text{nếu có cạnh } (i,j) \\ 0 & \text{ngược lại} \end{cases}$$

(Có trọng số: $$A[i][j] = w$$ nếu cạnh có trọng số $$w$$.)
</div>

**Đồ thị vô hướng**: Ma trận **đối xứng** ($$A[i][j] = A[j][i]$$).

<div class="textbook-example" markdown="1">
**Ví dụ**: 4 đỉnh, cạnh (0,1), (0,2), (1,2), (2,3):

```
    0 1 2 3
0 [ 0 1 1 0 ]
1 [ 1 0 1 0 ]
2 [ 1 1 0 1 ]
3 [ 0 0 1 0 ]
```
</div>

| Thao tác | Độ phức tạp |
|:---|:---|
| Kiểm tra cạnh $$(i,j)$$ | $$O(1)$$ |
| Liệt kê láng giềng của $$i$$ | $$O(n)$$ |
| Bộ nhớ | $$O(n^2)$$ |

## Danh sách kề

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Danh sách kề** gồm mảng (hoặc map) $$n$$ phần tử; phần tử thứ $$i$$ là danh sách các đỉnh $$j$$ sao cho $$(i,j) \in E$$ (hoặc cặp $$(j, w)$$ nếu có trọng số).
</div>

```python
# Đồ thị vô hướng — danh sách kề
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2],
}
```

| Thao tác | Độ phức tạp |
|:---|:---|
| Kiểm tra cạnh $$(i,j)$$ | $$O(\deg(i))$$ |
| Duyệt láng giềng $$i$$ | $$O(\deg(i))$$ |
| Bộ nhớ | $$O(n + m)$$ với $$m = |E|$$ |

<div class="content-box insight-box textbook-block" markdown="1">
**Chọn cấu trúc**: Đồ thị **dày** ($$m \approx n^2$$) → ma trận kề có thể hợp lý. Đồ thị **thưa** ($$m \ll n^2$$) — social network, web graph — **danh sách kề** là chuẩn công nghiệp.
</div>

## Ma trận kề vs danh sách kề

| Tiêu chí | Ma trận kề | Danh sách kề |
|:---|:---|:---|
| Đồ thị 1M đỉnh, ~3M cạnh | ~1 TB (không khả thi) | ~24 MB cạnh + overhead |
| BFS/DFS | Duyệt hàng/cột chậm hơn | Duyệt chỉ cạnh thật |
| Thuật toán nhân ma trận (PageRank) | Tự nhiên trên ma trận thưa CSR | Chuyển đổi được |

## Bài tập

### Bài tập 1

Viết ma trận kề cho đồ thị có hướng: cạnh (0→1), (1→2), (2→0), (2→3).

<details>
<summary>Đáp án</summary>

```
0→1, 1→2, 2→0, 2→3:
A[0][1]=A[1][2]=A[2][0]=A[2][3]=1, còn lại 0.
```

</details>

### Bài tập 2

Đồ thị $$n$$ đỉnh, $$m$$ cạnh. Khi nào danh sách kề tiết kiệm bộ nhớ hơn ma trận kề (bỏ hằng số)?

<details>
<summary>Đáp án</summary>

Khi $$O(n + m) < O(n^2)$$, tức $$m \ll n^2$$ — đồ thị thưa.

</details>

### Bài tập 3

Cài đặt hàm `has_edge_adj_list(graph, u, v)` và ước lượng độ phức tạp.

<details>
<summary>Đáp án</summary>

```python
def has_edge_adj_list(graph, u, v):
    return v in graph.get(u, [])
```

$$O(\deg(u))$$ — duyệt danh sách láng giềng của $$u$$.

</details>

## Tóm tắt

- **Ma trận kề**: $$O(1)$$ kiểm tra cạnh, $$O(n^2)$$ bộ nhớ.
- **Danh sách kề**: $$O(\deg)$$ kiểm tra, $$O(n+m)$$ bộ nhớ — ưu tiên đồ thị thưa.
- Chọn cấu trúc theo mật độ cạnh và thao tác thuật toán chính.

Trong bài tiếp theo, chúng ta học **đường đi, chu trình và liên thông**.