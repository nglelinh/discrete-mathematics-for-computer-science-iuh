---
layout: post
title: "Phép toán Logic"
categories: chapter01
date: 2021-01-01
order: 2
required: true
lang: vi
---

# Phép toán Logic

Trong bài này, chúng ta sẽ học các phép toán logic cơ bản để kết hợp các mệnh đề đơn giản thành các mệnh đề phức tạp hơn.

## 1. Phép phủ định (Negation) - NOT

**Ký hiệu**: ¬p hoặc ~p hoặc !p

**Định nghĩa**: Phủ định của mệnh đề p là mệnh đề có giá trị chân lý ngược lại với p.

### Bảng chân trị:
| p | ¬p |
|---|---|
| T | F |
| F | T |

**Ví dụ**:
- p: "Hôm nay trời nắng"
- ¬p: "Hôm nay trời không nắng"

## 2. Phép hội (Conjunction) - AND

**Ký hiệu**: p ∧ q

**Định nghĩa**: p ∧ q chỉ đúng khi cả p và q đều đúng.

### Bảng chân trị:
| p | q | p ∧ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**Ví dụ**:
- p: "Tôi có tiền"
- q: "Cửa hàng mở cửa"
- p ∧ q: "Tôi có tiền và cửa hàng mở cửa"

## 3. Phép tuyển (Disjunction) - OR

**Ký hiệu**: p ∨ q

**Định nghĩa**: p ∨ q chỉ sai khi cả p và q đều sai.

### Bảng chân trị:
| p | q | p ∨ q |
|---|---|-------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

**Ví dụ**:
- p: "Tôi đi xe bus"
- q: "Tôi đi xe máy"
- p ∨ q: "Tôi đi xe bus hoặc xe máy"

## 4. Phép kéo theo (Implication) - IF...THEN

**Ký hiệu**: p → q

**Định nghĩa**: p → q chỉ sai khi p đúng và q sai.

### Bảng chân trị:
| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**Ví dụ**:
- p: "Trời mưa"
- q: "Đường ướt"
- p → q: "Nếu trời mưa thì đường ướt"

### Lưu ý quan trọng:
- p được gọi là **giả thiết** (hypothesis)
- q được gọi là **kết luận** (conclusion)
- Khi p sai, p → q luôn đúng (vacuously true)

## 5. Phép tương đương (Biconditional) - IF AND ONLY IF

**Ký hiệu**: p ↔ q

**Định nghĩa**: p ↔ q đúng khi p và q có cùng giá trị chân lý.

### Bảng chân trị:
| p | q | p ↔ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

**Ví dụ**:
- p: "n là số chẵn"
- q: "n chia hết cho 2"
- p ↔ q: "n là số chẵn khi và chỉ khi n chia hết cho 2"

## 6. Phép tuyển loại trừ (Exclusive OR) - XOR

**Ký hiệu**: p ⊕ q

**Định nghĩa**: p ⊕ q đúng khi chỉ có một trong hai mệnh đề đúng.

### Bảng chân trị:
| p | q | p ⊕ q |
|---|---|-------|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

## Thứ tự ưu tiên của các phép toán

1. ¬ (phủ định)
2. ∧ (hội)
3. ∨ (tuyển)
4. → (kéo theo)
5. ↔ (tương đương)

## Ví dụ tính toán

Cho p = T, q = F, r = T. Tính giá trị của: ¬p ∨ (q → r)

**Giải**:
1. ¬p = ¬T = F
2. q → r = F → T = T
3. ¬p ∨ (q → r) = F ∨ T = T

## Ứng dụng trong lập trình

```python
# Trong Python
p = True
q = False

# Phép AND
result_and = p and q  # False

# Phép OR  
result_or = p or q   # True

# Phép NOT
result_not = not p   # False

# Phép XOR (sử dụng !=)
result_xor = p != q  # True
```

## Bài tập thực hành

### Bài tập 1: Tính giá trị chân lý
Cho p = T, q = F, r = T. Tính:
1. p ∧ ¬q
2. (p ∨ q) → r
3. p ↔ (q ∨ r)
4. ¬(p ∧ q) ∨ r

<details>
<summary>Đáp án</summary>

1. p ∧ ¬q = T ∧ T = T
2. (p ∨ q) → r = T → T = T
3. p ↔ (q ∨ r) = T ↔ T = T
4. ¬(p ∧ q) ∨ r = T ∨ T = T

</details>

### Bài tập 2: Dịch sang ngôn ngữ tự nhiên
Cho:
- p: "Tôi có thời gian"
- q: "Tôi có tiền"
- r: "Tôi đi xem phim"

Dịch các biểu thức sau:
1. p ∧ q → r
2. ¬p ∨ ¬q
3. r ↔ (p ∧ q)

## Tóm tắt

Các phép toán logic cơ bản:
- **¬p**: phủ định (NOT)
- **p ∧ q**: hội (AND)
- **p ∨ q**: tuyển (OR)
- **p → q**: kéo theo (IF...THEN)
- **p ↔ q**: tương đương (IF AND ONLY IF)
- **p ⊕ q**: tuyển loại trừ (XOR)

Trong bài tiếp theo, chúng ta sẽ học về **bảng chân trị** và cách sử dụng chúng để phân tích các mệnh đề phức tạp.
