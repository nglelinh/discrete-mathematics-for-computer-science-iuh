---
layout: post
title: "Tô màu Đồ thị và Ghép cặp — Ứng dụng"
categories: chapter17
date: 2021-01-01
order: 3
required: false
lang: en
excerpt: "Mục 17.3 (tùy chọn) giới thiệu tô màu đỉnh (scheduling, register allocation), ghép cặp trên đồ thị hai phía và liên hệ với độ phức tạp NP-hard."
---

Xếp lịch thi sao cho hai môn trùng sinh viên không cùng ca? Gán thanh ghi trong compiler sao cho biến sống đồng thời không dùng chung register? Cả hai là **tô màu đồ thị**. Ghép mentor–mentee hoặc task–worker là **ghép cặp** trên đồ thị hai phía. Mục 17.3 (tùy chọn) mở đầu các chủ đề này.

![Đồ thị vô hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="17.3">Tô màu — hai đỉnh kề nhau không cùng màu; số màu tối thiểu phụ thuộc cấu trúc đồ thị.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** tô màu đỉnh và **số sắc** $$\chi(G)$$.
- **Áp dụng** greedy coloring và nhận biết bài toán NP-hard tổng quát.
- **Định nghĩa** ghép cặp và matching tối đa trên đồ thị hai phía.
- **Liên hệ** với scheduling, register allocation và TSP/Hamilton (Ch.12).

**Từ khóa**: graph coloring, chromatic number, greedy coloring, bipartite matching, NP-hard.
</div>

## Tô màu đỉnh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Tô màu đỉnh** gán màu cho mỗi đỉnh sao cho hai đỉnh **kề nhau** không cùng màu. **Số sắc** $$\chi(G)$$ là số màu **ít nhất** cần thiết.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (lịch thi): Mỗi môn = đỉnh; cạnh nối hai môn có sinh viên chung. Mỗi **màu** = một **ca thi**. $$\chi(G)$$ = số ca tối thiểu.
</div>

**Thuật toán greedy**: Duyệt đỉnh theo thứ tự bất kỳ; gán màu nhỏ nhất chưa dùng bởi hàng xóm.

- **Đồ thị lá** (tree): $$\chi = 2$$ (nếu có cạnh) hoặc 1.
- **Chu trình $$C_n$$**: $$\chi = 2$$ nếu $$n$$ chẵn, 3 nếu lẻ.
- **Đồ thị hoàn chỉnh $$K_n$$**: $$\chi = n$$.

<div class="textbook-theorem" markdown="1">
**Định lý** (Brooks, ý tưởng): Đồ thị liên thông không phải clique hoặc cycle lẻ có $$\chi(G) \leq \Delta(G)$$ ($$\Delta$$ = bậc lớn nhất). Tìm $$\chi$$ tối ưu là **NP-hard**.
</div>

**Ứng dụng CNTT**: Register allocation (Chaitin-Briggs), xếp lịch radio, map coloring.

## Đồ thị hai phía và ghép cặp

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **Đồ thị hai phía**: $$V = L \cup R$$, mọi cạnh nối $$L$$ với $$R$$.
- **Matching**: Tập cạnh **không chung đỉnh**.
- **Matching lớn nhất** trên đồ thị hai phía: tìm bằng thuật toán tăng đường (Hopcroft-Karp) — $$O(E\sqrt{V})$$.
</div>

**Ví dụ**: Gán job cho máy, ghép người dùng–server, assignment problem.

| Bài toán | Đồ thị | Độ khó |
|:---|:---|:---|
| Tô màu tối ưu | Vô hướng | NP-hard |
| Matching max (bipartite) | Hai phía | Đa thức |
| Hamilton cycle | Vô hướng | NP-hard (Ch.12) |
| Shortest path (+) | Có trọng số | Dijkstra (17.1) |

## Tổng quan Chương 17

Chúng ta đã mở rộng từ đồ thị cơ bản (Ch.12) và cây (Ch.16):

1. **Shortest path** — Dijkstra, routing.
2. **Topo sort** — DAG, build, scheduling.
3. **Coloring / matching** — tài nguyên hữu hạn, ghép cặp.

Nhiều bài toán còn lại (TSP, clique, coloring tối ưu) nằm trong **NP-hard** — chủ đề Ch.20.

## Bài tập

### Bài tập 1

Đồ thị 5 đỉnh tạo vòng $$C_5$$. $$\chi$$ bằng bao nhiêu? Greedy theo thứ tự vòng có dùng đúng $$\chi$$ màu không?

<details>
<summary>Đáp án</summary>

$$\chi(C_5) = 3$$ (chu trình lẻ). Greedy theo vòng có thể dùng 3 màu — tối ưu; thứ tự xấu trên đồ thị khác có thể dùng thừa màu.

</details>

### Bài tập 2

3 môn A,B,C: A–B và B–C trùng sinh viên, A–C không. Số ca thi tối thiểu?

<details>
<summary>Đáp án</summary>

Đồ thị đường A–B–C: $$\chi = 2$$ (A,C cùng ca; B ca khác).

</details>

### Bài tập 3

Đồ thị hai phía: L={1,2}, R={a,b,c}, cạnh 1–a, 1–b, 2–b, 2–c. Matching lớn nhất có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

**2** cạnh (ví dụ 1–a và 2–c, hoặc 1–b và 2–c).

</details>

## Tóm tắt

- **Tô màu**: hàng xóm khác màu; $$\chi$$ NP-hard; greedy hữu ích thực tế.
- **Matching bipartite**: ghép cặp tối đa, đa thức.
- Ch.17 bổ sung **thuật toán đa thức** và **preview NP-hard** cho mô hình thực tế.

Chúng ta hoàn thành phần đồ thị nâng cao. Chương 18 trở đi chuyển sang **mô hình tính toán** — automata và ngôn ngữ hình thức.