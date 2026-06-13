---
layout: post
title: "Lượng từ và Lượng từ lồng nhau"
categories: chapter02
date: 2021-01-01
order: 2
required: true
lang: en
---

# Lượng từ và Lượng từ lồng nhau

Ở bài trước, chúng ta đã biết vị từ là gì và cách biến một phát biểu có biến thành mệnh đề bằng cách gán giá trị cụ thể. Nhưng trong toán học và lập trình, ta hiếm khi nói về một đối tượng cụ thể — ta cần nói về **tất cả** hoặc **ít nhất một** phần tử trong tập hợp.

Và chỉ cần thay một chữ "mọi" bằng "tồn tại", ý nghĩa của phát biểu có thể đảo ngược hoàn toàn:

- *"Mọi sinh viên đều qua môn"* — một khẳng định rất mạnh, chỉ cần một ngoại lệ là sai.
- *"Tồn tại một sinh viên qua môn"* — một khẳng định yếu hơn nhiều, chỉ cần một ví dụ là đúng.

Trong database, `FOR ALL` và `EXISTS` dẫn đến hai truy vấn có kết quả hoàn toàn khác nhau. Trong kiểm chứng phần mềm, đặt sai lượng từ có thể biến một đặc tả đúng thành vô nghĩa. Trong toán học, nhầm thứ tự lượng từ lồng nhau là một trong những lỗi suy luận phổ biến và tinh vi nhất.

Vì vậy, **lượng từ** không phải chi tiết ký hiệu cho có — chúng là công cụ kiểm soát **phạm vi** của phát biểu và **độ mạnh** của kết luận. Khi lượng từ bắt đầu lồng nhau — "với mọi x, tồn tại y sao cho..." — ta bước vào vùng đất mà nhiều lỗi suy luận tinh vi nhất xuất hiện, nhưng cũng là nơi tạo nên sức mạnh thật sự của toán học, specification và các bài toán tìm kiếm, tối ưu, chứng minh tự động.

Trong bài này, chúng ta sẽ học cách sử dụng lượng từ phổ dụng ($$\forall$$) và lượng từ tồn tại ($$\exists$$), cách kết hợp chúng với vị từ, và đặc biệt là cách đọc đúng ý nghĩa khi nhiều lượng từ lồng vào nhau.

## 1. Vị từ, miền xác định và lượng từ

**Định nghĩa**: Một **vị từ** $$P(x)$$ là một phát biểu chứa biến, chưa có giá trị chân trị cho đến khi biến được gán giá trị trong một **miền xác định**.

**Ký hiệu**:

- $$U$$: miền xác định (universe of discourse).
- $$P(x)$$: vị từ một biến.
- $$P(x,y)$$: vị từ hai biến.

**Ví dụ**: Nếu $$U = \mathbb{Z}$$ và $$P(x)$$ là "$$x$$ chia hết cho 2", thì $$P(4)$$ đúng, $$P(5)$$ sai.

#### Minh họa trực quan: Miền xác định như "sân chơi"

Hãy tưởng tượng **miền xác định** là sân chơi, và vị từ là luật chơi:

- **Sân chơi**: $$\mathbb{R}$$ (tất cả số thực)
- **Luật**: "Mọi $$x$$ đều có $$x^2 \geq 0$$" → Đúng với mọi sân chơi
- **Luật**: "Mọi $$x$$ đều có nghịch đảo" → **Sai** nếu sân chơi có 0 (vì 0 không có nghịch đảo)

**Quy tắc nhanh**:
- Miền càng rộng → Luật càng khó đúng
- Miền càng hẹp → Luật dễ đúng hơn

**Ví dụ trong SQL**:

```sql
-- Miền: tất cả sinh viên
SELECT * FROM students WHERE gpa >= 0;        -- Luôn đúng

-- Miền: sinh viên có điểm
SELECT * FROM students WHERE gpa >= 3.5;      -- Có thể đúng/sai
```

## 2. Lượng từ toàn thể

**Định nghĩa**: $$\forall x\,P(x)$$ đọc là "với mọi $$x$$, $$P(x)$$ đúng". Mệnh đề này đúng khi $$P(x)$$ đúng với tất cả phần tử trong miền xác định.

**Ký hiệu**: $$\forall$$, thường gợi nhớ từ tiếng Anh "for all".

**Ví dụ**:

- $$\forall x \in \mathbb{R},\ x^2 \ge 0$$ là đúng.
- $$\forall n \in \mathbb{N},\ n+1 > n$$ là đúng.
- $$\forall n \in \mathbb{Z},\ n^2 > n$$ là sai vì $$n=0$$ là phản ví dụ.

**Chứng minh một mệnh đề toàn thể** thường cần lập luận cho một phần tử tùy ý. Ví dụ, để chứng minh $$\forall n \in \mathbb{Z},\ n(n+1)$$ chẵn, lấy $$n$$ tùy ý. Trong hai số liên tiếp $$n$$ và $$n+1$$, một số chẵn, nên tích chia hết cho 2.

## 3. Lượng từ tồn tại

**Định nghĩa**: $$\exists x\,P(x)$$ đọc là "tồn tại ít nhất một $$x$$ sao cho $$P(x)$$ đúng".

**Ký hiệu**: $$\exists$$, thường gợi nhớ từ "exists".

**Ví dụ**:

- $$\exists x \in \mathbb{Z},\ x^2 = 9$$ đúng vì $$x=3$$ hoặc $$x=-3$$.
- $$\exists n \in \mathbb{N},\ n < 0$$ sai nếu $$\mathbb{N}$$ là tập số tự nhiên không âm.
- $$\exists p \in \mathbb{P},\ p$$ chẵn đúng vì $$p=2$$.

**Chứng minh tồn tại** có thể bằng cách đưa ra nhân chứng (witness). Ví dụ, để chứng minh $$\exists x \in \mathbb{Z}, x^2 = 16$$, chỉ cần nêu $$x=4$$.

## 4. Lượng từ duy nhất

**Định nghĩa**: $$\exists!x\,P(x)$$ nghĩa là tồn tại đúng một $$x$$ sao cho $$P(x)$$ đúng.

Một cách viết tương đương:

$$\exists x\big(P(x) \land \forall y(P(y) \to y=x)\big).$$

**Ví dụ**: Trong tập số nguyên, $$\exists!x(x+3=10)$$ đúng vì chỉ có $$x=7$$.

## 5. Lượng từ lồng nhau

Lượng từ lồng nhau là nơi nhiều sinh viên nhầm lẫn nhất. Thứ tự lượng từ có thể thay đổi ý nghĩa hoàn toàn.

**Ví dụ**: Với miền là sinh viên và môn học, đặt $$T(x,y)$$ là "sinh viên $$x$$ thích môn $$y$$".

- $$\forall x\exists y\,T(x,y)$$: mỗi sinh viên thích ít nhất một môn nào đó.
- $$\exists y\forall x\,T(x,y)$$: có một môn mà tất cả sinh viên đều thích.

Mệnh đề thứ hai mạnh hơn mệnh đề thứ nhất.

### Khối suy luận: Vì sao thứ tự quan trọng?

Giả sử có ba sinh viên An, Bình, Chi và ba môn Toán, Lý, Tin.

- An thích Toán.
- Bình thích Lý.
- Chi thích Tin.

Khi đó $$\forall x\exists y\,T(x,y)$$ đúng: ai cũng có ít nhất một môn thích. Nhưng $$\exists y\forall x\,T(x,y)$$ sai: không có môn chung cho cả ba.

## 6. Phủ định lượng từ

**Định lý De Morgan cho lượng từ**:

$$\neg\forall x\,P(x) \equiv \exists x\,\neg P(x)$$

$$\neg\exists x\,P(x) \equiv \forall x\,\neg P(x)$$

**Ví dụ**:

Câu: "Mọi sinh viên đều nộp bài."

$$\forall x\,N(x)$$

Phủ định đúng là: "Tồn tại ít nhất một sinh viên không nộp bài."

$$\exists x\,\neg N(x)$$

Không được phủ định thành "mọi sinh viên đều không nộp bài".

## 7. Dịch câu tự nhiên sang logic

**Ví dụ 1**: "Mọi số nguyên chẵn đều chia hết cho 2."

$$\forall n \in \mathbb{Z}\,(Even(n) \to DivisibleBy2(n)).$$

**Ví dụ 2**: "Có một sinh viên học tất cả các môn bắt buộc."

$$\exists s\,\forall c\,(Required(c) \to Takes(s,c)).$$

**Ví dụ 3**: "Mỗi tài khoản có đúng một email chính."

$$\forall a\,\exists! e\,PrimaryEmail(a,e).$$

## 10. Ứng dụng trong Khoa học Máy tính

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

Lượng từ cũng xuất hiện trong đặc tả phần mềm: "mọi request hợp lệ đều nhận response", "tồn tại một đường đi từ node nguồn đến node đích", "mỗi khóa ánh xạ đến đúng một giá trị".

## Bài tập thực hành

### Bài tập 1: Phủ định lượng từ

Viết phủ định của các công thức sau:

1. $$\forall x (P(x) \to Q(x))$$
2. $$\exists x \forall y (R(x,y))$$

<details>
<summary>Đáp án</summary>

1. $$\exists x (P(x) \land \lnot Q(x))$$
2. $$\forall x \exists y \lnot R(x,y)$$

</details>

### Bài tập 2: Dịch sang logic vị từ

Dịch câu sau sang ngôn ngữ logic vị từ (x là sinh viên, y là môn học):

"Mọi sinh viên đều có ít nhất một môn học mà họ đạt điểm tối đa."

<details>
<summary>Đáp án</summary>

$$\forall x \exists y (Student(x) \land Course(y) \land Takes(x,y) \land Score(x,y,10))$$

</details>

### Bài tập 3: Phân biệt thứ tự lượng từ

Giải thích tại sao hai công thức sau **không** tương đương:

- $$\forall x \exists y (y > x)$$
- $$\exists y \forall x (y > x)$$

<details>
<summary>Đáp án</summary>

Công thức thứ nhất đúng trên $$\mathbb{R}$$ (với mọi x luôn tồn tại y = x+1). Công thức thứ hai sai vì không tồn tại một y nào lớn hơn mọi x.

</details>

### Bài tập 4: Ứng dụng Python/SQL

Viết đoạn code Python và câu truy vấn SQL tương ứng với mệnh đề:

" Tồn tại một sinh viên có điểm trung bình > 9.0 "

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

## Tóm tắt

Lượng từ biến vị từ thành mệnh đề có giá trị đúng-sai. $$\forall$$ yêu cầu mọi phần tử thỏa mãn, $$\exists$$ chỉ cần một nhân chứng, còn $$\exists!$$ yêu cầu đúng một nhân chứng. Với lượng từ lồng nhau, thứ tự rất quan trọng; khi phủ định, phải đổi $$\forall$$ thành $$\exists$$ và ngược lại, đồng thời phủ định vị từ bên trong.
