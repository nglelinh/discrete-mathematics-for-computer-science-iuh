---
layout: post
title: "Cây khung và Cây khung Nhỏ nhất"
categories: chapter16
date: 2021-01-01
order: 3
required: true
lang: en
---

# Cây khung và Cây khung Nhỏ nhất

Khi một mạng đã có rất nhiều cạnh, ta thường không muốn giữ tất cả. Trong thiết kế hạ tầng, mạng điện, mạng truyền thông hay đường giao thông, mục tiêu thường là giữ hệ thống **vẫn liên thông** nhưng dùng ít liên kết hơn, và tốt nhất là tổng chi phí nhỏ nhất.


Cây xuất hiện ở rất nhiều tầng của hệ thống, nên việc hiểu cấu trúc và cách thao tác trên cây sẽ giúp các khái niệm sau này bớt rời rạc hơn.
Ý tưởng đó dẫn đến **cây khung** và **cây khung nhỏ nhất**. Một cây khung giữ lại đủ cạnh để nối tất cả các đỉnh mà không tạo chu trình. Nếu mỗi cạnh có chi phí, ta muốn chọn cây khung có tổng trọng số thấp nhất.

Đây là một chủ đề rất đẹp vì nó nối đồ thị, cây và tối ưu thành một bài toán vừa lý thuyết vừa cực kỳ thực tế. Nhiều bài toán thiết kế mạng trong đời sống có thể mô hình hóa rất trực tiếp bằng MST.

Trong bài này, chúng ta sẽ học khái niệm cây khung, hiểu mục tiêu của MST và chuẩn bị nền cho các thuật toán xây dựng chúng.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Định nghĩa** cây khung của đồ thị.
- **Liệt kê** tất cả cây khung của một đồ thị nhỏ.
- **Thực hiện** thuật toán Kruskal và Prim để tìm cây khung nhỏ nhất.
- **So sánh** ưu nhược điểm của hai thuật toán.
- **Áp dụng** vào bài toán thiết kế mạng thực tế.

**Từ khóa**: Cây khung (spanning tree), cây khung nhỏ nhất (MST), thuật toán Kruskal, thuật toán Prim, cạnh an toàn (safe edge), cấu trúc Union-Find (Disjoint Set).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter16/mst_example.svg" alt="Minh họa cây khung nhỏ nhất trên đồ thị 4 đỉnh có trọng số" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 16.3 — Đồ thị (trái) và cây khung nhỏ nhất (phải, nét đậm) với tổng trọng số tối thiểu.</figcaption>
</p>
</figure>

## 1. Cây khung

**Định nghĩa**: Cho đồ thị liên thông $$G = (V, E)$$. Cây khung (spanning tree) của $$G$$ là cây con $$T = (V, E')$$ với $$E' \subseteq E$$ chứa **tất cả** các đỉnh của $$G$$.

Nói cách khác, cây khung là tập con các cạnh của $$G$$ vừa đủ để giữ $$G$$ liên thông, không có cạnh thừa (không tạo chu trình).

**Định lý**: Mọi đồ thị liên thông đều có ít nhất một cây khung.

<div class="content-box example-box" markdown="1">
**Ví dụ**: Đồ thị $$K_3$$ (tam giác) có 3 đỉnh A, B, C và 3 cạnh.

Có 3 cây khung: bỏ cạnh (A,B), hoặc bỏ (B,C), hoặc bỏ (A,C).
</div>

## 2. Cây khung Nhỏ nhất (MST)

**Bài toán**: Cho đồ thị liên thông, vô hướng, có trọng số $$G = (V, E, w)$$. Tìm cây khung $$T$$ sao cho tổng trọng số là nhỏ nhất:

$$\min_{T} \sum_{e \in T} w(e)$$

<div class="content-box example-box" markdown="1">
**Ví dụ thực tế**: 4 tòa nhà cần được nối mạng cáp quang. Khoảng cách giữa các tòa:

| Từ | Đến | Chi phí |
|:-----|:-----|--------:|
| A | B | 4 |
| A | C | 2 |
| A | D | 5 |
| B | C | 1 |
| B | D | 3 |
| C | D | 6 |

MST sẽ chọn các cạnh (B,C)=1, (A,C)=2, (B,D)=3 → tổng chi phí = 6.
</div>

## 3. Thuật toán Kruskal

Ở phần này, đừng chỉ nhớ các bước. Hãy chú ý điều kiện áp dụng, thông tin được duy trì sau mỗi bước và lý do thuật toán cho kết quả đúng.

**Ý tưởng tham lam**: Sắp xếp các cạnh theo trọng số tăng dần, lần lượt thêm cạnh vào cây khung nếu cạnh đó không tạo chu trình.

```
THUẬT TOÁN: Kruskal(G)
1. T ← ∅
2. Sắp xếp các cạnh của G theo trọng số tăng dần
3. FOR mỗi cạnh (u,v) theo thứ tự đã sắp xếp DO
4.     IF T ∪ {(u,v)} không chứa chu trình THEN
5.         T ← T ∪ {(u,v)}
6.     END IF
7. END FOR
8. RETURN T
```

<div class="content-box example-box" markdown="1">
**Ví dụ với đồ thị 4 tòa nhà**:

| Bước | Cạnh (u,v,w) | Chọn? | Cây khung hiện tại |
|:---|:---|:---:|:---|
| 1 | (B,C,1) | ✓ | {BC} |
| 2 | (A,C,2) | ✓ | {BC, AC} |
| 3 | (B,D,3) | ✓ | {BC, AC, BD} |
| 4 | (A,B,4) | ✗ (chu trình) | {BC, AC, BD} |
| 5 | (A,D,5) | ✗ (chu trình) | {BC, AC, BD} |
| 6 | (C,D,6) | ✗ (chu trình) | {BC, AC, BD} |

Kết quả: BC + AC + BD = 1 + 2 + 3 = 6.
</div>

### Kiểm tra chu trình với Union-Find

Để kiểm tra nhanh một cạnh có tạo chu trình không, Kruskal dùng cấu trúc **Union-Find** (Disjoint Set):
- Ban đầu mỗi đỉnh là một tập riêng.
- Với cạnh (u,v): nếu Find(u) = Find(v) → u và v đã trong cùng cây → thêm cạnh sẽ tạo chu trình.
- Nếu khác tập: Union(u,v) để hợp nhất.

Độ phức tạp: $$O(E \log E)$$ (chủ yếu do sắp xếp cạnh).

## 4. Thuật toán Prim

Ở phần này, đừng chỉ nhớ các bước. Hãy chú ý điều kiện áp dụng, thông tin được duy trì sau mỗi bước và lý do thuật toán cho kết quả đúng.

**Ý tưởng**: Bắt đầu từ một đỉnh, mỗi bước thêm cạnh **nhỏ nhất** nối một đỉnh trong cây khung với một đỉnh ngoài cây khung.

```
THUẬT TOÁN: Prim(G, root)
1. T ← ∅
2. inTree ← {root}   // tập đỉnh trong cây
3. WHILE |inTree| < |V| DO
4.     Tìm cạnh (u,v) với u ∈ inTree, v ∉ inTree có w nhỏ nhất
5.     T ← T ∪ {(u,v)}
6.     inTree ← inTree ∪ {v}
7. END WHILE
8. RETURN T
```

<div class="content-box example-box" markdown="1">
**Ví dụ với đồ thị 4 tòa nhà, bắt đầu từ A**:

| Bước | Cạnh (u,v,w) | inTree | Tổng |
|:---|:---|:---|:---:|
| 1 | (A,C,2) | {A,C} | 2 |
| 2 | (C,B,1) | {A,C,B} | 3 |
| 3 | (B,D,3) | {A,C,B,D} | 6 |

Kết quả: AC + CB + BD = 2 + 1 + 3 = 6. Giống Kruskal!
</div>

Độ phức tạp: $$O(V^2)$$ với ma trận kề, hoặc $$O(E \log V)$$ với heap.

## So sánh Kruskal và Prim

| Tiêu chí | Kruskal | Prim |
|:---|---|:---|
| Chiến lược | Dựa trên cạnh | Dựa trên đỉnh |
| Cấu trúc dữ liệu | Union-Find | Heap / Ma trận kề |
| Độ phức tạp | $$O(E \log E)$$ | $$O(E \log V)$$ (heap) |
| Tốt khi... | Đồ thị thưa (E ≈ V) | Đồ thị dày (E ≈ V²) |
| Xử lý đồ thị không liên thông | Cho rừng khung | Chỉ cho một cây |

<div class="content-box insight-box" markdown="1">
**Nhận xét**: Cả hai thuật toán đều là **tham lam** (greedy) — mỗi bước đều chọn phương án tốt nhất tại thời điểm đó. Nhưng không phải bài toán tham lam nào cũng cho kết quả tối ưu! Với MST, thuật toán tham lam hoạt động nhờ tính chất "cắt" (cut property) của đồ thị có trọng số.
</div>

## Ứng dụng trong Khoa học Máy tính

- **Thiết kế mạng**: Mạng máy tính, mạng điện, mạng cấp thoát nước.
- **Mạch tích hợp**: Nối các thành phần trên chip với chi phí tối thiểu.
- **Phân cụm (clustering)**: MST được dùng trong bài toán phân cụm dữ liệu.
- **Giao thức mạng**: Spanning Tree Protocol (STP) trong Ethernet.
- **Xấp xỉ TSP**: Dùng MST để xấp xỉ bài toán người bán hàng.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Mô phỏng Thuật toán MST</h3>
<p>Công cụ cho phép bạn vẽ đồ thị có trọng số và xem từng bước của Kruskal và Prim — các cạnh được tô màu khi được chọn, và tổng trọng số cập nhật theo thời gian thực. <strong>Hãy thử:</strong> Vẽ một đồ thị 6 đỉnh, chạy cả hai thuật toán và so sánh kết quả.</p>
<div data-demo="kruskal-algorithm"></div>
</div>
<script src="{{ '/public/js/kruskal-algorithm.js' | relative_url }}"></script>

## Bài tập

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

1. Tìm tất cả cây khung của đồ thị 4 đỉnh hình vuông (A-B, B-C, C-D, D-A, A-C).
2. Cho đồ thị 5 đỉnh với các cạnh: (A,B,2), (A,C,3), (B,C,1), (B,D,4), (C,D,5), (C,E,4), (D,E,3). Tìm MST bằng Kruskal và Prim.
3. Tại sao thuật toán Kruskal cần cấu trúc Union-Find? Nếu không có nó, ta có thể làm gì khác?
4. **Thử thách**: Chứng minh tính chất "cắt" (cut property) — nếu (u,v) là cạnh nhỏ nhất nối hai tập đỉnh S và V\S, thì (u,v) thuộc mọi MST.

<details>
<summary>Hướng dẫn bài 4</summary>

**Tính chất cắt (Cut Property)**:

Gọi (u,v) là cạnh nhỏ nhất nối S và V\S. Giả sử có một MST T không chứa (u,v).

Vì T kết nối mọi đỉnh, tồn tại đường đi trong T từ u đến v. Đường đi này phải đi qua một cạnh (x,y) nào đó nối S và V\S (vì u ở S, v ở V\S).

Bây giờ, loại bỏ (x,y) khỏi T và thêm (u,v) vào:
- Trọng số: w(u,v) ≤ w(x,y) (vì (u,v) là cạnh nhỏ nhất nối S và V\S)
- Tính liên thông vẫn được giữ (u kết nối với v qua (u,v))

Vậy T' = T - {(x,y)} + {(u,v)} là MST chứa (u,v). □

Tính chất này đảm bảo mọi thuật toán tham lam (Kruskal, Prim) đều cho kết quả tối ưu.
</details>

## Tóm tắt

- **Cây khung**: tập con $$n-1$$ cạnh giữ đồ thị liên thông.
- **MST**: cây khung với tổng trọng số nhỏ nhất.
- **Kruskal**: sắp xếp cạnh, thêm cạnh không tạo chu trình (dùng Union-Find).
- **Prim**: xuất phát từ đỉnh, thêm cạnh nhỏ nhất nối cây với đỉnh ngoài.
- **Cả hai đều tham lam**: đúng nhờ tính chất cắt (cut property) của đồ thị.

Trong bài tiếp theo, chúng ta khám phá các ứng dụng thực tế của cây, từ nén dữ liệu đến cơ sở dữ liệu.

## Tài liệu Tham khảo

1. Joseph B. Kruskal, "On the Shortest Spanning Subtree of a Graph and the Traveling Salesman Problem," *Proc. AMS*, 1956.
2. Robert C. Prim, "Shortest Connection Networks and Some Generalizations," *Bell System Technical Journal*, 1957.
3. Thomas H. Cormen et al., *Introduction to Algorithms*, Chương 23.
