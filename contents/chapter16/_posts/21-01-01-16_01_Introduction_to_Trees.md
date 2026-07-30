---
layout: post
title: "Giới thiệu Cây"
categories: chapter16
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Cây = đồ thị liên thông không chu trình; cây có gốc, lá, depth, height; tính chất n−1 cạnh; cây khung; biểu diễn và ứng dụng FS/DOM/AST."
---

<div class="textbook-epigraph" markdown="1">

"A tree is a connected graph with no cycles — one of the most important structures in computer science."

<span class="epigraph-attribution">— Tinh thần Knuth / cấu trúc rời rạc</span>

</div>

Chương 12 đã giới thiệu đồ thị tổng quát. **Cây** (*tree*) là lớp con đặc biệt: **liên thông** và **không có chu trình**. File system, DOM HTML, cây cú pháp (parse tree / AST), cây biểu thức và nhiều cấu trúc chỉ mục đều mang hình dạng cây. Mục này định nghĩa cây, cây có gốc và các tính chất tương đương.

![Cây có gốc](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_rooted_example.svg)

<p class="textbook-figure-caption" data-figure="16.1">Cây có gốc: mỗi đỉnh khác gốc có đúng một cha; đường từ gốc đến mọi đỉnh là duy nhất.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** cây và cây có gốc (*rooted tree*).
- **Nêu** các điều kiện tương đương ($$n$$ đỉnh $$\iff$$ $$n-1$$ cạnh, …).
- **Phân biệt** lá, cha–con, độ sâu, chiều cao, rừng.
- **Nhận biết** cây trong filesystem, DOM và AST.

**Từ khóa**: cây (tree), gốc (root), lá (leaf), độ sâu (depth), chiều cao (height), rừng (forest), cây khung (spanning tree).

</div>

## 1. Định nghĩa cây

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Cây** là đồ thị vô hướng **liên thông** và **không có chu trình**.

**Cây có gốc** (*rooted tree*): chọn một đỉnh làm **gốc** (*root*); với mỗi đỉnh $$v$$ khác gốc, đỉnh liền trước trên đường đi duy nhất từ gốc đến $$v$$ gọi là **cha** của $$v$$; các đỉnh kề “xa gốc hơn” là **con**.

</div>

**Thuật ngữ thường dùng**

| Khái niệm | Định nghĩa |
|:---|:---|
| **Lá** (*leaf*) | Trong cây có gốc: đỉnh không có con. (Trên cây vô hướng không gốc: đỉnh bậc 1, khi $$n\ge 2$$.) |
| **Độ sâu** $$\mathrm{depth}(v)$$ | Số cạnh trên đường từ gốc đến $$v$$ |
| **Chiều cao** $$h(T)$$ | $$\max_v \mathrm{depth}(v)$$ |
| **Rừng** (*forest*) | Đồ thị vô hướng không chu trình (mỗi thành phần liên thông là một cây) |

<div class="textbook-theorem" markdown="1">

**Định lý** (tính chất tương đương). Cho đồ thị vô hướng $$G$$ có $$n \ge 1$$ đỉnh. Các mệnh đề sau **tương đương**:

1. $$G$$ là cây.
2. $$G$$ liên thông và có đúng $$n-1$$ cạnh.
3. $$G$$ không chu trình và có đúng $$n-1$$ cạnh.
4. Giữa mọi cặp đỉnh có **đúng một** đường đi đơn.
5. $$G$$ liên thông; thêm bất kỳ cạnh mới nào tạo **đúng một** chu trình.
6. $$G$$ không chu trình; xóa bất kỳ cạnh nào làm $$G$$ **không** còn liên thông.

</div>

*Ý tưởng.* Liên thông + không chu trình $$\implies$$ đúng một path giữa mọi cặp. Handshaking / đếm cạnh: cây $$n$$ đỉnh có $$n-1$$ cạnh. Thêm cạnh nối hai đỉnh đã có path → chu trình; bớt cạnh → tách thành phần.

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Cây 10 đỉnh có đúng 9 cạnh. Đồ thị liên thông 10 đỉnh, 10 cạnh **không** phải cây — buộc có chu trình.

</div>

## 2. Cây khung

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Cây khung** (*spanning tree*) của đồ thị liên thông $$G=(V,E)$$ là đồ thị con $$T=(V,E')$$ với $$E'\subseteq E$$ sao cho $$T$$ là cây — tức nối **mọi** đỉnh, không chu trình, $$|E'|=|V|-1$$.

</div>

Mọi đồ thị vô hướng liên thông có ít nhất một cây khung. Khi cạnh mang trọng số, việc chọn cây khung **tổng trọng số nhỏ nhất** là bài toán MST (Mục 16.3).

## 3. Biểu diễn và ứng dụng

```python
# Danh sách con (children list) — cây có gốc
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [], "E": [], "F": [],
}
```

- **Filesystem**: thư mục gốc; mỗi file/folder (trừ root) có một đường dẫn logic — path duy nhất.
- **DOM / JSON / XML**: cây lồng nhau; duyệt để render hoặc serialize.
- **AST**: compiler biểu diễn chương trình bằng cây; biến đổi tối ưu thao tác trên cây.

Symlink hoặc tham chiếu chéo có thể tạo **chu trình** — khi đó cấu trúc không còn là cây thuần; hệ thống phải phát hiện vòng.

![Parse tree](/discrete-mathematics-for-computer-science-iuh/img/course/Parse_tree.png)

<p class="textbook-figure-caption" data-figure="16.2">Parse tree — biểu diễn cấu trúc câu / biểu thức trong phân tích cú pháp.</p>

## Bài tập

### Bài tập 1

Đồ thị liên thông 15 đỉnh, 14 cạnh. Có phải cây không?

<details>
<summary>Đáp án</summary>

Có: liên thông và $$|E|=|V|-1$$ (điều kiện tương đương).

</details>

### Bài tập 2

Chứng minh ngắn: mọi cây $$n\ge 2$$ đỉnh có **ít nhất hai** lá (đỉnh bậc 1).

<details>
<summary>Đáp án</summary>

Tổng bậc $$= 2(n-1)$$. Nếu nhiều nhất một đỉnh bậc 1, thì ít nhất $$n-1$$ đỉnh có bậc $$\ge 2$$ → tổng bậc $$\ge 1 + 2(n-1) = 2n-1 > 2(n-1)$$ — mâu thuẫn. Vậy $$\ge 2$$ lá.

</details>

### Bài tập 3

Vì sao filesystem “lý tưởng” dùng cây, không dùng đồ thị có chu trình tự do?

<details>
<summary>Đáp án</summary>

Mỗi đối tượng có **một** đường từ root (đúng một path đơn). Chu trình làm mơ hồ đường dẫn và có thể khiến duyệt không kết thúc nếu không có kiểm soát.

</details>

### Bài tập 4

Đồ thị không chu trình có 12 đỉnh, 9 cạnh. Có bao nhiêu thành phần liên thông (cây trong rừng)?

<details>
<summary>Đáp án</summary>

Rừng: $$|E| = |V| - c$$ với $$c$$ = số thành phần. $$9 = 12 - c \implies c = 3$$.

</details>

## Tóm tắt

1. **Cây**: liên thông, không chu trình; $$n$$ đỉnh $$\iff$$ $$n-1$$ cạnh.
2. **Cây có gốc**: depth, height, parent/child, leaf.
3. **Cây khung**: nối mọi đỉnh của $$G$$ liên thông.
4. Ứng dụng: FS, DOM, AST — path duy nhất từ gốc.

Trong bài tiếp theo: **duyệt cây** — preorder, inorder, postorder và level-order.
