---

layout: post
title: "Quy tắc Suy luận trong Logic Vị từ"
categories: chapter02
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Trình bày bốn quy tắc suy luận cốt lõi với lượng từ trong logic vị từ (UI, UG, EI, EG), cách kết hợp với suy luận mệnh đề và các lỗi thường gặp."
---

Ở Chương 1, ta đã dùng Modus Ponens để suy diễn giữa các mệnh đề. Nhưng khi bước sang Logic Vị từ, các tiền đề đều bị "bọc" bên trong lớp vỏ lượng từ $$\forall x$$ và $$\exists x$$. Làm sao tháo bỏ lớp vỏ lượng từ để áp dụng suy diễn mệnh đề, rồi đóng gói lại kết luận mà **không vô tình chứng minh những điều sai sự thật**?

Bốn quy tắc suy diễn vị từ (**UI, UG, EI, EG**) chính là bộ luật kiểm soát việc "mở hộp" và "đóng hộp" biến lượng từ một cách tuyệt đối an toàn.

## Bản đồ kiến thức nền: Bốn quy tắc chuyển đổi giữa Lượng từ và Cá thể

1. **Cụ thể hóa Toàn thể (UI — Universal Instantiation)**:
   Từ $$\forall x\, P(x)$$, ta được phép suy ra $$P(c)$$ cho **bất kỳ** phần tử $$c$$ nào trong miền xác định (vì tính chất đúng cho tất cả nên tất nhiên đúng cho $$c$$).

2. **Tổng quát hóa Toàn thể (UG — Universal Generalization)**:
   Nếu ta chứng minh được $$P(c)$$ đúng cho một phần tử $$c$$ **hoàn toàn tùy ý** (không giả sử thêm đặc tính riêng nào của $$c$$), ta được phép kết luận $$\forall x\, P(x)$$.

3. **Cụ thể hóa Tồn tại (EI — Existential Instantiation)**:
   Từ $$\exists x\, P(x)$$, ta biết có ít nhất một nhân chứng nên được phép đặt tên nó là $$c$$ thỏa $$P(c)$$—**với điều kiện nghiêm ngặt $$c$$ phải là tên mới tinh (fresh constant)** chưa từng xuất hiện trước đó!

4. **Tổng quát hóa Tồn tại (EG — Existential Generalization)**:
   Nếu có một phần tử cụ thể $$c$$ thỏa $$P(c)$$, ta lập tức suy ra $$\exists x\, P(x)$$.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** bốn quy tắc suy diễn cho logic vị từ: UI, UG, EI và EG.
- **Chứng minh** mệnh đề có lượng từ bằng các bước suy diễn hình thức.
- **Liên hệ** suy diễn vị từ với chứng minh tính đúng đắn và đặc tả chương trình.

**Từ khóa**: universal instantiation, universal generalization, existential instantiation, existential generalization, rules of inference, predicate logic proofs.
</div>

## Ôn tập suy luận mệnh đề

Các quy tắc suy luận mệnh đề vẫn được sử dụng bình thường sau khi ta đã loại bỏ hoặc đưa vào lượng từ đúng cách.

| Quy tắc | Dạng |
|---|---|
| Modus Ponens | $$p\to q,\ p\ \vdash q$$ |
| Modus Tollens | $$p\to q,\ \neg q\ \vdash \neg p$$ |
| Tam đoạn luận giả thuyết | $$p\to q,\ q\to r\ \vdash p\to r$$ |
| Tam đoạn luận tuyển | $$p\lor q,\ \neg p\ \vdash q$$ |

**Ký hiệu**: $$\vdash$$ đọc là "suy ra được trong hệ chứng minh".

![Modus Ponens](/discrete-mathematics-for-computer-science-iuh/img/course/Modus_ponens.png)

<p class="textbook-figure-caption" data-figure="2.11">Modus Ponens — từ $$p \to q$$ và $$p$$ suy ra $$q$$; quy tắc suy luận mệnh đề nền tảng, thường kết hợp với UI trong logic vị từ.</p>
## Universal Instantiation (UI) — Cụ thể hóa toàn thể

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Từ một mệnh đề đúng với mọi phần tử trong miền, ta được phép suy ra nó đúng với một phần tử cụ thể $$c$$ bất kỳ trong miền đó.
</div>


<div class="textbook-equation" markdown="1">
$$\frac{\forall x\,P(x)}{P(c)}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó $$c$$ là một phần tử thuộc miền xác định.

<div class="textbook-example" markdown="1">
**Ví dụ**: Nếu $$\forall x\,(Student(x)\to NeedsLogic(x))$$ và $$Student(An)$$, thì áp dụng UI cho $$c = An$$ ta có:

<div class="textbook-equation" markdown="1">
$$Student(An)\to NeedsLogic(An).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Kết hợp với Modus Ponens, ta suy ra $$NeedsLogic(An)$$.
</div>


<div class="content-box insight-box textbook-block" markdown="1">
UI là quy tắc **hợp lệ** (valid): nếu tiền đề đúng thì kết luận chắc chắn đúng. Đây là bước nền tảng để áp dụng tính chất tổng quát cho từng đối tượng cụ thể trong chứng minh và kiểm chứng phần mềm.
</div>

### Bài tập thực hành: Universal Instantiation

**Bài tập 1**: Cho $$\forall x\,(Even(x) \to DivisibleBy2(x))$$ và $$Even(4)$$. Áp dụng UI và Modus Ponens để suy ra kết luận.

**Bài tập 2**: Cho $$\forall x\,(Prime(x) \to HasNoDivisor(x))$$. Viết biểu thức thu được sau khi áp dụng UI cho $$x = 7$$.

**Bài tập 3**: Giải thích tại sao từ $$\forall x\,P(x)$$ ta không thể tự động suy ra $$\exists x\,P(x)$$ nếu miền xác định có thể rỗng.

**Đáp án**:

1. $$Even(4) \to DivisibleBy2(4)$$ (UI), sau đó $$DivisibleBy2(4)$$ (Modus Ponens).
2. $$Prime(7) \to HasNoDivisor(7)$$.
3. UI chỉ suy ra $$P(c)$$ khi đã có một phần tử $$c$$ thuộc miền xác định; nếu miền rỗng thì không tồn tại phần tử nào để khẳng định $$\exists x\,P(x)$$.

![Modus Tollens](/discrete-mathematics-for-computer-science-iuh/img/course/Modus_tollens.png)

<p class="textbook-figure-caption" data-figure="2.12">Modus Tollens — từ $$p \to q$$ và $$\neg q$$ suy ra $$\neg p$$; bổ sung cho Modus Ponens trong chuỗi suy luận.</p>
## Universal Generalization (UG) — Tổng quát hóa toàn thể

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Nếu ta chứng minh được $$P(c)$$ cho một phần tử $$c$$ được chọn tùy ý trong miền mà không dùng bất kỳ giả thiết đặc biệt nào về $$c$$, thì có thể kết luận $$\forall x\,P(x)$$.
</div>


{% raw %}$$\frac{P(c)\ \text{với } c \text{ tùy ý}}{\forall x\,P(x)}$${% endraw %}

### Khối chứng minh mẫu

Chứng minh: $$\forall n\in\mathbb{Z},\ n(n+1)$$ chẵn.

Lấy $$n\in\mathbb{Z}$$ tùy ý. Vì $$n$$ và $$n+1$$ là hai số nguyên liên tiếp nên một trong hai số là số chẵn, do đó tích $$n(n+1)$$ chia hết cho 2. Vì $$n$$ được chọn tùy ý, theo UG ta kết luận mệnh đề đúng với mọi số nguyên $$n$$.

<div class="content-box warning-box textbook-block" markdown="1">
**Cảnh báo**: Không được dùng UG nếu phần tử đang xét không phải là phần tử tùy ý. Biết "An là sinh viên giỏi" không cho phép suy ra "mọi sinh viên đều giỏi".
</div>

### Khung giải thích (nên đọc chậm): Bắt quả tang lỗi "dùng lại tên biến trong EI" và sửa thành chứng minh chuẩn

Tại sao quy tắc **EI** bắt buộc phải chọn tên hằng mới tinh $$c$$? Hãy xem một "chứng minh" giả mạo cực kỳ tinh vi trên miền số nguyên $$\mathbb{Z}$$:
- Tiền đề 1: $$\exists x\, \text{Chẵn}(x)$$ (Đúng, ví dụ 2).
- Tiền đề 2: $$\exists x\, \text{Lẻ}(x)$$ (Đúng, ví dụ 3).
- Bước 3 (EI từ P1): Chọn $$c$$ sao cho $$\text{Chẵn}(c)$$.
- Bước 4 (**SAI!** EI từ P2 nhưng dùng lại cùng tên $$c$$): Chọn $$c$$ sao cho $$\text{Lẻ}(c)$$.
- Bước 5 (Hội + EG): Suy ra $$\exists x\, (\text{Chẵn}(x) \land \text{Lẻ}(x))$$ — *"Tồn tại số vừa chẵn vừa lẻ!"* (**Vô lý!**)

**Nguyên nhân lỗi**: Bước 4 vi phạm điều kiện *fresh constant* của EI—nhân chứng của số lẻ phải đặt tên khác là $$d$$, cho ra $$\text{Chẵn}(c) \land \text{Lẻ}(d)$$, hoàn toàn không suy ra được số vừa chẵn vừa lẻ!

#### Chuỗi suy diễn chuẩn (áp dụng đúng thứ tự EI trước UI)
Cho tiền đề: (1) $$\forall x\,(C(x) \to P(x))$$ (*Mọi sinh viên CNTT đều học lập trình*) và (2) $$\exists x\,(C(x) \land R(x))$$ (*Có sinh viên CNTT học Rust*). Chứng minh $$\exists x\,(P(x) \land R(x))$$:

| Bước | Biểu thức | Quy tắc |
| :---: | :--- | :--- |
| 1 | $$\exists x\,(C(x) \land R(x))$$ | Tiền đề 2 |
| 2 | $$C(a) \land R(a)$$ | **EI** (chọn hằng mới tinh $$a$$ **trước**!) |
| 3 | $$C(a)$$ và $$R(a)$$ | Rút gọn hội (Simplification) từ (2) |
| 4 | $$C(a) \to P(a)$$ | **UI** từ Tiền đề 1 (thế $$x = a$$ — hoàn toàn hợp lệ vì UI cho phép dùng bất kỳ $$a$$ nào!) |
| 5 | $$P(a)$$ | **Modus Ponens** từ (3) và (4) |
| 6 | $$P(a) \land R(a)$$ | Phép hội từ (5) và (3) |
| 7 | **$$\exists x\,(P(x) \land R(x))$$** | **EG** từ (6) — **ĐPCM!** |

## Existential Instantiation (EI) — Cụ thể hóa tồn tại

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Từ $$\exists x\,P(x)$$, ta được phép giới thiệu một hằng số mới $$c$$ sao cho $$P(c)$$ đúng.
</div>


<div class="textbook-equation" markdown="1">
$$\frac{\exists x\,P(x)}{P(c)}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Điều kiện bắt buộc: $$c$$ phải là một ký hiệu mới, chưa xuất hiện trước đó trong chứng minh và không mang thêm giả thiết đặc biệt nào.

<div class="textbook-example" markdown="1">
**Ví dụ**: Từ "tồn tại một sinh viên đạt điểm 10", ta có thể gọi sinh viên đó là $$s_0$$ và viết $$Score10(s_0)$$, nhưng không được tự ý đồng nhất $$s_0$$ với An nếu không có dữ kiện cho phép.
</div>


## Existential Generalization (EG) — Tổng quát hóa tồn tại

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Nếu biết $$P(c)$$ đúng với một phần tử cụ thể $$c$$ trong miền, ta có thể kết luận $$\exists x\,P(x)$$.
</div>


<div class="textbook-equation" markdown="1">
$$\frac{P(c)}{\exists x\,P(x)}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Biết $$Prime(2)$$, ta suy ra $$\exists x\,Prime(x)$$.

![Cây thuật ngữ logic](/discrete-mathematics-for-computer-science-iuh/img/course/Termstammbaum.png)

<p class="textbook-figure-caption" data-figure="2.13">Cây phân tích thuật ngữ (term tree) — minh họa cấu trúc công thức khi áp dụng quy tắc suy luận từng bước.</p>
</div>

## Ví dụ tổng hợp

**Bài toán**: Chứng minh lập luận sau là hợp lệ.

**Tiền đề**:
1. $$\forall x\,(Programmer(x) \to KnowsLogic(x))$$
2. $$Programmer(Linh)$$

**Kết luận cần chứng minh**: $$KnowsLogic(Linh)$$

<div class="textbook-proof" markdown="1">
**Chứng minh** (các bước suy luận):

| Bước | Mệnh đề | Lý do |
|:---:|:---|:---|
| 1 | $$\forall x\,(Programmer(x) \to KnowsLogic(x))$$ | Tiền đề (1) |
| 2 | $$Programmer(Linh) \to KnowsLogic(Linh)$$ | Từ (1) bằng **Universal Instantiation (UI)** |
| 3 | $$Programmer(Linh)$$ | Tiền đề (2) |
| 4 | $$KnowsLogic(Linh)$$ | Từ (2) và (3) bằng **Modus Ponens** |
</div>

**Kết luận**: $$KnowsLogic(Linh)$$ đã được chứng minh.

<div class="content-box example-box textbook-block" markdown="1">
Bảng chứng minh trên tuân theo cấu trúc chuẩn: cột **Bước** đánh số thứ tự từng dòng; cột **Mệnh đề** ghi công thức logic thu được; cột **Lý do** nêu rõ tiền đề hoặc quy tắc áp dụng (UI, MP, ...).
</div>

![Socrates](/discrete-mathematics-for-computer-science-iuh/img/course/Socrates_Louvre.jpg)

<p class="textbook-figure-caption" data-figure="2.14">Socrates — ví dụ kinh điển trong tam đoạn luận: "Người Hy Lạp là người; người thì phải chết; Socrates là người Hy Lạp" → Socrates phải chết.</p>
## Suy luận với lượng từ tồn tại

Xét lập luận:

1. $$\exists x\,(Student(x)\land LikesMath(x))$$
2. $$\forall x\,(LikesMath(x)\to CanLearnDiscreteMath(x))$$
3. Kết luận: $$\exists x\,(Student(x)\land CanLearnDiscreteMath(x))$$

<div class="textbook-proof" markdown="1">
**Chứng minh**:

1. Từ (1), dùng EI giới thiệu một hằng mới $$a$$ sao cho $$Student(a)\land LikesMath(a)$$.
2. Dùng phép giản lược (tách hội) để thu được $$Student(a)$$ và $$LikesMath(a)$$.
3. Từ (2), dùng UI với $$a$$: $$LikesMath(a)\to CanLearnDiscreteMath(a)$$.
4. Từ $$LikesMath(a)$$ và bước 3, dùng Modus Ponens: $$CanLearnDiscreteMath(a)$$.
5. Từ $$Student(a)$$ và $$CanLearnDiscreteMath(a)$$, dùng phép nối: $$Student(a)\land CanLearnDiscreteMath(a)$$.
6. Dùng EG: $$\exists x\,(Student(x)\land CanLearnDiscreteMath(x))$$.
</div>

![Cây quyết định](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="2.15">Cây quyết định — mô hình suy luận có cấu trúc phân nhánh, tương tự chuỗi suy luận UI/EI/MP trong logic vị từ.</p>
## Bài tập thực hành

### Bài tập 1: Nhận diện quy tắc

Xác định các quy tắc suy luận được dùng trong mỗi bước sau:

1. $$\forall x\,(P(x) \to Q(x))$$, $$P(a)$$ → $$Q(a)$$
2. $$P(c)$$ → $$\exists x\,P(x)$$

<details>
<summary>Đáp án</summary>

1. **Universal Instantiation (UI)** (để rút ra $$P(a) \to Q(a)$$) kết hợp với **Modus Ponens** (từ $$P(a) \to Q(a)$$ và $$P(a)$$ suy ra $$Q(a)$$).
2. **Existential Generalization (EG)**.

</details>

### Bài tập 2: Hoàn thiện chứng minh

Cho $$\forall x\,(Student(x) \to HasID(x))$$ và $$\exists x\,Student(x)$$. Chứng minh $$\exists x\,HasID(x)$$.

<details>
<summary>Đáp án</summary>

1. $$\exists x\,Student(x)$$ (tiền đề)
2. $$Student(c)$$ (EI với hằng mới $$c$$)
3. $$Student(c) \to HasID(c)$$ (UI từ tiền đề còn lại)
4. $$HasID(c)$$ (Modus Ponens từ 2 và 3)
5. $$\exists x\,HasID(x)$$ (EG từ 4)

</details>

### Bài tập 3: Tìm lỗi

Tìm và giải thích lỗi trong lập luận sau:

> Mọi sinh viên đều học Discrete Math.
> Lan là sinh viên.
> Vậy Lan học Discrete Math.
> Do đó mọi sinh viên đều học Discrete Math.

<details>
<summary>Đáp án</summary>

Lỗi nằm ở bước cuối: từ một trường hợp cụ thể (Lan) không được dùng UG để kết luận cho "mọi sinh viên" (UG chỉ áp dụng khi đối tượng được chọn tùy ý, không phải tên riêng cụ thể).

</details>

### Bài tập 4: Universal Instantiation và Modus Ponens

Cho các giả thiết:

1. $$\forall x\,(Human(x) \to Mortal(x))$$
2. $$Human(Socrates)$$

Ta suy ra $$Mortal(Socrates)$$ bằng UI và Modus Ponens. Hãy áp dụng quy trình tương tự cho các cặp giả thiết sau:

(a) $$\forall x\,(Student(x) \to TakesExam(x))$$ và $$Student(Lan)$$
(b) $$\forall x\,(Bird(x) \to CanFly(x))$$ và $$Bird(Eagle)$$
(c) $$\forall n\,(Even(n) \to DivisibleBy2(n))$$ và $$Even(42)$$

<details>
<summary>Đáp án</summary>

(a) UI từ (1): $$Student(Lan) \to TakesExam(Lan)$$; Modus Ponens với $$Student(Lan)$$: $$TakesExam(Lan)$$ ("Lan tham gia thi").

(b) UI từ (1): $$Bird(Eagle) \to CanFly(Eagle)$$; Modus Ponens với $$Bird(Eagle)$$: $$CanFly(Eagle)$$ ("Đại bàng bay được").

(c) UI từ (1): $$Even(42) \to DivisibleBy2(42)$$; Modus Ponens với $$Even(42)$$: $$DivisibleBy2(42)$$ ("42 chia hết cho 2").

</details>

### Bài tập 5: Existential Instantiation và Existential Generalization

Cho $$\exists x\,(Student(x) \land \neg Passed(x))$$.

(a) Áp dụng EI để giới thiệu một hằng số mới $$c$$. Điều kiện khi dùng EI là gì?
(b) Từ kết quả của EI, áp dụng EG để suy ra $$\exists x\,Student(x)$$.
(c) Giải thích tại sao từ $$\exists x\,P(x)$$ không thể suy ra $$\forall x\,P(x)$$ bằng EG.

<details>
<summary>Đáp án</summary>

(a) EI cho ta $$Student(c) \land \neg Passed(c)$$, với $$c$$ là hằng số mới chưa từng xuất hiện trong bất kỳ giả thiết hay bước suy luận nào trước đó, để tránh gán nhầm các tính chất của đối tượng khác cho nhân chứng này.

(b) Từ $$Student(c) \land \neg Passed(c)$$, dùng phép giản lược thu được $$Student(c)$$, rồi dùng EG suy ra $$\exists x\,Student(x)$$.

(c) EG chỉ cho phép suy ra lượng từ tồn tại ($$\exists$$), không suy ra được lượng từ toàn thể ($$\forall$$). Để kết luận $$\forall x\,P(x)$$ cần dùng UG với một phần tử tùy ý, trong khi hằng số $$c$$ sinh ra từ EI chỉ là một nhân chứng cụ thể.

</details>

### Bài tập 6: Áp dụng UG đúng cách

Cho $$\forall x\,(P(x) \to Q(x))$$ và $$\forall x\,P(x)$$.

(a) Chứng minh $$\forall x\,Q(x)$$ bằng UI và UG.
(b) Nếu thay giả thiết thứ hai thành $$P(a)$$ (với $$a$$ là một hằng số cụ thể), có thể suy ra $$\forall x\,Q(x)$$ không? Giải thích và nêu phản ví dụ.

<details>
<summary>Đáp án</summary>

(a) Chứng minh:
    - Gọi $$c$$ là phần tử tùy ý trong miền xác định.
    - UI từ $$\forall x\,P(x)$$: $$P(c)$$.
    - UI từ $$\forall x\,(P(x) \to Q(x))$$: $$P(c) \to Q(c)$$.
    - Modus Ponens: $$Q(c)$$.
    - Vì $$c$$ là phần tử tùy ý, áp dụng UG ta được $$\forall x\,Q(x)$$.
    Đây là dạng tam đoạn luận (syllogism) trong logic vị từ.

(b) **Không thể.** Từ $$P(a) \to Q(a)$$ (UI) và $$P(a)$$ ta chỉ suy ra được $$Q(a)$$; không được dùng UG vì $$a$$ là hằng số cụ thể chứ không phải phần tử tùy ý.

    Phản ví dụ trên miền $$\mathbb{Z}$$: đặt $$P(x)$$ là "$$x$$ chia hết cho 4", $$Q(x)$$ là "$$x$$ là số chẵn", và $$a = 4$$. Khi đó cả hai tiền đề $$\forall x\,(P(x) \to Q(x))$$ (mọi bội của 4 đều chẵn) và $$P(4)$$ (4 chia hết cho 4) đều đúng, nhưng kết luận $$\forall x\,Q(x)$$ ("mọi số nguyên đều chẵn") là sai vì 3 là số lẻ.

</details>

### Bài tập 7: Chứng minh bằng suy luận vị từ — Bài toán "Người Hy Lạp"

Chứng minh kết luận từ các giả thiết sau:

1. $$\forall x\,(Greek(x) \to Human(x))$$ — Người Hy Lạp là người.
2. $$\forall x\,(Human(x) \to Mortal(x))$$ — Người thì phải chết.
3. $$Greek(Socrates)$$ — Socrates là người Hy Lạp.

Kết luận: $$\exists x\,Mortal(x)$$ — Tồn tại người phải chết. Hãy viết từng bước suy luận.

<details>
<summary>Đáp án</summary>

- Bước 1 (UI từ 1): $$Greek(Socrates) \to Human(Socrates)$$
- Bước 2 (UI từ 2): $$Human(Socrates) \to Mortal(Socrates)$$
- Bước 3 (Hypothetical Syllogism từ bước 1 và bước 2): $$Greek(Socrates) \to Mortal(Socrates)$$
- Bước 4 (Modus Ponens từ bước 3 và giả thiết 3): $$Mortal(Socrates)$$
- Bước 5 (EG từ bước 4): $$\exists x\,Mortal(x)$$

Kết luận: Tồn tại người phải chết (cụ thể là Socrates). Đây là phiên bản logic vị từ của tam đoạn luận kinh điển thời Aristotle.

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

(a) **Lỗi:** EI chỉ áp dụng được khi lượng từ tồn tại $$\exists$$ nằm ở ngoài cùng, không áp dụng trực tiếp lên $$\forall x \exists y\,P(x, y)$$.
    Cách đúng: trước hết dùng UI với phần tử tùy ý $$c$$ để thu được $$\exists y\,P(c, y)$$, sau đó mới dùng EI để giới thiệu hằng số mới $$d$$ (có thể phụ thuộc vào $$c$$) sao cho $$P(c, d)$$.

(b) **Lỗi:** EG chỉ suy ra được lượng từ tồn tại $$\exists$$, không phải $$\forall$$. Từ $$P(a) \land Q(a)$$, EG cho $$\exists x\,(P(x) \land Q(x))$$; muốn có $$\forall x\,(P(x) \land Q(x))$$ thì cần dùng UG với phần tử tùy ý chứ không phải hằng số cụ thể $$a$$.

(c) **Lỗi:** Hai hằng số sinh ra từ hai lần EI không nhất thiết bằng nhau. Từ $$\exists x\,P(x)$$ ta dùng EI được $$P(c)$$; từ $$\exists x\,Q(x)$$ ta phải dùng một hằng số mới $$d$$ (không được tái sử dụng $$c$$) để có $$Q(d)$$, nên không thể suy ra $$\exists x\,(P(x) \land Q(x))$$.
    Phản ví dụ trên $$\mathbb{Z}$$: $$P(x)$$ là "$$x$$ là số chẵn", $$Q(x)$$ là "$$x$$ là số lẻ". Cả $$\exists x\,P(x)$$ ($$x = 2$$) và $$\exists x\,Q(x)$$ ($$x = 3$$) đều đúng, nhưng $$\exists x\,(P(x) \land Q(x))$$ sai vì không có số nguyên nào vừa chẵn vừa lẻ.

</details>

---


### Thử nghiệm: suy luận vị từ từng dòng

Duyệt từng dòng chứng minh với các quy tắc UI, EI, EG, thử hai lỗi kinh điển (tái sử dụng tên khi dùng EI, hoặc dùng UG từ hằng số cụ thể) và xem phản ví dụ trên mô hình nhỏ.

<div class="interactive-demo" markdown="1">
<div data-demo="predproof-explainer" data-preset="socrates"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Công cụ tương tác

Kéo thả các bước suy luận vị từ để ghép thành một chứng minh ngắn rồi kiểm tra từng dòng.
<div class="interactive-demo" markdown="1">
<div data-demo="predicate-proof-dnd"></div>
</div>
<script src="{{ '/public/js/predicate-proof-dnd.js' | relative_url }}"></script>

## Xem thêm / Video gợi ý

- [Quantifiers and Nested Quantifiers](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — Trefor Bazett (Clear examples with predicates)
- [Predicate Logic — ∀ and ∃](https://www.youtube.com/watch?v=8l7L9v0p0Q) — TrevTutor (Discrete Math playlist)


## Tóm tắt

- Bốn quy tắc suy luận với lượng từ gồm: **UI** (cụ thể hóa toàn thể), **UG** (tổng quát hóa toàn thể), **EI** (cụ thể hóa tồn tại) và **EG** (tổng quát hóa tồn tại).
- UI và EI kết hợp với các quy tắc suy luận mệnh đề (Modus Ponens, Modus Tollens, tam đoạn luận) tạo thành chuỗi chứng minh hợp lệ.
- UG chỉ được áp dụng khi phần tử được chọn **tùy ý**; EI yêu cầu hằng số mới **chưa xuất hiện** trước đó trong chứng minh.
- Các lỗi thường gặp: nhầm EG với UG, áp dụng EI khi $$\forall$$ nằm ngoài cùng, hoặc dùng chung một hằng số cho hai lần EI độc lập.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu **logic vị từ trong lập trình và cơ sở dữ liệu** — cách các khái niệm vị từ và lượng từ được triển khai trong thực tế.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=akiBw21opuw">Rules of Inference for Quantified Statements (Part 1)</a> — Neso Academy, tiếng Anh. Giới thiệu các quy tắc suy luận cho phát biểu có lượng từ.
- <a href="https://www.youtube.com/watch?v=RfSGkkkGtPg">Proof in predicate logic  1: Universal Instantiation</a> — Simon Cushing, tiếng Anh. Trình bày cụ thể quy tắc Universal Instantiation từ $$\forall x\,P(x)$$ xuống một phần tử.
- <a href="https://www.youtube.com/watch?v=a11_3qvelwE">Predicate Logic Proof Example 2: Using Instantiation and Generalization</a> — FREGE: A Logic Course Elaine Rich, Alan Cline, tiếng Anh. Minh họa một bài chứng minh kết hợp cụ thể hóa và tổng quát hóa.
