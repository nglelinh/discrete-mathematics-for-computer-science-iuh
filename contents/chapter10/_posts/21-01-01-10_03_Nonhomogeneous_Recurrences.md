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

Không phải mọi truy hồi đều được xây từ các giá trị trước đó một cách "sạch". Nhiều quá trình còn có thêm nguồn tác động bên ngoài, như chi phí cố định mỗi bước, lượng dữ liệu được bơm thêm, hay số lượng yêu cầu mới phát sinh theo thời gian.


Quan hệ truy hồi cho phép ta mô tả tiến trình theo từng bước, đúng với cách nhiều thuật toán đệ quy và dynamic programming vận hành.
Đó là lúc xuất hiện **quan hệ truy hồi không thuần nhất**. Ngoài phần phụ thuộc vào quá khứ, truy hồi còn có một thành phần bổ sung. Thành phần này làm bài toán phong phú hơn và cũng gần với ứng dụng hơn rất nhiều.

Trong phân tích thuật toán, dạng truy hồi này thường xuất hiện khi mỗi lời gọi còn kèm một lượng công việc phụ thêm. Trong mô hình hệ thống, nó mô tả các quá trình vừa kế thừa trạng thái cũ vừa nhận tác động mới từ môi trường.

Bài học này sẽ giúp chúng ta mở rộng kỹ thuật giải truy hồi sang trường hợp không thuần nhất, rồi dùng chúng để đọc các bài toán ứng dụng thực tế hơn.

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

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

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

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

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
<div data-demo="characteristic-solver"></div>
</div>
<script src="{{ '/public/js/characteristic-solver.js' | relative_url }}"></script>

## 7. Ứng dụng phân tích thuật toán

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

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

