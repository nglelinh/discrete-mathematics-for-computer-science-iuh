---
layout: post
title: "Quan hệ Truy hồi Không Thuần nhất và Ứng dụng"
categories: chapter10
date: 2021-01-01
order: 3
required: true
lang: vi
---

# Quan hệ Truy hồi Không Thuần nhất và Ứng dụng

Không phải truy hồi nào cũng “sạch” đến mức mỗi số hạng chỉ là tổ hợp của các số hạng trước. Nhiều hệ thống còn có lực tác động từ bên ngoài: thêm một lượng cố định mỗi vòng, cộng một hàm theo n, hay chịu một nguồn vào mới ở mỗi bước. Những phần “ngoại sinh” đó làm bài toán thực tế hơn — và cũng khó hơn.

**Truy hồi không thuần nhất** giúp mô hình hóa chính những tình huống đó. Học cách xử lý chúng là bước quan trọng để phân tích thuật toán có chi phí phụ thêm, mô hình hóa tiến trình có đầu vào liên tục, và hiểu cách một hệ quy luật nội tại phản ứng trước tác động từ bên ngoài.

## 1. Dạng tổng quát

Quan hệ truy hồi tuyến tính không thuần nhất bậc $k$ có dạng

$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}+f(n),
$$

trong đó $f(n)$ không đồng nhất bằng 0.

Quan hệ thuần nhất liên kết là

$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}.
$$

## 2. Nguyên lý chồng chất

Nghiệm tổng quát có dạng

$$
a_n=a_n^{(h)}+a_n^{(p)},
$$

trong đó:

- $a_n^{(h)}$ là nghiệm tổng quát của quan hệ thuần nhất liên kết.
- $a_n^{(p)}$ là một nghiệm riêng của quan hệ không thuần nhất.

**Chứng minh**: Nếu $L$ là toán tử tuyến tính tương ứng với vế trái sau khi chuyển hết về một phía, thì quan hệ có dạng $L(a)=f$. Nếu $L(h)=0$ và $L(p)=f$, thì $L(h+p)=L(h)+L(p)=f$. Do đó tổng của nghiệm thuần nhất và một nghiệm riêng là nghiệm của bài toán đầy đủ.

## 3. Phương pháp hệ số bất định

Khi $f(n)$ có dạng quen thuộc, ta đoán nghiệm riêng cùng “họ” với $f(n)$.

| Dạng $f(n)$ | Dạng thử cho $a_n^{(p)}$ |
|------------|---------------------------|
| Hằng số $d$ | $A$ |
| Đa thức bậc $m$ | đa thức bậc $m$ |
| $b^n$ | $Ab^n$ |
| $n^m b^n$ | đa thức bậc $m$ nhân $b^n$ |

Nếu dạng thử trùng với nghiệm thuần nhất, nhân thêm $n$ đủ số lần để độc lập tuyến tính.

## 4. Ví dụ với hằng số

Giải

$$
a_n=2a_{n-1}+3,\quad a_0=1.
$$

Phần thuần nhất: $a_n^{(h)}=C2^n$.

Thử nghiệm riêng hằng $a_n^{(p)}=A$. Thay vào:

$$
A=2A+3\Rightarrow A=-3.
$$

Vậy $a_n=C2^n-3$. Từ $a_0=1$, $C-3=1$ nên $C=4$. Do đó

$$
a_n=4\cdot2^n-3.
$$

## 5. Ví dụ với đa thức

Giải dạng tổng quát:

$$
a_n=a_{n-1}+n.
$$

Phần thuần nhất có nghiệm $C$. Vì $f(n)=n$ là đa thức bậc 1, thử $a_n^{(p)}=An^2+Bn$. Thay vào:

$$
An^2+Bn=A(n-1)^2+B(n-1)+n.
$$

So sánh hệ số cho $A=\frac12$. Ta có thể chọn $B=\frac12$, khi đó

$$
a_n^{(p)}=\frac{n(n+1)}2.
$$

Đây chính là tổng $1+2+\cdots+n$.

## 6. Trường hợp cộng hưởng

Xét

$$
a_n=2a_{n-1}+2^n.
$$

Phần thuần nhất có nghiệm $C2^n$. Nếu thử $A2^n$, nó trùng với nghiệm thuần nhất nên không thể xác định $A$. Ta phải thử

$$
a_n^{(p)}=An2^n.
$$

Đây gọi là hiện tượng **cộng hưởng**: tác động ngoài có cùng dạng với nghiệm tự nhiên của hệ.

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học chọn dạng $f(n)$ và nghiệm đặc trưng. Công cụ đề xuất dạng nghiệm riêng, cảnh báo khi xảy ra cộng hưởng và tự nhân thêm $n$.
</div>

## 7. Ứng dụng phân tích thuật toán

Quan hệ

$$
T(n)=2T(n/2)+n
$$

mô tả nhiều thuật toán chia để trị như merge sort. Đây không phải truy hồi tuyến tính theo chỉ số $n-1$, nhưng tư tưởng vẫn giống: nghiệm gồm phần do đệ quy và phần chi phí ngoài $n$ ở mỗi mức. Kết quả $T(n)=\Theta(n\log n)$ cho thấy thành phần không thuần nhất quyết định đáng kể độ phức tạp.

Với truy hồi tuyến tính, ví dụ số phép gán trong một vòng lặp tích lũy có thể thỏa

$$
a_n=a_{n-1}+2n+1,
$$

và nghiệm riêng bậc hai cho ta tổng chi phí bậc $\Theta(n^2)$.

## 8. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Tìm nghiệm riêng trước rồi quên cộng nghiệm thuần nhất.
- Dùng điều kiện đầu để xác định nghiệm riêng; điều kiện đầu chỉ xác định hằng số trong nghiệm tổng quát.
- Không kiểm tra cộng hưởng với nghiệm đặc trưng.
- Nhầm truy hồi không thuần nhất với truy hồi phi tuyến. Ví dụ $a_n=a_{n-1}^2+1$ là phi tuyến, không thuộc kỹ thuật này.
</div>

## 9. Ứng dụng trong Khoa học Máy tính

Truy hồi không thuần nhất mô hình hóa chi phí thuật toán khi mỗi bước có chi phí xử lý riêng. Nó cũng xuất hiện trong tài chính tính toán, mô phỏng hệ thống, hàng đợi, tăng trưởng dữ liệu và phân tích amortized. Biết tách nghiệm thuần nhất và nghiệm riêng giúp ta nhìn rõ phần nào đến từ “trạng thái cũ” và phần nào do “chi phí mới”.

```python
def recurrence(a0, n):
    a = a0
    values = [a]
    for k in range(1, n + 1):
        a = 2 * a + 3
        values.append(a)
    return values

print(recurrence(1, 6))
```

## Bài tập thực hành

### Bài tập 1

Giải $a_n=3a_{n-1}+2$ với $a_0=0$.

<details>
<summary>Đáp án</summary>

Thuần nhất: $C3^n$. Thử nghiệm riêng $A$: $A=3A+2\Rightarrow A=-1$. Vậy $a_n=C3^n-1$. Từ $a_0=0$, $C=1$. Do đó $a_n=3^n-1$.

</details>

### Bài tập 2

Cho $a_n=a_{n-1}+2n+1$, $a_0=0$. Dự đoán nghiệm tường minh.

<details>
<summary>Đáp án</summary>

$$
a_n=\sum_{k=1}^n(2k+1)=2\cdot\frac{n(n+1)}2+n=n^2+2n.
$$

</details>

### Bài tập 3

Với $a_n=2a_{n-1}+2^n$, nên thử nghiệm riêng dạng nào?

<details>
<summary>Đáp án</summary>

Vì $2^n$ đã là nghiệm của phần thuần nhất, phải nhân thêm $n$. Dạng thử là $An2^n$.

</details>

## Tóm tắt

- Quan hệ không thuần nhất có thêm thành phần $f(n)$.
- Nghiệm tổng quát bằng nghiệm thuần nhất cộng một nghiệm riêng.
- Phương pháp hệ số bất định chọn dạng nghiệm riêng theo dạng của $f(n)$.
- Nếu dạng thử trùng nghiệm thuần nhất, nhân thêm $n$.
- Trong CS, truy hồi không thuần nhất mô hình hóa chi phí mới phát sinh ở mỗi bước thuật toán.
