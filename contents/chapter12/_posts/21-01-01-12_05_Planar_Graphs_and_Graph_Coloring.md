---
layout: post
title: "Đồ thị Phẳng và Tô màu Đồ thị"
categories: chapter12
date: 2021-01-01
order: 5
required: true
lang: vi
---

# Đồ thị Phẳng và Tô màu Đồ thị

Có những bài toán mạng không chỉ quan tâm ai nối với ai, mà còn quan tâm cách biểu diễn hoặc phân bổ tài nguyên sao cho không xung đột. Bản đồ vùng lãnh thổ, thiết kế mạch, lập lịch thi, gán tần số vô tuyến, tất cả đều dẫn đến những câu hỏi kiểu này.


Đồ thị là mô hình chuẩn cho mạng, phụ thuộc và đường đi, nên mỗi khái niệm ở đây đều có thể nối trực tiếp sang bài toán thực tế trong phần mềm.
**Đồ thị phẳng** hỏi liệu ta có thể vẽ đồ thị trên mặt phẳng mà không để các cạnh cắt nhau hay không. **Tô màu đồ thị** hỏi cần bao nhiêu màu để các đỉnh kề nhau không trùng màu. Hai chủ đề nghe hình học, nhưng lại có rất nhiều ứng dụng hệ thống và tối ưu.

Điểm hấp dẫn là chúng biến một vấn đề trực quan thành một đối tượng toán học có thể phân tích chặt chẽ. Từ đó, ta hiểu rõ hơn giới hạn của cấu trúc mạng và chi phí tối thiểu để tránh xung đột.

Trong bài này, chúng ta sẽ tiếp cận hai khái niệm này như những công cụ mô hình hóa thực tế, rồi dần đi vào các kết quả nền tảng của chúng.

## 1. Đồ thị phẳng

**Định nghĩa**: Một đồ thị được gọi là **phẳng** (planar) nếu có thể vẽ nó trên mặt phẳng sao cho các cạnh chỉ gặp nhau tại đỉnh chung, không cắt nhau ở điểm giữa.

Một cách vẽ như vậy gọi là **phép nhúng phẳng** (planar embedding).

## 2. Công thức Euler

**Định lý**: Nếu một đồ thị phẳng liên thông có $v$ đỉnh, $e$ cạnh và $f$ miền (faces, kể cả miền ngoài), thì

$$
v-e+f=2.
$$

**Chứng minh phác thảo**: Với cây liên thông, $e=v-1$ và chỉ có một miền, nên $v-e+f=v-(v-1)+1=2$. Mỗi khi thêm một cạnh không phá tính phẳng và tạo chu trình mới, số cạnh tăng 1 và số miền cũng tăng 1, nên $v-e+f$ không đổi.

## 3. Hệ quả về số cạnh

Nếu $G$ là đồ thị phẳng đơn liên thông với $v\ge3$, thì

$$
e\le3v-6.
$$

Lý do: mỗi miền có ít nhất 3 cạnh biên, và mỗi cạnh nằm trên biên của nhiều nhất hai miền, nên $3f\le2e$. Kết hợp với Euler cho kết quả.

Nếu đồ thị không có chu trình độ dài 3, ta có hệ quả mạnh hơn:

$$
e\le2v-4.
$$

## 4. Không phẳng: $K_5$ và $K_{3,3}$

- $K_5$ có $v=5,e=10$, nhưng $3v-6=9$, nên không phẳng.
- $K_{3,3}$ có $v=6,e=9$ và không có tam giác; nếu phẳng thì phải có $e\le2v-4=8$, mâu thuẫn.

**Định lý Kuratowski**: Một đồ thị là phẳng khi và chỉ khi nó không chứa một phân chia con của $K_5$ hoặc $K_{3,3}$.

## 5. Tô màu đỉnh

**Định nghĩa**: Một **tô màu đỉnh hợp lệ** gán màu cho mỗi đỉnh sao cho hai đỉnh kề nhau có màu khác nhau.

**Sắc số** $\chi(G)$ là số màu ít nhất cần để tô màu hợp lệ đồ thị $G$.

**Ví dụ**:

- $\chi(K_n)=n$.
- Chu trình chẵn có sắc số 2.
- Chu trình lẻ có sắc số 3.

## 6. Định lý bốn màu

**Định lý bốn màu**: Mọi đồ thị phẳng đều có thể tô màu bằng nhiều nhất 4 màu.

Định lý này nổi tiếng vì chứng minh năm 1976 của Appel và Haken là một trong những chứng minh lớn đầu tiên sử dụng máy tính.

**Định lý năm màu**: Mọi đồ thị phẳng đều tô được bằng nhiều nhất 5 màu. Định lý này có chứng minh ngắn hơn và thường được trình bày trong các khóa cơ bản.

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học vẽ đồ thị nhỏ, công cụ kiểm tra điều kiện phẳng sơ bộ và cho phép tô màu đỉnh, cảnh báo khi hai đỉnh kề nhau cùng màu.

<div data-demo="graph-coloring-interactive"></div>
</div>
<script src="{{ '/public/js/graph-coloring-interactive.js' | relative_url }}"></script>

## 7. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Đồ thị phẳng không có nghĩa là mọi cách vẽ của nó đều không cắt nhau; chỉ cần tồn tại một cách vẽ phẳng.
- Công thức Euler chỉ áp dụng trực tiếp cho đồ thị phẳng liên thông.
- $e\le3v-6$ là điều kiện cần, không phải điều kiện đủ cho tính phẳng.
- Định lý bốn màu nói về đồ thị phẳng, không phải mọi đồ thị.
</div>

## 8. Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Đồ thị phẳng xuất hiện trong thiết kế mạch VLSI, mạng giao thông, hình học tính toán và mesh trong đồ họa. Tô màu đồ thị được dùng trong lập lịch thi, cấp phát thanh ghi trong trình biên dịch, phân bổ tần số vô tuyến và giải Sudoku. Nhiều biến thể tô màu là NP-hard, nên thuật toán heuristic rất quan trọng trong thực tế.

```python
def greedy_coloring(graph):
    colors = {}
    for v in graph:
        used = {colors[u] for u in graph[v] if u in colors}
        color = 0
        while color in used:
            color += 1
        colors[v] = color
    return colors
```

## Bài tập thực hành

### Bài tập 1

Một đồ thị phẳng liên thông có 8 đỉnh và 12 cạnh. Nó có bao nhiêu miền?

<details>
<summary>Đáp án</summary>

Theo Euler: $v-e+f=2$, nên $8-12+f=2$, suy ra $f=6$.

</details>

### Bài tập 2

Vì sao $K_5$ không phẳng?

<details>
<summary>Đáp án</summary>

$K_5$ có $v=5,e=10$. Nếu phẳng thì $e\le3v-6=9$, mâu thuẫn.

</details>

### Bài tập 3

Sắc số của chu trình 5 đỉnh là bao nhiêu?

<details>
<summary>Đáp án</summary>

Chu trình lẻ cần 3 màu, nên $\chi(C_5)=3$.

</details>

## Tóm tắt

- Đồ thị phẳng là đồ thị có thể vẽ không có cạnh cắt nhau.
- Công thức Euler: $v-e+f=2$ cho đồ thị phẳng liên thông.
- $K_5$ và $K_{3,3}$ là hai mô hình không phẳng cơ bản.
- Sắc số là số màu ít nhất để tô màu đỉnh hợp lệ.
- Ứng dụng gồm thiết kế mạch, lập lịch, cấp phát thanh ghi và phân bổ tài nguyên.
