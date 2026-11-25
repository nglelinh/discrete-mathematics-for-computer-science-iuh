---
layout: post
title: "Mã hóa Huffman và Cây Tìm kiếm Nhị phân"
categories: chapter16
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Mã Huffman không tiền tố (prefix-free) và thuật toán tham lam gộp tần suất; cây tìm kiếm nhị phân (BST), tìm kiếm/chèn, duyệt inorder tăng dần; so sánh với AVL và bảng băm."
---

> **Câu chuyện mở đầu:** Nếu bạn nén một văn bản tiếng Việt bằng mã ASCII cố định (8 bit cho mỗi chữ cái), chữ `a` xuất hiện hàng nghìn lần lại tốn y hệt số bit như chữ `z` hiếm gặp! Năm 1951, khi đang là sinh viên cao học tại MIT làm bài tập thay cho kỳ thi cuối kỳ, **David Huffman** đã nghĩ ra thuật toán xây cây từ dưới lên tạo ra **bộ mã tiền tố tối ưu tuyệt đối** — nền tảng của ZIP, JPEG và MP3 ngày nay! Song hành cùng nó là **Cây Tìm kiếm Nhị phân (BST)**, cấu trúc dữ liệu giúp tìm kiếm, chèn và xóa trong $$O(\log n)$$!

<div class="textbook-epigraph" markdown="1">

"Short codes for frequent symbols — trees make compression optimal under a simple model."

<span class="epigraph-attribution">— Tinh thần Huffman (1952)</span>

</div>

Hai ứng dụng kinh điển của cây nhị phân trong khoa học máy tính là **mã hóa Huffman** (gán chuỗi bit ngắn cho các ký tự xuất hiện thường xuyên để nén dữ liệu) và **cây tìm kiếm nhị phân (BST)** (duy trì thứ tự khóa để tìm kiếm và chèn theo chiều cao cây). Bài học tùy chọn này kết nối trực tiếp cả hai cấu trúc với nội dung duyệt cây ở Mục 16.2.

![Cây Huffman](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_huffman_example.svg)

<p class="textbook-figure-caption" data-figure="16.5">Cây Huffman: mỗi nút lá ứng với một ký tự, đường từ gốc đến lá tạo thành mã bit, được xây dựng bằng cách gộp dần hai nút nhẹ nhất.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** cây Huffman từ bảng tần suất bằng thuật toán tham lam.
- **Giải thích** tính chất **không tiền tố** (*prefix-free*) và lợi ích của nó khi giải mã.
- **Định nghĩa** BST, thực hiện tìm kiếm/chèn và giải thích vì sao duyệt inorder cho dãy tăng dần.
- **So sánh** BST thông thường, cây tìm kiếm tự cân bằng và bảng băm.

**Từ khóa**: Huffman coding, prefix-free, BST, skewed tree, AVL, Red-Black.

</div>

### Video ngắn: Mã Huffman

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/huffman-coding.mp4"></video>
</div>

Video dài khoảng 3 phút 7 giây: đếm tần suất ký tự trong chuỗi ABRACADABRA (5, 2, 2, 1, 1 — cùng bộ tần suất với Ví dụ 1), gộp dần hai nút nhẹ nhất bằng hàng đợi ưu tiên, gán bit 0/1 cho nhánh trái/phải để nén xuống 23 bit thay vì 33 bit, minh họa giải mã bằng con trỏ đi trên cây nhờ tính chất prefix-free, ví dụ $$A = 0, B = 01, C = 1$$ cho thấy mã không prefix-free gây nhập nhằng, bài luyện tập MISSISSIPPI (21 bit so với 22 bit của mã độ dài cố định), và giải thích vì sao cách gộp tham lam này tối ưu. Video về các thứ tự duyệt cây nằm ở Mục 16.2.

## Bản đồ kiến thức nền: Mã hóa Huffman và Cây Tìm kiếm Nhị phân (BST)

### 1. Mã Tiền tố (Prefix Code) & Thuật toán Tham lam Huffman
- **Mã tiền tố:** Không có mã của ký tự nào là phần đầu (prefix) của mã ký tự khác $$\iff$$ mọi ký tự đều nằm ở **nút lá** của một cây nhị phân (giải mã mượt mà không cần dấu phân cách!).
- **Thuật toán Huffman:** Lặp lại thao tác dùng Min-Heap lấy ra **hai nút có tần suất nhỏ nhất**, gộp thành nút cha có trọng số bằng tổng hai con, cho đến khi còn đúng 1 gốc — chứng minh được là đạt **độ dài mã trung bình nhỏ nhất có thể** (sát cận entropy Shannon $$H = -\sum p_i \log_2 p_i$$)!

### 2. Cây Tìm kiếm Nhị phân (BST) & Cân bằng Cây
- **Bất biến BST:** Tại mọi nút $$u$$, **toàn bộ** cây con trái đều có khóa $$< u$$ và **toàn bộ** cây con phải đều có khóa $$> u$$ (nhờ đó duyệt **Inorder** luôn ra dãy tăng dần!).
- **Cảnh báo suy biến:** Nếu chèn dãy đã sắp xếp $$1, 2, 3, \dots, n$$ vào BST thường, cây biến thành danh sách liên kết cao $$n$$ (tìm kiếm tụt xuống $$O(n)$$) — động lực ra đời các cây tự cân bằng **AVL, Red–Black và B-tree**!

## Ví dụ tính tay cầm tay chỉ việc: Dựng cây mã Huffman cho 4 ký tự

Cho 4 ký tự với xác suất xuất hiện: **A: $$0.45$$**, **B: $$0.30$$**, **C: $$0.15$$**, **D: $$0.10$$**.
1. **Bước 1:** Hai tần suất nhỏ nhất là `D(0.10)` và `C(0.15)` $$\to$$ gộp thành nút `(CD: 0.25)`. Hàng đợi còn: `{A: 0.45, B: 0.30, CD: 0.25}`.
2. **Bước 2:** Hai tần suất nhỏ nhất là `CD(0.25)` và `B(0.30)` $$\to$$ gộp thành `(B+CD: 0.55)`. Hàng đợi còn: `{A: 0.45, B+CD: 0.55}`.
3. **Bước 3:** Gộp hai nút cuối thành gốc `(1.00)`. Gán cạnh trái `0`, cạnh phải `1`:
   - `A` $$\to$$ `0` (1 bit)
   - `B` $$\to$$ `10` (2 bit)
   - `C` $$\to$$ `110` (3 bit)
   - `D` $$\to$$ `111` (3 bit)
4. **So sánh hiệu quả nén:**
   - Mã cố định: tốn **$$2.00$$ bit/ký tự**.
   - Mã Huffman: $$0.45(1) + 0.30(2) + 0.15(3) + 0.10(3) = 0.45 + 0.60 + 0.45 + 0.30 = \mathbf{1.80}$$ **bit/ký tự** (gần sát giới hạn lý thuyết entropy Shannon $$H \approx 1.78$$ bit!).

### Khung giải thích: 4 bước làm chủ Huffman và thao tác Xóa nút trên BST (nên đọc chậm)

#### Bước 1: Luôn dùng Min-Heap cho Huffman ($$O(k\log k)$$)
Mỗi bước gộp giảm số cây đi 1, nên với $$k$$ ký tự cần đúng $$k - 1$$ lần gộp; ký tự ít xuất hiện nhất luôn bị đẩy xuống tầng sâu nhất (mã dài nhất).

#### Bước 2: Kiểm tra bất biến BST trên TOÀN BỘ cây con (không chỉ con trực tiếp!)
Một lỗi kinh điển là chỉ kiểm tra `left < root < right` — phải kiểm tra `max(cây trái) < root < min(cây phải)`!

#### Bước 3: Xử lý 3 trường hợp khi Xóa nút trên BST
- Nút lá: xóa thẳng.
- Có 1 con: nối thẳng cha với con duy nhất đó.
- Có 2 con: thay khóa nút đó bằng **phần tử kế tiếp Inorder** (nút nhỏ nhất của cây con phải — vốn chỉ có tối đa 1 con phải!), rồi xóa nút kế tiếp ấy!

#### Bước 4: Giữ cây cân bằng để khóa chặt hiệu năng $$O(\log n)$$
Tốc độ mọi thao tác BST đều là $$O(h)$$; các cơ chế xoay cây (AVL, Red–Black) bảo đảm $$h = O(\log n)$$ trong mọi kịch bản đầu vào!

$$
\text{Min-Heap tần suất} \xrightarrow{\text{Gộp 2 nhỏ nhất}} \text{Mã Huffman tối ưu}
\qquad \Big\vert \qquad
\text{Bất biến BST} \xrightarrow{\text{Inorder}} \text{Dãy tăng dần } O(h).
$$

## Mã hóa Huffman

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Mã Huffman** gán cho mỗi ký tự một xâu bit sao cho **độ dài mã trung bình** (theo bảng tần suất cho trước) là nhỏ nhất trong lớp các mã nhị phân không tiền tố. **Cây Huffman** là một cây nhị phân có gốc trong đó mỗi **lá** đại diện cho một ký tự (có trọng số bằng tần suất), còn các nhánh trái và phải lần lượt gán bit 0 và 1.

</div>

**Thuật toán tham lam xây dựng cây Huffman**

1. Khởi tạo rừng ban đầu: mỗi ký tự là một nút lá có trọng số bằng tần suất của nó.
2. Lặp: chọn **hai** nút có trọng số **nhỏ nhất**, tạo một nút cha nối hai nút này với trọng số bằng tổng trọng số của chúng.
3. Dừng khi rừng chỉ còn **một** nút duy nhất (đó là gốc của cây).
4. Mã của mỗi ký tự là xâu bit đọc dọc theo đường đi từ gốc đến lá tương ứng.

<div class="textbook-theorem" markdown="1">

**Định lý.** Mã Huffman có tính chất **không tiền tố** (*prefix-free*): không có từ mã nào là phần đầu (tiền tố) của một từ mã khác. Nhờ đó, quá trình giải mã không cần ký tự phân cách — chỉ cần đọc từng bit đi từ gốc cho đến khi chạm một nút lá.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Cho bảng tần suất A:5, B:2, C:2, D:1, E:1. Đầu tiên gộp D và E thành nút có trọng số 2, sau đó tiếp tục gộp hai nút nhẹ nhất ở mỗi bước cho đến khi còn một gốc duy nhất. Một cây Huffman hợp lệ sẽ gán mã rất ngắn cho A (1 bit) và mã dài hơn cho các ký tự ít gặp hơn, giúp độ dài trung bình nhỏ hơn đáng kể so với mã độ dài cố định (cần 3 bit/ký tự vì $$2^3 \ge 5$$).

</div>

**Ứng dụng:** chuẩn nén DEFLATE (dùng trong ZIP) cùng nhiều bộ mã hóa ảnh và âm thanh sử dụng mã Huffman hoặc các biến thể (như mã hóa số học *arithmetic coding*) ở tầng nén entropy.

<div class="interactive-demo" markdown="1">
<div data-demo="huffman-coding"></div>
</div>
<script src="{{ '/public/js/huffman-coding.js' | relative_url }}"></script>

## Cây tìm kiếm nhị phân (BST)

![BST](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_bst_example.svg)

<p class="textbook-figure-caption" data-figure="16.6">BST: mọi khóa bên trái đều nhỏ hơn gốc, mọi khóa bên phải đều lớn hơn gốc; duyệt inorder cho dãy tăng dần.</p>

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Cây tìm kiếm nhị phân (BST)** là cây nhị phân có gốc thỏa mãn đồng thời ba điều kiện:

- mọi khóa trong **cây con trái** đều **nhỏ hơn** khóa của nút gốc;
- mọi khóa trong **cây con phải** đều **lớn hơn** khóa của nút gốc;
- cả hai cây con trái và phải đều là BST.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Chèn lần lượt các khóa 8, 3, 10, 1, 6, 14, 4, 7, 13 vào BST rỗng ta thu được cây như hình minh họa.  
Duyệt **inorder** cho dãy tăng dần: 1, 3, 4, 6, 7, 8, 10, 13, 14.

</div>

### Tìm kiếm và chèn

```text
SEARCH(node, x):
  IF node = null THEN return null
  IF x = node.key THEN return node
  IF x < node.key THEN return SEARCH(node.left, x)
  ELSE return SEARCH(node.right, x)
```

**Thao tác chèn:** đi theo nhánh trái/phải tương tự như khi tìm kiếm cho đến khi gặp vị trí `null`, sau đó gắn nút mới vào đó.

| Thao tác | Trung bình (cây ngẫu nhiên) | Trường hợp xấu nhất (cây lệch) |
|:---|:---:|:---:|
| Tìm kiếm / chèn / xóa | $$O(\log n)$$ | $$O(n)$$ |

Trường hợp xấu nhất xảy ra khi chèn một dãy khóa đã sắp xếp tăng dần (hoặc giảm dần), tạo thành cây **lệch** (*skewed*) có cấu trúc suy biến giống danh sách liên kết.

## So sánh BST, cây cân bằng và bảng băm

| Tiêu chí | BST thường | Cây AVL / Đỏ–Đen | Bảng băm (*Hash table*) |
|:---|:---|:---|:---|
| Tìm kiếm xấu nhất | $$O(n)$$ | $$O(\log n)$$ | $$O(n)$$ (hiếm gặp nếu hàm băm tốt) |
| Tìm kiếm trung bình | $$O(\log n)$$ | $$O(\log n)$$ | $$O(1)$$ |
| Duyệt có thứ tự | Inorder | Inorder | Không hỗ trợ tự nhiên |
| Ví dụ thực tế | Học tập, tập dữ liệu nhỏ | `std::map`, `TreeMap` | `dict`, `unordered_map` |

Nên chọn BST (hoặc cây tự cân bằng) khi cần **truy vấn theo đoạn** (*range query*), tìm phần tử đứng trước/sau (*predecessor/successor*) hoặc duyệt dữ liệu theo thứ tự. Ngược lại, bảng băm phù hợp khi ưu tiên tra cứu điểm nhanh mà không cần thứ tự khóa.

### Minh họa tương tác

Minh họa gộp từng cặp nút nhẹ nhất để dựng cây Huffman, tạo bảng mã tiền tố và mã hóa/giải mã thông điệp; chuyển sang thẻ BST để thử thao tác chèn, tìm và xóa nút:

<div class="interactive-demo" markdown="1">
<div data-demo="tree-explainer" data-mode="huffman"></div>
</div>
<script src="{{ '/public/js/explainers/tree-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Xét cây nhị phân sau:

```text
    M
   / \
  F   T
 /   / \
C   R   X
```

Hãy xác định các thứ tự duyệt preorder, inorder, postorder, danh sách các nút lá và chiều cao của cây (quy ước gốc có độ sâu 0).

<details>
<summary>Đáp án</summary>

Preorder: M, F, C, T, R, X.  
Inorder: C, F, M, R, T, X.  
Postorder: C, F, R, X, T, M.  
Các nút lá: C, R, X. Chiều cao của cây bằng 2.

</details>

### Bài tập 2

Cho bảng tần suất A=8, B=3, C=3, D=2. Trình bày ý tưởng các bước gộp trong thuật toán Huffman và giải thích vì sao ký tự A nhận mã ngắn hơn D.

<details>
<summary>Đáp án</summary>

Thuật toán luôn gộp hai nút nhẹ nhất ở mỗi bước (bắt đầu từ D với B hoặc C, rồi tiếp tục gộp các nút có tổng nhỏ hơn), do đó D, B và C nằm ở tầng sâu hơn so với A. Vì A có tần suất cao nhất nên nằm gần gốc hơn và nhận mã ngắn hơn, giúp giảm độ dài mã trung bình.

</details>

### Bài tập 3

Chèn lần lượt các khóa 5, 3, 7, 1, 4, 6, 8 vào một BST rỗng. Xác định dãy duyệt inorder và đường đi khi tìm khóa 4.

<details>
<summary>Đáp án</summary>

Cây thu được có gốc 5; nhánh trái là 3 (với con trái 1, con phải 4); nhánh phải là 7 (với con trái 6, con phải 8).  
Thứ tự inorder: 1, 3, 4, 5, 6, 7, 8.  
Đường đi tìm 4: $$5 \to 3 \to 4$$.

</details>

### Bài tập 4

Chèn lần lượt dãy 1, 2, 3, 4, 5 vào một BST rỗng. Độ phức tạp khi tìm khóa 5 là bao nhiêu?

<details>
<summary>Đáp án</summary>

Cây bị lệch hoàn toàn về bên phải nên để tìm khóa 5 cần đi qua cả 5 nút, tương ứng với độ phức tạp trường hợp xấu nhất $$O(n)$$. Nếu sử dụng cây tự cân bằng (như AVL), độ phức tạp được giữ ở mức $$O(\log n)$$.

</details>

## Tóm tắt

1. **Mã Huffman** sử dụng chiến lược tham lam gộp hai nút tần suất nhỏ nhất, tạo ra mã **không tiền tố** giúp nén dữ liệu hiệu quả.
2. **BST** duy trì bất biến trái $$<$$ gốc $$<$$ phải nên duyệt inorder cho dãy tăng dần; chi phí trung bình là $$O(\log n)$$ nhưng có thể suy biến thành $$O(n)$$ nếu cây lệch.
3. Việc lựa chọn giữa cây cân bằng và bảng băm phụ thuộc vào nhu cầu giữ thứ tự khóa hay ưu tiên tra cứu điểm.

Chương 16 khép lại tại đây. Chương 17 sẽ tiếp tục với các **thuật toán đồ thị nâng cao** như đường đi ngắn nhất và sắp xếp topo.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=JsTptu56GM8">How Computers Compress Text: Huffman Coding and Huffman Trees</a> — Tom Scott, tiếng Anh. Giới thiệu trực quan về mã hóa Huffman và cây mã.
- <a href="https://www.youtube.com/watch?v=co4_ahEDCho">3.4 Huffman Coding - Greedy Method</a> — Abdul Bari, tiếng Anh. Hướng dẫn từng bước dựng cây Huffman từ bảng tần suất.
- <a href="https://www.youtube.com/watch?v=pYT9F8_LFTM">Data structures: Binary Search Tree</a> — mycodeschool, tiếng Anh. Trình bày chi tiết về cây tìm kiếm nhị phân cho nửa sau của bài.
