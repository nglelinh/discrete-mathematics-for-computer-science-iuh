---
layout: post
title: "Đồ thị Euler và Đồ thị Hamilton"
categories: chapter12
date: 2021-01-01
order: 3
required: true
lang: vi
---

# Đồ thị Euler và Đồ thị Hamilton

Một người giao hàng muốn đi qua mọi tuyến đường đúng một lần. Một hệ thống kiểm tra muốn ghé qua mọi liên kết mà không lặp thừa. Ngược lại, có những bài toán không quan tâm đi qua mọi cạnh, mà quan tâm ghé thăm mọi điểm đúng một lần như trong lịch trình du lịch hay tối ưu tuyến thăm khách hàng. Hai nhu cầu đó trông giống nhau, nhưng bản chất lại khác hẳn.

Đó là lý do ta phải phân biệt **đồ thị Euler** và **đồ thị Hamilton**. Một bên nói về việc đi qua mọi cạnh, bên kia nói về việc đi qua mọi đỉnh. Hiểu sự khác nhau này không chỉ quan trọng trong lý thuyết đồ thị mà còn rất sát với các bài toán logistics, routing, thiết kế mạch và tối ưu tổ hợp.

## 1. Đồ thị Euler

**Định nghĩa**:

- **Đường đi Euler**: đường đi đi qua mọi cạnh đúng một lần.
- **Chu trình Euler**: đường đi Euler khép kín.
- **Đồ thị Euler**: đồ thị có chu trình Euler.

## 2. Định lý Euler

**Định lý**: Một đồ thị vô hướng liên thông có chu trình Euler khi và chỉ khi mọi đỉnh đều có bậc chẵn.

**Chứng minh phác thảo**:

- Nếu có chu trình Euler, mỗi khi đi vào một đỉnh bằng một cạnh, ta phải đi ra bằng một cạnh khác. Vì các cạnh được dùng đúng một lần, các cạnh incident với mỗi đỉnh ghép thành từng cặp vào-ra, nên bậc của mỗi đỉnh là chẵn.
- Ngược lại, nếu đồ thị liên thông và mọi bậc đều chẵn, ta có thể bắt đầu đi theo các cạnh chưa dùng cho đến khi quay về đỉnh xuất phát. Nếu còn cạnh chưa dùng, do liên thông sẽ tìm được chu trình phụ và ghép vào chu trình hiện có. Lặp lại đến khi dùng hết cạnh.

**Hệ quả**: Một đồ thị vô hướng liên thông có đường đi Euler không khép kín khi và chỉ khi có đúng hai đỉnh bậc lẻ. Đường đi bắt đầu ở một đỉnh bậc lẻ và kết thúc ở đỉnh bậc lẻ còn lại.

<div class="content-box example-box" markdown="1">
**Ví dụ**: Một đồ thị đường thẳng $A-B-C-D$ có hai đỉnh bậc lẻ là $A$ và $D$, nên có đường đi Euler từ $A$ đến $D$, nhưng không có chu trình Euler.
</div>

## 3. Thuật toán Hierholzer

Thuật toán Hierholzer tìm chu trình Euler:

1. Bắt đầu từ một đỉnh bất kỳ, đi theo các cạnh chưa dùng cho đến khi quay lại đỉnh xuất phát.
2. Nếu còn cạnh chưa dùng, chọn một đỉnh trên chu trình hiện tại còn cạnh chưa dùng.
3. Tạo chu trình phụ từ đỉnh đó và ghép vào chu trình cũ.
4. Lặp đến khi không còn cạnh chưa dùng.

Độ phức tạp có thể đạt $O(V+E)$ nếu biểu diễn danh sách kề tốt.

## 4. Đồ thị Hamilton

**Định nghĩa**:

- **Đường đi Hamilton**: đường đi thăm mọi đỉnh đúng một lần.
- **Chu trình Hamilton**: chu trình thăm mọi đỉnh đúng một lần và quay về đỉnh xuất phát.
- **Đồ thị Hamilton**: đồ thị có chu trình Hamilton.

Khác với Euler, không có điều kiện cần và đủ đơn giản dựa trên bậc đỉnh cho bài toán Hamilton.

## 5. Điều kiện đủ Dirac và Ore

**Định lý Dirac**: Nếu đồ thị đơn có $n\ge3$ đỉnh và mọi đỉnh có bậc ít nhất $n/2$, thì đồ thị có chu trình Hamilton.

**Định lý Ore**: Nếu với mọi cặp đỉnh không kề nhau $u,v$, ta có

$$
\deg(u)+\deg(v)\ge n,
$$

thì đồ thị có chu trình Hamilton.

Các định lý này là điều kiện đủ, không phải điều kiện cần.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học vẽ một đồ thị nhỏ. Công cụ kiểm tra bậc đỉnh để kết luận điều kiện Euler, và thử tìm chu trình Hamilton bằng backtracking.
</div>

## 6. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Euler đi qua **cạnh** đúng một lần; Hamilton đi qua **đỉnh** đúng một lần.
- Điều kiện bậc chẵn là cần và đủ cho chu trình Euler, nhưng không áp dụng cho Hamilton.
- Dirac và Ore chỉ là điều kiện đủ; nếu đồ thị không thỏa, vẫn có thể Hamilton.
- Đường đi Euler có thể lặp lại đỉnh; đường đi Hamilton không được lặp đỉnh.
</div>

## 7. Ứng dụng trong Khoa học Máy tính

Bài toán Euler xuất hiện trong kiểm tra mạch, tối ưu quét cạnh, ghép genome và bài toán người đưa thư Trung Hoa. Bài toán Hamilton liên quan trực tiếp đến Traveling Salesman Problem (TSP), lập lịch, routing và tối ưu hóa tổ hợp. Trong khi Euler có thuật toán đa thức, Hamilton là bài toán NP-complete trong dạng quyết định tổng quát.

```python
def has_euler_circuit(graph):
    return all(len(neighbors) % 2 == 0 for neighbors in graph.values())

g = {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['A', 'C']}
print(has_euler_circuit(g))
```

## Bài tập thực hành

### Bài tập 1

Đồ thị có các bậc đỉnh $2,2,4,4,6$ và liên thông. Có chu trình Euler không?

<details>
<summary>Đáp án</summary>

Có. Đồ thị liên thông và mọi đỉnh đều có bậc chẵn.

</details>

### Bài tập 2

Đồ thị liên thông có đúng bốn đỉnh bậc lẻ. Có đường đi Euler không?

<details>
<summary>Đáp án</summary>

Không. Đường đi Euler chỉ tồn tại khi số đỉnh bậc lẻ là 0 hoặc 2.

</details>

### Bài tập 3

Vì sao bài toán Hamilton thường khó hơn Euler?

<details>
<summary>Đáp án</summary>

Euler có điều kiện bậc đỉnh cần và đủ, dẫn đến thuật toán hiệu quả. Hamilton không có tiêu chuẩn đơn giản như vậy và bài toán quyết định Hamilton là NP-complete.

</details>

## Tóm tắt

- Euler quan tâm đến việc đi qua mọi cạnh đúng một lần.
- Hamilton quan tâm đến việc thăm mọi đỉnh đúng một lần.
- Đồ thị liên thông có chu trình Euler khi và chỉ khi mọi bậc đỉnh chẵn.
- Hamilton có các điều kiện đủ như Dirac và Ore nhưng không có tiêu chuẩn đơn giản tổng quát.
- Ứng dụng gồm routing, TSP, kiểm tra mạch, logistics và tối ưu hóa tổ hợp.
