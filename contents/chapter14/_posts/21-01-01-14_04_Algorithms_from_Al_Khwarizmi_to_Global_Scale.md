---
layout: post
title: "Thuật toán: Từ Al-Khwarizmi đến Quy mô Toàn cầu"
categories: chapter14
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Chương 14 đã xây dựng khái niệm thuật toán, ký hiệu Big-O và phân tích độ phức tạp. Mục bổ sung này khảo sát hành trình của thuật toán từ Al-Khwarizmi thế kỷ…"
---

Chương 14 đã xây dựng khái niệm thuật toán, ký hiệu Big-O và phân tích độ phức tạp. Mục bổ sung này khảo sát hành trình của thuật toán từ Al-Khwarizmi thế kỷ IX đến các hệ thống quy mô toàn cầu — PageRank, sắp xếp phân tán, proof-of-work — cho thấy một khái niệm thủ tục trở thành nền tảng của hạ tầng số hiện đại.

![Al-Khwarizmi](/discrete-mathematics-for-computer-science-iuh/img/course/Al-Khwarizmi.jpg)

<p class="textbook-figure-caption" data-figure="14.16">Từ Al-Khwarizmi, khái niệm thuật toán bắt đầu như quy trình có hệ thống để giải bài toán.</p>
![Quy mô toàn cầu](/discrete-mathematics-for-computer-science-iuh/img/course/Comparison_computational_complexity.svg)

<p class="textbook-figure-caption" data-figure="14.17">Cùng một ý tưởng thuật toán cơ bản trở thành thách thức hệ thống khi dữ liệu lên quy mô toàn cầu.</p>
![Sorting ở quy mô lớn](/discrete-mathematics-for-computer-science-iuh/img/course/Comparison_computational_complexity.svg)

<p class="textbook-figure-caption" data-figure="14.18">Sorting và searching ở Google/Netflix đòi hỏi distributed computation, indexing và fault tolerance.</p>
![Tìm kiếm quy mô lớn](/discrete-mathematics-for-computer-science-iuh/img/course/Binary_search_into_array.svg)

<p class="textbook-figure-caption" data-figure="14.19">Search hiện đại kết hợp thuật toán với cache, network và cấu trúc chỉ mục.</p>
![Proof-of-work](/discrete-mathematics-for-computer-science-iuh/img/course/Blockchain.svg)

<p class="textbook-figure-caption" data-figure="14.20">Cryptocurrency mining dùng bài toán tính toán làm cơ chế đồng thuận — thuật toán gặp kinh tế.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Mô tả** nguồn gốc khái niệm thuật toán từ Al-Khwarizmi đến khoa học máy tính hiện đại.
- **Giải thích** PageRank như thuật toán lặp trên đồ thị web.
- **Nhận biết** thách thức quy mô: phân tán, fault tolerance, độ phức tạp ở hệ thống toàn cầu.
- **Liên hệ** proof-of-work với bài toán tính toán khó nhưng kiểm tra dễ.

**Từ khóa**: PageRank, distributed algorithm, proof-of-work, scalability, Al-Khwarizmi.
</div>

## Phần 1: Al-Khwarizmi và nguồn gốc của chữ “algorithm"

### 1.1. Cái tên trở thành khái niệm

Từ “algorithm” bắt nguồn từ tên Latin hóa của Al-Khwarizmi,
nhà toán học Ba Tư sống vào thế kỷ IX.

Ông nổi tiếng với các công trình về đại số,
tính toán số học,
và các quy trình giải bài toán có hệ thống.

### 1.2. Thuật toán trước máy tính

Điều đáng nhớ là:
thuật toán tồn tại trước máy tính rất lâu.
Máy tính chỉ làm cho thuật toán chạy nhanh hơn,
lặp nhiều hơn,
và tác động rộng hơn.

Tinh thần của thuật toán từ đầu đã là:

- có đầu vào,
- có các bước rõ ràng,
- có tiêu chí dừng,
- có đầu ra đúng mục tiêu.

---

## Phần 2: Google Search và PageRank

### 2.1. Tìm kiếm web là bài toán khổng lồ

Khi web bùng nổ,
vấn đề không còn là “có dữ liệu không”.
Vấn đề là:
làm sao tìm đúng thứ quan trọng trong biển thông tin khổng lồ đó.

### 2.2. PageRank như thuật toán cho khái niệm uy tín

PageRank dùng cấu trúc liên kết giữa các trang để ước lượng tầm quan trọng.
Trang được nhiều trang quan trọng khác trỏ tới
sẽ có điểm cao hơn.

Đáng chú ý là:
một khái niệm mơ hồ như “uy tín”
được thuật toán hóa thành quy trình lặp có thể tính được ở quy mô lớn.

### 2.3. Search hiện đại còn nhiều lớp hơn

Google Search ngày nay không chỉ có PageRank.
Nó còn có hàng loạt tín hiệu:

- relevance,
- freshness,
- authority,
- user intent,
- personalization,
- anti-spam heuristics.

Nhưng PageRank vẫn là biểu tượng mạnh cho việc thuật toán có thể tái cấu trúc cách con người tiếp cận tri thức.

---

## Phần 3: Sorting và searching ở quy mô Google/Netflix

### 3.1. Sắp xếp và tìm kiếm nghe cơ bản, nhưng không hề nhỏ

Sorting và searching là bài toán nhập môn.
Nhưng ở quy mô hàng tỷ bản ghi,
chúng trở thành chuyện của:

- cache locality,
- distributed computation,
- streaming updates,
- indexing,
- fault tolerance.

### 3.2. Quy mô thay đổi bản chất engineering

Ở quy mô nhỏ,
`O(n log n)` có thể đủ.
Ở quy mô khổng lồ,
còn phải hỏi thêm:

- dữ liệu nằm ở đâu,
- mạng nhanh đến mức nào,
- đĩa đọc/ghi ra sao,
- hệ có thể song song bao nhiêu,
- consistency yêu cầu gì.

### 3.3. Thuật toán không sống một mình

Thuật toán tốt không tồn tại tách rời hệ thống.
Nó phải phù hợp bộ nhớ,
phần cứng,
network,
workload,
và mục tiêu sản phẩm.

---

## Phần 4: Cryptocurrency mining và proof-of-work

### 4.1. Một bài toán tính toán được dùng như cơ chế đồng thuận

Proof-of-work dùng bài toán khó tính nhưng dễ kiểm tra để chọn ai được thêm block mới.

Ví dụ,
miner phải thử nhiều nonce cho đến khi hash thỏa điều kiện khó nào đó.

### 4.2. Đây là thuật toán nhưng cũng là kinh tế học

Mining không chỉ là code chạy.
Nó gắn với:

- xác suất thành công,
- tiêu thụ điện,
- incentives,
- difficulty adjustment,
- game theory.

Đó là ví dụ hiện đại cho việc thuật toán đôi khi là giao điểm của toán,
hệ thống phân tán,
và cơ chế xã hội.

### 4.3. Bài học sâu hơn

Thuật toán không chỉ giải bài toán kỹ thuật có sẵn.
Đôi khi nó tạo ra chính luật chơi của một hệ sinh thái mới.

---

## Phần 5: Computational complexity — có bài toán quá khó

### 5.1. Không phải bài toán nào cũng giải nhanh được

Một trong những bài học khiêm tốn nhất của computer science là:
có những bài toán mà dường như không tồn tại thuật toán hiệu quả cho mọi trường hợp.

### 5.2. P, NP, NP-complete

Các lớp độ phức tạp cho chúng ta ngôn ngữ để nói về ranh giới khả thi.
Nếu một bài toán là NP-complete,
việc tìm thuật toán đa thức cho nó
sẽ có hệ quả chấn động.

### 5.3. Ảnh hưởng thực tế

Complexity không chỉ để thi lý thuyết.
Nó ảnh hưởng cách kỹ sư chọn:

- heuristics,
- approximation,
- randomized methods,
- preprocessing,
- caching,
- problem reformulation.

Biết bài toán khó đến đâu
giúp chúng ta tránh hứa những điều sản phẩm không thể giữ.

---

## Phần 6: Tương lai — thuật toán trong thế giới AI và hạ tầng lớn

Thuật toán sẽ còn là trái tim của:

- search,
- recommendation,
- privacy-preserving computation,
- distributed consensus,
- resource scheduling,
- AI inference optimization,
- robotics planning.

Ngay cả khi mô hình học máy ngày càng chiếm sân khấu,
thuật toán vẫn là thứ quyết định cách tài nguyên được dùng,
kết quả được tính,
và giới hạn hiệu năng được xử lý.

---

## Kết luận

Từ Al-Khwarizmi,
đến PageRank,
large-scale sorting/searching,
proof-of-work,
và computational complexity,
thuật toán hiện ra như ngôn ngữ hành động của khoa học máy tính.

Nó không chỉ là “cách làm”.
Nó là cách biến bài toán thành quy trình,
và biến quy trình thành sức mạnh ở quy mô toàn cầu.

---

## Bài tập thực hành

### Bài tập 1: Thuật toán cổ điển

Mô tả thuật toán Euclid tìm ước số chung lớn nhất (GCD) dưới dạng thuật toán.

<details>
<summary>Đáp án</summary>

```
while b != 0:
    a, b = b, a % b
return a
```

</details>

### Bài tập 2: PageRank

Giải thích tại sao PageRank có thể xem là một thuật toán lan truyền trên đồ thị.

<details>
<summary>Đáp án</summary>

Mỗi trang phân phối "điểm uy tín" cho các trang nó trỏ đến. Điểm cuối cùng của một trang phụ thuộc vào số lượng và chất lượng các trang trỏ đến nó.

</details>

### Bài tập 3: Ứng dụng thực tế

Tại sao thuật toán MapReduce là cần thiết khi xử lý dữ liệu quy mô internet?

<details>
<summary>Đáp án</summary>

Dữ liệu quá lớn để xử lý trên một máy. MapReduce chia nhỏ công việc, xử lý song song trên nhiều máy, rồi tổng hợp kết quả.

</details>

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Thuật toán là trái tim của khoa học máy tính — từ Al-Khwarizmi đến Google, Bitcoin và trí tuệ nhân tạo. Hiểu cách thiết kế, phân tích và triển khai thuật toán giúp chúng ta giải quyết vấn đề hiệu quả, xây dựng hệ thống có khả năng mở rộng và tạo ra công nghệ thay đổi thế giới. Đây là kỹ năng nền tảng nhất của mọi lập trình viên và nhà khoa học máy tính.
