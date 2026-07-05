---
layout: post
title: "Giới thiệu Cây"
categories: chapter16
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Chương 16 nghiên cứu cây — đồ thị liên thông không chu trình. Mục 16.1 định nghĩa cây có gốc, tính chất n − 1 cạnh và liên hệ với cấu trúc dữ liệu trong máy tính."
---

<div class="textbook-epigraph" markdown="1">

"A tree is a connected graph with no cycles — one of the most important structures in computer science."

<span class="epigraph-attribution">— Donald Knuth (spirit)</span>

</div>

Chương 12 đã giới thiệu đồ thị tổng quát. **Cây** (tree) là lớp con đặc biệt: liên thông nhưng **không có chu trình**. File system, DOM HTML, cây cú pháp (parse tree), cây biểu thức và index cơ sở dữ liệu đều là cây. Mục 16.1 đặt nền định nghĩa và các tính chất cơ bản.

![Cây cú pháp (parse tree)](/discrete-mathematics-for-computer-science-iuh/img/course/Parse_tree.png)

<p class="textbook-figure-caption" data-figure="16.1">Parse tree — cây biểu diễn cấu trúc câu hoặc biểu thức trong compiler.</p>
![Abstract syntax tree](/discrete-mathematics-for-computer-science-iuh/img/course/Abstract_syntax_tree_for_Euclidean_algorithm.svg)

<p class="textbook-figure-caption" data-figure="16.2">AST (abstract syntax tree) — cây cú pháp trừu tượng, nền tảng phân tích và biên dịch.</p>
![Đồ thị vô hướng liên thông](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="16.3">Cây là đồ thị vô hướng liên thông không chu trình — mọi cặp đỉnh có đúng một đường đi đơn.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** cây và cây có gốc (rooted tree).
- **Liệt kê** các tính chất tương đương của cây ($$n$$ đỉnh ⟺ $$n-1$$ cạnh).
- **Phân biệt** lá, cha, con, độ sâu, chiều cao.
- **Nhận biết** cây trong file system, DOM và AST.

**Từ khóa**: cây (tree), gốc (root), lá (leaf), độ sâu (depth), chiều cao (height), rừng (forest).
</div>

## Định nghĩa cây

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Cây** là đồ thị vô hướng **liên thông** và **không có chu trình**.

**Cây có gốc** (rooted tree): Chọn một đỉnh làm **gốc** (root); các đỉnh còn lại có quan hệ cha–con theo đường đi duy nhất từ gốc.
</div>

**Thuật ngữ**:
- **Lá** (leaf): đỉnh bậc 1 (trừ gốc đơn độc) hoặc không có con trong cây có gốc.
- **Độ sâu** $$\text{depth}(v)$$: số cạnh trên đường từ gốc đến $$v$$.
- **Chiều cao** $$h(T)$$: $$\max_v \text{depth}(v)$$.

<div class="textbook-theorem" markdown="1">
**Định lý** (tính chất cây): Cho đồ thị vô hướng $$G$$ có $$n \geq 1$$ đỉnh. Các điều kiện sau **tương đương**:

1. $$G$$ là cây.
2. $$G$$ liên thông và có đúng $$n - 1$$ cạnh.
3. $$G$$ không chu trình và có đúng $$n - 1$$ cạnh.
4. Giữa mọi cặp đỉnh có **đúng một** đường đi đơn.
5. $$G$$ liên thông; thêm bất kỳ cạnh nào tạo đúng **một** chu trình.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Cây 10 đỉnh có đúng $$10 - 1 = 9$$ cạnh. Nếu đồ thị liên thông có 10 đỉnh và 10 cạnh → **có chu trình**, không phải cây.
</div>

## Cây khung

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Cây khung** (spanning tree) của đồ thị liên thông $$G$$ là cây con chứa **tất cả** đỉnh của $$G$$.
</div>

Mọi đồ thị liên thông có ít nhất một cây khung. Chọn cây khung = chọn tập cạnh tối thiểu giữ liên thông — chủ đề mục 16.3 (MST).

## Biểu diễn cây

```python
# Danh sách con (children list)
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
```

JSON, XML, HTML DOM và thư mục filesystem đều là cây lồng nhau — **duyệt cây** là kỹ năng cốt lõi (mục 16.2).

## Bài tập

### Bài tập 1

Đồ thị liên thông 15 đỉnh, 14 cạnh. Có phải cây không?

<details>
<summary>Đáp án</summary>

Có — $$|E| = |V| - 1$$ và liên thông.

</details>

### Bài tập 2

Cây có 20 lá (đỉnh bậc 1). Khẳng định nào đúng về tổng bậc?

<details>
<summary>Đáp án</summary>

Mỗi lá đóng góp 1; mỗi cạnh đóng góp 2 vào tổng bậc. Tổng bậc = $$2(n-1)$$. Không suy ra số lá chỉ từ $$n$$ mà không thêm giả thiết — nhưng số lá ≥ 2 nếu $$n \geq 2$$.

</details>

### Bài tập 3

Giải thích vì sao filesystem dùng cây, không dùng đồ thị có chu trình tự do.

<details>
<summary>Đáp án</summary>

Mỗi file/thư mục có **một** đường dẫn duy nhất từ root — tương đương đúng một đường đi đơn trong cây. Chu trình (symlink vòng) phải xử lý đặc biệt.

</details>

## Tóm tắt

- **Cây**: liên thông, không chu trình; $$n$$ đỉnh ⟺ $$n-1$$ cạnh.
- **Cây có gốc**: depth, height, leaf, parent/child.
- **Spanning tree**: nối tất cả đỉnh, không cycle.
- Ứng dụng: FS, DOM, AST, index.

Trong bài tiếp theo, chúng ta học **duyệt cây** — preorder, inorder, postorder và level-order.