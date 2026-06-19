---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Mệnh đề

**Toán Rời Rạc — IUH**

Tiết 2 (45 phút) — Logic mệnh đề

---

# Mục tiêu tiết học

- Logic học nghiên cứu gì?
- Định nghĩa mệnh đề
- Phân loại mệnh đề
- Định lý bất toàn (Gödel)
- Tổng quan logic mệnh đề

---

# Logic học nghiên cứu cái gì?

**Logic** = quy tắc suy luận hợp lý

- Từ tiền đề **đúng** → kết luận **đúng**
- Quan tâm **hình thức**, không quan tâm nội dung cụ thể

---

# Hình thức vs Nội dung

| Quan tâm | Không quan tâm |
|:---|:---|
| Cấu trúc "Nếu P thì Q" | P, Q là gì |
| Quan hệ đúng/sai | Ý nghĩa thực tế |
| Quy tắc suy luận | Chủ đề tranh luận |

---

# Ví dụ: Cùng hình thức

- "Nếu trời mưa thì đường ướt"
- "Nếu n chẵn thì n² chẵn"

Cùng cấu trúc: **Nếu P thì Q**

---

# Ví dụ thực tế

Luật giao thông (trẻ em & ghế an toàn):

$$(p \land q \land r) \to s$$

- $p$: trẻ < 10 tuổi
- $q$: cao < 1,35 m
- $r$: xe gia đình/cá nhân
- $s$: bắt buộc lắp ghế

---

# Lịch sử logic học

**Aristotle** (~350 TCN)

- Hệ thống hóa quy luật suy luận
- Bảng tứ đối (square of opposition)

**George Boole** (1815–1864)

- Logic Boolean → nền tảng máy tính

---

# Logic trong lập trình

```python
if score >= 5:
    pass
```

Mỗi `if`, `while`, SQL `WHERE` đều hỏi:

**Mệnh đề này đúng hay sai?**

---

# Định nghĩa Mệnh đề

**Mệnh đề (Proposition)**:
Câu khẳng định có giá trị **đúng (T)** hoặc **sai (F)**, nhưng không vừa đúng vừa sai.

**Ký hiệu**: $p, q, r, s, ...$

---

# Điều kiện để là mệnh đề

- Là câu **khẳng định**
- Giá trị chân lý **xác định được**
- Không phụ thuộc biến chưa gán
- Không phải câu hỏi / mệnh lệnh / cảm thán

---

# Giá trị chân lý của mệnh đề

| Giá trị | Ký hiệu | Ý nghĩa |
|:-------:|:-------:|:--------|
| Đúng    | T / 1   | True    |
| Sai     | F / 0   | False   |

Mỗi mệnh đề tại một thời điểm chỉ có **duy nhất một** giá trị chân lý.

---

# Ví dụ mệnh đề

- "2 + 3 = 5" → **T**
- "Hà Nội là thủ đô Việt Nam" → **T**
- "5 > 10" → **F**
- "Mọi số nguyên tố đều lẻ" → **F** (vì 2 là số nguyên tố chẵn)

---

# Không phải mệnh đề

- "x + 1 = 5" → không phải (phụ thuộc biến $x$)
- "Hôm nay trời đẹp!" → không phải (chủ quan)
- "Mấy giờ rồi?" → không phải (câu hỏi)
- "Hãy đóng cửa!" → không phải (mệnh lệnh)

---

# Mệnh đề sơ cấp

**Định nghĩa**: Mệnh đề sơ cấp (Atomic proposition) là mệnh đề không thể được phân tích thêm thành các mệnh đề nhỏ hơn bằng các phép toán logic.

**Đặc điểm**:
- Không chứa bất kỳ phép toán logic nào (¬, ∧, ∨, →, ↔...)
- Là "nguyên tử" của hệ thống logic

**Ví dụ**:
- "2 + 3 = 5"
- "Hà Nội là thủ đô của Việt Nam"

---

# Mệnh đề phức hợp

**Định nghĩa**: Mệnh đề phức hợp (Compound proposition) là mệnh đề được tạo thành từ các mệnh đề khác thông qua các **phép toán logic** hoặc phủ định.

**Ví dụ**:
- "Hôm nay trời mưa **và** tôi có ô" → $p \land q$
- "**Nếu** trời mưa **thì** đường ướt" → $p \to q$

---

# Logic mệnh đề

**Propositional Logic** là hệ thống logic làm việc với:
- Các mệnh đề (sơ cấp và phức hợp)
- Các phép toán logic trên chúng
- Kết quả luôn là giá trị chân lý (đúng/sai)

Nền tảng của: điều kiện trong code, truy vấn SQL, hệ thống phân quyền, SAT solver, AI suy luận...

---

# Ký hiệu mệnh đề

Sử dụng các chữ cái thường $p, q, r, s, \dots$ để đại diện cho các mệnh đề.

---

# Ứng dụng — Lập trình

```python
if age >= 18 and is_student and has_valid_id:
    apply_discount()
```

3 mệnh đề sơ cấp → 1 mệnh đề phức hợp

---

# Ứng dụng — CSDL

```sql
SELECT * FROM students
WHERE gpa >= 3.2 AND credits >= 60;
```

Mỗi dòng = một lần kiểm tra mệnh đề

---

# Ứng dụng — Bảo mật

```python
can_delete = is_admin or (is_owner and not is_locked)
```

Sai một dấu ngoặc → **lỗ hổng bảo mật**

---

# Định lý bất toàn của Gödel (1931) - Định lý 1

**Định lý bất toàn thứ nhất**:
> Trong mọi hệ thống logic hình thức đủ mạnh để biểu diễn số học, luôn tồn tại những mệnh đề **đúng nhưng không thể chứng minh được** bên trong hệ thống đó.

**Hàm ý**:
Luôn có sự thật đúng nhưng không chứng minh được trong hệ thống.

---

# Định lý bất toàn của Gödel (1931) - Định lý 2

**Định lý bất toàn thứ hai**:
> Một hệ thống logic nhất quán **không thể tự chứng minh được tính nhất quán** của chính mình.

**Hàm ý**:
Không thể có hệ thống "hoàn hảo" tự chứng minh mình đúng.

---

# Ý nghĩa với Khoa học Máy tính

| Hạn chế theo Gödel              | Hệ quả trong CNTT                              |
|--------------------------------|------------------------------------------------|
| Không chứng minh được mọi sự thật | Không có thuật toán kiểm tra mọi chương trình |
| Hệ thống không tự chứng minh nhất quán | Cần test thủ công + review + formal methods  |
| Liên hệ trực tiếp với Halting Problem | Không thể viết chương trình dự đoán mọi chương trình có dừng hay không |
| Giới hạn của tự động hóa       | Compiler, static analyzer chỉ phát hiện một phần lỗi |

**Bài học thực tiễn**: Không bao giờ tin tưởng tuyệt đối vào bất kỳ hệ thống tự động nào. Luôn cần kiểm thử và con người.

---

# Mệnh đề trong thực tế CNTT

**Ví dụ CSDL**:
```sql
SELECT * FROM users
WHERE age >= 18 AND status = 'active';
```
Mỗi điều kiện `age >= 18` là một mệnh đề.

**Ví dụ Bảo mật**:
```python
if is_admin or (is_owner and not is_locked):
    delete()
```
Sai dấu ngoặc → lỗ hổng nghiêm trọng (như một số CVE thực tế).

---

# Ví dụ: Yêu cầu nghiệp vụ

Sinh viên đăng ký môn khi:

- Đã đóng học phí ($p$)
- Tài khoản không khóa ($q$)
- Học xong tiên quyết **hoặc** cố vấn cho phép ($r \lor s$)

$$p \land q \land (r \lor s)$$

---

# Số hàm Boolean

Với $n$ biến: có **$2^{2^n}$** hàm Boolean

| $n$ | Số hàm |
|:---:|:---:|
| 1 | 4 |
| 2 | 16 |
| 3 | 256 |
| 10 | $2^{1024}$ |

→ Bảng chân trị chỉ khả thi khi $n$ nhỏ

---

# Thực hành 1 (10 phút)

Câu nào là mệnh đề?

1. "Python là ngôn ngữ lập trình"
2. "x² = 4"
3. "Hãy học bài!"
4. "Nếu n chẵn thì n chia hết cho 2"

---

# Thực hành 2 (10 phút)

Đặt ký hiệu & viết công thức:

> Cho tải file nếu: đã đăng nhập, email xác thực, và (file < 10MB hoặc Premium)

---

# Thực hành 3 (15 phút)

Phân tích mệnh đề phức hợp:

> "Nếu trời mưa và tôi có ô thì tôi sẽ đi làm"

- Mệnh đề sơ cấp?
- Công thức logic?

---

# Nhầm lẫn thường gặp

- Nhầm **câu hỏi / mệnh lệnh** với mệnh đề
- Nhầm **vị từ** (có biến) với mệnh đề
- Nhầm **nội dung** tranh luận với **hình thức** logic

---

# Tóm tắt Tiết 2

- Logic = suy luận hợp lý theo **hình thức**
- Mệnh đề = khẳng định có giá trị T/F
- Sơ cấp vs phức hợp
- Gödel: giới hạn của hệ logic hình thức

---

# Bài tập ôn tập (1/2)

1. **Bài 1**: Xác định mệnh đề + giá trị:
   (a) "Hà Nội là thủ đô VN"
   (b) "x + 3 = 7"
   (c) "Hãy nộp bài!"
   (d) "Mọi số chẵn chia hết 2"
   (e) "Hôm nay có thể mưa"

2. **Bài 2**: Đặt biến + viết logic:
   > "Nếu đã đóng HP và active thì được đăng ký."

---

# Bài tập ôn tập (2/2)

3. **Bài 3**: Phân tích + công thức:
   > "Nếu trời mưa và có ô thì đi làm."

4. **Bài 4**: Cho ví dụ phức hợp trong code, phân tích thành sơ cấp.

5. **Bài 5**: Tại sao "x > 5" không phải mệnh đề?

---

# Tiết sau

**Biểu thức logic**

- Phép toán: ¬, ∧, ∨, →, ↔, ⊕
- Bảng chân trị
- Tương đương & luật logic
- Ví dụ: lọc sản phẩm, validator web

---

# Câu hỏi?