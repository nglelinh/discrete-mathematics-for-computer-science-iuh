---
layout: post
title: "Duyệt Cây và Ứng dụng"
categories: chapter16
date: 2021-01-01
order: 2
required: true
lang: en
---

# Duyệt Cây và Ứng dụng

Có cây rồi chưa đủ; điều quan trọng là ta **đi qua** nó theo cách nào. Duyệt sai thứ tự có thể làm chương trình in sai biểu thức, tìm kiếm kém hiệu quả, hoặc xử lý nhầm ưu tiên của dữ liệu. Trong compiler, database, AI search hay thao tác trên DOM, thứ tự duyệt quyết định trực tiếp kết quả.

Các chiến lược **tree traversal** như preorder, inorder, postorder hay level-order chính là những “lộ trình” chuẩn để thăm cấu trúc phân nhánh. Hiểu chúng giúp ta không chỉ học thêm vài thuật toán, mà còn hiểu vì sao cùng một cây lại có thể phục vụ nhiều mục tiêu khác nhau chỉ bằng cách đổi cách đi.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Thực hiện** duyệt tiền thứ tự, trung thứ tự, hậu thứ tự trên cây nhị phân.
- **Xây dựng** cây từ biểu thức số học và đánh giá bằng duyệt cây.
- **Chuyển đổi** biểu thức giữa ba dạng: tiền tố, trung tố, hậu tố.
- **Hiểu** ứng dụng của duyệt cây trong trình biên dịch và máy tính.

**Từ khóa**: Tiền thứ tự (preorder), trung thứ tự (inorder), hậu thứ tự (postorder), biểu thức tiền tố (prefix), trung tố (infix), hậu tố (postfix), ký pháp Ba Lan (Polish notation).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter16/tree_traversal_types.svg" alt="Minh họa ba kiểu duyệt cây nhị phân: preorder, inorder, postorder" width="80%" height="80%">
  <figcaption style="text-align: center;">Hình 16.2 — Ba kiểu duyệt cây nhị phân. Mũi tên chỉ thứ tự thăm nút.</figcaption>
</p>
</figure>

## 1. Ba Kiểu Duyệt Cây Nhị phân

Giả sử ta có cây nhị phân với gốc $$r$$, cây con trái $$T_L$$, cây con phải $$T_R$$. Ba kiểu duyệt được định nghĩa đệ quy:

### Tiền thứ tự (Preorder) — NLR
1. Thăm gốc (N - Node)
2. Duyệt cây con trái (L - Left)
3. Duyệt cây con phải (R - Right)

### Trung thứ tự (Inorder) — LNR
1. Duyệt cây con trái
2. Thăm gốc
3. Duyệt cây con phải

### Hậu thứ tự (Postorder) — LRN
1. Duyệt cây con trái
2. Duyệt cây con phải
3. Thăm gốc

<div class="content-box example-box" markdown="1">
**Ví dụ**: Duyệt cây biểu thức $$(a - b) \times (c + d)$$

Cây: `×` là gốc, con trái là `-` (con của `a` và `b`), con phải là `+` (con của `c` và `d`)

| Kiểu duyệt | Kết quả |
|:---|---|
| Preorder | × - a b + c d |
| Inorder | a - b × c + d |
| Postorder | a b - c d + × |

**Nhận xét quan trọng**: Inorder cho biểu thức trung tố (cần thêm dấu ngoặc để rõ thứ tự), Postorder cho biểu thức hậu tố — dạng máy tính có thể tính trực tiếp bằng ngăn xếp!
</div>

<div class="content-box insight-box" markdown="1">
**Bí quyết ghi nhớ**: Tên gọi nói lên thứ tự thăm **gốc**:
- **Pre**order: gốc trước (pre) khi duyệt con
- **In**order: gốc ở giữa (in) sau con trái, trước con phải
- **Post**order: gốc sau (post) khi duyệt hết con
</div>

## 2. Cây Biểu thức Số học

Mỗi biểu thức số học có thể biểu diễn thành cây nhị phân:
- **Nút trong** là toán tử (+, -, ×, ÷)
- **Lá** là toán hạng (số hoặc biến)

### Duyệt cây để tính giá trị

```
THUẬT TOÁN: Tính-Biểu-Thức(node)
IF node là lá THEN RETURN giá trị của node
left_val ← Tính-Biểu-Thức(con trái của node)
right_val ← Tính-Biểu-Thức(con phải của node)
RETURN áp dụng toán tử của node lên left_val và right_val
```

Đây chính là **duyệt hậu thứ tự**! Máy tính bỏ túi HP dùng ký pháp Ba Lan ngược (RPN) — tức hậu tố — để người dùng nhập biểu thức mà không cần dấu ngoặc.

### Chuyển đổi giữa các ký pháp

| Ký pháp | Thứ tự | Ví dụ |
|:---|---|:---|
| Tiền tố (Prefix) | Toán tử → Toán hạng trái → Toán hạng phải | `× - a b + c d` |
| Trung tố (Infix) | Có dấu ngoặc | `(a - b) × (c + d)` |
| Hậu tố (Postfix) | Toán hạng trái → Toán hạng phải → Toán tử | `a b - c d + ×` |

<div class="content-box example-box" markdown="1">
**Tính biểu thức hậu tố bằng ngăn xếp**:

Với `a b - c d + ×`, giả sử a=5, b=2, c=3, d=4:

| Bước | Ký tự | Ngăn xếp |
|:---|:---|---:|
| 1 | 5 | [5] |
| 2 | 2 | [5, 2] |
| 3 | - | [3] (5-2=3) |
| 4 | 3 | [3, 3] |
| 5 | 4 | [3, 3, 4] |
| 6 | + | [3, 7] (3+4=7) |
| 7 | × | [21] (3×7=21) |

Kết quả: 21. Chỉ một ngăn xếp, không cần dấu ngoặc, không cần quy tắc ưu tiên toán tử!
</div>

## 3. Ứng dụng trong Trình Biên dịch

Khi bạn viết `x = (a + b) * c` trong C++, trình biên dịch thực hiện:

1. **Phân tích cú pháp** (parsing): chuyển dòng code thành cây cú pháp (AST).
2. **Duyệt cây**: dùng duyệt hậu thứ tự để sinh mã máy.
3. **Tối ưu hóa**: các phép biến đổi trên cây để tăng tốc.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Trực quan hóa Duyệt Cây</h3>
<p>Công cụ hiển thị cây nhị phân và cho phép bạn chạy từng bước của ba kiểu duyệt. Mỗi nút được tô sáng khi được thăm, và kết quả duyệt được cập nhật theo thời gian thực. <strong>Hãy thử:</strong> So sánh kết quả preorder, inorder, postorder của cùng một cây.</p>
</div>

## Ứng dụng trong Khoa học Máy tính

Duyệt cây xuất hiện trong hầu hết mọi phần mềm:

- **Trình biên dịch**: phân tích cú pháp, sinh mã, tối ưu hóa.
- **Máy tính bỏ túi**: dùng ký pháp hậu tố (RPN) để tính toán.
- **Cơ sở dữ liệu**: duyệt B-tree để tìm kiếm và chèn.
- **Xử lý XML/HTML**: DOM traversal.
- **Trò chơi (AI)**: duyệt cây trò chơi (minimax, alpha-beta pruning).

## Bài tập

1. Vẽ cây nhị phân biểu diễn biểu thức $$(3 + 4) \times (5 - 2) \div 7$$.
2. Viết kết quả duyệt preorder, inorder, postorder của cây ở câu 1.
3. Tính giá trị biểu thức hậu tố `5 3 + 8 2 - ×` bằng ngăn xếp.
4. **Thử thách**: Cho kết quả duyệt preorder = `F B A D C E G I H` và inorder = `A B C D E F G H I`. Hãy khôi phục cây nhị phân ban đầu.

<details>
<summary>Hướng dẫn bài 4</summary>

**Phương pháp**: Preorder cho biết gốc. Inorder cho biết cây con trái và phải.

1. Preorder[0] = F → gốc là F.
2. Inorder: A B C D E là cây con trái của F, G H I là cây con phải.
3. Preorder tiếp theo là B → gốc cây con trái là B.
4. Inorder trái của B: A (cây con trái của B). Inorder phải của B: C D E (cây con phải của B).
5. Tiếp tục với C D E: Preorder cho thấy D là gốc...
6. Và cứ thế!

Cây kết quả:
```
        F
       / \
      B   G
     / \   \
    A   D   I
       / \ /
      C   E H
```

Phương pháp này gọi là "khôi phục cây từ hai dãy duyệt" — một bài toán kinh điển trong phỏng vấn kỹ thuật.
</details>

## Tóm tắt

- **Preorder (NLR)**: gốc → trái → phải. Dùng để sao chép cây.
- **Inorder (LNR)**: trái → gốc → phải. Dùng để xuất cây theo thứ tự (trong BST).
- **Postorder (LRN)**: trái → phải → gốc. Dùng để tính giá trị biểu thức, giải phóng bộ nhớ.
- **Ký pháp Ba Lan**: tiền tố (prefix) ↔ preorder, hậu tố (postfix) ↔ postorder.
- **Tính hậu tố**: dùng ngăn xếp — không cần dấu ngoặc!

Trong bài tiếp theo, chúng ta sẽ học về cây khung và cây khung nhỏ nhất.

## Tài liệu Tham khảo

1. Jan Łukasiewicz, *Elements of Mathematical Logic*, 1929 — nguồn gốc ký pháp Ba Lan.
2. Thomas H. Cormen et al., *Introduction to Algorithms* (CLRS), Chương 12.
