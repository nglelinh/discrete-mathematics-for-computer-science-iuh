---

layout: post
title: "Hoán vị và Tổ hợp"
categories: chapter07
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Hoán vị, chỉnh hợp, tổ hợp và hoán vị vòng tròn — phân biệt thứ tự, hàng thẳng so với bàn tròn, và các công thức n!, P(n,k), C(n,k), (n−1)!."
---

Ở mục trước chúng ta đã học quy tắc cộng và quy tắc nhân. Mục này giới thiệu **hoán vị** và **tổ hợp** — hai khái niệm phân biệt theo việc thứ tự có quan trọng hay không.

Khi sắp lịch thuyết trình, chọn đội thi hay sinh chuỗi ký tự, câu hỏi không chỉ là chọn **những gì** mà còn là có quan tâm đến **thứ tự** hay không. Nếu thứ tự quan trọng, số khả năng tăng rất nhanh; nếu không, nhiều cấu hình tưởng khác nhau thực ra là một. Các công thức giai thừa, chỉnh hợp và tổ hợp là kết quả tự nhiên của việc phân tích quá trình chọn và sắp xếp.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tính** hoán vị $$P(n,r)$$, tổ hợp $$C(n,r)$$ và hoán vị vòng tròn $$(n-1)!$$.
- **Phân biệt** bối cảnh có thứ tự / không thứ tự, xếp hàng / xếp vòng.
- **Giải** bài toán chọn nhóm, xếp hàng, xếp bàn tròn, phân công.

**Từ khóa**: hoán vị (permutation), hoán vị vòng tròn (circular permutation), tổ hợp (combination), $$n!$$, $$\binom{n}{r}$$.
</div>

## Giai thừa (Factorial)

Trước khi học hoán vị và tổ hợp, chúng ta cần hiểu về giai thừa.

<div class="textbook-definition" markdown="1">
**Định nghĩa**: n! = n × (n-1) × (n-2) × ... × 2 × 1
</div>

**Quy ước**: 0! = 1

![Giá trị giai thừa n! — tăng rất nhanh](/discrete-mathematics-for-computer-science-iuh/img/course/Factorial_growth.svg)

<p class="textbook-figure-caption" data-figure="7.6">Giá trị n! tăng rất nhanh (thang log₁₀) — từ 0! = 1 đến 10! = 3.628.800; nền tảng để tính hoán vị và tổ hợp.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**:
- 3! = 3 × 2 × 1 = 6
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1
</div>

### Tính chất của giai thừa
- n! = n × (n-1)!
- n! tăng rất nhanh: 10! = 3,628,800

## Hoán vị (Permutations)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hoán vị là cách sắp xếp toàn bộ n đối tượng theo một thứ tự nhất định.
</div>

![Hoán vị — sắp xếp có thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Permutation.svg)

<p class="textbook-figure-caption" data-figure="7.7">Hoán vị đếm số cách sắp xếp n đối tượng phân biệt — thứ tự là yếu tố quyết định.</p>
### Hoán vị không lặp

**Công thức**: Số hoán vị của n đối tượng phân biệt là:

<div class="textbook-equation" markdown="1">
$$P(n) = n!$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Có bao nhiêu cách sắp xếp 4 người ngồi thành hàng?

**Giải**: P(4) = 4! = 24 cách
</div>

## Hoán vị vòng tròn (Circular permutations)

Khi sắp xếp quanh **bàn tròn** (hoặc theo vòng), hai cách chỉ khác nhau bởi một **phép xoay** thường được coi là **cùng một** cách: không còn “ghế đầu” hay “ghế cuối” tuyệt đối — chỉ còn thứ tự tương đối (ai ngồi bên trái/phải ai).

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **hoán vị vòng tròn** của $$n$$ phần tử phân biệt là cách sắp xếp các phần tử theo vòng sao cho không phân biệt điểm bắt đầu và điểm kết thúc (các cách chỉ xoay lẫn nhau là một).
</div>

**Công thức**: Số hoán vị vòng tròn của $$n$$ phần tử phân biệt là:

<div class="textbook-equation" markdown="1">
$$P_{\text{vòng}}(n) = (n-1)! = \frac{n!}{n}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Giải thích**:

1. **Cố định một phần tử** (ví dụ cố định một người ngồi “mốc”), rồi sắp xếp $$n-1$$ phần tử còn lại: $$(n-1)!$$ cách.
2. Tương đương: có $$n!$$ cách xếp thành hàng; mỗi cấu hình vòng tương ứng đúng $$n$$ cách xoay trên hàng → chia cho $$n$$.

![Hoán vị vòng tròn — cố định một người](/discrete-mathematics-for-computer-science-iuh/img/course/circular_permutation.svg)

<p class="textbook-figure-caption" data-figure="7.7b">Cố định một người quanh bàn để loại bỏ sự quay vòng — số cách còn lại là $$(n-1)!$$.</p>

<div class="textbook-example" markdown="1">
**Ví dụ 1**: 5 người A, B, C, D, E ngồi quanh bàn tròn. Có bao nhiêu cách?

**Giải**: $$(5-1)! = 4! = 24$$ cách.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 2**: 8 người quanh bàn tròn (không phân biệt vị trí quay vòng). Có bao nhiêu cách?

**Giải**: $$(8-1)! = 7! = 5040$$ cách.
</div>

| | Xếp hàng thẳng | Xếp vòng tròn |
|:---|:---|:---|
| Phân biệt vị trí tuyệt đối? | Có (đầu–cuối) | Không (chỉ xoay) |
| Công thức | $$n!$$ | $$(n-1)!$$ |
| Ví dụ $$n = 5$$ | $$120$$ | $$24$$ |

**Ghi chú**: Nếu ghế đã **đánh số** (có “chỗ đầu bàn” cố định) thì dùng lại $$n!$$. Nếu đề còn coi hai cách **lật gương** là một (vòng cổ, không phân biệt chiều) thì thường chia thêm 2: $$(n-1)!/2$$ — chỉ áp dụng khi đề nêu rõ.

## Chỉnh hợp (k-Permutations)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Chỉnh hợp chập k của n là cách chọn k đối tượng từ n đối tượng phân biệt và sắp xếp chúng theo một thứ tự nhất định. Khác với hoán vị, chỉnh hợp chỉ lấy k đối tượng (k ≤ n) thay vì tất cả n đối tượng.
</div>

### Chỉnh hợp không lặp

**Công thức**: Số chỉnh hợp chập k của n là:

<div class="textbook-equation" markdown="1">
$$P(n,k) = \frac{n!}{(n-k)!} = n \times (n-1) \times \cdots \times (n-k+1)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
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

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Tổ hợp chập k của n là cách chọn k đối tượng từ n đối tượng phân biệt mà không quan tâm đến thứ tự.
</div>

**Công thức**: Số tổ hợp chập k của n là:

<div class="textbook-equation" markdown="1">
$$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ký hiệu khác**: $C_n^k$ cũng được sử dụng trong một số tài liệu.

![Tổ hợp — chọn không xét thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Combination.svg)

<p class="textbook-figure-caption" data-figure="7.8">Tổ hợp chập k đếm số cách chọn k phần tử từ n phần tử mà không quan tâm thứ tự.</p>
**Ví dụ 1**: Từ 10 học sinh, chọn 3 em để tham gia đội tuyển. Có bao nhiêu cách?

**Giải**: C(10,3) = 10!/(3!×7!) = (10×9×8)/(3×2×1) = 120 cách

**Ví dụ 2**: Một lớp có 12 nam và 8 nữ. Có bao nhiêu cách chọn một nhóm 4 người có đúng 2 nam?

**Giải**: 
- Chọn 2 nam từ 12 nam: C(12,2) = 66 cách
- Chọn 2 nữ từ 8 nữ: C(8,2) = 28 cách
- Theo quy tắc nhân: 66 × 28 = 1.848 cách

## So sánh Hoán vị và Tổ hợp

| Khía cạnh | Hoán vị / Chỉnh hợp | Tổ hợp |
|-----------|---------------------|--------|
| **Thứ tự** | Quan trọng | Không quan trọng |
| **Công thức** | P(n,k) = n!/(n-k)! | C(n,k) = n!/(k!(n-k)!) |
| **Ví dụ** | Sắp xếp học sinh | Chọn đội tuyển |
| **Kết quả** | P(n,k) ≥ C(n,k) | C(n,k) ≤ P(n,k) |

**Mối quan hệ**: P(n,k) = k! × C(n,k). Mỗi tổ hợp có thể sắp xếp thành k! hoán vị.

## Bảng tổng kết các công thức cơ bản

| Khái niệm | Chọn k từ n? | Thứ tự? | Lặp? | Công thức |
|:-----------|:------------:|:-------:|:----:|:----------|
| Hoán vị (hàng) | n (tất cả) | Có | Không | n! |
| Hoán vị vòng tròn | n (tất cả) | Có (tương đối) | Không | (n−1)! |
| Chỉnh hợp | k ≤ n | Có | Không | n!/(n-k)! |
| Tổ hợp | k ≤ n | Không | Không | n!/(k!(n-k)!) |

<div class="content-box info-box textbook-block" markdown="1">

**Mở rộng ở các bài sau**

- **Hoán vị/tổ hợp có lặp**, stars and bars, phương trình nghiệm nguyên → bài [Hoán vị và Tổ hợp Mở rộng]({{ '/contents/chapter07/21/01/01/Generalized_Permutations_and_Combinations.html' | relative_url }}) (`07_05`)
- **Hệ số nhị thức**, tam giác Pascal, đồng nhất thức tổ hợp → bài [Hệ số Nhị thức và Đồng nhất thức Tổ hợp]({{ '/contents/chapter07/21/01/01/Binomial_Coefficients_and_Identities.html' | relative_url }}) (`07_04`)

</div>

## Bài tập có lời giải

### Bài tập 1: Xếp sách lên kệ

Có 5 cuốn sách Toán, 4 cuốn sách Lý và 3 cuốn sách Hóa. Có bao nhiêu cách xếp 12 cuốn sách lên kệ sao cho các cuốn cùng môn đứng cạnh nhau?

**Giải**: 
- Coi mỗi bộ môn là một khối: có 3! = 6 cách sắp xếp thứ tự các môn
- Trong mỗi môn: Toán có 5! = 120 cách, Lý có 4! = 24 cách, Hóa có 3! = 6 cách
- Tổng số: 3! × 5! × 4! × 3! = 6 × 120 × 24 × 6 = 103.680 cách

### Bài tập 2: Chọn ủy ban

Một lớp có 15 nam và 12 nữ. Cần chọn một ủy ban gồm 5 người. Có bao nhiêu cách chọn nếu ủy ban phải có ít nhất 2 nữ?

**Giải**: Chúng ta tính tổng số cách chọn có 2 nữ, 3 nữ, 4 nữ và 5 nữ:
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
2. Từ 8 học sinh, chọn 3 em làm lớp trưởng, lớp phó, thư ký. Có bao nhiêu cách?
3. Có bao nhiêu cách sắp xếp chữ cái trong từ "COMPUTER"?
4. Có bao nhiêu cách xếp 7 người quanh bàn tròn (không phân biệt quay vòng)?

### Bài tập 3: Tổ hợp
1. Từ 12 người, chọn 5 người vào đội bóng. Có bao nhiêu cách?
2. Một hộp có 10 bi đỏ và 8 bi xanh. Chọn 4 bi bất kỳ. Có bao nhiêu cách?
3. Từ 12 nam và 8 nữ, chọn nhóm 4 người có đúng 2 nữ. Có bao nhiêu cách?

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
4. (7−1)! = 6! = 720 cách

**Bài tập 3:**
1. C(12,5) = 792 cách
2. C(18,4) = 3,060 cách
3. C(12,2) × C(8,2) = 66 × 28 = 1,848 cách

**Bài tập 4:**
1. 36⁸ ≈ 2.8 × 10¹² mật khẩu
2. 30 × C(29,2) = 30 × 406 = 12,180 cách
3. C(19,10) = 92,378 cách

</details>

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt
**Giai thừa**: n! = n × (n-1) × ... × 1
- Cơ sở cho hoán vị và tổ hợp

**Hoán vị**: Sắp xếp có thứ tự
- Hàng thẳng: $$n!$$; chỉnh hợp: $$P(n,k) = n!/(n-k)!$$
- Vòng tròn (không phân biệt xoay): $$(n-1)!$$

**Tổ hợp**: Chọn lựa không thứ tự  
- C(n,k) = n!/(k!(n-k)!)
- Không quan tâm đến thứ tự

**Mở rộng**: Hoán vị/tổ hợp có lặp (`07_05`); hệ số nhị thức và Pascal (`07_04`)

**Ứng dụng**: Mật mã, thuật toán, phân tích độ phức tạp

Trong bài tiếp theo, chúng ta sẽ học về **Nguyên lý Bao hàm-Loại trừ** - công cụ mạnh mẽ để đếm các tập hợp có giao nhau.
