---
layout: post
title: "Giới thiệu về Cây"
categories: chapter16
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu về Cây

Không phải mọi mạng liên kết đều rối như đồ thị tổng quát. Có những cấu trúc phân nhánh rất gọn, như thư mục trong máy tính, cây DOM của trang web, cây tổ chức nhân sự, cây cú pháp trong trình biên dịch hay cây quyết định trong machine learning.


Cây xuất hiện ở rất nhiều tầng của hệ thống, nên việc hiểu cấu trúc và cách thao tác trên cây sẽ giúp các khái niệm sau này bớt rời rạc hơn.
Đó là lý do **cây** trở thành một trong những cấu trúc quan trọng nhất của toán rời rạc và khoa học máy tính. Nó vừa đủ linh hoạt để biểu diễn phân cấp, vừa đủ có trật tự để thuật toán khai thác hiệu quả.

Học về cây là học cách mô hình hóa hệ thống phân cấp, đệ quy và lan truyền thông tin theo nhánh, những thứ xuất hiện liên tục từ cấu trúc dữ liệu đến AI. Đây cũng là bước tự nhiên sau chương đồ thị, khi ta muốn tập trung vào một lớp đồ thị đặc biệt nhưng cực kỳ hữu ích.

Trong bài này, chúng ta sẽ xây bộ khái niệm nền về cây để chuẩn bị cho các kỹ thuật duyệt, cây khung và ứng dụng ở các bài tiếp theo.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Định nghĩa** cây và các thuật ngữ liên quan: gốc, lá, cha, con, tổ tiên, hậu duệ.
- **Phân biệt** cây có gốc (rooted tree) và cây tự do (free tree).
- **Tính** số cạnh, số lá, chiều cao của cây.
- **Chứng minh** các tính chất cơ bản của cây.
- **Nhận biết** cây trong các bài toán CS: hệ thống tập tin, cây cú pháp, cây quyết định.

**Từ khóa**: Cây (tree), rừng (forest), gốc (root), lá (leaf), nút trong (internal node), cây con (subtree), cây m-phân (m-ary tree), cây nhị phân (binary tree).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter16/tree_types.svg" alt="Các loại cây: cây tự do, cây có gốc, cây nhị phân" width="80%" height="80%">
  <figcaption style="text-align: center;">Hình 16.1 — Ba cách nhìn về cấu trúc cây: cây tự do (trái), cây có gốc (giữa), cây nhị phân (phải).</figcaption>
</p>
</figure>

## 1. Định nghĩa Cây

Phần này đặt lại ngôn ngữ chung của bài học. Nắm chắc định nghĩa trước sẽ giúp các ví dụ và định lý phía sau trở nên dễ theo dõi hơn.

**Định nghĩa**: Cây (tree) là một đồ thị vô hướng, liên thông và không có chu trình đơn.

**Tính chất cơ bản của cây**:
- Giữa hai đỉnh bất kỳ có **đúng một** đường đi đơn.
- Cây có $$n$$ đỉnh thì có **đúng** $$n-1$$ cạnh.
- Nếu thêm một cạnh bất kỳ, đồ thị sẽ có chu trình.
- Nếu xóa một cạnh bất kỳ, đồ thị sẽ mất tính liên thông.

**Rừng** (forest): đồ thị không có chu trình (có thể không liên thông), mỗi thành phần liên thông là một cây.

<div class="content-box example-box" markdown="1">
**Ví dụ các cây**:

Đồ thị $$\{(A,B), (B,C), (B,D), (D,E)\}$$ — 5 đỉnh, 4 cạnh, liên thông, không chu trình → là cây.
</div>

<div class="content-box theorem-box" markdown="1">
**Định lý**: Mọi cây có $$n \geq 2$$ đỉnh đều có ít nhất 2 lá (đỉnh bậc 1).

*Chứng minh*: Giả sử cây chỉ có 0 hoặc 1 lá. Khi đó mọi đỉnh đều có bậc ≥ 2. Tổng số bậc ≥ 2n. Mà tổng số bậc = 2|E| = 2(n-1) = 2n-2. Mâu thuẫn. Vậy có ít nhất 2 lá.
</div>

## 2. Cây có Gốc

**Định nghĩa**: Cây có gốc (rooted tree) là cây trong đó một đỉnh được chọn làm **gốc** (root). Mỗi cạnh được định hướng ra xa gốc.

**Thuật ngữ quan trọng**:

| Thuật ngữ | Định nghĩa |
|:---|---|
| **Gốc** (root) | Đỉnh không có cha |
| **Lá** (leaf) | Đỉnh không có con |
| **Nút trong** (internal node) | Đỉnh có ít nhất một con |
| **Cha** (parent) của $$v$$ | Đỉnh $$u$$ duy nhất kề $$v$$ trên đường từ gốc |
| **Con** (child) của $$u$$ | Các đỉnh có cha là $$u$$ |
| **Tổ tiên** (ancestor) của $$v$$ | Các đỉnh trên đường từ gốc đến cha của $$v$$ |
| **Hậu duệ** (descendant) của $$v$$ | Các đỉnh có $$v$$ là tổ tiên |
| **Cây con** (subtree) | Một đỉnh và tất cả hậu duệ của nó |
| **Chiều cao** (height) | Độ dài đường đi dài nhất từ gốc đến lá |

<div class="content-box example-box" markdown="1">
**Ví dụ**: Xét cây thư mục:
```
/ (gốc)
├── home
│   ├── user1
│   └── user2
├── etc
│   └── config
└── var
    └── log
```
- Gốc: `/`
- Lá: `user1`, `user2`, `config`, `log`
- Chiều cao: 3 (từ `/` đến `user1` qua `home`)
- Cây con của `home`: gồm `home`, `user1`, `user2`
</div>

## 3. Cây m-phân và Cây Nhị phân

**Cây m-phân** (m-ary tree): mỗi nút trong có **tối đa** $$m$$ con.

- **Cây m-phân đầy đủ**: mỗi nút trong có **đúng** $$m$$ con.
- **Cây nhị phân** (binary tree): cây 2-phân.

**Tính chất của cây m-phân đầy đủ**:
- Có $$n$$ nút trong → tổng số đỉnh = $$mn + 1$$
- Số lá = $$(m-1)n + 1$$

<div class="content-box example-box" markdown="1">
**Ví dụ**: Một cây nhị phân đầy đủ (m=2) có 10 nút trong.
- Tổng số đỉnh: $$2 \times 10 + 1 = 21$$
- Số lá: $$(2-1) \times 10 + 1 = 11$$
</div>

**Cây nhị phân hoàn chỉnh** (complete binary tree): mọi tầng đều được lấp đầy, ngoại trừ tầng cuối cùng lấp đầy từ trái sang phải. Cấu trúc này được dùng để cài đặt **heap** — một cấu trúc dữ liệu quan trọng trong thuật toán sắp xếp và hàng đợi ưu tiên.

<div class="content-box insight-box" markdown="1">
**Một sự thật thú vị**: Cây nhị phân hoàn chỉnh có thể được lưu trong mảng mà không cần con trỏ! Nếu đánh số nút từ 1:
- Con trái của nút $$i$$: $$2i$$
- Con phải của nút $$i$$: $$2i + 1$$
- Cha của nút $$i$$: `floor(i/2)`

Đây là cách heap sort và priority queue được cài đặt hiệu quả trong thực tế.
</div>

<div class="interactive-tool" markdown="1">
<div data-demo="tree-traversal-visualizer"></div>
</div>
<script src="{{ '/public/js/tree-traversal-visualizer.js' | relative_url }}"></script>

## 4. Ứng dụng CS Quan trọng

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Cây xuất hiện trong hầu hết mọi lĩnh vực của khoa học máy tính:

- **Hệ thống tập tin**: Cấu trúc thư mục là một cây (trên Unix, mọi thứ đều bắt đầu từ `/`).
- **Cây cú pháp (AST)**: Trình biên dịch phân tích code thành cây cú pháp trừu tượng.
- **DOM (Document Object Model)**: Mỗi trang web là một cây các thẻ HTML.
- **Cơ sở dữ liệu**: B-tree và B+tree là cấu trúc chỉ mục chuẩn trong CSDL quan hệ.
- **Mạng máy tính**: Giao thức spanning tree ngăn vòng lặp trong mạng Ethernet.
- **AI**: Cây quyết định (decision tree) dùng trong học máy.
- **Nén dữ liệu**: Mã hóa Huffman (bài sau) dùng cây nhị phân để nén.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Xây dựng Cây</h3>
<p>Công cụ cho phép bạn xây dựng cây tương tác: thêm nút, xóa nút, chọn gốc. Cây tự động cập nhật và hiển thị các thông số: số nút, số lá, chiều cao. <strong>Hãy thử:</strong> Xây dựng cây thư mục của máy tính bạn và xem nó trông như thế nào.</p>
</div>

## Bài tập

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

1. Cho đồ thị với 8 đỉnh và 7 cạnh, liên thông. Đây có phải cây không? Giải thích.
2. Một cây nhị phân đầy đủ có 15 nút trong. Tính tổng số đỉnh và số lá.
3. Vẽ cây thư mục của dự án lập trình bạn đang làm. Xác định gốc, lá, chiều cao.
4. **Thử thách**: Chứng minh rằng trong một cây có gốc, số lá = 1 + tổng của (bậc mỗi nút - 1) trên tất cả các nút trong.

<details>
<summary>Hướng dẫn bài 4</summary>

Gọi $$L$$ là số lá, $$I$$ là số nút trong. Tổng số nút $$n = L + I$$.

Mỗi nút trong có ít nhất 1 con, và mọi nút (trừ gốc) đều có đúng 1 cha. 

Có $$n-1$$ cạnh (vì là cây). Mỗi cạnh nối một nút với cha của nó.

Tổng số con = số cạnh = $$n-1$$.

Tổng số con cũng = tổng số con của các nút trong = $$\sum_{v \in I} \deg(v)$$ (trong đó deg(v) là số con của v).

Vậy: $$\sum_{v \in I} \deg(v) = n - 1 = L + I - 1$$

Suy ra: $$L = \sum_{v \in I} (\deg(v) - 1) + 1$$

Với cây nhị phân đầy đủ, mỗi nút trong có deg(v) = 2, nên $$L = I \times 1 + 1 = I + 1$$ — đúng với công thức đã học.
</details>

## Tóm tắt

- **Cây**: đồ thị liên thông, không chu trình — $$n$$ đỉnh, $$n-1$$ cạnh.
- **Cây có gốc**: chọn một đỉnh làm gốc, định hướng ra xa.
- **Cây m-phân**: mỗi nút trong có tối đa m con.
- **Cây nhị phân**: trường hợp m = 2, quan trọng nhất trong CS.
- **Cây nhị phân hoàn chỉnh**: có thể lưu trong mảng không cần con trỏ.

Trong bài tiếp theo, chúng ta sẽ học cách duyệt cây — kỹ thuật thăm mọi nút trên cây theo thứ tự có hệ thống.

## Tài liệu Tham khảo

1. Thomas H. Cormen et al., *Introduction to Algorithms* (CLRS), Chương 10 (cấu trúc cây) và Chương 12 (cây nhị phân tìm kiếm).
2. Donald E. Knuth, *The Art of Computer Programming*, Vol. 1, Section 2.3.
