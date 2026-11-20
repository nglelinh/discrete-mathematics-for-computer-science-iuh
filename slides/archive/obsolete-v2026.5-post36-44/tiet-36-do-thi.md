---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Đồ thị — Định nghĩa & Biểu diễn

**Toán Rời Rạc**

Tiết 36 (45 phút) — Graph Theory Basics

---

## Mục tiêu tiết học

- Định nghĩa đồ thị $$G = (V, E)$$ và các loại đồ thị
- Hiểu bậc đỉnh, đường đi, chu trình, liên thông
- Biểu diễn bằng ma trận kề và danh sách kề
- So sánh hiệu quả bộ nhớ và thao tác
- Mô hình hóa bài toán CNTT bằng đồ thị

---

## Định nghĩa Đồ thị

**Đồ thị** (Graph) $$G = (V, E)$$:

- $$V$$: tập **đỉnh** (vertices / nodes)
- $$E$$: tập **cạnh** (edges) — thường $$E \subseteq V \times V$$

**Ví dụ**: Mạng xã hội — đỉnh = người, cạnh = quan hệ bạn bè.

**Mô hình hóa**: Nhiều bài toán CNTT → đồ thị.

---

## Các loại đồ thị

| Loại | Đặc điểm |
|:---|:---|
| **Vô hướng** | Cạnh không có hướng: $$\{u,v\}$$ |
| **Có hướng** | Cạnh có hướng: $$(u,v)$$ |
| **Có trọng số** | Mỗi cạnh có cost/weight |
| **Đơn đồ thị** | Không cạnh lặp, không khuyên |
| **Đa đồ thị** | Cho phép nhiều cạnh giữa 2 đỉnh |

---

## Bậc đỉnh (Degree)

**Đồ thị vô hướng**: $$\deg(v)$$ = số cạnh nối với $$v$$.

**Đồ thị có hướng**:
- **Bậc vào** $$\deg^-(v)$$: số cạnh vào $$v$$
- **Bậc ra** $$\deg^+(v)$$: số cạnh ra từ $$v$$

**Đỉnh cô lập**: $$\deg(v) = 0$$.

---

## Định lý Bắt tay (Handshaking Lemma)

**Đồ thị vô hướng**:

$$\sum_{v \in V} \deg(v) = 2|E|$$

**Chứng minh ý tưởng**: Mỗi cạnh đóng góp 2 vào tổng bậc (hai đầu).

**Hệ quả**: Số đỉnh bậc lẻ là **chẵn**.

**Ví dụ**: 5 đỉnh, tổng bậc = 12 → $$|E| = 6$$.

---

## Đường đi và Chu trình

**Đường đi** (path): Dãy đỉnh $$v_0, v_1, \ldots, v_k$$ với cạnh nối liên tiếp.

**Đường đi đơn**: Không lặp đỉnh.

**Chu trình** (cycle): Đường đi đóng — $$v_0 = v_k$$, $$k \ge 3$$.

**Đồ thị liên thông**: Mọi cặp đỉnh có đường đi nối (vô hướng).

---

## Đồ thị con và Đồ thị đầy đủ

**Đồ thị con**: $$G' = (V', E')$$ với $$V' \subseteq V$$, $$E' \subseteq E$$.

**Đồ thị đầy đủ** $$K_n$$: $$n$$ đỉnh, mọi cặp có cạnh — có $$|E| = \binom{n}{2}$$.

**Đồ thị hai phía** (bipartite): $$V = A \cup B$$, cạnh chỉ nối $$A$$–$$B$$.

**Ứng dụng**: Matching, phân công task, tô màu.

---

## Ma trận kề (Adjacency Matrix)

Đồ thị $$n$$ đỉnh — ma trận $$A_{n \times n}$$:

$$A[i][j] = \begin{cases} 1 & \text{nếu có cạnh } (i,j) \\ 0 & \text{ngược lại} \end{cases}$$

**Vô hướng**: Ma trận **đối xứng**.

**Có trọng số**: $$A[i][j] = w$$ (trọng số cạnh).

**Kiểm tra cạnh**: $$O(1)$$; **Bộ nhớ**: $$O(V^{2})$$.

---

## Ví dụ Ma trận kề

Đồ thị 4 đỉnh: cạnh (0,1), (0,2), (1,2), (2,3)

```
    0  1  2  3
0 [ 0  1  1  0 ]
1 [ 1  0  1  0 ]
2 [ 1  1  0  1 ]
3 [ 0  0  1  0 ]
```

**Duyệt láng giềng đỉnh $$i$$**: Quét cả hàng $$i$$ — $$O(V)$$.

---

## Danh sách kề (Adjacency List)

Mỗi đỉnh lưu danh sách đỉnh kề:

```
0 → [1, 2]
1 → [0, 2]
2 → [0, 1, 3]
3 → [2]
```

**Bộ nhớ**: $$O(V + E)$$

**Duyệt láng giềng**: $$O(\deg(v))$$ — hiệu quả khi đồ thị **thưa**.

---

## So sánh biểu diễn

| Tiêu chí | Ma trận kề | Danh sách kề |
|:---|:---|:---|
| Bộ nhớ | $$O(V^{2})$$ | $$O(V+E)$$ |
| Kiểm tra cạnh | $$O(1)$$ | $$O(\deg)$$ |
| Duyệt láng giềng | $$O(V)$$ | $$O(\deg)$$ |
| Đồ thị dày | Tốt | Kém hơn |
| Đồ thị thưa | Lãng phí | **Tốt** |

**Thực tế**: Hầu hết mạng thực → thưa → dùng danh sách kề.

---

## Ứng dụng mô hình hóa CNTT

| Bài toán | Đỉnh | Cạnh |
|:---|:---|:---|
| Mạng máy tính | Router/Switch | Kết nối |
| Mạng xã hội | Người dùng | Quan hệ |
| CSDL | Bảng | Foreign key |
| Git | Commit | Parent |
| Dependency | Package | Phụ thuộc |

**Tư duy**: Chọn $$V$$, $$E$$ phù hợp → áp dụng thuật toán đồ thị.

---

## Code — Biểu diễn đồ thị

```python
# Danh sách kề
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

# Kiểm tra cạnh (0, 2)
has_edge = 2 in graph[0]  # True
```

**Ma trận kề**: Dùng `numpy` hoặc list 2D cho đồ thị nhỏ/dày.

---

## Thực hành 1

Cho đồ thị 5 đỉnh, cạnh: (0,1), (1,2), (2,3), (3,4), (0,4).

1. Vẽ đồ thị
2. Tính bậc mỗi đỉnh
3. Kiểm tra Handshaking Lemma

---

## Thực hành 2

Với đồ thị trên:

1. Viết ma trận kề
2. Viết danh sách kề
3. Đồ thị có liên thông không? Có chu trình không?

---

## Tóm tắt Tiết 36

- **Đồ thị**: $$G = (V,E)$$ — mô hình hóa quan hệ
- **Bậc, đường đi, chu trình, liên thông** — khái niệm cơ bản
- **Handshaking**: $$\sum \deg(v) = 2|E|$$
- **Ma trận kề**: $$O(V^{2})$$, kiểm tra cạnh $$O(1)$$
- **Danh sách kề**: $$O(V+E)$$, tốt cho đồ thị thưa

---

## Liên hệ

**Định lý chính**: Handshaking Lemma — nền cho Euler (tiết 37).

**Edge case**: Đồ thị rỗng ($$E = \emptyset$$); đỉnh cô lập; đồ thị không liên thông.

**Liên hệ**: Đồ thị ↔ Truy hồi ↔ BFS/DFS (tiết 37) ↔ Thuật toán (ch14).

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Định nghĩa đồ thị, đường đi, chu trình, liên thông.

2. **Handshaking**: Đồ thị 6 đỉnh có tổng bậc 14. Có bao nhiêu cạnh?

3. **Biểu diễn**: Cho ma trận kề 3×3, viết danh sách kề tương ứng.

---

## Bài tập ôn tập (2/2)

4. **Mô hình hóa**: Mô hình hóa mạng 4 máy tính bằng đồ thị. Chọn biểu diễn phù hợp và giải thích.

5. **Bài 5**: $$K_5$$ có bao nhiêu cạnh? Chứng minh bằng công thức tổ hợp.
