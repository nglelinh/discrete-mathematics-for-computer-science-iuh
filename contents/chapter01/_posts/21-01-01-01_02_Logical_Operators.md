---
layout: post
title: "Phép toán Logic"
categories: chapter01
date: 2021-01-01
order: 2
required: true
lang: en
---

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

## Phân loại mệnh đề

Mệnh đề trong logic được phân thành hai loại:

### Mệnh đề sơ cấp (nguyên thủy)

**Định nghĩa**: Một **mệnh đề sơ cấp** (hay mệnh đề nguyên thủy) là mệnh đề **không thể xây dựng từ các mệnh đề khác** thông qua các liên từ logic hoặc trạng từ "không".

**Đặc điểm**:
- Không chứa phép toán logic (∧, ∨, ¬, →, ↔).
- Là đơn vị cơ bản nhất trong hệ thống logic.
- Được ký hiệu bằng chữ cái thường: `p`, `q`, `r`, `s`, ...

**Ví dụ**:
- "Hôm nay trời nắng"
- "2 + 3 = 5"
- "Tôi có tiền"
- "Cửa hàng mở cửa"

### Mệnh đề phức hợp

**Định nghĩa**: Một **mệnh đề phức hợp** là mệnh đề **được xây dựng từ các mệnh đề khác** nhờ liên kết bằng các **liên từ** (và, hay, khi và chỉ khi, …) hoặc **trạng từ "không"**.

**Đặc điểm**:
- Chứa ít nhất một phép toán logic.
- Được tạo thành từ mệnh đề sơ cấp thông qua các phép nối.
- Có thể phân tích thành các thành phần nhỏ hơn.

**Ví dụ**:
- "Tôi có tiền **và** cửa hàng mở cửa" → `p ∧ q`
- "Trời mưa **hoặc** đường ướt" → `p ∨ q`
- "**Không** phải hôm nay trời nắng" → `¬p`
- "Nếu trời mưa **thì** đường ướt" → `p → q`

<div class="content-box insight-box" markdown="1">
**Lưu ý**: Việc phân loại mệnh đề sơ cấp và phức hợp giúp ta xác định được đâu là "nguyên tử" và đâu là "phân tử" trong biểu thức logic. Khi phân tích điều kiện trong code, ta luôn bắt đầu bằng việc xác định các mệnh đề sơ cấp trước khi ghép chúng bằng các phép toán.
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

**Phủ định bất đẳng thức** (cách làm trực quan):

Khi phủ định một bất đẳng thức, ta làm theo **3 bước đơn giản**:

1. Giữ nguyên biến.
2. Đảo ngược dấu so sánh.
3. Viết kết quả.

**Bảng quy tắc nhanh**:

| Biểu thức gốc | Phủ định | Ghi nhớ |
|:---:|:---:|:---|
| $$n > 5$$ | $$n \leq 5$$ | Lớn hơn → nhỏ hơn hoặc bằng |
| $$x \geq 0$$ | $$x < 0$$ | Lớn hơn hoặc bằng → nhỏ hơn |
| $$a = b$$ | $$a \neq b$$ | Bằng → khác |
| $$x < 3$$ | $$x \geq 3$$ | Nhỏ hơn → lớn hơn hoặc bằng |

**Ví dụ thực tế**:

- "Tuổi lớn hơn 18" → Phủ định: "Tuổi nhỏ hơn hoặc bằng 18"
- "Điểm số >= 5" → Phủ định: "Điểm số < 5"

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

![Biểu đồ Venn: phép AND (∧)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-AND.png)

*Hình 1.7: Phép hội p ∧ q — chỉ đúng khi cả p và q đều đúng (vùng giao trên biểu đồ Venn).*

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

### Cách nhớ trực quan (OR)

OR đúng khi **ít nhất một** cái đúng. Dễ nhớ bằng quy tắc:

> "Một cái đúng → cả OR đúng"

### Bảng chân trị:

| p | q | p ∨ q |
|:---:|:---:|:---:|
| T | T | T | 
| T | F | T | 
| F | T | T | 
| F | F | F | 

![Biểu đồ Venn: phép OR (∨)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-OR.png)

*Hình 1.8: Phép tuyển p ∨ q — đúng khi ít nhất một trong hai mệnh đề đúng (OR bao hàm).*

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

![Biểu đồ Venn: mệnh đề kéo theo (→)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-Implication.PNG)

*Hình 1.9: Mệnh đề kéo theo p → q — chỉ sai khi p đúng mà q sai; khi p sai thì luôn đúng (vacuously true).*

![Biểu đồ Venn: phép XOR (⊕)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-XOR.png)

*Hình 1.10: Phép XOR p ⊕ q — đúng khi đúng đúng một trong hai mệnh đề (loại trừ lẫn nhau).*

![Luật De Morgan trên biểu đồ Venn](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

*Hình 1.11: Luật De Morgan — ¬(p ∧ q) ≡ ¬p ∨ ¬q và ¬(p ∨ q) ≡ ¬p ∧ ¬q, rất quan trọng khi viết điều kiện phủ định trong code.*

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

## Biểu thức logic

**Biểu thức logic** (logical expression) là sự kết hợp của các mệnh đề sơ cấp bằng các phép toán logic (¬, ∧, ∨, →, ↔, ⊕) và dấu ngoặc.

### Cú pháp biểu thức logic

Một biểu thức logic được xây dựng theo quy tắc:

- Mọi mệnh đề sơ cấp (p, q, r,...) là biểu thức logic.
- Nếu E là biểu thức logic thì ¬E cũng là biểu thức logic.
- Nếu E₁ và E₂ là biểu thức logic thì (E₁ ∧ E₂), (E₁ ∨ E₂), (E₁ → E₂), (E₁ ↔ E₂), (E₁ ⊕ E₂) cũng là biểu thức logic.

**Ví dụ biểu thức logic**:
- $$p \land q$$
- $$\neg p \lor (q \land r)$$
- $$(p \to q) \land (q \to p)$$
- $$p \oplus (q \land \neg r)$$

### Thứ tự ưu tiên toán tử

Khi viết biểu thức không có dấu ngoặc, thứ tự thực hiện là:

| Ưu tiên | Toán tử | Tên |
|:---:|:---|:---|
| 1 (cao nhất) | ¬ | Phủ định |
| 2 | ∧ | Hội |
| 3 | ∨ | Tuyển |
| 4 | → | Kéo theo |
| 5 | ↔ | Tương đương |
| 6 (thấp nhất) | ⊕ | XOR |

**Ví dụ**: $$p \land q \lor r$$ được hiểu là $$(p \land q) \lor r$$ (không phải $$p \land (q \lor r)$$).

<div class="content-box warning-box" markdown="1">
**Lưu ý**: Luôn dùng dấu ngoặc để biểu thức rõ ràng, tránh nhầm lẫn khi chuyển sang code.
</div>

## Bảng chân trị cho biểu thức phức hợp

Bảng chân trị không chỉ dùng cho từng phép toán riêng lẻ, mà còn dùng để phân tích toàn bộ biểu thức logic.

### Cách xây dựng bảng chân trị

**Bước 1**: Xác định số biến (n). Bảng có $$2^n$$ dòng.

**Bước 2**: Liệt kê tất cả tổ hợp giá trị chân lý của các biến.

**Bước 3**: Tính giá trị từng biểu thức con, từ trong ra ngoài.

**Bước 4**: Xác định giá trị cuối cùng của biểu thức.

### Ví dụ: Biểu thức $$(p \land q) \lor \neg r$$

| p | q | r | p ∧ q | ¬r | (p ∧ q) ∨ ¬r |
|---|---|---|-------|----|--------------|
| T | T | T | T     | F  | T            |
| T | T | F | T     | T  | T            |
| T | F | T | F     | F  | F            |
| T | F | F | F     | T  | T            |
| F | T | T | F     | F  | F            |
| F | T | F | F     | T  | T            |
| F | F | T | F     | F  | F            |
| F | F | F | F     | T  | T            |

Biểu thức đúng trong 4/8 trường hợp.

## Biểu thức tương đương

Hai biểu thức logic **E₁** và **E₂** là **tương đương** (logically equivalent) nếu chúng có cùng giá trị chân lý trong mọi trường hợp. Ký hiệu: $$E_1 \equiv E_2$$.

### Cách chứng minh tương đương

**Phương pháp 1 — Bảng chân trị**: Xây dựng bảng chân trị cho cả hai biểu thức, so sánh cột cuối cùng.

**Phương pháp 2 — Luật logic**: Biến đổi biểu thức này thành biểu thức kia bằng các luật logic (xem phần sau).

### Ví dụ: $$p \to q \equiv \neg p \lor q$$

Chứng minh bằng bảng chân trị:

| p | q | p → q | ¬p | ¬p ∨ q |
|---|---|-------|----|--------|
| T | T | T     | F  | T      |
| T | F | F     | F  | F      |
| F | T | T     | T  | T      |
| F | F | T     | T  | T      |

Hai cột cuối cùng giống hệt → hai biểu thức **tương đương**.

**Ý nghĩa thực tiễn**: Khi code, ta có thể thay `if p then q` bằng `not p or q` tùy ngữ cảnh.

## Các luật logic cơ bản

Dưới đây là các luật logic thường dùng để biến đổi biểu thức:

### 1. Luật phủ định kép (Double Negation)

$$\neg (\neg p) \equiv p$$

### 2. Luật De Morgan

$$\neg (p \land q) \equiv \neg p \lor \neg q$$
$$\neg (p \lor q) \equiv \neg p \land \neg q$$

**Ví dụ**: Phủ định của "Tôi có tiền và cửa hàng mở cửa" là "Tôi không có tiền HOẶC cửa hàng không mở cửa".

### 3. Luật giao hoán (Commutative)

$$p \land q \equiv q \land p$$
$$p \lor q \equiv q \lor p$$

### 4. Luật kết hợp (Associative)

$$(p \land q) \land r \equiv p \land (q \land r)$$
$$(p \lor q) \lor r \equiv p \lor (q \lor r)$$

### 5. Luật phân phối (Distributive)

$$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$
$$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$

### 6. Luật hấp thụ (Absorption)

$$p \land (p \lor q) \equiv p$$
$$p \lor (p \land q) \equiv p$$

### 7. Luật đồng nhất (Identity)

$$p \land T \equiv p$$
$$p \lor F \equiv p$$

### 8. Luật triệt tiêu (Domination)

$$p \land F \equiv F$$
$$p \lor T \equiv T$$

### 9. Luật bổ sung (Complement)

$$p \land \neg p \equiv F$$
$$p \lor \neg p \equiv T$$

<div class="content-box insight-box" markdown="1">
**Mẹo nhớ De Morgan**: Khi phủ định một biểu thức có ngoặc, đổi dấu ngoặc thành dấu kia VÀ phủ định từng thành phần bên trong.
</div>

## Ví dụ: Trang danh sách sản phẩm

### Yêu cầu lọc sản phẩm

Một trang thương mại điện tử có các bộ lọc:

- Danh mục: Điện thoại HOẶC Máy tính bảng
- Giá: Từ 5 triệu đến 15 triệu
- Thương hiệu: Samsung HOẶC Apple
- Còn hàng: true
- Đánh giá: ≥ 4 sao HOẶC có ≥ 100 lượt đánh giá

### Biểu thức logic

Ký hiệu:
- $$p$$: Danh mục là Điện thoại
- $$q$$: Danh mục là Máy tính bảng
- $$r$$: Giá ∈ [5tr, 15tr]
- $$s$$: Thương hiệu Samsung
- $$t$$: Thương hiệu Apple
- $$u$$: Còn hàng
- $$v$$: Đánh giá ≥ 4 sao
- $$w$$: Số lượt đánh giá ≥ 100

**Điều kiện lọc**:

$$(p \lor q) \land r \land (s \lor t) \land u \land (v \lor w)$$

### Code JavaScript

```javascript
const filteredProducts = products.filter(product => {
  const categoryMatch = product.category === 'phone' || product.category === 'tablet';
  const priceMatch = product.price >= 5000000 && product.price <= 15000000;
  const brandMatch = product.brand === 'Samsung' || product.brand === 'Apple';
  const inStock = product.inStock === true;
  const ratingMatch = product.rating >= 4 || product.reviewCount >= 100;
  
  return categoryMatch && priceMatch && brandMatch && inStock && ratingMatch;
});
```

**Nhận xét**: Nếu nhầm `&&` với `||` ở điều kiện giá, kết quả lọc sẽ sai hoàn toàn.

## Ví dụ: Validator trong web form

### Yêu cầu kiểm tra form đăng ký

Form yêu cầu:
- Tên không được rỗng
- Email hợp lệ (xem phần sau)
- Mật khẩu ≥ 8 ký tự VÀ chứa ít nhất 1 chữ hoa VÀ 1 chữ số
- Xác nhận mật khẩu trùng với mật khẩu
- Đồng ý điều khoản: true

### Biểu thức logic

Ký hiệu:
- $$p$$: Tên ≠ rỗng
- $$q$$: Email hợp lệ
- $$r$$: Mật khẩu ≥ 8 ký tự
- $$s$$: Mật khẩu chứa chữ hoa
- $$t$$: Mật khẩu chứa chữ số
- $$u$$: Xác nhận mật khẩu = mật khẩu
- $$v$$: Đồng ý điều khoản

**Điều kiện submit**:

$$p \land q \land (r \land s \land t) \land u \land v$$

### Code JavaScript

```javascript
function validateForm(formData) {
  const errors = [];
  
  if (!formData.name) errors.push("Tên không được rỗng");
  if (!isValidEmail(formData.email)) errors.push("Email không hợp lệ");
  if (formData.password.length < 8) errors.push("Mật khẩu ≥ 8 ký tự");
  if (!/[A-Z]/.test(formData.password)) errors.push("Mật khẩu cần chữ hoa");
  if (!/[0-9]/.test(formData.password)) errors.push("Mật khẩu cần chữ số");
  if (formData.password !== formData.confirmPassword) errors.push("Mật khẩu không khớp");
  if (!formData.agreeTerms) errors.push("Bạn phải đồng ý điều khoản");
  
  return errors.length === 0 ? { valid: true } : { valid: false, errors };
}
```

## Validator email

### Yêu cầu kiểm tra email

Email hợp lệ nếu:
- Có đúng 1 ký tự `@`
- Phần trước `@` không rỗng VÀ chỉ chứa chữ cái, chữ số, dấu chấm, gạch dưới
- Phần sau `@` có ít nhất 1 dấu chấm VÀ kết thúc bằng domain hợp lệ (.com, .vn, .org,...)

### Biểu thức logic (đơn giản hóa)

Ký hiệu:
- $$p$$: Có đúng 1 `@`
- $$q$$: Phần local không rỗng
- $$r$$: Phần local chỉ chứa ký tự hợp lệ
- $$s$$: Phần domain có ≥ 1 dấu chấm
- $$t$$: Domain kết thúc bằng TLD hợp lệ

**Điều kiện email hợp lệ**:

$$p \land q \land r \land s \land t$$

### Code JavaScript (regex + logic)

```javascript
function isValidEmail(email) {
  // Bước 1: Kiểm tra cấu trúc cơ bản bằng regex
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) return false;
  
  const [localPart, domain] = email.split('@');
  
  // Bước 2: Kiểm tra phần local
  const localValid = localPart.length > 0 && /^[a-zA-Z0-9._]+$/.test(localPart);
  
  // Bước 3: Kiểm tra phần domain
  const domainParts = domain.split('.');
  const domainValid = domainParts.length >= 2 && 
                      domainParts.every(part => part.length > 0) &&
                      ['com', 'vn', 'org', 'net', 'edu'].includes(domainParts[domainParts.length - 1]);
  
  return localValid && domainValid;
}

// Test cases
console.log(isValidEmail("user@example.com"));      // true
console.log(isValidEmail("user.name@domain.vn"));   // true
console.log(isValidEmail("user@domain"));           // false (thiếu TLD)
console.log(isValidEmail("@example.com"));          // false (local rỗng)
console.log(isValidEmail("user@@example.com"));     // false (nhiều @)
```

<div class="content-box insight-box" markdown="1">
**Lưu ý**: Validator email thực tế phức tạp hơn nhiều (RFC 5321). Ví dụ trên chỉ minh họa cách dùng logic mệnh đề để phân rã yêu cầu.
</div>

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

### Bài tập 5: Chứng minh tương đương logic

**Ví dụ**: Cho `p`, `q`, `r` là các biến mệnh đề. Chứng minh rằng:

$$(\neg p \to r) \land (q \to r) \iff (p \to q) \to r$$

**Giải**:

**Phương pháp 1: Bảng chân trị (8 dòng)**

| p | q | r | ¬p | ¬p → r | q → r | (¬p → r) ∧ (q → r) | p → q | (p → q) → r | Kết quả |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | T | T | T | T | T | T |
| T | T | F | F | T | T | T | T | F | F |
| T | F | T | F | T | T | T | F | T | T |
| T | F | F | F | T | F | F | F | T | F |
| F | T | T | T | T | T | T | T | T | T |
| F | T | F | T | F | T | F | T | F | F |
| F | F | T | T | T | T | T | T | T | T |
| F | F | F | T | F | T | F | T | F | F |

**Kết luận**: Hai vế có cùng cột chân trị → tương đương.

**Phương pháp 2: Luật tương đương (phân tích từng bước)**

Bước 1: Viết vế trái theo định nghĩa kéo theo
$$(\neg p \to r) \equiv (p \lor r)$$
$$(q \to r) \equiv (\neg q \lor r)$$

Bước 2: Vế trái trở thành
$$(p \lor r) \land (\neg q \lor r) \equiv (p \land \neg q) \lor r$$ (phân phối)

Bước 3: Vế phải
$$(p \to q) \to r \equiv (\neg p \lor q) \to r \equiv \neg(\neg p \lor q) \lor r \equiv (p \land \neg q) \lor r$$

Bước 4: Hai vế bằng nhau → chứng minh xong.

<div class="content-box example-box" markdown="1">
**Lưu ý**: Khi gặp bài tập chứng minh tương đương, sinh viên có thể chọn:
- Bảng chân trị (luôn đúng, nhưng dài)
- Luật tương đương (ngắn gọn hơn, cần nắm vững các luật)
</div>

### Bài tập 6: Mệnh đề kéo theo trong đời thường

Cho các mệnh đề:

- $$p$$: "Bạn chăm chỉ học tập"
- $$q$$: "Bạn đạt điểm cao"
- $$r$$: "Bạn có việc làm tốt"
- $$s$$: "Bạn hài lòng với cuộc sống"

Viết các câu sau dưới dạng ký hiệu logic:

(a) "Nếu bạn chăm chỉ học tập thì bạn đạt điểm cao."
(b) "Chỉ khi bạn đạt điểm cao bạn mới có việc làm tốt."
(c) "Bạn có việc làm tốt là đủ để bạn hài lòng với cuộc sống."
(d) "Bạn chăm chỉ học tập là cần thiết để đạt điểm cao."
(e) "Nếu không chăm chỉ thì không đạt điểm cao, và nếu không đạt điểm cao thì không có việc làm tốt."

<details>
<summary>Đáp án</summary>

(a) $$p \to q$$ — Nếu p thì q.

(b) $$q \to r$$ — "Chỉ khi q mới r" tương đương "r kéo theo q". Thực chất: nếu có việc làm tốt thì phải có điểm cao, tức $$r \to q$$.
    Cần phân biệt: "q là điều kiện cần cho r" = $$r \to q$$.

(c) $$r \to s$$ — "r là đủ để s" = $$r \to s$$.

(d) $$p \to q$$ — "p là cần thiết cho q" nghĩa là không thể có q nếu không có p, tức $$q \to p$$.
    Chính xác: "p là cần thiết cho q" = "nếu q thì p" = $$q \to p$$.
    
    Vậy đáp án đúng: $$q \to p$$ (không phải $$p \to q$$ — đây là lỗi thường gặp!).

(e) $$\neg p \to \neg q$$ và $$\neg q \to \neg r$$.
    Kết hợp: $$(\neg p \to \neg q) \land (\neg q \to \neg r)$$.
    Theo tam đoạn luận giả định: $$\neg p \to \neg r$$ (nếu không chăm chỉ thì không có việc làm tốt).

</details>

### Bài tập 7: XOR vs OR trong thực tế

Trong mỗi tình huống sau, "hoặc" được dùng theo nghĩa OR bao hàm (inclusive) hay XOR (loại trừ)? Giải thích.

(a) "Sinh viên được nhận học bổng nếu có điểm trung bình >= 8.0 hoặc có thành tích nghiên cứu."
(b) "Bạn có thể chọn thanh toán bằng thẻ tín dụng hoặc chuyển khoản."
(c) "Hệ thống cảnh báo nếu nhiệt độ > 100°C hoặc áp suất < 1 atm."
(d) "Trong trận đấu, đội thắng được 3 điểm, đội hòa được 1 điểm, hoặc đội thua được 0 điểm."
(e) "Để đăng nhập, bạn cần nhập đúng tên người dùng và mật khẩu, hoặc sử dụng xác thực vân tay."

<details>
<summary>Đáp án</summary>

(a) **OR bao hàm** — Sinh viên có thể vừa có điểm cao vừa có nghiên cứu, và vẫn nhận học bổng. Cả hai đều đúng thì kết quả vẫn đúng.

(b) **XOR** — Bạn thường chỉ được chọn một phương thức thanh toán, không thể cả hai. Trong giao diện, đây thường là nút radio, không phải checkbox.

(c) **OR bao hàm** — Cả hai điều kiện có thể xảy ra cùng lúc và hệ thống vẫn cảnh báo. Một cảnh báo vẫn là cảnh báo, dù có nhiều lý do.

(d) **XOR** — Một đội chỉ nhận được một kết quả duy nhất. Không thể vừa thắng vừa hòa. Ba trường hợp loại trừ lẫn nhau.

(e) **OR bao hàm** — Người dùng có thể vừa nhập đúng tên/mật khẩu vừa có vân tay, và vẫn đăng nhập được. Hệ thống thường chấp nhận cả hai.

</details>

### Bài tập 8: Biểu diễn điều kiện phức hợp bằng Python

Viết hàm Python cho mỗi yêu cầu sau, sử dụng các phép toán logic:

(a) `can_publish(post)` — Bài viết được đăng nếu đã được duyệt (reviewed) VÀ (nội dung đã hoàn chỉnh HOẶC tác giả là editor).

(b) `should_send_alert(system)` — Cảnh báo được gửi nếu (CPU > 90% HOẶC memory > 85%) VÀ không phải giờ bảo trì.

(c) `is_eligible_for_scholarship(student)` — Sinh viên đủ điều kiện nếu (GPA >= 3.5 VÀ không bị kỷ luật) HOẶC có giải thưởng đặc biệt.

<details>
<summary>Đáp án</summary>

```python
def can_publish(post):
    """Bài viết được đăng nếu đã duyệt và (hoàn chỉnh hoặc tác giả là editor)"""
    return post['reviewed'] and (post['complete'] or post['is_editor'])

# Test cases
print(can_publish({'reviewed': True, 'complete': True, 'is_editor': False}))   # True
print(can_publish({'reviewed': True, 'complete': False, 'is_editor': True}))   # True
print(can_publish({'reviewed': True, 'complete': False, 'is_editor': False}))  # False
print(can_publish({'reviewed': False, 'complete': True, 'is_editor': False}))  # False

def should_send_alert(system):
    """Cảnh báo nếu (CPU > 90% hoặc memory > 85%) và không phải giờ bảo trì"""
    high_load = system['cpu'] > 90 or system['memory'] > 85
    return high_load and not system['maintenance_hour']

print(should_send_alert({'cpu': 95, 'memory': 80, 'maintenance_hour': False}))  # True
print(should_send_alert({'cpu': 80, 'memory': 90, 'maintenance_hour': True}))   # False
print(should_send_alert({'cpu': 50, 'memory': 50, 'maintenance_hour': False}))  # False

def is_eligible_for_scholarship(student):
    """Học bổng nếu (GPA >= 3.5 và không kỷ luật) hoặc có giải thưởng"""
    good_grades = student['gpa'] >= 3.5
    no_discipline = not student['has_discipline']
    return (good_grades and no_discipline) or student['has_award']

print(is_eligible_for_scholarship({'gpa': 3.7, 'has_discipline': False, 'has_award': False}))  # True
print(is_eligible_for_scholarship({'gpa': 3.7, 'has_discipline': True, 'has_award': False}))   # False
print(is_eligible_for_scholarship({'gpa': 3.0, 'has_discipline': False, 'has_award': True}))    # True
```

</details>

### Bài tập 9: Dịch biểu thức logic thành câu tự nhiên

Cho các mệnh đề:
- $$a$$: "Tài khoản là admin"
- $$m$$: "Tài khoản là moderator"
- $$b$$: "Tài khoản bị khóa"
- $$v$$: "Tài khoản đã xác thực email"

Diễn giải các biểu thức sau thành câu tự nhiên:

(a) $$(a \lor m) \land \neg b$$
(b) $$v \to (a \lor m)$$
(c) $$(a \lor m) \leftrightarrow \neg b$$
(d) $$(a \land \neg b) \lor (m \land v)$$
(e) $$\neg v \to b$$

<details>
<summary>Đáp án</summary>

(a) "Tài khoản là admin hoặc moderator, và không bị khóa." — Điều kiện để có quyền truy cập đặc biệt.

(b) "Nếu tài khoản đã xác thực email thì nó là admin hoặc moderator." — Chỉ admin/moderator mới bắt buộc xác thực email? (Điều này có vẻ ngược — thực tế thường tất cả tài khoản đều cần xác thực. Đây là tình huống giả định.)

(c) "Tài khoản là admin hoặc moderator nếu và chỉ nếu nó không bị khóa." — Mọi tài khoản không bị khóa đều là admin/moderator (hơi vô lý!), hoặc mọi admin/moderator đều không bị khóa. Đây là bài học về việc đọc kỹ biểu thức: thực tế chiều $$\neg b \to (a \lor m)$$ không đúng (tài khoản thường cũng không bị khóa).

(d) "Hoặc (tài khoản là admin và không bị khóa) hoặc (tài khoản là moderator và đã xác thực email)." — Hai nhóm quyền riêng biệt.

(e) "Nếu tài khoản chưa xác thực email thì nó bị khóa." — Chính sách bảo mật yêu cầu xác thực email để tránh khóa tài khoản.

</details>

### Bài tập 10: Phân tích lỗi logic từ đề bài thực tế

Một đề bài yêu cầu sinh viên viết điều kiện: "Cho phép truy cập nếu người dùng đã đăng nhập và (có quyền admin hoặc là chủ sở hữu tài liệu)."

Sinh viên A viết: `if logged_in and is_admin or is_owner:`
Sinh viên B viết: `if logged_in and (is_admin or is_owner):`

(a) Biểu thức của sinh viên nào đúng? Giải thích.
(b) Với `logged_in = False, is_admin = True, is_owner = False`, kết quả mỗi biểu thức là gì?
(c) Lỗi của sinh viên A thuộc loại lỗi nào trong lập trình? Làm sao để tránh?

<details>
<summary>Đáp án</summary>

(a) **Sinh viên B đúng**. Trong hầu hết ngôn ngữ lập trình, `and` có độ ưu tiên cao hơn `or`. Biểu thức của A được hiểu là:
    `(logged_in and is_admin) or is_owner` — khác hoàn toàn với yêu cầu.
    Biểu thức của B: `logged_in and (is_admin or is_owner)` — khớp với yêu cầu.

(b) Với `logged_in = False, is_admin = True, is_owner = False`:
    - Sinh viên A: `(False and True) or False = False or False = False`
    - Sinh viên B: `False and (True or False) = False and True = False`
    Trong trường hợp này cả hai đều cho False, nhưng sẽ khác nhau ở các trường hợp khác.
    
    Thử với `logged_in = False, is_admin = False, is_owner = True`:
    - Sinh viên A: `(False and False) or True = False or True = True` — **sai!** Cho phép truy cập dù chưa đăng nhập.
    - Sinh viên B: `False and (False or True) = False and True = False` — **đúng**.

(c) Lỗi của sinh viên A là **lỗi thứ tự ưu tiên toán tử** (operator precedence bug). Đây là một trong những lỗi logic phổ biến nhất trong lập trình. Cách tránh:
    - Luôn dùng dấu ngoặc khi kết hợp `and`/`or` với nhau
    - Viết test case bao phủ ít nhất một trường hợp mỗi nhánh
    - Dùng công cụ phân tích tĩnh (linter) để phát hiện biểu thức mơ hồ

</details>

## Bài tập bổ sung: Diễn đạt vấn đề thực tế bằng logic mệnh đề (từ ccrr1_baitap1)

**Hướng dẫn chung:** Xác định mệnh đề đơn (ví dụ P, Q, R), dùng →, ∧, ∨, ¬ để diễn đạt điều kiện.

**Bài tập 1: Quản lý sự kiện**
Giả sử bạn quản lý sự kiện hội thảo. Các điều kiện:
- Nếu hội trường đủ lớn → tất cả khách có chỗ ngồi.
- Nếu tất cả khách có chỗ → hội thảo suôn sẻ.
- Nếu hội thảo suôn sẻ → nhận đánh giá tốt.
- Nhận đánh giá tốt chỉ khi chuẩn bị đầy đủ.

Diễn đạt bằng biểu thức logic.

**Bài tập 2: Hệ thống bảo mật**
Hệ thống cho phép truy cập nếu:
- Đúng tên đăng nhập và mật khẩu → cho phép truy cập.
- Không đúng tên hoặc mật khẩu → không cho phép.
- Không cho phép → phải thử lại.

Diễn đạt.

**Bài tập 3: Điều kiện mua hàng**
Cửa hàng online:
- Đủ tiền và đúng thông tin → giao dịch thành công.
- Không đủ tiền hoặc sai thông tin → hủy.
- Hủy → yêu cầu kiểm tra lại.

Diễn đạt.

**Bài tập 4: Điều kiện học bổng**
- GPA ≥ 3.5 hoặc thành tích đặc biệt → được xét duyệt.
- Không GPA và không đặc biệt → không xét.
- Được xét và nộp đơn đúng hạn → nhận học bổng.

Diễn đạt.

**Bài tập 5: Lập lịch làm việc**
- Cuối tuần hoặc lễ → nghỉ.
- Không cuối tuần và không lễ → phải đi làm.
- Cuối tuần nhưng có dự án gấp → vẫn phải đi làm.

Diễn đạt.

**Bài tập 6: Tam giác**
Cho a,b,c số thực. Diễn đạt:
a) Cạnh tam giác?
b) Cạnh tam giác vuông huyền c?
c) Cạnh tam giác vuông cân huyền c?
d) Cạnh tam giác đều?

P1(a,b,c) = ? etc.

### Bài tập bổ sung từ slide PPT: Viết biểu thức logic

Viết biểu thức logic mệnh đề cho các mô tả sau (sử dụng biến mệnh đề phù hợp):

1. Điều kiện để tháng (m) là dữ liệu hợp lệ.
2. Điều kiện để tháng m có 30 ngày.
3. Điều kiện để tháng 2 có 29 ngày.
4. Điều kiện để A, B, C là các góc của một tam giác.
5. Điều kiện để A, B, C là các góc của một tam giác vuông.
6. Điều kiện để A, B, C là các góc của một tam giác cân.
7. Điều kiện để A, B, C là các góc của một tam giác đều.
8. Điều kiện để học sinh A xét điểm theo tổ hợp A0 đậu vào khoa CNTT IUH năm 2019.
9. Điều kiện để bạn được nhận học bổng 100% trong học kỳ 1 năm học 2020-2021.
10. Điều kiện tiếng Anh để bạn được đăng ký học phần năm 3.

**Bài tập bổ sung (từ slide):** 

Bài tập 3: Hàm eq(X,Y) trả về 1 khi giá trị của X và Y là như nhau, trả về 0 trong các trường hợp còn lại. Biểu thức nào dưới đây là điều kiện cần và đủ để nhận về 1 khi hàm eq(eq(A,B), eq(B,C)) được gọi?

A. (A=B và B=C) hoặc (A#B và B#C)

B. (A=B và B=C) hoặc (A#B hoặc B#C)

C. (A=B và B=C) hoặc (A=C)

D. (A=B hoặc B=C) hoặc (A=C)



