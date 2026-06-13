---
layout: post
title: "Giải Quan hệ Truy hồi Tuyến tính"
categories: chapter10
date: 2021-01-01
order: 2
required: true
lang: vi
---

# Giải Quan hệ Truy hồi Tuyến tính

Viết được quan hệ truy hồi mới chỉ là nửa chặng đường. Trong thực tế, ta còn muốn biết giá trị ở bước thứ 50, thứ 1000, hay tốc độ tăng trưởng của cả dãy mà không phải tính lần lượt từng bước một.


Quan hệ truy hồi cho phép ta mô tả tiến trình theo từng bước, đúng với cách nhiều thuật toán đệ quy và dynamic programming vận hành.
Với lớp bài toán quan trọng nhất, **quan hệ truy hồi tuyến tính**, ta có thể tìm được công thức tường minh hoặc ít nhất mô tả rất rõ cấu trúc nghiệm. Đây là kỹ năng cực kỳ hữu ích trong phân tích thuật toán và các mô hình rời rạc.

Từ số phép gọi đệ quy, số cấu hình ở mỗi mức, đến độ phức tạp của những thuật toán chia để trị đơn giản, rất nhiều bài toán quy về giải đúng một truy hồi tuyến tính.

Trong bài này, chúng ta sẽ học các kỹ thuật giải loại truy hồi này và thấy vì sao một phương trình nhìn ngắn có thể chứa bên trong cả một quy luật tăng trưởng lớn.

## 1. Dạng tổng quát

**Định nghĩa**: Quan hệ truy hồi tuyến tính thuần nhất hệ số hằng bậc $k$ có dạng

$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k},\quad c_k\ne0.
$$

- **Tuyến tính**: các số hạng $a_{n-i}$ chỉ xuất hiện bậc nhất.
- **Thuần nhất**: không có thành phần ngoài chỉ phụ thuộc vào $n$.
- **Hệ số hằng**: $c_i$ không thay đổi theo $n$.
- Cần $k$ điều kiện đầu để xác định duy nhất dãy.

**Ví dụ**: Fibonacci thỏa $F_n=F_{n-1}+F_{n-2}$ với $F_0=0,F_1=1$.

## 2. Ý tưởng nghiệm dạng $r^n$

Giả sử $a_n=r^n$ với $r\ne0$. Thay vào truy hồi bậc hai

$$
a_n=c_1a_{n-1}+c_2a_{n-2}
$$

thu được

$$
r^n=c_1r^{n-1}+c_2r^{n-2}.
$$

Chia cho $r^{n-2}$:

$$
r^2-c_1r-c_2=0.
$$

Đây là **phương trình đặc trưng**.

<div class="content-box insight-box" markdown="1">
**Trực giác**: Nếu một dãy tăng theo quy luật nhân lặp lại, tỉ số giữa các số hạng liên tiếp gần giống một hằng số. Vì vậy nghiệm mũ $r^n$ là ứng viên tự nhiên cho hệ tuyến tính hệ số hằng.
</div>

## 3. Nghiệm phân biệt

Nếu phương trình đặc trưng bậc hai có hai nghiệm phân biệt $r_1,r_2$, nghiệm tổng quát là

$$
a_n=\alpha r_1^n+\beta r_2^n.
$$

Các hằng số $\alpha,\beta$ được xác định từ điều kiện đầu.

**Ví dụ**: Giải $a_n=5a_{n-1}-6a_{n-2}$, $a_0=2,a_1=5$.

Phương trình đặc trưng:

$$
r^2-5r+6=0=(r-2)(r-3).
$$

Nghiệm tổng quát:

$$
a_n=\alpha2^n+\beta3^n.
$$

Từ $a_0=2$: $\alpha+\beta=2$. Từ $a_1=5$: $2\alpha+3\beta=5$. Suy ra $\beta=1,\alpha=1$. Vậy

$$
a_n=2^n+3^n.
$$

## 4. Nghiệm bội

Nếu phương trình đặc trưng có nghiệm kép $r$, nghiệm tổng quát là

$$
a_n=(\alpha+\beta n)r^n.
$$

Tổng quát hơn, nếu $r$ là nghiệm bội $m$, ta có các thành phần

$$
r^n,\; nr^n,\; n^2r^n,\ldots,n^{m-1}r^n.
$$

**Ví dụ**: Giải $a_n=4a_{n-1}-4a_{n-2}$. Phương trình đặc trưng là

$$
r^2-4r+4=(r-2)^2=0,
$$

nên

$$
a_n=(\alpha+\beta n)2^n.
$$

## 5. Nghiệm phức

Nếu phương trình đặc trưng có nghiệm phức liên hợp $r=\rho(\cos\theta+i\sin\theta)$ và $\overline r$, nghiệm thực có dạng

$$
a_n=\rho^n(A\cos n\theta+B\sin n\theta).
$$

Trường hợp này xuất hiện trong các mô hình dao động rời rạc, bộ lọc tín hiệu và phân tích hệ thống tuyến tính.

## 6. Bậc cao hơn

Với truy hồi bậc $k$,

$$
a_n=c_1a_{n-1}+\cdots+c_ka_{n-k},
$$

phương trình đặc trưng là

$$
r^k-c_1r^{k-1}-c_2r^{k-2}-\cdots-c_k=0.
$$

Mỗi nghiệm phân biệt $r_i$ đóng góp một hạng $\alpha_i r_i^n$; nghiệm bội đóng góp thêm các nhân tử đa thức theo $n$.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học nhập hệ số $c_1,c_2$ và điều kiện đầu. Công cụ vẽ nghiệm đặc trưng trên trục số/phức và hiển thị vài số hạng đầu của dãy.
<div data-demo="linear-recurrence-solver"></div>
</div>
<script src="{{ '/public/js/linear-recurrence-solver.js' | relative_url }}"></script>

