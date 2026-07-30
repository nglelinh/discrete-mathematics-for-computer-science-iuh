---
layout: post
title: "Giới thiệu Đồ thị"
categories: chapter12
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Định nghĩa đồ thị G = (V, E), phân loại vô hướng/có hướng/có trọng số, bậc đỉnh và định lý bắt tay; mô hình hóa mạng và phụ thuộc trong khoa học máy tính."
---

<div class="textbook-epigraph" markdown="1">

"The Königsberg bridge problem is an example of a problem that could be solved only by means of graph theory."

<span class="epigraph-attribution">— Leonhard Euler</span>

</div>

Trong Chương 5, quan hệ được mô tả như tập các cặp. **Đồ thị** (graph) là cách hình thức hóa cùng ý tưởng đó dưới dạng cấu trúc $$G = (V, E)$$: đỉnh là đối tượng, cạnh là liên kết giữa chúng. Nhiều hệ thống trong khoa học máy tính mang đúng cấu trúc này — mạng xã hội, đồ thị phụ thuộc module, call graph, control-flow graph, và topology định tuyến — nên các định nghĩa của chương này là nền cho thuật toán và phân tích mạng ở các mục sau.

Mục này đặt các khái niệm cơ bản: định nghĩa, phân loại, bậc đỉnh và định lý bắt tay (*handshaking lemma*).

![Đồ thị vô hướng với bậc](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_undirected_degrees.svg)

<p class="textbook-figure-caption" data-figure="12.1">Đồ thị vô hướng: mỗi đỉnh có bậc bằng số cạnh kề; tổng bậc gấp đôi số cạnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** đồ thị $$G = (V, E)$$ và phân biệt vô hướng, có hướng, có trọng số.
- **Tính** bậc đỉnh (vào/ra khi có hướng) và áp dụng **định lý bắt tay**.
- **Nhận biết** đồ thị đơn, đa đồ thị, đồ thị đầy đủ $$K_n$$, đồ thị hai phía.
- **Mô hình hóa** bài toán tin học bằng đỉnh và cạnh (mạng, phụ thuộc, luồng điều khiển).

**Từ khóa**: đồ thị (graph), đỉnh (vertex), cạnh (edge), bậc (degree), định lý bắt tay (handshaking lemma), đồ thị hai phía (bipartite).

</div>

## 1. Định nghĩa đồ thị

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Một **đồ thị** là bộ đôi $$G = (V, E)$$ trong đó:

- $$V$$ là tập **đỉnh** (*vertices*, *nodes*) hữu hạn, không rỗng;
- $$E$$ là tập **cạnh** (*edges*) — mỗi cạnh nối một hoặc hai đỉnh của $$V$$.

</div>

Hai biến thể quan trọng theo cách đọc cạnh:

| Loại | Cạnh thuộc $$E$$ | Ý nghĩa |
|:---|:---|:---|
| **Vô hướng** | Cặp không thứ tự $$\{u,v\}$$ | Liên kết hai chiều |
| **Có hướng** (digraph) | Cặp có thứ tự $$(u,v)$$ | Liên kết một chiều từ $$u$$ sang $$v$$ |

Khi mỗi cạnh được gán một số thực (chi phí, độ trễ, băng thông), ta nói đồ thị **có trọng số** (*weighted graph*). Trọng số không đổi tập $$V$$ hay quan hệ kề; nó bổ sung dữ liệu cho bài toán tối ưu (đường ngắn nhất, cây khung tối thiểu — các chương sau).

![Đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_directed_example.svg)

<p class="textbook-figure-caption" data-figure="12.2">Đồ thị có hướng: cạnh $$(u,v)$$ biểu diễn quan hệ một chiều (phụ thuộc, gọi hàm, luồng dữ liệu).</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1** (mô hình hóa). Cùng một khung $$G=(V,E)$$ mô tả nhiều miền ứng dụng:

| Bài toán | Đỉnh $$V$$ | Cạnh $$E$$ |
|:---|:---|:---|
| Mạng xã hội | Người dùng | Quan hệ bạn bè (thường vô hướng) |
| Dependency graph | Module / package | `A` phụ thuộc `B` (có hướng) |
| Call graph | Hàm / phương thức | `f` gọi `g` (có hướng) |
| Trang web | URL | Siêu liên kết (có hướng) |
| Control-flow graph | Basic block | Nhánh điều khiển sau lệnh rẽ nhánh |

</div>

![Control-flow graph](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

<p class="textbook-figure-caption" data-figure="12.3">Control-flow graph: đỉnh là basic block, cạnh là nhánh điều khiển — nền tảng phân tích chương trình tĩnh.</p>

## 2. Các loại đồ thị

Ngoài phân loại theo hướng và trọng số, ta phân biệt theo cấu trúc cạnh:

| Loại | Đặc điểm |
|:---|:---|
| **Đồ thị đơn** (*simple graph*) | Tối đa một cạnh giữa hai đỉnh; không có **khuyên** (cạnh $$\{v,v\}$$ hoặc $$(v,v)$$) |
| **Đa đồ thị** (*multigraph*) | Cho phép nhiều cạnh song song giữa cùng một cặp đỉnh |
| **Đồ thị đầy đủ** $$K_n$$ | $$n$$ đỉnh; mọi cặp đỉnh khác nhau có đúng một cạnh (vô hướng). Khi đó $$|E| = \binom{n}{2}$$ |
| **Đồ thị hai phía** (*bipartite*) | $$V = A \cup B$$, $$A \cap B = \emptyset$$; mọi cạnh nối một đỉnh thuộc $$A$$ với một đỉnh thuộc $$B$$ |

![Đồ thị đầy đủ và hai phía](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_complete_bipartite.svg)

<p class="textbook-figure-caption" data-figure="12.4">Trái: $$K_4$$ với 6 cạnh. Phải: đồ thị hai phía — cạnh chỉ nối giữa hai tập, không nối trong cùng một phía.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Số cạnh của $$K_5$$:

$$
|E(K_5)| = \binom{5}{2} = 10.
$$

Với $$K_n$$ vô hướng đơn, mỗi đỉnh nối với $$n-1$$ đỉnh còn lại, nên $$\deg(v) = n-1$$ với mọi $$v$$.

</div>

**Đồ thị hai phía** xuất hiện tự nhiên khi mô hình quan hệ hai vai trò (người dùng–sản phẩm, sinh viên–lớp học, job–server). Một đặc trưng quan trọng (sẽ dùng lại khi xét chu trình): đồ thị vô hướng liên thông là hai phía khi và chỉ khi mọi chu trình đều có độ dài chẵn.

## 3. Bậc đỉnh

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Trong đồ thị **vô hướng**, **bậc** $$\deg(v)$$ của đỉnh $$v$$ là số cạnh kề với $$v$$ (mỗi khuyên, nếu có, thường được đếm hai lần).

Trong đồ thị **có hướng**:

- **bậc ra** $$\deg^+(v)$$ = số cạnh xuất phát từ $$v$$;
- **bậc vào** $$\deg^-(v)$$ = số cạnh đi vào $$v$$.

</div>

Hai hệ thức luôn đúng theo định nghĩa tập cạnh:

$$
\sum_{v \in V} \deg^+(v) = \sum_{v \in V} \deg^-(v) = |E|
$$

(trên digraph), vì mỗi cạnh đóng góp đúng 1 vào tổng bậc ra và đúng 1 vào tổng bậc vào.

## 4. Định lý bắt tay

<div class="textbook-theorem" markdown="1">

**Định lý** (Handshaking Lemma). Với đồ thị vô hướng $$G = (V,E)$$,

$$
\sum_{v \in V} \deg(v) = 2|E|.
$$

**Hệ quả.** Số đỉnh có bậc lẻ là một **số chẵn**.

</div>

*Phác thảo chứng minh.* Mỗi cạnh $$\{u,v\}$$ được đếm đúng hai lần trong tổng bậc — một lần ở $$u$$ và một lần ở $$v$$. Do đó tổng bậc bằng hai lần số cạnh.

Hệ quả suy ra từ quan sát: tổng các số nguyên bằng số chẵn khi và chỉ khi số các số hạng lẻ là chẵn. Vì $$2|E|$$ chẵn, số đỉnh bậc lẻ phải chẵn.

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Đồ thị Hình 12.1 có các bậc $$2,3,2,2,3$$. Tổng bậc:

$$
2+3+2+2+3 = 12 = 2|E| \implies |E| = 6,
$$

khớp với việc đếm cạnh trên hình.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4** (không tồn tại). Có tồn tại đồ thị vô hướng đơn với dãy bậc $$3,3,3$$ trên ba đỉnh không?

Tổng bậc $$= 9$$ lẻ, trong khi $$2|E|$$ luôn chẵn. Theo định lý bắt tay, **không** tồn tại đồ thị nào (kể cả đa đồ thị) với dãy bậc đó.

</div>

## 5. Ứng dụng nhanh trong tin học

Việc chọn mô hình vô hướng hay có hướng không mang tính trang trí: nó phản ánh ngữ nghĩa quan hệ.

- **Vô hướng**: kết bạn hai chiều, cáp mạng vật lý không định hướng, cạnh của mạch in khi chỉ quan tâm nối thông.
- **Có hướng**: import module, quyền “ai có thể đọc tài nguyên nào”, cạnh trên web, cạnh trên CFG.
- **Trọng số**: độ trễ link, chi phí build, xác suất chuyển trạng thái.

Các mục tiếp theo sẽ gắn cấu trúc này với biểu diễn máy tính (ma trận kề, danh sách kề), đường đi–liên thông, rồi điều kiện Euler và duyệt BFS/DFS.

## 6. Thử nghiệm tương tác

Bật/tắt cạnh trên đồ thị năm đỉnh; ma trận kề và bậc cập nhật tức thời. Kiểm tra trực tiếp hệ thức $$\sum \deg(v) = 2|E|$$.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-adjacency-builder"></div>
</div>
<script src="{{ '/public/js/graph-adjacency-builder.js' | relative_url }}"></script>


## Bài tập

### Bài tập 1

Đồ thị vô hướng có 8 đỉnh, mỗi đỉnh bậc 3. Có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

Theo định lý bắt tay,

$$
\sum \deg(v) = 8 \cdot 3 = 24 = 2|E| \implies |E| = 12.
$$

</details>

### Bài tập 2

$$K_5$$ có bao nhiêu cạnh? Mỗi đỉnh có bậc bao nhiêu?

<details>
<summary>Đáp án</summary>

$$
|E| = \binom{5}{2} = 10, \qquad \deg(v) = 4 \text{ với mọi đỉnh}.
$$

Kiểm tra: $$5 \cdot 4 = 20 = 2 \cdot 10$$.

</details>

### Bài tập 3

Cho dãy bậc: $$3, 3, 2, 2, 2, 2$$. Dãy này có thể là dãy bậc của một đồ thị vô hướng không? Nếu có, tính $$|E|$$.

<details>
<summary>Đáp án</summary>

Tổng bậc $$= 14$$ (chẵn) $$\implies |E| = 7$$. Số đỉnh bậc lẻ bằng 2 (chẵn) — thỏa hệ quả định lý bắt tay. Vậy **có thể** tồn tại đồ thị với dãy bậc đó (điều kiện handshaking là cần; với đồ thị đơn còn cần thêm điều kiện Havel–Hakimi / Erdős–Gállai, ngoài phạm vi mục này).

</details>

### Bài tập 4

Mô hình hóa: hệ thống build có các gói `app`, `libA`, `libB`, `core`. Biết `app` phụ thuộc `libA` và `libB`; `libA` và `libB` đều phụ thuộc `core`. Hãy nêu $$V$$, $$E$$ (có hướng) và tính $$\deg^+$$, $$\deg^-$$ của từng đỉnh.

<details>
<summary>Đáp án</summary>

$$
V = \{\mathrm{app}, \mathrm{libA}, \mathrm{libB}, \mathrm{core}\},
$$

$$
E = \{(\mathrm{app},\mathrm{libA}), (\mathrm{app},\mathrm{libB}), (\mathrm{libA},\mathrm{core}), (\mathrm{libB},\mathrm{core})\}.
$$

| Đỉnh | $$\deg^+$$ | $$\deg^-$$ |
|:---|:---:|:---:|
| app | 2 | 0 |
| libA | 1 | 1 |
| libB | 1 | 1 |
| core | 0 | 2 |

Tổng bậc ra = tổng bậc vào = $$|E| = 4$$.

</details>

## Tóm tắt

1. **Đồ thị** $$G=(V,E)$$ mô hình hóa quan hệ cặp; cạnh vô hướng hoặc có hướng (và có thể mang trọng số).
2. Phân loại cấu trúc: đơn / đa; $$K_n$$; hai phía — mỗi loại phản ánh ràng buộc khác nhau trên $$E$$.
3. **Bậc** đo mức “kết nối cục bộ”; trên digraph dùng bậc vào và bậc ra.
4. **Định lý bắt tay**: $$\sum \deg(v) = 2|E|$$; số đỉnh bậc lẻ luôn chẵn — công cụ kiểm tra nhanh tính khả thi của dãy bậc.

Trong bài tiếp theo, cùng một đồ thị trừu tượng được **biểu diễn** trên máy tính bằng ma trận kề hoặc danh sách kề; lựa chọn này quyết định độ phức tạp của các thao tác cơ bản.
