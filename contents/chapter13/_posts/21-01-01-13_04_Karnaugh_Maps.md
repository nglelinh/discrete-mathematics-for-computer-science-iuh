---
layout: post
title: "Bản đồ Karnaugh và Tối thiểu hóa Trực quan"
categories: chapter13
date: 2021-01-01
order: 4
required: true
lang: en
---

Có những biểu thức Boole đủ nhỏ để ta không cần lao ngay vào thuật toán đầy đủ. Chỉ cần sắp xếp các giá trị đầu ra theo một bảng đặc biệt, những vùng có thể gộp sẽ lộ ra rất trực quan. Đó là lý do **bản đồ Karnaugh** được dùng rất nhiều trong thiết kế logic cơ bản.

Đại số Boole nối logic với phần cứng và tối ưu biểu thức, vì vậy phần này vừa có ý nghĩa toán học vừa rất gần với thiết kế mạch và điều kiện trong code.
K-map biến việc tối thiểu hóa từ một chuỗi biến đổi đại số dễ nhầm thành một thao tác quan sát có quy tắc. Với số biến vừa phải, đây là cách nhanh và sáng sủa để rút gọn biểu thức.

Công cụ này đặc biệt hữu ích cho sinh viên vì nó giúp thấy trực tiếp vì sao các hạng tử được gộp, thay vì chỉ áp công thức máy móc. Từ đó, trực giác về tối thiểu hóa hàm Boole cũng mạnh lên rõ rệt.

Trong bài này, chúng ta sẽ học cách đọc và nhóm ô trên bản đồ Karnaugh, rồi dùng nó để tối thiểu hóa hàm Boole một cách trực quan nhưng vẫn chính xác.

![Bản đồ Karnaugh 4 biến](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

*Hình 13.16: K-map sắp xếp minterm theo mã Gray — ô kề chỉ khác đúng một biến.*

![Mã Gray](/discrete-mathematics-for-computer-science-iuh/img/course/gray_code.svg)

*Hình 13.17: Mã Gray đảm bảo hai giá trị liên tiếp chỉ khác một bit — nền tảng sắp xếp hàng/cột K-map.*

**Mã Gray (Gray Code) từ slide bài giảng:**
Mã Gray là một loại mã nhị phân trong đó hai giá trị liên tiếp chỉ khác nhau một bit. 
Điều này rất hữu ích trong các ứng dụng như mạch giải mã vị trí (encoder) hoặc các hệ thống cần giảm thiểu lỗi khi chuyển trạng thái.

Khi xây dựng bản đồ Karnaugh, một điểm quan trọng là thứ tự sắp xếp các biến trên trục (hàng và cột). Mã Gray thường được sử dụng để sắp xếp thứ tự các giá trị của các biến này, bởi vì:
Trong mã Gray, hai giá trị liên tiếp chỉ khác nhau một bit. Điều này giúp bản đồ Karnaugh duy trì tính liên kết logic: các ô liền kề chỉ khác nhau bởi một biến đầu vào.

![Từ K-map sang mạch](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

*Hình 13.18: Biểu thức tối tiểu từ K-map được hiện thực bằng cổng logic.*

**Xây dựng bản đồ Karnaugh (từ slide bài giảng):**
- Số lượng biến logic trong biểu thức sẽ quyết định kích thước bản đồ Karnaugh.
- Mã Gray được sử dụng để đánh số hàng và cột trong bản đồ để đảm bảo các ô liền kề chỉ khác nhau 1 bit.
- Điền giá trị đầu ra vào bản đồ
- Đánh dấu các ô có dòng tương ứng trên bảng chân trị là 1

Sau đó nhóm các ô 1 liền kề (số ô phải là lũy thừa của 2) để loại biến.

![Implicant nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/Logic_Gates.svg)

*Hình 13.19: Nhóm lớn nhất trên K-map tương ứng prime implicant — hạng tích không thể thu gọn thêm.*

![Don't-care conditions](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

*Hình 13.20: Ô don't-care (X) linh hoạt chọn 0 hoặc 1 để tạo nhóm lớn hơn và biểu thức ngắn hơn.*

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Xây dựng** bản đồ Karnaugh cho hàm 2, 3 và 4 biến.
- **Xác định** các nhóm (implicant) trên K-map đúng quy tắc.
- **Tìm** biểu thức tối tiểu dạng SOP từ K-map.
- **Xử lý** các điều kiện "không cần quan tâm" (don't-care conditions).
- **So sánh** K-map với phương pháp tối thiểu hóa đại số.

**Từ khóa**: Bản đồ Karnaugh (Karnaugh map), ô kề (adjacent cell), implicant nguyên tố (prime implicant), don't-care, biểu thức tối tiểu (minimal expression).

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

**Ví dụ**: Chuyển mã nhị phân $$1011_2$$ sang mã Gray:
- $$g_3 = b_3 = 1$$
- $$g_2 = b_3 \oplus b_2 = 1 \oplus 0 = 1$$
- $$g_1 = b_2 \oplus b_1 = 0 \oplus 1 = 1$$
- $$g_0 = b_1 \oplus b_0 = 1 \oplus 1 = 0$$

Kết quả: $$1011_2 \rightarrow 1110_{\text{Gray}}$$

#### Từ mã Gray sang mã nhị phân

Cho mã Gray $$g_{n-1}g_{n-2}\ldots g_1g_0$$, mã nhị phân tương ứng $$b_{n-1}b_{n-2}\ldots b_1b_0$$ được tính bằng:

$$b_{n-1} = g_{n-1}$$ (bit cao nhất giữ nguyên)

$$b_i = b_{i+1} \oplus g_i$$ cho $$i = 0, 1, \ldots, n-2$$

**Ví dụ**: Chuyển mã Gray $$1110$$ sang mã nhị phân:
- $$b_3 = g_3 = 1$$
- $$b_2 = b_3 \oplus g_2 = 1 \oplus 1 = 0$$
- $$b_1 = b_2 \oplus g_1 = 0 \oplus 1 = 1$$
- $$b_0 = b_1 \oplus g_0 = 1 \oplus 0 = 1$$

Kết quả: $$1110_{\text{Gray}} \rightarrow 1011_2$$

### Cách xây dựng mã Gray theo phương pháp phản chiếu

Đây là phương pháp trực quan để xây dựng mã Gray cho $$n$$ bit:

1. **Bước 1**: Bắt đầu với mã Gray 1 bit: 0, 1
2. **Bước 2**: Với mã $$n$$ bit, lấy mã $$n-1$$ bit, viết xuôi rồi viết ngược
3. **Bước 3**: Thêm 0 vào đầu nửa xuôi, thêm 1 vào đầu nửa ngược

**Ví dụ xây dựng mã Gray 3 bit**:

- **Gray 1 bit**: 0, 1
- **Gray 2 bit**: 
  - Lấy Gray 1 bit: 0, 1
  - Viết xuôi: 0, 1
  - Viết ngược: 1, 0
  - Thêm 0 vào đầu nửa xuôi: 00, 01
  - Thêm 1 vào đầu nửa ngược: 11, 10
  - Kết quả: 00, 01, 11, 10

- **Gray 3 bit**:
  - Lấy Gray 2 bit: 00, 01, 11, 10
  - Viết xuôi: 00, 01, 11, 10
  - Viết ngược: 10, 11, 01, 00
  - Thêm 0 vào đầu nửa xuôi: 000, 001, 011, 010
  - Thêm 1 vào đầu nửa ngược: 110, 111, 101, 100
  - Kết quả: 000, 001, 011, 010, 110, 111, 101, 100

<div class="content-box insight-box" markdown="1">
**Mã Gray trong thực tế**: Mã Gray không chỉ dùng trong K-map. Nó được dùng trong các bộ mã hóa vị trí (rotary encoders), cảm biến góc, và trong giao tiếp giữa các bộ phận của CPU để tránh lỗi khi nhiều bit thay đổi đồng thời. Ứng dụng quan trọng khác bao gồm:
- **Bộ mã hóa vị trí**: Sử dụng trong động cơ servo và robot để xác định góc quay chính xác.
- **Mã hóa tín hiệu**: Tr truyền thông số để giảm lỗi bit.
- **Thiết kế mạch số**: Đảm bảo chuyển trạng thái an toàn trong các FSM (Finite State Machines).
</div>

### Ứng dụng trong bản đồ Karnaugh

Mã Gray được sử dụng trong K-map để đảm bảo tính kề nhau giữa các ô. Khi sắp xếp các hàng và cột theo mã Gray, mỗi ô kề nhau chỉ khác đúng một biến, giúp việc nhóm các ô có giá trị 1 trở nên trực quan hơn.

**Ví dụ**: K-map 4 biến với các hàng và cột được sắp xếp theo mã Gray:

| $$xy$$ \ $$zw$$ | 00 | 01 | 11 | 10 |
|:---:|:---:|:---:|:---:|:---:|
| 00 | $$x'y'z'w'$$ | $$x'y'z'w$$ | $$x'y'zw$$ | $$x'y'zw'$$ |
| 01 | $$x'yz'w'$$ | $$x'yz'w$$ | $$x'yzw$$ | $$x'yzw'$$ |
| 11 | $$xyz'w'$$ | $$xyz'w$$ | $$xyzw$$ | $$xyzw'$$ |
| 10 | $$xy'z'w'$$ | $$xy'z'w$$ | $$xy'zw$$ | $$xy'zw'$$ |

Chú ý: các hàng (00, 01, 11, 10) và cột (00, 01, 11, 10) đều được sắp xếp theo mã Gray.

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

<div class="content-box info-box" markdown="1">
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

### Ví dụ 1: Tối thiểu hóa 3 biến

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

## K-map 4 biến

Với bốn biến $$x, y, z, w$$, K-map có 16 ô:

| $$xy$$ \ $$zw$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | $$x'y'z'w'$$ | $$x'y'z'w$$ | $$x'y'zw$$ | $$x'y'zw'$$ |
| $$01$$ | $$x'yz'w'$$ | $$x'yz'w$$ | $$x'yzw$$ | $$x'yzw'$$ |
| $$11$$ | $$xyz'w'$$ | $$xyz'w$$ | $$xyzw$$ | $$xyzw'$$ |
| $$10$$ | $$xy'z'w'$$ | $$xy'z'w$$ | $$xy'zw$$ | $$xy'zw'$$ |

### Ví dụ 2: Tối thiểu hóa 4 biến

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

## Điều kiện Don't-care

Trong thực tế, có những trường hợp hàm Boole không quan tâm đến giá trị đầu ra. Các điều kiện này được gọi là **don't-care conditions** và được ký hiệu bằng $$X$$ trên K-map.

Don't-care giúp việc nhóm trở nên linh hoạt hơn vì ta có thể coi chúng là 0 hoặc 1 tùy lợi.

### Ví dụ 3: Sử dụng Don't-care

Cho hàm $$F(x, y, z) = \sum m(0, 1, 3) + \sum d(5, 7)$$, trong đó $$d$$ là don't-care:

| $$xy$$ \ $$z$$ | $$0$$ | $$1$$ |
|:---:|:---:|:---:|
| $$00$$ | 1 | 1 |
| $$01$$ | 0 | X |
| $$11$$ | 0 | X |
| $$10$$ | 0 | 0 |

Ta có thể nhóm:
- Nhóm 1: ô (00,0) và (00,1): $$x'y'$$
- Nhóm 2: ô (00,1), (01,1), (11,1), (10,1) sử dụng don't-care: $$z$$

Kết quả: $$F = x'y' + z$$

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

## Kết luận

Trong bài này, chúng ta đã học:

1. **Mã Gray**: Hệ thống mã nhị phân đảm bảo mỗi bước chỉ thay đổi 1 bit, rất quan trọng trong thiết kế mạch số.
2. **Bản đồ Karnaugh**: Phương pháp trực quan để tối thiểu hóa hàm Boole.
3. **Quy tắc nhóm**: Các nguyên tắc để nhóm ô trên K-map.
4. **Điều kiện Don't-care**: Cách tận dụng các giá trị không quan tâm để tối ưu hóa.

Mã Gray và K-map có mối liên hệ chặt chẽ: mã Gray đảm bảo tính kề nhau giữa các ô, trong khi K-map tận dụng tính chất này để nhóm các hạng tử một cách trực quan. Hiểu rõ cả hai sẽ giúp sinh viên thiết kế mạch số hiệu quả hơn và tối thiểu hóa hàm Boole chính xác hơn.

**Từ khóa**: Mã Gray (Gray Code), mã hóa phản chiếu (reflected binary code), bản đồ Karnaugh (Karnaugh map), tối thiểu hóa hàm Boole (Boolean function minimization), implicant nguyên tố (prime implicant), điều kiện don't-care.
