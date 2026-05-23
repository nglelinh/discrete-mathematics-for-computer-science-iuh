---
layout: post
title: "Dãy số và Tổng"
categories: chapter04
date: 2021-01-01
order: 4
required: false
lang: en
---

# Dãy số và Tổng

Rất nhiều đối tượng trong khoa học máy tính không đứng yên, chúng xuất hiện theo thứ tự: dãy phép đo theo thời gian, dãy giá trị do một thuật toán sinh ra, dãy trạng thái của một tiến trình, hay các mức chi phí khi đầu vào tăng dần. Khi đó, ta cần ngôn ngữ để mô tả từng phần tử và cả toàn bộ mẫu hình của chúng.


Tư duy tập hợp giúp ta mô tả dữ liệu, miền giá trị và ràng buộc một cách chính xác, nên phần này là nền cho cả lập trình lẫn mô hình hóa.
**Dãy số** giúp ta biểu diễn cấu trúc theo thứ tự, còn **tổng** giúp ta gom nhiều giá trị thành một đại lượng có thể phân tích. Từ số phép gán trong một vòng lặp, tổng độ dài các đoạn dữ liệu, đến công thức đếm trong tổ hợp, hai khái niệm này xuất hiện liên tục.

Điểm hay là nhiều biểu thức nhìn dài và rối thực ra có quy luật rất rõ nếu ta biết cách viết bằng ký hiệu sigma hoặc nhận ra kiểu dãy quen thuộc. Khi đó, một bài toán tưởng thuần tính toán lại trở thành bài toán nhận dạng cấu trúc.

Trong bài học này, chúng ta sẽ xây nền về dãy số, các loại tổng thường gặp, và cách dùng chúng để diễn đạt gọn những mô hình tăng trưởng quen thuộc trong toán và lập trình.

## 1. Dãy số

**Định nghĩa**: Một **dãy số** là một hàm có miền xác định là tập các số nguyên dương hoặc số tự nhiên và miền giá trị là một tập số, thường là $$\mathbb{R}$$.

$$a: \mathbb{N}\to\mathbb{R},\quad n\mapsto a_n.$$

**Ký hiệu**: $$\{a_n\}_{n\ge 1}$$ hoặc $$a_1,a_2,a_3,\ldots$$.

**Ví dụ**:

- Dãy số chẵn: $$a_n=2n$$ cho $$2,4,6,8,\ldots$$.
- Dãy bình phương: $$a_n=n^2$$ cho $$1,4,9,16,\ldots$$.
- Dãy Fibonacci: $$F_1=1,F_2=1,F_n=F_{n-1}+F_{n-2}$$.

## 2. Dãy số học và dãy hình học

### Dãy số học

**Định nghĩa**: Dãy số học (cấp số cộng) có hiệu giữa hai số hạng liên tiếp không đổi.

$$a_n=a_1+(n-1)d,$$

trong đó $$d$$ là công sai.

**Ví dụ**: Dãy $$3,7,11,15,\ldots$$ có $$a_1=3,d=4$$, nên $$a_{100}=3+99\cdot4=399$$.

### Dãy hình học

**Định nghĩa**: Dãy hình học (cấp số nhân) có tỉ số giữa hai số hạng liên tiếp không đổi.

$$a_n=a_1r^{n-1},$$

trong đó $$r$$ là công bội.

**Ví dụ**: Dãy $$2,6,18,54,\ldots$$ có $$a_1=2,r=3$$, nên $$a_{10}=2\cdot3^9$$.

## 3. Dãy được định nghĩa đệ quy

**Định nghĩa**: Một dãy được định nghĩa đệ quy khi số hạng sau phụ thuộc vào một hoặc nhiều số hạng trước.

**Ví dụ**:

$$F_0=0,\quad F_1=1,\quad F_n=F_{n-1}+F_{n-2}\quad(n\ge 2).$$

### Nhận xét CS

Định nghĩa đệ quy gần với hàm đệ quy trong lập trình. Tuy nhiên, tính trực tiếp theo định nghĩa Fibonacci có thể rất chậm nếu không dùng memoization.

```python
from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

## 4. Ký hiệu tổng Sigma

**Định nghĩa**:

$$\sum_{i=m}^{n} a_i = a_m+a_{m+1}+\cdots+a_n.$$

**Ký hiệu**:

- $$i$$: chỉ số chạy.
- $$m$$: cận dưới.
- $$n$$: cận trên.
- $$a_i$$: số hạng tổng quát.

**Ví dụ**:

$$\sum_{i=1}^{5} i = 1+2+3+4+5=15.$$

## 5. Tính chất của tổng

Với hằng số $$c$$:

$$\sum_{i=m}^{n} c a_i = c\sum_{i=m}^{n}a_i.$$

$$\sum_{i=m}^{n}(a_i+b_i)=\sum_{i=m}^{n}a_i+\sum_{i=m}^{n}b_i.$$

$$\sum_{i=m}^{n}c = c(n-m+1).$$

## 6. Các công thức tổng quan trọng

| Tổng | Công thức |
|---|---|
| Tổng hằng | $$\sum_{i=1}^{n}1=n$$ |
| Tổng số tự nhiên | $$\sum_{i=1}^{n}i=\frac{n(n+1)}{2}$$ |
| Tổng bình phương | $$\sum_{i=1}^{n}i^2=\frac{n(n+1)(2n+1)}{6}$$ |
| Tổng lập phương | $$\sum_{i=1}^{n}i^3=\left(\frac{n(n+1)}{2}\right)^2$$ |
| Tổng hình học | $$\sum_{i=0}^{n}r^i=\frac{r^{n+1}-1}{r-1},\ r\ne1$$ |

### Khối chứng minh: Tổng số tự nhiên

Gọi $$S=1+2+\cdots+n$$. Viết ngược lại:

$$S=n+(n-1)+\cdots+1.$$

Cộng hai dòng:

$$2S=(n+1)+(n+1)+\cdots+(n+1)=n(n+1).$$

Vậy:

$$S=\frac{n(n+1)}{2}.$$

## 7. Tổng và vòng lặp

Vòng lặp đơn:

```python
for i in range(1, n+1):
    do_constant_work()
```

Số phép toán xấp xỉ:

$$\sum_{i=1}^{n}1=n.$$

Vòng lặp lồng nhau tam giác:

```python
for i in range(1, n+1):
    for j in range(1, i+1):
        do_constant_work()
```

Số phép toán:

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2).$$

## 8. Công cụ tương tác

Nếu dùng công cụ này, hãy dự đoán kết quả trước rồi mới thao tác. Việc so sánh dự đoán với kết quả thật sẽ giúp khái niệm bám chắc hơn.

<div class="interactive-demo" data-demo="summation-loop-visualizer">
  <p><strong>Demo đề xuất:</strong> chọn kiểu vòng lặp, công cụ hiển thị tổng Sigma tương ứng và số ô được duyệt trong lưới.</p>
</div>

<script src="{{ '/public/js/summation-loop-visualizer.js' | relative_url }}"></script>

## 9. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Quên rằng tổng hằng $$c$$ từ 1 đến $$n$$ là $$cn$$, không phải $$c$$.

**Nhầm lẫn 2**: Dùng công thức hình học cho $$r=1$$. Khi $$r=1$$, tổng là $$n+1$$ nếu chạy từ 0 đến $$n$$.

**Nhầm lẫn 3**: Nhầm chỉ số bắt đầu từ 0 và từ 1. Luôn kiểm tra số lượng số hạng.
</div>

## 10. Ứng dụng trong Khoa học Máy tính

- **Phân tích thuật toán**: số phép toán thường là tổng theo kích thước đầu vào.
- **Đệ quy**: dãy mô tả kích thước bài toán qua từng lời gọi.
- **Xử lý tín hiệu và AI**: vector, chuỗi thời gian, gradient descent đều dùng dãy và tổng.
- **Cơ sở dữ liệu**: aggregation như `SUM`, `AVG` là biểu hiện trực tiếp của ký hiệu tổng.

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

Dãy số mô tả giá trị theo chỉ số; tổng Sigma viết gọn phép cộng nhiều số hạng. Các công thức tổng cơ bản giúp chuyển vòng lặp thành biểu thức đóng và đánh giá độ phức tạp. Dãy đệ quy như Fibonacci kết nối trực tiếp với lập trình đệ quy và tối ưu bằng ghi nhớ.
