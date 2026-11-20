---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Cây — Duyệt, Huffman, BST

**Toán Rời Rạc**

Tiết 44 (45 phút) — Rooted Trees, Traversal, Huffman Coding, BST

---

## Mục tiêu tiết học

- Định nghĩa cây có gốc (rooted tree) và các khái niệm cơ bản
- Thực hiện duyệt cây: preorder, inorder, postorder
- Hiểu ý tưởng mã hóa Huffman
- Nắm cơ bản Cây tìm kiếm nhị phân (BST)
- Liên hệ cây với đồ thị (tiết 36–37) và độ phức tạp (tiết 38–39)

---

## Cây là gì?

**Cây** (tree) là đồ thị **liên thông không chu trình**.

**Cây có gốc** (rooted tree): Chọn một đỉnh làm **gốc** (root).

**Thuật ngữ**:
- **Đỉnh** (node/vertex), **cạnh** (edge)
- **Lá** (leaf): đỉnh không có con
- **Cha** (parent), **con** (child), **anh em** (sibling)
- **Độ sâu** (depth): số cạnh từ gốc
- **Chiều cao** (height): độ sâu lớn nhất

---

## Tính chất cây

Với cây có $$n$$ đỉnh ($$n \geq 1$$):

1. Có đúng $$n - 1$$ cạnh
2. Liên thông + không chu trình
3. Giữa mọi cặp đỉnh có **đúng một** đường đi đơn
4. Thêm 1 cạnh → tạo đúng 1 chu trình

**Cây vs Đồ thị** (tiết 36): Cây là đồ thị đặc biệt — không có chu trình.

**Cây khung** (spanning tree): Tập cạnh nối tất cả đỉnh, không chu trình.

---

## Biểu diễn cây

**1. Danh sách con (adjacency list)**:
```python
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
```

**2. Mảng cha** (parent array): `parent[i]` = cha của đỉnh $$i$$

**3. Cấu trúc lồng** (nested): JSON, XML, HTML DOM, file system

**Ứng dụng**: Parse cú pháp, biểu thức, cây thư mục.

---

## Duyệt cây — Ba thứ tự

| Thứ tự | Thứ tự thăm | Ví dụ |
|:---|:---|:---|
| **Preorder** | Gốc → Trái → Phải | Copy cây, serialize |
| **Inorder** | Trái → Gốc → Phải | BST → thứ tự tăng |
| **Postorder** | Trái → Phải → Gốc | Xóa cây, tính toán |

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

Preorder: **A B D E C F**
Inorder: **D B E A C F**
Postorder: **D E B F C A**

---

## Code — Duyệt đệ quy

```python
def preorder(node):
    if node is None: return
    visit(node)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None: return
    inorder(node.left)
    visit(node)
    inorder(node.right)

def postorder(node):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    visit(node)
```

**Độ phức tạp**: $$O(n)$$ với $$n$$ đỉnh — mỗi đỉnh thăm đúng 1 lần.

---

## BFS trên cây — Duyệt theo tầng

**Level-order** (BFS): Duyệt từng tầng từ gốc xuống.

```
Tầng 0: A
Tầng 1: B, C
Tầng 2: D, E, F
```

```python
from collections import deque
def level_order(root):
    q = deque([root])
    while q:
        node = q.popleft()
        visit(node)
        for child in node.children:
            q.append(child)
```

**Ứng dụng**: In cây theo tầng, tìm đỉnh ở độ sâu $$k$$.

---

## Mã hóa Huffman

**Bài toán**: Mã hóa ký tự với tần suất khác nhau — ký tự **thường gặp** dùng mã **ngắn**.

**Ý tưởng**:
1. Mỗi ký tự = lá cây, trọng số = tần suất
2. Gộp 2 lá nhỏ nhất thành nút cha (tần suất = tổng)
3. Lặp đến còn 1 nút (gốc)
4. Gán 0/1 cho cạnh trái/phải → mã nhị phân

**Tính chất**: Mã **prefix-free** — không mã nào là tiền tố của mã khác.

---

## Ví dụ Huffman

Tần suất: A=5, B=2, C=2, D=1, E=1

**Bước gộp**:
1. D+E → 2
2. B+C → 4 (hoặc gộp với nút 2)
3. Tiếp tục...

**Kết quả** (minh họa): A=0, B=10, C=11, D=110, E=111

**Độ dài trung bình** < mã cố định (ASCII 8 bit).

**Ứng dụng**: ZIP, JPEG, MP3, PNG — nén dữ liệu.

---

## Cây tìm kiếm nhị phân (BST)

**BST**: Cây nhị phân thỏa:
- Mọi giá trị **cây trái** < gốc
- Mọi giá trị **cây phải** > gốc
- Hai cây con cũng là BST

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

**Inorder duyệt** → **1, 3, 4, 6, 7, 8, 10, 13, 14** (tăng dần).

---

## BST — Thao tác cơ bản

**Tìm kiếm** $$x$$:
```
SEARCH(node, x):
    IF node = NULL RETURN NULL
    IF x = node.key RETURN node
    IF x < node.key RETURN SEARCH(node.left, x)
    ELSE RETURN SEARCH(node.right, x)
```

| Thao tác | Trung bình | Worst |
|:---|:---:|:---:|
| Tìm kiếm | $$O(\log n)$$ | $$O(n)$$ |
| Chèn | $$O(\log n)$$ | $$O(n)$$ |
| Xóa | $$O(\log n)$$ | $$O(n)$$ |

**Worst $$O(n)$$**: Cây lệch (skewed) — giống danh sách liên kết.

---

## BST vs Cân bằng (preview)

**Cây cân bằng** (AVL, Red-Black): Đảm bảo $$O(\log n)$$ mọi thao tác.

| | BST thường | AVL / Red-Black |
|:---|:---|:---|
| Worst search | $$O(n)$$ | $$O(\log n)$$ |
| Cân bằng | Không đảm bảo | Tự cân bằng |
| Dùng trong | Set nhỏ | `std::map`, Java `TreeMap` |

**Hash table** $$O(1)$$ trung bình — nhưng không có thứ tự.

---

## Ứng dụng cây trong CS

- **File system**: Thư mục = cây có gốc
- **DOM HTML**: Parse và duyệt trang web
- **Biểu thức**: Cây biểu thức số học (compiler)
- **Quyết định**: Decision tree (ML)
- **Huffman**: Nén file
- **BST/Heap**: Priority queue, database index

**Liên hệ**: DFS (tiết 37) trên cây = preorder/inorder/postorder.

---

## Thực hành 1

Cho cây:
```
    M
   / \
  F   T
 /   / \
C   R   X
```

1. Viết kết quả preorder, inorder, postorder
2. Liệt kê các lá
3. Chiều cao cây?

---

## Thực hành 2

Tần suất: A=8, B=3, C=3, D=2.

1. Xây cây Huffman (vẽ từng bước gộp)
2. Gán mã nhị phân cho mỗi ký tự
3. Mã hóa chuỗi "ABAC" — bao nhiêu bit?

---

## Thực hành 3

Cho BST: chèn lần lượt 5, 3, 7, 1, 4, 6, 8.

1. Vẽ cây sau khi chèn
2. Inorder duyệt → kết quả?
3. Tìm kiếm 4 — đi qua những nút nào?

---

## Tóm tắt Tiết 44

- **Cây**: $$n$$ đỉnh, $$n-1$$ cạnh, không chu trình
- **Duyệt**: preorder, inorder, postorder — đều $$O(n)$$
- **Huffman**: nén tối ưu prefix-free theo tần suất
- **BST**: trái < gốc < phải; inorder = tăng dần
- Cây là cấu trúc nền của file system, DOM, index

---

## Liên hệ

**Thuật toán chính**: Huffman greedy — luôn gộp 2 tần suất nhỏ nhất.

**Edge case**: BST skewed → $$O(n)$$; cây 1 đỉnh; rừng (forest).

**Liên hệ**: Đồ thị (tiết 36–37) ↔ Cây (tiết 44) ↔ Big-O (tiết 38–39).

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Cây 10 đỉnh có bao nhiêu cạnh? Giải thích.

2. **Duyệt**: Cho cây 5 đỉnh (vẽ tùy ý). Viết preorder và postorder.

3. **BST**: Chèn 9, 5, 12, 3, 7 vào BST rỗng. Vẽ cây và inorder.

---

## Bài tập ôn tập (2/2)

4. **Huffman**: Tần suất X=10, Y=5, Z=5, W=2. Xây cây và tính độ dài mã trung bình.

5. **Bài 5**: So sánh BST ($$O(\log n)$$ TB) và hash table ($$O(1)$$ TB) cho từ điển 1 triệu từ. Khi nào chọn BST?
