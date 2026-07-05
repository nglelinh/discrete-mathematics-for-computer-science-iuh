---
layout: post
title: "Cây khung và Cây khung Nhỏ nhất"
categories: chapter16
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Mục 16.3 giới thiệu cây khung nhỏ nhất (MST) và thuật toán Kruskal, Prim — nền tảng thiết kế mạng LAN, cluster và đường cáp tối thiểu."
---

Trong mạng máy tính, nối mọi máy với tổng chi phí cáp **nhỏ nhất** mà vẫn **liên thông** là bài toán **cây khung nhỏ nhất** (Minimum Spanning Tree, MST). Khác shortest path (tổng đường đi), MST tối ưu **tập cạnh** tạo cây phủ toàn bộ đỉnh. Mục 16.3 trình bày Kruskal và Prim.

![Đồ thị có trọng số](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="16.6">MST chọn tập cạnh tối thiểu nối mọi đỉnh — không có chu trình.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** MST trên đồ thị vô hướng có trọng số liên thông.
- **Mô tả** thuật toán Kruskal (Union-Find) và Prim (greedy từ gốc).
- **Phân tích** độ phức tạp $$O(E \log E)$$ và $$O(E \log V)$$.
- **Áp dụng** MST trong thiết kế mạng và clustering.

**Từ khóa**: spanning tree, MST, Kruskal, Prim, Union-Find, greedy.
</div>

## Định nghĩa MST

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho đồ thị vô hướng **liên thông** $$G = (V, E)$$ với trọng số $$w(e) \geq 0$$ trên mỗi cạnh. **Cây khung nhỏ nhất** (MST) là cây khung $$T \subseteq E$$ sao cho tổng trọng số $$\sum_{e \in T} w(e)$$ là **nhỏ nhất**.
</div>

<div class="textbook-theorem" markdown="1">
**Định lý** (tính chất greedy): Nếu $$(u,v)$$ là cạnh **nhẹ nhất** nối hai thành phần liên thông khác nhau trong quá trình xây MST, thì tồn tại MST chứa $$(u,v)$$.
</div>

## Thuật toán Kruskal

1. Sắp xếp cạnh theo trọng số tăng dần.
2. Duyệt từng cạnh $$(u,v)$$: nếu $$u$$ và $$v$$ thuộc **hai thành phần khác nhau** (Union-Find), **thêm** cạnh vào MST và **gộp** hai thành phần.
3. Dừng khi có $$|V| - 1$$ cạnh.

**Độ phức tạp**: $$O(E \log E)$$ (sort) + Union-Find gần $$O(E \,\alpha(V))$$.

<div class="interactive-demo" markdown="1">
<div data-demo="kruskal-algorithm"></div>
</div>
<script src="{{ '/public/js/kruskal-algorithm.js' | relative_url }}"></script>

## Thuật toán Prim

1. Bắt đầu từ đỉnh bất kỳ $$s$$; $$T = \{s\}$$.
2. Lặp: chọn cạnh **nhẹ nhất** nối đỉnh trong $$T$$ với đỉnh ngoài $$T$$; thêm vào MST.
3. Dừng khi $$|T| = |V|$$.

**Độ phức tạp**: Với heap: $$O(E \log V)$$.

| | Kruskal | Prim |
|:---|:---|:---|
| Cấu trúc phụ | Union-Find | Priority queue |
| Phù hợp | Đồ thị thưa | Đồ thị dày |
| Greedy trên | Cạnh toàn cục | Cạnh từ tập đã chọn |

## Bài tập

### Bài tập 1

4 đỉnh, cạnh (A,B,1), (B,D,2), (A,D,4), (B,C,5), (C,D,6). Tổng trọng số MST?

<details>
<summary>Đáp án</summary>

Chọn (A,B,1), (B,D,2), và cạnh thứ 3 nối C — nhẹ nhất là (B,C,5) hoặc qua D. MST: AB+BD+BC = 1+2+5 = **8** (kiểm tra: AD+BD+BC = 4+2+5=11).

</details>

### Bài tập 2

Vì sao Kruskal bỏ qua cạnh tạo chu trình?

<details>
<summary>Đáp án</summary>

Cây có $$|V|-1$$ cạnh, không chu trình. Cạnh nối hai đỉnh đã liên thông trong MST đang xây là thừa.

</details>

### Bài tập 3

MST có tối đa bao nhiêu cạnh? Tối thiểu?

<details>
<summary>Đáp án</summary>

Đúng $$|V| - 1$$ cạnh (cây phủ $$V$$ đỉnh).

</details>

## Tóm tắt

- **MST**: cây khung tổng trọng số nhỏ nhất.
- **Kruskal**: sort cạnh + Union-Find.
- **Prim**: mở rộng từ tập đỉnh đã chọn.
- Ứng dụng: LAN, cable layout, clustering.

Trong bài tiếp theo (tùy chọn), chúng ta học **Huffman** và **BST** — cây trong nén dữ liệu và tìm kiếm.