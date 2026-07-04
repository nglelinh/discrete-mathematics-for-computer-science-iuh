---
layout: post
title: "Knight's Tour: Deep dive từ cờ vua đến backtracking và Hamilton"
categories: chapter09
date: 2021-01-01
order: 12
required: false
lang: en
---

# Knight's Tour: Deep dive từ cờ vua đến backtracking và Hamilton

Minh mở LeetCode lúc 23 giờ, gõ `def knightTour(board):` rồi dừng tay. Bài toán nghe đơn giản: quân **mã** (knight) trên bàn cờ $$n \times n$$ phải **đi qua mọi ô đúng một lần**. Không được đứng yên hai lần, không được bỏ sót ô. Quay về ô xuất phát bằng một nước mã hợp lệ — đó là **chu trình** (closed tour). Dừng ở ô cuối mà không đóng vòng — **đường** (open tour).

Thử tay trên bàn $$5 \times 5$$, Minh tìm được một tour trong vài phút. Chuyển sang $$8 \times 8$$, cùng chiến lược “thử hướng nào cũng được” khiến máy treo sau vài giây. Không phải Python chậm — **không gian tìm kiếm** phình theo kiểu combinatorial explosion: không phải “thêm một ô” mà là **nhánh** backtrack nhân lên theo cấp số mũ.

Bài này là **deep dive**: mô hình đồ thị, thuật toán backtracking, heuristic **Warnsdorf** (1823), con số tour trên bàn $$8 \times 8$$, và vì sao bài toán gắn với **đường/chu trình Hamilton** — lớp NP-hard tổng quát mà slide đồ thị (tiết 37) sẽ gặp lại.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Knights_tour.svg"
       alt="Knight's tour trên bàn cờ 8×8 — quân mã đi qua mọi ô đúng một lần"
       width="45%" height="45%">
  <figcaption style="text-align: center;">Hình 9.12a: Bàn cờ → đồ thị → backtracking (+ Warnsdorf) → đường/chu trình Hamilton — cùng kiểu bùng nổ tổ hợp như pairwise testing (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Knight%27s_tour.svg">Ilmari Karonen / Wikimedia Commons</a>, public domain).</figcaption>
</p>
</figure>

---

## Bài toán — đi hết bàn, mỗi ô một lần

**Định nghĩa**: Cho bàn cờ $$n \times n$$. Một **Knight's tour** là dãy các ô $$(r_0,c_0), (r_1,c_1), \ldots, (r_{n^2-1}, c_{n^2-1})$$ sao cho:

1. Mỗi nước từ $$(r_i, c_i)$$ đến $$(r_{i+1}, c_{i+1})$$ là nước mã hợp lệ (chênh $$(\pm 2, \pm 1)$$ hoặc $$(\pm 1, \pm 2)$$).
2. Mọi ô trên bàn xuất hiện **đúng một lần** trong dãy.

| Loại tour | Điều kiện thêm | Ví dụ trực giác |
|:---|:---|:---|
| **Open tour** | Không yêu cầu quay về ô đầu | Đi hết 64 ô, dừng ở ô cuối |
| **Closed tour** | $$(r_{n^2-1}, c_{n^2-1})$$ nhảy mã về $$(r_0, c_0)$$ | Vòng khép kín — ô đầu = ô cuối + 1 nước mã |

Quân mã không đi theo hàng/cột/diagonal như xe/tượng; mỗi ô có **số láng giềng** khác nhau tùy vị trí (góc ít, trung tâm nhiều). Đó là manh mối đầu tiên cho heuristic — không phải mọi ô “còn trống” đều như nhau.

**Ví dụ** bàn $$3 \times 3$$: **không** tồn tại tour nào thăm đủ 9 ô. Ô trung tâm có 8 láng giềng mã nhưng cấu trúc nhỏ khiến không ghép được Hamilton path đủ dài — bài tập 1 sẽ kiểm tra tay.

---

## Mô hình đồ thị — Hamilton trên bàn cờ

Coi mỗi ô $$(r,c)$$ là một **đỉnh**. Nối cạnh giữa hai ô nếu quân mã có thể nhảy từ ô này sang ô kia trong một nước. Ta được đồ thị vô hướng $$G = (V, E)$$:

- $$|V| = n^2$$
- Bậc đỉnh thay đổi: ô góc bậc 2, cạnh biên bậc 3–4, vùng trung tâm bậc tối đa 8 (bàn đủ lớn).

![Đồ thị vô hướng — mô hình láng giềng](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

*Hình 9.20: Bàn cờ → đồ thị vô hướng; tìm tour = tìm đường đi qua mọi đỉnh (nguồn: Wikimedia Commons, chỉnh cho khóa học).*

**Open tour** ⟺ **đường Hamilton** (Hamiltonian path): đường đi qua **mọi đỉnh đúng một lần**.

**Closed tour** ⟺ **chu trình Hamilton** (Hamiltonian cycle): đường Hamilton đóng.

Khác **chu trình Euler** (mỗi **cạnh** một lần — điều kiện bậc chẵn, kiểm tra $$O(E)$$). Hamilton nhìn **đỉnh**, không có điều kiện bậc đơn giản tương đương, và bài toán tổng quát là **NP-hard**. Knight's graph là trường hợp **đặc biệt có cấu trúc** — nên heuristic như Warnsdorf thường tìm tour nhanh trên $$8 \times 8$$ dù bài toán tổng quát vẫn khó.

<div class="content-box insight-box" markdown="1">
**Cùng một backtracking, hai câu chuyện**: SAT solver (slide tiết 43) gán true/false cho biến và backtrack khi clause vỡ; Knight's tour gán “ô tiếp theo” và backtrack khi kẹt. Cả hai đều duyệt không gian tổ hợp — khác ở hàm kiểm tra hợp lệ (clause vs nước mã).
</div>

---

## Combinatorial explosion — vì sao “thử hết” không chạy

DFS thuần trên bàn $$8 \times 8$$: bước đầu từ ô xuất phát có tối đa 8 hướng; bước sau giảm dần vì không được lặp ô. Cây tìm kiếm có độ sâu 64, nhánh phân nhánh theo số láng giềng còn trống — **không** đủ 64! (vì quân mã không tới mọi ô từ mọi ô), nhưng vẫn cực lớn.

Ước lượng thô: nếu trung bình mỗi bước còn 4 lựa chọn, cây có cỡ $$4^{63}$$ — vượt xa số giây trong vũ trụ. Đây chính là **combinatorial explosion** giống nhân 324 cấu hình browser × OS trong QA: không gọi là “chậm” — gọi là **không thể exhaustive** nếu không cắt nhánh thông minh.

Hai hướng giảm:

1. **Pruning**: nếu từ ô hiện tại không còn đường đi tới ô trống nào (ô trống bị cô lập), quay lui ngay — không đợi đến bước 64.
2. **Heuristic**: ưu tiên ô “khó đi sau này” trước — **Warnsdorf**.

---

## Backtracking — khung code

Thuật toán cơ bản: đánh dấu ô đã thăm, thử lần lượt láng giềng mã, đệ quy, bỏ đánh dấu khi quay lui.

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

Trên $$5 \times 5$$, hàm này thường trả lời trong mili giây. Trên $$8 \times 8$$ với thứ tự `moves` cố định, có thể **không** tìm được tour dù tour tồn tại — cây tìm kiếm sai nhánh sâu trước khi gặp lời giải. Minh thêm một dòng: sắp xếp láng giềng theo Warnsdorf trước khi đệ quy — $$8 \times 8$$ gần như luôn ra tour.

**Closed tour**: sau khi `depth == n*n`, kiểm tra thêm ô cuối có nhảy mã về $$(r_0, c_0)$$ không.

---

## Warnsdorf's rule — deep dive

**Ý tưởng** (H. C. von Warnsdorf, 1823): từ ô hiện tại, chọn ô tiếp theo có **số láng giềng chưa thăm ít nhất** (accessibility thấp nhất). Ô “cổ chai” phải đi sớm; ô trung tâm nhiều lối thoát có thể để sau.

**Định nghĩa**: Với ô ứng viên $$v$$, đặt $$W(v) = |\{ u : u \text{ láng giềng mã của } v,\ u \text{ chưa thăm} \}|$$. Chọn $$v$$ với $$W(v)$$ **nhỏ nhất**. Hòa số: chọn ngẫu nhiên hoặc theo thứ tự cố định (ví dụ lexicographic $$(r,c)$$).

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

Thay vòng `for dr, dc in moves` trong `dfs` bằng `for nr, nc in warnsdorf_neighbors(...)`.

| Phương pháp | $$5 \times 5$$ | $$8 \times 8$$ (một ô đầu) | Ghi chú |
|:---|:---|:---|:---|
| DFS thứ tự cố định | Nhanh | Có thể **thất bại** / rất chậm | Phụ thuộc thứ tự nhánh |
| DFS + Warnsdorf | Nhanh | **Thường < 1 ms** | Heuristic, không chứng minh tối ưu mọi $$n$$ |
| Đếm **tất cả** tour | Khả thi | ~26.5 nghìn tỷ (closed, có hướng) | Cần thuật toán chuyên biệt, không Warnsdorf |

<div class="content-box warning-box" markdown="1">
Warnsdorf **không** đảm bảo tìm tour trên mọi bàn và mọi điểm xuất phát. Tồn tại cấu hình mà heuristic chọn sai và kẹt — khi đó cần backtracking đầy đủ hoặc đổi điểm xuất phát. Trong thực hành $$n \le 8$$, Warnsdorf + backtracking khi hòa là tiêu chuẩn.
</div>

**Tại sao hiệu quả?** Đồ thị knight có đỉnh bậc thấp ở góc (2) và cao ở giữa (8). Nếu để ô góc “sống sót” đến cuối, thường không còn nước vào. Warnsdorf ưu tiên ô ít lối — giảm **dead end** sớm, cắt nhánh lớn của cây tìm kiếm. Đây là minh họa điển hình: **cấu trúc đồ thị** + **heuristic** thay cho brute force.

---

## Con số tour trên bàn $$8 \times 8$$ và bàn nhỏ

Bàn **$$8 \times 8$$** là benchmark cổ điển:

| Câu hỏi | Kết quả (đã máy tính) |
|:---|:---|
| Số **closed tour có hướng** (directed) | $$26\,534\,728\,821\,064$$ |
| Số closed tour **vô hướng** (không phân biệt chiều) | $$13\,267\,364\,410\,532$$ |
| Open tour trên $$8 \times 8$$ | Tồn tại (nhiều) |

Con số ~26.5 nghìn tỷ tour **không** có nghĩa phải liệt kê hết để **tìm một** tour — chỉ cần một đường Hamilton. Đếm toàn bộ là bài toán khác (Divide-and-conquer, symmetry breaking — Martin Löbbing & Ingo Wegener, 1996; mở rộng bởi các nhóm sau).

**Bàn nhỏ** — điều kiện tồn tại (closed tour):

| $$n$$ | Closed tour? | Ghi chú |
|:---:|:---:|:---|
| 3 | Không | $$9$$ ô nhưng đồ thị không đủ |
| 4 | Không | Chứng minh bằng parity / case |
| 5 | Có | Dễ thử tay |
| 6 | Có | |
| $$n \ge 5$$ | Có (với mọi $$n$$ đủ lớn, trừ một vài ngoại lệ nhỏ) | Lịch sử toán: nhiều chứng minh từng lớp $$n$$ |

**Điểm xuất phát**: Mọi ô trên $$8 \times 8$$ đều là đầu của ít nhất một **open** tour; không phải mọi ô đều cho **closed** tour (có ô chỉ là đầu open).

---

## Độ phức tạp và NP-hardness

- **Hamiltonian path/cycle** trên đồ thị tổng quát: **NP-complete** (giảm từ SAT hoặc TSP).
- **Knight's tour** trên $$n \times n$$: vẫn thuộc lớp khó tổng quát khi $$n$$ tăng; nhưng đồ thị knight **sparse**, bậc tối đa 8, có cấu trúc lưới — thuật toán chuyên biệt và Warnsdorf hoạt động tốt cho $$n$$ thực tế.

| Bài toán | Đối tượng | Điều kiện nhanh | Thực tế |
|:---|:---|:---|:---|
| Euler cycle | Cạnh | Bậc chẵn | $$O(E)$$ |
| Hamilton cycle | Đỉnh | Không có test đơn giản | NP-hard; knight tour là case đặc biệt |
| Một tour knight $$8 \times 8$$ | Đỉnh | Warnsdorf + backtrack | Thường tức thì |

Ứng dụng CS không chỉ là cờ vua: tư duy **model as graph → search with pruning** xuất hiện trong lập lịch (routing), kiểm thử (cover path), và puzzle solver (Sudoku cũng là CSP + backtrack).

---

## Công cụ tương tác

<div data-demo="euler-hamilton-checker"></div>

Widget trên minh họa **Euler vs Hamilton** trên đồ thị nhỏ — cùng phân biệt “duyệt cạnh” và “duyệt đỉnh” mà Knight's tour thuộc về nhánh Hamilton.

---

## Ứng dụng trong Khoa học Máy tính

- **Backtracking template**: thử → đệ quy → undo — khung chung cho Sudoku, N-Queens, Knight's tour, và SAT.
- **Heuristic search**: Warnsdorf là bài học sớm về “không cần tối ưu toàn cục, chỉ cần rule cục bộ tốt”.
- **Interview / competitive programming**: biến thể LeetCode *Knight Probability in Chessboard*, *Minimum Knight Moves* (BFS ngắn nhất), và tour đủ ô.
- **Song song QA**: không thể test hết mọi đường đi — giống không thể thử hết mọi tour; cần cấu trúc và cắt nhánh (pairwise, property-based test).

Minh sau bài này giữ `warnsdorf_neighbors` trong repo cá nhân — không phải để chơi cờ, mà để nhắc: khi PM hỏi “sao không thử hết combination”, anh có thể kể Knight's tour và con số 26.5 nghìn tỷ.

---

## Bài tập thực hành

### Bài tập 1: Bàn $$3 \times 3$$

Chứng minh không tồn tại Knight's tour (open hay closed) thăm đủ 9 ô. Gợi ý: ô góc có bậc 2 trong đồ thị knight — đếm tối đa số ô có thể đến từ một góc nếu đi theo chuỗi nước mã.

<details>
<summary>Đáp án</summary>

Ô góc chỉ nối 2 ô. Trong tour dài 9, ô góc không thể ở giữa dãy (cần 2 láng giềng đã thăm + 1 chưa thăm). Case analysis trên $$3 \times 3$$ cho thấy không ghép được đường đi độ dài 8 cạnh qua 9 đỉnh — có thể kiểm tra bằng backtracking nhỏ hoặc bảng liệt kê đầy đủ.

</details>

### Bài tập 2: Warnsdorf tay

Trên bàn $$5 \times 5$$, xuất phát $$(0,0)$$. Liệt kê các ô láng giềng mã hợp lệ và tính $$W(v)$$ (số láng giềng chưa thăm) cho từng ứng viên bước đầu. Ô nào Warnsdorf chọn?

<details>
<summary>Đáp án</summary>

Từ $$(0,0)$$ chỉ có 2 nước: $$(1,2)$$ và $$(2,1)$$. Tính $$W$$ cho mỗi ô (giả sử chỉ ô xuất phát đã thăm): thường $$(2,1)$$ và $$(1,2)$$ có accessibility khác nhau — ô có $$W$$ nhỏ hơn được chọn. Chạy code `warnsdorf_neighbors(5,0,0,...)` để đối chiếu.

</details>

### Bài tập 3: Open vs closed

Giải open tour trên $$4 \times 4$$ bằng backtracking (có thể không tồn tại). Closed tour trên $$4 \times 4$$ có tồn tại không? Tra bảng bài học.

<details>
<summary>Đáp án</summary>

**Closed** tour trên $$4 \times 4$$: **không**. **Open** tour: có — tồn tại đường Hamilton mở (không đóng vòng). Đây là ví dụ “open có, closed không”.

</details>

### Bài tập 4: Đếm nhánh thô

Bước đầu tour $$8 \times 8$$ từ ô trung tâm (ví dụ $$(3,3)$$) có tối đa 8 láng giềng. Nếu **không** cắt nhánh, ước lượng số lá **tối đa** của cây tìm kiếm độ sâu 64 với nhánh 8 (cận trên siêu lỏng $$8^{63}$$). So sánh với $$2^{32}$$ (giới hạn 32-bit) — vì sao “thử hết” là không tương đương “chạy một lần trên laptop”?

<details>
<summary>Đáp án</summary>

$$8^{63} \approx 10^{57}$$ — lớn hơn $$2^{32} \approx 4 \times 10^9$$ khoảng $$10^{48}$$ lần. Ngay cận trên lỏng đã vượt mọi giới hạn thực tế; pruning và Warnsdorf thu nhỏ cây xuống đường đi **một** tour.

</details>

### Bài tập 5: Mô hình đồ thị

Bàn $$4 \times 4$$ có bao nhiêu đỉnh và (theo định nghĩa bài) tối đa bao nhiêu cạnh nếu đếm mỗi cặp láng giềng mã một cạnh? Một đỉnh góc bậc bao nhiêu?

<details>
<summary>Đáp án</summary>

$$|V| = 16$$. Ô góc bậc **2**. Tổng số cạnh: đếm tay hoặc chương trình — mỗi cạnh nối hai ô cách nhau một nước mã; đồ thị sparse, không phải $$K_{16}$$.

</details>

---

## Tóm tắt

**Knight's tour** = đi qua mọi ô đúng một lần bằng nước mã; **open** tương ứng **đường Hamilton**, **closed** tương ứng **chu trình Hamilton** trên đồ thị láng giềng mã.

Brute force backtrack gặp **combinatorial explosion** — cây tìm kiếm cỡ hàm mũ, không khả thi trên $$8 \times 8$$ nếu không heuristic. **Warnsdorf**: ưu tiên ô có ít láng giềng chưa thăm — cắt dead end, thường tìm tour tức thì.

Bàn $$8 \times 8$$ có **hơn 26 nghìn tỷ** closed tour có hướng, nhưng chỉ cần **một** tour cho ứng dụng; đếm toàn bộ là bài toán riêng. Bàn $$4 \times 4$$ không có closed tour; $$3 \times 3$$ không có tour nào đủ 9 ô.

Knight's tour nối chương 9 (explosion, backtracking thực chiến) với đồ thị Hamilton (tiết 37 / chương 12): cùng kỹ thuật **mô hình hóa + tìm kiếm có cấu trúc**, khác ở domain cờ vua và heuristic Warnsdorf.