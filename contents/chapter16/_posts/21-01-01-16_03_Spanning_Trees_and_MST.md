---
layout: post
title: "Cây khung và Cây khung Nhỏ nhất"
categories: chapter16
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Cây khung; MST; tính chất greedy; Kruskal (Union-Find) và Prim (priority queue); độ phức tạp và ứng dụng mạng."
---

<div class="textbook-epigraph" markdown="1">

"A minimum spanning tree is the cheapest way to keep a network connected."

<span class="epigraph-attribution">— Tinh thần thuật toán greedy trên đồ thị</span>

</div>

Nối mọi trạm với **tổng chi phí cáp nhỏ nhất** mà vẫn **liên thông** là bài toán **cây khung nhỏ nhất** (*Minimum Spanning Tree*, **MST**). Khác đường đi ngắn nhất (tối ưu path từ một nguồn), MST tối ưu **tập cạnh** tạo cây phủ toàn bộ đỉnh. Mục này định nghĩa MST và hai thuật toán greedy chuẩn: Kruskal và Prim.

![MST](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_mst_example.svg)

<p class="textbook-figure-caption" data-figure="16.4">MST: $$n-1$$ cạnh (đậm), không chu trình, tổng trọng số nhỏ nhất trong các cây khung.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** cây khung và MST trên đồ thị vô hướng có trọng số liên thông.
- **Mô tả** Kruskal (sort + Union–Find) và Prim (mở rộng từ tập đỉnh).
- **Nêu** độ phức tạp tiêu biểu $$O(E\log E)$$ và $$O(E\log V)$$.
- **Áp dụng** ý tưởng MST cho thiết kế mạng / clustering sơ cấp.

**Từ khóa**: spanning tree, MST, Kruskal, Prim, Union–Find, greedy.

</div>

## 1. Cây khung và MST

Nhắc lại: **cây khung** của $$G$$ liên thông là cây con chứa mọi đỉnh.

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho đồ thị vô hướng **liên thông** $$G=(V,E)$$ với trọng số $$w(e)$$ trên mỗi cạnh. **Cây khung nhỏ nhất** (MST) là cây khung $$T\subseteq E$$ sao cho

$$
\sum_{e\in T} w(e)
$$

là **nhỏ nhất** trong mọi cây khung của $$G$$.

</div>

Nếu các trọng số đôi một khác nhau, MST **duy nhất**. Trọng số trùng có thể cho nhiều MST khác nhau cùng tổng.

<div class="textbook-theorem" markdown="1">

**Định lý** (tính chất cạnh an toàn / cut property — dạng greedy). Xét phân hoạch $$V = S \cup (V\setminus S)$$ với $$S$$ khác rỗng và khác $$V$$. Nếu $$e$$ là cạnh **nhẹ nhất** có đúng một đầu trong $$S$$, thì tồn tại một MST chứa $$e$$.

</div>

Hệ quả: thuật toán luôn thêm cạnh “an toàn” theo cut hoặc theo thứ tự trọng số toàn cục vẫn đúng.

## 2. Thuật toán Kruskal

1. Sắp xếp mọi cạnh theo trọng số **tăng dần**.
2. Khởi tạo rừng: mỗi đỉnh là một thành phần (Union–Find).
3. Duyệt cạnh $$(u,v)$$ theo thứ tự: nếu $$u$$ và $$v$$ thuộc **hai thành phần khác nhau**, **thêm** cạnh vào MST và **hợp** hai thành phần; nếu cùng thành phần thì **bỏ** (tránh chu trình).
4. Dừng khi đã chọn $$|V|-1$$ cạnh.

**Độ phức tạp:** $$O(E\log E)$$ cho sort; Union–Find gần $$O(E\,\alpha(V))$$ với path compression / union by rank.

<div class="interactive-demo" markdown="1">
<div data-demo="kruskal-algorithm"></div>
</div>
<script src="{{ '/public/js/kruskal-algorithm.js' | relative_url }}"></script>

## 3. Thuật toán Prim

1. Chọn đỉnh xuất phát $$s$$; tập $$S=\{s\}$$.
2. Lặp cho đến khi $$|S|=|V|$$: chọn cạnh **nhẹ nhất** nối một đỉnh trong $$S$$ với một đỉnh ngoài $$S$$; thêm cạnh đó vào MST và đưa đỉnh mới vào $$S$$.
3. Cấu trúc hỗ trợ: hàng đợi ưu tiên (binary heap / Fibonacci heap).

**Độ phức tạp:** với binary heap thường $$O(E\log V)$$.

| | Kruskal | Prim |
|:---|:---|:---|
| Greedy trên | Cạnh toàn cục (đã sort) | Cạnh ra khỏi tập $$S$$ |
| Cấu trúc | Union–Find | Priority queue |
| Thường hợp hợp | Đồ thị **thưa** (sort cạnh) | Đồ thị **dày** hơn / triển khai từ một gốc |

## 4. Ví dụ tính tay

<div class="textbook-example" markdown="1">

**Ví dụ.** Bốn đỉnh $$A,B,C,D$$; cạnh  
$$(A,B,1)$$, $$(B,D,2)$$, $$(A,D,4)$$, $$(B,C,5)$$, $$(C,D,6)$$.

Kruskal: lấy $$AB(1)$$, $$BD(2)$$, bỏ $$AD(4)$$ (cùng thành phần $$A$$–$$B$$–$$D$$), lấy $$BC(5)$$.  
MST: $$\{AB,BD,BC\}$$, tổng $$1+2+5=8$$.

</div>

## 5. Ứng dụng

- Thiết kế LAN / cáp: liên thông với chi phí nhỏ.
- Clustering sơ cấp: bỏ các cạnh MST nặng nhất để tách cụm.
- Xấp xỉ một số bài toán mạng (nền cho thuật toán nâng cao hơn).

**Không nhầm với** đường đi ngắn nhất (Dijkstra): MST không đảm bảo path từ $$s$$ đến $$t$$ là ngắn nhất.

## Bài tập

### Bài tập 1

Với ví dụ mục 4, tổng trọng số MST là bao nhiêu? Có MST khác cùng tổng không nếu đổi trọng số $$BC$$ thành 6 và $$CD$$ thành 5?

<details>
<summary>Đáp án</summary>

Tổng **8**. Nếu $$BC=6$$, $$CD=5$$: Kruskal lấy $$AB,BD,CD$$ tổng $$1+2+5=8$$ — MST khác cạnh nhưng cùng tổng có thể xảy ra tùy bộ trọng số; ở đây vẫn 8.

</details>

### Bài tập 2

Vì sao Kruskal bỏ cạnh tạo chu trình?

<details>
<summary>Đáp án</summary>

Cây khung có đúng $$|V|-1$$ cạnh và không chu trình. Cạnh nối hai đỉnh đã cùng thành phần sẽ tạo chu trình và không cần cho liên thông của rừng đang xây.

</details>

### Bài tập 3

MST của đồ thị liên thông $$n$$ đỉnh có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

Đúng $$n-1$$ cạnh.

</details>

### Bài tập 4

Đồ thị không liên thông có MST không?

<details>
<summary>Đáp án</summary>

Không (theo định nghĩa phủ mọi đỉnh bằng **một** cây). Có thể nói **rừng khung nhỏ nhất** trên từng thành phần.

</details>

## Tóm tắt

1. **MST**: cây khung tổng trọng số nhỏ nhất.
2. **Cut property** biện minh greedy.
3. **Kruskal**: sort + Union–Find; **Prim**: mở rộng $$S$$ + heap.
4. Ứng dụng mạng / clustering; khác shortest path.

Trong bài tiếp theo (tùy chọn): **Huffman** và **BST**.
