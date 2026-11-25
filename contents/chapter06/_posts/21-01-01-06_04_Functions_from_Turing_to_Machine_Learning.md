---

layout: post
title: "Hàm số: Từ Turing đến Học máy"
categories: chapter06
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Bài đọc mở rộng nối nền tảng lý thuyết hàm số với hàm tính toán được, lập trình hàm, hàm băm mật mã, thiết kế API và mô hình học máy."
---


Thập niên 1930 chứng kiến một cuộc hội tụ kỳ diệu trong lịch sử khoa học máy tính: Alonzo Church định nghĩa tính toán bằng phép gọi hàm thuần túy (*Lambda Calculus*), còn Alan Turing mô hình hóa nó bằng một cỗ máy băng giấy cơ học—và cả hai thế giới tưởng chừng đối lập ấy hóa ra lại tương đương nhau tuyệt đối. Từ nền móng đó, khái niệm **hàm số** đã tiến hóa xuyên suốt gần một thế kỷ để trở thành xương sống của lập trình hàm (`map`/`filter`/`reduce`), hàm băm mật mã SHA-256, thiết kế API và các mạng nơ-ron học sâu ngày nay.

Ở các mục trước, chúng ta đã xây dựng nền tảng lý thuyết về hàm số. Mục bổ sung này kết nối khái niệm hàm toán học với hàm tính toán được, lập trình hàm, hàm băm mật mã, thiết kế API và mô hình học máy.

Mỗi khi gọi `user.get_profile(user_id)` hay viết `orders.map(o => o.total)`, ta đều sử dụng cùng một hợp đồng: đầu vào rõ ràng, đầu ra xác định và có thể kiểm thử độc lập. Từ Church và Turing cho đến `map`/`filter`/`reduce` và các endpoint dự đoán trong học máy, khái niệm hàm luôn là một trong những nền tảng bền vững nhất của khoa học máy tính.

## Bản đồ kiến thức nền: Bốn chặng tiến hóa của Hàm số trong Khoa học Máy tính

1. **Từ hàm toán học đến Hàm tính toán được (Luận đề Church–Turing)**:
   Không phải mọi hàm toán học đều có thuật toán tính được (ví dụ bài toán dừng *Halting Problem*). Church và Turing đã vẽ ra ranh giới chính xác cho lớp các hàm mà máy tính có thể thực thi hữu hạn bước.

2. **Lập trình hàm (Functional Programming) — Hàm thuần khiết & Bậc cao**:
   **Hàm thuần (pure function)** luôn trả về cùng một kết quả cho cùng đầu vào và không gây tác dụng phụ (*side effect*). Khi kết hợp với hàm bậc cao (`map`, `filter`, `reduce`) và phép hợp (*composition*), mã nguồn trở nên ngắn gọn, dễ kiểm thử và an toàn khi chạy song song.

3. **Hàm băm mật mã (Cryptographic Hash) — Ánh xạ một chiều bất khả nghịch**:
   Hàm băm $H: \{0,1\}^* \to \{0,1\}^{256}$ cố tình phá vỡ tính song ánh (miền vào vô hạn, miền ra hữu hạn) nhưng đòi hỏi ba tường thành bảo mật: kháng tiền ảnh (không đảo ngược được), kháng tiền ảnh thứ hai và kháng va chạm.

4. **Học máy & Thiết kế API — Hàm tham số hóa $f_\theta(x)$ và Hợp đồng giao diện**:
   Mỗi mô hình AI thực chất là một hàm khổng lồ $f_\theta(x)$ nơi ta không tự viết tay công thức, mà dùng **hàm mất mát (loss)** và gradient descent để tự động tìm bộ tham số $\theta$ tối ưu; còn một API tốt chính là một đặc tả hàm chặt chẽ về miền vào, miền ra và mã lỗi.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** mối liên hệ giữa hàm toán học, hàm tính toán được và hàm trong ngôn ngữ lập trình.
- **Viết** và **ghép** hàm bằng `map`, `filter`, `reduce`, closure và composition.
- **Phân biệt** hàm thuần (pure) với hàm có tác dụng phụ (side effect), đồng thời biết cách tách biệt chúng.
- **Mô hình hóa** API endpoint, pipeline dữ liệu và mô hình học máy như các hàm $$f: X \to Y$$ có hợp đồng rõ ràng.
- **Áp dụng** tính chất đơn ánh, toàn ánh khi thiết kế hàm băm, khóa chính và các phép biến đổi khả nghịch (decode, undo).

**Từ khóa**: hàm tính toán được (computable function), lập trình hàm (functional programming), hàm bậc cao (higher-order function), closure, hàm thuần (pure function), hàm băm (hash function), hợp đồng hàm (function contract).
</div>

---

## Phần 1: Lịch sử — từ hàm toán học đến hàm tính toán

### Hàm trước thời máy tính

Trong toán học cổ điển, hàm số dùng để mô tả mối quan hệ phụ thuộc: khi đầu vào thay đổi, đầu ra thay đổi theo một quy luật xác định. Chẳng hạn, biểu thức $$f(x)=x^2$$ nén vô số cặp giá trị vào một công thức ngắn gọn. Đây là sức mạnh đầu tiên của hàm số: biến một quy luật thành một đối tượng toán học có thể thao tác trực tiếp.

### Church, lambda calculus và khái niệm tính toán

Khi khoa học máy tính chưa hình thành như một ngành độc lập, Alonzo Church đã sử dụng phép tính lambda (lambda calculus) để nghiên cứu quá trình tính toán bằng ngôn ngữ của hàm số. Ý tưởng cốt lõi là biểu diễn mọi phép tính thông qua việc áp dụng hàm lên đối số, rồi rút gọn biểu thức theo các quy tắc hình thức chính xác.

Dù không phải là ngôn ngữ lập trình thực dụng đầu tiên, lambda calculus đã ảnh hưởng sâu sắc đến Haskell, ML, Scala, F# và nhiều ngôn ngữ hiện đại khác.

### Turing và mô hình cơ học của tính toán

Alan Turing tiếp cận bài toán từ một hướng khác: thay vì bắt đầu bằng hàm trừu tượng, ông mô hình hóa một cỗ máy cơ học thao tác các ký hiệu trên băng nhớ. Dù đi theo hai con đường khác nhau, Church và Turing đều đi đến cùng một kết luận về khái niệm "tính toán được". Từ đó, **hàm tính toán được** (computable function) trở thành đối tượng trung tâm của khoa học máy tính lý thuyết.

![Alan Turing — nền tảng tính toán](/discrete-mathematics-for-computer-science-iuh/img/course/Alan_Turing_Aged_16.jpg)

<p class="textbook-figure-caption" data-figure="6.19">Alan Turing và Alonzo Church (lambda calculus) đặt "hàm tính toán được" làm trung tâm của khoa học máy tính.</p>
---

## Phần 2: Lập trình hàm — khi chương trình được xây từ hàm

### Khai báo điều muốn làm thay vì điều khiển từng bước

Lập trình hàm (functional programming) đặt hàm số ở vị trí trung tâm trong thiết kế chương trình. Thay vì xoay quanh việc thay đổi trạng thái từng bước, phong cách này khuyến khích:

- hàm thuần (pure functions),
- dữ liệu bất biến (immutability),
- phép hợp hàm (composition),
- hàm bậc cao (higher-order functions).

Cách tiếp cận này giúp việc lập luận về tính đúng đắn của chương trình trở nên rõ ràng và dễ kiểm soát hơn trong nhiều tình huống.

### `map`, `filter`, `reduce`

Trong toán học, nếu $$f: A \to B$$ và $$S \subseteq A$$, ta có tập ảnh $$f(S) = \{f(x) \mid x \in S\}$$. Trong lập trình, phép biến đổi này chính là `map`.

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

**JavaScript** (rất phổ biến trong phát triển giao diện):

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

Mỗi thao tác trên đều áp dụng một hàm lên tập dữ liệu. Ta mô tả **điều muốn biến đổi** thay vì viết tay từng bước lặp — đúng với tinh thần khai báo (declarative) của lập trình hàm.

![Lập trình hàm — map, filter, reduce](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

<p class="textbook-figure-caption" data-figure="6.20">map, filter, reduce áp dụng hàm lên tập dữ liệu — thể hiện tinh thần của lập trình hàm.</p>
### Composition và tái sử dụng

Nếu $$f: A \to B$$ và $$g: B \to C$$, ta có hàm hợp $$(g \circ f)(x) = g(f(x))$$. Trong mã nguồn, cấu trúc này tương ứng với một pipeline, nơi đầu ra của hàm trước trở thành đầu vào của hàm kế tiếp.

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

Trong kỹ thuật dữ liệu (data engineering) và phát triển backend, pipeline thường đi theo chuỗi **parse → clean → validate → transform → aggregate**. Mỗi bước là một hàm nhỏ, dễ kiểm thử riêng lẻ và dễ thay thế.

<div class="content-box insight-box textbook-block" markdown="1">
**Mẹo thiết kế**: Nếu một hàm vừa đọc tệp, vừa phân tích dữ liệu, vừa kiểm tra hợp lệ rồi ghi vào cơ sở dữ liệu, nó sẽ rất khó theo dõi và kiểm thử. Hãy tách thành chuỗi các hàm nhỏ, mỗi hàm đảm nhận một trách nhiệm duy nhất (single responsibility).
</div>

### Vì sao kỹ sư phần mềm vẫn áp dụng phong cách hàm

Ngay cả khi không lập trình bằng Haskell, nhiều hệ thống vận hành thực tế vẫn mượn các nguyên lý của lập trình hàm vì những lợi ích cụ thể:

- dễ viết kiểm thử đơn vị,
- giảm tác dụng phụ không mong muốn,
- dễ suy luận về hành vi chương trình,
- thuận lợi hơn khi xử lý đồng thời (concurrency),
- dễ ghép nối và tái sử dụng qua composition.

Điều này cho thấy khái niệm hàm không chỉ nằm trong giáo trình lý thuyết mà còn định hình trực tiếp cách thiết kế phần mềm.

### Hàm bậc cao (higher-order functions)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm bậc cao là hàm nhận hàm khác làm tham số, hoặc trả về một hàm làm kết quả.
</div>

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

`map`, `filter` và `reduce` đều là các hàm bậc cao. Decorator trong Python cũng hoạt động theo cơ chế tương tự: bọc một hàm bằng một hàm khác để bổ sung tính năng ghi log, lưu đệm (cache) hoặc kiểm tra quyền truy cập.

### Closure và decorator

**Closure** là hàm lồng bên trong vẫn "ghi nhớ" các biến thuộc phạm vi của hàm bao ngoài ngay cả sau khi hàm bao ngoài đã kết thúc.

```python
def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

auth_log = make_logger("AUTH")
auth_log("User logged in")   # [AUTH] User logged in
```

**Decorator** là mẫu thiết kế rất phổ biến trong các web framework:

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

Decorator biến hàm gốc thành một hàm mới dạng $$(g \circ f)$$: vẫn giữ nguyên đầu vào và đầu ra, nhưng bổ sung thêm hành vi phụ như đo thời gian chạy hay ghi nhật ký.

### Hàm thuần (pure) và hàm có tác dụng phụ (impure)

| | **Pure function** | **Impure function** |
|:---|:---|:---|
| Cùng input | Luôn trả về cùng output | Có thể trả về output khác nhau |
| Side effect | Không đọc/ghi trạng thái bên ngoài | Đọc cơ sở dữ liệu, ghi tệp, gọi API |
| Kiểm thử | Dễ — chỉ cần kiểm tra cặp input/output | Khó hơn — cần giả lập (mock) môi trường |
| Song song hóa | An toàn hơn | Cần đồng bộ hóa, khóa (lock) |

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

<div class="content-box warning-box textbook-block" markdown="1">
**Thực hành tốt**: Hãy giữ **logic cốt lõi** dưới dạng hàm thuần và đẩy các thao tác I/O (cơ sở dữ liệu, HTTP, hệ thống tệp) ra lớp ngoài. Ví dụ: tách `calculate_tax(amount, rules)` (thuần) khỏi `save_invoice(invoice)` (impure) giúp kiểm thử phần tính thuế mà không cần kết nối cơ sở dữ liệu thật.
</div>

### Type hints và hợp đồng hàm

Type hints không làm thay đổi hành vi khi chạy (runtime) trong Python, nhưng giúp **hợp đồng hàm** (function contract) trở nên tường minh — tương tự việc khai báo domain và codomain trong toán học:

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

Trong TypeScript, hợp đồng kiểu còn được kiểm tra chặt chẽ hơn ở bước biên dịch:

```typescript
type User = { id: number; email: string };

function getUserById(id: number): User | null {
  // domain: number, codomain: User | null
  ...
}
```

Khi domain hoặc codomain mơ hồ (như `any`, `object`, hoặc `dict` không rõ khóa), lỗi thường phát sinh tại ranh giới tích hợp giữa các thành phần — đúng nơi mà định nghĩa hàm toán học yêu cầu mỗi đầu vào hợp lệ phải có đúng một đầu ra xác định.

---

## Phần 3: Mô hình học máy như các hàm dự đoán

### Nhìn mô hình học máy dưới góc độ hàm số

Ở mức trừu tượng, một mô hình học máy là một hàm:

<div class="textbook-equation" markdown="1">
$$
f: X \to Y
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Trong đó:

- $$X$$ là không gian đầu vào,
- $$Y$$ là không gian đầu ra hoặc không gian các phân phối xác suất.

Chẳng hạn, mô hình có thể nhận ảnh và trả về nhãn phân loại, nhận văn bản và trả về cảm xúc, hoặc nhận dữ liệu khách hàng và ước lượng xác suất rời bỏ dịch vụ.

### Từ đầu vào đến dự đoán

**Mô hình tuyến tính đơn giản** (dễ đọc và dễ kiểm thử):

```python
def predict_credit_risk(features: dict) -> bool:
    score = (
        0.3 * features["debt_ratio"]
        + 0.5 * features["late_payments"]
        - 0.2 * features["income_years"]
    )
    return score > 0.7
```

**Scikit-learn** — vẫn là ánh xạ $$f: \mathbb{R}^n \to \{0,1\}$$, nhưng phương thức `fit` học bộ trọng số trực tiếp từ dữ liệu:

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

**Inference endpoint** (FastAPI) — đóng gói hàm dự đoán để phục vụ trong môi trường vận hành:

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

Một mô hình thực tế có thể chứa hàng triệu tham số, nhưng **hợp đồng hàm không đổi**: đầu vào là vector đặc trưng, đầu ra là nhãn hoặc xác suất. Tương tự, bước lan truyền tiến (`forward`) của mạng nơ-ron là một hàm $$f_\theta: X \to Y$$ với bộ tham số $$\theta$$ cố định sau khi huấn luyện.

### Hàm mất mát, hàm kích hoạt và hàm mục tiêu

Hệ sinh thái học máy xoay quanh nhiều loại hàm khác nhau:

- hàm mất mát (loss functions),
- hàm kích hoạt (activation functions),
- hàm nhân (kernel functions),
- hàm chấm điểm (scoring functions),
- hàm mục tiêu (objective functions).

Dù kiến trúc mô hình ngày càng phức tạp, ngôn ngữ nền tảng để mô tả và phân tích chúng vẫn là ngôn ngữ của hàm số.

### Vòng lặp huấn luyện — hàm loss và hàm cập nhật

Huấn luyện mô hình là quá trình tìm tham số $$\theta$$ sao cho hàm dự đoán $$f_\theta$$ khớp tốt với dữ liệu. Trong đó, **hàm mất mát** $$L(\theta)$$ đo lường sai số, còn **bộ tối ưu hóa (optimizer)** là hàm cập nhật tham số:

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

Ở đây có **ba lớp hàm** phối hợp với nhau: $$f_\theta$$ (dự đoán), $$L$$ (đo sai số) và quy tắc cập nhật $$\theta \leftarrow \theta - \eta \nabla L$$. Việc tách rõ từng hàm giúp dễ gỡ lỗi và thay đổi bộ tối ưu hóa mà không phải sửa kiến trúc mô hình.

![Mô hình học máy như hàm ánh xạ](/discrete-mathematics-for-computer-science-iuh/img/course/Neural_network.svg)

<p class="textbook-figure-caption" data-figure="6.21">Mô hình học máy là hàm $$f: X \to Y$$ được học từ dữ liệu — ánh xạ từ đặc trưng đầu vào đến kết quả dự đoán.</p>
---

## Phần 4: Hàm băm mật mã (Cryptographic hash functions)

### Hàm băm không phải hàm ngẫu nhiên

Hàm băm mật mã nhận đầu vào có độ dài tùy ý và trả về chuỗi giá trị băm (digest) có độ dài cố định.

Ví dụ:

```python
import hashlib

message = b"discrete mathematics"
digest = hashlib.sha256(message).hexdigest()
print(digest)
```

Đây là hàm số theo đúng nghĩa toán học: cùng một đầu vào luôn cho ra cùng một đầu ra.

**Lưu mật khẩu** — hệ thống không lưu mật khẩu dạng văn bản thuần (plaintext) mà chỉ lưu ảnh của hàm băm kèm muối (salt):

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

Hàm `verify_password` là một hàm **Boolean** $$f: \text{String} \times \text{Salt} \times \text{Digest} \to \{\text{True}, \text{False}\}$$: nó không đơn ánh (vì mọi mật khẩu sai đều trả về `False`), nhưng vẫn hoàn toàn xác định.

### Các yêu cầu bảo mật đặc thù

Một hàm băm dùng trong bảo mật không chỉ cần tính toán xác định mà còn phải đáp ứng thêm các tính chất nghiêm ngặt:

- khó đảo ngược từ giá trị băm về đầu vào gốc,
- khó tìm được hai đầu vào khác nhau có cùng giá trị băm (chống va chạm),
- nhạy cảm với thay đổi nhỏ ở đầu vào,
- phân bố đầu ra đều trên miền đích.

Điều này minh họa rằng trong khoa học máy tính, hàm không chỉ là một ánh xạ mà còn đi kèm những đặc tả (specification) kỹ thuật chặt chẽ.

![Hàm băm — toàn ánh nhưng không đơn ánh](/discrete-mathematics-for-computer-science-iuh/img/course/Surjection.svg)

<p class="textbook-figure-caption" data-figure="6.22">SHA-256 có miền đích gồm $$2^{256}$$ giá trị nhưng không đơn ánh vì miền xác định vô hạn, nên va chạm là điều không thể tránh khỏi về mặt lý thuyết.</p>
### Ứng dụng của hàm băm

Hàm băm mật mã xuất hiện trong nhiều thành phần hạ tầng quan trọng:

- lưu trữ và xác thực mật khẩu,
- kiểm tra tính toàn vẹn dữ liệu,
- chữ ký số,
- blockchain,
- định địa chỉ theo nội dung (content addressing),
- khử trùng lặp dữ liệu (deduplication),
- hệ thống phân tán.

Từ một định nghĩa toán học ngắn gọn, hàm băm đã trở thành thành phần nền tảng của bảo mật và hạ tầng phần mềm hiện đại.

---

## Phần 5: Thiết kế API như đặc tả hàm

### Một API tốt giống một hàm được đặc tả rõ

Khi thiết kế một API, ta thực chất đang xác định đầy đủ các thành phần tương tự một hàm toán học:

- đầu vào hợp lệ là gì,
- đầu ra có cấu trúc ra sao,
- tiền điều kiện (preconditions) cần thỏa mãn,
- các trường hợp lỗi được xử lý thế nào,
- thao tác có gây ra tác dụng phụ (side effects) hay không.

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

Dù nghiệp vụ tưởng chừng đơn giản, đặc tả của hàm cần nêu rõ:

- `amount` phải là số dương (ràng buộc miền xác định),
- tài khoản gửi phải đủ số dư (tiền điều kiện),
- tài khoản gửi và nhận phải khác nhau,
- trả về trạng thái mới thay vì sửa trực tiếp dữ liệu toàn cục (giúp dễ kiểm thử và dễ hoàn tác).

**REST API** cũng mang bản chất của hàm số: endpoint `POST /transfer` nhận phần thân JSON và trả về mã trạng thái kèm dữ liệu JSON. Các chuẩn tài liệu như OpenAPI/Swagger chính là cách mô tả chính thức domain và codomain của từng endpoint.

### Đặc tả mơ hồ dẫn đến hệ thống dễ lỗi

Nhiều lỗi trong sản phẩm thực tế không bắt nguồn từ thuật toán phức tạp mà từ đặc tả không rõ ràng:

- đầu vào nào được xem là hợp lệ,
- giá trị `null` được diễn giải ra sao,
- múi giờ (timezone) được chuẩn hóa như thế nào,
- tính lũy đẳng (idempotency) có được đảm bảo khi gửi lại yêu cầu hay không.

Tiếp cận API như một hàm được đặc tả chặt chẽ giúp kỹ sư viết mã chính xác hơn, duyệt mã (review) hiệu quả hơn và tài liệu hóa nhất quán hơn.

![API design — đặc tả hàm rõ ràng](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

<p class="textbook-figure-caption" data-figure="6.23">API tốt giống một hàm được đặc tả rõ ràng — đầu vào, đầu ra, tiền điều kiện và mã lỗi đều không mơ hồ.</p>
### Giao diện thuần trong thế giới có tác dụng phụ

Phần mềm thực tế không thể tránh khỏi tác dụng phụ khi tương tác với mạng, tệp tin hay cơ sở dữ liệu. Chính vì vậy, việc giữ phần giao diện càng gần với mô hình hàm thuần càng có giá trị: nó hạn chế các hành vi ngoài dự đoán, giảm lỗi khi tích hợp và giúp cả người xây dựng lẫn người sử dụng API dễ dàng suy luận hơn.

---

## Phần 6: Tư duy hàm trong các hệ thống phức tạp

Khi hệ thống phần mềm ngày càng mở rộng, tư duy hàm tiếp tục phát huy vai trò trong nhiều kiến trúc hiện đại:

- các hàm serverless (serverless functions),
- đường ống xử lý dữ liệu (data pipelines),
- các dịch vụ suy luận học máy (ML inference endpoints),
- lập trình phản ứng (reactive programming),
- các phép biến đổi tất định (deterministic transforms),
- các giao diện đã được kiểm chứng (verified interfaces).

Ngay cả trong các hệ thống phân tán vốn chứa nhiều tác dụng phụ, các kỹ sư vẫn thường tách biệt và đưa càng nhiều phần xử lý càng tốt về dạng hàm gọn gàng, dễ suy luận.

**Serverless (AWS Lambda, Cloud Functions)** — mỗi trình xử lý (handler) là một hàm:

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

**Callback và trình xử lý sự kiện (event handler)** trong JavaScript, giao diện đồ họa (GUI) hay vòng lặp trò chơi (game loop) cũng tuân theo mô hình hàm: `onClick`, `onMessage`, `setTimeout(fn, 1000)` đều có thể xem là ánh xạ $$f: \text{Event} \to \text{Action}$$.

![Hàm hợp trong hệ thống phân tán](/discrete-mathematics-for-computer-science-iuh/img/course/Example_for_a_composition_of_two_functions.svg)

<p class="textbook-figure-caption" data-figure="6.24">Serverless functions và data pipelines hoạt động như chuỗi hàm hợp — mỗi bước ánh xạ đầu vào sang đầu ra xác định.</p>
---

### Khung giải thích (nên đọc chậm): Chạy tay một chuỗi `filter–map–reduce` và một bước học tham số của hàm $f_w(x)$

**Phần A — Chuỗi xử lý hàm thuần khiết (Pure Pipeline)**

Cho danh sách điểm số `S = [4, 7, 9, 5, 10]`. Ta ghép 3 hàm bậc cao nối tiếp nhau (không hề làm biến đổi mảng gốc `S`):
1. `filter(x >= 5, S)` $\to$ `[7, 9, 5, 10]` (lọc giữ các điểm đạt).
2. `map(x -> x * 10, ...)` $\to$ `[70, 90, 50, 100]` (quy đổi sang thang điểm 100).
3. `reduce((acc, x) -> acc + x, ..., 0)` $\to$ $70 + 90 + 50 + 100 = \mathbf{310}$ (tổng điểm, trung bình $\mathbf{77{,}5}$).

**Phần B — Một bước huấn luyện mô hình Học máy như tối ưu hóa hàm $f_w(x) = w \cdot x$**

Giả sử ta có một điểm dữ liệu $(x = 2,\; y = 10)$ (hàm đúng là $y = 5x$), nhưng mô hình khởi tạo sai ở $w_0 = 3$, tốc độ học $\eta = 0{,}1$, hàm mất mát $L(w) = \frac{1}{2}(wx - y)^2$:
1. **Dự đoán ban đầu**: $\hat{y}_0 = f_3(2) = 3 \times 2 = 6 \implies$ sai số $e_0 = \hat{y}_0 - y = 6 - 10 = -4$, độ mất mát $L(3) = \frac{1}{2}(-4)^2 = \mathbf{8{,}00}$.
2. **Tính đạo hàm theo tham số $w$**: $L'(w) = (wx - y)\cdot x = (-4) \times 2 = \mathbf{-8}$.
3. **Cập nhật tham số ngược chiều gradient**:
   $$w_1 = w_0 - \eta \cdot L'(w_0) = 3 - 0{,}1 \times (-8) = \mathbf{3{,}8}.$$
4. **Kiểm tra sau đúng 1 bước**: Dự đoán mới $\hat{y}_1 = 3{,}8 \times 2 = 7{,}6$, mất mát tụt mạnh xuống $L(3{,}8) = \frac{1}{2}(7{,}6 - 10)^2 = \mathbf{2{,}88}$ (giảm từ `8,00` xuống `2,88` chỉ sau một vòng lặp!). Mọi mô hình LLM hàng trăm tỷ tham số đều lặp lại chính cơ chế tối ưu hàm này ở quy mô lớn hơn.

## Kết luận

Hàm số không chỉ giới hạn trong đại số phổ thông mà hiện diện ở hầu hết mọi tầng của phần mềm: từ từng hàm trong mã nguồn, giao diện API cho đến các mô hình học máy. Từ nền tảng lý thuyết của Church và Turing đến Haskell, SHA-256 và các dịch vụ dự đoán hiện đại, khái niệm hàm luôn giữ vai trò cốt lõi trong khoa học máy tính.

---

## Bài tập thực hành

### Bài tập 1: Hàm đệ quy

Viết hàm đệ quy tính $$f(n) = n!$$ và giải thích tại sao đây là hàm tính toán được theo nghĩa của Turing.

<details>
<summary>Đáp án</summary>

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)
```

Hàm này tính toán được bằng máy Turing vì tồn tại thuật toán hữu hạn bước cho ra kết quả chính xác với mọi số nguyên không âm $$n$$.

</details>

### Bài tập 2: Hàm băm

Giải thích tại sao trên thực tế hàm băm SHA-256 thường được xem là toàn ánh nhưng không đơn ánh.

<details>
<summary>Đáp án</summary>

SHA-256 có đầu ra 256-bit (gồm $$2^{256}$$ giá trị khả dĩ), nhưng miền xác định chứa tập vô hạn các chuỗi đầu vào có độ dài bất kỳ. Vì miền xác định lớn hơn rất nhiều so với miền đích nên hàm chắc chắn không đơn ánh (tồn tại va chạm).

</details>

### Bài tập 3: Hàm trong học máy

Trong mô hình học máy, hàm dự đoán $$f: \mathbb{R}^n \to \mathbb{R}$$ thường không phải song ánh. Tại sao?

<details>
<summary>Đáp án</summary>

Vì nhiều đầu vào khác nhau (các điểm dữ liệu khác nhau trong $$\mathbb{R}^n$$) có thể ánh xạ về cùng một nhãn hoặc cùng một giá trị dự đoán, nên hàm không đơn ánh.

</details>

### Bài tập 4: Viết pipeline xử lý chuỗi

Cho danh sách email thô:

```python
raw = ["  AN@UNIV.EDU.VN  ", "", "binh@univ.edu.vn", "invalid"]
```

Viết hàm `process_emails(raw) -> list[str]` gồm ba bước (ba hàm con):

1. `strip_each` — bỏ khoảng trắng đầu và cuối chuỗi.
2. `drop_empty` — loại bỏ các chuỗi rỗng.
3. `normalize_case` — chuyển toàn bộ về chữ thường.

Ghép các bước bằng composition (gọi lồng nhau hoặc dùng `map`/`filter`). Kết quả mong đợi: `["an@univ.edu.vn", "binh@univ.edu.vn", "invalid"]`.

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

assert process_emails(raw) == ["an@univ.edu.vn", "binh@univ.edu.vn", "invalid"]
```

</details>

### Bài tập 5: Pure và impure

Phân loại các hàm sau là **pure** hay **impure** và giải thích ngắn gọn:

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

- `add_tax` — **pure**: kết quả chỉ phụ thuộc vào hai tham số `price` và `rate`.
- `get_current_user` — **impure**: đọc dữ liệu từ cơ sở dữ liệu và trạng thái phiên (`session`), phụ thuộc trạng thái bên ngoài.
- `random_id` — **impure**: dù không có tham số nhưng mỗi lần gọi lại trả về một kết quả ngẫu nhiên khác nhau.
- `parse_int` — **pure** trên miền các chuỗi số nguyên hợp lệ; với cùng một đầu vào `s`, hành vi (trả về số nguyên hoặc ném ngoại lệ) là hoàn toàn xác định.

</details>

### Bài tập 6: Decorator kiểm tra tham số

Viết decorator `@require_positive` bọc hàm nhận tham số `amount`: nếu `amount <= 0` thì ném `ValueError`, ngược lại gọi hàm gốc.

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

Endpoint `GET /users/{id}` trả về thông tin người dùng hoặc mã lỗi 404. Viết mã giả Python (hoặc FastAPI) thể hiện rõ:

- domain: `id` là số nguyên dương,
- codomain: thông tin `User` hoặc phản hồi lỗi,
- precondition: `id` hợp lệ,
- postcondition: không làm lộ mật khẩu trong dữ liệu trả về.

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

Domain: `user_id > 0`. Codomain: phản hồi HTTP kèm JSON an toàn. Việc tách `user_repo` ra lớp riêng giúp kiểm thử handler dễ dàng bằng đối tượng giả lập (mock).

</details>

### Bài tập 8: `map`/`reduce` trong thống kê

Cho danh sách điểm `scores = [7, 8, 5, 9, 6]`:

(a) Dùng `map` tính điểm sau khi cộng thêm 10% điểm thưởng (làm tròn 1 chữ số thập phân).
(b) Dùng `reduce` tìm điểm cao nhất (không dùng hàm `max()`).

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

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Hàm trong lập trình**: mỗi hàm là một hợp đồng từ domain sang codomain; cùng một đầu vào cho cùng một đầu ra (trừ hàm impure phụ thuộc trạng thái ngoài).
- **Lập trình hàm**: `map`, `filter`, `reduce`, composition, closure và decorator giúp ghép các hàm nhỏ thành pipeline dễ kiểm thử.
- **Pure và impure**: giữ logic tính toán cốt lõi dưới dạng hàm thuần và tách các thao tác I/O ra lớp ngoài.
- **Học máy**: `model.predict` là hàm $$f_\theta$$; quá trình huấn luyện tìm bộ tham số $$\theta$$ thông qua hàm mất mát và bộ tối ưu hóa.
- **Hàm băm và API**: SHA-256 hay REST endpoint đều đòi hỏi đặc tả tính chất hàm (tính xác định, tiền điều kiện, đầu vào/đầu ra) rõ ràng.
- **Tính chất toán học**: đơn ánh, toàn ánh, song ánh và hàm nghịch đảo (xem bài 06_02, 06_03) hỗ trợ thiết kế khóa, cơ chế hoàn tác và giải mã chính xác.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=dNRDvLACg5Q">Turing Machines Explained - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu khái niệm hàm tính toán được trên máy Turing, khớp với phần lịch sử của bài.
- <a href="https://www.youtube.com/watch?v=OixshZzH8t0">FUNCTIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Hợp đồng đầu vào–đầu ra, liên hệ trực tiếp với `map` và hàm trong lập trình.
- <a href="https://www.youtube.com/watch?v=jsraR-el8_o">Hash Collisions &amp; The Birthday Paradox - Computerphile</a> — Computerphile, tiếng Anh. Hàm băm và hiện tượng va chạm, gắn với phần hàm băm mật mã trong bài.
