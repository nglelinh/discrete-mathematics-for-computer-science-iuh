---
layout: post
title: "Hàm số: Từ Turing đến Học máy"
categories: chapter06
date: 2021-01-01
order: 4
required: false
lang: en
---

Mỗi lần bạn gọi `user.get_profile(user_id)` hay viết `orders.map(o => o.total)`, bạn đang dùng cùng một ý tưởng toán học: **mỗi đầu vào hợp lệ được gắn với đúng một đầu ra**. Nghe quen, nhưng trong khoa học máy tính, khái niệm hàm mở rộng thành cả một cách tổ chức phần mềm.

```python
def hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()

def predict_spam(subject: str, body: str) -> bool:
    features = extract_features(subject, body)
    return model.predict([features])[0] == "spam"
```

Hai hàm trên trông khác nhau — một cái bảo mật, một cái học máy — nhưng cùng tuân một hợp đồng: đầu vào rõ ràng, đầu ra xác định, có thể kiểm thử độc lập. Đó là lý do **tư duy hàm** (function thinking) xuất hiện khắp nơi: lambda calculus, lập trình hàm, thiết kế API, hàm băm mật mã, và mô hình dự đoán.

Từ Church và Turing đến `map`/`filter`/`reduce` trên Python và JavaScript, bài này nối lý thuyết hàm số (Chương 6) với cách kỹ sư viết code hàng ngày.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Giải thích** mối liên hệ giữa hàm toán học, hàm tính toán được, và hàm trong ngôn ngữ lập trình.
- **Viết** và **ghép** hàm bằng `map`, `filter`, `reduce`, closure, và composition.
- **Phân biệt** hàm thuần (pure) và hàm có tác dụng phụ (side effect), và biết khi nào nên tách chúng.
- **Mô hình hóa** API endpoint, pipeline dữ liệu, và mô hình ML như các hàm $$f: X \to Y$$ có hợp đồng rõ ràng.
- **Áp dụng** tính chất đơn ánh/toàn ánh khi thiết kế hash function, khóa chính, và hàm đảo ngược (decode, undo).

**Từ khóa**: hàm tính toán được (computable function), lập trình hàm (functional programming), hàm bậc cao (higher-order function), closure, hàm thuần (pure function), hàm băm (hash function), hợp đồng hàm (function contract).

---

## Phần 1: Lịch sử — từ hàm toán học đến hàm tính toán

### 1.1. Hàm trước thời máy tính

Trong toán học cổ điển,
hàm giúp mô tả sự phụ thuộc:
đầu vào thay đổi,
đầu ra thay đổi theo quy luật.

Ví dụ,
$f(x)=x^2$ là cách nén vô số cặp giá trị thành một công thức ngắn.
Đây là sức mạnh lớn đầu tiên của hàm:
biến quy luật thành đối tượng có thể thao tác.

### 1.2. Church, lambda calculus, và khái niệm tính toán

Khi khoa học máy tính chưa tồn tại như một ngành độc lập,
Alonzo Church đã dùng lambda calculus để nghiên cứu computation bằng ngôn ngữ của hàm.

Ý tưởng rất táo bạo:
ta có thể biểu diễn việc tính toán như áp dụng hàm lên đối số,
rồi rút gọn biểu thức theo quy tắc chính xác.

Lambda calculus không phải ngôn ngữ lập trình thực dụng đầu tiên,
nhưng nó ảnh hưởng sâu lên Haskell,
ML,
Scala,
F#,
và nhiều ngôn ngữ hiện đại.

### 1.3. Turing và mô hình cơ học của tính toán

Alan Turing tiếp cận vấn đề từ góc khác:
thay vì bắt đầu bằng hàm trừu tượng,
ông mô hình hóa một cỗ máy thao tác ký hiệu trên băng.

Church và Turing đi hai đường,
nhưng gặp nhau ở cùng kết luận:
có một khái niệm sâu về “tính được”.

Trong đó,
hàm tính toán được (computable function)
trở thành đối tượng cốt lõi.

![Alan Turing — nền tảng tính toán](/discrete-mathematics-for-computer-science-iuh/img/course/Alan_Turing_Aged_16.jpg)

*Hình 6.19: Alan Turing và Alonzo Church (lambda calculus) đặt "hàm tính toán được" làm trung tâm của khoa học máy tính.*

---

## Phần 2: Functional programming — khi chương trình được xây từ hàm

### 2.1. Khai báo điều muốn làm thay vì điều khiển từng bước

Functional programming đặt hàm ở trung tâm thiết kế chương trình.
Thay vì tập trung vào biến đổi trạng thái,
nó khuyến khích:

- pure functions,
- immutability,
- composition,
- higher-order functions.

Ý tưởng này rất hấp dẫn,
vì nó làm reasoning về chương trình dễ hơn trong nhiều tình huống.

### 2.2. `map`, `filter`, `reduce`

Toán học: nếu $$f: A \to B$$ và $$S \subseteq A$$, ta có thể nói $$f(S) = \{f(x) \mid x \in S\}$$. Trong lập trình, đó chính là `map`.

**Python**:

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# map: áp dụng f lên từng phần tử
squares = list(map(lambda x: x * x, nums))          # [1, 4, 9, 16, 25]

# filter: giữ phần tử thỏa predicate (hàm trả về bool)
evens = list(filter(lambda x: x % 2 == 0, nums))   # [2, 4]

# reduce: gộp tập thành một giá trị bằng hàm nhị phân
product = reduce(lambda acc, x: acc * x, nums, 1)  # 120

# List comprehension — cú pháp gọn, cùng ý tưởng map/filter
squares_lc = [x * x for x in nums if x % 2 == 1]   # [1, 9, 25]
```

**JavaScript** (rất phổ biến trong frontend):

```javascript
const orders = [
  { id: 1, total: 120, status: "paid" },
  { id: 2, total: 80,  status: "pending" },
];

const paidTotals = orders
  .filter(o => o.status === "paid")
  .map(o => o.total);

const revenue = paidTotals.reduce((sum, t) => sum + t, 0);  // 120
```

Mỗi thao tác là cách áp dụng hàm lên tập dữ liệu. Ta mô tả **điều muốn biến đổi**, không mô tả từng bước lặp tay — đúng tinh thần declarative của lập trình hàm.

![Lập trình hàm — map, filter, reduce](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

*Hình 6.20: map, filter, reduce áp dụng hàm lên tập dữ liệu — tinh thần functional programming.*

### 2.3. Composition và tái sử dụng

Nếu $$f: A \to B$$ và $$g: B \to C$$, ta có hàm hợp $$(g \circ f)(x) = g(f(x))$$. Trong code, đó là pipeline — output của hàm này là input của hàm kế tiếp.

```python
def parse_csv(raw: str) -> list[dict]:
    ...

def validate_rows(rows: list[dict]) -> list[dict]:
    return [r for r in rows if r.get("email") and "@" in r["email"]]

def normalize(rows: list[dict]) -> list[dict]:
    return [{**r, "email": r["email"].strip().lower()} for r in rows]

def to_json(rows: list[dict]) -> str:
    import json
    return json.dumps(rows, ensure_ascii=False)

# Ghép hàm: parse → validate → normalize → serialize
def process_upload(raw: str) -> str:
    return to_json(normalize(validate_rows(parse_csv(raw))))
```

Trong data engineering và backend, pipeline thường gồm: **parse → clean → validate → transform → aggregate**. Mỗi bước là một hàm nhỏ, dễ test riêng, dễ thay thế.

<div class="content-box insight-box" markdown="1">
**Mẹo thiết kế**: Nếu một hàm vừa đọc file, vừa parse, vừa validate, vừa ghi database — nó không còn là "một hàm" theo nghĩa dễ reason. Tách thành chuỗi hàm nhỏ; mỗi hàm một trách nhiệm (single responsibility).
</div>

### 2.4. Vì sao dân công nghiệp vẫn quan tâm functional style

Ngay cả khi không dùng Haskell,
nhiều hệ thống production vẫn mượn tinh thần functional vì:

- dễ test,
- giảm side effects,
- reasoning tốt hơn,
- hợp với concurrency,
- composition linh hoạt.

Điều đó cho thấy khái niệm hàm không chỉ sống trong giáo trình.
Nó ảnh hưởng trực tiếp đến architecture decisions.

### 2.5. Hàm bậc cao (higher-order functions)

**Định nghĩa**: Hàm bậc cao là hàm nhận hàm khác làm tham số, hoặc trả về hàm.

```python
def apply_twice(f, x):
    """Hàm bậc cao: nhận hàm f và áp dụng hai lần."""
    return f(f(x))

def make_multiplier(k):
    """Factory: trả về hàm nhân với k."""
    def multiply(x):
        return k * x
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

`map`, `filter`, `reduce` đều là hàm bậc cao. Decorator trong Python cũng vậy — bọc một hàm bằng hàm khác để thêm logging, cache, hoặc kiểm tra quyền.

### 2.6. Closure và decorator

**Closure**: hàm con "nhớ" biến của hàm cha ngay cả khi hàm cha đã kết thúc.

```python
def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

auth_log = make_logger("AUTH")
auth_log("User logged in")   # [AUTH] User logged in
```

**Decorator** — pattern rất phổ biến trong web framework:

```python
import time

def timed(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timed
def fetch_users():
    time.sleep(0.1)
    return ["An", "Bình"]

fetch_users()  # fetch_users took 0.1001s
```

Decorator biến hàm gốc thành hàm mới $$(g \circ f)$$: vẫn cùng input/output, nhưng thêm hành vi phụ (đo thời gian, ghi log).

### 2.7. Hàm thuần (pure) vs hàm có tác dụng phụ

| | **Pure function** | **Impure function** |
|:---|:---|:---|
| Cùng input | Luôn cùng output | Có thể khác output |
| Side effect | Không đọc/ghi state bên ngoài | Đọc DB, ghi file, gọi API |
| Kiểm thử | Dễ — chỉ cần assert input/output | Khó — cần mock môi trường |
| Song song hóa | An toàn hơn | Cần đồng bộ, lock |

```python
# Pure — chỉ phụ thuộc tham số
def discount(price: float, rate: float) -> float:
    return price * (1 - rate)

# Impure — phụ thuộc thời gian và state toàn cục
import datetime
visit_count = 0

def track_visit(user_id: str) -> str:
    global visit_count
    visit_count += 1
    return f"{user_id}@{datetime.datetime.now().isoformat()}"
```

<div class="content-box warning-box" markdown="1">
**Thực hành tốt**: Giữ **core logic** dưới dạng hàm thuần; đẩy I/O (database, HTTP, file) ra lớp ngoài. Ví dụ: `calculate_tax(amount, rules)` thuần, `save_invoice(invoice)` impure — dễ unit test phần tính thuế mà không cần database thật.
</div>

### 2.8. Type hints và hợp đồng hàm

Type hints không thay đổi hành vi runtime, nhưng làm **hợp đồng hàm** (function contract) rõ ràng — giống khai báo domain/codomain:

```python
from typing import Callable

def pipeline(
    data: list[str],
    transform: Callable[[str], str],
    predicate: Callable[[str], bool],
) -> list[str]:
    return [transform(x) for x in data if predicate(x)]

result = pipeline(
    ["  An  ", "  ", "Bình"],
    transform=str.strip,
    predicate=lambda s: len(s) > 0,
)
# ['An', 'Bình']
```

Trong TypeScript, hợp đồng còn chặt hơn:

```typescript
type User = { id: number; email: string };

function getUserById(id: number): User | null {
  // domain: number, codomain: User | null
  ...
}
```

Khi domain/codomain mơ hồ (`any`, `object`, `dict` không rõ key), bug thường xuất hiện ở ranh giới tích hợp — đúng chỗ mà định nghĩa hàm toán học yêu cầu "mỗi phần tử domain có đúng một ảnh".

---

## Phần 3: Machine learning models như các hàm dự đoán

### 3.1. Một mô hình học máy có thể nhìn như hàm

Ở mức trừu tượng,
model học máy là hàm:

$$
f: X \to Y
$$

Trong đó:

- $X$ là không gian đầu vào,
- $Y$ là không gian đầu ra hoặc phân phối xác suất.

Ví dụ,
mô hình nhận ảnh và trả nhãn,
nhận văn bản và trả sentiment,
nhận dữ liệu khách hàng và trả xác suất rời bỏ.

### 3.2. Input-to-prediction là tư duy hàm số ở quy mô mới

**Mô hình tuyến tính đơn giản** (dễ đọc, dễ test):

```python
def predict_credit_risk(features: dict) -> bool:
    score = (
        0.3 * features["debt_ratio"]
        + 0.5 * features["late_payments"]
        - 0.2 * features["income_years"]
    )
    return score > 0.7
```

**Scikit-learn** — cùng ý tưởng $$f: \mathbb{R}^n \to \{0,1\}$$, nhưng `fit` học trọng số từ dữ liệu:

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

X_train = np.array([[0.8, 2], [0.2, 0], [0.9, 5]])  # debt_ratio, late_payments
y_train = np.array([1, 0, 1])                          # 1 = risky

model = LogisticRegression()
model.fit(X_train, y_train)

# predict là hàm được học — cùng input → cùng output (sau khi train xong)
def predict_risk(features: list[float]) -> int:
    return int(model.predict([features])[0])

predict_risk([0.85, 3])  # 1
```

**Inference endpoint** (FastAPI) — đóng gói hàm cho production:

```python
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class CreditFeatures(BaseModel):
    debt_ratio: float
    late_payments: int

@app.post("/predict")
def predict_endpoint(body: CreditFeatures) -> dict:
    risky = predict_risk([body.debt_ratio, body.late_payments])
    return {"risky": bool(risky)}
```

Mô hình thật có hàng triệu tham số, nhưng **hợp đồng không đổi**: vector đặc trưng vào, nhãn hoặc xác suất ra. Hàm `forward` của mạng nơ-ron cũng là $$f_\theta: X \to Y$$ với $$\theta$$ cố định sau khi train.

### 3.3. Loss function, activation function, objective function

Thế giới ML đầy các hàm:

- loss functions,
- activation functions,
- kernel functions,
- scoring functions,
- objective functions.

Nói cách khác,
ngay cả khi mô hình rất hiện đại,
ngôn ngữ cơ bản để mô tả nó vẫn là ngôn ngữ của hàm.

### 3.4. Training loop — hàm loss và hàm cập nhật

Huấn luyện ML là quá trình tìm $$\theta$$ sao cho hàm dự đoán $$f_\theta$$ khớp dữ liệu. **Loss function** $$L(\theta)$$ đo sai số; **optimizer** là hàm cập nhật tham số:

```python
def mse_loss(y_true: float, y_pred: float) -> float:
    return (y_true - y_pred) ** 2

def train_step(weights: list[float], x: float, y: float, lr: float = 0.01):
    """Một bước gradient descent đơn giản (1 feature)."""
    y_pred = weights[0] * x + weights[1]
    error = y_pred - y
    # Cập nhật hàm f bằng cách chỉnh weights
    weights[0] -= lr * 2 * error * x
    weights[1] -= lr * 2 * error
    return mse_loss(y, y_pred)

w = [0.0, 0.0]
for x, y in [(1, 2), (2, 4), (3, 6)]:
    loss = train_step(w, x, y)
```

Ở đây có **ba lớp hàm**: $$f_\theta$$ (dự đoán), $$L$$ (đo lỗi), và bước cập nhật $$\theta \leftarrow \theta - \eta \nabla L$$. Tách rõ từng hàm giúp debug và thay optimizer mà không đổi mô hình.

![Mô hình học máy như hàm ánh xạ](/discrete-mathematics-for-computer-science-iuh/img/course/Neural_network.svg)

*Hình 6.21: Mô hình ML là hàm $$f: X \to Y$$ được học từ dữ liệu — từ đặc trưng đầu vào đến dự đoán đầu ra.*

---

## Phần 4: Cryptographic hash functions

### 4.1. Hash function không phải hàm ngẫu nhiên

Cryptographic hash function nhận input bất kỳ độ dài
và trả digest kích thước cố định.

Ví dụ:

```python
import hashlib

message = b"discrete mathematics"
digest = hashlib.sha256(message).hexdigest()
print(digest)
```

Đây là hàm theo nghĩa rất chính xác: cùng input, cùng output.

**Lưu mật khẩu** — không lưu plaintext, chỉ lưu ảnh của hàm băm:

```python
import hashlib
import os

def hash_password(plain: str, salt: bytes | None = None) -> tuple[str, str]:
    if salt is None:
        salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", plain.encode(), salt, 100_000)
    return salt.hex(), digest.hex()

def verify_password(plain: str, salt_hex: str, digest_hex: str) -> bool:
    salt = bytes.fromhex(salt_hex)
    _, new_digest = hash_password(plain, salt)
    return new_digest == digest_hex

salt, stored = hash_password("mySecret123")
assert verify_password("mySecret123", salt, stored)
assert not verify_password("wrong", salt, stored)
```

`verify_password` là hàm **boolean** $$f: \text{String} \times \text{Salt} \times \text{Digest} \to \{\text{True}, \text{False}\}$$ — không đơn ánh (nhiều mật khẩu sai → `False`), nhưng vẫn xác định.

### 4.2. Nhưng nó cần nhiều tính chất đặc biệt

Một hash tốt cho bảo mật không chỉ “tính ra giá trị”.
Nó còn cần:

- khó đảo ngược,
- khó tìm collision,
- nhạy với thay đổi nhỏ ở input,
- phân bố output đều.

Đó là ví dụ đẹp cho thấy:
trong computing,
hàm không chỉ là ánh xạ.
Nó còn mang specification rất cụ thể.

![Hàm băm — toàn ánh nhưng không đơn ánh](/discrete-mathematics-for-computer-science-iuh/img/course/Surjection.svg)

*Hình 6.22: SHA-256 là hàm toàn ánh (mọi digest đều khả dĩ) nhưng không đơn ánh (domain vô hạn → collision không tránh khỏi).*

### 4.3. Ứng dụng của hash

Hash functions sống trong:

- lưu mật khẩu,
- kiểm tra tính toàn vẹn,
- chữ ký số,
- blockchain,
- content addressing,
- deduplication,
- distributed systems.

Chúng là ví dụ mạnh cho việc một định nghĩa toán học đơn giản
có thể trở thành thành phần hạ tầng cực quan trọng.

---

## Phần 5: API design như đặc tả hàm

### 5.1. Một API tốt giống một hàm tốt

Khi thiết kế API,
ta đang làm điều gần với định nghĩa hàm:

- input là gì,
- output là gì,
- preconditions ra sao,
- errors khi nào,
- side effects có không.

Ví dụ:

```python
from dataclasses import dataclass
from enum import Enum

class TransferError(Enum):
    INVALID_AMOUNT = "amount must be positive"
    INSUFFICIENT_FUNDS = "sender balance too low"
    SAME_ACCOUNT = "sender and receiver must differ"

@dataclass
class TransferResult:
    ok: bool
    transaction_id: str | None = None
    error: TransferError | None = None

def transfer_money(
    sender_id: int,
    receiver_id: int,
    amount: float,
    balances: dict[int, float],
) -> tuple[TransferResult, dict[int, float]]:
    """
    Pure core với state truyền vào — dễ test, không đụng DB trực tiếp.
    Trả về (kết quả, balances mới).
    """
    if amount <= 0:
        return TransferResult(False, error=TransferError.INVALID_AMOUNT), balances
    if sender_id == receiver_id:
        return TransferResult(False, error=TransferError.SAME_ACCOUNT), balances
    if balances.get(sender_id, 0) < amount:
        return TransferResult(False, error=TransferError.INSUFFICIENT_FUNDS), balances

    new_balances = balances.copy()
    new_balances[sender_id] -= amount
    new_balances[receiver_id] = new_balances.get(receiver_id, 0) + amount
    return TransferResult(True, transaction_id="tx-001"), new_balances
```

Hàm này tưởng đơn giản, nhưng specification cần rõ:

- `amount` phải dương (domain constraint),
- sender phải đủ tiền (precondition),
- không chuyển cho chính mình,
- trả về state mới thay vì mutate global (dễ test, dễ undo).

**REST API** cũng là hàm: `POST /transfer` nhận JSON body, trả status code + JSON. OpenAPI/Swagger chính là tài liệu hóa domain/codomain của endpoint.

### 5.2. Hàm mơ hồ tạo hệ thống mơ hồ

Rất nhiều bug sản phẩm không đến từ thuật toán khó.
Chúng đến từ specification mờ:

- input nào hợp lệ,
- null được hiểu ra sao,
- timezone xử lý thế nào,
- idempotency có được đảm bảo không.

Nhìn API như hàm được đặc tả tốt
giúp kỹ sư viết code chính xác hơn,
review tốt hơn,
và tài liệu hóa rõ hơn.

![API design — đặc tả hàm rõ ràng](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

*Hình 6.23: API tốt giống hàm tốt — input, output, preconditions và errors phải được đặc tả không mơ hồ.*

### 5.3. Pure interface, messy world

Dĩ nhiên,
phần mềm thật có side effects.
Nhưng chính vì thế,
việc giữ phần interface càng “giống hàm” càng tốt
lại càng có giá trị.

Nó giảm bất ngờ,
giảm lỗi tích hợp,
và làm reasoning dễ hơn cho cả người viết lẫn người dùng API.

---

## Phần 6: Tương lai — function thinking trong hệ thống phức tạp

Khi hệ thống lớn lên,
tư duy hàm càng hữu ích:

- serverless functions,
- data pipelines,
- ML inference endpoints,
- reactive programming,
- deterministic transforms,
- verified interfaces.

Ngay cả trong distributed systems đầy side effects,
kỹ sư giỏi vẫn thường cố đẩy nhiều phần nhất có thể về dạng “hàm sạch, dễ reason”.

**Serverless (AWS Lambda, Cloud Functions)** — mỗi handler là một hàm:

```python
import json

def lambda_handler(event: dict, context) -> dict:
    """
    event: input (domain)
    return: output (codomain) — thường là HTTP response
    """
    user_id = event.get("pathParameters", {}).get("userId")
    if not user_id:
        return {"statusCode": 400, "body": '{"error": "missing userId"}'}

    user = get_user_pure(user_id)  # tách đọc DB ra layer riêng
    if user is None:
        return {"statusCode": 404, "body": '{"error": "not found"}'}

    return {"statusCode": 200, "body": json.dumps(user)}
```

**Callback và event handler** (JavaScript, GUI, game loop) cũng là hàm: `onClick`, `onMessage`, `setTimeout(fn, 1000)` — đều là $$f: \text{Event} \to \text{Action}$$.

![Hàm hợp trong hệ thống phân tán](/discrete-mathematics-for-computer-science-iuh/img/course/Example_for_a_composition_of_two_functions.svg)

*Hình 6.24: Serverless functions và data pipelines là chuỗi hàm hợp — mỗi bước ánh xạ input sang output xác định.*

---

## Kết luận

Hàm số không chỉ là chủ đề của đại số phổ thông.
Trong khoa học máy tính,
nó là cách ta hiểu computation,
tổ chức chương trình,
thiết kế API,
xây mô hình học máy,
và đảm bảo tính toàn vẹn dữ liệu.

Từ Church và Turing,
đến Haskell,
SHA-256,
và prediction services,
khái niệm hàm đã trở thành một trong những chiếc xương sống bền nhất của computing.

---

## Bài tập thực hành

### Bài tập 1: Hàm đệ quy

Viết hàm đệ quy tính $$f(n) = n!$$ và giải thích tại sao đây là hàm tính toán được theo Turing.

<details>
<summary>Đáp án</summary>

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)
```

Hàm này có thể được tính bằng máy Turing (có thuật toán hữu hạn).

</details>

### Bài tập 2: Hàm băm

Giải thích tại sao hàm băm SHA-256 là toàn ánh nhưng không đơn ánh trên thực tế.

<details>
<summary>Đáp án</summary>

Toàn ánh vì output là 256-bit (có $$2^{256}$$ giá trị). Không đơn ánh vì domain lớn hơn nhiều (các file có kích thước bất kỳ).

</details>

### Bài tập 3: Hàm trong ML

Trong mô hình học máy, hàm dự đoán $$f: \mathbb{R}^n \to \mathbb{R}$$ thường không phải song ánh. Tại sao?

<details>
<summary>Đáp án</summary>

Vì nhiều input khác nhau có thể cho cùng output (nhiều điểm dữ liệu có cùng nhãn hoặc giá trị dự đoán).

</details>

### Bài tập 4: Viết pipeline xử lý chuỗi

Cho danh sách email thô:

```python
raw = ["  AN@IUH.EDU.VN  ", "", "binh@iuh.edu.vn", "invalid"]
```

Viết hàm `process_emails(raw) -> list[str]` gồm ba bước (ba hàm con):

1. `strip_each` — bỏ khoảng trắng đầu cuối.
2. `drop_empty` — loại chuỗi rỗng.
3. `normalize_case` — chuyển về chữ thường.

Ghép bằng composition (gọi lần lượt hoặc dùng `map`/`filter`). Kết quả mong đợi: `["an@iuh.edu.vn", "binh@iuh.edu.vn", "invalid"]`.

<details>
<summary>Đáp án</summary>

```python
def strip_each(emails: list[str]) -> list[str]:
    return [e.strip() for e in emails]

def drop_empty(emails: list[str]) -> list[str]:
    return [e for e in emails if e]

def normalize_case(emails: list[str]) -> list[str]:
    return [e.lower() for e in emails]

def process_emails(raw: list[str]) -> list[str]:
    return normalize_case(drop_empty(strip_each(raw)))

assert process_emails(raw) == ["an@iuh.edu.vn", "binh@iuh.edu.vn", "invalid"]
```

</details>

### Bài tập 5: Pure vs impure

Phân loại các hàm sau là **pure** hay **impure**, giải thích ngắn:

```python
def add_tax(price, rate):
    return price * (1 + rate)

def get_current_user():
    return db.query("SELECT * FROM users WHERE id = session.user_id")

def random_id():
    import random
    return random.randint(1000, 9999)

def parse_int(s):
    return int(s.strip())
```

<details>
<summary>Đáp án</summary>

- `add_tax` — **pure**: chỉ phụ thuộc `price`, `rate`.
- `get_current_user` — **impure**: đọc DB và session (side effect / external state).
- `random_id` — **impure**: cùng "input" rỗng nhưng output khác nhau mỗi lần gọi.
- `parse_int` — **pure** với giả định `s` là chuỗi hợp lệ; ném exception nếu không parse được vẫn là deterministic với cùng `s`.

</details>

### Bài tập 6: Decorator kiểm tra tham số

Viết decorator `@require_positive` bọc hàm nhận số `amount`, ném `ValueError` nếu `amount <= 0`, ngược lại gọi hàm gốc.

```python
@require_positive
def withdraw(amount: float, balance: float) -> float:
    return balance - amount
```

<details>
<summary>Đáp án</summary>

```python
def require_positive(fn):
    def wrapper(amount, *args, **kwargs):
        if amount <= 0:
            raise ValueError("amount must be positive")
        return fn(amount, *args, **kwargs)
    return wrapper

@require_positive
def withdraw(amount: float, balance: float) -> float:
    return balance - amount

assert withdraw(50, 200) == 150
try:
    withdraw(-1, 200)
except ValueError:
    pass
else:
    raise AssertionError("expected ValueError")
```

</details>

### Bài tập 7: API như hàm

Endpoint `GET /users/{id}` trả user hoặc 404. Viết pseudo-code Python (hoặc FastAPI) mô tả:

- domain: `id` là số nguyên dương,
- codomain: `User` hoặc lỗi,
- precondition: `id` hợp lệ,
- postcondition: không expose mật khẩu trong response.

<details>
<summary>Đáp án</summary>

```python
@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict:
    if user_id <= 0:
        return {"status": 400, "body": "invalid id"}

    user = user_repo.find_by_id(user_id)  # impure layer
    if user is None:
        return {"status": 404, "body": "not found"}

    return {
        "status": 200,
        "body": {"id": user.id, "email": user.email},  # không trả password
    }
```

Domain: `user_id > 0`. Codomain: HTTP response + JSON an toàn. Tách `user_repo` giúp test handler với mock.

</details>

### Bài tập 8: `map`/`reduce` trong thống kê

Cho `scores = [7, 8, 5, 9, 6]`:

(a) Dùng `map` tính điểm sau khi cộng 10% điểm thưởng (làm tròn 1 chữ số thập phân).
(b) Dùng `reduce` tìm điểm cao nhất (không dùng `max()`).

<details>
<summary>Đáp án</summary>

```python
from functools import reduce

scores = [7, 8, 5, 9, 6]

bonus = list(map(lambda s: round(s * 1.1, 1), scores))
# [7.7, 8.8, 5.5, 9.9, 6.6]

highest = reduce(lambda a, b: a if a >= b else b, scores)
# 9
```

</details>

## Tóm tắt

- **Hàm trong lập trình**: mỗi hàm là hợp đồng domain → codomain; cùng input phải cho cùng output (trừ hàm impure có state bên ngoài).
- **Lập trình hàm**: `map`, `filter`, `reduce`, composition, closure, decorator — ghép hàm nhỏ thành pipeline dễ test.
- **Pure vs impure**: giữ logic tính toán thuần; tách I/O ra layer riêng.
- **ML**: `model.predict` là hàm $$f_\theta$$; training là tìm $$\theta$$ qua loss và optimizer.
- **Hash & API**: SHA-256 và REST endpoint đều cần đặc tả tính chất hàm (xác định, toàn ánh, preconditions) rõ ràng.
- **Tính chất toán**: đơn ánh, toàn ánh, song ánh và hàm nghịch đảo (xem bài 06_02, 06_03) giúp thiết kế khóa, undo, và giải mã chính xác.
