---

layout: post
title: "Phép toán Tập hợp"
categories: chapter04
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Trình bày các phép toán hợp, giao, hiệu, phần bù, hiệu đối xứng, các hằng đẳng thức tập hợp (bao gồm luật De Morgan) và ứng dụng trong SQL, Python và Bloom filter."
---

Ở mục trước, chúng ta đã định nghĩa tập hợp, phần tử, tập con và lực lượng. Mục này giới thiệu **phép toán tập hợp** — công cụ kết hợp, so sánh và loại trừ giữa các tập hợp. Trong thực tế, ta thường xuyên gặp các thao tác như tìm người dùng thuộc nhóm A **hoặc** B, tìm bản ghi xuất hiện trong nhật ký hôm qua nhưng không có hôm nay, xác định tài nguyên chung của hai dịch vụ, hay danh sách các nút chưa được duyệt. Các phép hợp, giao, hiệu và phần bù diễn đạt những yêu cầu đó một cách chính xác và làm nền tảng cho truy vấn dữ liệu, tối ưu điều kiện logic và mô hình hóa trạng thái. Hiểu rõ từng phép toán giúp tránh những lỗi phổ biến như nhầm giao với hợp hoặc bỏ quên tập vũ trụ khi lấy phần bù.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** các phép hợp, giao, hiệu, phần bù và hiệu đối xứng trên tập hợp.
- **Vẽ** biểu đồ Venn và chứng minh đẳng thức tập hợp bằng phương pháp phần tử.
- **Áp dụng** các phép toán tập hợp trong SQL (`UNION`, `INTERSECT`, `EXCEPT`) và Python.

**Từ khóa**: hợp, giao, hiệu, phần bù, hiệu đối xứng, luật De Morgan trên tập hợp.
</div>

## Các phép toán cơ bản

### Hợp (Union) — ∪

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A \cup B = \{x \mid x \in A \text{ hoặc } x \in B\}$$
</div>


Phép hợp gom tất cả các phần tử thuộc ít nhất một trong hai tập hợp. Từ "hoặc" được dùng theo nghĩa bao hàm (inclusive or): phần tử có thể thuộc $$A$$, thuộc $$B$$, hoặc thuộc cả hai.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$A = \{1, 2, 3\}$$, $$B = \{3, 4, 5\}$$
- $$A \cup B = \{1, 2, 3, 4, 5\}$$

![Biểu đồ Venn: hợp A ∪ B](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

<p class="textbook-figure-caption" data-figure="4.9">Phép hợp A ∪ B — vùng tô màu gồm mọi phần tử thuộc A, thuộc B, hoặc thuộc cả hai.</p>
</div>

<div class="math-example">
<strong>Ví dụ (thực tế)</strong>: Tập hợp sinh viên học Python hoặc Java
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

### Giao (Intersection) — ∩

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A \cap B = \{x \mid x \in A \text{ và } x \in B\}$$
</div>


Phép giao chỉ gồm các phần tử thuộc **đồng thời** cả hai tập hợp.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$A = \{1, 2, 3\}$$, $$B = \{3, 4, 5\}$$
- $$A \cap B = \{3\}$$

![Biểu đồ Venn: giao A ∩ B](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_intersect_B.svg)

<p class="textbook-figure-caption" data-figure="4.10">Phép giao A ∩ B — chỉ phần chồng lấn giữa hai tập hợp được tô màu.</p>
</div>

<div class="math-example">
<strong>Ví dụ (thực tế)</strong>: Sinh viên học cả Python và Java
<br>Python ∩ Java = {Bình}
</div>

```python
print(Python & Java)          # {'Bình'}
print(Python.intersection(Java))
```

**Tính chất**: Nếu $$A \cap B = \emptyset$$, ta nói $$A$$ và $$B$$ **rời nhau** (disjoint).

![Hai tập rời nhau (disjoint)](/discrete-mathematics-for-computer-science-iuh/img/course/Veranschaulichung_von_disjunkten_Mengen.svg)

<p class="textbook-figure-caption" data-figure="4.11">Khi A ∩ B = ∅, hai tập hợp không có phần tử chung — vùng giao trên biểu đồ Venn rỗng.</p>
### Hiệu (Difference) — \

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A \setminus B = \{x \mid x \in A \text{ và } x \notin B\}$$
</div>


Phép hiệu lấy các phần tử thuộc $$A$$ nhưng không thuộc $$B$$. Phép toán này **không giao hoán**: $$A \setminus B \ne B \setminus A$$ nói chung (trừ khi $$A = B$$).

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$A = \{1, 2, 3\}$$, $$B = \{3, 4, 5\}$$
- $$A \setminus B = \{1, 2\}$$
- $$B \setminus A = \{4, 5\}$$

![Biểu đồ Venn: hiệu A \ B](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_setminus_B.svg)

<p class="textbook-figure-caption" data-figure="4.12">Phép hiệu A \ B — lấy phần thuộc A nhưng không thuộc B (lưu ý: A \ B ≠ B \ A).</p>
```python
print(Python - Java)    # {'An', 'Chi'} -- học Python nhưng không học Java
print(Java - Python)    # {'Dung', 'Em'} -- học Java nhưng không học Python
```
</div>


### Phần bù (Complement) — Aᶜ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A^c = U \setminus A = \{x \in U \mid x \notin A\}$$ (với $$U$$ là tập vũ trụ — universal set).
</div>


Phần bù luôn phụ thuộc vào tập vũ trụ $$U$$; khi thay đổi $$U$$, phần bù của cùng một tập $$A$$ cũng thay đổi theo.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$U = \{1, 2, 3, 4, 5\}$$, $$A = \{1, 3, 5\}$$
- $$A^c = \{2, 4\}$$

![Biểu đồ Venn: phần bù Aᶜ](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-NOT-P.png)

<p class="textbook-figure-caption" data-figure="4.13">Phần bù Aᶜ = U \ A — mọi phần tử thuộc tập vũ trụ U nhưng không thuộc A.</p>
</div>

### Hiệu đối xứng (Symmetric Difference) — △

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$A \triangle B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$$
</div>


Hiệu đối xứng gồm các phần tử thuộc đúng một trong hai tập hợp (không thuộc đồng thời cả hai).

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$A = \{1, 2, 3\}$$, $$B = \{3, 4, 5\}$$
- $$A \triangle B = \{1, 2, 4, 5\}$$

![Biểu đồ Venn: hiệu đối xứng A △ B](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_symmetric_minus_B.svg)

<p class="textbook-figure-caption" data-figure="4.14">Hiệu đối xứng A △ B — các phần tử thuộc đúng một trong hai tập (tương đương phép XOR trong logic).</p>
```python
print(Python ^ Java)   # {'An', 'Chi', 'Dung', 'Em'}
# Hoặc:
print(Python.symmetric_difference(Java))
```
</div>

## Các hằng đẳng thức tập hợp quan trọng

Tương tự đại số số học, lý thuyết tập hợp có các hằng đẳng thức giúp biến đổi và rút gọn biểu thức tập hợp:

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

#### Minh họa trực quan: Luật De Morgan trong mã nguồn

![Minh họa De Morgan trên biểu đồ Venn](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

<p class="textbook-figure-caption" data-figure="4.15">Luật De Morgan — phần bù của hợp/giao tương ứng với giao/hợp của các phần bù.</p>
**Luật De Morgan** cho phép đưa phép lấy phần bù vào trong dấu ngoặc:

```python
# (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
not (x in A or x in B) == (x not in A) and (x not in B)

# (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
not (x in A and x in B) == (x not in A) or (x not in B)
```

**Quy tắc ghi nhớ**: Khi đưa `not` vào trong ngoặc, đổi `or` thành `and` và ngược lại.

## Ứng dụng trong Khoa học Máy tính

### Cơ sở dữ liệu (SQL)

![Cơ sở dữ liệu quan hệ và phép JOIN](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

<p class="textbook-figure-caption" data-figure="4.16">Phép JOIN trong SQL — kết hợp hai bảng theo điều kiện khớp, phản ánh trực tiếp tư duy tập hợp trong truy vấn.</p>
Các phép toán tập hợp tương ứng trực tiếp với các toán tử truy vấn trong SQL:

| Phép toán tập hợp | SQL | Ý nghĩa |
|-------------------|-----|---------|
| A ∪ B | `SELECT * FROM A UNION SELECT * FROM B` | Hợp |
| A ∩ B | `SELECT * FROM A INTERSECT SELECT * FROM B` | Giao |
| A \ B | `SELECT * FROM A EXCEPT SELECT * FROM B` | Hiệu |

### Lọc dữ liệu trong Python

```python
# Giả sử có hai tập người dùng
all_users = {"user1", "user2", "user3", "user4", "user5"}
premium_users = {"user1", "user3", "user5"}

# Người dùng chưa phải premium (phần bù trong all_users)
free_users = all_users - premium_users
print(free_users)  # {'user2', 'user4'}

# Người dùng đăng ký dịch vụ
service_a = {"user1", "user2", "user3"}
service_b = {"user3", "user4", "user5"}
at_least_one = service_a | service_b
both = service_a & service_b
exactly_one = service_a ^ service_b
```

### Bloom Filter

Bloom filter là cấu trúc dữ liệu xác suất dùng để kiểm tra xem một phần tử có thuộc tập hợp hay không. Cấu trúc này kết hợp mảng bit với các hàm băm để tiết kiệm bộ nhớ, đánh đổi bằng khả năng phát sinh dương tính giả (false positive), nhưng không có âm tính giả.

### Minh họa tương tác

Tô màu vùng biểu đồ Venn theo biểu thức nhập vào và so sánh hai biểu thức để kiểm chứng một hằng đẳng thức tập hợp.

<div class="interactive-demo" markdown="1">
<div data-demo="venn-explainer" data-sets="3" data-expr="(A ∪ B) \ C" data-focus="compare" data-expr-b="(A \ C) ∪ (B \ C)"></div>
</div>
<script src="{{ '/public/js/explainers/venn-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Tính toán cơ bản

Cho $$U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$$, $$A = \{1, 2, 3, 4, 5\}$$, $$B = \{4, 5, 6, 7, 8\}$$. Tính:

a) $$A \cup B$$  
b) $$A \cap B$$  
c) $$A \setminus B$$  
d) $$B \setminus A$$  
e) $$A^c$$

<details>
<summary>Đáp án</summary>

a) $$A \cup B = \{1, 2, 3, 4, 5, 6, 7, 8\}$$  
b) $$A \cap B = \{4, 5\}$$  
c) $$A \setminus B = \{1, 2, 3\}$$  
d) $$B \setminus A = \{6, 7, 8\}$$  
e) $$A^c = U \setminus A = \{6, 7, 8, 9, 10\}$$
</details>

### Bài tập 2: Luật De Morgan

Chứng minh $$(A \cup B)^c = A^c \cap B^c$$ bằng phương pháp lấy phần tử bất kỳ.

<details>
<summary>Đáp án</summary>

Lấy $$x \in (A \cup B)^c$$. Khi đó $$x \notin (A \cup B)$$, nghĩa là $$x \notin A$$ và $$x \notin B$$. Suy ra $$x \in A^c$$ và $$x \in B^c$$, tức $$x \in A^c \cap B^c$$.

Ngược lại, lấy $$x \in A^c \cap B^c$$. Khi đó $$x \in A^c$$ và $$x \in B^c$$, nghĩa là $$x \notin A$$ và $$x \notin B$$, suy ra $$x \notin (A \cup B)$$, tức $$x \in (A \cup B)^c$$.

Vậy $$(A \cup B)^c = A^c \cap B^c$$. ∎
</details>

### Bài tập 3: Nhận diện phép toán

Xác định phép toán tập hợp tương ứng với mỗi yêu cầu sau:

a) Tìm sinh viên đăng ký ít nhất một trong hai môn học.  
b) Tìm sinh viên đăng ký cả hai môn.  
c) Tìm sinh viên đăng ký môn thứ nhất nhưng không đăng ký môn thứ hai.  
d) Tìm sinh viên đăng ký đúng một trong hai môn.

<details>
<summary>Đáp án</summary>

a) Hợp ($$\cup$$)  
b) Giao ($$\cap$$)  
c) Hiệu ($$\setminus$$)  
d) Hiệu đối xứng ($$\triangle$$)
</details>

### Bài tập 4: Tính chất của phép toán tập hợp

Trong các khẳng định sau, khẳng định nào luôn đúng với mọi tập con $$S$$ và $$T$$ của tập vũ trụ $$U$$? Giải thích câu trả lời.

(a) $$S \setminus T = T \setminus S$$

(b) $$S \setminus T = S \cap \overline{T}$$

(c) $$S \setminus T = S \cup T$$

(d) $$S \setminus S = T \setminus T$$

(e) $$S \setminus (S \setminus T) = T \setminus (T \setminus S)$$

(f) $$(U \setminus T) \setminus S = U \setminus (T \setminus S)$$

(g) $$(S \setminus T) \cup (T \setminus S) \subseteq U \setminus (S \cap T)$$

(h) Nếu $$S \subseteq T$$ thì $$\overline{S} \subseteq \overline{T}$$.

(i) Nếu $$T \subseteq S \cap T$$ thì $$S \subseteq T \cap S$$.

<details>
<summary>Đáp án</summary>

(a) **Sai.** Phản ví dụ: $$S = \{1\}, T = \{2\}$$ cho $$S \setminus T = \{1\} \ne \{2\} = T \setminus S$$.

(b) **Đúng.** $$x \in S \setminus T \iff x \in S \land x \notin T \iff x \in S \land x \in \overline{T} \iff x \in S \cap \overline{T}$$.

(c) **Sai.** Phản ví dụ: $$S = \{1\}, T = \{2\}$$ cho $$S \setminus T = \{1\} \ne \{1, 2\} = S \cup T$$.

(d) **Đúng.** Vì $$S \setminus S = \emptyset$$ và $$T \setminus T = \emptyset$$ với mọi tập $$S, T$$.

(e) **Đúng.** Ta có $$S \setminus (S \setminus T) = S \cap T$$ và $$T \setminus (T \setminus S) = T \cap S = S \cap T$$, nên hai vế luôn bằng nhau.

(f) **Sai.** Vế trái là $$(U \setminus T) \setminus S = U \setminus (T \cup S)$$, còn vế phải là $$U \setminus (T \setminus S) = (U \setminus T) \cup S$$. Phản ví dụ: $$U = \{1, 2, 3\}, T = \{1\}, S = \{2\}$$, khi đó $$(U \setminus T) \setminus S = \{3\}$$ còn $$U \setminus (T \setminus S) = \{2, 3\}$$.

(g) **Đúng.** $$(S \setminus T) \cup (T \setminus S) = S \triangle T$$; mọi phần tử thuộc $$S \triangle T$$ đều nằm trong $$U$$ và không đồng thời thuộc cả $$S$$ và $$T$$, nên thuộc $$U \setminus (S \cap T)$$.

(h) **Sai.** Phép lấy phần bù đảo chiều bao hàm: nếu $$S \subseteq T$$ thì $$\overline{T} \subseteq \overline{S}$$. Phản ví dụ: $$U = \{1, 2\}, S = \{1\}, T = \{1, 2\}$$ có $$\overline{S} = \{2\} \not\subseteq \emptyset = \overline{T}$$.

(i) **Sai.** Giả thiết $$T \subseteq S \cap T$$ chỉ tương đương với $$T \subseteq S$$, không suy ra $$S \subseteq T$$. Phản ví dụ: $$T = \{1\}, S = \{1, 2\}$$, khi đó $$S \cap T = \{1\}$$ nên $$T \subseteq S \cap T$$ đúng, nhưng $$S = \{1, 2\} \not\subseteq \{1\} = T \cap S$$.

</details>

### Bài tập 5: Tích Descartes

**A.3** Trong các đẳng thức sau, đẳng thức nào luôn đúng với mọi tập hợp $$Q, R, S, T$$? Giải thích.

(a) $$(Q \times R) \cap (S \times T) = (Q \cap S) \times (R \cap T)$$

(b) $$(Q \times R) \cup (S \times T) = (Q \cup S) \times (R \cup T)$$

(c) $$(Q \times R) \setminus (S \times T) = (Q \setminus S) \times (R \setminus T)$$

<details>
<summary>Đáp án</summary>

(a) **Đúng.** $$(x, y) \in (Q \times R) \cap (S \times T) \iff x \in Q \land y \in R \land x \in S \land y \in T \iff x \in Q \cap S \land y \in R \cap T \iff (x, y) \in (Q \cap S) \times (R \cap T)$$.

(b) **Sai.** Phản ví dụ: $$Q = \{1\}, R = \{a\}, S = \{2\}, T = \{b\}$$. Vế trái là $$\{(1,a), (2,b)\}$$, còn vế phải là $$\{1,2\} \times \{a,b\} = \{(1,a), (1,b), (2,a), (2,b)\}$$.

(c) **Sai.** Phản ví dụ: $$Q = \{1,2\}, R = \{a\}, S = \{2\}, T = \{a\}$$. Vế trái là $$\{(1,a), (2,a)\} \setminus \{(2,a)\} = \{(1,a)\}$$, còn vế phải là $$\{1\} \times \emptyset = \emptyset$$.

</details>

### Bài tập 6: Quan hệ bao hàm và logic

**A.8** Trong các tương đương sau, phát biểu nào luôn đúng với mọi tập hợp $$Q, R, S, T$$? Giải thích.

(a) $$(R \cup S) \subseteq T \iff (R \subseteq T \land S \subseteq T)$$

(b) $$(R \cap S) \subseteq T \iff (R \subseteq T \lor S \subseteq T)$$

(c) $$Q \times R \subseteq S \times T \iff (Q \subseteq S \land R \subseteq T)$$

<details>
<summary>Đáp án</summary>

(a) **Đúng.** Nếu $$R \cup S \subseteq T$$ thì mọi phần tử của $$R$$ và của $$S$$ đều thuộc $$T$$, suy ra $$R \subseteq T$$ và $$S \subseteq T$$. Ngược lại, nếu $$R \subseteq T$$ và $$S \subseteq T$$ thì mọi phần tử thuộc $$R \cup S$$ đều thuộc $$T$$, nên $$R \cup S \subseteq T$$.

(b) **Sai.** Chiều $$(\Leftarrow)$$ luôn đúng, nhưng chiều $$(\Rightarrow)$$ không đúng tổng quát. Phản ví dụ: $$R = \{1\}, S = \{2\}, T = \{3\}$$, khi đó $$R \cap S = \emptyset \subseteq T$$ đúng, nhưng cả $$R \subseteq T$$ lẫn $$S \subseteq T$$ đều sai.

(c) **Sai** nếu cho phép tập rỗng. Chiều $$(\Leftarrow)$$ luôn đúng, nhưng chiều $$(\Rightarrow)$$ sai khi $$Q = \emptyset$$ hoặc $$R = \emptyset$$. Phản ví dụ: $$Q = \emptyset, R = \{1\}, S = \{1\}, T = \emptyset$$, khi đó $$Q \times R = \emptyset \subseteq \emptyset = S \times T$$ đúng, nhưng $$R \subseteq T$$ sai. *(Mệnh đề chỉ đúng khi bổ sung điều kiện $$Q \ne \emptyset$$ và $$R \ne \emptyset$$.)*

</details>


## Công cụ tương tác

Nhập hai tập hữu hạn để quan sát hợp, giao, hiệu và hiệu đối xứng trên sơ đồ; bên dưới, điền lực lượng các vùng Venn ba tập để kiểm tra công thức đếm.
<div class="interactive-demo" markdown="1">
<div data-demo="set-operations-visualizer"></div>
</div>
<script src="{{ '/public/js/set-operations-visualizer.js' | relative_url }}"></script>
<div class="interactive-demo" markdown="1">
<div data-demo="venn-counter"></div>
</div>
<script src="{{ '/public/js/venn-counter.js' | relative_url }}"></script>

## Định lý De Morgan (mở rộng)

<div class="textbook-theorem" markdown="1">
**Định lý**: Với mọi tập $$A, B \subseteq U$$,


<div class="textbook-equation" markdown="1">
$$
(A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Chứng minh** (theo định nghĩa):

- $$x \in (A \cup B)^c \iff x \notin A \cup B \iff x \notin A \land x \notin B \iff x \in A^c \land x \in B^c \iff x \in A^c \cap B^c$$.

Đẳng thức thứ hai được chứng minh tương tự.

<div class="textbook-lemma" markdown="1">
**Hệ quả** (De Morgan cho $$n$$ tập):

<div class="textbook-equation" markdown="1">
$$
\left( \bigcup_{i=1}^n A_i \right)^c = \bigcap_{i=1}^n A_i^c, \qquad \left( \bigcap_{i=1}^n A_i \right)^c = \bigcup_{i=1}^n A_i^c.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Ý nghĩa trong khoa học máy tính**:
- Biểu thức `NOT (A OR B)` tương đương `NOT A AND NOT B`, thường gặp khi viết điều kiện lọc.
- Được sử dụng trong tối ưu hóa truy vấn SQL và rút gọn biểu thức Boolean.


## Xem thêm / Video gợi ý

- [Set Theory — Cardinality and Infinity](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Numberphile (Hilbert's Hotel)
- [Introduction to Sets](https://www.youtube.com/watch?v=4l7L9v0p0Q) — Khan Academy (Basics + notation)

## Tóm tắt

- **Hợp** $$A \cup B$$: gom tất cả các phần tử thuộc ít nhất một trong hai tập.
- **Giao** $$A \cap B$$: lấy các phần tử thuộc đồng thời cả hai tập.
- **Hiệu** $$A \setminus B$$: lấy các phần tử thuộc $$A$$ nhưng không thuộc $$B$$.
- **Phần bù** $$A^c$$: lấy các phần tử thuộc tập vũ trụ $$U$$ nhưng không thuộc $$A$$.
- **Hiệu đối xứng** $$A \triangle B$$: lấy các phần tử thuộc đúng một trong hai tập.
- Các phép toán tuân theo các luật giao hoán, kết hợp, phân phối và De Morgan.
- Ứng dụng thực tế: truy vấn SQL, lọc dữ liệu trong Python và cấu trúc Bloom filter.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu về lực lượng tập hợp, tập lũy thừa, nguyên lý bao hàm–loại trừ và khái niệm tập vô hạn đếm được / không đếm được.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=4TlCToZZ5gA">SET OPERATIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu các phép hợp, giao, hiệu và phần bù.
- <a href="https://www.youtube.com/watch?v=EF3m9bSbtdI">The union of two sets</a> — Dr. Trefor Bazett, tiếng Anh. Chứng minh quan hệ bao hàm với phép hợp bằng phương pháp phần tử.
- <a href="https://www.youtube.com/watch?v=zEvQTK17xzY">The Intersection of Two Sets</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày phép giao và cách đọc trên sơ đồ Venn.
