---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Dạng Chuẩn tắc

**Toán Rời Rạc — IUH**

Tiết 4 (45 phút)

---

# Mục tiêu tiết học

- Ôn tập & mô hình hóa bài toán logic
- Luật về phép kéo theo
- Dạng chuẩn tắc tuyển (DNF)
- Dạng chuẩn tắc hội (CNF)
- Các định lý quan trọng

---

# Ôn tập — Logic mệnh đề

- Mệnh đề: khẳng định có giá trị **T/F**
- Mệnh đề sơ cấp vs phức hợp
- Ký hiệu: $p, q, r, ...$

---

# Ôn tập — Phép toán logic

| Ký hiệu | Tên | Code |
|:---:|:---|:---|
| $\neg$ | Phủ định | `not` |
| $\land$ | Hội | `and` |
| $\lor$ | Tuyển | `or` |
| $\to$ | Kéo theo | — |
| $\leftrightarrow$ | Tương đương | — |
| $\oplus$ | XOR | `!=` |

---

# Ôn tập — Bảng chân trị

- $n$ biến → **$2^n$** dòng
- Liệt kê mọi tổ hợp T/F
- Tính từ trong ra ngoài

| Loại | Đặc điểm |
|:---|:---|
| Tautology | Luôn T |
| Contradiction | Luôn F |
| Contingency | Tùy biến |

---

# Ôn tập — Tương đương logic

$E_1 \equiv E_2$ ⟺ cùng bảng chân trị

**Chứng minh:**
1. Bảng chân trị
2. Biến đổi bằng luật logic

---

# Ôn tập — Các luật logic cơ bản (đầy đủ)

| Tên luật              | Công thức                                      | Ghi chú |
|-----------------------|------------------------------------------------|---------|
| Phủ định kép          | $\neg\neg p \equiv p$                          | Double negation |
| De Morgan             | $\neg(p \land q) \equiv \neg p \lor \neg q$    | Rất quan trọng |
| De Morgan (2)         | $\neg(p \lor q) \equiv \neg p \land \neg q$    |         |
| Giao hoán             | $p \land q \equiv q \land p$                   | Commutative |
| Giao hoán OR          | $p \lor q \equiv q \lor p$                     |         |
| Kết hợp               | $(p \land q) \land r \equiv p \land (q \land r)$ | Associative |
| Phân phối             | $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ | Distributive |
| Phân phối (2)         | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ | |
| Bù (Complement)       | $p \lor \neg p \equiv T$, $p \land \neg p \equiv F$ | |
| Đồng nhất (Identity)  | $p \land T \equiv p$, $p \lor F \equiv p$      | |
| Nuốt (Domination)     | $p \lor T \equiv T$, $p \land F \equiv F$      | |
| Hấp thụ (Absorption)  | $p \lor (p \land q) \equiv p$                  | |
| Lũy đẳng (Idempotent) | $p \lor p \equiv p$, $p \land p \equiv p$      | |

**Các luật De Morgan, Phân phối và Bù được dùng nhiều nhất.**

---

# Luật về phép kéo theo (1)

**Định nghĩa kéo theo:**

$$p \to q \equiv \neg p \lor q$$

Dùng để loại bỏ $\to$ khi chuyển sang DNF/CNF

---

# Luật về phép kéo theo (2)

**Contrapositive (phản đảo):**

$$p \to q \equiv \neg q \to \neg p$$

Ví dụ: "Nếu mưa thì ướt" ≡ "Nếu không ướt thì không mưa"

---

# Luật về phép kéo theo (3)

**Exportation (xuất nhập):**

$$p \to (q \to r) \equiv (p \land q) \to r$$

Điều kiện lồng nhau ↔ điều kiện hội

---

# Luật về phép kéo theo (4)

| Công thức | Ý nghĩa |
|:---|:---|
| $(p \to q) \land (p \to r) \equiv p \to (q \land r)$ | Một giả thiết → nhiều KL |
| $(p \to r) \land (q \to r) \equiv (p \lor q) \to r$ | Nhiều GT → một KL |
| $p \to (q \to p)$ | **Tautology** |

---

# Đặt vấn đề: Mô hình hóa logic

**Bước 1:** Đọc yêu cầu nghiệp vụ

**Bước 2:** Đặt biến mệnh đề ($p, q, r...$)

**Bước 3:** Viết biểu thức logic

**Bước 4:** Kiểm tra (bảng chân trị / code)

---

# Ví dụ mô hình hóa

> Cho xem điểm nếu: đã đăng nhập, thuộc lớp, GV đã công bố

- $p$: đã đăng nhập
- $q$: thuộc lớp
- $r$: GV công bố điểm

$$p \land q \land r$$

---

# Ví dụ mô hình hóa (2)

> Đăng ký môn khi: đóng HP, TK active, (học xong TQ hoặc CV cho phép)

$$p \land q \land (r \lor s)$$

```python
can_register = paid and active and (passed_prereq or advisor_ok)
```

---

# Thảo luận (10 phút)

Chọn 1 tình huống & mô hình hóa:

- Đăng nhập hệ thống
- Lọc sản phẩm
- Phân quyền tài liệu

---

# Dạng chuẩn tắc — Tại sao?

Cùng ý logic, nhiều cách viết:

- Code dài → khó đọc
- SAT solver cần **CNF**
- Compiler tối ưu biểu thức Boolean

→ Cần **dạng chuẩn** thống nhất

---

# DNF — Chuẩn tắc tuyển

**Disjunctive Normal Form**

Tuyển (OR) của các hội (AND):

$$(l_1 \land l_2 \land \cdots) \lor (l_3 \land l_4) \lor \cdots$$

Mỗi $l_i$ là literal ($p$ hoặc $\neg p$)

---

# Ví dụ DNF

$$(p \land q) \lor (\neg p \land r)$$

- Term 1: $p \land q$
- Term 2: $\neg p \land r$
- Nối bằng $\lor$

---

# Cách xây dựng DNF từ bảng chân trị

**Định nghĩa DNF**:
Dạng chuẩn tắc tuyển = OR của các AND của literal.

---

# Quy trình xây DNF (bước 1-2)

1. Lập bảng chân trị đầy đủ.
2. Chỉ giữ các hàng có kết quả = **T**.

---

# Quy trình xây DNF (bước 3-4)

3. Mỗi hàng T → một term:
   - Biến = T → giữ nguyên
   - Biến = F → lấy $\neg$ biến
4. Nối tất cả term bằng $\lor$.

---

# Ví dụ chi tiết: Xây DNF cho $(p \lor q) \to r$

Biểu thức: $(p \lor q) \to r$

**Bảng chân trị** (chỉ hiện các hàng T):

| $p$ | $q$ | $r$ | $p \lor q$ | Kết quả | Ghi chú |
|:---:|:---:|:---:|:----------:|:-------:|---------|
| T | T | T | T          | T       | Chọn |
| T | F | T | T          | T       | Chọn |
| F | T | T | T          | T       | Chọn |
| F | F | T | F          | T       | Chọn |

**Xây các term** (từ các hàng T):

Quy tắc: Biến = T → giữ nguyên, Biến = F → $\neg$ biến. Nối bằng $\land$.

- Hàng p=T q=T r=T: $p \land q \land r$
- Hàng p=T q=F r=T: $p \land \neg q \land r$
- Hàng p=F q=T r=T: $\neg p \land q \land r$
- Hàng p=F q=F r=T: $\neg p \land \neg q \land r$

**DNF**:
$$(p \land q \land r) \lor (p \land \neg q \land r) \lor (\neg p \land q \land r) \lor (\neg p \land \neg q \land r)$$

**Rút gọn** (sau này dùng luật):
$$r \land (p \lor q) \lor (\neg p \land \neg q \land r)$$ (có thể tiếp tục rút gọn)

**Nhận xét**: DNF thường dài hơn CNF cho biểu thức này. Phương pháp bảng luôn cho kết quả đúng nhưng nên rút gọn thêm.

---

# CNF — Chuẩn tắc hội

**Conjunctive Normal Form**

Hội (AND) của các tuyển (OR):

$$(l_1 \lor l_2 \lor \cdots) \land (l_3 \lor l_4) \land \cdots$$

Mỗi ngoặc = một **clause** (mệnh đề con)

---

# Ví dụ CNF

$$(p \lor q) \land (\neg p \lor r) \land (q \lor \neg r)$$

Mỗi clause = một **ràng buộc** phải thỏa

---

# Cách xây dựng CNF từ bảng chân trị

**Định nghĩa CNF**:
Dạng chuẩn tắc hội = AND của các OR (clause) của literal.

---

# Quy trình xây CNF (bước 1-2)

1. Lập bảng chân trị.
2. Chỉ giữ các hàng có kết quả = **F**.

---

# Quy trình xây CNF (bước 3-4)

3. Mỗi hàng F → một clause:
   - Biến = T → lấy $\neg$ biến
   - Biến = F → giữ nguyên biến
   - Nối bằng $\lor$
4. Nối tất cả clause bằng $\land$.

**Lưu ý**: CNF là input chuẩn cho SAT solvers.

---

# Ví dụ chi tiết hơn: Xây CNF cho $(p \lor q) \to r$

Biểu thức: $(p \lor q) \to r$

**Bảng chân trị** (chỉ hiện các hàng F để ngắn gọn):

| $p$ | $q$ | $r$ | $p \lor q$ | Kết quả | Hàng F |
|:---:|:---:|:---:|:----------:|:-------:|:------:|
| T | T | F | T          | F       | 1      |
| T | F | F | T          | F       | 2      |
| F | T | F | T          | F       | 3      |

**Xây các clause** (từ các hàng F):

Quy tắc: Với mỗi biến trong hàng F:
- Nếu biến = T → đưa $\neg$ biến vào clause
- Nếu biến = F → đưa biến vào clause
- Nối bằng $\lor$

- Hàng 1 (p=T, q=T, r=F): $\neg p \lor \neg q \lor r$
- Hàng 2 (p=T, q=F, r=F): $\neg p \lor q \lor r$
- Hàng 3 (p=F, q=T, r=F): $p \lor \neg q \lor r$

**CNF đầy đủ**:
$$(\neg p \lor \neg q \lor r) \land (\neg p \lor q \lor r) \land (p \lor \neg q \lor r)$$

**Rút gọn** (dùng luật):
$$(\neg p \lor r) \land (\neg q \lor r)$$

**Nhận xét**: 
- Phương pháp bảng chân trị luôn đúng nhưng có thể cho CNF chưa tối ưu.
- Sau đó nên dùng luật logic (De Morgan, phân phối, bù...) để rút gọn.
- Kết quả cuối cùng chính là $(p \lor q) \to r \equiv (\neg p \lor r) \land (\neg q \lor r)$. 

Đây là ví dụ thực tế hơn khi mô hình hóa điều kiện nghiệp vụ có nhiều biến.

---

# DNF vs CNF

| | DNF | CNF |
|:---|:---|:---|
| Cấu trúc | OR của AND | AND của OR |
| Xây từ | Hàng **T** | Hàng **F** |
| Ứng dụng | Mô tả vùng đúng | SAT solver, ràng buộc |

---

# Định lý 1 — Sự tồn tại DNF & CNF

**Định lý**: Mọi biểu thức mệnh đề (mọi hàm Boolean hữu hạn) đều có thể được chuyển về dạng **DNF** và dạng **CNF**.

**Chứng minh**:
- Bảng chân trị của một biểu thức với $n$ biến luôn có $2^n$ dòng hữu hạn.
- Từ hàng T ta xây DNF, từ hàng F ta xây CNF.
- Do đó luôn tồn tại (ít nhất một).

---

# Định lý 2 — Tính duy nhất của DNF/CNF đầy đủ

**Định nghĩa DNF/CNF đầy đủ:**

- Mỗi term/clause chứa **đủ $n$ literal**
- Mỗi hàm Boolean có **đúng một** DNF đầy đủ
- Mỗi hàm Boolean có **đúng một** CNF đầy đủ

→ Dạng **chuẩn tắc** (canonical form)

---

# Định lý 3 — DNF ↔ CNF qua phủ định

$$\neg P \text{ có CNF} \Leftrightarrow P \text{ có DNF}$$

Áp dụng De Morgan mở rộng:

Phủ định DNF → CNF (và ngược lại)

---

# Rút gọn biểu thức

Chiến lược:

1. Loại bỏ $\to$: thay bằng $\neg p \lor q$
2. De Morgan — đẩy $\neg$ vào trong
3. Phân phối, gộp, loại hằng/bù

---

# Ví dụ rút gọn

$$\neg(p \lor \neg q) \land (r \lor \neg r)$$

$$\equiv (\neg p \land q) \land T \equiv \neg p \land q$$

---

# Thực hành 1 (15 phút)

Mô hình hóa & viết công thức:

> Tải file nếu: đăng nhập, email xác thực, (file < 10MB hoặc Premium)

---

# Thực hành 2 (20 phút)

Cho biểu thức: $(p \lor q) \land (\neg p \lor r)$

1. Lập bảng chân trị
2. Viết DNF đầy đủ
3. Xác nhận đã là CNF

---

# Thực hành 3 (15 phút)

Dùng luật kéo theo, chứng minh:

$$p \to (q \to r) \equiv (p \land q) \to r$$

(bảng chân trị hoặc biến đổi)

---

# Thực hành 4 (10 phút)

Chuyển sang CNF:

$$(p \land q) \lor (\neg p \land \neg q)$$

Gợi ý: đây tương đương $p \leftrightarrow q$

---

# Nhầm lẫn thường gặp

- Nhầm DNF (OR-AND) với CNF (AND-OR)
- Quên đổi literal khi xây CNF từ hàng F
- Bỏ bước loại bỏ $\to$ trước khi chuẩn hóa

---

# Tóm tắt Tiết 4

- Mô hình hóa: yêu cầu → biến → công thức
- Luật kéo theo: định nghĩa, contrapositive, exportation
- DNF = OR của AND | CNF = AND của OR
- Mọi công thức có DNF/CNF; dạng đầy đủ là duy nhất

---

# Bài tập ôn tập (1/2)

1. **Bài 1**: Chuyển sang DNF đầy đủ:
   $$(p \to q) \land (q \to r)$$

2. **Bài 2**: Chuyển sang CNF:
   $$(p \land q) \lor (\neg p \land \neg q)$$

3. **Bài 3**: Chứng minh:
   $$p \to (q \to r) \equiv (p \land q) \to r$$

---

# Bài tập ôn tập (2/2)

4. **Bài 4**: Mô hình hóa + viết DNF và CNF:
   > Sửa bài nếu admin, hoặc (tác giả và chưa khóa).

5. **Bài 5**: Giải thích khác biệt DNF vs CNF. SAT solver dùng dạng nào?

---

# Tiết sau

**Quy tắc suy diễn**

- Modus Ponens, Modus Tollens
- Tam đoạn luận
- Phương pháp mâu thuẫn

---

# Câu hỏi?