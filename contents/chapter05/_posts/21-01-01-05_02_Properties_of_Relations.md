---
layout: post
title: "Tính chất của Quan hệ"
categories: chapter05
date: 2021-01-01
order: 2
required: true
lang: en
---

Sau khi biết quan hệ là gì, bước quan trọng tiếp theo là phân biệt các kiểu hành vi khác nhau của quan hệ. Không phải cứ có liên kết giữa hai đối tượng là ta hiểu được cấu trúc của cả hệ thống.


Khi đọc phần này, hãy nghĩ đến các liên kết giữa đối tượng trong cơ sở dữ liệu, đồ thị và hệ thống phân quyền, vì quan hệ chính là cách ta mô tả những liên kết đó.
Ví dụ, quan hệ "bằng nhau" rất khác quan hệ "nhỏ hơn hoặc bằng", và cả hai lại khác hoàn toàn quan hệ "theo dõi nhau" trên mạng xã hội. Sự khác biệt đó được mô tả bằng các tính chất như phản xạ, đối xứng, phản đối xứng và bắc cầu.

Những tính chất này không phải để nhớ máy móc. Chúng quyết định ta có thể nhóm phần tử thành lớp tương đương, sắp xếp chúng theo thứ tự, hay suy luận thêm liên kết mới hay không. Trong thiết kế dữ liệu và thuật toán, hiểu sai một tính chất có thể kéo theo mô hình sai ngay từ đầu.

Trong bài này, chúng ta sẽ học cách nhận diện từng tính chất qua ví dụ cụ thể và thấy vì sao chúng lại quan trọng đến vậy trong toán rời rạc và CS.

## Các tính chất cơ bản

Cho quan hệ R trên tập hợp A (R ⊆ A × A):

### 1. Tính phản xạ (Reflexive)

**Định nghĩa**: R là phản xạ nếu ∀a ∈ A: (a, a) ∈ R

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

#### Minh họa trực quan: Phản xạ vs Phản đối xứng

**Bảng so sánh nhanh**:

| Tính chất | Ý nghĩa | Ví dụ |
|:---|:---|:---|
| **Phản xạ** | Mọi phần tử liên hệ với chính nó | `a R a` luôn đúng |
| **Phản đối xứng** | Nếu hai chiều thì phải bằng nhau | `a R b` và `b R a` ⇒ `a = b` |

**Mẹo nhớ**:
- Phản xạ = "tự liên hệ với mình"
- Phản đối xứng = "không có hai chiều trừ khi bằng nhau"

### 2. Tính đối xứng (Symmetric)

**Định nghĩa**: R là đối xứng nếu ∀a, b ∈ A: (a, b) ∈ R ⟹ (b, a) ∈ R

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

<div class="content-box insight-box" markdown="1">
**Trong CS**: Quan hệ "hai máy tính có kết nối mạng trực tiếp" là đối xứng. Quan hệ "thư mục cha chứa thư mục con" là không đối xứng (nếu A chứa B thì B không thể chứa A).
</div>

### 3. Tính phản đối xứng (Antisymmetric)

**Định nghĩa**: R là phản đối xứng nếu ∀a, b ∈ A: (a, b) ∈ R ∧ (b, a) ∈ R ⟹ a = b

**Ví dụ**:
- ✅ "≤" trên ℝ: nếu a ≤ b và b ≤ a thì a = b
- ✅ "⊆" trên tập hợp: nếu A ⊆ B và B ⊆ A thì A = B
- ❌ "≠" trên ℝ: nếu a ≠ b và b ≠ a thì a ≠ b (không suy ra a = b)

<div class="content-box warning-box" markdown="1">
**Phân biệt tinh tế**: Đối xứng và phản đối xứng **không phải** hai mặt đối lập! Một quan hệ có thể vừa đối xứng vừa phản đối xứng (ví dụ: quan hệ "="). Một quan hệ cũng có thể không đối xứng cũng không phản đối xứng (ví dụ: R = {(1,2), (2,1), (1,3)} -- có (1,2) và (2,1) nhưng không có (3,1)).
</div>

### 4. Tính bắc cầu (Transitive)

**Định nghĩa**: R là bắc cầu nếu ∀a, b, c ∈ A: (a, b) ∈ R ∧ (b, c) ∈ R ⟹ (a, c) ∈ R

**Ví dụ**:
- ✅ "<" trên ℝ: nếu a < b và b < c thì a < c
- ✅ "⊆" trên tập hợp: nếu A ⊆ B và B ⊆ C thì A ⊆ C
- ❌ "là cha của": nếu A là cha của B và B là cha của C thì A không phải là cha của C (mà là ông)

<div class="content-box insight-box" markdown="1">
**Bắc cầu trong CS**: Quan hệ "phụ thuộc" giữa các gói phần mềm cần có tính bắc cầu để phân tích dependency tree. Nếu package A phụ thuộc B và B phụ thuộc C, thì A phụ thuộc C (thường được suy ra bởi package manager).
</div>

### Bảng tổng kết nhanh

| Tính chất | Điều kiện | Ma trận | Đồ thị |
|-----------|-----------|---------|--------|
| Phản xạ | (a,a) ∈ R với mọi a | Đường chéo toàn 1 | Mọi đỉnh có vòng |
| Đối xứng | (a,b) ⟹ (b,a) | Đối xứng | Cung hai chiều |
| Phản đối xứng | (a,b) và (b,a) ⟹ a=b | Không có cặp đối xứng ngoài đường chéo | Không có chu trình 2 chiều |
| Bắc cầu | (a,b) + (b,c) ⟹ (a,c) | Tích ma trận (sẽ học) | Đường đi → cung trực tiếp |

## Ứng dụng kỹ thuật: khóa và phép chiếu

Trong cơ sở dữ liệu, tính chất của quan hệ không chỉ để phân loại mà còn để bảo đảm dữ liệu nhất quán qua thời gian. Một **primary key** phải xác định duy nhất mỗi bộ, nghĩa là không thể để hai hàng khác nhau có cùng khóa.

Nếu không gian khóa quá nhỏ so với số bản ghi, nguyên lý pigeonhole cho thấy trùng lặp là không tránh khỏi. Vì vậy, thiết kế khóa phải đủ lớn và ổn định để duy trì tính duy nhất lâu dài.

**Phép chiếu** (projection, $$\pi$$) trong đại số quan hệ là thao tác chọn một số thuộc tính từ mỗi bộ. Đây là bản dịch trực tiếp của ý tưởng toán học: từ bộ nhiều thành phần, ta chỉ giữ lại những tọa độ cần thiết.

```sql
SELECT DISTINCT student_id
FROM Enrollments;
```

Lệnh này chính là phép chiếu $$\pi_{student\_id}(Enrollments)$$, đồng thời `DISTINCT` loại các bộ trùng sau khi bỏ bớt thuộc tính.

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

## Tóm tắt

- **Phản xạ**: mọi phần tử có quan hệ với chính nó. Ma trận: đường chéo toàn 1
- **Đối xứng**: nếu aR b thì bR a. Ma trận: đối xứng qua đường chéo
- **Phản đối xứng**: không có hai phần tử khác nhau quan hệ hai chiều
- **Bắc cầu**: quan hệ "bảo toàn" qua chuỗi: aR b và bR c kéo theo aR c
- Bốn tính chất này là nền tảng để xây dựng **quan hệ tương đương** (phản xạ + đối xứng + bắc cầu) và **quan hệ thứ tự** (phản xạ + phản đối xứng + bắc cầu)

Trong bài tiếp theo, chúng ta sẽ khám phá chi tiết hai lớp quan hệ đặc biệt này và ứng dụng của chúng.
