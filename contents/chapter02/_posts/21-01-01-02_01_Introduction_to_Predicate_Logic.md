---
layout: post
title: "Giới thiệu Logic Vị từ"
categories: chapter02
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Logic Vị từ

Trong chương trước, logic mệnh đề đã cho chúng ta khả năng phân tích các phát biểu đúng/sai và ghép chúng lại bằng các phép toán. Nhưng hãy thử diễn đạt câu sau bằng logic mệnh đề: *"Mọi sinh viên đều phải đăng ký ít nhất một học phần."* Bạn sẽ thấy ngay vấn đề — logic mệnh đề không có cách nào nói về "mọi", "tồn tại", hay "với mỗi đối tượng x thỏa tính chất P".

Đây không phải hạn chế lý thuyết suông. Trong thực tế, hầu hết các yêu cầu phần mềm đều chứa cấu trúc kiểu này:

- *"Mọi giao dịch phải được xác thực trước khi xử lý."*
- *"Tồn tại ít nhất một server còn hoạt động trong cluster."*
- *"Với mỗi người dùng, có đúng một mã định danh duy nhất."*

Nếu chỉ gán cả câu vào một biến `p` hay `q`, ta mất toàn bộ cấu trúc bên trong — không thể suy luận, không thể kiểm chứng tự động, không thể viết truy vấn hay đặc tả hình thức.

**Logic vị từ** giải quyết chính xác vấn đề này. Nó mở rộng logic mệnh đề bằng cách thêm vào ba thành phần mới: **đối tượng** (biến), **thuộc tính/quan hệ** (vị từ), và **phạm vi** (lượng từ). Nhờ đó, ta có thể mô hình hóa thế giới thực một cách chi tiết và chính xác hơn rất nhiều.

Đây chính là nền tảng đứng sau:

- câu lệnh SQL với `WHERE`, `EXISTS`, `FOR ALL`,
- ngôn ngữ lập trình logic như Prolog,
- formal verification — kiểm chứng phần mềm bằng toán học,
- và các hệ suy luận trong trí tuệ nhân tạo.

Trong bài học này, chúng ta sẽ bắt đầu từ câu hỏi: **Vị từ là gì? Và làm sao biến một phát biểu có chứa biến thành mệnh đề có thể đánh giá đúng/sai?**

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Nhận biết** hạn chế của logic mệnh đề trong biểu diễn câu phức tạp.
- **Định nghĩa** vị từ (predicate) và miền xác định (domain).
- **Viết** vị từ một hoặc nhiều biến.
- **Phân biệt** vị từ và mệnh đề.
- **Liên hệ** vị từ với hàm Boolean trong lập trình.

**Từ khóa**: Vị từ (predicate), logic bậc nhất (first-order logic), miền xác định (domain), hàm Boolean.

## Hạn chế của Logic Mệnh đề

Xét các mệnh đề sau:
1. "Tất cả sinh viên đều học toán"
2. "Có một số sinh viên giỏi lập trình"
3. "Nếu x > 5 thì x² > 25"

Logic mệnh đề không thể biểu diễn được cấu trúc bên trong của các mệnh đề này.

<div class="content-box insight-box" markdown="1">
**Tại sao không?** Trong logic mệnh đề, bạn chỉ có thể đặt tên cho toàn bộ câu. p = "Tất cả sinh viên đều học toán". Nhưng nếu muốn suy luận "An là sinh viên, vậy An học toán", bạn cần biết cấu trúc bên trong của p — điều mà logic mệnh đề không cho phép. Logic vị từ giải quyết vấn đề này.
</div>

## Các thành phần của Logic Vị từ

### 1. Vị từ (Predicate)
**Định nghĩa**: Vị từ là một hàm trả về giá trị chân lý, mô tả tính chất hoặc quan hệ.

**Ký hiệu**: P(x), Q(x,y), R(x,y,z),...

**Ví dụ**:
- P(x): "x là sinh viên"
- Q(x,y): "x lớn hơn y"
- R(x): "x là số chẵn"

<div class="content-box note-box" markdown="1">
**Phân biệt vị từ và mệnh đề**: P(x) chưa phải là mệnh đề vì chưa biết x. Nhưng P(An) — thay x bằng "An" — là một mệnh đề, vì có thể xác định đúng/sai. Nói cách khác, vị từ là mệnh đề với các ô trống; khi điền đầy ô trống, ta có mệnh đề.
</div>

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

<div class="content-box warning-box" markdown="1">
**Lỗi thường gặp**: Nhiều sinh viên nghĩ ∀x ∃y và ∃y ∀x là như nhau. Hoàn toàn không! Hãy nhớ: ∀x ∃y — mỗi x chọn y riêng; ∃y ∀x — cùng một y cho mọi x. Đây là khác biệt cốt lõi và sẽ xuất hiện xuyên suốt chương này.
</div>

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter02/predicate_structure.svg" alt="Sơ đồ cấu trúc logic vị từ: vị từ, miền, lượng từ" width="65%" height="65%">
  <figcaption style="text-align: center;">Hình 2.1: Ba thành phần của logic vị từ — vị từ (tính chất/quan hệ), miền xác định (tập đối tượng), lượng từ (∀ và ∃)</figcaption>
</p>
</figure>

## Ứng dụng trong Khoa học Máy tính

### 1. SQL và Cơ sở dữ liệu

SQL WHERE clause là một ứng dụng trực tiếp của logic vị từ:

```sql
-- ∀x: "Tất cả sinh viên có GPA > 3.0"
SELECT * FROM Students WHERE GPA > 3.0;

-- ∃x: "Có ít nhất một sinh viên tên 'An'"
SELECT * FROM Students WHERE Name = 'An';
```

### 2. Kiểm tra điều kiện mảng

```python
# ∀i: tất cả phần tử dương
all_satisfy = all(x > 0 for x in arr)

# ∃i: có ít nhất một số chẵn
exists = any(x % 2 == 0 for x in arr)
```

### 3. Kiểu dữ liệu generic

Trong TypeScript, Java, Rust — các hàm generic hoạt động "với mọi kiểu T". Đây chính là lượng từ toàn thể:

```typescript
// ∀T: với mọi kiểu T
function identity<T>(x: T): T { return x; }
```

### 4. Kiểm chứng chương trình

Bất biến vòng lặp thường được biểu diễn bằng vị từ và lượng từ:
- $$\forall i (0 \leq i < k \implies P(a[i]))$$ — mọi phần tử trong đoạn [0..k-1] đều thỏa P

## Logic vị từ trong Trí tuệ Nhân tạo

Logic vị từ mở rộng logic mệnh đề bằng cách cho phép mô tả **quan hệ giữa các đối tượng**. Thay vì chỉ có mệnh đề nguyên tử như `p`, ta có thể viết `Knows(Alice, Bob)` hay `Enrolled(x, y)` để diễn đạt cấu trúc tri thức rõ hơn.

Các hệ suy luận AI như Prolog hay knowledge base dựa trên vị từ để rút ra kết luận mới từ luật cũ. Ví dụ, nếu biết `Student(An)` và luật `∀x (Student(x) → HasID(x))`, hệ có thể suy ra `HasID(An)`.

Trong NLP, predicate structure giúp mô hình hóa quan hệ giữa từ và thực thể: ai làm hành động nào, tác động lên đối tượng nào, và trong ngữ cảnh gì. Đây là nền của information extraction và semantic parsing.

Ví dụ tiêu biểu trong logic bậc nhất là:

$$Knows(Alice, Bob)$$

$$\forall x\,(Student(x) \to \exists y\,(Course(y) \land Enrolled(x,y)))$$

Mệnh đề thứ hai diễn đạt: mọi sinh viên đều tồn tại ít nhất một học phần mà họ đăng ký.

## Bài tập thực hành

### Bài tập 1: Biểu diễn vị từ
Viết vị từ cho các câu sau:
1. "x là số nguyên tố"
2. "x và y là bạn cùng lớp"
3. "x nằm giữa y và z"

### Bài tập 2: Vị từ hay mệnh đề?
Xác định các biểu thức sau là vị từ hay mệnh đề:
1. P(5) với P(x): "x > 3"
2. Q(x, y) với Q(x,y): "x + y = 10"
3. "2 + 2 = 5"

<details>
<summary>Đáp án</summary>

1. **Mệnh đề** — P(5) là "5 > 3", có giá trị chân lý T.
2. **Vị từ** — Q(x,y) chưa biết x,y nên chưa xác định được đúng/sai.
3. **Mệnh đề** — Câu khẳng định có giá trị chân lý F.
</details>

### Bài tập 3: Từ câu tiếng Việt sang logic
Biểu diễn bằng vị từ và lượng từ:
1. Mọi số chẵn đều chia hết cho 2.
2. Có một số nguyên tố nhỏ hơn 5.
3. Không phải mọi loài chim đều biết bay.

## Tóm tắt

- Logic mệnh đề không đủ để biểu diễn câu có cấu trúc bên trong
- **Vị từ** (predicate) là hàm trả về True/False, mô tả tính chất hoặc quan hệ
- **Miền xác định** (domain) là tập giá trị của biến
- Vị từ P(x) trở thành mệnh đề khi thay x bằng một giá trị cụ thể
- **Lượng từ toàn thể** ∀ và **lượng từ tồn tại** ∃ cho phép nói về "mọi" hoặc "một số"
- Thứ tự lượng từ thay đổi ý nghĩa của mệnh đề

Trong bài tiếp theo, chúng ta sẽ học chi tiết về **lượng từ và lượng từ lồng nhau**.
