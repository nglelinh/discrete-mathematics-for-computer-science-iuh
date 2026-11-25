---

layout: post
title: "Bảng Chân Trị và Ứng dụng"
categories: chapter01
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Giới thiệu bảng chân trị (truth table) — công cụ liệt kê mọi tổ hợp giá trị chân lý của biến, phân loại mệnh đề và thiết kế test case kiểm thử."
---

Làm sao chứng minh tuyệt đối rằng hai đoạn mã `if` phức tạp cho ra kết quả giống hệt nhau trên mọi đầu vào, hoặc một công thức logic luôn đúng trong mọi vũ trụ khả dĩ? Khi số biến còn nhỏ, **Bảng chân trị (Truth Table)** là kính hiển vi vét cạn: nó liệt kê toàn bộ $2^n$ tổ hợp chân trị của $n$ biến mệnh đề, không bỏ sót bất kỳ trường hợp biên nào.

## Bản đồ kiến thức nền: Bốn ý niệm cốt lõi xung quanh Bảng chân trị

1. **Quy mô tổ hợp $2^n$ và Bùng nổ hàm mũ**:
   Với $n$ biến mệnh đề, bảng chân trị có đúng $2^n$ dòng ($n=2 \Rightarrow 4$, $n=3 \Rightarrow 8$, $n=10 \Rightarrow 1.024$, $n=64 \Rightarrow 1{,}8 \times 10^{19}$). Đây chính là lý do bảng chân trị hoàn hảo cho kiểm chứng tay với $n \le 4$, nhưng ở quy mô hàng nghìn biến ta phải chuyển sang biến đổi tương đương và SAT Solver.

2. **Ba phân loại ngữ nghĩa của công thức**:
   - **Hằng đúng (Tautology)**: Cột kết quả gồm 100% giá trị `T` (ví dụ $p \lor \neg p$).
   - **Hằng sai / Mâu thuẫn (Contradiction)**: Cột kết quả gồm 100% giá trị `F` (ví dụ $p \land \neg p$).
   - **Tiếp liên (Contingency)**: Có ít nhất một dòng `T` và ít nhất một dòng `F`.

3. **Kiểm chứng tương đương logic bằng so sánh cột**:
   Hai công thức $A$ và $B$ tương đương logic ($A \equiv B$) khi và chỉ khi cột chân trị của chúng trùng khớp từng dòng một trên cả $2^n$ tổ hợp (tương đương $A \leftrightarrow B$ là hằng đúng).

4. **Liên hệ với Bảng kiểm thử biên (Decision Table Testing)**:
   Trong kiểm thử phần mềm (QA), mỗi dòng của bảng chân trị ứng với một ca kiểm thử (*test case*) giúp phát hiện lỗi thiếu nhánh `else` hoặc điều kiện phủ chồng lên nhau.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** bảng chân trị cho biểu thức có 2, 3 hoặc nhiều biến.
- **Tính** giá trị của biểu thức phức hợp từng bước.
- **Phân loại** biểu thức thành hằng đúng, hằng sai hoặc mệnh đề thường.
- **Ứng dụng** bảng chân trị để thiết kế test case bao phủ đủ các trường hợp.


**Từ khóa**: Bảng chân trị (truth table), tautology, contradiction, contingency, test case, exhaustive checking.
</div>


## Bảng chân trị là gì?

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Bảng chân trị là bảng liệt kê tất cả các tổ hợp giá trị chân lý có thể có của các mệnh đề thành phần cùng giá trị chân lý tương ứng của mệnh đề phức hợp.
</div>


![Không gian quyết định 2ⁿ tổ hợp](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="1.13">Với n biến, bảng chân trị có 2ⁿ dòng — liệt kê mọi tổ hợp giá trị chân lý một cách có hệ thống.</p>
## Cách xây dựng bảng chân trị

### Bước 1: Xác định số biến
Với $$n$$ biến, bảng chân trị có đúng **$$2^n$$ dòng**.

**Quy tắc nhanh**:
- 2 biến → 4 dòng.
- 3 biến → 8 dòng.
- 4 biến → 16 dòng.

### Bước 2: Liệt kê tất cả tổ hợp (không bỏ sót)

**Quy tắc liệt kê**: Các hàng có thể được sinh bằng cách đếm nhị phân từ $$0$$ đến $$2^n - 1$$.

Với 3 biến $$p, q, r$$:

| p | q | r | Ghi chú |
|:---:|:---:|:---:|:---|
| T | T | T | 111 |
| T | T | F | 110 |
| T | F | T | 101 |
| T | F | F | 100 |
| F | T | T | 011 |
| F | T | F | 010 |
| F | F | T | 001 |
| F | F | F | 000 |

**Quy tắc luân phiên**:
- Biến đầu tiên: đổi giá trị sau mỗi $$2^{n-1}$$ dòng.
- Biến thứ hai: đổi giá trị sau mỗi $$2^{n-2}$$ dòng.
- Biến cuối cùng: đổi giá trị ở mỗi dòng (T, F, T, F, ...).

### Bước 3: Tính toán từng bước (từ trong ra ngoài)

**Nguyên tắc**: Luôn tính các biểu thức con trước, sau đó mới tính biểu thức chính theo thứ tự từ trong ra ngoài.

**Ví dụ minh họa**:

```python
# Biểu thức: (p ∧ q) → r
# Ta tính theo thứ tự:

1. Tính p ∧ q trước
2. Sau đó mới tính (kết quả) → r
```

Khi lập bảng, nên thêm cột phụ cho từng biểu thức con để theo dõi rõ từng bước tính toán.

### Khung giải thích (nên đọc chậm): Tính tay bảng chân trị và chứng minh luật phản đảo $(p \to q) \equiv (\neg q \to \neg p)$

Thay vì thuộc lòng rằng *"Nếu trời mưa thì đường ướt"* tương đương với *"Nếu đường không ướt thì trời không mưa"*, hãy kiểm chứng từng ô bằng tay với $n = 2$ biến ($2^2 = 4$ dòng):

| Dòng | $p$ | $q$ | $\neg p$ | $\neg q$ | $A = (p \to q)$ | $B = (\neg q \to \neg p)$ | $A \leftrightarrow B$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `T` | `T` | `F` | `F` | `T` | `T` | **`T`** |
| 2 | `T` | `F` | `F` | `T` | `F` | `F` | **`T`** |
| 3 | `F` | `T` | `T` | `F` | `T` | `T` | **`T`** |
| 4 | `F` | `F` | `T` | `T` | `T` | `T` | **`T`** |

- So sánh cột $A$ (`T, F, T, T`) và cột $B$ (`T, F, T, T`): khớp nhau 100% trên cả 4 dòng!
- Cột $A \leftrightarrow B$ toàn bộ là `T` → là **Hằng đúng (Tautology)**, xác nhận $(p \to q) \equiv (\neg q \to \neg p)$.
- **Mẹo kiểm tra nhanh**: Lưu ý nếu viết nhầm thành mệnh đề đảo $q \to p$, cột kết quả là `T, T, F, T` (lệch ở dòng 2 và 3), chứng minh ngay bằng phản ví dụ rằng $p \to q \not\equiv q \to p$.

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

**Phân tích**: Chỉ có hàng thứ hai ($$p = T, q = T, r = F$$) làm biểu thức sai. Điều này có nghĩa là khi cả $$p$$ và $$q$$ đều đúng mà $$r$$ lại sai, khẳng định "nếu $$p$$ và $$q$$ thì $$r$$" bị vi phạm.

## Ví dụ 2: Bảng chân trị cho ¬(p ∨ q) ↔ (¬p ∧ ¬q)

| p | q | p ∨ q | ¬(p ∨ q) | ¬p | ¬q | ¬p ∧ ¬q | ¬(p ∨ q) ↔ (¬p ∧ ¬q) |
|---|---|-------|----------|----|----|---------|----------------------|
| T | T |   T   |    F     | F  | F  |    F    |          T           |
| T | F |   T   |    F     | F  | T  |    F    |          T           |
| F | T |   T   |    F     | T  | F  |    F    |          T           |
| F | F |   F   |    T     | T  | T  |    T    |          T           |

**Kết luận**: Cột cuối toàn giá trị T, nên biểu thức này luôn đúng (tautology). Đây chính là luật De Morgan và sẽ được trình bày kỹ hơn ở Mục 1.4.

<p class="textbook-figure-caption" data-figure="1.14">Định luật De Morgan — phần bù của hợp/giao tương ứng với giao/hợp của các phần bù.</p>
## Các khái niệm quan trọng

### Tautology (Hằng đúng)
Mệnh đề luôn nhận giá trị T trong mọi trường hợp.

<div class="textbook-example" markdown="1">
**Ví dụ**: $$p \lor \neg p$$

| p | ¬p | p ∨ ¬p |
|---|---|----|
| T | F  | T  |
| F | T  | T  |
</div>


### Contradiction (Hằng sai)
Mệnh đề luôn nhận giá trị F trong mọi trường hợp.

<div class="textbook-example" markdown="1">
**Ví dụ**: $$p \land \neg p$$

| p | ¬p | p ∧ ¬p |
|---|---|----|
| T | F  | F  |
| F | T  | F  |
</div>


### Contingency (Mệnh đề thường)
Mệnh đề có thể đúng hoặc sai tùy thuộc vào giá trị của các biến.

## Những nhầm lẫn thường gặp

- **Nhầm lẫn 1 — Quên số dòng**: Với $$n$$ biến, bảng có $$2^n$$ dòng, không phải $$2n$$. Lỗi thường gặp là chỉ liệt kê $$n + 1$$ dòng nên bỏ sót tổ hợp.
- **Nhầm lẫn 2 — Tính sai phép kéo theo**: Phép kéo theo (`→`) **chỉ sai khi $$p = T$$ và $$q = F$$**; mọi trường hợp khác đều đúng. Đây là lỗi phổ biến nhất khi lập bảng.
- **Nhầm lẫn 3 — Nhầm thứ tự ưu tiên**: `¬` có độ ưu tiên cao hơn `∧`, `∧` cao hơn `∨`, `∨` cao hơn `→`, và `→` cao hơn `↔`. Khi chưa chắc chắn, nên dùng dấu ngoặc.

## Ứng dụng của bảng chân trị

### Kiểm tra tính hợp lệ của lập luận
Một lập luận là hợp lệ nếu kết luận luôn đúng mỗi khi tất cả các tiền đề đều đúng.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- Tiền đề 1: $$p \to q$$
- Tiền đề 2: $$p$$
- Kết luận: $$q$$

| p | q | p → q | p ∧ (p → q) | [p ∧ (p → q)] → q |
|---|---|-------|-------------|-------------------|
| T | T |   T   |      T      |         T         |
| T | F |   F   |      F      |         T         |
| F | T |   T   |      F      |         T         |
| F | F |   T   |      F      |         T         |

**Kết luận**: Lập luận hợp lệ vì cột cuối toàn T.
</div>


## Bài tập thực hành

### Bài tập 1: Xây dựng bảng chân trị
Xây dựng bảng chân trị cho các biểu thức sau:
1. $$(p \to q) \land (q \to r) \to (p \to r)$$
2. $$(p \lor q) \land \neg(p \land q)$$
3. $$(p \leftrightarrow q) \leftrightarrow ((p \to q) \land (q \to p))$$

### Bài tập 2: Phân loại mệnh đề
Xác định các mệnh đề sau là hằng đúng (tautology), hằng sai (contradiction) hay mệnh đề thường (contingency):
1. $$p \to (q \to p)$$
2. $$(p \land q) \land \neg(p \lor q)$$
3. $$(p \to q) \to ((\neg q) \to (\neg p))$$

<details>
<summary>Gợi ý Bài tập 2</summary>

1. **Tautology** — Luôn đúng.
2. **Contradiction** — Luôn sai.
3. **Tautology** — Đây là quy tắc phản đảo (contrapositive).

</details>

### Bài tập 3: Ứng dụng thực tế
Một hệ thống báo động có 3 cảm biến A, B, C. Báo động kích hoạt khi:
- Cả A và B đều kích hoạt, HOẶC
- C kích hoạt và ít nhất một trong hai cảm biến A hoặc B kích hoạt.

Viết biểu thức logic và lập bảng chân trị cho hệ thống này.

### Bài tập 4: Bảng chân trị cho kiểm thử phần mềm

Một hệ thống cho phép sinh viên xem điểm nếu:

- $$p$$: Sinh viên đã đăng nhập.
- $$q$$: Sinh viên thuộc lớp học phần.
- $$r$$: Giảng viên đã công bố điểm.

Điều kiện: $$p \land q \land r$$.

1. Lập bảng chân trị đầy đủ.
2. Từ bảng đó, chọn ít nhất 4 test case quan trọng.
3. Giải thích vì sao test case "đã đăng nhập nhưng không thuộc lớp" cần được kiểm thử.

### Bài tập 5: Bảng chân trị 3 biến

Xây dựng bảng chân trị đầy đủ cho các biểu thức sau:

(a) $$(p \lor q) \land (q \lor r) \land (r \lor p)$$
(b) $$(p \to q) \lor (q \to r)$$
(c) $$p \oplus q \oplus r$$ (XOR ba ngôi — đúng khi số biến đúng là số lẻ)
(d) $$(p \land q) \lor (q \land r) \lor (r \land p)$$

<details>
<summary>Đáp án</summary>

Bảng chân trị 3 biến (8 dòng):

| p | q | r | (a) (p∨q)∧(q∨r)∧(r∨p) | (b) (p→q)∨(q→r) | (c) p⊕q⊕r | (d) (p∧q)∨(q∧r)∨(r∧p) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| F | F | F | F | T | F | F |
| F | F | T | F | T | T | F |
| F | T | F | F | T | T | F |
| F | T | T | T | T | F | T |
| T | F | F | F | T | T | F |
| T | F | T | T | T | F | T |
| T | T | F | T | T | F | T |
| T | T | T | T | T | T | T |

Nhận xét:
- (a) chỉ đúng khi có ít nhất 2 trong 3 biến đúng.
- (b) là **tautology** — luôn đúng, vì $$p \to q$$ chỉ sai khi $$p = T, q = F$$ còn $$q \to r$$ chỉ sai khi $$q = T, r = F$$; hai trường hợp này không thể đồng thời xảy ra.
- (c) là kiểm tra chẵn lẻ (parity check): đúng khi số biến nhận giá trị True là số lẻ.
- (d) đúng khi có ít nhất 2 biến đúng — tương đương với (a) nhưng viết dưới dạng khác.

</details>

### Bài tập 6: Từ bảng chân trị sang biểu thức

Cho bảng chân trị sau, hãy tìm biểu thức logic tương ứng:

| p | q | r | Kết quả |
|:---:|:---:|:---:|:---:|
| F | F | F | T |
| F | F | T | F |
| F | T | F | F |
| F | T | T | T |
| T | F | F | F |
| T | F | T | T |
| T | T | F | F |
| T | T | T | T |

Gợi ý: Dùng phương pháp **SOP** (tổng các tích / *sum of products*) — tìm các hàng có kết quả T và viết tuyển của các hội.

<details>
<summary>Đáp án</summary>

Các hàng có kết quả True:
- Hàng 1: $$p = F, q = F, r = F$$ → $$\neg p \land \neg q \land \neg r$$
- Hàng 4: $$p = F, q = T, r = T$$ → $$\neg p \land q \land r$$
- Hàng 6: $$p = T, q = F, r = T$$ → $$p \land \neg q \land r$$
- Hàng 8: $$p = T, q = T, r = T$$ → $$p \land q \land r$$

Biểu thức DNF:
<div class="textbook-equation" markdown="1">
$$(\neg p \land \neg q \land \neg r) \lor (\neg p \land q \land r) \lor (p \land \neg q \land r) \lor (p \land q \land r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Rút gọn:
- Nhóm hai hạng tử giữa: $$(\neg p \land \neg q \land \neg r) \lor (p \land q \land r) \lor [(\neg p \land q \land r) \lor (p \land \neg q \land r)]$$.
- Rút $$r$$ ra ngoài: $$r \land [(\neg p \land q) \lor (p \land \neg q)] \equiv r \land (p \oplus q)$$.
- Kết quả cuối: $$(\neg p \land \neg q \land \neg r) \lor (p \land q \land r) \lor (r \land (p \oplus q))$$.

</details>

### Bài tập 7: Ứng dụng bảng chân trị trong kiểm thử

Một hàm Python kiểm tra điều kiện nhập học:

```python
def can_enroll(has_degree, passed_exam, is_priority):
    return (has_degree or passed_exam) and not is_priority
```

(a) Lập bảng chân trị cho hàm `can_enroll`.
(b) Cần bao nhiêu test case để bao phủ 100% tổ hợp đầu vào?

<details>
<summary>Đáp án</summary>

(a) Bảng chân trị:

| has_degree | passed_exam | is_priority | (h.d ∨ p.e) | (h.d ∨ p.e) ∧ ¬i.p | Kết quả |
|:---:|:---:|:---:|:---:|:---:|:---:|
| F | F | F | F | F | F |
| F | F | T | F | F | F |
| F | T | F | T | T | T |
| F | T | T | T | F | F |
| T | F | F | T | T | T |
| T | F | T | T | F | F |
| T | T | F | T | T | T |
| T | T | T | T | F | F |

(b) Có 3 biến nên cần $$2^3 = 8$$ test case để bao phủ 100% tổ hợp đầu vào (exhaustive testing).

</details>

### Bài tập 8: Tautology, Contradiction, Contingency

Phân loại các biểu thức sau:

(a) $$(p \to q) \lor (q \to p)$$
(b) $$(p \to q) \land (p \land \neg q)$$
(c) $$(p \land q) \to (p \lor q)$$
(d) $$(p \to q) \land (q \to r) \land \neg(p \to r)$$
(e) $$(p \oplus q) \to (p \lor q)$$

<details>
<summary>Đáp án</summary>

(a) **Tautology** — Với mọi tổ hợp của $$p, q$$, luôn có ít nhất một trong hai mệnh đề kéo theo đúng. Nếu $$p = T, q = F$$ thì $$p \to q = F$$ nhưng $$q \to p = T$$; nếu $$p = F, q = T$$ thì $$p \to q = T$$.

(b) **Contradiction** — Do $$p \to q \equiv \neg p \lor q$$, kết hợp với $$p \land \neg q$$ ta có:
    $$(\neg p \lor q) \land p \land \neg q$$.
    Áp dụng luật phân phối: $$(\neg p \land p \land \neg q) \lor (q \land p \land \neg q) = F \lor F = F$$.

(c) **Tautology** — Nếu $$p \land q$$ đúng thì cả $$p$$ và $$q$$ đều đúng, suy ra $$p \lor q$$ đúng. Nếu $$p \land q$$ sai thì mệnh đề kéo theo luôn đúng.

(d) **Contradiction** — Nếu $$p \to q$$ và $$q \to r$$ cùng đúng thì theo tam đoạn luận giả định, $$p \to r$$ phải đúng nên $$\neg(p \to r)$$ không thể đúng. Đây là dạng phủ định của một quy tắc suy diễn hợp lệ.

(e) **Tautology** — Nếu $$p \oplus q$$ sai (chẳng hạn $$p = F, q = F$$) thì mệnh đề kéo theo đúng; nếu $$p \oplus q$$ đúng thì có đúng một biến đúng, suy ra $$p \lor q$$ cũng đúng nên mệnh đề kéo theo đúng.

</details>


## Công cụ tương tác

Sinh bảng chân trị và dạng chuẩn DNF/CNF cho một biểu thức với các biến $$p, q, r$$ (hỗ trợ `and`/`or`/`not` hoặc $$\land, \lor, \to, \leftrightarrow$$).
<div class="interactive-demo" markdown="1">
<div data-demo="truth-table-normal-form"></div>
</div>
<script src="{{ '/public/js/truth-table-normal-form.js' | relative_url }}"></script>


## Bài tập bổ sung: Tạo bảng chân trị (từ ccrr1_baitap1)

**Hướng dẫn chung:** Lập bảng chân trị với tất cả các tổ hợp giá trị có thể của các mệnh đề thành phần, sử dụng các phép toán logic cơ bản để tính từng bước.

- **Bài tập 1 (biểu thức đơn giản):** $$P \lor \neg Q$$
- **Bài tập 2 (biểu thức kết hợp):** $$(P \land Q) \to \neg R$$
- **Bài tập 3 (biểu thức phức tạp hơn):** $$\neg(P \lor Q) \leftrightarrow (\neg P \land \neg Q)$$
- **Bài tập 4 (biểu thức ba mệnh đề):** $$(P \land (Q \lor R)) \to (P \land Q)$$
- **Bài tập 5 (biểu thức có phủ định và kéo theo):** $$(\neg P \lor Q) \to (P \to Q)$$

**Bài tập bổ sung từ slide (hoàn thành bảng chân trị):**

Bài tập 1: Cho các mệnh đề chứa biến $$P: x < 0$$ và $$Q: y > 0$$. Hoàn thành bảng chân trị cho các biểu thức kết hợp từ $$P$$ và $$Q$$ (điền đầy đủ các cột giá trị cho $$P, Q$$ và các phép toán tương ứng).

---

## Xem thêm / Video gợi ý

- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Bảng chân trị** liệt kê tất cả $$2^n$$ tổ hợp giá trị của $$n$$ biến và giá trị tương ứng của biểu thức.
- Ba loại mệnh đề: **hằng đúng** (tautology), **hằng sai** (contradiction) và **mệnh đề thường** (contingency).
- Bảng chân trị dùng để kiểm tra **tính hợp lệ của lập luận**.
- Các lỗi thường gặp gồm: nhầm số hàng ($$2^n$$ thay vì $$2n$$), tính sai phép kéo theo, và bỏ qua thứ tự ưu tiên toán tử.
- Bảng chân trị được ứng dụng trực tiếp trong thiết kế test case và kiểm thử phần mềm.

Trong bài tiếp theo, chúng ta sẽ học **tương đương logic** và các **dạng chuẩn tắc** (DNF, CNF).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=UiGu57JzLkE">TRUTH TABLES - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Hướng dẫn cách lập bảng chân trị từng hàng, sát trọng tâm bài học.
- <a href="https://www.youtube.com/watch?v=LNSfM86I8is">Truth Table Example: ~p V ~q</a> — Dr. Trefor Bazett, tiếng Anh. Minh họa chi tiết một bảng chân trị có phép phủ định và phép tuyển.
