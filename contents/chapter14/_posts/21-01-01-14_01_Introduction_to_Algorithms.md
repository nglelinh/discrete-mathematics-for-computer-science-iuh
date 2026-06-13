---
layout: post
title: "Giới thiệu về Thuật toán"
categories: chapter14
date: 2021-01-01
order: 1
required: true
lang: en
---

Khi người dùng bấm tìm kiếm, khi hệ thống sắp xếp dữ liệu, khi ứng dụng kiểm tra đường đi hay mã hóa thông tin, đằng sau mỗi hành động đều có một chuỗi bước xử lý rõ ràng. Chuỗi bước đó chính là **thuật toán**.


Phân tích thuật toán không chỉ hỏi chương trình chạy được hay không, mà còn hỏi nó còn dùng được khi dữ liệu lớn lên nhanh đến mức nào.
Thuật toán không chỉ là đoạn code chạy được. Nó là ý tưởng giải bài toán một cách chính xác, hữu hạn và có thể lặp lại. Cùng một bài toán có thể có nhiều cách giải, nhưng không phải cách nào cũng hiệu quả, dễ kiểm chứng hay dễ mở rộng.

Học về thuật toán trong toán rời rạc giúp ta nhìn trước phần cài đặt. Ta học cách mô tả lời giải, phân tích tính đúng và so sánh chất lượng của các cách tiếp cận, thay vì lao ngay vào code.

Trong bài này, chúng ta sẽ xây khái niệm nền về thuật toán và lý do vì sao nó là trung tâm của toàn bộ khoa học máy tính.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Định nghĩa** thuật toán và các tính chất của một thuật toán tốt.
- **Mô tả** thuật toán bằng mã giả (pseudocode).
- **Phân biệt** các bài toán tính toán cơ bản: tìm kiếm, sắp xếp, tối ưu.
- **Vết** (trace) một thuật toán với đầu vào cụ thể.
- **Đánh giá** tính đúng đắn sơ bộ của thuật toán.

**Từ khóa**: Thuật toán (algorithm), đầu vào (input), đầu ra (output), mã giả (pseudocode), tính đúng đắn (correctness), tính hữu hạn (finiteness), tính xác định (definiteness).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter14/algorithm_puzzle.svg" alt="Minh họa khái niệm thuật toán như một chiếc máy nhận đầu vào và sinh đầu ra sau một số hữu hạn bước" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 14.1 — Thuật toán nhận đầu vào, xử lý theo từng bước xác định, và sinh ra đầu ra.</figcaption>
</p>
</figure>

## 1. Thuật toán là gì?

Ở phần này, đừng chỉ nhớ các bước. Hãy chú ý điều kiện áp dụng, thông tin được duy trì sau mỗi bước và lý do thuật toán cho kết quả đúng.

**Định nghĩa**: Thuật toán (algorithm) là một dãy hữu hạn các chỉ thị (instructions) chính xác để giải quyết một lớp bài toán. Thuật toán nhận **đầu vào** và sinh ra **đầu ra** sau một số hữu hạn bước.

### Tính chất của thuật toán

1. **Đầu vào** (input): Nhận giá trị từ tập xác định.
2. **Đầu ra** (output): Tạo ra kết quả từ đầu vào.
3. **Tính xác định** (definiteness): Mỗi bước được định nghĩa chính xác, không mơ hồ.
4. **Tính đúng đắn** (correctness): Với mọi đầu vào hợp lệ, thuật toán cho kết quả đúng.
5. **Tính hữu hạn** (finiteness): Thuật toán kết thúc sau hữu hạn bước.
6. **Tính hiệu quả** (effectiveness): Mỗi bước đủ đơn giản để thực thi được.

### Bài toán tìm kiếm

<div class="content-box example-box" markdown="1">
**Bài toán**: Cho danh sách $$n$$ số nguyên $$a_1, a_2, \ldots, a_n$$ và một giá trị $$x$$. Xác định vị trí của $$x$$ trong danh sách (hoặc trả về 0 nếu không tìm thấy).
</div>

<div class="content-box insight-box" markdown="1">
**Một câu hỏi thú vị**: Có những bài toán mà không thuật toán nào có thể giải được không? Câu trả lời là CÓ. Bài toán "dừng" (Halting Problem) — xác định xem một chương trình có dừng lại hay không — được Alan Turing chứng minh là không giải được vào năm 1936. Đây là một trong những khám phá nền tảng của khoa học máy tính lý thuyết.
</div>

## 2. Mã giả (Pseudocode)

Mã giả là cách mô tả thuật toán bằng ngôn ngữ tự nhiên kết hợp cấu trúc lập trình, giúp con người dễ đọc mà không phải lo về cú pháp của một ngôn ngữ cụ thể.

```
THUẬT TOÁN: Tìm-Phần-Tử-Lớn-Nhất
Đầu vào: Mảng a[1..n] gồm n số thực
Đầu ra: Giá trị lớn nhất trong mảng

1. max ← a[1]
2. FOR i ← 2 TO n DO
3.     IF a[i] > max THEN
4.         max ← a[i]
5.     END IF
6. END FOR
7. RETURN max
```

<div class="content-box example-box" markdown="1">
**Ví dụ vết**: Mảng `[7, 2, 9, 4, 6]`. Ban đầu `max = 7`. So sánh: `2 < 7`, bỏ qua; `9 > 7`, `max ← 9`; `4 < 9`; `6 < 9`. Kết quả: `max = 9`.
</div>

## 3. Thuật toán Tìm kiếm Tuyến tính

Ở phần này, đừng chỉ nhớ các bước. Hãy chú ý điều kiện áp dụng, thông tin được duy trì sau mỗi bước và lý do thuật toán cho kết quả đúng.

Thuật toán tìm kiếm đơn giản nhất: duyệt qua từng phần tử.

```
THUẬT TOÁN: Tìm-kiếm-Tuyến-tính
Đầu vào: Mảng a[1..n], giá trị cần tìm x
Đầu ra: Vị trí i sao cho a[i] = x, hoặc 0 nếu không tìm thấy

1. i ← 1
2. WHILE i ≤ n AND a[i] ≠ x DO
3.     i ← i + 1
4. END WHILE
5. IF i ≤ n THEN RETURN i
6. ELSE RETURN 0
```

| Trường hợp | Số bước so sánh |
|:---|---:|
| Tốt nhất (x ở đầu) | 1 |
| Xấu nhất (x ở cuối hoặc không có) | n |
| Trung bình | (n+1)/2 |

## 4. Thuật toán Sắp xếp Nổi bọt

```
THUẬT TOÁN: Sắp-xếp-Nổi-bọt
Đầu vào: Mảng a[1..n]
Đầu ra: Mảng đã sắp xếp không giảm

1. FOR i ← 1 TO n-1 DO
2.     FOR j ← 1 TO n-i DO
3.         IF a[j] > a[j+1] THEN
4.             hoán đổi a[j] và a[j+1]
5.         END IF
6.     END FOR
7. END FOR
8. RETURN a
```

<div class="content-box example-box" markdown="1">
**Ví dụ**: Sắp xếp `[5, 3, 8, 1]`.

Vòng 1 (i=1): `[3,5,8,1]` → `[3,5,1,8]`
Vòng 2 (i=2): `[3,1,5,8]`
Vòng 3 (i=3): `[1,3,5,8]`

Các phần tử lớn hơn "nổi" lên cuối mảng giống như bọt khí — đó là nguồn gốc tên gọi "sắp xếp nổi bọt".
</div>

## Các Bài toán và Thuật toán Kinh điển

### Bài toán Tìm kiếm

Tìm kiếm là một trong những bài toán cơ bản nhất. Hai thuật toán tiêu biểu:

| Thuật toán | Ý tưởng | Độ phức tạp | Yêu cầu |
|:---|:---|---:|:---|
| Tuyến tính | Duyệt tuần tự | $$O(n)$$ | Không |
| Nhị phân | Chia để trị | $$O(\log n)$$ | Mảng đã sắp xếp |

### Bài toán Sắp xếp

Sắp xếp là nền tảng của nhiều thuật toán khác. Một số thuật toán cơ bản:

| Thuật toán | Ý tưởng chính | Số phép so sánh (xấu nhất) |
|:---|:---|---:|
| Nổi bọt (Bubble Sort) | Đổi chỗ liên tiếp | $$n(n-1)/2$$ |
| Chèn (Insertion Sort) | Chèn vào vị trí đúng | $$n(n-1)/2$$ |
| Chọn (Selection Sort) | Chọn phần tử nhỏ nhất | $$n(n-1)/2$$ |
| Trộn (Merge Sort) | Chia để trị | $$n\log n$$ |

<div class="content-box insight-box" markdown="1">
**Tại sao sắp xếp quan trọng?** Dữ liệu được sắp xếp cho phép:
- Tìm kiếm nhanh hơn (nhị phân thay vì tuyến tính)
- Phát hiện trùng lặp dễ dàng hơn
- Tính toán thống kê hiệu quả (median, mode)
- Các thuật toán đồ thị (Kruskal, Prim) yêu cầu dữ liệu sắp xếp

Hầu hết mọi hệ thống phần mềm đều dùng sắp xếp ở một hình thức nào đó.
</div>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Thuật toán xuất hiện khắp mọi nơi trong CS:

- **Công cụ tìm kiếm**: Google dùng thuật toán PageRank để xếp hạng trang web.
- **Điều hướng GPS**: Thuật toán Dijkstra tìm đường đi ngắn nhất.
- **Nén dữ liệu**: Huffman coding (thuật toán tham lam).
- **Mạng xã hội**: Gợi ý bạn bè dùng thuật toán đồ thị.
- **AI/Machine Learning**: Gradient descent huấn luyện mạng nơ-ron.
- **Mật mã**: RSA dùng thuật toán lũy thừa modulo nhanh.

Hiểu thuật toán giúp bạn không chỉ *dùng* thư viện mà còn *tự thiết kế* giải pháp khi không có thư viện sẵn.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Trực quan hóa Thuật toán Sắp xếp</h3>
<p>Công cụ này cho phép bạn xem trực quan cách Bubble Sort hoạt động: các thanh màu đại diện cho các phần tử, và bạn thấy từng bước so sánh và đổi chỗ. <strong>Hãy thử:</strong> So sánh số bước của Bubble Sort với Insertion Sort trên cùng một dữ liệu đầu vào.</p>
<div data-demo="algorithm-visualization"></div>
</div>
<script src="{{ '/public/js/algorithm-visualization.js' | relative_url }}"></script>

## Bài tập

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

1. Viết mã giả cho thuật toán đếm số phần tử chẵn trong mảng.
2. Vết thuật toán tìm kiếm tuyến tính với mảng `[3, 7, 1, 9, 4]` và `x = 9`.
3. Tại sao thuật toán sắp xếp nổi bọt có hai vòng lặp lồng nhau? Mỗi vòng có vai trò gì?
4. Một thư viện có 1 triệu cuốn sách được sắp xếp theo tên. Bạn cần tìm cuốn "Discrete Mathematics". Sẽ dùng tìm kiếm tuyến tính hay nhị phân? Giải thích.
5. **Thử thách**: Viết mã giả cho thuật toán tìm số Fibonacci thứ $$n$$ bằng phương pháp lặp (không đệ quy). So với cách đệ quy, cách nào tốt hơn?

<details>
<summary>Đáp án bài 5</summary>

```
THUẬT TOÁN: Fibonacci-Lặp(n)
1. IF n = 0 THEN RETURN 0
2. IF n = 1 THEN RETURN 1
3. a ← 0, b ← 1
4. FOR i ← 2 TO n DO
5.     c ← a + b
6.     a ← b
7.     b ← c
8. END FOR
9. RETURN b
```

Thuật toán lặp chỉ mất $$O(n)$$ thời gian và $$O(1)$$ không gian, tốt hơn rất nhiều so với đệ quy $$O(2^n)$$ ở bài học sau.
</details>

## Tóm tắt

- **Thuật toán** là dãy hữu hạn các bước xác định để giải bài toán.
- **6 tính chất**: đầu vào, đầu ra, xác định, đúng đắn, hữu hạn, hiệu quả.
- **Mã giả**: mô tả thuật toán bằng ngôn ngữ tự nhiên + cấu trúc lập trình.
- **Bài toán cơ bản**: tìm kiếm (tuyến tính, nhị phân), sắp xếp (nổi bọt, chèn, chọn, trộn).
- **Vết thuật toán**: mô phỏng thủ công để kiểm tra tính đúng đắn.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu cách đo lường hiệu quả của thuật toán — ký hiệu Big-O.

## Tài liệu Tham khảo

1. Thomas H. Cormen et al., *Introduction to Algorithms* (CLRS), MIT Press, Chương 1-2.
2. Donald E. Knuth, *The Art of Computer Programming*, Vol. 1, Addison-Wesley.
3. Muhammad ibn Musa al-Khwarizmi, *Al-Kitab al-Mukhtasar*, khoảng năm 820 — cuốn sách về phương pháp tính toán có hệ thống đầu tiên.
