---
layout: post
title: "Nguyên lý Bao hàm - Loại trừ"
categories: chapter11
date: 2021-01-01
order: 3
required: true
lang: vi
---

# Nguyên lý Bao hàm - Loại trừ

Khi đếm các đối tượng thỏa nhiều điều kiện cùng lúc, cách cộng thẳng từng nhóm gần như chắc chắn sẽ sai nếu các nhóm có giao nhau. Đây là một vấn đề rất thực trong xác suất, truy vấn dữ liệu và cả các bài toán tổ hợp.


Hàm sinh mạnh ở chỗ nó đổi một dãy số thành đối tượng đại số dễ thao tác hơn, khá giống cách ta chọn biểu diễn phù hợp để làm bài toán đơn giản đi.
**Nguyên lý bao hàm, loại trừ** cho ta một khuôn mẫu chính xác để sửa hiện tượng đếm trùng. Ta cộng các nhóm riêng lẻ, trừ đi các phần giao đã bị tính hai lần, rồi tiếp tục điều chỉnh khi có giao của ba nhóm, bốn nhóm và hơn nữa.

Điều làm nguyên lý này đáng học là nó xuất hiện lặp đi lặp lại trong nhiều bối cảnh khác nhau. Một công cụ đúng ở tập hợp cũng đúng ở xác suất và nhiều bài toán đếm cấu hình.

Trong bài học này, chúng ta sẽ xây lại nguyên lý một cách có hệ thống và chuẩn bị nền cho các ứng dụng mạnh hơn ngay sau đó.

## 1. Công thức cho hai và ba tập

Với hai tập hữu hạn $A,B$,

$$
|A\cup B|=|A|+|B|-|A\cap B|.
$$

Với ba tập $A,B,C$,

$$
|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.
$$

**Giải thích**: Một phần tử nằm trong đúng một tập được đếm đúng một lần; nằm trong hai tập thì bị cộng hai lần rồi trừ một lần; nằm trong ba tập thì bị cộng ba lần, trừ ba lần, rồi cộng lại một lần.

## 2. Công thức tổng quát

Cho các tập $A_1,\ldots,A_n$, ta có

$$
\left|\bigcup_{i=1}^{n}A_i\right|
=\sum_{\emptyset\neq I\subseteq\{1,\ldots,n\}}(-1)^{|I|+1}\left|\bigcap_{i\in I}A_i\right|.
$$


**Chứng minh bằng đếm số lần**: Xét một phần tử thuộc đúng $r$ tập. Trong tổng trên, nó được tính

$$
\binom{r}{1}-\binom{r}{2}+\binom{r}{3}-\cdots+(-1)^{r+1}\binom{r}{r}=1.
$$

Do đó mỗi phần tử trong hợp được đếm đúng một lần.

<div class="content-box theorem-box" markdown="1">
**Quy tắc nhớ**: Dấu xen kẽ theo kích thước giao: tập đơn cộng, giao đôi trừ, giao ba cộng, rồi tiếp tục như vậy.
</div>

## 3. Dạng bù

Thay vì đếm phần hợp trực tiếp, ta thường đếm số phần tử **không vi phạm điều kiện nào** bằng cách lấy tổng không gian mẫu trừ đi hợp của các tập vi phạm.

**Ví dụ**: Số chuỗi nhị phân độ dài 8 có ít nhất một bit 0 và ít nhất một bit 1 là

$$
2^8-2=254.
$$

## 4. Ví dụ với chia hết

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Đếm các số từ 1 đến 100 chia hết cho 2 hoặc 5.

Gọi $A$ là tập số chia hết cho 2, $B$ là tập số chia hết cho 5. Khi đó

$$
|A|=50,\quad |B|=20,\quad |A\cap B|=10.
$$

Vậy

$$
|A\cup B|=50+20-10=60.
$$

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Công cụ cho phép bật/tắt ba tập trong sơ đồ Venn và hiển thị số lần mỗi vùng được cộng hoặc trừ trong công thức.
<div data-demo="venn-ie-three-sets"></div>
</div>
<script src="{{ '/public/js/venn-ie-three-sets.js' | relative_url }}"></script>

## 5. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Không dừng ở giao đôi khi có nhiều hơn hai tập.
- Phải xác định rõ không gian nền trước khi dùng dạng bù.
- Giao của các tập chia hết phải dùng bội chung nhỏ nhất.
- Công thức bao hàm-loại trừ là công thức đếm, không phải xác suất riêng lẻ.
</div>

## 6. Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Nguyên lý này xuất hiện trong sàng số nguyên tố, đếm mật khẩu thỏa ràng buộc, phân tích truy vấn cơ sở dữ liệu nhiều điều kiện, và đếm cấu hình cấm trong tự động hữu hạn. Trong lý thuyết độ phức tạp, nguyên lý bù trừ còn hỗ trợ đếm các đối tượng tránh một tập mẫu con nhất định.

```python
from math import lcm

def divisible_by_any(n, divisors):
    total = 0
    from itertools import combinations
    for r in range(1, len(divisors) + 1):
        for subset in combinations(divisors, r):
            term = n // lcm(*subset)
            total += term if r % 2 else -term
    return total

print(divisible_by_any(100, [2, 5]))
```

## Bài tập thực hành

### Bài tập 1

Một lớp có 40 sinh viên học Python, 35 học C++, 20 học cả hai. Có bao nhiêu sinh viên học ít nhất một ngôn ngữ?

<details>
<summary>Đáp án</summary>

$$
40+35-20=55.
$$

</details>

### Bài tập 2

Có bao nhiêu số từ 1 đến 200 chia hết cho 3 hoặc 4 hoặc 5?

<details>
<summary>Đáp án</summary>

$$
\begin{aligned}
&\lfloor200/3\rfloor+\lfloor200/4\rfloor+\lfloor200/5\rfloor \\
&-\lfloor200/12\rfloor-\lfloor200/15\rfloor-\lfloor200/20\rfloor \\
&+\lfloor200/60\rfloor=66+50+40-16-13-10+3=120.
\end{aligned}
$$

</details>

## Tóm tắt

- Bao hàm - loại trừ sửa lỗi đếm trùng trong hợp của nhiều tập.
- Dấu của công thức luân phiên theo kích thước giao.
- Dạng bù thường cho lời giải ngắn và đẹp hơn.
- Công thức này có vai trò trung tâm trong đếm, xác suất và thuật toán.
