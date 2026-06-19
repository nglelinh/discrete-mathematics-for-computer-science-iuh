---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Toán Rời Rạc cho Khoa học Máy tính

**IUH** — Tiết 1 (45 phút)

Nguyễn Lê Linh

---

# Làm quen

- Tên, lớp, kỳ học?
- Đã học toán rời rạc / logic chưa?
- Kỳ vọng gì từ môn học?

---

# Giới thiệu khóa học

**Toán Rời Rạc cho Khoa học Máy tính** — IUH

- Nền tảng toán cho sinh viên CNTT
- Tập trung ứng dụng lập trình & KHMT
- Tài liệu tương tác trên website khóa học

---

# Mục tiêu khóa học

- Hiểu khái niệm cơ bản toán rời rạc
- Nắm logic toán & phương pháp chứng minh
- Áp dụng tập hợp, quan hệ, hàm số
- Phân tích thuật toán & độ phức tạp
- Ứng dụng lý thuyết đồ thị

---

# Học viên đạt được gì?

- **Tư duy logic** — mệnh đề, vị từ
- **Chứng minh** — trực tiếp, phản chứng, quy nạp
- **Tập hợp & quan hệ** — mô hình hóa dữ liệu
- **Phân tích thuật toán** — độ phức tạp, đếm
- **Đồ thị** — mạng, tối ưu, tìm đường
- **Cấu trúc nâng cao** — truy hồi, Boole, mã hóa

---

# Định nghĩa Toán rời rạc

**Toán rời rạc (Discrete Mathematics)** là ngành toán học nghiên cứu các cấu trúc toán học có tính **rời rạc** (các đối tượng có thể đếm được, tách biệt).

**Đặc điểm chính**:
- Các phần tử là riêng biệt, không liên tục
- Tập hợp hữu hạn hoặc đếm được
- Không dùng khái niệm giới hạn, đạo hàm, tích phân

**Đối tượng nghiên cứu**: logic, tập hợp, quan hệ, hàm, đếm, đồ thị, đại số Boole, thuật toán...

---

# Định nghĩa Logic

**Logic** (luận lý học) là ngành khoa học nghiên cứu **các quy tắc suy luận hợp lý**.

**Mục tiêu**: Từ các **tiền đề đúng** rút ra **kết luận đúng** một cách có hệ thống và chặt chẽ.

**Đặc điểm quan trọng**:
- Chỉ quan tâm đến **hình thức** (cấu trúc) của lập luận.
- Không quan tâm đến nội dung thực tế của các phát biểu.

**Ví dụ cấu trúc**: "Nếu P thì Q" là cùng hình thức dù P/Q là gì.

---

# Rời rạc vs Liên tục

| Liên tục | Rời rạc |
|:---|:---|
| Giải tích, vi phân | Logic, tập hợp |
| Hàm số liên tục | Đồ thị, cây |
| Thay đổi mượt | Bước hữu hạn |

**Máy tính** xử lý bit, byte — dữ liệu rời rạc

---

# Tại sao Toán rời rạc là nền tảng của CNTT?

**Định nghĩa vai trò**:
Toán rời rạc cung cấp các công cụ toán học để:
- Mô tả cấu trúc dữ liệu
- Phân tích thuật toán
- Thiết kế hệ thống logic
- Chứng minh tính đúng đắn của chương trình

**Lý do cốt lõi**:
- Máy tính chỉ xử lý **dữ liệu rời rạc** (bit, số nguyên, trạng thái)
- Mọi thuật toán thực hiện **số bước hữu hạn**
- Logic là ngôn ngữ của mọi `if`, `while`, truy vấn, và quyết định tự động

**Ví dụ cụ thể**:
- CSDL quan hệ dựa trên lý thuyết tập hợp và quan hệ
- Mật mã RSA dựa trên lý thuyết số
- Trí tuệ nhân tạo sử dụng logic và suy diễn
- Phân tích độ phức tạp dùng Big-O (toán rời rạc)

---

# Các lĩnh vực chính của Toán rời rạc

| Lĩnh vực              | Nội dung chính                          | Ứng dụng CNTT                     |
|-----------------------|-----------------------------------------|-----------------------------------|
| Logic mệnh đề & vị từ | Mệnh đề, phép toán, suy diễn            | Điều kiện code, CSDL, AI          |
| Phương pháp chứng minh| Trực tiếp, phản chứng, quy nạp          | Kiểm chứng phần mềm               |
| Lý thuyết tập hợp     | Tập, phép toán, lực lượng               | Mô hình dữ liệu, SQL              |
| Quan hệ & Hàm         | Tính chất, tương đương, toàn ánh        | CSDL quan hệ, ánh xạ             |
| Đếm & Tổ hợp          | Hoán vị, tổ hợp, bao hàm-loại trừ       | Xác suất, mật mã, thuật toán      |
| Đồ thị                | Đường đi, Euler, Hamilton, tô màu       | Mạng, tối ưu, tìm đường           |
| Đại số Boole          | Hàm Boole, Karnaugh, mạch logic         | Thiết kế phần cứng                |
| Truy hồi & Hàm sinh   | Phương trình sai phân                   | Phân tích thuật toán đệ quy       |
| Lý thuyết số          | Chia hết, modulo, nguyên tố             | Mật mã RSA, blockchain            |
| Độ phức tạp           | Big-O, P vs NP                          | Đánh giá hiệu quả thuật toán      |

---

# Một số định lý và khái niệm nền tảng

- **Định lý Gödel về sự bất toàn** (1931)
- **Nguyên lý chuồng bồ câu** (Dirichlet)
- **Nguyên lý bao hàm - loại trừ**
- **Định lý về tính duy nhất của DNF/CNF**
- **Big-O notation** và phân tích tiệm cận

---

# Lịch sử ngắn gọn

**Aristotle** (384–322 TCN)
- Cha đẻ của logic hình thức
- Hệ thống hóa các quy luật suy luận (Tam đoạn luận)

**George Boole** (1815–1864)
- Sáng tạo Đại số Boolean
- Nền tảng cho mạch logic và máy tính hiện đại

**Kurt Gödel** (1906–1978)
- Định lý bất toàn — giới hạn của mọi hệ thống logic hình thức

**Claude Shannon** (1916–2001)
- Áp dụng logic Boolean vào thiết kế mạch điện tử (1937)

---

# Ứng dụng trong CNTT

| Lĩnh vực | Ứng dụng |
|:---|:---|
| Thuật toán | Big-O, cây, bảng băm |
| Mạng | Định tuyến, đồ thị |
| Mật mã | RSA, chữ ký số |
| AI | Suy luận, SAT solver |
| CSDL | Lược đồ, SQL |
| Lập trình | Kiểm chứng, test |

---

# Chương trình — Phần I

**Nền tảng Logic & Chứng minh**

| Ch | Nội dung |
|:---:|:---|
| 1 | Logic mệnh đề |
| 2 | Logic vị từ |
| 3 | Phương pháp chứng minh |

---

# Chương trình — Phần II & III

**Tập hợp, Quan hệ, Hàm** (4–6)

**Đếm** (7–8)

- Nguyên lý cộng, nhân, tổ hợp
- Nguyên lý chuồng bồ câu

---

# Chương trình — Phần IV–VI

| Phần | Chương | Nội dung |
|:---|:---:|:---|
| IV | 10–11 | Truy hồi, hàm sinh |
| V | 12–13 | Đồ thị, đại số Boole |
| VI | 14–16 | Thuật toán, số học, cây |

---

# Phương pháp học tập

- **Lý thuyết tương tác** — trực quan hóa trên web
- **Công cụ** — thực hành trên trình duyệt
- **Ví dụ thực tế** — code, SQL, hệ thống
- **Bài tập** — cơ bản → nâng cao

---

# Đánh giá

| Hạng mục | Tỷ lệ |
|:---|:---:|
| Giữa kỳ | 30% |
| Bài tập & thực hành | 20% |
| Cuối kỳ | 50% |

---

# Sách & tài liệu

**Giáo trình chính**

- Rosen — *Discrete Mathematics and Its Applications* (8e)
- Kolman & Busby — *Discrete Mathematical Structures* (6e)
- Nguyễn Hữu Anh — *Toán Rời Rạc*

**Tham khảo:** Epp, Johnsonbaugh, MIT OCW, Stanford CS103

---

# Website khóa học

- Bài giảng tương tác
- Công cụ: bảng chân trị, đồ thị, đếm...
- Bài tập có đáp án
- Liên hệ: **nglelinh@gmail.com**

---

# Thảo luận (15 phút)

1. Bạn đã gặp toán rời rạc ở đâu trong code?
2. Ví dụ: `if`, SQL, phân quyền?
3. Điều gì khiến bạn lo lắng về môn này?

---

# Tóm tắt Tiết 1

- Toán rời rạc = nền tảng KHMT
- Khóa học: logic → đếm → đồ thị → nâng cao
- Học tương tác, ứng dụng thực tế
- **Tiết sau:** Mệnh đề & Logic mệnh đề

---

# Bài tập ôn tập (1/2)

1. **Bài 1**: Rời rạc vs liên tục? Ví dụ code cho mỗi loại.

2. **Bài 2**: Liệt kê 3 tình huống code/SQL dùng logic hoặc rời rạc.

3. **Bài 3**: Tại sao máy tính chỉ xử lý dữ liệu rời rạc?

---

# Bài tập ôn tập (2/2)

4. **Bài 4**: Kiểm tra toàn bộ chương trình tự động có khả thi 100% không? Liên hệ Gödel.

5. **Bài 5** (tư duy): Môn Toán Rời Rạc giúp ích nhất môn nào trong CNTT? Tại sao?

---

# Câu hỏi?

**Tiết 2:** Mệnh đề — Logic học nghiên cứu gì?