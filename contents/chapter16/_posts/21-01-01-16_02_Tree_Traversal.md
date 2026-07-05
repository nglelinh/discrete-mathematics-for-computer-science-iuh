---
layout: post
title: "Duyệt Cây"
categories: chapter16
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Mục 16.2 trình bày các thứ tự duyệt cây — preorder, inorder, postorder và level-order (BFS) — cùng độ phức tạp O(n) và ứng dụng trong compiler và cấu trúc dữ liệu."
---

Duyệt cây là thao tác thăm mọi đỉnh **đúng một lần** theo quy tắc xác định. Thứ tự duyệt quyết định semantics: serialize cây, in BST theo thứ tự, giải phóng bộ nhớ, hoặc in DOM theo tầng. Mục 16.2 so sánh bốn thứ tự chuẩn.

![Call tree đệ quy](/discrete-mathematics-for-computer-science-iuh/img/course/Algorithms-F6CallTreeMemoized.png)

<p class="textbook-figure-caption" data-figure="16.4">Call tree — duyệt DFS trên cây lời gọi hàm; preorder tương ứng thứ tự vào hàm.</p>
![Cây quyết định](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="16.5">Decision tree — mỗi nhánh là một lựa chọn; duyệt postorder thường dùng khi tính từ lá lên gốc.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** preorder, inorder, postorder trên cây nhị phân.
- **Thực hiện** level-order (BFS) trên cây có gốc.
- **Giải thích** ứng dụng: serialize, BST inorder, xóa cây.
- **Phân tích** độ phức tạp $$O(n)$$ cho mọi thứ tự duyệt.

**Từ khóa**: preorder, inorder, postorder, level-order, DFS trên cây, BFS trên cây.
</div>

## Ba thứ tự DFS trên cây nhị phân

Cho cây nhị phân với gốc, trái, phải:

| Thứ tự | Thứ tự thăm | Ứng dụng |
|:---|:---|:---|
| **Preorder** | Gốc → Trái → Phải | Copy cây, serialize prefix |
| **Inorder** | Trái → Gốc → Phải | BST → thứ tự tăng |
| **Postorder** | Trái → Phải → Gốc | Xóa cây, tính từ lá lên |

<div class="textbook-example" markdown="1">
**Ví dụ**: Cây

```
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

## Level-order (BFS)

Duyệt theo **tầng** từ gốc xuống — dùng hàng đợi (queue).

```python
from collections import deque

def level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        visit(node)
        for child in node.children:
            q.append(child)
```

<div class="textbook-theorem" markdown="1">
**Độ phức tạp**: Mọi thứ tự duyệt trên cây $$n$$ đỉnh chạy trong **$$O(n)$$** thời gian và **$$O(h)$$** bộ nhớ đệ quy (DFS) hoặc **$$O(w)$$** queue (BFS, $$w$$ = max width).
</div>

## Liên hệ Ch.12

DFS trên **cây** = preorder / inorder / postorder tùy thời điểm `visit`. BFS trên cây = level-order. Trên đồ thị tổng quát, DFS/BFS có thể lặp đỉnh nếu không đánh dấu `visited`.

## Bài tập

### Bài tập 1

Cho cây mục ví dụ. Viết preorder và postorder.

<details>
<summary>Đáp án</summary>

Preorder: A, B, D, E, C, F. Postorder: D, E, B, F, C, A.

</details>

### Bài tập 2

BST: gốc 8, trái 3, phải 10, ... (như slide 44). Inorder cho thứ tự nào?

<details>
<summary>Đáp án</summary>

**Tăng dần** theo key — tính chất BST.

</details>

### Bài tập 3

Vì sao postorder phù hợp khi `delete(node)` cần xóa con trước cha?

<details>
<summary>Đáp án</summary>

Postorder thăm con trước gốc — khi đến `node`, cả subtree đã được giải phóng.

</details>

## Tóm tắt

- **Preorder / inorder / postorder**: DFS, $$O(n)$$.
- **Level-order**: BFS, in theo tầng.
- Inorder BST = sorted order.
- Postorder = bottom-up computation / delete.

Trong bài tiếp theo: **cây khung** và **cây khung nhỏ nhất (MST)**.