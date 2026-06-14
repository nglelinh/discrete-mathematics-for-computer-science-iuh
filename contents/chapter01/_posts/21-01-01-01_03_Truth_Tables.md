---
layout: post
title: "Bảng Chân Trị và Ứng dụng"
categories: chapter01
date: 2021-01-01
order: 3
required: true
lang: en
---

Sau khi học các phép toán logic như `and`, `or`, `not`, ta có thể viết được những biểu thức điều kiện khá phức tạp. Nhưng có một vấn đề rất thực tế: **trực giác của con người thường không đủ đáng tin** khi biểu thức bắt đầu dài ra.

Một điều kiện nhìn có vẻ hợp lý vẫn có thể sai ở đúng **một trường hợp hiếm gặp** — và chính trường hợp đó có thể làm hỏng một giao dịch ngân hàng, mở nhầm quyền truy cập, cho kết quả tìm kiếm sai, hoặc khiến test case bỏ sót lỗi quan trọng nhất. Trong kỹ thuật phần mềm, rất nhiều bug khó chịu không nằm ở cú pháp, mà nằm ở chỗ lập trình viên **tin rằng mình hiểu biểu thức**, trong khi máy tính lại hiểu theo một cách khác.

Đó là lý do ta cần đến **bảng chân trị**. Có thể xem bảng chân trị như một chiếc đèn pha chiếu sáng toàn bộ biểu thức logic: thay vì đoán mò hoặc thử vài ví dụ, ta liệt kê **mọi khả năng có thể xảy ra** và kiểm tra từng trường hợp một cách có hệ thống.

Nhờ bảng chân trị, chúng ta có thể:

- biết chắc một biểu thức hoạt động ra sao trong mọi trường hợp,
- kiểm tra hai cách viết điều kiện có thật sự tương đương hay không,
- phát hiện các mệnh đề luôn đúng hoặc luôn sai,
- và xác định những tổ hợp đầu vào quan trọng cần được kiểm thử trong phần mềm thực tế.

Nói cách khác, bảng chân trị biến logic từ thứ "có vẻ đúng" thành thứ **được chứng minh là đúng**. Trong bài này, chúng ta sẽ học cách xây dựng bảng chân trị, đọc ý nghĩa của nó và dùng nó như một công cụ kiểm chứng cho tư duy logic cũng như cho các biểu thức điều kiện trong lập trình.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Xây dựng** bảng chân trị cho biểu thức có 2, 3 hoặc nhiều biến.
- **Tính** giá trị của biểu thức phức hợp từng bước.
- **Phân loại** biểu thức thành hằng đúng, hằng sai, hoặc mệnh đề thường.
- **Kiểm tra** hai biểu thức có tương đương logic không.
- **Ứng dụng** bảng chân trị để thiết kế test case bao phủ đủ trường hợp.

**Từ khóa**: Bảng chân trị (truth table), tautology, contradiction, contingency, test case, exhaustive checking.

## Bảng chân trị là gì?

**Định nghĩa**: Bảng chân trị là bảng liệt kê tất cả các khả năng về giá trị chân lý của các mệnh đề thành phần và giá trị chân lý tương ứng của mệnh đề phức hợp.

## Cách xây dựng bảng chân trị (3 bước đơn giản)

### Bước 1: Xác định số biến
Với n biến, ta có đúng **2ⁿ dòng** trong bảng chân trị.

**Quy tắc nhanh**:
- 2 biến → 4 dòng
- 3 biến → 8 dòng
- 4 biến → 16 dòng

### Bước 2: Liệt kê tất cả tổ hợp (không bỏ sót)

**Mẹo trực quan**: Hãy tưởng tượng bạn đang đếm nhị phân từ 0 đến 2ⁿ−1.

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

**Quy tắc vàng**: Luôn tính các biểu thức con trước, sau đó mới tính biểu thức chính.

**Ví dụ minh họa**:

```python
# Biểu thức: (p ∧ q) → r
# Ta tính theo thứ tự:

1. Tính p ∧ q trước
2. Sau đó mới tính (kết quả) → r
```

**Mẹo thực tế**: Khi vẽ bảng, thêm cột phụ cho từng biểu thức con để dễ theo dõi.

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

## Các khái niệm quan trọng

### 1. Tautology (Hằng đúng)
Mệnh đề luôn có giá trị T trong mọi trường hợp.

**Ví dụ**: p ∨ ¬p

| p | ¬p | p ∨ ¬p |
|---|---|----|
| T | F  | T  |
| F | T  | T  |

### 2. Contradiction (Hằng sai)
Mệnh đề luôn có giá trị F trong mọi trường hợp.

**Ví dụ**: p ∧ ¬p

| p | ¬p | p ∧ ¬p |
|---|---|----|
| T | F  | F  |
| F | T  | F  |

### 3. Contingency (Mệnh đề thường)
Mệnh đề có thể đúng hoặc sai tùy thuộc vào giá trị của các biến.

## Những nhầm lẫn thường gặp

**Nhầm lẫn 1 — Quên số dòng**: Với n biến, bảng có 2ⁿ dòng, không phải 2n. Nhiều sinh viên mới học chỉ liệt kê n+1 dòng và bỏ sót tổ hợp.

**Nhầm lẫn 2 — Tính toán sai implication**: Implication (→) **chỉ sai khi p=T và q=F**. Mọi trường hợp khác đều đúng. Đây là lỗi phổ biến nhất.

**Nhầm lẫn 3 — Nhầm thứ tự ưu tiên**: ¬ có độ ưu tiên cao hơn ∧, ∧ cao hơn ∨, ∨ cao hơn →, → cao hơn ↔. Nếu không chắc, hãy dùng dấu ngoặc.

## Ứng dụng của bảng chân trị

### 1. Kiểm tra tính tương đương logic
Hai mệnh đề tương đương nếu chúng có cùng bảng chân trị.

**Ví dụ**: Kiểm tra p → q ≡ ¬p ∨ q

| p | q | p → q | ¬p | ¬p ∨ q |
|---|---|-------|----|----|
| T | T |   T   | F  | T  |
| T | F |   F   | F  | F  |
| F | T |   T   | T  | T  |
| F | F |   T   | T  | T  |

**Kết luận**: p → q ≡ ¬p ∨ q (tương đương)

### 2. Kiểm tra tính hợp lệ của lập luận
Lập luận hợp lệ nếu kết luận đúng khi tất cả tiền đề đúng.

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

### 3. Thiết kế mạch logic

Ví dụ: Thiết kế mạch cho (A ∧ B) ∨ C

Bảng chân trị:

| A | B | C | A ∧ B | (A ∧ B) ∨ C |
|---|---|---|---|-------------|
| 0 | 0 | 0 |   0   |      0      |
| 0 | 0 | 1 |   0   |      1      |
| 0 | 1 | 0 |   0   |      0      |
| 0 | 1 | 1 |   0   |      1      |
| 1 | 0 | 0 |   0   |      0      |
| 1 | 0 | 1 |   0   |      1      |
| 1 | 1 | 0 |   1   |      1      |
| 1 | 1 | 1 |   1   |      1      |

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

$$p \lor (q \land \neg r)$$

$$(p \lor q) \land \neg r$$

Trong đó $$p$$ là "admin", $$q$$ là "owner", $$r$$ là "resource locked". Nếu không tương đương, hãy chỉ ra một hàng làm phản ví dụ.

### Bài tập 6: Digital Logic Components

**A.4** This is about basic components in digital logic design. For this exercise, assume a length-n bit string has positions indexed from 0 to n−1, and view the indices as binary (base two) numbers. For example, 0101₁₀ = 0 because the subscript 10 means index two, which is the third position from the left, which is a 0 in 0101.

(a) Write the 2-dimensional table for the 2-to-1 multiplexer function:
Mux: {0,1}² × {0,1} → {0,1} where Mux(x, i) = xᵢ

(b) Write the 2-dimensional table for the 1-to-2 demultiplexer function:
Demux: {0,1} × {0,1} → {0,1}² where Demux(y, i) = bit string with y at index i and 0s elsewhere

(c) Write the table for the 2-to-4 decoder function:
Dec: {0,1}² → {0,1}⁴ where Dec(i) = bit string with 1 at index i and 0s elsewhere

(d) Write the table for the 4-to-2 priority encoder partial function:
Enc: {0,1}⁴ → {0,1}² where Enc(x) = index of the first 1 in x, or undefined if x has no 1

### Bài tập 7: Bảng chân trị 3 biến

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

### Bài tập 8: Từ bảng chân trị sang biểu thức

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

Gợi ý: Dùng phương pháp tổng các tích (sum of products) — tìm các hàng có kết quả T và viết hội của các tuyển.

<details>
<summary>Đáp án</summary>

Các hàng có kết quả True:
- Hàng 1: p=F, q=F, r=F → $$\neg p \land \neg q \land \neg r$$
- Hàng 4: p=F, q=T, r=T → $$\neg p \land q \land r$$
- Hàng 6: p=T, q=F, r=T → $$p \land \neg q \land r$$
- Hàng 8: p=T, q=T, r=T → $$p \land q \land r$$

Biểu thức DNF:
$$(\neg p \land \neg q \land \neg r) \lor (\neg p \land q \land r) \lor (p \land \neg q \land r) \lor (p \land q \land r)$$

Rút gọn:
- $$(\neg p \land \neg q \land \neg r) \lor (p \land q \land r) \lor [(\neg p \land q \land r) \lor (p \land \neg q \land r)]$$
- Có thể rút gọn thêm: Nhóm $$r \land [(\neg p \land q) \lor (p \land \neg q)] = r \land (p \oplus q)$$
- Kết quả cuối: $$(\neg p \land \neg q \land \neg r) \lor (p \land q \land r) \lor (r \land (p \oplus q))$$

</details>

### Bài tập 9: Ứng dụng bảng chân trị trong kiểm thử

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

### Bài tập 10: Tautology, Contradiction, Contingency

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


