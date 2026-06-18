---
layout: post
title: "Giới thiệu Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 1
required: true
lang: vi
---

Có những lúc ta muốn nén cả một dãy vô hạn vào trong một biểu thức duy nhất để dễ thao tác hơn. Nghe lạ, nhưng đó chính là điều **hàm sinh** làm được, và cũng là lý do nó trở thành một công cụ rất đẹp trong combinatorics.

Hàm sinh mạnh ở chỗ nó đổi một dãy số thành đối tượng đại số dễ thao tác hơn, khá giống cách ta chọn biểu diễn phù hợp để làm bài toán đơn giản đi.
Thay vì nhìn dãy như danh sách rời rạc từng số hạng, ta gói chúng vào một chuỗi hình thức. Khi đó, các phép cộng, nhân, đạo hàm hay biến đổi đại số trên hàm sinh sẽ phản ánh trực tiếp cấu trúc của bài toán đếm hoặc truy hồi phía sau.

Từ góc nhìn khoa học máy tính, đây là một cách đổi biểu diễn để làm bài toán dễ hơn, khá giống việc chọn cấu trúc dữ liệu hay mô hình trung gian phù hợp trước khi xử lý. Đổi góc nhìn đúng thường giúp lời giải gọn hơn rất nhiều.

Trong bài này, chúng ta sẽ làm quen với hàm sinh, ý nghĩa của các hệ số trong chuỗi, và vì sao công cụ này lại mạnh đến vậy trong toán rời rạc.

![Chuỗi lũy thừa hình thức](https://commons.wikimedia.org/wiki/Special:FilePath/Laurent_series.svg?width=640)

*Hình 11.1: Chuỗi lũy thừa $G(x)=\sum a_n x^n$ — mỗi hệ số $a_n$ mã hóa một số hạng của dãy.*

![Hàm sinh (generating function)](https://commons.wikimedia.org/wiki/Special:FilePath/R._V._Lapshin,_Generating_functions_and_squares.png?width=640)

*Hình 11.2: Hàm sinh gói cả dãy số vào một biểu thức duy nhất để thao tác bằng đại số.*

![Leonhard Euler](https://commons.wikimedia.org/wiki/Special:FilePath/Leonhard_Euler.jpg?width=640)

*Hình 11.3: Leonhard Euler (1707–1783) — nhà toán học tiên phong trong lý thuyết hàm sinh và chuỗi lũy thừa.*

![Dãy số học](https://commons.wikimedia.org/wiki/Special:FilePath/Arithmetic_progression.svg?width=640)

*Hình 11.4: Dãy số học là ví dụ đầu tiên: hệ số tăng tuyến tính tương ứng với cấu trúc đếm đơn giản.*

![Ký hiệu tổng Σ](https://commons.wikimedia.org/wiki/Special:FilePath/Sigma_summation_notation.svg?width=640)

*Hình 11.5: Ký hiệu Σ liên kết hàm sinh với các tổng hữu hạn và vô hạn trong tổ hợp.*

## 1. Định nghĩa

Phần này đặt lại ngôn ngữ chung của bài học. Nắm chắc định nghĩa trước sẽ giúp các ví dụ và định lý phía sau trở nên dễ theo dõi hơn.

Cho dãy số $a_0,a_1,a_2,\ldots$. **Hàm sinh thông thường** của dãy là

$$
G(x)=\sum_{n=0}^{\infty}a_nx^n=a_0+a_1x+a_2x^2+\cdots.
$$

Ký hiệu $[x^n]G(x)=a_n$ nói rằng $a_n$ là hệ số của $x^n$ trong khai triển của $G(x)$.

**Ví dụ**: Với dãy $1,1,1,\ldots$, ta có

$$
G(x)=1+x+x^2+x^3+\cdots=\frac{1}{1-x}
$$

nếu xem đây là chuỗi hình thức hoặc là chuỗi hội tụ khi $|x|<1$.

## 2. Chuỗi lũy thừa hình thức

Trong toán rời rạc, ta thường không quan tâm đến miền hội tụ. Ta xem

$$
G(x)=\sum_{n\ge0}a_nx^n
$$

như một **chuỗi lũy thừa hình thức** (formal power series). Điều quan trọng nhất không phải giá trị của $x$, mà là các quy tắc trên hệ số.

## 7. Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Hàm sinh được dùng để đếm cấu hình, phân tích thuật toán, mô hình hóa trạng thái động và suy ra công thức cho số cách phân rã một đối tượng tổ hợp. Trong lập trình sinh ngẫu nhiên và phân tích ký hiệu, các chuỗi sinh còn cho phép suy ra phân phối kích thước của đối tượng sinh ra.

```python
def coeffs(seq):
    return " + ".join(f"{a}x^{i}" if i else str(a) for i, a in enumerate(seq))

print(coeffs([1, 1, 1, 1]))
```

## Bài tập thực hành

### Bài tập 1

Tìm hàm sinh của dãy $a_n=2$ với mọi $n\ge0$.

<details>
<summary>Đáp án</summary>

$$
G(x)=\sum_{n\ge0}2x^n=\frac{2}{1-x}.
$$

</details>

### Bài tập 2

Tìm hàm sinh của dãy $a_n=n$.

<details>
<summary>Đáp án</summary>

Dùng công thức chuẩn:

$$
\sum_{n\ge1}nx^n=\frac{x}{(1-x)^2}.
$$

</details>

### Bài tập 3

Giải thích vì sao dịch chuỗi bằng cách nhân với $x$ lại hữu ích khi làm việc với truy hồi.

<details>
<summary>Đáp án</summary>

Vì các hạng $a_{n-1}$, $a_{n-2}$ trong truy hồi sẽ trở thành các hệ số của chuỗi sau khi nhân với $x$ hoặc $x^2$. Nhờ vậy, truy hồi được biến thành phương trình đại số trên hàm sinh.

</details>

## Tóm tắt

- Hàm sinh thông thường của dãy $\{a_n\}$ là $\sum a_nx^n$.
- Chuỗi lũy thừa hình thức cho phép thao tác hệ số mà không cần xét hội tụ.
- Phép cộng, nhân với hằng số, dịch chỉ số và đạo hàm là các công cụ cơ bản.
- Hàm sinh mã hóa bài toán đếm và là cầu nối giữa tổ hợp với đại số.
- Trong CS, hàm sinh hỗ trợ phân tích thuật toán và bài toán đếm cấu hình.
