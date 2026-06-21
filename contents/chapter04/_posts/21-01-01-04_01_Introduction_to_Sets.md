---
layout: post
title: "Giới thiệu Tập hợp"
categories: chapter04
date: 2021-01-01
order: 1
required: true
lang: en
---

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

![Georg Cantor — cha đẻ lý thuyết tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Georg_Cantor_1894.jpg)

*Hình 4.1: Georg Cantor (1845–1918), nhà toán học người Đức, người đặt nền móng cho lý thuyết tập hợp hiện đại.*

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

![Các phần tử riêng biệt trong một tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

*Hình 4.2: Phương pháp liệt kê — mỗi phần tử trong tập phải **riêng biệt** và được ghi rõ trong dấu ngoặc nhọn.*

### 2. Mô tả tính chất (Set-Builder Notation)

Mô tả tập hợp bằng tính chất của các phần tử. Cách này hữu ích khi tập có quá nhiều phần tử hoặc vô hạn.

**Cú pháp**: {x | P(x)} hoặc {x : P(x)}
Đọc: "Tập hợp các x sao cho P(x)"

![Biểu đồ Venn 3 tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

*Hình 4.3: Biểu đồ Venn minh họa quan hệ giữa 3 tập hợp — vùng giao (intersection) và vùng hợp (union).*

**Ví dụ**:
- A = {x | x là số nguyên và 1 ≤ x ≤ 5}
- B = {x | x^2 = 4}
- C = {n ∈ ℕ | n là số chẵn}

### 3. Sử dụng khoảng (cho số thực)

**Ví dụ**:
- [0, 1] = {x ∈ ℝ | 0 ≤ x ≤ 1}
- (0, 1) = {x ∈ ℝ | 0 < x < 1}
- [0, ∞) = {x ∈ ℝ | x ≥ 0}

![Ký hiệu khoảng trên trục số thực](/discrete-mathematics-for-computer-science-iuh/img/course/Interval.svg)

*Hình 4.4: Minh họa khoảng đóng [a, b], khoảng mở (a, b) và khoảng nửa mở trên trục số thực.*

### 2. Tập hợp con (Subset)

**Định nghĩa**: A ⊆ B nếu mọi phần tử của A đều thuộc B.

**Ký hiệu**:
- A ⊆ B: A là tập con của B
- A ⊂ B: A là tập con thực sự của B (A ⊆ B và A ≠ B)

**Tính chất**:
- ∅ ⊆ A với mọi tập hợp A
- A ⊆ A với mọi tập hợp A
- Nếu A ⊆ B và B ⊆ C thì A ⊆ C (bắc cầu)

![Biểu đồ Venn: A là tập con của B](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_subset_B.svg)

*Hình 4.5: Khi A ⊆ B, mọi phần tử của A đều nằm bên trong vùng của B trên biểu đồ Venn.*

![Ký hiệu tập rỗng ∅](/discrete-mathematics-for-computer-science-iuh/img/course/Empty_set.svg)

*Hình 4.6: Tập rỗng ∅ — tập hợp không chứa phần tử nào, nhưng vẫn là tập con của mọi tập hợp.*

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

### Bài tập 5: Tập lũy thừa (Power Set)

**A.2** The power set of a set S is pow(S) = {T : T ⊆ S}, the set of all subsets of S. For example,
pow({1, 2, 3}) = {∅, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

(a) Write all the elements of pow(pow({1})).

(b) Is it true that S ∩ T ∈ pow(S) ∩ pow(T) for all sets S and T? Justify your answer.

(c) Is it true that S ∪ T ∈ pow(S) ∪ pow(T) for all sets S and T? Justify your answer.

<details>
<summary>Đáp án</summary>

(a) pow({1}) = {∅, {1}}. Do đó:
pow(pow({1})) = {∅, {∅}, {{1}}, {∅, {1}}}.

(b) **Đúng.** Nếu x ∈ S ∩ T thì x ∈ S và x ∈ T, suy ra x ⊆ S và x ⊆ T (vì x là tập con của S và T do x ∈ pow(S) và x ∈ pow(T)). Vậy x ∈ pow(S) ∩ pow(T). Do đó S ∩ T ⊆ pow(S) ∩ pow(T). Chiều ngược lại cũng đúng nếu ta coi mọi phần tử của pow(S) ∩ pow(T) đều là tập con của S và T.

(c) **Sai.** Lấy S = {1}, T = {2}. Khi đó S ∪ T = {1, 2} ∉ pow(S) ∪ pow(T) vì {1, 2} không phải tập con của S hay T riêng lẻ.

</details>

## Định lý: Số tập con của một tập hợp hữu hạn

![Sơ đồ tập lũy thừa (power set)](/discrete-mathematics-for-computer-science-iuh/img/course/Powerset.svg)

*Hình 4.7: Tập lũy thừa P(S) gồm tất cả tập con của S — với |S| = n phần tử thì |P(S)| = 2ⁿ.*

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

## Các tập hợp số quan trọng

Trong toán học và khoa học máy tính, ta thường gặp các tập số lồng nhau:

![Sơ đồ các tập hợp số ℕ, ℤ, ℚ, ℝ, ℂ](/discrete-mathematics-for-computer-science-iuh/img/course/Euler_diagram_of_number_sets.svg)

*Hình 4.8: Quan hệ lồng nhau giữa các tập số — số tự nhiên ℕ ⊂ số nguyên ℤ ⊂ số hữu tỉ ℚ ⊂ số thực ℝ ⊂ số phức ℂ.*

## Tóm tắt

- **Tập hợp** là khái niệm nền tảng của toán học, gồm các phần tử riêng biệt
- Ba cách biểu diễn: **liệt kê**, **mô tả tính chất**, **khoảng số**
- **Tập rỗng** ∅: tập không có phần tử nào
- **Tập con** A ⊆ B: mọi phần tử của A đều thuộc B
- **Lực lượng** |A|: số phần tử của tập hữu hạn A
- Các tập hợp số: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ

Trong bài tiếp theo, chúng ta sẽ tìm hiểu các phép toán trên tập hợp: hợp, giao, hiệu, phần bù và hiệu đối xứng -- những công cụ mạnh mẽ để kết hợp và biến đổi các tập hợp.

## Bài tập bổ sung: Tập hợp (từ ccrr1_baitap2)

**Bài 1:** Danh sách tất cả các tập con của {1, 2, {b}}.

**Bài 2:** Giả sử U = {1,2,3,4,5,6,7,8,9,10}. Biểu diễn:
- A = tập số nguyên lẻ ⊆ U
- B = tập số nguyên chẵn ⊆ U
- C = tập số nguyên nhỏ hơn 5 ⊆ U
Tìm A ∪ B, A ∩ C.

**Bài 3:** Cho 
A = {1, {2}, 3, {4}, 5}
B = {1, {4}, 5, 3}
C = {{1,2,3}}
D = {1,3}
E = {1, {3}, 4, {5}}
F = {1,2,3,4,8}
Tìm: A ∩ C, B ∩ F, D ∪ C, C ∩ E, C ∪ (D ∩ F)

**Bài 4:** Liệt kê tất cả phần tử của {b,c,d} × {e,o}

**Bài 5:** Chứng minh với mọi tập A, B: nếu (A ∪ B) ⊆ (A ∩ B) thì A = B.

### Tập hợp các tập hợp con (Power set) - từ slide

Cho tập X, tập tất cả các tập con của X (Tập hợp lũy thừa P(X)) .

Ví dụ: X = {0, 1, 2}

P(X) = { ∅, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2} }

**Tính chất:**
- X ⊂ Y ⇒ P(X) ⊂ P(Y)
- Nếu X có n phần tử thì P(X) có 2^n phần tử.

Điều này quan trọng trong lý thuyết tính toán và độ phức tạp (số tập con là 2^ n).

### Biểu diễn tập hợp trên máy tính (từ slide PPT)

Có nhiều cách biểu diễn tập hợp trên máy tính. Một phương pháp phổ biến là sử dụng xâu bit (bit vector) khi tập vũ trụ U là hữu hạn.

**Phương pháp:**

Giả sử U = {a1, a2, ..., an} sắp xếp tùy ý.

Tập con A ⊆ U được biểu diễn bằng xâu bit độ dài n, trong đó bit thứ i là 1 nếu ai ∈ A, 0 nếu không.

**Ví dụ:**

U = {1,2,3,4,5,6,7,8,9,10} sắp xếp tăng dần.

A = {1,2,3,4,5} → 11111 00000

B = {1,3,5,7,9} → 10101 01010

**Phép toán trên bit:**

- Hợp A ∪ B: OR bit-wise

- Giao A ∩ B: AND bit-wise

Ví dụ: A ∪ B = 11111 00000 ∨ 10101 01010 = 11111 01010 → {1,2,3,4,5,7,9}

A ∩ B = 11111 00000 ∧ 10101 01010 = 10101 00000 → {1,3,5}

Lưu ý: Tập rỗng là 000...0 , U là 111...1 .

Điều này hữu ích trong lập trình (bitmask, Bloom filter, etc.).
