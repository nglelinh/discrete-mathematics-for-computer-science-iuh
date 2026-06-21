---
layout: post
title: "Quy tắc Cộng và Nhân"
categories: chapter07
date: 2021-01-01
order: 1
required: true
lang: en
---

Một hệ thống có bao nhiêu cách đăng nhập, một bộ mật khẩu có bao nhiêu khả năng, một thuật toán sinh ra bao nhiêu cấu hình, đó đều là các câu hỏi đếm. Trước khi học những công thức phức tạp hơn, ta cần nắm hai nguyên tắc nền tảng nhất của tổ hợp.


Các quy tắc đếm cho ta cách ước lượng số cấu hình có thể xảy ra mà không cần liệt kê hết, đây là kỹ năng rất gần với phân tích thuật toán và kiểm thử.
**Quy tắc cộng** áp dụng khi các lựa chọn loại trừ nhau. **Quy tắc nhân** áp dụng khi một quá trình gồm nhiều bước nối tiếp. Hai ý tưởng này nghe rất cơ bản, nhưng chúng là khung xương cho hầu hết bài toán đếm sau này.

Nhiều sai lầm xảy ra không phải vì công thức khó, mà vì đọc sai cấu trúc của bài toán. Lúc nào là "hoặc", lúc nào là "và", các trường hợp có giao nhau hay không, đó mới là phần quyết định.

Trong bài này, chúng ta sẽ luyện cách nhìn bài toán đếm qua cấu trúc lựa chọn, rồi dùng quy tắc cộng và nhân để biến những tình huống thực tế thành phép đếm rõ ràng.

![Cây quyết định — quy tắc nhân](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

*Hình 7.1: Quy tắc nhân tương ứng với cây quyết định — mỗi nhánh là một lựa chọn, tổng số đường đi bằng tích số cách ở từng bước.*

## Quy tắc Cộng (Addition Principle)

**Nguyên lý**: Nếu một tác vụ có thể được thực hiện theo m cách hoặc theo n cách (không trùng lặp), thì tổng số cách thực hiện tác vụ là m + n.

### Định nghĩa chính thức
Nếu A và B là hai tập hợp rời nhau (A ∩ B = ∅), thì |A ∪ B| = |A| + |B|.

![Phép hợp hai tập rời nhau](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

*Hình 7.2: Quy tắc cộng áp dụng khi các lựa chọn loại trừ nhau — tương ứng phép hợp của hai tập không giao.*

### Ví dụ 1: Chọn môn học
Một sinh viên có thể chọn:
- 3 môn toán học: Giải tích, Đại số, Hình học
- 2 môn tin học: Lập trình, Cấu trúc dữ liệu

**Hỏi**: Có bao nhiêu cách chọn 1 môn học?
**Đáp án**: 3 + 2 = 5 cách

### Ví dụ 2: Đi từ A đến C
Từ thành phố A đến C có thể đi:
- Đường bộ: 4 tuyến đường
- Đường hàng không: 2 chuyến bay
- Đường thủy: 1 tuyến tàu

**Tổng số cách**: 4 + 2 + 1 = 7 cách

## Quy tắc Nhân (Multiplication Principle)

**Nguyên lý**: Nếu một tác vụ gồm k bước liên tiếp, bước thứ i có nᵢ cách thực hiện, thì tổng số cách thực hiện tác vụ là n₁ × n₂ × ... × nₖ.

![Tính số hoán vị — quy tắc nhân](/discrete-mathematics-for-computer-science-iuh/img/course/Permutation_count_calculation.svg)

*Hình 7.3: Quy tắc nhân đếm số cách chọn và sắp xếp tuần tự — nền tảng của chỉnh hợp và hoán vị.*

### Ví dụ 3: Tạo mật khẩu
Tạo mật khẩu gồm:
- Ký tự đầu: 1 trong 26 chữ cái
- Ký tự thứ 2: 1 trong 10 chữ số
- Ký tự thứ 3: 1 trong 26 chữ cái

**Tổng số mật khẩu**: 26 × 10 × 26 = 6,760 mật khẩu

### Ví dụ 4: Đi từ A đến C qua B
- Từ A đến B: 3 cách
- Từ B đến C: 4 cách

**Tổng số cách đi từ A đến C qua B**: 3 × 4 = 12 cách

## Tích Descartes (Cartesian Product)

Tích Descartes là một khái niệm quan trọng kết nối lý thuyết tập hợp với quy tắc nhân.

### Định nghĩa

Tích Descartes của hai tập hợp A và B, ký hiệu A × B, là tập hợp tất cả các cặp có thứ tự (a, b) với a ∈ A và b ∈ B.

$$A \times B = \{(a, b) \;|\; a \in A, b \in B\}$$

### Công thức về lực lượng

Nếu |A| = m và |B| = n, thì |A × B| = m × n.

![Tổ hợp — chọn không xét thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Combination.svg)

*Hình 7.4: Tích Descartes mở rộng quy tắc nhân sang nhiều tập — mỗi cặp có thứ tự là một phần tử của tích.*

Tổng quát hơn, tích Descartes của k tập hợp A₁ × A₂ × ... × Aₖ có lực lượng:

$$|A_1 \times A_2 \times \cdots \times A_k| = |A_1| \times |A_2| \times \cdots \times |A_k|$$

### Ví dụ 5: Tích Descartes của hai tập hợp

Cho A = {a, b, c} và B = {1, 2}. Tìm A × B.

**Giải**: A × B = {(a,1), (a,2), (b,1), (b,2), (c,1), (c,2)}. Có 3 × 2 = 6 phần tử.

### Ví dụ 6: Mã sinh viên

Một trường đại học tạo mã sinh viên gồm 2 chữ cái in hoa (A-Z) và 3 chữ số (0-9). Hỏi có bao nhiêu mã khác nhau?

**Giải**: Gọi A là tập 26 chữ cái, B là tập 10 chữ số. Mỗi mã là một phần tử của A × A × B × B × B. Số mã là 26 × 26 × 10 × 10 × 10 = 676.000.

### Mối liên hệ với quy tắc nhân

Quy tắc nhân thực chất là hệ quả trực tiếp của công thức tính lực lượng tích Descartes. Khi một tác vụ gồm k bước, với bước thứ i có nᵢ cách thực hiện, ta có thể xem mỗi cách thực hiện toàn bộ tác vụ là một phần tử của tích Descartes của k tập hợp, trong đó tập thứ i có nᵢ phần tử.

## Nguyên lý Chuồng Bồ câu (Pigeonhole Principle)

**Nguyên lý**: Nếu có $$n$$ vật thể đặt vào $$m$$ hộp, với $$n > m$$, thì ít nhất một hộp chứa từ 2 vật thể trở lên.

$$n > m \implies \exists \text{ hộp chứa } \geq 2 \text{ vật}$$

![Nguyên lý chuồng chim — minh họa](/discrete-mathematics-for-computer-science-iuh/img/course/Pigeonhole.jpg)

*Hình 7.5: Nguyên lý chuồng bồ câu — nhiều đối tượng hơn ngăn chứa thì ít nhất một ngăn phải chứa từ hai đối tượng trở lên.*

**Ví dụ 1**: Trong một lớp có 13 sinh viên, có ít nhất 2 sinh viên sinh cùng tháng (vì 13 > 12 tháng).

**Ví dụ 2**: Trong một nhóm 367 người, có ít nhất 2 người có cùng ngày sinh (vì 367 > 366 ngày trong năm).

**Nguyên lý tổng quát**: Nếu có $$n$$ vật thể đặt vào $$m$$ hộp, thì ít nhất một hộp chứa từ $$\lceil n/m \rceil$$ vật thể trở lên.

**Ví dụ 3**: Nếu có 100 sinh viên làm 3 bài kiểm tra, có ít nhất $$\lceil 100/3 \rceil = 34$$ sinh viên có cùng số bài đạt yêu cầu.

<div class="content-box example-box" markdown="1">
**Ví dụ 4 - Ứng dụng trong CS**: Một mảng gồm 10 số nguyên. Chứng minh rằng tồn tại hai phần tử có hiệu chia hết cho 9.

**Giải**: Khi chia một số nguyên cho 9, số dư chỉ có thể là 0, 1, ..., 8 (9 loại). Với 10 số, theo nguyên lý chuồng bồ câu, có ít nhất hai số cùng số dư khi chia cho 9. Hiệu của chúng chia hết cho 9.
</div>

## Kết hợp Quy tắc Cộng và Nhân

Nhiều bài toán thực tế cần kết hợp cả hai quy tắc.

### Ví dụ 5: Đi du lịch
Từ Hà Nội đến Đà Nẵng có thể:
- **Bay trực tiếp**: 3 chuyến bay
- **Đi qua TP.HCM**: 
  - Hà Nội → TP.HCM: 4 chuyến bay
  - TP.HCM → Đà Nẵng: 2 chuyến bay

**Giải**:
- Đi qua TP.HCM: 4 × 2 = 8 cách (quy tắc nhân)
- Tổng cộng: 3 + 8 = 11 cách (quy tắc cộng)

### Ví dụ 6: Tạo tài khoản
Một website cho phép tạo username theo 2 định dạng:
- **Định dạng 1**: 1 chữ cái + 3 chữ số
- **Định dạng 2**: 2 chữ cái + 2 chữ số

**Giải**:
- Định dạng 1: 26 × 10 × 10 × 10 = 26,000 username
- Định dạng 2: 26 × 26 × 10 × 10 = 67,600 username
- Tổng cộng: 26,000 + 67,600 = 93,600 username

## Ứng dụng trong Khoa học Máy tính

### 1. Phân tích Thuật toán
```python
def count_operations(n):
    """Đếm số phép toán trong thuật toán"""
    # Vòng lặp ngoài: n lần
    # Vòng lặp trong: n lần
    # Mỗi lần: 1 phép toán
    return n * n * 1  # Quy tắc nhân: O(n²)

def count_paths(graph, start, end):
    """Đếm số đường đi trong đồ thị"""
    # Sử dụng quy tắc cộng cho các đường đi khác nhau
    # Sử dụng quy tắc nhân cho chuỗi cạnh liên tiếp
    pass
```

### 2. Mật mã học
```python
def password_strength(length, charset_size):
    """Tính số mật khẩu có thể tạo"""
    # Mỗi vị trí có charset_size lựa chọn
    # Tổng cộng length vị trí
    return charset_size ** length  # Quy tắc nhân

# Ví dụ: Mật khẩu 8 ký tự, bao gồm chữ và số
strength = password_strength(8, 36)  # 36^8 ≈ 2.8 × 10^12
```

### 3. Cơ sở dữ liệu
```sql
-- Đếm số bản ghi có thể tạo từ các bảng
-- Sử dụng quy tắc nhân cho JOIN
SELECT COUNT(*) FROM 
    (SELECT COUNT(*) as users FROM Users) u,
    (SELECT COUNT(*) as orders FROM Orders) o;
```

## Bài tập thực hành

### Bài tập 1: Quy tắc Cộng
1. Một sinh viên có thể chọn 1 trong 5 môn toán, 1 trong 3 môn lý, hoặc 1 trong 4 môn hóa. Hỏi có bao nhiêu cách chọn?

2. Từ thành phố A đến B có 3 đường bộ, 2 đường sắt, và 1 đường hàng không. Có bao nhiêu cách đi?

### Bài tập 2: Quy tắc Nhân
1. Tạo mã số gồm 2 chữ cái đầu và 3 chữ số cuối. Có bao nhiêu mã số khác nhau?

2. Một bữa ăn gồm 1 món khai vị (4 loại), 1 món chính (6 loại), và 1 món tráng miệng (3 loại). Có bao nhiêu cách chọn thực đơn?

### Bài tập 3: Kết hợp
1. Từ A đến C có thể đi trực tiếp (2 cách) hoặc qua B (A→B có 3 cách, B→C có 4 cách). Tổng cộng có bao nhiêu cách?

2. Tạo mật khẩu theo 2 định dạng:
   - Định dạng 1: 3 chữ cái + 2 chữ số
   - Định dạng 2: 2 chữ số + 3 chữ cái
   
   Có bao nhiêu mật khẩu khác nhau?

<details>
<summary>Đáp án</summary>

**Bài tập 1:**
1. 5 + 3 + 4 = 12 cách
2. 3 + 2 + 1 = 6 cách

**Bài tập 2:**
1. 26 × 26 × 10 × 10 × 10 = 676,000 mã số
2. 4 × 6 × 3 = 72 cách

**Bài tập 3:**
1. 2 + (3 × 4) = 2 + 12 = 14 cách
2. (26³ × 10²) + (10² × 26³) = 1,757,600 + 1,757,600 = 3,515,200 mật khẩu

</details>

## Bài tập bổ sung: Quy tắc cộng và nhân, điện thoại, biển số, mật khẩu (từ ccrr1_baitap2)

**Bài 1:** Chọn một cán bộ hoặc sinh viên tham gia hội đồng. Có 37 cán bộ và 63 sinh viên. Bao nhiêu cách?

**Bài 2:** Có bao nhiêu xâu nhị phân độ dài 7?

**Bài 3:** Số điện thoại di động VN: XXXNNNNNNN (XXX code mạng, N 0-9).
a) Vietel cần tối thiểu bao nhiêu code cho 38.249.516 thuê bao?
b) Số VIP: XXXYYYYNNN (4 chữ số trùng) hoặc XXXNNNNYYY (3 chữ số trùng). Mỗi code có bao nhiêu VIP?

**Bài 4:** Biển số A1A2A3N1N2N3N4N5N6 (A: A-Z, N:0-9). Bao nhiêu biển khác nhau?

**Bài 5:** Số 10 chữ số mà 3 chữ đầu và 3 chữ cuối giống nhau?

**Bài 6:** Đếm số n 5 chữ số nếu:
- n chẵn
- n lẻ gồm 2 chữ số khác nhau
- n chẵn gồm 2 chữ số khác nhau

**Bài 7:** Mật khẩu: 1 chữ cái + 3 hoặc 4 chữ số. Tối đa bao nhiêu? Không lặp chữ số thì sao?


