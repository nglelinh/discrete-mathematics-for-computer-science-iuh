---
layout: post
title: "Hoán vị và Tổ hợp Mở rộng"
categories: chapter07
date: 2021-01-01
order: 5
required: false
lang: en
---

# Hoán vị và Tổ hợp Mở rộng

Trong bài toán thực tế, các đối tượng không phải lúc nào cũng phân biệt hoàn toàn. Có khi phần tử được phép lặp lại, có khi nhiều phần tử giống nhau, có khi số cách chọn phải tính dưới ràng buộc bổ sung. Lúc đó, các công thức cơ bản của hoán vị và tổ hợp không còn đủ.


Các quy tắc đếm cho ta cách ước lượng số cấu hình có thể xảy ra mà không cần liệt kê hết, đây là kỹ năng rất gần với phân tích thuật toán và kiểm thử.
Phần **mở rộng** này giúp ta xử lý chính những tình huống gần thực tế hơn: chọn có lặp, sắp xếp khi có phần tử trùng, hay phân phối đối tượng vào các nhóm. Đây là những mẫu xuất hiện trong thiết kế mật khẩu, cấp phát tài nguyên, mã hóa và phân tích trạng thái hệ thống.

Điểm khó của các bài toán này không nằm ở công thức dài, mà ở chỗ nhận ra bản chất khác biệt của chúng so với bài toán chuẩn. Một thay đổi nhỏ trong điều kiện có thể làm số cách đếm đổi hoàn toàn.

Trong bài này, chúng ta sẽ mở rộng bộ công cụ tổ hợp đã có để giải những bài toán linh hoạt hơn và gần với ứng dụng hơn.

## 1. Tổ hợp có lặp

**Bài toán**: Có $n$ loại đồ vật, mỗi loại có số lượng không giới hạn. Chọn $r$ đồ vật, không xét thứ tự. Có bao nhiêu cách?

**Định lý**: Số tổ hợp có lặp chập $r$ từ $n$ loại là

$$
\binom{n+r-1}{r}=\binom{n+r-1}{n-1}.
$$

### Phương pháp Stars and Bars

Biểu diễn $r$ đồ vật bằng $r$ ngôi sao và dùng $n-1$ vạch để chia thành $n$ nhóm. Mỗi nhóm cho biết số đồ vật thuộc một loại.

**Ví dụ**: Chọn 5 chiếc bánh từ 3 loại. Một cấu hình

```text
**|***|
```

nghĩa là chọn 2 bánh loại 1, 3 bánh loại 2, 0 bánh loại 3. Tổng cộng có $5$ sao và $2$ vạch, nên số cách là

$$
\binom{7}{2}=21.
$$

**Chứng minh**: Ta sắp xếp $r$ sao và $n-1$ vạch trên một hàng gồm $r+n-1$ vị trí. Chọn vị trí cho các vạch là đủ xác định cấu hình, do đó có $\binom{r+n-1}{n-1}$ cách.

<div class="interactive-tool" data-demo="stars-bars-visualizer" markdown="1">
**Demo tương tác đề xuất**: Thanh kéo chọn $n$ và $r$, công cụ sinh các chuỗi sao-vạch tương ứng và chuyển từng chuỗi thành nghiệm $(x_1,\ldots,x_n)$.
</div>

<script src="{{ '/public/js/stars-bars-visualizer.js' | relative_url }}"></script>

## 2. Phương trình nghiệm nguyên không âm

Số nghiệm nguyên không âm của

$$
x_1+x_2+\cdots+x_n=r
$$

là

$$
\binom{n+r-1}{n-1}.
$$

**Ví dụ**: Số nghiệm nguyên không âm của $x_1+x_2+x_3+x_4=10$ là

$$
\binom{10+4-1}{4-1}=\binom{13}{3}=286.
$$

### Ràng buộc dưới

Nếu $x_i\ge a_i$, đặt $y_i=x_i-a_i\ge 0$. Khi đó

$$
y_1+\cdots+y_n=r-(a_1+\cdots+a_n).
$$

**Ví dụ**: Số nghiệm của $x_1+x_2+x_3=12$ với $x_1\ge2,x_2\ge1,x_3\ge4$ là số nghiệm của $y_1+y_2+y_3=5$, bằng $\binom{7}{2}=21$.

## 3. Hoán vị của đa tập

**Định nghĩa**: Một **đa tập** (multiset) cho phép phần tử xuất hiện nhiều lần. Nếu có $n$ đối tượng, trong đó loại 1 lặp $n_1$ lần, loại 2 lặp $n_2$ lần, ..., loại $k$ lặp $n_k$ lần, với $n_1+\cdots+n_k=n$, thì số hoán vị phân biệt là

$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$

**Ví dụ**: Từ `MISSISSIPPI` có 11 chữ cái: M xuất hiện 1, I xuất hiện 4, S xuất hiện 4, P xuất hiện 2. Số hoán vị phân biệt là

$$
\frac{11!}{1!4!4!2!}=34650.
$$

**Lý do phải chia**: Nếu tạm xem các chữ S là $S_1,S_2,S_3,S_4$ thì có $11!$ hoán vị. Nhưng hoán đổi các chữ S với nhau không tạo từ mới, nên mỗi từ bị đếm $4!$ lần do S, $4!$ lần do I và $2!$ lần do P.

## 4. Hệ số đa thức

Định lý nhị thức có bản mở rộng cho nhiều biến:

$$
(x_1+x_2+\cdots+x_m)^n
=\sum_{k_1+\cdots+k_m=n}\binom{n}{k_1,k_2,\ldots,k_m}x_1^{k_1}\cdots x_m^{k_m},
$$

trong đó

$$
\binom{n}{k_1,k_2,\ldots,k_m}=\frac{n!}{k_1!k_2!\cdots k_m!}.
$$

Các hệ số này gọi là **hệ số đa thức** (multinomial coefficients).

## 5. Ràng buộc trên và nguyên lý bù trừ

Nếu yêu cầu $0\le x_i\le b_i$, stars and bars đơn thuần chưa đủ. Ta thường đếm tất cả nghiệm không âm rồi loại nghiệm vi phạm $x_i\ge b_i+1$ bằng nguyên lý bù trừ.

**Ví dụ**: Số nghiệm của $x_1+x_2+x_3=10$ với $0\le x_i\le 4$.

Tổng nghiệm không âm là $\binom{12}{2}=66$. Gọi $A_i$ là tập nghiệm có $x_i\ge5$. Với $x_i'=x_i-5$, ta có số nghiệm trong mỗi $A_i$ là $\binom{7}{2}=21$. Giao đôi, ví dụ $x_1,x_2\ge5$, còn tổng bằng $0$, có $1$ nghiệm. Không có giao ba. Do đó số hợp lệ là

$$
66-3\cdot 21+3\cdot 1=6.
$$

## 6. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Tổ hợp có lặp không phải là $n^r$; $n^r$ đếm chuỗi có thứ tự.
- Stars and bars áp dụng trực tiếp cho nghiệm không âm, không áp dụng ngay cho nghiệm dương nếu chưa đổi biến.
- Hoán vị đa tập cần chia cho giai thừa của từng nhóm lặp, không chỉ chia cho số loại.
- Ràng buộc trên thường cần bù trừ; không thể chỉ thay $r$ bằng số nhỏ hơn một cách tùy tiện.
</div>

## 7. Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Trong phân tích thuật toán, stars and bars đếm số trạng thái khi phân phối tài nguyên giống nhau vào nhiều tiến trình. Trong học máy, hệ số đa thức xuất hiện trong mô hình phân phối đa thức cho văn bản. Trong kiểm thử, hoán vị đa tập giúp đếm số chuỗi đầu vào khác nhau khi có ký tự lặp. Trong quy hoạch động, hiểu cấu trúc nghiệm nguyên giúp thiết kế trạng thái hiệu quả hơn.

```python
from math import factorial

def multiset_permutations(counts):
    n = sum(counts)
    ans = factorial(n)
    for c in counts:
        ans //= factorial(c)
    return ans

print(multiset_permutations([1, 4, 4, 2]))
```

## Bài tập thực hành

### Bài tập 1: Chọn kẹo

Có 6 loại kẹo, mỗi loại không giới hạn. Có bao nhiêu cách chọn 12 viên kẹo?

<details>
<summary>Đáp án</summary>

Số cách là

$$
\binom{6+12-1}{12}=\binom{17}{12}=\binom{17}{5}=6188.
$$

</details>

### Bài tập 2: Nghiệm dương

Có bao nhiêu nghiệm nguyên dương của $x_1+x_2+x_3+x_4=20$?

<details>
<summary>Đáp án</summary>

Đặt $y_i=x_i-1\ge0$. Khi đó $y_1+y_2+y_3+y_4=16$. Số nghiệm là

$$
\binom{16+4-1}{4-1}=\binom{19}{3}=969.
$$

</details>

### Bài tập 3: Hoán vị đa tập

Có bao nhiêu chuỗi phân biệt tạo từ các chữ cái của `BANANA`?

<details>
<summary>Đáp án</summary>

`BANANA` có 6 chữ cái, A lặp 3 lần, N lặp 2 lần, B lặp 1 lần. Số chuỗi là

$$
\frac{6!}{3!2!1!}=60.
$$

</details>

## Tóm tắt

- **Tổ hợp có lặp** được giải bằng stars and bars: $\binom{n+r-1}{r}$.
- **Nghiệm nguyên không âm** của $x_1+\cdots+x_n=r$ tương ứng với cách phân phối $r$ vật giống nhau vào $n$ hộp.
- **Hoán vị đa tập** chia $n!$ cho giai thừa số lần lặp của từng loại.
- **Hệ số đa thức** mở rộng hệ số nhị thức cho nhiều biến.
- **Ràng buộc trên** thường cần kết hợp stars and bars với nguyên lý bù trừ.

Trong bài tiếp theo, chúng ta sẽ chuyển sang nền tảng của xác suất rời rạc.
