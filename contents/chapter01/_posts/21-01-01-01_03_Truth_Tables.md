---
layout: post
title: "Bảng Chân Trị và Ứng dụng"
categories: chapter01
date: 2021-01-01
order: 3
required: true
lang: en
---

Sau khi học các phép toán logic như `and`, `or`, `not`, ta có thể viết được những biểu thức điều kiện khá phức tạp. Nhưng có một vấn đề rất thực tế: **trực giác của con người thường không đủ đáng tin** khi biểu thức bắt đầu dài ra.

Một điều kiện nhìn có vẻ hợp lý vẫn có thể sai ở đúng **một trường hợp hiếm gặp** — và chính trường hợp đó có thể làm hỏng một giao dịch ngân hàng, mở nhầm quyền truy cập, cho kết quả tìm kiếm sai, hoặc khiến test case bỏ sót lỗi quan trọng nhất. Trong kỹ thuật phần mềm, rất nhiều bug khó chịu không nằm ở cú pháp, mà nằm ở chỗ lập trình viên **tin rằng mình hiểu biểu thức**, trong khi máy tính lại hiểu theo một cách khác.

Đó là lý do ta cần đến **bảng chân trị**. Có thể xem bảng chân trị như một chiếc đèn pha chiếu sáng toàn bộ biểu thức logic: thay vì đoán mò hoặc thử vài ví dụ, ta liệt kê **mọi khả năng có thể xảy ra** và kiểm tra từng trường hợp một cách có hệ thống.

Nhờ bảng chân trị, chúng ta có thể:

- biết chắc một biểu thức hoạt động ra sao trong mọi trường hợp,
- kiểm tra hai cách viết điều kiện có thật sự tương đương hay không,
- phát hiện các mệnh đề luôn đúng hoặc luôn sai,
- và xác định những tổ hợp đầu vào quan trọng cần được kiểm thử trong phần mềm thực tế.

Nói cách khác, bảng chân trị biến logic từ thứ "có vẻ đúng" thành thứ **được chứng minh là đúng**. Trong bài này, chúng ta sẽ học cách xây dựng bảng chân trị, đọc ý nghĩa của nó và dùng nó như một công cụ kiểm chứng cho tư duy logic cũng như cho các biểu thức điều kiện trong lập trình.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Xây dựng** bảng chân trị cho biểu thức có 2, 3 hoặc nhiều biến.
- **Tính** giá trị của biểu thức phức hợp từng bước.
- **Phân loại** biểu thức thành hằng đúng, hằng sai, hoặc mệnh đề thường.
- **Kiểm tra** hai biểu thức có tương đương logic không.
- **Ứng dụng** bảng chân trị để thiết kế test case bao phủ đủ trường hợp.

**Từ khóa**: Bảng chân trị (truth table), tautology, contradiction, contingency, test case, exhaustive checking.

## Bảng chân trị là gì?

**Định nghĩa**: Bảng chân trị là bảng liệt kê tất cả các khả năng về giá trị chân lý của các mệnh đề thành phần và giá trị chân lý tương ứng của mệnh đề phức hợp.

## Cách xây dựng bảng chân trị

### Bước 1: Xác định số biến
- Với n biến, ta có 2ⁿ dòng trong bảng chân trị

### Bước 2: Liệt kê tất cả tổ hợp
- Liệt kê tất cả các tổ hợp có thể của các biến

### Bước 3: Tính toán từng bước
- Tính giá trị của các biểu thức con trước
- Sau đó tính biểu thức chính

<div class="content-box insight-box" markdown="1">
**Mẹo liệt kê tổ hợp**: Để không bỏ sót tổ hợp nào, hãy tưởng tượng bạn đang đếm nhị phân. Với 3 biến p, q, r: liệt kê p với 4 T rồi 4 F; q với 2 T, 2 F, 2 T, 2 F; r với T, F, T, F, T, F, T, F. Các giá trị luân phiên theo lũy thừa giảm dần của 2.
</div>

## Ví dụ 1: Bảng chân trị cho (p ∧ q) → r

| p | q | r | p ∧ q | (p ∧ q) → r |
|---|---|---|---|-------------|
| T | T | T |   T   |      T      |
| T | T | F |   T   |      F      |
| T | F | T |   F   |      T      |
| T | F | F |   F   |      T      |
| F | T | T |   F   |      T      |
| F | T | F |   F   |      T      |
| F | F | T |   F   |      T      |
| F | F | F |   F   |      T      |

**Phân tích**: Chỉ có hàng thứ hai (p = T, q = T, r = F) làm cho biểu thức sai. Điều này có nghĩa: nếu cả p và q đều đúng mà r lại sai, thì lời hứa "nếu p và q thì r" bị vi phạm.

## Ví dụ 2: Bảng chân trị cho ¬(p ∨ q) ↔ (¬p ∧ ¬q)

| p | q | p ∨ q | ¬(p ∨ q) | ¬p | ¬q | ¬p ∧ ¬q | ¬(p ∨ q) ↔ (¬p ∧ ¬q) |
|---|---|-------|----------|----|----|---------|----------------------|
| T | T |   T   |    F     | F  | F  |    F    |          T           |
| T | F |   T   |    F     | F  | T  |    F    |          T           |
| F | T |   T   |    F     | T  | F  |    F    |          T           |
| F | F |   F   |    T     | T  | T  |    T    |          T           |

**Kết luận**: Biểu thức này luôn đúng (tautology). Đây chính là **định luật De Morgan** — một trong những tương đương quan trọng nhất trong logic!

## Các khái niệm quan trọng

### 1. Tautology (Hằng đúng)
Mệnh đề luôn có giá trị T trong mọi trường hợp.

**Ví dụ**: p ∨ ¬p

| p | ¬p | p ∨ ¬p |
|---|---|----|
| T | F  | T  |
| F | T  | T  |

### 2. Contradiction (Hằng sai)
Mệnh đề luôn có giá trị F trong mọi trường hợp.

**Ví dụ**: p ∧ ¬p

| p | ¬p | p ∧ ¬p |
|---|---|----|
| T | F  | F  |
| F | T  | F  |

### 3. Contingency (Mệnh đề thường)
Mệnh đề có thể đúng hoặc sai tùy thuộc vào giá trị của các biến.

## Những nhầm lẫn thường gặp

**Nhầm lẫn 1 — Quên số dòng**: Với n biến, bảng có 2ⁿ dòng, không phải 2n. Nhiều sinh viên mới học chỉ liệt kê n+1 dòng và bỏ sót tổ hợp.

**Nhầm lẫn 2 — Tính toán sai implication**: Implication (→) **chỉ sai khi p=T và q=F**. Mọi trường hợp khác đều đúng. Đây là lỗi phổ biến nhất.

**Nhầm lẫn 3 — Nhầm thứ tự ưu tiên**: ¬ có độ ưu tiên cao hơn ∧, ∧ cao hơn ∨, ∨ cao hơn →, → cao hơn ↔. Nếu không chắc, hãy dùng dấu ngoặc.

## Ứng dụng của bảng chân trị

### 1. Kiểm tra tính tương đương logic
Hai mệnh đề tương đương nếu chúng có cùng bảng chân trị.

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

Ví dụ: Thiết kế mạch cho (A ∧ B) ∨ C

Bảng chân trị:
| A | B | C | A ∧ B | (A ∧ B) ∨ C |
|---|---|---|---|-------------|
| 0 | 0 | 0 |   0   |      0      |
| 0 | 0 | 1 |   0   |      1      |
| 0 | 1 | 0 |   0   |      0      |
| 0 | 1 | 1 |   0   |      1      |
| 1 | 0 | 0 |   0   |      0      |
| 1 | 0 | 1 |   0   |      1      |
| 1 | 1 | 0 |   1   |      1      |
| 1 | 1 | 1 |   1   |      1      |

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter01/truth_table_diagram.svg" alt="Sơ đồ minh họa cấu trúc bảng chân trị" width="60%" height="60%">
  <figcaption style="text-align: center;">Hình 1.3: Cấu trúc bảng chân trị — cột biến, cột trung gian, cột kết quả</figcaption>
</p>
</figure>

## Công cụ tương tác

<div class="interactive-tool" markdown="1">
### Máy tính bảng chân trị

Nhập biểu thức logic (sử dụng &, |, !, ->, <->) và xem bảng chân trị tự động:

<input type="text" id="logic-expression" placeholder='Ví dụ: (p & q) | r' style="width: 80%; padding: 8px; margin: 10px 0;">
<button onclick="generateTruthTable()">Tạo bảng</button>
<div id="truth-table-result" style="margin-top: 15px;"></div>

<script>
function generateTruthTable() {
    const expression = document.getElementById('logic-expression').value;
    const resultDiv = document.getElementById('truth-table-result');
    
    if (!expression) {
        resultDiv.innerHTML = '<p style="color: #e63946;">Vui lòng nhập biểu thức!</p>';
        return;
    }
    
    // Phân tích biểu thức để tìm biến
    const vars = [...new Set(expression.match(/[a-z]/g) || ['p'])];
    const n = vars.length;
    const rows = Math.pow(2, n);
    
    let html = '<table style="border-collapse: collapse; margin: 10px 0;"><tr>';
    for (const v of vars) html += `<th style="border: 1px solid #ccc; padding: 6px 12px;">${v}</th>`;
    html += '<th style="border: 1px solid #ccc; padding: 6px 12px;">Kết quả</th></tr>';
    
    for (let i = 0; i < rows; i++) {
        html += '<tr>';
        const vals = {};
        for (let j = 0; j < n; j++) {
            const val = (i & Math.pow(2, n-1-j)) !== 0;
            vals[vars[j]] = val;
            html += `<td style="border: 1px solid #ccc; padding: 6px 12px; text-align: center;">${val ? 'T' : 'F'}</td>`;
        }
        // Tính đơn giản - trong thực tế cần parser
        const result = evaluateSimple(expression, vals);
        html += `<td style="border: 1px solid #ccc; padding: 6px 12px; text-align: center; font-weight: bold;">${result ? 'T' : 'F'}</td>`;
        html += '</tr>';
    }
    html += '</table>';
    html += '<p><em>Gợi ý: Hãy thử nhập các biểu thức như (p & q) | r, p -> q, hoặc !(p | q) &lt;-&gt; (!p & !q)</em></p>';
    resultDiv.innerHTML = html;
}

function evaluateSimple(expr, vals) {
    // Thay thế biến bằng giá trị
    let e = expr;
    for (const [v, val] of Object.entries(vals)) {
        e = e.replace(new RegExp(v, 'g'), val ? '1' : '0');
    }
    // Chuyển ký hiệu
    e = e.replace(/1/g, 'true').replace(/0/g, 'false');
    e = e.replace(/&/g, '&&').replace(/\|/g, '||').replace(/!/g, '!');
    e = e.replace(/->/g, ') <= false || ('); // đơn giản hóa
    try {
        return eval(e);
    } catch {
        return null;
    }
}
</script>
</div>

## Bài tập thực hành

### Bài tập 1: Xây dựng bảng chân trị
Xây dựng bảng chân trị cho các biểu thức sau:
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

Viết biểu thức logic và tạo bảng chân trị cho hệ thống này.

### Bài tập 4: Bảng chân trị cho kiểm thử phần mềm

Một hệ thống cho phép sinh viên xem điểm nếu:

- $$p$$: Sinh viên đã đăng nhập.
- $$q$$: Sinh viên thuộc lớp học phần.
- $$r$$: Giảng viên đã công bố điểm.

Điều kiện: $$p \land q \land r$$.

1. Lập bảng chân trị đầy đủ.
2. Từ bảng đó, chọn ít nhất 4 test case quan trọng.
3. Giải thích vì sao test case "đã đăng nhập nhưng không thuộc lớp" cần được kiểm thử.

### Bài tập 5: So sánh hai điều kiện phân quyền

Kiểm tra bằng bảng chân trị xem hai biểu thức sau có tương đương không:

$$p \lor (q \land \neg r)$$

$$(p \lor q) \land \neg r$$

Trong đó $$p$$ là "admin", $$q$$ là "owner", $$r$$ là "resource locked". Nếu không tương đương, hãy chỉ ra một hàng làm phản ví dụ.


