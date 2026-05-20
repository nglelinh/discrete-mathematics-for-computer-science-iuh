---
layout: post
title: "Giải Quan hệ Truy hồi bằng Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 2
required: true
lang: vi
---

# Giải Quan hệ Truy hồi bằng Hàm sinh

Truy hồi cho ta biết mỗi bước phụ thuộc vào bước trước, nhưng đôi khi giải nó bằng phương trình đặc trưng không thuận tiện hoặc không áp dụng đẹp. Đây là lúc hàm sinh trở thành “bộ đổi miền”: biến một bài toán trên dãy thành một bài toán đại số trên chuỗi lũy thừa.

Kỹ thuật này rất đáng học vì nó cho thấy một mô hình quen thuộc của toán học và khoa học máy tính: đổi cách nhìn bài toán để nó trở nên dễ xử lý hơn. Khi giải truy hồi bằng hàm sinh, ta không chỉ tìm công thức; ta còn học một chiến lược tư duy có thể tái sử dụng ở nhiều nơi khác.

## 1. Quy trình 4 bước

1. Đặt hàm sinh $G(x)=\sum_{n\ge0}a_nx^n$.
2. Nhân truy hồi với $x^n$ rồi cộng theo $n$ để tạo phương trình cho $G(x)$.
3. Giải đại số để tìm $G(x)$ dưới dạng phân thức.
4. Khai triển lại để đọc hệ số $a_n$.

<div class="content-box theorem-box" markdown="1">
**Mấu chốt**: Dịch chỉ số trong truy hồi tương ứng với nhân thêm $x$ hoặc $x^2$ trong hàm sinh. Nhờ đó, quan hệ đệ quy biến thành phương trình đại số.
</div>

## 2. Ví dụ Fibonacci

Xét dãy Fibonacci

$$
F_n=F_{n-1}+F_{n-2},\qquad F_0=0,\;F_1=1.
$$

Đặt

$$
G(x)=\sum_{n\ge0}F_nx^n.
$$

Nhân hai vế truy hồi với $x^n$ và cộng từ $n\ge2$:

$$
\sum_{n\ge2}F_nx^n=\sum_{n\ge2}F_{n-1}x^n+\sum_{n\ge2}F_{n-2}x^n.
$$

Ta viết lại:

$$
G(x)-F_0-F_1x=x\big(G(x)-F_0\big)+x^2G(x).
$$

Vì $F_0=0$ và $F_1=1$,

$$
G(x)-x=xG(x)+x^2G(x).
$$

Suy ra

$$
G(x)=\frac{x}{1-x-x^2}.
$$

Từ đó, ta có thể khai triển phân thức để thu được công thức tường minh cho $F_n$.

## 3. Phân thức từng phần

Nếu hàm sinh là phân thức hữu tỉ, ta thường phân tích thành tổng các phân thức đơn giản hơn. Ví dụ

$$
\frac{x}{1-x-x^2}
$$

có thể phân tích theo nghiệm của mẫu số để thu lại dạng kết hợp hai lũy thừa, khớp với kết quả từ phương trình đặc trưng.

**Nhận xét**: Phương trình đặc trưng và hàm sinh thực chất là hai con đường khác nhau dẫn tới cùng một nghiệm.

## 4. Một ví dụ truy hồi bậc 1

Giải

$$
a_n=2a_{n-1}+1,\qquad a_0=0.
$$

Đặt $G(x)=\sum_{n\ge0}a_nx^n$. Với $n\ge1$,

$$
\sum_{n\ge1}a_nx^n=2\sum_{n\ge1}a_{n-1}x^n+\sum_{n\ge1}x^n.
$$

Ta có

$$
G(x)-a_0=2xG(x)+\frac{x}{1-x}.
$$

Vì $a_0=0$,

$$
G(x)=\frac{x}{(1-x)(1-2x)}.
$$

Phân tích thành phần đơn sẽ cho công thức đóng của $a_n$.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Chọn một truy hồi bậc 1 hoặc bậc 2, công cụ tự động dựng phương trình cho $G(x)$ và hiển thị bước chuyển từ truy hồi sang phương trình đại số.
</div>

## 5. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Phải xử lý riêng vài số hạng đầu trước khi dịch chỉ số.
- Không được quên điều kiện đầu khi viết phương trình cho $G(x)$.
- Khi phân tích phân thức, phải đảm bảo khai triển lại đúng hệ số.
- Hàm sinh thường dẫn đến chuỗi vô hạn; chỉ cần làm việc với biểu thức hình thức của nó.
</div>

## 6. Ứng dụng trong Khoa học Máy tính

Hàm sinh cho phép giải các truy hồi xuất hiện trong phân tích thuật toán, đếm đường đi trên lưới, mô hình hóa chuỗi ký tự và tính số cấu hình trong tổ hợp. Nhiều bài toán trong lý thuyết ngôn ngữ hình thức cũng biểu diễn tự nhiên bằng hàm sinh, đặc biệt khi số đối tượng theo độ dài cần được mô tả.

```python
import sympy as sp
x = sp.symbols('x')
G = x / (1 - x - x**2)
print(sp.apart(G, x))
```

## Bài tập thực hành

### Bài tập 1

Tìm hàm sinh của dãy thỏa $a_n=a_{n-1}$ với $a_0=3$.

<details>
<summary>Đáp án</summary>

Dãy hằng $3,3,3,\ldots$ có hàm sinh

$$
G(x)=\frac{3}{1-x}.
$$

</details>

### Bài tập 2

Chứng minh hàm sinh của Fibonacci là $\frac{x}{1-x-x^2}$.

<details>
<summary>Đáp án</summary>

Làm theo đúng quy trình ở ví dụ Fibonacci: nhân truy hồi với $x^n$, cộng từ $n\ge2$, chuyển các tổng sang $G(x)$ và giải phương trình nhận được.

</details>

### Bài tập 3

Vì sao hàm sinh hữu ích hơn phương trình đặc trưng trong một số bài toán đếm?

<details>
<summary>Đáp án</summary>

Vì hàm sinh kết nối trực tiếp với hệ số đếm và dễ áp dụng cho bài toán tổ hợp, đặc biệt khi truy hồi gắn với số cách cấu hình, đường đi hoặc phân hoạch.

</details>

## Tóm tắt

- Hàm sinh biến truy hồi thành phương trình đại số.
- Quy trình chuẩn gồm bốn bước: đặt hàm sinh, biến đổi, giải, khai triển.
- Fibonacci là ví dụ kinh điển cho phương pháp này.
- Phân thức từng phần giúp trích xuất công thức đóng.
- Hàm sinh là công cụ mạnh trong đếm tổ hợp và phân tích thuật toán.
