---
layout: post
title: "Hoán vị và Tổ hợp Mở rộng"
categories: chapter07
date: 2021-01-01
order: 5
required: false
lang: en
---

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

![Tổ hợp có lặp — chọn r đồ vật từ n loại](/discrete-mathematics-for-computer-science-iuh/img/course/combination_with_repetition.svg)

*Hình 7.21: Tổ hợp có lặp — mỗi cách chọn ghi số lượng từng loại $(x_1,\ldots,x_n)$, không xét thứ tự, cho phép lặp.*

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

**Chứng minh (song ánh)** — gồm hai bước:

**Bước 1. Một cách chọn ↔ một bộ đếm.** Mỗi lần chọn $r$ đồ vật từ $n$ loại (không xét thứ tự, lặp được) tương ứng duy nhất với một bộ số nguyên không âm

$$
(x_1,x_2,\ldots,x_n),\qquad x_1+x_2+\cdots+x_n=r,
$$

trong đó $x_i$ là số đồ vật **loại $i$** được lấy. Ngược lại, mỗi bộ $(x_1,\ldots,x_n)$ xác định đúng một cách chọn. Vậy ta chỉ cần đếm số bộ như vậy.

**Bước 2. Stars and bars.** Với một bộ $(x_1,\ldots,x_n)$ cố định, vẽ $x_1$ sao, một vạch, $x_2$ sao, một vạch, …, $x_n$ sao. Tổng cộng có đúng $r$ sao và $n-1$ vạch, tức một chuỗi dài $r+n-1$ ký hiệu chỉ gồm sao và vạch.

Hai chuỗi khác nhau cho hai bộ $(x_1,\ldots,x_n)$ khác nhau, và mọi chuỗi hợp lệ đều sinh ra một bộ hợp lệ. Do đó số cách chọn bằng số cách sắp $r$ sao và $n-1$ vạch trên $r+n-1$ vị trí, tức số cách chọn vị trí cho các vạch:

$$
\binom{r+n-1}{n-1}=\binom{r+n-1}{r}.
$$

∎

<div class="content-box insight-box" markdown="1">
**Nhận xét**: Công thức $\binom{n+r-1}{r}$ **không** phải $\binom{n}{r}$. Khi $r>n$, tổ hợp thường cho $0$, nhưng tổ hợp có lặp vẫn có thể lớn — vì ta đang đếm **loại**, không phải $n$ vật phân biệt.
</div>

![Phương pháp stars and bars](/discrete-mathematics-for-computer-science-iuh/img/course/stars_and_bars.svg)

*Hình 7.22: Chuỗi sao–vạch tương ứng một phân phối $(x_1,x_2,x_3)$; số cách = $\binom{r+n-1}{n-1}$.*

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

**Chứng minh**: Theo Bước 1 ở mục 1, mỗi nghiệm nguyên không âm $(x_1,\ldots,x_n)$ của phương trình tương ứng một cách chọn $r$ đồ vật từ $n$ loại, và ngược lại. Số nghiệm vì thế bằng số tổ hợp có lặp, đã chứng minh ở trên. ∎

**Ví dụ**: Số nghiệm nguyên không âm của $x_1+x_2+x_3+x_4=10$ là

$$
\binom{10+4-1}{4-1}=\binom{13}{3}=286.
$$

### Ràng buộc dưới

Nếu $x_i\ge a_i$, đặt $y_i=x_i-a_i\ge 0$. Khi đó

$$
y_1+\cdots+y_n=r-(a_1+\cdots+a_n).
$$

**Chứng minh (song ánh)**: Đặt $y_i=x_i-a_i$. Khi đó $x_i\ge a_i$ khi và chỉ khi $y_i\ge 0$, và

$$
\sum_{i=1}^{n} y_i=\sum_{i=1}^{n}(x_i-a_i)=r-\sum_{i=1}^{n}a_i.
$$

Ánh xạ $(x_1,\ldots,x_n)\mapsto(y_1,\ldots,y_n)$ là song ánh giữa tập nghiệm có ràng buộc dưới và tập nghiệm không âm của phương trình mới. Số nghiệm bằng $\binom{n+r-(a_1+\cdots+a_n)-1}{n-1}$ khi vế phải không âm; nếu $r<a_1+\cdots+a_n$ thì không có nghiệm. ∎

**Ví dụ**: Số nghiệm của $x_1+x_2+x_3=12$ với $x_1\ge2,x_2\ge1,x_3\ge4$ là số nghiệm của $y_1+y_2+y_3=5$, bằng $\binom{7}{2}=21$.

## 3. Hoán vị của đa tập

**Định nghĩa**: Một **đa tập** (multiset) cho phép phần tử xuất hiện nhiều lần. Nếu có $n$ đối tượng, trong đó loại 1 lặp $n_1$ lần, loại 2 lặp $n_2$ lần, ..., loại $k$ lặp $n_k$ lần, với $n_1+\cdots+n_k=n$, thì số hoán vị phân biệt là

$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$

**Chứng minh tổ hợp**: Tạm thời **đánh nhãn** các phần tử trùng nhau để chúng trở thành phân biệt — ví dụ $S_1,S_2,S_3,S_4$ thay cho bốn chữ S giống nhau. Khi đó có $n!$ cách sắp xếp toàn bộ $n$ vị trí.

Một hoán vị **thực sự khác nhau** của đa tập (không phân biệt nhãn) tương ứng với đúng $n_1!\,n_2!\cdots n_k!$ cách sắp xếp có nhãn: ta có thể hoán đổi các phần tử cùng loại mà không đổi kết quả. Mỗi hoán vị đa tập vì thế bị đếm thừa $n_1!n_2!\cdots n_k!$ lần trong $n!$.

Chia cho hệ số trùng lặp:

$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$

∎

![Hoán vị của đa tập — MISSISSIPPI](/discrete-mathematics-for-computer-science-iuh/img/course/multiset_permutation.svg)

*Hình 7.23: Hoán vị đa tập — chữ cùng loại (I, S, …) hoán đổi không đổi từ, nên chia $n!$ cho $n_1!\cdots n_k!$.*

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

**Chứng minh tổ hợp**: Khai triển

$$
(x_1+x_2+\cdots+x_m)^n=(x_1+x_2+\cdots+x_m)(x_1+x_2+\cdots+x_m)\cdots(x_1+x_2+\cdots+x_m)
$$

($n$ ngoặc). Mỗi hạng tử trong tích là tích của $n$ lựa chọn, mỗi lựa chọn lấy một biến từ một ngoặc.

Để nhận hạng $x_1^{k_1}x_2^{k_2}\cdots x_m^{k_m}$ với $k_1+\cdots+k_m=n$, ta phải chọn đúng $k_1$ ngoặc lấy $x_1$, đúng $k_2$ ngoặc lấy $x_2$, …, đúng $k_m$ ngoặc lấy $x_m$. Số cách chọn là

$$
\binom{n}{k_1,k_2,\ldots,k_m}=\frac{n!}{k_1!k_2!\cdots k_m!},
$$

vì đây chính là số hoán vị của đa tập gồm $n$ “bước nhân”, trong đó $k_i$ bước giống nhau (cùng lấy $x_i$). ∎

**Ý nghĩa đếm khác**: $\binom{n}{k_1,\ldots,k_m}$ cũng bằng số cách chia $n$ đối tượng **phân biệt** vào $m$ nhóm có nhãn, sao cho nhóm $i$ chứa đúng $k_i$ phần tử.

![Hệ số đa thức — chia nhóm có nhãn](/discrete-mathematics-for-computer-science-iuh/img/course/multinomial_partition.svg)

*Hình 7.24: Hệ số đa thức $\binom{n}{k_1,\ldots,k_m}$ đếm số cách chia $n$ đối tượng phân biệt vào $m$ nhóm có kích thước cố định.*

## 5. Ràng buộc trên và nguyên lý bù trừ

Nếu yêu cầu $0\le x_i\le b_i$, stars and bars đơn thuần chưa đủ. Ta thường đếm tất cả nghiệm không âm rồi loại nghiệm vi phạm $x_i\ge b_i+1$ bằng nguyên lý bù trừ.

**Chứng minh ý tưởng**: Gọi $U$ là tập mọi nghiệm nguyên không âm của $x_1+\cdots+x_n=r$, và $A_i$ là tập nghiệm có $x_i\ge b_i+1$. Nghiệm hợp lệ là $U\setminus(A_1\cup\cdots\cup A_n)$, nên

$$
|U\setminus(A_1\cup\cdots\cup A_n)|=|U|-|A_1\cup\cdots\cup A_n|.
$$

Với mỗi $A_i$, đặt $x_i'=x_i-(b_i+1)\ge 0$; khi đó số nghiệm trong $A_i$ bằng số nghiệm không âm của một phương trình có tổng giảm đi $b_i+1$ — lại là một bài stars and bars. Giao $A_i\cap A_j$ xử lý tương tự bằng cách trừ đồng thời ở hai biến. Áp dụng công thức bù trừ cho $|A_1\cup\cdots\cup A_n|$ (xem bài `07_03`). ∎

![Bù trừ khi có ràng buộc trên](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

*Hình 7.25: Loại các nghiệm vi phạm $x_i\ge b_i+1$ bằng nguyên lý bù trừ (bài `07_03`).*

**Ví dụ**: Số nghiệm của $x_1+x_2+x_3=10$ với $0\le x_i\le 4$.

Tổng nghiệm không âm là $\binom{12}{2}=66$. Gọi $A_i$ là tập nghiệm có $x_i\ge5$. Với $x_i'=x_i-5$, ta có số nghiệm trong mỗi $A_i$ là $\binom{7}{2}=21$. Giao đôi, ví dụ $x_1,x_2\ge5$, còn tổng bằng $0$, có $1$ nghiệm. Không có giao ba. Do đó số hợp lệ là

$$
66-3\cdot 21+3\cdot 1=6.
$$

