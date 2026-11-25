---
layout: post
title: "Đường đi, Chu trình và Liên thông"
categories: chapter12
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Phân biệt walk, trail, path, cycle; khái niệm liên thông trên đồ thị vô hướng, liên thông yếu/mạnh trên đồ thị có hướng, thành phần liên thông và DAG."
---

<div class="textbook-epigraph" markdown="1">

"Connectivity is the global shape of a graph; paths are how that shape is experienced locally."

<span class="epigraph-attribution">— Tinh thần lý thuyết đồ thị</span>

</div>


Một hệ thống build phần mềm (như `make`, `webpack` hay trình quản lý gói `pip`) đột ngột báo lỗi `Circular dependency detected`, còn mạng máy tính mất kết nối hoàn toàn chỉ vì đứt đúng một sợi cáp quang. Cả hai sự cố rất quen thuộc đó đều là biểu hiện trực tiếp của **đường đi, chu trình và tính liên thông** trong lý thuyết đồ thị.

**Mạch bài học:** Phân biệt chính xác 4 khái niệm **walk, trail, path, cycle** $$\longrightarrow$$ **liên thông** trên đồ thị vô hướng & cầu/đỉnh khớp $$\longrightarrow$$ **liên thông mạnh (SCC)** trên đồ thị có hướng $$\longrightarrow$$ **DAG (đồ thị có hướng không chu trình)** và ứng dụng sắp xếp phụ thuộc.

## Kiến thức cần nhớ: Đường đi, chu trình và tính liên thông trả lời những câu hỏi gì?

- **Phân cấp hành trình trên đồ thị (Walk $$\supset$$ Trail $$\supset$$ Path):** *Walk* cho phép lặp cả đỉnh lẫn cạnh; *Trail* không lặp cạnh; *Path* không lặp đỉnh (nên tự động không lặp cạnh); còn *Cycle* là đường đi khép kín chỉ lặp lại đỉnh đầu = đỉnh cuối. Phân biệt rạch ròi 4 từ này giúp tránh nhầm lẫn khi chứng minh định lý Euler/Hamilton ở bài sau.
- **Liên thông & Thành phần liên thông (Connectivity & SCC):** Trên đồ thị vô hướng, quan hệ "có đường đi giữa $$u$$ và $$v$$" là một quan hệ tương đương phân hoạch đồ thị thành các **thành phần liên thông**. Trên đồ thị có hướng, ta phân biệt *liên thông yếu* (bỏ mũi tên thì liên thông) và *liên thông mạnh* (đi được cả hai chiều $$u \leadsto v$$ lẫn $$v \leadsto u$$).
- **DAG & Thứ tự Tô-pô (Directed Acyclic Graphs):** Một đồ thị có hướng có thể sắp xếp theo thứ tự thực thi hợp lệ (topological sort) **khi và chỉ khi nó không chứa chu trình có hướng nào (là DAG)** — nền tảng của lập lịch tác vụ, Git commit history và đồ thị tính toán trong PyTorch/TensorFlow.

Các cách biểu diễn đồ thị ở mục trước cho biết trực tiếp đỉnh nào kề với đỉnh nào. Tuy nhiên, nhiều câu hỏi thực tế lại xoay quanh cấu trúc toàn cục của đồ thị: hai máy tính có liên lạc được với nhau không, các mô-đun có phụ thuộc vòng hay không, hay một tập trang web có tách thành các cụm rời rạc hay không. Các khái niệm **đường đi**, **chu trình** và **liên thông** mô tả chính xác các câu hỏi đó và là cơ sở cho BFS, DFS, Union–Find cũng như phát hiện phụ thuộc vòng (circular dependency) trong hệ thống build.

![Walk, path và cycle](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_path_cycle_walk.svg)

<p class="textbook-figure-caption" data-figure="12.6">Trên cùng một đồ thị: path không lặp đỉnh, cycle là path khép kín, còn walk cho phép lặp đỉnh và cạnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** walk, trail, path và cycle dựa trên điều kiện lặp đỉnh và lặp cạnh.
- **Định nghĩa** tính liên thông trên đồ thị vô hướng và liên thông yếu/mạnh trên đồ thị có hướng.
- **Xác định** các thành phần liên thông và giải thích vai trò của chúng trong phân tích mạng.
- **Giải thích** khái niệm DAG và hệ quả của chu trình trên đồ thị phụ thuộc.

**Từ khóa**: walk, trail, path, cycle, liên thông (connected), thành phần liên thông (connected component), DAG.

</div>

## Walk, trail, path và cycle

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho đồ thị vô hướng $$G = (V,E)$$ (với đồ thị có hướng, các cạnh được đi theo đúng chiều mũi tên).

- **Walk** (*dãy đi*): dãy đỉnh $$v_0, v_1, \ldots, v_k$$ ($$k \ge 0$$) sao cho mỗi cặp liên tiếp $$\{v_i, v_{i+1}\}$$ là một cạnh của đồ thị. Cả đỉnh và cạnh đều **được phép lặp**.
- **Trail**: một walk **không lặp cạnh**.
- **Path** (*đường đi đơn*): một walk **không lặp đỉnh** (và do đó cũng không lặp cạnh).
- **Cycle** (*chu trình*): dãy $$v_0, v_1, \ldots, v_k$$ với $$k \ge 3$$, $$v_0 = v_k$$, các đỉnh $$v_0,\ldots,v_{k-1}$$ đôi một phân biệt và mỗi cặp liên tiếp là một cạnh.

**Độ dài** của walk, trail, path hoặc cycle là số cạnh trên dãy (bằng $$k$$ theo ký hiệu trên).

</div>

Quan hệ bao hàm theo mức độ ràng buộc tăng dần:

$$
\text{walk} \;\supset\; \text{trail} \;\supset\; \text{path};
$$

chu trình (cycle) là dạng khép kín của đường đi đơn (có độ dài tối thiểu bằng 3 trên đồ thị đơn vô hướng).

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Trên Hình 12.6:

- $$A\text{–}B\text{–}C\text{–}D$$ là **path** có độ dài 3;
- $$B\text{–}C\text{–}F\text{–}E\text{–}B$$ là **cycle** có độ dài 4;
- $$A\text{–}B\text{–}E\text{–}F\text{–}C\text{–}B\text{–}D$$ là **walk** nhưng không phải path vì đỉnh $$B$$ xuất hiện hai lần.

</div>

Trên **đồ thị có hướng**, các định nghĩa được phát biểu tương tự nhưng mỗi bước phải đi theo đúng chiều cạnh có hướng $$(v_i, v_{i+1})$$, không được đi ngược chiều cạnh.

## Liên thông trên đồ thị vô hướng

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Đồ thị vô hướng $$G$$ được gọi là **liên thông** (*connected*) nếu với mọi cặp đỉnh $$u, v \in V$$ đều tồn tại một đường đi (path) nối $$u$$ và $$v$$.

**Thành phần liên thông** (*connected component*) là một tập con đỉnh tối đại sao cho đồ thị con cảm sinh trên tập đó liên thông. Nói cách khác, các thành phần liên thông phân hoạch $$V$$ thành các tập rời nhau: trong mỗi thành phần, mọi cặp đỉnh đều nối được với nhau, và không có cạnh nào nối giữa hai thành phần khác nhau.

</div>

![Thành phần liên thông](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_connected_components.svg)

<p class="textbook-figure-caption" data-figure="12.7">Đồ thị gồm ba thành phần liên thông: không tồn tại đường đi nối giữa các thành phần khác nhau.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Đồ thị vô hướng gồm các cạnh $$AB$$, $$BC$$, $$CD$$ có đúng **một** thành phần liên thông là $$\{A,B,C,D\}$$ — đây là đồ thị đường (*path graph*) liên thông.

Nếu bổ sung thêm một đỉnh cô lập $$E$$ (không có cạnh kề), số thành phần liên thông tăng lên 2: $$\{A,B,C,D\}$$ và $$\{E\}$$.

</div>

Việc kiểm tra tính liên thông hoặc liệt kê các thành phần liên thông có thể thực hiện bằng BFS hoặc DFS từ một đỉnh rồi lặp lại trên các đỉnh chưa thăm (Mục 12.4). Khi các cạnh được thêm dần theo thời gian (như trong thuật toán Kruskal), cấu trúc Union–Find (*disjoint-set*) giải quyết bài toán này hiệu quả hơn.

## Liên thông trên đồ thị có hướng

Khi bỏ hướng của mọi cạnh trên đồ thị có hướng, ta thu được đồ thị vô hướng nền. Từ đó, ta phân biệt hai mức độ liên thông:

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho đồ thị có hướng (digraph) $$G$$:

- $$G$$ **liên thông yếu** nếu đồ thị vô hướng nền (thu được sau khi bỏ hướng mọi cạnh) là liên thông.
- $$G$$ **liên thông mạnh** nếu với mọi cặp đỉnh $$u, v$$ đều tồn tại đường đi **có hướng** từ $$u$$ đến $$v$$ **và** từ $$v$$ đến $$u$$.

**Thành phần liên thông mạnh** (SCC — *strongly connected component*) là tập đỉnh tối đại cảm sinh một đồ thị con liên thông mạnh.

</div>

Tính liên thông mạnh kéo theo liên thông yếu, nhưng chiều ngược lại nói chung không đúng.

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Xét đồ thị có hướng với các cạnh $$1\to 2$$, $$2\to 3$$, $$1\to 3$$:

- **Liên thông yếu**: có, vì khi bỏ hướng cạnh ta thu được đồ thị tam giác liên thông.
- **Liên thông mạnh**: **không**, vì không có đường đi có hướng từ đỉnh 3 về đỉnh 1 hoặc đỉnh 2.

</div>

## DAG và chu trình phụ thuộc

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **DAG** (*Directed Acyclic Graph*) là đồ thị có hướng **không chứa chu trình** có hướng nào.

</div>

DAG là mô hình tiêu chuẩn trong nhiều bài toán tin học:

- xác định thứ tự biên dịch/build khi không có phụ thuộc vòng (circular dependency);
- lập lịch tác vụ (task scheduling) với ràng buộc thứ tự “việc $$A$$ hoàn thành trước việc $$B$$”;
- biểu diễn luồng dữ liệu và các pipeline xử lý.

Mọi DAG đều tồn tại ít nhất một **thứ tự tôpô** (*topological order*) — cách sắp xếp các đỉnh sao cho mọi cạnh đều đi từ đỉnh đứng trước sang đỉnh đứng sau. Ngược lại, nếu đồ thị chứa chu trình có hướng thì không tồn tại thứ tự tôpô, và hệ thống build sẽ báo lỗi phụ thuộc vòng.

<div class="textbook-example" markdown="1">

**Ví dụ 4** (ứng dụng tin học). Nếu đồ thị phụ thuộc chứa chu trình

$$
A \to B \to C \to A,
$$

thì không có thứ tự biên dịch hợp lệ nào cho ba mô-đun này vì mỗi mô-đun đều yêu cầu một mô-đun khác trong vòng phải được build trước. Đây là lỗi thiết kế kiến trúc chứ không đơn thuần là lỗi cú pháp.

</div>

## Đồ thị con và clique

**Đồ thị con** $$G' = (V', E')$$ của $$G$$ thỏa mãn $$V' \subseteq V$$, $$E' \subseteq E$$ và mọi cạnh thuộc $$E'$$ chỉ nối các đỉnh nằm trong $$V'$$.

**Clique** là một tập con các đỉnh sao cho mọi cặp đỉnh phân biệt trong tập đều có cạnh nối với nhau — tức là đồ thị con cảm sinh trên tập đó đẳng cấu với $$K_r$$ (với $$r$$ là số đỉnh của tập). Khái niệm clique thường gặp khi phân tích các nhóm liên kết chặt trong mạng (chẳng hạn nhóm người dùng đều kết nối đôi một với nhau).

## Thử nghiệm tương tác

Bật/tắt các cạnh và quan sát ma trận kề: nếu một đỉnh có cả hàng và cột toàn 0 thì đó là đỉnh cô lập; khi đồ thị tách thành nhiều thành phần liên thông, các khối phần tử 1 trên ma trận (sau khi sắp xếp lại thứ tự đỉnh) sẽ tương ứng với từng thành phần đó.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-adjacency-builder"></div>
</div>
<script src="{{ '/public/js/graph-adjacency-builder.js' | relative_url }}"></script>

## Ví dụ tính tay làm từng bước: Phân biệt Walk/Trail/Path và kiểm tra DAG trên 5 đỉnh

Xét đồ thị có hướng gồm 5 tác vụ phần mềm $$V = \{A, B, C, D, E\}$$ với các cạnh phụ thuộc:
$$A \to B, \quad A \to C, \quad B \to D, \quad C \to D, \quad D \to E.$$

1. **Kiểm tra phân loại hành trình (nếu xét phiên bản vô hướng):**
   - $$A - B - D - C - A - B$$: lặp cả đỉnh $$A, B$$ và cạnh $$AB$$ $$\Rightarrow$$ chỉ là **walk** (không phải trail).
   - $$A - B - D - C - A$$: không lặp cạnh nào, chỉ lặp đỉnh đầu/cuối $$A$$ $$\Rightarrow$$ **cycle** (và là closed trail).
   - $$A - B - D - E$$: không lặp đỉnh nào $$\Rightarrow$$ **path** độ dài 3.
2. **Kiểm tra xem đồ thị có hướng ban đầu có phải DAG không (bằng thuật toán Kahn — xóa dần đỉnh bậc vào = 0):**
   - Ban đầu bậc vào: $$\deg^-(A)=0,\; \deg^-(B)=1,\; \deg^-(C)=1,\; \deg^-(D)=2,\; \deg^-(E)=1$$.
   - Bước 1: Chọn `A` ($$\deg^- = 0$$), xóa cạnh ra $$\Rightarrow \deg^-(B)=0, \deg^-(C)=0$$.
   - Bước 2: Chọn `B`, rồi `C` $$\Rightarrow \deg^-(D)$$ giảm từ 2 về 0.
   - Bước 3: Chọn `D` $$\Rightarrow \deg^-(E)=0$$, cuối cùng chọn `E`.
   - Ta xếp được cả 5/5 đỉnh: **`A → B → C → D → E`** (hoặc `A → C → B → D → E`) $$\Rightarrow$$ **Chắc chắn là DAG!**
3. **Nếu thêm đúng 1 cạnh ngược $$E \to B$$:**
   - Xuất hiện chu trình có hướng $$B \to D \to E \to B$$.
   - Tập $$\{B, D, E\}$$ gộp thành một **thành phần liên thông mạnh (SCC)** 3 đỉnh — không thể chạy build theo thứ tự tuyến tính được nữa!

### Giải thích: Liên kết từ cục bộ (cạnh) đến toàn cục (cấu trúc mạng)
1. **Bước 1 — Bổ đề rút gọn Walk thành Path:** Nếu tồn tại một walk bất kỳ từ $$u$$ tới $$v$$, bằng cách cắt bỏ mọi vòng lặp trung gian ta **luôn thu được một đường đi đơn (path)** từ $$u$$ tới $$v$$ với độ dài ngắn hơn hoặc bằng.
2. **Bước 2 — Đếm số cạnh tối thiểu để giữ liên thông:** Một đồ thị vô hướng liên thông có $$n$$ đỉnh cần ít nhất $$n - 1$$ cạnh (khi đó nó là một **cây** và mọi cạnh đều là **cầu** — đứt 1 cạnh là đứt mạng!).
3. **Bước 3 — Thu gọn mọi đồ thị có hướng về một DAG:** Nếu gom mỗi thành phần liên thông mạnh (SCC) thành một "siêu đỉnh" duy nhất, đồ thị thu gọn (condensation graph) thu được **luôn luôn là một DAG** — kết nối trọn vẹn hai khái niệm SCC và DAG thành một bức tranh thống nhất.

$$\text{Walk} \supset \text{Trail (không lặp cạnh)} \supset \text{Path (không lặp đỉnh)}, \qquad \text{DAG} \iff \text{Tồn tại thứ tự Tô-pô.}$$

## Bài tập

### Bài tập 1

Cho đồ thị vô hướng gồm các cạnh $$AB$$, $$BC$$, $$CD$$. Đồ thị có bao nhiêu thành phần liên thông? Hãy liệt kê.

<details>
<summary>Đáp án</summary>

Đồ thị có đúng một thành phần liên thông là $$\{A,B,C,D\}$$, vì mọi cặp đỉnh đều có đường đi nối với nhau.

</details>

### Bài tập 2

Phân biệt walk và path. Dãy $$A \to B \to C \to B \to D$$ có phải là path không?

<details>
<summary>Đáp án</summary>

Không. Đỉnh $$B$$ xuất hiện hai lần nên đây chỉ là một walk (có thể là trail nếu không lặp cạnh), **không** phải đường đi đơn (path).

</details>

### Bài tập 3

Cho đồ thị có hướng với các cạnh $$1\to 2$$, $$2\to 3$$, $$1\to 3$$. Đồ thị này có liên thông mạnh không? Có liên thông yếu không?

<details>
<summary>Đáp án</summary>

**Liên thông yếu**: có. **Liên thông mạnh**: không, vì không có đường đi có hướng từ 3 về 1 (hoặc từ 2 về 1).

</details>

### Bài tập 4

Chứng minh ngắn gọn rằng trên đồ thị vô hướng, quan hệ “tồn tại đường đi nối $$u$$ và $$v$$” (kể cả đường đi độ dài 0 khi $$u=v$$) là một quan hệ tương đương trên $$V$$. Các lớp tương đương của quan hệ này là gì?

<details>
<summary>Đáp án</summary>

- **Phản xạ**: mọi đỉnh đều có đường đi độ dài 0 đến chính nó.
- **Đối xứng**: vì đồ thị vô hướng, đảo ngược thứ tự đỉnh của đường đi từ $$u$$ đến $$v$$ cho đường đi từ $$v$$ đến $$u$$.
- **Bắc cầu**: ghép đường đi từ $$u$$ đến $$v$$ với đường đi từ $$v$$ đến $$w$$ tại đỉnh chung $$v$$ tạo thành walk từ $$u$$ đến $$w$$, từ đó rút gọn được thành path từ $$u$$ đến $$w$$.

Các lớp tương đương của quan hệ này chính là các **thành phần liên thông** của đồ thị.

</details>

### Bài tập 5

Một hệ thống phần mềm có các cạnh phụ thuộc `app→ui`, `app→api`, `ui→core`, `api→core`, `core→app`. Đồ thị này có phải là DAG không? Vì sao?

<details>
<summary>Đáp án</summary>

Không phải DAG, vì tồn tại chu trình có hướng, chẳng hạn $$\mathrm{app}\to\mathrm{ui}\to\mathrm{core}\to\mathrm{app}$$.

</details>

## Tóm tắt

1. **Walk, trail, path, cycle** tăng dần mức độ ràng buộc về việc không lặp cạnh và không lặp đỉnh; độ dài được đo bằng số cạnh.
2. Đồ thị vô hướng **liên thông** khi mọi cặp đỉnh đều có đường đi nối nhau; các **thành phần liên thông** phân hoạch tập đỉnh $$V$$.
3. Trên đồ thị có hướng, cần phân biệt **liên thông yếu** (khi bỏ hướng cạnh) và **liên thông mạnh** (đi được hai chiều theo đúng hướng cạnh).
4. **DAG** là đồ thị có hướng không chu trình — điều kiện cần để tồn tại thứ tự tôpô và quá trình build không gặp phụ thuộc vòng.

Ở bài tiếp theo, ta sẽ tìm hiểu hai bài toán đi qua toàn bộ cấu trúc đồ thị — **Euler** (phủ cạnh) và **Hamilton** (phủ đỉnh) — cùng hai thuật toán duyệt đồ thị cơ bản là **BFS** và **DFS**.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=hlHWguJVAdU">Guide to Walks, Trails, Paths, Circuits, and Cycles! [Graph Theory Tutorial]</a> — Vital Sine, tiếng Anh. Phân biệt walk, trail, path, circuit và cycle.
- <a href="https://www.youtube.com/watch?v=gC0RNpD2P1Y">Properties in Graph Theory: Complete, Connected, Subgraph, Induced Subgraph</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày tính liên thông, đồ thị con và đồ thị đầy đủ.
- <a href="https://www.youtube.com/watch?v=q6pKCP1W0dk">What is a Component of a Graph? | Connected Components, Graph Theory</a> — Wrath of Math, tiếng Anh. Giải thích trực quan về thành phần liên thông.
