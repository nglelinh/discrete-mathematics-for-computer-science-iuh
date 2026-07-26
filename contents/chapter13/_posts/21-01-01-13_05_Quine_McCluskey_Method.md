---
layout: post
title: "Phương pháp Quine–McCluskey"
categories: chapter13
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Phương pháp Quine–McCluskey: tối giản hàm Boole bằng bảng (phép dán, nguyên nhân nguyên tố, bảng phủ, nguyên tố cốt yếu), so với K-map và don't-care."
---

<div class="textbook-epigraph" markdown="1">

"Tabulate, combine, cover — Quine–McCluskey is the Karnaugh map written as an algorithm."

<span class="epigraph-attribution">— Tinh thần QM</span>

</div>

Phương pháp **Quine–McCluskey** (*tabulation method*) là kỹ thuật **hệ thống** tối thiểu hóa hàm Boolean bằng bảng. Phương pháp đặc biệt hữu ích khi số biến lớn hơn bốn, lúc bản đồ Karnaugh trở nên khó quan sát và dễ bỏ sót nhóm. Các **nguyên nhân hạng $$n$$** (minterm / từ tối tiểu) được ghi dạng bit; các cặp chỉ khác một bit được **dán** (gộp); sau đó chọn một tập hạng gọn nhất vẫn mô tả đúng hàm.

Quine–McCluskey thực hiện cùng phép rút gọn như K-map, nhưng dưới dạng quy trình bảng, kiểm chứng được từng bước và có thể thuật toán hóa.

Về cơ bản, phương pháp có **hai phần**:

1. **Phần 1 — Tìm dạng tổng chuẩn tắc thu gọn.**  
   Tìm các số hạng **ứng viên** để đưa vào khai triển cực tiểu — tức các **nguyên nhân nguyên tố** của $$F$$. Điểm xuất phát là tổng các nguyên nhân hạng $$n$$, vốn tạo nên **dạng nối rời chính tắc** (SOP chuẩn / tổng các tích đầy đủ).

2. **Phần 2 — Tìm dạng tổng chuẩn tắc tối thiểu.**  
   Trên **bảng phủ**, chọn một hệ nguyên nhân nguyên tố gọn nhất vẫn phủ hết các chỗ $$F = 1$$ — thu được **SOP (tổng các tích) tối tiểu**.

Kết quả là một SOP hai tầng tối tiểu, hoặc một trong vài cover tối ưu tương đương.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** vì sao dùng Quine–McCluskey khi K-map không còn tiện.
- **Mô tả** hai phần: tìm **nguyên nhân nguyên tố**, rồi chọn cover trên bảng phủ.
- **Thực hiện** **phép dán** (gộp minterm; dấu `-` tại bit khác nhau) cho hàm nhỏ (3–4 biến).
- **Nhận** **nguyên nhân nguyên tố cốt yếu** và hoàn tất cover tối tiểu.
- **Xử lý** don't-care: dùng ở phần 1, không bắt buộc phủ ở phần 2.
- **So sánh** Quine–McCluskey với K-map về phạm vi và cách trình bày.

**Từ khóa**: Quine–McCluskey, dạng nối rời chính tắc, nguyên nhân hạng $$n$$ (minterm / từ tối tiểu), phép dán, nguyên nhân nguyên tố, nguyên tố cốt yếu, dạng tổng chuẩn tắc thu gọn / tối thiểu, SOP (tổng các tích), bảng phủ, don't-care.

</div>

## 1. Vì sao cần thuật toán bảng?

K-map rất trực quan với **hai đến bốn** biến: mỗi ô là một nguyên nhân hạng $$n$$ (minterm), ô kề khác đúng một bit, khoanh nhóm là áp dụng $$xy + x\bar y = x$$ “bằng mắt”. Khi có **năm biến trở lên**, lưới chật, wrap-around nhiều hướng, và dễ bỏ sót nhóm hợp lệ.

Quine–McCluskey không phụ thuộc hình vẽ:

- mỗi nguyên nhân hạng $$n$$ được viết thành **chuỗi bit** cố định (ví dụ bốn biến $$wxyz$$);
- hai chuỗi **dán được** khi chỉ khác đúng **một** vị trí — đúng cùng đẳng thức $$xy + x\bar y = x$$;
- nhóm lớn trên K-map tương ứng chuỗi dán nhiều lần trên bảng.

Trên lớp, ta luyện tay với ví dụ **ba–bốn** biến để nắm quy trình. Với nhiều biến hơn, **cùng các bước** đó được máy thực hiện — ý tưởng không đổi, chỉ khác quy mô.

![Bảng Quine–McCluskey](/discrete-mathematics-for-computer-science-iuh/img/course/quine_mccluskey.svg)

<p class="textbook-figure-caption" data-figure="13.21">Phương pháp bảng: nhóm theo số bit 1; mũi tên thể hiện phép dán tạo nguyên nhân rộng hơn (ít litera hơn).</p>

![K-map — đối chiếu](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

<p class="textbook-figure-caption" data-figure="13.22">Cùng mục tiêu tối thiểu SOP (tổng các tích): K-map trên lưới; Quine–McCluskey trên bảng.</p>

## 2. Phần 1 — Tìm dạng tổng chuẩn tắc thu gọn

### (sinh nguyên nhân nguyên tố)

Mục tiêu phần 1: từ **dạng nối rời chính tắc** (tổng các nguyên nhân hạng $$n$$), tìm **mọi** hạng không còn dán rộng thêm được. Trong giáo trình Việt, hạng đó gọi là **nguyên nhân nguyên tố** của $$F$$ (tài liệu tiếng Anh: *prime implicant*). Đó là các tích không còn bỏ thêm biến nào mà vẫn chỉ phủ các chỗ hàm bằng **1** (và don't-care đã cho phép) — chính là **ứng viên** cho khai triển cực tiểu.

**Phương pháp Quine–McCluskey tìm dạng tổng chuẩn tắc thu gọn:**

**Bước 1.** Viết vào **cột thứ nhất** các biểu diễn của các **nguyên nhân hạng $$n$$** của hàm Boole $$F$$ (chuỗi bit của minterm / từ tối tiểu). Các biểu diễn được **chia nhóm**: trong mỗi nhóm, số ký hiệu **1** bằng nhau; các nhóm xếp theo **số bit 1 tăng dần**.

**Bước 2.** Lần lượt thực hiện tất cả các **phép dán** giữa biểu diễn ở nhóm có $$k$$ bit 1 với biểu diễn ở nhóm có $$k+1$$ bit 1 ($$k = 0, 1, 2, \ldots$$):

- Hai biểu diễn **dán được** khi khác đúng **một** bit; bit khác nhau thay bằng `-`.
- Biểu diễn nào tham gia **ít nhất một** phép dán được ghi nhận dấu `*` bên cạnh.
- Kết quả dán được ghi vào **cột tiếp theo**.

**Bước 3.** Lặp lại Bước 2 cho cột kế tiếp cho đến khi **không** thu thêm được cột mới. Khi đó, **tất cả các biểu diễn không có dấu `*`** chính là **mọi nguyên nhân nguyên tố** của $$F$$.

**Cơ sở toán.** Mỗi phép dán là một lần áp dụng

$$
xy + x\bar y = x.
$$

Chuỗi dán càng dài, tích càng ngắn (ít litera hơn), giống nhóm $$2^k$$ ô trên K-map.

![Bảng chân trị / minterm](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.23">Điểm xuất phát là tập nguyên nhân hạng $$n$$ — các hàng $$F = 1$$ — tương ứng dạng nối rời chính tắc (SOP chuẩn).</p>

## 3. Phần 2 — Tìm dạng tổng chuẩn tắc tối thiểu

### (bảng phủ và nguyên tố cốt yếu)

Sau phần 1 ta đã có danh sách **nguyên nhân nguyên tố**, nhưng thường **thừa**: không cần dùng hết vẫn mô tả đúng $$F$$. Phần 2 chọn một **phủ tối tiểu** (ít hạng; nếu cùng số hạng thì ưu tiên ít litera).

Lập **bảng phủ** như sau:

- mỗi **hàng** là một nguyên nhân nguyên tố;
- mỗi **cột** là một nguyên nhân hạng $$n$$ **bắt buộc** (chỗ $$F = 1$$; **không** đưa don't-care vào cột);
- đánh dấu `+` (hoặc ×) nếu hàng đó phủ cột tương ứng.

Một nguyên nhân nguyên tố gọi là **cốt yếu** khi tồn tại một cột chỉ có **đúng một** dấu: cột đó **bắt buộc** chọn đúng hàng đó — không có lựa chọn khác. Tên đầy đủ: **nguyên nhân nguyên tố cốt yếu** (tiếng Anh: *essential prime implicant*).

**Phương pháp Quine–McCluskey tìm dạng tổng chuẩn tắc tối thiểu:**

**Bước 1.** Phát hiện tất cả các **nguyên nhân nguyên tố cốt yếu**.

**Bước 2.** Xóa tất cả các **cột** đã được phủ bởi các nguyên tố cốt yếu.

**Bước 3.** Trong bảng còn lại, xóa nốt những **dòng** không còn dấu `+`. Nếu có **hai cột giống nhau** thì xóa bớt một cột.

**Bước 4.** Trên phần còn lại, tìm một hệ $$S$$ các nguyên nhân nguyên tố với **số hạng / số biến ít nhất** vẫn phủ các cột còn lại.

Kết quả: $$F$$ viết thành tổng các nguyên nhân trong (các nguyên tố cốt yếu) ∪ $$S$$ — đó là **dạng tổng chuẩn tắc tối thiểu** (SOP tối tiểu).

Trên K-map, các bước tương ứng là chọn tế bào cốt yếu rồi hoàn tất phủ (Mục 13.4).

## 4. Don't-care trong Quine–McCluskey

Đôi khi đặc tả **không quan tâm** đầu ra tại vài tổ hợp (mã không dùng, trạng thái không tới). Các vị trí đó gọi là **don't-care**, ký hiệu $$d$$ hoặc $$X$$.

Cách dùng trong QM rất rõ nếu tách theo phần:

- **Phần 1 (thu gọn):** đưa don't-care vào danh sách **như thể** chúng là nguyên nhân hạng $$n$$. Chúng giúp tạo nguyên nhân nguyên tố **lớn hơn** (ít litera hơn).
- **Phần 2 (tối thiểu):** **không** mở cột cho don't-care — ta **không bắt buộc** phủ chúng.

Như vậy $$X$$ chỉ dùng để sinh hạng gọn hơn; không bắt buộc xuất hiện trong cover tối thiểu.

<div class="textbook-example" markdown="1">

**Ví dụ phác (3 biến).** Cho $$F(a,b,c)$$ bằng **1** tại các hàng **1, 2, 5**; don't-care tại **0, 7**.

Ở phần 1, ta dán cả $$0$$ và $$7$$ cùng các minterm thật. Ở phần 2, bảng phủ **chỉ** có cột $$1$$, $$2$$, $$5$$. Một cover tối ưu thường gặp là

$$
F = \bar a\,\bar c + \bar b\,c
$$

Đối chiếu bằng bảng chân trị tám dòng.

</div>

## 5. Ví dụ bốn biến

Xét $$F(a,b,c,d)$$ bằng **1** tại các hàng **0, 2, 3, 5, 7, 8, 10, 11, 13, 15**.

Sau khi nhóm theo số bit 1 và dán cặp, các nguyên nhân nguyên tố điển hình gồm $$cd$$, $$bd$$, $$\bar b\,\bar d$$. Trên bảng phủ, $$\bar b\,\bar d$$ thường **cốt yếu** vì phủ cụm $$0,2,8,10$$; sau đó chọn thêm $$cd$$ (hoặc $$bd$$) để phủ nốt. Một kết quả tối tiểu:

$$
F = cd + \bar b\,\bar d.
$$

Hai thao tác then chốt của phương pháp: đánh dấu `*` sau mỗi phép dán (phần 1), và tìm cột chỉ còn một dấu `+` để xác định nguyên tố cốt yếu (phần 2).

## 5b. Ví dụ đầy đủ — hàm $$F_1$$

Phần dưới trình bày lời giải chi tiết với đủ bảng. Dạng đề điển hình: cho SOP (tổng các tích) dài, yêu cầu rút gọn bằng Quine–McCluskey.

<div class="textbook-example" markdown="1">

**Đề.** Cho

$$
\begin{aligned}
F_1
&=
\overline{w}\,xy\,\overline{z}
+\overline{w}\,x\,\overline{y}\,z
+\overline{w}\,xyz
+w\,\overline{x}\,\overline{y}\,z
+w\,\overline{x}\,yz
+wxyz.
\end{aligned}
$$

Hãy tối thiểu hóa $$F_1$$ bằng Quine–McCluskey (cả hai phần). Quy ước thứ tự biến $$wxyz$$ (bit cao đến thấp).

### Bước 0 — Đổi mỗi hạng thành nguyên nhân hạng $$n$$ (minterm)

Trước khi lập bảng, cần biết **hàm bằng 1 ở những hàng nào**. Với mỗi tích đầy đủ bốn litera:

- biến **không** gạch trên → bit **1**;
- biến **có** gạch trên → bit **0**;
- đọc bốn bit như một số thập phân → chỉ số minterm.

| Hạng trong $$F_1$$ | Mã $$wxyz$$ | Nguyên nhân hạng $$n$$ |
|:---|:---:|:---:|
| $$\overline{w}xy\overline{z}$$ | $$0110$$ | $$m_6$$ |
| $$\overline{w}x\overline{y}z$$ | $$0101$$ | $$m_5$$ |
| $$\overline{w}xyz$$ | $$0111$$ | $$m_7$$ |
| $$w\overline{x}\overline{y}z$$ | $$1001$$ | $$m_9$$ |
| $$w\overline{x}yz$$ | $$1011$$ | $$m_{11}$$ |
| $$wxyz$$ | $$1111$$ | $$m_{15}$$ |

Vậy $$F_1$$ bằng **1** tại các hàng **5, 6, 7, 9, 11, 15**.

Đề có đúng **sáu** hạng và **không** don't-care — sáu minterm trên chính là toàn bộ chỗ $$F_1 = 1$$ (dạng nối rời chính tắc của $$F_1$$).

### Phần 1 — Nhóm theo số bit 1 (Bước 1)

| Nhóm (số bit 1) | Minterm | Mã $$wxyz$$ |
|:---:|:---:|:---:|
| 2 | 5 | $$0101$$ |
| 2 | 6 | $$0110$$ |
| 2 | 9 | $$1001$$ |
| 3 | 7 | $$0111$$ |
| 3 | 11 | $$1011$$ |
| 4 | 15 | $$1111$$ |

### Phần 1 — Phép dán lần 1 (Bước 2)

Chỉ so **nhóm 2 với nhóm 3**, rồi **nhóm 3 với nhóm 4**. Hai mã dán được khi khác đúng một bit: bit khác nhau thay bằng `-`, và ta gắn dấu `*` cho mọi biểu diễn đã tham gia dán.

| Cặp dán | Mã mới | Phủ các minterm | Tích tương ứng |
|:---|:---:|:---:|:---|
| $$5$$ với $$7$$ | $$01{-}1$$ | $$5,7$$ | $$\overline{w}\,x\,z$$ ($$y$$ tự do) |
| $$6$$ với $$7$$ | $$011{-}$$ | $$6,7$$ | $$\overline{w}\,xy$$ ($$z$$ tự do) |
| $$9$$ với $$11$$ | $$10{-}1$$ | $$9,11$$ | $$w\,\overline{x}\,z$$ ($$y$$ tự do) |
| $$7$$ với $$15$$ | $${-}111$$ | $$7,15$$ | $$xyz$$ ($$w$$ tự do) |
| $$11$$ với $$15$$ | $$1{-}11$$ | $$11,15$$ | $$wyz$$ ($$x$$ tự do) |

Vì **mọi** minterm $$5,6,7,9,11,15$$ đều đã được dùng trong ít nhất một cặp, không còn minterm đơn nào (không `*`) là nguyên nhân nguyên tố.

### Phần 1 — Có dán lần 2 không? (Bước 3)

Hai mã đã có `-` chỉ dán tiếp được khi:

1. các dấu `-` nằm **cùng vị trí**, và  
2. phần bit còn lại khác **đúng một** chỗ.

Với các mã vừa thu được:

- $$01{-}1$$ và $$10{-}1$$ có `-` cùng cột, nhưng phần còn lại $$01$$ so với $$10$$ khác **hai** bit → **không** dán;
- các cặp khác thường lệch vị trí `-` (ví dụ $$011{-}$$ với $${-}111$$) → **không** dán.

Do đó **không** sinh được nguyên nhân phủ 4 minterm. Cả **năm** mã 2-ô ở bảng trên đều không bị đánh dấu `*` thêm, nên cả năm là **nguyên nhân nguyên tố**:

| Ký hiệu | Mã | Tích (nguyên nhân nguyên tố) | Phủ |
|:---:|:---:|:---|:---|
| $$N_1$$ | $$01{-}1$$ | $$\overline{w}\,xz$$ | $$5,7$$ |
| $$N_2$$ | $$011{-}$$ | $$\overline{w}\,xy$$ | $$6,7$$ |
| $$N_3$$ | $$10{-}1$$ | $$w\overline{x}z$$ | $$9,11$$ |
| $$N_4$$ | $${-}111$$ | $$xyz$$ | $$7,15$$ |
| $$N_5$$ | $$1{-}11$$ | $$wyz$$ | $$11,15$$ |

*(Ký hiệu $$N_i$$ = nguyên nhân nguyên tố thứ $$i$$ — tránh chữ cái tiếng Anh.)*

### Phần 2 — Bảng phủ

Hàng là nguyên nhân nguyên tố; cột là minterm bắt buộc; dấu `+` nghĩa là “hàng này phủ cột đó”.

| Nguyên nhân nguyên tố | 5 | 6 | 7 | 9 | 11 | 15 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $$N_1=\overline{w}xz$$ | + |  | + |  |  |  |
| $$N_2=\overline{w}xy$$ |  | + | + |  |  |  |
| $$N_3=w\overline{x}z$$ |  |  |  | + | + |  |
| $$N_4=xyz$$ |  |  | + |  |  | + |
| $$N_5=wyz$$ |  |  |  |  | + | + |

### Phần 2 — Tìm nguyên tố cốt yếu (Bước 1)

Xem từng cột: nếu chỉ có **một** dấu `+` thì nguyên nhân đó **bắt buộc** (cốt yếu).

| Cột minterm | Ai phủ? | Kết luận |
|:---:|:---|:---|
| 5 | chỉ $$N_1$$ | $$N_1$$ **cốt yếu** |
| 6 | chỉ $$N_2$$ | $$N_2$$ **cốt yếu** |
| 9 | chỉ $$N_3$$ | $$N_3$$ **cốt yếu** |
| 7 | $$N_1$$, $$N_2$$, $$N_4$$ | chưa buộc thêm |
| 11 | $$N_3$$, $$N_5$$ | chưa buộc thêm |
| 15 | $$N_4$$, $$N_5$$ | chưa buộc thêm |

Chọn ba nguyên tố cốt yếu $$N_1$$, $$N_2$$, $$N_3$$ (Bước 2: xóa các cột đã phủ):

- $$N_1$$ phủ $$5$$ và $$7$$;
- $$N_2$$ phủ $$6$$ và $$7$$;
- $$N_3$$ phủ $$9$$ và $$11$$.

Các minterm đã xong: $$5,6,7,9,11$$. **Còn lại** duy nhất cột $$15$$.

### Phần 2 — Phủ nốt $$m_{15}$$ (Bước 3–4)

Cột $$15$$ có hai lựa chọn ngang nhau: $$N_4=xyz$$ hoặc $$N_5=wyz$$. Chọn **một** trong hai đều cho cover tối tiểu (cùng 4 hạng tích):

$$
\begin{aligned}
F_1
&= \overline{w}\,xz + \overline{w}\,xy + w\overline{x}z + xyz, \\[0.4em]
F_1
&= \overline{w}\,xz + \overline{w}\,xy + w\overline{x}z + wyz.
\end{aligned}
$$

Nếu muốn viết gọn hơn (cùng hàm), có thể gom nhân tử:

$$
\begin{aligned}
F_1
&= \overline{w}\,x(y+z) + w\overline{x}z + xyz, \\[0.4em]
F_1
&= \overline{w}\,x(y+z) + wz(\overline{x}+y).
\end{aligned}
$$

Lưu ý: **không** có cover chỉ với 3 hạng — vì đã buộc chọn ba nguyên tố cốt yếu, mà $$m_{15}$$ vẫn cần thêm đúng một nguyên nhân nguyên tố nữa.

### Kiểm chứng nhanh

- Biểu thức gốc có **6** hạng; cover tối tiểu còn **4** tích (rút rõ).
- Tại $$m_{15}$$ ($$wxyz=1111$$): cả hai dạng đều bằng **1** nhờ $$xyz$$ hoặc $$wyz$$.
- Tại $$m_5$$ ($$0101$$): chỉ hạng $$\overline{w}xz$$ bằng **1**.
- Tại $$m_0$$ ($$0000$$): mọi hạng bằng **0** — đúng vì $$0$$ không thuộc tập minterm.

Cùng tập minterm **5, 6, 7, 9, 11, 15** trên K-map bốn biến cho các nhóm tương ứng $$N_1,\ldots,N_5$$; bảng Quine–McCluskey biểu diễn cùng phép gộp dưới dạng dán bit.

</div>

## 6. So sánh với K-map

| Phương pháp | Đặc trưng | Phạm vi điển hình |
|:---|:---|:---|
| K-map | Trực quan trên lưới | 2–4 biến |
| Quine–McCluskey | Bảng, phép dán, bảng phủ | Thuật toán hóa; số biến lớn hơn |
| Phần mềm hỗ trợ | Tự động hóa cùng khung khái niệm | Quy mô lớn |

Cốt lõi chung của hai phương pháp là **dán các nguyên nhân kề (khác một bit)** rồi **chọn một phủ đủ và gọn**.

<div class="interactive-demo" markdown="1">
<div data-demo="quine-mccluskey-simplifier"></div>
</div>
<script src="{{ '/public/js/quine-mccluskey-simplifier.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Chạy Quine–McCluskey (làm tay) cho

$$F(a,b,c,d)$$ bằng **1** tại các hàng **0, 2, 3, 5, 7, 8, 10, 11, 13, 15**

và nêu các **nguyên nhân nguyên tố cốt yếu**.

<details>
<summary>Đáp án</summary>

Tham khảo mục 5. Một cover tối tiểu thường gặp: $$F = cd + \bar b\,\bar d$$. Nguyên nhân $$\bar b\,\bar d$$ thường cốt yếu vì phủ cụm $$0,2,8,10$$.

</details>

### Bài tập 2

Cho $$F(a,b,c)$$ bằng **1** tại các hàng **1, 2, 5**; don't-care tại **0, 7**. Hoàn tất phần 1 và phần 2 (nhớ: don't-care chỉ giúp dán ở phần 1).

<details>
<summary>Đáp án</summary>

Một cover tối ưu thường gặp: $$F = \bar a\,\bar c + \bar b\,c$$. Đối chiếu bằng bảng tám dòng.

</details>

### Bài tập 3

Cho $$F(x,y,z)$$ bằng **1** tại các hàng **0, 1, 4, 5, 6**. Làm bằng **K-map** và bằng **Quine–McCluskey**, rồi so sánh SOP (tổng các tích) thu được.

<details>
<summary>Đáp án</summary>

Hai phương pháp phải cho **cùng hàm** (có thể khác cách viết hạng nhưng tương đương). Một dạng thường gặp: $$F = \bar x\,\bar z + x\bar y + y\bar z$$ — kiểm lại trên bảng 8 dòng.

</details>

### Bài tập 4 — $$F_1$$ (xem lời giải đầy đủ ở mục 5b)

Cho

$$
\begin{aligned}
F_1
&=
\overline{w}xy\overline{z}
+\overline{w}x\overline{y}z
+\overline{w}xyz
+w\overline{x}\overline{y}z
+w\overline{x}yz
+wxyz.
\end{aligned}
$$

1. Liệt kê các hàng $$F_1=1$$ (dạng nối rời chính tắc) với thứ tự bit $$wxyz$$.
2. Chạy **phần 1**: nhóm, phép dán, liệt kê mọi **nguyên nhân nguyên tố**.
3. Lập **bảng phủ**, chỉ ra **nguyên tố cốt yếu**, hoàn tất cover.
4. Viết ít nhất một SOP (tổng các tích) tối tiểu; nêu cover tối tiểu thứ hai nếu có.

<details>
<summary>Đáp án chi tiết</summary>

**1. Chuyển sang nguyên nhân hạng $$n$$ (minterm)**

| Hạng | $$wxyz$$ | $$m$$ |
|:---|:---:|:---:|
| $$\overline{w}xy\overline{z}$$ | $$0110$$ | 6 |
| $$\overline{w}x\overline{y}z$$ | $$0101$$ | 5 |
| $$\overline{w}xyz$$ | $$0111$$ | 7 |
| $$w\overline{x}\overline{y}z$$ | $$1001$$ | 9 |
| $$w\overline{x}yz$$ | $$1011$$ | 11 |
| $$wxyz$$ | $$1111$$ | 15 |

Vậy $$F_1$$ bằng **1** tại các hàng **5, 6, 7, 9, 11, 15**.

**2. Phần 1 — phép dán**

Nhóm theo số bit 1: $$\{5,6,9\}$$ (2 bit), $$\{7,11\}$$ (3 bit), $$\{15\}$$ (4 bit).

Các **nguyên nhân nguyên tố** (không dán được thành nhóm 4 ô):

| Mã | Tích | Phủ |
|:---:|:---|:---|
| $$01{-}1$$ | $$\overline{w}xz$$ | 5, 7 |
| $$011{-}$$ | $$\overline{w}xy$$ | 6, 7 |
| $$10{-}1$$ | $$w\overline{x}z$$ | 9, 11 |
| $${-}111$$ | $$xyz$$ | 7, 15 |
| $$1{-}11$$ | $$wyz$$ | 11, 15 |

**3. Phần 2 — bảng phủ**

|  | 5 | 6 | 7 | 9 | 11 | 15 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $$\overline{w}xz$$ | + |  | + |  |  |  |
| $$\overline{w}xy$$ |  | + | + |  |  |  |
| $$w\overline{x}z$$ |  |  |  | + | + |  |
| $$xyz$$ |  |  | + |  |  | + |
| $$wyz$$ |  |  |  |  | + | + |

Cốt yếu: cột 5 → $$\overline{w}xz$$; cột 6 → $$\overline{w}xy$$; cột 9 → $$w\overline{x}z$$.  
Ba nguyên nhân này phủ $$5,6,7,9,11$$. Còn $$15$$ → chọn **$$xyz$$** hoặc **$$wyz$$**.

**4. SOP tối tiểu** (hai cover tương đương)

$$
F_1 = \overline{w}xz + \overline{w}xy + w\overline{x}z + xyz
$$

hoặc

$$
F_1 = \overline{w}xz + \overline{w}xy + w\overline{x}z + wyz.
$$

Có thể gom:

$$
F_1 = \overline{w}x(y+z) + w\overline{x}z + xyz
= \overline{w}x(y+z) + wz(\overline{x}+y).
$$

Xem thêm **mục 5b** để đối chiếu từng bảng và phần kiểm chứng.

</details>

## Xem thêm

- Mục 13.4 — bản đồ Karnaugh (tế bào lớn ↔ nguyên nhân nguyên tố).  
- Mục 13.2 — dạng nối rời chính tắc (SOP chuẩn).  
- Mục 13.6 — bối cảnh ứng dụng.

## Tóm tắt

1. Quine–McCluskey tối thiểu hóa hàm Boolean bằng **bảng**, hữu ích khi số biến lớn hơn phạm vi K-map.  
2. **Phần 1** (dạng tổng chuẩn tắc thu gọn): phép **dán** các nguyên nhân hạng $$n$$ khác đúng một bit; biểu diễn không có dấu `*` là **nguyên nhân nguyên tố**.  
3. **Phần 2** (dạng tổng chuẩn tắc tối thiểu): **bảng phủ**, chọn **nguyên tố cốt yếu**, rồi phủ nốt phần còn lại.  
4. **Don't-care** chỉ tham gia phần 1; phần 2 không bắt buộc phủ chúng.  
5. K-map và Quine–McCluskey cùng khung “dán rồi phủ”, khác về hình thức trình bày và quy mô áp dụng.
