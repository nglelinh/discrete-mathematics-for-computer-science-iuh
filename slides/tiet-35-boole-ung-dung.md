---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Boolean — Ứng dụng chip

**Toán Rời Rạc**

Tiết 35 (45 phút) — From Boole to Modern Chips

---

## Mục tiêu tiết học

- Truy vết lịch sử: Boole → Shannon → máy tính số
- Hiểu từ truth table đến silicon
- Nhận biết vai trò SAT solvers trong công nghiệp
- Giới thiệu FPGA và logic khả trình
- Liên hệ tối thiểu hóa logic với thiết kế chip thực tế

---

## Hành trình lịch sử

**1854** — George Boole: *Laws of Thought* — đại số hóa logic.

**1937** — Claude Shannon (MIT): Luận văn mạch relay = Boole.

**1947** — Transistor → cổng logic trên silicon.

**Hôm nay**: Hàng tỷ transistor — mỗi cái là một "câu hỏi" Boole.

---

## Shannon — Cú ghép ý tưởng vĩ đại

Mạch relay: **đóng/mở** ↔ **1/0** ↔ **đúng/sai**

| Khái niệm | Mạch | Boole |
|:---|:---|:---|
| Công tắc đóng | Dòng chạy | 1 |
| Công tắc mở | Không dòng | 0 |
| Nối tiếp | AND | $$\cdot$$ |
| Song song | OR | $$+$$ |

**Hệ quả**: Logic trở thành **điện** — nền máy tính số.

---

## Từ Truth Table đến Silicon

**Bước thiết kế số**:

1. Yêu cầu (bộ cộng, ALU, decoder…)
2. Bảng chân trị / biểu thức Boole
3. Tối thiểu hóa (K-map, Quine, Espresso)
4. Sơ đồ mạch (cổng logic)
5. Layout trên chip (transistor)

**Mỗi bước tối ưu** → ít transistor, ít điện, ít trễ.

---

## Vì sao tối giản logic quan trọng?

Biểu thức ngắn hơn ⟹

- **Ít cổng** → ít transistor
- **Ít điện năng** — quan trọng mobile/AI chip
- **Độ trễ thấp** — tần số xung cao hơn
- **Diện tích nhỏ** — chi phí sản xuất thấp

**Ví dụ**: ALU 64-bit có thể cần **hàng nghìn** cổng cho một phép cộng.

---

## Công cụ EDA (Electronic Design Automation)

**Quy trình hiện đại**:

```
HDL (Verilog/VHDL) → Synthesis → Place & Route → Chip
```

**Tối thiểu hóa bên trong**:
- **Espresso**: Heuristic nhanh (thay Quine cho chip lớn)
- **ABC**: Hệ thống tối ưu logic mã nguồn mở

**Bạn viết**: `assign y = a & b | c;` — tool tự tối ưu.

---

## SAT Solvers — Từ lý thuyết đến công nghiệp

**Bài toán SAT**: Tồn tại gán true/false cho biến làm CNF **thỏa mãn**?

**Ứng dụng thực tế**:
- Hardware verification (kiểm chứng chip)
- Scheduling, planning
- Package dependency (npm, apt)
- Test generation, cryptanalysis

**Ý tưởng**: Mã hóa bài toán → CNF → giao cho SAT solver.

---

## Ví dụ SAT trong thực tế

**Kiểm chứng mạch**: "Có input nào làm output sai không?"

→ Chuyển thành CNF → SAT solver tìm counterexample.

**Dependency resolution**: "Có cách cài package không xung đột?"

→ Mỗi package = biến Boole; xung đột = mệnh đề cấm.

**SAT là NP-complete** — nhưng solver hiện đại rất mạnh trên thực tế.

---

## FPGA — Logic khả trình

**FPGA** (Field-Programmable Gate Array): Chip có thể **lập trình lại** sau sản xuất.

**Ứng dụng**:
- Prototyping nhanh (thay ASIC)
- Networking, DSP, embedded
- Low-latency finance, research hardware

**Lõi vẫn là Boole**: Synthesis tool chuyển HDL → mảng LUT (lookup table) Boole.

---

## LUT và Boolean trên FPGA

**LUT** (Look-Up Table): Bảng chân trị nhỏ được **hard-code** vào chip.

Ví dụ LUT 4-input: lưu $$2^{4} = 16$$ bit đầu ra → thực hiện **bất kỳ** hàm 4 biến.

**Kết nối LUT** → mạch lớn hơn (adder, multiplier, processor soft-core).

**Tối thiểu hóa**: Giảm số LUT = tiết kiệm tài nguyên FPGA.

---

## Ứng dụng phần mềm — Compiler & DB

**Compiler optimization**:
```c
if ((a && b) || (a && c))  →  if (a && (b || c))  // hấp thụ
```

**Query optimizer** (SQL): Chuẩn hóa WHERE → chọn index plan nhanh nhất.

**Bitmask / ACL**: `permissions & WRITE` — đánh giá biểu thức Boole trên hàng triệu bản ghi.

---

## Ứng dụng bảo mật & AI

- **Cryptography**: Hàm Boole trong S-box (AES), phân tích algebraic
- **Formal verification**: Coq, Dafny — chứng minh tính đúng mạch
- **Neural network**: Perceptron = hàm Boole với trọng số
- **Model checking**: Kiểm tra FSM bằng BDD/SAT

**Chung**: Boolean là **ngôn ngữ** mô tả hành vi rời rạc.

---

## Thực hành 1

Cho biểu thức: `F = (A'B + AB')(C + D')`

a) Vẽ mạch cổng
b) Ước lượng số cổng NOT, AND, OR
c) Đề xuất tối thiểu hóa

---

## Thực hành 2

Mô tả SAT: "Phân công 3 task cho 2 CPU sao cho không trùng lịch."

Gợi ý: Mỗi biến = task $$i$$ trên CPU $$j$$. Viết 2 ràng buộc CNF.

---

## Tóm tắt Tiết 35

- **Boole (1854) → Shannon (1937) → Transistor → Chip**
- Tối giản logic = **tiết kiệm vật lý** trên silicon
- **EDA**: Espresso, synthesis từ HDL
- **SAT**: Công cụ công nghiệp — verification, scheduling, dependencies
- **FPGA**: Boole khả trình qua LUT

---

## Liên hệ

**Định lý thực dụng**: Mọi hàm Boole có thể hiện thực bằng mạch tổ hợp hữu hạn.

**Edge case**: SAT NP-complete — instance lớn vẫn khó; heuristic EDA cho chip.

**Liên hệ**: Chương 13 (Boole) ↔ Chương 1 (SAT, tiết 43) ↔ Đồ thị (tiết 36–37).

---

## Bài tập ôn tập (1/2)

1. **Lịch sử**: Shannon đóng góp gì vào khoa học máy tính?

2. **Thiết kế**: Liệt kê 5 bước từ yêu cầu đến chip.

3. **SAT**: Phát biểu bài toán SAT. Cho một ví dụ ứng dụng ngoài mạch số.

---

## Bài tập ôn tập (2/2)

4. **FPGA**: Giải thích LUT 3-input lưu trữ gì. Có bao nhiêu hàm Boole 3 biến khác nhau?

5. **Bài 5**: So sánh ASIC vs FPGA. Khi nào tối thiểu hóa Boole quan trọng nhất?
