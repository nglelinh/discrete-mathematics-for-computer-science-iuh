---
layout: post
title: "Quy tắc Suy diễn"
categories: chapter01
date: 2021-01-01
order: 5
required: true
lang: en
---

Biết một điều kiện là đúng hay sai đã khó, nhưng đó mới chỉ là bước đầu. Trong thực tế, chúng ta hiếm khi có sẵn tất cả sự thật — ta phải **suy luận** để đi từ những điều đã biết đến những kết luận mới.

Một thám tử có nhiều manh mối: "Nếu hung thủ có chìa khóa thì đó là nội bộ" và "Hung thủ có chìa khóa". Ông ta kết luận: "Đây là nội bộ". Một compiler thấy: "Nếu kiểu dữ liệu không khớp thì báo lỗi" và "Kiểu không khớp". Nó kết luận: "Báo lỗi". Một hệ thống kiểm soát truy cập thấy: "Nếu người dùng có token hợp lệ thì cho phép truy cập" và "Người dùng có token hợp lệ". Nó kết luận: "Cho phép truy cập".

Cả ba tình huống trên đều dùng cùng một khuôn mẫu suy luận — một **quy tắc suy diễn**. Bài học này sẽ giới thiệu những quy tắc suy diễn cơ bản nhất, giúp bạn đi từ giả thiết đến kết luận một cách chắc chắn.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Giải thích** quy tắc suy diễn là gì và vì sao nó cần thiết.
- **Nhận diện** và **áp dụng** các quy tắc suy diễn cơ bản: Modus Ponens, Modus Tollens, tam đoạn luận giả định, tam đoạn luận tuyển, phép thêm, phép giản lược, phép nối, phép giải.
- **Kiểm tra** tính hợp lệ của một suy luận bằng quy tắc suy diễn.
- **Áp dụng** quy tắc suy diễn vào suy luận trong code, bảo mật, và kiểm thử.

**Từ khóa**: rule of inference, Modus Ponens, Modus Tollens, hypothetical syllogism, disjunctive syllogism, addition, simplification, conjunction, resolution, validity.

---

## 1. Định nghĩa Quy tắc Suy diễn

Trong các chứng minh toán học (và trong cả lập trình, phân tích hệ thống), ta thường thấy những lý luận dẫn xuất có dạng:

> Nếu $$p_1$$ và $$p_2$$ và $$\dots$$ và $$p_n$$ thì $$q$$.

Dạng lý luận này là **đúng** khi biểu thức

$$
(p_1 \land p_2 \land \dots \land p_n) \to q
$$

là **hằng đúng** (luôn đúng với mọi tổ hợp chân trị).

Ta gọi dạng lý luận trên là một **quy tắc suy diễn** (rule of inference). Có ba cách biểu diễn một quy tắc suy diễn:

**Cách 1 – Biểu thức hằng đúng:**

$$
(p_1 \land p_2 \land \dots \land p_n) \Rightarrow q
$$

(ký hiệu $$\Rightarrow$$ có nghĩa "kéo theo một cách logic", tức $$(p_1 \land \dots \land p_n) \to q$$ là hằng đúng).

**Cách 2 – Dòng suy diễn:**

$$
\begin{array}{c}
p_1 \\
p_2 \\
\vdots \\
p_n \\
\hline
\therefore q
\end{array}
$$

**Cách 3 – Mô hình suy diễn:**

> $$p_1$$
> $$p_2$$
> $$\vdots$$
> $$p_n$$
> 
> ————————————
> 
> $\therefore q$

Các biểu thức $$p_1, p_2, \dots, p_n$$ được gọi là **giả thiết** (hay **tiền đề**), biểu thức $$q$$ được gọi là **kết luận**.

![Bảng tứ đối — quan hệ suy luận cổ điển](/discrete-mathematics-for-computer-science-iuh/img/course/Square_of_opposition__set_diagrams.svg)

*Hình 1.21: Quy tắc suy diễn là nền tảng của mọi lập luận hợp lệ — từ tiền đề đúng rút ra kết luận đúng.*

---

## 2. Modus Ponens (Quy tắc Khẳng định)

Đây có lẽ là quy tắc suy diễn quen thuộc nhất. Nó nói rằng: nếu ta biết một mệnh đề kéo theo đúng và vế trái của nó đúng, thì vế phải cũng đúng.

$$
\begin{array}{c}
p \to q \\
p \\
\hline
\therefore q
\end{array}
$$

Tương đương với hằng đẳng thức:

$$
[(p \to q) \land p] \Rightarrow q
$$

**Ví dụ 1 (học tập):**

> Nếu học tốt thì thi đậu.
> SV A học tốt.
> 
> ——————————————
> 
> $$\therefore$$ SV A thi đậu.

**Ví dụ 2 (dân gian):**

> Nếu chuồn chuồn bay thấp thì trời mưa.
> Chuồn chuồn bay thấp.
> 
> ————————————————
> 
> $$\therefore$$ Trời mưa.

**Ví dụ 3 (lập trình – kiểm tra đầu vào):**

> Nếu `tuổi < 18` thì từ chối truy cập.
> `tuổi = 16`, vậy `tuổi < 18` là đúng.
> 
> ————————————————————
> 
> $$\therefore$$ Từ chối truy cập.

```python
def check_access(age):
    if age < 18:          # p → q: nếu tuổi < 18 thì từ chối
        return "DENIED"
    return "ALLOWED"

# Với age = 16: p đúng (age < 18), suy ra q đúng (DENIED)
print(check_access(16))   # DENIED
```

Modus Ponens là nền tảng của mọi câu lệnh `if-then` trong lập trình. Mỗi khi máy tính kiểm tra điều kiện trong `if` và thực thi thân của nó, nó đang làm một phép suy diễn Modus Ponens.

![Modus Ponens: p → q và p suy ra q](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-Implication.PNG)

*Hình 1.22: Modus Ponens — nếu p → q đúng và p đúng, thì q phải đúng (nền tảng của mọi câu lệnh `if`).*

---

## 3. Modus Tollens (Quy tắc Phủ định)

Quy tắc này là "ngược" của Modus Ponens: nếu $$p \to q$$ đúng nhưng $$q$$ sai (phủ định), thì $$p$$ cũng phải sai.

$$
\begin{array}{c}
p \to q \\
\neg q \\
\hline
\therefore \neg p
\end{array}
$$

Tức $$[(p \to q) \land \neg q] \Rightarrow \neg p$$ là hằng đúng.

**Ví dụ 1 (bảo mật):**

> Nếu người dùng là admin thì có quyền truy cập bảng `users`.
> Người dùng này **không có** quyền truy cập bảng `users`.
> 
> ————————————————————
> 
> $$\therefore$$ Người dùng này **không phải** admin.

**Ví dụ 2 (kiểm thử):**

> Nếu module không có lỗi thì tất cả test cases đều pass.
> Test case #7 **fail**.
> 
> ——————————————————————————
> 
> $$\therefore$$ Module **có lỗi**.

**Ví dụ 3 (xác thực – token):**

> Nếu token hợp lệ thì server trả về status 200.
> Server trả về status 401 (Unauthorized).
> 
> ————————————————————————————
> 
> $$\therefore$$ Token **không hợp lệ**.

Modus Tollens đặc biệt hữu ích trong debugging và kiểm thử: khi kết quả kỳ vọng không xảy ra, ta suy ra giả định ban đầu đã sai.

![Modus Tollens: p → q và ¬q suy ra ¬p](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-NOT.png)

*Hình 1.23: Modus Tollens — nếu p → q đúng nhưng q sai, thì p phải sai (dùng nhiều trong debugging và kiểm thử).*

---

## 4. Tam đoạn luận Giả định (Hypothetical Syllogism)

Quy tắc này cho phép "nối chuỗi" các mệnh đề kéo theo:

$$
\begin{array}{c}
p \to q \\
q \to r \\
\hline
\therefore p \to r
\end{array}
$$

Tức $$[(p \to q) \land (q \to r)] \Rightarrow (p \to r)$$.

**Ví dụ 1 (xử lý pipeline):**

> Nếu nhận được request thì log vào hệ thống.
> Nếu log thành công thì chuyển request đến controller.
> 
> —————————————————————————————
> 
> $$\therefore$$ Nếu nhận được request thì chuyển đến controller.

**Ví dụ 2 (phân quyền – role chaining):**

> Nếu user là editor thì user là contributor.
> Nếu user là contributor thì có quyền chỉnh sửa bài viết.
> 
> ————————————————————————————
> 
> $$\therefore$$ Nếu user là editor thì có quyền chỉnh sửa bài viết.

Tam đoạn luận giả định là cơ sở cho mọi chuỗi xử lý (pipeline) và kế thừa quyền (role hierarchy) trong hệ thống phần mềm. Nó cũng xuất hiện trong các chứng minh toán học dài — mỗi bước là một mắt xích trong chuỗi suy luận.

![Chuỗi suy luận — nối các mệnh đề kéo theo](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

*Hình 1.24: Tam đoạn luận giả định — từ p → q và q → r suy ra p → r, nền tảng của pipeline và kế thừa quyền.*

---

## 5. Tam đoạn luận Tuyển (Disjunctive Syllogism)

Khi ta biết một trong hai mệnh đề đúng, và một mệnh đề sai, thì mệnh đề còn lại phải đúng:

$$
\begin{array}{c}
p \lor q \\
\neg p \\
\hline
\therefore q
\end{array}
\quad\quad
\begin{array}{c}
p \lor q \\
\neg q \\
\hline
\therefore p
\end{array}
$$

**Ví dụ 1 (xử lý lỗi):**

> Lỗi xuất phát từ database hoặc từ network.
> Lỗi **không phải** từ database.
> 
> ————————————————————
> 
> $$\therefore$$ Lỗi từ network.

**Ví dụ 2 (tuyển chọn):**

> Hồ sơ được duyệt hoặc bị từ chối.
> Hồ sơ không bị từ chối.
> 
> ————————————————————
> 
> $$\therefore$$ Hồ sơ được duyệt.

Trong lập trình, quy tắc này thường được dùng trong xử lý ngoại lệ và chẩn đoán lỗi: khi ta thu hẹp không gian nguyên nhân, mỗi bước loại trừ là một ứng dụng của tam đoạn luận tuyển.

![Tam đoạn luận tuyển: p ∨ q và ¬p suy ra q](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-OR.png)

*Hình 1.25: Tam đoạn luận tuyển — biết p ∨ q đúng và ¬p đúng, suy ra q (loại trừ nguyên nhân trong chẩn đoán lỗi).*

---

## 6. Phép Thêm (Addition)

Từ một mệnh đề đúng, ta có thể thêm bất kỳ mệnh đề nào vào bằng phép tuyển (kết quả vẫn đúng):

$$
\begin{array}{c}
p \\
\hline
\therefore p \lor q
\end{array}
$$

Dù nghe có vẻ hiển nhiên, quy tắc này rất hữu ích trong các chứng minh phức tạp — nó cho phép ta mở rộng giả thiết khi cần:

**Ví dụ:**

> Hệ thống đang hoạt động.
> 
> ————————————
> 
> $$\therefore$$ Hệ thống đang hoạt động hoặc đang bảo trì.

---

## 7. Phép Giản lược (Simplification)

Ngược lại với phép thêm: từ một mệnh đề hội đúng, ta suy ra mỗi thành phần của nó cũng đúng:

$$
\begin{array}{c}
p \land q \\
\hline
\therefore p
\end{array}
\quad\quad
\begin{array}{c}
p \land q \\
\hline
\therefore q
\end{array}
$$

**Ví dụ (kiểm tra điều kiện phức hợp):**

> Tài khoản hợp lệ **và** mật khẩu đúng.
> 
> ————————————————————
> 
> $$\therefore$$ Tài khoản hợp lệ.

Khi một hàm trong code trả về tuple `(status, data)`, và ta chỉ quan tâm `status`, đó là một ứng dụng của Simplification.

---

## 8. Phép Nối (Conjunction)

Nếu hai mệnh đề đều đúng, ta có thể nối chúng thành một mệnh đề hội:

$$
\begin{array}{c}
p \\
q \\
\hline
\therefore p \land q
\end{array}
$$

**Ví dụ (kiểm tra bảo mật):**

> Người dùng đã xác thực.
> Người dùng có quyền admin.
> 
> ——————————————————
> 
> $$\therefore$$ Người dùng đã xác thực và có quyền admin.

Phép nối thường dùng ở cuối một chuỗi suy luận để tổng hợp kết luận từ nhiều chứng cứ riêng lẻ.

---

## 9. Phép Giải (Resolution)

Quy tắc này đặc biệt quan trọng trong các thuật toán chứng minh tự động (automated theorem proving) và SAT solvers:

$$
\begin{array}{c}
p \lor q \\
\neg p \lor r \\
\hline
\therefore q \lor r
\end{array}
$$

Nói cách khác: nếu $$p$$ đúng thì từ $$p \lor q$$ ta có $$q$$, còn nếu $$p$$ sai thì từ $$\neg p \lor r$$ ta có $$r$$. Dù thế nào, $$q \lor r$$ cũng đúng.

**Ví dụ (trí tuệ nhân tạo – suy luận trong hệ chuyên gia):**

> Dữ liệu bị hỏng ($$p$$) hoặc lỗi mạng ($$q$$).
> Dữ liệu không bị hỏng ($$\neg p$$) hoặc lỗi phần mềm ($$r$$).
> 
> ———————————————————————————————
> 
> $$\therefore$$ Lỗi mạng ($$q$$) hoặc lỗi phần mềm ($$r$$).

Resolution là nền tảng của **phương pháp chứng minh bác bỏ** (refutation proof) dùng trong SAT solvers. Khi kết hợp resolution với Clausausal Normal Form (CNF), máy tính có thể kiểm tra tính thỏa được của công thức với hàng triệu biến.

---

## 10. Bảng Tổng Hợp các Quy tắc Suy diễn

| Tên quy tắc | Dạng suy diễn | Tên gọi |
|---|---|---|
| Modus Ponens | $$ \dfrac{p \to q,\; p}{\therefore q} $$ | Quy tắc khẳng định |
| Modus Tollens | $$ \dfrac{p \to q,\; \neg q}{\therefore \neg p} $$ | Quy tắc phủ định |
| Hypothetical Syllogism | $$ \dfrac{p \to q,\; q \to r}{\therefore p \to r} $$ | Tam đoạn luận giả định |
| Disjunctive Syllogism | $$ \dfrac{p \lor q,\; \neg p}{\therefore q} $$ | Tam đoạn luận tuyển |
| Addition | $$ \dfrac{p}{\therefore p \lor q} $$ | Phép thêm |
| Simplification | $$ \dfrac{p \land q}{\therefore p} $$ | Phép giản lược |
| Conjunction | $$ \dfrac{p,\; q}{\therefore p \land q} $$ | Phép nối |
| Resolution | $$ \dfrac{p \lor q,\; \neg p \lor r}{\therefore q \lor r} $$ | Phép giải |

---

## 12. Ứng dụng trong Khoa học Máy tính

### 12.1. Kiểm chứng Hình thức (Formal Verification)

Các công cụ như Dafny, Coq, và Isabelle/HoL sử dụng quy tắc suy diễn để chứng minh chương trình đúng. Mỗi bước suy luận trong chứng minh là một quy tắc suy diễn được kiểm tra bởi máy tính.

### 12.2. SAT Solvers

SAT solver chuyển bài toán thành CNF và áp dụng resolution để kiểm tra tính thỏa được. Hàng triệu phép resolution mỗi giây là cách máy tính "suy luận" ở quy mô mà con người không thể làm được.

### 12.3. Hệ Thống Chuyên gia (Expert Systems)

Các hệ thống như Mycin (chẩn đoán bệnh) dùng mô hình suy diễn dạng:

> NẾU (triệu chứng A VÀ triệu chứng B) THÌ (bệnh C) với độ tin cậy 80%.

Mỗi lần người dùng nhập thêm triệu chứng, hệ thống dùng Modus Ponens để rút ra kết luận mới.

### 12.4. Hệ thống Kiểu (Type Systems)

Trong trình biên dịch, suy luận kiểu (type inference) dựa trên các quy tắc suy diễn. Ví dụ, một quy tắc đơn giản:

> Nếu $$e_1 : \text{Int}$$ và $$e_2 : \text{Int}$$ thì $$e_1 + e_2 : \text{Int}$$.

Trình biên dịch dùng Modus Ponens để suy ra kiểu của biểu thức phức hợp từ kiểu của các biểu thức con.

---

## Bài tập

### Bài tập 1: Nhận diện Quy tắc Suy diễn

Xác định quy tắc suy diễn được dùng trong mỗi suy luận sau:

(a) Nếu hôm nay là thứ Bảy thì không có lớp học. Hôm nay là thứ Bảy. Vậy không có lớp học.

(b) Nếu trời mưa thì tôi mang ô. Tôi không mang ô. Vậy trời không mưa.

(c) Nếu $$x = 2$$ thì $$x^2 = 4$$. Nếu $$x^2 = 4$$ thì $$\sqrt{x^2} = 2$$. Vậy nếu $$x = 2$$ thì $$\sqrt{x^2} = 2$$.

(d) Hệ thống bị tấn công từ bên ngoài hoặc từ nội bộ. Hệ thống không bị tấn công từ nội bộ. Vậy hệ thống bị tấn công từ bên ngoài.

<details>
<summary>Đáp án</summary>

(a) **Modus Ponens**: $$p \to q$$ (nếu thứ Bảy thì không lớp), $$p$$ (thứ Bảy), suy ra $$q$$ (không lớp).

(b) **Modus Tollens**: $$p \to q$$ (nếu mưa thì mang ô), $$\neg q$$ (không mang ô), suy ra $$\neg p$$ (không mưa).

(c) **Hypothetical Syllogism**: $$p \to q$$ và $$q \to r$$, suy ra $$p \to r$$.

(d) **Disjunctive Syllogism**: $$p \lor q$$ (ngoài hoặc trong) và $$\neg q$$ (không trong), suy ra $$p$$ (ngoài).

</details>

### Bài tập 2: Kiểm tra Tính Hợp lệ

Mỗi suy luận sau có hợp lệ không? Nếu không, hãy chỉ ra sai lầm và cho phản ví dụ.

(a) Nếu con số chia hết cho 2 thì nó là số chẵn. Con số là số chẵn. Vậy nó chia hết cho 2.

(b) Nếu file tồn tại thì đọc được. File không tồn tại. Vậy không đọc được.

(c) Nếu kết nối có timeout thì server quá tải hoặc mạng chậm. Kết nối có timeout. Vậy server quá tải.

<details>
<summary>Đáp án</summary>

(a) **Không hợp lệ** — Sai lầm khẳng định hệ quả (affirming the consequent). $$p \to q$$ và $$q$$ không suy ra $$p$$. Phản ví dụ: số 6 là số chẵn nhưng có thể không chia hết cho 2 trong một ngữ cảnh khác? Thực tế mọi số chẵn đều chia hết cho 2 nên phản ví dụ này đặc biệt khó tìm. Tuy nhiên về mặt logic thuần túy, dạng suy luận là sai. Một phản ví dụ tổng quát hơn: "Nếu là chó thì có 4 chân. Con vật có 4 chân. Vậy nó là chó." — Sai, vì mèo cũng 4 chân.

(b) **Không hợp lệ** — Sai lầm phủ định tiền đề (denying the antecedent). $$p \to q$$ và $$\neg p$$ không suy ra $$\neg q$$. Phản ví dụ: file tồn tại nhưng bị hỏng — không đọc được dù file tồn tại. Hoặc: file tồn tại nhưng không có quyền đọc.

(c) **Không hợp lệ** — Đây là trường hợp thiếu kết luận. Từ $$p \to (r \lor s)$$ và $$p$$, Modus Ponens cho ta $$r \lor s$$ (server quá tải hoặc mạng chậm). Không thể kết luận riêng $$r$$ (server quá tải) vì còn khả năng $$s$$ (mạng chậm). Đây không phải là một fallacy kinh điển, nhưng suy luận đi xa hơn những gì giả thiết cho phép.

</details>

### Bài tập 3: Suy luận trong Lập trình

Cho đoạn chương trình Python sau:

```python
if user.is_admin() or user.has_permission("edit"):
    document.editable = True
else:
    document.editable = False
```

Biết rằng `user.is_admin()` trả về `False`. Hãy dùng quy tắc suy diễn để suy ra trạng thái của `document.editable` trong hai trường hợp:

(a) `user.has_permission("edit")` trả về `True`.
(b) `user.has_permission("edit")` trả về `False`.

<details>
<summary>Đáp án</summary>

Đặt $$p =$$ "user.is_admin() đúng", $$q =$$ "user.has_permission('edit') đúng". Điều kiện trong `if` là $$p \lor q$$.

Biết $$\neg p$$ (admin trả về `False`).

(a) Nếu $$q$$ đúng: Từ $$p \lor q$$ và $$\neg p$$, Disjunctive Syllogism cho $$q$$. Kết luận: điều kiện `if` đúng → `document.editable = True`.

(b) Nếu $$q$$ sai (tức $$\neg q$$): Từ $$p \lor q$$ và $$\neg p$$, Disjunctive Syllogism không cho kết luận gì thêm vì cả hai mệnh đề đều sai. Phải dùng Modus Tollens gián tiếp: nếu điều kiện $$p \lor q$$ sai (vì cả $$p$$ và $$q$$ đều sai) thì thân `if` không được thực thi. Kết luận: `document.editable = False`.

</details>

### Bài tập 4: Ứng dụng Bảo mật

Một hệ thống có ba quy tắc kiểm soát truy cập:

> R1: Nếu người dùng có token hợp lệ thì được truy cập.
> R2: Nếu người dùng là admin thì có token hợp lệ.
> R3: Người dùng là admin hoặc người dùng bị chặn.

Biết người dùng không bị chặn. Hãy dùng các quy tắc suy diễn để chứng minh người dùng được truy cập.

<details>
<summary>Đáp án</summary>

Đặt:
- $$p =$$ "người dùng là admin"
- $$q =$$ "người dùng có token hợp lệ"
- $$r =$$ "người dùng được truy cập"
- $$s =$$ "người dùng bị chặn"

Các giả thiết:
1. $$q \to r$$ (R1)
2. $$p \to q$$ (R2)
3. $$p \lor s$$ (R3)
4. $$\neg s$$ (biết)

Suy luận:

- Bước 1: Từ $$p \lor s$$ (3) và $$\neg s$$ (4), Disjunctive Syllogism → $$p$$.
- Bước 2: Từ $$p \to q$$ (2) và $$p$$ (bước 1), Modus Ponens → $$q$$.
- Bước 3: Từ $$q \to r$$ (1) và $$q$$ (bước 2), Modus Ponens → $$r$$.

Kết luận: người dùng được truy cập.

</details>

### Bài tập 5: Chuỗi Suy luận

Dùng các quy tắc suy diễn để chứng minh rằng từ các giả thiết sau đây, ta có thể suy ra $$t$$:

1. $$p \to q$$
2. $$q \to r$$
3. $$r \to s$$
4. $$p$$

<details>
<summary>Đáp án</summary>

- Bước 1: Từ (1) $$p \to q$$ và (4) $$p$$, Modus Ponens → $$q$$.
- Bước 2: Từ (2) $$q \to r$$ và $$q$$ (bước 1), Modus Ponens → $$r$$.
- Bước 3: Từ (3) $$r \to s$$ và $$r$$ (bước 2), Modus Ponens → $$s$$.
- Bước 4: Từ $$s$$, Addition → $$s \lor t$$, nhưng vậy chưa đủ để có $$t$$.

Thực tế, với các giả thiết đã cho, ta chỉ có thể suy ra $$s$$, chứ không thể suy ra $$t$$. Đây là một bài học quan trọng: **không phải mọi thứ đều suy ra được từ giả thiết**. Quy tắc suy diễn chỉ cho ta những kết luận đã được "chứa sẵn" trong giả thiết.

Nếu ta muốn thêm một giả thiết để suy ra $$t$$, có thể thêm $$s \to t$$ (Hypothetical Syllogism nối chuỗi thành $$p \to t$$, rồi Modus Ponens với $$p$$ cho $$t$$) hoặc $$s$$ (rồi Addition: $$s \to s \lor t$$, nhưng vẫn chưa đủ!).

**Đáp án chính xác**: Không thể suy ra $$t$$ từ các giả thiết đã cho. Chỉ suy ra được $$s$$.

</details>

### Bài tập 6: Ứng dụng Modus Ponens trong suy luận hàng ngày

Xác định quy tắc suy diễn được dùng trong mỗi tình huống sau:

(a) "Nếu trời mưa thì đường ướt. Trời mưa. Vậy đường ướt."
(b) "Nếu tôi là sinh viên IUH thì tôi học Toán Rời Rạc. Tôi học Toán Rời Rạc. Vậy tôi là sinh viên IUH." — Suy luận này có hợp lệ không?
(c) "Nếu hệ thống bảo mật phát hiện xâm nhập thì nó sẽ ghi log và gửi cảnh báo. Hệ thống không ghi log. Vậy không có xâm nhập." — Suy luận này có hợp lệ không?
(d) "Nếu $$x$$ chia hết cho 4 thì $$x$$ là số chẵn. $$x$$ là số chẵn. Vậy $$x$$ chia hết cho 4." — Nếu sai, hãy cho phản ví dụ.

<details>
<summary>Đáp án</summary>

(a) **Modus Ponens**: $$p \to q$$ (mưa → ướt), $$p$$ (mưa), suy ra $$q$$ (ướt). Hợp lệ.

(b) **Không hợp lệ** — Đây là sai lầm "khẳng định hệ quả" (affirming the consequent). Ký hiệu: $$p \to q$$ và $$q$$ không suy ra $$p$$. Có thể tôi học Toán Rời Rạc vì tôi là sinh viên ngành CNTT của trường khác.

(c) **Hợp lệ** — Đây là **Modus Tollens**. Đặt $$p$$: "có xâm nhập", $$q$$: "ghi log và gửi cảnh báo". Ta có $$p \to q$$ và $$\neg q$$, suy ra $$\neg p$$. Tuy nhiên cần đảm bảo $$q$$ thực sự là kết quả tất yếu của $$p$$ — nếu hệ thống có thể bị lỗi không ghi log, suy luận này không còn đáng tin cậy.

(d) **Không hợp lệ** — Lại là "khẳng định hệ quả". Phản ví dụ: $$x = 6$$ — 6 là số chẵn nhưng không chia hết cho 4.

</details>

### Bài tập 7: Xây dựng chứng minh bằng suy diễn

Cho các giả thiết:

1. Nếu hôm nay là thứ Bảy thì không có lớp học. ($$s \to \neg c$$)
2. Nếu không có lớp học thì tôi đi bơi. ($$\neg c \to b$$)
3. Hôm nay là thứ Bảy. ($$s$$)

Hãy chứng minh: "Tôi đi bơi."

Viết từng bước suy luận và chỉ rõ quy tắc suy diễn được dùng.

<details>
<summary>Đáp án</summary>

- Bước 1: Từ (1) $$s \to \neg c$$ và (3) $$s$$, Modus Ponens → $$\neg c$$.
- Bước 2: Từ (2) $$\neg c \to b$$ và $$\neg c$$ (bước 1), Modus Ponens → $$b$$.

Kết luận: Tôi đi bơi. Đây là ví dụ của **Hypothetical Syllogism** mở rộng: $$s \to \neg c$$ và $$\neg c \to b$$ cho ta $$s \to b$$, kết hợp với $$s$$ cho $$b$$.

</details>

### Bài tập 8: Phát hiện suy luận sai

Mỗi suy luận sau **có vẻ** hợp lý nhưng thực chất sai. Hãy chỉ ra lỗi:

(a) "Nếu bạn học giỏi thì bạn sẽ kiếm được nhiều tiền. Bạn không học giỏi. Vậy bạn sẽ không kiếm được nhiều tiền."

(b) "Nếu một số chia hết cho 6 thì nó chia hết cho 2 và cho 3. Số 18 chia hết cho 2 và cho 3. Vậy 18 chia hết cho 6." — Suy luận này hợp lệ không?

(c) "Nếu là chó thì sủa. Con vật đó sủa. Vậy nó là chó."

<details>
<summary>Đáp án</summary>

(a) **Sai lầm: Phủ định tiền đề** (Denying the Antecedent).
    Dạng: $$p \to q$$, $$\neg p$$, suy ra $$\neg q$$. Không hợp lệ.
    Phản ví dụ: Bạn có thể không học giỏi nhưng trúng số độc đắc hoặc khởi nghiệp thành công và vẫn kiếm được nhiều tiền.

(b) **Hợp lệ** (bất ngờ!). Đây là trường hợp hiếm hoi mà affirming the consequent lại hợp lệ, vì thực tế "chia hết cho 6" và "chia hết cho 2 và cho 3" là tương đương. Nhưng về mặt logic thuần túy, dạng suy luận vẫn là không hợp lệ — nó hợp lệ ở đây vì nội dung của mệnh đề, không phải vì hình thức.

(c) **Sai lầm: Khẳng định hệ quả** (Affirming the Consequent).
    $$p \to q$$ (chó → sủa), $$q$$ (sủa), suy ra $$p$$ (chó). Sai.
    Phản ví dụ: Con mèo cũng có thể... không, mèo không sủa. Một con chó sói (wolf) sủa nhưng không phải chó nhà. Hoặc một con robot biết sủa.

</details>

### Bài tập 9: Resolution trong chứng minh tự động

Sử dụng quy tắc **Resolution** $$(p \lor q) \land (\neg p \lor r) \implies (q \lor r)$$ để suy ra kết luận từ các cặp clause sau:

(a) $$(a \lor b)$$ và $$(\neg a \lor c)$$
(b) $$(x \lor \neg y)$$ và $$(y \lor z)$$
(c) $$(\neg p \lor q)$$ và $$(\neg q \lor r)$$
(d) $$(p \lor q \lor r)$$ và $$(\neg p \lor s)$$

<details>
<summary>Đáp án</summary>

(a) Resolution: $$(a \lor b)$$ và $$(\neg a \lor c)$$ → $$(b \lor c)$$
    Giải thích: Nếu a đúng thì từ clause 2, c đúng. Nếu a sai thì từ clause 1, b đúng. Vậy ít nhất b hoặc c đúng.

(b) Resolution: $$(x \lor \neg y)$$ và $$(y \lor z)$$ → $$(x \lor z)$$
    Giải thích: Biến đổi $$(x \lor \neg y) \equiv (y \to x)$$ và $$(y \lor z) \equiv (\neg y \to z)$$. Theo tam đoạn luận giả định, $$(y \to x) \land (\neg y \to z)$$ cho ta kết luận gì? Resolution cho $$x \lor z$$.

(c) Resolution: $$(\neg p \lor q)$$ và $$(\neg q \lor r)$$ → $$(\neg p \lor r)$$
    Đây chính là **Hypothetical Syllogism** dưới dạng CNF: $$(\neg p \lor q) \equiv (p \to q)$$, $$(\neg q \lor r) \equiv (q \to r)$$, kết luận $$(\neg p \lor r) \equiv (p \to r)$$.

(d) Resolution: $$(p \lor q \lor r)$$ và $$(\neg p \lor s)$$ → $$(q \lor r \lor s)$$
    p và ¬p là cặp bù. Kết quả là tuyển của các literal còn lại.

</details>

### Qui tắc bổ sung từ slide bài giảng PPT

**Qui tắc phản chứng (Reductio ad absurdum):**
Để chứng minh mệnh đề p là hằng đúng, ta thêm ¬p vào các tiên đề và dẫn đến mâu thuẫn.

Tổng quát: ¬p → (q ∧ ¬q)  ⇒  p

**Ví dụ:** Chứng minh √2 là số vô tỷ.

**Qui tắc chứng minh theo trường hợp:**
[(p → r) ∧ (q → r)] ⇒ (p ∨ q) → r

**Phản ví dụ:**
Để chứng minh suy luận sai, tìm trường hợp tiên đề đúng, kết luận sai.

Ví dụ trong slide: Dùng p=1, q=0, r=1 để phản ví dụ cho một suy luận.

**Qui tắc phản ví dụ (counterexample):**
Chỉ cần một trường hợp làm các giả thiết đúng nhưng kết luận sai để bác bỏ.
