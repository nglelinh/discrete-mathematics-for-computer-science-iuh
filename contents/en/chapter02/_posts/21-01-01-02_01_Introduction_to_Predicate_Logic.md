---
layout: post
title: "Giới thiệu Logic Vị từ"
categories: chapter02
date: 2021-01-01
order: 1
required: true
lang: vi
---

# Giới thiệu Logic Vị từ

Logic mệnh đề có hạn chế khi biểu diễn các mệnh đề phức tạp. Logic vị từ (Predicate Logic) mở rộng logic mệnh đề để có thể biểu diễn và phân tích các mệnh đề có cấu trúc phức tạp hơn.

## Hạn chế của Logic Mệnh đề

Xét các mệnh đề sau:
1. "Tất cả sinh viên đều học toán"
2. "Có một số sinh viên giỏi lập trình"
3. "Nếu x > 5 thì x² > 25"

Logic mệnh đề không thể biểu diễn được cấu trúc bên trong của các mệnh đề này.

## Các thành phần của Logic Vị từ

### 1. Vị từ (Predicate)
**Định nghĩa**: Vị từ là một hàm trả về giá trị chân lý, mô tả tính chất hoặc quan hệ.

**Ký hiệu**: P(x), Q(x,y), R(x,y,z),...

**Ví dụ**:
- P(x): "x là sinh viên"
- Q(x,y): "x lớn hơn y"
- R(x): "x là số chẵn"

### 2. Miền (Domain/Universe)
**Định nghĩa**: Tập hợp tất cả các giá trị có thể của biến.

**Ví dụ**:
- Miền của x có thể là: tập số nguyên, tập sinh viên, tập các thành phố,...

### 3. Lượng từ (Quantifiers)

#### a) Lượng từ toàn thể (Universal Quantifier)
**Ký hiệu**: ∀x P(x)
**Đọc**: "Với mọi x, P(x)" hoặc "Tất cả x đều có tính chất P"

**Ví dụ**:
- ∀x (x² ≥ 0): "Với mọi số thực x, x² không âm"
- ∀x (Student(x) → StudyMath(x)): "Tất cả sinh viên đều học toán"

#### b) Lượng từ tồn tại (Existential Quantifier)  
**Ký hiệu**: ∃x P(x)
**Đọc**: "Tồn tại x sao cho P(x)" hoặc "Có ít nhất một x có tính chất P"

**Ví dụ**:
- ∃x (x² = 4): "Tồn tại x sao cho x² = 4"
- ∃x (Student(x) ∧ GoodAtProgramming(x)): "Có sinh viên giỏi lập trình"

## Ví dụ chi tiết

### Ví dụ 1: Biểu diễn mệnh đề
Cho miền là tập sinh viên trong lớp.
- S(x): "x học môn Toán rời rạc"
- P(x): "x giỏi lập trình"
- H(x): "x chăm học"

Biểu diễn các mệnh đề:
1. "Tất cả sinh viên đều học Toán rời rạc": ∀x S(x)
2. "Có sinh viên giỏi lập trình": ∃x P(x)
3. "Tất cả sinh viên chăm học đều giỏi lập trình": ∀x (H(x) → P(x))
4. "Có sinh viên vừa chăm học vừa giỏi lập trình": ∃x (H(x) ∧ P(x))

### Ví dụ 2: Quan hệ hai biến
Cho miền là tập số thực.
- L(x,y): "x < y"
- E(x,y): "x = y"

Biểu diễn:
1. "Với mọi x, tồn tại y lớn hơn x": ∀x ∃y L(x,y)
2. "Tồn tại số nhỏ nhất": ∃x ∀y (E(x,y) ∨ L(x,y))
3. "Không có số lớn nhất": ¬∃x ∀y L(y,x)

## Thứ tự của các lượng từ

Thứ tự của các lượng từ rất quan trọng!

**Ví dụ**:
- ∀x ∃y L(x,y): "Với mọi x, tồn tại y > x" (ĐÚNG với số thực)
- ∃y ∀x L(x,y): "Tồn tại y sao cho mọi x đều < y" (SAI với số thực)

## Phủ định của lượng từ

### Định luật De Morgan cho lượng từ:
- ¬∀x P(x) ≡ ∃x ¬P(x)
- ¬∃x P(x) ≡ ∀x ¬P(x)

**Ví dụ**:
- ¬∀x (x² ≥ 0) ≡ ∃x (x² < 0): "Không phải mọi x đều có x² ≥ 0" ≡ "Tồn tại x có x² < 0"

## Ứng dụng trong Khoa học Máy tính

### 1. Đặc tả phần mềm
```
Tiền điều kiện: ∀i (0 ≤ i < n → a[i] ≥ 0)
Hậu điều kiện: ∃j (0 ≤ j < n ∧ a[j] = max)
```

### 2. Cơ sở dữ liệu (SQL)
```sql
-- ∀x (Student(x) → ∃y (Course(y) ∧ Enrolled(x,y)))
-- "Mọi sinh viên đều đăng ký ít nhất một môn học"

SELECT * FROM Student s 
WHERE EXISTS (
    SELECT * FROM Enrollment e 
    WHERE e.student_id = s.id
);
```

### 3. Trí tuệ nhân tạo
```prolog
% ∀x (Human(x) → Mortal(x))
mortal(X) :- human(X).

% ∃x (Human(x) ∧ Philosopher(x))  
human(socrates).
philosopher(socrates).
```

## Bài tập thực hành

### Bài tập 1: Biểu diễn mệnh đề
Cho miền là tập số nguyên, biểu diễn các mệnh đề sau:
1. "Mọi số chẵn đều chia hết cho 2"
2. "Tồn tại số nguyên tố lẻ"
3. "Không có số nguyên nào lớn hơn tất cả các số nguyên khác"
4. "Với mọi số nguyên dương, tồn tại số nguyên dương lớn hơn nó"

### Bài tập 2: Phủ định
Viết phủ định của các mệnh đề sau:
1. ∀x (P(x) → Q(x))
2. ∃x (R(x) ∧ S(x))
3. ∀x ∃y L(x,y)
4. ∃x ∀y (P(x) → Q(y))

<details>
<summary>Đáp án Bài tập 2</summary>

1. ∃x (P(x) ∧ ¬Q(x))
2. ∀x (¬R(x) ∨ ¬S(x))
3. ∃x ∀y ¬L(x,y)
4. ∀x ∃y (P(x) ∧ ¬Q(y))

</details>

### Bài tập 3: Ứng dụng thực tế
Một hệ thống quản lý thư viện có:
- Book(x): "x là sách"
- Student(x): "x là sinh viên"
- Borrowed(x,y): "x mượn sách y"
- Available(x): "sách x có sẵn"

Biểu diễn các quy tắc:
1. "Mọi sinh viên đều có thể mượn sách"
2. "Không có sách nào vừa được mượn vừa có sẵn"
3. "Tồn tại sinh viên chưa mượn sách nào"

## Tóm tắt

- **Logic vị từ** mở rộng logic mệnh đề với vị từ và lượng từ
- **Vị từ P(x)**: hàm trả về giá trị chân lý
- **∀x P(x)**: "Với mọi x, P(x)"
- **∃x P(x)**: "Tồn tại x sao cho P(x)"
- **Thứ tự lượng từ** rất quan trọng
- **Phủ định**: ¬∀x P(x) ≡ ∃x ¬P(x)

Trong bài tiếp theo, chúng ta sẽ học về **các quy tắc suy luận** trong logic vị từ và cách áp dụng chúng trong chứng minh.
