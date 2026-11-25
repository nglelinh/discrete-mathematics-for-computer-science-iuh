---

layout: post
title: "Tương đương Logic và Các Dạng Chuẩn tắc"
categories: chapter01
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Trình bày khái niệm tương đương logic, các luật biến đổi biểu thức mệnh đề, cây biểu thức Boolean và hai dạng chuẩn tắc DNF, CNF."
---

Khi một hàm kiểm tra điều kiện có 12 biến Boolean, bảng chân trị phình lên $$2^{12} = 4.096$$ dòng—quá lớn để kiểm tra bằng tay và quá chậm để tối ưu mạch phần cứng. Thay vào đó, các nhà toán học và trình biên dịch dùng **đại số biến đổi tương đương** (như Luật De Morgan, phân phối, hấp thụ) để rút gọn biểu thức và đưa mọi công thức về hai dạng chuẩn vàng: **CNF (Conjunctive Normal Form)** và **DNF (Disjunctive Normal Form)**.

## Kiến thức cần nhớ: Bốn trụ cột của Tương đương Logic & Dạng chuẩn

1. **Hệ thống Luật Tương đương (Đại số Boole)**:
   Giống như các hằng đẳng thức đại số quen thuộc, bộ luật giao hoán, kết hợp, phân phối, hấp thụ ($$p \lor (p \land q) \equiv p$$), và đặc biệt **Luật De Morgan** ($$\neg(p \land q) \equiv \neg p \lor \neg q$$) cho phép biến đổi biểu thức mà bảo toàn tuyệt đối ngữ nghĩa.

2. **Khử phép kéo theo & tương đương**:
   Mọi công thức logic đều quy về được chỉ 3 phép $$\{\neg, \land, \lor\}$$ nhờ hai phép thay thế nền tảng: $$p \to q \equiv \neg p \lor q$$ và $$p \leftrightarrow q \equiv (\neg p \lor q) \land (\neg q \lor p)$$.

3. **Dạng chuẩn hội (CNF) và Dạng chuẩn tuyển (DNF)**:
   - **CNF** là phép HỘI ($$\land$$) của các mệnh đề tuyển (*clauses*): $$(l_1 \lor l_2) \land (l_3 \lor \neg l_4)$$. Đây là đầu vào tiêu chuẩn bắt buộc của mọi **SAT Solver**.
   - **DNF** là phép TUYỂN ($$\lor$$) của các mệnh đề hội: $$(l_1 \land l_2) \lor (\neg l_1 \land l_3)$$. Rất trực quan để liệt kê các kịch bản làm biểu thức Đúng (ví dụ trong bảng chân trị hoặc luật kinh doanh).

4. **Ứng dụng tối ưu hóa mã nguồn & vi mạch**:
   Trình biên dịch (LLVM/GCC) và công cụ tổng hợp mạch (FPGA/ASIC) áp dụng chính các luật rút gọn này để loại bỏ cổng logic thừa, giảm diện tích silicon và tiết kiệm điện năng.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phát biểu** chính xác khái niệm tương đương logic.
- **Sử dụng** các luật tương đương để rút gọn biểu thức mệnh đề.
- **Chuyển đổi** giữa biểu thức logic, bảng chân trị, DNF và CNF.
- **Nhận ra** các lỗi thường gặp khi áp dụng luật De Morgan, phép kéo theo và luật phân phối.
- **Giải thích** vai trò của CNF trong SAT solver và kiểm chứng phần mềm.


**Từ khóa**: logical equivalence, De Morgan, DNF, CNF, reduced form, Boolean function, canonical form.
</div>

## Tương đương logic

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hai mệnh đề phức hợp $$P$$ và $$Q$$ được gọi là **tương đương logic** nếu chúng có cùng giá trị chân trị trong mọi phép gán giá trị cho các biến mệnh đề. Khi đó ta viết:


<div class="textbook-equation" markdown="1">
$$P \equiv Q$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

Điều này tương đương với việc $$P \leftrightarrow Q$$ là một hằng đúng.

**Ký hiệu**:

- $$\equiv$$: tương đương logic, biểu thị quan hệ giữa hai công thức.
- $$\leftrightarrow$$: phép nối hai chiều, là một toán tử nằm bên trong công thức.
- $$T$$ và $$F$$: hằng đúng và hằng sai.

<div class="textbook-example" markdown="1">
**Ví dụ**: Chứng minh $$p \to q \equiv \neg p \lor q$$.

| $$p$$ | $$q$$ | $$p \to q$$ | $$\neg p \lor q$$ |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

Hai cột cuối giống nhau ở mọi hàng, do đó $$p \to q \equiv \neg p \lor q$$.
</div>


<div class="content-box insight-box textbook-block" markdown="1">
**Ghi nhớ**: Tương đương logic là quan hệ thay thế an toàn. Nếu $$P \equiv Q$$, ta có thể thay $$P$$ bằng $$Q$$ trong bất kỳ biểu thức lớn hơn nào mà không làm thay đổi bảng chân trị của toàn bộ biểu thức.
</div>

## Các luật tương đương cơ bản


| Tên luật | Công thức tiêu biểu | Ghi chú |
|:---|:---|:---|
| Đồng nhất | $$p \land T \equiv p$$, $$p \lor F \equiv p$$ | T và F là hằng |
| Nuốt | $$p \lor T \equiv T$$, $$p \land F \equiv F$$ | Giá trị bị chi phối bởi hằng |
| Lũy đẳng | $$p \lor p \equiv p$$, $$p \land p \equiv p$$ | Lặp lại không làm đổi giá trị |
| Phủ định kép | $$\neg\neg p \equiv p$$ | Hai lần phủ định triệt tiêu nhau |
| Giao hoán | $$p \lor q \equiv q \lor p$$, $$p \land q \equiv q \land p$$ | Đổi chỗ hai toán hạng |
| Kết hợp | $$(p \lor q) \lor r \equiv p \lor (q \lor r)$$ | Dấu ngoặc không làm đổi kết quả |
| Phân phối | $$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$ | Phân phối OR qua AND (và ngược lại) |
| De Morgan | $$\neg(p \land q) \equiv \neg p \lor \neg q$$ | Phủ định của AND/OR |
| Hấp thụ | $$p \lor (p \land q) \equiv p$$ | Thành phần phụ bị hấp thụ |
| Bù | $$p \lor \neg p \equiv T$$, $$p \land \neg p \equiv F$$ | Kết hợp biến với phủ định của nó |

Các luật **De Morgan**, **phân phối** và **bù** là những luật được dùng thường xuyên nhất khi rút gọn biểu thức.

### Giải thích: Biến đổi làm từng bước công thức $$(p \to q) \to r$$ về đúng dạng chuẩn CNF

Hãy thực hiện từng bước đại số chuẩn mực để chuyển $$F = (p \to q) \to r$$ sang dạng chuẩn hội (CNF), không bỏ qua bước trung gian nào:

1. **Bước 1 — Khử phép kéo theo bên trong** ($$A \to B \equiv \neg A \lor B$$):
   $$F \equiv (\neg p \lor q) \to r.$$
2. **Bước 2 — Khử phép kéo theo bên ngoài**:
   $$F \equiv \neg(\neg p \lor q) \lor r.$$
3. **Bước 3 — Đẩy dấu phủ định vào sát biến bằng Luật De Morgan & Phủ định kép**:
   $$F \equiv (\neg(\neg p) \land \neg q) \lor r \equiv (p \land \neg q) \lor r.$$
4. **Bước 4 — Áp dụng Luật Phân phối của $$\lor$$ đối với $$\land$$** ($$(A \land B) \lor C \equiv (A \lor C) \land (B \lor C)$$):
   $$F \equiv (p \lor r) \land (\neg q \lor r).$$

**Kiểm chứng lại bằng tay**:
- Công thức kết quả $$(p \lor r) \land (\neg q \lor r)$$ có đúng 2 mệnh đề tuyển nối nhau bằng $$\land$$ → **chuẩn CNF 100%**!
- Thử kiểm tra nhanh tại tổ hợp $$(p, q, r) = (\text{F}, \text{T}, \text{F})$$:
  - Biểu thức gốc: $$(\text{F} \to \text{T}) \to \text{F} = \text{T} \to \text{F} = \mathbf{\text{F}}$$.
  - Dạng CNF: $$(\text{F} \lor \text{F}) \land (\text{F} \lor \text{F}) = \text{F} \land \text{F} = \mathbf{\text{F}}$$. Khớp tuyệt đối!

## Công thức Boolean dưới dạng cây

Một công thức Boolean có thể được biểu diễn dưới dạng **cây có gốc** (rooted tree):

- **Nút gốc và nút trong**: mang nhãn là các phép toán logic (`¬`, `∧`, `∨`, `→`, `↔`, `⊕`).
- **Lá (nút cuối)**: mang nhãn là các biến (`p`, `q`, `r`, ...) hoặc hằng (`T`, `F`).

Cấu trúc của cây được xác định bởi **dấu ngoặc** và thứ tự ưu tiên trong công thức.

**Ví dụ chi tiết**: Xét công thức `((p ∨ q) → ¬r) ↔ p`.

Cây tương ứng:

```
          ↔
         / \
       →    p
      / \
    ∨    ¬
   / \    \
  p   q    r
```

**Bảng chân trị** của công thức này (thứ tự từ điển, T trước F):

| p | q | r | (p ∨ q) | ¬r | (p ∨ q) → ¬r | ((p ∨ q) → ¬r) ↔ p |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | F | F | F |
| T | T | F | T | T | T | T |
| T | F | T | T | F | F | F |
| T | F | F | T | T | T | T |
| F | T | T | T | F | F | T |
| F | T | F | T | T | T | F |
| F | F | T | F | F | T | F |
| F | F | F | F | T | T | F |

**Nhận xét**: Cây biểu thức giúp nhìn rõ **thứ tự tính toán** và **cấu trúc phân cấp** của công thức, trong đó mỗi phép toán là một nút trong và các biến là các lá.

Thử nhập một công thức khác vào khung dưới đây để xem cây của nó, rồi thay đổi giá trị các biến để theo dõi quá trình tính giá trị từ lá lên gốc.

<div class="interactive-demo" markdown="1">
<div data-demo="exprtree-explainer" data-formula="((p ∨ q) → ¬r) ↔ p"></div>
</div>

![Luật De Morgan trên biểu đồ Venn](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

<p class="textbook-figure-caption" data-figure="1.16">Luật De Morgan — ¬(p ∧ q) ≡ ¬p ∨ ¬q, công cụ biến đổi quan trọng khi rút gọn điều kiện.</p>
![DNF — tổng các tích (disjunction of conjunctions)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-OR.png)

<p class="textbook-figure-caption" data-figure="1.17">Dạng chuẩn tắc tuyển (DNF) — tuyển (OR) của các hội (AND), xây dựng từ các hàng có kết quả Đúng trong bảng chân trị.</p>
![CNF — tích các tổng (conjunction of disjunctions)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-AND.png)

<p class="textbook-figure-caption" data-figure="1.18">Dạng chuẩn tắc hội (CNF) — hội (AND) của các tuyển (OR), dạng chuẩn mà SAT solver yêu cầu.</p>
**Lưu ý quan trọng**: Các phép toán `∧`, `∨`, `⊕`, `↔` đều có tính **giao hoán** và **kết hợp**, còn phép kéo theo `→` thì không. Vì vậy, ta có thể viết `R ∧ Q ∧ P` thay vì `(R ∧ Q) ∧ P` và sắp xếp lại thứ tự các biến mà không làm thay đổi giá trị.

**Ứng dụng**:
- **Trình biên dịch** biểu diễn biểu thức Boolean dưới dạng cây trước khi tối ưu hóa.
- **Kiểm chứng hình thức** thao tác trực tiếp trên cấu trúc cây của công thức.
- **Phân tích tĩnh** dùng cây biểu thức để phát hiện nhánh chết hoặc điều kiện luôn đúng/sai.

Ta chứng minh $$\neg(p \land q) \equiv \neg p \lor \neg q$$ bằng bảng chân trị:

| $$p$$ | $$q$$ | $$p \land q$$ | $$\neg(p \land q)$$ | $$\neg p$$ | $$\neg q$$ | $$\neg p \lor \neg q$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

Hai cột $$\neg(p \land q)$$ và $$\neg p \lor \neg q$$ giống nhau ở mọi hàng, nên luật De Morgan đúng.

#### Minh họa bằng mã nguồn

Luật De Morgan xuất hiện thường xuyên khi viết điều kiện phủ định:

```python
# Vế trái: NOT (A AND B)
if not (is_admin and is_active):
    deny_access()

# Vế phải: NOT A OR NOT B — tương đương logic
if (not is_admin) or (not is_active):
    deny_access()
```

Hai điều kiện này **luôn cho cùng kết quả** trên mọi đầu vào. Vì vậy, luật De Morgan đóng vai trò quan trọng khi rút gọn biểu thức trong lập trình và tối ưu truy vấn.

## Biến đổi biểu thức logic

<div class="textbook-example" markdown="1">
**Ví dụ**: Rút gọn biểu thức $$\neg(p \lor \neg q) \land (r \lor \neg r)$$.

$$\begin{aligned}
\neg(p \lor \neg q) \land (r \lor \neg r)
&\equiv (\neg p \land \neg\neg q) \land T && \text{De Morgan và luật bù}\\
&\equiv (\neg p \land q) \land T && \text{phủ định kép}\\
&\equiv \neg p \land q && \text{đồng nhất.}
\end{aligned}$$

**Nhận xét**: Mỗi bước biến đổi cần nêu rõ luật được áp dụng. Trong chứng minh toán học và kiểm chứng chương trình, việc ghi rõ luật giúp phát hiện sai sót sớm.
</div>


## Công thức Dạng Rút gọn (Reduced Forms)

### Định nghĩa Dạng Rút gọn

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một biểu thức logic $$E$$ được gọi là **dạng rút gọn** (reduced form) nếu thỏa mãn đồng thời 3 điều kiện sau:


1. **Không chứa hằng số** $$T$$ hoặc $$F$$ (trừ khi toàn bộ biểu thức chỉ là hằng số đó).
2. **Không chứa cặp bù** (một literal và phủ định của nó trong cùng một clause hoặc term).
3. **Không chứa thành phần dư thừa** (các literal lặp lại trong cùng một clause/term, hoặc các term/clause trùng nhau).
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$\neg p \land q$$ là dạng rút gọn.
- $$(\neg p \land q) \lor (\neg p \land \neg q)$$ **không** phải dạng rút gọn (rút gọn được thành $$\neg p$$).
- $$p \lor \neg p$$ **không** phải dạng rút gọn (chứa cặp bù, rút gọn thành $$T$$).
- $$p \land p$$ **không** phải dạng rút gọn (lặp literal, rút gọn thành $$p$$).

**Mục tiêu**: Tìm dạng rút gọn ngắn gọn (ít literal nhất) tương đương với biểu thức ban đầu.
</div>


### Vì sao cần rút gọn?

Một biểu thức logic có thể được viết theo nhiều cách khác nhau, nhưng biểu thức rườm rà thường dẫn đến:

- **Mã nguồn khó đọc**: `if ((a && b) || (a && !b))` buộc người đọc phải phân tích thêm mới thấy nó tương đương `if (a)`.
- **Truy vấn nặng hơn**: nhiều điều kiện lồng nhau khiến bộ tối ưu truy vấn của cơ sở dữ liệu khó xử lý.
- **Tốn thêm chi phí tính toán**: nhiều phép toán hơn dẫn đến tốn nhiều chu kỳ CPU hơn.

**Bài toán rút gọn**: Cho một biểu thức logic, tìm biểu thức ngắn gọn nhất có thể mà vẫn tương đương logic với biểu thức ban đầu.

### Rút gọn bằng Luật Tương đương

Các luật tương đương ở bảng trên là công cụ chính để rút gọn. Quy trình thường dùng gồm bốn bước:

1. **Loại bỏ phép kéo theo**: thay $$p \to q$$ bằng $$\neg p \lor q$$.
2. **Áp dụng luật De Morgan** để đẩy phép phủ định vào sát các biến.
3. **Phân phối** và **gộp** các thành phần chung.
4. **Loại bỏ hằng số** bằng các luật đồng nhất, nuốt và bù.

**Ví dụ 1**: Rút gọn $$(\neg p \land q) \lor (\neg p \land \neg q)$$.

$$\begin{aligned}
(\neg p \land q) \lor (\neg p \land \neg q)
&\equiv \neg p \land (q \lor \neg q) && \text{(phân phối)} \\
&\equiv \neg p \land T && \text{(luật bù)} \\
&\equiv \neg p && \text{(đồng nhất)}.
\end{aligned}$$

**Ví dụ 2 (tối ưu điều kiện trong mã nguồn)**:

```python
# Biểu thức gốc
if (x > 0 and y > 0) or (x > 0 and y <= 0):
    do_something()

# Sau rút gọn: x > 0
if x > 0:
    do_something()
```

Điều kiện ban đầu có dạng $$(p \land q) \lor (p \land \neg q)$$ với $$p = (x > 0)$$ và $$q = (y > 0)$$, nên rút gọn thành $$p$$.

**Quan sát chính**: Hai hội $$p \land q$$ và $$p \land \neg q$$ chỉ khác nhau ở một literal ($$q$$ và $$\neg q$$). Khi gặp cặp như vậy, ta luôn gộp được thành $$p$$ (khử biến $$q$$). Đây là ý tưởng nền tảng của các thuật toán rút gọn biểu thức Boolean: phát hiện các cặp chỉ khác nhau đúng một literal và gộp chúng lại.

## Dạng chuẩn tắc tuyển DNF

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Dạng chuẩn tắc tuyển** (Disjunctive Normal Form, DNF) là biểu thức có dạng tuyển của các hội, trong đó mỗi thành phần nhỏ là một literal (biến hoặc phủ định của biến):


<div class="textbook-equation" markdown="1">
$$(l_{11} \land l_{12} \land \cdots) \lor (l_{21} \land l_{22} \land \cdots) \lor \cdots$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: $$(p \land q) \lor (\neg p \land r)$$ là một biểu thức ở dạng DNF.
</div>


### Tạo DNF từ bảng chân trị (cách trực quan)

Quy trình xây dựng DNF từ bảng chân trị gồm ba bước: (1) chỉ xét các hàng có kết quả **TRUE**; (2) với mỗi hàng đó, viết một hội (AND) trong đó biến có giá trị đúng giữ nguyên, biến có giá trị sai lấy phủ định; (3) lấy tuyển (OR) của tất cả các hội vừa tạo.

<div class="textbook-example" markdown="1">
**Ví dụ**: Xây dựng DNF cho $$p \to q$$.

Bảng chân trị:

| $$p$$ | $$q$$ | $$p \to q$$ |
|:---:|:---:|:---:|
| T | T | **T** |
| T | F | F |
| F | T | **T** |
| F | F | **T** |

**Bước 1 & 2**: Chỉ giữ lại 3 hàng có kết quả TRUE:

- Hàng 1 (`T, T`): $$p \land q$$
- Hàng 3 (`F, T`): $$\neg p \land q$$
- Hàng 4 (`F, F`): $$\neg p \land \neg q$$

**Bước 3**: Lấy tuyển của ba hội trên:

<div class="textbook-equation" markdown="1">
$$
(p \land q) \lor (\neg p \land q) \lor (\neg p \land \neg q)
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đây chính là **DNF đầy đủ** của $$p \to q$$.
</div>


#### Minh họa: DNF như bản đồ vùng đúng

Với hai biến, bảng chân trị tạo thành lưới 2×2 trong đó mỗi ô ứng với một phép gán giá trị. DNF đầy đủ phủ mọi ô có kết quả đúng bằng từng term riêng lẻ; khi rút gọn, các ô liền kề được gộp lại thành khối lớn hơn để thu được biểu thức ngắn hơn. Ví dụ trên rút gọn thành $$\neg p \lor q$$. Đây là ý tưởng nền tảng của các thuật toán tối thiểu hóa biểu thức Boolean trong trình biên dịch và tối ưu truy vấn.

## Dạng chuẩn tắc hội CNF

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Dạng chuẩn tắc hội** (Conjunctive Normal Form, CNF) là biểu thức có dạng hội của các tuyển:


<div class="textbook-equation" markdown="1">
$$(l_{11} \lor l_{12} \lor \cdots) \land (l_{21} \lor l_{22} \lor \cdots) \land \cdots$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: $$(p \lor q) \land (\neg p \lor r) \land (q \lor \neg r)$$ là một biểu thức ở dạng CNF.
</div>


**Ký hiệu**: Mỗi ngoặc trong CNF thường được gọi là một **mệnh đề con** (clause). CNF là dạng đầu vào tiêu chuẩn của nhiều bộ giải SAT.

**Lưu ý**: Trong khoa học máy tính, ta thường dùng bit `1` và `0` thay cho `T` và `F`, và ký hiệu biến là $$x_1, \dots, x_n$$. Ví dụ, gán $$x = 101$$ vào công thức $$(x_1 \land x_2 \land x_3) \lor (\neg x_1 \land \neg x_2 \land \neg x_3)$$ cho kết quả `0`.

**Toán tử bitwise trên chuỗi bit**: Các phép toán logic có thể được mở rộng sang **chuỗi bit** bằng cách áp dụng theo từng vị trí bit. Ví dụ:

- $$\neg 1010 = 0101$$
- $$1010 \land 0110 = 0010$$
- $$1010 \lor 0110 = 1110$$

### Tạo CNF từ bảng chân trị (cách trực quan)

Tương tự DNF, ta có thể xây dựng CNF từ bảng chân trị theo 3 bước:

1. **Xét bảng chân trị** và chỉ giữ lại các hàng có kết quả **FALSE**.
2. **Với mỗi hàng FALSE**, viết một tuyển (OR) sao cho nó sai tại đúng hàng đó:
   - Nếu biến nhận giá trị `TRUE` → lấy **phủ định** của biến.
   - Nếu biến nhận giá trị `FALSE` → giữ nguyên biến.
3. **Lấy hội (AND)** của tất cả các tuyển vừa tạo.

<div class="textbook-example" markdown="1">
**Ví dụ**: Xây dựng CNF cho $$p \to q$$.

Bảng chân trị (chỉ xét hàng FALSE):

| $$p$$ | $$q$$ | $$p \to q$$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

**Bước 1 & 2**: Chỉ có 1 hàng FALSE (`T, F`):

- Biến `p = TRUE` → lấy $$\neg p$$.
- Biến `q = FALSE` → giữ nguyên $$q$$.

Ta viết tuyển tương ứng: $$\neg p \lor q$$.

**Bước 3**: Vì chỉ có một mệnh đề con, CNF thu được là:

<div class="textbook-equation" markdown="1">
$$
\neg p \lor q
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
(Nếu có nhiều hàng FALSE, ta lấy **hội** của tất cả các tuyển tương ứng.)
</div>


#### Minh họa: CNF như danh sách ràng buộc

Xét CNF dưới góc nhìn lập trình:

```python
# CNF: (p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)
# Ý nghĩa: TẤT CẢ các mệnh đề con phải đúng

def is_satisfied(p, q, r):
    clause1 = p or q
    clause2 = (not p) or r
    clause3 = q or (not r)
    return clause1 and clause2 and clause3
```

Mỗi `clause` đóng vai trò như một ràng buộc. SAT solver cần tìm một phép gán biến sao cho **không có ràng buộc nào bị vi phạm**. Vì thế, CNF là dạng đầu vào tự nhiên cho hầu hết các bộ giải SAT hiện đại.

### Video ngắn: DNF và CNF

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/dnf-cnf-normal-forms.mp4"></video>
</div>

Video dài khoảng 2 phút 45 giây, trình bày khái niệm literal, cách lập DNF từ các hàng T và CNF từ các hàng F của bảng chân trị, cách biến đổi bằng luật, kiểm tra lại bằng bảng chân trị, và lý do SAT solver dùng CNF.

## Các định lý quan trọng về DNF và CNF

<div class="textbook-theorem" id="định-lý-1-sự-tồn-tại-dnf-và-cnf" markdown="1">
**Định lý 1 (Sự tồn tại DNF và CNF)**:

**Mọi biểu thức mệnh đề đều có thể đưa về dạng DNF và CNF.**
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh (phác thảo)**: Từ bảng chân trị, ta luôn xây dựng được DNF bằng cách lấy tuyển các hội ứng với các hàng đúng, và xây dựng CNF bằng cách lấy hội các tuyển ứng với các hàng sai (với hằng sai dùng quy ước tuyển rỗng, với hằng đúng dùng quy ước hội rỗng hoặc dạng tương đương $$p \land \neg p$$ / $$p \lor \neg p$$). Vì mọi biểu thức đều có bảng chân trị hữu hạn nên DNF và CNF luôn tồn tại.
</div>

### Định lý 2: Tính duy nhất của DNF/CNF đầy đủ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **DNF đầy đủ** (full DNF / canonical DNF) của hàm Boolean $$ f $$ trên $$ n $$ biến là biểu thức DNF trong đó **mỗi term** chứa đúng $$ n $$ literal (mỗi biến xuất hiện đúng một lần, ở dạng khẳng định hoặc phủ định). Tương tự, **CNF đầy đủ** (full CNF) là CNF trong đó mỗi clause chứa đúng $$ n $$ literal.
</div>


<div class="textbook-theorem" markdown="1">
**Định lý**: Mọi hàm Boolean $$ f:\{T,F\}^n\to\{T,F\} $$ đều có **đúng một** DNF đầy đủ và **đúng một** CNF đầy đủ (duy nhất, không kể thứ tự các term/clause và thứ tự literal bên trong mỗi term/clause).
</div>


<div class="textbook-proof" markdown="1">
**Chứng minh (Tính duy nhất của DNF đầy đủ)**:

Giả sử $$ D_1 $$ và $$ D_2 $$ là hai DNF đầy đủ cùng biểu diễn hàm $$ f $$ (do đó $$ D_1 \equiv D_2 $$).

1. **Mỗi term trong DNF đầy đủ tương ứng duy nhất với một phép gán (assignment)**:
   - Với phép gán $$ \alpha = (a_1, \dots, a_n) \in \{T,F\}^n $$, ta xây dựng term:
     $$
     m_\alpha = \bigwedge_{i=1}^n \ell_i, \quad \text{trong đó } \ell_i = x_i \text{ nếu } a_i = T,\quad \ell_i = \neg x_i \text{ nếu } a_i = F.
     $$
   - Term $$ m_\alpha $$ chỉ nhận giá trị đúng duy nhất tại phép gán $$ \alpha $$ (tức $$ m_\alpha(\alpha) = T $$ và sai tại mọi phép gán khác).

2. **Mối quan hệ giữa DNF đầy đủ và bảng chân trị**:
   - Giả sử $$ D_1 = m_{\alpha_1} \lor m_{\alpha_2} \lor \cdots \lor m_{\alpha_k} $$, trong đó $$ f(\alpha_j) = T $$ với mọi $$ j $$.
   - Tương tự, $$ D_2 = m_{\beta_1} \lor \cdots \lor m_{\beta_m} $$.
   - Vì $$ D_1 \equiv f $$ và $$ D_2 \equiv f $$, tập $$ \{\alpha_1,\dots,\alpha_k\} $$ và tập $$ \{\beta_1,\dots,\beta_m\} $$ đều chính là tập tất cả các phép gán làm $$ f = T $$.

3. **Mâu thuẫn nếu hai DNF đầy đủ khác nhau về tập term**:
   - Giả sử $$ D_1 \neq D_2 $$ (không kể thứ tự term và literal). Khi đó tồn tại ít nhất một phép gán $$ \alpha^* $$ sao cho $$ m_{\alpha^*} $$ xuất hiện trong $$ D_1 $$ nhưng không xuất hiện trong $$ D_2 $$ (hoặc ngược lại).
   - Xét giá trị của hai biểu thức tại phép gán $$ \alpha^* $$:
     - $$ D_1(\alpha^*) = T $$ (vì chứa term $$ m_{\alpha^*} $$ đúng tại $$ \alpha^* $$).
     - $$ D_2(\alpha^*) = F $$ (vì không chứa term nào đúng tại $$ \alpha^* $$).
   - Điều này mâu thuẫn với giả thiết $$ D_1 \equiv D_2 $$.

Do đó $$ D_1 = D_2 $$ (hai DNF đầy đủ có cùng tập hợp các term).
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh cho CNF đầy đủ**: Hoàn toàn tương tự bằng cách đối ngẫu hóa (thay $$ \lor $$ bằng $$ \land $$, $$ T $$ bằng $$ F $$, và mỗi literal bằng phủ định của nó), hoặc áp dụng Định lý 3 bên dưới cho $$ \neg f $$.
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả quan trọng**:
- DNF đầy đủ và CNF đầy đủ là **dạng chuẩn tắc** (canonical form) của hàm Boolean.
- Hai hàm Boolean bằng nhau khi và chỉ khi DNF đầy đủ (hoặc CNF đầy đủ) của chúng trùng nhau.
</div>

<div class="textbook-theorem" id="định-lý-3-mối-quan-hệ-giữa-dnf-và-cnf-qua-phủ-định" markdown="1">
**Định lý 3 (Mối quan hệ giữa DNF và CNF qua phủ định)**:

**Nếu** $$P$$ **có DNF** $$(l_{11} \land l_{12} \land \cdots) \lor (l_{21} \land l_{22} \land \cdots) \lor \cdots$$, **thì** $$\neg P$$ **có CNF** $$( \neg l_{11} \lor \neg l_{12} \lor \cdots) \land ( \neg l_{21} \lor \neg l_{22} \lor \cdots) \land \cdots$$.
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả**: Phủ định của DNF là CNF và ngược lại (áp dụng luật De Morgan mở rộng).
</div>

<div class="textbook-theorem" id="định-lý-4-biểu-diễn-hàm-boolean" markdown="1">
**Định lý 4 (Biểu diễn hàm Boolean)**:

**Mọi hàm Boolean** $$f: \{T,F\}^n \to \{T,F\}$$ **đều có biểu diễn DNF đầy đủ và CNF đầy đủ duy nhất**.
</div>

**Ý nghĩa trong khoa học máy tính**: Đây là nền tảng của:
- **Tối ưu trình biên dịch (compiler optimization)**: rút gọn biểu thức Boolean trong mã nguồn và mã trung gian.
- **Tối ưu truy vấn (query optimization)**: chuẩn hóa điều kiện lọc trong SQL để hệ quản trị cơ sở dữ liệu xử lý hiệu quả hơn.
- **SAT solver**: nhận đầu vào dạng CNF và tìm phép gán biến thỏa mãn công thức.

## Ứng dụng trong Khoa học Máy tính

- **Tối ưu điều kiện trong chương trình**: Trình biên dịch có thể chuyển `not (a and b)` thành `(not a) or (not b)` để đơn giản hóa nhánh điều kiện.
- **SAT solver**: Nhiều bài toán lập lịch, kiểm chứng phần mềm, giải Sudoku và phân tích phụ thuộc được mã hóa thành CNF.
- **Cơ sở dữ liệu**: Bộ tối ưu truy vấn SQL áp dụng các luật tương đương để đẩy điều kiện lọc xuống sớm hơn.

```python
# De Morgan trong kiểm tra điều kiện
if not (is_admin and is_active):
    deny_access()

# Tương đương với
if (not is_admin) or (not is_active):
    deny_access()
```

## Bài tập thực hành

### Bài tập 1: Chứng minh tương đương bằng bảng chân trị

Chứng minh rằng $$p \to (q \lor r) \equiv (p \to q) \lor (p \to r)$$ bằng cách lập bảng chân trị đầy đủ cho cả hai vế.

<details>
<summary>Đáp án</summary>

Bảng chân trị 8 hàng cho 3 biến cho thấy hai cột kết quả của hai vế giống nhau ở mọi tổ hợp giá trị. Do đó hai biểu thức tương đương logic.

</details>

### Bài tập 2: Rút gọn biểu thức

Rút gọn biểu thức sau về dạng đơn giản nhất:

<div class="textbook-equation" markdown="1">
$$\neg(p \land \neg q) \lor (\neg p \land q)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<details>
<summary>Đáp án</summary>

Áp dụng luật De Morgan, phủ định kép và luật hấp thụ:

<div class="textbook-equation" markdown="1">
$$\equiv (\neg p \lor q) \lor (\neg p \land q) \equiv \neg p \lor q$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 3: Chuyển sang DNF và CNF

Cho biểu thức $$(p \lor q) \land (\neg p \lor r)$$.

1. Viết dạng DNF đầy đủ.
2. Viết dạng CNF (đã ở dạng CNF).

<details>
<summary>Đáp án</summary>

- **DNF rút gọn**: Áp dụng luật phân phối ta có $(p \land \neg p) \lor (p \land r) \lor (q \land \neg p) \lor (q \land r) \equiv (p \land r) \lor (\neg p \land q) \lor (q \land r)$.
- **DNF đầy đủ** (mỗi term chứa đủ 3 biến $p, q, r$):
  $(p \land q \land r) \lor (p \land \neg q \land r) \lor (\neg p \land q \land r) \lor (\neg p \land q \land \neg r)$.
- **CNF**: Giữ nguyên $(p \lor q) \land (\neg p \lor r)$.

</details>

### Bài tập 4: Ứng dụng thực tế

Viết một đoạn mã Python kiểm tra điều kiện `not (user.is_banned() and user.is_inactive())` theo hai cách tương đương. Giải thích vì sao một trong hai cách dễ đọc hơn.

<details>
<summary>Đáp án</summary>

```python
if not (user.is_banned() and user.is_inactive()):
    allow_access()

# Tương đương (De Morgan)
if (not user.is_banned()) or (not user.is_inactive()):
    allow_access()
```

Cách thứ hai trực quan hơn khi đọc điều kiện cho phép và tận dụng đánh giá đoản mạch (short-circuit evaluation) ngay khi điều kiện đầu tiên đúng.

</details>

### Bài tập 5: Boolean Functions and Lexicographic Order

**A.5** Recall the lexicographic order on {0,1}ⁿ. We extend this to the lexicographic order on all functions f: {0,1}ⁿ → {0,1}: We say f lexicographically precedes g when f(x) = 0 and g(x) = 1 for the lexicographically lowest x such that f(x) ≠ g(x).

For i ∈ [16], define fᵢ: {0,1}² → {0,1} to be the i-th such function in lexicographic order. Write the 2-dimensional table for F: {0,1}² × [16] → {0,1} where F(x, i) = fᵢ(x).

### Bài tập 6: Logical Equivalences with Conditionals

**A.7** Determine which of the following hold. For each, if equivalent then write the shared truth table, and if inequivalent then give a counterexample truth assignment.

(a) ¬(P ⇔ Q) ≡ ¬P ⇔ Q

(b) ¬(P ⇒ Q) ≡ ¬P ⇒ Q

(c) (P ∨ Q) ⇒ R ≡ (P ⇒ R) ∧ (Q ⇒ R)

(d) (P ∧ Q) ⇒ R ≡ (P ⇒ R) ∨ (Q ⇒ R)

(e) (P ⇔ Q) ⇒ R ≡ (P ⇒ R) ⇔ (Q ⇒ R)

### Bài tập 7: Áp dụng luật De Morgan

Rút gọn các biểu thức sau bằng luật De Morgan và các luật tương đương khác:

(a) $$\neg(p \lor \neg q)$$
(b) $$\neg(\neg p \land (q \lor r))$$
(c) $$(\neg p \land \neg q) \lor \neg(\neg r \lor p)$$
(d) $$\neg((p \land q) \lor (\neg p \land \neg q))$$
(e) $$\neg(p \to q) \lor \neg(q \to p)$$

<details>
<summary>Đáp án</summary>

(a) $\neg(p \lor \neg q) \equiv \neg p \land \neg(\neg q) \equiv \neg p \land q$.

(b) $\neg(\neg p \land (q \lor r)) \equiv \neg(\neg p) \lor \neg(q \lor r) \equiv p \lor (\neg q \land \neg r)$.

(c) $(\neg p \land \neg q) \lor \neg(\neg r \lor p)$
    $\equiv (\neg p \land \neg q) \lor (\neg(\neg r) \land \neg p)$
    $\equiv (\neg p \land \neg q) \lor (r \land \neg p)$
    $\equiv \neg p \land (\neg q \lor r)$ (luật phân phối).

(d) $\neg((p \land q) \lor (\neg p \land \neg q))$
    $\equiv \neg(p \land q) \land \neg(\neg p \land \neg q)$
    $\equiv (\neg p \lor \neg q) \land (p \lor q)$
    $\equiv (\neg p \land p) \lor (\neg p \land q) \lor (\neg q \land p) \lor (\neg q \land q)$
    $\equiv F \lor (\neg p \land q) \lor (p \land \neg q) \lor F$
    $\equiv (\neg p \land q) \lor (p \land \neg q) \equiv p \oplus q$.
    Kết luận: Biểu thức tương đương với phép **XOR**.

(e) $\neg(p \to q) \lor \neg(q \to p)$
    $\equiv \neg(\neg p \lor q) \lor \neg(\neg q \lor p)$
    $\equiv (p \land \neg q) \lor (q \land \neg p)$
    $\equiv p \oplus q$.
    Kết luận: Biểu thức cũng tương đương với phép **XOR**.

</details>

### Bài tập 8: Kiểm tra tương đương bằng biến đổi

Không dùng bảng chân trị, hãy chứng minh các tương đương sau bằng biến đổi logic:

(a) $$p \to (q \to r) \equiv (p \land q) \to r$$
(b) $$(p \to q) \land (p \to r) \equiv p \to (q \land r)$$
(c) $$p \leftrightarrow q \equiv (p \to q) \land (q \to p)$$
(d) $$p \to (q \to p)$$ là hằng đúng.

<details>
<summary>Đáp án</summary>

(a) $p \to (q \to r) \equiv \neg p \lor (\neg q \lor r) \equiv (\neg p \lor \neg q) \lor r \equiv \neg(p \land q) \lor r \equiv (p \land q) \to r$.
    Đây là luật **exportation**: hai điều kiện lồng nhau tương đương với điều kiện hội.

(b) $(p \to q) \land (p \to r) \equiv (\neg p \lor q) \land (\neg p \lor r) \equiv \neg p \lor (q \land r) \equiv p \to (q \land r)$ (áp dụng luật phân phối).

(c) Đây chính là định nghĩa của phép tương đương hai chiều: $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$, có thể kiểm chứng trực tiếp bằng bảng chân trị.

(d) $p \to (q \to p) \equiv \neg p \lor (\neg q \lor p) \equiv (\neg p \lor p) \lor \neg q \equiv T \lor \neg q \equiv T$.
    Vậy biểu thức là hằng đúng (tautology).

</details>

### Bài tập 9: Chuyển đổi giữa DNF và CNF

Cho biểu thức: $$(p \land q) \lor (\neg p \land \neg q)$$.

(a) Biểu thức này đã ở dạng DNF chưa? Giải thích.
(b) Chuyển biểu thức sang dạng CNF.
(c) Nhận xét về ý nghĩa của biểu thức này — nó tương ứng với phép toán logic nào?

<details>
<summary>Đáp án</summary>

(a) **Đã ở dạng DNF** — DNF là tuyển của các hội. Biểu thức có dạng $C_1 \lor C_2$ với $C_1 = p \land q$ và $C_2 = \neg p \land \neg q$; mỗi hội chứa đúng hai literal và mỗi biến xuất hiện đúng một lần (đây cũng là DNF đầy đủ).

(b) Chuyển sang CNF:
    $(p \land q) \lor (\neg p \land \neg q)$
    $\equiv [(p \land q) \lor \neg p] \land [(p \land q) \lor \neg q]$ (phân phối)
    $\equiv [(p \lor \neg p) \land (q \lor \neg p)] \land [(p \lor \neg q) \land (q \lor \neg q)]$
    $\equiv [T \land (q \lor \neg p)] \land [(p \lor \neg q) \land T]$
    $\equiv (\neg p \lor q) \land (p \lor \neg q)$.

(c) Biểu thức này tương đương với **$p \leftrightarrow q$** (phép tương đương). Dạng DNF diễn đạt "hoặc cả hai cùng đúng, hoặc cả hai cùng sai"; dạng CNF diễn đạt "nếu $p$ thì $q$, và nếu $q$ thì $p$".

</details>

### Bài tập 10: Ứng dụng rút gọn biểu thức trong mã nguồn

Một lập trình viên viết điều kiện sau:

```python
if (user.is_active and not user.is_banned) or (user.is_active and user.has_vip):
    grant_access()
```

(a) Viết biểu thức logic cho điều kiện này.
(b) Rút gọn biểu thức bằng các luật tương đương.
(c) Viết lại đoạn mã Python gọn hơn.
(d) Kiểm tra với `user.is_active = True, user.is_banned = True, user.has_vip = False`: mã gốc và mã sau khi rút gọn có cho cùng kết quả không?

<details>
<summary>Đáp án</summary>

(a) Đặt $a$: `user.is_active`, $b$: `user.is_banned`, $v$: `user.has_vip`.
    Biểu thức: $(a \land \neg b) \lor (a \land v)$.

(b) Rút gọn theo luật phân phối:
    $(a \land \neg b) \lor (a \land v) \equiv a \land (\neg b \lor v)$.
    Ý nghĩa: "Người dùng đang hoạt động VÀ (không bị cấm HOẶC có VIP)".

(c) Mã nguồn sau khi rút gọn:
    ```python
    if user.is_active and (not user.is_banned or user.has_vip):
        grant_access()
    ```

(d) Kiểm tra với $a = T, b = T, v = F$:
    - Mã gốc: $(T \land \neg T) \lor (T \land F) = (T \land F) \lor F = F \lor F = F$.
    - Mã rút gọn: $T \land (\neg T \lor F) = T \land (F \lor F) = T \land F = F$.
    Hai cách cho kết quả giống nhau (cả hai đều không cấp quyền truy cập).

</details>

### Bài tập 11: Xác định dạng chuẩn

Cho các biểu thức sau, xác định xem mỗi biểu thức đã ở dạng DNF, CNF, cả hai hay không thuộc dạng nào:

(a) $$(p \lor q) \land (\neg p \lor r)$$
(b) $$(p \land \neg q) \lor (q \land r) \lor (\neg p \land \neg r)$$
(c) $$(p \lor q) \land (r)$$
(d) $$p \lor (q \land r)$$
(e) $$(p \to q) \land (q \to r)$$

<details>
<summary>Đáp án</summary>

(a) **CNF** — Hội của hai mệnh đề con tuyển các literal: $(p \lor q)$ và $(\neg p \lor r)$.

(b) **DNF** — Tuyển của ba hội các literal: $(p \land \neg q)$, $(q \land r)$ và $(\neg p \land \neg r)$.

(c) **CNF** — Biểu thức đang ở dạng hội của hai clause $(p \lor q)$ và $(r)$. Để đưa về DNF, cần áp dụng luật phân phối thành $(p \land r) \lor (q \land r)$.

(d) **DNF** — Tuyển của hai term $p$ và $(q \land r)$ (trong đó $p$ là hội của một literal).

(e) **Không phải dạng chuẩn** — Biểu thức còn chứa phép kéo theo $\to$. Sau khi loại bỏ phép kéo theo, ta thu được $(\neg p \lor q) \land (\neg q \lor r)$, khi đó mới là CNF.

</details>


## Công cụ tương tác

Đối chiếu hai biểu thức bằng bảng chân trị và xem dạng DNF/CNF mà công cụ sinh ra để kiểm tra tương đương logic.
<div class="interactive-demo" markdown="1">
<div data-demo="truth-table-normal-form"></div>
</div>
<script src="{{ '/public/js/truth-table-normal-form.js' | relative_url }}"></script>
<script src="{{ '/public/js/explainers/exprtree-explainer.js' | relative_url }}"></script>


## Bài tập bổ sung: Sử dụng các luật logic mệnh đề (từ ccrr1_baitap1)

**Hướng dẫn chung:** Sử dụng các luật logic để rút gọn các biểu thức sau.

Một số luật thường dùng:
- De Morgan: $$\neg(P \land Q) \equiv \neg P \lor \neg Q$$
- Phân phối: $$P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)$$
- Hấp thụ: $$P \lor (P \land Q) \equiv P$$
- Rút gọn (phân phối + bù): $$P \lor (\neg P \land Q) \equiv P \lor Q$$
- Biến đổi kéo theo: $$(P \to Q) \equiv (\neg P \lor Q)$$

- **Bài tập 1:** $$\neg(p \lor \neg q) \to \neg p$$
- **Bài tập 2:** $$\neg(p \to q) \to p$$
- **Bài tập 3:** $$\neg(p \land (\neg q \land q))$$
- **Bài tập 4:** $$(p \lor q) \land \neg(\neg p \land q)$$

---

## Xem thêm / Video gợi ý

- [Logical Equivalences ](https://www.youtube.com/watch?v=FMc7pZbvWKA) — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist, very structured)

---

## Tóm tắt

Tương đương logic cho phép biến đổi biểu thức mà không làm thay đổi ý nghĩa. Các luật De Morgan, phân phối, bù và đồng nhất được sử dụng thường xuyên trong lập trình và kiểm chứng.

DNF và CNF là hai dạng chuẩn tắc quan trọng:
- **DNF (Disjunctive Normal Form)**: tuyển của các hội literal — thường dùng trong các hệ quy tắc và biểu diễn vùng chân trị đúng.
- **CNF (Conjunctive Normal Form)**: hội của các tuyển literal — dùng trong phép giải (resolution), bộ giải SAT và kiểm chứng phần cứng.

Khả năng đưa biểu thức về dạng chuẩn là kỹ năng nền tảng cho trí tuệ nhân tạo, tối ưu truy vấn cơ sở dữ liệu và kiểm chứng hình thức.

Trong bài tiếp theo, chúng ta sẽ học **quy tắc suy diễn** — các mẫu lập luận hợp lệ đi từ tiền đề đến kết luận.



## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=ROgJE-_BC4M">#002 TOÁN RỜI RẠC Chứng minh hai mệnh đề là tương đương logic</a> — Đỗ Văn Đức - ĐH GTVT, tiếng Việt. Hướng dẫn cách chứng minh hai mệnh đề tương đương logic.
- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc, tiếng Anh. Trình bày các luật tương đương và cách kiểm chứng bằng bảng chân trị.
- <a href="https://www.youtube.com/watch?v=2cgHa02s_SA">Conjunctive Normal Form (CNF) and Disjunctive Normal Form (DNF)</a> — TrevTutor, tiếng Anh. Hướng dẫn đưa công thức về dạng chuẩn tắc DNF và CNF.
