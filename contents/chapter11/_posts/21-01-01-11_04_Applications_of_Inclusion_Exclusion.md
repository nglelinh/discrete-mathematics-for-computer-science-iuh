---
layout: post
title: "Ứng dụng của Nguyên lý Bao hàm - Loại trừ"
categories: chapter11
date: 2021-01-01
order: 4
required: false
lang: vi
---

# Ứng dụng của Nguyên lý Bao hàm - Loại trừ

Một nguyên lý toán học chỉ thật sự “sống” khi nó giải được bài toán cụ thể. Với bao hàm – loại trừ, sức mạnh không nằm ở công thức trừ qua cộng lại, mà ở khả năng áp nó vào các tình huống tưởng rất khác nhau: hoán vị có điểm cố định, số nghiệm nguyên, ràng buộc chia hết, hay các bài toán chọn lựa có điều kiện cấm.

Bài này tập trung vào ứng dụng để biến kỹ thuật thành phản xạ. Mục tiêu là khi gặp một bài toán đếm phức tạp, bạn nhận ra ngay đâu là các tập cần đếm, đâu là phần giao phải hiệu chỉnh, và vì sao cách tổ chức bài toán quyết định gần hết độ khó của lời giải.

## 1. Sàng Legendre và đếm số nguyên tố

Để đếm số nguyên tố không vượt quá $N$, ta đếm số số bị chia hết bởi ít nhất một số nguyên tố nhỏ hơn hoặc bằng $\sqrt N$, rồi loại bỏ chúng khỏi tập ứng viên. Ý tưởng này không thay thế sàng Eratosthenes trong tính toán thực tế, nhưng minh họa rất rõ cách bao hàm - loại trừ hoạt động.

**Ví dụ**: Với $N=30$, các số nguyên tố không vượt quá $\sqrt{30}$ là 2, 3, 5. Đếm các số chia hết cho ít nhất một trong 2,3,5 rồi điều chỉnh để không loại nhầm chính 2,3,5.

## 2. Hàm phi Euler

**Định nghĩa**: $\phi(n)$ là số các số nguyên dương không vượt quá $n$ và nguyên tố cùng nhau với $n$.

Nếu

$$
n=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k},
$$

thì

$$
\phi(n)=n\prod_{i=1}^{k}\left(1-\frac{1}{p_i}\right).
$$

**Ý tưởng chứng minh**: Đếm các số từ 1 đến $n$, rồi loại các số chia hết cho từng $p_i$ bằng bao hàm - loại trừ.

## 3. Số toàn ánh

Số ánh xạ toàn ánh từ một tập $m$ phần tử sang một tập $n$ phần tử có thể đếm bằng bao hàm - loại trừ:

$$
\text{Surj}(m,n)=\sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m.
$$

**Trực giác**: Bắt đầu từ tất cả ánh xạ có $n^m$ cách. Trừ các ánh xạ bỏ sót ít nhất một giá trị đích. Có $\binom{n}{1}(n-1)^m$ ánh xạ bỏ sót một giá trị, cộng lại phần bỏ sót hai giá trị, và cứ tiếp tục như vậy.

## 4. Hoán vị không điểm cố định

Một hoán vị của $n$ phần tử không có điểm cố định gọi là **derangement**. Số derangement ký hiệu $!n$ và có công thức

$$
!n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.
$$

Đây là kết quả kinh điển của bao hàm - loại trừ: bắt đầu từ $n!$ hoán vị, trừ hoán vị cố định ít nhất một vị trí, cộng lại hoán vị cố định ít nhất hai vị trí, v.v.

## 5. Ứng dụng trong tô màu và ràng buộc

Trong bài toán tô màu, ta thường cần đếm số cách gán màu sao cho các điều kiện cấm không xảy ra. Gọi $A_i$ là tập cách tô vi phạm cạnh thứ $i$. Số cách tô hợp lệ là tổng số cách tô trừ đi hợp các vi phạm, tức là dùng bao hàm - loại trừ.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học chọn số phần tử miền nguồn và miền đích. Công cụ hiển thị số toàn ánh bằng cách trừ các hàm bỏ sót giá trị đích.
</div>

## 6. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Trong số toàn ánh, không được dùng đơn giản $n^m$ vì $n^m$ đếm mọi ánh xạ, kể cả không phủ hết miền đích.
- Với $\phi(n)$, chỉ các thừa số nguyên tố phân biệt của $n$ xuất hiện trong tích.
- Derangement không phải là hoán vị không có chu trình; nó chỉ không có điểm cố định.
- Bao hàm - loại trừ có thể rất tốn kém khi số điều kiện lớn, vì có $2^n-1$ giao cần xét.
</div>

## 7. Ứng dụng trong Khoa học Máy tính

Trong kiểm thử phần mềm, số toàn ánh mô hình hóa việc phân phối ca kiểm thử sao cho mọi module đều được chạm tới. Trong bảo mật, derangement liên quan đến tráo khóa và phân phối bí mật sao cho không ai nhận đúng khóa cũ. Trong tối ưu tổ hợp, bao hàm - loại trừ là nền tảng của nhiều thuật toán đếm chính xác nhưng có độ phức tạp lũy thừa.

```python
from math import comb, factorial

def surjections(m, n):
    return sum((-1)**k * comb(n, k) * (n-k)**m for k in range(n+1))

def derangement(n):
    return factorial(n) * sum(((-1)**k) / factorial(k) for k in range(n+1))

print(surjections(5, 3))
```

## Bài tập thực hành

### Bài tập 1

Tính $\phi(12)$.

<details>
<summary>Đáp án</summary>

$12=2^2\cdot3$. Do đó

$$
\phi(12)=12\left(1-\frac12\right)\left(1-\frac13\right)=4.
$$

Các số là 1,5,7,11.

</details>

### Bài tập 2

Có bao nhiêu toàn ánh từ tập 4 phần tử vào tập 2 phần tử?

<details>
<summary>Đáp án</summary>

$$
2^4-\binom{2}{1}1^4=16-2=14.
$$

</details>

### Bài tập 3

Tính số derangement của 4 phần tử.

<details>
<summary>Đáp án</summary>

$$
!4=4!\left(1-1+\frac1{2!}-\frac1{3!}+\frac1{4!}\right)=9.
$$

</details>

## Tóm tắt

- Bao hàm - loại trừ có nhiều ứng dụng sâu hơn việc đếm hợp tập hợp.
- Sàng Legendre và hàm phi Euler dùng nó trong lý thuyết số.
- Số toàn ánh và derangement là hai ứng dụng tổ hợp kinh điển.
- Trong CS, nguyên lý này hỗ trợ kiểm thử, bảo mật, đếm chính xác và tối ưu tổ hợp.
