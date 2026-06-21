---
layout: post
title: "Quy tắc Suy luận trong Logic Vị từ"
categories: chapter02
date: 2021-01-01
order: 3
required: true
lang: en
---

Trong hai bài trước, chúng ta đã học cách biểu diễn các phát biểu phức tạp bằng vị từ và lượng từ. Nhưng biểu diễn được mới chỉ là nửa chặng đường. Câu hỏi quan trọng hơn là: **từ những gì đã biết, ta có thể suy ra kết luận gì — và bằng cách nào cho đúng?**

Đây không phải bài toán trừu tượng. Mỗi khi một hệ thống kiểm chứng phần mềm xác nhận rằng "chương trình thỏa mãn đặc tả", nó đang thực hiện một chuỗi suy luận logic hình thức. Mỗi khi một lập trình viên đọc tài liệu đặc tả và kết luận rằng hàm X phải trả về kết quả Y trong trường hợp Z, người đó cũng đang suy luận — dù thường là không hình thức.

Vấn đề là: suy luận không hình thức rất dễ sai. Con người có xu hướng "nhảy cóc" từ trực giác sang kết luận, bỏ qua các bước trung gian mà chính ở đó lỗi logic ẩn náu. Ví dụ:

- *"Mọi lập trình viên đều biết Python"* và *"An là lập trình viên"* — ta có thể kết luận *"An biết Python"*. Đây là suy luận hợp lệ.
- Nhưng từ *"Mọi lập trình viên đều biết Python"* và *"An biết Python"*, ta **không thể** kết luận *"An là lập trình viên"*. Đây là ngụy biện khẳng định hệ quả.

Trong logic vị từ, các **quy tắc suy luận** với lượng từ chính là bộ công cụ giúp ta tránh những sai lầm như vậy. Chúng cho ta biết:

- khi nào được thay "mọi x" bằng một phần tử cụ thể,
- khi nào được kết luận "tồn tại" từ một ví dụ,
- và vì sao một chứng minh hình thức có thể được máy tính kiểm tra từng bước.

Hiểu các quy tắc này là hiểu cách tri thức được biến thành kết luận — trong toán học, trong kiểm chứng phần mềm, trong trí tuệ nhân tạo, và trong chính cách ta lập luận hàng ngày.

## 1. Ôn tập suy luận mệnh đề

Các quy tắc suy luận mệnh đề vẫn được dùng sau khi ta đã loại bỏ hoặc đưa vào lượng từ đúng cách.

| Quy tắc | Dạng |
|---|---|
| Modus Ponens | $$p\to q,\ p\ \vdash q$$ |
| Modus Tollens | $$p\to q,\ \neg q\ \vdash \neg p$$ |
| Tam đoạn luận giả thuyết | $$p\to q,\ q\to r\ \vdash p\to r$$ |
| Tam đoạn luận tuyển | $$p\lor q,\ \neg p\ \vdash q$$ |

**Ký hiệu**: $$\vdash$$ đọc là "suy ra được trong hệ chứng minh".

![Modus Ponens](/discrete-mathematics-for-computer-science-iuh/img/course/Modus_ponens.png)

*Hình 2.11: Modus Ponens — từ $$p \to q$$ và $$p$$ suy ra $$q$$; quy tắc suy luận mệnh đề nền tảng, thường kết hợp với UI trong logic vị từ.*

## 2. Universal Instantiation (UI) - Cụ thể hóa toàn thể - Qui tắc đặc biệt hóa phổ dụng

**Định nghĩa**: Từ một mệnh đề đúng với mọi phần tử, ta được phép suy ra nó đúng với một phần tử cụ thể bất kỳ.

$$\frac{\forall x\,P(x)}{P(c)}$$

trong đó $$c$$ là một phần tử của miền xác định.

**Ví dụ**: Nếu $$\forall x(Student(x)\to NeedsLogic(x))$$ và $$Student(An)$$, thì bằng UI ta có:

$$Student(An)\to NeedsLogic(An).$$

Kết hợp Modus Ponens, suy ra $$NeedsLogic(An)$$.

<div class="content-box insight-box" markdown="1">
**Lưu ý**: UI là quy tắc **hợp lệ** (valid) — nếu tiền đề đúng thì kết luận chắc chắn đúng. Đây là nền tảng để áp dụng tính chất chung cho đối tượng cụ thể trong chứng minh và kiểm chứng phần mềm.
</div>

### Bài tập thực hành: Universal Instantiation

**Bài tập 1**: Cho $$\forall x\,(Even(x) \to DivisibleBy2(x))$$ và $$Even(4)$$. Áp dụng UI và Modus Ponens để suy ra kết luận.

**Bài tập 2**: Cho $$\forall x\,(Prime(x) \to HasNoDivisor(x))$$. Viết biểu thức sau khi áp dụng UI cho $$x = 7$$.

**Bài tập 3**: Giải thích tại sao từ $$\forall x\,P(x)$$ ta không thể suy ra $$\exists x\,P(x)$$ (UI không cho phép kết luận này).

**Đáp án**:

1. $$Even(4) \to DivisibleBy2(4)$$ (UI), sau đó $$DivisibleBy2(4)$$ (MP).
2. $$Prime(7) \to HasNoDivisor(7)$$.
3. UI chỉ đi từ "mọi" đến "một"; không bảo đảm tồn tại phần tử nào đó (có thể miền rỗng).

![Modus Tollens](/discrete-mathematics-for-computer-science-iuh/img/course/Modus_tollens.png)

*Hình 2.12: Modus Tollens — từ $$p \to q$$ và $$\neg q$$ suy ra $$\neg p$$; bổ sung cho Modus Ponens trong chuỗi suy luận.*

## 3. Universal Generalization (UG) - Tổng quát hóa toàn thể

**Định nghĩa**: Nếu ta chứng minh được $$P(c)$$ cho một phần tử $$c$$ được chọn tùy ý, không dùng giả thiết đặc biệt nào về $$c$$, thì có thể kết luận $$\forall xP(x)$$.

{% raw %}$$\frac{P(c)\ \text{với } c \text{ tùy ý}}{\forall x\,P(x)}$${% endraw %}

### Khối chứng minh mẫu

Chứng minh: $$\forall n\in\mathbb{Z},\ n(n+1)$$ chẵn.

Lấy $$n\in\mathbb{Z}$$ tùy ý. Hai số $$n$$ và $$n+1$$ là hai số nguyên liên tiếp, nên một trong hai số chẵn. Do đó tích $$n(n+1)$$ chia hết cho 2. Vì $$n$$ được chọn tùy ý, theo UG, kết luận đúng với mọi số nguyên $$n$$.

<div class="content-box warning-box" markdown="1">
**Cảnh báo**: Không được dùng UG nếu phần tử đang xét không tùy ý. Nếu biết "An là sinh viên giỏi" thì không thể suy ra "mọi sinh viên đều giỏi".
</div>

## 4. Existential Instantiation (EI) - Cụ thể hóa tồn tại

**Định nghĩa**: Từ $$\exists xP(x)$$, ta được phép đặt một hằng mới $$c$$ sao cho $$P(c)$$ đúng.

$$\frac{\exists x\,P(x)}{P(c)}$$

Điều kiện quan trọng: $$c$$ phải là tên mới, chưa mang thông tin đặc biệt nào khác.

**Ví dụ**: Từ "tồn tại một sinh viên đạt điểm 10", ta có thể gọi sinh viên đó là $$s_0$$ và viết $$Score10(s_0)$$. Nhưng không được tự ý cho rằng $$s_0$$ là An nếu chưa có dữ kiện.

## 5. Existential Generalization (EG) - Tổng quát hóa tồn tại

**Định nghĩa**: Nếu biết $$P(c)$$ đúng với một phần tử cụ thể $$c$$, ta có thể kết luận $$\exists xP(x)$$.

$$\frac{P(c)}{\exists x\,P(x)}$$

**Ví dụ**: Biết $$Prime(2)$$, suy ra $$\exists xPrime(x)$$.

![Cây thuật ngữ logic](/discrete-mathematics-for-computer-science-iuh/img/course/Termstammbaum.png)

*Hình 2.13: Cây phân tích thuật ngữ (term tree) — minh họa cấu trúc công thức khi áp dụng quy tắc suy luận từng bước.*

## 6. Ví dụ tổng hợp

**Bài toán**: Chứng minh lập luận sau hợp lệ.

**Tiền đề**:
1. $$∀x(Programmer(x) → KnowsLogic(x))$$
2. $$Programmer(Linh)$$

**Kết luận cần chứng minh**: $$KnowsLogic(Linh)$$

**Chứng minh** (các bước suy luận):

| Bước | Mệnh đề | Lý do |
|:---:|:---|:---|
| 1 | $$∀x(Programmer(x) → KnowsLogic(x))$$ | Tiền đề (1) |
| 2 | $$Programmer(Linh) → KnowsLogic(Linh)$$ | Từ (1) bằng **Universal Instantiation (UI)** |
| 3 | $$Programmer(Linh)$$ | Tiền đề (2) |
| 4 | $$KnowsLogic(Linh)$$ | Từ (2) và (3) bằng **Modus Ponens** |

**Kết luận**: $$KnowsLogic(Linh)$$ — đã được chứng minh.

<div class="content-box example-box" markdown="1">
**Cách đọc bảng chứng minh**:
- Cột **Bước**: số thứ tự suy luận (không trùng với số tiền đề).
- Cột **Mệnh đề**: biểu thức logic thu được ở bước đó.
- Cột **Lý do**: giải thích tại sao mệnh đề đó đúng (tiền đề, UI, MP, ...).
</div>

![Socrates](/discrete-mathematics-for-computer-science-iuh/img/course/Socrates_Louvre.jpg)

*Hình 2.14: Socrates — ví dụ kinh điển trong tam đoạn luận: "Người Hy Lạp là người; người thì phải chết; Socrates là người Hy Lạp" → Socrates phải chết.*

## 7. Suy luận với lượng từ tồn tại

Lập luận:

1. $$\exists x(Student(x)\land LikesMath(x))$$
2. $$\forall x(LikesMath(x)\to CanLearnDiscreteMath(x))$$
3. Kết luận: $$\exists x(Student(x)\land CanLearnDiscreteMath(x))$$

**Chứng minh**:

1. Từ (1), dùng EI đặt một hằng mới $$a$$ sao cho $$Student(a)\land LikesMath(a)$$.
2. Suy ra $$Student(a)$$ và $$LikesMath(a)$$ bằng tách hội.
3. Từ (2), dùng UI: $$LikesMath(a)\to CanLearnDiscreteMath(a)$$.
4. Từ $$LikesMath(a)$$ và bước 3, dùng Modus Ponens: $$CanLearnDiscreteMath(a)$$.
5. Từ $$Student(a)$$ và $$CanLearnDiscreteMath(a)$$, lập hội: $$Student(a)\land CanLearnDiscreteMath(a)$$.
6. Dùng EG: $$\exists x(Student(x)\land CanLearnDiscreteMath(x))$$.

![Cây quyết định](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

*Hình 2.15: Cây quyết định — mô hình suy luận có cấu trúc phân nhánh, tương tự chuỗi suy luận UI/EI/MP trong logic vị từ.*

## Bài tập thực hành

### Bài tập 1: Nhận diện quy tắc

Xác định quy tắc suy luận nào được dùng trong mỗi bước sau:

1. $$\forall x (P(x) \to Q(x))$$, $$P(a)$$ → $$Q(a)$$
2. $$P(c)$$ → $$\exists x P(x)$$

<details>
<summary>Đáp án</summary>

1. Universal Instantiation (UI)
2. Existential Generalization (EG)

</details>

### Bài tập 2: Hoàn thiện chứng minh

Cho: $$\forall x (Student(x) \to HasID(x))$$ và $$\exists x Student(x)$$.  
Chứng minh: $$\exists x HasID(x)$$.

<details>
<summary>Đáp án</summary>

1. $$\exists x Student(x)$$ (tiền đề)
2. $$Student(c)$$ (EI)
3. $$Student(c) \to HasID(c)$$ (UI)
4. $$HasID(c)$$ (Modus Ponens)
5. $$\exists x HasID(x)$$ (EG)

</details>

### Bài tập 3: Tìm lỗi

Tìm và sửa lỗi trong lập luận sau:

> Mọi sinh viên đều học Discrete Math.  
> Lan là sinh viên.  
> Vậy Lan học Discrete Math.  
> Do đó mọi sinh viên đều học Discrete Math.

<details>
<summary>Đáp án</summary>

Lỗi ở bước cuối: từ một trường hợp cụ thể (Lan) không được suy ra "mọi" (UG chỉ áp dụng khi đối tượng là tùy ý, không phải tên riêng).

</details>

### Bài tập 4: Universal Instantiation và Modus Ponens

Cho các giả thiết:

1. $$\forall x (Human(x) \to Mortal(x))$$
2. $$Human(Socrates)$$

Suy ra $$Mortal(Socrates)$$ bằng UI và Modus Ponens.

Hãy áp dụng quy trình tương tự cho:

(a) $$\forall x (Student(x) \to TakesExam(x))$$ và $$Student(Lan)$$
(b) $$\forall x (Bird(x) \to CanFly(x))$$ và $$Bird(Eagle)$$
(c) $$\forall n (Even(n) \to DivisibleBy2(n))$$ và $$Even(42)$$

<details>
<summary>Đáp án</summary>

(a) - UI từ (1): $$Student(Lan) \to TakesExam(Lan)$$
    - Modus Ponens với $$Student(Lan)$$: $$TakesExam(Lan)$$
    Kết luận: "Lan thi".

(b) - UI từ (1): $$Bird(Eagle) \to CanFly(Eagle)$$
    - Modus Ponens với $$Bird(Eagle)$$: $$CanFly(Eagle)$$
    Kết luận: "Đại bàng bay được".

(c) - UI từ (1): $$Even(42) \to DivisibleBy2(42)$$
    - Modus Ponens với $$Even(42)$$: $$DivisibleBy2(42)$$
    Kết luận: "42 chia hết cho 2" — đúng.

</details>

### Bài tập 5: Existential Instantiation và Existential Generalization

Cho $$\exists x (Student(x) \land \neg Passed(x))$$.

(a) Áp dụng EI để giới thiệu một hằng số mới c. Điều kiện khi dùng EI là gì?
(b) Từ kết quả của EI, áp dụng EG để suy ra $$\exists x (Student(x))$$.
(c) Giải thích tại sao từ $$\exists x P(x)$$ không thể suy ra $$\forall x P(x)$$ bằng EG.

<details>
<summary>Đáp án</summary>

(a) EI cho ta: $$Student(c) \land \neg Passed(c)$$, với c là hằng số mới, chưa từng xuất hiện trong bất kỳ giả thiết hay kết luận nào trước đó.
    
    Điều kiện: **c phải là một tên mới, không xuất hiện ở bất kỳ đâu trong chuỗi suy luận**. Lý do: nếu c đã xuất hiện, ta không thể đảm bảo nó là "nhân chứng tùy ý" cho mệnh đề tồn tại.

(b) Từ $$Student(c)$$ (bằng phép giản lược conjunction), EG cho ta: $$\exists x Student(x)$$.
    
    Chú ý: EG cho phép ta chuyển từ một trường hợp cụ thể sang "tồn tại" — đây là quy tắc rất trực quan: nếu Lan là sinh viên thì tồn tại sinh viên.

(c) EG chỉ cho phép suy ra **tồn tại** (∃), không phải **mọi** (∀). Từ $$P(c)$$ (với c cụ thể), EG cho $$\exists x P(x)$$. Để có $$\forall x P(x)$$, ta cần UG với c là phần tử tùy ý (arbitrary), không phải hằng số từ EI.

    Từ $$\exists x P(x)$$, EI giới thiệu P(c) với c là **nhân chứng cụ thể** (có thể có tính chất đặc biệt). Không thể suy ra mọi x đều có P(x) từ một nhân chứng.

</details>

### Bài tập 6: Áp dụng UG đúng cách

Xét suy luận sau:

Cho $$\forall x (P(x) \to Q(x))$$ và $$\forall x P(x)$$.

(a) Chứng minh $$\forall x Q(x)$$ bằng UI và UG.
(b) Nếu thay giả thiết thành $$\forall x (P(x) \to Q(x))$$ và $$P(a)$$ (với a là hằng số), có thể suy ra $$\forall x Q(x)$$ không? Giải thích.

<details>
<summary>Đáp án</summary>

(a) Chứng minh:
    - Gọi c là phần tử tùy ý bất kỳ trong miền.
    - UI từ $$\forall x P(x)$$: $$P(c)$$
    - UI từ $$\forall x (P(x) \to Q(x))$$: $$P(c) \to Q(c)$$
    - Modus Ponens: $$Q(c)$$
    - Vì c là phần tử tùy ý, UG cho: $$\forall x Q(x)$$
    
    Đây là một dạng của **sylogism** (tam đoạn luận) trong logic vị từ: nếu mọi x đều có P và mọi x đều có (P kéo theo Q), thì mọi x đều có Q.

(b) **Không thể.** Từ P(a) → Q(a) (UI) và P(a), ta chỉ suy ra Q(a). Không thể dùng UG ở đây vì a là hằng số cụ thể, không phải phần tử tùy ý. UG chỉ áp dụng khi biến được lượng từ hóa phổ dụng từ đầu hoặc là phần tử tùy ý chưa có ràng buộc.

    Phản ví dụ: P(x) = "x là số chẵn", Q(x) = "x chia hết cho 4". Nếu biết ∀x (P(x) → Q(x)) (sai!) và P(4) (đúng), không thể suy ra mọi số chẵn đều chia hết cho 4 (sai, vì 2 là số chẵn nhưng không chia hết cho 4).

</details>

### Bài tập 7: Chứng minh bằng suy luận vị từ — Bài toán "Người Hy Lạp"

Chứng minh kết luận từ các giả thiết:

1. $$\forall x (Greek(x) \to Human(x))$$ — Người Hy Lạp là người.
2. $$\forall x (Human(x) \to Mortal(x))$$ — Người thì phải chết.
3. $$Greek(Socrates)$$ — Socrates là người Hy Lạp.

Kết luận: $$\exists x Mortal(x)$$ — Tồn tại người phải chết.

Viết từng bước suy luận.

<details>
<summary>Đáp án</summary>

- Bước 1 (UI từ 1): $$Greek(Socrates) \to Human(Socrates)$$
- Bước 2 (UI từ 2): $$Human(Socrates) \to Mortal(Socrates)$$
- Bước 3 (Hypothetical Syllogism từ B1, B2): $$Greek(Socrates) \to Mortal(Socrates)$$
- Bước 4 (Modus Ponens từ B3 và giả thiết 3): $$Mortal(Socrates)$$
- Bước 5 (EG từ B4): $$\exists x Mortal(x)$$

Kết luận: Tồn tại người phải chết (cụ thể là Socrates).

Nhận xét: Đây là phiên bản logic vị từ của tam đoạn luận kinh điển từ thời Aristotle — một trong những suy luận lâu đời nhất trong lịch sử triết học phương Tây.

</details>

### Bài tập 8: Phát hiện lỗi suy luận với lượng từ

Tìm lỗi trong các suy luận sau:

(a) 
```
∀x ∃y P(x, y)
EI → P(c, d)  (với c, d là hằng số mới)
```

(b)
```
P(a) ∧ Q(a)
EG → ∀x (P(x) ∧ Q(x))
```

(c)
```
∃x P(x) ∧ ∃x Q(x)
→ ∃x (P(x) ∧ Q(x))
```

<details>
<summary>Đáp án</summary>

(a) **Lỗi:** EI chỉ áp dụng cho mệnh đề $$\exists x R(x)$$, không áp dụng trực tiếp cho $$\forall x \exists y P(x, y)$$.
    
    Cách đúng: Với c tùy ý, UI từ $$\forall x \exists y P(x, y)$$ cho $$\exists y P(c, y)$$. Sau đó EI cho $$P(c, d)$$ với d là hằng số mới (phụ thuộc vào c).
    
    Lỗi ở đây là áp dụng EI lên một công thức có lượng từ phổ dụng bên ngoài — EI chỉ áp dụng cho lượng từ tồn tại ở cấp cao nhất.

(b) **Lỗi:** EG suy ra $$\exists$$, không phải $$\forall$$.
    
    Từ $$P(a) \land Q(a)$$, EG đúng cho: $$\exists x (P(x) \land Q(x))$$.
    Muốn có $$\forall x (P(x) \land Q(x))$$, cần UG với a là phần tử tùy ý, không phải hằng số cụ thể.

(c) **Lỗi:** Hai hằng số từ hai lần EI có thể khác nhau.
    
    Từ $$\exists x P(x)$$, EI cho P(c).
    Từ $$\exists x Q(x)$$, EI cho Q(d) với d ≠ c (cả hai đều là hằng số mới).
    Ta có P(c) ∧ Q(d), nhưng không thể suy ra ∃x (P(x) ∧ Q(x)) vì c và d có thể khác nhau.
    
    Phản ví dụ: P(x) = "x là số chẵn", Q(x) = "x là số lẻ". ∃x P(x) đúng (x=2), ∃x Q(x) đúng (x=3), nhưng ∃x (P(x) ∧ Q(x)) sai vì không số nào vừa chẵn vừa lẻ.

</details>
