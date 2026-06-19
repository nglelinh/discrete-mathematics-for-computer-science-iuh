---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Quy tắc Suy diễn

**Toán Rời Rạc — IUH**

Tiết 5 (45 phút)

---

# Mục tiêu tiết học

- Định nghĩa quy tắc suy diễn
- Tự chứng minh bằng bảng chân trị
- Modus Ponens (khẳng định)
- Modus Tollens (phủ định)
- Tam đoạn luận giả định
- Phương pháp mâu thuẫn

---

# Từ mệnh đề đến suy luận

Biết T/F chưa đủ — cần **suy luận**:

- Từ điều **đã biết** → kết luận **mới**
- Thám tử, compiler, hệ thống phân quyền đều suy diễn

---

# Ví dụ suy luận hàng ngày

> Nếu học tốt thì thi đậu.
> SV A học tốt.
> 
> ∴ SV A thi đậu.

Cùng khuôn mẫu với `if-then` trong code

---

# Định nghĩa Quy tắc Suy diễn

**Quy tắc suy diễn** (Rule of Inference) là một dạng lập luận có dạng:

$$(p_1 \land p_2 \land \cdots \land p_n) \to q$$

trong đó biểu thức trên là một **hằng đúng** (tautology).

**Thành phần**:
- $p_1, p_2, \dots , p_n$: Các **tiền đề** (hay giả thiết)
- $q$: **Kết luận**

Nếu tất cả tiền đề đúng thì kết luận **bắt buộc** phải đúng.

---

# Ba cách biểu diễn quy tắc suy diễn

1. **Dạng hằng đúng**:
   $$(p_1 \land \dots \land p_n) \to q \text{ là tautology}$$

2. **Dạng dòng suy diễn**:
   ```
   p₁
   p₂
   ...
   pn
   ────
   ∴ q
   ```

3. **Dạng ký hiệu**:
   $$p_1, p_2, \dots , p_n \vdash q$$

---

# 3 cách biểu diễn

**1. Hằng đẳng:**

$$(p_1 \land \cdots \land p_n) \Rightarrow q$$

**2. Dòng suy diễn:**

```
p₁
p₂
...
pn
────
∴ q
```

**3. Lập luận hợp lệ** ⟺ cột kết luận toàn T khi mọi tiền đề T

---

# Kiểm tra bằng bảng chân trị

Lập luận hợp lệ khi:

$$[(p_1 \land \cdots \land p_n) \to q]$$

là **tautology**

Cột cuối của bảng chân trị = toàn **T**

---

# Thực hành: Tự chứng minh (1)

**Bài:** Chứng minh Modus Ponens hợp lệ

Tiền đề: $p \to q$ và $p$

Kết luận: $q$

Cần kiểm tra: $[(p \to q) \land p] \to q$ là tautology?

---

# Bảng chân trị — Modus Ponens

| $p$ | $q$ | $p \to q$ | $p \land (p \to q)$ | Kết quả |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T |
| T | F | F | F | T |
| F | T | T | F | T |
| F | F | T | F | T |

Cột cuối toàn **T** → lập luận **hợp lệ** ✓

---

# Modus Ponens — Khẳng định

$$\frac{p \to q,\; p}{\therefore q}$$

**Nếu** $p \to q$ **và** $p$ **thì** $q$

Nền tảng mọi câu lệnh `if` trong lập trình

---

# MP — Ví dụ học tập

> Nếu học tốt → thi đậu
> Học tốt
> 
> ∴ Thi đậu

---

# MP — Ví dụ lập trình

```python
if age < 18:      # p → q
    return "DENIED"

# age = 16 → p đúng → q đúng
```

Mỗi lần `if` chạy nhánh → một phép **Modus Ponens**

---

# Thực hành: Tự chứng minh (2)

**Bài:** Chứng minh Modus Tollens

Tiền đề: $p \to q$ và $\neg q$

Kết luận: $\neg p$

Kiểm tra: $[(p \to q) \land \neg q] \to \neg p$

---

# Modus Tollens — Phủ định

$$\frac{p \to q,\; \neg q}{\therefore \neg p}$$

**Nếu** $p \to q$ **và** $q$ sai **thì** $p$ sai

"Ngược" của Modus Ponens

---

# MT — Ví dụ bảo mật

> Nếu admin → truy cập bảng `users`
> Không truy cập được `users`
> 
> ∴ Không phải admin

---

# MT — Ví dụ kiểm thử

> Nếu không lỗi → mọi test pass
> Test #7 **fail**
> 
> ∴ Module **có lỗi**

Dùng nhiều trong **debugging**

---

# MT — Ví dụ API

> Nếu token hợp lệ → status 200
> Server trả 401
> 
> ∴ Token không hợp lệ

---

# Tam đoạn luận giả định

**Hypothetical Syllogism**

$$\frac{p \to q,\; q \to r}{\therefore p \to r}$$

Nối chuỗi mệnh đề kéo theo

---

# Tam đoạn luận — Ví dụ pipeline

> Nếu nhận request → log
> Nếu log OK → chuyển controller
> 
> ∴ Nếu nhận request → chuyển controller

---

# Tam đoạn luận — Ví dụ phân quyền

> Editor → Contributor
> Contributor → Sửa bài viết
> 
> ∴ Editor → Sửa bài viết

Nền tảng **kế thừa quyền** (role hierarchy)

---

# Thực hành: Tự chứng minh (3)

**Bài:** Chứng minh tam đoạn luận giả định

$$[(p \to q) \land (q \to r)] \to (p \to r)$$

→ Lập bảng chân trị 8 dòng (3 biến)

---

# Thực hành: Tam đoạn luận (4)

Chứng minh bằng bảng chân trị:

$$(p \to q) \land (q \to r) \land \neg(p \to r)$$

→ Đây là **contradiction** (phủ định quy tắc hợp lệ)

---

# Phương pháp mâu thuẫn (Proof by Contradiction)

**Định nghĩa**:
Để chứng minh một mệnh đề $P$ là đúng, ta giả sử phủ định của nó ($\neg P$) và dẫn đến mâu thuẫn.

**Các bước**:
1. Giả sử $\neg P$ là đúng.
2. Dùng các quy tắc suy diễn hợp lệ suy ra một mâu thuẫn (thường là $Q \land \neg Q$).
3. Vì giả thiết dẫn đến điều không thể xảy ra → $\neg P$ sai.
4. Do đó $P$ đúng.

**Cơ sở logic**:
$$\neg P \to (Q \land \neg Q) \quad \Rightarrow \quad P$$

---

# Mâu thuẫn (Contradiction)

**Định nghĩa**: Một mệnh đề có dạng $Q \land \neg Q$ — không thể vừa đúng vừa sai.

**Ví dụ thực tế**:
- Một biến không thể đồng thời là `True` và `False`
- Một user không thể vừa `logged_in = true` vừa `logged_in = false`

Đây là nền tảng của **luật phi mâu thuẫn** trong mọi hệ thống.

---

# Cơ sở logic

$$\neg P \to (Q \land \neg Q) \Rightarrow P$$

Nếu giả sử phủ định dẫn đến vô lý → kết luận gốc đúng

Chỉ 2 khả năng: $P$ hoặc $\neg P$

---

# Mâu thuẫn trong suy diễn

Dạng suy luận:

```
Giả sử ¬p
Suy ra q ∧ ¬q   (mâu thuẫn)
────────────
∴ p
```

Hoặc: tiền đề dẫn đến F → tiền đề không thể cùng đúng

---

# Ví dụ mâu thuẫn — Toán

Chứng minh: $\sqrt{2}$ vô tỷ

- Giả sử $\sqrt{2} = a/b$ (tối giản)
- Suy ra $a, b$ đều chẵn
- Mâu thuẫn với "tối giản"
- ∴ $\sqrt{2}$ vô tỷ

---

# Ví dụ mâu thuẫn — CS

Chứng minh: không thể vừa đăng nhập thành công vừa thất bại

$$p \land \neg p \equiv F$$

→ Luật **phi mâu thuẫn** trong hệ thống xác thực

---

# Khi nào dùng phản chứng?

- Kết luận mang tính **phủ định** ("không tồn tại...")
- Đường đi **trực tiếp** quá dài
- Chứng minh **duy nhất** hoặc **vô lý**

---

# Các quy tắc suy diễn cơ bản (nhóm 1)

**1. Modus Ponens (MP)**
$$\frac{p \to q,\ p}{\therefore q}$$

**2. Modus Tollens (MT)**
$$\frac{p \to q,\ \neg q}{\therefore \neg p}$$

**3. Hypothetical Syllogism**
$$\frac{p \to q,\ q \to r}{\therefore p \to r}$$

**4. Disjunctive Syllogism**
$$\frac{p \lor q,\ \neg p}{\therefore q}$$

---

# Các quy tắc suy diễn cơ bản (nhóm 2)

**5. Addition**
$$p \vdash p \lor q$$

**6. Simplification**
$$p \land q \vdash p$$

**7. Conjunction**
$$p,\ q \vdash p \land q$$

**8. Resolution** (quan trọng trong SAT)
$$\frac{p \lor q,\ \neg p \lor r}{\therefore q \lor r}$$

**9. Constructive Dilemma**
$$\frac{p \to q,\ r \to s,\ p \lor r}{\therefore q \lor s}$$

---

# Bằng chứng hợp lệ của các quy tắc

Mỗi quy tắc suy diễn hợp lệ khi và chỉ khi:
$$(p_1 \land p_2 \land \dots \land p_n) \to q$$
là một **tautology**.

**Ví dụ chứng minh MP**:
Bảng chân trị cho $[(p \to q) \land p] \to q$ có cột kết quả toàn T.

---

# Các ngụy biện thường gặp (Fallacies)

| Ngụy biện                  | Dạng sai                          | Ví dụ                              |
|----------------------------|-----------------------------------|------------------------------------|
| Khẳng định kết luận (Affirming the consequent) | $p \to q,\ q \vdash p$         | Nếu mưa thì ướt. Đường ướt. Vậy trời mưa. |
| Phủ định tiền đề (Denying the antecedent) | $p \to q,\ \neg p \vdash \neg q$ | Nếu mưa thì ướt. Không mưa. Vậy đường khô. |
| Sai lầm "hoặc"             | $p \lor q,\ p \vdash \neg q$      | Sai khi cả hai có thể đúng         |

**Lưu ý**: Không phải mọi lập luận nghe có vẻ logic đều là hợp lệ. Luôn kiểm tra bằng bảng chân trị hoặc quy tắc đã biết.

| Quy tắc | Dạng |
|:---|:---|
| Phép thêm | $p \vdash p \lor q$ |
| Phép giản lược | $p \land q \vdash p$ |
| Phép nối | $p,\; q \vdash p \land q$ |
| Resolution | $p \lor q,\; \neg p \lor r \vdash q \lor r$ |

---

# Ứng dụng trong CS

| Lĩnh vực | Quy tắc |
|:---|:---|
| `if-then` | Modus Ponens |
| Debug / test | Modus Tollens |
| Pipeline | Tam đoạn luận |
| SAT solver | Resolution + CNF |
| Chứng minh phần mềm | Mọi quy tắc |

---

# Thực hành 1 (20 phút)

**Tự chứng minh** bằng bảng chân trị:

Modus Tollens: $[(p \to q) \land \neg q] \to \neg p$

Làm nhóm, trình bày 1 dòng suy diễn

---

# Thực hành 2 (20 phút)

Nhận diện quy tắc suy diễn:

(a) Nếu mưa → mang ô. Không mang ô. ∴ Không mưa.

(b) Nếu $x=2$ → $x^2=4$. Nếu $x^2=4$ → $\sqrt{x^2}=2$. ∴ Nếu $x=2$ → $\sqrt{x^2}=2$.

---

# Thực hành 3 (15 phút)

Viết dòng suy diễn cho:

> Nếu token hợp lệ → cho phép truy cập
> Token hợp lệ
> 
> ∴ ?

Dùng đúng ký hiệu MP

---

# Thực hành 4 (15 phút)

Giải thích bằng **mâu thuẫn**:

> Không thể vừa `logged_in = True` vừa `logged_in = False`

Viết 3–4 bước suy luận

---

# Lỗi thường gặp

- Nhầm MP với MT (đảo $\neg q$ và $p$)
- "Khẳng định kết quả" — sai lập luận!
- Không kiểm tra tautology khi tự chứng minh
- Nhầm giả sử phản chứng với giả thiết gốc

---

# Tóm tắt Tiết 5

- Quy tắc suy diễn = tautology của $(tiền đề) \to kết luận$
- MP: khẳng định | MT: phủ định
- Tam đoạn luận: nối chuỗi $\to$
- Mâu thuẫn: giả sử $\neg P$ → vô lý → $P$

---

# Bài tập ôn tập (1/2)

1. **Bài 1**: Nhận diện quy tắc:
   > Nếu token hợp lệ thì truy cập. Token hợp lệ. Vậy truy cập được.

2. **Bài 2**: Viết dòng suy diễn dùng Modus Tollens:
   > Nếu lỗi thì test fail. Test #12 không fail.

3. **Bài 3**: Chứng minh Tam đoạn luận:
   $$[(p \to q) \land (q \to r)] \to (p \to r)$$

---

# Bài tập ôn tập (2/2)

4. **Bài 4**: Giải thích bằng mâu thuẫn:
   Tại sao không thể `is_logged_in = True` và `False` cùng lúc.

5. **Bài 5**: Nhận diện (hoặc sai lầm):
   > Nếu điểm >=5 thì qua môn. Anh ấy qua môn. Vậy điểm >=5.

---

# Tiết sau

**Logic vị từ** hoặc **Tam đoạn luận tuyển & Resolution**

- Lượng từ $\forall$, $\exists$
- Quy tắc suy diễn nâng cao

---

# Câu hỏi?