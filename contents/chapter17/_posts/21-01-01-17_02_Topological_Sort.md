---
layout: post
title: "Sắp xếp Topo trên DAG"
categories: chapter17
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Mục 17.2 định nghĩa DAG và topological sort — thứ tự đỉnh tôn trọng mọi cạnh — với thuật toán DFS và Kahn O(V+E), ứng dụng Makefile và lịch học."
---

`make build` chỉ biên dịch file B sau khi file A (phụ thuộc) đã xong — thứ tự đó là **sắp xếp topo** trên đồ thị task. Nếu A phụ thuộc B và B phụ thuộc A, build **deadlock** vì có **chu trình**. Mục 17.2 formal hóa DAG và hai cách topo sort chuẩn.

![Đồ thị có hướng đơn giản](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="17.2">DAG — cạnh có hướng, không chu trình; topo sort là thứ tự tôn trọng mọi mũi tên.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** DAG và topological ordering.
- **Thực hiện** topo sort bằng DFS (postorder ngược) và Kahn (BFS trên bậc vào).
- **Phân tích** độ phức tạp $$O(V+E)$$.
- **Áp dụng** topo sort trong build system, lịch môn học và phát hiện deadlock.

**Từ khóa**: DAG, topological sort, in-degree, Kahn, DFS postorder, cycle detection.
</div>

## DAG và sắp xếp topo

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **DAG** (Directed Acyclic Graph): Đồ thị **có hướng**, **không** chu trình.
- **Topological sort** của DAG $$G$$: Hoán vị $$v_1, v_2, \ldots, v_n$$ của đỉnh sao cho mọi cạnh $$(u,v)$$, $$u$$ xuất hiện **trước** $$v$$ trong hoán vị.
</div>

<div class="textbook-theorem" markdown="1">
**Định lý**: Đồ thị có hướng cho phép topo sort **khi và chỉ khi** nó là DAG (không có chu trình có hướng).
</div>

**Liên hệ Ch.5**: Quan hệ "phải hoàn thành trước" trên task là **thứ tự bộ phận** nếu không có phụ thuộc vòng.

## Thuật toán DFS

1. Chạy DFS trên toàn bộ đồ thị (mọi thành phần).
2. Khi **kết thúc** DFS tại $$u$$, **đẩy** $$u$$ vào danh sách.
3. **Đảo** danh sách (hoặc insert đầu) → topo order.

**Ý tưởng**: Đỉnh được "postorder" — con cháu xử lý trước cha trong phụ thuộc.

```
DFS-TOPO(G):
    visited ← ∅; order ← []
    for each v in V:
        if v ∉ visited: DFS-VISIT(v)
    return reverse(order)
```

## Thuật toán Kahn (BFS)

1. Tính **bậc vào** $$\text{indeg}(v)$$ mỗi đỉnh.
2. Queue chứa mọi đỉnh có $$\text{indeg} = 0$$.
3. Lặp: lấy $$u$$ khỏi queue, thêm vào kết quả; với mỗi cạnh $$(u,v)$$, giảm $$\text{indeg}(v)$$; nếu 0 thì đưa $$v$$ vào queue.
4. Nếu số đỉnh xuất < $$|V|$$ → **có chu trình**.

**Độ phức tạp**: Cả DFS và Kahn đều $$O(V+E)$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: Task A→B, A→C, B→D, C→D.

```
    A
   / \
  B   C
   \ /
    D
```

Topo sort hợp lệ: **A, B, C, D** hoặc **A, C, B, D** (B và C đổi chỗ được).
</div>

## Ứng dụng

| Lĩnh vực | Mô hình |
|:---|:---|
| Build (Make, Cargo) | File → đỉnh; phụ thuộc → cạnh |
| Lịch học | Môn tiên quyết → cạnh |
| Compiler | Thứ tự phân tích / codegen |
| Deadlock | Chu trình trong đồ thị chờ tài nguyên |

**Phát hiện chu trình**: Topo sort thất bại ⟺ có cycle — dùng trong static analysis và dependency check.

## Bài tập

### Bài tập 1

DAG: P→Q, P→R, Q→S, R→S. Liệt kê **mọi** topo sort.

<details>
<summary>Đáp án</summary>

P phải đầu, S phải cuối. Q, R đổi chỗ: **P, Q, R, S** và **P, R, Q, S**.

</details>

### Bài tập 2

Thêm cạnh S→P. Còn topo sort không?

<details>
<summary>Đáp án</summary>

Không — chu trình P→…→S→P. Kahn sẽ không xử lý hết 4 đỉnh.

</details>

### Bài tập 3

Cho 5 task với 6 cạnh phụ thuộc (tự vẽ DAG acyclic). Chạy Kahn — ghi từng bước queue.

<details>
<summary>Gợi ý</summary>

Bắt đầu từ indeg=0; mỗi lần pop ghi lại và cập nhật hàng xóm. So sánh với DFS postorder.

</details>

## Tóm tắt

- **DAG**: không chu trình có hướng — điều kiện cần và đủ cho topo sort.
- **DFS**: postorder rồi đảo; **Kahn**: queue indeg=0.
- $$O(V+E)$$; ứng dụng build, scheduling, phát hiện cycle.

Bài tùy chọn tiếp theo: **tô màu đồ thị** và **ghép cặp** — preview các bài toán đồ thị kinh điển khác.