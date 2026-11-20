---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Quan hệ trong Cơ sở Dữ liệu

**Toán Rời Rạc**

Tiết 42 (45 phút) — Relations as Tables, JOIN, Relational Algebra

---

## Mục tiêu tiết học

- Xem quan hệ hai ngôi như bảng dữ liệu (relation)
- Hiểu mô hình quan hệ của E. F. Codd (1970)
- Thực hiện các phép JOIN trong SQL
- Nắm các phép đại số quan hệ cơ bản
- Liên hệ quan hệ toán học (tiết 11–13) với CSDL thực tế

---

## Ôn — Quan hệ hai ngôi

**Định nghĩa**: $$R \subseteq A \times B$$ — tập các cặp có thứ tự $$(a, b)$$.

**Ví dụ**: $$R = \{(1, \text{An}), (2, \text{Bình}), (3, \text{Chi})\}$$

Trong toán: tập các cặp.
Trong CS: **bảng dữ liệu** — mỗi hàng là một tuple thuộc quan hệ.

**Liên hệ tiết 11–13**: Phản xạ, đối xứng, bắc cầu → ràng buộc CSDL.

---

## Mô hình quan hệ — E. F. Codd

**Ý tưởng (1970)**: Dữ liệu = **quan hệ** (bảng), thao tác = **đại số**.

- **Quan hệ** (relation): Bảng gồm các **hàng** (tuple)
- **Thuộc tính** (attribute): Cột — tên và kiểu dữ liệu
- **Miền** (domain): Tập giá trị hợp lệ của mỗi cột
- **Khóa** (key): Thuộc tính (hoặc tập) định danh duy nhất mỗi hàng

**Lợi ích**: Tách "dữ liệu là gì" khỏi "lưu trữ ra sao".

---

## Ví dụ — Bảng quan hệ

**Students** (id, name, major):

| id | name | major |
|:---:|:---:|:---:|
| 1 | An | CNTT |
| 2 | Bình | KT |
| 3 | Chi | CNTT |

**Enrollments** (student_id, course_id, grade):

| student_id | course_id | grade |
|:---:|:---:|:---:|
| 1 | CS101 | A |
| 1 | MA201 | B |
| 2 | CS101 | C |
| 3 | MA201 | A |

**Foreign key**: `student_id` tham chiếu `Students(id)`.

---

## Khóa và ràng buộc

- **Primary key**: Định danh duy nhất mỗi hàng (`Students.id`)
- **Foreign key**: Tham chiếu khóa bảng khác
- **Unique**: Không trùng lặp
- **NOT NULL**: Bắt buộc có giá trị

```sql
CREATE TABLE Enrollments (
    student_id INT,
    course_id  VARCHAR(10),
    grade      CHAR(1),
    FOREIGN KEY (student_id) REFERENCES Students(id)
);
```

**Ý nghĩa**: Quan hệ trừu tượng → ràng buộc máy tính cưỡng chế.

---

## Đại số quan hệ — Các phép cơ bản

| Phép | Ký hiệu | SQL tương đương |
|:---|:---:|:---|
| **Selection** $$\sigma$$ | Lọc hàng | `WHERE` |
| **Projection** $$\pi$$ | Chọn cột | `SELECT col1, col2` |
| **Join** $$\bowtie$$ | Ghép bảng | `JOIN` |
| **Union** $$\cup$$ | Hợp | `UNION` |
| **Difference** $$-$$ | Hiệu | `EXCEPT` |
| **Rename** $$\rho$$ | Đổi tên | `AS` alias |

**Query planner**: DBMS biến đổi SQL bằng luật đại số để tối ưu.

---

## Selection & Projection

**Selection** — lọc hàng thỏa điều kiện:

$$\sigma_{\text{major}=\text{'CNTT'}}(\text{Students})$$

```sql
SELECT * FROM Students WHERE major = 'CNTT';
-- Kết quả: An, Chi
```

**Projection** — chọn cột:

$$\pi_{\text{name, major}}(\text{Students})$$

```sql
SELECT name, major FROM Students;
```

---

## JOIN — Ghép hai quan hệ

**Ý tưởng**: Kết hợp hàng từ hai bảng qua **khóa chung**.

**INNER JOIN**: Chỉ giữ hàng **khớp** ở cả hai bảng.

```sql
SELECT s.name, e.course_id, e.grade
FROM Students s
INNER JOIN Enrollments e ON s.id = e.student_id;
```

| name | course_id | grade |
|:---:|:---:|:---:|
| An | CS101 | A |
| An | MA201 | B |
| Bình | CS101 | C |
| Chi | MA201 | A |

---

## Các loại JOIN

| Loại JOIN | Mô tả | Hàng không khớp |
|:---|:---|:---|
| **INNER** | Chỉ hàng khớp cả hai | Bỏ |
| **LEFT** | Giữ mọi hàng bảng trái | NULL bên phải |
| **RIGHT** | Giữ mọi hàng bảng phải | NULL bên trái |
| **FULL OUTER** | Giữ tất cả | NULL hai bên |
| **CROSS** | Tích Descartes | $$|A| \times |B|$$ hàng |

**Ví dụ LEFT JOIN**: Sinh viên chưa đăng ký môn nào vẫn xuất hiện (grade = NULL).

---

## Ví dụ LEFT JOIN

```sql
SELECT s.name, e.course_id
FROM Students s
LEFT JOIN Enrollments e ON s.id = e.student_id;
```

Giả sử thêm sinh viên D chưa đăng ký:

| name | course_id |
|:---:|:---:|
| An | CS101 |
| An | MA201 |
| Bình | CS101 |
| Chi | MA201 |
| D | **NULL** |

**Ứng dụng**: Tìm sinh viên **không** có enrollment → `WHERE e.course_id IS NULL`.

---

## Cartesian Product & Natural Join

**Tích Descartes**: $$A \times B$$ — mọi cặp hàng.

$$|\sigma_{...}(A \times B)|$$ có thể rất lớn → JOIN cần điều kiện.

**Natural Join** $$R \bowtie S$$: Tự động khớp cột cùng tên.

**Theta Join**: $$R \bowtie_\theta S$$ với điều kiện $$\theta$$ tùy ý.

**Chi phí**: JOIN là phép tốn kém nhất — optimizer quan trọng ($$O(n^{2})$$ naive).

---

## Quan hệ ↔ Đồ thị ↔ Mạng xã hội

**CSDL quan hệ**: Bảng, JOIN, SQL.

**Đồ thị** (tiết 36–37): Đỉnh + cạnh — `follows(A,B)`, `friends(A,B)`.

**Mạng xã hội**: Hàng tỷ quan hệ — không đối xứng (follow), có hướng.

**Recommendation**: Ma trận user–item là quan hệ hai ngôi (bipartite).

**Equivalence classes** (tiết 12): Chia input test thành lớp tương đương.

---

## Thực hành 1

Cho bảng **Courses** (id, title): (CS101, "TRR"), (MA201, "Giải tích").

Viết SQL INNER JOIN 3 bảng Students, Enrollments, Courses để lấy: `name, title, grade`.

---

## Thực hành 2

1. Viết LEFT JOIN tìm sinh viên **chưa đăng ký** môn nào.
2. Đếm số sinh viên theo `major` (gợi ý: `GROUP BY`).
3. Phép đại số tương ứng với `GROUP BY` là gì? (gợi ý: aggregation)

---

## Thực hành 3

Bảng A (2 hàng), B (3 hàng):

1. CROSS JOIN cho bao nhiêu hàng?
2. INNER JOIN với điều kiện `A.id = B.a_id` (giả sử 2 khớp) → bao nhiêu hàng?
3. Tại sao tránh CROSS JOIN không điều kiện trên bảng lớn?

---

## Tóm tắt Tiết 42

- **Quan hệ** = bảng = tập các tuple
- **Khóa**: primary, foreign — ràng buộc toàn vẹn
- **Đại số**: $$\sigma, \pi, \bowtie, \cup$$
- **JOIN**: INNER (khớp), LEFT (giữ trái), RIGHT, FULL
- Codd (1970) → SQL, PostgreSQL, MySQL

---

## Liên hệ

**Phép chính**: JOIN — nền của hầu hết truy vấn thực tế.

**Edge case**: NULL trong JOIN; duplicate key; Cartesian product vô tình.

**Liên hệ**: Quan hệ (tiết 11–13) ↔ CSDL (tiết 42) ↔ Đồ thị (tiết 36).

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Phân biệt selection ($$\sigma$$) và projection ($$\pi$$). Cho ví dụ SQL.

2. **JOIN**: INNER vs LEFT — khi nào dùng mỗi loại?

3. **SQL**: Viết truy vấn lấy tên sinh viên CNTT và điểm môn CS101.

---

## Bài tập ôn tập (2/2)

4. **Đại số**: Cho R = {(1,a), (2,b)} và S = {(1,x), (3,y)}. Tính $$R \bowtie S$$ với điều kiện R.col1 = S.col1.

5. **Bài 5**: Thiết kế 3 bảng (Student, Course, Enrollment) cho hệ đăng ký môn. Nêu primary key và foreign key. Viết 1 truy vấn JOIN có ý nghĩa.
