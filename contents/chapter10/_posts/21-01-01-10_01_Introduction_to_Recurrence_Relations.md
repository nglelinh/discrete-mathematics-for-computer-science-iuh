---
layout: post
title: "Giới thiệu Quan hệ Truy hồi"
categories: chapter10
date: 2021-01-01
order: 1
required: true
lang: vi
---

Nhiều bài toán không mô tả trực tiếp kết quả ở bước $$n$$, mà mô tả nó thông qua các bước trước đó. Dãy Fibonacci là ví dụ kinh điển, nhưng ý tưởng này còn xuất hiện trong đệ quy, phân tích thuật toán, mô hình dân số, lan truyền thông tin và dynamic programming.


Quan hệ truy hồi cho phép ta mô tả tiến trình theo từng bước, đúng với cách nhiều thuật toán đệ quy và dynamic programming vận hành.
**Quan hệ truy hồi** là cách viết chính xác cho kiểu phụ thuộc đó. Thay vì cho công thức đóng ngay từ đầu, ta mô tả quy tắc sinh ra phần tử tiếp theo từ một hoặc nhiều phần tử trước. Cách biểu diễn này rất tự nhiên với những quá trình tiến triển theo thời gian hay theo kích thước bài toán.

Điều quan trọng là truy hồi không chỉ là một công thức đẹp. Nó phản ánh cách hệ thống thực sự vận động, và giúp ta chuyển từ mô tả cục bộ sang hiểu biết toàn cục về cả dãy.

Trong bài học này, chúng ta sẽ làm quen với khái niệm quan hệ truy hồi, cách đọc các thành phần của nó và vì sao nó lại quan trọng trong toán rời rạc lẫn khoa học máy tính.

## Định nghĩa và Khái niệm

### Quan hệ Truy hồi

**Định nghĩa**: Quan hệ truy hồi là một phương trình biểu diễn số hạng thứ $$n$$ của một dãy số theo một hoặc nhiều số hạng đứng trước nó.

**Dạng tổng quát**:

$$a_n = f(a_{n-1}, a_{n-2}, \dots, a_{n-k}, n)$$

Trong đó:

- $$a_n$$ là số hạng thứ $$n$$ của dãy
- $$f$$ là một hàm số xác định mối liên hệ
- $$k$$ là **bậc** (order) của quan hệ truy hồi — cho biết cần bao nhiêu số hạng đằng trước để tính $$a_n$$
- Cần có $$k$$ **điều kiện đầu** (initial conditions): $$a_0, a_1, \dots, a_{k-1}$$

<div class="content-box insight-box" markdown="1">
**Tại sao cần điều kiện đầu?** Hãy tưởng tượng quan hệ truy hồi như một cỗ máy sản xuất: nó biết cách tạo ra số hạng tiếp theo từ những số hạng trước, nhưng không thể tự sinh ra số hạng đầu tiên. Điều kiện đầu chính là "nguyên liệu khởi tạo" cho cỗ máy đó.
</div>

### Ví dụ Cơ bản

#### 1. Dãy Fibonacci và bài toán đôi thỏ

**Bài toán gốc** (Fibonacci, 1202): Một đôi thỏ (gồm một thỏ đực và một thỏ cái) cứ mỗi tháng đẻ được một đôi thỏ con (cũng gồm một đực và một cái). Mỗi đôi thỏ con, khi tròn hai tháng tuổi, lại mỗi tháng đẻ ra một đôi thỏ con và quá trình sinh nở cứ thế tiếp diễn. Hỏi có bao nhiêu đôi thỏ sau $$n$$ tháng?

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter10/fibonacci_rabbits.svg" alt="Minh họa bài toán đôi thỏ Fibonacci" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 10.2: Bài toán đôi thỏ của Fibonacci — nguồn gốc kinh điển của dãy số Fibonacci.</figcaption>
</p>
</figure>

**Phân tích**: Gọi $$F_n$$ là số đôi thỏ sau $$n$$ tháng.

- Tháng 1: 1 đôi (thỏ ban đầu) $$\to F_1 = 1$$
- Tháng 2: 1 đôi (thỏ ban đầu chưa đẻ) $$\to F_2 = 1$$
- Tháng 3: 2 đôi (thỏ ban đầu + 1 đôi con) $$\to F_3 = 2$$
- Tháng $$n$$: số thỏ tháng $$n-1$$ cộng với số thỏ con mới sinh (bằng số thỏ tháng $$n-2$$ vì mỗi đôi thỏ cần 2 tháng tuổi để sinh).

**Quan hệ truy hồi Fibonacci**:

$$F_n = F_{n-1} + F_{n-2}, \quad F_1 = 1, F_2 = 1$$

**Dãy**: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

<div class="content-box fun-fact-box" markdown="1">
**Giai thoại**: Leonardo Fibonacci — nhà toán học người Ý thời Trung Cổ — không hề biết rằng dãy số mang tên ông sau này lại xuất hiện trong đến thế: tỷ lệ vàng trong kiến trúc, đường xoắn ốc trong vỏ ốc, sự sắp xếp lá cây, và thậm chí là thuật toán tìm kiếm trong khoa học máy tính hiện đại.
</div>

#### 2. Giai thừa

**Quan hệ**: $$n! = n \times (n-1)!$$

**Điều kiện ban đầu**: $$0! = 1$$

**Dãy**: 1, 1, 2, 6, 24, 120, 720, ...

#### 3. Tháp Hà Nội

Trò chơi Tháp Hà Nội (Tower of Hanoi) gồm ba cọc và $$n$$ đĩa kích thước khác nhau. Mỗi lần chỉ được di chuyển một đĩa, và không được đặt đĩa lớn lên trên đĩa nhỏ.

**Quan hệ**: $$H_n = 2H_{n-1} + 1$$

**Điều kiện ban đầu**: $$H_1 = 1$$

**Dãy**: 1, 3, 7, 15, 31, 63, ...

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter10/tower_of_hanoi.svg" alt="Bài toán Tháp Hà Nội với 3 đĩa" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 10.3: Tháp Hà Nội — một bài toán đệ quy cổ điển được mô hình hóa bằng quan hệ truy hồi $$H_n = 2H_{n-1} + 1$$.</figcaption>
</p>
</figure>

<div class="interactive-tool" markdown="1">
<div data-demo="recurrence-visualizer"></div>
</div>
<script src="{{ '/public/js/recurrence-visualizer.js' | relative_url }}"></script>

## Phân loại Quan hệ Truy hồi

### 1. Theo Tính tuyến tính (Linear vs Nonlinear)

Một quan hệ truy hồi được gọi là **tuyến tính** nếu nó có dạng tổng của các số hạng trước nhân với hệ số, không có tích hoặc lũy thừa giữa các số hạng.

| Loại | Dạng | Ví dụ |
|:-----|:-----|:------|
| **Tuyến tính** | $$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k} + f(n)$$ | $$a_n = 3a_{n-1} - 2a_{n-2}$$ |
| **Phi tuyến** | Có tích, lũy thừa giữa các $$a_{n-i}$$ | $$a_n = a_{n-1} \times a_{n-2}$$ hoặc $$a_n = a_{n-1}^2 + 1$$ |

**Ví dụ phân biệt**:

- $$a_n = 2a_{n-1} + a_{n-2}$$ là **tuyến tính** (hệ số hằng, không có tích)
- $$a_n = a_{n-1} \cdot a_{n-2}$$ là **phi tuyến** (có tích giữa các số hạng)
- {% raw %}$$a_n = \sqrt{a_{n-1}}$${% endraw %} là **phi tuyến** (có căn thức)

### 2. Theo Tính thuần nhất (Homogeneous vs Nonhomogeneous)

| Loại | Dạng | Ví dụ |
|:-----|:-----|:------|
| **Thuần nhất** | $$a_n = c_1 a_{n-1} + \dots + c_k a_{n-k}$$ | $$a_n = 3a_{n-1} - 2a_{n-2}$$ |
| **Không thuần nhất** | Có thêm $$f(n) \neq 0$$ | $$a_n = 2a_{n-1} + n$$ |

**Ví dụ**:

- $$F_n = F_{n-1} + F_{n-2}$$ là **tuyến tính thuần nhất** bậc 2
- $$H_n = 2H_{n-1} + 1$$ là **tuyến tính không thuần nhất** bậc 1
- $$a_n = a_{n-1} \cdot a_{n-2}$$ là **phi tuyến**

<div class="content-box warning-box" markdown="1">
**Sai lầm thường gặp**: Nhiều sinh viên nhầm lẫn giữa "bậc" và "tính tuyến tính". Bậc là số số hạng đằng trước được dùng để tính số hạng hiện tại. Tuyến tính là không có tích hay lũy thừa giữa các số hạng. Một quan hệ có thể bậc cao nhưng vẫn tuyến tính, và ngược lại — bậc thấp nhưng phi tuyến.
</div>

## Mô hình hóa bài toán bằng Quan hệ Truy hồi

Quan hệ truy hồi không chỉ là công cụ toán học trừu tượng — chúng xuất hiện tự nhiên khi mô hình hóa các bài toán thực tế có tính chất đệ quy. Quá trình mô hình hóa gồm ba bước:

1. **Xác định dãy số**: Xác định đại lượng cần tính ($$a_n$$) và ý nghĩa của chỉ số $$n$$ trong bài toán.
2. **Thiết lập quan hệ**: Tìm mối liên hệ giữa $$a_n$$ và các số hạng trước đó dựa trên cấu trúc bài toán.
3. **Xác định điều kiện đầu**: Tìm giá trị của một vài số hạng đầu tiên từ dữ kiện bài toán.

<div class="content-box example-box" markdown="1">
**Ví dụ 1: Lãi kép (Compound Interest)**

Gửi tiết kiệm 10 triệu đồng với lãi suất 0.5% mỗi tháng, lãi nhập gốc hàng tháng. Gọi $$a_n$$ là số tiền sau $$n$$ tháng.

Sau mỗi tháng, số tiền tăng thêm 0.5% so với tháng trước:

$$a_n = a_{n-1} + 0.005 \cdot a_{n-1} = 1.005 \cdot a_{n-1}$$

Điều kiện đầu: $$a_0 = 10\,000\,000$$ (tiền gốc)

Đây là quan hệ truy hồi tuyến tính thuần nhất bậc 1. Nghiệm:

$$a_n = 10\,000\,000 \cdot (1.005)^n$$
</div>

<div class="content-box example-box" markdown="1">
**Ví dụ 2: Số xâu nhị phân không chứa hai số 0 liên tiếp**

Đếm số xâu nhị phân độ dài $$n$$ không có hai bit 0 đứng cạnh nhau. Gọi $$a_n$$ là số xâu thỏa mãn.

Xét bit cuối cùng của xâu:

- Nếu bit cuối là 1: $$n-1$$ bit đầu có thể là bất kỳ xâu hợp lệ độ dài $$n-1$$ — $$a_{n-1}$$ cách
- Nếu bit cuối là 0: bit kề cuối phải là 1, và $$n-2$$ bit đầu là xâu hợp lệ độ dài $$n-2$$ — $$a_{n-2}$$ cách

Vậy:

$$a_n = a_{n-1} + a_{n-2}$$

Điều kiện đầu: $$a_1 = 2$$ (xâu "0" và "1"), $$a_2 = 3$$ (xâu "01", "10", "11")
</div>

<div class="content-box example-box" markdown="1">
**Ví dụ 3: Số cách lên cầu thang**

Có $$n$$ bậc thang, mỗi bước có thể đi 1 hoặc 2 bậc. Gọi $$a_n$$ là số cách lên đến bậc thứ $$n$$.

Để đến bậc $$n$$, ta phải đến từ bậc $$n-1$$ (đi 1 bước) hoặc bậc $$n-2$$ (đi 2 bước):

$$a_n = a_{n-1} + a_{n-2}$$

Điều kiện đầu: $$a_1 = 1$$ (chỉ 1 cách: đi 1 bước), $$a_2 = 2$$ (1+1 hoặc 2)

Dãy số thu được: 1, 2, 3, 5, 8, 13, ... — đây là dãy Fibonacci nhưng với điều kiện đầu khác.
</div>

## Quan hệ Truy hồi Bậc nhất

### Định nghĩa

Quan hệ truy hồi bậc nhất có dạng tổng quát:

$$a_n = f(a_{n-1}, n)$$

nghĩa là $$a_n$$ chỉ phụ thuộc vào số hạng ngay trước nó ($$a_{n-1}$$) và có thể cả chỉ số $$n$$.

### Truy hồi tuyến tính bậc nhất thuần nhất

Dạng chuẩn:

$$a_n = c \cdot a_{n-1} \quad \text{với} \quad a_0 = A$$

Nghiệm tổng quát:

$$a_n = A \cdot c^n$$

**Chứng minh**: Bằng quy nạp đơn giản:

- $$n = 0$$: $$a_0 = A = A \cdot c^0$$ (đúng)
- $$n = 1$$: $$a_1 = c \cdot a_0 = cA = A \cdot c^1$$
- Giả sử $$a_{n-1} = A \cdot c^{n-1}$$, thì $$a_n = c \cdot a_{n-1} = c \cdot A \cdot c^{n-1} = A \cdot c^n$$

<div class="content-box example-box" markdown="1">
**Ví dụ**: Dân số một thành phố hiện là 1,2 triệu người và tăng 1,5% mỗi năm. Gọi $$a_n$$ là dân số sau $$n$$ năm.

$$a_n = 1.015 \cdot a_{n-1}, \quad a_0 = 1.2 \times 10^6$$

Nghiệm: $$a_n = 1.2 \times 10^6 \cdot (1.015)^n$$

Sau 10 năm: $$a_{10} = 1.2 \times 10^6 \cdot (1.015)^{10} \approx 1.393 \times 10^6$$ người.
</div>

### Truy hồi tuyến tính bậc nhất không thuần nhất

Dạng chuẩn:

$$a_n = c \cdot a_{n-1} + f(n) \quad \text{với} \quad a_0 = A$$

Phương pháp giải gồm hai bước:

1. Tìm nghiệm thuần nhất: $$a_n^{(h)} = A_0 \cdot c^n$$
2. Tìm một nghiệm riêng $$a_n^{(p)}$$ phụ thuộc vào dạng của $$f(n)$$
3. Nghiệm tổng quát: $$a_n = a_n^{(h)} + a_n^{(p)}$$

#### Trường hợp $$f(n) = d$$ (hằng số)

Nghiệm riêng có dạng hằng số $$a_n^{(p)} = K$$. Thay vào quan hệ:

$$K = c \cdot K + d \quad\Rightarrow\quad K(1-c) = d \quad\Rightarrow\quad K = \frac{d}{1-c}$$

(Chú ý: trường hợp $$c = 1$$ cần xử lý riêng với nghiệm dạng $$K \cdot n$$)

<div class="content-box example-box" markdown="1">
**Ví dụ**: Giải $$a_n = 3a_{n-1} + 4$$ với $$a_0 = 1$$

Nghiệm thuần nhất: $$a_n^{(h)} = A \cdot 3^n$$

Nghiệm riêng: $$K = \frac{4}{1-3} = -2$$

Nghiệm tổng quát: $$a_n = A \cdot 3^n - 2$$

Từ $$a_0 = 1$$: $$1 = A - 2 \Rightarrow A = 3$$

Vậy: $$a_n = 3 \cdot 3^n - 2 = 3^{n+1} - 2$$

Kiểm tra: $$a_1 = 3^2 - 2 = 7$$, truy hồi: $$3 \cdot 1 + 4 = 7$$ ✓
</div>

#### Trường hợp $$f(n)$$ là đa thức bậc $$m$$

Nghiệm riêng có dạng đa thức cùng bậc:

$$a_n^{(p)} = b_0 + b_1 n + b_2 n^2 + \cdots + b_m n^m$$

<div class="content-box example-box" markdown="1">
**Ví dụ**: Giải $$a_n = 2a_{n-1} + 3n + 1$$ với $$a_0 = 2$$

Nghiệm thuần nhất: $$a_n^{(h)} = A \cdot 2^n$$

Nghiệm riêng dạng: $$a_n^{(p)} = B_0 + B_1 n$$

Thay vào: $$B_0 + B_1 n = 2(B_0 + B_1(n-1)) + 3n + 1$$

$$B_0 + B_1 n = 2B_0 + 2B_1 n - 2B_1 + 3n + 1$$

Cân bằng hệ số:

- Hệ số của $$n$$: $$B_1 = 2B_1 + 3 \Rightarrow -B_1 = 3 \Rightarrow B_1 = -3$$
- Hằng số: $$B_0 = 2B_0 - 2B_1 + 1 = 2B_0 + 6 + 1 \Rightarrow -B_0 = 7 \Rightarrow B_0 = -7$$

Nghiệm tổng quát: $$a_n = A \cdot 2^n - 3n - 7$$

Từ $$a_0 = 2$$: $$2 = A - 7 \Rightarrow A = 9$$

Vậy: $$a_n = 9 \cdot 2^n - 3n - 7$$

Kiểm tra: $$a_1 = 18 - 3 - 7 = 8$$, truy hồi: $$2 \cdot 2 + 3 + 1 = 8$$ ✓
</div>

<div class="content-box warning-box" markdown="1">
**Sai lầm thường gặp**: Khi tìm nghiệm riêng, sinh viên thường quên kiểm tra xem dạng nghiệm thử có trùng với nghiệm thuần nhất không. Nếu trùng, cần nhân thêm $$n$$ (hoặc $$n^s$$) vào nghiệm thử. Chúng ta sẽ học chi tiết về điều này trong Bài 10.3.
</div>

## Ứng dụng trong Khoa học Máy tính

### Phân tích độ phức tạp thuật toán

Các thuật toán đệ quy thường có độ phức tạp thời gian được biểu diễn bằng quan hệ truy hồi. Ví dụ:

- **Merge Sort**: $$T(n) = 2T(n/2) + n$$
- **Binary Search**: $$T(n) = T(n/2) + 1$$
- **Thuật toán Fibonacci đệ quy**: $$T(n) = T(n-1) + T(n-2) + 1$$

### Quy hoạch động (Dynamic Programming)

Quy hoạch động là kỹ thuật giải bài toán bằng cách kết hợp lời giải của các bài toán con — bản chất chính là xây dựng và giải các quan hệ truy hồi. Bài toán ba lô (Knapsack), chuỗi con chung dài nhất (LCS), và đường đi ngắn nhất (Bellman-Ford) đều dùng quan hệ truy hồi.

### Mô hình hóa hệ thống

Từ dân số, lãi suất ngân hàng, đến lan truyền virus trong mạng máy tính — tất cả đều có thể mô hình hóa bằng quan hệ truy hồi, giúp ta dự đoán được tương lai dựa trên quá khứ.

## Bài tập thực hành

### Bài tập 1: Xác định loại quan hệ truy hồi

Phân loại các quan hệ truy hồi sau (tuyến tính/phi tuyến, thuần nhất/không thuần nhất, bậc mấy):

a) $$a_n = 3a_{n-1} - 2a_{n-2}$$
b) $$a_n = a_{n-1}^2 + 1$$
c) $$a_n = 2a_{n-1} + n^2$$
d) $$a_n = a_{n-1} \cdot a_{n-2} + a_{n-3}$$

<details>
<summary>Đáp án</summary>

a) Tuyến tính thuần nhất, bậc 2.
b) Phi tuyến (có bình phương số hạng), bậc 1.
c) Tuyến tính không thuần nhất (có $$f(n) = n^2$$), bậc 1.
d) Phi tuyến (có tích $$a_{n-1} \cdot a_{n-2}$$), bậc 3.

</details>

### Bài tập 2: Thiết lập quan hệ truy hồi

Một người gửi 50 triệu đồng vào ngân hàng với lãi suất 0.7% mỗi tháng. Mỗi tháng, người đó rút ra 3 triệu đồng để tiêu. Thiết lập quan hệ truy hồi cho số dư sau $$n$$ tháng.

<details>
<summary>Đáp án</summary>

Gọi $$a_n$$ là số dư sau $$n$$ tháng. Sau mỗi tháng, số tiền tăng 0.7% (nhân 1.007) rồi trừ đi 3 triệu:

$$a_n = 1.007 \cdot a_{n-1} - 3, \quad a_0 = 50$$

Kiểm tra: $$a_1 = 1.007 \cdot 50 - 3 = 47.35$$ (triệu đồng) ✓
</details>

### Bài tập 3: Giải truy hồi bậc nhất

Giải các quan hệ truy hồi sau:

a) $$a_n = 2a_{n-1}$$ với $$a_0 = 5$$
b) $$a_n = a_{n-1} + 3$$ với $$a_0 = 4$$
c) $$a_n = -3a_{n-1}$$ với $$a_0 = 2$$

<details>
<summary>Đáp án</summary>

a) Nghiệm: $$a_n = 5 \cdot 2^n$$ (cấp số nhân). Dãy: 5, 10, 20, 40, 80, ...

b) Nghiệm: $$a_n = 4 + 3n$$ (cấp số cộng). Dãy: 4, 7, 10, 13, 16, ...

c) Nghiệm: $$a_n = 2 \cdot (-3)^n$$. Dãy: 2, -6, 18, -54, 162, ...
</details>

### Bài tập 4: Ứng dụng thực tế

Một công ty khởi nghiệp có 1000 người dùng vào tháng đầu tiên. Mỗi tháng, số người dùng tăng gấp đôi so với tháng trước. Hỏi sau 12 tháng có bao nhiêu người dùng?

<details>
<summary>Đáp án</summary>

Gọi $$u_n$$ là số người dùng sau $$n$$ tháng.

$$u_n = 2u_{n-1}, \quad u_1 = 1000$$

Nghiệm: $$u_n = 1000 \cdot 2^{n-1}$$

Sau 12 tháng: $$u_{12} = 1000 \cdot 2^{11} = 1000 \cdot 2048 = 2.048.000$$ người dùng.
</details>

## Tóm tắt

- **Quan hệ truy hồi**: phương trình biểu diễn $$a_n$$ theo các số hạng trước đó
- **Bậc** của quan hệ truy hồi: số số hạng đằng trước cần để tính $$a_n$$
- **Phân loại**: tuyến tính/phi tuyến, thuần nhất/không thuần nhất
- **Điều kiện đầu**: cần thiết để xác định duy nhất một dãy số
- **Mô hình hóa**: quy trình 3 bước (xác định dãy, thiết lập quan hệ, điều kiện đầu)
- **Truy hồi bậc nhất thuần nhất**: $$a_n = A \cdot c^n$$
- **Truy hồi bậc nhất không thuần nhất**: nghiệm = nghiệm thuần nhất + nghiệm riêng

Trong bài tiếp theo, chúng ta sẽ học phương pháp giải quan hệ truy hồi tuyến tính thuần nhất bậc cao bằng phương trình đặc trưng — một kỹ thuật mạnh mẽ để tìm công thức tường minh cho dãy Fibonacci và nhiều dãy số quan trọng khác.
