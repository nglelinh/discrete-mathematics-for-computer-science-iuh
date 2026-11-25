---

layout: post
title: "Giới thiệu Logic Vị từ"
categories: chapter02
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Mở rộng logic mệnh đề thành logic vị từ (first-order logic) với biến, vị từ, miền xác định và lượng từ toàn thể, tồn tại."
---

<div class="textbook-epigraph" markdown="1">

"The symbols of mathematics are not mere marks on paper; they represent ideas that can be combined and manipulated according to precise rules."

<span class="epigraph-attribution">— Alfred North Whitehead</span>

</div>

Trong chương này, chúng ta mở rộng **logic mệnh đề** thành **logic vị từ** (first-order logic) — hệ thống cho phép diễn đạt đối tượng, thuộc tính, quan hệ và phạm vi lượng hóa ($$\forall, \exists$$). Đây là công cụ cần thiết để biểu diễn yêu cầu phần mềm, truy vấn cơ sở dữ liệu và đặc tả hình thức một cách chính xác. Mục 2.1 bắt đầu từ khái niệm **vị từ** (predicate) và hạn chế của logic mệnh đề khi gặp các phát biểu có cấu trúc bên trong.

Ở chương trước, logic mệnh đề cho phép phân tích các phát biểu đúng/sai và ghép chúng bằng các phép toán logic. Tuy nhiên, câu *"Mọi sinh viên đều phải đăng ký ít nhất một học phần"* không thể được mô hình hóa đầy đủ nếu chỉ gán cả câu vào một biến $$p$$: chúng ta cần nói về *mọi*, *tồn tại* và *đối tượng cụ thể* — những yếu tố mà logic mệnh đề không biểu diễn được.

Logic vị từ bổ sung ba thành phần: **biến** (đại diện cho đối tượng), **vị từ** (mô tả thuộc tính hoặc quan hệ) và **lượng từ** (xác định phạm vi). Nhờ đó, chúng ta có thể biểu diễn truy vấn SQL với `WHERE` và `EXISTS`, đặc tả luật trong Prolog, và xây dựng các hệ suy luận trong kiểm chứng phần mềm và trí tuệ nhân tạo. Mục này trả lời hai câu hỏi căn bản: **vị từ là gì**, và **làm thế nào chuyển phát biểu chứa biến thành mệnh đề có thể đánh giá đúng/sai**.

Logic mệnh đề rất sắc bén, nhưng nó bất lực trước câu lập luận nổi tiếng nhất thời cổ đại: *"Mọi con người đều phải chết. Socrates là con người. Vậy Socrates phải chết."* Với logic mệnh đề, ba câu đó chỉ là ba ký hiệu $$p, q, r$$ rời rạc chẳng liên quan gì nhau—ta không thể nhìn vào bên trong câu để thấy mối quan hệ giữa tập hợp *con người* và cá thể *Socrates*.

**Logic Vị từ (Predicate Logic / First-Order Logic)** mở khóa cấu trúc bên trong của phát biểu bằng **biến**, **vị từ** (hàm trả về `True`/`False`), **miền xác định (Domain)** và hai **lượng từ** ($$\forall, \exists$$)—chính là nền tảng toán học của SQL, ngôn ngữ truy vấn đồ thị, Prolog và đặc tả phần mềm.

## Kiến thức cần nhớ: Bốn viên gạch của Logic Vị từ (Bậc nhất)

1. **Vị từ (Predicate / Propositional Function)**:
   Một vị từ $$P(x)$$ là một hàm nhận đối tượng $$x$$ trong miền xác định $$D$$ và trả về giá trị chân trị (`True`/`False`). Bản thân $$P(x)$$ chưa phải mệnh đề; nó chỉ trở thành mệnh đề khi ta **gắn giá trị cụ thể** ($$P(5)$$) hoặc **ràng buộc biến bằng lượng từ** ($$\forall x\, P(x)$$).

2. **Miền xác định (Domain of Discourse / Universe)**:
   Chân trị của cùng một công thức phụ thuộc chặt chẽ vào miền xác định! Ví dụ $$\exists x\,(x^2 = 2)$$ là **Sai** trên tập số nguyên $$\mathbb{Z}$$, nhưng là **Đúng** trên tập số thực $$\mathbb{R}$$.

3. **Lượng từ Toàn thể ($$\forall$$) & Lượng từ Tồn tại ($$\exists$$)**:
   - $$\forall x\, P(x)$$ tương đương phép HỘI khổng lồ $$P(x_1) \land P(x_2) \land \dots$$ trên toàn miền (chỉ cần **1 phản ví dụ** để bác bỏ!).
   - $$\exists x\, P(x)$$ tương đương phép TUYỂN khổng lồ $$P(x_1) \lor P(x_2) \lor \dots$$ (chỉ cần **1 nhân chứng** để chứng minh!).

4. **Biến tự do (Free Variable) vs. Biến bị ràng buộc (Bound Variable)**:
   Giống hệt biến cục bộ và biến toàn cục trong lập trình, một biến nằm trong tầm vực của $$\forall x$$ hoặc $$\exists x$$ là biến bị ràng buộc; công thức không còn biến tự do nào mới có chân trị xác định.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nhận biết** hạn chế của logic mệnh đề khi biểu diễn các phát biểu có cấu trúc bên trong.
- **Định nghĩa** vị từ (predicate) và miền xác định (domain).
- **Viết** vị từ một biến hoặc nhiều biến.
- **Phân biệt** vị từ và mệnh đề.
- **Liên hệ** vị từ với hàm Boolean trong lập trình.


**Từ khóa**: Vị từ (predicate), logic bậc nhất (first-order logic), miền xác định (domain), hàm Boolean.
</div>


## Hạn chế của Logic Mệnh đề

Xét các phát biểu sau:
1. "Tất cả sinh viên đều học toán."
2. "Có một số sinh viên giỏi lập trình."
3. "Nếu $$x > 5$$ thì $$x^2 > 25$$."

Logic mệnh đề không thể biểu diễn được cấu trúc bên trong của các phát biểu này.

![Chân dung Aristotle](/discrete-mathematics-for-computer-science-iuh/img/course/Aristotle.jpg)

<p class="textbook-figure-caption" data-figure="2.1">Aristotle — một trong những nền tảng của logic hình thức phương Tây; logic vị từ mở rộng logic mệnh đề để biểu diễn cấu trúc bên trong phát biểu.</p>
<div class="content-box insight-box textbook-block" markdown="1">
Trong logic mệnh đề, ta chỉ có thể đặt tên cho toàn bộ câu, chẳng hạn $$p$$ = "Tất cả sinh viên đều học toán". Nhưng để từ đó cùng dữ kiện "An là sinh viên" suy ra "An học toán", ta cần phân tích cấu trúc bên trong của $$p$$ — điều mà logic mệnh đề không hỗ trợ. Logic vị từ giải quyết hạn chế này bằng cách tách rõ đối tượng, thuộc tính và phạm vi.
</div>

## Các thành phần của Logic Vị từ

### Vị từ (Predicate)
<div class="textbook-definition" markdown="1">
**Định nghĩa**: Vị từ là một hàm trả về giá trị chân lý, dùng để mô tả tính chất của một đối tượng hoặc quan hệ giữa nhiều đối tượng.
</div>


**Ký hiệu**: $$P(x), Q(x,y), R(x,y,z), \ldots$$

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$P(x)$$: "$$x$$ là sinh viên."
- $$Q(x,y)$$: "$$x$$ lớn hơn $$y$$."
- $$R(x)$$: "$$x$$ là số chẵn."
</div>


#### Minh họa: vị từ như mẫu câu có chỗ trống

Vị từ có thể hình dung như một **mẫu câu có ô trống**: `P(x)` = "___ là sinh viên". Khi gán `x = An`, ta thu được `P(An)` = "An là sinh viên" — đây là một **mệnh đề** có giá trị chân lý xác định. Khi gán `x = 5`, `P(5)` = "5 là sinh viên" cũng là một mệnh đề (có giá trị sai). Như vậy, vị từ khi được gán giá trị cụ thể sẽ trở thành mệnh đề, còn khi chưa gán giá trị thì chưa phải mệnh đề.

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
### Miền (Domain/Universe)
<div class="textbook-definition" markdown="1">
**Định nghĩa**: Miền xác định là tập hợp tất cả các giá trị mà biến có thể nhận.
</div>


<div class="textbook-example" markdown="1">
**Ví dụ**:
- Miền của $$x$$ có thể là tập số nguyên, tập sinh viên, tập các thành phố, v.v.
</div>


### Lượng từ (Quantifiers)

#### a) Lượng từ toàn thể (Universal Quantifier)
**Ký hiệu**: $$\forall x\, P(x)$$
**Đọc**: "Với mọi $$x$$, $$P(x)$$" hoặc "Tất cả $$x$$ đều có tính chất $$P$$".

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$\forall x\, (x^2 \geq 0)$$: "Với mọi số thực $$x$$, $$x^2$$ không âm."
- $$\forall x\, (Student(x) \to StudyMath(x))$$: "Tất cả sinh viên đều học toán."
</div>


#### b) Lượng từ tồn tại (Existential Quantifier)
**Ký hiệu**: $$\exists x\, P(x)$$
**Đọc**: "Tồn tại $$x$$ sao cho $$P(x)$$" hoặc "Có ít nhất một $$x$$ có tính chất $$P$$".

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$\exists x\, (x^2 = 4)$$: "Tồn tại $$x$$ sao cho $$x^2 = 4$$."
- $$\exists x\, (Student(x) \land GoodAtProgramming(x))$$: "Có sinh viên giỏi lập trình."

![Ký hiệu hai lượng từ](/discrete-mathematics-for-computer-science-iuh/img/course/Symboles_math_matiques_des_deux_quantificateurs_logiques.png)

<p class="textbook-figure-caption" data-figure="2.3">Ký hiệu ∀ (với mọi) và ∃ (tồn tại) — hai lượng từ cơ bản mở rộng logic mệnh đề sang logic vị từ.</p>
</div>

## Ví dụ chi tiết

<div class="textbook-example" markdown="1">
**Ví dụ 1**: Biểu diễn mệnh đề với miền là tập sinh viên trong lớp.
- $$S(x)$$: "$$x$$ học môn Toán rời rạc."
- $$P(x)$$: "$$x$$ giỏi lập trình."
- $$H(x)$$: "$$x$$ chăm học."

Các mệnh đề tương ứng:
1. "Tất cả sinh viên đều học Toán rời rạc": $$\forall x\, S(x)$$
2. "Có sinh viên giỏi lập trình": $$\exists x\, P(x)$$
3. "Tất cả sinh viên chăm học đều giỏi lập trình": $$\forall x\, (H(x) \to P(x))$$
4. "Có sinh viên vừa chăm học vừa giỏi lập trình": $$\exists x\, (H(x) \land P(x))$$
</div>


<div class="textbook-example" markdown="1">
**Ví dụ 2**: Quan hệ hai biến với miền là tập số thực.
- $$L(x,y)$$: "$$x < y$$"
- $$E(x,y)$$: "$$x = y$$"

Các mệnh đề tương ứng:
1. "Với mọi $$x$$, tồn tại $$y$$ lớn hơn $$x$$": $$\forall x\, \exists y\, L(x,y)$$
2. "Tồn tại số nhỏ nhất": $$\exists x\, \forall y\, (E(x,y) \lor L(x,y))$$
3. "Không có số lớn nhất": $$\neg\exists x\, \forall y\, (E(y,x) \lor L(y,x))$$
</div>


### Giải thích: Kiểm tra bằng tay chân trị 4 công thức trên miền hữu hạn $$D = \{1, 2, 3\}$$

Để cảm nhận chính xác $$\forall$$ là phép `AND` còn $$\exists$$ là phép `OR`, hãy tự định giá trên miền nhỏ $$D = \{1, 2, 3\}$$ với vị từ $$P(x, y): \; x + y = 4$$:

| Công thức | Mở rộng tường minh trên $$D = \{1, 2, 3\}$$ | Chân trị | Nhân chứng / Phản ví dụ |
| :--- | :--- | :---: | :--- |
| $$\forall x\, \exists y\, (x + y = 4)$$ | Với $$x=1$$ chọn $$y=3$$ (`1+3=4`); $$x=2$$ chọn $$y=2$$ (`2+2=4`); $$x=3$$ chọn $$y=1$$ (`3+1=4`) | **`True`** | Mọi $$x \in D$$ đều tìm được $$y = 4 - x \in D$$ |
| $$\exists y\, \forall x\, (x + y = 4)$$ | Cần **1 số $$y$$ cố định** sao cho $$1+y=4$$ VÀ $$2+y=4$$ VÀ $$3+y=4$$ | **`False`** | Không có số $$y$$ nào cùng lúc bằng 3, 2 và 1! |
| $$\exists x\, (x^2 > 5)$$ | $$(1 > 5) \lor (4 > 5) \lor (9 > 5)$$ | **`True`** | Nhân chứng: $$x = 3$$ ($$3^2 = 9 > 5$$) |
| $$\forall x\, (x \text{ là số lẻ})$$ | $$P(1) \land P(2) \land P(3) = \text{T} \land \text{F} \land \text{T}$$ | **`False`** | Phản ví dụ: $$x = 2$$ |

Chỉ cần nhìn hai dòng đầu ($$\forall x\, \exists y$$ đúng nhưng $$\exists y\, \forall x$$ sai), bạn thấy ngay quy tắc vàng: **không bao giờ được tùy tiện đổi thứ tự giữa $$\forall$$ và $$\exists$$**!

## Thứ tự của các lượng từ

Thứ tự xuất hiện của các lượng từ quyết định ý nghĩa của công thức và không thể hoán đổi tùy ý.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$\forall x\, \exists y\, L(x,y)$$: "Với mọi $$x$$, tồn tại $$y > x$$" (đúng trên tập số thực).
- $$\exists y\, \forall x\, L(x,y)$$: "Tồn tại $$y$$ sao cho mọi $$x$$ đều nhỏ hơn $$y$$" (sai trên tập số thực).

![Phạm vi lượng từ lồng nhau](/discrete-mathematics-for-computer-science-iuh/img/course/QuantifierScopes_svg.svg)

<p class="textbook-figure-caption" data-figure="2.4">Phạm vi (scope) của lượng từ — thứ tự và phạm vi ∀, ∃ quyết định ý nghĩa khi nhiều lượng từ xuất hiện trong cùng một công thức.</p>
</div>

## Ứng dụng trong Khoa học Máy tính

### SQL và Cơ sở dữ liệu

Mệnh đề `WHERE` trong SQL là một ứng dụng trực tiếp của vị từ trên từng bản ghi:

```sql
-- Lọc các sinh viên thỏa vị từ GPA > 3.0
SELECT * FROM Students WHERE GPA > 3.0;

-- Tìm các sinh viên thỏa vị từ Name = 'An'
SELECT * FROM Students WHERE Name = 'An';
```

### Kiểm tra điều kiện mảng

```python
# ∀x: tất cả phần tử đều dương
all_satisfy = all(x > 0 for x in arr)

# ∃x: có ít nhất một số chẵn
exists = any(x % 2 == 0 for x in arr)
```

### Kiểu dữ liệu generic

Trong TypeScript, Java hay Rust, các hàm generic hoạt động "với mọi kiểu `T`" — tương ứng với lượng từ toàn thể:

```typescript
// ∀T: với mọi kiểu T
function identity<T>(x: T): T { return x; }
```

### Kiểm chứng chương trình

Bất biến vòng lặp thường được biểu diễn bằng vị từ và lượng từ:
- $$\forall i\, (0 \leq i < k \implies P(a[i]))$$ — mọi phần tử trong đoạn `[0..k-1]` đều thỏa mãn tính chất $$P$$.

![George Boole](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="2.5">George Boole — cha đẻ của đại số Boolean; nền tảng của logic mệnh đề và mở rộng sang logic vị từ trong khoa học máy tính.</p>
## Logic vị từ trong Trí tuệ Nhân tạo

Logic vị từ mở rộng logic mệnh đề bằng cách cho phép mô tả **quan hệ giữa các đối tượng**. Thay vì chỉ có các mệnh đề nguyên tử như `p`, ta có thể viết `Knows(Alice, Bob)` hay `Enrolled(x, y)` để biểu diễn cấu trúc tri thức rõ ràng hơn.

Các hệ suy luận AI như Prolog hay cơ sở tri thức (knowledge base) dựa trên vị từ để rút ra kết luận mới từ các luật đã có. Chẳng hạn, từ `Student(An)` và luật `∀x (Student(x) → HasID(x))`, hệ thống suy ra được `HasID(An)`. Trong xử lý ngôn ngữ tự nhiên (NLP), cấu trúc vị từ giúp mô hình hóa quan hệ giữa các thực thể — ai thực hiện hành động nào, tác động lên đối tượng nào và trong ngữ cảnh nào — làm nền tảng cho trích xuất thông tin và phân tích ngữ nghĩa.

Ví dụ tiêu biểu trong logic bậc nhất:

<div class="textbook-equation" markdown="1">
$$Knows(Alice, Bob)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$\forall x\,(Student(x) \to \exists y\,(Course(y) \land Enrolled(x,y)))$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mệnh đề thứ hai diễn đạt: mọi sinh viên đều đăng ký ít nhất một học phần.

## Bài tập thực hành

### Bài tập 1: Biểu diễn vị từ
Viết vị từ cho các câu sau:
1. "$$x$$ là số nguyên tố."
2. "$$x$$ và $$y$$ là bạn cùng lớp."
3. "$$x$$ nằm giữa $$y$$ và $$z$$."

### Bài tập 2: Vị từ hay mệnh đề?
Xác định các biểu thức sau là vị từ hay mệnh đề:
1. $$P(5)$$ với $$P(x)$$: "$$x > 3$$"
2. $$Q(x, y)$$ với $$Q(x,y)$$: "$$x + y = 10$$"
3. "$$2 + 2 = 5$$"

<details>
<summary>Đáp án</summary>

1. **Mệnh đề** — $P(5)$ là "$5 > 3$", có giá trị chân lý T.
2. **Vị từ** — $Q(x,y)$ chưa biết giá trị của $x, y$ nên chưa xác định được đúng/sai.
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

(a) **Đúng.** Với mọi số nguyên $x$, chọn $y = x + 0.5 \in \mathbb{R}$. Khi đó $x < x + 0.5 < x + 1$ luôn đúng.

(b) **Sai.** Phản ví dụ: chọn $x = 0 \in \mathbb{R}$. Điều kiện $0 < y < 1$ không có số nguyên $y \in \mathbb{Z}$ nào thỏa mãn.

(c) **Đúng.** Chọn $y = 0 \in \mathbb{R}$ (hoặc bất kỳ số nguyên nào). Với mọi $x \in \mathbb{Z}$, ta xét $P(x, 0)$ là $x < 0 < x + 1$: nếu $x \geq 0$ thì $x < 0$ sai; nếu $x \leq -1$ thì $x + 1 \leq 0$ nên $0 < x + 1$ sai. Do đó $P(x, 0)$ luôn sai, tức $\neg P(x, 0)$ đúng với mọi $x \in \mathbb{Z}$.

(d) **Sai.** Với mọi số nguyên $y \in \mathbb{Z}$, ta luôn có thể chọn $x = y - 0.5 \in \mathbb{R}$; khi đó $P(y - 0.5, y)$ là $y - 0.5 < y < y + 0.5$ (đúng), nên $\neg P(x, y)$ sai. Vậy không tồn tại $y \in \mathbb{Z}$ thỏa mãn.

</details>

### Bài tập 5: Xác định vị từ và miền xác định

Cho các câu sau, hãy xác định vị từ (predicate) và miền xác định (domain) phù hợp:

(a) "Mọi số nguyên tố đều lớn hơn 1."
(b) "Có một số thực $$x$$ sao cho $$x^2 = -1$$."
(c) "Mọi sinh viên CNTT đều học Toán Rời Rạc."
(d) "Một vài hàm số là không liên tục."
(e) "Tất cả loài chim đều biết bay."

<details>
<summary>Đáp án</summary>

(a) Vị từ $Prime(x)$: "$x$ là số nguyên tố" với miền $U = \mathbb{Z}$ (hoặc vị từ "$x > 1$" với miền là tập số nguyên tố).
    Dạng logic: $\forall x\, (Prime(x) \to x > 1)$.

(b) Vị từ $Q(x)$: "$x^2 = -1$" với miền $U = \mathbb{R}$.
    Dạng logic: $\exists x\, (x^2 = -1)$.
    Giá trị chân lý: **Sai**, vì không có số thực nào có bình phương bằng $-1$.

(c) Vị từ $S(x)$: "$x$ học Toán Rời Rạc" với miền $U = \{\text{sinh viên CNTT}\}$.
    Dạng logic: $\forall x\, S(x)$.

(d) Vị từ $F(x)$: "$x$ không liên tục" với miền $U = \{\text{các hàm số}\}$.
    Dạng logic: $\exists x\, F(x)$.
    Giá trị chân lý: **Đúng**, chẳng hạn hàm $f(x) = \frac{1}{x}$ không liên tục tại $x = 0$.

(e) Vị từ $B(x)$: "$x$ biết bay" với miền $U = \{\text{loài chim}\}$.
    Dạng logic: $\forall x\, B(x)$.
    Giá trị chân lý: **Sai**, vì có những loài chim không bay được như đà điểu, chim cánh cụt.

</details>

### Bài tập 6: Từ vị từ đến hàm Boolean

Chuyển các vị từ sau thành hàm Python (trả về `True`/`False`):

(a) $$P(x)$$: "$$x$$ là số chẵn" với miền $$\mathbb{Z}$$.
(b) $$Q(x, y)$$: "$$x$$ chia hết cho $$y$$" với miền $$\mathbb{Z} \times \mathbb{Z}^+$$.
(c) $$R(x)$$: "$$x$$ là palindrome" với miền là các chuỗi ký tự.
(d) $$S(x, y, z)$$: "$$z$$ là tổng của $$x$$ và $$y$$" với miền $$\mathbb{Z} \times \mathbb{Z} \times \mathbb{Z}$$.

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

Trong mỗi cặp sau, hai phát biểu có tương đương về mặt logic không? Giải thích.

(a) "Tất cả sinh viên đều giỏi toán." và "Không có sinh viên nào không giỏi toán."
(b) "Một số người thích cà phê." và "Không phải mọi người đều không thích cà phê."
(c) "Mọi số thực đều có bình phương không âm." và "Tồn tại số thực có bình phương âm."

<details>
<summary>Đáp án</summary>

(a) **Tương đương.** Đặt $G(x)$: "$x$ giỏi toán".
    - Câu 1: $\forall x\, G(x)$
    - Câu 2: $\neg\exists x\, \neg G(x)$ ("không có ai không giỏi toán")
    Theo luật phủ định lượng từ: $\forall x\, G(x) \equiv \neg\exists x\, \neg G(x)$.

(b) **Tương đương.** Đặt $C(x)$: "$x$ thích cà phê".
    - Câu 1: $\exists x\, C(x)$
    - Câu 2: $\neg\forall x\, \neg C(x)$ ("không phải mọi người đều không thích cà phê")
    Theo luật phủ định lượng từ: $\exists x\, C(x) \equiv \neg\forall x\, \neg C(x)$.

(c) **Phủ định của nhau.** Đặt $N(x)$: "$x$ có bình phương không âm".
    - Câu 1: $\forall x\, N(x)$ (đúng trên $\mathbb{R}$ vì $x^2 \geq 0$ với mọi $x \in \mathbb{R}$).
    - Câu 2: $\exists x\, \neg N(x)$ (sai vì không có số thực nào có bình phương âm).
    Hai câu là phủ định của nhau: $\neg\forall x\, N(x) \equiv \exists x\, \neg N(x)$.

</details>

### Bài tập 8: Vị từ trong xử lý ảnh

Trong một hệ thống nhận dạng ảnh, ta có các vị từ sau với miền là các pixel:
- $$R(p)$$: pixel $$p$$ có màu đỏ
- $$G(p)$$: pixel $$p$$ có màu xanh lá
- $$B(p)$$: pixel $$p$$ có màu xanh dương
- $$E(p)$$: pixel $$p$$ là biên (edge)
- $$Bright(p)$$: pixel $$p$$ có độ sáng > 200

Viết công thức logic cho các phát biểu sau:

(a) "Mọi pixel ở biên đều có độ sáng cao."
(b) "Có ít nhất một pixel màu đỏ và xanh dương." (Giải thích sự khác biệt giữa cú pháp logic và ràng buộc vật lý.)
(c) "Mọi pixel không phải biên đều không phải màu đỏ."
(d) "Tồn tại một pixel vừa là biên vừa có màu xanh lá."

<details>
<summary>Đáp án</summary>

(a) $\forall p\, (E(p) \to Bright(p))$ — "Nếu $p$ là biên thì $p$ có độ sáng cao."

(b) $\exists p\, (R(p) \land B(p))$ — Về mặt cú pháp logic, công thức này hợp lệ vì bản thân các vị từ chưa mang ràng buộc loại trừ lẫn nhau. Nếu muốn mô hình hóa ràng buộc thực tế (mỗi pixel chỉ mang một nhãn màu duy nhất), ta cần bổ sung tiên đề rằng $R(p), G(p), B(p)$ loại trừ lẫn nhau.

(c) $\forall p\, (\neg E(p) \to \neg R(p))$ — Tương đương logic với $\forall p\, (R(p) \to E(p))$ theo quy tắc phản đảo (khác cách diễn đạt trong ngôn ngữ tự nhiên nhưng cùng ý nghĩa logic).

(d) $\exists p\, (E(p) \land G(p))$.

</details>

## Bài tập bổ sung: Xác định giá trị chân lý (từ ccrr1_baitap1)

Xác định giá trị chân lý (đúng/sai) của các mệnh đề sau với miền xác định là tập số thực $$\mathbb{R}$$:

1. $$\exists x \in \mathbb{R},\; x^2 = 2$$
2. $$\exists x \in \mathbb{R}\; \exists y \in \mathbb{R},\; x + y \neq y + x$$
3. $$\exists x \in \mathbb{R}\; \exists y \in \mathbb{R},\; (x + 2y = 2) \land (2x + 4y = 5)$$
4. $$\exists x \in \mathbb{R},\; 2x^2 + 3x - 5 = 0$$
5. $$\forall x \in \mathbb{R},\; (3x^2 + 4x + 5 = 0) \to (2x^3 + 3x - 1 = 0)$$
6. $$\forall x \in [0, 5],\; \frac{2}{3}x^3 + 2x \geq -2$$

Trong bài tiếp theo, chúng ta sẽ tìm hiểu chi tiết về **lượng từ và lượng từ lồng nhau**.

---

## Xem thêm / Video gợi ý

- [Quantifiers and Nested Quantifiers](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — Trefor Bazett (Clear examples with predicates)
- [Predicate Logic — ∀ and ∃](https://www.youtube.com/watch?v=8l7L9v0p0Q) — TrevTutor (Discrete Math playlist)


## Tóm tắt

- Logic mệnh đề không biểu diễn được cấu trúc "mọi", "tồn tại" hay quan hệ giữa các đối tượng; logic vị từ bổ sung **biến**, **vị từ** và **lượng từ**.
- **Vị từ** $$P(x)$$ là phát biểu chứa biến; khi gán giá trị cụ thể trong **miền xác định**, ta thu được **mệnh đề** có giá trị chân lý xác định.
- Lượng từ toàn thể $$\forall$$ và tồn tại $$\exists$$ mở rộng phạm vi phát biểu; **thứ tự lượng từ** quyết định ý nghĩa của công thức.
- Trong khoa học máy tính, vị từ xuất hiện trong SQL, hàm Boolean, kiểu generic, kiểm chứng chương trình và các hệ suy luận AI.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=gyoqX0W-NH4">PREDICATE LOGIC and QUANTIFIER NEGATION - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu vị từ, miền xác định và lượng từ, phù hợp làm phần mở đầu cho chương.
- <a href="https://www.youtube.com/watch?v=9MPA_LUmmoo">Predicates and their Truth Sets</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày tập chân trị của vị từ, kết nối ký hiệu $$P(x)$$ với ví dụ cụ thể.
- <a href="https://www.youtube.com/watch?v=GJpezCUMOxA">Universal and Existential Quantifiers,  ∀ &quot;For All&quot; and ∃ &quot;There Exists&quot;</a> — Dr. Trefor Bazett, tiếng Anh. Hướng dẫn cách đọc $$\forall$$ và $$\exists$$ trước khi chuyển sang lượng từ lồng nhau.
