---
layout: post
title: "Phép toán Logic"
categories: chapter01
date: 2021-01-01
order: 2
required: true
lang: en
---

# Phép toán Logic

Ở bài trước, chúng ta đã biết mệnh đề là gì và vì sao mỗi phát biểu logic đều phải gắn với giá trị đúng hoặc sai. Nhưng trong thế giới thực, hệ thống hiếm khi phải ra quyết định chỉ dựa trên **một** điều kiện duy nhất.

Một website chỉ cho đăng nhập khi **mật khẩu đúng và tài khoản chưa bị khóa**. Một đơn hàng được giảm giá nếu **khách là thành viên VIP hoặc có mã khuyến mãi**. Một API chỉ cho truy cập nếu **người dùng đã xác thực và có quyền tương ứng**. Khi đó, bài toán không còn là "mệnh đề này đúng hay sai?" mà trở thành:

- Làm sao **ghép nhiều điều kiện** lại với nhau?
- Làm sao hiểu đúng giữa **và**, **hoặc**, **không** trong ngữ cảnh logic?
- Làm sao tránh những lỗi rất nhỏ trong biểu thức nhưng gây hậu quả rất lớn ngoài đời thực?

Đây chính là lúc các **phép toán logic** xuất hiện. Chúng là những "khớp nối" đứng sau `if`, `while`, bộ lọc tìm kiếm, kiểm soát truy cập, luật nghiệp vụ, hệ thống cảnh báo và hàng loạt quyết định tự động trong phần mềm hiện đại.

Điều thú vị là: nhiều lỗi nghiêm trọng trong hệ thống không đến từ thuật toán quá khó, mà đến từ những điều kiện tưởng như rất quen thuộc. Chỉ cần nhầm `and` với `or`, quên một dấu ngoặc, hay hiểu sai mệnh đề kéo theo, bạn có thể vô tình:

- mở nhầm quyền cho người dùng không hợp lệ,
- từ chối giao dịch hợp lệ,
- bỏ sót trường hợp kiểm thử,
- hoặc tạo ra bug logic rất khó phát hiện.

Vì vậy, học các phép toán logic không phải để thuộc ký hiệu cho đẹp, mà để **đọc đúng yêu cầu, viết đúng điều kiện và suy luận đúng hành vi của chương trình**. Trong bài học này, chúng ta sẽ lần lượt khám phá những phép nối cơ bản nhất của tư duy logic: phủ định, hội, tuyển, XOR, kéo theo và tương đương.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Sử dụng** chính xác các phép toán NOT, AND, OR, XOR, IF...THEN, IF AND ONLY IF.
- **Đọc** một điều kiện lập trình và chuyển nó sang ký hiệu logic.
- **Giải thích** vì sao mệnh đề kéo theo $$p \to q$$ đúng khi $$p$$ sai.
- **Phân biệt** OR bao hàm và XOR trong ngôn ngữ tự nhiên.
- **Áp dụng** các phép toán logic vào kiểm tra đầu vào, phân quyền, truy vấn dữ liệu và test case.

**Từ khóa**: NOT, AND, OR, XOR, implication, biconditional, truth value, condition, access control.

## Câu chuyện mở đầu: Điều kiện đăng nhập

<div class="content-box example-box" markdown="1">
Một hệ thống chỉ cho phép đăng nhập nếu:

- Người dùng nhập đúng mật khẩu.
- Tài khoản chưa bị khóa.
- Nếu đăng nhập từ thiết bị lạ thì phải nhập mã OTP.

Ký hiệu:

- $$p$$: Mật khẩu đúng.
- $$q$$: Tài khoản chưa bị khóa.
- $$r$$: Thiết bị lạ.
- $$s$$: OTP đúng.

Điều kiện đăng nhập:

$$p \land q \land (\neg r \lor s)$$

Trong code:

```python
can_login = correct_password and account_active and (not unknown_device or correct_otp)
```

Nếu bỏ dấu ngoặc, chương trình vẫn chạy nhưng có thể cho phép hoặc từ chối sai người dùng.
</div>

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

**Phủ định bất đẳng thức**: Khi phủ định một bất đẳng thức, ta đảo ngược dấu so sánh:
- Phủ định của $$n > 5$$ là $$n \leq 5$$
- Phủ định của $$x \geq 0$$ là $$x < 0$$
- Phủ định của $$a = b$$ là $$a \neq b$$

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**: Nhiều sinh viên viết phủ định của "n > 5" là "n < 5". Sai! Phủ định của "lớn hơn" phải là "nhỏ hơn hoặc bằng".
</div>

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

**Ví dụ trong lập trình**:

```python
if order_total >= 500000 and customer_tier == "vip":
    apply_discount()
```

Điều kiện chỉ đúng khi **cả hai** điều kiện con đều đúng. Đây là dạng phổ biến trong thương mại điện tử: đủ giá trị đơn hàng và đúng loại khách hàng.

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

**Ví dụ trong tìm kiếm**:

```sql
SELECT * FROM products
WHERE category = 'Laptop' OR category = 'Tablet';
```

Kết quả gồm sản phẩm thuộc ít nhất một trong hai loại. Trong logic toán, OR thường là **OR bao hàm**: nếu một sản phẩm thỏa cả hai điều kiện thì vẫn được chọn.

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

<div class="content-box insight-box" markdown="1">
**Tại sao p → q lại đúng khi p sai?** Đây là câu hỏi khiến nhiều sinh viên bối rối. Hãy nghĩ thế này: "Nếu trời mưa thì đường ướt." Câu này chỉ bị vi phạm nếu trời mưa (p đúng) mà đường không ướt (q sai). Nếu trời không mưa (p sai), câu nói không bị vi phạm dù đường có ướt hay không — ta không thể kết luận gì về nó.
</div>

**Ví dụ thực tế**: Quy định "Nếu sinh viên đạt từ 5 điểm trở lên thì qua môn". Với sinh viên không đạt từ 5 điểm trở lên, quy định này không bị vi phạm dù sinh viên đó qua hay rớt theo một điều kiện đặc biệt khác. Mệnh đề kéo theo chỉ bị sai khi giả thiết đúng nhưng kết luận sai.

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

**Ví dụ**: "Bạn có thể chọn trà **hoặc** cà phê" (ngụ ý không thể uống cả hai) — đây là XOR trong ngôn ngữ tự nhiên. OR thông thường (bao hàm) cho phép cả hai.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter01/logic_gates.svg" alt="Biểu diễn các cổng logic AND, OR, NOT qua mạch điện" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 1.2: Các cổng logic (logic gates) — mỗi phép toán logic tương ứng với một cổng trong mạch số</figcaption>
</p>
</figure>

## Tổng kết năm phép toán cơ bản

| Phép toán | Ký hiệu | Đọc là | Đúng khi |
|:---------|:-------:|:-------|:---------|
| Phủ định (Negation) | $$\neg p$$ | không p | p sai |
| Hội (Conjunction) | $$p \land q$$ | p và q | cả p và q đều đúng |
| Tuyển (Disjunction) | $$p \lor q$$ | p hay q | ít nhất một đúng |
| Kéo theo (Implication) | $$p \to q$$ | nếu p thì q | không xảy ra p đúng q sai |
| Tương đương (Biconditional) | $$p \leftrightarrow q$$ | p khi và chỉ khi q | p và q cùng chân trị |

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

## Những lỗi thường gặp

**Lỗi 1 — Nhầm OR bao hàm với XOR**: Trong tiếng Việt, từ "hoặc" đôi khi mang nghĩa bao hàm (một trong hai hoặc cả hai), đôi khi mang nghĩa loại trừ (chỉ một trong hai). Trong logic toán, mặc định OR là bao hàm (∨). XOR (⊕) phải được chỉ định rõ.

**Lỗi 2 — Hiểu sai implication**: Nhiều sinh viên nghĩ p → q có nghĩa là "p kéo theo q" theo quan hệ nhân quả. Thực ra nó chỉ là quan hệ về giá trị chân lý, không phải quan hệ nguyên nhân – kết quả. "Nếu 1+1=3 thì tôi là tổng thống" là một mệnh đề đúng (vì giả thiết sai), dù không có quan hệ nhân quả nào.

**Lỗi 3 — Quên dấu ngoặc**: `p ∧ q ∨ r` không có nghĩa rõ ràng nếu không có dấu ngoặc. Luật ưu tiên giúp, nhưng dùng dấu ngoặc luôn an toàn hơn.

<div class="interactive-tool" markdown="1">
### Công cụ tương tác: Tính giá trị biểu thức logic

Nhập giá trị cho p, q, r (T hoặc F) và xem kết quả của biểu thức:

<p>
  p: <select id="val-p"><option value="T">T</option><option value="F">F</option></select>
  q: <select id="val-q"><option value="T">T</option><option value="F">F</option></select>
  r: <select id="val-r"><option value="T">T</option><option value="F">F</option></select>
</p>
<p>Biểu thức: <code>(p ∧ q) → (¬r ∨ q)</code></p>
<button onclick="evalLogicExpr()">Tính</button>
<div id="logic-expr-result" style="margin-top: 10px; padding: 10px; background: #f8f9fa; border-radius: 6px;"></div>

<script>
function evalLogicExpr() {
    const p = document.getElementById('val-p').value === 'T';
    const q = document.getElementById('val-q').value === 'T';
    const r = document.getElementById('val-r').value === 'T';
    // (p ∧ q) → (¬r ∨ q)
    const left = p && q;
    const right = !r || q;
    const result = (!left) || right;
    document.getElementById('logic-expr-result').innerHTML =
        `<strong>Kết quả:</strong> ${result ? 'T (đúng)' : 'F (sai)'} <br>` +
        `<small>(p∧q) = ${left ? 'T' : 'F'}, (¬r∨q) = ${right ? 'T' : 'F'}</small>`;
}
</script>
</div>

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

### Bài tập 3: Điều kiện phân quyền

Một hệ thống cho phép người dùng sửa bài viết nếu:

- Người dùng là admin, hoặc
- Người dùng là tác giả bài viết và bài viết chưa bị khóa.

1. Đặt ký hiệu cho từng mệnh đề sơ cấp.
2. Viết biểu thức logic cho điều kiện trên.
3. Viết điều kiện bằng Python hoặc JavaScript.

### Bài tập 4: Tìm lỗi logic

Lập trình viên viết:

```python
can_edit = is_admin or is_author and not is_locked
```

1. Theo thứ tự ưu tiên toán tử trong Python, biểu thức này được hiểu như thế nào?
2. Hãy thêm dấu ngoặc để biểu thức rõ nghĩa.
3. Nếu yêu cầu đổi thành "admin cũng không được sửa bài đã khóa", biểu thức mới là gì?

## Tóm tắt

Các phép toán logic cơ bản:
- **¬p**: phủ định (NOT)
- **p ∧ q**: hội (AND)
- **p ∨ q**: tuyển (OR)
- **p → q**: kéo theo (IF...THEN)
- **p ↔ q**: tương đương (IF AND ONLY IF)
- **p ⊕ q**: tuyển loại trừ (XOR)
- Thứ tự ưu tiên: ¬ > ∧ > ∨ > → > ↔
- Implication chỉ sai khi giả thiết đúng và kết luận sai

Trong bài tiếp theo, chúng ta sẽ học về **bảng chân trị** và cách sử dụng chúng để phân tích các mệnh đề phức tạp.
