---
layout: post
title: "Giới thiệu Đồ thị"
categories: chapter12
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Định nghĩa đồ thị G = (V, E), phân loại đồ thị vô hướng, có hướng, có trọng số, khái niệm bậc đỉnh và định lý bắt tay trong mô hình hóa các hệ thống tin học."
---

<div class="textbook-epigraph" markdown="1">

"The Königsberg bridge problem is an example of a problem that could be solved only by means of graph theory."

<span class="epigraph-attribution">— Leonhard Euler</span>

</div>


Năm 1736, cư dân thành phố Königsberg đố nhau xem có thể đi dạo qua cả bảy cây cầu bắc qua sông Pregel sao cho mỗi cây cầu chỉ đi qua đúng một lần hay không. Leonhard Euler đã giải dứt điểm câu đố ấy bằng một bước nhảy trừu tượng thiên tài: **vứt bỏ toàn bộ hình dạng con sông, độ dài con đường và diện tích hòn đảo**, chỉ giữ lại 4 chấm tròn (đỉnh) và 7 nét nối (cạnh). Lý thuyết đồ thị — ngôn ngữ mô hình hóa mạng lưới của toàn bộ khoa học máy tính — đã ra đời từ chính nét vẽ tối giản đó.

**Mạch bài học:** Định nghĩa hình thức $$G = (V, E)$$ $$\longrightarrow$$ phân loại đồ thị (đơn, đa đồ thị, có hướng, có trọng số) $$\longrightarrow$$ **bậc đỉnh** (degree, in-degree, out-degree) $$\longrightarrow$$ **Định lý Bắt tay (Handshaking Lemma)** và ứng dụng trong tin học.

## Bản đồ kiến thức nền: Lý thuyết đồ thị mở đầu bằng những khái niệm trụ cột nào?

- **Trừu tượng hóa quan hệ nhị phân (Graph Abstraction $$G=(V,E)$$):** Mọi hệ thống gồm các thực thể và kết nối giữa chúng — từ mạng xã hội, định tuyến Internet, phụ thuộc gói phần mềm (`npm`/`pip`) đến bản đồ đường đi — đều thu gọn về tập đỉnh $$V$$ và tập cạnh $$E$$.
- **Phân loại cấu trúc cạnh (Graph Taxonomy):** Phân biệt đồ thị vô hướng vs. có hướng (digraph), đồ thị đơn (không khuyên, không cạnh song song) vs. đa đồ thị (multigraph), và đồ thị có trọng số (weighted graph) để chọn đúng thuật toán tương ứng.
- **Định lý Bắt tay & Tính chẵn lẻ (Handshaking Lemma):** Vì mỗi cạnh nối đúng 2 đầu mút, tổng bậc mọi đỉnh luôn bằng **đúng hai lần số cạnh**: $$\sum_{v \in V} \deg(v) = 2\vert E \vert$$ — kéo theo hệ quả bất biến cực mạnh: **số đỉnh bậc lẻ luôn luôn là một số chẵn**!

Ở Chương 5, quan hệ được mô tả như một tập hợp các cặp phần tử. **Đồ thị** (graph) hình thức hóa cùng ý tưởng đó dưới dạng cấu trúc $$G = (V, E)$$, trong đó đỉnh biểu diễn đối tượng và cạnh biểu diễn mối liên kết giữa chúng. Nhiều hệ thống trong khoa học máy tính có cấu trúc đồ thị tự nhiên — như mạng xã hội, đồ thị phụ thuộc mô-đun, đồ thị gọi hàm (call graph), đồ thị luồng điều khiển (control-flow graph) và tôpô định tuyến mạng — nên các khái niệm trong chương này là nền tảng cho thuật toán và phân tích mạng ở các mục tiếp theo.

Bài học này trình bày các khái niệm cơ bản: định nghĩa đồ thị, cách phân loại, bậc của đỉnh và định lý bắt tay (*handshaking lemma*).

![Đồ thị vô hướng với bậc](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_undirected_degrees.svg)

<p class="textbook-figure-caption" data-figure="12.1">Đồ thị vô hướng: bậc của mỗi đỉnh bằng số cạnh kề với nó, và tổng bậc các đỉnh gấp đôi số cạnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** đồ thị $$G = (V, E)$$ và phân biệt đồ thị vô hướng, có hướng, có trọng số.
- **Tính** bậc đỉnh (bao gồm bậc vào và bậc ra với đồ thị có hướng) và vận dụng **định lý bắt tay**.
- **Nhận biết** đồ thị đơn, đa đồ thị, đồ thị đầy đủ $$K_n$$ và đồ thị hai phía.
- **Mô hình hóa** bài toán tin học bằng đỉnh và cạnh (mạng, quan hệ phụ thuộc, luồng điều khiển).

**Từ khóa**: đồ thị (graph), đỉnh (vertex), cạnh (edge), bậc (degree), định lý bắt tay (handshaking lemma), đồ thị hai phía (bipartite).

</div>

## Định nghĩa đồ thị

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Một **đồ thị** là bộ đôi $$G = (V, E)$$, trong đó:

- $$V$$ là tập **đỉnh** (*vertices*, *nodes*) hữu hạn, khác rỗng;
- $$E$$ là tập **cạnh** (*edges*), mỗi cạnh nối một hoặc hai đỉnh thuộc $$V$$.

</div>

Theo hướng của liên kết, ta có hai loại đồ thị cơ bản:

| Loại | Cạnh thuộc $$E$$ | Ý nghĩa |
|:---|:---|:---|
| **Vô hướng** | Cặp không thứ tự $$\{u,v\}$$ | Liên kết hai chiều |
| **Có hướng** (digraph) | Cặp có thứ tự $$(u,v)$$ | Liên kết một chiều từ $$u$$ sang $$v$$ |

Khi mỗi cạnh được gán thêm một số thực (chẳng hạn chi phí, độ trễ hoặc băng thông), đồ thị được gọi là **đồ thị có trọng số** (*weighted graph*). Trọng số không làm thay đổi tập đỉnh $$V$$ hay quan hệ kề, mà cung cấp thêm dữ liệu cho các bài toán tối ưu như đường đi ngắn nhất hoặc cây khung nhỏ nhất ở các chương sau.

![Đồ thị có hướng](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_directed_example.svg)

<p class="textbook-figure-caption" data-figure="12.2">Đồ thị có hướng: cạnh $$(u,v)$$ biểu diễn quan hệ một chiều (phụ thuộc, gọi hàm, luồng dữ liệu).</p>

<div class="textbook-example" markdown="1">

**Ví dụ 1** (mô hình hóa). Cùng một cấu trúc $$G=(V,E)$$ có thể mô tả nhiều hệ thống thực tế:

| Bài toán | Đỉnh $$V$$ | Cạnh $$E$$ |
|:---|:---|:---|
| Mạng xã hội | Người dùng | Quan hệ bạn bè (thường vô hướng) |
| Dependency graph | Mô-đun / gói phần mềm | `A` phụ thuộc `B` (có hướng) |
| Call graph | Hàm / phương thức | `f` gọi `g` (có hướng) |
| Trang web | URL | Siêu liên kết (có hướng) |
| Control-flow graph | Basic block | Nhánh điều khiển sau lệnh rẽ nhánh |

</div>

![Control-flow graph](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

<p class="textbook-figure-caption" data-figure="12.3">Đồ thị luồng điều khiển (control-flow graph): đỉnh là khối lệnh cơ bản, cạnh là nhánh điều khiển — cơ sở của phân tích chương trình tĩnh.</p>

## Các loại đồ thị

Ngoài hướng và trọng số, đồ thị còn được phân loại theo cấu trúc cạnh:

| Loại | Đặc điểm |
|:---|:---|
| **Đồ thị đơn** (*simple graph*) | Có tối đa một cạnh giữa hai đỉnh và không có **khuyên** (cạnh $$\{v,v\}$$ hoặc $$(v,v)$$) |
| **Đa đồ thị** (*multigraph*) | Cho phép nhiều cạnh song song giữa cùng một cặp đỉnh |
| **Đồ thị đầy đủ** $$K_n$$ | Gồm $$n$$ đỉnh; mọi cặp đỉnh phân biệt đều được nối bởi đúng một cạnh (vô hướng), nên $$\vert E\vert  = \binom{n}{2}$$ |
| **Đồ thị hai phía** (*bipartite*) | $$V = A \cup B$$ với $$A \cap B = \emptyset$$; mọi cạnh đều nối một đỉnh thuộc $$A$$ với một đỉnh thuộc $$B$$ |

![Đồ thị đầy đủ và hai phía](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_complete_bipartite.svg)

<p class="textbook-figure-caption" data-figure="12.4">Trái: đồ thị đầy đủ $$K_4$$ gồm 6 cạnh. Phải: đồ thị hai phía với các cạnh chỉ nối giữa hai tập đỉnh, không nối trong cùng một tập.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Số cạnh của $$K_5$$ là:

$$
\lvert E(K_5) \rvert = \binom{5}{2} = 10.
$$

Trong đồ thị vô hướng đơn $$K_n$$, mỗi đỉnh nối với tất cả $$n-1$$ đỉnh còn lại, nên $$\deg(v) = n-1$$ với mọi đỉnh $$v$$.

</div>

**Đồ thị hai phía** xuất hiện tự nhiên khi mô hình hóa quan hệ giữa hai nhóm đối tượng khác vai trò (người dùng–sản phẩm, sinh viên–lớp học, tác vụ–máy chủ). Một tính chất quan trọng (sẽ gặp lại khi học về chu trình) là: đồ thị vô hướng liên thông là đồ thị hai phía khi và chỉ khi mọi chu trình trong nó đều có độ dài chẵn.

## Bậc đỉnh

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Trong đồ thị **vô hướng**, **bậc** $$\deg(v)$$ của đỉnh $$v$$ là số cạnh kề với $$v$$ (theo quy ước, mỗi khuyên tại $$v$$ được tính hai lần vào bậc của $$v$$).

Trong đồ thị **có hướng**:

- **bậc ra** $$\deg^+(v)$$ là số cạnh xuất phát từ $$v$$;
- **bậc vào** $$\deg^-(v)$$ là số cạnh đi vào $$v$$.

</div>

Trên đồ thị có hướng, ta luôn có hệ thức sau từ định nghĩa tập cạnh:

$$
\sum_{v \in V} \deg^+(v) = \sum_{v \in V} \deg^-(v) = \lvert E \rvert,
$$

vì mỗi cạnh có hướng đóng góp đúng 1 vào tổng bậc ra và đúng 1 vào tổng bậc vào.

## Định lý bắt tay

<div class="textbook-theorem" markdown="1">

**Định lý** (Handshaking Lemma). Với mọi đồ thị vô hướng $$G = (V,E)$$ (đồ thị đơn hoặc đa đồ thị; mỗi **khuyên** được tính **hai lần** vào bậc của đỉnh chứa nó), ta có:

$$
\sum_{v \in V} \deg(v) = 2\lvert E \rvert.
$$

**Hệ quả.** Số đỉnh có bậc lẻ trong một đồ thị vô hướng luôn là một **số chẵn**.

</div>

<div class="textbook-proof" markdown="1">
*Phác thảo chứng minh.* Mỗi cạnh $$\{u,v\}$$ nối hai đỉnh phân biệt được đếm đúng hai lần trong tổng bậc — một lần tại $$u$$ và một lần tại $$v$$. Mỗi khuyên $$\{v,v\}$$ cũng đóng góp đúng $$2$$ vào $$\deg(v)$$ theo quy ước ở định nghĩa bậc đỉnh, nên vẫn được đếm hai lần. Do đó, tổng bậc của tất cả các đỉnh bằng hai lần số cạnh.

Hệ quả suy ra từ tính chất số học: tổng các số nguyên là số chẵn khi và chỉ khi số lượng số hạng lẻ là chẵn. Vì $$2\vert E\vert $$ luôn chẵn, số đỉnh bậc lẻ phải là số chẵn.
</div>

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Đồ thị ở Hình 12.1 có bậc các đỉnh lần lượt là $$2,3,2,2,3$$. Tổng bậc bằng:

$$
2+3+2+2+3 = 12 = 2\lvert E \rvert \implies \lvert E \rvert = 6,
$$

khớp với số cạnh đếm trực tiếp trên hình.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4** (chứng minh không tồn tại). Có tồn tại đồ thị vô hướng đơn gồm 3 đỉnh với dãy bậc $$3,3,3$$ hay không?

Tổng bậc là $$9$$ (số lẻ), trong khi $$2\vert E\vert $$ luôn chẵn. Theo định lý bắt tay, **không** tồn tại đồ thị vô hướng nào (kể cả đa đồ thị) có dãy bậc như vậy.

</div>

### Video ngắn: Định lý bắt tay trong 20 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/handshake-lemma.mp4"></video>
</div>

Mỗi cạnh đóng góp vào bậc của **cả hai** đầu mút, nên mỗi lần thêm một cạnh thì tổng bậc tăng đúng $$2$$ (một khuyên có hai đầu trùng nhau nên cũng cộng $$2$$ vào bậc của đỉnh đó). Vì vậy $$\sum_v \deg(v)=2\vert E\vert $$ luôn là số chẵn, kéo theo số đỉnh bậc lẻ phải là số chẵn. Trong đồ thị minh họa (đồ thị đơn, không khuyên), có $$8$$ cạnh, tổng bậc bằng $$16$$ và có $$4$$ đỉnh bậc lẻ.

## Ứng dụng nhanh trong tin học

Việc lựa chọn mô hình vô hướng hay có hướng phản ánh trực tiếp bản chất của quan hệ cần biểu diễn:

- **Vô hướng**: quan hệ kết bạn hai chiều, cáp mạng vật lý không định hướng, các kết nối thông mạch trên bản mạch in.
- **Có hướng**: quan hệ import mô-đun, quyền truy cập tài nguyên, siêu liên kết giữa các trang web, nhánh điều khiển trên CFG.
- **Có trọng số**: độ trễ đường truyền, chi phí biên dịch, xác suất chuyển trạng thái.

Các mục tiếp theo sẽ trình bày cách biểu diễn đồ thị trong bộ nhớ (ma trận kề, danh sách kề), các khái niệm đường đi và liên thông, điều kiện Euler và thuật toán duyệt BFS/DFS.

## Thử nghiệm tương tác

Bật/tắt các cạnh trên đồ thị 5 đỉnh để quan sát ma trận kề và bậc đỉnh cập nhật tức thời, đồng thời kiểm chứng trực tiếp hệ thức $$\sum \deg(v) = 2\vert E\vert $$.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-adjacency-builder"></div>
</div>
<script src="{{ '/public/js/graph-adjacency-builder.js' | relative_url }}"></script>



## Công cụ tương tác

So sánh hai đồ thị nhỏ để kiểm tra xem chúng có cùng cấu trúc (đẳng cấu) hay không.
<div class="interactive-demo" markdown="1">
<div data-demo="graph-isomorphism-checker"></div>
</div>
<script src="{{ '/public/js/graph-isomorphism-checker.js' | relative_url }}"></script>

## Ví dụ tính tay cầm tay chỉ việc: Kiểm chứng Định lý Bắt tay và bác bỏ đồ thị bất khả thi

**Ví dụ 1 — Tính bậc đỉnh trên một mạng nội bộ nhỏ 5 máy chủ:**
Cho đồ thị vô hướng đơn $$G = (V, E)$$ với $$V = \{A, B, C, D, E\}$$ và 6 dây cáp:
$$E = \{\{A,B\}, \{A,C\}, \{B,C\}, \{B,D\}, \{C,E\}, \{D,E\}\}.$$
1. Đếm bậc từng đỉnh:
   - $$\deg(A) = 2$$ (nối $$B, C$$)
   - $$\deg(B) = 3$$ (nối $$A, C, D$$)
   - $$\deg(C) = 3$$ (nối $$A, B, E$$)
   - $$\deg(D) = 2$$ (nối $$B, E$$)
   - $$\deg(E) = 2$$ (nối $$C, D$$)
2. Kiểm tra Định lý Bắt tay:
   $$\sum_{v \in V} \deg(v) = 2 + 3 + 3 + 2 + 2 = 12 = 2 \times 6 = 2\vert E \vert.$$
3. Đếm số đỉnh bậc lẻ: chỉ có $$B$$ và $$C$$ (2 đỉnh — một số chẵn!).

**Ví dụ 2 — Dùng Định lý Bắt tay để phát hiện yêu cầu mạng "bất khả thi" trong 5 giây:**
Một kiến trúc sư đề xuất nối **9 máy chủ** sao cho mỗi máy kết nối trực tiếp với đúng **3 máy khác** (đồ thị 3-chính quy). Có thể nối được không?
- Tính tổng bậc yêu cầu: $$\sum \deg(v) = 9 \times 3 = 27$$ — là một **số lẻ**!
- Vì $$2\vert E \vert$$ bắt buộc phải chẵn, nên **chắc chắn KHÔNG tồn tại** sơ đồ nối dây nào thỏa mãn (khỏi tốn công thử vẽ!).

### Khung giải thích: Ba câu hỏi đầu tiên khi mô hình hóa bất kỳ bài toán nào bằng đồ thị (nên đọc chậm)

1. **Bước 1 — Đỉnh là gì, cạnh là gì?** Xác định rõ thực thể (người dùng, giao lộ, hàm gọi) làm đỉnh và mối quan hệ (kết bạn, đường một chiều, lời gọi hàm) làm cạnh.
2. **Bước 2 — Quan hệ có đối xứng không?** Nếu "A theo dõi B" không kéo theo "B theo dõi A" (như X/Twitter hay phụ thuộc thư viện), bắt buộc dùng **đồ thị có hướng** và theo dõi riêng $$\deg^-(v), \deg^+(v)$$ với bất biến $$\sum \deg^-(v) = \sum \deg^+(v) = \vert E \vert$$.
3. **Bước 3 — Dùng Định lý Bắt tay làm phép kiểm tra nhanh:** Tổng bậc chia 2 cho biết ngay số cạnh, và số đỉnh bậc lẻ phải luôn chẵn — quy tắc bất biến đơn giản nhưng chặn đứng rất nhiều sai sót thiết kế.

$$\sum_{v \in V} \deg(v) = 2\vert E \vert \quad (\text{vô hướng}), \qquad \sum_{v \in V} \deg^-(v) = \sum_{v \in V} \deg^+(v) = \vert E \vert \quad (\text{có hướng}).$$

## Bài tập

### Bài tập 1

Một đồ thị vô hướng có 8 đỉnh, mỗi đỉnh đều có bậc 3. Hỏi đồ thị có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

Theo định lý bắt tay:

$$
\sum \deg(v) = 8 \cdot 3 = 24 = 2\lvert E \rvert \implies \lvert E \rvert = 12.
$$

</details>

### Bài tập 2

Đồ thị đầy đủ $$K_5$$ có bao nhiêu cạnh và mỗi đỉnh có bậc bằng bao nhiêu?

<details>
<summary>Đáp án</summary>

$$
\lvert E \rvert = \binom{5}{2} = 10, \qquad \deg(v) = 4 \text{ với mọi đỉnh}.
$$

Kiểm tra lại bằng định lý bắt tay: $$5 \cdot 4 = 20 = 2 \cdot 10$$.

</details>

### Bài tập 3

Cho dãy số nguyên $$3, 3, 2, 2, 2, 2$$. Dãy này có thể là dãy bậc của một đồ thị vô hướng không? Nếu có, hãy tính $$\vert E\vert $$.

<details>
<summary>Đáp án</summary>

Tổng bậc bằng $$14$$ (chẵn), suy ra $$\vert E\vert  = 7$$. Số đỉnh bậc lẻ là 2 (số chẵn), thỏa mãn hệ quả của định lý bắt tay. Vì vậy, **có thể** tồn tại đồ thị vô hướng ứng với dãy bậc này (định lý bắt tay là điều kiện cần; với đồ thị đơn còn cần kiểm tra thêm tiêu chuẩn Havel–Hakimi hoặc Erdős–Gállai, ngoài phạm vi bài học này).

</details>

### Bài tập 4

Mô hình hóa hệ thống build gồm các gói `app`, `libA`, `libB`, `core`. Biết `app` phụ thuộc vào `libA` và `libB`; cả `libA` và `libB` đều phụ thuộc vào `core`. Hãy xác định tập đỉnh $$V$$, tập cạnh có hướng $$E$$, cùng $$\deg^+$$ và $$\deg^-$$ của từng đỉnh.

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

Tổng bậc ra bằng tổng bậc vào và bằng $$\vert E\vert  = 4$$.

</details>

## Tóm tắt

1. **Đồ thị** $$G=(V,E)$$ mô hình hóa quan hệ theo cặp; cạnh có thể vô hướng hoặc có hướng, và có thể gán thêm trọng số.
2. Phân loại theo cấu trúc cạnh gồm đồ thị đơn, đa đồ thị, đồ thị đầy đủ $$K_n$$ và đồ thị hai phía.
3. **Bậc đỉnh** phản ánh mức độ liên kết cục bộ; trên đồ thị có hướng, bậc được tách thành bậc vào và bậc ra.
4. **Định lý bắt tay**: $$\sum \deg(v) = 2\vert E\vert $$, suy ra số đỉnh bậc lẻ luôn là số chẵn — giúp kiểm tra nhanh tính hợp lệ của một dãy bậc.

Ở bài tiếp theo, đồ thị trừu tượng sẽ được **biểu diễn** trên máy tính bằng ma trận kề và danh sách kề — lựa chọn quyết định trực tiếp đến độ phức tạp của các thao tác cơ bản.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=C7YrMRdLkqo">Intro to Graph Theory | Definitions &amp; Ex: 7 Bridges of Konigsberg</a> — Dr. Trefor Bazett, tiếng Anh. Giới thiệu định nghĩa đồ thị qua bài toán bảy cây cầu Königsberg.
- <a href="https://www.youtube.com/watch?v=-DocD-YLlPY">#1 [Lý thuyết đồ thị | Toán rời rạc]. Các Khái Niệm Cơ Bản Của Đồ Thị | Lý Thuyết Đồ Thị Bài 1</a> — 28tech, tiếng Việt. Trình bày các khái niệm cơ bản của đồ thị bằng tiếng Việt.
- <a href="https://www.youtube.com/watch?v=HkNdNpKUByM">INTRODUCTION to GRAPH THEORY - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Bài mở đầu về lý thuyết đồ thị: đỉnh, cạnh và bậc.
