---
layout: post
title: "Giới thiệu Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 1
required: true
lang: vi
---

# Giới thiệu Hàm sinh

Thoạt nhìn, một dãy số chỉ là danh sách các hệ số. Nhưng nếu gói cả dãy ấy vào trong một biểu thức đại số duy nhất, ta có thể cộng, nhân, biến đổi và “đọc ra” thông tin đếm theo cách rất bất ngờ. Đó là lý do **hàm sinh** được xem như một chiếc hộp công cụ cực mạnh của tổ hợp và toán rời rạc.

Với hàm sinh, bài toán đếm không còn chỉ là đếm trực tiếp. Ta biến nó thành thao tác trên chuỗi lũy thừa, rồi để đại số làm phần việc nặng. Kỹ thuật này đặc biệt hữu ích khi đối mặt với các cấu hình nhiều ràng buộc, các dãy được xác định gián tiếp, và các bài toán mà cách đếm thô trở nên rối rắm.

## 1. Định nghĩa

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

<div class="content-box warning-box" markdown="1">
**Lưu ý**: Không nên nhầm hàm sinh với một hàm giải tích thông thường. Ở đây, ý nghĩa chính nằm ở việc thao tác hệ số, không phải giá trị số tại một điểm cụ thể.
</div>

## 3. Các hàm sinh cơ bản

- Dãy hằng $1,1,1,\ldots$:

$$
\sum_{n\ge0}x^n=\frac{1}{1-x}.
$$

- Dãy chỉ có số 1 ở vị trí 0: $1,0,0,\ldots$:

$$
1.
$$

- Dãy $1,2,3,4,\ldots$:

$$
\sum_{n\ge1}nx^n=\frac{x}{(1-x)^2}.
$$

- Dãy số nhị thức theo hàng $n$:

$$
(1+x)^n=\sum_{k=0}^{n}\binom{n}{k}x^k.
$$

## 4. Phép toán cơ bản

### 4.1. Cộng và nhân với hằng số

Nếu $A(x)=\sum a_nx^n$ và $B(x)=\sum b_nx^n$, thì

$$
A(x)+B(x)=\sum (a_n+b_n)x^n,
$$

và với hằng số $c$,

$$
cA(x)=\sum (ca_n)x^n.
$$

### 4.2. Dịch chỉ số

Nếu $A(x)=\sum_{n\ge0}a_nx^n$, thì

$$
 xA(x)=\sum_{n\ge0}a_nx^{n+1}.
$$

Do đó nhân với $x$ tương ứng với “dịch sang phải một bước”. Đây là lý do hàm sinh đặc biệt phù hợp với truy hồi.

### 4.3. Đạo hàm

Nếu

$$
A(x)=\sum_{n\ge0}a_nx^n,
$$

thì

$$
A'(x)=\sum_{n\ge1}na_nx^{n-1}.
$$

Đạo hàm rất hữu ích để tạo hệ số $n, n(n-1),\ldots$ từ chuỗi đơn giản.

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học nhập một dãy ngắn, công cụ sinh hàm sinh đến vài hạng đầu và minh họa phép nhân với $x$, đạo hàm và cộng chuỗi.
</div>

## 5. Ý nghĩa tổ hợp

Một hàm sinh không chỉ là công cụ đại số. Mỗi hệ số có thể đếm số đối tượng theo kích thước. Ví dụ, nếu $a_n$ là số cách chọn một bộ sản phẩm tổng trọng lượng $n$, thì hàm sinh chính là cách ghi lại toàn bộ bảng đếm đó trong một biểu thức duy nhất.

## 6. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Không phải mọi chuỗi lũy thừa đều phải hội tụ trong bài này.
- $[x^n]G(x)$ là phép lấy hệ số, không phải phép chia.
- Dịch chỉ số phải theo dõi cẩn thận số hạng đầu tiên.
- Hàm sinh thông thường khác với hàm sinh mũ; hai loại này phục vụ những mục đích khác nhau.
</div>

## 7. Ứng dụng trong Khoa học Máy tính

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
