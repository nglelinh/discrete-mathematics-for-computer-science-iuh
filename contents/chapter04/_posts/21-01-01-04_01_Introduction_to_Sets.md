---
layout: post
title: "Giới thiệu Tập hợp"
categories: chapter04
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Tập hợp

Khi viết truy vấn SQL, lọc người dùng theo vai trò, gom các node đã thăm trong thuật toán, hay mô tả tập ký tự hợp lệ của một bộ phân tích cú pháp, ta đang làm việc với cùng một ý tưởng rất nền tảng: **tập hợp**.


Tư duy tập hợp giúp ta mô tả dữ liệu, miền giá trị và ràng buộc một cách chính xác, nên phần này là nền cho cả lập trình lẫn mô hình hóa.
Tập hợp cho phép ta nói chính xác cái gì thuộc về một nhóm và cái gì không. Nghe đơn giản, nhưng đây là ngôn ngữ đứng phía sau dữ liệu, quan hệ, hàm số, xác suất, đồ thị và rất nhiều mô hình mà khoa học máy tính dùng hằng ngày.

Nếu thiếu tư duy tập hợp, nhiều phát biểu kỹ thuật sẽ trở nên mơ hồ. Hai điều kiện tưởng giống nhau có thể khác hoàn toàn chỉ vì miền phần tử khác nhau. Một lỗi nhỏ trong cách mô tả tập đầu vào cũng có thể kéo theo sai lệch trong thiết kế thuật toán hay chứng minh.

Trong bài này, chúng ta sẽ xây nền từ khái niệm phần tử, cách ký hiệu tập hợp, đến những kiểu tập quen thuộc mà bạn sẽ gặp xuyên suốt phần còn lại của môn học.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Định nghĩa** được khái niệm tập hợp và các phần tử.
- **Sử dụng** thành thạo các ký hiệu: $$\in$$, $$\notin$$, $$\subseteq$$, $$\emptyset$$.
- **Biểu diễn** tập hợp bằng ba cách: liệt kê, mô tả tính chất, và khoảng số.
- **Phân biệt** các tập hợp số quan trọng: $$\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$$.
- **Xác định** quan hệ tập con, tập hợp bằng nhau, và lực lượng tập hợp.
- **Áp dụng** khái niệm tập hợp trong lập trình Python.

## Định nghĩa Tập hợp

Phần này đặt lại ngôn ngữ chung của bài học. Nắm chắc định nghĩa trước sẽ giúp các ví dụ và định lý phía sau trở nên dễ theo dõi hơn.

**Định nghĩa**: Tập hợp là một bộ sưu tập các đối tượng riêng biệt, được gọi là các **phần tử** hay **thành phần** của tập hợp.

> Cantor đã định nghĩa tập hợp một cách trực quan: "Một tập hợp là sự kết hợp thành một tổng thể của những đối tượng xác định, phân biệt của trực giác hay tư duy của chúng ta."

### Ký hiệu:
- Tập hợp: A, B, C, ... (chữ cái in hoa)
- Phần tử: a, b, c, ... (chữ cái thường)
- Quan hệ thuộc: a ∈ A (a thuộc A)
- Quan hệ không thuộc: a ∉ A (a không thuộc A)

## Cách biểu diễn tập hợp

### 1. Liệt kê (Roster Method)

Liệt kê tất cả các phần tử trong dấu ngoặc nhọn. Đây là cách trực quan nhất, phù hợp với tập có ít phần tử.

**Ví dụ**:
- A = {1, 2, 3, 4, 5}
- B = {a, e, i, o, u} (các nguyên âm)
- C = {đỏ, xanh, vàng}

### 2. Mô tả tính chất (Set-Builder Notation)

Mô tả tập hợp bằng tính chất của các phần tử. Cách này hữu ích khi tập có quá nhiều phần tử hoặc vô hạn.

**Cú pháp**: {x | P(x)} hoặc {x : P(x)}
Đọc: "Tập hợp các x sao cho P(x)"

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter04/venn-set-representation.svg" alt="Minh họa ba cách biểu diễn tập hợp" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 4.1: Ba cách biểu diễn tập hợp: liệt kê (trái), mô tả tính chất (giữa), và biểu đồ Venn (phải)</figcaption>
</p>
</figure>

**Ví dụ**:
- A = {x | x là số nguyên và 1 ≤ x ≤ 5}
- B = {x | x^2 = 4}
- C = {n ∈ ℕ | n là số chẵn}

### 3. Sử dụng khoảng (cho số thực)

**Ví dụ**:
- [0, 1] = {x ∈ ℝ | 0 ≤ x ≤ 1}
- (0, 1) = {x ∈ ℝ | 0 < x < 1}
- [0, ∞) = {x ∈ ℝ | x ≥ 0}



### 2. Tập hợp con (Subset)

**Định nghĩa**: A ⊆ B nếu mọi phần tử của A đều thuộc B.

**Ký hiệu**:
- A ⊆ B: A là tập con của B
- A ⊂ B: A là tập con thực sự của B (A ⊆ B và A ≠ B)

**Tính chất**:
- ∅ ⊆ A với mọi tập hợp A
- A ⊆ A với mọi tập hợp A
- Nếu A ⊆ B và B ⊆ C thì A ⊆ C (bắc cầu)

<div class="content-box example-box" markdown="1">
**Ví dụ trực quan**: Cho A = {a, b}, hãy liệt kê tất cả tập con của A.

Các tập con: ∅, {a}, {b}, {a, b}. Có tất cả 4 tập con.

Trong Python:
```python
A = {'a', 'b'}
# Có thể kiểm tra:
print({'a'}.issubset(A))  # True
print({'c'}.issubset(A))  # False
```
</div>

### 3. Tập hợp bằng nhau

**Định nghĩa**: A = B nếu A ⊆ B và B ⊆ A.

Đây là cách chứng minh hai tập hợp bằng nhau phổ biến nhất: chứng minh tập này là con của tập kia và ngược lại.

### 4. Lực lượng (Cardinality)

**Định nghĩa**: Số phần tử của tập hợp A, ký hiệu |A| hoặc #A.

**Ví dụ**:
- |{1, 2, 3}| = 3
- |∅| = 0
- |ℕ| = ∞ (vô hạn đếm được -- sẽ học chi tiết ở bài 4.3)

<div class="content-box insight-box" markdown="1">
**Lực lượng trong CS**: Khi bạn gọi `len(set([1, 2, 3]))` trong Python, kết quả 3 chính là lực lượng của tập hợp đó. Trong cơ sở dữ liệu, `SELECT COUNT(*) FROM table` cũng là tính lực lượng.
</div>

## Bài tập thực hành

### Bài tập 1: Nhận diện phần tử

Cho A = {1, 3, 5, 7, 9}. Xác định tính đúng sai của các khẳng định sau:

a) 3 ∈ A
b) 2 ∈ A
c) 6 ∉ A
d) ∅ ∈ A

<details>
<summary>Đáp án</summary>

a) ✅ Đúng. 3 có trong tập A.
b) ❌ Sai. 2 không có trong tập A.
c) ✅ Đúng. 6 không thuộc A.
d) ❌ Sai. ∅ (tập rỗng) không phải là phần tử của A. Các phần tử của A đều là số, không phải tập hợp.
</details>

### Bài tập 2: Biểu diễn tập hợp

Viết tập hợp sau dưới dạng liệt kê và dạng mô tả tính chất:

a) Tập các số tự nhiên chẵn nhỏ hơn 10
b) Tập các ước số của 12

<details>
<summary>Đáp án</summary>

a) Liệt kê: {0, 2, 4, 6, 8}
   Mô tả: A = {n ∈ ℕ₀ | n là số chẵn và n < 10} hoặc A = {2k | k ∈ ℕ₀, 2k < 10}

b) Liệt kê: {1, 2, 3, 4, 6, 12}
   Mô tả: B = {n ∈ ℕ | n chia hết 12}
</details>

### Bài tập 3: Quan hệ tập con

Cho A = {1, 2, 3, 4}. Tìm tất cả tập con của A có đúng 2 phần tử.

<details>
<summary>Đáp án</summary>

Có 6 tập con: {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}.

Công thức: Với tập có |A| = n, số tập con có đúng k phần tử là C(n,k) = n!/(k!(n-k)!).
Ở đây: C(4,2) = 4!/(2!2!) = 6.
</details>

### Bài tập 4: Lập trình

Viết hàm Python `is_subset(A, B)` kiểm tra A có phải tập con của B không.

<details>
<summary>Đáp án</summary>

```python
def is_subset(A, B):
    """Kiểm tra A có phải tập con của B không"""
    for element in A:
        if element not in B:
            return False
    return True

# Kiểm tra
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(is_subset(A, B))  # True

# Cách ngắn hơn:
print(A.issubset(B))  # True
```
</details>

## Định lý: Số tập con của một tập hữu hạn

**Định lý**: Một tập hợp hữu hạn \( A \) có đúng \( 2^{|A|} \) tập con (bao gồm cả ∅ và \( A \)).

**Chứng minh**:

Giả sử \( A = \{a_1, a_2, \dots, a_n\} \), \( |A| = n \).

1. Mỗi tập con \( B \subseteq A \) được xác định bởi việc chọn hoặc không chọn từng phần tử \( a_i \).

2. Với mỗi \( a_i \), có đúng 2 lựa chọn:
   - \( a_i \in B \)
   - \( a_i \notin B \)

3. Do đó, tổng số tập con là:
   $$
   2 \times 2 \times \cdots \times 2 \quad (n \text{ lần}) = 2^n.
   $$

**Hệ quả**:
- \( |A| = 0 \) (tập rỗng): có \( 2^0 = 1 \) tập con (chính nó).
- \( |A| = 1 \): có 2 tập con.
- \( |A| = 10 \): có \( 2^{10} = 1024 \) tập con.
- \( |A| = 20 \): đã có hơn 1 triệu tập con.

**Ý nghĩa trong Khoa học Máy tính**:
- **Không gian trạng thái** của một hệ thống \( n \) bit có \( 2^n \) trạng thái.
- **Tập con** xuất hiện trong thiết kế thuật toán (subset sum, knapsack), database (power set indexing), và AI (feature selection).

## Tóm tắt

- **Tập hợp** là khái niệm nền tảng của toán học, gồm các phần tử riêng biệt
- Ba cách biểu diễn: **liệt kê**, **mô tả tính chất**, **khoảng số**
- **Tập rỗng** ∅: tập không có phần tử nào
- **Tập con** A ⊆ B: mọi phần tử của A đều thuộc B
- **Lực lượng** |A|: số phần tử của tập hữu hạn A
- Các tập hợp số: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ

Trong bài tiếp theo, chúng ta sẽ tìm hiểu các phép toán trên tập hợp: hợp, giao, hiệu, phần bù và hiệu đối xứng -- những công cụ mạnh mẽ để kết hợp và biến đổi các tập hợp.
