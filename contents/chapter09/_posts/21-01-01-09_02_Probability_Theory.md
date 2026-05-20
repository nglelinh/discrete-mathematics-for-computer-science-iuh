---
layout: post
title: "Lý thuyết Xác suất — Tiên đề và Tính chất"
categories: chapter09
date: 2021-01-01
order: 2
required: true
lang: en
---

# Lý thuyết Xác suất — Tiên đề và Tính chất

Khi bài toán xác suất bắt đầu có nhiều biến cố cùng lúc, trực giác lại dễ sai. Hai sự kiện có thể chồng lấn, loại trừ nhau, độc lập hoặc hoàn toàn phụ thuộc lẫn nhau. Trong phân tích rủi ro hay thiết kế hệ thống, nhầm một trong các mối quan hệ này có thể dẫn đến ước lượng sai rất xa thực tế.

Bài này đi sâu hơn vào các quy tắc vận hành của xác suất: cách cộng, cách nhân, cách hiểu giao–hợp–bù, và cách đọc đúng mối liên hệ giữa các biến cố. Mục tiêu không chỉ là tính ra đáp án, mà là xây được một mô hình đúng cho tình huống ngẫu nhiên đang xét.

## 1. Không gian xác suất

**Định nghĩa**: Một **không gian xác suất** gồm ba thành phần $(S,\mathcal{F},P)$:

- $S$: không gian mẫu, tập tất cả kết quả có thể.
- $\mathcal{F}$: họ các biến cố, thường là tập con của $S$ trong trường hợp hữu hạn.
- $P$: hàm xác suất gán cho mỗi biến cố $E$ một số thực $P(E)$.

Trong môn học này, ta chủ yếu xét không gian mẫu hữu hạn, nên có thể hiểu biến cố là mọi tập con $E\subseteq S$.

**Ví dụ**: Tung một con xúc xắc cân bằng. Khi đó $S=\{1,2,3,4,5,6\}$; biến cố “ra số chẵn” là $E=\{2,4,6\}$ và $P(E)=3/6=1/2$.

## 2. Ba tiên đề Kolmogorov

Với mọi biến cố $E$ và các biến cố đôi một xung khắc $E_1,E_2,\ldots$, xác suất thỏa:

1. **Không âm**: $P(E)\ge 0$.
2. **Chuẩn hóa**: $P(S)=1$.
3. **Cộng tính**: Nếu $E_i\cap E_j=\emptyset$ khi $i\ne j$, thì

$$
P\left(\bigcup_i E_i\right)=\sum_i P(E_i).
$$

<div class="content-box theorem-box" markdown="1">
**Tư tưởng cốt lõi**: Xác suất là “độ đo” của biến cố. Một biến cố không thể có xác suất âm, toàn bộ không gian chắc chắn xảy ra, và các phần không chồng lấn thì cộng được.
</div>

## 3. Các hệ quả quan trọng

### 3.1. Xác suất biến cố rỗng

Vì $S$ và $\emptyset$ xung khắc, đồng thời $S\cup\emptyset=S$, ta có

$$
1=P(S)=P(S\cup\emptyset)=P(S)+P(\emptyset)=1+P(\emptyset).
$$

Suy ra $P(\emptyset)=0$.

### 3.2. Biến cố đối

Nếu $\overline{E}=S\setminus E$, thì $E\cap\overline{E}=\emptyset$ và $E\cup\overline{E}=S$. Do đó

$$
P(\overline{E})=1-P(E).
$$

### 3.3. Quy tắc cộng tổng quát

Với hai biến cố bất kỳ,

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$

Đây là phiên bản xác suất của nguyên lý bù trừ.

**Chứng minh**: Tách $A\cup B$ thành ba phần rời nhau: chỉ thuộc $A$, chỉ thuộc $B$, và thuộc cả hai. Khi cộng $P(A)+P(B)$, phần $A\cap B$ bị tính hai lần, nên phải trừ một lần.

## 4. Không gian mẫu đồng khả năng

Nếu $S$ hữu hạn và mọi kết quả có khả năng như nhau, thì với mọi biến cố $E$,

$$
P(E)=\frac{|E|}{|S|}.
$$

**Ví dụ**: Chọn ngẫu nhiên một chuỗi nhị phân độ dài 4. Có $2^4=16$ chuỗi. Biến cố có đúng hai bit 1 có $\binom{4}{2}=6$ chuỗi, nên xác suất là $6/16=3/8$.

## 5. Xác suất có điều kiện

**Định nghĩa**: Nếu $P(B)>0$, xác suất của $A$ khi biết $B$ đã xảy ra là

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

Công thức này không phải là mẹo tính toán; nó định nghĩa một không gian mẫu mới. Khi biết $B$ xảy ra, ta chỉ còn xét các kết quả nằm trong $B$.

**Quy tắc nhân**:

$$
P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A).
$$

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học chọn một sơ đồ Venn gồm hai biến cố $A,B$. Công cụ tô lại vùng $B$ thành không gian mẫu mới và hiển thị tỉ lệ của phần $A\cap B$ bên trong $B$.
</div>

## 6. Biến cố độc lập

**Định nghĩa**: Hai biến cố $A$ và $B$ độc lập nếu

$$
P(A\cap B)=P(A)P(B).
$$

Nếu $P(B)>0$, điều này tương đương với $P(A\mid B)=P(A)$: biết $B$ xảy ra không làm thay đổi xác suất của $A$.

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- **Độc lập** không có nghĩa là **xung khắc**. Nếu $A$ và $B$ xung khắc và đều có xác suất dương, chúng không độc lập.
- $P(A\mid B)$ không bằng $P(B\mid A)$ nói chung.
- Xác suất nhỏ không đồng nghĩa với không thể xảy ra; xác suất 0 trong mô hình liên tục cũng không nhất thiết là bất khả.
</div>

## 7. Ứng dụng trong Khoa học Máy tính

Trong thuật toán ngẫu nhiên, ta dùng xác suất để mô tả thời gian chạy trung bình và xác suất lỗi. Trong học máy, mô hình phân loại dự đoán nhãn dựa trên phân phối xác suất. Trong an toàn thông tin, xác suất giúp đánh giá khả năng đoán mật khẩu, va chạm hàm băm và rủi ro tấn công. Trong kiểm thử phần mềm, xác suất được dùng để lấy mẫu đầu vào và ước lượng độ tin cậy.

```python
from fractions import Fraction

# Xác suất một chuỗi nhị phân độ dài 8 có đúng ba bit 1
from math import comb
p = Fraction(comb(8, 3), 2**8)
print(p)
```

## Bài tập thực hành

### Bài tập 1

Tung hai xúc xắc cân bằng. Tính xác suất tổng bằng 7.

<details>
<summary>Đáp án</summary>

Không gian mẫu có 36 kết quả. Có 6 kết quả cho tổng 7: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$. Xác suất là $6/36=1/6$.

</details>

### Bài tập 2

Một chuỗi nhị phân độ dài 5 được chọn ngẫu nhiên. Tính xác suất chuỗi có ít nhất một bit 1.

<details>
<summary>Đáp án</summary>

Dùng biến cố đối: chỉ có một chuỗi không có bit 1 là `00000`. Do đó xác suất là $1-1/32=31/32$.

</details>

### Bài tập 3

Nếu $P(A)=0.4$, $P(B)=0.5$, $P(A\cap B)=0.2$, hai biến cố có độc lập không?

<details>
<summary>Đáp án</summary>

Có, vì $P(A)P(B)=0.4\cdot0.5=0.2=P(A\cap B)$.

</details>

## Tóm tắt

- Không gian xác suất gồm không gian mẫu, họ biến cố và hàm xác suất.
- Ba tiên đề Kolmogorov dẫn đến các quy tắc quen thuộc như biến cố đối và quy tắc cộng.
- Xác suất có điều kiện thu hẹp không gian mẫu về biến cố đã biết.
- Độc lập nghĩa là thông tin về biến cố này không làm thay đổi xác suất của biến cố kia.
- Các khái niệm này là nền tảng cho thuật toán ngẫu nhiên, học máy, bảo mật và kiểm thử.
