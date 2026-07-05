---
layout: post
title: "Mã hóa Huffman và Cây Tìm kiếm Nhị phân"
categories: chapter16
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Mục 16.4 (tùy chọn) giới thiệu mã hóa Huffman prefix-free cho nén dữ liệu và BST — cấu trúc tìm kiếm O(log n) trung bình với inorder tăng dần."
---

Khi nén file ZIP hoặc tra cứu từ trong `std::map`, bạn đang dùng **cây** theo hai hướng khác nhau: Huffman gán mã nhị phân ngắn cho ký tự thường gặp; BST giữ dữ liệu có thứ tự để tìm kiếm nhanh. Mục 16.4 (tùy chọn) nối hai ứng dụng kinh điển này với duyệt cây đã học ở 16.2.

![Cây cú pháp trừu tượng](/discrete-mathematics-for-computer-science-iuh/img/course/Abstract_syntax_tree_for_Euclidean_algorithm.svg)

<p class="textbook-figure-caption" data-figure="16.7">AST — cây biểu diễn cấu trúc; BST và Huffman cũng là cây nhị phân có quy tắc trên nhãn/trọng số.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** cây Huffman từ tần suất ký tự bằng thuật toán greedy.
- **Giải thích** tính chất prefix-free và ứng dụng nén (ZIP, JPEG, MP3).
- **Định nghĩa** BST và thực hiện tìm kiếm, chèn trên cây nhị phân.
- **So sánh** BST, cây cân bằng (AVL/Red-Black) và hash table.

**Từ khóa**: Huffman coding, prefix-free, BST, skewed tree, AVL, Red-Black.
</div>

## Mã hóa Huffman

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Mã Huffman** là mã nhị phân gán cho từng ký tự sao cho **độ dài trung bình** của mã là nhỏ nhất (với tần suất cho trước). Cây Huffman là cây nhị phân có gốc: mỗi **lá** là ký tự, trọng số lá = tần suất; cạnh trái = 0, cạnh phải = 1.
</div>

**Thuật toán greedy**:

1. Khởi tạo rừng: mỗi ký tự là một lá, trọng số = tần suất.
2. Lặp: chọn **hai** nút có trọng số **nhỏ nhất**, gộp thành nút cha (trọng số = tổng).
3. Dừng khi còn **một** nút (gốc).
4. Đọc đường từ gốc đến lá → mã nhị phân.

<div class="textbook-theorem" markdown="1">
**Định lý**: Mã Huffman là **prefix-free** — không có mã nào là tiền tố của mã khác. Do đó giải mã không cần dấu phân cách: đọc bit liên tiếp cho đến khi khớp một lá.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Tần suất A=5, B=2, C=2, D=1, E=1.

**Bước gộp**: D+E → 2; rồi gộp với B hoặc C; tiếp tục đến một gốc.

**Mã minh họa** (một cây hợp lệ): A=0, B=10, C=11, D=110, E=111.

Độ dài trung bình nhỏ hơn mã cố định 8 bit/ký tự (ASCII).
</div>

**Ứng dụng**: DEFLATE (ZIP), JPEG, MP3, PNG — phần entropy coding thường dùng Huffman hoặc biến thể (Arithmetic coding).

## Cây tìm kiếm nhị phân (BST)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **BST** (Binary Search Tree) là cây nhị phân có gốc thỏa:

- Mọi giá trị ở **cây con trái** **nhỏ hơn** gốc.
- Mọi giá trị ở **cây con phải** **lớn hơn** gốc.
- Hai cây con cũng là BST.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: BST sau khi chèn 8, 3, 10, 1, 6, 14, 4, 7, 13:

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

**Inorder** (Trái → Gốc → Phải): 1, 3, 4, 6, 7, 8, 10, 13, 14 — **tăng dần**.
</div>

### Tìm kiếm và chèn

```
SEARCH(node, x):
    IF node = NULL RETURN NULL
    IF x = node.key RETURN node
    IF x < node.key RETURN SEARCH(node.left, x)
    ELSE RETURN SEARCH(node.right, x)
```

**Chèn**: Tìm vị trí NULL theo quy tắc BST, gán nút mới.

| Thao tác | Trung bình | Worst case |
|:---|:---:|:---:|
| Tìm kiếm | $$O(\log n)$$ | $$O(n)$$ |
| Chèn | $$O(\log n)$$ | $$O(n)$$ |
| Xóa | $$O(\log n)$$ | $$O(n)$$ |

**Worst $$O(n)$$**: Cây **lệch** (skewed) — chèn theo thứ tự tăng tạo cây giống danh sách liên kết.

## BST, cây cân bằng và hash table

| | BST thường | AVL / Red-Black | Hash table |
|:---|:---|:---|:---|
| Worst search | $$O(n)$$ | $$O(\log n)$$ | $$O(n)$$ |
| Trung bình | $$O(\log n)$$ | $$O(\log n)$$ | $$O(1)$$ |
| Thứ tự | Inorder có thứ tự | Có | Không |
| Dùng trong | Set nhỏ, học tập | `std::map`, `TreeMap` | `unordered_map`, dict |

**Khi chọn BST**: Cần **duyệt theo thứ tự** (range query, predecessor/successor) hoặc dữ liệu **ngẫu nhiên** giữ cây cân bằng trung bình. Hash table ưu tiên tra cứu đơn lẻ nhanh, không cần thứ tự.

## Bài tập

### Bài tập 1

Cho cây:

```
    M
   / \
  F   T
 /   / \
C   R   X
```

Viết preorder, inorder, postorder. Liệt kê lá. Chiều cao?

<details>
<summary>Đáp án</summary>

Preorder: M, F, C, T, R, X. Inorder: C, F, M, R, T, X. Postorder: C, F, R, X, T, M.

Lá: C, R, X. Chiều cao = 2 (đường M→T→X hoặc M→F→C).

</details>

### Bài tập 2

Tần suất A=8, B=3, C=3, D=2. Vẽ các bước gộp Huffman, gán mã, mã hóa "ABAC" — bao nhiêu bit?

<details>
<summary>Đáp án</summary>

Gộp D(2)+B(3) hoặc D+C trước → nút 5; tiếp gộp với C/B… Một mã hợp lệ: A=0 (1 bit), B=100, C=101, D=11 (tùy cây). "ABAC" ≈ 1+3+1+1 = 6 bit (kiểm tra theo cây bạn vẽ).

</details>

### Bài tập 3

Chèn lần lượt 5, 3, 7, 1, 4, 6, 8 vào BST rỗng. Vẽ cây. Inorder? Tìm 4 — đi qua nút nào?

<details>
<summary>Đáp án</summary>

Gốc 5; trái 3 (1, 4); phải 7 (6, 8). Inorder: 1, 3, 4, 5, 6, 7, 8.

Tìm 4: 5 → 3 → 4.

</details>

## Tóm tắt

- **Huffman**: greedy gộp hai tần suất nhỏ nhất; mã prefix-free, nén theo entropy.
- **BST**: trái < gốc < phải; inorder = tăng dần; $$O(\log n)$$ TB, $$O(n)$$ worst nếu lệch.
- Cây nền tảng: filesystem, DOM, AST, index, nén đa phương tiện.

Chúng ta đã hoàn thành Chương 16. Chương 17 mở rộng sang **đường đi ngắn nhất**, **sắp xếp topo** và ứng dụng đồ thị nâng cao.