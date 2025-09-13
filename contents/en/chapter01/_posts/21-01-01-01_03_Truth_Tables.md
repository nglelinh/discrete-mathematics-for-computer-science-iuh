---
layout: post
title: "Bảng Chân Trị và Ứng dụng"
categories: chapter01
date: 2021-01-01
order: 3
required: true
lang: vi
---

# Bảng Chân Trị và Ứng dụng

Bảng chân trị là công cụ quan trọng để phân tích và hiểu các mệnh đề logic phức tạp. Trong bài này, chúng ta sẽ học cách xây dựng và sử dụng bảng chân trị.

## Bảng chân trí là gì?

**Định nghĩa**: Bảng chân trị là bảng liệt kê tất cả các khả năng về giá trị chân lý của các mệnh đề thành phần và giá trị chân lý tương ứng của mệnh đề phức hợp.

## Cách xây dựng bảng chân trí

### Bước 1: Xác định số biến
- Với n biến, ta có 2ⁿ dòng trong bảng chân trí

### Bước 2: Liệt kê tất cả tổ hợp
- Liệt kê tất cả các tổ hợp có thể của các biến

### Bước 3: Tính toán từng bước
- Tính giá trị của các biểu thức con trước
- Sau đó tính biểu thức chính

## Ví dụ 1: Bảng chân trí cho (p ∧ q) → r

| p | q | r | p ∧ q | (p ∧ q) → r |
|---|---|---|-------|-------------|
| T | T | T |   T   |      T      |
| T | T | F |   T   |      F      |
| T | F | T |   F   |      T      |
| T | F | F |   F   |      T      |
| F | T | T |   F   |      T      |
| F | T | F |   F   |      T      |
| F | F | T |   F   |      T      |
| F | F | F |   F   |      T      |

## Ví dụ 2: Bảng chân trí cho ¬(p ∨ q) ↔ (¬p ∧ ¬q)

| p | q | p ∨ q | ¬(p ∨ q) | ¬p | ¬q | ¬p ∧ ¬q | ¬(p ∨ q) ↔ (¬p ∧ ¬q) |
|---|---|-------|----------|----|----|---------|----------------------|
| T | T |   T   |    F     | F  | F  |    F    |          T           |
| T | F |   T   |    F     | F  | T  |    F    |          T           |
| F | T |   T   |    F     | T  | F  |    F    |          T           |
| F | F |   F   |    T     | T  | T  |    T    |          T           |

**Kết luận**: Biểu thức này luôn đúng (tautology) - đây chính là định luật De Morgan!

## Các khái niệm quan trọng

### 1. Tautology (Hằng đúng)
Mệnh đề luôn có giá trị T trong mọi trường hợp.

**Ví dụ**: p ∨ ¬p

| p | ¬p | p ∨ ¬p |
|---|----|----|
| T | F  | T  |
| F | T  | T  |

### 2. Contradiction (Hằng sai)
Mệnh đề luôn có giá trị F trong mọi trường hợp.

**Ví dụ**: p ∧ ¬p

| p | ¬p | p ∧ ¬p |
|---|----|----|
| T | F  | F  |
| F | T  | F  |

### 3. Contingency (Mệnh đề thường)
Mệnh đề có thể đúng hoặc sai tùy thuộc vào giá trị của các biến.

## Ứng dụng của bảng chân trí

### 1. Kiểm tra tính tương đương logic
Hai mệnh đề tương đương nếu chúng có cùng bảng chân trí.

**Ví dụ**: Kiểm tra p → q ≡ ¬p ∨ q

| p | q | p → q | ¬p | ¬p ∨ q |
|---|---|-------|----|----|
| T | T |   T   | F  | T  |
| T | F |   F   | F  | F  |
| F | T |   T   | T  | T  |
| F | F |   T   | T  | T  |

**Kết luận**: p → q ≡ ¬p ∨ q (tương đương)

### 2. Kiểm tra tính hợp lệ của lập luận
Lập luận hợp lệ nếu kết luận đúng khi tất cả tiền đề đúng.

**Ví dụ**: 
- Tiền đề 1: p → q
- Tiền đề 2: p
- Kết luận: q

| p | q | p → q | p ∧ (p → q) | [p ∧ (p → q)] → q |
|---|---|-------|-------------|-------------------|
| T | T |   T   |      T      |         T         |
| T | F |   F   |      F      |         T         |
| F | T |   T   |      F      |         T         |
| F | F |   T   |      F      |         T         |

**Kết luận**: Lập luận hợp lệ (cột cuối toàn T)

### 3. Thiết kế mạch logic

```
Ví dụ: Thiết kế mạch cho (A ∧ B) ∨ C

Bảng chân trí:
| A | B | C | A ∧ B | (A ∧ B) ∨ C |
|---|---|---|-------|-------------|
| 0 | 0 | 0 |   0   |      0      |
| 0 | 0 | 1 |   0   |      1      |
| 0 | 1 | 0 |   0   |      0      |
| 0 | 1 | 1 |   0   |      1      |
| 1 | 0 | 0 |   0   |      0      |
| 1 | 0 | 1 |   0   |      1      |
| 1 | 1 | 0 |   1   |      1      |
| 1 | 1 | 1 |   1   |      1      |
```

## Công cụ tương tác

<div id="truth-table-calculator" style="border: 1px solid #ccc; padding: 20px; margin: 20px 0;">
    <h4>Máy tính bảng chân trí</h4>
    <p>Nhập biểu thức logic (sử dụng &, |, !, ->, <->):</p>
    <input type="text" id="logic-expression" placeholder="Ví dụ: (p & q) | r" style="width: 300px; padding: 5px;">
    <button onclick="generateTruthTable()" style="padding: 5px 10px;">Tạo bảng</button>
    <div id="truth-table-result" style="margin-top: 15px;"></div>
</div>

<script>
function generateTruthTable() {
    const expression = document.getElementById('logic-expression').value;
    const resultDiv = document.getElementById('truth-table-result');
    
    if (!expression) {
        resultDiv.innerHTML = '<p style="color: red;">Vui lòng nhập biểu thức!</p>';
        return;
    }
    
    // Đây là ví dụ đơn giản - trong thực tế cần parser phức tạp hơn
    resultDiv.innerHTML = `
        <p><strong>Biểu thức:</strong> ${expression}</p>
        <p><em>Chức năng này đang được phát triển...</em></p>
        <p>Hãy thử tự tạo bảng chân trí theo các bước đã học!</p>
    `;
}
</script>

## Bài tập thực hành

### Bài tập 1: Xây dựng bảng chân trí
Xây dựng bảng chân trí cho các biểu thức sau:
1. (p → q) ∧ (q → r) → (p → r)
2. (p ∨ q) ∧ ¬(p ∧ q)
3. (p ↔ q) ↔ ((p → q) ∧ (q → p))

### Bài tập 2: Phân loại mệnh đề
Xác định các mệnh đề sau là tautology, contradiction hay contingency:
1. p → (q → p)
2. (p ∧ q) ∧ ¬(p ∨ q)
3. (p → q) → ((¬q) → (¬p))

<details>
<summary>Gợi ý Bài tập 2</summary>

1. **Tautology** - Luôn đúng
2. **Contradiction** - Luôn sai  
3. **Tautology** - Đây là định luật contrapositive

</details>

### Bài tập 3: Ứng dụng thực tế
Một hệ thống báo động có 3 cảm biến A, B, C. Báo động kích hoạt khi:
- Cả A và B đều kích hoạt, HOẶC
- C kích hoạt và ít nhất một trong A hoặc B kích hoạt

Viết biểu thức logic và tạo bảng chân trí cho hệ thống này.

## Tóm tắt

- **Bảng chân trí** giúp phân tích mệnh đề phức tạp
- **Tautology**: luôn đúng
- **Contradiction**: luôn sai
- **Contingency**: có thể đúng hoặc sai
- Ứng dụng: kiểm tra tương đương, lập luận hợp lệ, thiết kế mạch

Trong bài tiếp theo, chúng ta sẽ học về **các định luật logic** và cách sử dụng chúng để đơn giản hóa các biểu thức phức tạp.
