---
layout: post
title: "Hệ thức Truy hồi trong Thuật toán và Hệ thống"
categories: chapter10
date: 2021-01-01
order: 4
required: false
lang: en
---

Một trong những điều đẹp nhất của toán rời rạc là khả năng mô tả cấu trúc lớn bằng quy tắc nhỏ lặp lại.
Hệ thức truy hồi làm đúng điều đó.

Thay vì mô tả trực tiếp mọi giá trị,
ta nói giá trị hiện tại phụ thuộc vào các giá trị trước như thế nào.

Từ bài toán thỏ Fibonacci năm 1202,
đến divide-and-conquer algorithms,
dynamic programming,
population models,
và signal processing,
truy hồi xuất hiện như ngôn ngữ tự nhiên của những hệ thống có ký ức.

---

## Phần 1: Lịch sử — Fibonacci và bài toán thỏ

### 1.1. Một bài toán tưởng vui nhưng sống rất lâu

Trong *Liber Abaci* năm 1202,
Leonardo of Pisa — thường gọi là Fibonacci — nêu bài toán sinh sản của thỏ.
Từ đó xuất hiện dãy số nổi tiếng:

$$
F_n = F_{n-1} + F_{n-2}
$$

Điểm hấp dẫn ở đây không chỉ là dãy số.
Điểm hấp dẫn là ý tưởng mô tả tương lai bằng quá khứ gần.

### 1.2. Tư duy truy hồi là tư duy cấu trúc

Nhiều hiện tượng trong tự nhiên,
kinh tế,
và computing
không thuận tiện nếu mô tả từng bước độc lập.
Chúng thích hợp hơn với quy luật:

“Giá trị tiếp theo phụ thuộc vào vài giá trị trước đó.”

Chính vì thế,
hệ thức truy hồi trở thành cầu nối giữa pattern và prediction.

![Xoắn ốc Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Fibonacci_spiral.svg)

*Hình 10.15: Bài toán thỏ của Fibonacci mở ra một cách mô tả tăng trưởng và cấu trúc lặp rất bền trong toán học và computing.*

---

## Phần 2: Phân tích thuật toán chia để trị

### 2.1. Vì sao divide-and-conquer sinh ra truy hồi

Khi thuật toán chia bài toán kích thước `n`
thành các bài toán con,
rồi ghép kết quả,
chi phí thường thỏa một recurrence.

Ví dụ merge sort:

$$
T(n) = 2T(n/2) + n
$$

Đây không phải ký hiệu trang trí.
Nó là bản tóm tắt bản chất thời gian chạy.

### 2.2. Master Theorem như công cụ công nghiệp nhỏ gọn

Master Theorem giúp giải nhanh nhiều recurrence kiểu:

$$
T(n)=aT(n/b)+f(n)
$$

Từ đó,
kỹ sư có thể phân biệt:

- thuật toán nào scale ổn,
- thuật toán nào tăng quá nhanh,
- optimization nào thật sự đáng giá.

### 2.3. Từ sách giáo khoa đến production

Search systems,
parallel sort,
tree processing,
geometric partitioning,
FFT-style methods
đều có tinh thần divide-and-conquer.

Phân tích recurrence vì thế không chỉ giúp qua môn.
Nó giúp hiểu chi phí kiến trúc của nhiều hệ thống thật.

![Master Theorem — phân tích chia để trị](/discrete-mathematics-for-computer-science-iuh/img/course/Master_theorem.png)

*Hình 10.16: Master Theorem giải nhanh $T(n)=aT(n/b)+f(n)$ — công cụ nền cho phân tích merge sort, FFT và nhiều thuật toán chia để trị.*

![Merge Sort — sơ đồ thuật toán](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

*Hình 10.17: Divide-and-conquer sinh truy hồi tự nhiên — chi phí chia, đệ quy con, và ghép kết quả.*

---

## Phần 3: Dynamic programming — truy hồi cộng với trí nhớ

### 3.1. Fibonacci ngây thơ và bài học về chồng lặp

Nếu cài Fibonacci đệ quy trực tiếp:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

ta lặp lại rất nhiều lời gọi con giống nhau.

### 3.2. Memoization biến truy hồi thành hiệu quả

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

Đây là khoảnh khắc dynamic programming tỏa sáng:
giữ lại kết quả cũ để tránh tính lại.

### 3.3. DP trong thế giới thật

Dynamic programming sống trong:

- shortest paths,
- sequence alignment,
- edit distance,
- resource allocation,
- parsing,
- optimization over states.

Nhiều bài toán công nghiệp nhìn ngoài rất khác nhau,
nhưng khi bóc lớp vỏ,
chúng đều nói:
“bài toán lớn có thể xây từ bài toán con nào,
và ta có đang lặp lại không?”

![Dynamic programming — memoization](/discrete-mathematics-for-computer-science-iuh/img/course/Dsa_dynamic_programming_salmon_fish_memoized_step_n.png)

*Hình 10.18: Dynamic programming khai thác truy hồi nhưng thêm trí nhớ, biến ý tưởng đẹp thành công cụ hiệu quả.*

![Cây gọi đệ quy Fibonacci — trước memoization](/discrete-mathematics-for-computer-science-iuh/img/course/Algorithms-F6CallTreeMemoized.png)

*Hình 10.19: Memoization loại bỏ tính lại — cùng truy hồi nhưng từ exponential xuống linear thời gian.*

---

## Phần 4: Population growth và mô hình hóa quá trình

### 4.1. Truy hồi tự nhiên trong mô hình dân số

Nếu dân số năm sau phụ thuộc dân số năm nay và tỷ lệ sinh-tử,
ta có recurrence.

Ví dụ đơn giản:

$$
P_{n+1} = 1.02P_n
$$

Hoặc mô hình phong phú hơn:

$$
P_{n+1}=P_n + births_n - deaths_n + migration_n
$$

### 4.2. Từ sinh học đến user growth

Trong digital products,
tư duy tương tự xuất hiện khi mô hình hóa:

- active users,
- retention,
- churn,
- referrals,
- viral growth.

Nghĩa là bài học về population không chỉ dành cho sinh thái học.
Nó còn gợi trực giác về product dynamics.

![Tháp Hà Nội — truy hồi exponential](/discrete-mathematics-for-computer-science-iuh/img/course/Tower_of_Hanoi.gif)

*Hình 10.20: Tháp Hà Nội có $H_n = 2H_{n-1}+1$ — mô hình tăng trưởng exponential từ truy hồi đơn giản.*

---

## Phần 5: Signal processing và IIR filters

### 5.1. Bộ lọc có ký ức

Trong signal processing,
nhiều bộ lọc tạo output hiện tại dựa trên:

- input hiện tại,
- input quá khứ,
- output quá khứ.

Ví dụ dạng đơn giản:

$$
y_n = ax_n + by_{n-1}
$$

Đây là recurrence rất thật.

### 5.2. Vì sao nó quan trọng với CS

Không phải mọi sinh viên CS đều học DSP sâu,
nhưng tư duy ở đây rất bổ ích:

- hệ thống có state,
- trạng thái hiện tại phụ thuộc lịch sử,
- stability phụ thuộc hệ số,
- behavior dài hạn cần phân tích từ recurrence.

Ý tưởng này nối tốt sang control systems,
stream processing,
feedback loops,
và một số mô hình thời gian trong ML.

---

## Phần 6: Tương lai — recurrence thinking trong AI và systems

Ngay cả khi công cụ ngày càng hiện đại,
tư duy truy hồi vẫn còn:

- recurrent architectures,
- state-space models,
- streaming analytics,
- caching dynamics,
- recursive data structures,
- time-series forecasting.

Hệ thức truy hồi là ngôn ngữ để nói về “hôm nay mang dấu vết của hôm qua”.
Và rất nhiều hệ thống tính toán có đúng tính chất đó.

---

## Kết luận

Từ bài toán thỏ của Fibonacci,
đến Master Theorem,
dynamic programming,
population models,
và IIR filters,
hệ thức truy hồi cho ta một cách nghĩ sâu về cấu trúc lặp và phụ thuộc theo thời gian.

Trong computing,
đó là một năng lực cực quý:
thấy được quy luật phía sau quá trình,
thay vì chỉ nhìn từng bước riêng lẻ.

---

## Bài tập thực hành

### Bài tập 1: Viết công thức đệ quy

Viết công thức đệ quy cho số lần gọi hàm trong thuật toán Merge Sort với kích thước n.

<details>
<summary>Đáp án</summary>

$$T(n) = 2T(n/2) + n$$ (với $$T(1) = 1$$).

</details>

### Bài tập 2: Giải recurrence đơn giản

Giải $$T(n) = T(n-1) + 3$$, $$T(1) = 2$$.

<details>
<summary>Đáp án</summary>

$$T(n) = 3n - 1$$.

</details>

### Bài tập 3: Ứng dụng DP

Viết recurrence cho bài toán tính số cách leo cầu thang n bậc (mỗi bước 1 hoặc 2 bậc).

<details>
<summary>Đáp án</summary>

$$a_n = a_{n-1} + a_{n-2}$$, $$a_1=1$$, $$a_2=2$$ (dãy Fibonacci).

</details>

## Tóm tắt

Quan hệ đệ quy là ngôn ngữ tự nhiên để mô tả thuật toán chia để trị, quy hoạch động và nhiều hệ thống thực tế. Hiểu cách viết, giải và phân tích recurrence giúp chúng ta đánh giá hiệu năng thuật toán, thiết kế giải pháp tối ưu và mô hình hóa các quá trình động. Đây là cầu nối giữa toán học rời rạc và kỹ thuật phần mềm hiệu quả.
