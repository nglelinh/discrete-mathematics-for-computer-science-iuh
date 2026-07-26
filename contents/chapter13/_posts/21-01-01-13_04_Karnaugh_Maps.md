---
layout: post
title: "Bản đồ Karnaugh và Tối thiểu hóa Trực quan"
categories: chapter13
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Mã Gray, K-map 2–4 biến, tế bào lớn và quy trình 5 bước phủ tối tiểu, don't-care và liên hệ đại số/QM."
---

<div class="textbook-epigraph" markdown="1">

"A Karnaugh map is a truth table rearranged so that adjacency means algebraic cancellation."

<span class="epigraph-attribution">— Tinh thần K-map</span>

</div>

Biến đổi đại số (bài 13.3) rút gọn được nhiều biểu thức, nhưng khi số minterm tăng, “nhìn ra” cặp $$xy + xy' = x$$ dễ sót.

**Bản đồ Karnaugh** (K-map) giải quyết việc đó bằng cách **sắp lại** bảng chân trị trên lưới:

1. Mỗi ô = một minterm (một hàng của bảng).
2. Hai ô **kề nhau** (kể cả mép đối diện) luôn khác **đúng một bit**.
3. Gộp các ô kề = áp dụng $$xy + xy' = x$$ “bằng mắt”.

Với **2–4 biến**, mắt người đọc lưới nhanh hơn chuỗi biến đổi đại số. Kết quả vẫn là **SOP** (tổng các tích) tối tiểu hai tầng, tương đương hàm gốc.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** mã Gray và vì sao K-map dùng thứ tự Gray trên trục.
- **Dựng** K-map 2, 3, 4 biến và điền $$1$$ từ $$\sum m(\ldots)$$.
- **Nhóm** ô đúng quy tắc (lũy thừa của 2, wrap-around, chồng nhóm).
- **Áp dụng** quy trình 5 bước tìm **phủ tối tiểu** bằng **tế bào lớn** (implicant nguyên tố).
- **Đọc** từng nhóm thành một tích và viết $$F$$ tối tiểu.
- **Dùng** don't-care ($$X$$) để nới nhóm khi đặc tả cho phép.

**Từ khóa**: Karnaugh map, mã Gray, implicant, tế bào lớn, phủ tối tiểu, prime implicant, don't-care.

</div>

## 1. Mã Gray — nền tảng của sự “kề”

Trong nhị phân thường, bước từ $$01$$ sang $$10$$ đổi **hai** bit cùng lúc. Trên K-map, nếu hai ô đó đặt cạnh nhau, việc gộp sẽ **không** tương ứng một biến bị loại. **Mã Gray** sắp thứ tự sao cho hai giá trị liên tiếp (và hai đầu mút của trục, nhờ tính chu kỳ) chỉ khác **một** bit.

Với hai bit, thứ tự Gray là $$00,01,11,10$$ — đúng thứ tự cột/hàng chuẩn trên K-map. Bit Gray cao nhất bằng bit nhị phân cao nhất; các bit thấp hơn $$g_i=b_{i+1}\oplus b_i$$. Ví dụ $$1011_2$$ → Gray $$1110$$ vì $$g_3=1$$, $$g_2=1\oplus0=1$$, $$g_1=0\oplus1=1$$, $$g_0=1\oplus1=0$$.

Ngoài K-map, Gray còn giảm lỗi trạng thái trung gian ở encoder quay và một số FSM — cùng tinh thần “mỗi bước một bit”.

![Nhị phân vs Gray](/discrete-mathematics-for-computer-science-iuh/img/course/Gray_vs_binary.svg)

<p class="textbook-figure-caption" data-figure="13.40">Thứ tự nhị phân thường đổi 2 bit (01→10); Gray chỉ đổi 1 bit — bắt buộc cho trục K-map.</p>

![Bảng mã Gray 3-bit](/discrete-mathematics-for-computer-science-iuh/img/course/gray_code.svg)

<p class="textbook-figure-caption" data-figure="13.41">Bảng chuyển nhị phân → Gray 3-bit (dùng làm thứ tự hàng/cột).</p>

## 2. Ý tưởng K-map

### 2.1. Ba ý chính

| Ý | Giải thích |
|:---|:---|
| **Ô** | Mỗi ô = một minterm (một hàng bảng chân trị) |
| **Kề** | Hai ô kề (kể cả mép đối diện — *wrap-around*) khác đúng **một** litera |
| **Gộp** | Gộp các ô kề = áp dụng $$xy + xy' = x$$ trên mặt phẳng |

### 2.2. Quy tắc khoanh nhóm (học thuộc)

1. Chỉ khoanh ô mang **1** (hoặc **X** nếu dùng don't-care).
2. Kích thước nhóm phải là lũy thừa của 2: $$1, 2, 4, 8, \ldots$$
3. Ưu tiên nhóm **lớn** (loại được nhiều biến hơn → tích ngắn hơn).
4. Các nhóm **được chồng**: một ô **1** có thể thuộc nhiều nhóm.
5. Mọi ô **1** phải được phủ **ít nhất một lần**; don't-care **không** bắt buộc phủ.

![Năm quy tắc khoanh nhóm](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_grouping_rules.svg)

<p class="textbook-figure-caption" data-figure="13.42">Quy tắc khoanh nhóm trên K-map.</p>

Nhóm $$2^k$$ ô hợp lệ loại được $$k$$ biến. **Implicant nguyên tố** (prime implicant) = nhóm không còn mở rộng thêm được mà vẫn hợp lệ.

## 3. K-map hai biến

Lưới $$2\times2$$ với hàng $$x$$, cột $$y$$ (mỗi ô = một **tiểu hạng** / minterm):

![K-map 2 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_2var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.43">K-map 2 biến: bốn ô $$m_0$$–$$m_3$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1 (slide — gom một hàng).**  
$$F = xy + x\bar y$$. Điền hai ô hàng $$x=1$$ → nhóm 2 ô: $$F = x$$.  
Đây chính là $$x(y+\bar y)=x$$ “bằng mắt”.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2 (slide — hai nhóm).**  
$$A = xy + \bar x y + \bar x\bar y = \sum m(0,1,3)$$.  
Hàng $$x=0$$ đầy $$1$$ → $$\bar x$$; cột $$y=1$$ → $$y$$.  
$$A = \bar x + y$$ (kiểm: tại $$10$$ hàm **0**).

Cùng cover với cách đọc $$m_0,m_1$$ thành $$\bar x$$ và $$m_1,m_3$$ thành $$y$$.

</div>

![K-map 2 biến — ví dụ](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_2var_example.svg)

<p class="textbook-figure-caption" data-figure="13.44">$$\sum m(0,1,3)$$: nhóm $$\bar x$$ và $$y$$ → $$A=\bar x+y$$.</p>

## 4. K-map ba biến

Tám ô: thường xếp $$xy$$ theo Gray dọc ($$00,01,11,10$$) và $$z$$ ngang ($$0,1$$) — hoặc cột theo Gray $$yz$$. Hàng $$10$$ kề hàng $$00$$ nhờ wrap.

![K-map 3 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_3var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.45">K-map 3 biến: hàng Gray, cột $$z$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ (slide — 5 hạng → 2 hạng).**  
Rút gọn

$$
F = xy\bar z + x\bar y\bar z + \bar x y z + \bar x y\bar z + \bar x\bar y\bar z.
$$

Trên K-map (cột Gray $$yz$$): nhóm bốn ô mang $$\bar z$$ → $$\bar z$$; nhóm hai ô mang $$\bar x y$$ → $$\bar x y$$.

$$
F = \bar z + \bar x y.
$$

Kiểm nhanh: tại $$111$$, $$\bar z=0$$ và $$\bar x y=0$$ → $$F=0$$; tại $$011$$, $$\bar x y=1$$ → $$F=1$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F=\sum m(0,1,2,5,7)$$.  
Một cách nhóm: hàng $$xy=00$$ cả hai ô → $$x'y'$$; hai ô $$z=0$$ ở $$xy=00$$ và $$01$$ → $$x'z'$$; hai ô $$z=1$$ ở $$xy=11$$ và $$10$$ → $$xz$$.  
$$F=x'y'+x'z'+xz$$. Nên đối chiếu vài vector với bảng gốc để chắc không sót/không thừa.

</div>

![K-map 3 biến — ví dụ](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_3var_example.svg)

<p class="textbook-figure-caption" data-figure="13.46">Ví dụ 3 biến với ba nhóm; một cover: $$F=x'y'+x'z'+xz$$.</p>

## 5. K-map bốn biến

Mười sáu ô; cả hàng $$xy$$ và cột $$zw$$ đều Gray $$00,01,11,10$$. Góc bốn ô $$z'w'$$ (các tổ hợp $$**00$$ và $$**10$$ ở hai mép) thường tạo nhóm “vòng” lớn.

![K-map 4 biến — cấu trúc](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_4var_blank.svg)

<p class="textbook-figure-caption" data-figure="13.47">K-map 4 biến: số trong ô = chỉ số minterm.</p>

![K-map 4 biến — wrap-around](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_4var_wrap.svg)

<p class="textbook-figure-caption" data-figure="13.48">Bốn góc kề trên torus — nhóm wrap-around hợp lệ.</p>

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F=\sum m(0,1,2,5,6,7,8,9,10,14)$$.  
Một cover hay gặp trong tài liệu: $$F=z'w'+x'w+x'yz+yzw'$$ — tương ứng lần lượt nhóm góc $$z'w'$$, cặp mang $$x'w$$, v.v. Bài tập yêu cầu bạn **tự khoanh** trên giấy rồi mới chép tích; đừng học thuộc chuỗi hạng.

</div>

## 6. Phủ tối tiểu và tế bào lớn — quy trình 5 bước

Khi đã biết “khoanh nhóm lớn”, vẫn còn câu hỏi: **chọn tập nhóm nào** để vừa phủ hết các ô $$1$$ vừa không thừa? Đây chính là bài toán **phủ tập** (set cover) trên K-map.

<div class="textbook-definition" markdown="1">

**Phủ và phủ tối tiểu.** Cho họ $$\mathcal{S}=\{X_1,\ldots,X_n\}$$ các tập con của $$X$$. $$\mathcal{S}$$ là **phủ** của $$X$$ nếu $$X=\bigcup_i X_i$$. Phủ gọi là **tối tiểu** (irredundant) nếu bỏ bất kỳ $$X_i$$ nào thì không còn phủ được $$X$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ tập.** $$X=\{a,b,c,d\}$$, $$A=\{a,b\}$$, $$B=\{c,d\}$$, $$C=\{a,d\}$$, $$D=\{b,c\}$$.  
Họ $$\{A,B,C,D\}$$ phủ nhưng **không** tối tiểu (thừa). Các phủ tối tiểu gồm $$\{A,B\}$$ và $$\{C,D\}$$. Họ $$\{B,D\}$$ không phủ.

</div>

![Phủ tối tiểu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_set_cover.svg)

<p class="textbook-figure-caption" data-figure="13.49">Phủ tối tiểu trên tập: bỏ bớt tập con thì không còn phủ.</p>

Trên K-map, mỗi **tế bào lớn** (nhóm lũy thừa 2 không mở rộng thêm được) ứng với một **implicant nguyên tố**. Các ô mang $$1$$ là tập $$X$$ cần phủ.

![Tế bào lớn cốt yếu](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_essential_cell.svg)

<p class="textbook-figure-caption" data-figure="13.50">Ô 1 chỉ thuộc một tế bào lớn → tế bào đó **cốt yếu** (essential PI).</p>

Thuật toán tìm công thức đa thức tối tiểu (SOP hai cấp) gồm **năm bước** — mỗi bước một hình:

![Bước 1](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_1.svg)

<p class="textbook-figure-caption" data-figure="13.51">Bước 1: vẽ K-map và điền 1 (và X).</p>

![Bước 2](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_2.svg)

<p class="textbook-figure-caption" data-figure="13.52">Bước 2: liệt kê mọi tế bào lớn.</p>

![Bước 3](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_3.svg)

<p class="textbook-figure-caption" data-figure="13.53">Bước 3: chọn tế bào cốt yếu.</p>

![Bước 4](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_4.svg)

<p class="textbook-figure-caption" data-figure="13.54">Bước 4: hoàn tất phủ (nhánh nếu cần).</p>

![Bước 5](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_step_5.svg)

<p class="textbook-figure-caption" data-figure="13.55">Bước 5: đọc SOP tối tiểu.</p>

<div class="textbook-definition" markdown="1">

**Thuật toán 5 bước (K-map → SOP tối tiểu).**

1. **Vẽ** K-map của $$f$$ và đánh dấu các ô $$1$$ (và $$X$$ nếu có).
2. **Liệt kê** tất cả **tế bào lớn** của $$\mathrm{kar}(f)$$ — tức mọi implicant nguyên tố.
3. **Chọn bắt buộc**: tế bào lớn $$T$$ **nhất thiết** phải chọn nếu tồn tại một ô $$1$$ **chỉ** thuộc $$T$$ (không nằm trong tế bào lớn nào khác). Đây là implicant **cốt yếu**.
4. **Hoàn tất phủ**: nếu các tế bào ở bước 3 đã phủ hết các ô $$1$$ thì đó là (các) phủ tối tiểu. Nếu còn ô chưa phủ, với mỗi ô còn lại chọn một trong các tế bào lớn chứa nó; thu được các họ phủ, rồi **loại** các họ không tối tiểu (thừa tập).
5. **Đọc biểu thức**: mỗi phủ tối tiểu → một SOP; giữ dạng không bị dạng khác thực sự đơn giản hơn.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1 (slide — phủ cốt yếu đủ).**  
Hàm bốn biến sau khi điền K-map có các tế bào lớn gồm (trong số khác) nhóm cả “khối $$x$$” và nhóm $$yz$$, mỗi nhóm chứa ô **chỉ** thuộc nó. Bước 3 buộc chọn cả hai; bước 4 thấy đã phủ hết → phủ tối tiểu duy nhất; bước 5:

$$
f = x + yz.
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2 (slide — hai dạng tối tiểu “đơn giản như nhau”).**  
Khi bước 3 **chưa** phủ hết, bạn **nhánh**: với một ô còn lại, thử lần lượt từng tế bào lớn chứa nó.

Giả sử các tế bào cốt yếu đã chọn là $$\bar x\bar t$$, $$xzt$$, $$\bar z\bar t$$, còn **một** ô chưa phủ nằm trong đúng hai tế bào lớn (ví dụ $$\bar x\bar y z$$ và $$\bar y zt$$). Hai phủ tối tiểu:

$$
\begin{aligned}
f_1 &= \bar z\bar t + \bar x\bar t + xzt + \bar x\bar y z, \\
f_2 &= \bar z\bar t + \bar x\bar t + xzt + \bar y zt.
\end{aligned}
$$

Cùng số hạng / độ phức tạp tương đương → **cả hai** là công thức đa thức tối tiểu (không bắt buộc chỉ còn một đáp án).

</div>

**Liên hệ Quine–McCluskey (13.5).** Bước 2–3 trên K-map chính là “sinh implicant nguyên tố + implicant cốt yếu” của QM; bước 4 là bảng phủ / nhánh Petrick viết tay trên lưới. K-map cho mắt; QM cho máy. Slide “Bản đồ Karnaugh” cũng có phần QM — giáo trình tách sang bài 13.5 cho gọn.

## 7. Don't-care

Đôi khi đặc tả không quan tâm đầu ra tại vài vector (mã không dùng, trạng thái không tới). Ký $$X$$ trên K-map: được phép coi là $$1$$ để **phình** nhóm, nhưng không bắt buộc phủ nếu không có lợi. Cùng ý sẽ gặp lại ở Quine–McCluskey: don't-care tham gia sinh implicant, không buộc xuất hiện trong cover.

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F=\sum m(0,1,3)+d(5,7)$$.  
Dùng $$X$$ ở cột $$z=1$$ có thể kéo thành cả cột $$z$$, cộng nhóm hàng $$x'y'$$, nhận $$F=x'y'+z$$ — ngắn hơn nếu bỏ không dùng $$X$$.

</div>

![Don't-care trên K-map](/discrete-mathematics-for-computer-science-iuh/img/course/Kmap_dont_care.svg)

<p class="textbook-figure-caption" data-figure="13.56">$$X$$ nới nhóm cột $$z$$; không bắt buộc phủ $$X$$ → $$F=x'y'+z$$.</p>

## 8. K-map và đại số

K-map giỏi **nhìn** với $$n\le 4$$ (năm–sáu biến đã chật). Đại số chứng minh đẳng thức và xử lý biểu thức ký hiệu. Từ năm biến trở lên, chuyển sang tabulation (13.5) hoặc heuristic công nghiệp. Cả ba tầng cùng nói ngôn ngữ implicant.

## Bài tập

### Bài tập 1

Chuyển $$1101_2$$ sang Gray. Liệt kê Gray 3 bit theo thứ tự.

<details>
<summary>Đáp án</summary>

$$1101\to 1011$$ (Gray).  
3 bit: $$000,001,011,010,110,111,101,100$$.

</details>

### Bài tập 2

Tối thiểu hóa bằng K-map:

(a) $$F = xy + x\bar y$$ (hai biến).  
(b) $$A = xy + \bar x y + \bar x\bar y$$.  
(c) $$\sum m(0,1,2,4,5)$$ ba biến.

<details>
<summary>Đáp án</summary>

(a) $$F=x$$.  
(b) $$A=\bar x + y$$.  
(c) Một dạng gọn: $$F=x'z'+y'z'+xy'$$ — đối chiếu với bảng của bạn.

</details>

### Bài tập 2b — Slide 3 biến

Rút gọn bằng K-map:

$$
F = xy\bar z + x\bar y\bar z + \bar x y z + \bar x y\bar z + \bar x\bar y\bar z.
$$

<details>
<summary>Đáp án</summary>

$$F = \bar z + \bar x y$$ (nhóm bốn ô $$\bar z$$ và cặp $$\bar x y$$).

</details>

### Bài tập 3

$$F=\sum m(0,1,5)+d(2,7)$$. Dùng $$X$$ khéo để rút gọn.

<details>
<summary>Đáp án</summary>

Có thể đạt $$F=x'z'+y'z$$ hoặc dạng tương đương ngắn; mọi ô $$1$$ phải phủ, $$X$$ tùy chọn.

</details>

### Bài tập 4 — Phủ tối tiểu

Cho $$X=\{a,b,c,d\}$$ và $$A=\{a,b\}$$, $$B=\{c,d\}$$, $$C=\{a,d\}$$, $$D=\{b,c\}$$.

(a) $$\{A,B,C,D\}$$ có phải phủ tối tiểu không?  
(b) Nêu hai phủ tối tiểu khác nhau.  
(c) Trên K-map, “tế bào lớn nhất thiết phải chọn” tương ứng khái niệm nào của QM?

<details>
<summary>Đáp án</summary>

(a) Không — có thể bỏ bớt vẫn phủ.  
(b) $$\{A,B\}$$ và $$\{C,D\}$$ (còn các phủ tối tiểu khác tùy định nghĩa).  
(c) **Implicant nguyên tố cốt yếu** (essential prime implicant).

</details>

### Bài tập 5 — Năm bước

Với $$F(x,y,z)=\sum m(0,2,4,5,6)$$: vẽ K-map 3 biến, liệt kê tế bào lớn, chỉ ra tế bào cốt yếu (nếu có), viết một SOP (tổng các tích) tối tiểu. Nêu rõ bạn đã đi qua bước nào của quy trình 5 bước.

<details>
<summary>Đáp án</summary>

Một cover thường gặp: nhóm bốn ô $$z'=0$$ cho $$z'$$ và cặp mang $$xy'$$ hoặc tương đương — ví dụ $$F=z'+xy'$$ (kiểm bảng). Tế bào phủ một ô “cô đơn” (nếu có) là cốt yếu. Quy trình: B1 vẽ → B2 tế bào lớn → B3 cốt yếu → B4 phủ → B5 đọc SOP (tổng các tích).

</details>

## Xem thêm

- <a href="https://www.youtube.com/watch?v=dJsguV1PaPQ">Karnaugh maps</a> — luyện khoanh nhóm

## Tóm tắt

Gray bảo đảm kề hình học = kề Hamming. K-map biến việc gộp minterm thành thao tác hình học trên lưới 2–4 biến; **tế bào lớn** + **phủ tối tiểu** (5 bước) chọn cover không thừa; don't-care nới nhóm khi đặc tả cho phép. Bài sau thuật toán hóa cùng ý tưởng bằng **bảng Quine–McCluskey**.
