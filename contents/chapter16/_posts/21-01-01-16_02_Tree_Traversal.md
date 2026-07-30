---
layout: post
title: "Duyệt Cây"
categories: chapter16
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Preorder, inorder, postorder trên cây nhị phân; level-order (BFS); độ phức tạp O(n); ứng dụng serialize, BST, xóa cây."
---

<div class="textbook-epigraph" markdown="1">

"The order in which we visit the nodes is not cosmetic — it is the algorithm."

<span class="epigraph-attribution">— Tinh thần duyệt cây</span>

</div>

**Duyệt cây** là thao tác thăm mọi đỉnh **đúng một lần** theo quy tắc cố định. Thứ tự quyết định semantics: serialize, in BST theo thứ tự tăng, giải phóng bộ nhớ bottom-up, hay in DOM theo tầng. Mục này so sánh preorder, inorder, postorder và level-order.

![Duyệt cây nhị phân](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_binary_traversal.svg)

<p class="textbook-figure-caption" data-figure="16.3">Cùng một cây nhị phân: ba thứ tự DFS khác nhau bởi thời điểm thăm gốc so với hai con.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** preorder, inorder, postorder trên cây nhị phân.
- **Thực hiện** level-order (BFS) trên cây có gốc.
- **Giải thích** ứng dụng: serialize, inorder BST, xóa cây.
- **Phân tích** độ phức tạp $$O(n)$$ và bộ nhớ phụ.

**Từ khóa**: preorder, inorder, postorder, level-order, DFS trên cây, BFS trên cây.

</div>

## 1. Ba thứ tự DFS trên cây nhị phân

Cho nút có con trái và con phải (có thể rỗng):

| Thứ tự | Quy tắc thăm | Ứng dụng điển hình |
|:---|:---|:---|
| **Preorder** (NLR) | Gốc → Trái → Phải | Copy cây, serialize prefix, “vào” hàm |
| **Inorder** (LNR) | Trái → Gốc → Phải | BST → dãy tăng |
| **Postorder** (LRN) | Trái → Phải → Gốc | Xóa cây, tính biểu thức từ lá lên |

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Cây

```text
        A
       / \
      B   C
     / \   \
    D   E   F
```

- Preorder: **A, B, D, E, C, F**
- Inorder: **D, B, E, A, C, F**
- Postorder: **D, E, B, F, C, A**

</div>

```python
def preorder(node):
    if node is None:
        return
    visit(node)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    visit(node)
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    visit(node)
```

Trên cây **không nhị phân** (nhiều con), preorder = gốc rồi lần lượt các con; postorder = các con rồi gốc; “inorder” chỉ chuẩn hóa tự nhiên cho cây nhị phân (hoặc cần quy ước thứ tự con).

## 2. Level-order (BFS)

Duyệt theo **tầng** từ gốc xuống — hàng đợi (*queue*).

```python
from collections import deque

def level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        visit(node)
        for child in getattr(node, "children",
                             [c for c in (node.left, node.right) if c]):
            q.append(child)
```

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Cùng cây Ví dụ 1: level-order **A, B, C, D, E, F**.

</div>

## 3. Độ phức tạp và liên hệ Chương 12

<div class="textbook-theorem" markdown="1">

**Định lý.** Trên cây $$n$$ đỉnh, mọi thứ tự duyệt trên (DFS hoặc BFS) chạy trong thời gian $$O(n)$$. Bộ nhớ phụ: $$O(h)$$ cho stack đệ quy DFS ($$h$$ = chiều cao), hoặc $$O(w)$$ cho queue BFS ($$w$$ = độ rộng tầng lớn nhất).

</div>

Trên **đồ thị** tổng quát, DFS/BFS cần tập `visited` để không lặp đỉnh. Trên **cây** (có gốc, cạnh chỉ cha–con), mỗi đỉnh được vào cấu trúc đúng một lần nếu chỉ đi xuống con — không cần đánh dấu chu trình.

| Cấu trúc | Tương ứng duyệt cây |
|:---|:---|
| DFS “thăm khi vào” | Preorder |
| DFS “thăm giữa hai con” (nhị phân) | Inorder |
| DFS “thăm khi ra” | Postorder |
| BFS | Level-order |

## 4. Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="tree-traversal-visualizer"></div>
</div>
<script src="{{ '/public/js/tree-traversal-visualizer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Với cây Ví dụ 1, viết preorder và postorder.

<details>
<summary>Đáp án</summary>

Preorder: A, B, D, E, C, F.  
Postorder: D, E, B, F, C, A.

</details>

### Bài tập 2

Vì sao **inorder** trên BST cho dãy key tăng dần?

<details>
<summary>Đáp án</summary>

Theo định nghĩa BST, mọi key trái $$<$$ gốc $$<$$ mọi key phải. Inorder thăm trái → gốc → phải nên ghép ba đoạn đã sắp thành dãy tăng toàn cục (quy nạp theo chiều cao).

</details>

### Bài tập 3

Vì sao **postorder** phù hợp khi `delete(node)` phải giải phóng con trước cha?

<details>
<summary>Đáp án</summary>

Postorder thăm hai con trước gốc. Khi đến `node`, toàn bộ subtree đã được giải phóng — không còn tham chiếu “treo” từ cha tới vùng nhớ đã free.

</details>

### Bài tập 4

Cây đầy đủ nhị phân chiều cao $$h$$ (gốc depth 0) có bao nhiêu nút? Level-order thăm nút cuối cùng là nút nào về mặt vị trí?

<details>
<summary>Đáp án</summary>

Số nút $$n = 2^{h+1}-1$$. Level-order thăm theo tầng; nút cuối là lá phải cùng của tầng $$h$$.

</details>

## Tóm tắt

1. **Preorder / inorder / postorder**: DFS; khác thời điểm `visit`.
2. **Level-order**: BFS theo tầng.
3. Tất cả $$O(n)$$; inorder BST = sorted; postorder = bottom-up.
4. Cây không cần `visited` như đồ thị có chu trình.

Trong bài tiếp theo: **cây khung** và **MST** (Kruskal, Prim).
