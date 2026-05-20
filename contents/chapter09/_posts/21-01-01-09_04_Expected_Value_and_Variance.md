---
layout: post
title: "Kỳ vọng và Phương sai"
categories: chapter09
date: 2021-01-01
order: 4
required: true
lang: en
---

# Kỳ vọng và Phương sai

Biết một biến cố có thể xảy ra chưa đủ; ta còn muốn biết trung bình lâu dài sẽ ra sao và mức dao động quanh trung bình lớn đến mức nào. Một game có lợi nhuận kỳ vọng dương nhưng biến động quá lớn vẫn có thể nguy hiểm; một thuật toán ngẫu nhiên chạy nhanh trung bình nhưng phương sai cao có thể gây trải nghiệm thất thường.

**Kỳ vọng** và **phương sai** giúp ta đo hai khía cạnh đó một cách gọn gàng. Chúng là công cụ cốt lõi của thống kê, mô phỏng, phân tích thuật toán ngẫu nhiên, tài chính và đánh giá hiệu năng hệ thống. Đây là lúc xác suất bắt đầu trở thành ngôn ngữ để ra quyết định, không chỉ là trò tung đồng xu.

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
</div>

## 6. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Kỳ vọng không phải là “giá trị chắc chắn xảy ra”.
- Tuyến tính kỳ vọng không cần độc lập, nhưng công thức $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)$ cần độc lập hoặc hiệp phương sai bằng 0.
- Phương sai đo bình phương độ lệch, nên đơn vị bị bình phương; độ lệch chuẩn dễ diễn giải hơn.
- Kỳ vọng bằng 0 không có nghĩa trò chơi không rủi ro; phương sai vẫn có thể rất lớn.
</div>

## 7. Ứng dụng trong Khoa học Máy tính

Trong phân tích thuật toán, kỳ vọng đo thời gian chạy trung bình của quicksort, hashing và randomized algorithms. Phương sai giúp đánh giá độ ổn định: hai thuật toán có cùng kỳ vọng nhưng thuật toán có phương sai thấp thường dễ dự đoán hơn. Trong học máy, kỳ vọng và phương sai xuất hiện trong bias-variance tradeoff, đánh giá rủi ro và tối ưu hàm mất mát.

```python
import random

def simulate_die(trials=100000):
    values = [random.randint(1, 6) for _ in range(trials)]
    mean = sum(values) / trials
    var = sum((x - mean) ** 2 for x in values) / trials
    return mean, var

print(simulate_die())
```

## Bài tập thực hành

### Bài tập 1

Tung một đồng xu cân bằng 10 lần. Kỳ vọng số mặt ngửa là bao nhiêu?

<details>
<summary>Đáp án</summary>

Đây là phân phối nhị thức với $n=10,p=1/2$. Kỳ vọng là $np=5$.

</details>

### Bài tập 2

Một trò chơi trả 100 nghìn đồng nếu tung xúc xắc ra 6, và mất 10 nghìn đồng nếu ra mặt khác. Kỳ vọng lợi nhuận là bao nhiêu?

<details>
<summary>Đáp án</summary>

Đơn vị nghìn đồng:

$$
E=100\cdot\frac16+(-10)\cdot\frac56=\frac{100-50}{6}=\frac{50}{6}\approx8.33.
$$

</details>

### Bài tập 3

Nếu $X$ nhận giá trị 0,1,2 với xác suất lần lượt $1/4,1/2,1/4$, tính $E[X]$ và $\operatorname{Var}(X)$.

<details>
<summary>Đáp án</summary>

$E[X]=0\cdot1/4+1\cdot1/2+2\cdot1/4=1$.

$E[X^2]=0+1\cdot1/2+4\cdot1/4=1.5$.

$\operatorname{Var}(X)=1.5-1^2=0.5$.

</details>

## Tóm tắt

- Biến ngẫu nhiên là hàm từ không gian mẫu vào số thực.
- Kỳ vọng là trung bình có trọng số theo xác suất.
- Tuyến tính kỳ vọng đúng ngay cả khi các biến không độc lập.
- Phương sai đo độ phân tán quanh kỳ vọng; độ lệch chuẩn là căn bậc hai của phương sai.
- Trong CS, hai đại lượng này dùng để phân tích thuật toán ngẫu nhiên, mô hình học máy và rủi ro hệ thống.
