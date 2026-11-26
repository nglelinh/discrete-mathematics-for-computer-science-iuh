---

layout: post
title: "Lượng từ và Lượng từ lồng nhau"
categories: chapter02
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Trình bày chi tiết lượng từ toàn thể, tồn tại, duy nhất, lượng từ lồng nhau, quy tắc phủ định De Morgan và cách dịch câu tự nhiên sang logic vị từ."
---

Hầu hết các định nghĩa tinh hoa nhất trong toán học và khoa học máy tính—từ định nghĩa giới hạn $$\varepsilon\text{–}\delta$$ trong giải tích, tính liên tục, cho đến ràng buộc khóa ngoại trong cơ sở dữ liệu hay thuật toán sắp xếp—đều được viết bằng **lượng từ lồng nhau (Nested Quantifiers)** như $$\forall x\,\exists y\, P(x, y)$$.

Hiểu đúng lượng từ lồng nhau giống như đọc đúng **vòng lặp `for` lồng nhau** trong mã nguồn: chỉ cần đảo sai thứ tự hai vòng lặp hoặc phủ định nhầm một dấu, toàn bộ ý nghĩa chương trình đảo ngược hoàn toàn.

## Kiến thức cần nhớ: Bốn chìa khóa làm chủ Lượng từ Lồng nhau

1. **Tương đương vòng lặp lồng nhau (`all` / `any`)**:
   - $$\forall x\, \exists y\, P(x, y)$$ $$\iff$$ `all(any(P(x, y) for y in D) for x in D)` (giá trị $$y$$ được phép **phụ thuộc** vào $$x$$).
   - $$\exists y\, \forall x\, P(x, y)$$ $$\iff$$ `any(all(P(x, y) for x in D) for y in D)` (phải chọn **một $$y$$ duy nhất dùng chung** cho mọi $$x$$).

2. **Luật De Morgan mở rộng cho Lượng từ**:
   Phủ định đi qua lượng từ sẽ **lật ngược loại lượng từ**:
   $$\neg(\forall x\, P(x)) \equiv \exists x\, \neg P(x), \qquad \neg(\exists x\, P(x)) \equiv \forall x\, \neg P(x).$$
   Với lượng từ lồng nhau, dấu $$\neg$$ đi từ trái sang phải và lật lần lượt từng lượng từ một!

3. **Lượng từ tồn tại duy nhất ($$\exists! x\, P(x)$$)**:
   Diễn tả *"có đúng một phần tử $$x$$ thỏa $$P(x)$$"*, được định nghĩa chặt bằng hai vế: **tồn tại** ($$\exists x\, P(x)$$) VÀ **duy nhất** ($$\forall y\,(P(y) \to y = x)$$).

4. **Cách ghép điều kiện giới hạn miền với $$\forall$$ và $$\exists$$**:
   Lỗi kinh điển nhất của sinh viên là dùng sai liên từ: với **$$\forall$$** phải dùng **kéo theo ($$\to$$)** ($$\forall x\,(SV(x) \to HocToan(x))$$), còn với **$$\exists$$** phải dùng **hội ($$\land$$)** ($$\exists x\,(SV(x) \land Diem10(x))$$).

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Sử dụng** lượng từ toàn thể $$\forall$$ và tồn tại $$\exists$$ đúng ngữ cảnh.
- **Phân tích** lượng từ lồng nhau và ảnh hưởng của thứ tự lượng từ.
- **Dịch** các phát biểu toán học và yêu cầu phần mềm sang công thức có lượng từ.

**Từ khóa**: lượng từ (quantifier), lồng lượng từ, phạm vi (scope), phủ định lượng từ.
</div>

## Vị từ, miền xác định và lượng từ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **vị từ** $$P(x)$$ là phát biểu chứa biến, chưa có giá trị chân trị cho đến khi biến được gán giá trị cụ thể trong một **miền xác định**.
</div>


**Ký hiệu**:

- $$U$$: miền xác định (universe of discourse).
- $$P(x)$$: vị từ một biến.
- $$P(x,y)$$: vị từ hai biến.

<div class="textbook-example" markdown="1">
**Ví dụ**: Nếu $$U = \mathbb{Z}$$ và $$P(x)$$ là "$$x$$ chia hết cho 2", thì $$P(4)$$ đúng và $$P(5)$$ sai.
</div>


#### Minh họa: miền xác định và phạm vi chân trị

**Miền xác định** quy định tập giá trị mà biến có thể nhận, còn vị từ mô tả tính chất cần kiểm tra trên miền đó. Chẳng hạn trên miền $$\mathbb{R}$$, mệnh đề "Mọi $$x$$ đều có $$x^2 \geq 0$$" là đúng, nhưng "Mọi $$x$$ đều có nghịch đảo" lại sai vì miền chứa số 0. Tổng quát, miền càng rộng thì mệnh đề toàn thể càng khó đúng, còn miền càng hẹp thì càng dễ thỏa mãn.

![Miền xác định](/discrete-mathematics-for-computer-science-iuh/img/course/Universe_of_discourse_1.png)

<p class="textbook-figure-caption" data-figure="2.6">Miền xác định (universe of discourse) — tập hợp tất cả giá trị mà biến trong vị từ có thể nhận; phạm vi miền ảnh hưởng trực tiếp đến chân trị của mệnh đề lượng từ.</p>
**Ví dụ trong SQL**:

```sql
-- Miền: tất cả sinh viên
SELECT * FROM students WHERE gpa >= 0;        -- Luôn đúng

-- Miền: sinh viên có điểm
SELECT * FROM students WHERE gpa >= 3.5;      -- Có thể đúng/sai
```

## Lượng từ toàn thể

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$\forall x\,P(x)$$ đọc là "với mọi $$x$$, $$P(x)$$ đúng". Mệnh đề này đúng khi $$P(x)$$ đúng với tất cả các phần tử trong miền xác định.
</div>


**Ký hiệu**: $$\forall$$, gợi nhớ từ tiếng Anh "for all".

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$\forall x \in \mathbb{R},\ x^2 \ge 0$$ là đúng.
- $$\forall n \in \mathbb{N},\ n+1 > n$$ là đúng.
- $$\forall n \in \mathbb{Z},\ n^2 > n$$ là sai vì $$n = 0$$ là phản ví dụ.

**Chứng minh một mệnh đề toàn thể** thường thực hiện bằng cách xét một phần tử tùy ý. Chẳng hạn, để chứng minh $$\forall n \in \mathbb{Z},\ n(n+1)$$ chẵn, lấy $$n \in \mathbb{Z}$$ tùy ý: trong hai số nguyên liên tiếp $$n$$ và $$n + 1$$ luôn có một số chẵn, nên tích của chúng chia hết cho 2.

![Bảng đối lập với một vị từ](/discrete-mathematics-for-computer-science-iuh/img/course/Square_of_opposition__one_predicate.svg)

<p class="textbook-figure-caption" data-figure="2.7">Bảng đối lập (square of opposition) với một vị từ — minh họa quan hệ logic giữa các mệnh đề lượng từ toàn thể và phủ định.</p>
</div>

## Lượng từ tồn tại

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$\exists x\,P(x)$$ đọc là "tồn tại ít nhất một $$x$$ sao cho $$P(x)$$ đúng".
</div>


**Ký hiệu**: $$\exists$$, gợi nhớ từ tiếng Anh "exists".

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$\exists x \in \mathbb{Z},\ x^2 = 9$$ đúng vì có $$x = 3$$ (hoặc $$x = -3$$).
- $$\exists n \in \mathbb{N},\ n < 0$$ sai khi $$\mathbb{N}$$ là tập số tự nhiên không âm.
- $$\exists p \in \mathbb{P},\ p$$ chẵn đúng vì có số nguyên tố $$p = 2$$.

**Chứng minh tồn tại** có thể thực hiện bằng cách chỉ ra một nhân chứng (witness). Ví dụ, để chứng minh $$\exists x \in \mathbb{Z},\ x^2 = 16$$, chỉ cần nêu $$x = 4$$.

![Lượng từ tồn tại](/discrete-mathematics-for-computer-science-iuh/img/course/Existential_Quantification.png)

<p class="textbook-figure-caption" data-figure="2.8">Ký hiệu ∃ (existential quantification) — khẳng định tồn tại ít nhất một phần tử trong miền thỏa mãn vị từ.</p>
</div>

### Giải thích: Phủ định từng bước một phát biểu lượng từ lồng nhau 3 tầng

Hãy tự tay phủ định mệnh đề: *"Mọi sinh viên đều có ít nhất một môn học mà họ đạt điểm tối đa"* trên miền sinh viên $$S$$ và miền môn học $$C$$:
$$A \equiv \forall s \in S,\; \exists c \in C,\; \text{MaxScore}(s, c).$$

Ta đẩy dấu $$\neg$$ lần lượt từ ngoài vào trong từng tầng một:
1. **Đẩy $$\neg$$ qua $$\forall s \in S$$** (lật thành $$\exists s \in S$$):
   $$\neg A \equiv \exists s \in S,\; \neg\big(\exists c \in C,\; \text{MaxScore}(s, c)\big).$$
2. **Đẩy $$\neg$$ qua $$\exists c \in C$$** (lật thành $$\forall c \in C$$):
   $$\neg A \equiv \exists s \in S,\; \forall c \in C,\; \neg \text{MaxScore}(s, c).$$

**Dịch ngược sang tiếng Việt tự nhiên**: *"Tồn tại ít nhất một sinh viên mà ở mọi môn học họ đều không đạt điểm tối đa."*

**Kiểm chứng bằng ma trận $$2 \times 2$$** (`1` = đạt điểm tối đa, `0` = không đạt):
- Bảng 1: `An: [1, 0]`, `Bình: [0, 1]` → Mỗi hàng đều có ít nhất một số `1` ⇒ $$A = \mathbf{\text{True}}$$, $$\neg A = \mathbf{\text{False}}$$.
- Bảng 2: `An: [1, 1]`, `Bình: [0, 0]` → Hàng của Bình toàn số `0` (nhân chứng $$s = \text{Bình}$$ thỏa $$\forall c, \neg\text{MaxScore}$$) ⇒ $$A = \mathbf{\text{False}}$$, $$\neg A = \mathbf{\text{True}}$$.

## Lượng từ duy nhất

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$\exists!x\,P(x)$$ nghĩa là tồn tại **đúng một** $$x$$ sao cho $$P(x)$$ đúng.
</div>


Cách viết tương đương bằng $$\exists$$ và $$\forall$$:

<div class="textbook-equation" markdown="1">
$$\exists x\big(P(x) \land \forall y(P(y) \to y=x)\big).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Trong tập số nguyên, $$\exists!x\,(x+3=10)$$ đúng vì chỉ có duy nhất $$x = 7$$ thỏa mãn.
</div>


### Video ngắn: Lượng từ lồng nhau và Luật De Morgan

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/quantifiers-nested.mp4"></video>
</div>

Video dài khoảng 28 giây (có thuyết minh tiếng Việt): phân biệt thứ tự $\forall x\exists y$ với $\exists y\forall x$ và quy tắc đẩy dấu phủ định qua lượng từ.

## Lượng từ lồng nhau

Lượng từ lồng nhau là vị trí rất dễ phát sinh lỗi suy luận, vì việc đổi thứ tự lượng từ có thể làm thay đổi hoàn toàn ý nghĩa của mệnh đề.

<div class="textbook-example" markdown="1">
**Ví dụ**: Với miền là tập sinh viên và tập môn học, đặt $$T(x,y)$$ là "sinh viên $$x$$ thích môn $$y$$".

- $$\forall x\exists y\,T(x,y)$$: mỗi sinh viên thích ít nhất một môn nào đó.
- $$\exists y\forall x\,T(x,y)$$: có một môn mà tất cả sinh viên đều thích.

Mệnh đề thứ hai mạnh hơn mệnh đề thứ nhất.
</div>


### Vì sao thứ tự lượng từ quan trọng

Giả sử có ba sinh viên An, Bình, Chi và ba môn Toán, Lý, Tin:

- An thích Toán.
- Bình thích Lý.
- Chi thích Tin.

Khi đó $$\forall x\exists y\,T(x,y)$$ đúng vì sinh viên nào cũng có ít nhất một môn yêu thích, nhưng $$\exists y\forall x\,T(x,y)$$ sai vì không có môn nào được cả ba sinh viên cùng thích.

![Lượng từ lồng nhau](/discrete-mathematics-for-computer-science-iuh/img/course/Square_of_opposition__set_diagrams.svg)

<p class="textbook-figure-caption" data-figure="2.9">Sơ đồ tập hợp minh họa quan hệ giữa các mệnh đề lượng từ — hỗ trợ đọc đúng ý nghĩa khi nhiều lượng từ lồng nhau.</p>
## Phủ định lượng từ

**Định lý De Morgan cho lượng từ**:

<div class="textbook-equation" markdown="1">
$$\neg\forall x\,P(x) \equiv \exists x\,\neg P(x)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$\neg\exists x\,P(x) \equiv \forall x\,\neg P(x)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**:

Xét câu "Mọi sinh viên đều nộp bài":

<div class="textbook-equation" markdown="1">
$$\forall x\,N(x)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Phủ định đúng là "Tồn tại ít nhất một sinh viên không nộp bài":

<div class="textbook-equation" markdown="1">
$$\exists x\,\neg N(x)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Không được phủ định thành "mọi sinh viên đều không nộp bài".

![Biểu đồ Venn AND/OR](/discrete-mathematics-for-computer-science-iuh/img/course/venn_diagram_and_or.svg)

<p class="textbook-figure-caption" data-figure="2.10">Biểu đồ Venn cho phép AND và OR — trực quan hóa luật De Morgan khi phủ định lượng từ (∀ ↔ ∃).</p>
</div>

## Dịch câu tự nhiên sang logic

**Ví dụ 1**: "Mọi số nguyên chẵn đều chia hết cho 2."

<div class="textbook-equation" markdown="1">
$$\forall n \in \mathbb{Z}\,(Even(n) \to DivisibleBy2(n)).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ 2**: "Có một sinh viên học tất cả các môn bắt buộc."

<div class="textbook-equation" markdown="1">
$$\exists s\,\forall c\,(Required(c) \to Takes(s,c)).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ 3**: "Mỗi tài khoản có đúng một email chính."

<div class="textbook-equation" markdown="1">
$$\forall a\,\exists! e\,PrimaryEmail(a,e).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
## Ứng dụng trong Khoa học Máy tính

```python
scores = [8, 9, 7]
all_pass = all(score >= 5 for score in scores)   # forall
has_excellent = any(score >= 9 for score in scores)  # exists
```

Trong SQL:

```sql
SELECT * FROM Students s
WHERE EXISTS (
  SELECT 1 FROM Enrollments e
  WHERE e.student_id = s.id AND e.course = 'Discrete Math'
);
```

Lượng từ cũng xuất hiện thường xuyên trong đặc tả phần mềm: "mọi yêu cầu hợp lệ đều nhận được phản hồi", "tồn tại một đường đi từ nút nguồn đến nút đích", hay "mỗi khóa ánh xạ đến đúng một giá trị".

## Bài tập thực hành

### Bài tập 1: Phủ định lượng từ

Viết phủ định của các công thức sau:

1. $$\forall x\, (P(x) \to Q(x))$$
2. $$\exists x\, \forall y\, (R(x,y))$$

<details>
<summary>Đáp án</summary>

1. $\exists x\, (P(x) \land \lnot Q(x))$
2. $\forall x\, \exists y\, \lnot R(x,y)$

</details>

### Bài tập 2: Dịch sang logic vị từ

Dịch câu sau sang ngôn ngữ logic vị từ ($$x$$ là sinh viên, $$y$$ là môn học):

"Mọi sinh viên đều có ít nhất một môn học mà họ đạt điểm tối đa."

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$\forall x\,\big(Student(x) \to \exists y\,(Course(y) \land Takes(x,y) \land Score(x,y,10))\big)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
(Lưu ý: với lượng từ toàn thể $\forall x$, điều kiện lọc miền $Student(x)$ đi với phép kéo theo $\to$, không dùng phép hội $\land$.)
</details>

### Bài tập 3: Phân biệt thứ tự lượng từ

Giải thích tại sao hai công thức sau **không** tương đương trên $$\mathbb{R}$$:

- $$\forall x\, \exists y\, (y > x)$$
- $$\exists y\, \forall x\, (y > x)$$

<details>
<summary>Đáp án</summary>

Công thức thứ nhất đúng trên $\mathbb{R}$ vì với mọi $x$ ta luôn chọn được $y = x + 1 > x$. Công thức thứ hai sai vì không tồn tại số thực $y$ nào lớn hơn mọi số thực $x$.

</details>

### Bài tập 4: Ứng dụng Python/SQL

Viết đoạn mã Python và câu truy vấn SQL tương ứng với mệnh đề:

"Tồn tại một sinh viên có điểm trung bình > 9.0."

<details>
<summary>Đáp án</summary>

```python
any(student.gpa > 9.0 for student in students)
```

```sql
SELECT EXISTS (
  SELECT 1 FROM students WHERE gpa > 9.0
);
```

</details>

### Bài tập 5: Quantifiers with Floor and Ceiling

**A.10** For each of the following propositions, determine whether it's true or false, and justify your answer. (The floor function ⌊x⌋ rounds x down to an integer toward −∞, and the ceiling function ⌈x⌉ rounds x up to an integer toward +∞.)

(a) (∃x ∈ ℝ) (∀y ∈ ℝ) (x + y = x y)

(b) (∃x ∈ ℝ) (∀y ∈ ℝ) (x + y ≤ 2 x y)

(c) (∃x ∈ ℝ) (∀y ∈ ℝ) (⌈y⌉ = ⌊y + x⌋)

(d) (∀x ∈ ℤ) (∃y ∈ ℕ) (y² ≤ x² ⇒ x ≤ 0) Hint: Use P ⇒ Q ≡ ¬P ∨ Q.

<details>
<summary>Đáp án</summary>

(a) **Sai.** Giả sử tồn tại $x \in \mathbb{R}$ thỏa mãn. Với $y = 0$ ta có $x + 0 = 0 \iff x = 0$. Khi đó thay $y = 1$ ta được $0 + 1 = 0 \cdot 1 \iff 1 = 0$ (vô lý). Vậy không tồn tại $x$ thỏa mãn.

(b) **Sai.** Giả sử tồn tại $x \in \mathbb{R}$ thỏa mãn. Với $y = 0$, bất phương trình cho $x \leq 0$. Với $y = 1$, bất phương trình cho $x + 1 \leq 2x \iff x \geq 1$. Hai điều kiện $x \leq 0$ và $x \geq 1$ mâu thuẫn nhau.

(c) **Sai.** Giả sử tồn tại $x \in \mathbb{R}$ sao cho $\lceil y \rceil = \lfloor y + x \rfloor$ với mọi $y \in \mathbb{R}$.
    - Thay $y = 0$: $\lceil 0 \rceil = 0$, nên $\lfloor x \rfloor = 0 \implies 0 \leq x < 1$.
    - Với mọi $x \in [0, 1)$, chọn $y = \frac{1 - x}{2}$. Khi đó $0 < y < 1$ nên $\lceil y \rceil = 1$, nhưng $0 < y + x = \frac{1 + x}{2} < 1$ nên $\lfloor y + x \rfloor = 0 \neq 1$ (chẳng hạn nếu $x = 0.5$ và $y = 0.25$ thì $\lceil 0.25 \rceil = 1 \neq \lfloor 0.75 \rfloor = 0$).
    Vậy không tồn tại $x \in \mathbb{R}$ thỏa mãn.

(d) **Đúng.** Với $x \in \mathbb{Z}$, biến đổi $(y^2 \leq x^2 \Rightarrow x \leq 0) \equiv (y^2 > x^2) \lor (x \leq 0)$. Nếu $x \leq 0$, chọn $y = 0 \in \mathbb{N}$ thì vế phải đúng. Nếu $x > 0$, chọn $y = x + 1 \in \mathbb{N}$ thì $y^2 > x^2$ nên vế trái đúng. Do đó với mọi $x \in \mathbb{Z}$ luôn tồn tại $y \in \mathbb{N}$ thỏa mãn.

</details>

### Bài tập 6: Quantifier Equivalence Laws

**A.11** Determine which of the following hold. For each, if equivalent then informally explain why, and if inequivalent then exhibit particular predicates that form a counterexample. Assume the domains are always non-empty.

(a) ∃x (P(x) ∧ ∀y Q(y)) ≡ ∀y ∃x (P(x) ∧ Q(y))

(b) ∀x ∃y (P(x, y) ∨ Q(x, y)) ≡ (∀x ∃y P(x, y)) ∨ (∀x ∃y Q(x, y))

(c) (∃x ∀y P(x, y)) ⇒ (∀y ∃x P(x, y)) ≡ (∃x ∀y P(x, y)) ⇒ (∃x ∃y P(x, y))

<details>
<summary>Đáp án</summary>

(a) **Tương đương.** Nếu vế trái đúng, tồn tại $x_0$ thỏa $P(x_0)$ và mọi $y$ thỏa $Q(y)$; khi đó với mọi $y$, chọn $x = x_0$ ta có $P(x_0) \land Q(y)$, nên vế phải đúng. Ngược lại, nếu vế phải đúng: do miền không rỗng, lấy một $y_0$ bất kỳ sẽ có $x_{y_0}$ thỏa $P(x_{y_0})$, đồng thời với mọi $y$ đều có $Q(y)$ đúng, nên vế trái đúng.

(b) **Không tương đương.** Phản ví dụ trên miền $\{0, 1\}$: đặt $P(0,0) = T$ và $P(x,y) = F$ với các cặp còn lại; đặt $Q(1,1) = T$ và $Q(x,y) = F$ với các cặp còn lại.
    - Vế trái $\forall x \exists y\,(P(x,y) \lor Q(x,y))$: với $x = 0$ chọn $y = 0$ ($P(0,0) = T$), với $x = 1$ chọn $y = 1$ ($Q(1,1) = T$) → **đúng**.
    - Vế phải: $\forall x \exists y\,P(x,y)$ sai (tại $x = 1$ không có $y$ nào), và $\forall x \exists y\,Q(x,y)$ sai (tại $x = 0$ không có $y$ nào), nên tuyển hai vế **sai**.

(c) **Tương đương.** Cả hai vế đều là hằng đúng trên miền không rỗng: từ $\exists x \forall y\,P(x,y)$ luôn suy ra $\forall y \exists x\,P(x,y)$, và từ $\forall y \exists x\,P(x,y)$ (trên miền không rỗng) luôn suy ra $\exists x \exists y\,P(x,y)$. Vì hai vế đều luôn đúng nên chúng tương đương logic.

</details>

### Bài tập 7: Phủ định lượng từ trong đời thường

Phủ định các câu sau và diễn đạt lại bằng câu tiếng Việt tự nhiên (không dùng ký hiệu toán học):

(a) "Mọi sinh viên trong lớp đều nộp bài đúng hạn."
(b) "Có ít nhất một máy chủ còn hoạt động."
(c) "Mọi giao dịch đều được ghi log."
(d) "Tồn tại một lỗ hổng bảo mật chưa được vá."
(e) "Không ai không thích âm nhạc." (gợi ý: viết lại dưới dạng lượng từ trước)

<details>
<summary>Đáp án</summary>

(a) **Phủ định**: "Có ít nhất một sinh viên trong lớp không nộp bài đúng hạn."
    Ký hiệu: $\neg\forall x\, N(x) \equiv \exists x\, \neg N(x)$.

(b) **Phủ định**: "Mọi máy chủ đều ngừng hoạt động." (Không còn máy chủ nào hoạt động.)
    Ký hiệu: $\neg\exists x\, H(x) \equiv \forall x\, \neg H(x)$.

(c) **Phủ định**: "Có ít nhất một giao dịch không được ghi log."
    Ký hiệu: $\neg\forall x\, L(x) \equiv \exists x\, \neg L(x)$.

(d) **Phủ định**: "Mọi lỗ hổng bảo mật đều đã được vá."
    Ký hiệu: $\neg\exists x\, V(x) \equiv \forall x\, \neg V(x)$.

(e) Câu gốc "Không ai không thích âm nhạc" là $\neg\exists x\, \neg M(x) \equiv \forall x\, M(x)$ ("mọi người đều thích âm nhạc").
    **Phủ định**: "Có ít nhất một người không thích âm nhạc." ($\exists x\, \neg M(x)$).

</details>

### Bài tập 8: Dịch câu tiếng Việt có lượng từ lồng nhau

Dịch các câu sau sang logic vị từ và xác định miền xác định phù hợp:

(a) "Mọi sinh viên đều có một mã số duy nhất."
(b) "Có một cuốn sách mà mọi sinh viên đều đọc."
(c) "Mọi người đều có người mà họ yêu thương." (không nhất thiết là cùng một người)
(d) "Có một người mà mọi người đều kính trọng."
(e) "Không có sinh viên nào thích tất cả các môn học."

<details>
<summary>Đáp án</summary>

(a) $\forall s \in Student\; \exists! m \in ID\; HasID(s, m)$ — mỗi sinh viên $s$ có duy nhất một mã số $m$. Nếu không dùng $\exists!$, có thể viết:
    $\forall s\, \exists m\, \big(HasID(s,m) \land \forall n\, (HasID(s,n) \to n = m)\big)$.

(b) $\exists b \in Book\; \forall s \in Student\; Read(s, b)$ — lượng từ $\exists$ đứng trước $\forall$ biểu thị cùng một cuốn sách chung cho mọi sinh viên.

(c) $\forall p \in People\; \exists q \in People\; Love(p, q)$ — $q$ phụ thuộc vào $p$, nên mỗi người có thể yêu thương một người khác nhau.

(d) $\exists p \in People\; \forall q \in People\; Respect(q, p)$ — tồn tại cùng một người $p$ được mọi người kính trọng.

(e) $\neg\exists s \in Student\; \forall m \in Subject\; Like(s, m)$, tương đương với $\forall s \in Student\; \exists m \in Subject\; \neg Like(s, m)$ ("với mọi sinh viên $s$, tồn tại ít nhất một môn $m$ mà $s$ không thích").

</details>

### Bài tập 9: Xác định chân trị với lượng từ lồng nhau

Cho miền $$U = \mathbb{Z}$$ (tập số nguyên). Xác định các mệnh đề sau đúng hay sai:

(a) $$\forall x\; \exists y\; (x + y = 0)$$
(b) $$\exists y\; \forall x\; (x + y = 0)$$
(c) $$\forall x\; \forall y\; (x < y \to x^2 < y^2)$$
(d) $$\exists x\; \exists y\; (x^2 + y^2 = 0)$$
(e) $$\forall x\; \exists y\; (y = x^2)$$

<details>
<summary>Đáp án</summary>

(a) **Đúng.** Với mọi $x \in \mathbb{Z}$, chọn $y = -x \in \mathbb{Z}$ thì $x + (-x) = 0$ ($y$ phụ thuộc vào $x$).

(b) **Sai.** Không có số nguyên $y$ cố định nào cộng với mọi $x \in \mathbb{Z}$ đều bằng 0 (với bất kỳ $y$ nào, chỉ cần chọn $x \neq -y$ sẽ làm $x + y \neq 0$).

(c) **Sai.** Phản ví dụ: $x = -3, y = 2$ có $x < y$ nhưng $x^2 = 9 > 4 = y^2$. (Mệnh đề này đúng trên $\mathbb{N}$, nhưng sai trên $\mathbb{Z}$.)

(d) **Đúng.** Chọn $x = 0, y = 0$ ta có $0^2 + 0^2 = 0$.

(e) **Đúng.** Với mọi số nguyên $x \in \mathbb{Z}$, bình phương $x^2$ cũng là một số nguyên, nên luôn tồn tại $y = x^2 \in \mathbb{Z}$ thỏa mãn.

</details>

### Bài tập 10: Ứng dụng truy vấn cơ sở dữ liệu

Cho lược đồ cơ sở dữ liệu:
- `SinhVien(mãSV, tên, tuổi, lớp)`
- `HọcPhần(mãHP, tênHP, tínChỉ)`
- `ĐăngKý(mãSV, mãHP, điểm)`

Viết công thức logic vị từ và câu truy vấn SQL tương ứng cho các yêu cầu sau:

(a) "Tìm tất cả sinh viên đăng ký học phần 'Toán Rời Rạc'."
(b) "Sinh viên nào đã đăng ký mọi học phần?"
(c) "Học phần nào không có sinh viên nào đăng ký?"
(d) "Tìm các sinh viên đã đăng ký ít nhất một học phần 3 tín chỉ."

<details>
<summary>Đáp án</summary>

Đặt các vị từ:
- $SV(s, n, t, l)$: $s$ là sinh viên có tên $n$, tuổi $t$, lớp $l$.
- $HP(m, ten, tc)$: $m$ là mã học phần có tên $ten$, số tín chỉ $tc$.
- $DK(s, m, d)$: sinh viên $s$ đăng ký học phần $m$ với điểm $d$.

(a) $\exists m, tc, d\, (HP(m, \text{"Toán Rời Rạc"}, tc) \land DK(s, m, d))$
```sql
SELECT sv.* FROM SinhVien sv
JOIN DangKy dk ON sv.maSV = dk.maSV
JOIN HocPhan hp ON dk.maHP = hp.maHP
WHERE hp.tenHP = 'Toán Rời Rạc'
```

(b) $\forall m, ten, tc\, (HP(m, ten, tc) \to \exists d\, DK(s, m, d))$
```sql
SELECT maSV FROM SinhVien sv
WHERE NOT EXISTS (
    SELECT maHP FROM HocPhan
    WHERE maHP NOT IN (
        SELECT maHP FROM DangKy WHERE maSV = sv.maSV
    )
)
```
Đây là phép chia (division) trong đại số quan hệ.

(c) $\neg\exists s, d\; DK(s, m, d)$
```sql
SELECT * FROM HocPhan hp
WHERE NOT EXISTS (
    SELECT 1 FROM DangKy WHERE maHP = hp.maHP
)
```

(d) $\exists m, ten, d\, (HP(m, ten, 3) \land DK(s, m, d))$
```sql
SELECT DISTINCT sv.* FROM SinhVien sv
JOIN DangKy dk ON sv.maSV = dk.maSV
JOIN HocPhan hp ON dk.maHP = hp.maHP
WHERE hp.tinChi = 3
```

</details>

---


## Công cụ tương tác

Bật/tắt các ô trong lưới “sinh viên × môn học” để quan sát sự khác nhau giữa $$\forall x\exists y$$ và $$\exists y\forall x$$.
<div class="interactive-demo" markdown="1">
<div data-demo="nested-quantifier-grid"></div>
</div>
<script src="{{ '/public/js/nested-quantifier-grid.js' | relative_url }}"></script>

## Xem thêm / Video gợi ý

- [Quantifiers and Nested Quantifiers](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — Trefor Bazett (Clear examples with predicates)
- [Predicate Logic — ∀ and ∃](https://www.youtube.com/watch?v=8l7L9v0p0Q) — TrevTutor (Discrete Math playlist)


## Tóm tắt

- Lượng từ $$\forall$$ (toàn thể) và $$\exists$$ (tồn tại) kiểm soát phạm vi và độ mạnh của phát biểu; thay đổi lượng từ có thể làm đảo ngược ý nghĩa.
- **Thứ tự lượng từ lồng nhau** quyết định ngữ nghĩa: $$\forall x \exists y$$ khác với $$\exists y \forall x$$.
- **Phủ định lượng từ** tuân theo luật De Morgan: $$\neg\forall x\,P(x) \equiv \exists x\,\neg P(x)$$ và $$\neg\exists x\,P(x) \equiv \forall x\,\neg P(x)$$.
- Lượng từ duy nhất $$\exists!$$ diễn đạt "tồn tại đúng một" phần tử thỏa mãn vị từ.
- Trong SQL và Python, `EXISTS`/`NOT EXISTS` và `all()`/`any()` là hiện thực trực tiếp của $$\exists$$ và $$\forall$$.

Trong bài tiếp theo, chúng ta sẽ học **quy tắc suy luận** với lượng từ để rút ra kết luận hợp lệ từ các tiền đề đã biết.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=jLVKV5LJjaw">Negating Logical Statements with Multiple Quantifiers</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày lượng từ lồng nhau và cách giữ đúng thứ tự khi phủ định.
- <a href="https://www.youtube.com/watch?v=q1rKFGSiZE8">Negating Universal and Existential Quantifiers</a> — Dr. Trefor Bazett, tiếng Anh. Hướng dẫn phủ định $$\forall$$ và $$\exists$$ từng bước.
- <a href="https://www.youtube.com/watch?v=7HvCgm4vBv4">[Discrete Mathematics] Negating Quantifiers and Translation Examples</a> — TrevTutor, tiếng Anh. Minh họa cách dịch câu có lượng từ và viết phủ định.
