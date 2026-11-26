---
layout: post
title: "Bản đồ Karnaugh và Tối thiểu hóa Trực quan"
categories: chapter13
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Bản đồ Karnaugh (K-map) cho hàm 2–4 biến theo thứ tự mã Gray, khái niệm tế bào lớn, quy trình 5 bước tìm phủ tối tiểu và xử lý trạng thái không xác định (don't-care)."
---

> **Câu chuyện mở đầu:** Rút gọn đại số Boole bằng tay giống như giải cờ vua mù: rất dễ bỏ sót một phép nhân bản $$a = a + a$$ hay một số hạng đồng thuận ẩn! Năm 1953, kỹ sư viễn thông Maurice Karnaugh tại Bell Labs nghĩ ra một mẹo thị giác tuyệt đẹp: **sắp xếp bảng chân trị lên một hình chữ nhật theo thứ tự mã Gray sao cho hai ô kề nhau luôn chỉ khác nhau đúng 1 bit** — biến đại số Boole thành trò chơi khoanh các hình chữ nhật kích thước $$1, 2, 4, 8$$!

<div class="textbook-epigraph" markdown="1">

"A Karnaugh map is a truth table rearranged so that adjacency means algebraic cancellation."

<span class="epigraph-attribution">— Tinh thần K-map</span>

</div>

Biến đổi đại số ở Mục 13.3 giúp rút gọn nhiều biểu thức Boole. Tuy nhiên, khi số **minterm** tăng lên, việc tìm các cặp hoặc nhóm hạng tử có thể gộp — chẳng hạn $$xy + x\bar y = x$$ — trở nên khó theo dõi và dễ bỏ sót.

**Bản đồ Karnaugh** (Karnaugh Map, viết tắt **K-map**) là cách sắp xếp lại bảng chân trị trên một lưới hai chiều với ba đặc trưng:

- mỗi ô tương ứng với đúng một minterm;
- hai ô kề nhau (kể cả ở hai mép đối diện của bảng) chỉ khác nhau đúng một biến;
- việc khoanh gộp một nhóm ô kề hợp lệ tương đương với bước rút gọn đại số trên các minterm đó.

Với các hàm Boole từ 2 đến 4 biến, K-map cho phép tìm trực quan dạng **SOP** (tổng các tích / *Sum of Products*) tối tiểu hai tầng có cùng bảng chân trị với hàm ban đầu.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** vai trò của mã Gray trong việc đánh nhãn hàng và cột của K-map.
- **Xây dựng** K-map 2, 3, 4 biến và điền đúng các ô có $$F=1$$.
- **Khoanh nhóm** theo quy tắc kích thước lũy thừa của 2, tính vòng mép (wrap-around) và cho phép chồng nhóm.
- **Áp dụng** quy trình năm bước: xác định tế bào lớn, tế bào cốt yếu, tìm phủ không thừa và viết SOP tối tiểu.
- **Chuyển đổi** mỗi nhóm thành một đơn thức tích để viết biểu thức $$F$$.
- **Xử lý** các ô don't-care khi đặc tả bài toán cho phép.

**Từ khóa**: K-map, mã Gray, minterm, tế bào lớn, hạng nguyên tố (*prime implicant*), phủ tối tiểu, don't-care.

</div>

## Kiến thức cần nhớ: Bản đồ Karnaugh (K-map) và Tô-pô của Siêu lập phương

### 1. Mã Gray & Tính kề trên Siêu lập phương $$Q_n$$
- **Bản chất:** Trên trục K-map 2 biến, thứ tự luôn là **$$00,\; 01,\; 11,\; 10$$** (KHÔNG phải $$00, 01, 10, 11$$!), để hai cột kề nhau — kể cả cột đầu $$00$$ với cột cuối $$10$$ — luôn chỉ khác đúng **1 bit**! Về mặt tô-pô, K-map 4 biến chính là mặt **hình xuyến $$T^2$$** (mép trên nối mép dưới, mép trái nối mép phải!).

### 2. Khoanh nhóm $$2^k$$ ô = Khử đúng $$k$$ biến!
- **Bản chất:** Một nhóm hình chữ nhật hợp lệ gồm $$2^k$$ ô toàn số $$1$$ tương ứng với một mặt con $$k$$-chiều của siêu lập phương $$Q_n$$ — tự động áp dụng luật $$xy + x\bar{y} = x$$ lặp lại $$k$$ lần để **khử đúng $$k$$ biến**!

### 3. Implicant Nguyên tố Cốt yếu (EPI) & Trạng thái Không quan tâm (Don't-care $$d$$)
- **Bản chất:** Khoanh các nhóm lớn nhất có thể (**Prime Implicant**), ưu tiên chọn nhóm chứa ít nhất một ô $$1$$ không ai khác phủ được (**Essential PI**). Các ô **Don't-care ($$d$$)** (tổ hợp đầu vào không bao giờ xảy ra, như mã BCD $$10..15$$) được tự do coi là $$1$$ nếu giúp mở rộng nhóm to hơn, hoặc $$0$$ nếu không cần!

## Ví dụ tính tay làm từng bước: Tối thiểu hóa hàm 3 biến $$f(A,B,C) = \sum m(0, 2, 4, 5, 6)$$ trên K-map

Lập bảng K-map 3 biến với hàng $$A \in \{0, 1\}$$ và cột $$BC \in \{00, 01, 11, 10\}$$:

| $$A \setminus BC$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|---|---|---|---|---|
| **$$0$$** | **1** ($$m_0$$) | 0 ($$m_1$$) | 0 ($$m_3$$) | **1** ($$m_2$$) |
| **$$1$$** | **1** ($$m_4$$) | **1** ($$m_5$$) | 0 ($$m_7$$) | **1** ($$m_6$$) |

1. **Nhóm 1 (4 ô cuộn vòng mép trái–phải!):** Cột $$BC = 00$$ ($$m_0, m_4$$) ghép vòng với cột $$BC = 10$$ ($$m_2, m_6$$). Kiểm tra biến không đổi: $$A$$ đổi ($$0,1$$), $$B$$ đổi ($$0,1$$), chỉ còn **$$C = 0$$** không đổi $$\implies$$ số hạng **$$\bar{C}$$**!
2. **Nhóm 2 (2 ô phủ nốt $$m_5$$):** Ghép $$m_4(100)$$ với $$m_5(101)$$ (tái sử dụng $$m_4$$ để nhóm lớn nhất!). Biến không đổi: $$A=1, B=0 \implies$$ số hạng **$$A\bar{B}$$**!
3. **Kết quả tối tiểu:** $$f(A, B, C) = \bar{C} + A\bar{B}$$ (chỉ cần 1 cổng NOT, 1 cổng AND, 1 cổng OR — so với 5 minterm ban đầu!).

### Giải thích: Quy tắc 4 bước khoanh K-map không bao giờ sai
#### Bước 1: Kiểm tra thứ tự Mã Gray trên cả hai trục
Luôn viết $$00, 01, 11, 10$$ và nhớ rằng mép trên chạm mép dưới, mép trái chạm mép phải (4 góc của K-map 4 biến thậm chí ghép thành 1 nhóm 4 ô!).

#### Bước 2: Tìm mọi nhóm cực đại có kích thước lũy thừa của 2 ($$1, 2, 4, 8, 16$$)
Nhóm càng lớn, số biến bị khử càng nhiều và cổng AND càng gọn. Được phép dùng chung một ô $$1$$ cho nhiều nhóm khác nhau nhờ luật $$a + a = a$$.

#### Bước 3: Bắt buộc chọn hết các Essential Prime Implicants (EPI) trước
Nếu một ô $$1$$ chỉ nằm trong duy nhất 1 nhóm cực đại, nhóm đó **bắt buộc** có mặt trong đáp án tối ưu.

#### Bước 4: Phủ nốt các ô $$1$$ còn sót bằng ít nhóm nhất (bỏ qua các ô Don't-care chưa dùng)
Không bao giờ thêm nhóm chỉ để phủ riêng ô Don't-care $$d$$!

$$
\text{Mã Gray (kề 1 bit)}
\;\xrightarrow{\;\text{Khoanh nhóm }2^k\text{ ô}\;}\;
\text{Khử }k\text{ biến}
\;\xrightarrow{\;\text{Chọn EPI + Phủ tối tiểu}\;}\;
\text{SOP tối giản}.
$$

## Mã Gray và tính kề trên trục

### Hạn chế của thứ tự nhị phân thông thường

Trên dãy nhị phân chuẩn $$00, 01, 10, 11$$, bước chuyển từ $$01$$ sang $$10$$ thay đổi đồng thời cả hai bit. Nếu đặt hai mã này kề nhau trên lưới, việc gộp chúng sẽ không tương ứng với phép triệt một biến theo đẳng thức $$xy + x\bar y = x$$.

### Mã Gray

**Mã Gray** sắp xếp các chuỗi bit sao cho hai mã liên tiếp chỉ khác nhau đúng một bit. Nhờ đó, tính kề hình học trên lưới trùng khớp với khoảng cách Hamming bằng 1, nên việc gộp ô phản ánh đúng phép rút gọn đại số.

Thứ tự mã Gray 2 bit là:

$$
00,\; 01,\; 11,\; 10.
$$

Hai đầu mút $$00$$ và $$10$$ cũng chỉ khác nhau đúng một bit, nên hai mép đối diện của lưới vẫn kề nhau (*wrap-around*). Trục hàng và cột của K-map 2–4 biến đều tuân theo thứ tự này.

![Nhị phân vs Gray](/discrete-mathematics-for-computer-science-iuh/img/course/Gray_vs_binary.svg)

<p class="textbook-figure-caption" data-figure="13.40">So sánh thứ tự nhị phân thông thường (đổi hai bit giữa 01 và 10) với mã Gray (luôn đổi đúng một bit).</p>

![Thứ tự Gray 3-bit](/discrete-mathematics-for-computer-science-iuh/img/course/gray_code.svg)

<p class="textbook-figure-caption" data-figure="13.41">Thứ tự mã Gray ba bit.</p>

### Video ngắn: Bản đồ Karnaugh

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/karnaugh-maps-gray-code.mp4"></video>
</div>

Video dài khoảng 3 phút 16 giây, trình bày cách tạo mã Gray bằng phép phản chiếu và đường đi trên khối lập phương, lý do hai ô kề nhau gộp được ($$xy + x\bar y = x$$), K-map 2, 3 và 4 biến với các nhóm 2, 4, 8 ô, nhóm vòng qua mép, nhóm bốn góc, ô don't-care và các quy tắc khoanh nhóm để đọc dạng SOP tối giản. Mọi lời giải trong video đều được kiểm chứng bằng cách duyệt vét cạn mọi cách phủ.

## Cấu trúc K-map và quy tắc khoanh nhóm

### Ba thành phần chính

| Thành phần | Định nghĩa |
|:---|:---|
| Ô | Biểu diễn một minterm, tương ứng với một hàng trong bảng chân trị |
| Kề | Hai ô kề nhau (kể cả qua mép đối diện) khác nhau đúng một biến |
| Gộp | Khoanh nhóm các ô kề hợp lệ, tương đương phép rút gọn $$xy + x\bar y = x$$ trên tập minterm đó |

### Năm quy tắc khoanh nhóm

1. Chỉ khoanh các ô mang giá trị **1** (hoặc **X** khi bài toán có don't-care).  
2. Số ô trong mỗi nhóm phải là lũy thừa của 2: $$1, 2, 4, 8, \ldots$$  
3. Ưu tiên nhóm có kích thước lớn nhất có thể: mỗi lần gấp đôi số ô sẽ triệt thêm một biến trong đơn thức tích.  
4. Các nhóm được phép chồng lên nhau: một ô **1** có thể thuộc nhiều nhóm khác nhau.  
5. Mọi ô **1** đều phải được phủ bởi ít nhất một nhóm; các ô **X** không bắt buộc phải nằm trong nhóm nào.

![Năm quy tắc khoanh nhóm](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_grouping_rules.svg)

<p class="textbook-figure-caption" data-figure="13.42">Năm quy tắc khoanh nhóm trên K-map.</p>

### Tế bào lớn và hạng nguyên tố

**Tế bào lớn** là một nhóm hợp lệ có kích thước lũy thừa của 2 mà không thể mở rộng thành nhóm hợp lệ lớn hơn nữa.

**Hạng nguyên tố** (*prime implicant*) là đơn thức tích ứng với một tế bào lớn — không thể rút gọn thêm bằng cách gộp minterm.

Một nhóm hợp lệ gồm $$2^{k}$$ ô sẽ triệt tiêu đúng $$k$$ biến (các biến thay đổi giá trị bên trong nhóm) và giữ lại những biến không đổi.

## K-map hai biến

K-map 2 biến là lưới $$2\times 2$$ với hàng theo $$x\in\{0,1\}$$ và cột theo $$y\in\{0,1\}$$, gồm 4 ô tương ứng với 4 minterm $$m_0,\ldots,m_3$$.

![K-map 2 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_2var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.43">Cấu trúc K-map hai biến.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Cho $$F = xy + x\bar y$$.

Hai ô trên hàng $$x=1$$ đều mang giá trị **1**. Khi khoanh nhóm hai ô này, biến $$y$$ thay đổi còn $$x$$ giữ nguyên bằng **1**, suy ra:

$$
F = x = x(y+\bar y).
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Cho $$A = xy + \bar x y + \bar x\bar y$$, tức $$A=1$$ tại $$(x,y)\in\{(0,0),(0,1),(1,1)\}$$.

Khoanh hàng $$x=0$$ cho tích $$\bar x$$; khoanh cột $$y=1$$ cho tích $$y$$ (ô $$(0,1)$$ thuộc cả hai nhóm). Do đó:

$$
A = \bar x + y.
$$

Kiểm tra tại $$(1,0)$$: $$A = 0$$, khớp với biểu thức SOP ban đầu.

</div>

![K-map 2 biến — ví dụ](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_2var_example.svg)

<p class="textbook-figure-caption" data-figure="13.44">Các minterm 0, 1, 3 cho kết quả $$A=\bar x+y$$.</p>

## K-map ba biến

### Sắp xếp lưới

- Hàng: cặp biến $$(x,y)$$ theo mã Gray $$00, 01, 11, 10$$.  
- Cột: biến $$z\in\{0,1\}$$.

Hàng $$10$$ kề với hàng $$00$$ qua mép bảng. Toàn lưới biểu diễn đủ 8 minterm.

![K-map 3 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_3var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.45">K-map ba biến với hàng Gray $$(x,y)$$ và cột $$z$$.</p>

### Quy tắc đọc nhóm thành tích

Trên mỗi nhóm hợp lệ:

1. biến thay đổi giữa 0 và 1 sẽ bị loại bỏ;  
2. biến luôn bằng **1** được giữ ở dạng nguyên;  
3. biến luôn bằng **0** được giữ ở dạng bù.

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Rút gọn

$$
F = xy\bar z + x\bar y\bar z + \bar x y z + \bar x y\bar z + \bar x\bar y\bar z.
$$

Các minterm theo thứ tự $$xyz$$ là $$110, 100, 011, 010, 000$$.

Bốn ô nằm trên cột $$z=0$$ tạo thành nhóm 4 ô ứng với $$\bar z$$; hai ô $$010$$ và $$011$$ tạo thành nhóm 2 ô ứng với $$\bar x y$$. Vậy:

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

**Ví dụ 2.** Cho $$F=1$$ tại các minterm có chỉ số $$0, 1, 2, 5, 7$$.

| Nhóm | Minterm | Tích |
|:---|:---|:---|
| Hàng $$xy=00$$ | $$m_0,m_1$$ | $$\bar x\bar y$$ |
| Cột $$z=0$$, hàng $$00$$ và $$01$$ | $$m_0,m_2$$ | $$\bar x\bar z$$ |
| Cột $$z=1$$, hàng $$11$$ và $$10$$ | $$m_7,m_5$$ | $$xz$$ |

Kết quả:

$$
F = \bar x\bar y + \bar x\bar z + xz.
$$

Biểu thức này khớp hoàn toàn với bảng chân trị của tập minterm đã cho.

</div>

![K-map 3 biến — ví dụ](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_3var_example.svg)

<p class="textbook-figure-caption" data-figure="13.46">Minh họa rút gọn $$F=\bar x\bar y+\bar x\bar z+xz$$.</p>

## K-map bốn biến

### Sắp xếp lưới

Lưới gồm 16 ô:

- hàng $$(x,y)$$ theo mã Gray $$00, 01, 11, 10$$;  
- cột $$(z,w)$$ theo mã Gray $$00, 01, 11, 10$$.

Chỉ số ghi trong mỗi ô (nếu có) biểu thị chỉ số minterm $$m_k$$.

![K-map 4 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_4var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.47">Cấu trúc K-map bốn biến.</p>

### Tính vòng mép (Wrap-around)

Do tính tuần hoàn của mã Gray:

- cột ngoài cùng bên trái kề với cột ngoài cùng bên phải;
- hàng trên cùng kề với hàng dưới cùng;
- bốn ô ở bốn góc của bảng tạo thành một nhóm 4 ô hợp lệ.

![K-map 4 biến — wrap-around](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_4var_wrap.svg)

<p class="textbook-figure-caption" data-figure="13.48">Nhóm bốn góc nhờ tính vòng mép (wrap-around).</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** Cho $$F=1$$ tại các minterm có chỉ số $$0,1,2,5,6,7,8,9,10,14$$.

Với quy ước hàng $$xy$$, cột $$zw$$ (ô tại hàng $$xy$$, cột $$zw$$ là minterm $$m_k$$ với $$k = 8x+4y+2z+w$$), ta có bảng sau:

| $$xy \backslash zw$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|---|---|---|---|---|
| $$00$$ | **1** ($$m_0$$) | **1** ($$m_1$$) | 0 ($$m_3$$) | **1** ($$m_2$$) |
| $$01$$ | 0 ($$m_4$$) | **1** ($$m_5$$) | **1** ($$m_7$$) | **1** ($$m_6$$) |
| $$11$$ | 0 ($$m_{12}$$) | 0 ($$m_{13}$$) | 0 ($$m_{15}$$) | **1** ($$m_{14}$$) |
| $$10$$ | **1** ($$m_8$$) | **1** ($$m_9$$) | 0 ($$m_{11}$$) | **1** ($$m_{10}$$) |

Ta chọn các nhóm lớn nhất trước rồi phủ các ô **1** còn lại:

- **Nhóm 4 ô vòng mép trên–dưới** $$\{m_0,m_1,m_8,m_9\}$$: gồm hàng $$00$$ và $$10$$ (kề nhau qua mép), cột $$00,01$$. Trong nhóm này $$y=0$$ và $$z=0$$ cố định, còn $$x$$ và $$w$$ thay đổi, nên tích tương ứng là $$\bar y\bar z$$.
- **Nhóm 4 ô cả cột $$zw=10$$** $$\{m_2,m_6,m_{10},m_{14}\}$$: có $$z=1$$, $$w=0$$ cố định, cho tích $$z\bar w$$.
- **Nhóm 2 ô** $$\{m_5,m_7\}$$: thuộc hàng $$01$$, cột $$01$$ và $$11$$; có $$x=0$$, $$y=1$$, $$w=1$$ cố định, cho tích $$\bar x y w$$.

Cả ba nhóm đều là tế bào lớn cốt yếu: $$m_9$$ chỉ thuộc $$\bar y\bar z$$, $$m_{14}$$ chỉ thuộc $$z\bar w$$, và $$\bar x y w$$ là nhóm 2 ô duy nhất phủ được $$m_7$$ (đồng thời phủ luôn $$m_5$$). Phủ tối tiểu duy nhất (3 tích, 7 litera) là:

$$
F = \bar y\bar z + z\bar w + \bar x y w.
$$

Lưu ý rằng mọi nhóm hợp lệ chỉ được chứa các ô **1** (không chứa ô **0**): chẳng hạn không thể khoanh cột $$00$$ ($$\bar z\bar w$$) vì có $$m_4, m_{12}$$ bằng 0, và không thể khoanh $$\bar x w$$ vì chứa $$m_3$$ bằng 0.

</div>

## Phủ tối tiểu

![K-map bước 1: điền bảng chân trị](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_1.svg)

![K-map bước 2: tìm tế bào đơn độc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_2.svg)

![K-map bước 3: khoanh tế bào lớn](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_3.svg)

![K-map bước 4: chọn phủ tối tiểu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_4.svg)

![K-map bước 5: đọc công thức tối tiểu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_5.svg)

Mục tiêu cuối cùng là chọn một họ tế bào lớn phủ hết mọi ô **1**, không dư thừa và cho biểu thức SOP ngắn gọn nhất.

### Phủ tập hợp

<div class="textbook-definition" markdown="1">

**Phủ.** Họ tập con $$\mathcal{S}=\{X_1,\ldots,X_n\}$$ là một phủ của tập $$X$$ nếu $$X=\bigcup_i X_i$$.

**Phủ không thừa** (*irredundant cover*): là một phủ mà nếu bỏ đi bất kỳ tập $$X_i$$ nào thì phần còn lại $$\mathcal{S}\setminus\{X_i\}$$ không còn phủ hết $$X$$.

</div>

Trên K-map, $$X$$ là tập tất cả các ô **1** và mỗi $$X_i$$ là một tế bào lớn.

<div class="textbook-example" markdown="1">

**Ví dụ.** Cho $$X=\{a,b,c,d\}$$ và các tập con $$A=\{a,b\}$$, $$B=\{c,d\}$$, $$C=\{a,d\}$$, $$D=\{b,c\}$$.

- $$\{A,B,C,D\}$$ là một phủ nhưng bị thừa.  
- $$\{A,B\}$$ và $$\{C,D\}$$ là hai phủ không thừa.  
- $$\{B,D\}$$ không phải là phủ của $$X$$ (thiếu phần tử $$a$$).

</div>

![Phủ tối tiểu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_set_cover.svg)

<p class="textbook-figure-caption" data-figure="13.49">Phủ không thừa trên một họ tập con.</p>

### Tế bào cốt yếu

Nếu tồn tại một ô **1** chỉ thuộc duy nhất một tế bào lớn $$T$$ thì $$T$$ bắt buộc phải có mặt trong mọi phủ không thừa. Khi đó $$T$$ được gọi là **tế bào lớn cốt yếu** (*essential prime implicant*).

![Tế bào lớn cốt yếu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_essential_cell.svg)

<p class="textbook-figure-caption" data-figure="13.50">Một ô 1 chỉ thuộc duy nhất một tế bào lớn sẽ xác định ngay một tế bào cốt yếu.</p>

### Quy trình năm bước

1. Lập K-map và điền các ô $$F=1$$ (cùng các ô **X** nếu có).  
2. Liệt kê tất cả các tế bào lớn.  
3. Chọn trước toàn bộ các tế bào lớn cốt yếu.  
4. Nếu các tế bào cốt yếu chưa phủ hết các ô **1**, bổ sung thêm các tế bào lớn khác cho phần còn lại và loại bỏ các phủ thừa.  
5. Đọc mỗi tế bào trong phủ thành một tích rồi nối bằng phép OR để được SOP tối tiểu. Một hàm có thể có nhiều dạng SOP tối tiểu có cùng độ phức tạp.

<div class="textbook-example" markdown="1">

**Ví dụ 1.**  
Khi hai tế bào lớn $$x$$ và $$yz$$ đều là cốt yếu và đã phủ kín mọi ô **1**, hàm có SOP tối tiểu duy nhất:

$$
f = x + yz.
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.**  
Giả sử các tế bào cốt yếu là $$\bar x\bar t$$, $$xzt$$, $$\bar z\bar t$$, và còn lại một ô **1** duy nhất thuộc đồng thời hai tế bào lớn $$\bar x\bar y z$$ và $$\bar y zt$$. Khi đó ta có hai phủ không thừa đều là SOP tối tiểu:

$$
\begin{aligned}
f_1 &= \bar z\bar t + \bar x\bar t + xzt + \bar x\bar y z, \\
f_2 &= \bar z\bar t + \bar x\bar t + xzt + \bar y zt.
\end{aligned}
$$

</div>

## Trạng thái không xác định (Don't-care)

Khi đầu ra tại một số tổ hợp đầu vào không bao giờ xảy ra hoặc không ảnh hưởng đến hệ thống, ta ký hiệu các ô đó là **X** trên K-map:

- ô **X** có thể được coi là **1** nếu giúp mở rộng nhóm lớn hơn;  
- ô **X** không bắt buộc phải được phủ.

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét hàm 3 biến có $$F=1$$ tại các minterm $$0, 1, 3$$ và don't-care tại $$5, 7$$.

Khi coi hai ô **X** tại $$5, 7$$ như **1**, ta có thể gom cả cột $$z=1$$ thành nhóm 4 ô ($$z$$), kết hợp với nhóm 2 ô ở hàng $$00$$ ($$\bar x\bar y$$):

$$
F = \bar x\bar y + z.
$$

Mọi ô **1** đều đã được phủ đầy đủ.

</div>

![Don't-care trên K-map](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_dont_care.svg)

<p class="textbook-figure-caption" data-figure="13.56">Dùng ô don't-care để mở rộng nhóm, thu được $$F=\bar x\bar y+z$$.</p>

## So sánh với biến đổi đại số

| Phương pháp | Phạm vi phù hợp |
|:---|:---|
| Biến đổi đại số (13.3) | Biểu thức ít hạng tử, cấu trúc dễ nhận biết |
| Bản đồ Karnaugh (K-map) | Hàm từ 2 đến 4 biến |

Khi số biến $$n \ge 5$$, lưới K-map trở nên cồng kềnh và khó quan sát bằng mắt; khi đó ta chuyển sang các phương pháp dạng bảng như Quine–McCluskey (bài 13.5) hoặc công cụ tự động.


## Công cụ tương tác

Đánh dấu các ô 1 (và tùy chọn don't-care) trên K-map 4 biến để tìm nhóm hợp lệ và rút gọn hàm.
<div class="interactive-demo" markdown="1">
<div data-demo="kmap-interactive"></div>
</div>
<script src="{{ '/public/js/kmap-interactive.js' | relative_url }}"></script>


### Minh họa liên kết: K-map, bảng chân trị và mạch SOP

Với bốn biến $$p,q,r,s$$, bấm trực tiếp vào ô trên K-map hoặc cột F của bảng chân trị để xem các nhóm tối tiểu và mạch SOP tương ứng tự động cập nhật; bạn cũng có thể đổi số biến (2–4) hoặc nhập biểu thức tùy ý.

<div class="interactive-demo" markdown="1">
<div data-demo="boolean-explainer" data-vars="4" data-focus="kmap" data-expr="(p ∧ q) ∨ (¬r ∧ s)"></div>
</div>
<script src="{{ '/public/js/explainers/boolean-explainer.js' | relative_url }}"></script>


## Bài tập

### Bài tập 1

Tối thiểu hóa các hàm sau bằng K-map:

(a) $$F = xy + x\bar y$$.  
(b) $$A = xy + \bar x y + \bar x\bar y$$.  
(c) $$F=1$$ tại các minterm $$0,1,2,4,5$$ của hàm ba biến $$x,y,z$$.

<details>
<summary>Đáp án</summary>

(a) $$F=x$$.  
(b) $$A=\bar x + y$$.  
(c) Nhóm 4 ô $$\{m_0, m_1, m_4, m_5\}$$ cho $$\bar y$$ và nhóm 2 ô $$\{m_0, m_2\}$$ cho $$\bar x\bar z$$, suy ra SOP tối tiểu là $$F = \bar y + \bar x\bar z$$.

</details>

### Bài tập 2

Rút gọn biểu thức sau bằng K-map:

$$
F = xy\bar z + x\bar y\bar z + \bar x y z + \bar x y\bar z + \bar x\bar y\bar z.
$$

<details>
<summary>Đáp án</summary>

$$F = \bar z + \bar x y$$.

</details>

### Bài tập 3

Cho hàm 3 biến có $$F=1$$ tại các minterm $$0,1,5$$ và don't-care tại $$2,7$$. Tìm một dạng SOP tối tiểu.

<details>
<summary>Đáp án</summary>

$$F=\bar x\bar z + \bar y z$$ (hoặc dạng tối tiểu tương đương như $$\bar x\bar y + \bar y z$$, có cùng giá trị trên mọi ô không phải don't-care).

</details>

### Bài tập 4

Cho $$X=\{a,b,c,d\}$$, $$A=\{a,b\}$$, $$B=\{c,d\}$$, $$C=\{a,d\}$$, $$D=\{b,c\}$$.

(a) $$\{A,B,C,D\}$$ có phải là phủ không thừa không?  
(b) Nêu hai phủ không thừa của $$X$$.  
(c) Trên K-map, thế nào là tế bào **cốt yếu**?

<details>
<summary>Đáp án</summary>

(a) Không, vì có thể bỏ bớt tập con mà vẫn phủ hết $$X$$.  
(b) Hai phủ không thừa là $$\{A,B\}$$ và $$\{C,D\}$$.  
(c) Tế bào cốt yếu (*essential prime implicant*) là tế bào lớn chứa ít nhất một ô **1** không thuộc bất kỳ tế bào lớn nào khác, nên bắt buộc phải có mặt trong mọi phủ không thừa.

</details>

### Bài tập 5

Cho $$F(x,y,z)=1$$ tại các minterm $$0,2,4,5,6$$. Lập K-map, xác định các tế bào lớn và tìm một SOP tối tiểu theo quy trình năm bước.

<details>
<summary>Đáp án</summary>

$$F=\bar z + x\bar y$$.  
Các bước thực hiện: lập K-map 3 biến; tìm hai tế bào lớn $$\bar z$$ (gồm $$m_0,m_2,m_4,m_6$$) và $$x\bar y$$ (gồm $$m_4,m_5$$); cả hai đều cốt yếu và phủ đủ 5 ô **1**; đọc tổng SOP tương ứng.

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=dJsguV1PaPQ">Karnaugh maps</a>  
- Mục 13.3 — tối thiểu hóa đại số  

## Tóm tắt

1. Mã Gray bảo đảm hai mã liên tiếp chỉ khác nhau đúng một bit, giúp tính kề trên K-map tương ứng trực tiếp với phép gộp đại số.  
2. K-map biểu diễn bảng chân trị trên lưới; các nhóm kích thước lũy thừa của 2 cho dạng SOP tối tiểu.  
3. Tế bào lớn tương ứng với hạng nguyên tố; quy trình năm bước giúp xây dựng phủ không thừa.  
4. Ô don't-care giúp mở rộng kích thước nhóm mà không bắt buộc phải được phủ.  
5. K-map phù hợp cho hàm 2 đến 4 biến; với số biến lớn hơn, lưới trở nên cồng kềnh.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=P_PQ0v89qr8">[TOÁN RỜI RẠC] - BẢN ĐỒ KARNAUGH 3 BIẾN - TS TRẦN HOAN</a> — Học Toán Cùng Thầy Kenka - Tiến Sĩ Trần Hoan, tiếng Việt. Hướng dẫn bản đồ Karnaugh 3 biến bằng tiếng Việt.
- <a href="https://www.youtube.com/watch?v=FPrcIhqNPVo">Karnaugh Map (K&#x27; Map) - Part 1</a> — Neso Academy, tiếng Anh. Trình bày các quy tắc khoanh nhóm trên K-map.
- <a href="https://www.youtube.com/watch?v=k_gavfON5uA">4 Variable Karnaugh Map (Part 1)</a> — Neso Academy, tiếng Anh. Hướng dẫn giải K-map bốn biến.
