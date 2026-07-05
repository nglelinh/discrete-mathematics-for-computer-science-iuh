---

layout: post
title: "Giới thiệu Logic Vị từ"
categories: chapter02
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Trong chương này chúng ta mở rộng logic mệnh đề thành logic vị từ (first-order logic) — hệ thống cho phép nói về đối tượng, thuộc tính, quan hệ và phạm vi…"
---

<div class="textbook-epigraph" markdown="1">

"The symbols of mathematics are not mere marks on paper; they represent ideas that can be combined and manipulated according to precise rules."

<span class="epigraph-attribution">— Alfred North Whitehead</span>

</div>

Trong chương này chúng ta mở rộng **logic mệnh đề** thành **logic vị từ** (first-order logic) — hệ thống cho phép nói về đối tượng, thuộc tính, quan hệ và phạm vi lượng hóa (∀, ∃). Đây là bước tiếp theo để biểu diễn yêu cầu phần mềm, truy vấn cơ sở dữ liệu và đặc tả hình thức một cách chính xác. Mục 2.1 bắt đầu từ khái niệm **vị từ** (predicate) và hạn chế của logic mệnh đề khi gặp phát biểu có cấu trúc bên trong.

Ở chương trước, logic mệnh đề cho phép phân tích phát biểu đúng/sai và ghép chúng bằng các phép toán logic. Tuy nhiên, câu *"Mọi sinh viên đều phải đăng ký ít nhất một học phần"* không thể được mô hình hóa đầy đủ nếu chỉ gán cả câu vào một biến $$p$$: chúng ta cần nói về *mọi*, *tồn tại*, và *đối tượng cụ thể* — điều mà logic mệnh đề không hỗ trợ.

Logic vị từ bổ sung ba thành phần: **biến** (đối tượng), **vị từ** (thuộc tính hoặc quan hệ), và **lượng từ** (phạm vi). Nhờ đó, chúng ta có thể viết truy vấn SQL với `WHERE` và `EXISTS`, đặc tả trong Prolog, và xây dựng các hệ suy luận trong kiểm chứng phần mềm và trí tuệ nhân tạo. Mục này trả lời hai câu hỏi căn bản: **vị từ là gì**, và **làm sao biến phát biểu có biến thành mệnh đề có thể đánh giá đúng/sai**.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nhận biết** hạn chế của logic mệnh đề trong biểu diễn câu phức tạp.
- **Định nghĩa** vị từ (predicate) và miền xác định (domain).
- **Viết** vị từ một hoặc nhiều biến.
- **Phân biệt** vị từ và mệnh đề.
- **Liên hệ** vị từ với hàm Boolean trong lập trình.


**Từ khóa**: Vị từ (predicate), logic bậc nhất (first-order logic), miền xác định (domain), hàm Boolean.
</div>


## Hạn chế của Logic Mệnh đề

Xét các mệnh đề sau:
1. "Tất cả sinh viên đều học toán"
2. "Có một số sinh viên giỏi lập trình"
3. "Nếu x > 5 thì x² > 25"

Logic mệnh đề không thể biểu diễn được cấu trúc bên trong của các mệnh đề này.

![Chân dung Aristotle](/discrete-mathematics-for-computer-science-iuh/img/course/Aristotle.jpg)

<p class="textbook-figure-caption" data-figure="2.1">Aristotle — một trong những nền tảng của logic hình thức phương Tây; logic vị từ mở rộng logic mệnh đề để biểu diễn cấu trúc bên trong phát biểu.</p>
<div class="content-box insight-box textbook-block" markdown="1">
Trong logic mệnh đề, ta chỉ có thể đặt tên cho toàn bộ câu: $$p$$ = "Tất cả sinh viên đều học toán". Nhưng để suy luận "An là sinh viên, vậy An học toán", cần biết cấu trúc bên trong của $$p$$ — điều mà logic mệnh đề không cho phép. Logic vị từ giải quyết vấn đề này bằng cách tách đối tượng, thuộc tính và phạm vi.
</div>

## Các thành phần của Logic Vị từ

### 1. Vị từ (Predicate)
<div class="textbook-definition" markdown="1">
**Định nghĩa**: Vị từ là một hàm trả về giá trị chân lý, mô tả tính chất hoặc quan hệ.
</div>


**Ký hiệu**: P(x), Q(x,y), R(x,y,z),...

<div class="textbook-example" markdown="1">
**Ví dụ**:
- P(x): "x là sinh viên"
- Q(x,y): "x lớn hơn y"
- R(x): "x là số chẵn"
</div>


#### Minh họa: vị từ như mẫu câu có chỗ trống

Vị từ có thể được hình dung như một **mẫu câu có ô trống**: `P(x)` = "___ là sinh viên". Khi gán `x = An`, ta có `P(An)` = "An là sinh viên" — đây là **mệnh đề** có giá trị chân lý. Khi gán `x = 5`, `P(5)` = "5 là sinh viên" cũng là mệnh đề, nhưng sai. Quy tắc tổng quát: vị từ kết hợp với giá trị cụ thể tạo thành mệnh đề; vị từ chưa được gán giá trị thì chưa phải mệnh đề.

**Ví dụ trong lập trình**:

```python
# Vị từ
def is_student(x):
    return x in students_list

# Mệnh đề (đã có giá trị)
is_student("An")      # True hoặc False
is_student("Nguyễn")  # True hoặc False
```

![Cú pháp logic bậc nhất](/discrete-mathematics-for-computer-science-iuh/img/course/Logiquepremierordre_syntaxe.svg)

<p class="textbook-figure-caption" data-figure="2.2">Cây cú pháp của công thức logic bậc nhất — vị từ kết hợp với lượng từ và các phép toán logic tạo thành công thức có cấu trúc phân cấp.</p>
### 2. Miền (Domain/Universe)
<div class="textbook-definition" markdown="1">
**Định nghĩa**: Tập hợp tất cả các giá trị có thể của biến.
</div>


<div class="textbook-example" markdown="1">
**Ví dụ**:
- Miền của x có thể là: tập số nguyên, tập sinh viên, tập các thành phố,...
</div>


### 3. Lượng từ (Quantifiers)

#### a) Lượng từ toàn thể (Universal Quantifier)
**Ký hiệu**: ∀x P(x)
**Đọc**: "Với mọi x, P(x)" hoặc "Tất cả x đều có tính chất P"

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ∀x (x² ≥ 0): "Với mọi số thực x, x² không âm"
- ∀x (Student(x) → StudyMath(x)): "Tất cả sinh viên đều học toán"
</div>


#### b) Lượng từ tồn tại (Existential Quantifier)  
**Ký hiệu**: ∃x P(x)
**Đọc**: "Tồn tại x sao cho P(x)" hoặc "Có ít nhất một x có tính chất P"

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ∃x (x² = 4): "Tồn tại x sao cho x² = 4"
- ∃x (Student(x) ∧ GoodAtProgramming(x)): "Có sinh viên giỏi lập trình"

![Ký hiệu hai lượng từ](/discrete-mathematics-for-computer-science-iuh/img/course/Symboles_math_matiques_des_deux_quantificateurs_logiques.png)

<p class="textbook-figure-caption" data-figure="2.3">Ký hiệu ∀ (với mọi) và ∃ (tồn tại) — hai lượng từ cơ bản mở rộng logic mệnh đề sang logic vị từ.</p>
</div>

## Ví dụ chi tiết

<div class="textbook-example" markdown="1">
**Ví dụ 1**: Biểu diễn mệnh đề:
Cho miền là tập sinh viên trong lớp.
- S(x): "x học môn Toán rời rạc"
- P(x): "x giỏi lập trình"
- H(x): "x chăm học"

Biểu diễn các mệnh đề:
1. "Tất cả sinh viên đều học Toán rời rạc": ∀x S(x)
2. "Có sinh viên giỏi lập trình": ∃x P(x)
3. "Tất cả sinh viên chăm học đều giỏi lập trình": ∀x (H(x) → P(x))
4. "Có sinh viên vừa chăm học vừa giỏi lập trình": ∃x (H(x) ∧ P(x))
</div>


<div class="textbook-example" markdown="1">
**Ví dụ 2**: Quan hệ hai biến:
Cho miền là tập số thực.
- L(x,y): "x < y"
- E(x,y): "x = y"

Biểu diễn:
1. "Với mọi x, tồn tại y lớn hơn x": ∀x ∃y L(x,y)
2. "Tồn tại số nhỏ nhất": ∃x ∀y (E(x,y) ∨ L(x,y))
3. "Không có số lớn nhất": ¬∃x ∀y L(y,x)
</div>


## Thứ tự của các lượng từ

Thứ tự của các lượng từ quyết định ý nghĩa của công thức và không thể hoán đổi tùy ý.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ∀x ∃y L(x,y): "Với mọi x, tồn tại y > x" (ĐÚNG với số thực)
- ∃y ∀x L(x,y): "Tồn tại y sao cho mọi x đều < y" (SAI với số thực)

![Phạm vi lượng từ lồng nhau](/discrete-mathematics-for-computer-science-iuh/img/course/QuantifierScopes_svg.svg)

<p class="textbook-figure-caption" data-figure="2.4">Phạm vi (scope) của lượng từ — thứ tự và phạm vi ∀, ∃ quyết định ý nghĩa khi nhiều lượng từ xuất hiện trong cùng một công thức.</p>
</div>

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

![George Boole](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="2.5">George Boole — cha đẻ của đại số Boolean; nền tảng của logic mệnh đề và mở rộng sang logic vị từ trong khoa học máy tính.</p>
## Logic vị từ trong Trí tuệ Nhân tạo

Logic vị từ mở rộng logic mệnh đề bằng cách cho phép mô tả **quan hệ giữa các đối tượng**. Thay vì chỉ có mệnh đề nguyên tử như `p`, ta có thể viết `Knows(Alice, Bob)` hay `Enrolled(x, y)` để diễn đạt cấu trúc tri thức rõ hơn.

Các hệ suy luận AI như Prolog hay knowledge base dựa trên vị từ để rút ra kết luận mới từ luật cũ. Ví dụ, nếu biết `Student(An)` và luật `∀x (Student(x) → HasID(x))`, hệ có thể suy ra `HasID(An)`.

Trong NLP, predicate structure giúp mô hình hóa quan hệ giữa từ và thực thể: ai làm hành động nào, tác động lên đối tượng nào, và trong ngữ cảnh gì. Đây là nền của information extraction và semantic parsing.

Ví dụ tiêu biểu trong logic bậc nhất là:

<div class="textbook-equation" markdown="1">
$$Knows(Alice, Bob)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$\forall x\,(Student(x) \to \exists y\,(Course(y) \land Enrolled(x,y)))$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
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

### Bài tập 4: Truth of Quantified Predicates

**A.9** Let P(x, y) be the predicate "x < y < x + 1". For each of the following propositions, determine whether it's true or false, and justify your answer.

(a) (∀x ∈ ℤ) (∃y ∈ ℝ) P(x, y)

(b) (∀x ∈ ℝ) (∃y ∈ ℤ) P(x, y)

(c) (∃y ∈ ℝ) (∀x ∈ ℤ) ¬P(x, y)

(d) (∃y ∈ ℤ) (∀x ∈ ℝ) ¬P(x, y)

<details>
<summary>Đáp án</summary>

(a) **Đúng.** Với mọi số nguyên x, ta chọn y = x + 0.5. Khi đó x < x + 0.5 < x + 1 luôn đúng.

(b) **Sai.** Chọn x = 0. Chọn y nguyên bất kỳ. Điều kiện y < x + 1 = 1 và y > x = 0 cho thấy y phải là số thực giữa 0 và 1, không có số nguyên nào thỏa mãn. Phản ví dụ: x = 0, không tồn tại y ∈ ℤ để 0 < y < 1.

(c) **Đúng.** Lấy y = 0.5. Với mọi x ∈ ℤ, P(x, 0.5) tức x < 0.5 < x + 1 luôn sai khi x ≠ 0 (vì nếu x ≥ 1 thì x > 0.5, nếu x ≤ -1 thì x + 1 ≤ 0 < 0.5). Với x = 0, 0 < 0.5 < 1 là đúng, nhưng ta cần ¬P(x, y) cho mọi x, và x = 0 là phản ví dụ. Thực tế mệnh đề này **sai** vì ∀x ∈ ℤ: x < 0.5 < x + 1 chỉ sai với x ≥ 1 hoặc x ≤ -1, nhưng với x = 0 thì đúng.

(d) **Sai.** Lấy y nguyên bất kỳ. Với x = y, P(y, y) tức y < y < y + 1, hiển nhiên sai. Nhưng cần ¬P(x, y) đúng với ∀x ∈ ℝ. Với x = y - 0.5, P(y - 0.5, y): y - 0.5 < y < y + 0.5 đúng, nên ¬P sai. Vậy không tồn tại y ∈ ℤ thỏa mãn.

</details>

### Bài tập 5: Xác định vị từ và miền xác định

Cho các câu sau, hãy xác định vị từ (predicate) và miền xác định (domain) phù hợp:

(a) "Mọi số nguyên tố đều lớn hơn 1."
(b) "Có một số thực x sao cho x² = -1."
(c) "Mọi sinh viên CNTT đều học Toán Rời Rạc."
(d) "Một vài hàm số là không liên tục."
(e) "Tất cả loài chim đều biết bay."

<details>
<summary>Đáp án</summary>

(a) Vị từ $$P(x)$$: "x là số nguyên tố" với miền $$U = \mathbb{Z}$$.
    Hoặc: $$P(x)$$: "x > 1" với miền $$U = \{\text{số nguyên tố}\}$$.
    Dạng logic: $$\forall x (Prime(x) \to x > 1)$$.

(b) Vị từ $$Q(x)$$: "x² = -1" với miền $$U = \mathbb{R}$$.
    Dạng logic: $$\exists x (x^2 = -1)$$.
    Giá trị: **Sai** — không có số thực nào thỏa mãn x² = -1.

(c) Vị từ $$S(x)$$: "x học Toán Rời Rạc" với miền $$U = \{\text{sinh viên CNTT}\}$$.
    Dạng logic: $$\forall x S(x)$$.

(d) Vị từ $$F(x)$$: "x là không liên tục" với miền $$U = \{\text{các hàm số}\}$$.
    Dạng logic: $$\exists x F(x)$$.
    Giá trị: **Đúng** — ví dụ hàm $$f(x) = \frac{1}{x}$$ không liên tục tại x = 0.

(e) Vị từ $$B(x)$$: "x biết bay" với miền $$U = \{\text{loài chim}\}$$.
    Dạng logic: $$\forall x B(x)$$.
    Giá trị: **Sai** — có những loài chim không bay được như đà điểu (ostrich), chim cánh cụt (penguin).

</details>

### Bài tập 6: Từ vị từ đến hàm Boolean

Chuyển các vị từ sau thành hàm Python (trả về True/False):

(a) P(x): "x là số chẵn" với miền ℤ.
(b) Q(x, y): "x chia hết cho y" với miền ℤ × ℤ⁺.
(c) R(x): "x là palindrome" với miền là các chuỗi ký tự.
(d) S(x, y, z): "z là tổng của x và y" với miền ℤ × ℤ × ℤ.

<details>
<summary>Đáp án</summary>

```python
def P(x):
    """x là số chẵn"""
    return x % 2 == 0

def Q(x, y):
    """x chia hết cho y"""
    if y <= 0:
        raise ValueError("y phải là số nguyên dương")
    return x % y == 0

def R(x):
    """x là palindrome"""
    if not isinstance(x, str):
        raise TypeError("x phải là chuỗi")
    cleaned = x.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def S(x, y, z):
    """z là tổng của x và y"""
    return z == x + y

# Test cases
print(P(4))     # True
print(P(7))     # False
print(Q(10, 5)) # True
print(Q(10, 3)) # False
print(R("racecar"))    # True
print(R("hello"))     # False
print(R("A man a plan a canal panama"))  # True
print(S(2, 3, 5))  # True
print(S(2, 3, 6))  # False
```

</details>

### Bài tập 7: Phân biệt ngữ nghĩa vị từ

Trong mỗi cặp sau, hai phát biểu có khác nhau về mặt logic không? Giải thích.

(a) "Tất cả sinh viên đều giỏi toán." và "Không có sinh viên nào không giỏi toán."
(b) "Một số người thích cà phê." và "Không phải mọi người đều không thích cà phê."
(c) "Mọi số thực đều có bình phương không âm." và "Tồn tại số thực có bình phương âm."

<details>
<summary>Đáp án</summary>

(a) **Tương đương.** Đặt $$G(x)$$: "x giỏi toán".
    - Câu 1: $$\forall x G(x)$$
    - Câu 2: $$\neg\exists x \neg G(x)$$ — "không có ai không giỏi toán"
    Theo luật tương đương: $$\forall x G(x) \equiv \neg\exists x \neg G(x)$$

(b) **Tương đương.** Đặt $$C(x)$$: "x thích cà phê".
    - Câu 1: $$\exists x C(x)$$
    - Câu 2: $$\neg\forall x \neg C(x)$$ — "không phải mọi người đều không thích cà phê"
    Theo luật tương đương: $$\exists x C(x) \equiv \neg\forall x \neg C(x)$$

(c) **Phủ định của nhau.** Đặt $$N(x)$$: "x có bình phương không âm".
    - Câu 1: $$\forall x N(x)$$ — đúng với số thực (vì $$x^2 \geq 0$$ với mọi $$x \in \mathbb{R}$$)
    - Câu 2: $$\exists x \neg N(x)$$ — sai vì không có số thực nào có bình phương âm
    Hai câu là phủ định của nhau: $$\neg\forall x N(x) \equiv \exists x \neg N(x)$$.

</details>

### Bài tập 8: Vị từ trong xử lý ảnh

Trong một hệ thống nhận dạng ảnh, ta có các vị từ sau với miền là các pixel:
- $$R(p)$$: pixel p có màu đỏ
- $$G(p)$$: pixel p có màu xanh lá
- $$B(p)$$: pixel p có màu xanh dương
- $$E(p)$$: pixel p là biên (edge)
- $$Bright(p)$$: pixel p có độ sáng > 200

Viết công thức logic cho:

(a) "Mọi pixel ở biên đều có độ sáng cao."
(b) "Có ít nhất một pixel màu đỏ và xanh dương." (Chỉ một pixel không thể vừa đỏ vừa xanh dương — hãy giải thích!)
(c) "Mọi pixel không phải biên đều không phải màu đỏ."
(d) "Tồn tại một pixel vừa là biên vừa có màu xanh lá."

<details>
<summary>Đáp án</summary>

(a) $$\forall p (E(p) \to Bright(p))$$
    "Nếu p là biên thì p có độ sáng cao."

(b) $$\exists p (R(p) \land B(p))$$
    Về mặt logic, công thức này hoàn toàn hợp lệ. Trong thực tế, một pixel không thể vừa đỏ vừa xanh dương (mỗi pixel có một màu duy nhất trong hệ màu RGB), nhưng xét thuần túy logic, không có ràng buộc nào cấm cả hai vị từ cùng đúng. Đây là điểm khác biệt giữa logic và thực tế vật lý — nếu muốn mô hình hóa chính xác, ta cần thêm ràng buộc: mỗi pixel chỉ có đúng một màu.

(c) $$\forall p (\neg E(p) \to \neg R(p))$$
    Tương đương với: $$\forall p (R(p) \to E(p))$$ (theo contrapositive).
    Nghĩa là mọi pixel đỏ đều là biên — điều này khác với câu gốc về mặt ngữ nghĩa, dù tương đương về mặt logic.

(d) $$\exists p (E(p) \land G(p))$$

</details>

## Bài tập bổ sung: Xác định giá trị chân lý (từ ccrr1_baitap1)

**Bài tập logic vị từ:** Xác định giá trị chân lý (true/false) của các mệnh đề sau (với miền xác định R số thực):

1. ∃x ∈ R, x² = 2

2. ∃x ∈ R ∃y ∈ R, x + y ≠ y + x

3. ∃x ∈ R ∃y ∈ R, (x + 2y = 2) ∧ (2x + 4y = 5)

4. ∃x ∈ R, 2x² + 3x − 5 = 0

5. ∀x ∈ R, (3x² + 4x + 5 = 0) → (2x³ + 3x − 1 = 0)

6. ∀x ∈ [0, 5], (2/3)x³ + 2x ≥ −2

Trong bài tiếp theo, chúng ta sẽ học chi tiết về **lượng từ và lượng từ lồng nhau**.

---

## Xem thêm / Video gợi ý

- [Quantifiers and Nested Quantifiers](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — Trefor Bazett (Clear examples with predicates)
- [Predicate Logic — ∀ and ∃](https://www.youtube.com/watch?v=8l7L9v0p0Q) — TrevTutor (Discrete Math playlist)


## Tóm tắt

- Logic mệnh đề không biểu diễn được cấu trúc "mọi", "tồn tại" hay quan hệ giữa đối tượng; logic vị từ bổ sung **biến**, **vị từ** và **lượng từ**.
- **Vị từ** $$P(x)$$ là phát biểu chứa biến; khi gán giá trị cụ thể trong **miền xác định**, ta thu được **mệnh đề** có giá trị chân lý.
- Lượng từ toàn thể $$\forall$$ và tồn tại $$\exists$$ mở rộng phạm vi phát biểu; **thứ tự lượng từ** quyết định ý nghĩa công thức.
- Trong khoa học máy tính, vị từ xuất hiện trong SQL, hàm Boolean, generic types, kiểm chứng chương trình và hệ suy luận AI.