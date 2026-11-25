---

layout: post
title: "Hàm sinh trong Phép đếm và Mã hóa"
categories: chapter11
date: 2021-01-01
order: 5
required: false
lang: en
excerpt: "Tổng hợp các ứng dụng mở rộng của hàm sinh: từ ý tưởng của Euler năm 1748, bài toán phân hoạch, hàm sinh xác suất (PGF), giải truy hồi phức tạp đến đa thức đếm trọng số trong lý thuyết mã hóa."
---

Năm 1748, Leonhard Euler nhận được một bức thư hỏi về số cách tách một số nguyên thành tổng các số nguyên nhỏ hơn (bài toán phân hoạch). Thay vì đếm thủ công từng trường hợp, Euler viết ra một tích vô hạn của các chuỗi hình học — khai sinh ra phương pháp **hàm sinh** hiện đại. Hơn hai thế kỷ sau, đúng công cụ ấy lại xuất hiện ở trung tâm của **lý thuyết xác suất (PGF)** và **mã sửa lỗi (weight enumerator)** trong viễn thông 5G và lưu trữ đám mây.

**Mạch bài học:** Bước ngoặt **phân hoạch số nguyên** của Euler (1748) $$\longrightarrow$$ **hàm sinh xác suất (PGF)** tính kỳ vọng và phương sai bằng đạo hàm $$\longrightarrow$$ **đa thức đếm trọng số (weight enumerator)** trong mã sửa lỗi $$\longrightarrow$$ phương pháp ký hiệu (symbolic method) trong tổ hợp hiện đại.

## Bản đồ kiến thức nền: Hàm sinh kết nối Số học, Xác suất và Lý thuyết Mã hóa như thế nào?

- **Phân hoạch số nguyên (Integer Partitions):** Số cách phân tích $$n$$ thành tổng các số nguyên dương không kể thứ tự $$p(n)$$ không có công thức sơ cấp đơn giản, nhưng hàm sinh của nó lại đẹp đến ngỡ ngàng: $$\sum_{n=0}^{\infty} p(n)x^n = \prod_{k=1}^{\infty} \frac{1}{1 - x^k}$$.
- **Hàm sinh xác suất (Probability Generating Function — PGF):** Với biến ngẫu nhiên rời rạc $$X \in \{0, 1, 2, \dots\}$$, đặt $$P_X(s) = \sum_{k \ge 0} \Pr(X=k)s^k$$. Phép cộng hai biến độc lập $$X + Y$$ biến thành phép **nhân** $$P_{X+Y}(s) = P_X(s)P_Y(s)$$, còn kỳ vọng chỉ việc lấy đạo hàm tại $$s = 1$$: $$E[X] = P_X'(1)$$!
- **Đa thức đếm trọng số (Weight Enumerator in Coding Theory):** Một mã tuyến tính $$C$$ gồm các từ mã nhị phân có hàm sinh $$W_C(x) = \sum_{w=0}^n A_w x^w$$ ($$A_w$$ là số từ mã có đúng $$w$$ bit `1`). Biểu thức này cho phép tính ngay xác suất lỗi không phát hiện được trên kênh truyền nhiễu!

Ở các mục trước, chúng ta đã định nghĩa hàm sinh, áp dụng hàm sinh để giải quan hệ truy hồi và tìm hiểu nguyên lý bao hàm–loại trừ. Mục cuối của Chương 11 tổng hợp các **ứng dụng mở rộng** của hàm sinh: từ ý tưởng của Euler (1748) khi biến dãy số thành đối tượng đại số, cho đến bài toán phân hoạch (partition), **hàm sinh xác suất** (PGF), giải các hệ thức truy hồi phức tạp và **đa thức đếm trọng số** (weight enumerator) trong lý thuyết mã hóa. Khi việc liệt kê trực tiếp không còn khả thi, đóng gói cả dãy vào $$G(x)=\sum a_n x^n$$ cho phép ta xử lý bài toán bằng công cụ đại số thay vì đếm thủ công từng bước.

---

![Euler và hàm sinh](/discrete-mathematics-for-computer-science-iuh/img/course/Leonhard_Euler.jpg)

<p class="textbook-figure-caption" data-figure="11.21">Euler xem các dãy số như đối tượng đại số, đặt nền móng cho phương pháp hàm sinh trong tổ hợp học.</p>
![Hàm sinh xác suất (PGF)](/discrete-mathematics-for-computer-science-iuh/img/course/3D_surface_graph_of_generating_function_for_Fibonacci_numbers.png)

<p class="textbook-figure-caption" data-figure="11.22">Hàm sinh xác suất chuyển phân phối rời rạc thành một hàm có thể vi phân, nhân và phân tích bằng đại số.</p>
![Đếm tổ hợp bằng hệ số](/discrete-mathematics-for-computer-science-iuh/img/course/Za_by_Power_Series_Expansion.png)

<p class="textbook-figure-caption" data-figure="11.23">Khi nhân các chuỗi lũy thừa hình thức, hệ số của $$x^n$$ cho biết số cách đạt tổng $$n$$.</p>
![Giải truy hồi bằng hàm sinh](/discrete-mathematics-for-computer-science-iuh/img/course/Fibonacci_spiral.svg)

<p class="textbook-figure-caption" data-figure="11.24">Các hệ thức truy hồi phức tạp trở thành phương trình đại số khi chuyển sang miền hàm sinh.</p>
![Weight enumerator trong mã hóa](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="11.25">Đa thức đếm từ mã theo trọng số Hamming — một dạng hàm sinh quen thuộc trong lý thuyết mã hóa.</p>
## Phần 1: Euler và bước ngoặt năm 1748

### Euler nhìn dãy số như một đối tượng đại số

Leonhard Euler nhận ra cấu trúc ẩn đằng sau các dãy số rời rạc bằng cách không chỉ xem chúng là một danh sách giá trị, mà coi chúng là các hệ số của một chuỗi lũy thừa (power series). Ví dụ, dãy $$a_0, a_1, a_2, \ldots$$ có thể được đóng gói thành:

<div class="textbook-equation" markdown="1">
$$
A(x)=a_0+a_1x+a_2x^2+\cdots
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Cách biểu diễn này mở ra hướng tiếp cận mới cho các bài toán tổ hợp.

### Vì sao cách nhìn này hiệu quả

Khi chuyển bài toán đếm sang bài toán thao tác trên biểu thức, ta có thể tận dụng đại số, giải tích hình thức và các phép biến đổi chuỗi để rút ra kết quả đếm. Đây là tư duy “chuyển đổi ngôn ngữ để đơn giản hóa bài toán” rất quen thuộc trong khoa học máy tính.

---

## Phần 2: Đếm tổ hợp bằng hàm sinh

### Hệ số là lời giải của bài toán đếm

Giả sử ta cần đếm số cách tạo ra một tổng cho trước từ các lựa chọn thành phần. Hàm sinh cho phép mã hóa từng lựa chọn thành một thừa số, rồi trích xuất hệ số tương ứng. Chẳng hạn, nếu một thành phần có thể được chọn $$0, 1, 2, \ldots$$ lần, thừa số ứng với nó có dạng:

<div class="textbook-equation" markdown="1">
$$
1+x+x^2+x^3+\cdots = \frac{1}{1-x}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Khi nhân nhiều chuỗi như vậy lại với nhau, hệ số của $$x^n$$ chính là số cách đạt được tổng $$n$$.

### Bài toán phân hoạch (Partition problems)

Một ví dụ kinh điển là đếm số cách phân tích một số nguyên dương thành tổng các số nguyên dương. Với dạng bài toán này, việc liệt kê thủ công nhanh chóng trở nên bất khả thi khi kích thước tăng lên, trong khi hàm sinh lại biểu diễn cấu trúc bài toán một cách tự nhiên.

### Ý nghĩa đối với sinh viên Khoa học Máy tính

Không phải ai cũng cần làm việc trực tiếp với các đồng nhất thức phân hoạch mỗi ngày. Tuy nhiên, hàm sinh rèn luyện một kỹ năng quan trọng: nhận biết cách mã hóa một cấu trúc rời rạc sang biểu diễn đại số để xử lý hiệu quả hơn.

---

## Phần 3: Hàm sinh xác suất (Probability Generating Functions)

### Đóng gói phân phối xác suất bằng chuỗi lũy thừa

Nếu biến ngẫu nhiên rời rạc $$X$$ nhận các giá trị nguyên không âm, ta định nghĩa hàm sinh xác suất (probability generating function, PGF) của $$X$$ là:

<div class="textbook-equation" markdown="1">
$$
G_X(s)=\sum_{k\ge0} P(X=k)s^k
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nhờ đó, toàn bộ phân phối xác suất của $$X$$ được đóng gói thành một đối tượng đại số thuận tiện cho tính toán.

### Ứng dụng của PGF

Hàm sinh xác suất hỗ trợ các tác vụ sau:

- tính kỳ vọng và các mô-men bậc cao,
- phân tích tổng của các biến ngẫu nhiên độc lập,
- nghiên cứu các quá trình phân nhánh (branching processes),
- suy ra các tính chất của phân phối.

Một lần nữa, ta gặp lại cùng một nguyên lý: chuyển một cấu trúc phức tạp thành hàm số để thao tác dễ dàng hơn.

### Cầu nối sang lý thuyết hàng đợi và hệ thống ngẫu nhiên

Trong các mô hình hàng đợi (queueing), lưu lượng mạng (traffic processes) và hệ thống ngẫu nhiên theo thời gian, hàm sinh là công cụ tiêu chuẩn để phân tích phân phối trạng thái của hệ thống.

---

## Phần 4: Giải truy hồi phức tạp bằng hàm sinh

### Khi hệ thức truy hồi không còn dễ đoán nghiệm

Một số hệ thức truy hồi đơn giản có thể giải trực tiếp, nhưng nhiều hệ thức phức tạp hơn sẽ trở nên dễ xử lý khi ta nhân cả hai vế với $$x^n$$, lấy tổng theo `n` và chuyển toàn bộ bài toán thành quan hệ đại số giữa các hàm sinh.

### Tư duy chuyển miền biểu diễn

Đây là cách tiếp cận quen thuộc trong khoa học máy tính: đổi biểu diễn để tối ưu hóa phép toán. Tương tự cách biến đổi Fourier nhanh (FFT) chuyển tín hiệu từ miền thời gian sang miền tần số, hàm sinh chuyển bài toán trên dãy số sang bài toán trên chuỗi hàm.

### Ứng dụng trong phân tích thuật toán

Khi phân tích thuật toán đếm, quá trình ngẫu nhiên hoặc các cấu trúc tổ hợp phức tạp, hàm sinh thường mang lại biểu thức gọn hơn và làm rõ quy luật tăng trưởng hơn so với việc tính tay từng bước.

---

## Phần 5: Lý thuyết mã hóa và đếm từ mã

### Mã hóa không chỉ dừng ở việc biến đổi bit

Trong lý thuyết mã hóa (coding theory), ta cần xác định nhiều thuộc tính cấu trúc của một bộ mã:

- số lượng từ mã (codewords),
- phân bố trọng số của các từ mã,
- khoảng cách Hamming giữa các từ mã,
- khả năng phát hiện và sửa lỗi của mã.

### Đa thức đếm trọng số (Weight enumerator) như một dạng hàm sinh

Mỗi bộ mã có thể gắn với một đa thức đếm số lượng từ mã theo từng mức trọng số — đây là một dạng hàm sinh trực tiếp. Thông qua đa thức này, ta có thể phân tích cấu trúc đại số của mã, đánh giá khả năng chống lỗi và suy ra nhiều tính chất liên hệ giữa các bộ mã.

### Từ lý thuyết đến truyền thông và lưu trữ

Mã sửa lỗi (error-correcting codes) được ứng dụng rộng rãi trong:

- đĩa quang,
- truyền thông vệ tinh,
- mã QR,
- bộ nhớ máy tính,
- truyền dữ liệu qua kênh nhiễu.

Trong các hệ thống này, hàm sinh giúp đếm và phân tích không gian cấu trúc của mã phục vụ thiết kế thực tế, chứ không chỉ dừng ở bài toán lý thuyết.

---

## Phần 6: Phương pháp ký hiệu trong tính toán hiện đại

Dù các công cụ tính toán số hiện đại rất phát triển, các phương pháp ký hiệu (symbolic methods) như hàm sinh vẫn giữ vai trò quan trọng trong:

- tổ hợp giải tích (analytic combinatorics),
- mô hình hóa hiệu năng (performance models),
- phân tích xác suất (probabilistic analysis),
- nghiên cứu cấu trúc mã hóa (code structure studies),
- bài toán đếm thuật toán (algorithmic counting).

Các phương pháp này cho thấy việc chọn đúng cách biểu diễn bài toán thường mang lại hiệu quả căn bản, bên cạnh việc tăng năng lực phần cứng tính toán.

---

## Kết luận

Từ ý tưởng của Euler đến bài toán phân hoạch, hàm sinh xác suất, giải hệ thức truy hồi và lý thuyết mã hóa, hàm sinh thể hiện một nguyên lý xuyên suốt: đóng gói cấu trúc rời rạc vào dạng hàm và dùng đại số để xử lý. Đây là phong cách tư duy không chỉ phục vụ riêng Chương 11 mà còn xuất hiện nhiều lần trong khoa học máy tính.

---

## Ví dụ tính tay cầm tay chỉ việc: Tính kỳ vọng bằng PGF và đa thức trọng số mã lặp

**Phần A — Tính kỳ vọng và phương sai khi tung 1 con xúc xắc bằng PGF:**
Hàm sinh xác suất của 1 lần tung xúc xắc (1..6 đều xác suất $$1/6$$) là:
$$P_X(s) = \frac{1}{6}(s + s^2 + s^3 + s^4 + s^5 + s^6).$$
1. **Kiểm tra chuẩn hóa tại $$s = 1$$:** $$P_X(1) = \frac{1}{6}(6) = 1$$.
2. **Tính kỳ vọng bằng đạo hàm cấp 1 tại $$s = 1$$:**
   $$P_X'(s) = \frac{1}{6}(1 + 2s + 3s^2 + 4s^3 + 5s^4 + 6s^5) \;\Longrightarrow\; E[X] = P_X'(1) = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3{,}5.$$
3. **Tung 2 con xúc xắc độc lập $$S = X_1 + X_2$$:** PGF của tổng là $$\big(P_X(s)\big)^2$$, nên hệ số của $$s^7$$ chính là xác suất tổng bằng 7: $$[s^7]\big(P_X(s)\big)^2 = \frac{6}{36} = \frac{1}{6}$$!

**Phần B — Đa thức đếm trọng số của mã kiểm tra chẵn lẻ $$C$$ độ dài 3 (3 bit, tổng bit chẵn):**
Các từ mã hợp lệ của $$C$$ là: `000` (trọng số 0), `011`, `101`, `110` (đều trọng số 2).
- Đa thức trọng số: $$W_C(x) = 1 + 3x^2$$.
- Nếu truyền từ mã `000` qua kênh đối xứng nhị phân có xác suất lật bit $$p = 0{,}01$$, lỗi chỉ **không bị phát hiện** khi biến thành một từ mã hợp lệ khác (tức bị lật đúng 2 bit):
  $$P_{\text{undetected}} = 3 p^2 (1 - p) = 3 (0{,}01)^2 (0{,}99) = 0{,}000297 \approx 0{,}03\%.$$

### Khung giải thích: Ba công dụng "vượt biên giới" của hàm sinh (nên đọc chậm)

1. **Bước 1 — Trong tổ hợp, tích của các chuỗi là bài toán chọn độc lập:** Tích Euler $$\prod_{k \ge 1}(1-x^k)^{-1}$$ chọn số lần xuất hiện của từng mệnh giá $$1, 2, 3, \dots$$ rồi tự động cộng tổng bằng số mũ.
2. **Bước 2 — Trong xác suất, đạo hàm tại $$s = 1$$ kéo số mũ xuống làm trọng số:** Nhờ $$(s^k)'\vert_{s=1} = k$$, các mô-men thống kê (kỳ vọng, phương sai) được tính hoàn toàn bằng phép vi phân đại số thay vì cộng chuỗi thủ công.
3. **Bước 3 — Trong mã hóa, đa thức trọng số tóm gọn khả năng chống nhiễu:** Thay giá trị $$x = \frac{p}{1-p}$$ vào đa thức trọng số $$W_C(x)$$ lập tức cho biết chính xác xác suất giải mã sai của cả hệ thống truyền tin!

$$\text{PGF: } E[X] = P_X'(1), \qquad \text{Coding: } W_C(x) = \sum_{w=0}^n A_w x^w \;\Longrightarrow\; P_{\text{undetected}} = (1-p)^n\!\left[W_C\!\left(\frac{p}{1-p}\right) - 1\right].$$

## Bài tập thực hành

### Bài tập 1: Viết hàm sinh

Viết hàm sinh cho số cách chọn $$k$$ phần tử từ $$n$$ loại khác nhau (có lặp lại, không phân biệt thứ tự).

<details>
<summary>Đáp án</summary>

$$\frac{1}{(1-x)^n}$$ (hàm sinh của tổ hợp lặp).

</details>

### Bài tập 2: Giải truy hồi bằng hàm sinh

Dùng hàm sinh giải hệ thức truy hồi $$a_n = a_{n-1} + a_{n-2}$$ với $$a_0=0$$, $$a_1=1$$.

<details>
<summary>Đáp án</summary>

Hàm sinh thu được là $$G(x) = \frac{x}{1-x-x^2}$$.  
Hệ số của $$x^n$$ chính là số Fibonacci thứ $$n$$ ($$F_n$$).

</details>

### Bài tập 3: Ứng dụng trong mã hóa

Giải thích vai trò của hàm sinh trong lý thuyết mã hóa thông qua đa thức đếm trọng số (weight enumerator).

<details>
<summary>Đáp án</summary>

Đa thức đếm trọng số (weight enumerator polynomial) mô tả phân bố trọng số Hamming của các từ mã, từ đó giúp đánh giá khoảng cách tối thiểu và khả năng phát hiện hoặc sửa lỗi của bộ mã.

</details>


## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

Hàm sinh là công cụ hiệu quả để giải bài toán đếm và quan hệ truy hồi. Từ tổ hợp, phân hoạch đến xác suất và lý thuyết mã hóa, hàm sinh chuyển các bài toán rời rạc phức tạp thành các phép toán đại số có hệ thống.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=mZ9gmFtxBNg">Solve Counting Problems with Generating Functions (8.4.5)</a> — SawFin Mathematics, tiếng Anh. Giới thiệu cách giải bài toán đếm tổ hợp bằng hệ số hàm sinh.
- <a href="https://www.youtube.com/watch?v=X8jsijhllIA">But what are Hamming codes? The origin of error correction</a> — 3Blue1Brown, tiếng Anh. Giới thiệu mã Hamming và khoảng cách mã, liên hệ trực tiếp với phần weight enumerator trong bài.
- <a href="https://www.youtube.com/watch?v=bOXCLR3Wric">Olympiad level counting  (Generating functions)</a> — 3Blue1Brown, tiếng Anh. Minh họa cách diễn giải hệ số hàm sinh như số cấu hình đếm được.
