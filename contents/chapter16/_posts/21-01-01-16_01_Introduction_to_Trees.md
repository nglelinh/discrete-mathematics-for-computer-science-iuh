---
layout: post
title: "Giới thiệu Cây"
categories: chapter16
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Cây là đồ thị liên thông không chu trình; cây có gốc, lá, độ sâu, chiều cao; tính chất n−1 cạnh; cây khung; biểu diễn và ứng dụng trong hệ thống tệp, DOM và AST."
---

<div class="textbook-epigraph" markdown="1">

"A tree is a connected graph with no cycles — one of the most important structures in computer science."

<span class="epigraph-attribution">— Tinh thần Knuth / cấu trúc rời rạc</span>

</div>

Chương 12 đã giới thiệu khái niệm đồ thị tổng quát. **Cây** (*tree*) là một lớp con đặc biệt của đồ thị, thỏa mãn hai điều kiện: **liên thông** và **không có chu trình**. Hệ thống tệp (file system), cây DOM của HTML, cây cú pháp (parse tree / AST), cây biểu thức và nhiều cấu trúc chỉ mục đều mang cấu trúc cây. Bài học này trình bày định nghĩa cây, cây có gốc và các điều kiện tương đương của cây.

![Cây có gốc](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_rooted_example.svg)

<p class="textbook-figure-caption" data-figure="16.1">Cây có gốc: mỗi đỉnh khác gốc có đúng một đỉnh cha và có đường đi duy nhất từ gốc đến mọi đỉnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** cây và cây có gốc (*rooted tree*).
- **Phát biểu** các điều kiện tương đương của cây (như $$n$$ đỉnh $$\iff$$ $$n-1$$ cạnh).
- **Phân biệt** lá, quan hệ cha–con, độ sâu, chiều cao và rừng.
- **Nhận diện** cấu trúc cây trong hệ thống tệp, DOM và AST.

**Từ khóa**: cây (tree), gốc (root), lá (leaf), độ sâu (depth), chiều cao (height), rừng (forest), cây khung (spanning tree).

</div>

## Định nghĩa cây

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Cây** là đồ thị vô hướng **liên thông** và **không có chu trình**.

**Cây có gốc** (*rooted tree*) được tạo ra khi chọn một đỉnh cố định làm **gốc** (*root*). Với mỗi đỉnh $$v$$ khác gốc, đỉnh liền trước nó trên đường đi duy nhất từ gốc đến $$v$$ gọi là **cha** của $$v$$, còn các đỉnh kề nằm xa gốc hơn gọi là **con** của $$v$$.

</div>

**Thuật ngữ thường dùng**

| Khái niệm | Định nghĩa |
|:---|:---|
| **Lá** (*leaf*) | Trong cây có gốc: đỉnh không có con. (Trên cây vô hướng không gốc với $$n\ge 2$$: đỉnh có bậc 1.) |
| **Độ sâu** $$\mathrm{depth}(v)$$ | Số cạnh trên đường đi từ gốc đến $$v$$ |
| **Chiều cao** $$h(T)$$ | $$\max_v \mathrm{depth}(v)$$ |
| **Rừng** (*forest*) | Đồ thị vô hướng không có chu trình (mỗi thành phần liên thông là một cây) |

<div class="textbook-theorem" markdown="1">

**Định lý** (Các tính chất tương đương của cây). Cho đồ thị vô hướng $$G$$ có $$n \ge 1$$ đỉnh. Các mệnh đề sau là **tương đương**:

1. $$G$$ là một cây.
2. $$G$$ liên thông và có đúng $$n-1$$ cạnh.
3. $$G$$ không có chu trình và có đúng $$n-1$$ cạnh.
4. Giữa mọi cặp đỉnh có **đúng một** đường đi đơn.
5. $$G$$ liên thông và việc thêm bất kỳ cạnh mới nào cũng tạo ra **đúng một** chu trình.
6. $$G$$ không có chu trình và việc xóa bất kỳ cạnh nào cũng làm $$G$$ mất tính liên thông.

</div>

*Ý tưởng chứng minh.* Tính liên thông kết hợp với việc không có chu trình đảm bảo có đúng một đường đi đơn giữa mọi cặp đỉnh. Khi đếm số cạnh, một cây gồm $$n$$ đỉnh luôn có đúng $$n-1$$ cạnh. Thêm một cạnh nối hai đỉnh vốn đã có đường đi sẽ tạo chu trình, còn bỏ đi một cạnh bất kỳ sẽ tách đồ thị thành hai thành phần liên thông.

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Một cây gồm 10 đỉnh có đúng 9 cạnh. Ngược lại, một đồ thị liên thông có 10 đỉnh và 10 cạnh **không** phải là cây vì chắc chắn chứa chu trình.

</div>

## Cây khung

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Cây khung** (*spanning tree*) của đồ thị liên thông $$G=(V,E)$$ là đồ thị con $$T=(V,E')$$ với $$E'\subseteq E$$ sao cho $$T$$ là một cây — tức là nối **mọi** đỉnh của $$G$$, không có chu trình và có $$\vert E'\vert =\vert V\vert -1$$.

</div>

Mọi đồ thị vô hướng liên thông đều có ít nhất một cây khung. Khi các cạnh mang trọng số, bài toán tìm cây khung có **tổng trọng số nhỏ nhất** gọi là bài toán cây khung nhỏ nhất — MST (Mục 16.3).

## Biểu diễn và ứng dụng

```python
# Danh sách con (children list) — cây có gốc
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [], "E": [], "F": [],
}
```

- **Hệ thống tệp (Filesystem)**: có một thư mục gốc; mỗi tệp hoặc thư mục (trừ gốc) có đúng một đường dẫn logic duy nhất.
- **DOM / JSON / XML**: dữ liệu tổ chức lồng nhau dạng cây, được duyệt để kết xuất (render) hoặc tuần tự hóa (serialize).
- **Cây cú pháp trừu tượng (AST)**: trình biên dịch biểu diễn chương trình dưới dạng cây để thực hiện phân tích và tối ưu hóa.

Lưu ý rằng các liên kết mềm (*symlink*) hoặc tham chiếu chéo có thể tạo ra **chu trình**; khi đó cấu trúc không còn là cây thuần túy và hệ thống cần cơ chế phát hiện vòng lặp.

![Parse tree](/discrete-mathematics-for-computer-science-iuh/img/course/Parse_tree.png)

<p class="textbook-figure-caption" data-figure="16.2">Cây phân tích cú pháp (parse tree) — biểu diễn cấu trúc câu hoặc biểu thức trong phân tích cú pháp.</p>

### Minh họa tương tác

Minh họa dựng cây từ dãy khóa và quan sát số nút cũng như chiều cao của cây:

<div class="interactive-demo" markdown="1">
<div data-demo="tree-explainer" data-mode="traversal"></div>
</div>
<script src="{{ '/public/js/explainers/tree-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Một đồ thị liên thông có 15 đỉnh và 14 cạnh. Đồ thị này có phải là cây không?

<details>
<summary>Đáp án</summary>

Có. Vì đồ thị liên thông và có $$\vert E\vert =\vert V\vert -1$$, thỏa mãn điều kiện tương đương của cây.

</details>

### Bài tập 2

Chứng minh ngắn gọn rằng mọi cây có $$n\ge 2$$ đỉnh đều có **ít nhất hai** lá (đỉnh bậc 1).

<details>
<summary>Đáp án</summary>

Tổng bậc của mọi đỉnh trong cây là $$2(n-1)$$. Vì cây liên thông với $$n\ge 2$$ nên mọi đỉnh đều có bậc ít nhất bằng 1. Nếu cây có nhiều nhất một đỉnh bậc 1, thì ít nhất $$n-1$$ đỉnh còn lại có bậc $$\ge 2$$, suy ra tổng bậc $$\ge 1 + 2(n-1) = 2n-1 > 2(n-1)$$ — mâu thuẫn. Vậy cây có ít nhất 2 lá.

</details>

### Bài tập 3

Vì sao hệ thống tệp lý tưởng sử dụng cấu trúc cây thay vì đồ thị có chu trình tự do?

<details>
<summary>Đáp án</summary>

Cấu trúc cây đảm bảo mỗi tệp hoặc thư mục có **duy nhất một** đường dẫn đơn từ thư mục gốc. Nếu có chu trình, đường dẫn sẽ trở nên mơ hồ và các thao tác duyệt thư mục có thể lặp vô hạn nếu không có cơ chế kiểm soát.

</details>

### Bài tập 4

Một đồ thị không có chu trình gồm 12 đỉnh và 9 cạnh. Đồ thị này có bao nhiêu thành phần liên thông (tức số cây trong rừng)?

<details>
<summary>Đáp án</summary>

Trong một rừng gồm $$c$$ thành phần liên thông, ta có công thức $$\vert E\vert  = \vert V\vert  - c$$. Thay số: $$9 = 12 - c \implies c = 3$$ thành phần liên thông.

</details>

## Tóm tắt

1. **Cây** là đồ thị liên thông, không có chu trình; cây $$n$$ đỉnh luôn có đúng $$n-1$$ cạnh.
2. **Cây có gốc** xác định rõ quan hệ cha–con, lá, độ sâu và chiều cao.
3. **Cây khung** là cây con phủ toàn bộ tập đỉnh của một đồ thị liên thông.
4. Cấu trúc cây xuất hiện phổ biến trong hệ thống tệp, DOM và AST nhờ tính duy nhất của đường đi từ gốc.

Trong bài tiếp theo, ta sẽ tìm hiểu các thuật toán **duyệt cây**: preorder, inorder, postorder và level-order.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=zEQZpTizgLo">[Discrete Mathematics] Trees</a> — TrevTutor, tiếng Anh. Giới thiệu khái niệm cây trong toán rời rạc: liên thông và không chu trình.
- <a href="https://www.youtube.com/watch?v=tVuEZakQxhQ">Intro to Tree Graphs | Trees in Graph Theory, Equivalent Definitions</a> — Wrath of Math, tiếng Anh. Các định nghĩa tương đương của cây.
- <a href="https://www.youtube.com/watch?v=1XC3p2zBK34">Introduction to tree algorithms | Graph Theory</a> — WilliamFiset, tiếng Anh. Nhìn cây như một lớp đồ thị đặc biệt và chuyển tiếp sang thuật toán trên cây.
