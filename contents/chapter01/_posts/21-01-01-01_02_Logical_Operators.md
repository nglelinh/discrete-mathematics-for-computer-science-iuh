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

| p | q | p ∨ q | Ghi nhớ |
|:---:|:---:|:---:|:---|
| T | T | T | Có ít nhất 1 cái đúng |
| T | F | T | p đúng |
| F | T | T | q đúng |
| F | F | F | Cả hai sai |

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


