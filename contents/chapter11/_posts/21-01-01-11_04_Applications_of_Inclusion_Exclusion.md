---
layout: post
title: "Ứng dụng của Nguyên lý Bao hàm - Loại trừ"
categories: chapter11
date: 2021-01-01
order: 4
required: false
lang: vi
---

Một nguyên lý chỉ thật sự sống khi nó giải được bài toán cụ thể. Với bao hàm, loại trừ cũng vậy. Sức mạnh của nó lộ rõ nhất khi các điều kiện giao nhau chằng chịt và những cách đếm đơn giản đều dẫn đến sai số.


Hàm sinh mạnh ở chỗ nó đổi một dãy số thành đối tượng đại số dễ thao tác hơn, khá giống cách ta chọn biểu diễn phù hợp để làm bài toán đơn giản đi.
Trong tổ hợp, ta dùng nó để đếm các cấu hình tránh ràng buộc nào đó. Trong xác suất, ta dùng nó để tính khả năng xảy ra ít nhất một biến cố. Trong khoa học máy tính, nó xuất hiện khi phân tích tập bản ghi thỏa nhiều điều kiện hoặc số cấu hình hợp lệ trong hệ thống có ràng buộc chồng lấn.

Phần khó nhất thường không phải là thực hiện phép cộng trừ, mà là mô hình hóa đúng tập cần đếm và giao của các tập con liên quan. Khi làm đúng bước đó, công thức còn lại khá cơ học.

Bài này sẽ tập trung vào các ví dụ ứng dụng để biến một nguyên lý trừu tượng thành công cụ thực chiến trong giải bài toán.

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

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Trong bài toán tô màu, ta thường cần đếm số cách gán màu sao cho các điều kiện cấm không xảy ra. Gọi $A_i$ là tập cách tô vi phạm cạnh thứ $i$. Số cách tô hợp lệ là tổng số cách tô trừ đi hợp các vi phạm, tức là dùng bao hàm - loại trừ.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học chọn số phần tử miền nguồn và miền đích. Công cụ hiển thị số toàn ánh bằng cách trừ các hàm bỏ sót giá trị đích.
<div data-demo="surjection-counter"></div>
</div>
<script src="{{ '/public/js/surjection-counter.js' | relative_url }}"></script>

