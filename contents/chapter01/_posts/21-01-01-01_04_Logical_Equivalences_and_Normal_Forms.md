---
layout: post
title: "Tương đương Logic và Các Dạng Chuẩn tắc"
categories: chapter01
date: 2021-01-01
order: 4
required: true
lang: en
---

Cùng một ý logic có thể được viết theo rất nhiều cách khác nhau. Một lập trình viên thích điều kiện ngắn gọn, một database engine lại muốn biểu thức dễ tối ưu, còn SAT solver hay công cụ kiểm chứng hình thức lại cần công thức ở một dạng chuẩn để xử lý hàng triệu biến. Nhìn bề ngoài, các biểu thức này có thể khác nhau hoàn toàn — nhưng câu hỏi quan trọng là: **chúng có thật sự nói cùng một điều không?**

Đây không chỉ là câu hỏi của toán học thuần túy. Trong khoa học máy tính, khả năng biến đổi biểu thức logic một cách an toàn có ảnh hưởng rất lớn đến thực tế:

- giúp rút gọn điều kiện để code dễ đọc hơn,
- giúp tối ưu truy vấn và luật lọc trong hệ thống,
- giúp chuẩn hóa công thức cho bộ giải SAT,
- và giúp các công cụ kiểm chứng phần mềm xử lý bài toán hiệu quả hơn.

Một phép biến đổi nhỏ trên biểu thức có thể làm chương trình dễ hiểu hơn, điều kiện gọn hơn, hoặc bộ giải chạy nhanh hơn rất nhiều. Nhưng điều đó chỉ đúng khi ta biến đổi **đúng luật**. Nếu suy luận cảm tính, chỉ cần đổi sai một bước là toàn bộ ý nghĩa logic của biểu thức có thể bị phá vỡ.

Chính vì vậy, bài học này giới thiệu hai ý tưởng cực kỳ quan trọng:

- **Tương đương logic**: hai biểu thức khác hình thức nhưng giống nhau về ý nghĩa trong mọi trường hợp.
- **Dạng chuẩn tắc**: những cách viết chuẩn hóa giúp biểu thức trở nên dễ xử lý hơn đối với con người lẫn máy tính.

Trong bài này, chúng ta sẽ học cách nhận ra khi nào hai công thức thực sự tương đương, cách áp dụng các luật biến đổi cơ bản, và cách đưa biểu thức về các dạng chuẩn quen thuộc như DNF và CNF — những dạng xuất hiện rất nhiều trong logic toán, trí tuệ nhân tạo và kiểm chứng hệ thống.

### Minh họa trực quan: Hai biểu thức, một ý nghĩa

Hãy quan sát hai đoạn code sau:

```python
# Cách 1
if not (is_admin or is_active):
    deny_access()

# Cách 2  
if not is_admin and not is_active:
    deny_access()
```

Hai điều kiện này **hoàn toàn tương đương** về mặt logic, dù cú pháp khác nhau. Người đọc code dễ hiểu hơn với Cách 2, nhưng cả hai đều cho kết quả giống hệt nhau trên mọi đầu vào. Đây chính là ý nghĩa của **tương đương logic**.

## Mục tiêu học tập

Sau bài này, sinh viên có thể:

- Phát biểu chính xác khái niệm tương đương logic.
- Sử dụng các luật tương đương để rút gọn biểu thức mệnh đề.
- Chuyển đổi giữa biểu thức logic, bảng chân trị, DNF và CNF.
- Nhận ra lỗi thường gặp khi áp dụng De Morgan, kéo theo và phân phối.
- Giải thích vai trò của CNF trong SAT solver và kiểm chứng phần mềm.

## 1. Tương đương logic

**Định nghĩa**: Hai mệnh đề phức hợp $$P$$ và $$Q$$ được gọi là **tương đương logic** nếu chúng có cùng giá trị chân trị trong mọi phép gán giá trị cho các biến mệnh đề. Khi đó ta viết:

$$P \equiv Q$$

Tương đương với việc $$P \leftrightarrow Q$$ là một hằng đúng.

**Ký hiệu**:

- $$\equiv$$: tương đương logic, dùng cho quan hệ giữa hai công thức.
- $$\leftrightarrow$$: phép nối hai chiều, là một toán tử nằm trong công thức.
- $$T$$ và $$F$$: hằng đúng và hằng sai.

**Ví dụ**: Chứng minh $$p \to q \equiv \neg p \lor q$$.

| $$p$$ | $$q$$ | $$p \to q$$ | $$\neg p \lor q$$ |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

Hai cột cuối giống nhau ở mọi hàng, do đó $$p \to q \equiv \neg p \lor q$$.

### Minh họa bằng code: Kiểm tra tương đương thực tế

Thay vì chỉ nhìn bảng chân trị, ta có thể viết một đoạn code nhỏ để kiểm tra hai biểu thức có luôn cho cùng kết quả không:

```python
def check_equivalence():
    """Kiểm tra p → q ≡ ¬p ∨ q trên tất cả tổ hợp"""
    for p in [True, False]:
        for q in [True, False]:
            left = (not p) or q          # ¬p ∨ q
            right = (not p) or q         # p → q cũng viết là (not p) or q
            print(f"p={p}, q={q} → left={left}, right={right}, equal={left == right}")

check_equivalence()
# Kết quả: luôn equal = True
```

**Bài học từ ví dụ**: Khi bạn thấy một điều kiện phức tạp trong code, hãy thử viết phiên bản tương đương đơn giản hơn. Compiler và database engine cũng làm điều tương tự để tối ưu.

<div class="content-box insight-box" markdown="1">
**Ghi nhớ**: Tương đương logic là quan hệ "thay thế an toàn". Nếu $$P \equiv Q$$, ta có thể thay $$P$$ bằng $$Q$$ trong bất kỳ biểu thức lớn hơn nào mà không đổi bảng chân trị của toàn bộ biểu thức.
</div>

## 2. Các luật tương đương cơ bản

**Lưu ý**: Ký hiệu \(\equiv\) **không phải** là một phép toán logic — nó là một khẳng định về hai công thức (hai công thức này có cùng bảng chân trị).

| Tên luật | Công thức tiêu biểu | Ghi chú |
|:---|:---|:---|
| Đồng nhất | $$p \land T \equiv p$$, $$p \lor F \equiv p$$ | T và F là hằng |
| Nuốt | $$p \lor T \equiv T$$, $$p \land F \equiv F$$ | Bị "nuốt" bởi hằng |
| Lũy đẳng | $$p \lor p \equiv p$$, $$p \land p \equiv p$$ | Lặp lại không đổi |
| Phủ định kép | $$\neg\neg p \equiv p$$ | Hai lần phủ định |
| Giao hoán | $$p \lor q \equiv q \lor p$$, $$p \land q \equiv q \land p$$ | Đổi chỗ |
| Kết hợp | $$(p \lor q) \lor r \equiv p \lor (q \lor r)$$ | Dấu ngoặc không quan trọng |
| Phân phối | $$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$ | Phân phối OR qua AND |
| De Morgan | $$\neg(p \land q) \equiv \neg p \lor \neg q$$ | Phủ định của AND/OR |
| Hấp thụ | $$p \lor (p \land q) \equiv p$$ | Bị "hấp thụ" |
| Bù | $$p \lor \neg p \equiv T$$, $$p \land \neg p \equiv F$$ | Luật bù |

**Mẹo nhớ**: Các luật De Morgan, Phân phối, và Bù là những luật hay dùng nhất khi rút gọn biểu thức.

## Công thức Boolean dưới dạng cây

Một công thức Boolean có thể được biểu diễn dưới dạng **cây** (rooted tree):

- **Nút gốc và nút trong**: được gán nhãn bởi các phép toán logic (`¬`, `∧`, `∨`, `→`, `↔`, `⊕`).
- **Lá (nút cuối)**: được gán nhãn bởi các biến (`p`, `q`, `r`, ...) hoặc hằng (`T`, `F`).

Cấu trúc của cây được xác định bởi **dấu ngoặc** trong công thức.

**Ví dụ chi tiết**: Xét công thức `((p ∨ q) → ¬r) ↔ p`

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

**Bảng chân trị** của công thức này (thứ tự lexicographic, T trước F):

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

**Nhận xét**: Cây giúp ta thấy rõ **thứ tự tính toán** và **cấu trúc phân cấp** của công thức. Mỗi phép toán tương ứng với một nút trong, và các biến là lá.

![Cây quyết định — cấu trúc công thức Boolean](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

*Hình 1.16: Biểu diễn công thức Boolean dưới dạng cây — mỗi nút là một phép toán, lá là biến hoặc hằng.*

![Luật De Morgan trên biểu đồ Venn](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

*Hình 1.17: Luật De Morgan — ¬(p ∧ q) ≡ ¬p ∨ ¬q, công cụ biến đổi quan trọng nhất khi rút gọn điều kiện.*

![DNF — tổng các tích (disjunction of conjunctions)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-OR.png)

*Hình 1.18: Dạng chuẩn tắc tuyển (DNF) — tổng (OR) của các tích (AND), xây từ các hàng có kết quả Đúng trong bảng chân trị.*

![CNF — tích các tổng (conjunction of disjunctions)](/discrete-mathematics-for-computer-science-iuh/img/course/Venn-Diagram-AND.png)

*Hình 1.19: Dạng chuẩn tắc hội (CNF) — tích (AND) của các tổng (OR), dạng chuẩn mà SAT solver yêu cầu.*

**Lưu ý quan trọng**: Các phép toán `∧`, `∨`, `⊕`, `↔` là **giao hoán** (đổi chỗ được) và **kết hợp** (dấu ngoặc không quan trọng). Riêng `→` không có hai tính chất này.

Do đó ta có thể viết `R ∧ Q ∧ P` thay vì `(R ∧ Q) ∧ P`, và viết các biến theo bất kỳ thứ tự nào.

**Ứng dụng**:
- **Trình biên dịch** biểu diễn biểu thức Boolean dưới dạng cây trước khi tối ưu.
- **Kiểm chứng hình thức** thường làm việc trên cấu trúc cây của công thức.
- **Phân tích tĩnh** dùng cây biểu thức để phát hiện nhánh chết hoặc điều kiện luôn đúng/sai.

Ta chứng minh $$\neg(p \land q) \equiv \neg p \lor \neg q$$ bằng bảng chân trị.

| $$p$$ | $$q$$ | $$p \land q$$ | $$\neg(p \land q)$$ | $$\neg p$$ | $$\neg q$$ | $$\neg p \lor \neg q$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

Hai cột $$\neg(p \land q)$$ và $$\neg p \lor \neg q$$ giống nhau. Vậy luật đúng.

#### Minh họa bằng code

Luật De Morgan cũng xuất hiện liên tục khi viết điều kiện phủ định:

```python
# Vế trái: NOT (A AND B)
if not (is_admin and is_active):
    deny_access()

# Vế phải: NOT A OR NOT B — tương đương logic
if (not is_admin) or (not is_active):
    deny_access()
```

Hai điều kiện **luôn cho cùng kết quả** trên mọi đầu vào. Đây là lý do De Morgan cực kỳ quan trọng khi rút gọn biểu thức trong lập trình và tối ưu truy vấn.

## 3. Biến đổi biểu thức logic

**Ví dụ**: Rút gọn biểu thức $$\neg(p \lor \neg q) \land (r \lor \neg r)$$.

$$\begin{aligned}
\neg(p \lor \neg q) \land (r \lor \neg r)
&\equiv (\neg p \land \neg\neg q) \land T && \text{De Morgan và luật bù}\\
&\equiv (\neg p \land q) \land T && \text{phủ định kép}\\
&\equiv \neg p \land q && \text{đồng nhất.}
\end{aligned}$$

**Nhận xét**: Mỗi dòng biến đổi phải nêu rõ luật được dùng. Trong chứng minh toán học và kiểm chứng chương trình, việc ghi luật giúp phát hiện sai sót sớm.

## 4. Công thức Dạng Rút gọn (Reduced Forms)

### 4.0. Định nghĩa Dạng Rút gọn

**Định nghĩa**: Một biểu thức logic $$E$$ được gọi là **dạng rút gọn** (reduced form) nếu nó thỏa mãn đồng thời 3 điều kiện sau:

1. **Không chứa hằng số** $$T$$ hoặc $$F$$ (trừ khi biểu thức chỉ là hằng số đó).
2. **Không chứa cặp bù** (literal và phủ định của nó trong cùng một clause hoặc term).
3. **Không chứa thừa số chung** (các literal lặp lại trong cùng một clause/term, hoặc các term/clause trùng nhau).

**Ví dụ**:
- $$\neg p \land q$$ là dạng rút gọn.
- $$(\neg p \land q) \lor (\neg p \land \neg q)$$ **không** phải dạng rút gọn (có thể rút gọn thành $$\neg p$$).
- $$p \lor \neg p$$ **không** phải dạng rút gọn (cặp bù → rút gọn thành $$T$$).
- $$p \land p$$ **không** phải dạng rút gọn (thừa số → rút gọn thành $$p$$).

**Mục tiêu**: Tìm dạng rút gọn ngắn nhất (ít literal nhất) tương đương với biểu thức ban đầu.

### 4.1. Vì sao cần rút gọn?

Một biểu thức logic có thể viết bằng rất nhiều cách khác nhau — nhưng không phải cách nào cũng tiện lợi. Trong thực tế, biểu thức dài thường đồng nghĩa với:

- **Code khó đọc**: `if ((a && b) || (a && !b))` làm người đọc phải dừng lại suy nghĩ.
- **Truy vấn nặng hơn**: nhiều điều kiện lồng nhau khiến database engine khó tối ưu.
- **Xử lý chậm hơn**: nhiều phép toán hơn → nhiều thời gian CPU hơn.

**Bài toán rút gọn**: Cho một biểu thức logic, tìm biểu thức **ngắn nhất có thể** mà vẫn tương đương logic với biểu thức ban đầu.

### 4.2. Rút gọn bằng Luật Tương đương

Các luật tương đương ở Section 2 là công cụ chính để rút gọn. Chiến lược chung:

1. **Loại bỏ kéo theo**: thay $$p \to q$$ bằng $$\neg p \lor q$$.
2. **Áp dụng De Morgan** để đẩy phủ định vào sâu bên trong.
3. **Phân phối** và **gộp** các thành phần giống nhau.
4. **Loại bỏ hằng số** bằng luật đồng nhất, nuốt, bù.

**Ví dụ 1**: Rút gọn $$(\neg p \land q) \lor (\neg p \land \neg q)$$.

$$\begin{aligned}
(\neg p \land q) \lor (\neg p \land \neg q)
&\equiv \neg p \land (q \lor \neg q) && \text{(phân phối)} \\
&\equiv \neg p \land T && \text{(luật bù)} \\
&\equiv \neg p && \text{(đồng nhất)}.
\end{aligned}$$

**Ví dụ 2 (tối ưu điều kiện trong code)**:

```python
# Biểu thức gốc
if (x > 0 and y > 0) or (x > 0 and y <= 0):
    do_something()

# Sau rút gọn: x > 0
if x > 0:
    do_something()
```

Điều kiện đầu tương đương $$(p \land q) \lor (p \land \neg q)$$ với $$p = (x > 0)$$ và $$q = (y > 0)$$, và ta đã biết nó rút gọn thành $$p$$.

**Quan sát chính**: Hai hội $$p \land q$$ và $$p \land \neg q$$ chỉ khác nhau ở một literal ($$q$$ và $$\neg q$$). Khi gặp cặp như vậy, ta luôn gộp được thành $$p$$ (mất biến $$q$$). Đây là ý tưởng nền tảng của mọi thuật toán rút gọn: **phát hiện các cặp chỉ khác nhau một literal và gộp chúng**.

## 5. Dạng chuẩn tắc tuyển DNF

**Định nghĩa**: **Dạng chuẩn tắc tuyển** (Disjunctive Normal Form, DNF) là biểu thức có dạng tuyển của các hội, trong đó mỗi thành phần nhỏ là một literal hoặc phủ định của literal:

$$(l_{11} \land l_{12} \land \cdots) \lor (l_{21} \land l_{22} \land \cdots) \lor \cdots$$

**Ví dụ**: $$(p \land q) \lor (\neg p \land r)$$ là DNF.

### Tạo DNF từ bảng chân trị (cách trực quan)

Hãy làm theo **3 bước đơn giản**:

1. **Nhìn vào bảng chân trị**, chỉ quan tâm đến những hàng có kết quả **TRUE**.
2. **Với mỗi hàng TRUE**, viết một hội (AND) mô tả đúng hàng đó:
   - Nếu biến là `TRUE` → giữ nguyên biến.
   - Nếu biến là `FALSE` → lấy phủ định của biến.
3. **Lấy tuyển (OR)** của tất cả các hội vừa tạo.

**Ví dụ**: Xây dựng DNF cho $$p \to q$$

Bảng chân trị:

| $$p$$ | $$q$$ | $$p \to q$$ |
|:---:|:---:|:---:|
| T | T | **T** |
| T | F | F |
| F | T | **T** |
| F | F | **T** |

**Bước 1 & 2**: Chỉ giữ 3 hàng TRUE:

- Hàng 1 (`T, T`): $$p \land q$$
- Hàng 3 (`F, T`): $$\neg p \land q$$
- Hàng 4 (`F, F`): $$\neg p \land \neg q$$

**Bước 3**: Lấy tuyển:

$$
(p \land q) \lor (\neg p \land q) \lor (\neg p \land \neg q)
$$

Đây chính là **DNF đầy đủ** của $$p \to q$$.

#### Minh họa trực quan: DNF như một "bản đồ vùng đúng"

Hãy tưởng tượng bảng chân trị là một lưới 2×2 (với 2 biến). Mỗi ô tương ứng với một assignment:

- DNF đầy đủ chính là **tô màu tất cả các ô đúng**, mỗi ô được tô bằng một "hình chữ nhật nhỏ" (một term).
- Khi rút gọn, ta **gộp các ô liền kề** thành một hình chữ nhật lớn hơn → biểu thức ngắn hơn.

Ví dụ trên, ta đang tô 3 ô, và có thể gộp thành $$\neg p \lor q$$.

Đây chính là ý tưởng đằng sau các thuật toán tối thiểu hóa biểu thức Boolean mà compiler và công cụ tối ưu truy vấn sử dụng.

## 6. Dạng chuẩn tắc hội CNF

**Định nghĩa**: **Dạng chuẩn tắc hội** (Conjunctive Normal Form, CNF) là biểu thức có dạng hội của các tuyển:

$$(l_{11} \lor l_{12} \lor \cdots) \land (l_{21} \lor l_{22} \lor \cdots) \land \cdots$$

**Ví dụ**: $$(p \lor q) \land (\neg p \lor r) \land (q \lor \neg r)$$ là CNF.

**Ký hiệu**: Mỗi ngoặc trong CNF thường được gọi là một **mệnh đề con** (clause). CNF là dạng chuẩn mà nhiều SAT solver nhận vào.

**Lưu ý**: Chúng ta thường dùng bit `1` và `0` thay cho `T` và `F`, và ký hiệu biến là \(x_1, \dots, x_n\). Ví dụ: gán \(x = 101\) vào công thức \((x_1 \land x_2 \land x_3) \lor (\neg x_1 \land \neg x_2 \land \neg x_3)\) cho kết quả `0`.

**Toán tử bitwise trên chuỗi bit**: Chúng ta có thể mở rộng các phép toán logic thành toán tử trên **chuỗi bit** bằng cách áp dụng từng bit một. Ví dụ:

- \(1010 = 0101\)
- \(1010 \land 0110 = 0010\)
- \(1010 \lor 0110 = 1110\)

### Tạo CNF từ bảng chân trị (cách trực quan)

Tương tự DNF, ta cũng có thể xây dựng CNF từ bảng chân trị theo **3 bước**:

1. **Nhìn vào bảng chân trị**, chỉ quan tâm đến những hàng có kết quả **FALSE**.
2. **Với mỗi hàng FALSE**, viết một tuyển (OR) mô tả đúng hàng đó:
   - Nếu biến là `TRUE` → lấy **phủ định** của biến.
   - Nếu biến là `FALSE` → giữ nguyên biến.
3. **Lấy hội (AND)** của tất cả các tuyển vừa tạo.

**Ví dụ**: Xây dựng CNF cho $$p \to q$$

Bảng chân trị (chỉ quan tâm hàng FALSE):

| $$p$$ | $$q$$ | $$p \to q$$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

**Bước 1 & 2**: Chỉ có 1 hàng FALSE (`T, F`):

- Biến `p = TRUE` → lấy $$\neg p$$
- Biến `q = FALSE` → giữ nguyên $$q$$

→ Viết tuyển: $$\neg p \lor q$$

**Bước 3**: Vì chỉ có 1 clause, CNF chính là:

$$
\neg p \lor q
$$

(Trong trường hợp có nhiều hàng FALSE, ta sẽ lấy **hội** của tất cả các tuyển.)

#### Minh họa: CNF như "danh sách các ràng buộc"

Hãy xem CNF dưới góc nhìn lập trình:

```python
# CNF: (p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)
# Ý nghĩa: TẤT CẢ các mệnh đề con phải đúng

def is_satisfied(p, q, r):
    clause1 = p or q
    clause2 = (not p) or r
    clause3 = q or (not r)
    return clause1 and clause2 and clause3
```

Mỗi `clause` là một ràng buộc. SAT solver phải tìm một assignment sao cho **không có ràng buộc nào bị vi phạm**. Đây là lý do CNF là dạng đầu vào tự nhiên cho hầu hết các bộ giải SAT hiện đại.

## 7. Các định lý quan trọng về DNF và CNF

### Định lý 1: Sự tồn tại DNF và CNF
**Mọi biểu thức mệnh đề đều có thể đưa về DNF và CNF.**

**Chứng minh (phác thảo)**: Từ bảng chân trị, ta luôn xây dựng được DNF bằng cách tuyển các hội tương ứng với các hàng đúng; tương tự CNF bằng hội các tuyển tương ứng với các hàng sai. Do mọi biểu thức đều có bảng chân trị hữu hạn, nên DNF/CNF luôn tồn tại.

### Định lý 2: Tính duy nhất của DNF/CNF đầy đủ

**Định nghĩa**: Một **DNF đầy đủ** (full DNF / canonical DNF) của hàm Boolean $$ f $$ trên $$ n $$ biến là biểu thức DNF trong đó **mỗi term** chứa đúng $$ n $$ literal (mỗi biến xuất hiện đúng một lần, có thể phủ định). Tương tự, **CNF đầy đủ** (full CNF) là CNF trong đó mỗi clause chứa đúng $$ n $$ literal.

**Định lý**: Mọi hàm Boolean $$ f:\{T,F\}^n\to\{T,F\} $$ đều có **đúng một** DNF đầy đủ và **đúng một** CNF đầy đủ (duy nhất, không kể thứ tự các term/clause và thứ tự literal bên trong term/clause).

**Chứng minh (Tính duy nhất của DNF đầy đủ)**:

Giả sử $$ D_1 $$ và $$ D_2 $$ là hai DNF đầy đủ cùng biểu diễn hàm $$ f $$.

1. **Mỗi term trong DNF đầy đủ tương ứng duy nhất với một assignment**:
   - Với assignment $$ \alpha = (a_1, \dots, a_n) \in \{T,F\}^n $$, ta xây dựng term:
     $$
     m_\alpha = \bigwedge_{i=1}^n \ell_i, \quad \text{trong đó } \ell_i = x_i \text{ nếu } a_i = T,\quad \ell_i = \neg x_i \text{ nếu } a_i = F.
     $$
   - Term $$ m_\alpha $$ chỉ đúng duy nhất tại assignment $$ \alpha $$, và $$ m_\alpha(\alpha) = T $$.

2. **Mối quan hệ giữa DNF đầy đủ và bảng chân trị**:
   - Giả sử $$ D_1 = m_{\alpha_1} \lor m_{\alpha_2} \lor \cdots \lor m_{\alpha_k} $$, trong đó $$ f(\alpha_j) = T $$ với mọi $$ j $$.
   - Tương tự $$ D_2 = m_{\beta_1} \lor \cdots \lor m_{\beta_m} $$.
   - Vì $$ D_1 \equiv f $$ và $$ D_2 \equiv f $$, nên tập $$ \{\alpha_1,\dots,\alpha_k\} $$ chính là tập tất cả các assignment mà $$ f = T $$. Tương tự với $$ D_2 $$.

3. **Mâu thuẫn nếu hai DNF khác nhau**:
   - Giả sử $$ D_1 \not\equiv D_2 $$ (không kể thứ tự term). Khi đó tồn tại ít nhất một assignment $$ \alpha^* $$ sao cho $$ m_{\alpha^*} $$ xuất hiện trong $$ D_1 $$ nhưng không xuất hiện trong $$ D_2 $$ (hoặc ngược lại).
   - Xét giá trị của hai DNF tại assignment $$ \alpha^* $$:
     - $$ D_1(\alpha^*) = T $$ (vì chứa term $$ m_{\alpha^*} $$ đúng tại $$ \alpha^* $$).
     - $$ D_2(\alpha^*) = F $$ (vì không chứa term nào đúng tại $$ \alpha^* $$).
   - Điều này mâu thuẫn với giả thiết $$ D_1 \equiv D_2 $$.

Do đó $$ D_1 \equiv D_2 $$.

**Chứng minh cho CNF đầy đủ**: Hoàn toàn tương tự bằng cách dual hóa (thay $$ \lor $$ bằng $$ \land $$, $$ T $$ bằng $$ F $$, và literal bằng phủ định của nó), hoặc áp dụng Định lý 3 bên dưới cho $$ \neg f $$.

**Hệ quả quan trọng**:
- DNF đầy đủ và CNF đầy đủ là **dạng chuẩn tắc** (canonical form) của hàm Boolean.
- Hai hàm Boolean bằng nhau khi và chỉ khi DNF đầy đủ (hoặc CNF đầy đủ) của chúng trùng nhau.

### Định lý 3: Mối quan hệ giữa DNF và CNF qua phủ định
**Nếu** $$P$$ **có DNF** $$(l_{11} \land l_{12} \land \cdots) \lor (l_{21} \land l_{22} \land \cdots) \lor \cdots$$, **thì** $$\neg P$$ **có CNF** $$( \neg l_{11} \lor \neg l_{12} \lor \cdots) \land ( \neg l_{21} \lor \neg l_{22} \lor \cdots) \land \cdots$$.

**Hệ quả**: Phủ định của DNF là CNF và ngược lại (áp dụng De Morgan mở rộng).

### Định lý 4: Biểu diễn hàm Boolean
**Mọi hàm Boolean** $$f: \{T,F\}^n \to \{T,F\}$$ **đều có biểu diễn DNF và CNF duy nhất** (đầy đủ).

**Ý nghĩa CS**: Đây là nền tảng của:
- **Compiler optimization**: rút gọn biểu thức Boolean trong mã nguồn và mã trung gian.
- **Query optimization**: chuẩn hóa điều kiện lọc trong SQL để database engine xử lý hiệu quả hơn.
- **SAT solver**: nhận đầu vào dạng CNF và tìm cách gán biến sao cho biểu thức đúng.

## 8. Ứng dụng trong Khoa học Máy tính

- **Tối ưu điều kiện trong chương trình**: Compiler có thể thay `not (a and b)` bằng `(not a) or (not b)` để đơn giản hóa nhánh.
- **SAT solver**: Nhiều bài toán lập lịch, kiểm chứng phần mềm, giải Sudoku và phân tích phụ thuộc được mã hóa thành CNF.
- **Cơ sở dữ liệu**: Tối ưu truy vấn SQL dùng các luật tương đương để đẩy điều kiện lọc xuống sớm hơn.

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

Bảng chân trị 8 hàng cho 3 biến cho thấy hai cột cuối luôn giống nhau ở mọi tổ hợp giá trị. Do đó hai biểu thức tương đương.

</details>

### Bài tập 2: Rút gọn biểu thức

Rút gọn biểu thức sau về dạng đơn giản nhất:

$$\neg(p \land \neg q) \lor (\neg p \land q)$$

<details>
<summary>Đáp án</summary>

Áp dụng De Morgan và các luật bù, đồng nhất:

$$\equiv (\neg p \lor q) \lor (\neg p \land q) \equiv \neg p \lor q$$

</details>

### Bài tập 3: Chuyển sang DNF và CNF

Cho biểu thức $$(p \lor q) \land (\neg p \lor r)$$.

1. Viết dạng DNF đầy đủ.
2. Viết dạng CNF (đã là CNF).

<details>
<summary>Đáp án</summary>

- DNF: $$(p \land \neg p) \lor (p \land r) \lor (q \land \neg p) \lor (q \land r)$$ (rút gọn thành $$(p \land r) \lor (q \land \neg p) \lor (q \land r)$$).
- CNF: Giữ nguyên $$(p \lor q) \land (\neg p \lor r)$$.

</details>

### Bài tập 4: Ứng dụng thực tế

Viết một đoạn mã Python kiểm tra điều kiện `not (user.is_banned() and user.is_inactive())` theo hai cách tương đương. Giải thích tại sao một trong hai cách dễ đọc và tối ưu hơn.

<details>
<summary>Đáp án</summary>

```python
if not (user.is_banned() and user.is_inactive()):
    allow_access()

# Tương đương (De Morgan)
if (not user.is_banned()) or (not user.is_inactive()):
    allow_access()
```

Cách thứ hai dễ đọc hơn và có thể tận dụng short-circuit evaluation tốt hơn trong một số trình biên dịch.

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

(a) $$\neg(p \lor \neg q) \equiv \neg p \land \neg(\neg q) \equiv \neg p \land q$$

(b) $$\neg(\neg p \land (q \lor r)) \equiv \neg(\neg p) \lor \neg(q \lor r) \equiv p \lor (\neg q \land \neg r)$$

(c) $$(\neg p \land \neg q) \lor \neg(\neg r \lor p)$$
    $$\equiv (\neg p \land \neg q) \lor (\neg(\neg r) \land \neg p)$$
    $$\equiv (\neg p \land \neg q) \lor (r \land \neg p)$$
    $$\equiv \neg p \land (\neg q \lor r)$$ (luật phân phối)

(d) $$\neg((p \land q) \lor (\neg p \land \neg q))$$
    $$\equiv \neg(p \land q) \land \neg(\neg p \land \neg q)$$
    $$\equiv (\neg p \lor \neg q) \land (p \lor q)$$
    $$\equiv (\neg p \land p) \lor (\neg p \land q) \lor (\neg q \land p) \lor (\neg q \land q)$$
    $$\equiv F \lor (\neg p \land q) \lor (p \land \neg q) \lor F$$
    $$\equiv (\neg p \land q) \lor (p \land \neg q) \equiv p \oplus q$$
    Kết luận: Biểu thức gốc tương đương với **XOR**.

(e) $$\neg(p \to q) \lor \neg(q \to p)$$
    $$\equiv \neg(\neg p \lor q) \lor \neg(\neg q \lor p)$$
    $$\equiv (p \land \neg q) \lor (q \land \neg p)$$
    $$\equiv p \oplus q$$
    Kết luận: Cũng tương đương với **XOR**!

</details>

### Bài tập 8: Kiểm tra tương đương bằng biến đổi

Không dùng bảng chân trị, hãy chứng minh các tương đương sau bằng biến đổi logic:

(a) $$p \to (q \to r) \equiv (p \land q) \to r$$
(b) $$(p \to q) \land (p \to r) \equiv p \to (q \land r)$$
(c) $$p \leftrightarrow q \equiv (p \to q) \land (q \to p)$$
(d) $$p \to (q \to p)$$ là hằng đúng

<details>
<summary>Đáp án</summary>

(a) 
    $$p \to (q \to r) \equiv \neg p \lor (\neg q \lor r) \equiv (\neg p \lor \neg q) \lor r \equiv \neg(p \land q) \lor r \equiv (p \land q) \to r$$
    Đây là luật **exportation**: điều kiện lồng nhau tương đương với điều kiện hội.

(b)
    $$(p \to q) \land (p \to r) \equiv (\neg p \lor q) \land (\neg p \lor r)$$
    $$\equiv \neg p \lor (q \land r)$$ (luật phân phối)
    $$\equiv p \to (q \land r)$$

(c) Đây là định nghĩa của tương đương:
    $$p \leftrightarrow q \equiv (p \to q) \land (q \to p)$$
    Đây chính là định nghĩa, không cần chứng minh — nhưng có thể kiểm tra bằng bảng chân trị.

(d)
    $$p \to (q \to p) \equiv \neg p \lor (\neg q \lor p) \equiv (\neg p \lor p) \lor \neg q \equiv T \lor \neg q \equiv T$$
    Vậy đây là hằng đúng (tautology). Câu nói này có nghĩa: "Nếu p đúng, thì (bất kỳ điều gì cũng kéo theo p)" — một sự thật hiển nhiên về logic.

</details>

### Bài tập 9: Chuyển đổi giữa DNF và CNF

Cho biểu thức: $$(p \land q) \lor (\neg p \land \neg q)$$

(a) Biểu thức này đã ở dạng DNF chưa? Giải thích.
(b) Chuyển sang dạng CNF.
(c) Nhận xét về ý nghĩa của biểu thức này — nó tương ứng với phép toán logic nào?

<details>
<summary>Đáp án</summary>

(a) **Đã ở dạng DNF** — DNF là tuyển của các hội. Biểu thức có dạng $$C_1 \lor C_2$$ với $$C_1 = p \land q$$ và $$C_2 = \neg p \land \neg q$$. Mỗi hội chứa đúng hai literal, mỗi biến xuất hiện đúng một lần.

(b) Chuyển sang CNF:
    $$(p \land q) \lor (\neg p \land \neg q)$$
    Phân phối: $$\equiv [(p \land q) \lor \neg p] \land [(p \land q) \lor \neg q]$$
    $$\equiv [(p \lor \neg p) \land (q \lor \neg p)] \land [(p \lor \neg q) \land (q \lor \neg q)]$$
    $$\equiv [T \land (q \lor \neg p)] \land [(p \lor \neg q) \land T]$$
    $$\equiv (q \lor \neg p) \land (p \lor \neg q)$$
    CNF: $$(\neg p \lor q) \land (p \lor \neg q)$$

(c) Biểu thức này tương đương với **$$p \leftrightarrow q$$** (tương đương). Dạng DNF nói: "hoặc cả hai cùng đúng, hoặc cả hai cùng sai". Dạng CNF nói: "nếu p thì q, và nếu q thì p" — cùng một ý nghĩa.

</details>

### Bài tập 10: Ứng dụng rút gọn biểu thức trong code

Một lập trình viên viết điều kiện phức tạp:

```python
if (user.is_active and not user.is_banned) or (user.is_active and user.has_vip):
    grant_access()
```

(a) Viết biểu thức logic cho điều kiện này.
(b) Rút gọn biểu thức bằng các luật tương đương.
(c) Viết lại code Python tối ưu hơn.
(d) Kiểm tra: với `user.is_active = True, user.is_banned = True, user.has_vip = False`, code gốc và code rút gọn có cho cùng kết quả không?

<details>
<summary>Đáp án</summary>

(a) Đặt $$a$$: "user.is_active", $$b$$: "user.is_banned", $$v$$: "user.has_vip"
    Biểu thức: $$(a \land \neg b) \lor (a \land v)$$

(b) Rút gọn:
    $$(a \land \neg b) \lor (a \land v)$$
    $$\equiv a \land (\neg b \lor v)$$ (luật phân phối)
    
    Ý nghĩa: "Người dùng đang hoạt động VÀ (không bị cấm HOẶC có VIP)".

(c) Code rút gọn:
    ```python
    if user.is_active and (not user.is_banned or user.has_vip):
        grant_access()
    ```

(d) Kiểm tra với $$a = T, b = T, v = F$$:
    - Code gốc: $$(T \land \neg T) \lor (T \land F) = (T \land F) \lor F = F \lor F = F$$
    - Code rút gọn: $$T \land (\neg T \lor F) = T \land (F \lor F) = T \land F = F$$
    Hai kết quả giống nhau (cả hai đều từ chối truy cập).

</details>

### Bài tập 11: Xác định dạng chuẩn

Cho các biểu thức sau, xác định xem biểu thức đã ở dạng DNF, CNF, cả hai, hay không phải dạng nào:

(a) $$(p \lor q) \land (\neg p \lor r)$$
(b) $$(p \land \neg q) \lor (q \land r) \lor (\neg p \land \neg r)$$
(c) $$(p \lor q) \land (r)$$
(d) $$p \lor (q \land r)$$
(e) $$(p \to q) \land (q \to r)$$

<details>
<summary>Đáp án</summary>

(a) **CNF** — Hội của các tuyển. Mỗi clause là tuyển của các literal: $$(p \lor q)$$ và $$(\neg p \lor r)$$.

(b) **DNF** — Tuyển của các hội. Mỗi term là hội của các literal: $$(p \land \neg q)$$, $$(q \land r)$$, $$(\neg p \land \neg r)$$.

(c) **Cả DNF và CNF**:
    - Là CNF: hội của hai clause: $$(p \lor q)$$ và $$(r)$$.
    - Là DNF: tuyển của hai term: $$(p \land r)$$ và $$(q \land r)$$ (nếu phân phối). Thực ra dạng hiện tại là hội của $$(p \lor q)$$ và $$r$$ nên là CNF. Muốn là DNF thì phải biến đổi.

(d) **DNF** — Tuyển của hai term: $$p$$ và $$(q \land r)$$. Lưu ý $$p$$ là hội của một literal (trường hợp đặc biệt của DNF).

(e) **Không phải dạng chuẩn** — Vì chứa $$p \to q$$ và $$q \to r$$, không phải literal. Cần loại bỏ kéo theo trước:
    $$(\neg p \lor q) \land (\neg q \lor r)$$ — lúc này là CNF.

</details>

## Bài tập bổ sung: Sử dụng các luật logic mệnh đề (từ ccrr1_baitap1)

**Hướng dẫn chung:** Sử dụng các luật logic để rút gọn biểu thức.

Ví dụ luật:
- De Morgan: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
- Phân phối: P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)
- Đồng nhất: P ∨ (P ∧ Q) ≡ P
- Bổ sung: P ∨ (¬P ∧ Q) ≡ P ∨ Q
- Tương đương: (P → Q) ↔ (¬P ∨ Q)

**Bài tập 1:** ¬(p ∨ ¬q) → ¬p

**Bài tập 2:** ¬(p → q) → p

**Bài tập 3:** ¬(p ∧ (¬q ∧ q))

**Bài tập 4:** (p ∨ q) ∧ ¬(¬p ∧ q)



