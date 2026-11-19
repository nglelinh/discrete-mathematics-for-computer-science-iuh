# Kế hoạch xây dựng explainer tương tác cho Toán Rời Rạc

Tài liệu này đề xuất cách xây dựng một hệ thống trực quan hóa tương tác trên trình duyệt — theo tinh thần [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) (Polo Club, Georgia Tech) — cho khóa [Toán Rời Rạc cho Khoa học Máy tính](https://nglelinh.github.io/discrete-mathematics-for-computer-science-iuh/). Mục tiêu không phải là thêm vài máy tính cầm tay, mà là để sinh viên *nhìn từng bước* một khái niệm trừu tượng, tự chỉnh tham số, và nối ngay lại bài lý thuyết đang học.

**Trạng thái:** chỉ là kế hoạch (chưa triển khai). Viết tháng 11/2026, dựa trên cấu trúc hiện tại của repo `discrete-mathematics-for-computer-science-iuh`.

## 1. Bối cảnh và mục tiêu

Transformer Explainer thành công vì bốn đặc điểm, và khóa này nên sao chép đúng bốn đặc điểm đó:

1. **Chạy ngay trên trình duyệt**, không cài đặt, không máy chủ.
2. **Luồng tổng thể + chi tiết khi cần** — nhìn cả kiến trúc, rồi mở ra từng phép tính.
3. **Tham số tương tác** — kéo thanh trượt, đổi input, thấy kết quả đổi tức thì.
4. **Gắn với lý thuyết** — mỗi khung hình tương ứng một định nghĩa, một công thức, một bài học.

Khóa Discrete Math *đã có* nền tảng cho (1) và một phần (3). Trong `public/js/` hiện có khoảng 50 widget vanilla JS, được nhúng vào bài bằng mẫu:

```html
<div class="interactive-demo" markdown="1">
  <div data-demo="bfs-dfs-visualizer"></div>
</div>
<script src="{{ '/public/js/bfs-dfs-visualizer.js' | relative_url }}"></script>
```

`tools.html` đóng vai trò mục lục công cụ. README cũng đã nêu “lý thuyết tương tác” như một phương pháp giảng dạy.

Khoảng trống so với mức explainer:

- Nhiều widget chỉ là máy tính nhỏ (3–6 KB, logic bị nén một dòng), chưa có hoạt ảnh từng bước, chưa có chú thích lý thuyết cạnh hình.
- Một số công cụ khá tốt (`bfs-dfs-visualizer.js`, `truth-table-normal-form.js`, `predicate-proof-dnd.js`, `dfa-simulator.js`) nhưng **chưa được gắn đều vào bài** — khoảng 30 file JS chưa xuất hiện trong `contents/`.
- Chưa có ngôn ngữ thiết kế chung, chưa có chế độ “bài tập hướng dẫn” (guided exercise) đi kèm, chưa có bản đồ “khái niệm → công cụ → bài học”.
- Giao diện tiếng Việt đã có ở nhiều widget, nhưng trải nghiệm còn rời rạc.

Định hướng: **nâng cấp và thống nhất** những gì đã có, rồi làm vài explainer “kỳ cựu” (flagship) đạt chất lượng Transformer Explainer, chứ không viết lại từ không.

## 2. Khóa học hiện tại (cần bám vào)

Site là Jekyll, nội dung chính bằng tiếng Việt (tên file bài học tiếng Anh), cấu hình đa ngữ trong `_config.yml` đang được để dành. Có 20 chương:

| Ch. | Tiêu đề | Nhóm |
|----:|---------|------|
| 1 | Logic mệnh đề | Nền tảng |
| 2 | Logic vị từ | Nền tảng |
| 3 | Phương pháp chứng minh | Nền tảng |
| 4 | Lý thuyết tập hợp | Tập hợp / quan hệ / hàm |
| 5 | Quan hệ | Tập hợp / quan hệ / hàm |
| 6 | Hàm số | Tập hợp / quan hệ / hàm |
| 7 | Nguyên lý đếm cơ bản | Đếm |
| 8 | Nguyên lý Dirichlet | Đếm |
| 9 | Ứng dụng CNTT hiện đại | Ứng dụng |
| 10 | Quan hệ truy hồi | Truy hồi / hàm sinh |
| 11 | Hàm sinh và bao hàm–loại trừ | Truy hồi / hàm sinh |
| 12 | Lý thuyết đồ thị | Đồ thị / cây / thuật toán |
| 13 | Đại số Boole | Boole / mạch |
| 14 | Thuật toán và độ phức tạp (Big-O) | Thuật toán |
| 15 | Lý thuyết số và mật mã | Số học |
| 16 | Cây, MST, Huffman, BST | Đồ thị / cây / thuật toán |
| 17 | Đồ thị nâng cao (Dijkstra, tô màu, matching) | Đồ thị / cây / thuật toán |
| 18 | Mô hình tính toán (DFA/NFA/regex/TM) | Automat / ngôn ngữ / phức tạp |
| 19 | Ngôn ngữ hình thức và văn phạm | Automat / ngôn ngữ / phức tạp |
| 20 | Độ phức tạp tính toán | Automat / ngôn ngữ / phức tạp |

Mọi explainer mới phải trỏ ngược về bài cụ thể (ví dụ `12-04`, `17-01`, `01-03`), dùng ký hiệu và ví dụ đã có trong giáo trình, và nhúng được vào trang bài bằng `data-demo` như hiện nay.

## 3. Chủ đề nào được lợi nhiều nhất

Không phải mọi chương đều đáng làm explainer đầy đủ. Ưu tiên những chủ đề (a) sinh viên hay hiểu sai khi chỉ đọc công thức, (b) có trạng thái từng bước để vẽ, (c) chỉnh một tham số là thấy hệ quả, (d) dùng được trên lớp 10–15 phút.

### Ưu tiên cao (P0) — làm flagship

| Chủ đề | Chương | Vì sao đáng làm | Đã có sẵn trong repo |
|--------|--------|-----------------|----------------------|
| Bảng chân trị, tương đương, DNF/CNF | 1 | Thao tác ∧ ∨ → ↔ và “hàng nào làm mệnh đề đúng” rất hợp explainer | `truth-table-normal-form.js` (chưa gắn bài), `logic-operator-widgets.js` |
| Tập hợp và biểu đồ Venn | 4, 7, 11 | Phép toán và bao hàm–loại trừ “nhìn được” | `set-operations-visualizer.js`, `venn-counter.js`, `venn-ie-three-sets.js` (một phần chưa gắn bài) |
| Quan hệ: ma trận, tính chất, bao đóng Warshall | 5 | Ma trận ↔ đồ thị có hướng là chỗ sinh viên hay đứt mạch | `relation-matrix-toggle.js`, `relation-properties-checker.js`, `warshall-visualizer.js` (chủ yếu chưa gắn bài) |
| Hàm: đơn ánh, toàn ánh, song ánh, hợp hàm | 6 | Sơ đồ mũi tên và đếm tiềnảnh là trực quan | `function-arrow-checker.js`, `function-property-checker.js`, `function-composition-pipeline.js` (chưa gắn bài) |
| Đếm: hoán vị, tổ hợp, stars-and-bars | 7 | Tham số n, k đổi là thấy công thức và hình đổi | `binomial-coefficient-calc.js`, `stars-bars-visualizer.js`, `inclusion-exclusion-toggle.js` |
| Duyệt đồ thị BFS/DFS, Euler/Hamilton | 12 | Đã có widget từng bước tốt nhất khóa học; nên nâng thành explainer chuẩn | `bfs-dfs-visualizer.js`, `euler-hamilton-checker.js`, `graph-adjacency-builder.js` |
| Dijkstra | 17 | Cần thấy tập S, khoảng cách d(v), cạnh được thư giãn | `dijkstra-visualizer.js` (bản nhỏ, đã gắn `17-01`) |
| MST (Kruskal/Prim) | 16 | Rất hợp hoạt ảnh từng cạnh, union-find | `kruskal-algorithm.js` |
| Đại số Boole, cổng, Karnaugh | 13 | Ô 0/1/X, nhóm lũy thừa 2, đa thức tối tiểu | `kmap-interactive.js`, `logic-gates-builder.js` (chưa gắn bài), `boolean-expression-evaluator.js`, `quine-mccluskey-simplifier.js` |
| Duyệt cây, Huffman | 16 | Pre/in/post-order và xây cây mã là “nhìn là hiểu” | `tree-traversal-visualizer.js`, `huffman-coding.js` |

### Ưu tiên trung bình (P1)

| Chủ đề | Chương | Ghi chú |
|--------|--------|---------|
| Lượng từ lồng nhau | 2 | Lưới đối tượng × tính chất; đã có `nested-quantifier-grid.js` |
| Chứng minh trực tiếp / quy nạp từng bước | 3 | `direct-proof-builder.js`, `induction-step-checker.js` — hỗ trợ bài tập hơn là “wow visual” |
| Nguyên lý Dirichlet | 8 | `pigeonhole-visualizer.js` — trực quan nhưng nông; nên gắn ví dụ hashing / birthday (chương 9) |
| Quan hệ truy hồi và hàm sinh | 10–11 | `recurrence-visualizer.js`, `linear-recurrence-solver.js`, `generating-function-explorer.js` |
| Euclid, modulo, RSA | 15 | `euclidean-algorithm.js`, `modular-arithmetic-calc.js`, `rsa-simulator.js` — nên có hoạt ảnh vòng chia và sơ đồ trao khóa |
| DFA / NFA / regex | 18 | `dfa-simulator.js` đã viết nhưng chưa commit/gắn bài; đây là flagship tự nhiên của nửa sau khóa học |
| Cây phân tích, CYK, PDA | 19 | Hợp explainer, nhưng công hơn và dùng sau trong kỳ |

### Ưu tiên thấp hơn hoặc làm nhẹ (P2)

- **Chương 9** (ứng dụng CNTT): tái sử dụng explainer của logic/đếm/tập hợp trên case study, không cần tool riêng.
- **Chương 14 (Big-O):** `big-o-growth-comparator.js` đủ nếu làm đồ thị so sánh rõ; khó thành explainer “từng bước”.
- **Chương 20 (P/NP, reduction):** rất khó vẽ trung thực. Nên làm *một* bộ demo giảm SAT → 3SAT và IS/CLIQUE/VC với đồ thị nhỏ, cộng liên kết ra SAT solver, chứ không hứa explainer đầy đủ.
- Máy Turing, pumping lemma: có công cụ ngoài (JFLAP và các mô phỏng sẵn); liên kết và chỉ tự làm bản rút gọn nếu còn sức.

## 4. Đề xuất công cụ và phác thảo giao diện

Mỗi explainer theo một khung chung (giống Transformer Explainer): **thanh input / tham số phía trên**, **luồng chính ở giữa**, **panel “đang xảy ra bước này” và công thức bên phải hoặc dưới**, **bài tập hướng dẫn có thể thu gọn**.

Gợi ý UI cho từng nhóm P0:

### 4.1. Logic Explainer (Ch. 1)

- Ô nhập công thức với `P, Q, R` và các phép `¬ ∧ ∨ → ↔`.
- Bảng chân trị được tô từng hàng; click một hàng để thấy phép tính con (cây biểu thức).
- Thanh trượt hoặc nút “ẩn/hiện cột trung gian”.
- Nút “xuất DNF / CNF” và đánh dấu các hàng làm mệnh đề đúng — nối với `01-03`, `01-04`.
- Bài tập: “Biến `(P ∧ Q) → R` thành CNF; kiểm tra tương đương với công thức của bạn.”

### 4.2. Set / Venn Explainer (Ch. 4, 7, 11)

- Ba tập A, B, C; nhập phần tử hoặc dùng tập mẫu.
- Click vùng Venn để bật/tắt membership; công thức (`A ∪ B`, `A ∩ B^c`, …) đổi theo vùng đang chọn.
- Chế độ bao hàm–loại trừ: bật từng hạng tử `|A|`, `|A ∩ B|`, … và thấy tổng chạy.
- Nối `04-02`, `07-03`, `11-03`.

### 4.3. Relation Explainer (Ch. 5)

- Ba khung cạnh nhau: danh sách cặp, ma trận 0/1, đồ thị có hướng.
- Sửa một phía, hai phía còn lại cập nhật.
- Đèn kiểm tra: phản xạ, đối xứng, phản đối xứng, bắc cầu; nút “tính bao đóng” chạy Warshall từng vòng `k`.
- Chế độ quan hệ tương đương (phân hoạch) và Hasse diagram cho thứ tự bộ phận.
- Nối `05-02`, `05-03`, `05-04`.

### 4.4. Function Explainer (Ch. 6)

- Hai hàng nút (miền và miền giá trị) với mũi tên kéo-thả.
- Đèn “đơn ánh / toàn ánh / song ánh” cập nhật tức thì; đếm tiềnảnh từng điểm.
- Chế độ hợp hàm `g ∘ f` dạng đường ống.
- Bài tập: “Biến hàm cho trước thành song ánh bằng cách thêm/bớt đúng một mũi tên” (nếu được).

### 4.5. Counting Explainer (Ch. 7–8)

- Chọn mô hình: hoán vị, tổ hợp, lặp, stars-and-bars.
- Thanh `n`, `k`; hình (chỗ ngồi, ngôi sao/cạnh) và công thức $$C(n,k)$$, $$P(n,k)$$, $$C(n+k-1,k)$$ đổi cùng lúc.
- Pigeonhole: `n` vật vào `m` hộp, tô hộp vượt trần; ví dụ phụ “sinh nhật / collision”.
- Nối `07-02`, `07-05`, `08-01`, `09-07`.

### 4.6. Graph Algorithm Explainer (Ch. 12, 16, 17) — flagship nên làm trước

Đây là “Transformer Explainer” của khóa: một canvas đồ thị dùng chung, nhiều thuật toán.

- Sinh viên vẽ / sửa đồ thị (thêm đỉnh, cạnh, trọng số) hoặc chọn đồ thị mẫu.
- Chọn thuật toán: BFS, DFS, Euler tour, Dijkstra, Kruskal, Prim, tô màu tham lam.
- Điều khiển: Bước trước / bước sau / chạy chậm; panel hàng đợi hoặc heap; tập đã thăm; cạnh đang xét.
- Cột phải: bất biến (ví dụ “với BFS, `d(v)` là số cạnh ngắn nhất từ s”; với Dijkstra, bất biến tập S).
- Xuất thứ tự thăm, cây duyệt / cây khung, khoảng cách.
- Tái sử dụng và nâng `bfs-dfs-visualizer.js` (đã có queue/stack, từng bước, reset) thành lõi chung.

### 4.7. Boolean / K-map Explainer (Ch. 13, một phần Ch. 9)

- Nhập hàm 2–4 biến hoặc click minterm.
- Lưới Karnaugh; sinh viên khoanh nhóm, tool chấm nhóm hợp lệ (hình chữ nhật, kích thước lũy thừa 2, wrap-around).
- Song song: mạch cổng (AND/OR/NOT, rồi NAND) và đa thức tối tiểu.
- Bước “so với Quine–McCluskey” để thấy cùng một hàm, hai thuật toán.
- Nối `13-03`, `13-04`, `13-05`, `09-04`.

### 4.8. Tree / Huffman Explainer (Ch. 16)

- Cây nhị phân mẫu; nút pre/in/post-order với stack hoặc đệ quy được vẽ.
- Huffman: nhập tần suất ký tự, từng bước gộp hai nút nhỏ nhất, hiện mã và độ dài trung bình.
- Nối `16-02`, `16-04`.

### 4.9. Automata Explainer (Ch. 18, P1 nhưng rất “đáng đồng tiền”)

- Vẽ DFA/NFA (trạng thái, mũi tên, ε), nhập chuỗi, chạy từng ký tự, tô trạng thái hiện tại.
- Chế độ subset construction: NFA → DFA, từng tập trạng thái được tạo ra.
- Ô regex ↔ Automat (phạm vi hạn chế).
- Nối `18-01` đến `18-05`, `18-07`. Nền tảng: `dfa-simulator.js` (chưa gắn bài).

Mọi explainer đều có một mục **“Bài tập hướng dẫn”** (5–7 bước, giống bài 08-02 bên khóa Deep Learning) và liên kết “xem lại lý thuyết” tới permalink Jekyll của bài.

## 5. Công nghệ phù hợp với site Jekyll

Ràng buộc: site tĩnh, GitHub Pages, bài học là Markdown, widget đang là IIFE vanilla JS tự gắn vào `data-demo="..."`.

**Đề xuất:**

- **Giữ cách nhúng hiện tại.** Explainer mới vẫn mount bằng `data-demo` và một file (hoặc một bundle) trong `public/js/` hoặc `public/explainers/`. Không phụ thuộc backend.
- **Lõi flagship (đồ thị, logic, automat):** viết bằng **Svelte** (cùng hướng với Transformer Explainer) biên dịch ra JS tĩnh, vẽ bằng **SVG + D3** (đồ thị, Venn, cây) hoặc SVG thuần (K-map, ma trận). Đây là công cụ build, không phải runtime khung nặng trên trang bài.
- **Widget nhỏ đã ổn:** giữ vanilla JS, chỉ chỉnh CSS cho thống nhất, rồi gắn nốt vào bài còn thiếu.
- **Design system nhẹ:** một file `public/css/explainer.css` (viền, typography, nút Bước/Reset, màu tập/cạnh/trạng thái) để mọi tool trông cùng một họ.
- **Không iframe công cụ ngoài làm trải nghiệm chính** (phụ thuộc mạng, khác ngôn ngữ, khác ký hiệu). Được phép có mục “Xem thêm” tới VisuAlgo, JFLAP, v.v.
- **Ngôn ngữ UI: tiếng Việt trước**; khóa các chuỗi trong một dictionary nhỏ để sau này bật `en` khi `_config.yml` bật đa ngữ.
- **Gói bài tập:** JSON nhỏ cạnh mỗi tool (`public/explainers/exercises/12-04-bfs.json`) để tái sử dụng trên lớp và trong phần bài tập cuối bài.
- **Kiểm thử:** unit test thuần cho phần thuật toán (BFS thứ tự thăm, Warshall, nhóm K-map hợp lệ) bằng Node; vài smoke test Playwright cho flagship (tùy chọn, giai đoạn sau).
- **Không cần** React/Next, không cần server Python. Tránh phụ thuộc CDN bắt buộc (bundle vào repo) để dùng được khi demo offline trong lớp.

Kho `interactive_math` (cùng thư mục `teaching/`) có một số trực quan hóa (kể cả graph-theory); chỉ **tham khảo và tái sử dụng ý tưởng/đoạn mã nếu giấy phép cho phép**, không trộn hai site thành một runtime.

## 6. Giai đoạn, ưu tiên và ước lượng

Ước lượng theo **người-ngày** cho một developer đã quen repo (đã có widget). Một “cột mốc” có thể demo được trên lớp.

| Giai đoạn | Việc làm | Ưu tiên | Ước lượng |
|-----------|----------|---------|-----------|
| **0. Nền** | Kiểm kê widget (cái nào gắn bài, cái nào chỉ là máy tính); chốt design system; viết `docs` nhúng + quy ước `data-demo`; bản đồ “bài học → tool”. | P0 | 3–5 ngày |
| **1. Gắn nốt những gì đã có** | Nhúng các JS chưa dùng vào đúng bài (truth table vào 01-03/01-04, K-map vào 13-04, Venn/set vào 04-02, quan hệ/Warshall vào 05, hàm vào 06, DFA vào 18, pigeonhole vào 08). Sửa lỗi nhỏ, thống nhất CSS. | P0 | 4–6 ngày — *giá trị lớp học nhanh nhất* |
| **2. Flagship đồ thị** | Nâng BFS/DFS + Dijkstra + Kruskal/Prim + Euler lên một Graph Explainer dùng chung, có bước tới/lui, bất biến, đồ thị do SV vẽ, bài tập hướng dẫn. | P0 | 12–16 ngày |
| **3. Logic + Boole + K-map** | Explainer công thức–bảng chân trị–DNF/CNF; K-map có chấm nhóm; cổng logic 2–4 biến. | P0 | 10–14 ngày |
| **4. Tập hợp, quan hệ, hàm** | Venn tương tác; Relation Explainer 3 khung; Function Explainer mũi tên. | P0 | 10–14 ngày |
| **5. Đếm + truy hồi** | Stars-and-bars / C(n,k) / pigeonhole; visualizer dãy truy hồi (số hạng, cây đệ quy, so với công thức đóng). | P1 | 7–10 ngày |
| **6. Automata** | DFA/NFA từng ký tự + subset construction; regex ở phạm vi hẹp. | P1 | 12–16 ngày |
| **7. Cây, Huffman, số học, hoàn thiện** | Nâng traversal/Huffman; Euclid/RSA từng bước; guided exercises đều; mục lục `tools.html` làm hub thật sự. | P1 | 7–10 ngày |
| **8. (Tùy chọn) Ngôn ngữ hình thức & phức tạp** | Parse tree / CYK rút gọn; một bộ reduction SAT–3SAT–CLIQUE. | P2 | 8–12 ngày |

**Tổng P0 (giai đoạn 0–4):** khoảng **6–8 tuần** làm tập trung, hoặc một học kỳ nếu làm song song giảng dạy.  
**Thêm P1 (5–7):** khoảng **+4–6 tuần**.  
Nên ra mắt được **giai đoạn 1 + 2** trước một kỳ học (đồ thị + gắn widget cũ), rồi bổ sung dần.

Thứ tự ra mắt đề xuất trong một kỳ: *Ch. 1 (logic) → Ch. 4–6 (tập/quan hệ/hàm) → Ch. 7–8 (đếm) → Ch. 12–17 (đồ thị/cây)* đúng tiến độ giảng. Flagship đồ thị có thể được dev trước dù dạy sau, vì tái sử dụng nhiều và “thuyết phục” nhất khi demo.

## 7. Cách dùng trên lớp và trong bài tập

**Trên lớp (10–15 phút):**

- Mở explainer đã nhúng ngay trong bài, không đổi tab (trừ lúc “xem thêm”).
- Giảng viên chạy một ví dụ mẫu (cùng ví dụ trong slide/giáo trình), dừng ở bước dễ sai (mask tương lai không có ở đây, nhưng tương đương: quên cạnh đã xét trong Kruskal, quên hàng `P=0` trong bảng chân trị, quên ô wrap-around của K-map).
- Một sinh viên đề xuất bước tiếp theo trước khi bấm “Bước sau”.

**Tự học:**

- Mỗi explainer có 5–7 bước guided exercise, viết câu trả lời ngắn trong vở hoặc form bài tập.
- Cuối bài lý thuyết có mục “Thực hành với explainer” (mẫu giống bài 08-02 bên khóa Deep Learning).

**Bài tập chấm được (một phần):**

- Với logic, quan hệ, hàm, K-map, DFA: tool có thể **kiểm tra** câu trả lời (đúng/sai, gợi ý), không thay bài chứng minh viết.
- Với đồ thị: nộp thứ tự thăm / cây khung / khoảng cách; tool so khớp với đồ thị đề bài (đồ thị được chốt trong JSON).

**Đánh giá:** chiếm một phần mục “Bài tập và thực hành 20%” đã ghi trong README — không thay bài thi viết, nhưng có thể là bài tập bắt buộc trước buổi đồ thị / logic.

**Không dùng explainer để:** chứng minh hình thức dài, bài NP-complete mang tính giảm trừ phức tạp (trừ demo nhỏ), hoặc thay việc sinh viên tự lập bảng chân trị lần đầu (hãy để họ làm tay, rồi đối chiếu).

## 8. Công cụ sẵn có để tái sử dụng hoặc tham khảo

### Trong repo này (tái sử dụng trước)

- Lõi từng bước tốt: `public/js/bfs-dfs-visualizer.js`.
- Logic / chứng minh: `truth-table-normal-form.js`, `predicate-proof-dnd.js`, `logic-operator-widgets.js`.
- Quan hệ / hàm / tập: các file `relation-*`, `function-*`, `set-operations-visualizer.js`, `warshall-visualizer.js`, `hasse-diagram.js`.
- Đồ thị / cây: `dijkstra-visualizer.js`, `kruskal-algorithm.js`, `graph-coloring-interactive.js`, `graph-adjacency-builder.js`, `tree-traversal-visualizer.js`, `huffman-coding.js`, `euler-hamilton-checker.js`.
- Boole: `kmap-interactive.js`, `quine-mccluskey-simplifier.js`, `logic-gates-builder.js`.
- Đếm / truy hồi / số: `stars-bars-visualizer.js`, `recurrence-visualizer.js`, `euclidean-algorithm.js`, `rsa-simulator.js`.
- Automat (chưa gắn bài): `public/js/dfa-simulator.js`.
- Mục lục: `tools.html`.

### Bên ngoài — thiết kế và đối chuẩn (không thay thế sản phẩm của khóa)

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) và [CNN Explainer](https://poloclub.github.io/cnn-explainer/) — chuẩn mực “tổng thể + chi tiết + tham số”. Mã nguồn MIT: [poloclub/transformer-explainer](https://github.com/poloclub/transformer-explainer).
- [VisuAlgo](https://visualgo.net/) — BFS/DFS, Dijkstra, MST, cây; rất mạnh nhưng đóng, khác ngôn ngữ/ký hiệu; dùng như “xem thêm”, không nhúng làm lõi.
- [Data Structure Visualizations (Galles, USFCA)](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html) — Dijkstra, Kruskal, Prim, Union-Find.
- [algorithm-visualizer](https://algorithm-visualizer.org/) và repo [algorithm-visualizer/algorithm-visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer).
- [Graph Online](https://graphonline.ru/en/) — vẽ đồ thị, chạy thuật toán; tham khảo UX tạo đồ thị.
- [JFLAP](https://www.jflap.org/) — chuẩn mực DFA/NFA/PDA/TM (desktop); trên web có thể xem [automaton simulator](https://automatonsimulator.com/) hoặc các dự án fsm.js mã mở.
- Bảng chân trị: nhiều máy tính mở, ví dụ ý tưởng từ các truth-table generator cổ điển; tự làm để khớp ký hiệu giáo trình (`∧ ∨ → ↔`).
- Karnaugh: các K-map solver phổ biến (chỉ đối chiếu kết quả); logic mạch có thể tham khảo tinh thần [Nand2Tetris](https://www.nand2tetris.org/) (phần cứng) nhưng không thay K-map 4 biến của chương 13.
- Toán rời rạc tổng quát: applets trong hệ sinh thái Rosen / các demo [Wolfram Demonstrations — Discrete Math](https://demonstrations.wolfram.com/topic.html?topic=Discrete+Mathematics) (giấy phép hạn chế, không nhúng nguyên).
- [SageMath / Sage Cell](https://sagecell.sagemath.org/) — tốt cho đếm và hàm sinh, nhưng nặng và phụ thuộc dịch vụ ngoài; chỉ dùng như liên kết phụ.
- Thư viện vẽ: [D3](https://d3js.org/), [Cytoscape.js](https://js.cytoscape.org/) (đồ thị), SVG thuần cho ma trận và K-map.

Khi sao chép ý tưởng hoặc đoạn mã, ghi nguồn và tuân giấy phép (MIT/BSD thì được, với ghi công; công cụ đóng thì chỉ link).

## 9. Rủi ro, phạm vi và tiêu chí xong việc

**Rủi ro:**

- Làm quá nhiều tool nông thay vì ít tool sâu — đây là sai lầm dễ gặp vì repo *đã* có nhiều widget.
- Widget thuật toán vẽ sai một cạnh trường hợp (đồ thị không liên thông, cạnh 0, K-map wrap) sẽ dạy sai. Cần test thuật toán tách khỏi UI.
- Hiệu năng canvas khi đồ thị > ~30 đỉnh: giới hạn rõ trên UI (“dùng cho ví dụ học, không phải đồ thị lớn”).
- Phụ thuộc CDN hoặc iframe sẽ hỏng khi dạy offline.

**Tiêu chí một explainer được coi là xong:**

1. Chạy trong trang bài Jekyll, tiếng Việt, không cần server.
2. Có bước tới/lui hoặc tương tác tham số, không chỉ “nhấn = ra kết quả”.
3. Có chú thích / công thức / bất biến cạnh hình.
4. Có bài tập hướng dẫn và liên kết ngược tới bài lý thuyết.
5. Có ít nhất một bộ test cho phần tính toán cốt lõi.
6. Ghi nguồn nếu dùng lại mã hoặc hình ngoài.

**Việc không làm trong kế hoạch này:** viết lại toàn bộ giáo trình, xây LMS, chấm thi tự động toàn phần, hay port toàn bộ VisuAlgo.

## 10. Việc nên làm ngay sau khi duyệt kế hoạch

1. Chốt làm **Giai đoạn 0–2** trong kỳ tới (gắn widget cũ + Graph Explainer).
2. Chọn 3 bài “neo” để gắn guided exercise trước: `01-03` (bảng chân trị), `12-04` (BFS/DFS), `17-01` (Dijkstra).
3. Không push / không mở trang công cụ mới cho đến khi flagship đồ thị ổn định trên bản local.

Kế hoạch này cố ý đi từ cái đã có. Thành công không phải là 50 widget mới, mà là vài explainer sinh viên chịu mở lại khi ôn thi — và giảng viên dùng được ngay trên trang bài, trong một buổi học.


## Tiến độ thực hiện

Cập nhật: 2026-11-18 (Asia/Saigon). Làm **chỉ trên máy local**, chưa commit / chưa push. Nhánh đang checkout: `feature/interactive-explainer-plan`.

### Giai đoạn 0 — xong

Đã viết `docs/widget-inventory.md`: danh sách widget đã gắn, gắn dở, chưa gắn, file hạ tầng, và những file không đụng vì là thay đổi chưa commit của Linh (`bfs-dfs-visualizer.js`, `euler-hamilton-checker.js`, `dfa-simulator.js`).

### Giai đoạn 1 — xong (phần P0/P1 đã lên kế hoạch gắn bài)

- Sửa bốn bài có `data-demo` nhưng thiếu `<script>`: 02-04, 09-00, 09-04, 09-12.
- Bổ sung tương thích `data-demo` cho một số widget cũ (`truth-table-normal-form`, `venn-counter`, `set-operations-visualizer`, `function-property-checker`, `predicate-proof-dnd`, wrapper `logic-operator-widgets`).
- Nhúng các widget chưa gắn vào bài tương ứng (chi tiết trong inventory và báo cáo).
- **Không gắn** các widget xác suất (chưa có chương riêng) và `tree-traversal-animation.js` (trùng 16-02).
- **Không sửa** các file JS đang bẩn / untracked của Linh; `dfa-simulator.js` chỉ được nhúng vào 18-01.

### Giai đoạn 2 — xong (vanilla, rồi nâng cấp Svelte + D3)

Flagship Graph Explainer (BFS, DFS, Dijkstra, Kruskal, Prim), UI tiếng Việt:

- Bản vanilla (vòng trước) vẫn giữ tại `public/js/graph-explainer.js` làm **dự phòng** (chạy không cần build).
- Bản chính viết lại bằng **Svelte + D3**: chuyển động mượt, bố cục lực / kéo đỉnh, zoom, token chạy trên cạnh đang xét, bảng hàng đợi / ngăn xếp / hàng đợi ưu tiên / khoảng cách, giả mã đồng bộ, chỉnh sửa đồ thị và trọng số, chỉnh tốc độ, đồ thị mẫu.
- Nguồn: `explainers/src/graph/`. Bundle: `public/js/explainers/graph-explainer.js`.
- Bài 12-04, 16-03, 17-01 đã chuyển `<script>` sang bundle Svelte.

**Toolchain:** thư mục `explainers/` (Vite library mode, xuất IIFE + CSS gói trong JS). Jekyll `exclude` thư mục nguồn. Hướng dẫn build: `explainers/README.md`.

```bash
cd explainers && npm install && npm run build   # ra public/js/explainers/
cd explainers && npm run dev                    # xem trước tách Jekyll
```

### Giai đoạn 3 — xong (logic / Boole)

Explainer liên kết **bảng chân trị ↔ mạch ↔ bản đồ Karnaugh** (`explainers/src/boolean/`, bundle `boolean-explainer.js`):

- 2–4 biến; nhập biểu thức (∧ ∨ ¬ → ↔ ⊕) hoặc đảo bit trên bảng / K-map.
- **Don't-care (×):** ô chu kỳ 0 → 1 → ×; Quine–McCluskey dùng × làm ô tự do nhưng chỉ phủ ô bắt buộc.
- **SOP và CNF/POS** (khoanh các ô 0), kèm dạng chuẩn Σm / ΠM.
- **Mạch từ AST của biểu thức gốc**, cùng mạch SOP tối tiểu và POS tối tiểu; bấm tín hiệu vào để chạy giá trị qua từng cổng.
- **So sánh hai biểu thức** song song (tương đương hay không, phản ví dụ).
- Nhúng: 01-03, 01-04, 13-03, 13-04.

### Bổ sung — Quine–McCluskey (bài 13-05)

`qm-explainer` (`explainers/src/qm/`, bundle riêng): nhập minterm + don't-care hoặc biểu thức, 2–6 biến; dán cột theo số bit 1 với dấu «-» và ✓, nguyên nhân nguyên tố, bảng phủ với nguyên tố cốt yếu, trội hàng/cột, Petrick, SOP tối tiểu; chạy/lùi/tiến từng bước kèm giải thích tiếng Việt; K-map đối chiếu cho 2–4 biến. Ví dụ mẫu khớp bài (F₁ mục 5b, don't-care mục 4, bốn biến mục 5). Test đối chiếu vét cạn trong `tests/qm.test.js`.

### Giai đoạn 4 — xong (tập hợp, quan hệ, hàm)

- **Venn** (`venn-explainer`): canvas 2–3 tập, biểu thức ∪ ∩ \ Δ ′ ¬, so sánh hai biểu thức, bao hàm–loại trừ, bấm vùng. Bài: 04-01, 04-02, 07-03, 11-03.
- **Quan hệ** (`relation-explainer`): ma trận ↔ đồ thị ↔ tính chất kèm phản ví dụ, bao đóng, Warshall từng bước, lớp tương đương, Hasse. Bài: 05-01…05-04.
- **Hàm** (`function-explainer`): vẽ mũi tên, đơn/toàn/song ánh kèm lý do, hàm ngược, hàm hợp. Bài: 06-01…06-03.

### Giai đoạn 5 — xong (đếm, truy hồi)

- **Đếm** (`counting-explainer`, BigInt): Pascal, liệt kê tổ hợp/hoán vị, sao–vạch, chuồng bồ câu. Bài: 07-02, 07-04, 07-05, 08-01.
- **Truy hồi** (`recurrence-explainer`): công thức đóng (nghiệm phân biệt / kép / phức; nghiệm riêng hằng–tuyến tính–bậc hai), định lý Master, cây gọi fib. Bài: 10-01…10-04.

### Giai đoạn 6 — xong (automata)

`automata-explainer`: mô phỏng DFA / NFA / ε-NFA từng ký tự (tập trạng thái sống), **xây dựng tập con** từng bước (bảng + DFA hiện dần), **tối thiểu hóa DFA**, tự vẽ / sửa máy. Bài: 18-01…18-05, 18-11.

### Giai đoạn 7 — xong (cây, Huffman, số học, hub)

- **Cây** (`tree-explainer`): Huffman từng bước + mã hóa/giải mã, duyệt tiền/trung/hậu/mức, BST chèn/tìm/xóa. Bài: 16-01, 16-02, 16-04.
- **Số học** (`numtheory-explainer`): Euclid mở rộng/Bézout, mặt đồng hồ modulo + bảng, lũy thừa nhanh, sàng, RSA đồ chơi. Bài: 15-01…15-04.
- **`tools.html` thành hub:** 10 thẻ explainer (liên kết tới mọi bài có nhúng) + bảng widget cổ điển; dữ liệu sinh bởi `explainers/gen-tools-data.mjs` vào `_data/tools.yml`.

### Giai đoạn 8 — chưa làm (P2, tùy chọn)

Parse tree / CYK rút gọn và bộ reduction SAT–3SAT–CLIQUE (ngôn ngữ hình thức & phức tạp).

### Kiểm chứng (2026-11-18)

- `cd explainers && npm run build` — 10 bundle.
- `npm test` — 86 test đơn vị đạt (gồm QM, Pascal, topo, logic, language) (Boolean, Venn, quan hệ/hàm, đếm/truy hồi, automata, cây, số học).
- `bundle exec jekyll build` (build ra thư mục tạm) thành công; `node check-pages.mjs` trên 39 bài + `/tools/`: không lỗi console, mọi `data-demo` được mount, bấm mọi nút / đổi mọi select không ném lỗi. Chụp ảnh từng explainer để kiểm tra hiển thị.


### Bổ sung: Tam giác Pascal (07-04)
- `pascal-explainer` (nằm trong `counting-explainer.js`): xây tam giác từ đỉnh xuống, mỗi ô = tổng hai ô cha (hoạt ảnh trượt + cộng), tổng hàng 2ⁿ, đối xứng, cây gậy khúc côn cầu, tô màu mod 2 (Sierpiński).
- Quy tắc: một trang chỉ nạp MỘT bundle Svelte.


### Đợt rà soát toàn bộ bài học (2026-11-19) — đã làm

Rà soát 120+ bài; hầu hết quy trình thuật toán lõi đã có explainer (BFS/DFS/Dijkstra/Kruskal/Prim, Euclid/lũy thừa nhanh/RSA, Warshall, Hasse, K-map, QM, automata, Huffman, truy hồi). Đợt này thêm 8 explainer vào các bài chỉ có chữ/bảng:

| Explainer | Bài | Bundle |
|:---|:---|:---|
| `topo-explainer` (Kahn + DFS, chu trình) | 17-02 | `graph-explainer.js` |
| `induction-explainer` (domino, thiếu cơ sở, n²+n+41) | 03-03 | `logic-explainer.js` (mới) |
| `dpll-explainer` | 01-06 | `logic-explainer.js` |
| `bits-explainer` (bù hai, cộng/tràn, endianness, Y2038) | 09-03, 09-02 | `logic-explainer.js` |
| `cyk-explainer` | 19-11 | `language-explainer.js` (mới) |
| `derive-explainer` (cây phân tích, nhập nhằng) | 19-07 | `language-explainer.js` |
| `pda-explainer` | 19-08 | `language-explainer.js` |
| `tm-explainer` | 18-12 | `language-explainer.js` |

Ngoài ra 16-03 có thêm một explainer Prim riêng. Thanh điều khiển dùng chung: `src/shared/Stepper.svelte`.

### Còn lại, theo thứ tự ưu tiên

1. 04-03 Cantor đường chéo / khách sạn Hilbert (hoạt ảnh).
2. 20-08 SAT → 3SAT (chuyển từng mệnh đề), 20-09 IS ↔ CLIQUE ↔ VC (bù đồ thị), 20-11 xấp xỉ vertex cover.
3. 18-07/18-08 Regex → NFA (Thompson) và loại trạng thái (Kleene); 18-06 Mealy/Moore; 18-09, 19-10 trò chơi bổ đề bơm; 19-09 CFG → PDA.
4. 17-03 ghép cặp (đường tăng) và tô màu tham lam theo thứ tự.
5. 13-07 mạch cộng nhớ lan (ripple-carry) từng bit.
6. 09-07/09-08 mô phỏng nghịch lý ngày sinh và va chạm băm; 09-05 hàng đợi.
7. 15-xx định lý số dư Trung Hoa, Miller–Rabin, Diffie–Hellman.
8. 01-05/02-03 kiểm tra suy diễn từng dòng; 03-02 phản chứng; 07-01 cây quyết định cho quy tắc nhân/cộng; 14-01 sắp xếp/tìm kiếm.

### Kiểm chứng đợt này

- `npm run build` — 13 bundle; `npm test` — 86/86; `node gen-tools-data.mjs` — 20 explainer; Jekyll build ra thư mục tạm; `check-pages.mjs` trên 49 trang + `/tools/`: 0 lỗi console.
- Kịch bản Chrome riêng (`play`, bước, đổi preset, màn hình 390px): không tràn ngang, 0 lỗi.


### Đợt rà soát tiếp theo (2026-11-19) — đã làm hết danh sách "còn lại" 1–8 (trừ 03-02)

| Explainer | Bài | Bundle |
|:---|:---|:---|
| `infinity-explainer` (đường chéo Cantor, khách sạn Hilbert, ghép cặp ℕ×ℕ) | 04-03 | `logic-explainer.js` |
| `reduction-explainer` (SAT→3SAT, IS/CLIQUE/VC, xấp xỉ VC) | 20-08, 20-09, 20-11 | `complexity-explainer.js` (mới) |
| `regex-explainer` (Thompson, loại trạng thái) | 18-07, 18-08 | `language-explainer.js` |
| `mealy-explainer` | 18-06 | `language-explainer.js` |
| `pumping-explainer` (chính quy / CFL) | 18-09, 19-10 | `language-explainer.js` |
| `cfgpda-explainer` | 19-09 | `language-explainer.js` |
| `match-explainer` (ghép cặp Kuhn, tô màu tham lam) | 17-03 | `graph-explainer.js` |
| `adder-explainer` (ripple-carry, cộng/trừ, tràn) | 13-07 | `logic-explainer.js` |
| `sim-explainer` (sinh nhật, băm, hàng đợi/Little) | 09-07, 09-08, 09-05 | `logic-explainer.js` |
| `crypto-explainer` (CRT, Miller–Rabin, Diffie–Hellman) | 15-02, 15-03 | `numtheory-explainer.js` |
| `inference-explainer` (kiểm tra suy diễn bằng bảng chân trị) | 01-05 | `logic-explainer.js` |
| `rule-explainer` (cây cộng/nhân + bao hàm–loại trừ) | 07-01 | `counting-explainer.js` |
| `sort-explainer` (sắp xếp, tìm kiếm, đếm so sánh) | 14-01 | `recurrence-explainer.js` |

Bài học chỉ được chèn thêm khối (sao lưu ở `/tmp/dx-backups-t84/`), không sửa nội dung.

### Còn lại

1. 03-02 phản chứng √2 (stepper); 02-03 suy diễn vị từ từng dòng.
2. Các bài lý thuyết thuần (chứng minh) không có thuật toán để minh họa.

### Kiểm chứng đợt này

- `npm run build` — 14 bundle; `npm test` — 113/113; `node gen-tools-data.mjs` — 33 explainer; Jekyll build ra thư mục tạm; `check-pages.mjs` trên 67 trang + `/tools/`: 0 lỗi console; kịch bản Chrome riêng duyệt mọi tab/select/stepper và màn hình 390px: không tràn ngang, 0 lỗi.

### Hai ứng viên cuối (2026-11-19) — đã làm

| Explainer | Bài | Bundle |
|:---|:---|:---|
| `contradiction-explainer` (√2 vô tỷ, vô hạn số nguyên tố) | 03-02 | `logic-explainer.js` |
| `predproof-explainer` (UI/EI/EG/UG, hai lỗi kinh điển, phản ví dụ trên mô hình ≤ 3 phần tử) | 02-03 | `logic-explainer.js` |

Danh sách ứng viên đã hết. Kiểm chứng: 14 bundle, `npm test` 116/116, `gen-tools-data` 35 explainer, `check-pages` 69 trang + `/tools/` 0 lỗi console.
