---
layout: post
title: "Tô màu Đồ thị và Ghép cặp"
categories: chapter17
date: 2021-01-01
order: 3
required: false
lang: en
excerpt: "Tô màu đỉnh, sắc số χ(G) và tô màu tham lam; ghép cặp trên đồ thị hai phía (bipartite matching); liên hệ với xếp lịch, phân bổ thanh ghi và các bài toán NP-hard."
---

> **Câu chuyện mở đầu:** Phòng đào tạo cần xếp lịch thi cuối kỳ sao cho không sinh viên nào bị trùng hai môn thi cùng một ca; trình biên dịch C++ cần phân bổ hàng trăm biến vào chỉ 16 thanh ghi CPU; còn nền tảng gọi xe cần ghép tài xế với hành khách sao cho phục vụ được nhiều chuyến nhất. Ba bài toán tưởng như chẳng liên quan gì nhau ấy thực chất đều là hai bài toán trụ cột của Lý thuyết Đồ thị: **Tô màu Đồ thị (Graph Coloring)** và **Ghép cặp (Matching)**!

<div class="textbook-epigraph" markdown="1">

"Color so that neighbors disagree — match so that no two edges share a vertex."

<span class="epigraph-attribution">— Tinh thần tô màu và matching</span>

</div>

Khi xếp lịch thi, hai môn học có chung sinh viên không thể thi cùng một ca; khi biên dịch chương trình, hai biến có khoảng sống chồng lấp không thể dùng chung một thanh ghi. Cả hai bài toán đều được mô hình hóa bằng **tô màu đỉnh**. Trong khi đó, bài toán ghép công việc với máy móc hoặc ghép sinh viên với đề tài lại thuộc lớp **ghép cặp (*matching*)** trên đồ thị hai phía. Bài học tùy chọn này giới thiệu hai họ bài toán đó và đặt chúng vào phổ độ khó giữa các thuật toán đa thức (Dijkstra, sắp xếp topo) với các bài toán NP-hard (TSP, tô màu tối ưu ở Chương 20).

![Tô màu](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_coloring_example.svg)

<p class="textbook-figure-caption" data-figure="17.3">Tô màu đỉnh: hai đỉnh kề nhau phải khác màu; số màu ít nhất cần dùng gọi là sắc số $$\chi(G)$$.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** phép tô màu đỉnh và sắc số $$\chi(G)$$.
- **Áp dụng** thuật toán tô màu tham lam và nêu giá trị $$\chi$$ cho cây, chu trình $$C_n$$ và đồ thị đầy đủ $$K_n$$.
- **Định nghĩa** tập ghép cặp (*matching*) và ghép cặp cực đại trên đồ thị hai phía.
- **Định vị** các bài toán đồ thị quen thuộc trên phổ độ khó (thời gian đa thức so với NP-hard).

**Từ khóa**: graph coloring, chromatic number, greedy coloring, bipartite matching, NP-hard.

</div>

## Bản đồ kiến thức nền: Tô màu Đồ thị, Đồ thị Hai phía và Ghép cặp

### 1. Sắc số $$\chi(G)$$ & Độ phức tạp tính toán
- **Tô màu đỉnh hợp lệ:** Hai đỉnh nối cạnh phải khác màu (tương ứng hai môn thi có chung sinh viên phải khác ca!). Số màu ít nhất gọi là **sắc số $$\chi(G)$$**.
- **Ranh giới độ phức tạp sắc nét:** Kiểm tra $$\chi(G) \le 2$$ cực dễ trong $$O(V + E)$$ (chính là kiểm tra **đồ thị hai phía** bằng BFS!), nhưng kiểm tra $$\chi(G) \le 3$$ lập tức nhảy vọt thành **NP-đầy đủ**!

### 2. Đặc trưng Đồ thị Hai phía (Bipartite Graph)
- **Định lý kinh điển:** Một đồ thị là hai phía (tô được bằng 2 màu) **khi và chỉ khi nó không chứa bất kỳ chu trình độ dài LẺ nào** (như tam giác $$C_3$$, ngũ giác $$C_5$$)!

### 3. Ghép cặp Cực đại & Định lý Hôn nhân Hall
- **Ghép cặp (Matching):** Tập các cạnh đôi một không chung đỉnh.
- **Định lý Hall:** Trên đồ thị hai phía $$G = (L \cup R, E)$$, tồn tại ghép cặp phủ hết tập trái $$L$$ **khi và chỉ khi** với mọi tập con $$S \subseteq L$$, tập láng giềng $$N(S) \subseteq R$$ thỏa mãn **$$\lvert N(S)\rvert \ge \lvert S\rvert$$**!
- **Thuật toán Đường tăng (Augmenting Path / Hopcroft–Karp):** Tìm đường đi xen kẽ cạnh ngoài/trong ghép cặp nối hai đỉnh tự do rồi đảo trạng thái để tăng kích thước ghép cặp lên $$+1$$ (Định lý Berge)!

## Ví dụ tính tay cầm tay chỉ việc: Áp dụng Định lý Hall kiểm tra Ghép cặp 3 Ứng viên – 3 Vị trí

Cho 3 ứng viên $$L = \{A, B, C\}$$ và 3 công việc $$R = \{J_1, J_2, J_3\}$$:
- **Trường hợp 1:** $$A \to \{J_1\}$$, $$B \to \{J_1\}$$, $$C \to \{J_1, J_2, J_3\}$$.
  Kiểm tra tập con $$S = \{A, B\}$$: $$\lvert S\rvert = 2$$, nhưng tập láng giềng $$N(S) = \{J_1\}$$ chỉ có $$\lvert N(S)\rvert = 1 < 2$$! Vi phạm điều kiện Hall $$\implies$$ **không thể** xếp đủ việc cho cả 3 người!
- **Trường hợp 2:** Sửa lại cho $$B$$ biết thêm $$J_2$$ ($$B \to \{J_1, J_2\}$$) và $$C \to \{J_2, J_3\}$$.
  Kiểm tra nhanh mọi tập con $$S \subseteq \{A, B, C\}$$:
  - Kích thước 1: $$\lvert N(A)\rvert = 1,\; \lvert N(B)\rvert = 2,\; \lvert N(C)\rvert = 2$$ (đều $$\ge 1$$). ✓
  - Kích thước 2: $$\lvert N(A,B)\rvert = 2,\; \lvert N(A,C)\rvert = 3,\; \lvert N(B,C)\rvert = 3$$ (đều $$\ge 2$$). ✓
  - Kích thước 3: $$\lvert N(A,B,C)\rvert = 3 \ge 3$$. ✓
  Thỏa mãn 100% điều kiện Hall $$\implies$$ tồn tại ghép cặp hoàn hảo: **$$A-J_1,\; B-J_2,\; C-J_3$$**!

### Khung giải thích: 4 bước giải quyết bài toán Lập lịch và Phân công bằng Đồ thị (nên đọc chậm)

#### Bước 1: Mô hình hóa "Xung đột" thành Tô màu, "Ghép đôi" thành Matching
Hễ hai đối tượng *không được dùng chung tài nguyên* (hai môn thi trùng sinh viên, hai biến sống đồng thời trong hàm) $$\to$$ nối cạnh và **tô màu**. Hễ cần *ghép 1–1* giữa hai nhóm (tài xế–khách, ứng viên–việc) $$\to$$ dựng đồ thị hai phía và tìm **ghép cặp cực đại**.

#### Bước 2: Dùng chặn trên nhanh $$\chi(G) \le \Delta(G) + 1$$ (Thuật toán Tham lam)
Với bậc lớn nhất $$\Delta$$, thuật toán tô màu tham lam luôn dùng không quá $$\Delta + 1$$ màu (và theo Định lý Brooks, chỉ trừ đồ thị đầy đủ $$K_n$$ và chu trình lẻ $$C_{2k+1}$$, ta thậm chí chỉ cần tối đa $$\Delta$$ màu!).

#### Bước 3: Kiểm tra nhanh tính Hai phía trước khi tìm Matching
Chạy BFS tô 2 màu Đỏ/Xanh; nếu gặp cạnh nối hai đỉnh cùng màu $$\implies$$ phát hiện ngay chu trình lẻ!

#### Bước 4: Quy bài toán Ghép cặp Hai phía về Luồng Cực đại (Max Flow)
Nối nguồn $$s$$ tới mọi đỉnh $$L$$ (dung lượng 1) và mọi đỉnh $$R$$ tới đích $$t$$ (dung lượng 1): kích thước ghép cặp cực đại chính bằng **luồng cực đại từ $$s$$ đến $$t$$**!

$$
\text{Xung đột} \to \text{Tô màu }\chi(G)
\qquad \Big\vert \qquad
\text{Phân công 1–1} \to \text{Hai phía + Hall }(\lvert N(S)\rvert \ge \lvert S\rvert) \to \text{Đường tăng}.
$$

## Tô màu đỉnh

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Tô màu đỉnh** là phép gán cho mỗi đỉnh một màu sao cho không có hai đỉnh **kề nhau** nào mang cùng màu. **Sắc số** (*chromatic number*) $$\chi(G)$$ là số lượng màu **ít nhất** đủ để tô màu hợp lệ cho đồ thị $$G$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1** (Xếp lịch thi). Xem mỗi môn thi là một đỉnh và nối cạnh giữa hai môn nếu có ít nhất một sinh viên đăng ký cả hai. Khi đó mỗi **màu** tương ứng với một **ca thi**, còn $$\chi(G)$$ chính là số ca thi tối thiểu về mặt lý thuyết.

</div>

**Tô màu tham lam (*greedy coloring*).** Duyệt các đỉnh theo một thứ tự cố định và gán cho mỗi đỉnh màu có chỉ số nhỏ nhất chưa được dùng bởi các đỉnh kề đã tô. Thuật toán luôn cho ra cách tô hợp lệ sử dụng không quá $$\Delta(G)+1$$ màu (với $$\Delta(G)$$ là bậc lớn nhất trong đồ thị), nhưng **không** đảm bảo đạt giá trị tối ưu $$\chi(G)$$.

| Lớp đồ thị | Sắc số $$\chi$$ |
|:---|:---|
| Cây có ít nhất một cạnh | $$2$$ |
| Chu trình $$C_n$$ | $$2$$ nếu $$n$$ chẵn; $$3$$ nếu $$n$$ lẻ |
| Đồ thị đầy đủ $$K_n$$ | $$n$$ |
| Đồ thị hai phía (có cạnh) | $$2$$ |

<div class="textbook-theorem" markdown="1">

**Định lý** (Brooks — ý chính). Nếu $$G$$ là đồ thị liên thông, không phải đồ thị đầy đủ $$K_n$$ và không phải chu trình lẻ, thì $$\chi(G)\le \Delta(G)$$. Tuy nhiên, bài toán tìm giá trị tối ưu $$\chi(G)$$ trên đồ thị tổng quát là **NP-hard**.

</div>

**Ứng dụng trong khoa học máy tính:** phân bổ thanh ghi (*register allocation*) trên đồ thị xung đột, phân kênh tần số không dây và bài toán tô màu bản đồ cổ điển.

<div class="interactive-demo" markdown="1">
<div data-demo="graph-coloring-interactive"></div>
</div>
<script src="{{ '/public/js/graph-coloring-interactive.js' | relative_url }}"></script>

### Thử nghiệm: tô màu tham lam so với số màu tối ưu

Thay đổi thứ tự duyệt đỉnh để quan sát số màu mà chiến lược tham lam sử dụng so với sắc số $$\chi(G)$$:

<div class="interactive-demo" markdown="1">
<div data-demo="match-explainer" data-tab="coloring"></div>
</div>
<script src="{{ '/public/js/explainers/graph-explainer.js' | relative_url }}"></script>

## Đồ thị hai phía và ghép cặp

![Matching](/discrete-mathematics-for-computer-science-iuh/img/course/Graph_bipartite_matching.svg)

<p class="textbook-figure-caption" data-figure="17.4">Ghép cặp (matching): tập các cạnh không chung đầu mút; trên đồ thị hai phía, ghép cặp cực đại giải được trong thời gian đa thức.</p>

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **Đồ thị hai phía (*bipartite graph*)**: đồ thị có tập đỉnh phân hoạch thành $$V=L\cup R$$ sao cho mọi cạnh chỉ nối một đỉnh thuộc $$L$$ với một đỉnh thuộc $$R$$.
- **Ghép cặp (*matching*)**: tập con các cạnh sao cho **không** có hai cạnh nào chung đỉnh.
- **Ghép cặp lớn nhất (*maximum matching*)**: ghép cặp có số cạnh nhiều nhất (trên đồ thị hai phía, có thể tìm bằng thuật toán đường tăng hoặc Hopcroft–Karp trong $$O(E\sqrt{V})$$).

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Xét $$L=\{1,2\}$$, $$R=\{a,b,c\}$$ với các cạnh $$1a, 1b, 2b, 2c$$. Một ghép cặp có kích thước 2 là $$\{1a, 2c\}$$.

</div>

Ghép cặp hai phía được ứng dụng trong bài toán phân công công việc cho nhân sự, ghép sinh viên với đề tài và các bài toán phân bổ (*assignment*).

### Thử nghiệm: ghép cặp bằng đường tăng

Theo dõi thuật toán Kuhn tìm ghép cặp cực đại từng bước và xem ví dụ vi phạm điều kiện Hall:

<div class="interactive-demo" markdown="1">
<div data-demo="match-explainer" data-tab="matching"></div>
</div>

## Bản đồ độ khó (Chương 12–17)

| Bài toán | Lớp đồ thị điển hình | Độ khó (trong giáo trình) |
|:---|:---|:---|
| BFS, DFS, sắp xếp topo, chu trình Euler | Đồ thị tổng quát / DAG | **P** (thời gian đa thức) |
| Dijkstra ($$w\ge 0$$) | Đồ thị trọng số không âm | **P** |
| Ghép cặp lớn nhất trên đồ thị hai phía | Đồ thị hai phía | **P** |
| Cây khung nhỏ nhất (MST) | Đồ thị vô hướng có trọng số | **P** |
| Tô màu tối ưu $$\chi(G)$$ | Đồ thị vô hướng tổng quát | **NP-hard** |
| Chu trình Hamilton / TSP | Đồ thị vô hướng / tối ưu | **NP-hard** (Ch.12, Ch.20) |

Chương 17 vừa bổ sung các thuật toán **đa thức** cốt lõi (đường đi ngắn nhất, sắp xếp topo), vừa mở ra góc nhìn sớm về lớp bài toán **NP-hard** thông qua tô màu đồ thị và bài toán Hamilton.

## Tổng quan Chương 17

1. **Đường đi ngắn nhất** — thuật toán Dijkstra và bài toán định tuyến.
2. **Sắp xếp topo** — DAG, hệ thống build và lập lịch phụ thuộc.
3. **Tô màu và ghép cặp** — bài toán chia sẻ tài nguyên hữu hạn và phân công cặp đôi.

## Bài tập

### Bài tập 1

Sắc số $$\chi(C_5)$$ bằng bao nhiêu? Nếu tô màu tham lam theo thứ tự đi vòng quanh chu trình thì thuật toán dùng bao nhiêu màu?

<details>
<summary>Đáp án</summary>

$$\chi(C_5)=3$$ vì $$C_5$$ là chu trình lẻ. Khi duyệt theo thứ tự vòng, thuật toán tham lam cũng dùng đúng 3 màu — đạt tối ưu trên ví dụ này (tuy nhiên trên nhiều đồ thị khác, chiến lược tham lam có thể dùng nhiều màu hơn $$\chi(G)$$).

</details>

### Bài tập 2

Ba môn học A, B, C có các cặp trùng sinh viên là A–B và B–C, còn A và C không trùng sinh viên. Cần ít nhất bao nhiêu ca thi?

<details>
<summary>Đáp án</summary>

Đồ thị tương ứng là đường đi A–B–C nên có sắc số $$\chi=2$$ (A và C có thể xếp cùng một ca, còn B xếp ở ca khác).

</details>

### Bài tập 3

Ghép cặp lớn nhất trên đồ thị ở Ví dụ 2 có bao nhiêu cạnh?

<details>
<summary>Đáp án</summary>

Có **2** cạnh (ví dụ $$\{1a, 2c\}$$), vì tập $$L$$ chỉ có 2 đỉnh.

</details>

### Bài tập 4

Vì sao bài toán tô màu tối ưu được xem là “khó hơn” ghép cặp hai phía trong khung lý thuyết độ phức tạp của giáo trình?

<details>
<summary>Đáp án</summary>

Ghép cặp lớn nhất trên đồ thị hai phía có thuật toán chạy trong thời gian đa thức. Ngược lại, tính sắc số $$\chi(G)$$ trên đồ thị tổng quát là bài toán NP-hard, hiện không có thuật toán thời gian đa thức đơn giản như Dijkstra hay sắp xếp topo.

</details>

## Tóm tắt

1. **Tô màu đỉnh**: các đỉnh kề nhau mang màu khác nhau; sắc số $$\chi(G)$$ có thể xấp xỉ bằng chiến lược tham lam nhưng tìm giá trị tối ưu là NP-hard.
2. **Ghép cặp hai phía**: chọn tập cạnh không chung đỉnh; bài toán tìm ghép cặp lớn nhất thuộc lớp **P**.
3. Chương 17 kết nối các thuật toán đồ thị thời gian đa thức với cánh cửa dẫn sang lớp bài toán NP-hard ở Chương 20.

Từ Chương 18 trở đi, ta sẽ chuyển sang **mô hình tính toán**: ô-tô-mát và ngôn ngữ hình thức.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=3VeQhNF5-rE">Vertex Colorings and the Chromatic Number of Graphs | Graph Theory</a> — Wrath of Math, tiếng Anh. Giới thiệu về tô màu đỉnh và sắc số của đồ thị.
- <a href="https://www.youtube.com/watch?v=J7g5HMZgKMU">[Discrete Mathematics] Graph Coloring and Chromatic Polynomials</a> — TrevTutor, tiếng Anh. Tô màu đồ thị và đa thức sắc, bám sát nửa đầu bài học.
- <a href="https://www.youtube.com/watch?v=HZLKDC9OSaQ">2.11.7 Bipartite Matching</a> — MIT OpenCourseWare, tiếng Anh. Ghép cặp trên đồ thị hai phía, tương ứng với phần matching của bài.
