---

layout: post
title: "Quy nạp Toán học"
categories: chapter03
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Giới thiệu nguyên lý quy nạp toán học, quy trình hai bước cơ sở và quy nạp cùng các ứng dụng vào dãy số, chia hết, bất đẳng thức, bất biến vòng lặp và đệ quy."
---

Ở mục trước, chúng ta đã học chứng minh phản chứng — giả sử phủ định của kết luận rồi dẫn đến mâu thuẫn. Mục này giới thiệu **quy nạp toán học** (mathematical induction), phương pháp chứng minh dành cho các mệnh đề phụ thuộc vào số tự nhiên. Nhiều đối tượng trong khoa học máy tính — như dãy Fibonacci, lời gọi đệ quy, số mức của cây hay chi phí thuật toán — được xây dựng theo từng bước; việc kiểm tra vài giá trị đầu không đủ để khẳng định tính chất đúng với mọi $$n$$. Quy nạp giải quyết vấn đề này bằng hai bước: chứng minh mệnh đề đúng ở điểm khởi đầu (**bước cơ sở**), sau đó chứng minh rằng nếu mệnh đề đúng ở bước $$k$$ thì cũng đúng ở bước $$k+1$$ (**bước quy nạp**). Cách tư duy này tương ứng trực tiếp với lập trình đệ quy: bước cơ sở ứng với trường hợp dừng (base case), còn bước quy nạp ứng với bước đệ quy bảo toàn tính đúng đắn.

![Hiệu ứng domino](/discrete-mathematics-for-computer-science-iuh/img/course/Domino_effect.gif)

<p class="textbook-figure-caption" data-figure="3.11">Hiệu ứng domino — nếu quân đầu tiên ngã và mỗi quân ngã đều làm quân kế tiếp ngã, thì toàn bộ hàng domino sẽ ngã.</p>

Làm sao một lập trình viên chứng minh một hàm đệ quy như `merge_sort(arr)` hoạt động đúng với **mọi** kích thước mảng $$n = 1, 2, 3, \dots, 10^9$$ mà không thể chạy thử vô hạn lần? Câu trả lời chính là **Quy nạp Toán học (Mathematical Induction)**—hình ảnh kinh điển của hàng quân domino vô hạn: chỉ cần xô đổ quân đầu tiên và đảm bảo hễ quân thứ $$k$$ đổ thì quân thứ $$k+1$$ chắc chắn đổ theo, toàn bộ hàng vô hạn sẽ đổ rạp!

## Kiến thức cần nhớ: Bốn trụ cột của Quy nạp Toán học & Đệ quy

1. **Quy nạp yếu (Weak Induction)**:
   Để chứng minh $$\forall n \ge n_0,\; P(n)$$: chứng minh **Bước cơ sở** $$P(n_0)$$, sau đó chứng minh **Bước quy nạp** $$P(k) \to P(k+1)$$ với mọi $$k \ge n_0$$.

2. **Quy nạp mạnh (Strong Induction)**:
   Giả thiết quy nạp cho phép dùng toàn bộ $$P(n_0), P(n_0+1), \dots, P(k)$$ để chứng minh $$P(k+1)$$. Cực kỳ thiết yếu cho định lý phân tích thừa số nguyên tố, dãy Fibonacci và thuật toán chia để trị (như Merge Sort gọi đệ quy trên kích thước $$n/2$$ chứ không phải $$n-1$$!).

3. **Quy nạp cấu trúc (Structural Induction)**:
   Mở rộng quy nạp từ số tự nhiên sang các cấu trúc dữ liệu đệ quy trong Khoa học Máy tính: danh sách liên kết, cây nhị phân, cây cú pháp trừu tượng (AST) và công thức logic.

4. **Bất biến vòng lặp (Loop Invariant)**:
   Chứng minh một vòng lặp `while`/`for` chạy đúng chính là một bài quy nạp ẩn: bất biến đúng trước vòng lặp (cơ sở), được bảo toàn sau mỗi lượt lặp (bước quy nạp), và khi vòng lặp dừng nó kéo theo kết quả mong muốn.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

1. Phát biểu đúng nguyên lý quy nạp toán học.
2. Phân biệt **bước cơ sở** và **bước quy nạp**.
3. Viết một chứng minh quy nạp hoàn chỉnh, chặt chẽ và rõ ràng.
4. Nhận biết khi nào nên dùng quy nạp thay cho chứng minh trực tiếp hay phản chứng.
5. Áp dụng quy nạp cho công thức tổng, bất đẳng thức, tính chia hết và các cấu trúc rời rạc.
6. Liên hệ quy nạp với đệ quy, quan hệ truy hồi, vòng lặp và cấu trúc dữ liệu trong khoa học máy tính.
</div>

## Trực giác: Vì sao quy nạp hợp lý?

### Hình ảnh domino

Xét một hàng domino vô hạn được xếp liên tiếp nhau. Nếu quân đầu tiên ngã và bất cứ khi nào quân thứ $$k$$ ngã thì nó cũng làm quân thứ $$k+1$$ ngã, toàn bộ hàng domino sẽ đổ.

Trong quy nạp toán học:

- Mệnh đề $$P(n)$$ tương ứng với trạng thái "quân domino thứ $$n$$ đã ngã".
- Chứng minh $$P(n_0)$$ đúng tương ứng với việc đẩy ngã **quân đầu tiên**.
- Chứng minh $$P(k) \Rightarrow P(k+1)$$ tương ứng với việc đảm bảo **mỗi quân ngã sẽ kéo theo quân kế tiếp**.

Hình ảnh domino giúp ta nắm trực giác, còn lời giải chính thức vẫn phải được trình bày bằng ngôn ngữ toán học chính xác.

![Hiệu ứng domino quy nạp](/discrete-mathematics-for-computer-science-iuh/img/course/Induction_domino_effect.jpg)

<p class="textbook-figure-caption" data-figure="3.12">Domino và quy nạp — bước cơ sở tương ứng việc đẩy quân đầu tiên; bước quy nạp đảm bảo mỗi quân kéo theo quân kế tiếp.</p>
### Trực giác thứ hai: Xây dựng từng tầng

Một cách hiểu khác gần với khoa học máy tính là xem quy nạp như quá trình xây dựng đối tượng theo từng tầng: ta biết đối tượng nhỏ nhất hoạt động đúng, rồi chứng minh rằng nếu đối tượng kích thước $$k$$ đúng thì đối tượng kích thước $$k+1$$ cũng đúng. Chẳng hạn:

- Xâu độ dài $$k+1$$ được tạo từ xâu độ dài $$k$$ bằng cách thêm một ký tự.
- Danh sách kích thước $$k+1$$ được tạo từ danh sách kích thước $$k$$ bằng cách thêm một phần tử.
- Cây lớn hơn được xây dựng từ các cây con nhỏ hơn.

Vì thế, quy nạp không chỉ là một kỹ thuật chứng minh mà còn phản ánh đúng cách nhiều cấu trúc rời rạc được hình thành.

### Trực giác thứ ba: Cấu trúc đệ quy

Trong lập trình, nhiều đối tượng được định nghĩa đệ quy:

- Giai thừa: $$n! = n \cdot (n-1)!$$
- Dãy Fibonacci: $$F_n = F_{n-1} + F_{n-2}$$
- Cây nhị phân: gồm nút gốc và hai cây con trái, phải.

Khi đối tượng được định nghĩa đệ quy, phương pháp chứng minh tự nhiên nhất cho các tính chất của nó thường là quy nạp.

### Minh họa domino: Bước cơ sở và bước quy nạp

Quan sát các quân domino đổ lần lượt khi có đủ **bước cơ sở** và **bước quy nạp**; hai ví dụ cuối cho thấy điều gì xảy ra khi thiếu bước cơ sở, hoặc khi chỉ kiểm tra hữu hạn trường hợp (biểu thức $$n^2 + n + 41$$ cho giá trị nguyên tố với $$n = 0, \ldots, 39$$ nhưng là hợp số tại $$n = 40$$).

<div class="interactive-demo" markdown="1">
<div data-demo="induction-explainer" data-preset="sum"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

### Video ngắn: Quy nạp toán học

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/induction-dominoes.mp4"></video>
</div>

Video dài khoảng 3 phút 20 giây, trình bày hình ảnh domino và hai bước của quy nạp, chứng minh $$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$, ví dụ $$n^2 + n + 41$$ cho thấy thử nhiều giá trị chưa phải là chứng minh, hai lỗi chứng minh sai (quên bước cơ sở, bài toán "mọi con ngựa cùng màu") và phần giới thiệu quy nạp mạnh.

## Nguyên lý quy nạp toán học

Giả sử $$P(n)$$ là một mệnh đề phụ thuộc vào số tự nhiên $$n$$, và ta cần chứng minh:

<div class="textbook-equation" markdown="1">
$$P(n) \text{ đúng với mọi } n \ge n_0$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta thực hiện hai bước:

1. **Bước cơ sở**: Chứng minh $$P(n_0)$$ đúng.
2. **Bước quy nạp**: Giả sử $$P(k)$$ đúng với một số nguyên $$k \ge n_0$$ bất kỳ (gọi là *giả thiết quy nạp*), chứng minh $$P(k+1)$$ cũng đúng.

Khi đó, theo nguyên lý quy nạp toán học, $$P(n)$$ đúng với mọi $$n \ge n_0$$.

### Dạng logic

<div class="textbook-equation" markdown="1">
$$P(n_0) \wedge \forall k \ge n_0\,[P(k) \Rightarrow P(k+1)] \Rightarrow \forall n \ge n_0\, P(n)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Trong bước quy nạp, câu mở đầu chuẩn là:

> Giả sử với một $$k \ge n_0$$ bất kỳ, mệnh đề $$P(k)$$ đúng.

Sau đó, ta nêu rõ mục tiêu:

> Cần chứng minh $$P(k+1)$$ đúng.

Lưu ý rằng ta **không được** chọn một giá trị cụ thể như $$k=5$$, vì bước quy nạp phải đúng với mọi $$k \ge n_0$$.

![Trực quan hóa quy nạp](/discrete-mathematics-for-computer-science-iuh/img/course/Visualization_of_induction.svg)

<p class="textbook-figure-caption" data-figure="3.13">Trực quan hóa quy nạp toán học — hai bước cơ sở và quy nạp kết hợp để khẳng định mệnh đề đúng với mọi $n$.</p>
## Mẫu trình bày một chứng minh quy nạp

Khi viết lời giải, nên tuân theo cấu trúc sau:

1. Nêu rõ mệnh đề $$P(n)$$ và miền giá trị của $$n$$.
2. Chứng minh bước cơ sở tại $$n = n_0$$.
3. Phát biểu giả thiết quy nạp: "Giả sử $$P(k)$$ đúng với một $$k \ge n_0$$ bất kỳ".
4. Chứng minh $$P(k+1)$$ đúng.
5. Kết luận theo nguyên lý quy nạp toán học.

### Giải thích: Chạy tay một chứng minh quy nạp bất đẳng thức $$2^n > n^2$$ (với mọi $$n \ge 5$$)

Chú ý điểm khởi đầu không phải lúc nào cũng là $$n = 1$$! Với $$n = 2, 3, 4$$ ta thấy $$2^4 = 16 \not> 16 = 4^2$$. Mệnh đề chỉ bắt đầu đúng từ $$n_0 = 5$$:

1. **Bước cơ sở ($$n = 5$$)**:
   - Vế trái: $$2^5 = 32$$. Vế phải: $$5^2 = 25$$. Vì $$32 > 25$$, $$P(5)$$ **Đúng**!
2. **Giả thiết quy nạp**: Giả sử với một số nguyên $$k \ge 5$$ nào đó, ta đã có $$2^k > k^2$$.
3. **Bước quy nạp (chứng minh $$2^{k+1} > (k+1)^2$$)**:
   Xuất phát từ vế trái và dùng giả thiết quy nạp:
   $$2^{k+1} = 2 \cdot 2^k > 2k^2 = k^2 + k^2.$$
   Ta cần so sánh $$k^2 + k^2$$ với $$(k+1)^2 = k^2 + 2k + 1$$, tức là chỉ cần kiểm tra $$k^2 > 2k + 1$$ với $$k \ge 5$$:
   $$k^2 - 2k - 1 = (k - 1)^2 - 2 \ge (5 - 1)^2 - 2 = 16 - 2 = 14 > 0!$$
   Do đó $$k^2 > 2k + 1$$, suy ra:
   $$2^{k+1} > k^2 + k^2 > k^2 + 2k + 1 = (k+1)^2.$$
4. **Kết luận**: Theo nguyên lý quy nạp toán học, $$2^n > n^2$$ đúng với mọi số nguyên $$n \ge 5$$ (giải thích trực tiếp vì sao thuật toán $$O(2^n)$$ luôn chậm hơn $$O(n^2)$$ ngay từ kích thước rất nhỏ!).

## Sai lầm thường gặp khi học quy nạp

1. **Quên bước cơ sở**: Không chứng minh điểm khởi đầu thì chuỗi suy luận không có cơ sở để bắt đầu.
2. **Dùng giả thiết quy nạp sai phạm vi**: Giả thiết quy nạp thông thường chỉ cho phép dùng $$P(k)$$, không cho phép tự ý giả sử $$P(k+2)$$ hay một mệnh đề mạnh hơn.
3. **Không nêu rõ mục tiêu**: Biến đổi dài dòng nhưng không ghi rõ biểu thức cần chứng minh cho $$P(k+1)$$.
4. **Thay chứng minh bằng ví dụ**: Kiểm tra một số giá trị đầu không thể thay thế chứng minh quy nạp.
5. **Nhầm chiều suy luận**: Phải đi từ giả thiết $$P(k)$$ để suy ra $$P(k+1)$$, không được giả sử cả hai cùng đúng.
6. **Bỏ qua điều kiện miền giá trị**: Có những mệnh đề chỉ đúng từ một ngưỡng nhất định (ví dụ $$n \ge 4$$ hoặc $$n \ge 5$$), nên phải chọn đúng $$n_0$$ ở bước cơ sở.

## Ví dụ 1: Tổng của $$n$$ số tự nhiên đầu tiên

<div class="textbook-lemma" markdown="1">
**Mệnh đề.** Với mọi $$n \ge 1$$,

<div class="textbook-equation" markdown="1">
$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh.**

**Bước cơ sở**: Với $$n=1$$,

<div class="textbook-equation" markdown="1">
$$1 = \frac{1(1+1)}{2} = 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mệnh đề đúng tại $$n=1$$.

**Bước quy nạp**: Giả sử với một $$k \ge 1$$ bất kỳ, ta có:

<div class="textbook-equation" markdown="1">
$$1 + 2 + \cdots + k = \frac{k(k+1)}{2}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cần chứng minh:

<div class="textbook-equation" markdown="1">
$$1 + 2 + \cdots + k + (k+1) = \frac{(k+1)(k+2)}{2}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Thật vậy, áp dụng giả thiết quy nạp ta được:

<div class="textbook-equation" markdown="1">
$$1 + 2 + \cdots + k + (k+1) = \frac{k(k+1)}{2} + (k+1)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Suy ra mệnh đề đúng với $$k+1$$.

Vậy theo nguyên lý quy nạp toán học, công thức đúng với mọi $$n \ge 1$$.
</div>

Đây là ví dụ mẫu mực vì biểu thức tại $$k+1$$ tách trực tiếp thành phần ứng với $$k$$ cộng thêm số hạng mới.

![Chứng minh Pythagore](/discrete-mathematics-for-computer-science-iuh/img/course/Pythagorean_proof.svg)

<p class="textbook-figure-caption" data-figure="3.14">Chứng minh hình học — quy nạp thường gắn với trực giác hình học, chẳng hạn tổng $n$ số lẻ đầu tiên bằng $n^2$ tương ứng với diện tích hình vuông cạnh $n$.</p>
## Ví dụ 2: Tổng cấp số nhân

<div class="textbook-lemma" markdown="1">
**Mệnh đề.** Với mọi $$n \ge 0$$,

<div class="textbook-equation" markdown="1">
$$1 + 2 + 2^2 + \cdots + 2^n = 2^{n+1} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh.**

**Bước cơ sở**: Với $$n=0$$,

<div class="textbook-equation" markdown="1">
$$1 = 2^{0+1} - 1 = 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mệnh đề đúng tại $$n=0$$.

**Bước quy nạp**: Giả sử với một $$k \ge 0$$ bất kỳ,

<div class="textbook-equation" markdown="1">
$$1 + 2 + 2^2 + \cdots + 2^k = 2^{k+1} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cần chứng minh:

<div class="textbook-equation" markdown="1">
$$1 + 2 + 2^2 + \cdots + 2^k + 2^{k+1} = 2^{k+2} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta có:

<div class="textbook-equation" markdown="1">
$$1 + 2 + 2^2 + \cdots + 2^k + 2^{k+1} = (2^{k+1} - 1) + 2^{k+1} = 2^{k+2} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy mệnh đề đúng với mọi $$n \ge 0$$.
</div>

Tổng này thường xuất hiện khi đếm số nút của cây nhị phân đầy đủ theo từng mức hoặc khi phân tích các thuật toán chia đôi dữ liệu.

## Ví dụ 3: Tính chia hết

<div class="textbook-lemma" markdown="1">
**Mệnh đề.** Với mọi $$n \ge 1$$, số $$7^n - 1$$ chia hết cho $$6$$.
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh.**

**Bước cơ sở**: Với $$n=1$$,

<div class="textbook-equation" markdown="1">
$$7^1 - 1 = 6$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
chia hết cho $$6$$.

**Bước quy nạp**: Giả sử với một $$k \ge 1$$ bất kỳ, $$7^k - 1$$ chia hết cho $$6$$. Khi đó tồn tại số nguyên $$m$$ sao cho:

<div class="textbook-equation" markdown="1">
$$7^k - 1 = 6m$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cần chứng minh $$7^{k+1} - 1$$ chia hết cho $$6$$. Ta có:

<div class="textbook-equation" markdown="1">
$$7^{k+1} - 1 = 7 \cdot 7^k - 1 = 7(7^k - 1) + 6$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Theo giả thiết quy nạp, $$7^k - 1 = 6m$$, do đó:

<div class="textbook-equation" markdown="1">
$$7^{k+1} - 1 = 7 \cdot 6m + 6 = 6(7m + 1)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Suy ra $$7^{k+1} - 1$$ chia hết cho $$6$$.

Vậy mệnh đề đúng với mọi $$n \ge 1$$.
</div>

Trong các bài toán chia hết, sau khi áp dụng giả thiết quy nạp, ta thường biến đổi biểu thức về dạng:

<div class="textbook-equation" markdown="1">
$$d \times (\text{số nguyên})$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
với $$d$$ là ước số cần chứng minh.

## Ví dụ 4: Bất đẳng thức Bernoulli

<div class="textbook-lemma" markdown="1">
**Mệnh đề.** Với mọi $$n \in \mathbb{N}$$ và mọi $$x \ge -1$$,

<div class="textbook-equation" markdown="1">
$$(1+x)^n \ge 1 + nx$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh.**

**Bước cơ sở**: Với $$n=0$$,

<div class="textbook-equation" markdown="1">
$$(1+x)^0 = 1 = 1 + 0x$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mệnh đề đúng tại $$n=0$$.

**Bước quy nạp**: Giả sử với một $$k \ge 0$$ bất kỳ,

<div class="textbook-equation" markdown="1">
$$(1+x)^k \ge 1 + kx$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cần chứng minh:

<div class="textbook-equation" markdown="1">
$$(1+x)^{k+1} \ge 1 + (k+1)x$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Nhân hai vế giả thiết quy nạp với $$1+x \ge 0$$, chiều bất đẳng thức không đổi:

<div class="textbook-equation" markdown="1">
$$(1+x)^{k+1} = (1+x)^k(1+x) \ge (1+kx)(1+x)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Tiếp tục khai triển:

<div class="textbook-equation" markdown="1">
$$(1+kx)(1+x) = 1 + (k+1)x + kx^2 \ge 1 + (k+1)x$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
vì $$kx^2 \ge 0$$.

Vậy mệnh đề đúng với mọi $$n \in \mathbb{N}$$.
</div>

Trong bài này, điều kiện $$x \ge -1$$ đóng vai trò thiết yếu vì nó đảm bảo $$1+x \ge 0$$, nhờ đó phép nhân hai vế với $$(1+x)$$ giữ nguyên chiều bất đẳng thức.

## Ví dụ 5: Tổng các số lẻ đầu tiên

<div class="textbook-lemma" markdown="1">
**Mệnh đề.** Với mọi $$n \ge 1$$,

<div class="textbook-equation" markdown="1">
$$1 + 3 + 5 + \cdots + (2n-1) = n^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh.**

**Bước cơ sở**: Với $$n=1$$,

<div class="textbook-equation" markdown="1">
$$1 = 1^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mệnh đề đúng tại $$n=1$$.

**Bước quy nạp**: Giả sử với một $$k \ge 1$$ bất kỳ,

<div class="textbook-equation" markdown="1">
$$1 + 3 + 5 + \cdots + (2k-1) = k^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cần chứng minh:

<div class="textbook-equation" markdown="1">
$$1 + 3 + 5 + \cdots + (2k-1) + (2k+1) = (k+1)^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta có:

<div class="textbook-equation" markdown="1">
$$1 + 3 + 5 + \cdots + (2k-1) + (2k+1) = k^2 + (2k+1) = (k+1)^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy mệnh đề đúng với mọi $$n \ge 1$$.
</div>

Về mặt hình học, để mở rộng một hình vuông cạnh $$k$$ thành hình vuông cạnh $$k+1$$, ta thêm một viền gồm đúng $$2k+1$$ ô vuông. Ví dụ này cho thấy quy nạp gắn liền với cả biến đổi đại số lẫn trực giác hình học.

## Ví dụ 6: Ứng dụng trong Khoa học Máy tính — Bất biến vòng lặp

Trong lập trình, **bất biến vòng lặp** (loop invariant) là một tính chất được bảo toàn sau mỗi lần lặp; cách chứng minh tính chất này thực chất dựa trên quy nạp.

Xét thuật toán tính tổng sau:

```text
sum := 0
for i := 1 to n do
    sum := sum + i
```

Ta cần chứng minh rằng sau khi kết thúc vòng lặp, `sum = 1 + 2 + ... + n`.

### Bất biến vòng lặp

Sau khi kết thúc lần lặp thứ $$k$$, ta có:

<div class="textbook-equation" markdown="1">
$$sum = 1 + 2 + \cdots + k$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đây là một mệnh đề phụ thuộc vào số lần lặp $$k$$, và ta chứng minh nó bằng quy nạp theo $$k$$.

**Bước cơ sở**: Sau lần lặp thứ nhất ($$k=1$$), `sum = 1`, đúng với công thức.

**Bước quy nạp**: Giả sử sau lần lặp thứ $$k$$, ta có:

<div class="textbook-equation" markdown="1">
$$sum = 1 + 2 + \cdots + k$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ở lần lặp thứ $$k+1$$, chương trình cộng thêm $$(k+1)$$, nên giá trị mới là:

<div class="textbook-equation" markdown="1">
$$sum = 1 + 2 + \cdots + k + (k+1)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Như vậy bất biến đúng tại bước $$k+1$$. Do đó, sau lần lặp thứ $$n$$, chương trình cho kết quả đúng.

Quy nạp vì vậy là nền tảng của nhiều chứng minh về tính đúng đắn của chương trình.

![Đồ thị luồng điều khiển](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

<p class="textbook-figure-caption" data-figure="3.15">Đồ thị luồng điều khiển — bất biến vòng lặp được chứng minh bằng quy nạp theo số lần lặp, tương ứng với bước quy nạp $P(k) \Rightarrow P(k+1)$.</p>
## Ví dụ 7: Ứng dụng trong Khoa học Máy tính — Số nút của cây nhị phân đầy đủ

<div class="textbook-lemma" markdown="1">
**Mệnh đề.** Một cây nhị phân đầy đủ (mọi mức đều chứa đủ số nút tối đa) có chiều cao $$h$$ (gốc ở mức $$0$$) có tổng số nút là:

<div class="textbook-equation" markdown="1">
$$1 + 2 + 2^2 + \cdots + 2^h = 2^{h+1} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh theo quy nạp trên $$h$$.**

**Bước cơ sở**: Với $$h=0$$, cây chỉ có nút gốc, nên số nút là $$1 = 2^{0+1} - 1$$.

**Bước quy nạp**: Giả sử cây đầy đủ chiều cao $$k$$ có $$2^{k+1} - 1$$ nút. Xét cây đầy đủ chiều cao $$k+1$$: khi thêm mức thứ $$k+1$$, mức này có $$2^{k+1}$$ nút. Do đó tổng số nút là:

<div class="textbook-equation" markdown="1">
$$(2^{k+1} - 1) + 2^{k+1} = 2^{k+2} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mệnh đề đúng với $$k+1$$. Vậy công thức đúng với mọi $$h \ge 0$$.
</div>

Cây nhị phân xuất hiện rộng rãi trong các cấu trúc như heap, cây tìm kiếm nhị phân, cây cú pháp, cây biểu thức số học và các thuật toán duyệt cây theo mức. Do đó, quy nạp trên chiều cao hoặc cấu trúc cây là kỹ năng rất thiết thực.

## Ví dụ 8: Ứng dụng trong Khoa học Máy tính — Tính đúng đắn của hàm đệ quy

Xét thuật toán đệ quy tính giai thừa:

```text
factorial(n):
    if n = 0 then return 1
    else return n * factorial(n-1)
```

Ta cần chứng minh hàm `factorial(n)` trả về đúng giá trị $$n!$$ với mọi $$n \ge 0$$.

**Bước cơ sở**: Với $$n=0$$, hàm trả về `1`, đúng bằng $$0! = 1$$.

**Bước quy nạp**: Giả sử lời gọi `factorial(k)` trả về đúng $$k!$$ với một $$k \ge 0$$ bất kỳ. Khi gọi `factorial(k+1)`, hàm tính:

```text
factorial(k+1) = (k+1) * factorial(k)
```

Theo giả thiết quy nạp, `factorial(k) = k!`, nên:

<div class="textbook-equation" markdown="1">
$$factorial(k+1) = (k+1)k! = (k+1)!$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy hàm trả về đúng kết quả với $$k+1$$. Do đó chương trình đúng với mọi $$n \ge 0$$. $$\square$$

Chứng minh hàm đệ quy thường gắn liền với quy nạp, vì bản thân lời gọi đệ quy giả định kết quả đúng trên bài toán con nhỏ hơn.

## Ví dụ 9: Ứng dụng trong Khoa học Máy tính — Giải quan hệ truy hồi

Giả sử một thuật toán chia để trị có thời gian chạy thỏa mãn quan hệ truy hồi:

<div class="textbook-equation" markdown="1">
$$T(1) = 1, \qquad T(n) = 2T(n/2) + n \text{ với } n = 2^m$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta cần chứng minh rằng với mọi $$n$$ là lũy thừa của $$2$$:

<div class="textbook-equation" markdown="1">
$$T(n) = n \log_2 n + n$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Bước cơ sở**: Với $$m=0$$ (tức $$n=1$$),

<div class="textbook-equation" markdown="1">
$$T(1) = 1 = 1 \cdot \log_2 1 + 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mệnh đề đúng tại $$m=0$$.

**Bước quy nạp**: Giả sử công thức đúng với $$n = 2^m$$, tức là:

<div class="textbook-equation" markdown="1">
$$T(2^m) = 2^m m + 2^m$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cần chứng minh:

<div class="textbook-equation" markdown="1">
$$T(2^{m+1}) = 2^{m+1}(m+1) + 2^{m+1}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta có:

<div class="textbook-equation" markdown="1">
$$T(2^{m+1}) = 2T(2^m) + 2^{m+1}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$= 2(2^m m + 2^m) + 2^{m+1} = 2^{m+1}m + 2^{m+1} + 2^{m+1}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$= 2^{m+1}m + 2^{m+2} = 2^{m+1}(m+2)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mặt khác,

<div class="textbook-equation" markdown="1">
$$2^{m+1}(m+1) + 2^{m+1} = 2^{m+1}(m+2)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Hai vế bằng nhau, nên công thức đúng với $$m+1$$. Vậy với mọi $$n = 2^m$$:

<div class="textbook-equation" markdown="1">
$$T(n) = n \log_2 n + n$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
$$\square$$

Đây là dạng phân tích quen thuộc khi đánh giá thời gian chạy của merge sort, cây đoạn (segment tree) và nhiều thuật toán chia để trị khác.

## Ứng dụng trong Khoa học Máy tính

Khi áp dụng quy nạp vào lập trình và hệ thống, cần xác định rõ các yếu tố được mô hình hóa và các yếu tố được lược bỏ. Quy nạp xuất hiện thường xuyên trong nhiều mảng của khoa học máy tính:

### Chứng minh tính đúng đắn của thuật toán

- Quy nạp theo số bước lặp.
- Quy nạp theo kích thước đầu vào.
- Quy nạp theo độ sâu lời gọi đệ quy.

### Phân tích cấu trúc dữ liệu đệ quy

- Danh sách liên kết.
- Cây nhị phân và cây tổng quát.
- Cây cú pháp trừu tượng (AST).

### Phân tích thời gian chạy

- Giải và kiểm chứng nghiệm của quan hệ truy hồi.
- Chứng minh cận trên và cận dưới độ phức tạp.
- Xác minh công thức thời gian của thuật toán đệ quy.

### Chứng minh tính chất của chương trình

- Bất biến vòng lặp và tiền/hậu điều kiện.
- Số lượng thao tác sau $$n$$ bước lặp.
- Tính dừng của một số quá trình tính toán.

### Tư duy phân rã theo cấu trúc

Một kỹ năng quan trọng trong khoa học máy tính là trả lời câu hỏi: "Bài toán lớn được cấu thành từ những bài toán con nào?" Quy nạp buộc ta mô tả mối liên hệ đó một cách chính xác.

## Bài toán con thỏ (Fibonacci)

Một ví dụ kinh điển kết nối quy nạp với lập trình đệ quy là **bài toán con thỏ** do Leonardo Fibonacci nêu ra khoảng năm 1202 trong tác phẩm *Liber Abaci*.

### Đề bài

Giả sử ta đặt **một đôi thỏ** mới sinh vào một chuồng kín với các quy tắc sau:

1. Mỗi đôi thỏ sinh **một đôi con** mỗi tháng, bắt đầu từ **tháng thứ hai** sau khi sinh.
2. Một đôi con cần **đúng một tháng** để trưởng thành trước khi bắt đầu sinh sản.
3. Thỏ không chết và không rời khỏi chuồng.

**Câu hỏi:** Sau $$n$$ tháng, có bao nhiêu đôi thỏ trong chuồng?

### Mô hình hóa

Gọi $$F_n$$ là số đôi thỏ vào **cuối tháng** $$n$$.

| Tháng $$n$$ | $$F_n$$ | Giải thích |
|:---:|:---:|:---|
| 1 | 1 | Một đôi ban đầu, chưa sinh con |
| 2 | 1 | Đôi ban đầu vừa trưởng thành |
| 3 | 2 | Giữ 1 đôi cũ, thêm 1 đôi con |
| 4 | 3 | Giữ 2 đôi cũ, thêm 1 đôi con từ đôi trưởng thành |
| 5 | 5 | Giữ 3 đôi cũ, thêm 2 đôi con |

**Ý tưởng cốt lõi:** Vào cuối tháng $$n$$, ta vẫn có toàn bộ $$F_{n-1}$$ đôi từ tháng trước. Số đôi con mới sinh trong tháng $$n$$ đúng bằng số đôi **đã trưởng thành** — tức các đôi đã tồn tại từ cuối tháng $$n-2$$, bằng $$F_{n-2}$$.

Do đó:

<div class="textbook-equation" markdown="1">
$$F_n = F_{n-1} + F_{n-2}, \qquad n \ge 3$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
với điều kiện đầu $$F_1 = 1$$, $$F_2 = 1$$. Dãy thu được gọi là **dãy Fibonacci**: $$1, 1, 2, 3, 5, 8, 13, 21, \ldots$$

*(Một số tài liệu đánh chỉ số từ $$F_0 = 0$$, $$F_1 = 1$$; đây vẫn là cùng một dãy, chỉ khác vị trí bắt đầu.)*

### Liên hệ với đệ quy

Hàm tính số Fibonacci trong lập trình phản ánh trực tiếp cấu trúc quy nạp:

```python
def fib(n):
    if n <= 2:
        return 1              # bước cơ sở: F_1, F_2
    return fib(n-1) + fib(n-2)  # bước đệ quy: F_n = F_{n-1} + F_{n-2}
```

- **Bước cơ sở** tương ứng với điều kiện đầu $$F_1, F_2$$.
- **Bước đệ quy** tương ứng với quan hệ truy hồi: dùng kết quả đúng ở các chỉ số nhỏ hơn để tính giá trị hiện tại.

<div class="textbook-example" markdown="1">
**Ví dụ quy nạp trên dãy Fibonacci:**

Sau khi thiết lập quan hệ truy hồi, ta có thể dùng quy nạp để chứng minh các tính chất của dãy.

<div class="textbook-lemma" markdown="1">
**Mệnh đề.** Với mọi $$n \ge 1$$,

<div class="textbook-equation" markdown="1">
$$F_1 + F_2 + \cdots + F_n = F_{n+2} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Chứng minh.**

**Bước cơ sở** ($$n=1$$): $$F_1 = 1 = F_3 - 1 = 2 - 1$$. Mệnh đề đúng tại $$n=1$$.

**Bước quy nạp**: Giả sử với một $$k \ge 1$$ bất kỳ,

<div class="textbook-equation" markdown="1">
$$F_1 + \cdots + F_k = F_{k+2} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Cần chứng minh:

<div class="textbook-equation" markdown="1">
$$F_1 + \cdots + F_k + F_{k+1} = F_{k+3} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta có:

<div class="textbook-equation" markdown="1">
$$F_1 + \cdots + F_k + F_{k+1} = (F_{k+2} - 1) + F_{k+1} = F_{k+3} - 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
vì $$F_{k+3} = F_{k+2} + F_{k+1}$$ theo quan hệ truy hồi. Vậy mệnh đề đúng với mọi $$n \ge 1$$. $$\square$$

Bài toán con thỏ minh họa quy trình quen thuộc trong khoa học máy tính: **mô hình hóa** → **định nghĩa truy hồi/đệ quy** → **chứng minh tính chất bằng quy nạp**.
</div>


## Liên hệ giữa quy nạp và quan hệ truy hồi

Quan hệ truy hồi dùng để **định nghĩa** một đại lượng dựa trên các giá trị trước đó, còn quy nạp dùng để **chứng minh** công thức tổng quát hoặc tính chất của đại lượng đó.

Ví dụ, xét dãy số xác định bởi:

<div class="textbook-equation" markdown="1">
$$a_1 = 1, \qquad a_{n+1} = a_n + 2n + 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta có thể dự đoán công thức tổng quát:

<div class="textbook-equation" markdown="1">
$$a_n = n^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
và dùng quy nạp để chứng minh dự đoán này.

### Minh họa nhanh

**Bước cơ sở**: $$a_1 = 1 = 1^2$$.

**Bước quy nạp**: Giả sử $$a_k = k^2$$ với một $$k \ge 1$$ bất kỳ. Khi đó:

<div class="textbook-equation" markdown="1">
$$a_{k+1} = a_k + 2k + 1 = k^2 + 2k + 1 = (k+1)^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy $$a_n = n^2$$ với mọi $$n \ge 1$$.

## Khi nào nên nghĩ đến quy nạp?

Ta nên cân nhắc dùng quy nạp khi gặp các dấu hiệu sau:

1. Mệnh đề phát biểu cho "mọi số tự nhiên $$n \ge n_0$$".
2. Biểu thức tại $$n+1$$ liên hệ trực tiếp với biểu thức tại $$n$$.
3. Đối tượng được xây dựng từng bước hoặc định nghĩa đệ quy.
4. Biểu thức chứa tổng, tích, lũy thừa hoặc số lượng nút/mức của cấu trúc.
5. Bài toán liên quan đến thuật toán đệ quy, vòng lặp, cây hoặc dãy số.

## Checklist viết bước quy nạp

Khi trình bày một chứng minh quy nạp, có thể kiểm tra theo các bước sau:

1. Xác định rõ mệnh đề $$P(n)$$.
2. Nêu rõ miền giá trị của $$n$$.
3. Chọn đúng điểm bắt đầu $$n_0$$.
4. Kiểm chứng bước cơ sở $$P(n_0)$$ bằng tính toán trực tiếp.
5. Ở bước quy nạp, phát biểu rõ: "Giả sử $$P(k)$$ đúng với một $$k \ge n_0$$ bất kỳ".
6. Viết rõ mục tiêu: "Cần chứng minh $$P(k+1)$$ đúng".
7. Xuất phát từ biểu thức của $$P(k+1)$$ (hoặc vế thuận tiện hơn) để biến đổi.
8. Chỉ sử dụng đúng nội dung giả thiết quy nạp cho phép.
9. Kết luận rõ ràng theo nguyên lý quy nạp.

<div class="interactive-tool" markdown="1">
## Bài tập tự luyện

### Bài 1

Chứng minh bằng quy nạp rằng với mọi $$n \ge 1$$,

<div class="textbook-equation" markdown="1">
$$1 + 3 + 5 + \cdots + (2n-1) = n^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bài 2

Chứng minh bằng quy nạp rằng với mọi $$n \ge 1$$,

<div class="textbook-equation" markdown="1">
$$1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bài 3

Chứng minh rằng với mọi $$n \ge 1$$, số $$5^n - 1$$ chia hết cho $$4$$.

### Bài 4

Chứng minh rằng với mọi $$n \ge 5$$,

<div class="textbook-equation" markdown="1">
$$2^n > n^2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
*Gợi ý:* Chọn đúng bước cơ sở là điểm quan trọng của bài này.

### Bài 5

Một cây nhị phân đầy đủ (mọi mức đều đủ nút) có $$h$$ mức (tính từ mức $$1$$). Hãy chứng minh rằng số lá của cây là $$2^{h-1}$$.

### Bài 6

Xét đoạn mã sau:

```text
product := 1
for i := 1 to n do
    product := 2 * product
```

Hãy dùng quy nạp theo số vòng lặp để chứng minh rằng sau khi kết thúc, `product = 2^n`.

### Bài 7

Cho hàm đệ quy:

```text
power2(n):
    if n = 0 then return 1
    else return 2 * power2(n-1)
```

Hãy chứng minh bằng quy nạp rằng `power2(n)` trả về đúng giá trị $$2^n$$ với mọi $$n \ge 0$$.

### Bài 8 — Sửa lỗi chứng minh

Một sinh viên muốn chứng minh rằng với mọi $$n \ge 1$$,

<div class="textbook-equation" markdown="1">
$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
và viết như sau:

> Giả sử công thức đúng với $$n=k+1$$. Khi đó
> $$1 + 2 + \cdots + k + (k+1) = \frac{(k+1)(k+2)}{2}$$
> nên công thức đúng.

Hãy chỉ ra chỗ sai trong lập luận trên và viết lại bước quy nạp cho đúng.

### Bài 9 — Bài tập ứng dụng khoa học máy tính

Giả sử một thuật toán đệ quy có số lời gọi hàm thỏa mãn:

<div class="textbook-equation" markdown="1">
$$C(0) = 1, \qquad C(n+1) = C(n) + 2$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Hãy dùng quy nạp để chứng minh rằng:

<div class="textbook-equation" markdown="1">
$$C(n) = 2n + 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

## Công cụ tương tác

Điền bước cơ sở và bước quy nạp, rồi kiểm tra xem các giả thiết đã được sử dụng đúng hay chưa.
<div class="interactive-demo" markdown="1">
<div data-demo="induction-checker"></div>
</div>
<script src="{{ '/public/js/induction-step-checker.js' | relative_url }}"></script>

## Bài tập bổ sung: Quy nạp toán học

**Hướng dẫn chung:**

1. Chứng minh $$P(n)$$ đúng với giá trị nhỏ nhất $$n_0$$.
2. Giả thiết quy nạp: giả sử $$P(k)$$ đúng với một số nguyên $$k \ge n_0$$ bất kỳ.
3. Chứng minh rằng nếu $$P(k)$$ đúng thì $$P(k+1)$$ cũng đúng.

**Bài tập 1:** $$\sum_{k=1}^n k = \frac{n(n+1)}{2}$$ với mọi $$n \ge 1$$.

**Bài tập 2:** $$2^n \ge n^2$$ với mọi $$n \ge 4$$.

**Bài tập 3:** $$1 + 3 + 5 + \cdots + (2n - 1) = n^2$$ với mọi $$n \ge 1$$.

**Bài tập 4:** $$3^n \ge 2^{n+1}$$ với mọi $$n \ge 2$$.

**Bài tập 5:** $$n^3 - n$$ chia hết cho $$6$$ với mọi $$n \ge 1$$.

**Bài tập 6:** $$\frac{n(n+1)(2n+1)}{6}$$ là số nguyên với mọi $$n \ge 1$$.

---

## Xem thêm / Video gợi ý

- [How to Write a Proof](https://www.youtube.com/watch?v=7jZ5n8k0p0Q) — 3Blue1Brown (Essence of mathematics)
- [Direct Proof, Contradiction, Induction](https://www.youtube.com/watch?v=6l7L9v0p0Q) — MIT OCW (Gilbert Strang style clarity)


## Tóm tắt

- **Quy nạp toán học**: chứng minh bước cơ sở $$P(n_0)$$ và bước quy nạp $$P(k) \Rightarrow P(k+1)$$ để suy ra $$P(n)$$ đúng với mọi $$n \ge n_0$$.
- Giả thiết quy nạp chỉ áp dụng cho một $$k \ge n_0$$ bất kỳ (không chọn giá trị cụ thể và không giả sử sẵn cho mọi $$n$$).
- Ứng dụng: chứng minh công thức tổng, tính chia hết, bất đẳng thức, bất biến vòng lặp và tính đúng đắn của hàm đệ quy.
- Quan hệ truy hồi dùng để **định nghĩa** dãy; quy nạp dùng để **chứng minh** tính chất của dãy.
- Liên hệ khoa học máy tính: bất biến vòng lặp (loop invariant), phân tích thời gian chạy và chứng minh thuật toán đệ quy.

Trong chương tiếp theo, chúng ta sẽ chuyển sang **lý thuyết tập hợp** — một nền tảng cơ bản của toán học rời rạc.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Y58qpGu_N1U">M03 - Bài 3- Quy nạp toán học | Nguyễn Hữu Hoàng Tùng Official</a> — Nguyễn Hữu Hoàng Tùng Official, tiếng Việt. Giới thiệu quy nạp toán học bằng tiếng Việt với bước cơ sở và bước quy nạp.
- <a href="https://www.youtube.com/watch?v=Tm2PJPvAULs">MATHEMATICAL INDUCTION - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Khuôn mẫu chứng minh quy nạp trên dãy và tổng.
- <a href="https://www.youtube.com/watch?v=GdM_iA1Zek4">Intro to Mathematical Induction</a> — Dr. Trefor Bazett, tiếng Anh. Một bài chứng minh quy nạp đầy đủ từ giả thiết $$P(k)$$ sang $$P(k+1)$$.

</div>
