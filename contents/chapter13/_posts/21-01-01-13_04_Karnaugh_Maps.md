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

**So sánh mã Gray và mã nhị phân thông thường cho 2 bit**:

| Số thập phân | Mã nhị phân | Mã Gray |
|:---:|:---:|:---:|
| 0 | 00 | 00 |
| 1 | 01 | 01 |
| 2 | 10 | 11 |
| 3 | 11 | 10 |

Trong mã nhị phân thông thường, từ 01 (1) sang 10 (2) có 2 bit thay đổi. Trong mã Gray, mỗi bước chỉ thay đổi 1 bit: 00 → 01 → 11 → 10.

**Cách xây dựng mã Gray cho $$n$$ bit**:
1. Bắt đầu với mã Gray 1 bit: 0, 1
2. Với mã $$n$$ bit, lấy mã $$n-1$$ bit, viết xuôi rồi viết ngược
3. Thêm 0 vào đầu nửa xuôi, thêm 1 vào đầu nửa ngược

**Ví dụ xây dựng mã Gray 3 bit**:
- Gray 1 bit: 0, 1
- Gray 2 bit: 00, 01, 11, 10
- Gray 3 bit: 000, 001, 011, 010, 110, 111, 101, 100

<div class="content-box insight-box" markdown="1">
**Mã Gray trong thực tế**: Mã Gray không chỉ dùng trong K-map. Nó được dùng trong các bộ mã hóa vị trí (rotary encoders), cảm biến góc, và trong giao tiếp giữa các bộ phận của CPU để tránh lỗi khi nhiều bit thay đổi đồng thời.
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

### Ví dụ 2: Nhóm bao biên

Cho hàm $$F(x, y, z) = \sum m(0, 2, 4, 6)$$:

| $$xy$$ \ $$z$$ | $$0$$ | $$1$$ |
|:---:|:---:|:---:|
| $$00$$ | 1 | 0 |
| $$01$$ | 1 | 0 |
| $$11$$ | 1 | 0 |
| $$10$$ | 1 | 0 |

Cột $$z = 0$$ có 4 ô: toàn bộ cột. Nhưng 4 ô này cũng tạo thành 2 nhóm bao biên:
- Các ô ở biên trái và phải (cột $$z = 0$$) kề nhau qua wrap-around

Tuy nhiên, 4 ô này thực chất là tất cả các tổ hợp với $$z = 0$$:

$$F = z'$$

<div class="content-box warning-box" markdown="1">
**Sai lầm thường gặp**: Sinh viên thường quên quy tắc "wrap-around" — các ô ở cạnh trên kề với cạnh dưới, cạnh trái kề với cạnh phải. Hãy tưởng tượng K-map như một hình xuyến (torus) — các cạnh đối diện thực sự chạm nhau!
</div>

## K-map 4 biến

Với bốn biến $$w, x, y, z$$, K-map có 16 ô:

| $$wx$$ \ $$yz$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | $$w'x'y'z'$$ | $$w'x'y'z$$ | $$w'x'yz$$ | $$w'x'yz'$$ |
| $$01$$ | $$w'xy'z'$$ | $$w'xy'z$$ | $$w'xyz$$ | $$w'xyz'$$ |
| $$11$$ | $$wxy'z'$$ | $$wxy'z$$ | $$wxyz$$ | $$wxyz'$$ |
| $$10$$ | $$wx'y'z'$$ | $$wx'y'z$$ | $$wx'yz$$ | $$wx'yz'$$ |

<div class="interactive-tool" markdown="1">
<div data-demo="kmap-interactive"></div>
</div>
<script src="{{ '/public/js/kmap-interactive.js' | relative_url }}"></script>

### Ví dụ 3: K-map 4 biến

Cho hàm $$F(w, x, y, z) = \sum m(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14)$$:

| $$wx$$ \ $$yz$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | 1 | 1 | 0 | 1 |
| $$01$$ | 1 | 1 | 0 | 1 |
| $$11$$ | 1 | 1 | 0 | 1 |
| $$10$$ | 1 | 1 | 0 | 1 |

Nhìn kỹ, các ô với $$y = 0$$ (cột $$yz = 00, 01, 10$$) đều là 1:

$$F = y'$$

### Ví dụ 4: Tối thiểu hóa phức tạp hơn

Cho $$F(w, x, y, z) = \sum m(0, 2, 8, 10, 12, 14)$$:

| $$wx$$ \ $$yz$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | 1 | 0 | 0 | 1 |
| $$01$$ | 0 | 0 | 0 | 0 |
| $$11$$ | 0 | 0 | 0 | 1 |
| $$10$$ | 1 | 0 | 0 | 1 |

Nhóm 1: bốn góc (ô 0, 2, 8, 10): $$w'z'$$
- Các góc kề nhau qua wrap-around theo cả hai chiều

Nhóm 2: hai ô ở hàng $$wx = 11$$, cột $$10$$ và hàng $$wx = 10$$, cột $$10$$: $$wyz'$$

Kết quả: $$F = w'z' + wyz'$$

## Điều kiện "Không cần quan tâm" (Don't-care Conditions)

### Khái niệm

Trong nhiều mạch thực tế, một số tổ hợp đầu vào không bao giờ xảy ra. Với các tổ hợp này, đầu ra không được xác định (có thể là 0 hoặc 1). Ta ký hiệu chúng bằng $$X$$ (don't-care) trên K-map và có thể chọn giá trị phù hợp để tối ưu hóa.

### Ví dụ: Mạch hiển thị 7 đoạn

Xét mạch điều khiển đèn LED hiển thị số thập phân (0-9) trên 4 bit $$A, B, C, D$$. Các tổ hợp từ 1010 đến 1111 không bao giờ xảy ra (don't-care).

Hàm điều khiển đoạn a (đoạn trên cùng) với don't-care:

K-map:

| $$AB$$ \ $$CD$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | 1 | 0 | 1 | 1 |
| $$01$$ | 0 | 1 | 1 | 1 |
| $$11$$ | X | X | X | X |
| $$10$$ | 1 | 1 | X | X |

Nếu coi X = 1 ở những vị trí chiến lược, ta có thể nhóm lớn hơn:
- Coi X ở (11, 00), (11, 10), (10, 10) = 1: nhóm 8 ô (hàng 00 và 10, cột 00 và 10): $$B'D'$$
- Coi X ở (11, 10), (11, 11), (10, 11) = 1: nhóm 8 ô $$C$$

Kết quả tối ưu: $$F_a = A + B'D' + C + BD$$

<div class="content-box warning-box" markdown="1">
**Lưu ý về don't-care**: 
- Các ô don't-care chỉ nên được gán 1 nếu chúng giúp tạo nhóm lớn hơn.
- Không bắt buộc phải nhóm tất cả các ô don't-care.
- Một ô don't-care có thể được dùng trong nhiều nhóm khác nhau.
- Việc gán giá trị cho don't-care ảnh hưởng đến mạch thực tế, nhưng không ảnh hưởng đến hành vi mong muốn.
</div>

## Quy trình Tối thiểu hóa bằng K-map

1. Vẽ K-map với kích thước phù hợp (2, 3, hoặc 4 biến).
2. Điền giá trị từ bảng chân trị hoặc từ dạng $$\sum m$$.
3. Xác định tất cả các implicant nguyên tố (prime implicant) — nhóm lớn nhất có thể.
4. Chọn các implicant nguyên tố cốt yếu (essential prime implicant) — nhóm duy nhất phủ một ô 1 nào đó.
5. Nếu còn ô 1 chưa được phủ, chọn thêm implicant để phủ chúng.
6. Viết biểu thức tối tiểu: mỗi implicant thành một tích, lấy tổng các tích.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Trình tối thiểu hóa bằng K-map</h3>
<p>Công cụ trực quan này cho phép bạn nhập bảng chân trị (hoặc nhấp vào các ô trên K-map để bật/tắt) và xem kết quả tối thiểu hóa ngay lập tức. Các nhóm được tô màu và giải thích chi tiết. <strong>Hãy thử:</strong> Tạo hàm với một số don't-care và xem cách chúng giúp tối ưu biểu thức.</p>
</div>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

K-map là công cụ chuẩn trong thiết kế mạch số. Các ứng dụng cụ thể:

- **Thiết kế ALU**: Tối ưu hóa mạch số học và logic trong CPU.
- **Bộ giải mã (decoder)**: Mạch chuyển mã nhị phân sang 7-đoạn, hoặc địa chỉ bộ nhớ.
- **Bộ đa hợp (multiplexer)**: Chọn một trong nhiều đầu vào dựa trên tín hiệu điều khiển.
- **Máy tính nhúng**: Tối ưu hóa mạch điều khiển trong các thiết bị IoT.
- **FPGA**: Các công cụ CAD tự động dùng K-map và các biến thể để tổng hợp mạch.

## Bài tập

### Bài tập 1: K-map 3 biến

Dùng K-map tối thiểu hóa:

a) $$F(x, y, z) = \sum m(0, 2, 4, 6)$$

b) $$F(x, y, z) = \sum m(1, 3, 5, 7)$$

<details>
<summary>Đáp án</summary>

a) 
| $$xy$$ \ $$z$$ | $$0$$ | $$1$$ |
|:---:|:---:|:---:|
| $$00$$ | 1 | 0 |
| $$01$$ | 1 | 0 |
| $$11$$ | 1 | 0 |
| $$10$$ | 1 | 0 |

Nhóm 4 ô ở cột $$z = 0$$: $$F = z'$$

b)
| $$xy$$ \ $$z$$ | $$0$$ | $$1$$ |
|:---:|:---:|:---:|
| $$00$$ | 0 | 1 |
| $$01$$ | 0 | 1 |
| $$11$$ | 0 | 1 |
| $$10$$ | 0 | 1 |

Nhóm 4 ô ở cột $$z = 1$$: $$F = z$$

</details>

### Bài tập 2: K-map 4 biến

Cho hàm $$F(w, x, y, z) = \sum m(0, 1, 3, 4, 5, 7, 12, 13, 15)$$.

a) Vẽ K-map.
b) Xác định các implicant nguyên tố.
c) Viết biểu thức tối tiểu dạng SOP.

<details>
<summary>Đáp án</summary>

K-map:

| $$wx$$ \ $$yz$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | 1 | 1 | 1 | 0 |
| $$01$$ | 1 | 1 | 1 | 0 |
| $$11$$ | 1 | 1 | 1 | 0 |
| $$10$$ | 0 | 0 | 0 | 0 |

Các implicant nguyên tố:
- Nhóm 8 ô (hàng 00 và 01, cột 00, 01, 11) và (hàng 11, cột 00, 01, 11) thực chất là toàn bộ các hàng 00, 01, 11 với các cột 00, 01, 11: tất cả các ô có $$y = 0$$ hoặc $$z = 1??$$ 

Thực tế, nhìn kỹ: tất cả các ô 1 đều có $$x = 0$$ (hàng 00 và 01). Vậy $$F = x'$$.

</details>

### Bài tập 3: Don't-care

Tối thiểu hóa hàm $$F(A, B, C, D) = \sum m(2, 3, 7, 9, 11, 13) + d(1, 10, 15)$$ với d là don't-care.

<details>
<summary>Đáp án</summary>

K-map với don't-care (ghi X cho các ô không cần quan tâm):

| $$AB$$ \ $$CD$$ | $$00$$ | $$01$$ | $$11$$ | $$10$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$00$$ | 0 | X | 1 | 1 |
| $$01$$ | 0 | 0 | 1 | 0 |
| $$11$$ | 0 | 1 | X | 1 |
| $$10$$ | 0 | 1 | 0 | X |

Coi X = 1 ở các ô chiến lược:

Nhóm tối ưu:
- Nhóm 1: ô (00, 10), (00, 11), (01, 10), (01, 11)... được $$A'C$$
- Nhóm 2: ô (00, 11), (11, 01), (10, 01) với X giúp: $$BD$$
- Nhóm 3: ô (00, 10), (10, 10) với X giúp: $$B'CD'$$

Kết quả: $$F = A'C + BD + B'CD'$$

</details>

## Tóm tắt

- **Bản đồ Karnaugh**: công cụ đồ họa cho tối thiểu hóa hàm Boole 2-4 biến.
- **Ô kề**: khác nhau đúng 1 biến, có thể ở vị trí biên đối diện (wrap-around).
- **Nhóm**: kích thước lũy thừa của 2, càng lớn càng đơn giản.
- **Implicant nguyên tố**: nhóm lớn nhất không thể mở rộng thêm.
- **Implicant nguyên tố cốt yếu**: nhóm duy nhất phủ một ô 1 nào đó.
- **Don't-care**: tận dụng để tối ưu thêm, không bắt buộc phải nhóm hết.

Trong bài tiếp theo, chúng ta sẽ học phương pháp Quine-McCluskey dùng cho hàm nhiều biến hơn.

## Tài liệu Tham khảo

1. Maurice Karnaugh, "The Map Method for Synthesis of Combinational Logic Circuits," *Transactions of the AIEE*, 1953 — bài báo gốc.
2. M. Morris Mano, *Digital Design*, chương 3 về K-map.
