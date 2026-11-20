---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Tổng kết Khóa học

**Toán Rời Rạc**

Tiết 45 (45 phút) — Tổng kết + Feedback + Hướng tự học

---

## Mục tiêu tiết học

- Tổng hợp toàn bộ kiến thức qua 6 phần của khóa học
- Nhìn lại mạch logic: Logic → Chứng minh → Ứng dụng CS
- Nhận diện kỹ năng đã đạt được
- Hướng dẫn tự học tiếp (automata, P/NP, formal methods)
- Thu feedback; nhắc lịch **thi cuối kỳ riêng**

---

## Cấu trúc khóa học — 45 tiết

| Phần | Tiết | Chủ đề |
|:---:|:---:|:---|
| **I** | 1–10 | Logic, chứng minh, tập hợp |
| **II** | 11–15 | Quan hệ, hàm |
| **III** | 16–23 | Đếm, tổ hợp |
| **IV** | 24–29 | Truy hồi + ôn số phức / HTTH |
| **V** | 30–37 | Boolean, đồ thị |
| **VI** | 38–44 | Thuật toán, số học, CSDL, SAT, cây |

**Đánh giá**: KT thường xuyên 20% · Giữa kỳ 30% · **Cuối kỳ 50%** (lịch riêng)

---

## Phần I — Logic & Tập hợp (Tiết 1–10)

**Nội dung chính**:
- Logic mệnh đề: AND, OR, NOT, implication, equivalence
- Logic vị từ: $$\forall$$, $$\exists$$, phủ định lượng từ
- Chứng minh: trực tiếp, phản chứng, quy nạp
- Tập hợp: phép toán, De Morgan, biểu diễn

**Ứng dụng CS**: Điều kiện code, validator, SQL `WHERE`, filter logic.

**KT1** (tiết 10): Logic + quy nạp + tập hợp.

---

## Phần II — Quan hệ & Hàm (Tiết 11–15)

**Nội dung chính**:
- Quan hệ: phản xạ, đối xứng, bắc cầu
- Tương đương, thứ tự, sơ đồ Hasse
- Hàm: đơn ánh, toàn ánh, song ánh
- Hàm ngược, hợp hàm

**Ứng dụng CS**: CSDL (tiết 42), equivalence testing, API mapping.

**Mạch nối**: Quan hệ (tiết 11–13) → CSDL JOIN (tiết 42).

---

## Phần III — Đếm (Tiết 16–23)

**Nội dung chính**:
- Nguyên lý cộng, nhân; hoán vị, tổ hợp
- Bao hàm–loại trừ; nhị thức Newton, tam giác Pascal
- Nguyên lý chuồng bồ câu; ứng dụng bảo mật

**Ứng dụng CS**: Đếm password, birthday attack, xác suất collision.

**KT giữa kỳ** (tiết 23): Quan hệ + Hàm + Đếm (~50% học kỳ).

---

## Phần IV — Truy hồi & Ôn tập (Tiết 24–29)

**Nội dung chính**:
- Quan hệ truy hồi tuyến tính (thuần nhất / không thuần nhất)
- Giải HTTH: đặc trưng, nghiệm kép / phức (sin–cos)
- Ôn số phức (tiết 28) + ôn bài tập HTTH (tiết 29)
- Ứng dụng: đệ quy, Fibonacci, Hanoi, chia để trị

**Ứng dụng CS**: Phân tích đệ quy, DP, độ phức tạp (tiết 39).

**Mạch nối**: Truy hồi → Big-O đệ quy → Fibonacci $$O(n)$$ vs $$O(2^{n})$$.

---

## Phần V — Boolean & Đồ thị (Tiết 30–37)

**Nội dung chính**:
- Đại số Boolean, hàm Boole, cổng logic
- Karnaugh, Quine-McCluskey — tối thiểu hóa
- Đồ thị: biểu diễn, BFS, DFS
- Euler, Hamilton, topo sort

**Ứng dụng CS**: Thiết kế mạch, SAT (tiết 43), routing, scheduling.

**Mạch nối**: Boolean → CNF → SAT solver.

---

## Phần VI — Thuật toán, Số học, Cây (Tiết 38–44)

**Nội dung chính**:
- Big-O, $$\Omega$$, $$\Theta$$; phân tích độ phức tạp
- Lý thuyết số: chia hết, GCD, modulo
- Mật mã: RSA, đối xứng vs bất đối xứng
- Quan hệ ↔ CSDL, JOIN
- SAT solver, DPLL
- Cây: duyệt, Huffman, BST

**KT5** (nội dung): Thuật toán, số học, cây — ôn qua bài tập cuối slide.

---

## Mạch kiến thức xuyên suốt

```
Logic → Chứng minh → Đếm → Truy hồi
  ↓         ↓          ↓        ↓
Boolean → SAT    Quan hệ → CSDL
  ↓                    ↓
Đồ thị → BFS/DFS → Cây → BST/Huffman
  ↓
Big-O → Phân tích → P/NP
  ↓
Modulo → RSA → Bảo mật
```

**Một câu**: Toán rời rạc = **ngôn ngữ mô hình hóa** cho CS.

---

## Kỹ năng đã đạt được

- **Mô hình hóa** vấn đề bằng logic, quan hệ, đồ thị, cây
- **Chứng minh** chặt chẽ (trực tiếp, phản chứng, quy nạp)
- **Đếm** và phân tích tổ hợp có căn cứ
- **Phân tích thuật toán** bằng Big-O và độ phức tạp
- **Tối ưu** biểu thức Boolean (Karnaugh, Quine)
- **Ứng dụng** số học modulo, mật mã, CSDL, SAT

---

## Ôn tập qua bài tập slide

Khóa học **không** dành tiết riêng cho luyện thi.

**Cách ôn hiệu quả**:
1. Làm lại **Bài tập ôn tập** cuối mỗi slide (tiết 1–44)
2. Làm bài trong `contents/chapterNN/`
3. Tập trung **định nghĩa + ví dụ + chứng minh ngắn**
4. Giải thích "tại sao" và "ứng dụng ở đâu"

**Nguồn**: 62 bài Jekyll + slide + README.

---

## Hướng tự học tiếp (1/2)

**Automata & Ngôn ngữ hình thức**:
- FA, PDA, Turing machine
- Chomsky hierarchy
- Compiler: lexer, parser

**Lý thuyết đồ thị nâng cao**:
- Cây khung nhỏ nhất (Kruskal, Prim)
- Tô màu đồ thị, planar graphs
- Network flow

---

## Hướng tự học tiếp (2/2)

**Độ phức tạp tính toán**:
- Lớp P, NP, NP-complete
- Bài toán $$P \stackrel{?}{=} NP$$
- Cook-Levin, quy dẫn đa thức

**Formal methods**:
- TLA+, Alloy, Coq, Dafny
- Model checking, theorem proving

**Tài liệu**: Rosen *Discrete Mathematics*, Sipser *Theory of Computation*, CLRS.

---

## Thi cuối kỳ — Lưu ý

- **Thi cuối kỳ** theo **lịch riêng** của nhà trường
- **Không** sử dụng tiết 44–45 cho thi/ôn thi
- Tiết 44: nội dung mới (Cây)
- Tiết 45: tổng kết + feedback (tiết học này)
- Tỷ lệ: **50%** điểm cuối kỳ

**Phạm vi gợi ý**: Toàn bộ 6 phần — trọng tâm định nghĩa, tính toán, chứng minh ngắn, ứng dụng CS.

---

## Phản hồi khóa học

Giúp cải thiện khóa học lần sau:

1. Phần nào **hữu ích nhất** cho bạn?
2. Phần nào cần **thêm ví dụ / thực hành**?
3. Tốc độ giảng: quá nhanh / vừa / quá chậm?
4. Slide vs `contents/` — bạn dùng nguồn nào nhiều hơn?
5. Góp ý tự do

**Liên hệ**: nglelinh@gmail.com

---

## Lời kết

**Toán rời rạc** không phải toán "xa lập trình" — nó là **nền móng**:

- Logic → code đúng
- Đếm → bảo mật, xác suất
- Đồ thị & cây → dữ liệu, thuật toán
- Boolean & SAT → phần cứng, verification
- Số học & RSA → bảo mật thông tin

**Tiếp tục học** — CS là hành trình dài, TRR là bước khởi đầu vững chắc.

---

## Cảm ơn sinh viên!

**Toán Rời Rạc cho Khoa học Máy tính**

- 45 tiết nội dung · 6 phần · v2026.4
- Giảng viên: **Nguyễn Lê Linh**
- Email: nglelinh@gmail.com
