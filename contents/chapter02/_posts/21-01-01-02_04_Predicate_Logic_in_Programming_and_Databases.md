---
layout: post
title: "Logic Vị từ trong Lập trình và Cơ sở Dữ liệu"
categories: chapter02
date: 2021-01-01
order: 4
required: false
lang: en
---

Mỗi lần bạn viết `assert age >= 18` hay thêm điều kiện `WHERE NOT EXISTS (...)`, bạn đang dùng cùng một ngôn ngữ toán học: **logic vị từ** (predicate logic) với lượng từ $$\forall$$ và $$\exists$$.

```python
from pydantic import BaseModel, Field, field_validator

class Student(BaseModel):
    id: int = Field(gt=0)
    gpa: float = Field(ge=0.0, le=4.0)

    @field_validator("gpa")
    @classmethod
    def gpa_must_be_finite(cls, v: float) -> float:
        assert v == v  # ∀ giá trị hợp lệ: không phải NaN
        return v
```

Đoạn code trên không chỉ "kiểm tra input". Nó là một **đặc tả** (specification): với mọi đối tượng `Student` được tạo thành công, các vị từ `id > 0`, `0 ≤ gpa ≤ 4` đều đúng. Trong SQL, cùng ý tưởng xuất hiện dưới dạng `CHECK`, `FOREIGN KEY`, và truy vấn có `EXISTS` / `NOT EXISTS`.

Từ Frege và lượng từ ∀/∃ đến validation schema, contract programming, và truy vấn quan hệ — bài này nối Chương 2 với cách kỹ sư viết phần mềm an toàn hàng ngày.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Dịch** yêu cầu nghiệp vụ có "mọi" / "tồn tại" sang công thức logic vị từ và sang SQL/Python tương đương.
- **Viết** assertion, validator, và schema kiểu Pydantic/Zod như triển khai thực tế của vị từ.
- **Phân biệt** phủ định lượng từ ($$\lnot \forall$$ ↔ $$\exists \lnot$$) khi đọc `NOT EXISTS` và điều kiện lồng nhau.
- **Mô hình hóa** ràng buộc CSDL (UNIQUE, FOREIGN KEY, CHECK) bằng $$\forall$$ và $$\exists$$ trên miền bản ghi.
- **Nhận ra** khi nào cần đặc tả hình thức (formal spec) thay vì chỉ test vài trường hợp.

**Từ khóa**: logic vị từ (predicate logic), lượng từ (quantifier), đặc tả (specification), assertion, schema validation, truy vấn quan hệ (relational query).

---

## Phần 1: Từ yêu cầu tiếng Việt đến công thức

### 1.1. Mẫu dịch thường gặp

| Câu nghiệp vụ | Logic vị từ (miền $$D$$) |
|---|---|
| Mọi sinh viên đều đã đăng ký ít nhất một học phần | $$\forall s \in D_{student},\ \exists c \in D_{course},\ Enrolled(s,c)$$ |
| Có ít nhất một server còn sống | $$\exists h \in D_{host},\ Healthy(h)$$ |
| Không tồn tại hai email trùng nhau | $$\lnot \exists u_1, u_2 \in D_{user},\ (u_1 \neq u_2 \land SameEmail(u_1,u_2))$$ |
| Mọi đơn hàng đều có đúng một người mua | $$\forall o \in D_{order},\ \exists! u \in D_{user},\ Buyer(o,u)$$ |

**Ví dụ**: "Mọi giao dịch phải được xác thực trước khi xử lý"

$$\forall t \in Transactions,\ Processed(t) \limpl Verified(t)$$

Đọc theo hướng lập trình: *nếu* `processed(t)` thì *bắt buộc* `verified(t)` đã đúng trước đó.

![Gottlob Frege — nền tảng logic vị từ hiện đại](/discrete-mathematics-for-computer-science-iuh/img/course/gottlob_frege.svg)

*Hình 2.16: Gottlob Frege — đặt nền cho logic vị từ (first-order logic); hôm nay cùng cấu trúc ∀/∃ xuất hiện trong SQL và validation code.*

### 1.2. Phủ định lượng từ — lỗi hay gặp nhất

Luật De Morgan cho lượng từ:

$$\lnot \forall x\, P(x) \equiv \exists x\, \lnot P(x)$$
$$\lnot \exists x\, P(x) \equiv \forall x\, \lnot P(x)$$

**SQL**: "Không có đơn hàng nào chưa thanh toán" **không** phải `NOT EXISTS (unpaid orders)` theo nghĩa mơ hồ — phải viết rõ:

```sql
-- ∀ order: NOT (status = 'unpaid')
-- tương đương NOT EXISTS (SELECT 1 FROM orders o WHERE o.status = 'unpaid')
SELECT COUNT(*) = 0 AS all_paid
FROM orders
WHERE status = 'unpaid';
```

<div class="content-box warning-box" markdown="1">
**Cẩn thận**: $$\forall x \exists y$$ và $$\exists y \forall x$$ **không** tương đương. "Mỗi sinh viên có một cố vấn" khác "Có một cố vấn cho mọi sinh viên". Thứ tự lượng từ trong spec ảnh hưởng trực tiếp đến thiết kế API và schema.
</div>

---

## Phần 2: Logic vị từ trong SQL

### 2.1. `EXISTS` và `NOT EXISTS`

`EXISTS (subquery)` đúng khi subquery trả về **ít nhất một dòng** — đó chính là $$\exists$$.

```sql
-- Sinh viên đã đăng ký ít nhất một học phần
SELECT s.id, s.name
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.id
);

-- Sinh viên chưa đăng ký học phần nào  ≡  ∀ course: NOT enrolled(s, course)
SELECT s.id, s.name
FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.id
);
```

### 2.2. `FOREIGN KEY` và `UNIQUE` như vị từ toàn cục

```sql
CREATE TABLE enrollments (
    student_id INT REFERENCES students(id),
    course_id  INT REFERENCES courses(id),
    PRIMARY KEY (student_id, course_id)
);
```

- `REFERENCES students(id)`: mọi `student_id` trong `enrollments` phải tồn tại trong `students` — $$\forall e \in Enrollments,\ \exists s \in Students,\ e.student\_id = s.id$$.
- `PRIMARY KEY`: không tồn tại hai dòng trùng cặp khóa — tính duy nhất.

![Truy vấn SQL — thể hiện ∃ và ∀ qua EXISTS, JOIN, ràng buộc](/discrete-mathematics-for-computer-science-iuh/img/course/sql_query.svg)

*Hình 2.17: Truy vấn SQL biểu diễn lượng từ qua EXISTS/NOT EXISTS và ràng buộc quan hệ — cùng ý tưởng với công thức ∀/∃ trên miền bản ghi.*

### 2.3. `CHECK` — vị từ trên từng dòng

```sql
ALTER TABLE students
ADD CONSTRAINT gpa_range CHECK (gpa >= 0 AND gpa <= 4);
```

Đây là $$\forall s \in Students,\ 0 \le s.gpa \le 4$$ được DBMS kiểm tra mỗi lần `INSERT`/`UPDATE`.

---

## Phần 3: Assertion và schema trong code

### 3.1. `assert` — hợp đồng runtime

```python
def transfer(from_id: int, to_id: int, amount: float, balance: dict[int, float]) -> None:
    assert amount > 0, "∀ giao dịch hợp lệ: amount > 0"
    assert from_id in balance and balance[from_id] >= amount
    balance[from_id] -= amount
    balance[to_id] = balance.get(to_id, 0) + amount
```

`assert` không thay thế validation phía client, nhưng bảo vệ **invariant** nội bộ: điều kiện phải đúng với mọi trạng thái hợp lệ của chương trình.

### 3.2. Pydantic / Zod — vị từ trên kiểu dữ liệu

**Python (Pydantic)**:

```python
from pydantic import BaseModel, Field

class CreateOrder(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(ge=1, le=99)
```

**TypeScript (Zod)**:

```typescript
import { z } from "zod";

const CreateOrder = z.object({
  productId: z.number().int().positive(),
  quantity: z.number().int().min(1).max(99),
});
```

Mỗi ràng buộc `.positive()`, `.min(1)` là một vị từ một biến: $$P(x)$$ phải đúng trước khi object được chấp nhận.

### 3.3. Design by Contract (DbC)

```python
def withdraw(balance: float, amount: float) -> float:
    """
    Precondition:  amount > 0
    Postcondition: result == balance - amount
    Invariant:     result >= 0
    """
    if amount <= 0:
        raise ValueError("precondition violated")
    new_balance = balance - amount
    if new_balance < 0:
        raise ValueError("invariant violated: negative balance")
    return new_balance
```

Precondition/postcondition/invariant là ba lớp vị từ bọc hàm — tiền thân của các công cụ như Eiffel, và tinh thần của Rust `debug_assert!`, Kotlin `require`/`check`.

<div class="content-box insight-box" markdown="1">
**Nhận xét**: Test kiểm tra *một số* input; đặc tả ∀/∃ nói *mọi* input trong miền. Validation schema là điểm giao thực dụng: bạn viết vài dòng code nhưng đang mã hóa phạm vi ∀ trên request body.
</div>

---

## Phần 4: Ứng dụng nâng cao

### 4.1. Kiểm chứng và SMT/SAT

Khi hệ thống cực kỳ nhạy cảm (hàng không, thanh toán, kernel), người ta dùng **model checker** hoặc **SMT solver** để hỏi: "Có tồn tại trạng thái vi phạm invariant không?" — tức $$\exists$$ counterexample. Nếu solver trả `unsat`, ta có bằng chứng mọi luồng thỏa spec (trong mô hình hữu hạn).

### 4.2. Policy as code

```python
def can_refund(order, user) -> bool:
    # ∀ refund: user là owner HOẶC user là admin
    return order.user_id == user.id or user.role == "admin"
```

Rule engine, OPA (Open Policy Agent), và IAM policy JSON đều là logic vị từ ẩn: biến (subject, resource), vị từ (`is_owner`, `has_role`), lượng từ trong rule tập hợp (`any`, `all`).

## Công cụ tương tác

<div data-demo="nested-quantifier-grid"></div>

---

## Bài tập thực hành

### Bài tập 1: Dịch sang logic vị từ

Viết công thức cho: "Mọi khóa học đều có ít nhất một giảng viên phụ trách."

<details>
<summary>Đáp án</summary>

$$\forall c \in Courses,\ \exists t \in Teachers,\ Teaches(t, c)$$

</details>

### Bài tập 2: SQL với EXISTS

Viết truy vấn trả về `course_id` của các khóa **chưa có** sinh viên nào đăng ký. Bảng: `courses(id, title)`, `enrollments(student_id, course_id)`.

<details>
<summary>Đáp án</summary>

```sql
SELECT c.id, c.title
FROM courses c
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.id
);
```

Tương đương: $$\forall s,\ \lnot Enrolled(s, c)$$ cho từng khóa $$c$$ được chọn.

</details>

### Bài tập 3: Phủ định lượng từ

Câu "Không phải mọi sinh viên đều đạt điểm ≥ 5" tương đương công thức nào?

(a) $$\forall s,\ Score(s) < 5$$

(b) $$\exists s,\ Score(s) < 5$$

(c) $$\lnot \exists s,\ Score(s) \ge 5$$

<details>
<summary>Đáp án</summary>

**(b)**. $$\lnot \forall s,\ Score(s) \ge 5 \equiv \exists s,\ \lnot(Score(s) \ge 5) \equiv \exists s,\ Score(s) < 5$$.

(a) sai vì nói *mọi* sinh viên đều dưới 5. (c) sai vì phủ định *tồn tại* người đạt ≥ 5.

</details>

### Bài tập 4: Pydantic validator

Thêm validator đảm bảo `end_date >= start_date` cho class:

```python
class Booking(BaseModel):
    start_date: date
    end_date: date
```

<details>
<summary>Đáp án</summary>

```python
from datetime import date
from pydantic import BaseModel, model_validator

class Booking(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def end_after_start(self):
        if self.end_date < self.start_date:
            raise ValueError("end_date must be >= start_date")
        return self
```

Vị từ: $$\forall booking,\ booking.end\_date \ge booking.start\_date$$.

</details>

### Bài tập 5: Thứ tự lượng từ

Phân biệt nghĩa hai câu:

1. $$\forall s \in Students,\ \exists m \in Mentors,\ Assigned(s,m)$$
2. $$\exists m \in Mentors,\ \forall s \in Students,\ Assigned(s,m)$$

<details>
<summary>Đáp án</summary>

1. Mỗi sinh viên có **một** cố vấn (cố vấn có thể khác nhau giữa các sinh viên).
2. Có **một** cố vấn chung phụ trách **tất cả** sinh viên — mạnh hơn và hiếm khi đúng trong thực tế.

</details>

### Bài tập 6: Invariant tài khoản

Viết `assert` hoặc `if/raise` bảo vệ invariant: tổng số dư mọi tài khoản không đổi sau `transfer`.

```python
def transfer(balances: dict[str, float], src: str, dst: str, amt: float) -> None:
    total_before = sum(balances.values())
    # ... thực hiện chuyển ...
    total_after = sum(balances.values())
```

<details>
<summary>Đáp án</summary>

```python
def transfer(balances: dict[str, float], src: str, dst: str, amt: float) -> None:
    assert amt > 0 and balances[src] >= amt
    total_before = sum(balances.values())
    balances[src] -= amt
    balances[dst] = balances.get(dst, 0) + amt
    total_after = sum(balances.values())
    assert abs(total_before - total_after) < 1e-9, "invariant: conservation of total balance"
```

</details>

### Bài tập 7: Zod schema

Viết schema Zod cho user: `email` hợp lệ, `age` số nguyên từ 18 đến 120.

<details>
<summary>Đáp án</summary>

```typescript
import { z } from "zod";

const UserSchema = z.object({
  email: z.string().email(),
  age: z.number().int().min(18).max(120),
});
```

</details>

### Bài tập 8: Từ spec đến test

Cho vị từ $$\forall x \in \mathbb{Z},\ x^2 \ge 0$$. Đề xuất **một** test Python và giải thích vì sao test alone không chứng minh ∀.

<details>
<summary>Đáp án</summary>

```python
def test_square_non_negative():
    for x in [-3, 0, 7, 100]:
        assert x * x >= 0
```

Test chỉ kiểm tra hữu hạn giá trị; ∀ khẳng định trên vô hạn số nguyên. Cần chứng minh (induction hoặc đại số) hoặc đặc tả hình thức — đó là lý do kết hợp test + spec.

</details>

## Tóm tắt

- **∀ / ∃**: xương sống của yêu cầu "mọi" và "có tồn tại"; dịch sang SQL (`EXISTS`, ràng buộc) và validation schema.
- **Phủ định lượng từ**: `NOT EXISTS` phải đọc qua luật De Morgan; tránh nhầm thứ tự lượng từ lồng nhau.
- **Ràng buộc CSDL**: FOREIGN KEY, UNIQUE, CHECK là vị từ toàn cục trên miền bản ghi.
- **Code**: `assert`, Pydantic/Zod, DbC là triển khai thực dụng của precondition/postcondition/invariant.
- **Test vs spec**: test kiểm tra mẫu; ∀/∃ mô tả toàn miền — hai lớp bổ sung nhau.

Trong các chương tiếp theo, chúng ta sẽ dùng cùng tinh thần "phát biểu chính xác rồi suy luận" khi học chứng minh, tập hợp, và quan hệ — nền của thiết kế phần mềm đáng tin cậy.