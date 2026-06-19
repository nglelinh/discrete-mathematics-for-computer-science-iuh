---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Biểu thức Logic

**Toán Rời Rạc — IUH**

Tiết 3 (45 phút)

---

# Mục tiêu tiết học

- Các phép toán biểu thức logic
- Bảng chân trị
- Biểu thức tương đương
- Các luật logic
- Ứng dụng: lọc SP, validator web, email

---

# Biểu thức logic

Kết hợp mệnh đề sơ cấp bằng:

$$\neg, \land, \lor, \to, \leftrightarrow, \oplus$$

Ví dụ: $\neg p \lor (q \land r)$

---

# Phép toán logic — Định nghĩa hình thức

Dưới đây là 6 phép toán logic cơ bản cùng định nghĩa và bảng chân trị đầy đủ.

---

# 1. Phép phủ định (Negation) — NOT

**Ký hiệu**: $\neg p$

**Định nghĩa**: Phủ định của mệnh đề $p$ là mệnh đề có giá trị chân lý ngược lại với $p$.

| $p$ | $\neg p$ |
|:---:|:---:|
| T | F |
| F | T |

**Code**: `not p` hoặc `!p`

---

# 2. Phép hội (Conjunction) — AND

**Ký hiệu**: $p \land q$

**Định nghĩa**: $p \land q$ đúng **khi và chỉ khi** cả $p$ và $q$ đều đúng.

| $p$ | $q$ | $p \land q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**Code**: `p and q`

---

# 3. Phép tuyển (Disjunction) — OR

**Ký hiệu**: $p \lor q$

**Định nghĩa**: $p \lor q$ sai **khi và chỉ khi** cả $p$ và $q$ đều sai (OR bao hàm).

| $p$ | $q$ | $p \lor q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

**Code**: `p or q`

---

# 4. Phép kéo theo (Implication) — IF...THEN

**Ký hiệu**: $p \to q$

**Định nghĩa**: $p \to q$ **chỉ sai** khi tiền đề $p$ đúng và kết luận $q$ sai.

| $p$ | $q$ | $p \to q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

**Lưu ý quan trọng**: Khi $p$ sai, $p \to q$ luôn đúng (vacuously true).

---

# 5. Phép tương đương (Biconditional)

**Ký hiệu**: $p \leftrightarrow q$

**Định nghĩa**: $p \leftrightarrow q$ đúng khi $p$ và $q$ có cùng giá trị chân lý.

$$p \leftrightarrow q \equiv (p \to q) \land (q \to p)$$

---

# 6. Phép XOR (Exclusive OR)

**Ký hiệu**: $p \oplus q$

**Định nghĩa**: $p \oplus q$ đúng khi **chỉ một** trong hai mệnh đề đúng.

| $p$ | $q$ | $p \oplus q$ |
|:---:|:---:|:---:|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

---

# Phép tương đương — IFF

**Ký hiệu:** $p \leftrightarrow q$ — cùng giá trị chân lý

$$p \leftrightarrow q \equiv (p \to q) \land (q \to p)$$

---

# Phép XOR

**Ký hiệu:** $p \oplus q$ — đúng khi **đúng đúng một** vế

Code: `p != q`

| Tình huống | OR | XOR |
|:---|:---:|:---:|
| Thanh toán: thẻ hoặc CK | | ✓ |
| Cảnh báo: nhiệt độ hoặc áp suất | ✓ | |

---

# Thứ tự ưu tiên

| Ưu tiên | Toán tử |
|:---:|:---|
| 1 | $\neg$ |
| 2 | $\land$ |
| 3 | $\lor$ |
| 4 | $\to$ |
| 5 | $\leftrightarrow$ |
| 6 | $\oplus$ |

**Luôn dùng ngoặc** khi không chắc!

---

# Ví dụ đăng nhập

$$p \land q \land (\neg r \lor s)$$

- $p$: mật khẩu đúng
- $q$: tài khoản active
- $r$: thiết bị lạ
- $s$: OTP đúng

```python
can_login = pwd_ok and active and (not unknown or otp_ok)
```

---

# Bảng chân trị (Truth Table)

**Định nghĩa**: Bảng chân trị là bảng liệt kê **tất cả** các tổ hợp giá trị chân lý có thể có của các biến và giá trị tương ứng của biểu thức.

**Số dòng**:
- Với $n$ biến → **chính xác $2^n$ dòng**
- 1 biến: 2 dòng
- 2 biến: 4 dòng
- 3 biến: 8 dòng
- 4 biến: 16 dòng

---

# Phương pháp xây dựng bảng chân trị

**Các bước chi tiết**:

1. Xác định số biến $n$
2. Liệt kê tất cả tổ hợp giá trị theo thứ tự nhị phân (từ 00...0 đến 11...1)
3. Xây dựng cột cho từng biểu thức con, tính từ trong ra ngoài (theo thứ tự ưu tiên)
4. Cột cuối cùng là kết quả của toàn bộ biểu thức

**Mẹo**: Luôn dùng ngoặc để tránh nhầm lẫn thứ tự.

---

# Phân loại biểu thức logic

| Loại              | Định nghĩa                           | Ví dụ           |
|-------------------|--------------------------------------|-----------------|
| **Tautology**     | Luôn đúng với mọi gán                | $p \lor \neg p$ |
| **Contradiction** | Luôn sai với mọi gán                 | $p \land \neg p$|
| **Contingency**   | Tùy gán (đôi khi đúng/sai)           | $p \land q$     |

---

# Tầm quan trọng của phân loại

- **Tautology**: luôn an toàn (nền tảng luật logic)
- **Contradiction**: lỗi logic nghiêm trọng
- **Contingency**: phụ thuộc dữ liệu thực tế

---

# Ví dụ phân loại

- $p \to (q \to p)$ → **Tautology**
- $(p \land q) \land \neg(p \land q)$ → **Contradiction**
- $p \land q$ → **Contingency**

---

# Tương đương logic

**Định nghĩa**:
Hai biểu thức $E_1$ và $E_2$ là **tương đương logic** (ký hiệu $E_1 \equiv E_2$) nếu chúng có cùng bảng chân trị ở mọi trường hợp.

**Tương đương quan trọng nhất**:
$$p \to q \equiv \neg p \lor q$$

**Ứng dụng**: Dùng để loại bỏ phép kéo theo khi chuyển sang DNF/CNF.

---

# Ví dụ: $(p \land q) \to r$

| $p$ | $q$ | $r$ | $p \land q$ | Kết quả |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T |
| T | T | F | T | **F** |
| T | F | * | F | T |
| F | * | * | F | T |

Chỉ sai khi $p$, $q$ đúng mà $r$ sai

---

# Phân loại biểu thức

| Loại | Đặc điểm | Ví dụ |
|:---|:---|:---|
| **Tautology** | Luôn T | $p \lor \neg p$ |
| **Contradiction** | Luôn F | $p \land \neg p$ |
| **Contingency** | Tùy biến | $p \land q$ |

---

# Biểu thức tương đương

$E_1 \equiv E_2$ ⟺ cùng bảng chân trị mọi trường hợp

**Quan trọng:** $p \to q \equiv \neg p \lor q$

---

# Chứng minh tương đương

| $p$ | $q$ | $p \to q$ | $\neg p \lor q$ |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

→ Hai cột giống nhau

---

# Các luật logic cơ bản (nhóm 1)

| Luật                  | Công thức                                          |
|-----------------------|----------------------------------------------------|
| Phủ định kép          | $\neg\neg p \equiv p$                              |
| De Morgan (1)         | $\neg(p \land q) \equiv \neg p \lor \neg q$        |
| De Morgan (2)         | $\neg(p \lor q) \equiv \neg p \land \neg q$        |

---

# Các luật logic cơ bản (nhóm 2)

| Luật                  | Công thức                                          |
|-----------------------|----------------------------------------------------|
| Giao hoán             | $p \land q \equiv q \land p$ , $p \lor q \equiv q \lor p$ |
| Kết hợp               | $(p \land q) \land r \equiv p \land (q \land r)$ |
| Phân phối             | $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ |

---

# Các luật logic cơ bản (nhóm 3)

| Luật                  | Công thức                                          |
|-----------------------|----------------------------------------------------|
| Bù (Complement)       | $p \lor \neg p \equiv T$ , $p \land \neg p \equiv F$ |
| Hấp thụ (Absorption)  | $p \lor (p \land q) \equiv p$ , $p \land (p \lor q) \equiv p$ |
| Đồng nhất (Identity)  | $p \land T \equiv p$ , $p \lor F \equiv p$ |
| Lũy đẳng (Idempotent) | $p \lor p \equiv p$ , $p \land p \equiv p$ |

**Ghi nhớ**: De Morgan, Phân phối và Bù là ba luật dùng nhiều nhất.

---

# De Morgan trong code

```python
# Cách 1
if not (is_admin and is_active):
    deny()

# Cách 2 — tương đương
if (not is_admin) or (not is_active):
    deny()
```

---

# Ví dụ: Trang danh sách sản phẩm

**Bộ lọc e-commerce:**

- Danh mục: Điện thoại **hoặc** Tablet
- Giá: 5–15 triệu
- Hãng: Samsung **hoặc** Apple
- Còn hàng
- ≥ 4 sao **hoặc** ≥ 100 đánh giá

---

# Công thức lọc SP

$$(p \lor q) \land r \land (s \lor t) \land u \land (v \lor w)$$

| Biến | Ý nghĩa |
|:---|:---|
| $p, q$ | Điện thoại, Tablet |
| $r$ | Giá hợp lệ |
| $s, t$ | Samsung, Apple |
| $u$ | Còn hàng |
| $v, w$ | Rating, review count |

---

# Code lọc sản phẩm

```javascript
return (cat === 'phone' || cat === 'tablet')
    && price >= 5e6 && price <= 15e6
    && (brand === 'Samsung' || brand === 'Apple')
    && inStock
    && (rating >= 4 || reviewCount >= 100);
```

Nhầm `&&` / `||` → kết quả sai hoàn toàn

---

# Ví dụ: Validator form đăng ký

Điều kiện submit:

$$p \land q \land (r \land s \land t) \land u \land v$$

- $p$: tên ≠ rỗng
- $q$: email hợp lệ
- $r,s,t$: mật khẩu (độ dài, hoa, số)
- $u$: xác nhận khớp
- $v$: đồng ý điều khoản

---

# Validator email

Email hợp lệ khi:

$$p \land q \land r \land s \land t$$

- $p$: đúng 1 ký tự `@`
- $q$: phần local không rỗng
- $r$: local chỉ ký tự hợp lệ
- $s$: domain có ≥ 1 dấu `.`
- $t$: TLD hợp lệ (.com, .vn...)

---

# Code validator email

```javascript
function isValidEmail(email) {
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))
    return false;
  const [local, domain] = email.split('@');
  const localOk = local.length > 0
    && /^[a-zA-Z0-9._]+$/.test(local);
  const parts = domain.split('.');
  const domainOk = parts.length >= 2
    && ['com','vn','org'].includes(parts.at(-1));
  return localOk && domainOk;
}
```

---

# Test email

| Email | Kết quả |
|:---|:---:|
| user@example.com | T |
| user.name@domain.vn | T |
| user@domain | F |
| @example.com | F |
| user@@example.com | F |

---

# Lỗi thường gặp

1. **Implication:** $p \to q$ **chỉ sai** khi $p$=T và $q$=F (không phải khi $p$ sai)
2. **Số dòng bảng chân trị:** Chính xác $2^n$ dòng, không phải $2n$
3. **Thứ tự ưu tiên:** Trong Python `and` có độ ưu tiên cao hơn `or` (giống toán học)
4. **Dấu ngoặc:** `a and b or c` ≠ `a and (b or c)` → luôn dùng ngoặc khi nghi ngờ
5. **Vacuously true:** Quên rằng khi $p$ sai thì $p\to q$ luôn đúng

---

# Tóm tắt các phép toán

| Phép toán | Ký hiệu | Tên tiếng Anh     | Đúng khi nào?                     | Code    |
|-----------|---------|-------------------|-----------------------------------|---------|
| Phủ định  | $\neg$  | Negation          | Ngược với $p$                     | `not`   |
| Hội       | $\land$ | Conjunction       | Cả hai đúng                       | `and`   |
| Tuyển     | $\lor$  | Disjunction       | Ít nhất một đúng                  | `or`    |
| Kéo theo  | $\to$   | Implication       | Không xảy ra T → F                | —       |
| Tương đương | $\leftrightarrow$ | Biconditional | Cùng giá trị                      | —       |
| XOR       | $\oplus$| Exclusive OR      | Chính xác một đúng                | `!=`    |

---

# Thực hành 1 (15 phút)

Cho $p$=T, $q$=F, $r$=T. Tính:

1. $p \land \neg q$
2. $(p \lor q) \to r$
3. $\neg(p \land q) \lor r$

---

# Thực hành 2 (15 phút)

Lập bảng chân trị cho:

$$(p \to q) \land (q \to r) \to (p \to r)$$

(Tam đoạn luận — có phải tautology?)

---

# Thực hành 3 (20 phút)

Viết biểu thức logic + code cho:

> Cho sửa bài viết nếu: admin, hoặc (là tác giả và bài chưa khóa)

So sánh:
`is_admin or is_author and not is_locked`

---

# Thực hành 4 (15 phút)

Dùng De Morgan rút gọn:

$$\neg(p \lor \neg q) \land (r \lor \neg r)$$

---

# Tóm tắt Tiết 3

- 6 phép toán logic cơ bản
- Bảng chân trị = công cụ kiểm chứng
- Tương đương & luật logic → rút gọn code
- Ứng dụng: filter, validator, phân quyền

---

# Bài tập ôn tập (1/2)

1. **Bài 1**: Cho p = True, q = False, r = True. Tính:
   - (a) `¬q ∨ r`
   - (b) `(p → q) ∧ r`

2. **Bài 2**: Lập bảng chân trị cho:
   $$(p \lor q) \to (\neg p \lor r)$$

---

# Bài tập ôn tập (2/2)

3. **Bài 3**: Viết biểu thức + code cho:
   > Truy cập nếu đã đăng nhập VÀ (admin HOẶC (thành viên VÀ chưa khóa))

4. **Bài 4**: Chứng minh:
   $$p \to q \equiv \neg p \lor q$$

5. **Bài 5** (thách thức): Viết logic cho validator email (có @, local, domain).

---

# Tiết sau

**Quy tắc suy diễn** hoặc **Logic vị từ**

- Modus ponens, tam đoạn luận
- Lượng từ ∀, ∃

---

# Câu hỏi?