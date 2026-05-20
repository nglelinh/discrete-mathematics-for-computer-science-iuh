---
layout: post
title: "Ứng dụng của Cây trong Khoa học Máy tính"
categories: chapter16
date: 2021-01-01
order: 4
required: false
lang: en
---

# Ứng dụng của Cây trong Khoa học Máy tính

Sau khi học định nghĩa, tính chất, cách duyệt và cây khung, câu hỏi lớn còn lại là: cây thật sự được dùng ở đâu? Câu trả lời là gần như khắp nơi trong khoa học máy tính: từ cấu trúc dữ liệu tìm kiếm, hệ thống file, chỉ mục cơ sở dữ liệu, cây quyết định, đến phân tích cú pháp và nén dữ liệu.

Bài này tập trung vào **ứng dụng của cây** để nối lý thuyết với thực hành. Mục tiêu không chỉ là biết thêm ví dụ, mà là nhìn ra vì sao khi một bài toán có phân cấp, có chia nhánh hoặc cần tìm kiếm hiệu quả, cấu trúc cây thường là lựa chọn tự nhiên và mạnh mẽ nhất.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Giải thích** mã hóa Huffman và ứng dụng trong nén dữ liệu.
- **Xây dựng** cây Huffman cho một bảng tần suất.
- **Mô tả** nguyên lý hoạt động của cây tìm kiếm nhị phân (BST).
- **Hiểu** ứng dụng của cây trong cơ sở dữ liệu (B-tree) và AI (decision tree).
- **So sánh** các cấu trúc cây khác nhau và trường hợp sử dụng.

**Từ khóa**: Mã hóa Huffman, cây Huffman, cây tìm kiếm nhị phân (BST), cây cân bằng (AVL), B-tree, cây quyết định (decision tree), nén dữ liệu.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter16/tree_applications_overview.svg" alt="Sơ đồ tổng quan các ứng dụng của cây trong khoa học máy tính" width="80%" height="80%">
  <figcaption style="text-align: center;">Hình 16.4 — Các ứng dụng chính của cây: nén, tìm kiếm, chỉ mục, AI, và biểu diễn cú pháp.</figcaption>
</p>
</figure>

## 1. Mã hóa Huffman

David Huffman phát minh thuật toán năm 1952 khi còn là sinh viên MIT. Thầy giáo của ông giao bài tập về nhà: tìm mã nhị phân tối ưu cho một bảng tần suất. Huffman không tìm được tài liệu tham khảo nào, nên ông tự nghĩ ra một giải pháp — và đó chính là thuật toán nén dữ liệu nổi tiếng nhất thế giới.

Mã hóa Huffman là thuật toán nén dữ liệu **không mất mát** (lossless) tối ưu: ký tự xuất hiện thường xuyên được mã ngắn hơn, ký tự hiếm được mã dài hơn.

### Thuật toán Xây dựng Cây Huffman

```
THUẬT TOÁN: Huffman(S)   // S là tập ký tự với tần suất
1. Tạo nút lá cho mỗi ký tự, với trọng số = tần suất
2. WHILE còn nhiều hơn 1 nút DO
3.     Lấy 2 nút có trọng số nhỏ nhất
4.     Tạo nút mới, trọng số = tổng 2 con
5.     Gán 2 nút làm con trái và phải
6. END WHILE
7. Gán mã: đường sang trái = 0, sang phải = 1
```

<div class="content-box example-box" markdown="1">
**Ví dụ**: Mã hóa văn bản "ABRACADABRA" (tần suất: A=5, B=2, R=2, C=1, D=1)

| Bước | Các nút hiện tại |
|:------|:----------------|
| Ban đầu | (A,5), (B,2), (R,2), (C,1), (D,1) |
| 1 | (A,5), (B,2), (R,2), (CD,2) |
| 2 | (A,5), (R,2), (B_CD,4) |
| 3 | (A,5), (R_B_CD,6) |
| 4 | (A_R_B_CD,11) |

Cây kết quả → mã: A=0, R=10, B=110, C=1110, D=1111.

Tổng bit mã hóa: 5×1 + 2×3 + 2×2 + 1×4 + 1×4 = 23 bit.
So với mã ASCII: 11 × 8 = 88 bit → tỉ lệ nén ~74%!
</div>

### Ứng dụng

- **JPEG, MP3, PNG, ZIP**: Huffman là thành phần của nhiều chuẩn nén.
- **Giao thức HTTP/2**: Dùng Huffman để nén header.
- **Fax machine**: Dùng Huffman để nén ảnh đen trắng.

## 2. Cây Tìm kiếm Nhị phân (BST)

Mỗi nút trong BST thỏa mãn:
- Khóa của nút > mọi khóa trong cây con trái
- Khóa của nút < mọi khóa trong cây con phải

<div class="content-box example-box" markdown="1">
**Tìm kiếm trên BST**:

Với cây chứa các số: {15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9}

Tìm x=13:
- So sánh với gốc (15): 13 < 15 → sang trái
- So sánh với 6: 13 > 6 → sang phải
- So sánh với 7: 13 > 7 → sang phải
- So sánh với 13: bằng → tìm thấy!

Chỉ mất 4 phép so sánh, thay vì 11 phép nếu tìm tuyến tính trong mảng.
</div>

**Độ phức tạp**: $$O(h)$$ với $$h$$ là chiều cao cây. Trung bình $$h = O(\log n)$$, xấu nhất $$h = O(n)$$ (cây suy biến).

### Cây Cân bằng: AVL và Red-Black

Để tránh trường hợp xấu nhất (cây suy biến thành danh sách), các cây cân bằng tự động điều chỉnh sau mỗi lần chèn/xóa:

- **Cây AVL**: chênh lệch chiều cao hai cây con ≤ 1.
- **Cây Đỏ-Đen (Red-Black Tree)**: mỗi nút có màu đỏ hoặc đen, đảm bảo cân bằng.

Cả hai đều đảm bảo $$O(\log n)$$ cho mọi thao tác.

<div class="content-box insight-box" markdown="1">
**Bạn dùng cây cân bằng mỗi ngày mà không biết!**
- `std::map` và `std::set` trong C++ dùng Red-Black Tree.
- `TreeMap` và `TreeSet` trong Java dùng Red-Black Tree.
- Hầu hết các hash map khi xảy ra va chạm đều chuyển sang cây cân bằng.
</div>

## 3. Cây trong Cơ sở Dữ liệu: B-tree

B-tree tổng quát hóa cây nhị phân thành cây m-phân, mỗi nút có thể chứa nhiều khóa và nhiều con. Đây là cấu trúc chỉ mục chuẩn trong cơ sở dữ liệu quan hệ.

- Mỗi nút chứa $$k$$ khóa và $$k+1$$ con.
- Chiều cao thấp (thường 3-4 tầng) ngay cả với hàng tỷ bản ghi.
- Được thiết kế để hoạt động hiệu quả với bộ nhớ phân cấp (cache, RAM, đĩa).

**Tại sao B-tree thắng BST trong CSDL?** Vì mỗi nút của B-tree chiếm đúng một block đĩa (thường 4KB), tối ưu hóa I/O. Với BST, mỗi nút chỉ là một giá trị nhỏ, gây lãng phí I/O.

<div class="content-box example-box" markdown="1">
**B-tree với bậc 4** (mỗi nút tối đa 3 khóa):

Một B-tree chứa 1 tỷ khóa chỉ cần chiều cao tối đa 5 (với bậc 1000). So với BST cần 30 tầng. Mỗi tầng là một I/O — sự khác biệt giữa 5 lần đọc đĩa và 30 lần!
</div>

## 4. Cây Quyết định trong AI

Cây quyết định (decision tree) là mô hình học máy dùng cấu trúc cây để đưa ra quyết định:

- **Nút trong**: kiểm tra một thuộc tính (feature).
- **Nhánh**: giá trị của thuộc tính.
- **Lá**: quyết định (phân lớp hoặc giá trị dự đoán).

Cây quyết định là nền tảng của:
- **Random Forest**: kết hợp nhiều cây quyết định.
- **XGBoost, LightGBM**: thuật toán mạnh nhất trong các cuộc thi Kaggle.

<div class="content-box example-box" markdown="1">
**Ví dụ đơn giản**: Cây quyết định dự đoán có đi chơi hay không:

```
           [Thời tiết?]
          /     |      \
      Nắng    Mây     Mưa
       /       |        \
    [Độ ẩm?]  Đi      [Gió?]
    /     \          /     \
  Cao    TB        Mạnh   Nhẹ
   |      |          |      |
 Không   Đi       Không    Đi
```
</div>

## 5. Các Cấu trúc Cây Khác

| Cấu trúc | Mục đích | Ứng dụng |
|:---|---|:---|
| **Trie** | Lưu trữ chuỗi | Tự động hoàn thành (autocomplete), kiểm tra chính tả |
| **Heap** | Ưu tiên | Hàng đợi ưu tiên, Heap Sort, thuật toán Dijkstra |
| **Segment Tree** | Truy vấn khoảng | Xử lý dãy số, bài toán RMQ (Range Minimum Query) |
| **Cây cú pháp (AST)** | Biểu diễn code | Trình biên dịch, phân tích code |
| **Cây họ (Genealogy)** | Quan hệ huyết thống | Phả hệ, sinh học |

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Mã hóa Huffman</h3>
<p>Nhập một văn bản và công cụ sẽ xây dựng cây Huffman, hiển thị mã nhị phân cho mỗi ký tự, và tính tỉ lệ nén. Quan sát cách các ký tự xuất hiện thường xuyên được mã ngắn hơn. <strong>Hãy thử:</strong> So sánh mã Huffman của một văn bản tiếng Việt với văn bản tiếng Anh.</p>
</div>

## Ứng dụng trong Khoa học Máy tính

Cây là cấu trúc dữ liệu linh hoạt nhất trong khoa học máy tính. Nó xuất hiện ở mọi cấp độ — từ kiến trúc vi xử lý (cây quyết định trong branch prediction) đến các ứng dụng web (DOM tree), từ nén file (Huffman) đến trí tuệ nhân tạo (decision tree, random forest).

Hiểu cây không chỉ giúp bạn giải bài toán hiệu quả hơn, mà còn giúp bạn *thiết kế* cấu trúc dữ liệu mới khi cần. Rất nhiều cấu trúc dữ liệu hiện đại (BKD-tree, R-tree, quadtree) là những biến thể của cây, được tối ưu cho các bài toán cụ thể.

## Bài tập

1. Xây dựng cây Huffman cho văn bản "AABBBCCCDDDDEEEEE" (A=2, B=3, C=3, D=4, E=5). Tính tỉ lệ nén.
2. Chèn các số [5, 3, 7, 2, 4, 6, 8] vào BST rỗng. Vẽ cây kết quả. Tìm kiếm 4 cần bao nhiêu bước?
3. Tìm hiểu: tại sao PostgreSQL và MySQL dùng B-tree (thực ra là B+tree) cho chỉ mục, thay vì BST hay hash table?
4. **Thử thách**: Cho dãy [8, 3, 10, 1, 6, 14, 4, 7, 13], chèn tuần tự vào BST rồi xóa nút 3. Vẽ cây kết quả sau mỗi bước.

<details>
<summary>Hướng dẫn bài 4</summary>

Xóa nút khỏi BST có 3 trường hợp:
1. Nút lá: xóa trực tiếp.
2. Nút có một con: thay nút bằng con của nó.
3. Nút có hai con: tìm nút kế tiếp (inorder successor — nút nhỏ nhất trong cây con phải), thay thế.

Trong trường hợp này, nút 3 có hai con (1 và 6). Inorder successor của 3 là 4 (nhỏ nhất trong cây con phải của 3). Thay 3 bằng 4.

Bài toán "xóa nút trên BST" là một câu hỏi phỏng vấn kinh điển. Hãy chắc chắn bạn hiểu cả ba trường hợp!
</details>

## Tóm tắt

- **Huffman**: nén không mất mát dùng cây nhị phân với tần suất.
- **BST**: tìm kiếm nhanh $$O(\log n)$$ trung bình.
- **Cây cân bằng**: AVL, Red-Black — đảm bảo $$O(\log n)$$.
- **B-tree**: chỉ mục CSDL — tối ưu I/O đĩa.
- **Cây quyết định**: mô hình AI/ML.
- **Trie, Heap, Segment Tree**: các biến thể cây cho bài toán đặc thù.

Bài này kết thúc chương Cây và cũng là bài cuối cùng của giáo trình Toán Rời Rạc cho Khoa học Máy tính. Chúc các bạn thành công!

## Tài liệu Tham khảo

1. David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proc. IRE*, 1952.
2. Rudolf Bayer, Edward M. McCreight, "Organization and Maintenance of Large Ordered Indexes," 1972 — bài báo B-tree gốc.
3. Thomas H. Cormen et al., *Introduction to Algorithms*, Chương 12 (BST), 18 (B-tree), 19 (Fibonacci heap).
4. Leo Breiman, "Random Forests," *Machine Learning*, 2001 — ứng dụng cây quyết định trong học máy.
