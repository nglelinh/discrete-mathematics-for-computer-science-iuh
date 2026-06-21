---
layout: post
title: "Máy Trạng thái Hữu hạn trong Kỹ thuật Phần mềm"
categories: chapter18
date: 2021-01-01
order: 6
required: false
lang: en
---

Mỗi lần bạn đợi nút "Gửi" chuyển sang "Đang gửi…" rồi "Thành công" hoặc "Lỗi", hay khi regex `^[a-z]+$` khớp chuỗi input — bạn đang làm việc với **máy trạng thái hữu hạn** (finite state machine, FSM).

```python
from enum import Enum, auto

class OrderState(Enum):
    DRAFT = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELLED = auto()

TRANSITIONS = {
    (OrderState.DRAFT, "pay"): OrderState.PAID,
    (OrderState.PAID, "ship"): OrderState.SHIPPED,
    (OrderState.DRAFT, "cancel"): OrderState.CANCELLED,
    (OrderState.PAID, "cancel"): OrderState.CANCELLED,
}

def transition(state: OrderState, event: str) -> OrderState:
    key = (state, event)
    if key not in TRANSITIONS:
        raise ValueError(f"illegal transition: {state.name} + {event}")
    return TRANSITIONS[key]
```

Đoạn code trên là DFA trong đời thực: tập trạng thái hữu hạn, bảng chữ cái sự kiện (`pay`, `ship`, `cancel`), hàm chuyển $$\delta$$ xác định. Không có "bộ nhớ tự do" — mọi thông tin cần thiết nằm trong trạng thái hiện tại.

Từ DFA/NFA trong lý thuyết đến Redux reducer, giao thức TCP, và lexer regex — bài này nối Chương 18 với kỹ thuật phần mềm hàng ngày.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Mô hình hóa** luồng UI, đơn hàng, và giao thức bằng FSM/DFA với trạng thái và chuyển hợp lệ.
- **Triển khai** state machine trong Python/TypeScript và từ chối transition không hợp lệ.
- **Liên hệ** regex với NFA/DFA và hiểu vì sao engine regex dùng automata.
- **Phân biệt** FSM (bộ nhớ hữu hạn) với parser/ngữ cảnh cần ngăn xếp (CFG).
- **Thiết kế** protocol handler đọc byte stream theo trạng thái.

**Từ khóa**: máy trạng thái hữu hạn (FSM), DFA, NFA, automaton, state machine, regex, reducer, giao thức (protocol).

---

## Phần 1: FSM trong lý thuyết và trong code

### 1.1. Bộ năm $$(Q, \Sigma, \delta, q_0, F)$$

Trong Chương 18, DFA gồm:

- $$Q$$: tập trạng thái hữu hạn
- $$\Sigma$$: bảng chữ cái đầu vào (ký hiệu / sự kiện)
- $$\delta: Q \times \Sigma \to Q$$: hàm chuyển **xác định**
- $$q_0$$: trạng thái bắt đầu
- $$F \subseteq Q$$: trạng thái chấp nhận

Trong phần mềm, "chấp nhận" thường là trạng thái **ổn định** (stable): `SHIPPED`, `AUTHENTICATED`, `PARSED_OK`.

![Sơ đồ trạng thái UML — mô hình hóa hành vi đối tượng](/discrete-mathematics-for-computer-science-iuh/img/course/uml_state_machine.svg)

*Hình 18.26: Sơ đồ trạng thái (state diagram) — cùng cấu trúc toán học với DFA, dùng trong thiết kế UI và domain model.*

### 1.2. Enum + bảng chuyển = DFA có thể kiểm thử

```typescript
type TrafficLight = "RED" | "YELLOW" | "GREEN";

const nextLight: Record<TrafficLight, TrafficLight> = {
  RED: "GREEN",
  GREEN: "YELLOW",
  YELLOW: "RED",
};

function step(light: TrafficLight): TrafficLight {
  return nextLight[light];
}
```

Mỗi `light` chỉ có **một** trạng thái kế — đúng định nghĩa DFA. Unit test chỉ cần duyệt hữu hạn trạng thái.

<div class="content-box insight-box" markdown="1">
**Nhận xét**: FSM ép bạn liệt kê mọi transition hợp lệ. Bug "trạng thái không mong đợi" thường là cạnh thiếu trong $$\delta$$ — sửa bằng cách làm rõ diagram trước khi viết code.
</div>

---

## Phần 2: NFA, regex, và lexer

### 2.1. Regex là cách viết gọn NFA

Pattern `a(b|c)*` mô tả NFA: đọc `a`, rồi lặp `b` hoặc `c`. Engine regex (PCRE, Java `Pattern`, Python `re`) biên dịch pattern thành automata rồi mô phỏng.

```python
import re

TOKEN_SPEC = [
    ("NUMBER", r"\d+"),
    ("PLUS",   r"\+"),
    ("IDENT",  r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("SKIP",   r"[ \t]+"),
]

def tokenize(code: str):
    master = "|".join(f"(?P<{name}>{pat})" for name, pat in TOKEN_SPEC)
    for m in re.finditer(master, code):
        kind = m.lastgroup
        if kind != "SKIP":
            yield kind, m.group()
```

Lexer **không** cần ngữ pháp ngữ cảnh tự do — chỉ cần lớp **regular language** (DFA/NFA đủ).

![Phân tích từ vựng (lexical analysis) trong trình biên dịch](/discrete-mathematics-for-computer-science-iuh/img/course/lexical_analysis.svg)

*Hình 18.27: Lexical analysis — đọc chuỗi ký tự theo trạng thái; mỗi token class thường tương ứng một automaton hoặc nhánh trong NFA tổng hợp.*

### 2.2. DFA vs NFA trong thực thi

- **DFA**: mô phỏng $$O(n)$$ trên chuỗi dài $$n$$, một trạng thái hiện tại.
- **NFA**: có thể có nhiều nhánh; subset construction chuyển sang DFA (có thể nở số trạng thái).

Trong product, regex engine chấp nhận NFA + backtracking cho feature tiện; lexer compiler thường dùng DFA sinh tự động (lex/flex).

---

## Phần 3: State machine trong UI và backend

### 3.1. Form wizard và async request

```typescript
type FormStatus = "idle" | "submitting" | "success" | "error";

function reducer(state: FormStatus, action: { type: string }): FormStatus {
  switch (state) {
    case "idle":
      if (action.type === "SUBMIT") return "submitting";
      return state;
    case "submitting":
      if (action.type === "OK") return "success";
      if (action.type === "FAIL") return "error";
      return state;
    case "error":
      if (action.type === "RETRY") return "submitting";
      return state;
    case "success":
      return state; // terminal
    default:
      return state;
  }
}
```

Redux `reducer` là DFA: `(state, action) -> state`. React `useReducer` giữ graph transition tập trung, tránh `if` rải rác.

### 3.2. TCP và giao thức tầng thấp

TCP connection (đơn giản hóa): `CLOSED` → `SYN_SENT` → `ESTABLISHED` → `FIN_WAIT` → `CLOSED`. Mỗi segment nhận được là ký hiệu đầu vào; vi phạm thứ tự → reset. Đây là lý do protocol spec vẽ state diagram — implementer code đúng theo $$\delta$$.

![Automaton hữu hạn — nền tảng nhận diện ngôn ngữ chính quy](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_theory.svg)

*Hình 18.28: Lý thuyết automata — FSM nhận diện ngôn ngữ chính quy; cùng mô hình cho regex, lexer, và protocol handler.*

---

## Phần 4: Mealy/Moore và mở rộng

### 4.1. Output gắn trạng thái (Moore) hoặc cạnh (Mealy)

- **Moore**: `state === "PAID"` → hiển thị icon "đã thanh toán".
- **Mealy**: sự kiện `pay` trên cạnh `DRAFT → PAID` → phát email xác nhận.

Trong game và embedded, Mealy/Moore chính thức hơn; trong web app, side effect thường nằm ở middleware sau transition hợp lệ.

### 4.2. Khi FSM không đủ

Ngôn ngữ $$a^n b^n$$ không phải regular — cần **stack** (PDA / CFG). Ví dụ: kiểm tra ngoặc cân `((()))` bằng FSM thuần **không** được; parser cần Chương 19.

<div class="content-box warning-box" markdown="1">
**Cẩn thận**: Đừng nhồi mọi biến vào "trạng thái" vô hạn. Nếu context phụ thuộc độ sâu ngăn xếp tùy ý, đó là dấu hiệu cần parser/ngữ cảnh, không chỉ FSM.
</div>

---

## Bài tập thực hành

### Bài tập 1: Vẽ DFA đơn giản

Thiết kế DFA trên $$\Sigma = \{0,1\}$$ chấp nhận chuỗi có **số chữ số 1 chẵn** (kể cả chuỗi rỗng). Liệt kê $$Q$$, $$q_0$$, $$F$$.

<details>
<summary>Đáp án</summary>

- $$Q = \{even, odd\}$$
- $$q_0 = even$$
- $$F = \{even\}$$
- $$\delta(even, 0)=even$$, $$\delta(even, 1)=odd$$, $$\delta(odd, 0)=odd$$, $$\delta(odd, 1)=even$$

</details>

### Bài tập 2: Implement transition table

Hoàn thiện hàm `step` cho traffic light ba màu: chỉ `timer` event được phép, theo chu trình RED → GREEN → YELLOW → RED.

<details>
<summary>Đáp án</summary>

```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3

def step(light: Light) -> Light:
    table = {
        Light.RED: Light.GREEN,
        Light.GREEN: Light.YELLOW,
        Light.YELLOW: Light.RED,
    }
    return table[light]

assert step(step(step(Light.RED))) == Light.RED
```

</details>

### Bài tập 3: Regex và ngôn ngữ

Pattern `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` mô tả ngôn ngữ gì? Có phải regular language không?

<details>
<summary>Đáp án</summary>

Chuỗi dạng `YYYY-MM-DD` với mỗi phần là chữ số cố định độ dài. Có — mọi pattern hữu hạn trên alphabet hữu hạn đều tương đương một NFA/DFA.

</details>

### Bài tập 4: Reducer UI

Thêm transition: từ `success`, event `RESET` về `idle`. Cập nhật `reducer` ở Phần 3.1.

<details>
<summary>Đáp án</summary>

```typescript
case "success":
  if (action.type === "RESET") return "idle";
  return state;
```

</details>

### Bài tập 5: Transition bất hợp lệ

Với `OrderState` ở đầu bài, gọi `transition(OrderState.SHIPPED, "cancel")` nên làm gì? Giải thích theo FSM.

<details>
<summary>Đáp án</summary>

Nên `raise ValueError` (hoặc trả lỗi tương đương) vì cặp `(SHIPPED, cancel)` không thuộc $$\delta$$. Trạng thái terminal không có cạnh hủy — đây là **từ chối input** giống DFA không có transition.

</details>

### Bài tập 6: Lexer token

Viết `tokenize("x = 12")` trả list `[(IDENT,x), (?,=), (NUMBER,12)]` dùng spec Phần 2.1 (thêm token `EQ` với pattern `=`).

<details>
<summary>Đáp án</summary>

Thêm `("EQ", r"=")` vào `TOKEN_SPEC`. Kết quả: `[('IDENT', 'x'), ('EQ', '='), ('NUMBER', '12')]`.

</details>

### Bài tập 7: FSM vs ngăn xếp

Chuỗi ngoặc `(()())` có được nhận bởi DFA đếm mod 2 không? Chuỗi nào cần stack?

<details>
<summary>Đáp án</summary>

Đếm mod 2 (chẵn/lẻ số `(`) **không** đủ để kiểm tra cân ngoặc — `(()` và `())` có thể cùng parité nhưng một cái sai. Cần stack hoặc CFG để khớp $$a^n b^n$$-style nesting.

</details>

### Bài tập 8: Thiết kế protocol

Mô tả FSM cho HTTP client đơn giản: `IDLE` --(send request)--> `WAITING` --(200)--> `DONE` --(close)--> `IDLE`; từ `WAITING` --(timeout)--> `ERROR`. Viết bảng transition.

<details>
<summary>Đáp án</summary>

| Trạng thái | Sự kiện | Trạng thái kế |
|---|---|---|
| IDLE | send | WAITING |
| WAITING | 200 | DONE |
| WAITING | timeout | ERROR |
| DONE | close | IDLE |
| ERROR | reset | IDLE |

</details>

## Tóm tắt

- **FSM/DFA**: trạng thái hữu hạn + chuyển xác định — mô hình cho UI flow, domain lifecycle, protocol.
- **Enum + bảng $$\delta$$**: cách implement dễ test; từ chối transition không định nghĩa.
- **Regex/lexer**: NFA/DFA thực tế nhất trong compiler và validation chuỗi.
- **Reducer**: DFA trong frontend state management.
- **Giới hạn**: ngôn ngữ cần bộ nhớ ngăn xếp (cân ngoặc) vượt FSM — chuyển sang CFG (Chương 19).

Trong bài tiếp theo về ngôn ngữ hình thức, chúng ta leo lên phân cấp Chomsky — từ regex đến parser và cây cú pháp trừu tượng (AST).