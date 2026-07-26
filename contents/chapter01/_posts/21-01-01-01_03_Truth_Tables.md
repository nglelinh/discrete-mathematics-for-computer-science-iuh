---

layout: post
title: "Bảng Chân Trị và Ứng dụng"
categories: chapter01
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã học các phép toán logic và cách ghép chúng thành biểu thức điều kiện. Mục này giới thiệu bảng chân trị (truth table) — công cụ liệt kê…"
---

Ở mục trước chúng ta đã học các phép toán logic và cách ghép chúng thành biểu thức điều kiện. Mục này giới thiệu **bảng chân trị** (truth table) — công cụ liệt kê mọi tổ hợp giá trị chân lý của biến và tính giá trị của biểu thức tương ứng.

Khi biểu thức logic dài ra, trực giác của con người thường không đủ đáng tin. Một điều kiện nhìn hợp lý vẫn có thể sai ở đúng một trường hợp biên — và trường hợp đó có thể làm hỏng giao dịch ngân hàng, mở nhầm quyền truy cập, cho kết quả tìm kiếm sai, hoặc khiến test case bỏ sót lỗi. Nhiều bug trong kỹ thuật phần mềm không nằm ở cú pháp mà ở chỗ lập trình viên tin rằng mình hiểu biểu thức, trong khi máy tính đánh giá theo quy tắc ưu tiên khác.

Bảng chân trị liệt kê **mọi khả năng** một cách có hệ thống, thay cho việc đoán mò hoặc thử vài ví dụ. Nhờ đó chúng ta có thể xác định chính xác hành vi của biểu thức trong mọi trường hợp, kiểm tra tương đương logic giữa hai cách viết, phân loại mệnh đề thành hằng đúng, hằng sai hoặc mệnh đề thường, và chọn tổ hợp đầu vào quan trọng cho kiểm thử. Mục này trình bày cách xây dựng bảng chân trị, đọc ý nghĩa của nó, và ứng dụng vào kiểm chứng logic trong lập trình.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** bảng chân trị cho biểu thức có 2, 3 hoặc nhiều biến.
- **Tính** giá trị của biểu thức phức hợp từng bước.
- **Phân loại** biểu thức thành hằng đúng, hằng sai, hoặc mệnh đề thường.
- **Kiểm tra** hai biểu thức có tương đương logic không.
- **Ứng dụng** bảng chân trị để thiết kế test case bao phủ đủ trường hợp.


**Từ khóa**: Bảng chân trị (truth table), tautology, contradiction, contingency, test case, exhaustive checking.
</div>


## Bảng chân trị là gì?

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Bảng chân trị là bảng liệt kê tất cả các khả năng về giá trị chân lý của các mệnh đề thành phần và giá trị chân lý tương ứng của mệnh đề phức hợp.
</div>


![Không gian quyết định 2ⁿ tổ hợp](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="1.13">Với n biến, bảng chân trị có 2ⁿ dòng — liệt kê mọi tổ hợp giá trị chân lý một cách có hệ thống.</p>
## Cách xây dựng bảng chân trị

### Bước 1: Xác định số biến
Với n biến, ta có đúng **2ⁿ dòng** trong bảng chân trị.

**Quy tắc nhanh**:
- 2 biến → 4 dòng
- 3 biến → 8 dòng
- 4 biến → 16 dòng

### Bước 2: Liệt kê tất cả tổ hợp (không bỏ sót)

**Quy tắc liệt kê**: Các hàng có thể được sinh bằng cách đếm nhị phân từ 0 đến $$2^n - 1$$.

Với 3 biến p, q, r:

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
- Biến đầu tiên: thay đổi mỗi 2^(n−1) dòng
- Biến thứ hai: thay đổi mỗi 2^(n−2) dòng
- Biến cuối cùng: thay đổi mỗi dòng (T, F, T, F...)

### Bước 3: Tính toán từng bước (từ trong ra ngoài)

**Nguyên tắc**: Luôn tính các biểu thức con trước, sau đó mới tính biểu thức chính (từ trong ra ngoài).

**Ví dụ minh họa**:

```python
# Biểu thức: (p ∧ q) → r
# Ta tính theo thứ tự:

1. Tính p ∧ q trước
2. Sau đó mới tính (kết quả) → r
```

Khi lập bảng, nên thêm cột phụ cho từng biểu thức con để theo dõi từng bước tính toán.

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

![Minh họa De Morgan bằng biểu đồ Venn](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

<p class="textbook-figure-caption" data-figure="1.14">Định luật De Morgan — phần bù của hợp/giao tương ứng với giao/hợp của các phần bù.</p>
## Các khái niệm quan trọng

### 1. Tautology (Hằng đúng)
Mệnh đề luôn có giá trị T trong mọi trường hợp.

<div class="textbook-example" markdown="1">
**Ví dụ**: p ∨ ¬p

| p | ¬p | p ∨ ¬p |
|---|---|----|
| T | F  | T  |
| F | T  | T  |
</div>


### 2. Contradiction (Hằng sai)
Mệnh đề luôn có giá trị F trong mọi trường hợp.

<div class="textbook-example" markdown="1">
**Ví dụ**: p ∧ ¬p

| p | ¬p | p ∧ ¬p |
|---|---|----|
| T | F  | F  |
| F | T  | F  |
</div>


### 3. Contingency (Mệnh đề thường)
Mệnh đề có thể đúng hoặc sai tùy thuộc vào giá trị của các biến.

## Những nhầm lẫn thường gặp

**Nhầm lẫn 1 — Quên số dòng**: Với n biến, bảng có 2ⁿ dòng, không phải 2n. Lỗi thường gặp: chỉ liệt kê n+1 dòng và bỏ sót tổ hợp.

**Nhầm lẫn 2 — Tính toán sai implication**: Implication (→) **chỉ sai khi p=T và q=F**. Mọi trường hợp khác đều đúng. Đây là lỗi phổ biến nhất.

**Nhầm lẫn 3 — Nhầm thứ tự ưu tiên**: ¬ có độ ưu tiên cao hơn ∧, ∧ cao hơn ∨, ∨ cao hơn →, → cao hơn ↔. Nếu không chắc, hãy dùng dấu ngoặc.

## Ứng dụng của bảng chân trị

### 1. Kiểm tra tính tương đương logic
Hai mệnh đề tương đương nếu chúng có cùng bảng chân trị.

<div class="textbook-example" markdown="1">
**Ví dụ**: Kiểm tra p → q ≡ ¬p ∨ q

| p | q | p → q | ¬p | ¬p ∨ q |
|---|---|-------|----|----|
| T | T |   T   | F  | T  |
| T | F |   F   | F  | F  |
| F | T |   T   | T  | T  |
| F | F |   T   | T  | T  |

**Kết luận**: p → q ≡ ¬p ∨ q (tương đương)
</div>


### 2. Kiểm tra tính hợp lệ của lập luận
Lập luận hợp lệ nếu kết luận đúng khi tất cả tiền đề đúng.

<div class="textbook-example" markdown="1">
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

<div class="textbook-equation" markdown="1">
$$p \lor (q \land \neg r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$(p \lor q) \land \neg r$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Trong đó $$p$$ là "admin", $$q$$ là "owner", $$r$$ là "resource locked". Nếu không tương đương, hãy chỉ ra một hàng làm phản ví dụ.

### Bài tập 6: Bảng chân trị 3 biến

Xây dựng bảng chân trị đầy đủ cho các biểu thức sau:

(a) $$(p \lor q) \land (q \lor r) \land (r \lor p)$$
(b) $$(p \to q) \lor (q \to r)$$
(c) $$p \oplus q \oplus r$$ (XOR ba ngôi — đúng khi có lẻ số biến đúng)
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
| T | F | T | T | T | F | F |
| T | T | F | T | T | F | T |
| T | T | T | T | T | T | T |

Nhận xét:
- (a) chỉ đúng khi có ít nhất 2 trong 3 biến đúng.
- (b) là **tautology** — luôn đúng (vì $$p \to q$$ chỉ sai khi p=T,q=F và $$q \to r$$ chỉ sai khi q=T,r=F, hai trường hợp không thể đồng thời xảy ra).
- (c) là parity check: đúng khi số biến True là lẻ.
- (d) đúng khi có ít nhất 2 biến đúng — giống (a) nhưng viết khác.

</details>

### Bài tập 7: Từ bảng chân trị sang biểu thức

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

Gợi ý: Dùng phương pháp **SOP** (tổng các tích / *sum of products*) — tìm các hàng có kết quả T và viết hội của các tuyển.

<details>
<summary>Đáp án</summary>

Các hàng có kết quả True:
- Hàng 1: p=F, q=F, r=F → $$\neg p \land \neg q \land \neg r$$
- Hàng 4: p=F, q=T, r=T → $$\neg p \land q \land r$$
- Hàng 6: p=T, q=F, r=T → $$p \land \neg q \land r$$
- Hàng 8: p=T, q=T, r=T → $$p \land q \land r$$

Biểu thức DNF:
<div class="textbook-equation" markdown="1">
$$(\neg p \land \neg q \land \neg r) \lor (\neg p \land q \land r) \lor (p \land \neg q \land r) \lor (p \land q \land r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Rút gọn:
- $$(\neg p \land \neg q \land \neg r) \lor (p \land q \land r) \lor [(\neg p \land q \land r) \lor (p \land \neg q \land r)]$$
- Có thể rút gọn thêm: Nhóm $$r \land [(\neg p \land q) \lor (p \land \neg q)] = r \land (p \oplus q)$$
- Kết quả cuối: $$(\neg p \land \neg q \land \neg r) \lor (p \land q \land r) \lor (r \land (p \oplus q))$$

</details>

### Bài tập 8: Ứng dụng bảng chân trị trong kiểm thử

Một hàm Python kiểm tra điều kiện nhập học:

```python
def can_enroll(has_degree, passed_exam, is_priority):
    return (has_degree or passed_exam) and not is_priority
```

(a) Lập bảng chân trị cho hàm `can_enroll`.
(b) Có bao nhiêu test case cần để bao phủ 100% tổ hợp đầu vào?
(c) Nếu thay đổi yêu cầu thành "cần có bằng hoặc thi đỗ, và không thuộc diện ưu tiên, và (có bằng hoặc ưu tiên)", hãy viết biểu thức mới và so sánh bảng chân trị.

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

(b) Có 3 biến → $$2^3 = 8$$ test case để bao phủ 100% tổ hợp đầu vào (exhaustive testing).

(c) Biểu thức mới: `(has_degree or passed_exam) and not is_priority and (has_degree or is_priority)`

Rút gọn: $$(p \lor q) \land \neg r \land (p \lor r)$$
= $$(p \lor q) \land (p \lor r) \land \neg r$$
= $$(p \lor (q \land r)) \land \neg r$$ (luật phân phối)
= $$(p \land \neg r) \lor (q \land r \land \neg r)$$
= $$p \land \neg r$$ (vì $$q \land r \land \neg r = F$$)

Kết quả: Biểu thức mới tương đương với "có bằng và không thuộc diện ưu tiên" — hoàn toàn khác với bảng gốc!

</details>

### Bài tập 9: Tautology, Contradiction, Contingency

Phân loại các biểu thức sau:

(a) $$(p \to q) \lor (q \to p)$$
(b) $$(p \to q) \land (p \land \neg q)$$
(c) $$(p \land q) \to (p \lor q)$$
(d) $$(p \to q) \land (q \to r) \land \neg(p \to r)$$
(e) $$(p \oplus q) \to (p \lor q)$$

<details>
<summary>Đáp án</summary>

(a) **Tautology** — Với mọi tổ hợp p,q, luôn có ít nhất một trong hai mệnh đề kéo theo đúng. Nếu p=T,q=F thì p→q=F nhưng q→p=T. Nếu p=F,q=T thì p→q=T.

(b) **Contradiction** — $$p \to q \equiv \neg p \lor q$$. Kết hợp với $$p \land \neg q$$:
    $$(\neg p \lor q) \land p \land \neg q$$
    Phân phối: $$(\neg p \land p \land \neg q) \lor (q \land p \land \neg q) = F \lor F = F$$

(c) **Tautology** — Nếu cả p∧q đúng thì p và q đều đúng, do đó p∨q cũng đúng. Nếu p∧q sai thì mệnh đề kéo theo luôn đúng.

(d) **Contradiction** — Nếu p→q và q→r đúng, theo tam đoạn luận giả định thì p→r phải đúng. Do đó không thể có p→r sai. Đây là dạng phủ định của một quy tắc suy diễn hợp lệ.

(e) **Tautology** — p⊕q (XOR) đúng khi p và q khác nhau. Khi đó p∨q luôn đúng (vì ít nhất một biến đúng). Vậy p⊕q→p∨q là hằng đúng. Kiểm tra hàng duy nhất cần quan tâm: nếu p=F,q=F thì p⊕q=F nên mệnh đề kéo theo đúng; nếu p⊕q=T thì p∨q=T nên mệnh đề kéo theo cũng đúng.

</details>

## Bài tập bổ sung: Tạo bảng chân trị (từ ccrr1_baitap1)

**Hướng dẫn chung:** Lập bảng chân trị với tất cả giá trị có thể của các mệnh đề thành phần. Sử dụng các phép toán logic cơ bản để tính toán.

**Bài tập 1: Biểu thức đơn giản**
P ∨ ¬Q

**Bài tập 2: Biểu thức kết hợp**
(P ∧ Q) → ¬R

**Bài tập 3: Biểu thức phức tạp hơn**
¬(P ∨ Q) ↔ (¬P ∧ ¬Q)

**Bài tập 4: Biểu thức với ba mệnh đề**
(P ∧ (Q ∨ R)) → (P ∧ Q)

**Bài tập 5: Biểu thức với phủ định và hàm kéo theo**
(¬P ∨ Q) → (P → Q)

**Bài tập bổ sung từ slide (hoàn thành bảng chân trị):**

Bài tập 1: Cho các mệnh đề tham biến P: x<0 và Q: y>0. Hoàn thành bảng chân trị cho các biểu thức (các cột cần điền giá trị cho P, Q, và các phép toán).

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Bảng chân trị** liệt kê tất cả tổ hợp giá trị của $$n$$ biến ($$2^n$$ hàng) và giá trị của biểu thức tương ứng.
- Ba loại mệnh đề: **hằng đúng** (tautology), **hằng sai** (contradiction), **mệnh đề thường** (contingency).
- Bảng chân trị dùng để **kiểm tra tương đương logic** và **tính hợp lệ của lập luận**.
- Lỗi thường gặp: nhầm số hàng ($$2^n$$ không phải $$2n$$), tính sai kéo theo, bỏ qua thứ tự ưu tiên toán tử.
- Ứng dụng trong thiết kế test case và kiểm thử phần mềm.

Trong bài tiếp theo, chúng ta học **tương đương logic** và cách đưa biểu thức về các **dạng chuẩn tắc** (DNF, CNF).
