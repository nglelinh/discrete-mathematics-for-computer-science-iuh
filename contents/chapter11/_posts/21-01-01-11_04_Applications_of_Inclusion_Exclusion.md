---

layout: post
title: "Ứng dụng của Nguyên lý Bao hàm - Loại trừ"
categories: chapter11
date: 2021-01-01
order: 4
required: false
lang: vi
excerpt: "Ở mục trước chúng ta đã chứng minh công thức bao hàm–loại trừ tổng quát. Mục này áp dụng nguyên lý vào các bài toán cổ điển: sàng Legendre, hàm Euler , số…"
---

Ở mục trước chúng ta đã chứng minh công thức bao hàm–loại trừ tổng quát. Mục này áp dụng nguyên lý vào các bài toán cổ điển: **sàng Legendre**, **hàm Euler** $$\phi(n)$$, **số toàn ánh**, **derangement**, và đếm cấu hình có ràng buộc (tô màu). Phần then chốt thường không nằm ở phép cộng trừ mà ở **mô hình hóa** đúng tập cần đếm và các giao $$A_i \cap A_j$$; sau khi xác định được các tập con, công thức còn lại là thay số theo khuôn đã học.

![Ứng dụng bao hàm–loại trừ](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="11.16">Sàng Legendre và hàm Euler đều dùng cùng khuôn: cộng, trừ giao, cộng lại giao cao hơn.</p>
![Phân tích thừa số nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/PrimeDecompositionExample.svg)

<p class="textbook-figure-caption" data-figure="11.17">Hàm $\phi(n)$ loại các số chia hết cho từng thừa số nguyên tố của $n$.</p>
![Cấu trúc số nguyên](/discrete-mathematics-for-computer-science-iuh/img/course/Euler_diagram_of_number_sets.svg)

<p class="textbook-figure-caption" data-figure="11.18">Đếm số nguyên tố cùng nhau, số toàn ánh và derangement đều là bài toán đếm trên tập số.</p>
![Đếm cấu hình có ràng buộc](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="11.19">Bài toán tô màu: mỗi vi phạm là một tập con — bao hàm–loại trừ đếm cách tô hợp lệ.</p>
![Ánh xạ và đếm](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="11.20">Số toàn ánh đếm ánh xạ không bỏ sót giá trị đích — ứng dụng trong phân bố và hashing.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** bao hàm–loại trừ vào sàng Legendre và hàm Euler $$\phi(n)$$.
- **Tính** số toàn ánh và số derangement bằng công thức IE.
- **Mô hình hóa** bài toán tô màu / ràng buộc thành hợp các tập vi phạm.

**Từ khóa**: sàng Legendre, hàm Euler, toàn ánh (surjection), derangement, tô màu đồ thị.
</div>

## Sàng Legendre và đếm số nguyên tố

Để đếm số nguyên tố không vượt quá $N$, ta đếm số số bị chia hết bởi ít nhất một số nguyên tố nhỏ hơn hoặc bằng $\sqrt N$, rồi loại bỏ chúng khỏi tập ứng viên. Ý tưởng này không thay thế sàng Eratosthenes trong tính toán thực tế, nhưng minh họa rất rõ cách bao hàm - loại trừ hoạt động.

<div class="textbook-example" markdown="1">
**Ví dụ**: Với $N=30$, các số nguyên tố không vượt quá $\sqrt{30}$ là 2, 3, 5. Đếm các số chia hết cho ít nhất một trong 2,3,5 rồi điều chỉnh để không loại nhầm chính 2,3,5.
</div>


## 2. Hàm phi Euler

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $\phi(n)$ là số các số nguyên dương không vượt quá $n$ và nguyên tố cùng nhau với $n$.
</div>


Nếu

<div class="textbook-equation" markdown="1">
$$
n=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
thì

<div class="textbook-equation" markdown="1">
$$
\phi(n)=n\prod_{i=1}^{k}\left(1-\frac{1}{p_i}\right).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ý tưởng chứng minh**: Đếm các số từ 1 đến $n$, rồi loại các số chia hết cho từng $p_i$ bằng bao hàm - loại trừ.

## 3. Số toàn ánh

Số ánh xạ toàn ánh từ một tập $m$ phần tử sang một tập $n$ phần tử có thể đếm bằng bao hàm - loại trừ:

<div class="textbook-equation" markdown="1">
$$
\text{Surj}(m,n)=\sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Trực giác**: Bắt đầu từ tất cả ánh xạ có $n^m$ cách. Trừ các ánh xạ bỏ sót ít nhất một giá trị đích. Có $\binom{n}{1}(n-1)^m$ ánh xạ bỏ sót một giá trị, cộng lại phần bỏ sót hai giá trị, và cứ tiếp tục như vậy.

## 4. Hoán vị không điểm cố định

Một hoán vị của $n$ phần tử không có điểm cố định gọi là **derangement**. Số derangement ký hiệu $!n$ và có công thức

<div class="textbook-equation" markdown="1">
$$
!n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đây là kết quả kinh điển của bao hàm - loại trừ: bắt đầu từ $n!$ hoán vị, trừ hoán vị cố định ít nhất một vị trí, cộng lại hoán vị cố định ít nhất hai vị trí, v.v.

## 5. Ứng dụng trong tô màu và ràng buộc

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Phần này liên hệ khái niệm toán học với bài toán thực tế trong lập trình và hệ thống.

Trong bài toán tô màu, ta thường cần đếm số cách gán màu sao cho các điều kiện cấm không xảy ra. Gọi $A_i$ là tập cách tô vi phạm cạnh thứ $i$. Số cách tô hợp lệ là tổng số cách tô trừ đi hợp các vi phạm, tức là dùng bao hàm - loại trừ.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học chọn số phần tử miền nguồn và miền đích. Công cụ hiển thị số toàn ánh bằng cách trừ các hàm bỏ sót giá trị đích.
<div data-demo="surjection-counter"></div>
</div>
<script src="{{ '/public/js/surjection-counter.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Tính $$\phi(12)$$ bằng công thức $$n \prod(1 - 1/p_i)$$.

<details>
<summary>Đáp án</summary>

$$12 = 2^2 \cdot 3$$. $$\phi(12) = 12(1 - 1/2)(1 - 1/3) = 12 \cdot 1/2 \cdot 2/3 = 4$$.

</details>

### Bài tập 2

Có bao nhiêu ánh xạ toàn ánh từ tập 3 phần tử sang tập 2 phần tử?

<details>
<summary>Đáp án</summary>

$$\text{Surj}(3,2) = 2^3 - \binom{2}{1}1^3 = 8 - 2 = 6$$ (hoặc công thức tổng: $$2^3 - 2\cdot 1^3 = 6$$).

</details>

### Bài tập 3

Tính $$!4$$ (số derangement trên 4 phần tử).

<details>
<summary>Đáp án</summary>

$$!4 = 4!(1 - 1 + 1/2 - 1/6 + 1/24) = 24 \cdot 9/24 = 9$$.

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Sàng Legendre**: loại bội của các số nguyên tố nhỏ — minh họa bao hàm–loại trừ trên tập số.
- **Hàm Euler** $$\phi(n)$$: $$\phi(n) = n \prod (1 - 1/p_i)$$ — chứng minh bằng loại các số chia hết cho $$p_i$$.
- **Số toàn ánh**: $$\text{Surj}(m,n) = \sum_{k=0}^{n} (-1)^k \binom{n}{k}(n-k)^m$$.
- **Derangement** $$!n$$: $$!n = n! \sum_{k=0}^{n} (-1)^k/k!$$.
- **Tô màu / ràng buộc**: đếm cấu hình hợp lệ = tổng không gian trừ hợp các vi phạm.

Trong bài tiếp theo, chúng ta tổng hợp **hàm sinh** trong phép đếm, xác suất và lý thuyết mã hóa.
