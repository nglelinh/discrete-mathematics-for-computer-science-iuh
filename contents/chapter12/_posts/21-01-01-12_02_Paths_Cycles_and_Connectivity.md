---
layout: post
title: "Đường đi, Chu trình và Tính liên thông"
categories: chapter12
date: 2021-01-01
order: 2
required: true
lang: vi
---

# Đường đi, Chu trình và Tính liên thông

Biết một đồ thị có những đỉnh và cạnh vẫn chưa nói được nhiều nếu ta không hiểu chúng liên kết thành dòng chảy ra sao. Một mạng có thể rất lớn nhưng bị chia cắt; một hệ thống có thể tồn tại chu trình gây lặp vô hạn; một ứng dụng dẫn đường cần biết liệu có đi từ A đến B được không trước khi bàn chuyện tối ưu.

Vì thế, các khái niệm **đường đi, chu trình, liên thông** là lớp từ vựng đầu tiên để “đọc” một đồ thị. Chúng giúp ta mô tả khả năng tiếp cận, phát hiện vòng lặp, hiểu cấu trúc mạng và chuẩn bị cho các bài toán quan trọng hơn như Euler, Hamilton, shortest path và spanning tree.

## 1. Đường đi (Path)

**Định nghĩa**: **Đường đi** từ đỉnh $v_0$ đến đỉnh $v_k$ trong đồ thị là một dãy các đỉnh $v_0, v_1, \ldots, v_k$ sao cho $\{v_{i-1}, v_i\}$ (hoặc $(v_{i-1}, v_i)$ trong đồ thị có hướng) là một cạnh của đồ thị với mọi $i = 1, 2, \ldots, k$.

- **Độ dài** (length) của đường đi: số cạnh $k$
- **Đường đi đơn** (simple path): không có đỉnh nào lặp lại
- Ký hiệu đường đi độ dài $k$: $v_0 - v_1 - \cdots - v_k$

<div class="content-box example-box" markdown="1">
**Ví dụ**: Đồ thị $G$ với các cạnh: $\{A,B\}, \{B,C\}, \{C,D\}, \{A,D\}$

- $A-B-C-D$: đường đi độ dài 3 (đường đi đơn)
- $A-D-C-B$: đường đi độ dài 3 = $A-D-C-B$
</div>

## 2. Chu trình (Cycle / Circuit)

**Định nghĩa**: **Chu trình** là một đường đi $v_0, v_1, \ldots, v_k$ trong đó $v_0 = v_k$ và $k \geq 3$, và $v_1, \ldots, v_k$ đều phân biệt (không lặp đỉnh trừ điểm đầu-cuối).

- **Chu trình đơn** (simple cycle): không có đỉnh nào lặp lại ngoài điểm đầu-cuối
- **Độ dài chu trình**: số cạnh $k$

<div class="content-box example-box" markdown="1">
**Ví dụ**: Với các cạnh $\{A,B\}, \{B,C\}, \{C,A\}$, chu trình $A-B-C-A$ có độ dài 3.
</div>

## 3. Tính liên thông

**Định nghĩa**: Đồ thị được gọi là **liên thông** nếu có đường đi giữa mọi cặp đỉnh.

**Thành phần liên thông** (connected component): tập cực đại các đỉnh sao cho bất kỳ hai đỉnh nào trong tập cũng có đường đi nối chúng.

<div class="content-box example-box" markdown="1">
**Ví dụ**: Đồ thị với các cạnh $\{A,B\}, \{B,C\}, \{D,E\}$ có hai thành phần liên thông: $\{A,B,C\}$ và $\{D,E\}$.
</div>

## 4. Thuật toán duyệt đồ thị

### 4.1. Tìm kiếm theo chiều rộng (BFS)

BFS khám phá đồ thị theo "lớp": bắt đầu từ một đỉnh, thăm tất cả hàng xóm, rồi thăm hàng xóm của hàng xóm, v.v.

**Độ phức tạp**: $O(V + E)$ với $V$ đỉnh và $E$ cạnh.

**Ứng dụng**: Tìm đường đi ngắn nhất trong đồ thị không trọng số, kiểm tra liên thông.

### 4.2. Tìm kiếm theo chiều sâu (DFS)

DFS khám phá đồ thị bằng cách đi sâu nhất có thể trước khi quay lại.

**Độ phức tạp**: $O(V + E)$.

**Ứng dụng**: Phát hiện chu trình, sắp xếp tô pô, tìm thành phần liên thông mạnh.

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học chọn một đỉnh bắt đầu. Công cụ hiển thị quá trình BFS và DFS song song, tô màu các đỉnh theo thứ tự thăm.
</div>

## 5. Cầu và điểm khớp

**Cầu** (bridge): cạnh mà nếu xóa đi sẽ làm tăng số thành phần liên thông.

**Điểm khớp** (articulation point): đỉnh mà nếu xóa đi sẽ làm tăng số thành phần liên thông.

Các khái niệm này quan trọng trong phân tích độ bền của mạng.

## 6. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Đường đi đơn không có cạnh lặp lại, nhưng chu trình đơn không có đỉnh lặp lại (ngoài đầu-cuối).
- Liên thông là tính chất của toàn bộ đồ thị; một đỉnh không thể "liên thông" một mình.
- BFS tìm đường đi ngắn nhất trong đồ thị không trọng số, nhưng không hoạt động với trọng số âm.
- Một đồ thị có thể có nhiều thành phần liên thông; mỗi thành phần là liên thông.
</div>

## 7. Ứng dụng trong Khoa học Máy tính

Trong mạng máy tính, BFS và DFS được dùng để tìm đường định tuyến, phát hiện vòng lặp, và kiểm tra khả năng kết nối. Trong phân tích mạng xã hội, tính liên thông giúp xác định các cộng đồng. Trong hệ điều hành, phát hiện deadlock liên quan đến tìm chu trình trong đồ thị chờ tài nguyên.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B'], 'D': ['A']}
bfs(graph, 'A')
```

## Bài tập thực hành

### Bài tập 1

Cho đồ thị với cạnh $\{A,B\}, \{B,C\}, \{C,D\}, \{D,A\}, \{B,D\}$. Liệt kê tất cả chu trình đơn độ dài 3.

<details>
<summary>Đáp án</summary>

$A-B-D-A$ và $B-C-D-B$.

</details>

### Bài tập 2

Một đồ thị có 5 đỉnh và 4 cạnh. Nó có thể liên thông không?

<details>
<summary>Đáp án</summary>

Có. Ví dụ: cạnh $\{A,B\}, \{B,C\}, \{C,D\}, \{D,E\}$ tạo thành một đường đi liên thông.

</details>

### Bài tập 3

Tìm tất cả cầu trong đồ thị với cạnh $\{A,B\}, \{B,C\}, \{C,D\}, \{D,A\}, \{C,E\}$.

<details>
<summary>Đáp án</summary>

Cạnh $\{C,E\}$ là cầu vì xóa nó sẽ cô lập đỉnh $E$.

</details>

## Tóm tắt

- **Đường đi** là dãy đỉnh nối tiếp bằng cạnh; **chu trình** là đường đi khép kín.
- **Tính liên thông** đo khả năng đi từ bất kỳ đỉnh nào đến bất kỳ đỉnh nào.
- **BFS** và **DFS** là hai thuật toán duyệt cơ bản với độ phức tạp $O(V+E)$.
- **Cầu** và **điểm khớp** là các yếu tố quan trọng trong phân tích độ bền mạng.
- Trong CS, các khái niệm này ứng dụng trong định tuyến, phát hiện deadlock, và phân tích mạng xã hội.
