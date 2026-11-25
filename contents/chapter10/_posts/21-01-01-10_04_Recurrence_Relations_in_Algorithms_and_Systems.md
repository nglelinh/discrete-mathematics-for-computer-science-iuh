---
layout: post
title: "Hệ thức Truy hồi trong Thuật toán và Hệ thống"
categories: chapter10
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Tổng hợp các ứng dụng tiêu biểu của hệ thức truy hồi trong khoa học máy tính: từ Fibonacci, chia để trị, quy hoạch động đến mô hình tăng trưởng và xử lý tín hiệu."
---

Nếu ba bài đầu của Chương 10 trang bị cho bạn bộ công cụ đại số để giải truy hồi trên giấy, thì bài này mở rộng ống kính ra toàn bộ thế giới phần mềm và kỹ thuật: từ tốc độ của **Merge Sort**, bảng ghi nhớ của **Quy hoạch động**, đường cong tăng trưởng người dùng cho đến **bộ lọc tín hiệu số IIR** trong tai nghe chống ồn và các mô hình chuỗi trong AI hiện đại.

**Mạch bài học:** Từ bài toán đôi thỏ Fibonacci $$\longrightarrow$$ **Chia để trị & Định lý Thợ (Master Theorem)** $$\longrightarrow$$ **Quy hoạch động (DP)** $$\longrightarrow$$ mô hình tăng trưởng sản phẩm số, **bộ lọc IIR** trong DSP và tư duy trạng thái hồi quy trong AI.

## Bản đồ kiến thức nền: Vì sao truy hồi là ngôn ngữ chung của Thuật toán, DSP và AI?

- **Chia để trị & Định lý Thợ (Divide-and-Conquer & Master Theorem):** Biểu diễn thời gian chạy $$T(n) = aT(n/b) + f(n)$$ qua cuộc giằng co giữa tốc độ sinh nhánh đệ quy $$n^{\log_b a}$$ và chi phí gộp kết quả $$f(n)$$ tại mỗi tầng.
- **Quy hoạch động (Dynamic Programming = Recurrence + Memoization):** Biến một hệ thức truy hồi có các bài toán con gối nhau (overlapping subproblems) từ cây đệ quy mũ $$O(2^n)$$ thành bảng điền tuần tự đa thức $$O(n)$$ hoặc $$O(n^2)$$.
- **Hệ thống có ký ức (Stateful Systems — IIR Filters & RNN/SSM):** Trong xử lý tín hiệu số, bộ lọc phản hồi vô hạn $$y[n] = \alpha x[n] + (1-\alpha) y[n-1]$$ chính là truy hồi tuyến tính bậc 1; còn trong học sâu, mạng hồi quy (RNN) và mô hình không gian trạng thái (State Space Models như Mamba) đều cập nhật trạng thái ẩn $$h_t = F(h_{t-1}, x_t)$$ bằng đúng tư duy truy hồi.

Ở các bài trước, chúng ta đã định nghĩa, phân loại và học cách giải quan hệ truy hồi tuyến tính (cả thuần nhất lẫn không thuần nhất). Bài này tổng hợp những **ứng dụng quan trọng** của hệ thức truy hồi trong khoa học máy tính và kỹ thuật hệ thống. Thay vì mô tả trực tiếp từng giá trị độc lập, truy hồi cho phép ta diễn đạt quy luật "trạng thái hiện tại phụ thuộc vào các trạng thái trước như thế nào". Từ bài toán đôi thỏ của Fibonacci (năm 1202) đến thuật toán chia để trị, quy hoạch động, mô hình tăng trưởng người dùng và bộ lọc tín hiệu (IIR filter), truy hồi là ngôn ngữ tự nhiên của mọi hệ thống có **trạng thái và ký ức**.

---

## Phần 1: Góc nhìn lịch sử — Fibonacci và bài toán đôi thỏ

### Bài toán Fibonacci

Trong tác phẩm *Liber Abaci* xuất bản năm 1202, Leonardo of Pisa — thường được biết đến với tên gọi Fibonacci — đã đề xuất bài toán mô tả quá trình sinh sản của thỏ. Từ đó ra đời dãy số nổi tiếng:

<div class="textbook-equation" markdown="1">
$$
F_n = F_{n-1} + F_{n-2}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Giá trị sâu xa của bài toán không chỉ nằm ở bản thân dãy số, mà ở tư duy mô tả trạng thái tương lai thông qua các trạng thái gần nhất trong quá khứ.

### Tư duy truy hồi là tư duy cấu trúc

Rất nhiều hiện tượng trong tự nhiên, kinh tế và khoa học máy tính rất khó diễn tả nếu xét từng thời điểm tách rời nhau. Ngược lại, chúng trở nên rõ ràng và gọn gàng hơn nhiều khi được mô tả bằng một quy luật chuyển tiếp: *"Giá trị tiếp theo phụ thuộc vào một vài giá trị trước đó."* Chính vì vậy, hệ thức truy hồi trở thành cầu nối giữa việc nhận diện quy luật (pattern) và dự đoán hành vi hệ thống (prediction).

![Xoắn ốc Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Fibonacci_spiral.svg)

<p class="textbook-figure-caption" data-figure="10.15">Bài toán đôi thỏ của Fibonacci mở ra một cách mô tả tăng trưởng và cấu trúc lặp đầy sức mạnh trong toán học và khoa học máy tính.</p>

---

## Phần 2: Phân tích thuật toán chia để trị

### Vì sao chia để trị sinh ra hệ thức truy hồi?

Khi một thuật toán chia bài toán kích thước $$n$$ thành các bài toán con nhỏ hơn, giải đệ quy từng bài toán con rồi hợp nhất kết quả, tổng chi phí thực thi của nó thường thỏa mãn một hệ thức truy hồi. Chẳng hạn, với thuật toán Merge Sort:

<div class="textbook-equation" markdown="1">
$$
T(n) = 2T(n/2) + n
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Biểu thức này không phải ký hiệu hình thức, mà là bản tóm tắt chính xác cấu trúc thời gian chạy của thuật toán: chia đôi mảng thành 2 bài toán con kích thước $$n/2$$ và tốn chi phí tuyến tính $$n$$ để trộn kết quả.

### Video ngắn: Chia để trị và định lý thợ

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/divide-and-conquer-master.mp4"></video>
</div>

Video dài khoảng 2 phút 53 giây: cây đệ quy của $$T(n) = 2T(n/2) + n$$ với $$n = 16$$ (mỗi tầng tốn đúng $$n$$, tổng $$80 = n\log_2 n + n$$), cùng kết quả bằng cách thế ngược, tìm kiếm nhị phân $$T(n/2) + 1$$, hai trường hợp "lá thắng" $$4T(n/2) + n$$ và "gốc thắng" $$2T(n/2) + n^2$$, ba trường hợp của định lý thợ với bảng ví dụ (merge sort, Karatsuba, Strassen) và một hệ thức định lý không áp dụng được: $$2T(n/2) + n\log n$$.

### Định lý Thợ (Master Theorem) — công cụ phân tích gọn nhẹ

Định lý Thợ (Master Theorem) cho phép đánh giá nhanh độ phức tạp của lớp truy hồi chia để trị phổ biến:

<div class="textbook-equation" markdown="1">
$$
T(n)=aT(n/b)+f(n)
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nhờ công cụ này, kỹ sư phần mềm có thể nhanh chóng xác định:

- Thuật toán nào mở rộng (scale) tốt khi dữ liệu tăng lớn.
- Thuật toán nào có chi phí tăng quá nhanh và sớm chạm ngưỡng nghẽn cổ chai.
- Cải tiến tối ưu hóa nào thực sự tạo ra khác biệt đáng kể về bậc độ phức tạp.

### Từ giáo trình đến hệ thống thực tế

Tinh thần chia để trị hiện diện rộng rãi trong các hệ thống tìm kiếm, sắp xếp song song (parallel sort), xử lý cấu trúc cây, phân hoạch không gian hình học và các thuật toán biến đổi Fourier nhanh (FFT). Vì thế, kỹ năng phân tích hệ thức truy hồi không chỉ phục vụ việc học lý thuyết mà còn giúp đánh giá chi phí kiến trúc của các hệ thống thực tế.

![Master Theorem — phân tích chia để trị](/discrete-mathematics-for-computer-science-iuh/img/course/Master_theorem.png)

<p class="textbook-figure-caption" data-figure="10.16">Định lý Thợ (Master Theorem) giúp giải nhanh dạng $$T(n)=aT(n/b)+f(n)$$ — công cụ nền tảng khi phân tích Merge Sort, FFT và nhiều thuật toán chia để trị.</p>

![Merge Sort — sơ đồ thuật toán](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

<p class="textbook-figure-caption" data-figure="10.17">Mô hình chia để trị dẫn tới quan hệ truy hồi một cách tự nhiên qua ba pha: chia bài toán, giải đệ quy bài toán con và hợp nhất kết quả.</p>

---

## Phần 3: Quy hoạch động — truy hồi kết hợp với bộ nhớ

### Đệ quy ngây thơ và bài học về bài toán con gối nhau

Nếu cài đặt dãy Fibonacci trực tiếp theo định nghĩa đệ quy:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

chương trình sẽ lặp lại rất nhiều lời gọi hàm giống hệt nhau, khiến thời gian chạy bùng nổ theo hàm mũ.

### Ghi nhớ kết quả (Memoization) giúp truy hồi trở nên hiệu quả

Chỉ cần lưu lại các kết quả đã tính để tái sử dụng:

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

Đây chính là cốt lõi của quy hoạch động (dynamic programming): giữ nguyên công thức truy hồi, nhưng bổ sung bộ nhớ để tránh tính toán dư thừa.

### Quy hoạch động trong thực tế

Kỹ thuật quy hoạch động xuất hiện ở rất nhiều bài toán ứng dụng:

- Tìm đường đi ngắn nhất trên đồ thị (shortest paths).
- Gióng hàng chuỗi sinh học (sequence alignment).
- Tính khoảng cách biên tập giữa hai văn bản (edit distance).
- Phân bổ tài nguyên (resource allocation).
- Phân tích cú pháp (parsing) và tối ưu hóa theo trạng thái.

Nhìn bề ngoài, các bài toán này thuộc nhiều lĩnh vực khác nhau, nhưng khi đi vào bản chất, tất cả đều xoay quanh hai câu hỏi: *"Bài toán lớn được xây dựng từ những bài toán con nào?"* và *"Các bài toán con đó có bị tính lặp lại hay không?"*

![Dynamic programming — memoization](/discrete-mathematics-for-computer-science-iuh/img/course/Dsa_dynamic_programming_salmon_fish_memoized_step_n.png)

<p class="textbook-figure-caption" data-figure="10.18">Quy hoạch động khai thác công thức truy hồi kết hợp với cơ chế lưu trữ trạng thái, biến mô hình toán học thành thuật toán hiệu quả.</p>

![Cây gọi đệ quy Fibonacci — trước memoization](/discrete-mathematics-for-computer-science-iuh/img/course/Algorithms-F6CallTreeMemoized.png)

<p class="textbook-figure-caption" data-figure="10.19">Kỹ thuật memoization loại bỏ các lời gọi trùng lặp, đưa thời gian chạy từ bậc hàm mũ xuống bậc tuyến tính.</p>

---

## Phần 4: Mô hình hóa tăng trưởng dân số và sản phẩm số

### Truy hồi trong mô hình tăng trưởng dân số

Khi dân số năm sau phụ thuộc vào dân số năm hiện tại cùng các tỷ lệ sinh, tử và di cư, ta có thể biểu diễn trực tiếp bằng một hệ thức truy hồi. Ở dạng đơn giản nhất (tăng trưởng đều 2% mỗi năm):

<div class="textbook-equation" markdown="1">
$$
P_{n+1} = 1.02P_n
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Ở dạng tổng quát hơn:

<div class="textbook-equation" markdown="1">
$$
P_{n+1}=P_n + \text{births}_n - \text{deaths}_n + \text{migration}_n
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

### Từ sinh thái học đến tăng trưởng người dùng (User Growth)

Trong lĩnh vực sản phẩm số (digital products), cách tư duy tương tự được dùng để mô hình hóa các chỉ số cốt lõi như:

- Lượng người dùng hoạt động (active users).
- Tỷ lệ giữ chân người dùng (retention) và tỷ lệ rời bỏ (churn).
- Hiệu ứng giới thiệu (referrals) và tăng trưởng lan truyền (viral growth).

Nhờ vậy, bài toán tăng trưởng dân số không chỉ có ý nghĩa trong sinh thái học mà còn mang lại trực giác hữu ích khi phân tích động học tăng trưởng của sản phẩm công nghệ.

![Tháp Hà Nội — truy hồi exponential](/discrete-mathematics-for-computer-science-iuh/img/course/Tower_of_Hanoi.gif)

<p class="textbook-figure-caption" data-figure="10.20">Tháp Hà Nội với hệ thức $$H_n = 2H_{n-1}+1$$ minh họa rõ tốc độ tăng trưởng hàm mũ xuất phát từ một quy luật truy hồi rất đơn giản.</p>

---

## Phần 5: Xử lý tín hiệu và bộ lọc IIR

### Bộ lọc có ký ức

Trong xử lý tín hiệu số (Digital Signal Processing — DSP), nhiều bộ lọc tạo ra đầu ra (output) tại thời điểm hiện tại dựa trên đầu vào hiện tại, các đầu vào trước đó và cả các đầu ra trong quá khứ. Một dạng bộ lọc phản hồi xung vô hạn (IIR filter) đơn giản có công thức:

<div class="textbook-equation" markdown="1">
$$
y_n = a x_n + b y_{n-1}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Đây thực chất là một quan hệ truy hồi tuyến tính không thuần nhất bậc nhất.

### Ý nghĩa đối với sinh viên Khoa học Máy tính

Dù không phải ai cũng đi sâu vào xử lý tín hiệu, góc nhìn này vẫn rất giá trị trong thiết kế hệ thống nói chung:

- Hệ thống có trạng thái (stateful) luôn chịu ảnh hưởng từ lịch sử vận hành.
- Tính ổn định (stability) của hệ thống phụ thuộc trực tiếp vào độ lớn các hệ số (như mô-đun nghiệm đặc trưng $$\rho$$ đã học ở Bài 10.2).
- Hành vi dài hạn của hệ thống có thể được dự đoán sớm thông qua việc phân tích hệ thức truy hồi.

Tư duy này liên kết chặt chẽ với hệ thống điều khiển (control systems), xử lý luồng dữ liệu (stream processing), vòng phản hồi (feedback loops) và các mô hình chuỗi thời gian trong học máy.

---

## Phần 6: Tư duy truy hồi trong AI và hệ thống hiện đại

Ngay cả trong bối cảnh công nghệ AI và hệ thống phân tán phát triển nhanh chóng, tư duy truy hồi vẫn giữ vai trò trung tâm ở nhiều bài toán:

- Các kiến trúc mạng hồi quy (recurrent architectures) và mô hình không gian trạng thái (state-space models).
- Phân tích dữ liệu luồng (streaming analytics) và dự báo chuỗi thời gian (time-series forecasting).
- Cơ chế bộ nhớ đệm (caching dynamics) và cấu trúc dữ liệu đệ quy.

Hệ thức truy hồi chính là ngôn ngữ toán học để mô tả những hệ thống mà *"hôm nay mang dấu vết của hôm qua"* — đặc trưng phổ biến của phần lớn các hệ thống tính toán hiện đại.

---

## Kết luận

Từ bài toán đôi thỏ của Fibonacci đến Định lý Thợ, quy hoạch động, mô hình tăng trưởng người dùng và bộ lọc IIR, hệ thức truy hồi mang lại một góc nhìn sâu sắc về cấu trúc lặp và sự phụ thuộc theo thời gian. Trong khoa học máy tính, đây là năng lực quan trọng giúp kỹ sư nhìn thấy quy luật tổng thể đằng sau một quá trình, thay vì chỉ quan sát rời rạc từng bước thực thi.

---

### Minh hoạ tương tác

Khám phá Định lý Thợ cho truy hồi chia để trị $$T(n) = aT(n/b) + f(n)$$ và quan sát cây gọi đệ quy (với chế độ Fibonacci hiển thị số lần gọi hàm) qua công cụ dưới đây:

<div class="interactive-demo" markdown="1">
<div data-demo="recurrence-explainer" data-mode="dc"></div>
</div>
<script src="{{ '/public/js/explainers/recurrence-explainer.js' | relative_url }}"></script>

## Ví dụ tính tay cầm tay chỉ việc: Bộ lọc làm mượt IIR bậc 1 và Quy hoạch động cầu thang

**Phần A — Chạy tay bộ lọc làm mượt mũ (Exponential Moving Average — IIR bậc 1) trong giám sát độ trễ API:**
Hệ thức truy hồi: $$y_n = 0{,}5 x_n + 0{,}5 y_{n-1}$$ với $$y_0 = 0$$. Giả sử độ trễ API đo được có một cú sốc đơn vị ở giây 1 rồi trở về bình thường: $$x = (100, 0, 0, 0, \dots)$$ (ms).
- $$y_1 = 0{,}5(100) + 0{,}5(0) = 50\text{ ms}$$
- $$y_2 = 0{,}5(0) + 0{,}5(50) = 25\text{ ms}$$
- $$y_3 = 0{,}5(0) + 0{,}5(25) = 12{,}5\text{ ms}$$
- $$y_4 = 0{,}5(0) + 0{,}5(12{,}5) = 6{,}25\text{ ms}$$
- **Nhận xét:** Nghiệm đặc trưng của phần thuần nhất là $$r = 0{,}5 < 1$$, nên cú sốc giảm theo cấp số nhân $$y_n = 100 \cdot (0{,}5)^n$$ và bộ lọc **ổn định (stable)**. Nếu hệ số phản hồi là $$1{,}1 > 1$$, chỉ một nhiễu nhỏ cũng làm đầu ra bùng nổ ra vô cực!

**Phần B — So sánh độ phức tạp đệ quy thuần vs. DP cho bài toán leo $$n=5$$ bậc thang (mỗi bước đi 1 hoặc 2 bậc):**
- Truy hồi: $$w_n = w_{n-1} + w_{n-2}$$ với $$w_0 = 1, w_1 = 1$$.
- Điền bảng DP từ trái sang phải (chỉ cần 4 phép cộng, bộ nhớ $$O(1)$$):
  $$w_2 = 1 + 1 = 2, \quad w_3 = 2 + 1 = 3, \quad w_4 = 3 + 2 = 5, \quad w_5 = 5 + 3 = 8\text{ cách.}$$
- Trong khi đó, đệ quy thuần không lưu bảng phải gọi lại $$w_2$$ tới 3 lần và tổng số lời gọi bùng nổ theo $$O(\varphi^n)$$ với $$\varphi \approx 1{,}618$$.

### Khung giải thích: Ba góc nhìn thống nhất của tư duy truy hồi trong kỹ thuật (nên đọc chậm)

1. **Bước 1 — Dùng truy hồi để đo chi phí thuật toán:** Khi thấy hàm gọi lại chính nó trên nửa dữ liệu, viết ngay $$T(n) = aT(n/b) + f(n)$$ để biết liệu thuật toán thuộc $$O(n)$$, $$O(n\log n)$$ hay $$O(n^2)$$.
2. **Bước 2 — Dùng truy hồi để thiết kế thuật toán (DP):** Nếu bài toán tối ưu có cấu trúc con tối ưu, viết công thức truy hồi trước rồi biến nó thành vòng lặp điền bảng — tránh sa lầy vào chi tiết cài đặt quá sớm.
3. **Bước 3 — Dùng nghiệm đặc trưng để kiểm tra độ ổn định hệ thống:** Trong bộ lọc IIR, chuỗi tăng trưởng người dùng hay kiến trúc AI tuần tự, điều kiện $$\vert r_{\max} \vert < 1$$ đảm bảo nhiễu quá khứ tắt dần thay vì làm mất ổn định hệ thống.

$$\text{Truy hồi } y_n = F(y_{n-1}, x_n) \;\Longrightarrow\; \text{Master Theorem (Chia để trị)} \;+\; \text{DP (Bảng nhớ)} \;+\; \text{IIR/SSM (Ổn định } \vert r \vert < 1\text{)}.$$

## Bài tập thực hành

### Bài tập 1: Thiết lập công thức truy hồi

Hãy viết hệ thức truy hồi mô tả thời gian chạy của thuật toán Merge Sort trên mảng có kích thước $$n$$.

<details>
<summary>Đáp án</summary>

$$T(n) = 2T(n/2) + n$$ với điều kiện đầu $$T(1) = 1$$ (hoặc hằng số $$c$$).

</details>

### Bài tập 2: Giải truy hồi đơn giản

Tìm công thức đóng của $$T(n) = T(n-1) + 3$$ với $$T(1) = 2$$.

<details>
<summary>Đáp án</summary>

Đây là cấp số cộng có công sai $$3$$, nên $$T(n) = 2 + 3(n - 1) = 3n - 1$$.

</details>

### Bài tập 3: Ứng dụng quy hoạch động

Viết hệ thức truy hồi kèm điều kiện đầu cho bài toán đếm số cách leo hết cầu thang $$n$$ bậc, biết mỗi bước chỉ được đi 1 bậc hoặc 2 bậc.

<details>
<summary>Đáp án</summary>

$$a_n = a_{n-1} + a_{n-2}$$ với $$a_1 = 1$$ và $$a_2 = 2$$ (tuân theo quy luật dãy Fibonacci).

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Ôn tập về quan hệ tương đương)

## Tóm tắt

Quan hệ truy hồi là ngôn ngữ tự nhiên để mô tả các thuật toán chia để trị, quy hoạch động và nhiều hệ thống động trong thực tế. Việc biết cách thiết lập, giải và phân tích hệ thức truy hồi giúp chúng ta đánh giá chính xác hiệu năng thuật toán, thiết kế giải pháp tối ưu và kết nối chặt chẽ toán học rời rạc với kỹ thuật phần mềm.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=OynWkEj0S-s">2.4.1 Masters Theorem in Algorithms for Dividing Function #1</a> — Abdul Bari (tiếng Anh). Hướng dẫn chi tiết cách áp dụng Định lý Thợ cho truy hồi chia để trị.
- <a href="https://www.youtube.com/watch?v=eAaP4XaB8hM">RECURRENCE RELATIONS - DISCRETE MATHEMATICS</a> — TrevTutor (tiếng Anh). Củng cố dạng truy hồi tổng quát đứng sau các công thức đánh giá độ phức tạp.
