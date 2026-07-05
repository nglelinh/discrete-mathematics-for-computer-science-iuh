---
layout: post
title: "Đường đi, Chu trình và Liên thông"
categories: chapter12
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Mục 12.3 định nghĩa walk, path, cycle và các khái niệm liên thông — nền tảng cho BFS, DFS và phân tích mạng trong khoa học máy tính."
---

Đồ thị không chỉ lưu **ai nối với ai** — ta cần hỏi **đi từ đâu đến đâu được không**, có vòng lặp không, mạng có tách rời thành cụm không. Các khái niệm đường đi và liên thông là nền của reachability trong compiler (dead code), phân tích phụ thuộc (circular dependency) và kiểm tra kết nối mạng.

![Đồ thị vô hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="12.7">Đường đi nối hai đỉnh — kiểm tra liên thông trả lời “có route không?”.</p>
![Đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="12.8">Trên đồ thị có hướng: phân biệt liên thông yếu và liên thông mạnh.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** walk, trail, path, cycle.
- **Định nghĩa** đồ thị liên thông (vô hướng) và liên thông yếu / mạnh (có hướng).
- **Xác định** thành phần liên thông và ứng dụng Union-Find.
- **Nhận diện** chu trình trong dependency graph.

**Từ khóa**: walk, path, cycle, liên thông (connected), thành phần liên thông (connected component), DAG.
</div>

## Walk, trail, path, cycle

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **Walk** (đi bộ): Dãy đỉnh $$v_0, v_1, \ldots, v_k$$ sao cho mỗi cặp liên tiếp là cạnh (đỉnh có thể lặp).
- **Trail**: Walk không lặp **cạnh**.
- **Path** (đường đi đơn): Trail không lặp **đỉnh**.
- **Cycle** (chu trình): Path đóng với $$v_0 = v_k$$, $$k \ge 3$$ (đồ thị đơn).
</div>

**Độ dài** đường đi = số cạnh trên path.

<div class="textbook-example" markdown="1">
**Ví dụ**: Trên đồ thị tam giác + đuôi, $$A \to B \to C \to A$$ là chu trình độ dài 3. $$A \to B \to A$$ (nếu có cạnh hai chiều hoặc hai cạnh) có thể là walk nhưng không phải cycle đơn nếu lặp cạnh.
</div>

## Liên thông

<div class="textbook-definition" markdown="1">
**Định nghĩa** (vô hướng): $$G$$ **liên thông** nếu với mọi $$u, v \in V$$ tồn tại đường đi giữa $$u$$ và $$v$$.

**Thành phần liên thông**: Tập con đỉnh tối đa liên thông với nhau.
</div>

<div class="textbook-definition" markdown="1">
**Định nghĩa** (có hướng):

- **Liên thông yếu**: Bỏ hướng cạnh, đồ thị vô hướng tương ứng liên thông.
- **Liên thông mạnh**: Với mọi $$u, v$$ có đường đi có hướng từ $$u$$ đến $$v$$.
</div>

**DAG** (Directed Acyclic Graph): Đồ thị có hướng **không** có chu trình — mô hình task scheduling, build pipeline (không circular dependency).

<div class="textbook-example" markdown="1">
**Ví dụ** (CS): Nếu module `A → B → C → A` tồn tại trong dependency graph, hệ thống build báo **circular dependency** — đó là chu trình có hướng.
</div>

## Đồ thị con và đồ thị đầy đủ

**Đồ thị con** $$G' = (V', E')$$: $$V' \subseteq V$$, $$E' \subseteq E$$ (và mọi cạnh trong $$E'$$ nối đỉnh trong $$V'$$).

**Clique**: Tập đỉnh mà mọi cặp có cạnh — ứng dụng trong nhóm bạn bè chặt, clustering.

## Bài tập

### Bài tập 1

Đồ thị vô hướng: cạnh AB, BC, CD. Có bao nhiêu thành phần liên thông? Liệt kê.

<details>
<summary>Đáp án</summary>

1 thành phần: $$\{A,B,C,D\}$$ — đồ thị đường liên thông.

</details>

### Bài tập 2

Phân biệt walk và path. Cho walk $$A \to B \to C \to B \to D$$. Có phải path không?

<details>
<summary>Đáp án</summary>

Không — đỉnh $$B$$ lặp. Đây là walk, không phải path đơn.

</details>

### Bài tập 3

Đồ thị có hướng: $$1 \to 2$$, $$2 \to 3$$, $$1 \to 3$$. Liên thông mạnh không? Liên thông yếu?

<details>
<summary>Đáp án</summary>

**Yếu**: có (bỏ hướng vẫn nối được). **Mạnh**: không — không có đường từ 3 về 1.

</details>

## Tóm tắt

- **Walk / trail / path / cycle** — độ nghiêm ngặt tăng dần.
- **Liên thông** vô hướng; **yếu / mạnh** có hướng.
- **DAG** không chu trình — scheduling, topological sort (Ch.12 mở rộng).
- Chu trình trong dependency = lỗi kiến trúc.

Trong bài tiếp theo, chúng ta học **Euler, Hamilton** và ý tưởng **BFS/DFS**.