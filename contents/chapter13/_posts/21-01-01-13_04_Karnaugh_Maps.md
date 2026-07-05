---

layout: post
title: "Bản đồ Karnaugh và Tối thiểu hóa Trực quan"
categories: chapter13
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã tối thiểu hóa hàm Boole bằng biến đổi đại số. Mục này giới thiệu bản đồ Karnaugh (K-map) — phương pháp trực quan nhóm các minterm kề…"
---

Ở mục trước chúng ta đã tối thiểu hóa hàm Boole bằng biến đổi đại số. Mục này giới thiệu **bản đồ Karnaugh** (K-map) — phương pháp trực quan nhóm các minterm kề nhau để rút gọn biểu thức. Với 2–4 biến, K-map cung cấp cách có hệ thống để tìm biểu thức tối tiểu mà không cần thao tác đại số dài dòng.

![Bản đồ Karnaugh 4 biến](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

<p class="textbook-figure-caption" data-figure="13.16">K-map sắp xếp minterm theo mã Gray — ô kề chỉ khác đúng một biến.</p>
![Mã Gray](/discrete-mathematics-for-computer-science-iuh/img/course/gray_code.svg)

<p class="textbook-figure-caption" data-figure="13.17">Mã Gray đảm bảo hai giá trị liên tiếp chỉ khác một bit — nền tảng sắp xếp hàng/cột K-map.</p>
**Mã Gray (Gray Code).**
Mã Gray là một loại mã nhị phân trong đó hai giá trị liên tiếp chỉ khác nhau một bit. 
Điều này rất hữu ích trong các ứng dụng như mạch giải mã vị trí (encoder) hoặc các hệ thống cần giảm thiểu lỗi khi chuyển trạng thái.

Khi xây dựng bản đồ Karnaugh, một điểm quan trọng là thứ tự sắp xếp các biến trên trục (hàng và cột). Mã Gray thường được sử dụng để sắp xếp thứ tự các giá trị của các biến này, bởi vì:
Trong mã Gray, hai giá trị liên tiếp chỉ khác nhau một bit. Điều này giúp bản đồ Karnaugh duy trì tính liên kết logic: các ô liền kề chỉ khác nhau bởi một biến đầu vào.

![Từ K-map sang mạch](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

<p class="textbook-figure-caption" data-figure="13.18">Biểu thức tối tiểu từ K-map được hiện thực bằng cổng logic.</p>
**Xây dựng bản đồ Karnaugh.**
- Số lượng biến logic trong biểu thức sẽ quyết định kích thước bản đồ Karnaugh.
- Mã Gray được sử dụng để đánh số hàng và cột trong bản đồ để đảm bảo các ô liền kề chỉ khác nhau 1 bit.
- Điền giá trị đầu ra vào bản đồ
- Đánh dấu các ô có dòng tương ứng trên bảng chân trị là 1

Sau đó nhóm các ô 1 liền kề (số ô phải là lũy thừa của 2) để loại biến.

![Implicant nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

<p class="textbook-figure-caption" data-figure="13.19">Nhóm lớn nhất trên K-map tương ứng prime implicant — hạng tích không thể thu gọn thêm.</p>
![Don't-care conditions](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="13.20">Ô don't-care (X) linh hoạt chọn 0 hoặc 1 để tạo nhóm lớn hơn và biểu thức ngắn hơn.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** bản đồ Karnaugh cho hàm 2, 3 và 4 biến.
- **Xác định** các nhóm (implicant) trên K-map đúng quy tắc.
- **Tìm** biểu thức tối tiểu dạng SOP từ K-map.
- **Xử lý** các điều kiện "không cần quan tâm" (don't-care conditions).
- **So sánh** K-map với phương pháp tối thiểu hóa đại số.

**Từ khóa**: Bản đồ Karnaugh (Karnaugh map), ô kề (adjacent cell), implicant nguyên tố (prime implicant), don't-care, biểu thức tối tiểu (minimal expression).
</div>

## Mã Gray (Gray Code)

Mã Gray là hệ thống mã nhị phân trong đó hai giá trị liên tiếp chỉ khác nhau **đúng một bit**. Điều này rất quan trọng trong bản đồ Karnaugh vì nó đảm bảo các ô kề nhau chỉ khác nhau một biến.

### Tại sao mã Gray quan trọng?

Trong mã nhị phân thông thường, khi chuyển từ một số sang số tiếp theo, nhiều bit có thể thay đổi đồng thời. Ví dụ, từ 0111 (7) sang 1000 (8), cả 4 bit đều thay đổi. Điều này gây ra vấn đề trong các mạch số vì các bit không thay đổi chính xác cùng một lúc, dẫn đến trạng thái trung gian sai.

Mã Gray giải quyết vấn đề này bằng cách đảm bảo mỗi bước chỉ thay đổi **đúng một bit**, loại bỏ hoàn toàn lỗi trạng thái trung gian.

### So sánh mã Gray và mã nhị phân thông thường

**Ví dụ 2 bit**:

| Số thập phân | Mã nhị phân | Số bit thay đổi | Mã Gray | Số bit thay đổi |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 00 | - | 00 | - |
| 1 | 01 | 1 | 01 | 1 |
| 2 | 10 | 2 | 11 | 1 |
| 3 | 11 | 1 | 10 | 1 |

Trong mã nhị phân thông thường, từ 01 (1) sang 10 (2) có **2 bit thay đổi**. Trong mã Gray, mỗi bước chỉ thay đổi 1 bit: 00 → 01 → 11 → 10.

**Ví dụ 3 bit**:

| Số thập phân | Mã nhị phân | Mã Gray |
|:---:|:---:|:---:|
| 0 | 000 | 000 |
| 1 | 001 | 001 |
| 2 | 010 | 011 |
| 3 | 011 | 010 |
| 4 | 100 | 110 |
| 5 | 101 | 111 |
| 6 | 110 | 101 |
| 7 | 111 | 100 |

### Các tính chất của mã Gray

1. **Tính duy nhất**: Mỗi số nguyên có đúng một mã Gray tương ứng.
2. **Tính chu kỳ**: Mã Gray cuối cùng (10...0) chỉ khác mã Gray đầu tiên (00...0) đúng một bit, tạo thành chu trình khép kín.
3. **Tính đối xứng**: Mã Gray có tính đối xứng qua trung tâm.
4. **Độ dài bit**: Với $$n$$ bit, mã Gray biểu diễn được $$2^n$$ giá trị từ 0 đến $$2^n - 1$$.

### Công thức chuyển đổi

#### Từ mã nhị phân sang mã Gray

Cho mã nhị phân $$b_{n-1}b_{n-2}\ldots b_1b_0$$, mã Gray tương ứng $$g_{n-1}g_{n-2}\ldots g_1g_0$$ được tính bằng:

$$g_{n-1} = b_{n-1}$$ (bit cao nhất giữ nguyên)

$$g_i = b_{i+1} \oplus b_i$$ cho $$i = 0, 1, \ldots, n-2$$

Trong đó $$\oplus$$ là phép XOR (phép cộng modulo 2).

<div class="textbook-example" markdown="1">
**Ví dụ**: Chuyển mã nhị phân $$1011_2$$ sang mã Gray:
- $$g_3 = b_3 = 1$$
- $$g_2 = b_3 \oplus b_2 = 1 \oplus 0 = 1$$
- $$g_1 = b_2 \oplus b_1 = 0 \oplus 1 = 1$$
- $$g_0 = b_1 \oplus b_0 = 1 \oplus 1 = 0$$

Kết quả: $$1011_2 \rightarrow 1110_{\text{Gray}}$$
</div>

## Giới thiệu Bản đồ Karnaugh

### Tại sao cần K-map?

Tối thiểu hóa bằng đại số đòi hỏi kinh nghiệm và sự tinh tế. Với các hàm có 2-4 biến, K-map cung cấp một phương pháp trực quan có hệ thống:

- Các ô trên K-map được sắp xếp sao cho ô kề nhau khác nhau đúng một biến.
- Nhóm các ô có giá trị 1 lại với nhau để tạo thành các tích đơn giản hơn.

### K-map 2 biến

Cho hai biến $$x, y$$:

| | $$y = 0$$ | $$y = 1$$ |
|---|:---:|:---:|
| $$x = 0$$ | $$x'y'$$ | $$x'y$$ |
| $$x = 1$$ | $$xy'$$ | $$xy$$ |

Ví dụ: $$F(x, y) = x'y' + x'y + xy$$

| | $$y = 0$$ | $$y = 1$$ |
|---|:---:|:---:|
| $$x = 0$$ | 1 | 1 |
| $$x = 1$$ | 0 | 1 |

Nhóm: cột $$y = 1$$ (cả 2 ô) $$= y$$, và ô $$(x=0, y=0)$$ tách riêng $$= x'y'$$

Kết quả: $$F = y + x'y'$$

<div class="content-box info-box textbook-block" markdown="1">
**Quy tắc nhóm trên K-map**:
1. Nhóm chỉ gồm các ô có giá trị 1 (hoặc don't-care).
2. Nhóm phải là hình chữ nhật với kích thước là lũy thừa của 2 (1, 2, 4, 8, ...).
3. Nhóm càng lớn càng tốt (càng ít biến trong tích).
4. Nhóm có thể chồng lên nhau.
5. Các ô ở biên đối diện được coi là kề nhau (wrap-around).
</div>

## K-map 3 biến

Với ba biến $$x, y, z$$, K-map có 8 ô được sắp xếp:

| $$xy$$ \ $$z$$ | $$z = 0$$ | $$z = 1$$ |
|:---:|:---:|:---:|
| $$00$$ | $$x'y'z'$$ | $$x'y'z$$ |
| $$01$$ | $$x'yz'$$ | $$x'yz$$ |
| $$11$$ | $$xyz'$$ | $$xyz$$ |
| $$10$$ | $$xy'z'$$ | $$xy'z$$ |

Chú ý: các hàng được sắp xếp theo mã Gray (00, 01, 11, 10) để đảm bảo tính kề nhau.

<div class="textbook-example" markdown="1">
**Ví dụ** 1: Tối thiểu hóa 3 biến:

Cho hàm $$F(x, y, z) = \sum m(0, 1, 2, 5, 7)$$:

| $$xy$$ \ $$z$$ | $$0$$ | $$1$$ |
|:---:|:---:|:---:|
| $$00$$ | 1 | 1 |
| $$01$$ | 1 | 0 |
| $$11$$ | 0 | 1 |
| $$10$$ | 0 | 1 |

Xác định các nhóm:
- Nhóm 1: hai ô ở hàng $$xy = 00$$ ($$z = 0, 1$$): $$x'y'$$
- Nhóm 2: ô $$(xy = 01, z = 0)$$ và ô $$(xy = 00, z = 0)$$: $$x'z'$$
- Nhóm 3: ô $$(xy = 10, z = 1)$$ và ô $$(xy = 11, z = 1)$$: $$xz$$

Kết quả: $$F = x'y' + x'z' + xz$$
</div>

## K-map 4 biến

Với bốn biến $$x, y, z, w$$, K-map có 16 ô:

| $$xy$$ \ $$zw$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | $$x'y'z'w'$$ | $$x'y'z'w$$ | $$x'y'zw$$ | $$x'y'zw'$$ |
| $$01$$ | $$x'yz'w'$$ | $$x'yz'w$$ | $$x'yzw$$ | $$x'yzw'$$ |
| $$11$$ | $$xyz'w'$$ | $$xyz'w$$ | $$xyzw$$ | $$xyzw'$$ |
| $$10$$ | $$xy'z'w'$$ | $$xy'z'w$$ | $$xy'zw$$ | $$xy'zw'$$ |

<div class="textbook-example" markdown="1">
**Ví dụ** 2: Tối thiểu hóa 4 biến:

Cho hàm $$F(x, y, z, w) = \sum m(0, 1, 2, 5, 6, 7, 8, 9, 10, 14)$$:

| $$xy$$ \ $$zw$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | 1 | 1 | 0 | 1 |
| $$01$$ | 0 | 1 | 1 | 1 |
| $$11$$ | 0 | 0 | 0 | 1 |
| $$10$$ | 1 | 1 | 0 | 1 |

Xác định các nhóm:
- Nhóm lớn: 4 ô ở góc (00,00), (00,10), (10,00), (10,10): $$z'w'$$
- Nhóm 2: ô (00,01) và (10,01): $$x'w$$
- Nhóm 2: ô (01,01) và (01,11): $$x'yz$$
- Nhóm 2: ô (01,10) và (11,10): $$yzw'$$

Kết quả: $$F = z'w' + x'w + x'yz + yzw'$$
</div>

## Điều kiện Don't-care

Trong thực tế, có những trường hợp hàm Boole không quan tâm đến giá trị đầu ra. Các điều kiện này được gọi là **don't-care conditions** và được ký hiệu bằng $$X$$ trên K-map.

Don't-care giúp việc nhóm trở nên linh hoạt hơn vì chúng ta có thể coi chúng là 0 hoặc 1 tùy lợi.

<div class="textbook-example" markdown="1">
**Ví dụ** 3: Sử dụng Don't-care:

Cho hàm $$F(x, y, z) = \sum m(0, 1, 3) + \sum d(5, 7)$$, trong đó $$d$$ là don't-care:

| $$xy$$ \ $$z$$ | $$0$$ | $$1$$ |
|:---:|:---:|:---:|
| $$00$$ | 1 | 1 |
| $$01$$ | 0 | X |
| $$11$$ | 0 | X |
| $$10$$ | 0 | 0 |

Chúng ta có thể nhóm:
- Nhóm 1: ô (00,0) và (00,1): $$x'y'$$
- Nhóm 2: ô (00,1), (01,1), (11,1), (10,1) sử dụng don't-care: $$z$$

Kết quả: $$F = x'y' + z$$
</div>

## So sánh K-map với tối thiểu hóa đại số

| Tiêu chí | K-map | Đại số Boole |
|---|---|---|
| Phạm vi | 2-4 biến hiệu quả | Mọi số biến |
| Tính trực quan | Cao | Thấp |
| Tốc độ | Nhanh với số biến nhỏ | Chậm hơn |
| Độ chính xác | Đúng tuyệt đối | Phụ thuộc kỹ năng |
| Ứng dụng | Thiết kế mạch cơ bản | Chứng minh, phát triển lý thuyết |

## Bài tập

### Bài tập 1: Xây dựng mã Gray

1. Xây dựng danh sách mã Gray 4 bit bằng phương pháp phản chiếu.
2. Chuyển mã nhị phân $$1101_2$$ sang mã Gray.
3. Chuyển mã Gray $$1011$$ sang mã nhị phân.

### Bài tập 2: Sử dụng K-map

1. Tối thiểu hóa hàm $$F(x, y) = \sum m(0, 2, 3)$$ bằng K-map 2 biến.
2. Tối thiểu hóa hàm $$F(x, y, z) = \sum m(0, 1, 2, 4, 5)$$ bằng K-map 3 biến.
3. Tối thiểu hóa hàm $$F(x, y, z, w) = \sum m(0, 1, 2, 3, 8, 9, 10, 11)$$ bằng K-map 4 biến.

### Bài tập 3: Don't-care conditions

1. Tối thiểu hóa hàm $$F(x, y, z) = \sum m(0, 1, 5) + \sum d(2, 7)$$.
2. Tìm hàm Boole đơn giản nhất thỏa mãn bảng chân trị sau với don't-care:

| $$x$$ | $$y$$ | $$z$$ | $$F$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | X |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | X |
| 1 | 1 | 1 | 1 |

## Xem thêm / Video gợi ý

- [Boolean Algebra and Karnaugh Maps](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Neso Academy (Gate level + minimization)

## Tóm tắt

- **Mã Gray**: hai giá trị liên tiếp chỉ khác một bit; dùng để sắp xếp hàng và cột trên K-map.
- **Bản đồ Karnaugh**: phương pháp trực quan tối thiểu hóa hàm Boole với 2–4 biến.
- **Quy tắc nhóm**: nhóm các ô 1 (hoặc don't-care) thành hình chữ nhật có kích thước lũy thừa của 2; ưu tiên nhóm lớn nhất.
- **Don't-care**: các tổ hợp đầu vào không quan tâm giúp tạo nhóm lớn hơn và biểu thức ngắn hơn.
- **So sánh**: K-map trực quan và nhanh với ít biến; đại số Boole và Quine–McCluskey phù hợp khi số biến tăng.

Trong bài tiếp theo, chúng ta sẽ học phương pháp Quine–McCluskey — phiên bản thuật toán của tối thiểu hóa hàm Boole.
