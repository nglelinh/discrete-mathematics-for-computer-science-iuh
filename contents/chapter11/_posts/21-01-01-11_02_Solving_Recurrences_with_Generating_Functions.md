---
layout: post
title: "Giải Quan hệ Truy hồi bằng Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 2
required: true
lang: vi
---

Khi một quan hệ truy hồi quá khó nhìn ra công thức nghiệm bằng các kỹ thuật quen thuộc, ta có thể đổi góc nhìn. Thay vì bám vào từng số hạng, ta chuyển cả dãy sang một hàm sinh rồi thao tác ở cấp biểu thức.

Hàm sinh mạnh ở chỗ nó đổi một dãy số thành đối tượng đại số dễ thao tác hơn, khá giống cách ta chọn biểu diễn phù hợp để làm bài toán đơn giản đi.
Đây là một ý tưởng rất mạnh: biến bài toán truy hồi trong miền chỉ số thành bài toán đại số trong miền hàm. Nhiều truy hồi vốn rối khi nhìn trực tiếp lại trở nên dễ xử lý hơn hẳn sau bước biến đổi này.

Cách làm đó cũng phản ánh một tư duy quan trọng trong khoa học máy tính, chọn biểu diễn thích hợp để lời giải tự nhiên hơn. Không phải lúc nào ta cũng giải bài toán ở dạng ban đầu của nó.

Trong bài này, chúng ta sẽ học cách dùng hàm sinh để giải truy hồi, từ thiết lập biểu thức ban đầu đến rút ra hệ số và công thức cần tìm.

![Dãy Fibonacci](https://commons.wikimedia.org/wiki/Special:FilePath/Fibonacci_spiral.svg?width=640)

*Hình 11.6: Dãy Fibonacci $F_n=F_{n-1}+F_{n-2}$ — ví dụ kinh điển giải truy hồi bằng hàm sinh.*

![Hàm sinh của dãy Fibonacci](https://commons.wikimedia.org/wiki/Special:FilePath/Contour_graph_of_generating_function_for_Fibonacci_numbers.png?width=640)

*Hình 11.7: Đồ thị contour của hàm sinh Fibonacci — nhân truy hồi với $x^n$ rồi cộng theo $n$ biến quan hệ đệ quy thành phương trình trên $G(x)$.*

![Khai triển chuỗi lũy thừa](https://commons.wikimedia.org/wiki/Special:FilePath/Za_by_Power_Series_Expansion_(n=4).png?width=640)

*Hình 11.8: Khai triển chuỗi lũy thừa — sau khi tìm $G(x)$ dạng phân thức, mở rộng lại để đọc hệ số $a_n$.*

![Dãy hình học](https://commons.wikimedia.org/wiki/Special:FilePath/Geometric_sequence.svg?width=640)

*Hình 11.9: Truy hồi bậc 1 thường cho hàm sinh chứa nhân tử $1/(1-rx)$ — dãy hình học.*

![Cây quyết định phân tích](https://commons.wikimedia.org/wiki/Special:FilePath/Decision_tree.svg?width=640)

*Hình 11.10: Phân tích truy hồi theo từng bước — tư duy hệ thống giống duyệt cây trong thuật toán.*

## 1. Quy trình 4 bước

1. Đặt hàm sinh $G(x)=\sum_{n\ge0}a_nx^n$.
2. Nhân truy hồi với $x^n$ rồi cộng theo $n$ để tạo phương trình cho $G(x)$.
3. Giải đại số để tìm $G(x)$ dưới dạng phân thức.
4. Khai triển lại để đọc hệ số $a_n$.

<div class="content-box theorem-box" markdown="1">
**Mấu chốt**: Dịch chỉ số trong truy hồi tương ứng với nhân thêm $x$ hoặc $x^2$ trong hàm sinh. Nhờ đó, quan hệ đệ quy biến thành phương trình đại số.
</div>

## 2. Ví dụ Fibonacci

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

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
<div data-demo="gf-recurrence-solver"></div>
</div>
<script src="{{ '/public/js/gf-recurrence-solver.js' | relative_url }}"></script>

