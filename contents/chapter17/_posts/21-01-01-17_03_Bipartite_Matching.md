---
layout: post
title: "Ghép cặp trong Đồ thị Hai phần"
categories: chapter17
date: 2021-01-01
order: 3
required: true
lang: en
---

# Ghép cặp trong Đồ thị Hai phần

Một trường đại học có $$30$$ sinh viên đăng ký thực tập và $$30$$ công ty cần thực tập sinh. Mỗi sinh viên đã đánh dấu các công ty mình quan tâm, mỗi công ty cũng đã liệt kê các kỹ năng cần thiết. Câu hỏi: có thể phân công sao cho mỗi sinh viên thực tập ở **đúng một công ty** mà mình đã đăng ký không? Nếu không, phân công được nhiều nhất bao nhiêu cặp?

Đây là một dạng của bài toán **ghép cặp trong đồ thị hai phần** (bipartite matching) - một trong những bài toán đẹp và hữu ích nhất của lý thuyết đồ thị. Nó xuất hiện trong phân công công việc, ghép tạng hiến, lập lịch máy bay, ghép đôi sinh viên với phòng thí nghiệm, và thậm chí cả các thuật toán xếp ghép website hẹn hò. Trong bài này, chúng ta sẽ học hai định lý cổ điển - **Hall** và **König** - và thấy cách quy bài toán matching về Max-Flow.

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** đồ thị hai phần (bipartite graph), ghép cặp (matching), ghép cặp cực đại, ghép cặp hoàn hảo.
- **Phát biểu** và **áp dụng** Định lý Hall (Marriage Theorem).
- **Phát biểu** và **áp dụng** Định lý König về quan hệ giữa matching và vertex cover.
- **Quy đổi** bài toán bipartite matching thành Max-Flow.
- **Nhận diện** các bài toán thực tế có thể mô hình hóa bằng matching.

**Từ khóa**: đồ thị hai phần (bipartite graph), ghép cặp (matching), ghép cặp cực đại (maximum matching), ghép cặp hoàn hảo (perfect matching), phủ đỉnh (vertex cover), Định lý Hall, Định lý König.

## 1. Đồ thị Hai phần

**Định nghĩa**: Một đồ thị $$G = (V, E)$$ gọi là **đồ thị hai phần** (bipartite) nếu tập đỉnh có thể chia thành hai tập rời nhau $$V = X \cup Y$$ ($$X \cap Y = \emptyset$$) sao cho mọi cạnh đều nối một đỉnh trong $$X$$ với một đỉnh trong $$Y$$.

Ký hiệu: $$G = (X \cup Y, E)$$.

**Đặc trưng**: $$G$$ là bipartite khi và chỉ khi $$G$$ không chứa **chu trình lẻ** (định lý König-Egerváry).

<div class="content-box example-box" markdown="1">
**Ví dụ 1**:

- $$X = \{$$ sinh viên A, B, C $$\}$$, $$Y = \{$$ công ty P, Q, R $$\}$$.
- Cạnh thể hiện sinh viên đã đăng ký công ty: $$\{(A, P), (A, Q), (B, Q), (B, R), (C, P)\}$$.

Đồ thị này có $$3 + 3 = 6$$ đỉnh và $$5$$ cạnh, không có cạnh nội trong $$X$$ hay nội trong $$Y$$.
</div>

## 2. Ghép cặp

**Định nghĩa**: Một **ghép cặp** (matching) $$M$$ trong đồ thị $$G$$ là một tập con của cạnh $$M \subseteq E$$ sao cho **không có hai cạnh nào** trong $$M$$ chia sẻ đỉnh chung.

Tương đương: mỗi đỉnh có **bậc** $$\leq 1$$ trong đồ thị con $$(V, M)$$.

- Đỉnh **được ghép** (matched) nếu có cạnh thuộc $$M$$ đi qua.
- Đỉnh **không được ghép** (unmatched / exposed) nếu không.

**Ghép cặp cực đại** (maximum matching): matching có **nhiều cạnh nhất** trên $$G$$.

**Ghép cặp hoàn hảo** (perfect matching): matching ghép **mọi đỉnh** của $$G$$. Trong bipartite $$X \cup Y$$ với $$|X| = |Y|$$, perfect matching ghép mọi đỉnh của $$X$$ với mọi đỉnh của $$Y$$.

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: Trong Ví dụ 1, ta có ba lựa chọn matching:

- $$M_1 = \{(A, P), (B, R)\}$$ - matching kích thước $$2$$, đỉnh $$C$$ và $$Q$$ chưa ghép.
- $$M_2 = \{(A, Q), (B, R), (C, P)\}$$ - matching kích thước $$3$$, mọi sinh viên đều có công ty. Đây là **maximum matching** và là **perfect matching** từ phía $$X$$ (mọi sinh viên được ghép, dù công ty $$Q$$ chưa).
- $$M_3 = \{(A, P), (B, Q)\}$$ - matching kích thước $$2$$.

Maximum matching ở đây $$= 3$$.
</div>

## 3. Định lý Hall (Marriage Theorem)

**Câu hỏi**: khi nào tồn tại perfect matching ghép mọi đỉnh của $$X$$ với một đỉnh trong $$Y$$?

Với $$S \subseteq X$$, ký hiệu

$$N(S) = \{ y \in Y : \exists x \in S, (x, y) \in E \}$$

là tập **láng giềng** của $$S$$ trong $$Y$$.

**Định lý Hall (1935)**: Đồ thị hai phần $$G = (X \cup Y, E)$$ có matching ghép mọi đỉnh $$X$$ vào $$Y$$ khi và chỉ khi với mọi $$S \subseteq X$$,

$$|N(S)| \geq |S|.$$

**Trực giác**: muốn ghép $$k$$ sinh viên thì các sinh viên đó cùng nhau phải có ít nhất $$k$$ công ty trong số họ. Nếu $$5$$ sinh viên cùng chỉ chọn $$3$$ công ty, không thể ghép tất cả $$5$$.

**Chứng minh (chiều nghịch, mệnh đề chính)**: bằng quy nạp trên $$|X|$$, hoặc qua thuật toán augmenting path. Chi tiết xem Bondy-Murty.

<div class="content-box example-box" markdown="1">
**Ví dụ 3**: Quay lại Ví dụ 1 với $$X = \{A, B, C\}$$, $$Y = \{P, Q, R\}$$.

Kiểm tra điều kiện Hall:

- $$|N(\{A\})| = |\{P, Q\}| = 2 \geq 1$$. OK.
- $$|N(\{B\})| = |\{Q, R\}| = 2 \geq 1$$. OK.
- $$|N(\{C\})| = |\{P\}| = 1 \geq 1$$. OK.
- $$|N(\{A, B\})| = |\{P, Q, R\}| = 3 \geq 2$$. OK.
- $$|N(\{A, B, C\})| = |\{P, Q, R\}| = 3 \geq 3$$. OK.

Mọi tập con của $$X$$ đều thỏa - vậy tồn tại perfect matching. Ta đã tìm thấy ở Ví dụ 2: $$M_2$$.
</div>

<div class="content-box example-box" markdown="1">
**Ví dụ 4 (Hall thất bại)**: $$X = \{A, B, C\}$$, $$Y = \{P, Q\}$$, cạnh $$\{(A, P), (B, P), (C, Q)\}$$.

$$|N(\{A, B\})| = |\{P\}| = 1 < 2$$. **Vi phạm Hall**.

Vậy không có matching ghép tất cả $$X$$. Thật vậy, maximum matching $$= 2$$ (ví dụ $$\{(A, P), (C, Q)\}$$).
</div>

## 4. Phủ Đỉnh và Định lý König

**Định nghĩa**: Một **phủ đỉnh** (vertex cover) của đồ thị $$G$$ là một tập con $$C \subseteq V$$ sao cho **mọi cạnh** của $$G$$ có ít nhất một đầu mút trong $$C$$.

**Phủ đỉnh cực tiểu** (minimum vertex cover) là vertex cover có ít đỉnh nhất.

**Quan hệ**: trong đồ thị tổng quát, $$|\text{min vertex cover}| \geq |\text{max matching}|$$ (vì mỗi cạnh matching cần ít nhất một đỉnh phủ riêng).

**Định lý König (1931)**: Trong **đồ thị hai phần**,

$$|\text{max matching}| = |\text{min vertex cover}|.$$

<div class="content-box insight-box" markdown="1">
**Ý nghĩa**: trong bipartite, hai bài toán đối ngẫu (matching cực đại - tối đa, vertex cover - tối thiểu) có cùng giá trị tối ưu. Đây là trường hợp đặc biệt của **định lý dual** trong tối ưu tuyến tính.
</div>

<div class="content-box example-box" markdown="1">
**Ví dụ 5**: Ví dụ 1 có maximum matching $$= 3$$.

Vertex cover $$C = \{P, Q, R\}$$ (toàn bộ $$Y$$) phủ mọi cạnh, kích thước $$3$$.

Vertex cover khác: $$C' = \{A, B, P\}$$. Kiểm tra:

- Cạnh $$(A, P)$$: $$A \in C'$$. OK.
- Cạnh $$(A, Q)$$: $$A \in C'$$. OK.
- Cạnh $$(B, Q)$$: $$B \in C'$$. OK.
- Cạnh $$(B, R)$$: $$B \in C'$$. OK.
- Cạnh $$(C, P)$$: $$P \in C'$$. OK.

$$|C'| = 3 = $$ max matching. Khớp König.
</div>

## 5. Quy về Max-Flow

Định lý mạnh: bài toán **bipartite maximum matching** có thể được giải bằng **Max-Flow**.

**Phép biến đổi**:

1. Thêm hai đỉnh mới: nguồn $$s$$ và đích $$t$$.
2. Thêm cạnh $$(s, x)$$ với dung lượng $$1$$ cho mỗi $$x \in X$$.
3. Thêm cạnh $$(y, t)$$ với dung lượng $$1$$ cho mỗi $$y \in Y$$.
4. Mỗi cạnh $$(x, y) \in E$$ trở thành cạnh có hướng từ $$x$$ sang $$y$$ với dung lượng $$1$$.

**Tuyên bố**: giá trị luồng cực đại trong mạng này bằng kích thước matching cực đại.

**Chứng minh phác thảo**: Vì mọi dung lượng nguyên, luồng cực đại nguyên (định lý tính nguyên ở bài 17_02). Mỗi đơn vị luồng từ $$s$$ qua $$x \to y$$ đến $$t$$ tương ứng với một cặp ghép $$(x, y)$$. Ràng buộc dung lượng $$1$$ ở $$(s, x)$$ và $$(y, t)$$ đảm bảo $$x$$ và $$y$$ chỉ ghép một lần. $$\square$$

**Hệ quả thuật toán**: chạy Edmonds-Karp trên mạng đã xây dựng cho ta matching cực đại trong thời gian $$O(V \cdot E^2)$$. Có thuật toán chuyên dụng (Hopcroft-Karp 1973) chạy nhanh hơn: $$O(E \sqrt{V})$$.

## 6. Ứng dụng

**Phân công công việc** (assignment problem): $$n$$ nhân viên, $$n$$ công việc, mỗi cặp có "khả năng tương thích". Maximum matching trên bipartite tương thích.

**Lập lịch**: $$n$$ máy bay, $$n$$ giờ cất cánh; mỗi máy bay chỉ phù hợp một số khe giờ.

**Ghép tạng** (kidney exchange): bệnh nhân và người hiến tương thích lập đồ thị bipartite; matching tối đa số cuộc ghép.

**Phân lớp học**: $$n$$ sinh viên đăng ký môn tự chọn; bipartite (sinh viên, môn) với giới hạn sĩ số.

**Trình tự gen** (sequencing): ghép cặp phân đoạn DNA trùng khớp.

## Tổng kết

- Bipartite graph chia đỉnh thành hai phần, mọi cạnh nối giữa hai phần.
- Matching = tập cạnh không chia sẻ đỉnh. Mục tiêu: maximum matching.
- **Định lý Hall**: matching ghép hết $$X$$ tồn tại khi và chỉ khi $$|N(S)| \geq |S|$$ cho mọi $$S \subseteq X$$.
- **Định lý König**: trong bipartite, max matching = min vertex cover.
- Quy về Max-Flow: thêm nguồn, đích, dung lượng $$1$$; max-flow = max matching.

## Bài tập

1. Vẽ đồ thị bipartite có $$4$$ đỉnh mỗi bên và tìm maximum matching bằng tay. Xác định một vertex cover tối thiểu để kiểm tra König.
2. Cho $$X = \{1, 2, 3, 4, 5\}$$ với láng giềng $$N(1) = \{a, b\}, N(2) = \{a\}, N(3) = \{a, c\}, N(4) = \{c\}, N(5) = \{b, d\}$$. Kiểm tra điều kiện Hall và tìm matching nếu tồn tại.
3. Xây dựng mạng max-flow tương ứng cho đồ thị bipartite ở Bài 2 và áp dụng Ford-Fulkerson.
4. Chứng minh: trong đồ thị bipartite, một matching $$M$$ là cực đại khi và chỉ khi **không tồn tại đường tăng** $$M$$-alternating (đường xen kẽ cạnh ngoài/trong $$M$$ bắt đầu và kết thúc tại đỉnh chưa ghép).
5. Tìm hiểu thuật toán Hopcroft-Karp và giải thích vì sao nó nhanh hơn Edmonds-Karp tổng quát cho bipartite matching.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Hall, P. (1935). *On Representatives of Subsets*. Journal of the London Mathematical Society.
- König, D. (1931). *Graphs and Matrices*. Matematikai és Fizikai Lapok.
- Hopcroft, J. E., Karp, R. M. (1973). *An $$n^{5/2}$$ Algorithm for Maximum Matchings in Bipartite Graphs*. SIAM J. Comput.
- Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4th ed.), Chương 25.
- Bondy, J. A., Murty, U. S. R. (2008). *Graph Theory*. Springer GTM 244.
</div>
