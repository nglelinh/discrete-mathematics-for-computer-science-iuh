---

layout: post
title: "Hoán vị và Tổ hợp Mở rộng"
categories: chapter07
date: 2021-01-01
order: 5
required: false
lang: en
excerpt: "Ở mục trước chúng ta đã học hệ số nhị thức và đồng nhất thức. Mục này mở rộng sang hoán vị và tổ hợp tổng quát — xử lý các tình huống có lặp, có phần tử trùng…"
---

Ở mục trước chúng ta đã học hệ số nhị thức và đồng nhất thức. Mục này mở rộng sang **hoán vị và tổ hợp tổng quát** — xử lý các tình huống có lặp, có phần tử trùng hoặc có ràng buộc bổ sung.

Trong bài toán thực tế, các đối tượng không phải lúc nào cũng phân biệt hoàn toàn. Có khi phần tử được phép lặp lại, có khi nhiều phần tử giống nhau, có khi số cách chọn phải tính dưới ràng buộc phân phối. Điểm khó không nằm ở công thức dài mà ở chỗ nhận ra bản chất khác biệt so với bài toán chuẩn.

## 1. Tổ hợp có lặp

**Bài toán**: Có $n$ loại đồ vật, mỗi loại có số lượng không giới hạn. Chọn $r$ đồ vật, không xét thứ tự. Có bao nhiêu cách?

<div class="textbook-theorem" markdown="1">
**Định lý**: Số tổ hợp có lặp chập $r$ từ $n$ loại là
</div>

<div class="textbook-equation" markdown="1">
$$
\binom{n+r-1}{r}=\binom{n+r-1}{n-1}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
![Tổ hợp có lặp — chọn r đồ vật từ n loại](/discrete-mathematics-for-computer-science-iuh/img/course/combination_with_repetition.svg)

<p class="textbook-figure-caption" data-figure="7.21">Tổ hợp có lặp — mỗi cách chọn ghi số lượng từng loại $(x_1,\ldots,x_n)$, không xét thứ tự, cho phép lặp.</p>
### Phương pháp Stars and Bars

Biểu diễn $r$ đồ vật bằng $r$ ngôi sao và dùng $n-1$ vạch để chia thành $n$ nhóm. Mỗi nhóm cho biết số đồ vật thuộc một loại.

<div class="textbook-example" markdown="1">
**Ví dụ**: Chọn 5 chiếc bánh từ 3 loại. Một cấu hình

```text
**|***|
```

nghĩa là chọn 2 bánh loại 1, 3 bánh loại 2, 0 bánh loại 3. Tổng cộng có $5$ sao và $2$ vạch, nên số cách là

<div class="textbook-equation" markdown="1">
$$
\binom{7}{2}=21.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh (song ánh)** — gồm hai bước:

**Bước 1. Một cách chọn ↔ một bộ đếm.** Mỗi lần chọn $r$ đồ vật từ $n$ loại (không xét thứ tự, lặp được) tương ứng duy nhất với một bộ số nguyên không âm

<div class="textbook-equation" markdown="1">
$$
(x_1,x_2,\ldots,x_n),\qquad x_1+x_2+\cdots+x_n=r,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó $x_i$ là số đồ vật **loại $i$** được lấy. Ngược lại, mỗi bộ $(x_1,\ldots,x_n)$ xác định đúng một cách chọn. Vậy chúng ta chỉ cần đếm số bộ như vậy.

**Bước 2. Stars and bars.** Với một bộ $(x_1,\ldots,x_n)$ cố định, vẽ $x_1$ sao, một vạch, $x_2$ sao, một vạch, …, $x_n$ sao. Tổng cộng có đúng $r$ sao và $n-1$ vạch, tức một chuỗi dài $r+n-1$ ký hiệu chỉ gồm sao và vạch.

Hai chuỗi khác nhau cho hai bộ $(x_1,\ldots,x_n)$ khác nhau, và mọi chuỗi hợp lệ đều sinh ra một bộ hợp lệ. Do đó số cách chọn bằng số cách sắp $r$ sao và $n-1$ vạch trên $r+n-1$ vị trí, tức số cách chọn vị trí cho các vạch:

<div class="textbook-equation" markdown="1">
$$
\binom{r+n-1}{n-1}=\binom{r+n-1}{r}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
∎
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Nhận xét**: Công thức $\binom{n+r-1}{r}$ **không** phải $\binom{n}{r}$. Khi $r>n$, tổ hợp thường cho $0$, nhưng tổ hợp có lặp vẫn có thể lớn — vì chúng ta đang đếm **loại**, không phải $n$ vật phân biệt.
</div>

![Phương pháp stars and bars](/discrete-mathematics-for-computer-science-iuh/img/course/stars_and_bars.svg)

<p class="textbook-figure-caption" data-figure="7.22">Chuỗi sao–vạch tương ứng một phân phối $(x_1,x_2,x_3)$; số cách = $\binom{r+n-1}{n-1}$.</p>
<div class="interactive-tool" data-demo="stars-bars-visualizer" markdown="1">
**Demo tương tác đề xuất**: Thanh kéo chọn $n$ và $r$, công cụ sinh các chuỗi sao-vạch tương ứng và chuyển từng chuỗi thành nghiệm $(x_1,\ldots,x_n)$.
</div>

<script src="{{ '/public/js/stars-bars-visualizer.js' | relative_url }}"></script>

## 2. Phương trình nghiệm nguyên không âm

Số nghiệm nguyên không âm của

<div class="textbook-equation" markdown="1">
$$
x_1+x_2+\cdots+x_n=r
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
là

<div class="textbook-equation" markdown="1">
$$
\binom{n+r-1}{n-1}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh**: Theo Bước 1 ở mục 1, mỗi nghiệm nguyên không âm $(x_1,\ldots,x_n)$ của phương trình tương ứng một cách chọn $r$ đồ vật từ $n$ loại, và ngược lại. Số nghiệm vì thế bằng số tổ hợp có lặp, đã chứng minh ở trên. ∎

<div class="textbook-example" markdown="1">
**Ví dụ**: Số nghiệm nguyên không âm của $x_1+x_2+x_3+x_4=10$ là

<div class="textbook-equation" markdown="1">
$$
\binom{10+4-1}{4-1}=\binom{13}{3}=286.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

### Ràng buộc dưới

Nếu $x_i\ge a_i$, đặt $y_i=x_i-a_i\ge 0$. Khi đó

<div class="textbook-equation" markdown="1">
$$
y_1+\cdots+y_n=r-(a_1+\cdots+a_n).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh (song ánh)**: Đặt $y_i=x_i-a_i$. Khi đó $x_i\ge a_i$ khi và chỉ khi $y_i\ge 0$, và

<div class="textbook-equation" markdown="1">
$$
\sum_{i=1}^{n} y_i=\sum_{i=1}^{n}(x_i-a_i)=r-\sum_{i=1}^{n}a_i.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ánh xạ $(x_1,\ldots,x_n)\mapsto(y_1,\ldots,y_n)$ là song ánh giữa tập nghiệm có ràng buộc dưới và tập nghiệm không âm của phương trình mới. Số nghiệm bằng $\binom{n+r-(a_1+\cdots+a_n)-1}{n-1}$ khi vế phải không âm; nếu $r<a_1+\cdots+a_n$ thì không có nghiệm. ∎

<div class="textbook-example" markdown="1">
**Ví dụ**: Số nghiệm của $x_1+x_2+x_3=12$ với $x_1\ge2,x_2\ge1,x_3\ge4$ là số nghiệm của $y_1+y_2+y_3=5$, bằng $\binom{7}{2}=21$.
</div>

## 3. Hoán vị của đa tập

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **đa tập** (multiset) cho phép phần tử xuất hiện nhiều lần. Nếu có $n$ đối tượng, trong đó loại 1 lặp $n_1$ lần, loại 2 lặp $n_2$ lần, ..., loại $k$ lặp $n_k$ lần, với $n_1+\cdots+n_k=n$, thì số hoán vị phân biệt là
</div>

<div class="textbook-equation" markdown="1">
$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh tổ hợp**: Tạm thời **đánh nhãn** các phần tử trùng nhau để chúng trở thành phân biệt — ví dụ $S_1,S_2,S_3,S_4$ thay cho bốn chữ S giống nhau. Khi đó có $n!$ cách sắp xếp toàn bộ $n$ vị trí.

Một hoán vị **thực sự khác nhau** của đa tập (không phân biệt nhãn) tương ứng với đúng $n_1!\,n_2!\cdots n_k!$ cách sắp xếp có nhãn: chúng ta có thể hoán đổi các phần tử cùng loại mà không đổi kết quả. Mỗi hoán vị đa tập vì thế bị đếm thừa $n_1!n_2!\cdots n_k!$ lần trong $n!$.

Chia cho hệ số trùng lặp:

<div class="textbook-equation" markdown="1">
$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
∎

![Hoán vị của đa tập — MISSISSIPPI](/discrete-mathematics-for-computer-science-iuh/img/course/multiset_permutation.svg)

<p class="textbook-figure-caption" data-figure="7.23">Hoán vị đa tập — chữ cùng loại (I, S, …) hoán đổi không đổi từ, nên chia $n!$ cho $n_1!\cdots n_k!$.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Từ `MISSISSIPPI` có 11 chữ cái: M xuất hiện 1, I xuất hiện 4, S xuất hiện 4, P xuất hiện 2. Số hoán vị phân biệt là

<div class="textbook-equation" markdown="1">
$$
\frac{11!}{1!4!4!2!}=34650.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Lý do phải chia**: Nếu tạm xem các chữ S là $S_1,S_2,S_3,S_4$ thì có $11!$ hoán vị. Nhưng hoán đổi các chữ S với nhau không tạo từ mới, nên mỗi từ bị đếm $4!$ lần do S, $4!$ lần do I và $2!$ lần do P.
</div>

## 4. Hệ số đa thức

Định lý nhị thức có bản mở rộng cho nhiều biến:

<div class="textbook-equation" markdown="1">
$$
(x_1+x_2+\cdots+x_m)^n
=\sum_{k_1+\cdots+k_m=n}\binom{n}{k_1,k_2,\ldots,k_m}x_1^{k_1}\cdots x_m^{k_m},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k_1,k_2,\ldots,k_m}=\frac{n!}{k_1!k_2!\cdots k_m!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Các hệ số này gọi là **hệ số đa thức** (multinomial coefficients).

**Chứng minh tổ hợp**: Khai triển

<div class="textbook-equation" markdown="1">
$$
(x_1+x_2+\cdots+x_m)^n=(x_1+x_2+\cdots+x_m)(x_1+x_2+\cdots+x_m)\cdots(x_1+x_2+\cdots+x_m)
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
($n$ ngoặc). Mỗi hạng tử trong tích là tích của $n$ lựa chọn, mỗi lựa chọn lấy một biến từ một ngoặc.

Để nhận hạng $x_1^{k_1}x_2^{k_2}\cdots x_m^{k_m}$ với $k_1+\cdots+k_m=n$, chúng ta phải chọn đúng $k_1$ ngoặc lấy $x_1$, đúng $k_2$ ngoặc lấy $x_2$, …, đúng $k_m$ ngoặc lấy $x_m$. Số cách chọn là

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k_1,k_2,\ldots,k_m}=\frac{n!}{k_1!k_2!\cdots k_m!},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
vì đây chính là số hoán vị của đa tập gồm $n$ “bước nhân”, trong đó $k_i$ bước giống nhau (cùng lấy $x_i$). ∎

**Ý nghĩa đếm khác**: $\binom{n}{k_1,\ldots,k_m}$ cũng bằng số cách chia $n$ đối tượng **phân biệt** vào $m$ nhóm có nhãn, sao cho nhóm $i$ chứa đúng $k_i$ phần tử.

![Hệ số đa thức — chia nhóm có nhãn](/discrete-mathematics-for-computer-science-iuh/img/course/multinomial_partition.svg)

<p class="textbook-figure-caption" data-figure="7.24">Hệ số đa thức $\binom{n}{k_1,\ldots,k_m}$ đếm số cách chia $n$ đối tượng phân biệt vào $m$ nhóm có kích thước cố định.</p>
## 5. Ràng buộc trên và nguyên lý bù trừ

Nếu yêu cầu $0\le x_i\le b_i$, stars and bars đơn thuần chưa đủ. Chúng ta thường đếm tất cả nghiệm không âm rồi loại nghiệm vi phạm $x_i\ge b_i+1$ bằng nguyên lý bù trừ.

**Chứng minh ý tưởng**: Gọi $U$ là tập mọi nghiệm nguyên không âm của $x_1+\cdots+x_n=r$, và $A_i$ là tập nghiệm có $x_i\ge b_i+1$. Nghiệm hợp lệ là $U\setminus(A_1\cup\cdots\cup A_n)$, nên

<div class="textbook-equation" markdown="1">
$$
|U\setminus(A_1\cup\cdots\cup A_n)|=|U|-|A_1\cup\cdots\cup A_n|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với mỗi $A_i$, đặt $x_i'=x_i-(b_i+1)\ge 0$; khi đó số nghiệm trong $A_i$ bằng số nghiệm không âm của một phương trình có tổng giảm đi $b_i+1$ — lại là một bài stars and bars. Giao $A_i\cap A_j$ xử lý tương tự bằng cách trừ đồng thời ở hai biến. Áp dụng công thức bù trừ cho $|A_1\cup\cdots\cup A_n|$ (xem bài `07_03`). ∎

![Bù trừ khi có ràng buộc trên](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="7.25">Loại các nghiệm vi phạm $x_i\ge b_i+1$ bằng nguyên lý bù trừ (bài `07_03`).</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Số nghiệm của $x_1+x_2+x_3=10$ với $0\le x_i\le 4$.

Tổng nghiệm không âm là $\binom{12}{2}=66$. Gọi $A_i$ là tập nghiệm có $x_i\ge5$. Với $x_i'=x_i-5$, chúng ta có số nghiệm trong mỗi $A_i$ là $\binom{7}{2}=21$. Giao đôi, ví dụ $x_1,x_2\ge5$, còn tổng bằng $0$, có $1$ nghiệm. Không có giao ba. Do đó số hợp lệ là

<div class="textbook-equation" markdown="1">
$$
66-3\cdot 21+3\cdot 1=6.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
---
</div>

## Bài tập

### Bài tập 1

Có bao nhiêu cách chọn 6 viên kẹo từ 4 loại (không xét thứ tự, cho phép lặp)?

<details>
<summary>Đáp án</summary>

$$\binom{4+6-1}{6} = \binom{9}{6} = 84$$.

</details>

### Bài tập 2

Sắp xếp chữ MISSISSIPPI. Có bao nhiêu hoán vị khác nhau?

<details>
<summary>Đáp án</summary>

$$11! / (4! \cdot 4! \cdot 2!) = 34650$$.

</details>

### Bài tập 3

Số nghiệm không âm của $$x_1 + x_2 + x_3 = 10$$ với $$x_i \le 4$$ cho mọi $$i$$?

<details>
<summary>Đáp án</summary>

Tổng không ràng buộc: $$\binom{12}{2} = 66$$. IE: $$66 - 3\cdot 21 + 3\cdot 1 = 6$$.

</details>

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt

- **Tổ hợp có lặp**: chọn $$r$$ đồ vật từ $$n$$ loại (không giới hạn số lượng mỗi loại) cho $$\binom{n+r-1}{r}$$ cách; phương pháp stars and bars
- **Hoán vị có lặp**: sắp xếp $$n$$ đối tượng với $$n_i$$ phần tử giống nhau loại $$i$$ cho $$\frac{n!}{n_1! n_2! \cdots n_k!}$$ cách
- **Phân phối vào nhóm**: đếm cách chia đối tượng vào các ô có ràng buộc
- **Ứng dụng CS**: thiết kế mật khẩu, cấp phát tài nguyên, mã hóa và phân tích trạng thái hệ thống
