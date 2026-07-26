---
layout: post
title: "Bản đồ Karnaugh và Tối thiểu hóa Trực quan"
categories: chapter13
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "K-map 2–4 biến với thứ tự Gray, tế bào lớn và quy trình 5 bước phủ tối tiểu, don't-care."
---

<div class="textbook-epigraph" markdown="1">

"A Karnaugh map is a truth table rearranged so that adjacency means algebraic cancellation."

<span class="epigraph-attribution">— Tinh thần K-map</span>

</div>

Biến đổi đại số (Mục 13.3) cho phép rút gọn nhiều biểu thức Boolean. Khi số **minterm** tăng, việc nhận diện các cặp hoặc nhóm hạng tử có thể gộp — ví dụ $$xy + x\bar y = x$$ — trở nên khó và dễ bỏ sót.

**Bản đồ Karnaugh** (Karnaugh Map, **K-map**) là cách biểu diễn bảng chân trị trên lưới với các tính chất sau:

- mỗi ô tương ứng một minterm;
- hai ô kề nhau, kể cả hai mép đối diện, khác nhau đúng một biến;
- gộp các ô kề hợp lệ tương đương phép rút gọn đại số trên các minterm đó.

Đối với hàm Boolean từ hai đến bốn biến, phương pháp này cho biểu thức **SOP** (tổng các tích / *Sum of Products*) tối tiểu hai tầng, tương đương hàm ban đầu theo bảng chân trị.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** vai trò của mã Gray trên trục K-map.
- **Xây dựng** K-map 2, 3, 4 biến và điền các ô $$F=1$$.
- **Khoanh nhóm** theo quy tắc lũy thừa của 2, wrap-around và chồng nhóm.
- **Áp dụng** quy trình năm bước: tế bào lớn, cốt yếu, phủ, SOP tối tiểu.
- **Biểu diễn** mỗi nhóm bằng một tích và viết $$F$$.
- **Xử lý** don't-care khi đặc tả cho phép.

**Từ khóa**: K-map, mã Gray, minterm, tế bào lớn, hạng nguyên tố (*prime implicant*), phủ tối tiểu, don't-care.

</div>

## 1. Mã Gray và tính kề trên trục

### 1.1. Thứ tự nhị phân thường

Trên dãy $$00,01,10,11$$, bước từ $$01$$ sang $$10$$ thay đổi đồng thời hai bit. Nếu hai mã đó được đặt kề trên K-map và gộp thành một nhóm, phép gộp không tương ứng việc triệt một biến theo đẳng thức dạng $$xy + x\bar y = x$$.

### 1.2. Mã Gray

**Mã Gray** là thứ tự các xâu bit trong đó hai mã liên tiếp khác nhau đúng một bit. Hệ quả: kề hình học trên lưới trùng với kề Hamming, do đó gộp ô tương ứng rút gọn đại số.

Thứ tự Gray hai bit:

$$
00,\; 01,\; 11,\; 10.
$$

Hai đầu mút $$00$$ và $$10$$ cũng khác nhau một bit, nên mép đối diện của lưới vẫn kề nhau (*wrap-around*). Trục hàng và cột của K-map 2–4 biến được gán theo thứ tự này.

![Nhị phân vs Gray](/discrete-mathematics-for-computer-science-iuh/img/course/Gray_vs_binary.svg)

<p class="textbook-figure-caption" data-figure="13.40">So sánh bước nhị phân thường (đổi hai bit) và mã Gray (đổi một bit).</p>

![Thứ tự Gray 3-bit](/discrete-mathematics-for-computer-science-iuh/img/course/gray_code.svg)

<p class="textbook-figure-caption" data-figure="13.41">Thứ tự Gray ba bit.</p>

## 2. Cấu trúc K-map và quy tắc nhóm

### 2.1. Ba thành phần

| Thành phần | Định nghĩa |
|:---|:---|
| Ô | Một minterm, tương ứng một hàng của bảng chân trị |
| Kề | Hai ô kề (kể cả mép đối diện) khác đúng một biến |
| Gộp | Nhóm các ô kề hợp lệ, tương đương $$xy + x\bar y = x$$ trên tập minterm đó |

### 2.2. Quy tắc khoanh nhóm

1. Chỉ khoanh các ô mang giá trị **1**, hoặc **X** khi có don't-care.  
2. Số ô của mỗi nhóm là lũy thừa của 2: $$1, 2, 4, 8, \ldots$$  
3. Ưu tiên nhóm có lực lượng lớn hơn: mỗi lần gộp đôi triệt thêm một biến trong tích.  
4. Các nhóm được phép giao nhau: một ô **1** có thể thuộc nhiều nhóm.  
5. Mọi ô **1** phải thuộc ít nhất một nhóm. Ô **X** không bắt buộc thuộc nhóm nào.

![Năm quy tắc khoanh nhóm](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_grouping_rules.svg)

<p class="textbook-figure-caption" data-figure="13.42">Quy tắc khoanh nhóm trên K-map.</p>

### 2.3. Tế bào lớn và hạng nguyên tố

**Tế bào lớn** là nhóm lũy thừa của 2 không mở rộng được thêm mà vẫn hợp lệ.

**Hạng nguyên tố** (*prime implicant*) là tích tương ứng tế bào lớn: không còn rút gọn thêm bằng việc gộp minterm.

Một nhóm gồm $$2^{k}$$ ô hợp lệ triệt $$k$$ biến — các biến thay đổi giá trị trên nhóm — và giữ lại các biến không đổi.

## 3. K-map hai biến

Lưới $$2\times 2$$: hàng theo $$x\in\{0,1\}$$, cột theo $$y\in\{0,1\}$$. Bốn ô là bốn minterm $$m_0,\ldots,m_3$$.

![K-map 2 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_2var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.43">K-map hai biến.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1.**  
$$F = xy + x\bar y$$.

Hai ô hàng $$x=1$$ mang **1**. Nhóm hai ô đó: biến $$y$$ thay đổi, $$x$$ cố định bằng **1**, suy ra

$$
F = x = x(y+\bar y).
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.**  
$$A = xy + \bar x y + \bar x\bar y,$$  
tức $$A=1$$ tại $$(x,y)\in\{(0,0),(0,1),(1,1)\}$$.

Hàng $$x=0$$ cho nhóm $$\bar x$$. Cột $$y=1$$ cho nhóm $$y$$. Ô $$(0,1)$$ thuộc cả hai nhóm. Do đó

$$
A = \bar x + y.
$$

Tại $$(1,0)$$: $$A = 0$$, khớp với việc hàng đó không xuất hiện trong SOP ban đầu.

</div>

![K-map 2 biến — ví dụ](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_2var_example.svg)

<p class="textbook-figure-caption" data-figure="13.44">Các minterm 0, 1, 3: $$A=\bar x+y$$.</p>

## 4. K-map ba biến

### 4.1. Sắp xếp lưới

- Hàng: $$(x,y)$$ theo Gray $$00,01,11,10$$.  
- Cột: $$z\in\{0,1\}$$.

Hàng $$10$$ kề hàng $$00$$. Lưới gồm tám minterm.

![K-map 3 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_3var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.45">K-map ba biến: hàng Gray $$(x,y)$$, cột $$z$$.</p>

### 4.2. Đọc nhóm thành tích

Trên một nhóm hợp lệ:

1. biến thay đổi giá trị bị triệt;  
2. biến luôn bằng **1** xuất hiện dưới dạng nguyên;  
3. biến luôn bằng **0** xuất hiện dưới dạng bù.

<div class="textbook-example" markdown="1">

**Ví dụ 1.**  
$$
F = xy\bar z + x\bar y\bar z + \bar x y z + \bar x y\bar z + \bar x\bar y\bar z.
$$

Các minterm theo thứ tự $$xyz$$: $$110,100,011,010,000$$.

Bốn minterm có $$z=0$$ tạo nhóm $$\bar z$$. Hai minterm $$010$$ và $$011$$ tạo nhóm $$\bar x y$$. Vậy

$$
F = \bar z + \bar x y.
$$

| $$(x,y,z)$$ | SOP gốc | $$\bar z+\bar x y$$ |
|:---:|:---:|:---:|
| $$111$$ | 0 | 0 |
| $$011$$ | 1 | 1 |
| $$110$$ | 1 | 1 |

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.**  
$$F=1$$ tại các chỉ số minterm $$0,1,2,5,7$$.

| Nhóm | Minterm | Tích |
|:---|:---|:---|
| Hàng $$xy=00$$ | $$m_0,m_1$$ | $$\bar x\bar y$$ |
| Cột $$z=0$$, hàng $$00$$ và $$01$$ | $$m_0,m_2$$ | $$\bar x\bar z$$ |
| Cột $$z=1$$, hàng $$11$$ và $$10$$ | $$m_7,m_5$$ | $$xz$$ |

$$
F = \bar x\bar y + \bar x\bar z + xz.
$$

Biểu thức này trùng bảng chân trị của tập minterm đã cho.

</div>

![K-map 3 biến — ví dụ](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_3var_example.svg)

<p class="textbook-figure-caption" data-figure="13.46">$$F=\bar x\bar y+\bar x\bar z+xz$$.</p>

## 5. K-map bốn biến

### 5.1. Sắp xếp lưới

Mười sáu ô với:

- hàng $$(x,y)$$: Gray $$00,01,11,10$$;  
- cột $$(z,w)$$: Gray $$00,01,11,10$$.

Chỉ số trong ô, nếu có, là chỉ số minterm $$m_k$$.

![K-map 4 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_4var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.47">K-map bốn biến.</p>

### 5.2. Wrap-around

Do tính tuần hoàn của thứ tự Gray:

- cột ngoài cùng trái kề cột ngoài cùng phải;
- hàng trên cùng kề hàng dưới cùng;
- bốn góc tạo thành một nhóm bốn ô hợp lệ.

![K-map 4 biến — wrap-around](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_4var_wrap.svg)

<p class="textbook-figure-caption" data-figure="13.48">Nhóm bốn góc (wrap-around).</p>

<div class="textbook-example" markdown="1">

**Ví dụ.**  
$$F=1$$ tại các chỉ số $$0,1,2,5,6,7,8,9,10,14$$.

Quy trình: điền lưới; chọn các nhóm lực lượng lớn nhất trước; phủ các ô **1** còn lại bằng nhóm nhỏ hơn; đọc từng nhóm thành tích.

Một phủ thu được là

$$
F = \bar z\bar w + \bar x w + \bar x y z + y z\bar w.
$$

Mỗi phủ hợp lệ phải phủ đúng tập minterm của $$F$$ và không chứa ô mang **0**.

</div>

## 6. Phủ tối tiểu

Bài toán tiếp theo là chọn một họ tế bào lớn phủ mọi ô **1**, không thừa, và cho SOP gọn.

### 6.1. Phủ tập

<div class="textbook-definition" markdown="1">

**Phủ.** Họ $$\mathcal{S}=\{X_1,\ldots,X_n\}$$ phủ tập $$X$$ nếu $$X=\bigcup_i X_i$$.

**Phủ không thừa** (*irredundant cover*): với mọi $$i$$, $$\mathcal{S}\setminus\{X_i\}$$ không còn phủ $$X$$.

</div>

Trên K-map, $$X$$ là tập các ô **1** và mỗi $$X_i$$ là một tế bào lớn.

<div class="textbook-example" markdown="1">

**Ví dụ.** $$X=\{a,b,c,d\}$$, $$A=\{a,b\}$$, $$B=\{c,d\}$$, $$C=\{a,d\}$$, $$D=\{b,c\}$$.

- $$\{A,B,C,D\}$$ là phủ nhưng thừa.  
- $$\{A,B\}$$ và $$\{C,D\}$$ là phủ không thừa.  
- $$\{B,D\}$$ không phủ $$X$$.

</div>

![Phủ tối tiểu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_set_cover.svg)

<p class="textbook-figure-caption" data-figure="13.49">Phủ không thừa trên một họ tập con.</p>

### 6.2. Tế bào cốt yếu

Nếu một ô **1** thuộc đúng một tế bào lớn $$T$$ thì $$T$$ thuộc mọi phủ không thừa. $$T$$ được gọi là tế bào **cốt yếu** (*essential prime implicant*).

![Tế bào lớn cốt yếu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_essential_cell.svg)

<p class="textbook-figure-caption" data-figure="13.50">Ô chỉ thuộc một tế bào lớn xác định tế bào cốt yếu.</p>

### 6.3. Quy trình năm bước

**Quy trình năm bước.**

1. Lập K-map và đánh dấu các ô $$F=1$$ (cùng **X** nếu có).  
2. Liệt kê mọi tế bào lớn.  
3. Chọn mọi tế bào cốt yếu.  
4. Nếu các tế bào cốt yếu chưa phủ hết ô **1**, bổ sung tế bào lớn cho các ô còn lại; loại bỏ các phủ thừa.  
5. Mỗi tế bào trong phủ tương ứng một tích; SOP tối tiểu là tổng (OR) các tích đó. Có thể tồn tại nhiều SOP tối tiểu tương đương về độ phức tạp.

<div class="textbook-example" markdown="1">

**Ví dụ 1.**  
Hai tế bào lớn $$x$$ và $$yz$$ đều cốt yếu và phủ hết các ô **1**. SOP tối tiểu duy nhất:

$$
f = x + yz.
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.**  
Các tế bào cốt yếu: $$\bar x\bar t$$, $$xzt$$, $$\bar z\bar t$$. Một ô **1** còn lại thuộc đúng hai tế bào lớn $$\bar x\bar y z$$ và $$\bar y zt$$. Hai phủ không thừa:

$$
\begin{aligned}
f_1 &= \bar z\bar t + \bar x\bar t + xzt + \bar x\bar y z, \\
f_2 &= \bar z\bar t + \bar x\bar t + xzt + \bar y zt.
\end{aligned}
$$

Cả hai đều là SOP tối tiểu.

</div>

## 7. Don't-care

Nếu đầu ra tại một số vector không được đặc tả, các ô tương ứng được ký **X** trên K-map:

- **X** có thể được xem như **1** để tạo nhóm lớn hơn;  
- **X** không bắt buộc thuộc phủ.

<div class="textbook-example" markdown="1">

**Ví dụ.** Ba biến; $$F=1$$ tại minterm $$0,1,3$$; don't-care tại $$5,7$$.

Coi **X** như **1** cho phép nhóm cả cột $$z=1$$ thành $$z$$, kết hợp nhóm hàng $$\bar x\bar y$$:

$$
F = \bar x\bar y + z.
$$

Mọi ô **1** vẫn được phủ.

</div>

![Don't-care trên K-map](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_dont_care.svg)

<p class="textbook-figure-caption" data-figure="13.56">Don't-care mở rộng nhóm: $$F=\bar x\bar y+z$$.</p>

## 8. So sánh với biến đổi đại số

| Phương pháp | Phạm vi điển hình |
|:---|:---|
| Biến đổi đại số (13.3) | Ít hạng, cấu trúc biểu thức rõ |
| K-map | Hai đến bốn biến |

Với $$n\ge 5$$, lưới K-map trở nên cồng kềnh; khi đó cần các phương pháp rút gọn dạng bảng hoặc công cụ hỗ trợ ngoài phạm vi bài này.

## Bài tập

### Bài tập 1

Tối thiểu hóa bằng K-map:

(a) $$F = xy + x\bar y$$.  
(b) $$A = xy + \bar x y + \bar x\bar y$$.  
(c) $$F=1$$ tại các minterm $$0,1,2,4,5$$ của hàm ba biến $$x,y,z$$.

<details>
<summary>Đáp án</summary>

(a) $$F=x$$.  
(b) $$A=\bar x + y$$.  
(c) $$F=\bar x\bar y + \bar x\bar z + x\bar y$$.

</details>

### Bài tập 2

Rút gọn

$$
F = xy\bar z + x\bar y\bar z + \bar x y z + \bar x y\bar z + \bar x\bar y\bar z.
$$

<details>
<summary>Đáp án</summary>

$$F = \bar z + \bar x y$$.

</details>

### Bài tập 3

$$F=1$$ tại minterm $$0,1,5$$; don't-care tại $$2,7$$ (ba biến). Tìm một SOP tối tiểu.

<details>
<summary>Đáp án</summary>

$$F=\bar x\bar z + \bar y z$$ (hoặc dạng tương đương cùng bảng chân trị trên các ô không phải don't-care).

</details>

### Bài tập 4

Cho $$X=\{a,b,c,d\}$$, $$A=\{a,b\}$$, $$B=\{c,d\}$$, $$C=\{a,d\}$$, $$D=\{b,c\}$$.

(a) $$\{A,B,C,D\}$$ có phải phủ không thừa không?  
(b) Nêu hai phủ không thừa.  
(c) Trên K-map, thế nào là tế bào **cốt yếu**?

<details>
<summary>Đáp án</summary>

(a) Không.  
(b) $$\{A,B\}$$, $$\{C,D\}$$.  
(c) Tế bào lớn chứa ít nhất một ô **1** không thuộc tế bào lớn nào khác — bắt buộc nằm trong mọi phủ không thừa (*essential prime implicant*).

</details>

### Bài tập 5

$$F(x,y,z)=1$$ tại minterm $$0,2,4,5,6$$. Lập K-map, xác định tế bào lớn và một SOP tối tiểu theo quy trình năm bước.

<details>
<summary>Đáp án</summary>

$$F=\bar z + x\bar y$$.  
Các bước: lập lưới; liệt kê tế bào lớn; chọn cốt yếu (nếu có); hoàn tất phủ; đọc SOP.

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=dJsguV1PaPQ">Karnaugh maps</a>  
- Mục 13.3 — tối thiểu hóa đại số  

## Tóm tắt

1. Mã Gray bảo đảm hai mã liên tiếp khác đúng một bit, nên kề trên K-map tương ứng gộp đại số.  
2. K-map biểu diễn bảng chân trị trên lưới; nhóm lũy thừa của 2 cho SOP tối tiểu.  
3. Tế bào lớn đồng nhất với hạng nguyên tố; quy trình năm bước xây phủ không thừa.  
4. Don't-care mở rộng nhóm mà không bắt buộc được phủ.  
5. K-map phù hợp hàm hai đến bốn biến; với $$n$$ lớn hơn, lưới trở nên cồng kềnh.
