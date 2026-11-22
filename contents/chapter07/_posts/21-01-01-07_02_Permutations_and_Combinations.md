---

layout: post
title: "Hoán vị và Tổ hợp"
categories: chapter07
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Hoán vị, chỉnh hợp, tổ hợp và hoán vị vòng tròn — phân biệt thứ tự, xếp hàng thẳng so với bàn tròn, cùng các công thức n!, P(n,k), C(n,k), (n−1)!."
---

Ở mục trước, chúng ta đã học quy tắc cộng và quy tắc nhân. Mục này giới thiệu **hoán vị** và **tổ hợp** — hai khái niệm cơ bản được phân biệt dựa trên việc thứ tự sắp xếp có quan trọng hay không.

Khi sắp lịch thuyết trình, chọn đội tuyển hay sinh chuỗi ký tự, câu hỏi không chỉ là chọn **những phần tử nào**, mà còn là có xét đến **thứ tự** hay không. Nếu thứ tự quan trọng, số khả năng tăng rất nhanh; nếu không, nhiều cách sắp xếp khác nhau sẽ được gộp làm một. Các công thức giai thừa, chỉnh hợp và tổ hợp đều bắt nguồn trực tiếp từ việc phân tích quá trình chọn và sắp xếp đó.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tính** chỉnh hợp $$P(n,r)$$, tổ hợp $$C(n,r)$$ và hoán vị vòng tròn $$(n-1)!$$.
- **Phân biệt** bài toán có thứ tự với không thứ tự, xếp hàng thẳng với xếp vòng tròn.
- **Giải** các bài toán chọn nhóm, xếp hàng, xếp bàn tròn và phân công nhiệm vụ.

**Từ khóa**: hoán vị (permutation), hoán vị vòng tròn (circular permutation), tổ hợp (combination), $$n!$$, $$\binom{n}{r}$$.
</div>

## Giai thừa (Factorial)

Trước khi đi vào hoán vị và tổ hợp, ta ôn lại khái niệm giai thừa.

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$$
</div>

**Quy ước**: $$0! = 1$$.

![Giá trị giai thừa n! — tăng rất nhanh](/discrete-mathematics-for-computer-science-iuh/img/course/Factorial_growth.svg)

<p class="textbook-figure-caption" data-figure="7.6">Giá trị n! tăng rất nhanh (thang log₁₀) — từ 0! = 1 đến 10! = 3.628.800; đây là nền tảng để tính hoán vị và tổ hợp.</p>
<div class="textbook-example" markdown="1">
**Ví dụ**:
- 3! = 3 × 2 × 1 = 6
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1
</div>

### Tính chất của giai thừa
- $$n! = n \times (n-1)!$$
- $$n!$$ tăng rất nhanh theo $$n$$: chẳng hạn $$10! = 3.628.800$$.

### Video ngắn: Hoán vị và tổ hợp

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/permutations-combinations.mp4"></video>
</div>

Video dài khoảng 2 phút 18 giây, minh họa cây lựa chọn cho $$3! = 6$$ hoán vị, chỉnh hợp $$P(8,3) = 336$$ qua bục trao huy chương, cách gom 24 bộ có thứ tự thành 4 tập hợp để rút ra $$C(n,k) = P(n,k)/k!$$, so sánh $$P(10,3) = 720$$ với $$C(10,3) = 120$$, bảng bốn kiểu đếm (có/không thứ tự, có/không lặp) trên tập $$\{A,B,C\}$$ và bốn câu đố nhanh.

## Hoán vị (Permutations)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hoán vị là một cách sắp xếp toàn bộ $$n$$ đối tượng phân biệt theo một thứ tự xác định.
</div>

![Hoán vị — sắp xếp có thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Permutation.svg)

<p class="textbook-figure-caption" data-figure="7.7">Hoán vị đếm số cách sắp xếp n đối tượng phân biệt — trong đó thứ tự là yếu tố quyết định.</p>
### Hoán vị không lặp

**Công thức**: Số hoán vị của $$n$$ đối tượng phân biệt là:

<div class="textbook-equation" markdown="1">
$$P(n) = n!$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Có bao nhiêu cách xếp 4 người ngồi thành một hàng ngang?

**Giải**: P(4) = 4! = 24 cách.
</div>

## Hoán vị vòng tròn (Circular permutations)

Khi sắp xếp các phần tử quanh **bàn tròn** (hoặc thành một vòng khép kín), hai cách xếp chỉ khác nhau bởi một **phép xoay** thường được xem là **như nhau**: không còn vị trí "đầu hàng" hay "cuối hàng" tuyệt đối mà chỉ còn thứ tự tương đối (ai ngồi bên trái, ai ngồi bên phải ai).

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **hoán vị vòng tròn** của $$n$$ phần tử phân biệt là cách sắp xếp các phần tử theo một vòng khép kín mà không phân biệt điểm bắt đầu hay kết thúc (các cấu hình thu được từ nhau bằng phép xoay được coi là một).
</div>

**Công thức**: Số hoán vị vòng tròn của $$n$$ phần tử phân biệt là:

<div class="textbook-equation" markdown="1">
$$P_{\text{vòng}}(n) = (n-1)! = \frac{n!}{n}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Giải thích**:

1. **Cố định một phần tử** làm mốc (ví dụ cố định vị trí của một người), rồi sắp xếp $$n-1$$ phần tử còn lại theo thứ tự: có $$(n-1)!$$ cách.
2. Tương đương: có $$n!$$ cách xếp thành hàng thẳng; mỗi cấu hình vòng tròn tương ứng đúng $$n$$ cách xoay trên hàng thẳng, nên ta chia cho $$n$$.

![Hoán vị vòng tròn — cố định một người](/discrete-mathematics-for-computer-science-iuh/img/course/circular_permutation.svg)

<p class="textbook-figure-caption" data-figure="7.7b">Cố định một người quanh bàn tròn để loại bỏ các phép xoay tương đương — số cách còn lại là $$(n-1)!$$.</p>

<div class="textbook-example" markdown="1">
**Ví dụ 1**: Xếp 5 người A, B, C, D, E ngồi quanh một bàn tròn. Có bao nhiêu cách?

**Giải**: $$(5-1)! = 4! = 24$$ cách.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 2**: Xếp 8 người quanh một bàn tròn (không phân biệt các phép xoay). Có bao nhiêu cách?

**Giải**: $$(8-1)! = 7! = 5040$$ cách.
</div>

| | Xếp hàng thẳng | Xếp vòng tròn |
|:---|:---|:---|
| Phân biệt vị trí tuyệt đối? | Có (đầu–cuối) | Không (chỉ xét thứ tự xoay) |
| Công thức | $$n!$$ | $$(n-1)!$$ |
| Ví dụ $$n = 5$$ | $$120$$ | $$24$$ |

**Ghi chú**: Nếu các ghế đã được **đánh số** (có vị trí cố định) thì số cách xếp quay về $$n!$$. Nếu bài toán còn xem hai cách **lật gương** là một (như xâu hạt thành vòng cổ, không phân biệt chiều kim đồng hồ và ngược chiều kim đồng hồ) thì chia thêm 2: $$(n-1)!/2$$ (với $$n \ge 3$$) — chỉ áp dụng khi đề bài nêu rõ.

## Chỉnh hợp (k-Permutations)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Chỉnh hợp chập $$k$$ của $$n$$ là cách chọn $$k$$ đối tượng từ $$n$$ đối tượng phân biệt và sắp xếp chúng theo một thứ tự nhất định. Khác với hoán vị, chỉnh hợp chỉ lấy $$k$$ đối tượng ($$k \le n$$) thay vì toàn bộ $$n$$ đối tượng.
</div>

### Chỉnh hợp không lặp

**Công thức**: Số chỉnh hợp chập $$k$$ của $$n$$ là:

<div class="textbook-equation" markdown="1">
$$P(n,k) = \frac{n!}{(n-k)!} = n \times (n-1) \times \cdots \times (n-k+1)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ý nghĩa**: Chọn $$k$$ đối tượng từ $$n$$ đối tượng phân biệt và sắp xếp thứ tự cho chúng.

**Ví dụ 1**: Từ 10 học sinh, chọn 3 em và xếp thành một hàng. Có bao nhiêu cách?

**Giải**: P(10,3) = 10!/(10-3)! = 10!/7! = 10 × 9 × 8 = 720 cách.

**Ví dụ 2**: Một cuộc thi có 8 thí sinh. Hỏi có bao nhiêu cách trao ba huy chương Vàng, Bạc, Đồng cho ba thí sinh khác nhau?

**Giải**: Số cách chọn 3 thí sinh từ 8 thí sinh và gán thứ tự giải (Vàng, Bạc, Đồng) là:

P(8,3) = 8!/(8-3)! = 8!/5! = 8 × 7 × 6 = 336 cách.

### Phân biệt Hoán vị và Chỉnh hợp

| Tiêu chí | Hoán vị | Chỉnh hợp |
|:---------|:---------|:-----------|
| Số đối tượng lấy ra | Tất cả $$n$$ | $$k$$ đối tượng ($$k \le n$$) |
| Thứ tự | Có xét thứ tự | Có xét thứ tự |
| Công thức | P(n) = n! | P(n,k) = n!/(n-k)! |

## Tổ hợp (Combinations)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Tổ hợp chập $$k$$ của $$n$$ là cách chọn $$k$$ đối tượng từ $$n$$ đối tượng phân biệt mà không quan tâm đến thứ tự.
</div>

**Công thức**: Số tổ hợp chập $$k$$ của $$n$$ là:

<div class="textbook-equation" markdown="1">
$$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ký hiệu khác**: $$C_n^k$$ cũng thường được dùng trong nhiều tài liệu tiếng Việt.

![Tổ hợp — chọn không xét thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Combination.svg)

<p class="textbook-figure-caption" data-figure="7.8">Tổ hợp chập k đếm số cách chọn k phần tử từ n phần tử mà không quan tâm đến thứ tự.</p>
**Ví dụ 1**: Từ 10 học sinh, chọn 3 em vào đội tuyển. Có bao nhiêu cách?

**Giải**: C(10,3) = 10!/(3!×7!) = (10×9×8)/(3×2×1) = 120 cách.

**Ví dụ 2**: Một lớp có 12 nam và 8 nữ. Có bao nhiêu cách chọn một nhóm 4 người gồm đúng 2 nam?

**Giải**:
- Chọn 2 nam từ 12 nam: C(12,2) = 66 cách.
- Chọn 2 nữ từ 8 nữ: C(8,2) = 28 cách.
- Theo quy tắc nhân: 66 × 28 = 1.848 cách.

## So sánh Hoán vị và Tổ hợp

| Khía cạnh | Hoán vị / Chỉnh hợp | Tổ hợp |
|-----------|---------------------|--------|
| **Thứ tự** | Quan trọng | Không quan trọng |
| **Công thức** | P(n,k) = n!/(n-k)! | C(n,k) = n!/(k!(n-k)!) |
| **Ví dụ** | Xếp hàng, trao giải nhất/nhì/ba | Chọn đội tuyển, chọn ủy ban |
| **So sánh giá trị** | P(n,k) ≥ C(n,k) | C(n,k) ≤ P(n,k) |

**Mối quan hệ**: P(n,k) = k! × C(n,k), bởi mỗi tổ hợp gồm $$k$$ phần tử có thể sắp xếp theo $$k!$$ thứ tự khác nhau.

## Bảng tổng kết các công thức cơ bản

| Khái niệm | Chọn k từ n? | Thứ tự? | Lặp? | Công thức |
|:-----------|:------------:|:-------:|:----:|:----------|
| Hoán vị (hàng thẳng) | n (tất cả) | Có | Không | n! |
| Hoán vị vòng tròn | n (tất cả) | Có (tương đối) | Không | (n−1)! |
| Chỉnh hợp | k ≤ n | Có | Không | n!/(n-k)! |
| Tổ hợp | k ≤ n | Không | Không | n!/(k!(n-k)!) |

<div class="content-box info-box textbook-block" markdown="1">

**Mở rộng ở các bài sau**

- **Hoán vị/tổ hợp có lặp**, phương pháp stars and bars và phương trình nghiệm nguyên → bài [Hoán vị và Tổ hợp Mở rộng]({{ '/contents/chapter07/21/01/01/Generalized_Permutations_and_Combinations.html' | relative_url }}) (`07_05`).
- **Hệ số nhị thức**, tam giác Pascal và đồng nhất thức tổ hợp → bài [Hệ số Nhị thức và Đồng nhất thức Tổ hợp]({{ '/contents/chapter07/21/01/01/Binomial_Coefficients_and_Identities.html' | relative_url }}) (`07_04`).

</div>

### Minh hoạ tương tác

Minh hoạ phép đếm: liệt kê trực tiếp các tổ hợp và chỉnh hợp C(n,k), P(n,k) để đối chiếu với công thức.

<div class="interactive-demo" markdown="1">
<div data-demo="counting-explainer" data-tab="choose"></div>
</div>
<script src="{{ '/public/js/explainers/counting-explainer.js' | relative_url }}"></script>

## Bài tập có lời giải

### Bài tập 1: Xếp sách lên kệ

Có 5 cuốn sách Toán, 4 cuốn sách Lý và 3 cuốn sách Hóa (tất cả đều khác nhau). Có bao nhiêu cách xếp 12 cuốn sách lên kệ sao cho các cuốn cùng môn luôn đứng cạnh nhau?

**Giải**:
- Coi mỗi bộ môn là một khối: có 3! = 6 cách sắp xếp thứ tự các khối.
- Trong từng khối: sách Toán có 5! = 120 cách, sách Lý có 4! = 24 cách, sách Hóa có 3! = 6 cách.
- Tổng số cách: 3! × 5! × 4! × 3! = 6 × 120 × 24 × 6 = 103.680 cách.

### Bài tập 2: Chọn ủy ban

Một lớp có 15 nam và 12 nữ. Cần chọn một ủy ban gồm 5 người sao cho có ít nhất 2 nữ. Hỏi có bao nhiêu cách chọn?

**Giải**: Ta chia trường hợp theo số nữ trong ủy ban (2, 3, 4 hoặc 5 nữ):
- 2 nữ + 3 nam: C(12,2) × C(15,3) = 66 × 455 = 30.030.
- 3 nữ + 2 nam: C(12,3) × C(15,2) = 220 × 105 = 23.100.
- 4 nữ + 1 nam: C(12,4) × C(15,1) = 495 × 15 = 7.425.
- 5 nữ + 0 nam: C(12,5) × C(15,0) = 792 × 1 = 792.

Tổng số cách: 30.030 + 23.100 + 7.425 + 792 = 61.347 cách.

### Bài tập 3: Thành lập số

Từ các chữ số 0, 1, 2, 3, 4, 5 có thể lập được bao nhiêu số tự nhiên có 4 chữ số khác nhau?

**Giải**:
- Chữ số hàng nghìn không thể bằng 0, nên có 5 cách chọn (1, 2, 3, 4 hoặc 5).
- Ba vị trí còn lại được chọn và sắp xếp từ 5 chữ số chưa dùng: P(5,3) = 5!/2! = 60 cách.
- Tổng số: 5 × 60 = 300 số.

## Bài tập tự luyện

Khi giải các bài toán đếm, hãy xác định trước các dữ kiện, yêu cầu về thứ tự/lặp và công cụ tương ứng trước khi bắt tay vào tính toán để tránh nhầm lẫn ngay từ bước đầu.

1. Có bao nhiêu cách sắp xếp 5 học sinh ngồi vào một hàng ghế gồm 5 chỗ?

2. Một hộp có 10 viên bi đỏ và 8 viên bi xanh. Có bao nhiêu cách chọn 4 viên bi sao cho có ít nhất 1 viên bi đỏ?

3. Từ các chữ số 1, 2, 3, 4, 5, 6, 7 có thể lập được bao nhiêu số chẵn có 4 chữ số khác nhau?

4. Có bao nhiêu cách xếp 3 quyển sách Toán, 2 quyển sách Văn và 4 quyển sách Anh (các quyển khác nhau) lên kệ mà không đòi hỏi sách cùng môn phải đứng cạnh nhau?

5. Một nhóm có 10 nam và 7 nữ. Cần chọn ra 5 người sao cho số nam nhiều hơn số nữ. Hỏi có bao nhiêu cách chọn?

## Ứng dụng trong Khoa học Máy tính

### Thuật toán tìm kiếm
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

### Mật mã học
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

### Phân tích thuật toán
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
1. Tính: 7!, 0!, 1!.
2. So sánh: 10! và 3⁶.
3. Tìm số nguyên dương nhỏ nhất $$n$$ sao cho $$n! > 1000$$.

### Bài tập 2: Hoán vị
1. Có bao nhiêu cách sắp xếp 6 cuốn sách khác nhau lên một kệ?
2. Từ 8 học sinh, chọn 3 em làm lớp trưởng, lớp phó và thư ký. Có bao nhiêu cách?
3. Có bao nhiêu cách sắp xếp các chữ cái trong từ "COMPUTER"?
4. Có bao nhiêu cách xếp 7 người ngồi quanh một bàn tròn (không phân biệt các phép xoay)?

### Bài tập 3: Tổ hợp
1. Từ 12 người, chọn 5 người vào một đội bóng. Có bao nhiêu cách?
2. Một hộp có 10 bi đỏ và 8 bi xanh. Chọn ngẫu nhiên 4 bi bất kỳ. Có bao nhiêu cách?
3. Từ 12 nam và 8 nữ, chọn một nhóm 4 người gồm đúng 2 nữ. Có bao nhiêu cách?

### Bài tập 4: Ứng dụng
1. Một mật khẩu dài 8 ký tự gồm chữ thường và chữ số (36 ký tự). Có bao nhiêu mật khẩu khác nhau?
2. Trong một lớp gồm 30 học sinh, chọn 1 lớp trưởng và 2 lớp phó. Có bao nhiêu cách?
3. Lập một đội tuyển 11 người từ 20 cầu thủ, trong đó có 1 thủ môn cố định đã được chọn sẵn. Có bao nhiêu cách chọn 10 người còn lại?

<details>
<summary>Đáp án</summary>

**Bài tập 1:**
1. 7! = 5.040; 0! = 1; 1! = 1.
2. 10! = 3.628.800 > 3⁶ = 729.
3. n = 7 (vì 6! = 720 < 1000 < 5.040 = 7!).

**Bài tập 2:**
1. 6! = 720 cách.
2. P(8,3) = 8!/(8-3)! = 336 cách.
3. 8! = 40.320 cách (cả 8 chữ cái đều khác nhau).
4. (7−1)! = 6! = 720 cách.

**Bài tập 3:**
1. C(12,5) = 792 cách.
2. C(18,4) = 3.060 cách.
3. C(12,2) × C(8,2) = 66 × 28 = 1.848 cách.

**Bài tập 4:**
1. 36⁸ ≈ 2,8 × 10¹² mật khẩu.
2. 30 × C(29,2) = 30 × 406 = 12.180 cách.
3. C(19,10) = 92.378 cách.

</details>

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt

**Giai thừa**: $$n! = n \times (n-1) \times \cdots \times 1$$ — nền tảng của các công thức hoán vị và tổ hợp.

**Hoán vị và chỉnh hợp** (có xét thứ tự):
- Hàng thẳng: $$n!$$; chỉnh hợp chập $$k$$: $$P(n,k) = n!/(n-k)!$$.
- Vòng tròn (không phân biệt phép xoay): $$(n-1)!$$.

**Tổ hợp** (không xét thứ tự):
- $$C(n,k) = n!/(k!(n-k)!)$$.

**Mở rộng**: Hoán vị và tổ hợp có lặp (`07_05`); hệ số nhị thức và tam giác Pascal (`07_04`).

**Ứng dụng**: Mật mã học, thiết kế thuật toán và phân tích độ phức tạp.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu **Nguyên lý Bù trừ** — công cụ đếm các tập hợp có phần giao nhau.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=lpKiw1Xj8RQ">Toán rời rạc 18. Hoán Vị và Voán Vị Lặp</a> — TITV, tiếng Việt. Trình bày hoán vị và ví dụ về chỉnh hợp bằng tiếng Việt.
- <a href="https://www.youtube.com/watch?v=tkhyQXqVxWA">FACTORIALS and PERMUTATIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giai thừa và hoán vị, tương ứng nửa đầu bài học.
- <a href="https://www.youtube.com/watch?v=kWPj-Q5e9Lo">COMBINATIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Tổ hợp trong các bài toán không xét thứ tự.
