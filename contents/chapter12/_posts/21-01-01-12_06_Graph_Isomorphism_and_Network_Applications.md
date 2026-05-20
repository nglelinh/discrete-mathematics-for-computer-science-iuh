---
layout: post
title: "Đẳng cấu Đồ thị và Ứng dụng Mạng"
categories: chapter12
date: 2021-01-01
order: 6
required: false
lang: vi
---

# Đẳng cấu Đồ thị và Ứng dụng Mạng

Hai mạng có thể trông hoàn toàn khác nhau trên hình vẽ nhưng thực ra cùng một cấu trúc, chỉ khác cách đặt tên đỉnh. Ngược lại, hai sơ đồ nhìn na ná nhau có thể khác bản chất ở một liên kết nhỏ. Trong phân tích mạng, hóa học tính toán, an toàn thông tin hay tối ưu hóa cơ sở dữ liệu, việc nhận ra “cùng cấu trúc hay không” là một câu hỏi rất quan trọng.

Đó chính là tinh thần của **đẳng cấu đồ thị**. Từ đây, lý thuyết đồ thị bước gần hơn đến ứng dụng mạng thực tế: so khớp cấu trúc, phát hiện mẫu, mô hình hóa hệ thống liên kết và hiểu vì sao hình thức bên ngoài không phải lúc nào cũng phản ánh đúng bản chất bên trong.

## 1. Định nghĩa đẳng cấu

Hai đồ thị $G_1=(V_1,E_1)$ và $G_2=(V_2,E_2)$ được gọi là **đẳng cấu** nếu tồn tại một song ánh

$$
f:V_1\to V_2
$$

sao cho với mọi $u,v\in V_1$,

$$
\{u,v\}\in E_1 \iff \{f(u),f(v)\}\in E_2.
$$

Nói cách khác, $f$ là phép đổi tên đỉnh bảo toàn quan hệ kề nhau.

## 2. Ví dụ trực quan

Nếu một đồ thị là hình vuông $A-B-C-D-A$ và đồ thị khác là chu trình $1-2-3-4-1$, chúng đẳng cấu qua ánh xạ $A\mapsto1$, $B\mapsto2$, $C\mapsto3$, $D\mapsto4$.

Điều quan trọng: hình vẽ không quyết định đẳng cấu. Cấu trúc cạnh mới quyết định.

## 3. Bất biến đồ thị

**Bất biến** là đại lượng không đổi dưới đẳng cấu. Nếu hai đồ thị có bất biến khác nhau, chúng chắc chắn không đẳng cấu.

Các bất biến phổ biến:

| Bất biến | Ý nghĩa |
|----------|---------|
| Số đỉnh | $|V|$ phải bằng nhau |
| Số cạnh | $|E|$ phải bằng nhau |
| Dãy bậc | Danh sách bậc sắp xếp tăng/giảm |
| Số thành phần liên thông | Cấu trúc liên thông phải khớp |
| Số chu trình độ dài 3 | Số tam giác phải khớp |
| Sắc số | Nếu biết được, phải bằng nhau |

<div class="content-box warning-box" markdown="1">
**Lưu ý**: Bất biến giống nhau không đảm bảo đẳng cấu. Chúng chỉ giúp bác bỏ nhanh trường hợp không đẳng cấu.
</div>

## 4. Ma trận kề và đẳng cấu

Nếu $A_G$ là ma trận kề của $G$, thì đổi tên đỉnh tương ứng với hoán vị hàng và cột của ma trận. Hai đồ thị đẳng cấu khi tồn tại ma trận hoán vị $P$ sao cho

$$
A_{G_2}=P^T A_{G_1} P.
$$

Cách nhìn này rất quan trọng trong tính toán vì bài toán đẳng cấu trở thành bài toán tìm hoán vị phù hợp.

## 5. Độ phức tạp

Bài toán Graph Isomorphism (GI) hỏi: cho hai đồ thị, chúng có đẳng cấu không?

GI thuộc NP, nhưng chưa biết là P hay NP-complete trong mô hình cổ điển. Năm 2015, László Babai công bố thuật toán thời gian quasi-polynomial cho GI, một bước tiến lớn trong lý thuyết độ phức tạp.

## 6. Ứng dụng mạng

Trong phân tích mạng, ta thường tìm **motif** — các mẫu con nhỏ xuất hiện lặp lại. Hai motif được xem là giống nhau nếu đẳng cấu. Ứng dụng:

- Phân tích mạng xã hội: tìm cấu trúc nhóm bạn, cộng đồng nhỏ.
- Sinh học tính toán: phát hiện motif trong mạng protein.
- An ninh mạng: nhận diện mẫu tấn công có cấu trúc tương tự.
- Hóa học: so sánh cấu trúc phân tử.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Người học kéo thả ánh xạ giữa hai tập đỉnh. Công cụ kiểm tra từng cạnh có được bảo toàn không và báo phép ánh xạ có phải đẳng cấu hay không.
</div>

## 7. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Hai đồ thị vẽ giống nhau chưa chắc đẳng cấu nếu quan hệ cạnh khác nhau.
- Hai đồ thị có cùng số đỉnh, số cạnh và dãy bậc vẫn có thể không đẳng cấu.
- Đẳng cấu không quan tâm tên đỉnh, tọa độ hình học hay cách vẽ.
- Đồ thị con đẳng cấu khó hơn kiểm tra đẳng cấu toàn đồ thị và có liên hệ với bài toán NP-complete.
</div>

## 8. Ứng dụng trong Khoa học Máy tính

Đẳng cấu đồ thị xuất hiện trong cơ sở dữ liệu đồ thị, tìm kiếm mẫu, tối ưu trình biên dịch, kiểm chứng mạch, nhận dạng ảnh và hóa học tính toán. Trong hệ thống mạng, đẳng cấu giúp nhận diện các cấu trúc lặp lại dù nhãn nút khác nhau. Trong machine learning trên đồ thị, vấn đề biểu diễn đồ thị sao cho tôn trọng đẳng cấu là nền tảng của graph neural networks.

```python
def degree_sequence(graph):
    return sorted((len(neighbors) for neighbors in graph.values()), reverse=True)

g1 = {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['A', 'C']}
g2 = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
print(degree_sequence(g1) == degree_sequence(g2))
```

## Bài tập thực hành

### Bài tập 1

Hai đồ thị có số đỉnh khác nhau. Chúng có thể đẳng cấu không?

<details>
<summary>Đáp án</summary>

Không. Đẳng cấu cần một song ánh giữa hai tập đỉnh, nên số đỉnh phải bằng nhau.

</details>

### Bài tập 2

Hai đồ thị đều có 5 đỉnh, 5 cạnh và dãy bậc $(2,2,2,2,2)$. Có thể kết luận chúng đẳng cấu không?

<details>
<summary>Đáp án</summary>

Trong trường hợp đồ thị đơn 5 đỉnh mà mọi đỉnh bậc 2, đồ thị là chu trình $C_5$, nên chúng đẳng cấu. Nhưng nói chung cùng dãy bậc không đủ để kết luận.

</details>

### Bài tập 3

Nêu một bất biến có thể dùng để bác bỏ đẳng cấu ngoài số đỉnh và số cạnh.

<details>
<summary>Đáp án</summary>

Ví dụ: dãy bậc, số thành phần liên thông, số tam giác, sắc số, hoặc số chu trình độ dài nhất định.

</details>

## Tóm tắt

- Đẳng cấu đồ thị là phép đổi tên đỉnh bảo toàn quan hệ kề nhau.
- Bất biến đồ thị giúp bác bỏ nhanh các cặp không đẳng cấu.
- Ma trận kề của hai đồ thị đẳng cấu liên hệ qua ma trận hoán vị.
- Bài toán Graph Isomorphism có vị trí đặc biệt trong lý thuyết độ phức tạp.
- Ứng dụng gồm hóa học tính toán, phân tích mạng, tìm motif, kiểm chứng mạch và graph ML.
