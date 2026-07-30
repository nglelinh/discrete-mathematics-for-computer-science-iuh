---
layout: post
title: "Sắp xếp Topo trên DAG"
categories: chapter17
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "DAG và topological sort; DFS postorder đảo; Kahn (indegree + queue); O(V+E); build system, lịch môn, phát hiện chu trình."
---

<div class="textbook-epigraph" markdown="1">

"If A must finish before B, draw A → B — then ask for a linear order that respects every arrow."

<span class="epigraph-attribution">— Tinh thần topological sort</span>

</div>

Hệ build chỉ biên dịch $$B$$ sau khi phụ thuộc $$A$$ xong — thứ tự đó là **sắp xếp topo**. Nếu $$A$$ phụ thuộc $$B$$ và $$B$$ phụ thuộc $$A$$, có **chu trình**: không tồn tại thứ tự hợp lệ. Mục này định nghĩa DAG, topo sort, và hai thuật toán $$O(V+E)$$: DFS và Kahn.

![DAG topo](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_topo_dag.svg)

<p class="textbook-figure-caption" data-figure="17.2">DAG: mọi cạnh có hướng, không chu trình; topo order tôn trọng mọi mũi tên.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** DAG và topological ordering.
- **Thực hiện** topo sort bằng DFS (postorder đảo) và Kahn (indegree).
- **Phân tích** độ phức tạp $$O(V+E)$$.
- **Áp dụng** cho build system, lịch môn, phát hiện deadlock / circular dependency.

**Từ khóa**: DAG, topological sort, in-degree, Kahn, DFS postorder, cycle detection.

</div>

## 1. DAG và sắp xếp topo

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **DAG** (*Directed Acyclic Graph*): đồ thị **có hướng**, **không** có chu trình có hướng.
- **Topological sort** của digraph $$G$$: hoán vị $$v_1,\ldots,v_n$$ của $$V$$ sao cho mọi cạnh $$(u,v)$$, đỉnh $$u$$ xuất hiện **trước** $$v$$ trong hoán vị.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** Digraph có topological ordering **khi và chỉ khi** nó là DAG.

</div>

Nếu có chu trình, đi quanh chu trình không thể sắp “trước/sau” nhất quán. Nếu là DAG, luôn tồn tại ít nhất một topo order (có thể nhiều).

**Liên hệ Ch.5 / Ch.12.** Quan hệ “phải xong trước” trên task là **thứ tự bộ phận** khi không phụ thuộc vòng; topo sort là **mở rộng tuyến tính** của thứ tự đó.

## 2. Thuật toán DFS

1. DFS trên toàn đồ thị (mọi đỉnh chưa thăm).
2. Khi **kết thúc** thăm $$u$$ (sau mọi đỉnh reachable từ $$u$$ theo cạnh xuôi), **ghi** $$u$$ vào danh sách.
3. **Đảo** danh sách (hoặc chèn đầu) → topo order.

```text
DFS-TOPO(G):
  visited ← ∅; order ← []
  for each v in V:
    if v ∉ visited: DFS-VISIT(v)
  return reverse(order)

DFS-VISIT(u):
  visited.add(u)
  for each v kề từ u:
    if v ∉ visited: DFS-VISIT(v)
  order.append(u)   // postorder
```

Phát hiện chu trình (biến thể): cạnh tới đỉnh **đang** trên stack đệ quy (màu xám) ⇒ cycle.

## 3. Thuật toán Kahn (BFS / indegree)

1. Tính $$\mathrm{indeg}(v)$$ với mọi $$v$$.
2. Queue các đỉnh $$\mathrm{indeg}=0$$.
3. Lặp: lấy $$u$$; ghi vào kết quả; với mỗi $$(u,v)$$ giảm $$\mathrm{indeg}(v)$$; nếu về 0 thì enqueue $$v$$.
4. Nếu số đỉnh xuất $$<|V|$$ ⇒ **có chu trình**.

**Độ phức tạp.** Cả DFS và Kahn: $$O(V+E)$$ với danh sách kề.

<div class="textbook-example" markdown="1">

**Ví dụ.** Cạnh $$A\to B$$, $$A\to C$$, $$B\to D$$, $$C\to D$$.

```text
    A
   / \
  B   C
   \ /
    D
```

Topo hợp lệ: **A, B, C, D** hoặc **A, C, B, D**.  
Kahn: ban đầu chỉ $$A$$ có indeg 0; sau $$A$$ thì $$B,C$$; sau cùng $$D$$.

</div>

## 4. Ứng dụng

| Lĩnh vực | Mô hình |
|:---|:---|
| Build (Make, Cargo, npm) | File/package = đỉnh; phụ thuộc = cạnh |
| Lịch học | Môn tiên quyết = cạnh |
| Pipeline compiler / CI | Giai đoạn = đỉnh |
| Deadlock | Chu trình trong đồ thị chờ tài nguyên |

**Circular dependency:** topo sort thất bại ⇔ có cycle — tín hiệu lỗi kiến trúc / import vòng.

## Bài tập

### Bài tập 1

DAG: $$P\to Q$$, $$P\to R$$, $$Q\to S$$, $$R\to S$$. Liệt kê mọi topo sort.

<details>
<summary>Đáp án</summary>

$$P$$ đầu, $$S$$ cuối; $$Q$$ và $$R$$ hoán vị: **P,Q,R,S** và **P,R,Q,S**.

</details>

### Bài tập 2

Thêm $$S\to P$$. Còn topo sort không? Kahn phát hiện thế nào?

<details>
<summary>Đáp án</summary>

Không — chu trình $$P\to\cdots\to S\to P$$. Kahn không bao giờ lấy đủ $$|V|$$ đỉnh (không còn indeg 0 sau vài bước, hoặc ngay từ đầu không xử lý hết).

</details>

### Bài tập 3

Vì sao đỉnh indeg 0 có thể đứng đầu một topo order?

<details>
<summary>Đáp án</summary>

Không có cạnh vào ⇒ không ràng buộc “ai phải trước nó”. Sau khi xếp nó, giảm indeg hàng xóm mô phỏng “đã thỏa điều kiện tiên quyết”.

</details>

### Bài tập 4

So sánh ngắn DFS-topo và Kahn về cấu trúc dữ liệu phụ.

<details>
<summary>Đáp án</summary>

DFS: stack đệ quy + postorder. Kahn: mảng indeg + queue. Cùng $$O(V+E)$$.

</details>

## Tóm tắt

1. **DAG** ⇔ tồn tại topo sort.
2. **DFS**: postorder rồi đảo; **Kahn**: queue indeg 0.
3. $$O(V+E)$$; dùng cho build, scheduling, phát hiện cycle.

Bài tùy chọn tiếp theo: **tô màu** và **ghép cặp**.
