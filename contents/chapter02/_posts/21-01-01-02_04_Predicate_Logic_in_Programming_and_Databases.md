---

layout: post
title: "Logic Vị từ trong Lập trình và Cơ sở Dữ liệu"
categories: chapter02
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Kết nối vị từ và lượng từ với thực hành kỹ thuật phần mềm: truy vấn SQL (EXISTS, CHECK, FOREIGN KEY), assertion, schema validation và Design by Contract."
---

Nếu bạn từng nghĩ lượng từ $\forall$ và $\exists$ chỉ sống trên bảng phấn toán học, hãy mở ngay một tệp truy vấn SQL hoặc mã Python/TypeScript của bất kỳ ứng dụng web nào: `EXISTS (SELECT ...)`, `NOT EXISTS`, `all(...)`, `any(...)`, `assert`, và ràng buộc `CHECK` trong cơ sở dữ liệu chính là **Logic Vị từ đang chạy ở tốc độ triệu bản ghi mỗi giây**.

## Bản đồ kiến thức nền: Bốn cầu nối trực tiếp từ Logic Vị từ sang Phần mềm & CSDL

1. **Phép tính Quan hệ (Relational Calculus) → SQL**:
   SQL được Edgar F. Codd thiết kế trực tiếp từ Logic Vị từ bậc nhất: mỗi bảng là một vị từ (ví dụ `Enrolled(sid, cid)` đúng khi sinh viên `sid` đăng ký môn `cid`), mệnh đề `WHERE` là điều kiện lọc, và `EXISTS` chính là lượng từ $\exists$.

2. **Biểu diễn lượng từ Toàn thể ($\forall$) trong SQL bằng Phủ định kép**:
   SQL không có từ khóa `FOR ALL` trực tiếp. Để truy vấn *"Tìm sinh viên đã học **tất cả** các môn bắt buộc"*, ta dùng chính Luật De Morgan lượng từ:
   $$\forall c\, P(s, c) \;\equiv\; \neg \exists c\, \neg P(s, c)$$
   và viết thành `WHERE NOT EXISTS (... WHERE NOT EXISTS (...))`!

3. **Tiền điều kiện, Hậu điều kiện & Bất biến (Design by Contract)**:
   Trong lập trình, `assert all(a[i] <= a[i+1] for i in range(n-1))` dịch thẳng công thức hậu điều kiện $\forall i \in [0, n-2],\; a[i] \le a[i+1]$ của thuật toán sắp xếp thành mã kiểm chứng tự động.

4. **Logic 3 giá trị (`TRUE`, `FALSE`, `UNKNOWN`) với `NULL` trong SQL**:
   Một khác biệt thực tế sống còn: trong SQL, so sánh với `NULL` trả về `UNKNOWN`, nên `NOT IN (SELECT ...)` sẽ trả về **tập rỗng** nếu truy vấn con chứa dù chỉ 1 giá trị `NULL`—đó là lý do kỹ sư CSDL luôn ưu tiên `NOT EXISTS`.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Dịch** yêu cầu nghiệp vụ có "mọi" hoặc "tồn tại" sang công thức logic vị từ và sang mã SQL/Python tương đương.
- **Viết** assertion, validator và schema (Pydantic/Zod) như hiện thực trực tiếp của vị từ.
- **Phân biệt** quy tắc phủ định lượng từ ($$\lnot \forall$$ ↔ $$\exists \lnot$$) khi đọc `NOT EXISTS` và các điều kiện lồng nhau.
- **Mô hình hóa** các ràng buộc cơ sở dữ liệu (`UNIQUE`, `FOREIGN KEY`, `CHECK`) bằng $$\forall$$ và $$\exists$$ trên miền bản ghi.
- **Nhận biết** sự khác nhau giữa kiểm thử một số mẫu và đặc tả trên toàn miền.


**Từ khóa**: logic vị từ (predicate logic), lượng từ (quantifier), đặc tả (specification), assertion, schema validation, truy vấn quan hệ (relational query).
</div>


---

## Phần 1: Từ yêu cầu tiếng Việt đến công thức

### Mẫu dịch thường gặp

| Câu nghiệp vụ | Logic vị từ (miền $$D$$) |
|---|---|
| Mọi sinh viên đều đã đăng ký ít nhất một học phần | $$\forall s \in D_{student},\ \exists c \in D_{course},\ Enrolled(s,c)$$ |
| Có ít nhất một máy chủ còn hoạt động | $$\exists h \in D_{host},\ Healthy(h)$$ |
| Không tồn tại hai email trùng nhau | $$\lnot \exists u_1, u_2 \in D_{user},\ (u_1 \neq u_2 \land SameEmail(u_1,u_2))$$ |
| Mọi đơn hàng đều có đúng một người mua | $$\forall o \in D_{order},\ \exists! u \in D_{user},\ Buyer(o,u)$$ |

<div class="textbook-example" markdown="1">
**Ví dụ**: "Mọi giao dịch phải được xác thực trước khi xử lý."

<div class="textbook-equation" markdown="1">
$$\forall t \in Transactions,\ Processed(t) \limpl Verified(t)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Diễn giải theo góc nhìn lập trình: *nếu* `processed(t)` đúng thì *bắt buộc* `verified(t)` đã đúng trước đó.

![Gottlob Frege — nền tảng logic vị từ hiện đại](/discrete-mathematics-for-computer-science-iuh/img/course/gottlob_frege.svg)

<p class="textbook-figure-caption" data-figure="2.16">Gottlob Frege — đặt nền móng cho logic vị từ (first-order logic); ngày nay cùng cấu trúc ∀/∃ xuất hiện trong SQL và mã kiểm tra dữ liệu.</p>
</div>

### Phủ định lượng từ — lỗi thường gặp nhất

Luật De Morgan cho lượng từ:

<div class="textbook-equation" markdown="1">
$$\lnot \forall x\, P(x) \equiv \exists x\, \lnot P(x)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$\lnot \exists x\, P(x) \equiv \forall x\, \lnot P(x)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Trong SQL**: phát biểu "Không có đơn hàng nào chưa thanh toán" ($$\neg\exists o,\, status(o) = \text{'unpaid'}$$, tương đương $$\forall o,\, status(o) \neq \text{'unpaid'}$$) được viết rõ ràng như sau:

```sql
-- ∀ order: NOT (status = 'unpaid')
-- tương đương NOT EXISTS (SELECT 1 FROM orders o WHERE o.status = 'unpaid')
SELECT COUNT(*) = 0 AS all_paid
FROM orders
WHERE status = 'unpaid';
```

<div class="content-box warning-box textbook-block" markdown="1">
**Cẩn thận**: $$\forall x \exists y$$ và $$\exists y \forall x$$ **không** tương đương. "Mỗi sinh viên có một cố vấn" khác với "Có một cố vấn cho mọi sinh viên". Đổi thứ tự lượng từ trong đặc tả sẽ làm thay đổi yêu cầu, kéo theo thiết kế API và lược đồ cơ sở dữ liệu cũng khác đi.
</div>

---

## Phần 2: Logic vị từ trong SQL

### `EXISTS` và `NOT EXISTS`

Biểu thức `EXISTS (subquery)` nhận giá trị đúng khi truy vấn con trả về **ít nhất một dòng** — tương ứng trực tiếp với lượng từ $$\exists$$.

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

### `FOREIGN KEY` và `UNIQUE` như vị từ toàn cục

```sql
CREATE TABLE enrollments (
    student_id INT REFERENCES students(id),
    course_id  INT REFERENCES courses(id),
    PRIMARY KEY (student_id, course_id)
);
```

- `REFERENCES students(id)`: mọi `student_id` trong `enrollments` phải tồn tại trong `students`, tức $$\forall e \in Enrollments,\ \exists s \in Students,\ e.student\_id = s.id$$.
- `PRIMARY KEY`: không tồn tại hai dòng trùng cùng cặp khóa — bảo đảm tính duy nhất.

![Truy vấn SQL — thể hiện ∃ và ∀ qua EXISTS, JOIN, ràng buộc](/discrete-mathematics-for-computer-science-iuh/img/course/sql_query.svg)

<p class="textbook-figure-caption" data-figure="2.17">Truy vấn SQL biểu diễn lượng từ qua EXISTS/NOT EXISTS và ràng buộc quan hệ — cùng ý tưởng với công thức ∀/∃ trên miền bản ghi.</p>
### `CHECK` — vị từ trên từng dòng

```sql
ALTER TABLE students
ADD CONSTRAINT gpa_range CHECK (gpa >= 0 AND gpa <= 4);
```

Ràng buộc này biểu diễn $$\forall s \in Students,\ 0 \le s.gpa \le 4$$ và được hệ quản trị cơ sở dữ liệu kiểm tra mỗi khi thực hiện `INSERT` hoặc `UPDATE`.

---

### Khung giải thích (nên đọc chậm): Chuyển hóa câu hỏi "Sinh viên học ĐỦ mọi môn bắt buộc" từ Logic Vị từ sang SQL và chạy tay trên bảng mẫu

Cho 2 bảng nhỏ:
- `Required(cid)`: `{ 'CS101', 'CS102' }`
- `Enrolled(sid, cid)`: `{ ('An', 'CS101'), ('An', 'CS102'), ('Bình', 'CS101') }`

**Bước 1 — Viết bằng Logic Vị từ**:
Tìm sinh viên $s$ thỏa $\forall c \in \text{Required},\; \text{Enrolled}(s, c)$.

**Bước 2 — Biến đổi bằng De Morgan để khử $\forall$**:
$$\forall c \in \text{Required},\; \text{Enrolled}(s, c) \;\equiv\; \neg \exists c \in \text{Required},\; \neg \text{Enrolled}(s, c).$$
*(Đọc thành lời: "Không tồn tại môn bắt buộc $c$ nào mà sinh viên $s$ chưa đăng ký!")*

**Bước 3 — Dịch thẳng sang SQL**:
```sql
SELECT s.sid
FROM Students s
WHERE NOT EXISTS (
    SELECT 1 FROM Required r
    WHERE NOT EXISTS (
        SELECT 1 FROM Enrolled e
        WHERE e.sid = s.sid AND e.cid = r.cid
    )
);
```

**Bước 4 — Chạy tay trên từng sinh viên**:
- Với **`An`**: Môn `CS101` có trong `Enrolled` (subquery trong = `True` → `NOT EXISTS` trong = `False`); môn `CS102` cũng có (`False`). Vậy tập các môn *bị thiếu* của An là **rỗng $\emptyset$** → `NOT EXISTS` ngoài trả về **`True` → Chọn `An`!**
- Với **`Bình`**: Môn `CS102` không có trong `Enrolled` → tập các môn *bị thiếu* của Bình là `{'CS102'}` (khác rỗng!) → `NOT EXISTS` ngoài trả về **`False` → Loại `Bình`!**

## Phần 3: Assertion và schema trong mã nguồn

### `assert` — hợp đồng kiểm tra tại thời điểm chạy

```python
def transfer(from_id: int, to_id: int, amount: float, balance: dict[int, float]) -> None:
    assert amount > 0, "∀ giao dịch hợp lệ: amount > 0"
    assert from_id in balance and balance[from_id] >= amount
    balance[from_id] -= amount
    balance[to_id] = balance.get(to_id, 0) + amount
```

`assert` không thay thế việc kiểm tra dữ liệu đầu vào từ phía người dùng, nhưng giúp bảo vệ **bất biến (invariant)** nội bộ — những điều kiện phải luôn đúng ở mọi trạng thái hợp lệ của chương trình.

### Pydantic / Zod — vị từ trên kiểu dữ liệu

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

Mỗi ràng buộc như `.positive()`, `.min(1)` là một vị từ một biến $$P(x)$$ phải thỏa mãn trước khi đối tượng được chấp nhận.

### Design by Contract (DbC)

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

Tiền điều kiện (precondition), hậu điều kiện (postcondition) và bất biến (invariant) là ba lớp vị từ bao quanh một hàm — nền tảng của ngôn ngữ Eiffel và tinh thần của `debug_assert!` trong Rust hay `require`/`check` trong Kotlin.

<div class="content-box insight-box textbook-block" markdown="1">
**Nhận xét**: Kiểm thử (test) chỉ kiểm tra trên *một số* đầu vào cụ thể, còn đặc tả $$\forall/\exists$$ phát biểu cho *toàn bộ* miền giá trị. Validation schema là điểm giao thực dụng: chỉ cần vài dòng mã để mã hóa điều kiện $$\forall$$ áp dụng cho mọi dữ liệu yêu cầu (request body).
</div>

---

## Phần 4: Ứng dụng nâng cao

### Kiểm chứng và SMT/SAT

Với các hệ thống đòi hỏi độ tin cậy cao (hàng không, thanh toán, nhân hệ điều hành), kỹ sư sử dụng **model checker** hoặc **SMT solver** để hỏi: "Có tồn tại trạng thái nào vi phạm bất biến không?" — tức tìm một phản ví dụ theo lượng từ $$\exists$$. Nếu bộ giải trả về `unsat`, ta có chứng cứ rằng mọi luồng thực thi trong mô hình đều thỏa mãn đặc tả.

### Policy as code

```python
def can_refund(order, user) -> bool:
    # ∀ refund: user là owner HOẶC user là admin
    return order.user_id == user.id or user.role == "admin"
```

Các hệ quy tắc (rule engine), OPA (Open Policy Agent) và chính sách IAM dạng JSON đều dựa trên cấu trúc logic vị từ: biến (chủ thể, tài nguyên), vị từ (`is_owner`, `has_role`) và lượng từ trên tập hợp (`any`, `all`).

## Công cụ tương tác

<div data-demo="nested-quantifier-grid"></div>

<script src="{{ '/public/js/nested-quantifier-grid.js' | relative_url }}"></script>
---

## Bài tập thực hành

### Bài tập 1: Dịch sang logic vị từ

Viết công thức logic vị từ cho câu: "Mọi khóa học đều có ít nhất một giảng viên phụ trách."

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$\forall c \in Courses,\ \exists t \in Teachers,\ Teaches(t, c)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2: SQL với EXISTS

Viết truy vấn trả về `id` và `title` của các khóa học **chưa có** sinh viên nào đăng ký, cho hai bảng `courses(id, title)` và `enrollments(student_id, course_id)`.

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

Tương đương với $$\forall s,\ \lnot Enrolled(s, c)$$ cho từng khóa học $$c$$ được chọn.

</details>

### Bài tập 3: Phủ định lượng từ

Câu "Không phải mọi sinh viên đều đạt điểm ≥ 5" tương đương với công thức nào sau đây?

(a) $$\forall s,\ Score(s) < 5$$

(b) $$\exists s,\ Score(s) < 5$$

(c) $$\lnot \exists s,\ Score(s) \ge 5$$

<details>
<summary>Đáp án</summary>

**(b)**. Theo luật De Morgan cho lượng từ: $$\lnot \forall s,\ Score(s) \ge 5 \equiv \exists s,\ \lnot(Score(s) \ge 5) \equiv \exists s,\ Score(s) < 5$$.

Phương án (a) sai vì khẳng định *mọi* sinh viên đều dưới 5; phương án (c) sai vì phủ định hoàn toàn việc có sinh viên đạt ≥ 5.

</details>

### Bài tập 4: Pydantic validator

Bổ sung validator bảo đảm `end_date >= start_date` cho lớp sau:

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

Vị từ tương ứng: $$\forall booking,\ booking.end\_date \ge booking.start\_date$$.

</details>

### Bài tập 5: Thứ tự lượng từ

Phân biệt ý nghĩa của hai công thức sau:

1. $$\forall s \in Students,\ \exists m \in Mentors,\ Assigned(s,m)$$
2. $$\exists m \in Mentors,\ \forall s \in Students,\ Assigned(s,m)$$

<details>
<summary>Đáp án</summary>

1. Mỗi sinh viên đều có một cố vấn (cố vấn có thể khác nhau giữa các sinh viên).
2. Có một cố vấn chung phụ trách tất cả sinh viên — phát biểu mạnh hơn và ít gặp hơn trong thực tế.

</details>

### Bài tập 6: Invariant tài khoản

Viết `assert` hoặc `if`/`raise` để bảo vệ bất biến: tổng số dư của tất cả các tài khoản không thay đổi sau khi gọi `transfer`.

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

Viết schema Zod cho đối tượng người dùng gồm `email` hợp lệ và `age` là số nguyên trong đoạn từ 18 đến 120.

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

### Bài tập 8: Từ đặc tả đến kiểm thử

Cho vị từ $$\forall x \in \mathbb{Z},\ x^2 \ge 0$$. Đề xuất một hàm kiểm thử Python và giải thích vì sao chỉ chạy kiểm thử không đủ để chứng minh mệnh đề với $$\forall$$.

<details>
<summary>Đáp án</summary>

```python
def test_square_non_negative():
    for x in [-3, 0, 7, 100]:
        assert x * x >= 0
```

Kiểm thử chỉ đánh giá được trên một số hữu hạn giá trị, trong khi $$\forall$$ khẳng định trên tập vô hạn các số nguyên. Để khẳng định cho toàn miền, cần chứng minh toán học (đại số hoặc quy nạp) hoặc kiểm chứng hình thức; vì vậy kiểm thử và đặc tả luôn bổ sung cho nhau.

</details>


## Xem thêm / Video gợi ý

- [Quantifiers and Nested Quantifiers](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — Trefor Bazett (Clear examples with predicates)
- [Predicate Logic — ∀ and ∃](https://www.youtube.com/watch?v=8l7L9v0p0Q) — TrevTutor (Discrete Math playlist)

## Tóm tắt

- **$$\forall$$ / $$\exists$$**: nền tảng của các yêu cầu "mọi" và "tồn tại", ánh xạ trực tiếp sang SQL (`EXISTS`, ràng buộc bảng) và validation schema.
- **Phủ định lượng từ**: khi đọc `NOT EXISTS` cần áp dụng luật De Morgan và tránh nhầm thứ tự lượng từ lồng nhau.
- **Ràng buộc cơ sở dữ liệu**: `FOREIGN KEY`, `UNIQUE`, `CHECK` thực chất là các vị từ trên miền bản ghi.
- **Trong mã nguồn**: `assert`, Pydantic/Zod và Design by Contract là hiện thực của tiền điều kiện, hậu điều kiện và bất biến.
- **Kiểm thử và đặc tả**: kiểm thử kiểm tra trên mẫu cụ thể, còn $$\forall/\exists$$ mô tả toàn miền — hai lớp bảo đảm bổ trợ cho nhau.

Trong các chương tiếp theo, chúng ta sẽ tiếp tục áp dụng cách tiếp cận phát biểu chính xác rồi suy luận khi học về chứng minh, tập hợp và quan hệ.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=76v3gRns28U">Basics of Relational Algebra</a> — Neso Academy, tiếng Anh. Giới thiệu đại số quan hệ — cơ sở lý thuyết của `SELECT` và các điều kiện lọc.
- <a href="https://www.youtube.com/watch?v=gyoqX0W-NH4">PREDICATE LOGIC and QUANTIFIER NEGATION - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Củng cố kiến thức vị từ và lượng từ đứng sau `assert` và `WHERE EXISTS`.
- <a href="https://www.youtube.com/watch?v=lCcBxgFWEG4">Relational Algebra Operations Explained | SQL for Beginners</a> — CodeLucky, tiếng Anh. Giải thích các phép chọn, chiếu, kết nối tương ứng với điều kiện trên bảng dữ liệu.
