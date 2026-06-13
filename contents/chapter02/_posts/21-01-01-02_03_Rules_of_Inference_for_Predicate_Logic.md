---
layout: post
title: "Quy tắc Suy luận trong Logic Vị từ"
categories: chapter02
date: 2021-01-01
order: 3
required: true
lang: en
---

# Quy tắc Suy luận trong Logic Vị từ

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

## 2. Universal Instantiation (UI) - Cụ thể hóa toàn thể

**Định nghĩa**: Từ một mệnh đề đúng với mọi phần tử, ta được phép suy ra nó đúng với một phần tử cụ thể bất kỳ.

$$\frac{\forall x\,P(x)}{P(c)}$$

trong đó $$c$$ là một phần tử của miền xác định.

**Ví dụ**: Nếu $$\forall x(Student(x)\to NeedsLogic(x))$$ và $$Student(An)$$, thì bằng UI ta có:

$$Student(An)\to NeedsLogic(An).$$

Kết hợp Modus Ponens, suy ra $$NeedsLogic(An)$$.

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

## 6. Ví dụ tổng hợp

Chứng minh lập luận sau hợp lệ:

1. $$\forall x(Programmer(x)\to KnowsLogic(x))$$
2. $$Programmer(Linh)$$
3. Kết luận: $$KnowsLogic(Linh)$$

**Chứng minh**:

1. $$\forall x(Programmer(x)\to KnowsLogic(x))$$ — tiền đề.
2. $$Programmer(Linh)\to KnowsLogic(Linh)$$ — từ (1) bằng UI.
3. $$Programmer(Linh)$$ — tiền đề.
4. $$KnowsLogic(Linh)$$ — từ (2), (3) bằng Modus Ponens.

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

## 10. Ứng dụng trong Khoa học Máy tính

- **Type systems**: Kiểu tổng quát như `List<T>` dùng ý tưởng "với mọi kiểu T".
- **Theorem prover**: Coq, Lean, Isabelle thực thi các quy tắc suy luận tương tự nhưng nghiêm ngặt hơn.
- **Program verification**: Đặc tả như "mọi trạng thái reachable đều thỏa invariant" cần UI/UG để chứng minh.
- **Database logic**: Query optimizer và Datalog dựa trên suy luận với biến và lượng từ.

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

## Tóm tắt

UI đi từ "mọi" đến "một trường hợp cụ thể". UG đi từ "phần tử tùy ý" đến "mọi". EI đi từ "tồn tại" đến một nhân chứng mới. EG đi từ một nhân chứng cụ thể đến kết luận tồn tại. Sử dụng đúng điều kiện của từng quy tắc là chìa khóa để tránh lập luận sai.
