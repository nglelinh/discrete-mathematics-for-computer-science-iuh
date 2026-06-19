---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Lý thuyết Đồ thị

**Toán Rời Rạc — IUH**

Tiết 37 (45 phút)

---

# Mục tiêu

- Định nghĩa đồ thị, đỉnh, cạnh
- Biểu diễn đồ thị
- Các khái niệm cơ bản: đường đi, chu trình, liên thông
- Ứng dụng mạng và social

---

# Định nghĩa + Tính chất sâu

**Đồ thị** G = (V, E)
- V: tập đỉnh (vertices)
- E: tập cạnh (edges) — có thể là tập con của V × V

**Các loại quan trọng**:
- Vô hướng (undirected) / Có hướng (directed)
- Có trọng số / Không trọng số
- Đơn đồ thị / Đa đồ thị / Vòng lặp

**Độ** của đỉnh: số cạnh liên kết.

**Đường đi (path)**, **Chu trình (cycle)**, **Liên thông (connected)**.

**Định lý cơ bản**:
- Trong đồ thị vô hướng, tổng bậc các đỉnh = 2 |E| (Handshaking lemma).

---

# Biểu diễn + Hiệu quả

- Ma trận kề (Adjacency Matrix): O(V²) bộ nhớ, kiểm tra cạnh nhanh O(1)
- Danh sách kề (Adjacency List): O(V + E) bộ nhớ, duyệt láng giềng hiệu quả

---

# Thuật toán cơ bản + Phân tích

- **BFS**: Tìm đường ngắn nhất không trọng số. Độ phức tạp O(V + E)
- **DFS**: Phát hiện chu trình, sắp xếp topo. O(V + E)
- **Dijkstra**: Đường ngắn nhất có trọng số không âm. O((V+E) log V) với heap

---

# Ứng dụng nâng cao trong CNTT

- Mạng máy tính & Routing (BFS/DFS, shortest path)
- Mạng xã hội: phát hiện cộng đồng, độ trung tâm
- Lịch trình công việc: topological sort (sắp xếp công việc phụ thuộc)
- Cơ sở dữ liệu: biểu diễn quan hệ, query optimization
- Trí tuệ nhân tạo: tìm kiếm trạng thái (game tree, planning)

**Edge case quan trọng**:
- Đồ thị không liên thông
- Đồ thị có chu trình âm (Bellman-Ford cần thiết)

---

# Chiều sâu & Liên hệ (1)

**Định lý chính**:
Handshaking: ∑ deg(v) = 2|E|.

**Edge case**:
Không liên thông, chu trình âm.

---

# Chiều sâu & Liên hệ (2)

**Liên hệ**:
- Đồ thị ↔ Truy hồi.
- Đồ thị ↔ Đếm.

**Ứng dụng nâng cao**:
- Mạng xã hội (PageRank).
- Compiler topo sort.
- AI search.

---

# Bài tập ôn tập (1/2)

1. Vẽ đồ thị từ ma trận kề.

2. Thực hiện BFS/DFS.

---

# Bài tập ôn tập (2/2)

3. (Thách thức) Chứng minh đồ thị có Euler cycle nếu tất cả đỉnh bậc chẵn.

---

# Tiết sau

Ứng dụng đồ thị nâng cao.

---

# Câu hỏi?