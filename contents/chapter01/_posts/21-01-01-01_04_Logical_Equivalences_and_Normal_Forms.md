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
- giúp thiết kế mạch logic,
- và giúp các công cụ kiểm chứng phần mềm xử lý bài toán hiệu quả hơn.

Một phép biến đổi nhỏ trên biểu thức có thể làm chương trình dễ hiểu hơn, mạch logic gọn hơn, hoặc bộ giải chạy nhanh hơn rất nhiều. Nhưng điều đó chỉ đúng khi ta biến đổi **đúng luật**. Nếu suy luận cảm tính, chỉ cần đổi sai một bước là toàn bộ ý nghĩa logic của biểu thức có thể bị phá vỡ.

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

**Lưu ý quan trọng**: Các phép toán `∧`, `∨`, `⊕`, `↔` là **giao hoán** (đổi chỗ được) và **kết hợp** (dấu ngoặc không quan trọng). Riêng `→` không có hai tính chất này.

Do đó ta có thể viết `R ∧ Q ∧ P` thay vì `(R ∧ Q) ∧ P`, và viết các biến theo bất kỳ thứ tự nào.

**Ứng dụng**:
- **Trình biên dịch** biểu diễn biểu thức Boolean dưới dạng cây trước khi tối ưu.
- **Mạch logic** trong phần cứng chính là cây Boolean (mỗi cổng là một nút).
- **Kiểm chứng hình thức** thường làm việc trên cấu trúc cây của công thức.

Ta chứng minh $$\neg(p \land q) \equiv \neg p \lor \neg q$$ bằng bảng chân trị.

| $$p$$ | $$q$$ | $$p \land q$$ | $$\neg(p \land q)$$ | $$\neg p$$ | $$\neg q$$ | $$\neg p \lor \neg q$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

Hai cột $$\neg(p \land q)$$ và $$\neg p \lor \neg q$$ giống nhau. Vậy luật đúng.

#### Minh họa bằng mạch logic

Luật De Morgan có ý nghĩa rất trực quan khi ta vẽ **mạch logic**:

- **Vế trái** `NOT (A AND B)`: một cổng AND rồi đảo ngược đầu ra.
- **Vế phải** `NOT A OR NOT B`: hai cổng NOT riêng biệt, rồi cho vào cổng OR.

Hai mạch này **luôn cho cùng kết quả** trên mọi đầu vào. Đây là lý do De Morgan cực kỳ quan trọng trong thiết kế mạch số và tối ưu phần cứng.

## 3. Biến đổi biểu thức logic

**Ví dụ**: Rút gọn biểu thức $$\neg(p \lor \neg q) \land (r \lor \neg r)$$.

$$\begin{aligned}
\neg(p \lor \neg q) \land (r \lor \neg r)
&\equiv (\neg p \land \neg\neg q) \land T && \text{De Morgan và luật bù}\\
&\equiv (\neg p \land q) \land T && \text{phủ định kép}\\
&\equiv \neg p \land q && \text{đồng nhất.}
\end{aligned}$$

**Nhận xét**: Mỗi dòng biến đổi phải nêu rõ luật được dùng. Trong chứng minh toán học và kiểm chứng chương trình, việc ghi luật giúp phát hiện sai sót sớm.

## 4. Dạng chuẩn tắc tuyển DNF

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

Đây chính là ý tưởng đằng sau các thuật toán tối thiểu hóa logic (Karnaugh map, Espresso, Quine–McCluskey) mà compiler và công cụ thiết kế mạch sử dụng.

## 5. Dạng chuẩn tắc hội CNF

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

## 6. Các định lý quan trọng về DNF và CNF

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
- **Bảng LUT** (Look-Up Table) trong FPGA: mỗi hàm Boolean được lưu dưới dạng DNF/CNF.
- **Thuật toán tối thiểu hóa logic** (Quine–McCluskey, Espresso): rút gọn DNF/CNF để giảm số cổng logic.
- **SAT solver**: nhận đầu vào dạng CNF và tìm cách gán biến sao cho biểu thức đúng.

## 7. Công cụ tương tác

<div class="interactive-tool" data-tool="truth-table-normal-form">
  <p><strong>Demo đề xuất:</strong> nhập một biểu thức như <code>(p -> q) and (q -> r)</code>, công cụ sinh bảng chân trị, DNF và CNF tương ứng.</p>
</div>

<script src="{{ '/public/js/truth-table-normal-form.js' | relative_url }}"></script>

## 8. Ứng dụng trong Khoa học Máy tính

- **Tối ưu điều kiện trong chương trình**: Compiler có thể thay `not (a and b)` bằng `(not a) or (not b)` để đơn giản hóa nhánh.
- **Mạch số**: Cổng AND, OR, NOT tương ứng trực tiếp với hội, tuyển, phủ định.
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


