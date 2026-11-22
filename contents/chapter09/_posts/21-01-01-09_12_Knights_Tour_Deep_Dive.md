---
layout: post
title: "Knight's Tour: Deep dive từ cờ vua đến backtracking và Hamilton"
categories: chapter09
date: 2021-01-01
order: 12
required: false
lang: en
excerpt: "Phân tích bài toán mã đi tuần (Knight's Tour) dưới góc nhìn đồ thị Hamilton, hiện tượng bùng nổ tổ hợp trong quay lui (backtracking) và quy tắc heuristic Warnsdorf."
---

Ở các mục trước, chúng ta đã gặp hiện tượng **bùng nổ tổ hợp (combinatorial explosion)** trong kiểm thử phần mềm và vận hành hệ thống. Mục bổ sung chuyên sâu (deep dive) này khảo sát cùng hiện tượng đó qua một bài toán cổ điển của khoa học máy tính — **bài toán mã đi tuần (Knight's Tour)**: quân **mã** trên bàn cờ $$n \times n$$ phải **đi qua mọi ô đúng một lần**. Trong mô hình đồ thị láng giềng nước mã, **open tour** tương ứng với **đường đi Hamilton**, còn **closed tour** tương ứng với **chu trình Hamilton**. Trên bàn $$5 \times 5$$, quay lui (backtracking) thuần túy thường chạy rất nhanh; nhưng trên bàn $$8 \times 8$$, cây tìm kiếm phình to theo cấp số mũ nên cần **quy tắc heuristic Warnsdorf** (1823) và cắt nhánh. Bài viết trình bày mô hình đồ thị, khung mã backtracking, con số ~26,5 nghìn tỷ closed tour có hướng trên bàn $$8 \times 8$$, và mối liên hệ với độ phức tạp của bài toán đường/chu trình Hamilton (Chương 12).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Knights_tour.svg"
       alt="Knight's tour trên bàn cờ 8×8 — quân mã đi qua mọi ô đúng một lần"
       width="45%" height="45%">
  <figcaption style="text-align: center;">Hình 9.12a: Bàn cờ → đồ thị → quay lui (+ Warnsdorf) → đường/chu trình Hamilton — cùng bản chất bùng nổ tổ hợp như bài toán kiểm thử tổ hợp (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Knight%27s_tour.svg">Ilmari Karonen / Wikimedia Commons</a>, public domain).</figcaption>
</p>
</figure>

---

## Bài toán — đi qua mọi ô đúng một lần

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho bàn cờ kích thước $$n \times n$$. Một **Knight's tour** (hành trình mã đi tuần) là dãy các ô $$(r_0,c_0), (r_1,c_1), \ldots, (r_{n^2-1}, c_{n^2-1})$$ sao cho:

1. Mỗi bước chuyển từ $$(r_i, c_i)$$ sang $$(r_{i+1}, c_{i+1})$$ là một nước đi hợp lệ của quân mã (độ lệch $$(\pm 2, \pm 1)$$ hoặc $$(\pm 1, \pm 2)$$).
2. Mọi ô trên bàn cờ xuất hiện **đúng một lần** trong dãy.
</div>

| Loại hành trình | Điều kiện bổ sung | Trực giác |
|:---|:---|:---|
| **Open tour** (hành trình mở) | Không yêu cầu quay lại ô xuất phát | Đi qua đủ 64 ô rồi dừng tại ô cuối |
| **Closed tour** (hành trình khép kín) | Từ $$(r_{n^2-1}, c_{n^2-1})$$ có thể nhảy một nước mã về $$(r_0, c_0)$$ | Tạo thành vòng khép kín qua toàn bộ bàn cờ |

Khác với quân xe hay quân tượng, số ô kế tiếp hợp lệ của quân mã phụ thuộc mạnh vào vị trí: ô góc chỉ có 2 láng giềng, còn các ô ở vùng trung tâm có tối đa 8 láng giềng. Sự chênh lệch này chính là gợi ý trực tiếp cho quy tắc heuristic.

**Ví dụ** bàn $$3 \times 3$$: **không** tồn tại hành trình mã đi tuần nào đi qua đủ 9 ô. Lý do rất trực tiếp: trên bàn $$3 \times 3$$, ô trung tâm $$(1,1)$$ **không có láng giềng mã nào** (bậc bằng 0, mọi bước dịch $$(\pm 2, \pm 1)$$ hay $$(\pm 1, \pm 2)$$ đều ra ngoài bàn cờ), trong khi 8 ô viền xung quanh nối với nhau thành một chu trình riêng.

---

## Mô hình đồ thị — bài toán Hamilton trên bàn cờ

Coi mỗi ô $$(r, c)$$ là một **đỉnh**, và nối cạnh vô hướng giữa hai đỉnh nếu quân mã có thể nhảy từ ô này sang ô kia trong một nước. Ta thu được đồ thị vô hướng $$G = (V, E)$$ với:

- Số đỉnh $$\vert V\vert = n^2$$.
- Bậc của đỉnh thay đổi theo vị trí: với bàn đủ lớn, ô góc có bậc 2, ô sát góc trên cạnh biên có bậc 3, các ô biên còn lại có bậc 4 và các ô vùng trung tâm có bậc tối đa 8.

![Đồ thị vô hướng — mô hình láng giềng](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="9.20">Mô hình hóa bàn cờ thành đồ thị vô hướng; tìm hành trình mã đi tuần tương đương với tìm đường đi qua mọi đỉnh đúng một lần (nguồn: Wikimedia Commons, chỉnh cho khóa học).</p>

Khi đó:

- **Open tour** $$\iff$$ **đường đi Hamilton** (Hamiltonian path): đường đi qua **mọi đỉnh đúng một lần**.
- **Closed tour** $$\iff$$ **chu trình Hamilton** (Hamiltonian cycle): đường đi Hamilton khép kín.

Khác với **chu trình Euler** (đi qua mỗi **cạnh** đúng một lần — chỉ cần kiểm tra điều kiện bậc chẵn và tính liên thông trong thời gian $$O(E)$$), bài toán Hamilton xét **đỉnh**, không có tiêu chuẩn bậc đơn giản tương đương và thuộc lớp **NP-hard** trên đồ thị tổng quát. Tuy nhiên, đồ thị nước mã có cấu trúc lưới đặc biệt nên các heuristic như Warnsdorf thường tìm được lời giải rất nhanh trên bàn $$8 \times 8$$.

<div class="content-box insight-box textbook-block" markdown="1">
**Cùng một khung quay lui, hai miền bài toán**: Bộ giải SAT gán giá trị đúng/sai cho biến và quay lui khi một mệnh đề bị vi phạm; Knight's tour chọn ô kế tiếp và quay lui khi đi vào ngõ cụt. Cả hai đều duyệt không gian tổ hợp và chỉ khác nhau ở điều kiện ràng buộc.
</div>

---

## Bùng nổ tổ hợp — vì sao tìm kiếm vét cạn không khả thi

Với DFS quay lui thuần trên bàn $$8 \times 8$$, độ sâu của cây tìm kiếm là 64 và mỗi bước phân nhánh theo số ô láng giềng chưa thăm (tối đa 8). Nếu ước lượng thô mỗi bước còn trung bình 4 lựa chọn, kích thước cây tìm kiếm đã lên tới cỡ $$4^{63}$$ — vượt xa khả năng duyệt vét cạn trên mọi máy tính. Đây chính là **bùng nổ tổ hợp** tương tự bài toán 324 cấu hình kiểm thử trong QA.

Có hai hướng thu hẹp không gian tìm kiếm:

1. **Cắt nhánh (pruning)**: nếu xuất hiện ô trống bị cô lập không còn lối vào, quay lui ngay thay vì đi sâu đến bước 64.
2. **Heuristic dẫn đường**: ưu tiên đi vào những ô có ít lựa chọn thoát hơn trước — chính là **quy tắc Warnsdorf**.

---

## Backtracking — khung cài đặt cơ bản

Thuật toán quay lui cơ bản gồm bốn bước lặp: đánh dấu ô đã thăm, thử lần lượt từng nước mã hợp lệ, gọi đệ quy và hoàn tác đánh dấu khi quay lui.

```python
def knight_tour(n: int, r0: int = 0, c0: int = 0) -> list[tuple[int, int]] | None:
    """Tìm open tour trên bàn n×n; None nếu không tồn tại."""
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]
    path: list[tuple[int, int]] = []
    visited = [[False] * n for _ in range(n)]

    def legal(r: int, c: int) -> bool:
        return 0 <= r < n and 0 <= c < n and not visited[r][c]

    def dfs(r: int, c: int, depth: int) -> bool:
        visited[r][c] = True
        path.append((r, c))
        if depth == n * n:
            return True
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if legal(nr, nc) and dfs(nr, nc, depth + 1):
                return True
        visited[r][c] = False
        path.pop()
        return False

    return path if dfs(r0, c0, 1) else None
```

Trên bàn $$5 \times 5$$, hàm trên thường tìm ra lời giải trong vài mili giây. Nhưng trên bàn $$8 \times 8$$ với thứ tự `moves` cố định, thuật toán có thể sa lầy rất lâu vào các nhánh cụt sâu trước khi chạm tới lời giải. Chỉ cần sắp xếp danh sách ô kế tiếp theo quy tắc Warnsdorf trước khi đệ quy, bàn $$8 \times 8$$ gần như luôn tìm thấy hành trình tức thì.

Để tìm **closed tour**, tại điều kiện dừng `depth == n * n`, chỉ cần kiểm tra thêm xem ô cuối cùng có cách ô xuất phát $$(r_0, c_0)$$ đúng một nước mã hay không.

---

## Quy tắc Warnsdorf — phân tích chi tiết

**Ý tưởng** (H. C. von Warnsdorf, 1823): từ ô hiện tại, luôn ưu tiên đi tới ô láng giềng hợp lệ có **số láng giềng chưa thăm ít nhất** (độ tiếp cận thấp nhất). Những ô “cổ chai” ở góc và cạnh biên cần được ghé sớm, còn các ô trung tâm nhiều lối thoát có thể để lại sau.

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với mỗi ô ứng viên $$v$$, đặt $$W(v) = \vert \{ u : u \text{ là láng giềng mã của } v \text{ và } u \text{ chưa thăm} \}\vert $$. Ưu tiên chọn $$v$$ có $$W(v)$$ **nhỏ nhất**; nếu nhiều ô có cùng $$W(v)$$, phá hòa bằng cách chọn ngẫu nhiên hoặc theo thứ tự cố định (chẳng hạn thứ tự từ điển $$(r, c)$$).
</div>

```python
def warnsdorf_neighbors(n: int, r: int, c: int, visited: list[list[bool]]) -> list[tuple[int, int]]:
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]
    candidates = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            degree = 0
            for dr2, dc2 in moves:
                ar, ac = nr + dr2, nc + dc2
                if 0 <= ar < n and 0 <= ac < n and not visited[ar][ac]:
                    degree += 1
            candidates.append((degree, nr, nc))
    candidates.sort(key=lambda t: (t[0], t[1], t[2]))
    return [(nr, nc) for _, nr, nc in candidates]
```

Trong hàm `dfs`, chỉ cần thay vòng `for dr, dc in moves` bằng `for nr, nc in warnsdorf_neighbors(n, r, c, visited)`.

| Phương pháp | Bàn $$5 \times 5$$ | Bàn $$8 \times 8$$ (từ một ô đầu) | Ghi chú |
|:---|:---|:---|:---|
| DFS thứ tự cố định | Nhanh | Có thể rất chậm do sa lầy nhánh cụt | Phụ thuộc mạnh vào thứ tự nhánh |
| DFS + Warnsdorf | Nhanh | **Thường < 1 ms** | Heuristic, không đảm bảo không cần quay lui với mọi $$n$$ |
| Đếm **tất cả** closed tour | Không tồn tại (25 ô lẻ) | ~26,5 nghìn tỷ (có hướng) | Cần thuật toán đếm chuyên biệt, không dùng Warnsdorf |

<div class="content-box warning-box textbook-block" markdown="1">
Quy tắc Warnsdorf **không** đảm bảo thành công ở bước tham lam đầu tiên trên mọi kích thước bàn cờ và mọi cách phá hòa. Vẫn tồn tại những cấu hình khiến heuristic đi vào ngõ cụt; khi đó cần kết hợp quay lui đầy đủ hoặc đổi quy tắc phá hòa. Trong thực tế với $$n \le 8$$, Warnsdorf kết hợp quay lui là giải pháp tiêu chuẩn.
</div>

Vì sao Warnsdorf hiệu quả? Do các ô góc chỉ có bậc 2 trong khi ô giữa có bậc 8, nếu để sót các ô góc đến giai đoạn cuối thì rất dễ mất hết lối vào. Ưu tiên xử lý sớm các ô ít láng giềng giúp loại bỏ sớm các nhánh cụt lớn của cây tìm kiếm.

---

## Số lượng hành trình trên bàn $$8 \times 8$$ và các bàn nhỏ

Bàn cờ tiêu chuẩn **$$8 \times 8$$** là mốc chuẩn kinh điển:

| Đại lượng | Kết quả đã tính bằng máy tính |
|:---|:---|
| Số **closed tour có hướng** (directed) | $$26\,534\,728\,821\,064$$ |
| Số **closed tour vô hướng** (không phân biệt chiều đi) | $$13\,267\,364\,410\,532$$ |
| Open tour trên $$8 \times 8$$ | Tồn tại rất nhiều |

Con số ~26,5 nghìn tỷ closed tour có hướng (được tính bằng kỹ thuật chia để trị và phá đối xứng bởi Martin Löbbing & Ingo Wegener năm 1996, cùng các nghiên cứu xác minh sau này) không có nghĩa ta phải duyệt hết để **tìm một** hành trình; tìm một lời giải và đếm tất cả lời giải là hai bài toán hoàn toàn khác nhau.

**Điều kiện tồn tại trên bàn vuông $$n \times n$$**:

Vì mỗi nước đi của quân mã luôn đổi màu ô (trắng sang đen hoặc đen sang trắng), đồ thị nước mã là **đồ thị hai phía**. Mọi chu trình khép kín trong đồ thị hai phía đều phải có độ dài chẵn; do đó, khi $$n$$ lẻ (tổng số ô $$n^2$$ lẻ), **không bao giờ tồn tại closed tour**. Theo định lý Schwenk cho bàn vuông $$n \times n$$:

| $$n$$ | Open tour? | Closed tour? | Ghi chú |
|:---:|:---:|:---:|:---|
| 3 | Không | Không | Ô trung tâm $$(1,1)$$ bị cô lập (bậc 0) |
| 4 | Không | Không | Không đủ bậc và cấu trúc liên kết để tạo đường Hamilton 16 ô |
| 5 | **Có** | **Không** | 25 ô lẻ nên không thể khép kín; ví dụ điển hình của “open có, closed không” |
| 6 | **Có** | **Có** | Bàn vuông nhỏ nhất có closed tour |
| $$n \ge 6$$ | **Có** | **Có khi và chỉ khi $$n$$ chẵn** | Với mọi $$n \ge 5$$ đều có open tour; closed tour đòi hỏi $$n \ge 6$$ và $$n$$ chẵn |

**Về điểm xuất phát trên bàn $$8 \times 8$$**: Vì một **closed tour** là chu trình Hamilton đi qua mọi ô và nối ô cuối trở về ô đầu, nên **mọi ô** trên bàn $$8 \times 8$$ đều có thể đóng vai trò ô xuất phát cho cả closed tour lẫn open tour (chỉ cần bắt đầu đi dọc theo chu trình từ ô đó).

---

## Độ phức tạp và liên hệ với NP-hardness

- Bài toán tìm **đường đi / chu trình Hamilton** trên đồ thị tổng quát là **NP-complete** (có thể quy dẫn từ SAT hoặc TSP).
- **Knight's tour** trên bàn $$n \times n$$ là một trường hợp đặc biệt có cấu trúc lưới thưa (bậc tối đa 8); nhờ cấu trúc này, các thuật toán chuyên biệt (thậm chí chạy trong thời gian tuyến tính theo số ô) và heuristic Warnsdorf giải quyết rất hiệu quả trong thực tế.

| Bài toán | Đối tượng duyệt | Điều kiện kiểm tra nhanh | Thực tế giải |
|:---|:---|:---|:---|
| Chu trình Euler | Mọi cạnh đúng 1 lần | Mọi đỉnh bậc chẵn (và liên thông) | $$O(E)$$ |
| Chu trình Hamilton | Mọi đỉnh đúng 1 lần | Không có tiêu chuẩn bậc đơn giản | NP-hard trên đồ thị tổng quát |
| Một Knight's tour $$8 \times 8$$ | Mọi ô đúng 1 lần | Warnsdorf + quay lui | Thường tìm thấy trong < 1 ms |

Tư duy **mô hình hóa thành đồ thị → tìm kiếm kèm cắt nhánh và heuristic** không chỉ áp dụng cho cờ vua mà còn xuất hiện phổ biến trong định tuyến (routing), kiểm thử phủ đường đi và giải bài toán thỏa mãn ràng buộc (như Sudoku hay N-Queens).

---

## Công cụ tương tác

<div data-demo="euler-hamilton-checker"></div>

<script src="{{ '/public/js/euler-hamilton-checker.js' | relative_url }}"></script>

Widget trên minh họa sự khác biệt giữa **Euler và Hamilton** trên đồ thị nhỏ — phân biệt rõ “duyệt cạnh” với “duyệt đỉnh” (nhánh mà bài toán Knight's tour thuộc về).

---

## Ứng dụng trong Khoa học Máy tính

- **Khung quay lui (backtracking template)**: Thử → đệ quy → hoàn tác là mẫu thuật toán chung cho Sudoku, N-Queens, Knight's tour và bộ giải SAT.
- **Tìm kiếm heuristic**: Quy tắc Warnsdorf minh họa rằng một tiêu chí cục bộ đơn giản, tận dụng cấu trúc bài toán có thể cắt giảm mạnh không gian tìm kiếm.
- **Lập trình thi đấu và phỏng vấn**: Nhiều bài toán quen thuộc dùng đồ thị quân mã như *Knight Probability in Chessboard* (quy hoạch động) hay *Minimum Knight Moves* (BFS tìm đường đi ngắn nhất).
- **Liên hệ với kiểm thử QA**: Giống như không thể duyệt hết mọi hành trình mã đi tuần, trong kiểm thử cũng không thể chạy vét cạn mọi cấu hình mà cần cấu trúc hóa bằng pairwise và cắt nhánh.

Minh giữ lại hàm `warnsdorf_neighbors` trong kho mã cá nhân như một ví dụ trực quan mỗi khi cần giải thích vì sao tìm kiếm vét cạn nhanh chóng chạm giới hạn tổ hợp.

---

## Bài tập thực hành

### Bài tập 1: Bàn $$3 \times 3$$

Chứng minh không tồn tại Knight's tour (cả open lẫn closed) đi qua đủ 9 ô trên bàn $$3 \times 3$$.

<details>
<summary>Đáp án</summary>

Xét ô trung tâm $$(1,1)$$ trên bàn $$3 \times 3$$ (chỉ số hàng và cột thuộc $$\{0, 1, 2\}$$). Mọi nước đi của quân mã đều thay đổi một tọa độ đi $$\pm 2$$; từ tọa độ $$1$$, cả $$1 + 2 = 3$$ lẫn $$1 - 2 = -1$$ đều vượt khỏi biên bàn cờ. Vì vậy ô $$(1,1)$$ có **bậc bằng 0** (bị cô lập hoàn toàn, không nối với bất kỳ ô nào khác), nên đồ thị nước mã không liên thông và không thể có đường đi hay chu trình Hamilton qua đủ 9 ô.

</details>

### Bài tập 2: Áp dụng Warnsdorf bằng tay

Trên bàn $$5 \times 5$$, xuất phát từ ô $$(0,0)$$. Liệt kê các ô láng giềng mã hợp lệ ở bước đầu và tính $$W(v)$$ (số láng giềng chưa thăm) cho từng ô ứng viên. Warnsdorf sẽ chọn ô nào?

<details>
<summary>Đáp án</summary>

Từ $$(0,0)$$ có đúng 2 nước đi hợp lệ là $$(1,2)$$ và $$(2,1)$$. Khi chỉ mới thăm $$(0,0)$$:
- Từ $$(1,2)$$, các láng giềng mã chưa thăm trên bàn $$5 \times 5$$ là $$(0,4), (2,0), (2,4), (3,1), (3,3)$$ → $$W(1,2) = 5$$.
- Từ $$(2,1)$$, các láng giềng mã chưa thăm là $$(4,0), (0,2), (4,2), (1,3), (3,3)$$ → $$W(2,1) = 5$$.

Do tính đối xứng của bàn cờ qua đường chéo chính, hai ứng viên **hòa nhau** với cùng $$W = 5$$. Khi áp dụng quy tắc phá hòa theo thứ tự từ điển trong hàm `warnsdorf_neighbors`, thuật toán sẽ chọn $$(1,2)$$ trước.

</details>

### Bài tập 3: Open tour và closed tour trên bàn $$4 \times 4$$ và $$5 \times 5$$

Trên bàn $$4 \times 4$$, open tour và closed tour có tồn tại không? Trên bàn $$5 \times 5$$ thì sao? Tra bảng trong bài học để đối chiếu.

<details>
<summary>Đáp án</summary>

- Trên bàn **$$4 \times 4$$**: **không tồn tại** cả open tour lẫn closed tour.
- Trên bàn **$$5 \times 5$$**: **có** open tour nhưng **không có** closed tour (vì $$5 \times 5 = 25$$ là số ô lẻ, còn đồ thị nước mã là đồ thị hai phía nên không thể có chu trình độ dài lẻ). Bàn $$5 \times 5$$ chính là ví dụ điển hình của trường hợp “open có, closed không”.

</details>

### Bài tập 4: Ước lượng cận trên thô của cây tìm kiếm

Từ một ô trung tâm trên bàn $$8 \times 8$$ (ví dụ $$(3,3)$$), quân mã có tối đa 8 nước đi. Nếu không cắt nhánh, cận trên thô cho số lá của cây tìm kiếm độ sâu 64 với hệ số nhánh 8 là $$8^{63}$$. So sánh đại lượng này với $$2^{32}$$ (không gian 32-bit) để thấy vì sao duyệt vét cạn không khả thi.

<details>
<summary>Đáp án</summary>

Ta có $$8^{63} = 2^{189} \approx 7{,}8 \times 10^{56}$$, lớn hơn $$2^{32} \approx 4{,}3 \times 10^9$$ khoảng $$10^{47}$$ lần. Ngay cả khi loại bớt các nhánh bất hợp lệ, không gian tìm kiếm vẫn quá lớn đối với duyệt vét cạn; chỉ có cắt nhánh và heuristic Warnsdorf mới giúp tìm nhanh một hành trình.

</details>

### Bài tập 5: Mô hình đồ thị trên bàn $$4 \times 4$$

Đồ thị nước mã của bàn $$4 \times 4$$ có bao nhiêu đỉnh, bao nhiêu cạnh, và mỗi ô góc có bậc bằng bao nhiêu?

<details>
<summary>Đáp án</summary>

- Số đỉnh: $$\vert V\vert = 4 \times 4 = 16$$.
- Mỗi ô góc (4 ô) có bậc **2**.
- Ngoài 4 ô góc bậc 2, có 8 ô biên còn lại bậc **3** và 4 ô trung tâm bậc **4**. Theo bổ đề bắt tay, tổng số cạnh là:
  $$\vert E\vert = \frac{4 \times 2 + 8 \times 3 + 4 \times 4}{2} = \frac{8 + 24 + 16}{2} = 24 \text{ cạnh}$$
Đây là đồ thị thưa, ít cạnh hơn rất nhiều so với đồ thị đầy đủ $$K_{16}$$ (120 cạnh).

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

**Knight's tour** yêu cầu quân mã đi qua mọi ô trên bàn cờ đúng một lần: **open tour** tương ứng với **đường đi Hamilton**, còn **closed tour** tương ứng với **chu trình Hamilton** trên đồ thị láng giềng nước mã.

Quay lui thuần túy trên bàn $$8 \times 8$$ gặp **bùng nổ tổ hợp**; kết hợp **quy tắc Warnsdorf** (ưu tiên ô có ít láng giềng chưa thăm nhất) giúp tránh ngõ cụt sớm và thường tìm ra lời giải trong chưa đầy 1 mili giây. Bàn $$8 \times 8$$ có hơn 26,5 nghìn tỷ closed tour có hướng, nhưng tìm một hành trình khác hẳn với bài toán đếm toàn bộ. Trên các bàn vuông nhỏ: bàn $$3 \times 3$$ và $$4 \times 4$$ không có tour nào; bàn $$5 \times 5$$ chỉ có open tour (không có closed tour do số ô lẻ); từ $$n \ge 6$$, closed tour tồn tại khi và chỉ khi $$n$$ chẵn.

Bài toán này kết nối trực tiếp chủ đề bùng nổ tổ hợp của Chương 9 với lý thuyết đồ thị Hamilton ở Chương 12 qua phương pháp chung: **mô hình hóa đồ thị kết hợp tìm kiếm có cấu trúc**.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=WN_5ZOFDFqU">Backtracking Explained - Knights Tour</a> — Satheeshkumar Kanakasabapathy, tiếng Anh. Minh họa từng bước giải bài toán mã đi tuần bằng thuật toán quay lui.
- <a href="https://www.youtube.com/watch?v=t_6VByupc1U">[Discrete Mathematics] Hamilton Cycles</a> — TrevTutor, tiếng Anh. Giới thiệu chu trình Hamilton, kết nối trực tiếp với mô hình đồ thị của bài toán mã đi tuần.
