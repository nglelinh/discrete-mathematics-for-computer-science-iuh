---

layout: post
title: "Hoán vị và Tổ hợp Mở rộng"
categories: chapter07
date: 2021-01-01
order: 5
required: false
lang: en
excerpt: "Mở rộng phép đếm sang tổ hợp có lặp (stars and bars), phương trình nghiệm nguyên có ràng buộc, hoán vị đa tập và hệ số đa thức."
---

Ở mục trước, chúng ta đã học hệ số nhị thức và các đồng nhất thức tổ hợp. Mục này mở rộng sang **hoán vị và tổ hợp tổng quát** để xử lý những bài toán có yếu tố lặp, có các phần tử giống nhau hoặc đi kèm ràng buộc bổ sung.

Trong thực tế, các đối tượng không phải lúc nào cũng hoàn toàn phân biệt: có khi một loại phần tử được chọn nhiều lần, có khi nhiều phần tử trong tập hợp giống hệt nhau, hoặc số lượng phân phối phải thỏa mãn cận dưới và cận trên. Điểm mấu chốt không nằm ở việc ghi nhớ công thức dài, mà ở chỗ nhận diện chính xác mô hình bài toán.

## Tổ hợp có lặp

**Bài toán**: Có $$n$$ loại đồ vật khác nhau, mỗi loại có số lượng không giới hạn. Hỏi có bao nhiêu cách chọn $$r$$ đồ vật mà không xét thứ tự?

<div class="textbook-theorem" markdown="1">
**Định lý**: Số tổ hợp có lặp chập $$r$$ từ $$n$$ loại là:
</div>

<div class="textbook-equation" markdown="1">
$$
\binom{n+r-1}{r}=\binom{n+r-1}{n-1}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
![Tổ hợp có lặp — chọn r đồ vật từ n loại](/discrete-mathematics-for-computer-science-iuh/img/course/combination_with_repetition.svg)

<p class="textbook-figure-caption" data-figure="7.21">Tổ hợp có lặp — mỗi cách chọn được xác định bởi bộ số lượng từng loại $$(x_1,\ldots,x_n)$$, không xét thứ tự và cho phép lặp.</p>

### Video ngắn: Sao và vạch

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/stars-and-bars.mp4"></video>
</div>

Video dài khoảng 2 phút 15 giây, minh họa bài toán chọn 5 chiếc bánh từ 3 loại bằng dãy 5 ngôi sao và 2 vạch ngăn, đếm số cách bằng việc chọn 2 trong 7 vị trí cho vạch ($$\binom{7}{2} = 21$$, liệt kê đủ 21 dãy), tổng quát thành công thức $$\binom{r+n-1}{n-1}$$ qua ví dụ $$x_1+x_2+x_3+x_4 = 10$$, xử lý ràng buộc dưới bằng cách đổi biến và ràng buộc trên bằng nguyên lý bù trừ ($$66 - 63 + 3 = 6$$).

### Phương pháp Stars and Bars (Sao và vạch)

Ta biểu diễn $$r$$ đồ vật bằng $$r$$ ngôi sao và dùng $$n-1$$ vạch ngăn để chia chúng thành $$n$$ nhóm, mỗi nhóm tương ứng với số đồ vật thuộc một loại.

<div class="textbook-example" markdown="1">
**Ví dụ**: Chọn 5 chiếc bánh từ 3 loại. Cấu hình

```text
**|***|
```

biểu thị việc chọn 2 bánh loại 1, 3 bánh loại 2 và 0 bánh loại 3. Vì có tổng cộng $$5$$ ngôi sao và $$2$$ vạch ngăn nên số cách chọn là:

<div class="textbook-equation" markdown="1">
$$
\binom{7}{2}=21.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh (song ánh)** gồm hai bước:

**Bước 1. Tương ứng giữa cách chọn và bộ đếm.** Mỗi cách chọn $$r$$ đồ vật từ $$n$$ loại (không xét thứ tự, cho phép lặp) tương ứng duy nhất với một bộ số nguyên không âm

<div class="textbook-equation" markdown="1">
$$
(x_1,x_2,\ldots,x_n),\qquad x_1+x_2+\cdots+x_n=r,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó $$x_i$$ là số đồ vật thuộc **loại $$i$$** được chọn. Ngược lại, mỗi bộ $$(x_1,\ldots,x_n)$$ cũng xác định đúng một cách chọn. Do đó, bài toán quy về đếm số bộ nghiệm như vậy.

**Bước 2. Mã hóa bằng sao và vạch.** Với mỗi bộ $$(x_1,\ldots,x_n)$$, ta viết liên tiếp $$x_1$$ ngôi sao, một vạch, $$x_2$$ ngôi sao, một vạch, …, đến $$x_n$$ ngôi sao. Chuỗi thu được dài đúng $$r+n-1$$ ký hiệu, gồm $$r$$ ngôi sao và $$n-1$$ vạch.

Hai chuỗi khác nhau tương ứng với hai bộ $$(x_1,\ldots,x_n)$$ khác nhau, và mọi chuỗi hợp lệ đều cho ra một bộ nghiệm duy nhất. Vậy số cách chọn bằng số cách chọn vị trí cho $$n-1$$ vạch trong tổng số $$r+n-1$$ vị trí:

<div class="textbook-equation" markdown="1">
$$
\binom{r+n-1}{n-1}=\binom{r+n-1}{r}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
∎
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Nhận xét**: Công thức $$\binom{n+r-1}{r}$$ **khác** với $$\binom{n}{r}$$. Khi $$r>n$$, tổ hợp không lặp bằng $$0$$, nhưng tổ hợp có lặp vẫn dương vì ta được phép chọn nhiều đồ vật thuộc cùng một loại.
</div>

![Phương pháp stars and bars](/discrete-mathematics-for-computer-science-iuh/img/course/stars_and_bars.svg)

<p class="textbook-figure-caption" data-figure="7.22">Mỗi chuỗi sao–vạch tương ứng với một phân phối $$(x_1,x_2,x_3)$$; tổng số cách bằng $$\binom{r+n-1}{n-1}$$.</p>
<div class="interactive-tool" data-demo="stars-bars-visualizer" markdown="1">
**Demo tương tác**: Dùng thanh kéo để chọn $$n$$ và $$r$$, công cụ sẽ sinh các chuỗi sao–vạch tương ứng và chuyển từng chuỗi thành bộ nghiệm $$(x_1,\ldots,x_n)$$.
</div>

<script src="{{ '/public/js/stars-bars-visualizer.js' | relative_url }}"></script>

## Phương trình nghiệm nguyên không âm

Số nghiệm nguyên không âm của phương trình

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
**Chứng minh**: Theo Bước 1 ở mục trên, mỗi nghiệm nguyên không âm $$(x_1,\ldots,x_n)$$ của phương trình tương ứng một–một với một cách chọn $$r$$ đồ vật từ $$n$$ loại, nên số nghiệm bằng đúng số tổ hợp có lặp đã chứng minh. ∎

<div class="textbook-example" markdown="1">
**Ví dụ**: Số nghiệm nguyên không âm của phương trình $$x_1+x_2+x_3+x_4=10$$ là:

<div class="textbook-equation" markdown="1">
$$
\binom{10+4-1}{4-1}=\binom{13}{3}=286.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

### Ràng buộc dưới

Nếu các biến có cận dưới $$x_i\ge a_i$$, ta đổi biến $$y_i=x_i-a_i\ge 0$$ để đưa về phương trình:

<div class="textbook-equation" markdown="1">
$$
y_1+\cdots+y_n=r-(a_1+\cdots+a_n).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh (song ánh)**: Đặt $$y_i=x_i-a_i$$. Khi đó $$x_i\ge a_i$$ khi và chỉ khi $$y_i\ge 0$$, đồng thời:

<div class="textbook-equation" markdown="1">
$$
\sum_{i=1}^{n} y_i=\sum_{i=1}^{n}(x_i-a_i)=r-\sum_{i=1}^{n}a_i.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ánh xạ $$(x_1,\ldots,x_n)\mapsto(y_1,\ldots,y_n)$$ là một song ánh giữa tập nghiệm có ràng buộc dưới và tập nghiệm nguyên không âm của phương trình mới. Số nghiệm bằng $$\binom{n+r-(a_1+\cdots+a_n)-1}{n-1}$$ nếu vế phải không âm; nếu $$r<a_1+\cdots+a_n$$ thì phương trình vô nghiệm. ∎

<div class="textbook-example" markdown="1">
**Ví dụ**: Số nghiệm nguyên của $$x_1+x_2+x_3=12$$ với $$x_1\ge2, x_2\ge1, x_3\ge4$$ bằng số nghiệm nguyên không âm của $$y_1+y_2+y_3=5$$, tức $$\binom{7}{2}=21$$.
</div>

## Hoán vị của đa tập

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **đa tập** (multiset) cho phép phần tử xuất hiện nhiều lần. Nếu có $$n$$ đối tượng gồm $$k$$ loại, trong đó loại 1 lặp $$n_1$$ lần, loại 2 lặp $$n_2$$ lần, …, loại $$k$$ lặp $$n_k$$ lần (với $$n_1+\cdots+n_k=n$$), thì số hoán vị phân biệt là:
</div>

<div class="textbook-equation" markdown="1">
$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh tổ hợp**: Tạm thời **đánh nhãn** các phần tử giống nhau để xem chúng như phân biệt (ví dụ $$S_1, S_2, S_3, S_4$$ thay cho bốn chữ S giống nhau). Khi đó có $$n!$$ cách sắp xếp toàn bộ $$n$$ vị trí.

Tuy nhiên, mỗi hoán vị phân biệt của đa tập (khi bỏ nhãn) tương ứng với đúng $$n_1!\,n_2!\cdots n_k!$$ cách sắp xếp có nhãn, vì việc hoán đổi nội bộ các phần tử cùng loại không tạo ra cấu hình mới. Do đó mỗi hoán vị thực sự đã bị đếm lặp $$n_1!n_2!\cdots n_k!$$ lần trong $$n!$$. Chia cho hệ số trùng lặp này, ta thu được:

<div class="textbook-equation" markdown="1">
$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
∎

![Hoán vị của đa tập — MISSISSIPPI](/discrete-mathematics-for-computer-science-iuh/img/course/multiset_permutation.svg)

<p class="textbook-figure-caption" data-figure="7.23">Hoán vị đa tập — việc đổi chỗ các chữ cùng loại (I, S, …) không tạo từ mới, nên ta chia $$n!$$ cho $$n_1!\cdots n_k!$$.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Từ `MISSISSIPPI` gồm 11 chữ cái: M xuất hiện 1 lần, I xuất hiện 4 lần, S xuất hiện 4 lần và P xuất hiện 2 lần. Số hoán vị phân biệt là:

<div class="textbook-equation" markdown="1">
$$
\frac{11!}{1!4!4!2!}=34650.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Lý do phải chia**: Nếu tạm phân biệt các chữ S thành $$S_1,S_2,S_3,S_4$$ thì có $$11!$$ cách xếp, nhưng đổi chỗ các chữ S không tạo từ mới nên mỗi từ bị đếm lặp $$4!$$ lần do S, $$4!$$ lần do I và $$2!$$ lần do P.
</div>

## Hệ số đa thức

Định lý nhị thức có thể mở rộng cho tổng của nhiều biến:

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
Các hệ số này được gọi là **hệ số đa thức** (multinomial coefficients).

<div class="textbook-proof" markdown="1">
**Chứng minh tổ hợp**: Khai triển tích gồm $$n$$ ngoặc:

<div class="textbook-equation" markdown="1">
$$
(x_1+x_2+\cdots+x_m)^n=(x_1+x_2+\cdots+x_m)(x_1+x_2+\cdots+x_m)\cdots(x_1+x_2+\cdots+x_m).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mỗi hạng tử thu được bằng cách chọn một biến từ mỗi ngoặc rồi nhân lại. Để nhận hạng tử $$x_1^{k_1}x_2^{k_2}\cdots x_m^{k_m}$$ với $$k_1+\cdots+k_m=n$$, ta phải chọn đúng $$k_1$$ ngoặc lấy $$x_1$$, $$k_2$$ ngoặc lấy $$x_2$$, …, và $$k_m$$ ngoặc lấy $$x_m$$. Số cách chọn chính là số hoán vị của đa tập gồm $$n$$ bước chọn, trong đó có $$k_i$$ bước cùng lấy $$x_i$$:

<div class="textbook-equation" markdown="1">
$$
\binom{n}{k_1,k_2,\ldots,k_m}=\frac{n!}{k_1!k_2!\cdots k_m!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Ý nghĩa đếm khác**: $$\binom{n}{k_1,\ldots,k_m}$$ cũng là số cách chia $$n$$ đối tượng **phân biệt** vào $$m$$ nhóm có nhãn, sao cho nhóm thứ $$i$$ nhận đúng $$k_i$$ phần tử.

![Hệ số đa thức — chia nhóm có nhãn](/discrete-mathematics-for-computer-science-iuh/img/course/multinomial_partition.svg)

<p class="textbook-figure-caption" data-figure="7.24">Hệ số đa thức $$\binom{n}{k_1,\ldots,k_m}$$ đếm số cách chia $$n$$ đối tượng phân biệt vào $$m$$ nhóm có kích thước cho trước.</p>
## Ràng buộc trên và nguyên lý bù trừ

Khi bài toán yêu cầu thêm cận trên $$0\le x_i\le b_i$$, phương pháp sao và vạch đơn thuần không còn đủ. Ta đếm toàn bộ nghiệm nguyên không âm rồi dùng nguyên lý bù trừ để loại bỏ các nghiệm vi phạm $$x_i\ge b_i+1$$.

<div class="textbook-proof" markdown="1">
**Chứng minh ý tưởng**: Gọi $$U$$ là tập tất cả các nghiệm nguyên không âm của $$x_1+\cdots+x_n=r$$, và $$A_i$$ là tập các nghiệm thỏa $$x_i\ge b_i+1$$. Tập nghiệm hợp lệ là $$U\setminus(A_1\cup\cdots\cup A_n)$$, nên:

<div class="textbook-equation" markdown="1">
$$
|U\setminus(A_1\cup\cdots\cup A_n)|=|U|-|A_1\cup\cdots\cup A_n|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với mỗi tập $$A_i$$, đổi biến $$x_i'=x_i-(b_i+1)\ge 0$$ đưa bài toán về đếm nghiệm không âm với tổng giảm đi $$b_i+1$$ (lại giải bằng sao và vạch). Các phần giao $$A_i\cap A_j$$ được xử lý tương tự bằng cách trừ đồng thời ở nhiều biến, sau đó áp dụng công thức bù trừ cho $$\vert A_1\cup\cdots\cup A_n\vert $$ (xem bài `07_03`).
</div>

![Bù trừ khi có ràng buộc trên](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="7.25">Loại bỏ các nghiệm vi phạm $$x_i\ge b_i+1$$ bằng nguyên lý bù trừ (bài `07_03`).</p>
<div class="textbook-example" markdown="1">
**Ví dụ**: Tìm số nghiệm nguyên của $$x_1+x_2+x_3=10$$ thỏa $$0\le x_i\le 4$$.

Tổng số nghiệm không âm là $$\binom{12}{2}=66$$. Gọi $$A_i$$ là tập nghiệm có $$x_i\ge5$$. Đặt $$x_i'=x_i-5$$, mỗi $$A_i$$ có $$\binom{7}{2}=21$$ nghiệm. Mỗi giao đôi (chẳng hạn $$x_1,x_2\ge5$$) còn tổng bằng $$0$$ nên chỉ có $$1$$ nghiệm. Giao ba bằng rỗng vì $$5+5+5 > 10$$. Do đó số nghiệm hợp lệ là:

<div class="textbook-equation" markdown="1">
$$
66-3\cdot 21+3\cdot 1=6.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
---
</div>

### Minh hoạ tương tác

Minh hoạ bài toán "sao và vạch": chia $$k$$ vật giống nhau vào $$n$$ hộp phân biệt và đối chiếu với công thức tổ hợp có lặp.

<div class="interactive-demo" markdown="1">
<div data-demo="counting-explainer" data-tab="stars"></div>
</div>
<script src="{{ '/public/js/explainers/counting-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Có bao nhiêu cách chọn 6 viên kẹo từ 4 loại kẹo khác nhau (không xét thứ tự, cho phép chọn trùng loại)?

<details>
<summary>Đáp án</summary>

$$\binom{4+6-1}{6} = \binom{9}{6} = 84$$.

</details>

### Bài tập 2

Sắp xếp các chữ cái của từ `MISSISSIPPI`. Có bao nhiêu hoán vị phân biệt?

<details>
<summary>Đáp án</summary>

$$11! / (4! \cdot 4! \cdot 2!) = 34650$$.

</details>

### Bài tập 3

Tìm số nghiệm nguyên không âm của phương trình $$x_1 + x_2 + x_3 = 10$$ thỏa mãn $$x_i \le 4$$ với mọi $$i$$.

<details>
<summary>Đáp án</summary>

Tổng số nghiệm không ràng buộc: $$\binom{12}{2} = 66$$. Áp dụng nguyên lý bù trừ: $$66 - 3\cdot 21 + 3\cdot 1 = 6$$.

</details>

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt

- **Tổ hợp có lặp**: chọn $$r$$ đồ vật từ $$n$$ loại (số lượng mỗi loại không giới hạn) có $$\binom{n+r-1}{r}$$ cách, chứng minh qua phương pháp sao và vạch (stars and bars).
- **Hoán vị đa tập**: sắp xếp $$n$$ đối tượng gồm $$k$$ loại với số lượng $$n_1, \ldots, n_k$$ cho $$\frac{n!}{n_1! n_2! \cdots n_k!}$$ cách.
- **Phân phối có ràng buộc**: xử lý cận dưới bằng phép đổi biến và cận trên bằng nguyên lý bù trừ.
- **Ứng dụng trong Khoa học Máy tính**: thiết kế mật khẩu, cấp phát tài nguyên, mã hóa và phân tích trạng thái hệ thống.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=ZcSSI6VY1kM">COMBINATIONS with REPETITION - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu tổ hợp có lặp và phương pháp sao và vạch.
- <a href="https://www.youtube.com/watch?v=P37nKjSWv_o">Toán rời rạc 20. Tổ hợp lặp và Chỉnh hợp lặp</a> — TITV, tiếng Việt. Bài giảng tiếng Việt về tổ hợp lặp và chỉnh hợp lặp.
- <a href="https://www.youtube.com/watch?v=je6xyt2UZCw">How many ways are there to reorder the word MISSISSIPPI?  // Choose Formula Example</a> — Dr. Trefor Bazett, tiếng Anh. Minh họa hoán vị của đa tập qua ví dụ từ MISSISSIPPI.
