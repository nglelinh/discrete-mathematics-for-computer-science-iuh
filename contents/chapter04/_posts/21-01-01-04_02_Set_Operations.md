---
layout: post
title: "Phép toán Tập hợp"
categories: chapter04
date: 2021-01-01
order: 2
required: true
lang: en
---

Biết một tập hợp là gì mới chỉ là bước đầu. Trong thực tế, ta gần như luôn cần kết hợp, so sánh hoặc loại trừ giữa nhiều tập: người dùng thuộc nhóm A **hoặc** B, bản ghi có trong log hôm qua nhưng không có hôm nay, tập tài nguyên chung của hai service, hay danh sách node chưa được thăm.


Tư duy tập hợp giúp ta mô tả dữ liệu, miền giá trị và ràng buộc một cách chính xác, nên phần này là nền cho cả lập trình lẫn mô hình hóa.
Các **phép toán tập hợp** như hợp, giao, hiệu và phần bù chính là công cụ để diễn đạt những thao tác đó một cách ngắn gọn và chính xác. Chúng không chỉ là ký hiệu của toán, mà còn là nền tảng cho truy vấn dữ liệu, tối ưu điều kiện logic và mô hình hóa trạng thái trong chương trình.

Điều đáng chú ý là nhiều sai sót trong phân tích bài toán đến từ việc hiểu mơ hồ các phép này. Nhầm giao với hợp hay bỏ quên miền nền có thể khiến kết quả lệch hoàn toàn dù hình thức nhìn rất hợp lý.

Bài học này sẽ giúp chúng ta nhìn các phép toán tập hợp như những thao tác rất thực tế, rồi chuyển dần sang cách viết và suy luận chuẩn trong toán rời rạc.

## Các phép toán cơ bản

### 1. Hợp (Union) -- ∪

**Định nghĩa**: A ∪ B = {x | x ∈ A hoặc x ∈ B}

Phép hợp gom tất cả phần tử thuộc ít nhất một trong hai tập. Từ "hoặc" ở đây theo nghĩa bao hàm (inclusive or): có thể thuộc A, hoặc B, hoặc cả hai.

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∪ B = {1, 2, 3, 4, 5}

![Biểu đồ Venn: hợp A ∪ B](https://commons.wikimedia.org/wiki/Special:FilePath/Union_of_sets_A_and_B.svg?width=500)

*Hình 4.9: Phép hợp A ∪ B — vùng tô màu gồm mọi phần tử thuộc A, thuộc B, hoặc thuộc cả hai.*

<div class="math-example">
<strong>Ví dụ thực tế</strong>: Tập hợp sinh viên học Python hoặc Java
<br>Python = {An, Bình, Chi}, Java = {Bình, Dung, Em}
<br>Python ∪ Java = {An, Bình, Chi, Dung, Em}
</div>

```python
# Hợp trong Python
Python = {"An", "Bình", "Chi"}
Java = {"Bình", "Dung", "Em"}
print(Python | Java)        # {'An', 'Bình', 'Chi', 'Dung', 'Em'}
print(Python.union(Java))   # Tương tự
```

### 2. Giao (Intersection) -- ∩

**Định nghĩa**: A ∩ B = {x | x ∈ A và x ∈ B}

Giao chỉ gồm các phần tử thuộc **đồng thời** cả hai tập.

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∩ B = {3}

![Biểu đồ Venn: giao A ∩ B](https://commons.wikimedia.org/wiki/Special:FilePath/Venn_A_intersect_B.svg?width=500)

*Hình 4.10: Phép giao A ∩ B — chỉ vùng chồng lấn giữa hai tập được tô màu.*

<div class="math-example">
<strong>Ví dụ thực tế</strong>: Sinh viên học cả Python và Java
<br>Python ∩ Java = {Bình}
</div>

```python
print(Python & Java)          # {'Bình'}
print(Python.intersection(Java))
```

**Tính chất**: Nếu A ∩ B = ∅, ta nói A và B **rời nhau** (disjoint).

![Hai tập rời nhau (disjoint)](https://commons.wikimedia.org/wiki/Special:FilePath/Veranschaulichung_von_disjunkten_Mengen.svg?width=500)

*Hình 4.11: Khi A ∩ B = ∅, hai tập không có phần tử chung — vùng giao trên biểu đồ Venn rỗng.*

### 3. Hiệu (Difference) -- \

**Định nghĩa**: A \ B = {x | x ∈ A và x ∉ B}

Hiệu lấy các phần tử thuộc A nhưng không thuộc B. **Không giao hoán**: A \ B ≠ B \ A (trừ khi A = B).

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A \ B = {1, 2}
- B \ A = {4, 5}

![Biểu đồ Venn: hiệu A \ B](https://commons.wikimedia.org/wiki/Special:FilePath/Venn_A_setminus_B.svg?width=500)

*Hình 4.12: Phép hiệu A \ B — lấy phần thuộc A nhưng không thuộc B (lưu ý: A \ B ≠ B \ A).*

```python
print(Python - Java)    # {'An', 'Chi'} -- học Python nhưng không học Java
print(Java - Python)    # {'Dung', 'Em'} -- học Java nhưng không học Python
```

### 4. Phần bù (Complement) -- Aᶜ

**Định nghĩa**: Aᶜ = U \ A = {x ∈ U | x ∉ A}
(với U là tập vũ trụ -- universal set)

Phần bù phụ thuộc vào tập vũ trụ U. Nếu thay đổi U, phần bù thay đổi theo.

**Ví dụ**:
- U = {1, 2, 3, 4, 5}, A = {1, 3, 5}
- Aᶜ = {2, 4}

![Biểu đồ Venn: phần bù Aᶜ](https://commons.wikimedia.org/wiki/Special:FilePath/Venn-Diagram-NOT-P.png?width=400)

*Hình 4.13: Phần bù Aᶜ = U \ A — mọi phần tử trong tập vũ trụ U nhưng không thuộc A.*

### 5. Hiệu đối xứng (Symmetric Difference) -- △

**Định nghĩa**: A △ B = (A \ B) ∪ (B \ A) = (A ∪ B) \ (A ∩ B)

Hiệu đối xứng lấy các phần tử thuộc đúng một trong hai tập (không thuộc cả hai).

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A △ B = {1, 2, 4, 5}

![Biểu đồ Venn: hiệu đối xứng A △ B](https://commons.wikimedia.org/wiki/Special:FilePath/Venn_A_symmetric_minus_B.svg?width=500)

*Hình 4.14: Hiệu đối xứng A △ B — các phần tử thuộc đúng một trong hai tập (tương đương XOR trong logic).*

```python
print(Python ^ Java)   # {'An', 'Chi', 'Dung', 'Em'} 
# Hoặc:
print(Python.symmetric_difference(Java))
```

## Các hằng đẳng thức tập hợp quan trọng

Giống như đại số có các hằng đẳng thức (a + b)² = a² + 2ab + b², lý thuyết tập hợp cũng có những hằng đẳng thức giúp biến đổi và đơn giản hóa biểu thức:

| Luật | Công thức |
|------|-----------|
| Giao hoán | A ∪ B = B ∪ A, A ∩ B = B ∩ A |
| Kết hợp | (A ∪ B) ∪ C = A ∪ (B ∪ C), (A ∩ B) ∩ C = A ∩ (B ∩ C) |
| Phân phối | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C), A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| De Morgan | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ, (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ |
| Bù đôi | (Aᶜ)ᶜ = A |
| Phần tử trung hòa | A ∪ ∅ = A, A ∩ U = A |
| Phần tử nuốt | A ∪ U = U, A ∩ ∅ = ∅ |
| Lũy đẳng | A ∪ A = A, A ∩ A = A |

#### Minh họa trực quan: Luật De Morgan trong code

![Minh họa De Morgan trên biểu đồ Venn](https://commons.wikimedia.org/wiki/Special:FilePath/Intersections_of_two_sets_and_their_complements.svg?width=640)

*Hình 4.15: Luật De Morgan — phần bù của hợp/giao tương ứng với giao/hợp của các phần bù.*

**Luật De Morgan** cho phép "phân phối" phép bù:

```python
# (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
not (x in A or x in B) == (x not in A) and (x not in B)

# (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
not (x in A and x in B) == (x not in A) or (x not in B)
```

**Mẹo nhớ**: Đảo dấu `not` → đổi `and` thành `or` (và ngược lại).

## Ứng dụng trong Khoa học Máy tính

### 1. Cơ sở dữ liệu (SQL)

![Cơ sở dữ liệu quan hệ và phép JOIN](https://commons.wikimedia.org/wiki/Special:FilePath/Square_join.png?width=500)

*Hình 4.16: Phép JOIN trong SQL — kết hợp hai bảng (hai tập bộ) theo điều kiện khớp, tư duy tập hợp nằm ở lõi truy vấn.*

Các phép toán tập hợp tương ứng trực tiếp với các truy vấn SQL:

| Phép toán tập hợp | SQL | Ý nghĩa |
|-------------------|-----|---------|
| A ∪ B | `SELECT * FROM A UNION SELECT * FROM B` | Hợp |
| A ∩ B | `SELECT * FROM A INTERSECT SELECT * FROM B` | Giao |
| A \ B | `SELECT * FROM A EXCEPT SELECT * FROM B` | Hiệu |

### 2. Lọc dữ liệu trong Python

```python
# Giả sử có hai danh sách người dùng
all_users = {"user1", "user2", "user3", "user4", "user5"}
premium_users = {"user1", "user3", "user5"}

# Người dùng chưa phải premium (phần bù)
free_users = all_users - premium_users
print(free_users)  # {'user2', 'user4'}

# Người dùng đăng ký ít nhất một dịch vụ
service_a = {"user1", "user2", "user3"}
service_b = {"user3", "user4", "user5"}
at_least_one = service_a | service_b
both = service_a & service_b
exactly_one = service_a ^ service_b
```

### 3. Bloom Filter

Bloom filter là cấu trúc dữ liệu xác suất dùng để kiểm tra "một phần tử có thuộc tập hợp không". Nó là ứng dụng thông minh của phép toán tập hợp và hàm băm, tiết kiệm bộ nhớ nhưng có thể cho kết quả dương tính giả (false positive).

## Bài tập thực hành

### Bài tập 1: Tính toán cơ bản

Cho U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, A = {1, 2, 3, 4, 5}, B = {4, 5, 6, 7, 8}. Tính:

a) A ∪ B
b) A ∩ B
c) A \ B
d) B \ A
e) Aᶜ

<details>
<summary>Đáp án</summary>

a) A ∪ B = {1, 2, 3, 4, 5, 6, 7, 8}
b) A ∩ B = {4, 5}
c) A \ B = {1, 2, 3}
d) B \ A = {6, 7, 8}
e) Aᶜ = U \ A = {6, 7, 8, 9, 10}
</details>

### Bài tập 2: De Morgan

Chứng minh (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ bằng cách lấy phần tử bất kỳ.

<details>
<summary>Đáp án</summary>

Lấy x ∈ (A ∪ B)ᶜ. Khi đó x ∉ (A ∪ B), nghĩa là x ∉ A và x ∉ B. Vậy x ∈ Aᶜ và x ∈ Bᶜ, suy ra x ∈ Aᶜ ∩ Bᶜ.

Ngược lại: Lấy x ∈ Aᶜ ∩ Bᶜ. Khi đó x ∈ Aᶜ và x ∈ Bᶜ, nghĩa là x ∉ A và x ∉ B, suy ra x ∉ (A ∪ B), tức x ∈ (A ∪ B)ᶜ.

Vậy (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ. ∎
</details>

### Bài tập 3: Xác định tên

Hãy xác định phép toán tập hợp thích hợp cho mỗi tình huống:

a) Tìm sinh viên đăng ký ít nhất một trong hai môn học
b) Tìm sinh viên đăng ký cả hai môn
c) Tìm sinh viên đăng ký môn thứ nhất nhưng không đăng ký môn thứ hai
d) Tìm sinh viên đăng ký đúng một trong hai môn

<details>
<summary>Đáp án</summary>

a) Hợp (∪)
b) Giao (∩)
c) Hiệu (\)
d) Hiệu đối xứng (△)
</details>

### Bài tập 4: Tính chất của phép toán tập hợp

Which of the following properties are guaranteed to hold for all subsets S and T of a
universe U? Justify your answers.

(a) S \ T = T \ S

(b) S \ T = S ∩ T̅

(c) S \ T = S ∪ T

(d) S \ S = T \ T

(e) S \ (S \ T) = T \ (T \ S)

(f) (U \ T) \ S = U \ (T \ S)

(g) (S \ T) ∪ (T \ S) ⊆ U \ (S ∩ T)

(h) If S ⊆ T then S̅ ⊆ T̅.

(i) If T ⊆ S ∩ T then S ⊆ T ∩ S.

<details>
<summary>Đáp án</summary>

(a) **Sai.** Phản ví dụ: S = {1}, T = {2}. S \ T = {1}, T \ S = {2}.

(b) **Đúng.** x ∈ S \ T ⇔ x ∈ S ∧ x ∉ T ⇔ x ∈ S ∧ x ∈ T̅ ⇔ x ∈ S ∩ T̅.

(c) **Sai.** Phản ví dụ: S = {1}, T = {2}. S \ T = {1}, S ∪ T = {1, 2}.

(d) **Đúng.** S \ S = ∅ và T \ T = ∅ với mọi S, T.

(e) **Sai.** Phản ví dụ: S = {1, 2}, T = {2}. S \ (S \ T) = S \ {1} = {2}, T \ (T \ S) = T \ ∅ = {2}. Trường hợp này đúng, nhưng với S = {1}, T = {1, 2}: S \ (S \ T) = {1} \ ∅ = {1}, T \ (T \ S) = {1,2} \ {2} = {1}. Thực tế mệnh đề này **đúng** — đây là tính chất đối xứng của hiệu tập hợp.

(f) **Đúng.** (U \ T) \ S = (U ∩ T̅) ∩ S̅ = U ∩ (T̅ ∩ S̅) = U \ (T ∪ S). Và U \ (T \ S) = U \ (T ∩ S̅) = U ∩ (T ∩ S̅)̅ = U ∩ (T̅ ∪ S) = (U ∩ T̅) ∪ (U ∩ S) = (U \ T) ∪ S. Hai vế không bằng nhau. Thực tế mệnh đề này **sai**. Phản ví dụ: U = {1,2,3}, T = {1}, S = {2}. (U \ T) \ S = {2,3} \ {2} = {3}. U \ (T \ S) = {1,2,3} \ {1} = {2,3}.

(g) **Đúng.** (S \ T) ∪ (T \ S) là hiệu đối xứng S △ T. Mọi phần tử của S △ T đều thuộc U và không đồng thời thuộc cả S và T, nên chúng thuộc U \ (S ∩ T).

(h) **Sai.** Nếu S ⊆ T thì T̅ ⊆ S̅ (phần bù đảo ngược chiều bao hàm).

(i) **Đúng.** T ⊆ S ∩ T ⇒ T ⊆ S và T ⊆ T (hiển nhiên). Từ T ⊆ S thì T ∩ S = T, do đó S ⊆ T ∩ S ⇔ S ⊆ T, đúng vì T ⊆ S.

</details>

### Bài tập 5: Tích Descartes

**A.3** Which of the following properties are guaranteed to hold for all sets Q, R, S, T? Justify
your answers.

(a) (Q × R) ∩ (S × T) = (Q ∩ S) × (R ∩ T)

(b) (Q × R) ∪ (S × T) = (Q ∪ S) × (R ∪ T)

(c) (Q × R) \ (S × T) = (Q \ S) × (R \ T)

<details>
<summary>Đáp án</summary>

(a) **Đúng.** (x, y) ∈ (Q × R) ∩ (S × T) ⇔ x ∈ Q ∧ y ∈ R ∧ x ∈ S ∧ y ∈ T ⇔ x ∈ Q ∩ S ∧ y ∈ R ∩ T ⇔ (x, y) ∈ (Q ∩ S) × (R ∩ T).

(b) **Sai.** Phản ví dụ: Q = {1}, R = {a}, S = {2}, T = {b}. Vế trái: (Q × R) ∪ (S × T) = {(1,a), (2,b)}. Vế phải: (Q ∪ S) × (R ∪ T) = {1,2} × {a,b} = {(1,a), (1,b), (2,a), (2,b)}.

(c) **Sai.** Phản ví dụ: Q = {1,2}, R = {a}, S = {2}, T = {a}. Vế trái: (Q × R) \ (S × T) = {(1,a), (2,a)} \ {(2,a)} = {(1,a)}. Vế phải: (Q \ S) × (R \ T) = {1} × ∅ = ∅.

</details>

### Bài tập 6: Set Relationships with Logic

**A.8** Which of the following statements are guaranteed to hold for all sets Q, R, S, T? Justify your answers.

(a) (R ∪ S) ⊆ T ⇔ (R ⊆ T ∧ S ⊆ T)

(b) (R ∩ S) ⊆ T ⇔ (R ⊆ T ∨ S ⊆ T)

(c) Q × R ⊆ S × T ⇔ (Q ⊆ S ∧ R ⊆ T)

<details>
<summary>Đáp án</summary>

(a) **Đúng.** Nếu (R ∪ S) ⊆ T thì mọi phần tử của R và S đều thuộc T, nên R ⊆ T và S ⊆ T. Ngược lại, nếu R ⊆ T và S ⊆ T thì mọi phần tử của R ∪ S đều thuộc T, nên (R ∪ S) ⊆ T.

(b) **Sai.** Không đúng theo chiều (⇐): lấy R = {1}, S = ∅, T = {2}. Khi đó R ⊆ T sai, S ⊆ T đúng, nhưng (R ∩ S) = ∅ ⊆ T luôn đúng. Nhưng chiều (⇒) cũng sai: lấy R = {1}, S = {2}, T = {3}. R ∩ S = ∅ ⊆ T, nhưng R ⊈ T và S ⊈ T.

(c) **Đúng.** Nếu Q × R ⊆ S × T, lấy x ∈ Q, y ∈ R bất kỳ: (x,y) ∈ Q × R ⊆ S × T, suy ra x ∈ S, y ∈ T. Vậy Q ⊆ S và R ⊆ T. Ngược lại, nếu Q ⊆ S, R ⊆ T thì (x,y) ∈ Q × R ⇒ x ∈ Q ⊆ S, y ∈ R ⊆ T ⇒ (x,y) ∈ S × T.

</details>

## Định lý De Morgan (mở rộng)

**Định lý**: Với mọi tập \( A, B \subseteq U \),

$$
(A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c.
$$

**Chứng minh** (bằng định nghĩa):

- \( x \in (A \cup B)^c \iff x \notin A \cup B \iff x \notin A \land x \notin B \iff x \in A^c \land x \in B^c \iff x \in A^c \cap B^c \).

Tương tự cho đẳng thức thứ hai.

**Hệ quả** (De Morgan cho n tập):

$$
\left( \bigcup_{i=1}^n A_i \right)^c = \bigcap_{i=1}^n A_i^c, \qquad \left( \bigcap_{i=1}^n A_i \right)^c = \bigcup_{i=1}^n A_i^c.
$$

**Ý nghĩa CS**:
- `NOT (A OR B)` = `NOT A AND NOT B` (rất hay gặp trong điều kiện lọc).
- Dùng trong tối ưu truy vấn SQL và biểu thức Boolean.

## Tóm tắt

- **Hợp** A ∪ B: gom tất cả phần tử của cả hai tập
- **Giao** A ∩ B: phần tử chung của cả hai tập
- **Hiệu** A \ B: phần tử của A nhưng không thuộc B
- **Phần bù** Aᶜ: phần tử trong U nhưng không thuộc A
- **Hiệu đối xứng** A △ B: phần tử thuộc đúng một trong hai tập
- Các phép toán tuân theo luật: giao hoán, kết hợp, phân phối, De Morgan
- Ứng dụng thực tế: SQL queries, lọc dữ liệu, Bloom filter

Trong bài tiếp theo, chúng ta sẽ tìm hiểu về lực lượng tập hợp, tập lũy thừa, nguyên lý bao hàm -- loại trừ và khái niệm về tập vô hạn đếm được / không đếm được.
