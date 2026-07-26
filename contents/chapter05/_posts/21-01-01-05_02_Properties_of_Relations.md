---

layout: post
title: "Tính chất của Quan hệ"
categories: chapter05
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Bốn tính chất quan hệ; kiểm phản xạ/đối xứng/phản đối xứng/bắc cầu trên ma trận 0-1 và đồ thị."
---

Ở mục trước chúng ta đã định nghĩa quan hệ, các cách biểu diễn và ứng dụng cơ bản trong cơ sở dữ liệu và đồ thị. Mục này giới thiệu bốn tính chất cơ bản — phản xạ, đối xứng, phản đối xứng và bắc cầu — dùng để phân loại và phân tích cấu trúc quan hệ.

Không phải mọi liên kết giữa hai đối tượng đều có cùng bản chất: quan hệ "bằng nhau" khác quan hệ "nhỏ hơn hoặc bằng", và cả hai lại khác quan hệ "theo dõi" trên mạng xã hội. Các tính chất này quyết định liệu chúng ta có thể nhóm phần tử thành lớp tương đương, sắp xếp theo thứ tự hay suy luận thêm liên kết mới hay không. Trong thiết kế dữ liệu và thuật toán, hiểu sai một tính chất có thể dẫn đến mô hình sai ngay từ đầu.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Kiểm tra** tính phản xạ, đối xứng, bắc cầu của quan hệ.
- **Phân biệt** quan hệ tương đương và thứ tự bộ phận.
- **Nhận diện** các tính chất trong schema CSDL và đồ thị.

**Từ khóa**: phản xạ, đối xứng, bắc cầu, quan hệ tương đương, thứ tự bộ phận.
</div>

## Các tính chất cơ bản

Cho quan hệ R trên tập hợp A (R ⊆ A × A):

### 1. Tính phản xạ (Reflexive)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: R là phản xạ nếu ∀a ∈ A: (a, a) ∈ R
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ "=" trên ℝ: mọi số đều bằng chính nó
- ✅ "≤" trên ℝ: mọi số đều ≤ chính nó  
- ❌ "<" trên ℝ: không có số nào < chính nó

**Trong ma trận**: Đường chéo chính toàn số 1
```
[1 ? ?]
[? 1 ?]
[? ? 1]
```

**Trong đồ thị có hướng**: Mỗi đỉnh đều có vòng (loop) -- khuyên từ đỉnh về chính nó.

![Đồ thị có hướng — tính phản xạ](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.7">Trong đồ thị có hướng, tính phản xạ tương ứng với mỗi đỉnh có vòng (loop) quay về chính nó.</p>
</div>

#### Minh họa trực quan: Phản xạ vs Phản đối xứng

**Bảng so sánh nhanh**:

| Tính chất | Ý nghĩa | Ví dụ |
|:---|:---|:---|
| **Phản xạ** | Mọi phần tử liên hệ với chính nó | `a R a` luôn đúng |
| **Phản đối xứng** | Nếu hai chiều thì phải bằng nhau | `a R b` và `b R a` ⇒ `a = b` |

**Quy tắc nhớ**:
- Phản xạ = "tự liên hệ với mình"
- Phản đối xứng = "không có hai chiều trừ khi bằng nhau"

### 2. Tính đối xứng (Symmetric)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: R là đối xứng nếu ∀a, b ∈ A: (a, b) ∈ R ⟹ (b, a) ∈ R
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ "=" trên ℝ: nếu a = b thì b = a
- ✅ "≠" trên ℝ: nếu a ≠ b thì b ≠ a
- ❌ "<" trên ℝ: nếu a < b thì b ≮ a

**Trong ma trận**: Ma trận đối xứng qua đường chéo chính
```
[? a b]
[a ? c]
[b c ?]
```

![Đồ thị vô hướng — tính đối xứng](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="5.8">Quan hệ đối xứng thường được mô hình hóa bằng đồ thị vô hướng — mỗi cạnh nối hai chiều.</p>
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Trong CS**: Quan hệ "hai máy tính có kết nối mạng trực tiếp" là đối xứng. Quan hệ "thư mục cha chứa thư mục con" là không đối xứng (nếu A chứa B thì B không thể chứa A).
</div>

### 3. Tính phản đối xứng (Antisymmetric)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: R là phản đối xứng nếu ∀a, b ∈ A: (a, b) ∈ R ∧ (b, a) ∈ R ⟹ a = b
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ "≤" trên ℝ: nếu a ≤ b và b ≤ a thì a = b
- ✅ "⊆" trên tập hợp: nếu A ⊆ B và B ⊆ A thì A = B
- ❌ "≠" trên ℝ: nếu a ≠ b và b ≠ a thì a ≠ b (không suy ra a = b)
</div>

<div class="content-box warning-box textbook-block" markdown="1">
![Đồ thị có hướng — tính phản đối xứng](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.9">Tính phản đối xứng cấm hai phần tử khác nhau liên hệ hai chiều — không có cặp cung ngược nhau giữa hai đỉnh khác nhau.</p>
**Phân biệt tinh tế**: Đối xứng và phản đối xứng **không phải** hai mặt đối lập! Một quan hệ có thể vừa đối xứng vừa phản đối xứng (ví dụ: quan hệ "="). Một quan hệ cũng có thể không đối xứng cũng không phản đối xứng (ví dụ: R = {(1,2), (2,1), (1,3)} -- có (1,2) và (2,1) nhưng không có (3,1)).
</div>

### 4. Tính bắc cầu (Transitive)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: R là bắc cầu nếu ∀a, b, c ∈ A: (a, b) ∈ R ∧ (b, c) ∈ R ⟹ (a, c) ∈ R
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ "<" trên ℝ: nếu a < b và b < c thì a < c
- ✅ "⊆" trên tập hợp: nếu A ⊆ B và B ⊆ C thì A ⊆ C
- ❌ "là cha của": nếu A là cha của B và B là cha của C thì A không phải là cha của C (mà là ông)
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Bắc cầu trong CS**: Quan hệ "phụ thuộc" giữa các gói phần mềm cần có tính bắc cầu để phân tích dependency tree. Nếu package A phụ thuộc B và B phụ thuộc C, thì A phụ thuộc C (thường được suy ra bởi package manager).
</div>

![Đường đi gián tiếp — tính bắc cầu](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.10">Tính bắc cầu cho phép suy ra quan hệ gián tiếp: nếu có đường a → b → c thì phải có cung (a, c).</p>
### Bảng tổng kết nhanh

| Tính chất | Điều kiện | Ma trận | Đồ thị |
|-----------|-----------|---------|--------|
| Phản xạ | (a,a) ∈ R với mọi a | Đường chéo toàn 1 | Mọi đỉnh có vòng |
| Đối xứng | (a,b) ⟹ (b,a) | Đối xứng | Cung hai chiều |
| Phản đối xứng | (a,b) và (b,a) ⟹ a=b | Không có cặp đối xứng ngoài đường chéo | Không có chu trình 2 chiều |
| Bắc cầu | (a,b) + (b,c) ⟹ (a,c) | Tích ma trận (sẽ học) | Đường đi → cung trực tiếp |

![Ma trận quan hệ và ma trận kề](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.11">Ma trận 0-1 mã hóa quan hệ — hàng i, cột j bằng 1 khi và chỉ khi (aᵢ, aⱼ) thuộc quan hệ.</p>

## Kiểm tra tính chất trên ma trận quan hệ

Khi $$R$$ là quan hệ trên $$A=\{a_1,\ldots,a_n\}$$ và $$M_R=[m_{ij}]$$ là ma trận $$n\times n$$ với $$m_{ij}=1$$ khi và chỉ khi $$(a_i,a_j)\in R$$, các tính chất đọc thẳng từ $$M_R$$ như sau.

<div class="textbook-definition" markdown="1">

**Tiêu chí ma trận.**

1. **Phản xạ**: $$m_{ii}=1$$ với mọi $$i$$ (đường chéo chính toàn 1).
2. **Đối xứng**: $$m_{ij}=m_{ji}$$ với mọi $$i,j$$ ($$M_R$$ đối xứng).
3. **Phản đối xứng** (phản xứng): nếu $$i\neq j$$ thì $$m_{ij}=0$$ hoặc $$m_{ji}=0$$ (không có cặp 1 đối xứng ngoài đường chéo).
4. **Bắc cầu**: nếu $$m_{ik}=1$$ và $$m_{kj}=1$$ thì $$m_{ij}=1$$ (mọi đường dài 2 đều có cung tắt). Kiểm tra thực tế thường qua lũy thừa Boolean hoặc Warshall ở bài 5.4.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ.** Trên $$A=\{1,2,3\}$$ với

$$
M_R=\begin{pmatrix}1&1&0\\0&1&1\\0&0&1\end{pmatrix}.
$$

- Đường chéo toàn 1 ⇒ phản xạ.
- $$m_{12}=1$$ nhưng $$m_{21}=0$$ ⇒ không đối xứng; đồng thời với $$i\neq j$$ không có cặp $$1$$–$$1$$ đối xứng ⇒ phản đối xứng.
- Có $$(1,2)$$ và $$(2,3)$$ nhưng $$m_{13}=0$$ ⇒ **không** bắc cầu.

</div>

**Lưu ý thực hành.** Phản xạ / đối xứng / phản đối xứng kiểm bằng mắt trên ma trận trong vài giây. Bắc cầu dễ sót khi $$n$$ lớn — đó là lý do thuật toán Warshall xuất hiện ở bài tiếp theo.

## Ứng dụng kỹ thuật: khóa và phép chiếu

Trong cơ sở dữ liệu, tính chất của quan hệ không chỉ để phân loại mà còn để bảo đảm dữ liệu nhất quán qua thời gian. Một **primary key** phải xác định duy nhất mỗi bộ, nghĩa là không thể để hai hàng khác nhau có cùng khóa.

Nếu không gian khóa quá nhỏ so với số bản ghi, nguyên lý pigeonhole cho thấy trùng lặp là không tránh khỏi. Vì vậy, thiết kế khóa phải đủ lớn và ổn định để duy trì tính duy nhất lâu dài.

**Phép chiếu** (projection, $$\pi$$) trong đại số quan hệ là thao tác chọn một số thuộc tính từ mỗi bộ. Đây là bản dịch trực tiếp của ý tưởng toán học: từ bộ nhiều thành phần, chúng ta chỉ giữ lại những tọa độ cần thiết.

```sql
SELECT DISTINCT student_id
FROM Enrollments;
```

Lệnh này chính là phép chiếu $$\pi_{student\_id}(Enrollments)$$, đồng thời `DISTINCT` loại các bộ trùng sau khi bỏ bớt thuộc tính.

![Phép chiếu trong cơ sở dữ liệu](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="5.12">Primary key tạo quan hệ đơn ánh giữa bản ghi và khóa; phép chiếu chọn một phần thuộc tính từ mỗi bộ.</p>
```python
enrollments = {("S01", "CS101"), ("S01", "MATH101"), ("S02", "CS101")}
projection = {student_id for (student_id, _) in enrollments}
```

Ở đây, `projection` là kết quả chiếu quan hệ hai ngôi xuống thuộc tính thứ nhất.

## Bài tập thực hành

### Bài tập 1: Nhận diện tính chất

Xác định các tính chất của quan hệ R = {(1,1), (1,2), (2,2), (2,3), (3,3)} trên A = {1, 2, 3}.

<details>
<summary>Đáp án</summary>

- Phản xạ: ✅ (có (1,1), (2,2), (3,3) -- mọi phần tử)
- Đối xứng: ❌ (có (1,2) nhưng không có (2,1))
- Phản đối xứng: ✅ (không có cặp đối xứng nào ngoài đường chéo)
- Bắc cầu: ✅ (kiểm tra: (1,2) và (2,3) → cần (1,3)? KHÔNG có (1,3)!)

Kết luận: R có phản xạ, phản đối xứng, nhưng **không** bắc cầu!
</details>

### Bài tập 2: So sánh hai quan hệ

So sánh tính chất của quan hệ "≤" và "<" trên ℝ.

<details>
<summary>Đáp án</summary>

| Tính chất | ≤ | < |
|-----------|---|---|
| Phản xạ | ✅ (a ≤ a) | ❌ (a ≮ a) |
| Đối xứng | ❌ (1 ≤ 2 nhưng 2 ≰ 1) | ❌ (1 < 2 nhưng 2 ≮ 1) |
| Phản đối xứng | ✅ (a ≤ b và b ≤ a ⇒ a = b) | ✅ (a < b và b < a không bao giờ xảy ra) |
| Bắc cầu | ✅ (a ≤ b và b ≤ c ⇒ a ≤ c) | ✅ (a < b và b < c ⇒ a < c) |
</details>

### Bài tập 3: Đọc tính chất từ ma trận

Cho quan hệ trên $$A=\{a,b,c\}$$ với

$$
M_R=\begin{pmatrix}1&1&1\\1&1&0\\0&0&1\end{pmatrix}.
$$

Xác định phản xạ, đối xứng, phản đối xứng. Có chắc bắc cầu không? Nêu một bộ ba (nếu có) chứng minh không bắc cầu.

<details>
<summary>Đáp án</summary>

- Phản xạ: ✅ (đường chéo 1).
- Đối xứng: ❌ ($$m_{13}=1$$ nhưng $$m_{31}=0$$).
- Phản đối xứng: ❌ (có $$m_{12}=m_{21}=1$$ với $$a\neq b$$).
- Bắc cầu: ❌ — ví dụ $$(c,a)$$ không có; hoặc $$(a,b)$$ và $$(b,a)$$ ok nhưng kiểm $$(a,c)$$ và $$(c,\cdot)$$: có $$(b,a)$$ và $$(a,c)$$ ⇒ cần $$(b,c)$$, mà $$m_{23}=0$$. Vậy không bắc cầu.

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Phản xạ**: mọi phần tử có quan hệ với chính nó. Ma trận: đường chéo toàn 1
- **Đối xứng**: nếu aR b thì bR a. Ma trận: đối xứng qua đường chéo
- **Phản đối xứng**: không có hai phần tử khác nhau quan hệ hai chiều; ma trận: với $$i\neq j$$ thì $$m_{ij}m_{ji}=0$$
- **Bắc cầu**: quan hệ "bảo toàn" qua chuỗi: aR b và bR c kéo theo aR c
- **Kiểm ma trận**: phản xạ/đối xứng/phản đối xứng đọc trực tiếp; bắc cầu cần kiểm đường dài 2 (hoặc Warshall)
- Bốn tính chất này là nền tảng để xây dựng **quan hệ tương đương** (phản xạ + đối xứng + bắc cầu) và **quan hệ thứ tự** (phản xạ + phản đối xứng + bắc cầu)

Trong bài tiếp theo, chúng ta sẽ khám phá chi tiết hai lớp quan hệ đặc biệt này và ứng dụng của chúng.
