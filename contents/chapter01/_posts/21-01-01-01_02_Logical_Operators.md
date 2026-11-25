---

layout: post
title: "Phép toán Logic"
categories: chapter01
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Giới thiệu các phép toán logic cơ bản (phủ định, hội, tuyển, XOR, kéo theo, tương đương), thứ tự ưu tiên toán tử và các luật biến đổi biểu thức."
---

Một mệnh đề đơn lẻ như *"Mật khẩu đúng"* hiếm khi đủ để mô tả luật nghiệp vụ hay thuật toán thực tế. Sức mạnh thật sự của logic xuất hiện khi ta ghép nhiều mệnh đề lại bằng các **toán tử logic** ($$\neg, \land, \lor, \oplus, \to, \leftrightarrow$$)—từ điều kiện đăng nhập bảo mật cho đến mạch cộng nhị phân 64-bit trong bộ xử lý.

## Bản đồ kiến thức nền: Bốn trục tư duy khi làm việc với Toán tử Logic

1. **Năm toán tử cơ bản và độ ưu tiên (Precedence)**:
   Thứ tự ưu tiên chuẩn từ cao xuống thấp là: dấu ngoặc `()` $$\succ$$ Phủ định ($$\neg$$) $$\succ$$ Hội ($$\land$$) $$\succ$$ Tuyển ($$\lor$$) $$\succ$$ Kéo theo ($$\to$$) $$\succ$$ Tương đương ($$\leftrightarrow$$). Nắm chắc thứ tự này giúp đọc công thức phức hợp không sai ngoặc.

2. **Tuyển bao hàm (Inclusive OR $$\lor$$) vs. Tuyển loại trừ (XOR $$\oplus$$)**:
   Trong tiếng Việt hàng ngày, chữ *"hoặc"* thường mang nghĩa chọn 1 trong 2 (XOR: *"trà hoặc cà phê"*). Trong toán học và lập trình, $$\lor$$ (`||`) là **tuyển bao hàm** (đúng cả khi cả hai vế cùng đúng), còn $$\oplus$$ (`^`) chỉ đúng khi hai vế **khác nhau**—và là phép toán xương sống của mật mã đối xứng và mã sửa lỗi.

3. **Phép kéo theo ($$p \to q$$) — "Lời hứa hợp đồng"**:
   $$p \to q$$ chỉ **Sai** trong duy nhất một trường hợp: điều kiện $$p$$ Đúng nhưng kết luận $$q$$ Sai (thất hứa). Khi $$p$$ Sai, lời hứa không hề bị vi phạm nên $$p \to q$$ mặc nhiên **Đúng** (*vacuously true*).

4. **Đánh giá đoản mạch (Short-Circuit Evaluation) trong lập trình**:
   Trong C/Java/Python/Rust, `A && B` không thèm tính `B` nếu `A` đã `False`, và `A || B` không tính `B` nếu `A` đã `True`—nhờ đó biểu thức `ptr != null && ptr.value > 0` an toàn tuyệt đối.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Sử dụng** chính xác các phép toán NOT, AND, OR, XOR, IF...THEN, IF AND ONLY IF.
- **Đọc** một điều kiện lập trình và chuyển đổi sang ký hiệu logic.
- **Giải thích** vì sao mệnh đề kéo theo $$p \to q$$ vẫn đúng khi $$p$$ sai.
- **Phân biệt** phép OR bao hàm và phép XOR trong ngôn ngữ tự nhiên.
- **Áp dụng** các phép toán logic vào kiểm tra đầu vào, phân quyền, truy vấn dữ liệu và thiết kế test case.


**Từ khóa**: NOT, AND, OR, XOR, implication, biconditional, truth value, condition, access control.
</div>


## Câu chuyện mở đầu: Điều kiện đăng nhập

<div class="content-box example-box textbook-block" markdown="1">
Một hệ thống chỉ cho phép đăng nhập nếu thỏa mãn các điều kiện sau:

- Người dùng nhập đúng mật khẩu.
- Tài khoản chưa bị khóa.
- Nếu đăng nhập từ thiết bị lạ thì phải nhập mã OTP.

Ký hiệu:

- $$p$$: Mật khẩu đúng.
- $$q$$: Tài khoản chưa bị khóa.
- $$r$$: Thiết bị lạ.
- $$s$$: OTP đúng.

Điều kiện đăng nhập:

<div class="textbook-equation" markdown="1">
$$p \land q \land (\neg r \lor s)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Trong mã nguồn:

```python
can_login = correct_password and account_active and (not unknown_device or correct_otp)
```

Nếu bỏ dấu ngoặc, chương trình vẫn chạy bình thường nhưng có thể cho phép hoặc từ chối sai người dùng do thứ tự ưu tiên toán tử thay đổi.
</div>

## Phân loại mệnh đề

Mệnh đề trong logic được phân thành hai loại:

### Mệnh đề sơ cấp (nguyên thủy)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **mệnh đề sơ cấp** (hay mệnh đề nguyên thủy) là mệnh đề **không thể xây dựng từ các mệnh đề khác** thông qua các liên từ logic hoặc trạng từ "không".
</div>


**Đặc điểm**:
- Không chứa phép toán logic (`∧`, `∨`, `¬`, `→`, `↔`).
- Là đơn vị cơ bản nhất trong hệ thống logic.
- Thường được ký hiệu bằng chữ cái thường: `p`, `q`, `r`, `s`, ...

<div class="textbook-example" markdown="1">
**Ví dụ**:
- "Hôm nay trời nắng."
- "2 + 3 = 5."
- "Tôi có tiền."
- "Cửa hàng mở cửa."
</div>


### Mệnh đề phức hợp

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **mệnh đề phức hợp** là mệnh đề **được xây dựng từ các mệnh đề khác** nhờ liên kết bằng các **liên từ** (và, hay, khi và chỉ khi, ...) hoặc **trạng từ "không"**.
</div>


**Đặc điểm**:
- Chứa ít nhất một phép toán logic.
- Được tạo thành từ các mệnh đề sơ cấp thông qua các phép nối.
- Có thể phân tích thành các thành phần nhỏ hơn.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- "Tôi có tiền **và** cửa hàng mở cửa" → `p ∧ q`
- "Trời mưa **hoặc** đường ướt" → `p ∨ q`
- "**Không** phải hôm nay trời nắng" → `¬p`
- "Nếu trời mưa **thì** đường ướt" → `p → q`
</div>


<div class="content-box insight-box textbook-block" markdown="1">
**Lưu ý**: Phân biệt mệnh đề sơ cấp và mệnh đề phức hợp giúp xác định rõ các thành phần cơ bản và cấu trúc ghép nối trong biểu thức logic. Khi phân tích một điều kiện trong mã nguồn, ta luôn bắt đầu bằng việc tách ra các mệnh đề sơ cấp trước khi ghép chúng lại bằng các phép toán.
</div>

### Khung giải thích (nên đọc chậm): Tính tay giá trị một điều kiện kiểm tra quyền truy cập và bảng chân trị $$p \to q$$

Giả sử hệ thống học vụ kiểm tra điều kiện cấp quyền tải đề thi cho sinh viên theo công thức:
$$F \equiv (\neg b \land (s \lor t)) \to a$$
trong đó: $$b$$: tài khoản bị khóa (`is_banned`), $$s$$: đã đóng học phí (`fee_paid`), $$t$$: là giảng viên (`is_teacher`), $$a$$: được phép truy cập (`allowed`).

Hãy kiểm tra bằng tay 3 tình huống cụ thể:

| Tình huống | $$(b, s, t, a)$$ | $$\neg b$$ | $$s \lor t$$ | Tiền đề $$P = \neg b \land (s \lor t)$$ | Kết quả $$P \to a$$ | Ý nghĩa thực tế |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Sinh viên hợp lệ được vào** | `(F, T, F, T)` | `T` | `T` | `T` | **`T`** | Thỏa điều kiện và được cấp quyền → Hợp lệ |
| **2. Giảng viên không bị khóa nhưng bị chặn** | `(F, F, T, F)` | `T` | `T` | `T` | **`F`** | Tiền đề `T` nhưng kết luận `F` → **Hệ thống vi phạm hợp đồng!** |
| **3. Tài khoản bị khóa** | `(T, T, F, F)` | `F` | `T` | `F` | **`T`** | Tiền đề `F` → Phép kéo theo đúng rỗng (*vacuously true*), quy tắc không bị vi phạm |

Nhìn vào dòng 3, bạn thấy ngay vì sao quy ước `F → F = T` không hề "vô lý": quy tắc chỉ hứa cấp quyền cho người *không bị khóa*, nên khi tài khoản bị khóa, việc từ chối truy cập hoàn toàn tuân thủ hợp đồng!

## Phép phủ định (Negation) — NOT

**Ký hiệu**: `¬p`, `~p` hoặc `!p`

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Phủ định của mệnh đề $$p$$ là mệnh đề có giá trị chân lý ngược lại với $$p$$.
</div>


### Bảng chân trị

| p | ¬p |
|---|---|
| T | F |
| F | T |

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$p$$: "Hôm nay trời nắng."
- $$\neg p$$: "Hôm nay trời không nắng."

**Phủ định bất đẳng thức** (cách làm trực quan):

Khi phủ định một bất đẳng thức, ta thực hiện theo 3 bước:

1. Giữ nguyên biến và giá trị so sánh.
2. Đảo ngược dấu so sánh (lưu ý kèm hoặc bỏ dấu bằng tương ứng).
3. Viết kết quả.

**Bảng quy tắc nhanh**:

| Biểu thức gốc | Phủ định | Ghi nhớ |
|:---:|:---:|:---|
| $$n > 5$$ | $$n \leq 5$$ | Lớn hơn → nhỏ hơn hoặc bằng |
| $$x \geq 0$$ | $$x < 0$$ | Lớn hơn hoặc bằng → nhỏ hơn |
| $$a = b$$ | $$a \neq b$$ | Bằng → khác |
| $$x < 3$$ | $$x \geq 3$$ | Nhỏ hơn → lớn hơn hoặc bằng |

**Ví dụ** (thực tế):

- "Tuổi lớn hơn 18" → Phủ định: "Tuổi nhỏ hơn hoặc bằng 18."
- "Điểm số >= 5" → Phủ định: "Điểm số < 5."
</div>


## Phép hội (Conjunction) — AND

**Ký hiệu**: `p ∧ q`

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$p \land q$$ chỉ đúng khi cả $$p$$ và $$q$$ đều đúng.
</div>


### Bảng chân trị

| p | q | p ∧ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

![Biểu đồ Venn: phép AND (∧)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-AND.png)

<p class="textbook-figure-caption" data-figure="1.7">Phép hội p ∧ q — chỉ đúng khi cả p và q đều đúng (vùng giao trên biểu đồ Venn).</p>
<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$p$$: "Tôi có tiền."
- $$q$$: "Cửa hàng mở cửa."
- $$p \land q$$: "Tôi có tiền và cửa hàng mở cửa."

**Ví dụ trong lập trình**:

```python
if order_total >= 500000 and customer_tier == "vip":
    apply_discount()
```

Điều kiện chỉ đúng khi **cả hai** điều kiện con đều đúng. Đây là dạng phổ biến trong thương mại điện tử: đơn hàng đạt giá trị tối thiểu và khách hàng thuộc đúng nhóm ưu đãi.
</div>


## Phép tuyển (Disjunction) — OR

**Ký hiệu**: `p ∨ q`

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$p \lor q$$ chỉ sai khi cả $$p$$ và $$q$$ đều sai.
</div>


### Tính chất (OR)

Phép tuyển đúng khi có **ít nhất một** toán hạng đúng: chỉ cần một trong hai mệnh đề đúng thì $$p \lor q$$ đã đúng.

### Bảng chân trị

| p | q | p ∨ q |
|:---:|:---:|:---:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

![Biểu đồ Venn: phép OR (∨)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-OR.png)

<p class="textbook-figure-caption" data-figure="1.8">Phép tuyển p ∨ q — đúng khi ít nhất một trong hai mệnh đề đúng (OR bao hàm).</p>
<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$p$$: "Tôi đi xe bus."
- $$q$$: "Tôi đi xe máy."
- $$p \lor q$$: "Tôi đi xe bus hoặc xe máy."

**Ví dụ trong tìm kiếm**:

```sql
SELECT * FROM products
WHERE category = 'Laptop' OR category = 'Tablet';
```

Kết quả gồm các sản phẩm thuộc ít nhất một trong hai loại. Trong logic toán, OR mặc định là **OR bao hàm** (inclusive OR): nếu một đối tượng thỏa mãn đồng thời cả hai điều kiện thì kết quả vẫn đúng.
</div>


## Phép kéo theo (Implication) — IF...THEN

**Ký hiệu**: `p → q`

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$p \to q$$ chỉ sai khi $$p$$ đúng và $$q$$ sai.
</div>


### Bảng chân trị

| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$p$$: "Trời mưa."
- $$q$$: "Đường ướt."
- $$p \to q$$: "Nếu trời mưa thì đường ướt."
</div>


### Lưu ý quan trọng
- $$p$$ được gọi là **giả thiết** (hypothesis).
- $$q$$ được gọi là **kết luận** (conclusion).
- Khi $$p$$ sai, $$p \to q$$ luôn đúng (vacuously true).

![Biểu đồ Venn: mệnh đề kéo theo (→)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-Implication.PNG)

<p class="textbook-figure-caption" data-figure="1.9">Mệnh đề kéo theo p → q — chỉ sai khi p đúng mà q sai; khi p sai thì luôn đúng (vacuously true).</p>
![Biểu đồ Venn: phép XOR (⊕)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-XOR.png)

<p class="textbook-figure-caption" data-figure="1.10">Phép XOR p ⊕ q — đúng khi đúng một trong hai mệnh đề đúng (loại trừ lẫn nhau).</p>
![Luật De Morgan trên biểu đồ Venn](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

<p class="textbook-figure-caption" data-figure="1.11">Luật De Morgan — ¬(p ∧ q) ≡ ¬p ∨ ¬q và ¬(p ∨ q) ≡ ¬p ∧ ¬q, rất quan trọng khi viết điều kiện phủ định trong mã nguồn.</p>
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

**Biểu thức logic** (logical expression) là sự kết hợp của các mệnh đề sơ cấp bằng các phép toán logic (`¬`, `∧`, `∨`, `→`, `↔`, `⊕`) và dấu ngoặc.

### Cú pháp biểu thức logic

Một biểu thức logic được xây dựng theo các quy tắc sau:

- Mọi mệnh đề sơ cấp (`p`, `q`, `r`, ...) đều là biểu thức logic.
- Nếu `E` là biểu thức logic thì `¬E` cũng là biểu thức logic.
- Nếu `E₁` và `E₂` là biểu thức logic thì `(E₁ ∧ E₂)`, `(E₁ ∨ E₂)`, `(E₁ → E₂)`, `(E₁ ↔ E₂)`, `(E₁ ⊕ E₂)` cũng là biểu thức logic.

**Ví dụ biểu thức logic**:
- $$p \land q$$
- $$\neg p \lor (q \land r)$$
- $$(p \to q) \land (q \to p)$$
- $$p \oplus (q \land \neg r)$$

### Thứ tự ưu tiên toán tử

Khi viết biểu thức không có dấu ngoặc, thứ tự thực hiện các phép toán là:

| Ưu tiên | Toán tử | Tên |
|:---:|:---|:---|
| 1 (cao nhất) | ¬ | Phủ định |
| 2 | ∧ | Hội |
| 3 | ∨ | Tuyển |
| 4 | → | Kéo theo |
| 5 | ↔ | Tương đương |
| 6 (thấp nhất) | ⊕ | XOR |

<div class="textbook-example" markdown="1">
**Ví dụ**: $$p \land q \lor r$$ được hiểu là $$(p \land q) \lor r$$ (không phải $$p \land (q \lor r)$$).
</div>


<div class="content-box warning-box textbook-block" markdown="1">
**Lưu ý**: Luôn dùng dấu ngoặc để biểu thức rõ nghĩa và tránh nhầm lẫn khi chuyển sang mã nguồn.
</div>

## Bảng chân trị cho biểu thức phức hợp

Bảng chân trị không chỉ dùng cho từng phép toán riêng lẻ mà còn dùng để phân tích toàn bộ một biểu thức logic phức hợp.

### Cách xây dựng bảng chân trị

- **Bước 1**: Xác định số biến $$n$$. Bảng sẽ có đúng $$2^n$$ dòng.
- **Bước 2**: Liệt kê tất cả các tổ hợp giá trị chân lý của các biến.
- **Bước 3**: Tính giá trị từng biểu thức con theo thứ tự từ trong ra ngoài.
- **Bước 4**: Xác định giá trị cuối cùng của toàn bộ biểu thức.

<div class="textbook-example" markdown="1">
**Ví dụ**: Biểu thức $$(p \land q) \lor \neg r$$:

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

Biểu thức đúng trong 5/8 trường hợp.
</div>


## Biểu thức tương đương

Hai biểu thức logic $$E_1$$ và $$E_2$$ là **tương đương** (logically equivalent) nếu chúng có cùng giá trị chân lý trong mọi trường hợp. Ký hiệu: $$E_1 \equiv E_2$$.

### Cách chứng minh tương đương

- **Phương pháp 1 — Bảng chân trị**: Lập bảng chân trị cho cả hai biểu thức rồi so sánh hai cột kết quả cuối cùng.
- **Phương pháp 2 — Luật logic**: Biến đổi biểu thức này thành biểu thức kia bằng các luật tương đương (trình bày ở phần sau).

<div class="textbook-example" markdown="1">
**Ví dụ**: Chứng minh $$p \to q \equiv \neg p \lor q$$ bằng bảng chân trị:

| p | q | p → q | ¬p | ¬p ∨ q |
|---|---|-------|----|--------|
| T | T | T     | F  | T      |
| T | F | F     | F  | F      |
| F | T | T     | T  | T      |
| F | F | T     | T  | T      |

Hai cột kết quả giống nhau ở mọi dòng, nên hai biểu thức **tương đương**.

**Ý nghĩa thực tiễn**: Trong lập trình, ta có thể biểu diễn điều kiện kéo theo `if p then q` bằng `not p or q` tùy ngữ cảnh.
</div>


## Các luật logic cơ bản

Dưới đây là các luật logic thường dùng để biến đổi biểu thức:

### Luật phủ định kép (Double Negation)

<div class="textbook-equation" markdown="1">
$$\neg (\neg p) \equiv p$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Luật De Morgan

<div class="textbook-equation" markdown="1">
$$\neg (p \land q) \equiv \neg p \lor \neg q$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$\neg (p \lor q) \equiv \neg p \land \neg q$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Phủ định của "Tôi có tiền và cửa hàng mở cửa" là "Tôi không có tiền HOẶC cửa hàng không mở cửa".
</div>


### Luật giao hoán (Commutative)

<div class="textbook-equation" markdown="1">
$$p \land q \equiv q \land p$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$p \lor q \equiv q \lor p$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Luật kết hợp (Associative)

<div class="textbook-equation" markdown="1">
$$(p \land q) \land r \equiv p \land (q \land r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$(p \lor q) \lor r \equiv p \lor (q \lor r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Luật phân phối (Distributive)

<div class="textbook-equation" markdown="1">
$$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Luật hấp thụ (Absorption)

<div class="textbook-equation" markdown="1">
$$p \land (p \lor q) \equiv p$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$p \lor (p \land q) \equiv p$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Luật đồng nhất (Identity)

<div class="textbook-equation" markdown="1">
$$p \land T \equiv p$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$p \lor F \equiv p$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Luật triệt tiêu (Domination)

<div class="textbook-equation" markdown="1">
$$p \land F \equiv F$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$p \lor T \equiv T$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Luật bổ sung (Complement)

<div class="textbook-equation" markdown="1">
$$p \land \neg p \equiv F$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$p \lor \neg p \equiv T$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="content-box insight-box textbook-block" markdown="1">
**Ghi nhớ De Morgan**: Khi phủ định một biểu thức trong ngoặc, ta đổi phép hội thành phép tuyển (hoặc ngược lại) **và** phủ định từng thành phần bên trong.
</div>

## Ví dụ: Trang danh sách sản phẩm

### Yêu cầu lọc sản phẩm

Một trang thương mại điện tử áp dụng các bộ lọc sau:

- Danh mục: Điện thoại HOẶC Máy tính bảng.
- Giá: Từ 5 triệu đến 15 triệu.
- Thương hiệu: Samsung HOẶC Apple.
- Còn hàng: `true`.
- Đánh giá: ≥ 4 sao HOẶC có ≥ 100 lượt đánh giá.

### Biểu thức logic

Ký hiệu:
- $$p$$: Danh mục là Điện thoại.
- $$q$$: Danh mục là Máy tính bảng.
- $$r$$: Giá nằm trong khoảng [5 triệu, 15 triệu].
- $$s$$: Thương hiệu Samsung.
- $$t$$: Thương hiệu Apple.
- $$u$$: Còn hàng.
- $$v$$: Đánh giá ≥ 4 sao.
- $$w$$: Số lượt đánh giá ≥ 100.

**Điều kiện lọc**:

<div class="textbook-equation" markdown="1">
$$(p \lor q) \land r \land (s \lor t) \land u \land (v \lor w)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Mã nguồn JavaScript

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

**Nhận xét**: Nếu viết nhầm `&&` thành `||` ở điều kiện giá, kết quả lọc sẽ sai hoàn toàn.

## Ví dụ: Validator trong web form

### Yêu cầu kiểm tra form đăng ký

Form đăng ký yêu cầu:
- Tên không được để trống.
- Email hợp lệ (xem phần tiếp theo).
- Mật khẩu dài ≥ 8 ký tự VÀ chứa ít nhất 1 chữ hoa VÀ 1 chữ số.
- Xác nhận mật khẩu trùng với mật khẩu.
- Đã đồng ý điều khoản (`true`).

### Biểu thức logic

Ký hiệu:
- $$p$$: Tên không rỗng.
- $$q$$: Email hợp lệ.
- $$r$$: Mật khẩu ≥ 8 ký tự.
- $$s$$: Mật khẩu chứa chữ hoa.
- $$t$$: Mật khẩu chứa chữ số.
- $$u$$: Xác nhận mật khẩu trùng mật khẩu.
- $$v$$: Đồng ý điều khoản.

**Điều kiện gửi form (submit)**:

<div class="textbook-equation" markdown="1">
$$p \land q \land (r \land s \land t) \land u \land v$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Mã nguồn JavaScript

```javascript
function validateForm(formData) {
  const errors = [];
  
  if (!formData.name) errors.push("Tên không được rỗng");
  if (!isValidEmail(formData.email)) errors.push("Email không hợp lệ");
  if (formData.password.length < 8) errors.push("Mật khẩu ≥ 8 ký tự");
  if (!/[A-Z]/.test(formData.password)) errors.push("Mật khẩu cần chữ hoa");
  if (!/[0-9]/.test(formData.password)) errors.push("Mật khẩu cần chữ số");
  if (formData.password !== formData.confirmPassword) errors.push("Mật khẩu không khớp");
  if (!formData.agreeTerms) errors.push("Phải đồng ý điều khoản");
  
  return errors.length === 0 ? { valid: true } : { valid: false, errors };
}
```

## Validator email

### Yêu cầu kiểm tra email

Một địa chỉ email được xem là hợp lệ (ở mức đơn giản hóa) nếu:
- Có đúng 1 ký tự `@`.
- Phần trước `@` không rỗng VÀ chỉ chứa chữ cái, chữ số, dấu chấm hoặc gạch dưới.
- Phần sau `@` có ít nhất 1 dấu chấm VÀ kết thúc bằng tên miền hợp lệ (`.com`, `.vn`, `.org`, ...).

### Biểu thức logic (đơn giản hóa)

Ký hiệu:
- $$p$$: Có đúng 1 ký tự `@`.
- $$q$$: Phần local không rỗng.
- $$r$$: Phần local chỉ chứa ký tự hợp lệ.
- $$s$$: Phần domain có ≥ 1 dấu chấm.
- $$t$$: Domain kết thúc bằng TLD hợp lệ.

**Điều kiện email hợp lệ**:

<div class="textbook-equation" markdown="1">
$$p \land q \land r \land s \land t$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Mã nguồn JavaScript (regex + logic)

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

<div class="content-box insight-box textbook-block" markdown="1">
**Lưu ý**: Trình kiểm tra email trong thực tế phức tạp hơn nhiều (chuẩn RFC 5321). Ví dụ trên chỉ minh họa cách dùng logic mệnh đề để phân rã yêu cầu kiểm tra.
</div>

## Bài tập thực hành

### Bài tập 1: Tính giá trị chân lý
Cho $$p = T$$, $$q = F$$, $$r = T$$. Tính giá trị chân lý của các biểu thức sau:
1. $$p \land \neg q$$
2. $$(p \lor q) \to r$$
3. $$p \leftrightarrow (q \lor r)$$
4. $$\neg(p \land q) \lor r$$

<details>
<summary>Đáp án</summary>

1. $$p \land \neg q = T \land T = T$$.
2. $$(p \lor q) \to r = T \to T = T$$.
3. $$p \leftrightarrow (q \lor r) = T \leftrightarrow T = T$$.
4. $$\neg(p \land q) \lor r = T \lor T = T$$.

</details>

### Bài tập 3: Điều kiện phân quyền

Một hệ thống cho phép người dùng sửa bài viết nếu:

- Người dùng là admin, hoặc
- Người dùng là tác giả bài viết và bài viết chưa bị khóa.

1. Đặt ký hiệu cho từng mệnh đề sơ cấp.
2. Viết biểu thức logic cho điều kiện trên.
3. Viết điều kiện bằng Python hoặc JavaScript.

### Bài tập 4: Tìm lỗi logic

Một lập trình viên viết điều kiện sau:

```python
can_edit = is_admin or is_author and not is_locked
```

1. Theo thứ tự ưu tiên toán tử trong Python, biểu thức này được hiểu như thế nào?
2. Hãy thêm dấu ngoặc để biểu thức rõ nghĩa.
3. Nếu yêu cầu đổi thành "admin cũng không được sửa bài đã khóa", biểu thức mới là gì?

### Bài tập 5: Chứng minh tương đương logic

<div class="textbook-example" markdown="1">
**Ví dụ**: Cho $$p, q, r$$ là các biến mệnh đề. Chứng minh rằng:

<div class="textbook-equation" markdown="1">
$$(\neg p \to r) \land (q \to r) \iff (p \to q) \to r$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Giải**:

**Phương pháp 1: Bảng chân trị (8 dòng)**

| p | q | r | ¬p | ¬p → r | q → r | (¬p → r) ∧ (q → r) | p → q | (p → q) → r | Kết quả (↔) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | T | T | T | T | T | T |
| T | T | F | F | T | F | F | T | F | T |
| T | F | T | F | T | T | T | F | T | T |
| T | F | F | F | T | T | T | F | T | T |
| F | T | T | T | T | T | T | T | T | T |
| F | T | F | T | F | F | F | T | F | T |
| F | F | T | T | T | T | T | T | T | T |
| F | F | F | T | F | T | F | T | F | T |

**Kết luận**: Hai vế có cột giá trị chân lý giống hệt nhau ở cả 8 dòng (cột tương đương toàn T), nên hai biểu thức tương đương.

**Phương pháp 2: Luật tương đương (biến đổi từng bước)**

Bước 1: Biến đổi vế trái theo định nghĩa phép kéo theo:
<div class="textbook-equation" markdown="1">
$$(\neg p \to r) \equiv (p \lor r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$(q \to r) \equiv (\neg q \lor r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Bước 2: Áp dụng luật phân phối cho vế trái:
$$(p \lor r) \land (\neg q \lor r) \equiv (p \land \neg q) \lor r$$.

Bước 3: Biến đổi vế phải:
<div class="textbook-equation" markdown="1">
$$(p \to q) \to r \equiv (\neg p \lor q) \to r \equiv \neg(\neg p \lor q) \lor r \equiv (p \land \neg q) \lor r$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Bước 4: Hai vế cùng tương đương với $$(p \land \neg q) \lor r$$, suy ra điều phải chứng minh.
</div>


<div class="content-box example-box textbook-block" markdown="1">
**Lưu ý**: Khi gặp bài tập chứng minh tương đương, sinh viên có thể chọn một trong hai cách:
- Bảng chân trị (luôn kiểm chứng được đầy đủ, nhưng dài khi có nhiều biến).
- Luật tương đương (ngắn gọn hơn, đòi hỏi nắm vững các luật biến đổi).
</div>

### Bài tập 6: Mệnh đề kéo theo trong đời thường

Cho các mệnh đề:

- $$p$$: "Bạn chăm chỉ học tập."
- $$q$$: "Bạn đạt điểm cao."
- $$r$$: "Bạn có việc làm tốt."
- $$s$$: "Bạn hài lòng với cuộc sống."

Viết các câu sau dưới dạng ký hiệu logic:

(a) "Nếu bạn chăm chỉ học tập thì bạn đạt điểm cao."
(b) "Chỉ khi bạn đạt điểm cao bạn mới có việc làm tốt."
(c) "Bạn có việc làm tốt là đủ để bạn hài lòng với cuộc sống."
(d) "Bạn chăm chỉ học tập là cần thiết để đạt điểm cao."
(e) "Nếu không chăm chỉ thì không đạt điểm cao, và nếu không đạt điểm cao thì không có việc làm tốt."

<details>
<summary>Đáp án</summary>

(a) $$p \to q$$ — "Nếu $$p$$ thì $$q$$".

(b) $$r \to q$$ — "Chỉ khi $$q$$ mới $$r$$" có nghĩa là nếu có việc làm tốt thì bắt buộc phải đạt điểm cao (tức $$q$$ là điều kiện cần cho $$r$$).

(c) $$r \to s$$ — "$$r$$ là điều kiện đủ để $$s$$".

(d) $$q \to p$$ — "$$p$$ là điều kiện cần cho $$q$$" nghĩa là không thể có $$q$$ nếu không có $$p$$, hay "nếu $$q$$ thì $$p$$" (lưu ý tránh viết nhầm thành $$p \to q$$).

(e) $$(\neg p \to \neg q) \land (\neg q \to \neg r)$$. Theo tam đoạn luận giả định, từ hai mệnh đề này có thể suy ra $$\neg p \to \neg r$$ ("nếu không chăm chỉ thì không có việc làm tốt").

</details>

### Bài tập 7: XOR và OR trong thực tế

Trong mỗi tình huống sau, từ "hoặc" được dùng theo nghĩa OR bao hàm (inclusive) hay XOR (loại trừ)? Giải thích.

(a) "Sinh viên được nhận học bổng nếu có điểm trung bình >= 8.0 hoặc có thành tích nghiên cứu."
(b) "Bạn có thể chọn thanh toán bằng thẻ tín dụng hoặc chuyển khoản."
(c) "Hệ thống cảnh báo nếu nhiệt độ > 100°C hoặc áp suất < 1 atm."
(d) "Trong trận đấu, đội thắng được 3 điểm, đội hòa được 1 điểm, hoặc đội thua được 0 điểm."
(e) "Để đăng nhập, bạn cần nhập đúng tên người dùng và mật khẩu, hoặc sử dụng xác thực vân tay."

<details>
<summary>Đáp án</summary>

(a) **OR bao hàm** — Sinh viên có thể vừa có điểm trung bình >= 8.0 vừa có thành tích nghiên cứu và vẫn nhận học bổng.

(b) **XOR** — Người dùng thường chỉ chọn một phương thức thanh toán cho mỗi giao dịch; trong giao diện, đây thường là nút radio thay vì checkbox.

(c) **OR bao hàm** — Cả hai điều kiện đều có thể xảy ra đồng thời và hệ thống vẫn phát cảnh báo.

(d) **XOR** — Một đội chỉ nhận một kết quả duy nhất trong trận đấu; ba trường hợp loại trừ lẫn nhau.

(e) **OR bao hàm** — Người dùng có thể thỏa mãn cả hai phương thức xác thực và vẫn đăng nhập được.

</details>

### Bài tập 8: Biểu diễn điều kiện phức hợp bằng Python

Viết hàm Python cho mỗi yêu cầu sau bằng các phép toán logic:

(a) `can_publish(post)` — Bài viết được đăng nếu đã được duyệt (`reviewed`) VÀ (nội dung đã hoàn chỉnh HOẶC tác giả là editor).

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
- $$a$$: "Tài khoản là admin."
- $$m$$: "Tài khoản là moderator."
- $$b$$: "Tài khoản bị khóa."
- $$v$$: "Tài khoản đã xác thực email."

Diễn giải các biểu thức sau thành câu tiếng Việt tự nhiên:

(a) $$(a \lor m) \land \neg b$$
(b) $$v \to (a \lor m)$$
(c) $$(a \lor m) \leftrightarrow \neg b$$
(d) $$(a \land \neg b) \lor (m \land v)$$
(e) $$\neg v \to b$$

<details>
<summary>Đáp án</summary>

(a) "Tài khoản là admin hoặc moderator, và không bị khóa." — Điều kiện để có quyền truy cập đặc biệt.

(b) "Nếu tài khoản đã xác thực email thì nó là admin hoặc moderator." — Tình huống giả định, cho thấy chiều kéo theo khác với yêu cầu thực tế thông thường.

(c) "Tài khoản là admin hoặc moderator khi và chỉ khi nó không bị khóa." — Mệnh đề hai chiều này khẳng định cả hai chiều, trong đó chiều $$\neg b \to (a \lor m)$$ ngụ ý mọi tài khoản không bị khóa đều là admin hoặc moderator (thường không đúng trong hệ thống thực tế vì tài khoản thường cũng không bị khóa).

(d) "Hoặc (tài khoản là admin và không bị khóa), hoặc (tài khoản là moderator và đã xác thực email)." — Mô tả hai nhóm điều kiện phân quyền riêng biệt.

(e) "Nếu tài khoản chưa xác thực email thì nó bị khóa." — Chính sách yêu cầu xác thực email để không bị khóa tài khoản.

</details>

### Bài tập 10: Phân tích lỗi logic từ đề bài thực tế

Một đề bài yêu cầu viết điều kiện: "Cho phép truy cập nếu người dùng đã đăng nhập và (có quyền admin hoặc là chủ sở hữu tài liệu)."

Sinh viên A viết: `if logged_in and is_admin or is_owner:`
Sinh viên B viết: `if logged_in and (is_admin or is_owner):`

(a) Biểu thức của sinh viên nào đúng? Giải thích.
(b) Với `logged_in = False, is_admin = True, is_owner = False`, kết quả của mỗi biểu thức là gì?
(c) Lỗi của sinh viên A thuộc loại lỗi nào trong lập trình và cách phòng tránh là gì?

<details>
<summary>Đáp án</summary>

(a) **Sinh viên B đúng**. Trong hầu hết ngôn ngữ lập trình, `and` có độ ưu tiên cao hơn `or`. Biểu thức của sinh viên A được hiểu là `(logged_in and is_admin) or is_owner`, khác với yêu cầu đề bài. Biểu thức của sinh viên B (`logged_in and (is_admin or is_owner)`) khớp với yêu cầu.

(b) Với `logged_in = False, is_admin = True, is_owner = False`:
    - Sinh viên A: `(False and True) or False = False`.
    - Sinh viên B: `False and (True or False) = False`.
    Trong trường hợp này cả hai đều trả về `False`, nhưng sẽ khác nhau ở các tổ hợp khác. Ví dụ với `logged_in = False, is_admin = False, is_owner = True`:
    - Sinh viên A: `(False and False) or True = True` (**sai**, cho phép truy cập dù chưa đăng nhập).
    - Sinh viên B: `False and (False or True) = False` (**đúng**).

(c) Lỗi của sinh viên A là **lỗi thứ tự ưu tiên toán tử** (operator precedence bug). Cách phòng tránh:
    - Luôn dùng dấu ngoặc rõ ràng khi kết hợp `and` và `or`.
    - Viết test case bao phủ các nhánh điều kiện.
    - Sử dụng công cụ phân tích tĩnh (linter) để phát hiện biểu thức dễ gây nhầm lẫn.

</details>

## Bài tập bổ sung: Diễn đạt vấn đề thực tế bằng logic mệnh đề (từ ccrr1_baitap1)

**Hướng dẫn chung:** Đặt ký hiệu cho các mệnh đề đơn (ví dụ $$P, Q, R$$) và sử dụng các phép toán $$\to, \land, \lor, \neg$$ để biểu diễn từng điều kiện.

**Bài tập 1: Quản lý sự kiện**
Giả sử một người quản lý sự kiện hội thảo cần mô hình hóa các điều kiện sau bằng biểu thức logic:
- Nếu hội trường đủ lớn thì tất cả khách đều có chỗ ngồi.
- Nếu tất cả khách có chỗ ngồi thì hội thảo diễn ra suôn sẻ.
- Nếu hội thảo diễn ra suôn sẻ thì nhận được đánh giá tốt.
- Chỉ nhận được đánh giá tốt khi đã chuẩn bị đầy đủ.

**Bài tập 2: Hệ thống bảo mật**
Biểu diễn các quy tắc truy cập sau bằng logic mệnh đề:
- Đúng tên đăng nhập và đúng mật khẩu thì cho phép truy cập.
- Không đúng tên đăng nhập hoặc không đúng mật khẩu thì không cho phép truy cập.
- Nếu không được phép truy cập thì phải thử lại.

**Bài tập 3: Điều kiện mua hàng**
Biểu diễn các quy tắc xử lý giao dịch của một cửa hàng trực tuyến:
- Đủ tiền và đúng thông tin thì giao dịch thành công.
- Không đủ tiền hoặc sai thông tin thì hủy giao dịch.
- Nếu hủy giao dịch thì yêu cầu kiểm tra lại.

**Bài tập 4: Điều kiện học bổng**
Biểu diễn các điều kiện xét học bổng sau:
- GPA ≥ 3.5 hoặc có thành tích đặc biệt thì được xét duyệt.
- Không đạt GPA ≥ 3.5 và không có thành tích đặc biệt thì không được xét duyệt.
- Được xét duyệt và nộp đơn đúng hạn thì nhận học bổng.

**Bài tập 5: Lập lịch làm việc**
Biểu diễn các quy tắc lịch làm việc sau:
- Là cuối tuần hoặc ngày lễ thì được nghỉ.
- Không phải cuối tuần và không phải ngày lễ thì phải đi làm.
- Là cuối tuần nhưng có dự án gấp thì vẫn phải đi làm.

**Bài tập 6: Tam giác**
Cho $$a, b, c$$ là các số thực. Viết biểu thức logic diễn đạt điều kiện để $$a, b, c$$ lần lượt là:
(a) Độ dài ba cạnh của một tam giác.
(b) Độ dài ba cạnh của một tam giác vuông có cạnh huyền $$c$$.
(c) Độ dài ba cạnh của một tam giác vuông cân có cạnh huyền $$c$$.
(d) Độ dài ba cạnh của một tam giác đều.

### Bài tập bổ sung từ slide PPT: Viết biểu thức logic

Viết biểu thức logic mệnh đề cho các mô tả sau (đặt biến mệnh đề phù hợp):

1. Điều kiện để tháng `m` là dữ liệu hợp lệ.
2. Điều kiện để tháng `m` có 30 ngày.
3. Điều kiện để tháng 2 có 29 ngày.
4. Điều kiện để `A, B, C` là các góc của một tam giác.
5. Điều kiện để `A, B, C` là các góc của một tam giác vuông.
6. Điều kiện để `A, B, C` là các góc của một tam giác cân.
7. Điều kiện để `A, B, C` là các góc của một tam giác đều.
8. Điều kiện để học sinh A xét điểm theo tổ hợp A0 đậu vào khoa CNTT năm 2019.
9. Điều kiện để bạn được nhận học bổng 100% trong học kỳ 1 năm học 2020–2021.
10. Điều kiện tiếng Anh để bạn được đăng ký học phần năm 3.

**Bài tập bổ sung (từ slide):**

Bài tập 3: Hàm `eq(X, Y)` trả về `1` khi giá trị của `X` và `Y` bằng nhau, và trả về `0` trong các trường hợp còn lại. Biểu thức nào dưới đây là điều kiện cần và đủ để lời gọi `eq(eq(A, B), eq(B, C))` trả về `1`?

A. `(A = B và B = C) hoặc (A ≠ B và B ≠ C)`

B. `(A = B và B = C) hoặc (A ≠ B hoặc B ≠ C)`

C. `(A = B và B = C) hoặc (A = C)`

D. `(A = B hoặc B = C) hoặc (A = C)`

---


## Công cụ tương tác

Nhập một câu để kiểm tra xem nó có phải mệnh đề không, rồi tính giá trị chân trị của biểu thức với các biến $$P, Q, R$$.
<div class="interactive-demo" markdown="1">
<div data-demo="proposition-checker"></div>
</div>
<div class="interactive-demo" markdown="1">
<div data-demo="logic-evaluator"></div>
</div>
<script src="{{ '/public/js/logic-operator-widgets.js' | relative_url }}"></script>

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Phép toán logic** (`¬`, `∧`, `∨`, `→`, `↔`, `⊕`) ghép các mệnh đề sơ cấp thành mệnh đề phức hợp; mỗi phép toán có bảng chân trị riêng và toán tử tương ứng trong ngôn ngữ lập trình.
- **Mệnh đề kéo theo** $$p \to q$$ chỉ sai khi $$p$$ đúng và $$q$$ sai; khi $$p$$ sai thì luôn đúng (vacuously true).
- **Biểu thức logic** tuân theo thứ tự ưu tiên: `¬` > `∧` > `∨` > `→` > `↔` > `⊕`; nên dùng dấu ngoặc để tránh nhầm lẫn.
- Hai biểu thức **tương đương** ($$\equiv$$) khi có cùng bảng chân trị; các **luật logic** (De Morgan, phân phối, hấp thụ, bù, v.v.) cho phép biến đổi biểu thức mà không làm thay đổi ý nghĩa.
- Các phép toán logic được ứng dụng trực tiếp trong kiểm tra đầu vào, phân quyền, truy vấn dữ liệu và thiết kế test case.

Trong bài tiếp theo, chúng ta sẽ dùng **bảng chân trị** để liệt kê và kiểm chứng mọi trường hợp của biểu thức logic.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=p78HgbsYw2M">001B TOÁN RỜI RẠC Logic mệnh đề Thế nào là mệnh đề Phép toán mệnh đề</a> — Đỗ Văn Đức - ĐH GTVT, tiếng Việt. Minh họa các phép toán mệnh đề qua ví dụ tiếng Việt.
- <a href="https://www.youtube.com/watch?v=7mulE-zramc">Intro to Truth Tables |  Negation, Conjunction, and Disjunction</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày phủ định, hội và tuyển trên bảng chân trị, khớp với các phép toán cơ bản của bài.
- <a href="https://www.youtube.com/watch?v=xag9TEAORK4">CONDITIONALS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giải thích phép kéo theo — phép toán thường bị hiểu nhầm khi chuyển từ câu điều kiện tự nhiên.
