---

layout: post
title: "Quy tắc Suy diễn"
categories: chapter01
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Giới thiệu các quy tắc suy diễn cơ bản trong logic mệnh đề (Modus Ponens, Modus Tollens, tam đoạn luận, phép giải) và ứng dụng trong kiểm chứng."
---

Biết viết công thức logic mới chỉ là có "từ vựng"; biết nối các tiền đề thành một chuỗi lập luận không thể bác bỏ mới là biết "suy nghĩ toán học". Từ bộ kiểm tra kiểu (type checker) của trình biên dịch, hệ chuyên gia suy luận luật, cho đến các bộ chứng minh định lý tự động, mọi cỗ máy suy diễn đều vận hành dựa trên một tập nhỏ các **Quy tắc Suy diễn (Rules of Inference)** chuẩn xác.

## Bản đồ kiến thức nền: Bốn trụ cột của Lý thuyết Suy diễn

1. **Lập luận hợp lệ (Valid Argument) vs. Tiền đề đúng (Soundness)**:
   Một lập luận $(P_1 \land P_2 \land \dots \land P_k) \to Q$ là **hợp lệ (valid)** nếu nó là hằng đúng—nghĩa là *không thể nào* mọi tiền đề đều Đúng mà kết luận lại Sai. Nếu mọi tiền đề còn đúng trong thực tế nữa, lập luận được gọi là **vững chắc (sound)**.

2. **Bộ quy tắc suy diễn kinh điển**:
   - **Modus Ponens**: Từ $p$ và $p \to q$, suy ra $q$.
   - **Modus Tollens**: Từ $\neg q$ và $p \to q$, suy ra $\neg p$.
   - **Tam đoạn luận giả định**: Từ $p \to q$ và $q \to r$, suy ra $p \to r$.
   - **Tam đoạn luận tuyển**: Từ $p \lor q$ và $\neg p$, suy ra $q$.
   - **Phân giải (Resolution)**: Từ $p \lor q$ và $\neg p \lor r$, suy ra $q \lor r$ (nền tảng của Prolog và SAT/CDCL!).

3. **Ngụy biện hình thức (Formal Fallacies)**:
   Hai cái bẫy phổ biến nhất: **Khẳng định hệ quả** (từ $p \to q$ và $q$ suy ra $p$ — SAI!) và **Phủ định tiền đề** (từ $p \to q$ và $\neg p$ suy ra $\neg q$ — SAI!).

4. **Chứng minh từng dòng (Natural Deduction)**:
   Mỗi dòng trong một chuỗi suy diễn đều phải ghi rõ **xuất xứ** (Tiền đề, Luật tương đương, hay Quy tắc suy diễn áp dụng lên những dòng nào trước đó), giúp cả con người lẫn máy tính kiểm chứng cơ học từng bước.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** quy tắc suy diễn là gì và vai trò của nó trong lập luận hình thức.
- **Nhận diện** và **áp dụng** các quy tắc suy diễn cơ bản: Modus Ponens, Modus Tollens, tam đoạn luận giả định, tam đoạn luận tuyển, phép thêm, phép giản lược, phép nối và phép giải.
- **Kiểm tra** tính hợp lệ của một lập luận bằng quy tắc suy diễn.
- **Áp dụng** quy tắc suy diễn vào phân tích mã nguồn, bảo mật và kiểm thử.


**Từ khóa**: rule of inference, Modus Ponens, Modus Tollens, hypothetical syllogism, disjunctive syllogism, addition, simplification, conjunction, resolution, validity.
</div>


---

## Định nghĩa Quy tắc Suy diễn

Trong chứng minh toán học cũng như phân tích hệ thống, ta thường gặp những lập luận có dạng:

> Nếu $$p_1$$ và $$p_2$$ và $$\dots$$ và $$p_n$$ thì $$q$$.

Lập luận này là **hợp lệ** khi biểu thức

<div class="textbook-equation" markdown="1">
$$
(p_1 \land p_2 \land \dots \land p_n) \to q
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
là **hằng đúng** (luôn đúng với mọi tổ hợp giá trị chân lý).

Dạng lập luận hợp lệ như trên gọi là một **quy tắc suy diễn** (rule of inference). Có ba cách biểu diễn phổ biến:

**Cách 1 — Biểu thức hằng đúng:**

<div class="textbook-equation" markdown="1">
$$
(p_1 \land p_2 \land \dots \land p_n) \Rightarrow q
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
(ký hiệu $$\Rightarrow$$ có nghĩa "kéo theo logic", tức $$(p_1 \land \dots \land p_n) \to q$$ là hằng đúng).

**Cách 2 — Dòng suy diễn:**

<div class="textbook-equation" markdown="1">
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
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Cách 3 — Mô hình suy diễn:**

> $$p_1$$
> $$p_2$$
> $$\vdots$$
> $$p_n$$
> 
> ————————————
> 
> $$\therefore q$$

Các biểu thức $$p_1, p_2, \dots, p_n$$ gọi là **giả thiết** (hay **tiền đề**), còn $$q$$ gọi là **kết luận**.

![Bảng tứ đối — quan hệ suy luận cổ điển](/discrete-mathematics-for-computer-science-iuh/img/course/Square_of_opposition__set_diagrams.svg)

<p class="textbook-figure-caption" data-figure="1.21">Quy tắc suy diễn là nền tảng của mọi lập luận hợp lệ — từ tiền đề đúng rút ra kết luận đúng.</p>
---

### Khung giải thích (nên đọc chậm): Dựng chuỗi suy diễn 6 bước tìm nguyên nhân sập máy chủ

Giả sử hệ thống giám sát ghi nhận 4 sự kiện (tiền đề) sau:
- $P_1$: Nếu CPU quá tải ($c$) thì độ trễ tăng cao ($l$): $c \to l$.
- $P_2$: Nếu độ trễ tăng cao ($l$) thì cảnh báo đỏ sẽ bật ($a$): $l \to a$.
- $P_3$: Hoặc CPU quá tải ($c$), hoặc kết nối cơ sở dữ liệu bị ngắt ($d$): $c \lor d$.
- $P_4$: Thực tế cảnh báo đỏ **không** bật ($\neg a$).

**Mục tiêu**: Chứng minh chặt chẽ rằng kết nối cơ sở dữ liệu đã bị ngắt ($d$).

| Bước | Biểu thức suy ra | Căn cứ áp dụng |
| :---: | :--- | :--- |
| 1 | $c \to l$ | Tiền đề $P_1$ |
| 2 | $l \to a$ | Tiền đề $P_2$ |
| 3 | $c \to a$ | **Tam đoạn luận giả định** từ bước (1) và (2) |
| 4 | $\neg a$ | Tiền đề $P_4$ |
| 5 | $\neg c$ | **Modus Tollens** từ bước (3) và (4) |
| 6 | $c \lor d$ | Tiền đề $P_3$ |
| 7 | **$d$** | **Tam đoạn luận tuyển** từ bước (6) và (5) — **ĐPCM!** |

Chuỗi 7 dòng này chính là cách một công cụ chẩn đoán sự cố tự động (hoặc bộ suy diễn logic) đi từ các triệu chứng quan sát được đến đúng nguyên nhân gốc rễ mà không hề đoán mò.

## Modus Ponens (Quy tắc Khẳng định)

Đây là quy tắc suy diễn quen thuộc nhất: nếu mệnh đề kéo theo $$p \to q$$ đúng và $$p$$ đúng, thì $$q$$ cũng phải đúng.

<div class="textbook-equation" markdown="1">
$$
\begin{array}{c}
p \to q \\
p \\
\hline
\therefore q
\end{array}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Dạng biểu thức hằng đúng tương ứng:

<div class="textbook-equation" markdown="1">
$$
[(p \to q) \land p] \Rightarrow q
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ 1 (học tập):**

> Nếu học tốt thì thi đậu.
> Sinh viên A học tốt.
> 
> ——————————————
> 
> $$\therefore$$ Sinh viên A thi đậu.

**Ví dụ 2 (dân gian):**

> Nếu chuồn chuồn bay thấp thì trời mưa.
> Chuồn chuồn bay thấp.
> 
> ————————————————
> 
> $$\therefore$$ Trời mưa.

**Ví dụ 3 (lập trình — kiểm tra đầu vào):**

> Nếu `tuổi < 18` thì từ chối truy cập.
> `tuổi = 16`, vậy `tuổi < 18` đúng.
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

Modus Ponens là cơ chế đằng sau câu lệnh `if-then` trong lập trình: khi điều kiện trong `if` đúng, chương trình thực thi nhánh tương ứng.

![Modus Ponens: p → q và p suy ra q](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-Implication.PNG)

<p class="textbook-figure-caption" data-figure="1.22">Modus Ponens — nếu p → q đúng và p đúng, thì q phải đúng (nền tảng của câu lệnh `if`).</p>
---

## Modus Tollens (Quy tắc Phủ định)

Quy tắc này đi theo chiều ngược lại với Modus Ponens: nếu $$p \to q$$ đúng nhưng $$q$$ sai, thì $$p$$ cũng phải sai.

<div class="textbook-equation" markdown="1">
$$
\begin{array}{c}
p \to q \\
\neg q \\
\hline
\therefore \neg p
\end{array}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Tức là $$[(p \to q) \land \neg q] \Rightarrow \neg p$$ là hằng đúng.

**Ví dụ 1 (bảo mật):**

> Nếu người dùng là admin thì có quyền truy cập bảng `users`.
> Người dùng này **không có** quyền truy cập bảng `users`.
> 
> ————————————————————
> 
> $$\therefore$$ Người dùng này **không phải** admin.

**Ví dụ 2 (kiểm thử):**

> Nếu module không có lỗi thì tất cả test case đều đạt (pass).
> Test case #7 **không đạt (fail)**.
> 
> ——————————————————————————
> 
> $$\therefore$$ Module **có lỗi**.

**Ví dụ 3 (xác thực — token):**

> Nếu token hợp lệ thì máy chủ trả về mã trạng thái 200.
> Máy chủ trả về mã trạng thái 401 (Unauthorized).
> 
> ————————————————————————————
> 
> $$\therefore$$ Token **không hợp lệ**.

Modus Tollens đặc biệt hữu ích trong gỡ lỗi (debugging) và kiểm thử: khi kết quả kỳ vọng không xảy ra, ta suy ra giả định ban đầu đã sai.

![Modus Tollens: p → q và ¬q suy ra ¬p](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-NOT.png)

<p class="textbook-figure-caption" data-figure="1.23">Modus Tollens — nếu p → q đúng nhưng q sai, thì p phải sai (dùng nhiều trong debugging và kiểm thử).</p>
---

## Tam đoạn luận Giả định (Hypothetical Syllogism)

Quy tắc này cho phép nối chuỗi hai mệnh đề kéo theo liên tiếp:

<div class="textbook-equation" markdown="1">
$$
\begin{array}{c}
p \to q \\
q \to r \\
\hline
\therefore p \to r
\end{array}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Tức là $$[(p \to q) \land (q \to r)] \Rightarrow (p \to r)$$.

**Ví dụ 1 (chuỗi xử lý — pipeline):**

> Nếu nhận được yêu cầu (request) thì ghi log vào hệ thống.
> Nếu ghi log thành công thì chuyển yêu cầu đến controller.
> 
> —————————————————————————————
> 
> $$\therefore$$ Nếu nhận được yêu cầu thì chuyển đến controller.

**Ví dụ 2 (phân quyền — kế thừa vai trò):**

> Nếu người dùng là editor thì người dùng là contributor.
> Nếu người dùng là contributor thì có quyền chỉnh sửa bài viết.
> 
> ————————————————————————————
> 
> $$\therefore$$ Nếu người dùng là editor thì có quyền chỉnh sửa bài viết.

Tam đoạn luận giả định là cơ sở cho các chuỗi xử lý (pipeline) và cơ chế kế thừa quyền (role hierarchy) trong hệ thống phần mềm, đồng thời xuất hiện thường xuyên trong các chứng minh toán học nhiều bước.

---

## Tam đoạn luận Tuyển (Disjunctive Syllogism)

Khi biết ít nhất một trong hai mệnh đề là đúng và một trong hai mệnh đề đó sai, ta suy ra mệnh đề còn lại phải đúng:

<div class="textbook-equation" markdown="1">
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
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ 1 (chẩn đoán lỗi):**

> Lỗi xuất phát từ cơ sở dữ liệu hoặc từ mạng.
> Lỗi **không phải** từ cơ sở dữ liệu.
> 
> ————————————————————
> 
> $$\therefore$$ Lỗi xuất phát từ mạng.

**Ví dụ 2 (xét duyệt):**

> Hồ sơ được duyệt hoặc bị từ chối.
> Hồ sơ không bị từ chối.
> 
> ————————————————————
> 
> $$\therefore$$ Hồ sơ được duyệt.

Trong kỹ thuật phần mềm, quy tắc này thường dùng trong xử lý ngoại lệ và chẩn đoán sự cố: mỗi bước loại trừ một nguyên nhân là một lần áp dụng tam đoạn luận tuyển.

![Tam đoạn luận tuyển: p ∨ q và ¬p suy ra q](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-OR.png)

<p class="textbook-figure-caption" data-figure="1.25">Tam đoạn luận tuyển — biết p ∨ q đúng và ¬p đúng, suy ra q (loại trừ nguyên nhân trong chẩn đoán lỗi).</p>
---

## Phép Thêm (Addition)

Từ một mệnh đề đúng, ta có thể ghép thêm bất kỳ mệnh đề nào bằng phép tuyển mà kết quả vẫn đúng:

<div class="textbook-equation" markdown="1">
$$
\begin{array}{c}
p \\
\hline
\therefore p \lor q
\end{array}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Quy tắc này hữu ích trong các chứng minh phức tạp khi cần mở rộng giả thiết sang dạng tuyển.

**Ví dụ:**

> Hệ thống đang hoạt động.
> 
> ————————————
> 
> $$\therefore$$ Hệ thống đang hoạt động hoặc đang bảo trì.

---

## Phép Giản lược (Simplification)

Ngược lại với phép thêm: từ một mệnh đề hội đúng, ta suy ra mỗi thành phần của nó đều đúng:

<div class="textbook-equation" markdown="1">
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
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ (kiểm tra điều kiện phức hợp):**

> Tài khoản hợp lệ **và** mật khẩu đúng.
> 
> ————————————————————
> 
> $$\therefore$$ Tài khoản hợp lệ.

Khi một hàm trả về cặp `(status, data)` và ta chỉ trích xuất `status`, thao tác đó tương tự như phép giản lược.

---

## Phép Nối (Conjunction)

Nếu hai mệnh đề đều đúng riêng lẻ, ta có thể ghép chúng thành một mệnh đề hội:

<div class="textbook-equation" markdown="1">
$$
\begin{array}{c}
p \\
q \\
\hline
\therefore p \land q
\end{array}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ (kiểm tra bảo mật):**

> Người dùng đã xác thực.
> Người dùng có quyền admin.
> 
> ——————————————————
> 
> $$\therefore$$ Người dùng đã xác thực và có quyền admin.

Phép nối thường được dùng ở cuối chuỗi suy luận để gộp các kết luận riêng lẻ thành một kết luận tổng hợp.

---

## Phép Giải (Resolution)

Quy tắc này giữ vai trò trung tâm trong chứng minh định lý tự động (automated theorem proving) và bộ giải SAT:

<div class="textbook-equation" markdown="1">
$$
\begin{array}{c}
p \lor q \\
\neg p \lor r \\
\hline
\therefore q \lor r
\end{array}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Giải thích: nếu $$p$$ sai thì từ $$p \lor q$$ suy ra $$q$$ đúng; nếu $$p$$ đúng thì từ $$\neg p \lor r$$ suy ra $$r$$ đúng. Trong mọi trường hợp, $$q \lor r$$ đều đúng.

**Ví dụ (trí tuệ nhân tạo — suy luận trong hệ chuyên gia):**

> Dữ liệu bị hỏng ($$p$$) hoặc lỗi mạng ($$q$$).
> Dữ liệu không bị hỏng ($$\neg p$$) hoặc lỗi phần mềm ($$r$$).
> 
> ———————————————————————————————
> 
> $$\therefore$$ Lỗi mạng ($$q$$) hoặc lỗi phần mềm ($$r$$).

Phép giải (resolution) là nền tảng của **phương pháp chứng minh bác bỏ** (refutation proof) trong các bộ giải SAT. Khi kết hợp phép giải với dạng chuẩn tắc hội (Conjunctive Normal Form — CNF), máy tính có thể kiểm tra tính thỏa mãn của công thức với số lượng biến rất lớn.

---

### Thử nghiệm: kiểm tra một suy diễn bằng bảng chân trị

Chọn quy tắc mẫu hoặc tự nhập tiền đề và kết luận; bảng chân trị sẽ chỉ ra dòng phản ví dụ nếu suy diễn không hợp lệ (ví dụ hai ngụy biện phổ biến).

<div class="interactive-demo" markdown="1">
<div data-demo="inference-explainer" data-preset="mp"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Bảng Tổng Hợp các Quy tắc Suy diễn

| Tên quy tắc | Dạng suy diễn | Tên tiếng Việt |
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

## Ứng dụng trong Khoa học Máy tính

### Kiểm chứng Hình thức (Formal Verification)

Các công cụ như Dafny, Coq và Isabelle/HOL dùng các quy tắc suy diễn để chứng minh tính đúng đắn của chương trình; mỗi bước chứng minh đều được máy tính kiểm tra tự động.

### SAT Solvers

Bộ giải SAT chuyển bài toán về dạng CNF và áp dụng phép giải (cùng các kỹ thuật tìm kiếm) để kiểm tra tính thỏa mãn của công thức ở quy mô vượt quá khả năng tính thủ công.

### Hệ Thống Chuyên gia (Expert Systems)

Các hệ thống như MYCIN (hỗ trợ chẩn đoán bệnh) sử dụng tập luật suy diễn có dạng:

> NẾU (triệu chứng A VÀ triệu chứng B) THÌ (bệnh C) với độ tin cậy 80%.

Mỗi khi người dùng cung cấp thêm triệu chứng, hệ thống áp dụng Modus Ponens để rút ra kết luận mới.

### Hệ thống Kiểu (Type Systems)

Trong trình biên dịch, quá trình suy luận kiểu (type inference) dựa trên các quy tắc suy diễn. Ví dụ:

> Nếu $$e_1 : \text{Int}$$ và $$e_2 : \text{Int}$$ thì $$e_1 + e_2 : \text{Int}$$.

Trình biên dịch dùng Modus Ponens để suy ra kiểu của biểu thức phức hợp từ kiểu của các biểu thức con.

---

## Bài tập

### Bài tập 1: Nhận diện Quy tắc Suy diễn

Xác định quy tắc suy diễn được dùng trong mỗi lập luận sau:

(a) Nếu hôm nay là thứ Bảy thì không có lớp học. Hôm nay là thứ Bảy. Vậy không có lớp học.

(b) Nếu trời mưa thì tôi mang ô. Tôi không mang ô. Vậy trời không mưa.

(c) Nếu $$x = 2$$ thì $$x^2 = 4$$. Nếu $$x^2 = 4$$ thì $$\sqrt{x^2} = 2$$. Vậy nếu $$x = 2$$ thì $$\sqrt{x^2} = 2$$.

(d) Hệ thống bị tấn công từ bên ngoài hoặc từ nội bộ. Hệ thống không bị tấn công từ nội bộ. Vậy hệ thống bị tấn công từ bên ngoài.

<details>
<summary>Đáp án</summary>

(a) **Modus Ponens**: $$p \to q$$ (nếu thứ Bảy thì không có lớp), $$p$$ (thứ Bảy), suy ra $$q$$ (không có lớp).

(b) **Modus Tollens**: $$p \to q$$ (nếu mưa thì mang ô), $$\neg q$$ (không mang ô), suy ra $$\neg p$$ (không mưa).

(c) **Hypothetical Syllogism**: $$p \to q$$ và $$q \to r$$, suy ra $$p \to r$$.

(d) **Disjunctive Syllogism**: $$p \lor q$$ (bên ngoài hoặc nội bộ) và $$\neg q$$ (không từ nội bộ), suy ra $$p$$ (từ bên ngoài).

</details>

### Bài tập 2: Kiểm tra Tính Hợp lệ

Mỗi suy luận sau có hợp lệ không? Nếu không, hãy chỉ ra lỗi ngụy biện và nêu phản ví dụ.

(a) Nếu một số chia hết cho 2 thì nó là số chẵn. Số đó là số chẵn. Vậy nó chia hết cho 2.

(b) Nếu file tồn tại thì đọc được. File không tồn tại. Vậy không đọc được.

(c) Nếu kết nối bị timeout thì máy chủ quá tải hoặc mạng chậm. Kết nối bị timeout. Vậy máy chủ quá tải.

<details>
<summary>Đáp án</summary>

(a) **Không hợp lệ về mặt hình thức** — Ngụy biện khẳng định hệ quả (affirming the consequent): từ $$p \to q$$ và $$q$$ không thể suy ra $$p$$. Ở đây kết luận tình cờ đúng về mặt số học vì "chia hết cho 2" và "là số chẵn" tương đương nhau, nhưng dạng lập luận là sai. Phản ví dụ cho dạng lập luận này: "Nếu là chó thì có 4 chân. Con vật này có 4 chân. Vậy nó là chó" (sai vì mèo cũng có 4 chân).

(b) **Không hợp lệ** — Ngụy biện phủ định tiền đề (denying the antecedent): từ $$p \to q$$ và $$\neg p$$ không thể suy ra $$\neg q$$. Phản ví dụ cần làm hai tiền đề đúng ($$p$$ sai, nên $$p \to q$$ và $$\neg p$$ đều đúng) nhưng kết luận sai ($$q$$ đúng): chẳng hạn file không còn tồn tại trên đĩa ($$p$$ sai) nhưng nội dung vẫn đọc được từ bộ nhớ đệm/cache ($$q$$ đúng). Phản ví dụ tổng quát hơn: "Nếu trời mưa thì đường ướt. Trời không mưa. Vậy đường không ướt" (sai vì đường có thể ướt do xe tưới nước).

(c) **Không hợp lệ** — Từ $$p \to (r \lor s)$$ và $$p$$, Modus Ponens chỉ cho phép suy ra $$r \lor s$$ (máy chủ quá tải hoặc mạng chậm), không thể kết luận riêng $$r$$ (máy chủ quá tải) vì có thể chỉ có $$s$$ đúng (mạng chậm trong khi máy chủ bình thường).

</details>

### Bài tập 3: Suy luận trong Lập trình

Cho đoạn chương trình Python sau:

```python
if user.is_admin() or user.has_permission("edit"):
    document.editable = True
else:
    document.editable = False
```

Biết rằng `user.is_admin()` trả về `False`. Hãy dùng quy tắc suy diễn để suy ra giá trị của `document.editable` trong hai trường hợp:

(a) `user.has_permission("edit")` trả về `True`.
(b) `user.has_permission("edit")` trả về `False`.

<details>
<summary>Đáp án</summary>

Đặt $$p$$: `user.is_admin()` đúng, $$q$$: `user.has_permission("edit")` đúng. Điều kiện của `if` là $$p \lor q$$. Ta biết $$\neg p$$ đúng.

(a) Nếu $$q$$ đúng: từ $$q$$, áp dụng **Addition** (phép thêm) ta có $$p \lor q$$ đúng. Áp dụng **Modus Ponens** với nhánh `if`, suy ra `document.editable = True`.

(b) Nếu $$q$$ sai (tức $$\neg q$$ đúng): từ $$\neg p$$ và $$\neg q$$, áp dụng **Conjunction** (phép nối) ta có $$\neg p \land \neg q$$, theo luật De Morgan tương đương với $$\neg(p \lor q)$$. Điều kiện `if` sai nên nhánh `else` được thực thi, suy ra `document.editable = False`.

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
- $$p$$: "người dùng là admin"
- $$q$$: "người dùng có token hợp lệ"
- $$r$$: "người dùng được truy cập"
- $$s$$: "người dùng bị chặn"

Các giả thiết:
1. $$q \to r$$ (R1)
2. $$p \to q$$ (R2)
3. $$p \lor s$$ (R3)
4. $$\neg s$$ (dữ kiện cho trước)

Các bước suy luận:

- Bước 1: Từ $$p \lor s$$ (3) và $$\neg s$$ (4), theo **Disjunctive Syllogism** → $$p$$.
- Bước 2: Từ $$p \to q$$ (2) và $$p$$ (bước 1), theo **Modus Ponens** → $$q$$.
- Bước 3: Từ $$q \to r$$ (1) và $$q$$ (bước 2), theo **Modus Ponens** → $$r$$.

Kết luận: Người dùng được truy cập.

</details>

### Bài tập 5: Chuỗi Suy luận

Kiểm tra xem từ các giả thiết sau đây có thể dùng các quy tắc suy diễn để suy ra $$t$$ hay không:

1. $$p \to q$$
2. $$q \to r$$
3. $$r \to s$$
4. $$p$$

<details>
<summary>Đáp án</summary>

- Bước 1: Từ (1) $$p \to q$$ và (4) $$p$$, theo **Modus Ponens** → $$q$$.
- Bước 2: Từ (2) $$q \to r$$ và $$q$$ (bước 1), theo **Modus Ponens** → $$r$$.
- Bước 3: Từ (3) $$r \to s$$ và $$r$$ (bước 2), theo **Modus Ponens** → $$s$$.

Từ các giả thiết đã cho, ta chỉ suy ra được $$s$$ chứ **không thể suy ra $$t$$** (vì không có giả thiết nào liên hệ $$t$$ với $$p, q, r, s$$; phép Addition chỉ cho $$s \lor t$$). Nếu muốn suy ra $$t$$, cần bổ sung thêm giả thiết chẳng hạn $$s \to t$$.

</details>

### Bài tập 6: Ứng dụng Modus Ponens trong suy luận hàng ngày

Xác định quy tắc suy diễn (hoặc lỗi ngụy biện) trong mỗi tình huống sau:

(a) "Nếu trời mưa thì đường ướt. Trời mưa. Vậy đường ướt."
(b) "Nếu tôi là sinh viên thì tôi học Toán Rời Rạc. Tôi học Toán Rời Rạc. Vậy tôi là sinh viên." — Suy luận này có hợp lệ không?
(c) "Nếu hệ thống bảo mật phát hiện xâm nhập thì nó sẽ ghi log và gửi cảnh báo. Hệ thống không ghi log. Vậy không có xâm nhập." — Suy luận này có hợp lệ không?
(d) "Nếu $$x$$ chia hết cho 4 thì $$x$$ là số chẵn. $$x$$ là số chẵn. Vậy $$x$$ chia hết cho 4." — Nếu sai, hãy nêu phản ví dụ.

<details>
<summary>Đáp án</summary>

(a) **Modus Ponens**: $$p \to q$$ (mưa → ướt) và $$p$$ (mưa), suy ra $$q$$ (ướt). Lập luận hợp lệ.

(b) **Không hợp lệ** — Ngụy biện khẳng định hệ quả (affirming the consequent): $$p \to q$$ và $$q$$ không suy ra $$p$$. Một người không phải sinh viên vẫn có thể tự học Toán Rời Rạc.

(c) **Hợp lệ** — Đặt $$p$$: "phát hiện xâm nhập", $$q$$: "ghi log", $$r$$: "gửi cảnh báo". Ta có $$p \to (q \land r)$$ và $$\neg q$$. Từ $$\neg q$$, theo Addition có $$\neg q \lor \neg r$$, theo De Morgan là $$\neg(q \land r)$$, rồi áp dụng **Modus Tollens** suy ra $$\neg p$$ (không phát hiện xâm nhập). Lưu ý trong thực tế, kết luận chỉ đáng tin khi tiền đề $$p \to (q \land r)$$ thực sự đúng (hệ thống ghi log không bị lỗi).

(d) **Không hợp lệ** — Ngụy biện khẳng định hệ quả. Phản ví dụ: $$x = 6$$ là số chẵn nhưng không chia hết cho 4.

</details>

### Bài tập 7: Xây dựng chứng minh bằng suy diễn

Cho các giả thiết:

1. Nếu hôm nay là thứ Bảy thì không có lớp học ($$s \to \neg c$$).
2. Nếu không có lớp học thì tôi đi bơi ($$\neg c \to b$$).
3. Hôm nay là thứ Bảy ($$s$$).

Hãy chứng minh: "Tôi đi bơi." Viết rõ từng bước và nêu tên quy tắc suy diễn được dùng.

<details>
<summary>Đáp án</summary>

- Bước 1: Từ (1) $$s \to \neg c$$ và (3) $$s$$, theo **Modus Ponens** → $$\neg c$$.
- Bước 2: Từ (2) $$\neg c \to b$$ và $$\neg c$$ (bước 1), theo **Modus Ponens** → $$b$$.

Kết luận: Tôi đi bơi. (Cũng có thể dùng **Hypothetical Syllogism** cho (1) và (2) để thu được $$s \to b$$, sau đó dùng Modus Ponens với (3) để suy ra $$b$$.)

</details>

### Bài tập 8: Phát hiện suy luận sai

Mỗi suy luận sau trông có vẻ hợp lý nhưng mắc lỗi logic. Hãy chỉ ra lỗi trong từng câu:

(a) "Nếu bạn học giỏi thì bạn sẽ kiếm được nhiều tiền. Bạn không học giỏi. Vậy bạn sẽ không kiếm được nhiều tiền."

(b) "Nếu một số chia hết cho 6 thì nó chia hết cho 2 và cho 3. Số 18 chia hết cho 2 và cho 3. Vậy 18 chia hết cho 6." — Suy luận này có hợp lệ về mặt hình thức không?

(c) "Nếu là chó thì biết sủa. Con vật đó biết sủa. Vậy nó là chó."

<details>
<summary>Đáp án</summary>

(a) **Ngụy biện phủ định tiền đề** (Denying the Antecedent): dạng $$p \to q$$, $$\neg p$$, suy ra $$\neg q$$ là không hợp lệ. Phản ví dụ: một người không học giỏi vẫn có thể kiếm được nhiều tiền nhờ kinh doanh hoặc trúng thưởng.

(b) **Không hợp lệ về mặt hình thức** — Đây là dạng ngụy biện khẳng định hệ quả ($$p \to q$$ và $$q$$ không suy ra $$p$$). Kết luận ở đây đúng về mặt số học chỉ vì theo nội dung toán học, "chia hết cho 6" tương đương với "chia hết cho 2 và cho 3", chứ không phải do hình thức suy luận hợp lệ.

(c) **Ngụy biện khẳng định hệ quả** (Affirming the Consequent): $$p \to q$$ (chó → sủa) và $$q$$ (sủa) không suy ra $$p$$ (chó). Phản ví dụ: chó sói (wolf) hoặc một con robot được lập trình phát tiếng sủa.

</details>

### Bài tập 9: Resolution trong chứng minh tự động

Sử dụng quy tắc **Resolution** $$(p \lor q) \land (\neg p \lor r) \Rightarrow (q \lor r)$$ để suy ra kết luận từ các cặp mệnh đề con sau:

(a) $$(a \lor b)$$ và $$(\neg a \lor c)$$
(b) $$(x \lor \neg y)$$ và $$(y \lor z)$$
(c) $$(\neg p \lor q)$$ và $$(\neg q \lor r)$$
(d) $$(p \lor q \lor r)$$ và $$(\neg p \lor s)$$

<details>
<summary>Đáp án</summary>

(a) Từ $$(a \lor b)$$ và $$(\neg a \lor c)$$ suy ra $$(b \lor c)$$. Nếu $$a$$ đúng thì từ mệnh đề 2 có $$c$$ đúng; nếu $$a$$ sai thì từ mệnh đề 1 có $$b$$ đúng.

(b) Từ $$(x \lor \neg y)$$ và $$(y \lor z)$$ suy ra $$(x \lor z)$$ (khử cặp bù $$\neg y$$ và $$y$$).

(c) Từ $$(\neg p \lor q)$$ và $$(\neg q \lor r)$$ suy ra $$(\neg p \lor r)$$. Đây chính là **Hypothetical Syllogism** viết dưới dạng CNF vì $$(\neg p \lor q) \equiv (p \to q)$$, $$(\neg q \lor r) \equiv (q \to r)$$ và $$(\neg p \lor r) \equiv (p \to r)$$.

(d) Từ $$(p \lor q \lor r)$$ và $$(\neg p \lor s)$$ suy ra $$(q \lor r \lor s)$$: khử cặp bù $$p$$ và $$\neg p$$, giữ lại tuyển của các literal còn lại.

</details>

### Quy tắc bổ sung từ slide bài giảng PPT

- **Quy tắc phản chứng (Reductio ad absurdum):** Để chứng minh mệnh đề $$p$$ là đúng, ta giả sử $$\neg p$$ rồi suy ra một mâu thuẫn:
  $$\neg p \to (q \land \neg q) \Rightarrow p$$.
  Ví dụ kinh điển: chứng minh $$\sqrt{2}$$ là số vô tỷ.

- **Quy tắc chứng minh theo trường hợp:**
  $$[(p \to r) \land (q \to r)] \Rightarrow ((p \lor q) \to r)$$.

- **Quy tắc phản ví dụ (counterexample):** Để bác bỏ một suy luận, chỉ cần chỉ ra một tổ hợp giá trị làm tất cả các giả thiết đều đúng nhưng kết luận lại sai (chẳng hạn dùng $$p = 1, q = 0, r = 1$$ để kiểm tra một suy luận mẫu trong slide).

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Quy tắc suy diễn** là dạng lập luận trong đó $$(p_1 \land \cdots \land p_n) \to q$$ là hằng đúng; có thể biểu diễn dưới dạng biểu thức, dòng suy diễn hoặc mô hình suy diễn.
- Các quy tắc cơ bản gồm: **Modus Ponens**, **Modus Tollens**, **tam đoạn luận giả định**, **tam đoạn luận tuyển**, **phép thêm**, **phép giản lược**, **phép nối** và **phép giải** (resolution).
- Modus Ponens gắn liền với cấu trúc `if-then`, còn Modus Tollens hữu ích trong gỡ lỗi và kiểm thử.
- Resolution là nền tảng của chứng minh bác bỏ (refutation) và bộ giải SAT.
- Các quy tắc suy diễn được ứng dụng trong kiểm chứng hình thức, hệ chuyên gia, hệ thống kiểu và phân tích bảo mật.

Trong bài tiếp theo (tùy chọn), chúng ta sẽ tìm hiểu **SAT solver** — công cụ tự động kiểm tra tính thỏa mãn của công thức Boolean ở dạng CNF.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=8DW0K3mnc-0">RULES of INFERENCE - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Tổng quan các quy tắc suy diễn thường dùng trong chứng minh mệnh đề.
- <a href="https://www.youtube.com/watch?v=NTSZMdGlo4g">Logical Arguments - Modus Ponens &amp; Modus Tollens</a> — Dr. Trefor Bazett, tiếng Anh. Giải thích chi tiết Modus Ponens và Modus Tollens — hai quy tắc được dùng nhiều nhất trong bài.
- <a href="https://www.youtube.com/watch?v=pHWaxuyfK2s">Logical Argument Forms: Generalizations, Specialization, Contradiction</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày khái quát hóa, đặc biệt hóa và chứng minh phản chứng trong lập luận.
