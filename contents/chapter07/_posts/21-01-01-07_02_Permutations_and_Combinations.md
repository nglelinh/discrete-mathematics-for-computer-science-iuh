---
layout: post
title: "Hoán vị và Tổ hợp"
categories: chapter07
date: 2021-01-01
order: 2
required: true
lang: en
---

Khi sắp lịch thuyết trình, chọn đội thi, sinh chuỗi ký tự, hay xét mọi cách điền dữ liệu vào các vị trí khác nhau, câu hỏi không chỉ là chọn **những gì** mà còn là có quan tâm đến **thứ tự** hay không.


Các quy tắc đếm cho ta cách ước lượng số cấu hình có thể xảy ra mà không cần liệt kê hết, đây là kỹ năng rất gần với phân tích thuật toán và kiểm thử.
Đó là ranh giới giữa **hoán vị** và **tổ hợp**. Nếu thứ tự quan trọng, số khả năng tăng rất nhanh. Nếu thứ tự không quan trọng, nhiều cấu hình tưởng khác nhau thực ra lại là một. Phân biệt đúng hai kiểu bài này là kỹ năng cốt lõi trong combinatorics và cũng rất thực tế trong lập trình.

Các công thức quen thuộc như giai thừa, chỉnh hợp, tổ hợp không nên được học như danh sách phải nhớ. Chúng nên được nhìn như kết quả tự nhiên của việc phân tích quá trình chọn và sắp xếp.

Trong bài học này, chúng ta sẽ đi từ trực giác đếm đơn giản đến các công thức chuẩn, đồng thời luyện cách nhận ra bài toán thuộc loại nào trước khi tính.

## Giai thừa (Factorial)

Trước khi học hoán vị và tổ hợp, chúng ta cần hiểu về giai thừa.

**Định nghĩa**: n! = n × (n-1) × (n-2) × ... × 2 × 1

**Quy ước**: 0! = 1

![Giai thừa từ 0! đến 4!](/discrete-mathematics-for-computer-science-iuh/img/course/Factorial_from_0__to_4_.svg)

*Hình 7.6: Giai thừa n! tăng rất nhanh — nền tảng để tính hoán vị và tổ hợp.*

**Ví dụ**:
- 3! = 3 × 2 × 1 = 6
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1

### Tính chất của giai thừa
- n! = n × (n-1)!
- n! tăng rất nhanh: 10! = 3,628,800

## Hoán vị (Permutations)

**Định nghĩa**: Hoán vị là cách sắp xếp toàn bộ n đối tượng theo một thứ tự nhất định.

![Hoán vị — sắp xếp có thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Permutation.svg)

*Hình 7.7: Hoán vị đếm số cách sắp xếp n đối tượng phân biệt — thứ tự là yếu tố quyết định.*

### Hoán vị không lặp

**Công thức**: Số hoán vị của n đối tượng phân biệt là:

$$P(n) = n!$$

**Ví dụ**: Có bao nhiêu cách sắp xếp 4 người ngồi thành hàng?

**Giải**: P(4) = 4! = 24 cách

### Hoán vị có lặp

Khi có các đối tượng giống nhau, số hoán vị giảm đi do các đối tượng cùng loại không thể phân biệt.

**Công thức**: Cho n đối tượng gồm k loại, loại thứ i có nᵢ đối tượng giống nhau (n₁ + n₂ + ... + nₖ = n). Số hoán vị có lặp là:

$$\frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}$$

**Ví dụ**: Có bao nhiêu cách sắp xếp các chữ cái trong từ "BANANA"?

**Giải**: 
- Tổng: 6 chữ cái
- B: 1, A: 3, N: 2
- Kết quả: 6!/(1! × 3! × 2!) = 720/(1 × 6 × 2) = 60 cách

## Chỉnh hợp (k-Permutations)

**Định nghĩa**: Chỉnh hợp chập k của n là cách chọn k đối tượng từ n đối tượng phân biệt và sắp xếp chúng theo một thứ tự nhất định. Khác với hoán vị, chỉnh hợp chỉ lấy k đối tượng (k ≤ n) thay vì tất cả n đối tượng.

### Chỉnh hợp không lặp

**Công thức**: Số chỉnh hợp chập k của n là:

$$P(n,k) = \frac{n!}{(n-k)!} = n \times (n-1) \times \cdots \times (n-k+1)$$

**Ý nghĩa**: Chọn k đối tượng từ n đối tượng và sắp xếp chúng (thứ tự có ý nghĩa).

**Ví dụ 1**: Có 10 học sinh, chọn 3 em để xếp thành hàng (chọn và sắp xếp thứ tự). Có bao nhiêu cách?

**Giải**: P(10,3) = 10!/(10-3)! = 10!/7! = 10 × 9 × 8 = 720 cách

**Ví dụ 2**: Một cuộc thi có 8 thí sinh. Hỏi có bao nhiêu cách trao huy chương Vàng, Bạc, Đồng cho ba thí sinh khác nhau?

**Giải**: Số cách chọn 3 người từ 8 và sắp xếp thứ tự (Vàng, Bạc, Đồng) là:

P(8,3) = 8!/(8-3)! = 8!/5! = 8 × 7 × 6 = 336 cách

### Phân biệt Hoán vị và Chỉnh hợp

| Tiêu chí | Hoán vị | Chỉnh hợp |
|:---------|:---------|:-----------|
| Số đối tượng lấy ra | Tất cả n | k đối tượng (k ≤ n) |
| Thứ tự | Có ý nghĩa | Có ý nghĩa |
| Công thức | P(n) = n! | P(n,k) = n!/(n-k)! |

## Tổ hợp (Combinations)

**Định nghĩa**: Tổ hợp chập k của n là cách chọn k đối tượng từ n đối tượng phân biệt mà không quan tâm đến thứ tự.

**Công thức**: Số tổ hợp chập k của n là:

$$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

**Ký hiệu khác**: $C_n^k$ cũng được sử dụng trong một số tài liệu.

![Tổ hợp — chọn không xét thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Combination.svg)

*Hình 7.8: Tổ hợp chập k đếm số cách chọn k phần tử từ n phần tử mà không quan tâm thứ tự.*

**Ví dụ 1**: Từ 10 học sinh, chọn 3 em để tham gia đội tuyển. Có bao nhiêu cách?

**Giải**: C(10,3) = 10!/(3!×7!) = (10×9×8)/(3×2×1) = 120 cách

**Ví dụ 2**: Một lớp có 12 nam và 8 nữ. Có bao nhiêu cách chọn một nhóm 4 người có đúng 2 nam?

**Giải**: 
- Chọn 2 nam từ 12 nam: C(12,2) = 66 cách
- Chọn 2 nữ từ 8 nữ: C(8,2) = 28 cách
- Theo quy tắc nhân: 66 × 28 = 1.848 cách

## Tổ hợp lặp (Combinations with Repetition)

**Định nghĩa**: Tổ hợp lặp chập k từ n loại đối tượng là cách chọn k đối tượng (không quan tâm thứ tự) từ n loại, trong đó mỗi loại có thể được chọn nhiều lần.

**Công thức**: Số tổ hợp lặp chập k từ n loại là:

$$C_R(n,k) = C(n+k-1,k) = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n-1)!}$$

**Ví dụ 1**: Một cửa hàng bán 4 loại bánh: A, B, C, D. Bạn muốn mua 5 cái bánh. Hỏi có bao nhiêu cách chọn?

**Giải**: Đây là tổ hợp lặp chập 5 từ 4 loại:

C_R(4,5) = C(4+5-1,5) = C(8,5) = C(8,3) = 56 cách

**Ví dụ 2**: Có bao nhiêu nghiệm nguyên không âm của phương trình x₁ + x₂ + x₃ = 6?

**Giải**: Mỗi nghiệm tương ứng với một tổ hợp lặp chập 6 từ 3 loại:

C_R(3,6) = C(3+6-1,6) = C(8,6) = C(8,2) = 28 nghiệm

## Công thức Nhị thức Newton (Binomial Theorem)

**Định lý**: Với mọi số nguyên $$n \geq 0$$:

$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k = \binom{n}{0} x^n + \binom{n}{1} x^{n-1} y + \binom{n}{2} x^{n-2} y^2 + \cdots + \binom{n}{n} y^n$$

**Ví dụ 1**: Khai triển $$(x + y)^3$$:
$$(x + y)^3 = \binom{3}{0}x^3 + \binom{3}{1}x^2 y + \binom{3}{2}xy^2 + \binom{3}{3}y^3 = x^3 + 3x^2 y + 3xy^2 + y^3$$

**Ví dụ 2**: Tìm hệ số của $$x^3 y^2$$ trong khai triển $$(x + y)^5$$:
Hệ số là $$\binom{5}{2} = 10$$.

**Hệ quả quan trọng**:
- Tổng các hệ số: $$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$ (cho $$x = y = 1$$)
- Tổng các hệ số đan dấu: $$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$$ (cho $$x = 1, y = -1$$)

## Hoán vị lặp và Tổ hợp lặp (Repeated Permutations & Combinations)

Những công thức này được dùng khi các đối tượng có thể được chọn nhiều lần.

### Hoán vị lặp

Khi có $$n$$ đối tượng gồm $$k$$ loại, loại thứ $$i$$ có $$n_i$$ đối tượng giống nhau ($$\sum n_i = n$$):

Số hoán vị lặp = $$\frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}$$

**Ví dụ**: Số cách sắp xếp các chữ cái trong từ "BANANA":
$$\frac{6!}{1! \times 3! \times 2!} = \frac{720}{1 \times 6 \times 2} = 60$$

### Tổ hợp lặp (Combinations with Repetition)

Số cách chọn $$k$$ đối tượng từ $$n$$ loại (mỗi loại không giới hạn số lượng, không quan tâm thứ tự):

$$C_R(n, k) = \binom{n + k - 1}{k}$$

**Ví dụ**: Một tiệm kem có 5 vị. Có bao nhiêu cách chọn 3 cây kem?
$$C_R(5, 3) = \binom{5 + 3 - 1}{3} = \binom{7}{3} = 35$$

## Bảng tổng kết các công thức

| Khái niệm | Chọn k từ n? | Thứ tự? | Lặp? | Công thức |
|:-----------|:------------:|:-------:|:----:|:----------|
| Hoán vị | n (tất cả) | Có | Không | n! |
| Hoán vị có lặp | n (tất cả) | Có | Có | n!/(n₁!×...×nₖ!) |
| Chỉnh hợp | k ≤ n | Có | Không | n!/(n-k)! |
| Tổ hợp | k ≤ n | Không | Không | n!/(k!(n-k)!) |
| Tổ hợp lặp | k bất kỳ | Không | Có | C(n+k-1, k) |

![Tam giác Pascal](/discrete-mathematics-for-computer-science-iuh/img/course/Pascal_triangle.svg)

*Hình 7.9: Tam giác Pascal — mỗi hệ số nhị thức $\binom{n}{k}$ bằng tổng hai hệ số phía trên.*

![Khai triển nhị thức và tam giác Pascal](/discrete-mathematics-for-computer-science-iuh/img/course/Binomial_theorem_visualisation.svg)

*Hình 7.10: Định lý nhị thức liên kết khai triển $(x+y)^n$ với hệ số tổ hợp trong tam giác Pascal.*

## Bài tập có lời giải

### Bài tập 1: Xếp sách lên kệ

Có 5 cuốn sách Toán, 4 cuốn sách Lý và 3 cuốn sách Hóa. Có bao nhiêu cách xếp 12 cuốn sách lên kệ sao cho các cuốn cùng môn đứng cạnh nhau?

**Giải**: 
- Coi mỗi bộ môn là một khối: có 3! = 6 cách sắp xếp thứ tự các môn
- Trong mỗi môn: Toán có 5! = 120 cách, Lý có 4! = 24 cách, Hóa có 3! = 6 cách
- Tổng số: 3! × 5! × 4! × 3! = 6 × 120 × 24 × 6 = 103.680 cách

### Bài tập 2: Chọn ủy ban

Một lớp có 15 nam và 12 nữ. Cần chọn một ủy ban gồm 5 người. Có bao nhiêu cách chọn nếu ủy ban phải có ít nhất 2 nữ?

**Giải**: Ta tính tổng số cách chọn có 2 nữ, 3 nữ, 4 nữ và 5 nữ:
- 2 nữ + 3 nam: C(12,2) × C(15,3) = 66 × 455 = 30.030
- 3 nữ + 2 nam: C(12,3) × C(15,2) = 220 × 105 = 23.100
- 4 nữ + 1 nam: C(12,4) × C(15,1) = 495 × 15 = 7.425
- 5 nữ + 0 nam: C(12,5) × C(15,0) = 792 × 1 = 792

Tổng số: 30.030 + 23.100 + 7.425 + 792 = 61.347 cách

### Bài tập 3: Thành lập số

Từ các chữ số 0, 1, 2, 3, 4, 5 có thể lập được bao nhiêu số tự nhiên có 4 chữ số khác nhau?

**Giải**: 
- Chữ số đầu tiên (hàng nghìn) không thể là 0: có 5 cách chọn (1, 2, 3, 4, 5)
- Sau khi chọn chữ số đầu, còn 3 vị trí với 5 chữ số còn lại
- Số cách chọn và sắp xếp 3 vị trí còn lại: P(5,3) = 5!/2! = 60
- Tổng số: 5 × 60 = 300 số

## Bài tập tự luyện

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

1. Có bao nhiêu cách sắp xếp 5 học sinh ngồi vào một hàng ghế có 5 chỗ?

2. Một hộp có 10 viên bi đỏ và 8 viên bi xanh. Có bao nhiêu cách chọn 4 viên bi trong đó có ít nhất 1 viên bi đỏ?

3. Từ các chữ số 1, 2, 3, 4, 5, 6, 7 có thể lập được bao nhiêu số chẵn có 4 chữ số khác nhau?

4. Có bao nhiêu cách xếp 3 quyển sách Toán, 2 quyển sách Văn và 4 quyển sách Anh lên kệ sao cho các quyển cùng môn không nhất thiết đứng cạnh nhau?

5. Một nhóm có 10 nam và 7 nữ. Cần chọn ra 5 người sao cho số nam nhiều hơn số nữ. Hỏi có bao nhiêu cách chọn?

6. Tìm số nghiệm nguyên không âm của phương trình x₁ + x₂ + x₃ + x₄ = 8.

7. Một cửa hàng kem có 5 vị khác nhau. Bạn muốn mua 3 cây kem, mỗi cây có thể chọn bất kỳ vị nào. Có bao nhiêu cách chọn?

## So sánh Hoán vị và Tổ hợp

| Khía cạnh | Hoán vị | Tổ hợp |
|-----------|---------|--------|
| **Thứ tự** | Quan trọng | Không quan trọng |
| **Công thức** | P(n,k) = n!/(n-k)! | C(n,k) = n!/(k!(n-k)!) |
| **Ví dụ** | Sắp xếp học sinh | Chọn đội tuyển |
| **Kết quả** | P(n,k) ≥ C(n,k) | C(n,k) ≤ P(n,k) |

### Mối quan hệ
P(n,k) = k! × C(n,k)

**Giải thích**: Mỗi tổ hợp có thể sắp xếp thành k! hoán vị.

## Tính chất của Tổ hợp

### 1. Tính đối xứng
C(n,k) = C(n,n-k)

**Ví dụ**: C(10,3) = C(10,7) = 120

### 2. Tam giác Pascal
C(n,k) = C(n-1,k-1) + C(n-1,k)

**Tam giác Pascal**:
```
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
```

### 3. Tổng các tổ hợp
∑(k=0 to n) C(n,k) = 2ⁿ

**Ví dụ**: C(3,0) + C(3,1) + C(3,2) + C(3,3) = 1 + 3 + 3 + 1 = 8 = 2³

## Ứng dụng trong Khoa học Máy tính

### 1. Thuật toán tìm kiếm
```python
def binary_search_complexity(n):
    """Độ phức tạp tìm kiếm nhị phân"""
    # Số lần chia đôi tối đa
    return math.ceil(math.log2(n))

def combination_search(items, k):
    """Tìm tất cả tổ hợp k phần tử"""
    # Số tổ hợp cần kiểm tra
    return math.comb(len(items), k)
```

### 2. Mật mã học
```python
def brute_force_time(password_length, charset_size):
    """Thời gian brute force mật khẩu"""
    # Số mật khẩu có thể: charset_size^password_length
    total_passwords = charset_size ** password_length
    return total_passwords / (2 * 1000000)  # Giây (1M mật khẩu/giây)

def key_combinations(key_bits):
    """Số khóa mã hóa có thể"""
    return 2 ** key_bits
```

### 3. Phân tích thuật toán
```python
def subset_generation(n):
    """Số tập con của tập n phần tử"""
    return 2 ** n  # Mỗi phần tử có 2 lựa chọn: có hoặc không

def permutation_sort_complexity(n):
    """Độ phức tạp worst-case của permutation sort"""
    return factorial(n)  # Kiểm tra tất cả hoán vị
```

## Bài tập thực hành

### Bài tập 1: Giai thừa
1. Tính: 7!, 0!, 1!
2. So sánh: 10! và 3⁶
3. Tìm n sao cho n! > 1000

### Bài tập 2: Hoán vị
1. Có bao nhiêu cách sắp xếp 6 cuốn sách trên kệ?
2. Từ 8 học sinh, chọn 3 em làm lớp trường, lớp phó, thư ký. Có bao nhiêu cách?
3. Có bao nhiêu cách sắp xếp chữ cái trong từ "COMPUTER"?

### Bài tập 3: Tổ hợp
1. Từ 12 người, chọn 5 người vào đội bóng. Có bao nhiêu cách?
2. Một hộp có 10 bi đỏ và 8 bi xanh. Chọn 4 bi bất kỳ. Có bao nhiêu cách?
3. Chứng minh: C(n,0) + C(n,1) + ... + C(n,n) = 2ⁿ

### Bài tập 4: Ứng dụng
1. Một mật khẩu gồm 8 ký tự (chữ và số). Có bao nhiêu mật khẩu khác nhau?
2. Trong một lớp 30 học sinh, chọn 1 lớp trưởng và 2 lớp phó. Có bao nhiêu cách?
3. Tạo đội tuyển 11 người từ 20 cầu thủ, trong đó có 1 thủ môn cố định. Có bao nhiêu cách chọn 10 người còn lại?

<details>
<summary>Đáp án</summary>

**Bài tập 1:**
1. 7! = 5,040; 0! = 1; 1! = 1
2. 10! = 3,628,800 > 3⁶ = 729
3. n = 7 (vì 6! = 720 < 1000 < 5040 = 7!)

**Bài tập 2:**
1. 6! = 720 cách
2. P(8,3) = 8!/(8-3)! = 336 cách
3. 8! = 40,320 cách (tất cả chữ cái khác nhau)

**Bài tập 3:**
1. C(12,5) = 792 cách
2. C(18,4) = 3,060 cách
3. Sử dụng khai triển nhị thức (1+1)ⁿ = 2ⁿ

**Bài tập 4:**
1. 36⁸ ≈ 2.8 × 10¹² mật khẩu
2. 30 × C(29,2) = 30 × 406 = 12,180 cách
3. C(19,10) = 92,378 cách

</details>

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

**Giai thừa**: n! = n × (n-1) × ... × 1
- Cơ sở cho hoán vị và tổ hợp

**Hoán vị**: Sắp xếp có thứ tự
- P(n,k) = n!/(n-k)!
- Quan tâm đến thứ tự

**Tổ hợp**: Chọn lựa không thứ tự  
- C(n,k) = n!/(k!(n-k)!)
- Không quan tâm đến thứ tự

**Ứng dụng**: Mật mã, thuật toán, phân tích độ phức tạp

## Bài tập bổ sung: Hoán vị, chỉnh hợp, tổ hợp (từ ccrr1_baitap2)

**Bài toán về hoán vị**
1. Bao nhiêu cách xếp 5 người thành một hàng?
2. Từ 0,1,2,3,4 lập bao nhiêu số tự nhiên 5 chữ số khác nhau?
3. Thương nhân bán hàng 8 thành phố: bắt đầu 1, qua 7 cái kia bất kỳ thứ tự. Bao nhiêu lộ trình?
4. Sắp xếp 5 người vào bàn tròn 5 chỗ (xoay cùng chiều coi như giống)?
5. Hoán vị của MISSISSIPPI?

**Bài toán chỉnh hợp**
1. Xếp 5 người vào băng ghế 7 chỗ?
2. Số tự nhiên 4 chữ số khác nhau từ {0,1,2,3,4,5}?
3. 8 vận động viên: huy chương vàng, bạc, đồng. Bao nhiêu cách (tất cả kết cục xảy ra)?
4. Đội 20 cầu thủ chọn 11, phân 11 vị trí:
   a. Ai cũng chơi bất cứ vị trí?
   b. 1 thủ môn chỉ định, còn lại bất kỳ?
   c. 3 thủ môn chỉ định, còn lại bất kỳ?
5. 8 người thang máy tòa 13 tầng:
   a. Mỗi người tầng khác?
   b. Mỗi người tầng bất kỳ?

**Bài toán tổ hợp**
1. Biển đăng ký ô tô 6 chữ số + 2 chữ cái (không O,I). Tối đa bao nhiêu?
2. Nhóm 5 nam 3 nữ. Chọn 3 người có ít nhất 1 nữ?
3. Số 4 chữ số khác nhau chữ số giảm dần?

Trong bài tiếp theo, chúng ta sẽ học về **Nguyên lý Bao hàm-Loại trừ** - công cụ mạnh mẽ để đếm các tập hợp có giao nhau.
