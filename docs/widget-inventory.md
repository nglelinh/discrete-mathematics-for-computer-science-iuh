# Kiểm kê widget tương tác (Giai đoạn 0)

Cập nhật: 2026-11-18. Repo `discrete-mathematics-for-computer-science-iuh`, nhánh đang checkout: `feature/interactive-explainer-plan`.

Quy ước nhúng phổ biến trong bài học:

```html
<div class="interactive-demo" markdown="1">
<div data-demo="ten-widget"></div>
</div>
<script src="{{ '/public/js/ten-widget.js' | relative_url }}"></script>
```

Một số file cũ mount bằng `data-tool` hoặc `id` thay vì `data-demo` (đã được bổ sung tương thích `data-demo` ở Giai đoạn 1, trừ các file JS có thay đổi chưa commit của Linh).

Không có thư mục `contents/en` / `contents/vi` tách riêng: bài học nằm ở `contents/chapterXX/_posts/`, nội dung tiếng Việt (một số front matter ghi `lang: en`).

## File hạ tầng (không phải widget bài học)

| File | Vai trò |
|------|---------|
| `script.js` | Script chung site |
| `textbook.js` | Hành vi giáo trình (được nạp ở layout) |
| `multilang.js` | Chuyển ngữ (đa ngữ đang tắt trong `_config.yml`) |
| `exercise-system.js` | Hệ thống bài tập, nạp ở layout |

## Widget đã gắn vào bài (trước Giai đoạn 1)

| File | `data-demo` (hoặc tương đương) | Bài đã gắn |
|------|--------------------------------|------------|
| `algorithm-complexity-analyzer.js` | `algorithm-complexity-analyzer` | 14-03 |
| `algorithm-visualization.js` | `algorithm-visualization` | 14-01 |
| `bfs-dfs-visualizer.js` | `bfs-dfs-visualizer` | 12-04. **File đang có thay đổi local chưa commit của Linh — không ghi đè.** |
| `big-o-growth-comparator.js` | `big-o-growth-comparator` | 14-02 |
| `binomial-coefficient-calc.js` | `binomial-coefficient-calc` | 07-04 |
| `boolean-algebra-checker.js` | `boolean-algebra-checker` | 13-01 |
| `boolean-expression-evaluator.js` | `boolean-expression-evaluator` | 13-02 |
| `characteristic-solver.js` | `characteristic-solver` | 10-03 |
| `dijkstra-visualizer.js` | `dijkstra-visualizer` | 17-01 |
| `euclidean-algorithm.js` | `euclidean-algorithm` | 15-01 |
| `euler-hamilton-checker.js` | `euler-hamilton-checker` | 12-04; 09-12 có `data-demo` nhưng **thiếu thẻ script** (sửa ở Giai đoạn 1). **File JS đang có thay đổi local chưa commit — không ghi đè.** |
| `gf-recurrence-solver.js` | `gf-recurrence-solver` | 11-02 |
| `graph-adjacency-builder.js` | `graph-adjacency-builder` | 12-01, 12-02, 12-03 |
| `graph-coloring-interactive.js` | `graph-coloring-interactive` | 17-03 |
| `huffman-coding.js` | `huffman-coding` | 16-04 |
| `inclusion-exclusion-toggle.js` | `inclusion-exclusion-toggle` | 07-03 |
| `kruskal-algorithm.js` | `kruskal-algorithm` | 16-03 |
| `linear-recurrence-solver.js` | `linear-recurrence-solver` | 10-02 |
| `modular-arithmetic-calc.js` | `modular-arithmetic-calc` | 15-02 |
| `modular-calculator.js` | `modular-calculator` | 15-01 |
| `number-theory-apps.js` | `number-theory-apps` | 15-04 |
| `quine-mccluskey-simplifier.js` | `quine-mccluskey-simplifier` | 13-05 |
| `recurrence-visualizer.js` | `recurrence-visualizer` | 10-01 |
| `relation-property-checker.js` | `data-tool="relation-practice-checker"` | 05-05 |
| `rsa-simulator.js` | `rsa-simulator` | 15-03 |
| `stars-bars-visualizer.js` | `stars-bars-visualizer` | 07-05 |
| `surjection-counter.js` | `surjection-counter` | 11-04 |
| `tree-traversal-visualizer.js` | `tree-traversal-visualizer` | 16-02 |
| `venn-ie-three-sets.js` | `venn-ie-three-sets` | 11-03 |

## Gắn dở (có `data-demo` trong bài nhưng thiếu `<script>`) — sửa ở Giai đoạn 1

| File | Bài | Ghi chú |
|------|-----|---------|
| `nested-quantifier-grid.js` | 02-04 | Có `data-demo="nested-quantifier-grid"`, thiếu script |
| `logic-operator-widgets.js` | 09-00 | Bài dùng `data-demo="logic-operator-widgets"` nhưng widget vốn chỉ nhận `proposition-checker` / `logic-evaluator` |
| `logic-gates-builder.js` | 09-04 | Có `data-demo`, thiếu script |
| `euler-hamilton-checker.js` | 09-12 | Có `data-demo`, thiếu script |

## Widget có file nhưng chưa gắn bài (trước Giai đoạn 1)

| File | Selector dự kiến | Bài nên gắn (P0/P1) |
|------|------------------|---------------------|
| `truth-table-normal-form.js` | `data-tool` / `data-demo="truth-table-normal-form"` | 01-03, 01-04 |
| `set-operations-visualizer.js` | `id="set-operations-visualizer"` (và `data-demo`) | 04-02 |
| `venn-counter.js` | `data-tool` / `data-demo="venn-counter"` | 04-02 |
| `relation-matrix-toggle.js` | `data-demo="relation-matrix-toggle"` | 05-01 |
| `relation-properties-checker.js` | `data-demo="relation-classifier"` | 05-02 |
| `hasse-diagram.js` | `data-demo="hasse-diagram"` | 05-03 |
| `warshall-visualizer.js` | `data-demo="relation-closure-warshall"` | 05-04 |
| `function-arrow-checker.js` | `data-demo="function-arrow-checker"` | 06-02 |
| `function-property-checker.js` | `data-tool` / `data-demo="function-property-checker"` | 06-02 |
| `function-composition-pipeline.js` | `data-demo="function-composition-pipeline"` | 06-03 |
| `pigeonhole-visualizer.js` | `data-demo="pigeonhole-visualizer"` | 08-01 |
| `generating-function-explorer.js` | `data-demo="generating-function-explorer"` | 11-01 |
| `graph-isomorphism-checker.js` | `data-demo="graph-isomorphism-checker"` | 12-01 |
| `kmap-interactive.js` | `data-demo="kmap-interactive"` | 13-04 |
| `logic-gates-builder.js` | `data-demo="logic-gates-builder"` | 13-03 (và sửa script ở 09-04) |
| `direct-proof-builder.js` | `data-demo="direct-proof-builder"` | 03-01 |
| `induction-step-checker.js` | `data-demo="induction-checker"` | 03-03 |
| `predicate-proof-dnd.js` | `id="predicate-proof-demo"` / `data-demo="predicate-proof-dnd"` | 02-03 |
| `dfa-simulator.js` | `data-demo="dfa-simulator"` | 18-01. **File untracked của Linh — chỉ nhúng, không sửa file JS.** |
| `summation-loop-visualizer.js` | `data-demo="summation-loop-visualizer"` | 14-03 |
| `nested-quantifier-grid.js` | `data-demo="nested-quantifier-grid"` | 02-02 (và sửa script ở 02-04) |
| `logic-operator-widgets.js` | `proposition-checker`, `logic-evaluator`, hoặc wrapper `logic-operator-widgets` | 01-02 (và sửa 09-00) |

## Để giai đoạn sau (không gắn trong P0–P2)

| File | Lý do |
|------|--------|
| `bayes-calculator.js` | Không có chương xác suất riêng; dễ gắn nhầm |
| `binomial-distribution.js` | Như trên |
| `conditional-probability-viz.js` | Như trên |
| `dice-probability-simulator.js` | Gần 09-07 (birthday) nhưng không cùng mô hình toán; để P1/P2 khi có bài xác suất |
| `tree-traversal-animation.js` | Trùng chức năng với `tree-traversal-visualizer.js` đã gắn ở 16-02 |

## Flagship Giai đoạn 2

File mới `public/js/graph-explainer.js`, mount `data-demo="graph-explainer"`, tùy chọn `data-algorithm="bfs|dfs|dijkstra|kruskal|prim"`.

Vanilla JS + SVG, không thêm pipeline Svelte/D3 (tránh phụ thuộc build mới trên GitHub Pages). Không ghi đè `bfs-dfs-visualizer.js` / `dijkstra-visualizer.js` / `kruskal-algorithm.js`; nhúng thêm cạnh widget cũ.

## Ghi chú chất lượng

- Nhiều widget P0 cũ là IIFE ngắn (3–6 KB, CSS nội tuyến), đủ dùng như máy tính/minh họa, chưa phải explainer từng bước.
- `bfs-dfs-visualizer.js` (~12 KB, có bước tới/lui) là widget thuật toán đầy đủ nhất trước Giai đoạn 2.
- Lỗi thường gặp: bài đã đặt `data-demo` nhưng quên `<script src>`.


## Explainer Svelte + D3 (bổ sung sau inventory ban đầu)

Cập nhật: 2026-11-18 (Asia/Saigon). Nguồn trong `explainers/`, bundle tại `public/js/explainers/`.

| Bundle | `data-demo` | Bài đã nhúng |
| --- | --- | --- |
| `explainers/graph-explainer.js` | `graph-explainer` (`data-algorithm`) | 12-04, 16-03, 17-01 (thay script vanilla; file `public/js/graph-explainer.js` giữ làm dự phòng) |
| `explainers/boolean-explainer.js` | `boolean-explainer` (`data-vars`, `data-focus`, `data-expr`) | 01-03, 01-04, 13-03, 13-04 (thêm, không thay widget cũ) |
| `explainers/venn-explainer.js` | `venn-explainer` (`data-sets`, `data-expr`, `data-expr-b`, `data-focus`) | 04-01, 04-02, 07-03, 11-03 (thêm) |
| `explainers/relation-explainer.js` | `relation-explainer` (`data-preset`, `data-focus`) | 05-01, 05-02, 05-03, 05-04 (thêm) |
| `explainers/function-explainer.js` | `function-explainer` (`data-preset`, `data-focus`) | 06-01, 06-02, 06-03 (thêm) |
| `explainers/counting-explainer.js` | `counting-explainer` (`data-tab`, `data-n`, `data-k`) | 07-02, 07-04, 07-05, 08-01 (thêm) |
| `explainers/recurrence-explainer.js` | `recurrence-explainer` (`data-mode`, `data-preset`) | 10-01, 10-02, 10-03, 10-04 (thêm) |
| `explainers/automata-explainer.js` | `automata-explainer` (`data-preset`, `data-tab`, `data-input`) | 18-01, 18-02, 18-03, 18-04, 18-05, 18-11 (thêm) |
| `explainers/tree-explainer.js` | `tree-explainer` (`data-mode`, `data-freqs`, `data-keys`, `data-msg`) | 16-01, 16-02, 16-04 (thêm) |
| `explainers/numtheory-explainer.js` | `numtheory-explainer` (`data-tab`, `data-a`, `data-b`) | 15-01, 15-02, 15-03, 15-04 (thêm) |
| `explainers/qm-explainer.js` | `qm-explainer` (`data-preset`, `data-vars`, `data-minterms`, `data-dc`, `data-expr`, `data-names`, `data-start`) | 13-05 (thêm; widget `quine-mccluskey-simplifier` giữ nguyên) |
| `explainers/counting-explainer.js` | `pascal-explainer` (`data-tab`, `data-rows`, `data-mode`, `data-color`, `data-k`, `data-n`, `data-autoplay`) | 07-04 (thêm; widget `binomial-coefficient-calc` và explainer đếm giữ nguyên; Pascal nằm chung bundle đếm để tránh hai runtime Svelte trên một trang) |
| `explainers/graph-explainer.js` | `topo-explainer` (`data-preset`, `data-algo`, `data-cycle`) | 17-02 (mới; Kahn + DFS, phát hiện chu trình); 16-03 thêm một `graph-explainer data-algorithm="prim"` |
| `explainers/logic-explainer.js` | `induction-explainer` (`data-preset`) | 03-03 (mới; domino, thiếu cơ sở, n²+n+41; widget `induction-checker` giữ nguyên) |
| `explainers/logic-explainer.js` | `dpll-explainer` (`data-preset`, `data-cnf`) | 01-06 (mới; DPLL từng bước) |
| `explainers/logic-explainer.js` | `bits-explainer` (`data-tab`, `data-bits`, `data-value`, `data-a`, `data-b`) | 09-03 (bù hai · cộng có nhớ · Y2038), 09-02 (endianness) |
| `explainers/language-explainer.js` | `cyk-explainer` (`data-preset`, `data-input`, `data-grammar`) | 19-11 (mới) |
| `explainers/language-explainer.js` | `derive-explainer` (`data-preset`, `data-input`, `data-grammar`) | 19-07 (mới; dẫn xuất trái nhất, nhập nhằng) |
| `explainers/language-explainer.js` | `pda-explainer` (`data-preset`, `data-input`) | 19-08 (mới) |
| `explainers/language-explainer.js` | `tm-explainer` (`data-preset`, `data-input`) | 18-12 (mới) |
| `explainers/logic-explainer.js` | `infinity-explainer` | 04-03 (mới) |
| `explainers/logic-explainer.js` | `inference-explainer` | 01-05 (mới) |
| `explainers/logic-explainer.js` | `adder-explainer` | 13-07 (mới) |
| `explainers/logic-explainer.js` | `sim-explainer` | 09-07 · 09-08 · 09-05 (mới) |
| `explainers/graph-explainer.js` | `match-explainer` | 17-03 (2 lần) (mới) |
| `explainers/complexity-explainer.js` | `reduction-explainer` | 20-08 · 20-09 · 20-11 (mới) |
| `explainers/language-explainer.js` | `regex-explainer` | 18-07 · 18-08 (mới) |
| `explainers/language-explainer.js` | `mealy-explainer` | 18-06 (mới) |
| `explainers/language-explainer.js` | `pumping-explainer` | 18-09 · 19-10 (mới) |
| `explainers/language-explainer.js` | `cfgpda-explainer` | 19-09 (mới) |
| `explainers/numtheory-explainer.js` | `crypto-explainer` | 15-02 · 15-03 (mới) |
| `explainers/counting-explainer.js` | `rule-explainer` | 07-01 (mới) |
| `explainers/recurrence-explainer.js` | `sort-explainer` | 14-01 (mới) |
| `explainers/logic-explainer.js` | `contradiction-explainer` (`data-tab`, `data-a`, `data-b`, `data-primes`) | 03-02 (mới) |
| `explainers/logic-explainer.js` | `predproof-explainer` (`data-preset`) | 02-03 (mới; vẫn giữ widget `predicate-proof-dnd`) |

`boolean-explainer` giờ còn nhận `data-expr-b`, `data-dc`, `data-mode`, `data-form`, `data-circuit`. Widget cũ ở mọi bài trên **vẫn được giữ**. Danh sách đầy đủ theo bài nằm ở trang `/tools/` (sinh từ `_data/tools.yml`).
