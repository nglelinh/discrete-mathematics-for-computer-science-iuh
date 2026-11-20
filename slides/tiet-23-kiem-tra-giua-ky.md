---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Kiểm tra Giữa kỳ — Ôn đề 1

**Cấu trúc rời rạc**

Tiết 23 (45 phút) — Logic + Phương pháp đếm

---

### Câu 1

Cho biểu thức logic:

$$E(p,q,r) = (p \to q) \wedge (\neg p \vee r)$$

**a)** Xác định độ ưu tiên của các phép toán trong biểu thức này.

**b)** Lập bảng chân trị đầy đủ cho $$E(p,q,r)$$.

---

### Câu 1 — Lời giải

**a)** Độ ưu tiên (giảm dần): $\neg$, rồi $\wedge$, rồi $\vee$, rồi $\to$.

Thứ tự tính: (1) $\neg p$ → (2) $p \to q$ và $\neg p \vee r$ → (3) $\wedge$.

**b)** Cột $E$: **1, 1, 1, 1, 0, 0, 0, 1** (theo $pqr$ từ 000 → 111).

| $p$ | $q$ | $r$ | $E$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | **1** |
| 0 | 0 | 1 | **1** |
| 0 | 1 | 0 | **1** |
| 0 | 1 | 1 | **1** |
| 1 | 0 | 0 | **0** |
| 1 | 0 | 1 | **0** |
| 1 | 1 | 0 | **0** |
| 1 | 1 | 1 | **1** |

*Giải thích:* $p \to q$ sai chỉ khi $p=1,q=0$; $\neg p \vee r$ sai chỉ khi $p=1,r=0$.

---

### Câu 2

Rút gọn về dạng đơn giản nhất. **Chỉ rõ luật logic** từng bước:

$$F(p,q,r) = (p \wedge q) \vee (p \wedge \neg q) \vee (\neg p \wedge r)$$

---

### Câu 2 — Lời giải

| Bước | Biểu thức | Luật |
|:----:|-----------|------|
| 1 | $(p \wedge q) \vee (p \wedge \neg q) \vee (\neg p \wedge r)$ | Cho trước |
| 2 | $p \wedge (q \vee \neg q) \vee (\neg p \wedge r)$ | Phân phối |
| 3 | $p \vee (\neg p \wedge r)$ | Bù + đơn giản |
| 4 | $p \vee r$ | Phân phối / hấp thụ |

**Đáp án:** $F(p,q,r) \equiv p \vee r$

---

Miền $X$: các modules trong hệ thống. Vị từ:

- $T(x)$: module $x$ đã được kiểm thử
- $B(x)$: module $x$ có lỗi (bug)
- $P(x)$: module $x$ đang production

**a)** Ký hiệu vị từ + lượng từ:

i. Tồn tại ít nhất một module có lỗi chưa được kiểm thử.

ii. Mọi module đưa vào sản xuất đều không có lỗi.

**b)** Phủ định đầy đủ của (a) ii và dịch ra tiếng Việt.

---

### Câu 3 — Lời giải

**a)**

i. $\exists x\,(B(x) \wedge \neg T(x))$

ii. $\forall x\,(P(x) \to \neg B(x))$

**b)** Phủ định của (ii):

$$\exists x\,(P(x) \wedge B(x))$$

*Dịch:* “Tồn tại ít nhất một module đang production **và** có lỗi.”

*Giải thích:* $\neg\forall x\,(P\to\neg B) \equiv \exists x\,(P \wedge B)$  
(vì $\neg(A\to B) \equiv A \wedge \neg B$ và $\neg\neg B \equiv B$).

---

### Câu 4

Kiểm tra tính đúng đắn. Nếu đúng: chứng minh bằng quy tắc suy diễn  
(Modus Ponens, Tam đoạn luận, …). Nếu sai: đưa phản ví dụ.

1. $b \to t$ (Build thành công $\Rightarrow$ chạy được test)
2. $t \to d$ (Chạy được test $\Rightarrow$ được phép deploy)
3. $b$ (Build thành công)
4. $\therefore d$ (Được phép deploy)

---

### Câu 4 — Lời giải

**Suy luận ĐÚNG.**

**Chứng minh (cách 1 — hai lần Modus Ponens):**

1. Từ (1) $b \to t$ và (3) $b$: **MP** $\Rightarrow t$
2. Từ (2) $t \to d$ và $t$: **MP** $\Rightarrow d$

**Cách 2 — Tam đoạn luận + MP:**

1. Từ (1) và (2): **Tam đoạn luận** $\Rightarrow b \to d$
2. Từ $b \to d$ và (3) $b$: **MP** $\Rightarrow d$

*Giải thích:* cả ba tiền đề đều được dùng; ngữ cảnh CI/CD hợp lý (build → test → deploy).

---

## Phần II — Phương pháp đếm

Câu 5–11: tập hợp, nguyên lý nhân, Dirichlet, bao hàm–loại trừ, tổ hợp (lặp), nhị thức Newton.

---

### Câu 5

Tập vũ trụ $U = \{1,2,3,4,5,6,7,8\}$.  
$A$ = tập các số **chẵn** trong $U$.

**a)** Xác định $\mathcal{P}(A)$ và $|\mathcal{P}(A)|$.

**b)** Tập $B$ có bit vector `10110001` (thứ tự tăng dần phần tử $U$).  
Liệt kê $A \cap B$.

---

### Câu 5 — Lời giải

**a)** $A = \{2,4,6,8\}$, $|A| = 4$

$$|\mathcal{P}(A)| = 2^{4} = 16$$

*(Không bắt buộc liệt kê đủ 16 tập con.)*

**b)** Bit vector `10110001` $\Leftrightarrow$ $B = \{1,3,4,8\}$

$$A \cap B = \{4, 8\}$$

*Giải thích bit vector:* vị trí $i$ = 1 $\Leftrightarrow$ phần tử thứ $i$ của $U$ thuộc $B$.

---

### Câu 6

Product ID gồm **5 ký tự**, loại I hoặc E (được lặp ký tự):

- **Internal (I):** 2 chữ cái (A–Z) + 3 chữ số (0–9)
- **External (E):** 5 chữ số (0–9)

**a)** Số lượng Internal ID tối đa?

**b)** Tổng số ID tối đa (cả I và E)?

---

### Câu 6 — Lời giải

**Nguyên lý nhân** (lựa chọn độc lập, có lặp):

**a)** Internal: $26 \times 26 \times 10 \times 10 \times 10 = 26^{2} \times 10^{3}$

$$= 676 \times 1000 = \mathbf{676\,000}$$

**b)** External: $10^{5} = 100\,000$

Tổng (I hoặc E — **nguyên lý cộng**):

$$676\,000 + 100\,000 = \mathbf{776\,000}$$

---

### Câu 7

Phân phối **100 packets** đến **15 routers**.

**a)** Theo Dirichlet: kết luận gì về số packets **tối thiểu** phải do **cùng một** router xử lý? (Công thức + tính.)

**b)** 100 packets gửi trong **5 phút (300 giây)**. Chứng minh: có **ít nhất một giây** nhận **ít nhất 1** packet.

---

### Câu 7 — Lời giải

**a)** Bồ câu = 100 packets, chuồng = 15 routers:

$$\left\lceil \frac{100}{15} \right\rceil = 7$$

$\Rightarrow$ **ít nhất một router** xử lý **tối thiểu 7** packets.

**b)** Bồ câu = 100 packets, chuồng = 300 giây:

$$\left\lceil \frac{100}{300} \right\rceil = 1$$

$\Rightarrow$ **ít nhất một giây** nhận **ít nhất 1** packet.

*Giải thích:* nguyên lý Dirichlet (mạnh): $\lceil n/k \rceil$ là cận dưới cho “nhiều nhất trong một chuồng”.

---

### Câu 8

Khảo sát 100 SV: Python $P$, Java $J$, C++ $C$

- $|P|=50$, $|J|=40$, $|C|=30$
- $|P \cap J|=20$, $|P \cap C|=15$, $|J \cap C|=10$
- $|P \cap J \cap C|=5$

**a)** Số SV biết **đúng một** trong 3 ngôn ngữ?

**b)** Số SV **không biết** ngôn ngữ nào trong 3 loại?

---

### Câu 8 — Lời giải

**a)** Chỉ một ngôn ngữ (trừ hai giao, cộng lại giao ba):

- Chỉ $P$: $50 - 20 - 15 + 5 = 20$
- Chỉ $J$: $40 - 20 - 10 + 5 = 15$
- Chỉ $C$: $30 - 15 - 10 + 5 = 10$

Tổng: $20 + 15 + 10 = \mathbf{45}$

**b)** Bao hàm–loại trừ:

$$|P \cup J \cup C| = 50+40+30 - 20-15-10 + 5 = 80$$

Không biết ngôn ngữ nào: $100 - 80 = \mathbf{20}$

---

### Câu 9

Chọn nhóm dự án **5** người từ **12** lập trình viên:  
**5 Senior (S)** và **7 Junior (J)**.

Có bao nhiêu cách chọn sao cho nhóm có **ít nhất 1 Senior**?

---

### Câu 9 — Lời giải (bù trừ)

**Cách 1 — Bù trừ** (nhanh):

$$\binom{12}{5} - \binom{7}{5} = 792 - 21 = \mathbf{771}$$

- $\binom{12}{5}$: mọi nhóm 5 người (không điều kiện)
- $\binom{7}{5}$: nhóm **0 Senior** (toàn 5 Junior) — loại bỏ

*“Ít nhất 1 Senior” = tổng − “không có Senior”.*

---

### Câu 9 — Lời giải (liệt kê)

**Cách 2 — Liệt kê theo số Senior $k$.**

Nhóm 5 người: chọn $k$ Senior và $5-k$ Junior, với $k \geq 1$.

$$k \in \{1,2,3,4,5\}, \quad \binom{5}{k}\binom{7}{5-k}$$

---

| $k$ (S) | Junior | Công thức | Giá trị |
|:-------:|:------:|-----------|--------:|
| 1 | 4 | $\binom{5}{1}\binom{7}{4}$ | $5 \times 35 = 175$ |
| 2 | 3 | $\binom{5}{2}\binom{7}{3}$ | $10 \times 35 = 350$ |
| 3 | 2 | $\binom{5}{3}\binom{7}{2}$ | $10 \times 21 = 210$ |
| 4 | 1 | $\binom{5}{4}\binom{7}{1}$ | $5 \times 7 = 35$ |
| 5 | 0 | $\binom{5}{5}\binom{7}{0}$ | $1 \times 1 = 1$ |

Tổng: $175 + 350 + 210 + 35 + 1 = \mathbf{771}$ *(trùng bù trừ)*.

*Giải thích:* mỗi dòng là **nguyên lý nhân** (chọn S rồi chọn J); các dòng **rời nhau** (khác số S) nên cộng lại — **nguyên lý cộng**. Không có $k=0$ vì yêu cầu **ít nhất 1** Senior.

---

### Câu 10

4 loại topping: Cherry (C), Kẹo dẻo (K), Hạt (H), Socola (S).

**a)** Chọn **7** muỗng, **có lặp**, **không xét thứ tự**. Bao nhiêu cách?

**b)** Phải có **ít nhất 1** muỗng C và **ít nhất 1** muỗng S. Bao nhiêu cách?

---

### Câu 10 — Lời giải

**Tổ hợp lặp** (stars and bars): số nghiệm không âm $x_1+\cdots+x_k = n$ là $\binom{n+k-1}{n}$.

**a)** $n=7$, $k=4$:

$$\binom{7+4-1}{7} = \binom{10}{7} = \mathbf{120}$$

**b)** Đặt trước 1C + 1S; còn 5 muỗng tự do từ 4 loại:

$$\binom{5+4-1}{5} = \binom{8}{5} = \mathbf{56}$$

---

### Câu 11

Dùng **định lý nhị thức Newton**:

$$(x+y)^{n} = \sum_{k=0}^{n}\binom{n}{k} x^{n-k} y^{k}$$

**a)** Tìm **hệ số** của $x^{3} y^{2}$ trong khai triển $(2x - y)^{5}$.

**b)** Tính $\displaystyle\sum_{k=0}^{6}\binom{6}{k}$.

---

### Câu 11 — Lời giải

**a)** Viết $(2x - y)^{5} = (2x + (-y))^{5}$.

Hạng tử chứa $x^{3} y^{2}$ ứng với $k=2$ (lấy $(-y)$ đúng 2 lần):

$$\binom{5}{2}\, (2)^{3}\, (-1)^{2} = 10 \cdot 8 \cdot 1 = \mathbf{80}$$

*Giải thích:* công thức tổng quát — hệ số $x^{a} y^{b}$ trong $(\alpha x + \beta y)^{n}$ ($a+b=n$) là $\binom{n}{b}\,\alpha^{a}\,\beta^{b}$.

**b)** Thế $x=y=1$ vào $(x+y)^{6}$:

$$\sum_{k=0}^{6}\binom{6}{k} = (1+1)^{6} = 2^{6} = \mathbf{64}$$

---

## Tóm tắt công thức ôn nhanh

| Chủ đề | Gợi nhớ |
|--------|---------|
| Logic | Ưu tiên ¬ ∧ ∨ →; luật phân phối, bù |
| Vị từ | $\neg\forall \equiv \exists\neg$; $\neg(A\to B)\equiv A\wedge\neg B$ |
| Suy diễn | MP: $p\to q$, $p$ $\Rightarrow$ $q$ |
| Tập / bit | $\|\mathcal{P}(A)\|=2^{\|A\|}$ |
| Đếm | Nhân · Cộng · $\lceil n/k\rceil$ · PIE |
| Tổ hợp | $\binom{n}{k}$; lặp: $\binom{n+k-1}{n}$ |
| Nhị thức | $(x+y)^{n}=\sum\binom{n}{k}x^{n-k}y^{k}$; $\sum\binom{n}{k}=2^{n}$ |

---

## Hết tiết

**Nguồn đầy đủ:** `material/2025_CTRR_GiuaKy_De1_01102025.pdf`  
**Đáp án chi tiết:** `material/2025_CTRR_GiuaKy_De1_01102025_DapAn.pdf`

Tiết sau: **Hệ thức truy hồi** (tiết 24).

---

## Câu hỏi?
