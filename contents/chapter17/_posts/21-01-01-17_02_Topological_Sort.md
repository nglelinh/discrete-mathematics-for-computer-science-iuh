---
layout: post
title: "Sắp xếp Topo trên DAG"
categories: chapter17
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Đồ thị có hướng không chu trình (DAG) và sắp xếp topo; thuật toán DFS (postorder đảo ngược) và Kahn (bậc vào kết hợp hàng đợi); độ phức tạp O(V+E) cùng ứng dụng trong hệ thống build, xếp lịch và phát hiện chu trình."
---

> **Câu chuyện mở đầu:** Buổi sáng thức dậy bạn không thể đi giày trước khi mang tất, và ở đại học bạn không thể học *Thuật toán* trước khi qua môn *Cấu trúc Dữ liệu*! Trong Khoa học Máy tính, bất kỳ hệ thống nào có ràng buộc thứ tự phụ thuộc — từ `Makefile` biên dịch hàng nghìn tệp mã nguồn, lịch quản lý dự án (PERT/CPM), cho đến thứ tự tính đạo hàm ngược (backpropagation) trong PyTorch — đều được mô hình hóa bằng **Đồ thị có hướng không chu trình (DAG)** và giải quyết gọn gàng bằng **Sắp xếp Topo**!

<div class="textbook-epigraph" markdown="1">

"If A must finish before B, draw A → B — then ask for a linear order that respects every arrow."

<span class="epigraph-attribution">— Tinh thần topological sort</span>

</div>

Trong một hệ thống biên dịch (build system), mô-đun $$B$$ chỉ được biên dịch sau khi mô-đun phụ thuộc $$A$$ đã hoàn tất — một thứ tự thực hiện hợp lệ như vậy gọi là **sắp xếp topo** (*topological sort*). Nếu $$A$$ phụ thuộc $$B$$ và $$B$$ lại phụ thuộc $$A$$, ta có một **chu trình** và không tồn tại thứ tự hợp lệ nào. Bài học này định nghĩa DAG, sắp xếp topo và trình bày hai thuật toán tuyến tính $$O(V+E)$$: DFS và Kahn.

![DAG topo](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_topo_dag.svg)

<p class="textbook-figure-caption" data-figure="17.2">DAG là đồ thị có hướng không chu trình; thứ tự topo tôn trọng chiều của mọi cạnh.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** DAG và thứ tự sắp xếp topo (*topological ordering*).
- **Thực hiện** sắp xếp topo bằng DFS (đảo ngược thứ tự postorder) và bằng thuật toán Kahn (dựa trên bậc vào).
- **Phân tích** độ phức tạp thời gian $$O(V+E)$$ của hai thuật toán.
- **Áp dụng** sắp xếp topo cho hệ thống build, lập lịch môn học và phát hiện deadlock hoặc phụ thuộc vòng.

**Từ khóa**: DAG, topological sort, in-degree, Kahn, DFS postorder, cycle detection.

</div>

## Bản đồ kiến thức nền: DAG và Hai Thuật toán Sắp xếp Topo Kinh điển

### 1. Điều kiện Cần và Đủ để tồn tại Sắp xếp Topo
- **Định lý cốt lõi:** Một đồ thị có hướng $$G$$ có thứ tự sắp xếp topo (mọi cạnh $$u \to v$$ đều có $$u$$ đứng trước $$v$$) **khi và chỉ khi $$G$$ là một DAG** (không chứa bất kỳ chu trình có hướng nào!).

### 2. Hai thuật toán tuyến tính $$O(V + E)$$
- **Thuật toán Kahn (Dựa trên Bậc vào — BFS/Queue):** Lặp lại việc rút một đỉnh có `in-degree = 0` (không còn điều kiện tiên quyết nào!), ghi vào kết quả và giảm bậc vào của các đỉnh kề đi 1. Nếu cuối cùng xuất ra ít hơn $$V$$ đỉnh $$\implies$$ **đồ thị chắc chắn có chu trình**!
- **Thuật toán DFS (Dựa trên Thời điểm kết thúc `finish time`):** Chạy DFS; mỗi khi một đỉnh duyệt xong hết các con, đẩy nó vào đầu danh sách (hoặc đảo ngược thứ tự kết thúc DFS)!

### 3. Đường găng (Critical Path) trên DAG
- **Bản chất:** Sau khi sắp xếp topo, ta tìm được **đường đi ngắn nhất VÀ đường đi dài nhất** trên DAG trong thời gian tuyến tính $$O(V + E)$$ (kể cả khi có trọng số âm!) chỉ bằng một vòng lặp quy hoạch động duy nhất!

## Ví dụ tính tay cầm tay chỉ việc: Chạy Thuật toán Kahn cho Lộ trình 5 Môn học

Cho 5 môn với các cạnh tiên quyết:
`Toán RR → CTDL`, `Lập trình → CTDL`, `CTDL → Thuật toán`, `CTDL → Hệ điều hành`.

1. **Tính bậc vào ban đầu (`in-degree`):**
   - `Toán RR`: **0**, `Lập trình`: **0**, `CTDL`: **2**, `Thuật toán`: **1**, `Hệ điều hành`: **1**.
   - Khởi tạo Queue chứa các đỉnh bậc vào 0: `[Toán RR, Lập trình]`.
2. **Rút `Toán RR`:** Giảm bậc vào `CTDL` từ `2 → 1`. Kết quả: `[Toán RR]`.
3. **Rút `Lập trình`:** Giảm bậc vào `CTDL` từ `1 → 0` $$\to$$ đẩy `CTDL` vào Queue! Kết quả: `[Toán RR, Lập trình]`.
4. **Rút `CTDL`:** Giảm bậc vào `Thuật toán` (`1 → 0`) và `Hệ điều hành` (`1 → 0`) $$\to$$ đẩy cả hai vào Queue!
5. **Rút `Thuật toán` rồi `Hệ điều hành`:** Thu được thứ tự hợp lệ gồm đủ **5/5 đỉnh**:
   `Toán RR → Lập trình → CTDL → Thuật toán → Hệ điều hành`!
   *(Chú ý: thứ tự topo **không nhất thiết duy nhất** — đổi `Lập trình` lên trước `Toán RR` vẫn hoàn toàn hợp lệ!)*

### Khung giải thích: 4 bước dùng Sắp xếp Topo giải bài toán Phụ thuộc và Quy hoạch động (nên đọc chậm)

#### Bước 1: Vẽ đúng chiều mũi tên phụ thuộc
Quy ước nhất quán: nếu $$A$$ phải làm **trước** $$B$$ thì vẽ cạnh $$A \to B$$ ($$B$$ phụ thuộc $$A$$). Vẽ ngược chiều sẽ cho thứ tự đảo ngược!

#### Bước 2: Dùng Kahn để vừa sắp xếp vừa phát hiện lỗi vòng lặp (Cycle Detection)
Trong trình quản lý gói (`npm`, `pip`, `cargo`), nếu gói A cần B và B cần A, bậc vào của cả A và B mãi bằng 1 nên Kahn dừng sớm với số đỉnh $$< V$$ — báo ngay lỗi *circular dependency*!

#### Bước 3: Kiểm tra tính duy nhất của Thứ tự Topo
Một DAG có thứ tự topo **duy nhất** khi và chỉ khi tại mọi bước của thuật toán Kahn, hàng đợi Queue luôn có **đúng 1 phần tử** (tương đương tồn tại một đường đi Hamilton nối liền tất cả $$V$$ đỉnh!).

#### Bước 4: Mở khóa Quy hoạch động trên DAG trong $$O(V + E)$$
Duyệt các đỉnh theo đúng thứ tự topo đảm bảo khi tính `dp[v]`, mọi đỉnh tiền nhiệm `dp[u]` ($$u \to v$$) đều đã được tính xong — biến hàng loạt bài toán đếm đường đi và lịch biểu dự án thành 5 dòng code!

$$
\text{Đồ thị phụ thuộc }G
\;\xrightarrow{\;\text{Kahn (in-degree) / DFS}\;}\;
\begin{cases}
\text{Đủ }V\text{ đỉnh} \implies \text{DAG + Thứ tự Topo }O(V+E) \\
< V\text{ đỉnh} \implies \text{Có chu trình phụ thuộc!}
\end{cases}
$$

## DAG và sắp xếp topo

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **DAG** (*Directed Acyclic Graph*): đồ thị **có hướng** và **không** chứa chu trình có hướng.
- **Sắp xếp topo** (*topological sort*) của đồ thị có hướng $$G$$: một hoán vị $$v_1,\ldots,v_n$$ của tập đỉnh $$V$$ sao cho với mọi cạnh có hướng $$(u,v)$$, đỉnh $$u$$ luôn đứng **trước** đỉnh $$v$$ trong hoán vị.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** Một đồ thị có hướng có thứ tự sắp xếp topo **khi và chỉ khi** nó là một DAG.

</div>

Nếu đồ thị chứa chu trình, không thể sắp xếp các đỉnh trên chu trình sao cho mọi mũi tên đều đi từ trái sang phải. Ngược lại, mọi DAG đều có ít nhất một thứ tự topo (và thường có nhiều hơn một thứ tự hợp lệ).

**Liên hệ Chương 5 và Chương 12.** Quan hệ “phải hoàn thành trước” trên tập công việc tạo thành một **quan hệ thứ tự bộ phận** khi không có phụ thuộc vòng; sắp xếp topo chính là một **mở rộng tuyến tính** của thứ tự bộ phận đó.

## Thuật toán DFS

1. Chạy DFS trên toàn bộ đồ thị (bắt đầu từ mọi đỉnh chưa được thăm).
2. Khi **kết thúc** việc thăm đỉnh $$u$$ (sau khi đã thăm hết các đỉnh đi tới được từ $$u$$), **thêm** $$u$$ vào danh sách kết quả.
3. **Đảo ngược** danh sách (hoặc chèn từng đỉnh vào đầu danh sách) để thu được thứ tự topo.

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

Để phát hiện chu trình trong DFS, ta theo dõi trạng thái đỉnh đang nằm trên ngăn xếp đệ quy (màu xám): nếu gặp một cạnh đi tới đỉnh màu xám thì đồ thị có chu trình.

## Thuật toán Kahn (BFS / bậc vào)

1. Tính bậc vào $$\mathrm{indeg}(v)$$ cho mọi đỉnh $$v \in V$$.
2. Đưa tất cả các đỉnh có $$\mathrm{indeg}=0$$ vào hàng đợi.
3. Lặp khi hàng đợi còn phần tử: lấy đỉnh $$u$$ ra và ghi vào kết quả; với mỗi cạnh $$(u,v)$$, giảm $$\mathrm{indeg}(v)$$ đi 1 và nếu $$\mathrm{indeg}(v)$$ về 0 thì đưa $$v$$ vào hàng đợi.
4. Khi kết thúc, nếu số đỉnh đã xuất ra nhỏ hơn $$\vert V\vert $$ thì đồ thị **có chu trình**.

**Độ phức tạp.** Cả DFS và Kahn đều chạy trong thời gian $$O(V+E)$$ khi đồ thị được biểu diễn bằng danh sách kề.

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét đồ thị có các cạnh $$A\to B$$, $$A\to C$$, $$B\to D$$, $$C\to D$$:

```text
    A
   / \
  B   C
   \ /
    D
```

Hai thứ tự topo hợp lệ là **A, B, C, D** và **A, C, B, D**.  
Với thuật toán Kahn: ban đầu chỉ có $$A$$ đạt bậc vào bằng 0; sau khi loại $$A$$ thì $$B$$ và $$C$$ có bậc vào bằng 0; cuối cùng là $$D$$.

</div>

### Minh họa sắp xếp topo: Kahn và DFS từng bước

Chạy thuật toán **Kahn** (bậc vào và hàng đợi) hoặc **DFS** (hậu tự đảo ngược) trên một DAG để quan sát bậc vào giảm dần, trạng thái hàng đợi/ngăn xếp và thứ tự topo được hình thành. Bạn có thể bật tùy chọn “thêm cạnh tạo chu trình” để xem thuật toán phát hiện chu trình và dừng lại.

<div class="interactive-demo" markdown="1">
<div data-demo="topo-explainer" data-preset="courses" data-algo="kahn"></div>
</div>
<script src="{{ '/public/js/explainers/graph-explainer.js' | relative_url }}"></script>

## Ứng dụng

| Lĩnh vực | Mô hình hóa bằng DAG |
|:---|:---|
| Hệ thống build (Make, Cargo, npm) | Tệp hoặc gói là đỉnh; quan hệ phụ thuộc là cạnh |
| Lập kế hoạch học tập | Môn học tiên quyết là cạnh có hướng |
| Pipeline trình biên dịch / CI | Các giai đoạn xử lý là đỉnh |
| Phát hiện deadlock | Chu trình trong đồ thị chờ tài nguyên |

**Phụ thuộc vòng (*circular dependency*):** sắp xếp topo thất bại tương đương với việc đồ thị tồn tại chu trình — dấu hiệu điển hình của lỗi kiến trúc hoặc vòng lặp import.

## Bài tập

### Bài tập 1

Cho DAG gồm các cạnh $$P\to Q$$, $$P\to R$$, $$Q\to S$$, $$R\to S$$. Hãy liệt kê tất cả các thứ tự sắp xếp topo hợp lệ.

<details>
<summary>Đáp án</summary>

Đỉnh $$P$$ phải đứng đầu và đỉnh $$S$$ phải đứng cuối; hai đỉnh $$Q$$ và $$R$$ có thể hoán vị cho nhau. Vậy có hai thứ tự hợp lệ là **P, Q, R, S** và **P, R, Q, S**.

</details>

### Bài tập 2

Nếu thêm cạnh $$S\to P$$ vào đồ thị ở Bài tập 1 thì còn tồn tại thứ tự topo hay không? Thuật toán Kahn phát hiện điều này như thế nào?

<details>
<summary>Đáp án</summary>

Không còn thứ tự topo vì đã hình thành chu trình $$P\to Q\to S\to P$$ (và $$P\to R\to S\to P$$). Khi chạy thuật toán Kahn, mọi đỉnh đều có bậc vào lớn hơn 0 ngay từ đầu (hoặc hàng đợi sẽ cạn sớm trước khi xử lý hết $$\vert V\vert $$ đỉnh), nên số đỉnh xuất ra nhỏ hơn $$\vert V\vert $$.

</details>

### Bài tập 3

Vì sao một đỉnh có bậc vào bằng 0 luôn có thể đứng ở vị trí đầu tiên trong một thứ tự topo?

<details>
<summary>Đáp án</summary>

Đỉnh có bậc vào bằng 0 không có cạnh nào đi vào nó, nghĩa là không có ràng buộc công việc nào phải hoàn thành trước nó. Sau khi xếp đỉnh này, việc giảm bậc vào của các đỉnh kề mô phỏng rằng điều kiện tiên quyết đó đã được thỏa mãn.

</details>

### Bài tập 4

So sánh ngắn gọn thuật toán sắp xếp topo bằng DFS và thuật toán Kahn về cấu trúc dữ liệu phụ.

<details>
<summary>Đáp án</summary>

DFS sử dụng ngăn xếp đệ quy (hoặc ngăn xếp tường minh) cùng danh sách lưu thứ tự postorder, trong khi Kahn sử dụng mảng bậc vào kết hợp hàng đợi. Cả hai đều có độ phức tạp thời gian $$O(V+E)$$.

</details>

## Tóm tắt

1. Một đồ thị có hướng là **DAG** khi và chỉ khi tồn tại thứ tự sắp xếp topo.
2. **DFS** thu được thứ tự topo bằng cách đảo ngược postorder; **Kahn** dùng hàng đợi xử lý dần các đỉnh bậc vào bằng 0.
3. Cả hai thuật toán đều có độ phức tạp $$O(V+E)$$, ứng dụng rộng rãi trong hệ thống build, lập lịch và phát hiện chu trình.

Bài tùy chọn tiếp theo sẽ giới thiệu bài toán **tô màu đồ thị** và **ghép cặp trên đồ thị hai phía**.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=GYmq98CVm2c">Topological sort in 5 minutes - Inside code</a> — Inside code, tiếng Anh. Giới thiệu nhanh khái niệm và cách thực hiện sắp xếp topo trên DAG.
- <a href="https://www.youtube.com/watch?v=eL-KzMXSXXI">Topological Sort Algorithm | Graph Theory</a> — WilliamFiset, tiếng Anh. Trình bày sắp xếp topo bằng DFS và thứ tự kết thúc.
- <a href="https://www.youtube.com/watch?v=cIBFEhD77b4">Topological Sort | Kahn&#x27;s Algorithm | Graph Theory</a> — WilliamFiset, tiếng Anh. Trình bày thuật toán Kahn theo bậc vào, cách tiếp cận thứ hai của bài.
