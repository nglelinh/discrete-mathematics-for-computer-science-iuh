---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Tương đương & Thứ tự Bộ phận

**Toán Rời Rạc**

Tiết 12 (45 phút) — Equivalence & Partial Order

---

## Mục tiêu tiết học

- Định nghĩa quan hệ tương đương và lớp tương đương
- Hiểu định lý: tương đương ⇔ phân hoạch (partition)
- Định nghĩa thứ tự bộ phận (partial order) và poset
- Vẽ và đọc biểu đồ Hasse
- Nhận biết min, max, cực tiểu, cực đại; ứng dụng CNTT

---

## Quan hệ Tương đương

**Định nghĩa**: $$R$$ trên $$A$$ là **quan hệ tương đương** nếu thỏa:

1. **Phản xạ**: $$\forall a,\; aRa$$
2. **Đối xứng**: $$aRb \Rightarrow bRa$$
3. **Bắc cầu**: $$aRb \land bRc \Rightarrow aRc$$

**Ký hiệu**: thường viết $$a \sim b$$ thay cho $$(a,b) \in R$$.

**Ý nghĩa**: Gom các phần tử "giống nhau" theo một tiêu chí.

---

## Ví dụ: Đồng dư modulo $$n$$

Trên $$\mathbb{Z}$$: $$a \equiv b \pmod{n} \Leftrightarrow n \mid (a-b)$$

**Chứng minh tương đương**:
- Phản xạ: $$a-a=0$$ chia hết cho $$n$$
- Đối xứng: $$n \mid (a-b) \Rightarrow n \mid (b-a)$$
- Bắc cầu: $$n \mid (a-b)$$ và $$n \mid (b-c) \Rightarrow n \mid (a-c)$$

**CS**: Hash bucket — hai key cùng bucket ≈ cùng lớp tương đương.

---

## Lớp tương đương

Với quan hệ tương đương $$\sim$$ trên $$A$$:

**Lớp tương đương** của $$a$$:
$$[a] = \{x \in A \mid x \sim a\}$$

**Ví dụ** (modulo 3 trên $$\mathbb{Z}$$):
- $$[0] = \{\ldots,-6,-3,0,3,6,\ldots\}$$
- $$[1] = \{\ldots,-5,-2,1,4,7,\ldots\}$$
- $$[2] = \{\ldots,-4,-1,2,5,8,\ldots\}$$

---

## Phân hoạch (Partition)

**Phân hoạch** của $$A$$: họ $$\{A_i\}$$ các tập con **không rỗng**, **đôi một rời**, hợp = $$A$$.

**Định lý** (tương đương ⇔ phân hoạch):
- Mỗi quan hệ tương đương tạo phân hoạch các lớp $$[a]$$
- Mỗi phân hoạch $$\{A_i\}$$ xác định quan hệ: $$aRb \Leftrightarrow a,b$$ cùng một $$A_i$$

**Hệ quả**: $$[a] \cap [b] \neq \emptyset \Rightarrow [a]=[b]$$.

---

## Ứng dụng Tương đương

- **Modular arithmetic**: lớp số dư khi chia cho $$n$$
- **Phân loại dữ liệu**: GPA, nhóm người dùng cùng vai trò
- **Union-Find**: quản lý thành phần liên thông (đồ thị)
- **Type equivalence** (compiler): biểu thức cùng kiểu

---

## Thứ tự Bộ phận (Partial Order)

**Định nghĩa**: $$R$$ trên $$A$$ là **thứ tự bộ phận** nếu:

1. **Phản xạ**: $$aRa$$
2. **Phản đối xứng**: $$aRb \land bRa \Rightarrow a=b$$
3. **Bắc cầu**: $$aRb \land bRc \Rightarrow aRc$$

Cặp $$(A, R)$$ gọi là **poset** (partially ordered set).

**Ký hiệu phổ biến**: $$\preceq$$ hoặc $$\subseteq$$.

---

## Ví dụ Partial Order

- $$(\mathcal{P}(S), \subseteq)$$: tập con theo quan hệ ⊆
- $$(\mathbb{N}, \mid)$$: chia hết trên số tự nhiên
- **Dependency**: module $$A$$ phải build trước $$B$$ (nếu không có vòng)

**Không so sánh được**: Với $$S=\{a,b\}$$, $$\{a\}$$ và $$\{b\}$$ không ⊆ lẫn nhau.

Đó là lý do gọi **bộ phận** (partial), không phải toàn phần.

---

## Thứ tự Toàn phần vs Bộ phận

**Thứ tự toàn phần** (total/linear order):
$$\forall a,b \in A,\; aRb \lor bRa$$

**Ví dụ**: $$(\mathbb{R}, \le)$$ — mọi cặp đều so sánh được.

**Partial order**: có thể tồn tại $$a, b$$ **không so sánh** ($$a \not\preceq b$$ và $$b \not\preceq a$$).

**CS**: Topological sort chỉ áp dụng khi DAG (không chu trình) — poset hữu hạn.

---

## Biểu đồ Hasse

**Hasse diagram** = vẽ poset đã **đơn giản hóa**:

1. Bỏ vòng phản xạ (mỗi đỉnh tự $$\preceq$$ chính nó)
2. Bỏ cạnh **suy ra** từ bắc cầu (chỉ giữ **cạnh phủ** — cover)
3. Vẽ phần tử **lớn hơn** ở **phía trên**

**Ví dụ**: Ước của 12 theo $$\mid$$: $$\{1,2,3,4,6,12\}$$.

Cạnh phủ: $$1 \prec 2$$, $$1 \prec 3$$, $$2 \prec 4$$, $$2 \prec 6$$, ...

---

## Lớp, đại diện, tập thương

$$[a]_R = \{b \in A \mid bRa\}$$

- Mỗi $$x \in [a]_R$$ là **đại diện** của lớp
- **Tập thương** $$A/R = \{[a]_R \mid a \in A\}$$
- Đồng dư modulo $$m$$: $$\mathbb{Z}_m = \{[0]_m,\ldots,[m-1]_m\}$$

**Mệnh đề**: $$aRb \Leftrightarrow [a]=[b] \Leftrightarrow [a]\cap[b]\neq\emptyset$$

---

## Min, Max (toàn cục)

Trong poset $$(S, \preceq)$$:

- **Min** (nhỏ nhất): $$a \preceq x$$ với **mọi** $$x$$ — nếu có thì **duy nhất**
- **Max** (lớn nhất): $$x \preceq a$$ với **mọi** $$x$$ — nếu có thì **duy nhất**

**Ví dụ**:
- $$(\mathcal{P}(B),\subseteq)$$: $$\min=\emptyset$$, $$\max=B$$
- $$\{x\in\mathbb{R}: x^2<100\}$$ với $$\le$$: **không** có min/max

---

## Tối tiểu & Tối đại (cục bộ)

- **Tối tiểu** (minimal): không có $$x \neq a$$ với $$x \preceq a$$
- **Tối đại** (maximal): không có $$x \neq a$$ với $$a \preceq x$$

**Khác min/max**:
- Có thể có **nhiều** tối tiểu / tối đại
- Min (nếu có) = tối tiểu **duy nhất**

**Trên Hasse**: tối tiểu = không cạnh xuống; tối đại = không cạnh lên

---

## Ví dụ: chia hết

Poset $$(\{2,4,5,10,12,20,25\}, \mid)$$:

| | Phần tử |
|:---|:---|
| Tối tiểu | $$2$$, $$5$$ |
| Tối đại | $$12$$, $$20$$, $$25$$ |
| Min / Max | **không có** |

$$4$$ và $$5$$ **không so sánh được**.

Poset hữu hạn ≠ ∅ luôn có ≥ 1 tối tiểu và ≥ 1 tối đại.

---

## Thứ tự tốt (Well-order)

$$(S,\preceq)$$ **sắp tốt** nếu mọi tập con ≠ ∅ đều có **min**.

| Poset | Sắp tốt? |
|:---|:---|
| $$(\mathbb{N},\le)$$ | ✅ |
| $$(\mathbb{Z},\le)$$ | ❌ ($$\mathbb{Z}$$ không có min) |

**CS**: chứng minh thuật toán dừng bằng measure trên $$\mathbb{N}$$.

---

## Thứ tự từ điển

Trên chuỗi bit $$\{0,1\}^n$$:

- **Product order**: $$a\le b$$ khi $$a_i\le b_i$$ mọi $$i$$ → thường **bộ phận**  
  ($$01$$  conf  $$10$$)
- **Từ điển (lex)**: so sánh bit khác nhau **đầu tiên** → **toàn phần**  
  (= thứ tự số nhị phân / `strcmp`)

**CS**: `sort`, trie, so sánh khóa.

---

## Ứng dụng Thứ tự trong CNTT

- **Build system / CI**: poset task → topological sort
- **Permission lattice**: quyền bao hàm theo ⊆
- **Version control**: commit DAG, merge theo tổ tiên
- **Scheduler**: ưu tiên job theo thứ tự phụ thuộc
- **Well-order**: foundation cho induction / termination

---

## Thực hành 1

Trên $$A=\{1,2,\ldots,10\}$$, quan hệ $$aRb \Leftrightarrow$$ "cùng số dư khi chia 5".

1. Chứng minh $$R$$ là tương đương
2. Liệt kê các lớp; viết $$A/R$$
3. Kiểm tra đây là phân hoạch của $$A$$

---

## Thực hành 2

Cho $$S=\{a,b,c\}$$, poset $$(\mathcal{P}(S), \subseteq)$$.

1. Liệt kê 8 tập con; vẽ **Hasse**
2. Tìm tối tiểu, tối đại, min, max
3. $$\{a\}$$ và $$\{b\}$$ so sánh được không?

---

## Thực hành 3

Poset $$(\{2,4,5,10,12,20,25\}, \mid)$$.

1. Vẽ Hasse (phác)
2. Tối tiểu / tối đại / min / max?
3. $$(\mathbb{N},\le)$$ vs $$(\mathbb{Z},\le)$$: cái nào sắp tốt?

---

## Tóm tắt Tiết 12

- **Tương đương** → lớp + tập thương $$A/R$$ + phân hoạch
- **Partial order** → poset; **toàn phần** nếu mọi cặp so sánh được
- **Hasse**: chỉ cạnh phủ
- **Min/max** ≠ **tối tiểu/tối đại**
- **Well-order**: $$(\mathbb{N},\le)$$ có; **lex** trên bit = toàn phần
- Tương đương **gom**; thứ tự **sắp xếp / phụ thuộc**

---

## Bài tập ôn tập (1/2)

1. **Bài 1**: Chứng minh "cùng chiều cao (làm tròn mét)" trên tập người là tương đương. Mô tả các lớp.

2. **Bài 2**: Cho phân hoạch $$A=\{1,2,3,4\}$$ thành $$\{1,4\}$$ và $$\{2,3\}$$. Viết quan hệ tương đương tương ứng.

3. **Bài 3**: Vẽ Hasse cho $$(\{1,2,3,4\}, \mid)$$. Tìm tối tiểu, tối đại.

---

## Bài tập ôn tập (2/2)

4. **Bài 4**: Poset $$(\{2,4,5,10,12,20,25\},\mid)$$ — liệt kê tối tiểu/tối đại; có min không?

5. **Bài 5**: Trên $$\{0,1\}^3$$, nêu product order vs lex; tại sao topo sort cần partial order (không bắt buộc total)?
