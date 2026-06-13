---
layout: post
title: "Kỳ vọng và Phương sai"
categories: chapter09
date: 2021-01-01
order: 4
required: true
lang: en
---

Biết xác suất của từng kết quả vẫn chưa đủ khi ta muốn tóm tắt hành vi của cả một quá trình ngẫu nhiên. Nếu một thuật toán ngẫu nhiên chạy nhiều lần, ta muốn biết nó thường tốn bao nhiêu bước. Nếu một hệ thống chịu nhiễu, ta muốn biết kết quả dao động mạnh hay yếu quanh mức trung bình.


Xác suất giúp ta chuyển từ trực giác mơ hồ sang đánh giá định lượng, điều rất quan trọng khi phân tích thuật toán ngẫu nhiên, dữ liệu nhiễu và rủi ro hệ thống.
**Kỳ vọng** giúp ta đo giá trị trung bình dài hạn, còn **phương sai** đo mức độ phân tán quanh giá trị đó. Hai khái niệm này là bộ đôi trung tâm trong xác suất, thống kê và phân tích hiệu năng.

Trong khoa học máy tính, chúng xuất hiện khi đánh giá randomized algorithm, phân tích tải hệ thống, học máy, xử lý tín hiệu và nhiều mô hình có thành phần ngẫu nhiên. Chúng cho ta cái nhìn sâu hơn nhiều so với chỉ nhìn từng xác suất rời rạc.

Trong bài này, chúng ta sẽ xây trực giác cho kỳ vọng và phương sai, rồi dùng chúng để đọc hành vi tổng thể của biến ngẫu nhiên một cách có hệ thống.

## 1. Biến ngẫu nhiên rời rạc

**Định nghĩa**: Một **biến ngẫu nhiên** $X$ là hàm ánh xạ từ không gian mẫu $S$ vào tập số thực:

$$
X:S\to \mathbb{R}.
$$

Biến ngẫu nhiên không phải là “biến có giá trị ngẫu nhiên” theo nghĩa lập trình; nó là một hàm, còn sự ngẫu nhiên đến từ kết quả trong $S$.

**Ví dụ**: Tung hai đồng xu. Không gian mẫu là $S=\{HH,HT,TH,TT\}$. Nếu $X$ là số mặt ngửa, thì $X(HH)=2$, $X(HT)=1$, $X(TH)=1$, $X(TT)=0$.

## 2. Kỳ vọng

**Định nghĩa**: Với biến ngẫu nhiên rời rạc $X$ nhận các giá trị $x$, kỳ vọng của $X$ là

$$
E[X]=\sum_x xP(X=x).
$$

Kỳ vọng là trung bình có trọng số theo xác suất. Nó không nhất thiết là một giá trị mà $X$ có thể nhận.

**Ví dụ**: Tung một xúc xắc cân bằng. Nếu $X$ là số chấm,

$$
E[X]=\frac{1+2+3+4+5+6}{6}=3.5.
$$

Không có mặt nào mang giá trị 3.5, nhưng trung bình dài hạn tiến gần 3.5.

## 3. Tuyến tính của kỳ vọng

**Định lý**: Với mọi biến ngẫu nhiên $X,Y$ và hằng số $a,b$,

$$
E[aX+bY]=aE[X]+bE[Y].
$$

Điều quan trọng: tính chất này đúng **không cần** $X$ và $Y$ độc lập.

**Chứng minh ý tưởng**: Kỳ vọng là phép tổng có trọng số. Phép tổng phân phối qua phép cộng và nhân hằng số, nên kỳ vọng cũng phân phối qua phép cộng và nhân hằng số.

**Ví dụ CS**: Một thuật toán thực hiện $n$ phép thử độc lập, mỗi phép thành công với xác suất $p$. Gọi $X_i=1$ nếu phép thử thứ $i$ thành công, ngược lại $0$. Tổng số thành công là $X=X_1+\cdots+X_n$. Khi đó

$$
E[X]=E[X_1]+\cdots+E[X_n]=np.
$$

## 4. Phương sai và độ lệch chuẩn

**Định nghĩa**: Phương sai của $X$ là

$$
\operatorname{Var}(X)=E[(X-E[X])^2].
$$

Công thức tính thường dùng:

$$
\operatorname{Var}(X)=E[X^2]-(E[X])^2.
$$

**Chứng minh**:

$$
\begin{aligned}
E[(X-\mu)^2]
&=E[X^2-2\mu X+\mu^2]\\
&=E[X^2]-2\mu E[X]+\mu^2\\
&=E[X^2]-2\mu^2+\mu^2\\
&=E[X^2]-\mu^2,
\end{aligned}
$$

trong đó $\mu=E[X]$.

**Độ lệch chuẩn** là $\sigma=\sqrt{\operatorname{Var}(X)}$, có cùng đơn vị với $X$.

## 5. Phân phối Bernoulli và nhị thức

Nếu $X$ là biến Bernoulli với $P(X=1)=p$ và $P(X=0)=1-p$, thì

$$
E[X]=p,\quad \operatorname{Var}(X)=p(1-p).
$$

Nếu $Y$ là số lần thành công trong $n$ phép thử Bernoulli độc lập xác suất $p$, thì $Y$ có phân phối nhị thức:

$$
P(Y=k)=\binom{n}{k}p^k(1-p)^{n-k},
$$

và

$$
E[Y]=np,\quad \operatorname{Var}(Y)=np(1-p).
$$

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học thay đổi $n$ và $p$ của phân phối nhị thức. Công cụ vẽ biểu đồ cột, đánh dấu kỳ vọng và hiển thị phương sai.
<div data-demo="binomial-distribution"></div>
</div>
<script src="{{ '/public/js/binomial-distribution.js' | relative_url }}"></script>

