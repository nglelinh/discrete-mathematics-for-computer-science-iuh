---
layout: post
title: "Mã hóa Huffman và Cây Tìm kiếm Nhị phân"
categories: chapter16
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Huffman prefix-free và greedy gộp tần suất; BST, tìm/chèn, inorder tăng; so sánh AVL/hash — ứng dụng nén và tìm kiếm."
---

<div class="textbook-epigraph" markdown="1">

"Short codes for frequent symbols — trees make compression optimal under a simple model."

<span class="epigraph-attribution">— Tinh thần Huffman (1952)</span>

</div>

Hai ứng dụng kinh điển của cây nhị phân: **mã Huffman** gán bit ngắn cho ký tự thường gặp (nén); **BST** giữ khóa có thứ tự để tìm/chèn theo chiều cao. Mục tùy chọn này nối cả hai với duyệt cây (Mục 16.2).

![Cây Huffman](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_huffman_example.svg)

<p class="textbook-figure-caption" data-figure="16.5">Cây Huffman: lá mang ký tự; đường gốc→lá là mã; greedy gộp hai nút nhẹ nhất.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây** cây Huffman từ bảng tần suất bằng greedy.
- **Giải thích** tính **prefix-free** và hệ quả giải mã.
- **Định nghĩa** BST; tìm kiếm và chèn; nêu inorder tăng dần.
- **So sánh** BST thường, cây cân bằng và bảng băm.

**Từ khóa**: Huffman coding, prefix-free, BST, skewed tree, AVL, Red-Black.

</div>

## 1. Mã hóa Huffman

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Mã Huffman** gán cho mỗi ký tự một xâu bit sao cho **độ dài trung bình** (theo tần suất cho trước) là nhỏ nhất trong lớp mã prefix nhị phân tương ứng. **Cây Huffman**: cây nhị phân có gốc; mỗi **lá** là một ký tự (trọng số = tần suất); cạnh trái/phải mã hóa bit 0/1.

</div>

**Thuật toán greedy**

1. Khởi tạo rừng: mỗi ký tự một lá, trọng số = tần suất.
2. Lặp: chọn **hai** nút trọng số **nhỏ nhất**, tạo nút cha (trọng số = tổng).
3. Dừng khi còn **một** nút (gốc).
4. Mã của ký tự = xâu bit trên đường từ gốc đến lá.

<div class="textbook-theorem" markdown="1">

**Định lý.** Mã Huffman là **prefix-free**: không mã nào là tiền tố của mã khác. Do đó giải mã không cần ký tự phân cách — đọc bit cho đến khi chạm một lá.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Tần suất A:5, B:2, C:2, D:1, E:1. Gộp D+E → 2; tiếp tục gộp các nút nhẹ nhất đến một gốc. Một cây hợp lệ có thể cho A mã ngắn (1 bit), các ký tự hiếm mã dài hơn. Độ dài trung bình nhỏ hơn mã cố định (ví dụ 3 bit/ký tự nếu $$2^3\ge 5$$ ký tự).

</div>

**Ứng dụng:** DEFLATE (ZIP), nhiều codec ảnh/âm thanh dùng Huffman hoặc biến thể (arithmetic coding) ở tầng entropy.

<div class="interactive-demo" markdown="1">
<div data-demo="huffman-coding"></div>
</div>
<script src="{{ '/public/js/huffman-coding.js' | relative_url }}"></script>

## 2. Cây tìm kiếm nhị phân (BST)

![BST](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_bst_example.svg)

<p class="textbook-figure-caption" data-figure="16.6">BST: mọi key trái nhỏ hơn gốc, mọi key phải lớn hơn gốc; inorder cho dãy tăng.</p>

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **BST** (*Binary Search Tree*) là cây nhị phân có gốc thỏa:

- mọi key ở **cây con trái** **nhỏ hơn** key gốc;
- mọi key ở **cây con phải** **lớn hơn** key gốc;
- hai cây con cũng là BST.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Chèn lần lượt 8, 3, 10, 1, 6, 14, 4, 7, 13 cho cây như hình.  
**Inorder**: 1, 3, 4, 6, 7, 8, 10, 13, 14 — tăng dần.

</div>

### Tìm kiếm và chèn

```text
SEARCH(node, x):
  IF node = null THEN return null
  IF x = node.key THEN return node
  IF x < node.key THEN return SEARCH(node.left, x)
  ELSE return SEARCH(node.right, x)
```

**Chèn:** đi như tìm kiếm đến chỗ `null`, gắn nút mới.

| Thao tác | Trung bình (cây ngẫu nhiên) | Worst case (lệch) |
|:---|:---:|:---:|
| Tìm / chèn / xóa | $$O(\log n)$$ | $$O(n)$$ |

Worst case: chèn đã sắp tăng tạo cây **lệch** (*skewed*) — giống danh sách liên kết.

## 3. BST, cây cân bằng và hash table

| | BST thường | AVL / Red-Black | Hash table |
|:---|:---|:---|:---|
| Worst search | $$O(n)$$ | $$O(\log n)$$ | $$O(n)$$ (hiếm nếu tốt) |
| Trung bình | $$O(\log n)$$ | $$O(\log n)$$ | $$O(1)$$ |
| Duyệt thứ tự | Inorder | Inorder | Không tự nhiên |
| Ví dụ | Học tập, set nhỏ | `std::map`, `TreeMap` | `dict`, `unordered_map` |

Chọn BST (hoặc cây cân bằng) khi cần **range query**, predecessor/successor, hoặc duyệt theo thứ tự. Hash ưu tiên tra cứu điểm nhanh, không yêu cầu thứ tự.

## Bài tập

### Bài tập 1

Cây

```text
    M
   / \
  F   T
 /   / \
C   R   X
```

Preorder, inorder, postorder? Lá? Chiều cao (depth gốc = 0)?

<details>
<summary>Đáp án</summary>

Preorder: M, F, C, T, R, X.  
Inorder: C, F, M, R, T, X.  
Postorder: C, F, R, X, T, M.  
Lá: C, R, X. Chiều cao = 2.

</details>

### Bài tập 2

Tần suất A=8, B=3, C=3, D=2. Mô tả các bước gộp Huffman (ý tưởng) và vì sao A thường nhận mã ngắn hơn D.

<details>
<summary>Đáp án</summary>

Luôn gộp hai nút nhẹ nhất trước (D với B hoặc C, …) → D/B/C nằm sâu hơn A. A tần suất cao nên gần gốc hơn → mã ngắn hơn, giảm độ dài trung bình.

</details>

### Bài tập 3

Chèn 5, 3, 7, 1, 4, 6, 8 vào BST rỗng. Inorder? Đường tìm 4?

<details>
<summary>Đáp án</summary>

Cây: gốc 5; trái 3 (1,4); phải 7 (6,8).  
Inorder: 1, 3, 4, 5, 6, 7, 8.  
Tìm 4: $$5 \to 3 \to 4$$.

</details>

### Bài tập 4

Chèn 1,2,3,4,5 vào BST rỗng. Độ phức tạp tìm 5?

<details>
<summary>Đáp án</summary>

Cây lệch phải; tìm 5 đi 5 nút — $$O(n)$$ worst case. Cây cân bằng (AVL) sẽ giữ $$O(\log n)$$.

</details>

## Tóm tắt

1. **Huffman**: greedy gộp hai tần suất nhỏ nhất; mã **prefix-free**; nén theo tần suất.
2. **BST**: trái $$<$$ gốc $$<$$ phải; inorder = sorted; $$O(\log n)$$ TB, $$O(n)$$ nếu lệch.
3. Cây cân bằng / hash: chọn theo nhu cầu thứ tự vs tra cứu điểm.

Chương 16 kết thúc. Chương 17 mở **đồ thị nâng cao**: đường ngắn nhất, topo sort, …
