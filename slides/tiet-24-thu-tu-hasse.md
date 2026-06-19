---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Quan hệ Thứ tự + Biểu đồ Hasse

**Toán Rời Rạc — IUH**

Tiết 24 (45 phút)

---

# Mục tiêu

- Quan hệ thứ tự bộ phận (partial order)
- Biểu đồ Hasse
- Thứ tự toàn phần
- Ứng dụng: CSDL, phân cấp, topological sort

---

# Định nghĩa

**Quan hệ thứ tự bộ phận** (Partial Order):
- Phản xạ
- Phản xứng
- Bắc cầu

**Phần tử cực tiểu / cực đại**, min, max, inf, sup.

**Biểu đồ Hasse**: Đồ thị đơn giản hóa của poset (không vẽ các cạnh bắc cầu).

---

# Thứ tự toàn phần (Total Order / Linear Order)

Mọi cặp phần tử đều so sánh được.

---

# Chiều sâu & Liên hệ

**Định lý**: Trong poset hữu hạn luôn tồn tại phần tử cực tiểu / cực đại.

**Liên hệ**:
- Thứ tự ↔ Đồ thị (Hasse là DAG).
- Thứ tự ↔ Quan hệ (tính chất phản xứng).

**Ứng dụng nâng cao**:
- Topological sort trong scheduler.
- Partial order trong type systems / permission.
- Hasse trong visualization của lattice.

---

# Bài tập ôn tập

1. Vẽ Hasse diagram cho tập con của {1,2,3}.
2. Tìm phần tử min/max/inf/sup.
3. (Thách thức) Chứng minh một quan hệ là partial order và vẽ Hasse.

---

# Tiết sau

Tối tiểu hóa hàm Boole.

---

# Câu hỏi?