# Explainer tương tác (Svelte + D3 + Vite)

Thư mục này chứa **mã nguồn** các explainer nhúng vào giáo trình Jekyll. Bước build tạo file tĩnh
(IIFE, CSS đã gói trong JS) tại `../public/js/explainers/<tên>.js`. Bài học nhúng bundle bằng thẻ `<script>`
và `data-demo`, giống widget cũ. Jekyll **không** xử lý thư mục `explainers/` (đã `exclude` trong `_config.yml`).

## ⚠️ Chạy trang web: build ở `explainers/`, phục vụ từ **gốc repo**

```bash
# 1) Build explainer (trong explainers/)
cd explainers
npm install          # một lần, hoặc khi package.json đổi
npm run build

# 2) QUAY RA GỐC REPO rồi mới chạy Jekyll
cd ..
bundle exec jekyll serve
```

Mở **có baseurl**: <http://127.0.0.1:4000/discrete-mathematics-for-computer-science-iuh/> (baseurl lấy từ `_config.yml`).
Ví dụ bài có explainer:
`http://127.0.0.1:4000/discrete-mathematics-for-computer-science-iuh/contents/chapter18/18_05_Subset_Construction_Proof/`
và hub công cụ: `http://127.0.0.1:4000/discrete-mathematics-for-computer-science-iuh/tools/`.

> **Không** chạy `jekyll serve` từ bên trong `explainers/` — thư mục đó bị loại khỏi site và không có `_config.yml`,
> kết quả là trang **404**. Luôn `cd ..` về gốc repo trước khi chạy Jekyll. Cũng đừng chạy `npm` ở gốc repo; luôn `cd explainers`.
> Mỗi khi sửa file trong `src/`, chạy lại `npm run build` (Jekyll `serve` tự nạp lại file tĩnh trong `public/`).

Muốn thử mà không đụng `_site` đang dùng, build ra thư mục khác:

```bash
bundle exec jekyll build -d /tmp/dx-site/discrete-mathematics-for-computer-science-iuh
cd /tmp/dx-site && python3 -m http.server 4011
# → http://127.0.0.1:4011/discrete-mathematics-for-computer-science-iuh/
```

## Lệnh

| Lệnh (trong `explainers/`) | Việc |
| --- | --- |
| `npm run build` | Build mọi bundle (xóa và tạo lại `public/js/explainers/`) |
| `npm run build -- tree-explainer` | Chỉ build một bundle (không xóa các bundle khác) |
| `npm test` | Test đơn vị cho thuật toán thuần (`tests/*.test.js`, Node ≥ 18) |
| `npm run dev` | Xem trước tách khỏi Jekyll (Vite, http://127.0.0.1:5173/) |
| `node check-pages.mjs <base-url> <đường-dẫn>...` | Kiểm tra bằng Chrome headless: mount, bấm mọi nút, đổi mọi select, báo lỗi console |
| `node gen-tools-data.mjs` | Sinh lại `../_data/tools.yml` cho trang hub `tools.html` (chạy sau khi thêm/bớt embed) |

Ví dụ kiểm tra (đặt `CHROME` nếu Chrome không ở đường dẫn macOS mặc định, `PORT` để đổi cổng CDP):

```bash
node check-pages.mjs http://127.0.0.1:4011/discrete-mathematics-for-computer-science-iuh \
  /contents/chapter18/18_05_Subset_Construction_Proof/ /tools/
```

## Nhúng vào bài học

```html
<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa3" data-tab="subset"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>
```

| `data-demo` | Thuộc tính tùy chọn |
| --- | --- |
| `graph-explainer` | `data-algorithm`: `bfs` `dfs` `dijkstra` `kruskal` `prim` |
| `boolean-explainer` | `data-vars` (2–4), `data-expr`, `data-expr-b`, `data-dc` (don't-care, ví dụ `1,5`), `data-mode` (`single`\|`compare`), `data-form` (`sop`\|`pos`), `data-circuit` (`ast`\|`sop`\|`pos`), `data-focus` (`table`\|`circuit`\|`kmap`) |
| `qm-explainer` | `data-preset` (`f1` `dc3` `four` `cyclic` `five` `six`), `data-vars` (2–6), `data-minterms` (`5,6,9-11`), `data-dc`, `data-expr`, `data-names` (`w,x,y,z`), `data-start` (số bước hoặc `end`) |
| `venn-explainer` | `data-sets` (2\|3), `data-expr`, `data-expr-b`, `data-focus` (`shade`\|`compare`\|`ie`) |
| `relation-explainer` | `data-preset` (`mod2` `leq` `div` `lt` `sym` `next` `empty`), `data-focus` (`props` `warshall` `classes` `hasse`) |
| `function-explainer` | `data-preset` (`inj` `surj` `bij` `sq` `inc` `bad`), `data-focus` (`props` `inverse` `compose`) |
| `pascal-explainer` (nằm trong bundle `counting-explainer.js`) | `data-tab` (`build` `rowsum` `sym` `hockey`), `data-rows` (0–14), `data-mode` (`value` `binom`), `data-color` (`none` `mod2`), `data-k`, `data-n`, `data-autoplay` (`1`) |
| `counting-explainer` | `data-tab` (`pascal` `choose` `stars` `pigeon`), `data-n`, `data-k` |
| `recurrence-explainer` | `data-mode` (`linear` `dc` `fib`), `data-preset` (`fib` `hanoi` `two` `double` `complex` `nonhom`) |
| `automata-explainer` | `data-preset` (`dfa01` `even1` `nfa101` `nfa3` `enfa` `empty`), `data-tab` (`simulate` `subset` `minimize`), `data-input` |
| `tree-explainer` | `data-mode` (`huffman` `traversal` `bst`), `data-freqs` (`a:5 b:9`), `data-keys` (`8 3 10`), `data-msg` |
| `numtheory-explainer` | `data-tab` (`euclid` `modular` `fastexp` `sieve` `rsa`), `data-a`, `data-b` |
| `topo-explainer` (trong bundle `graph-explainer.js`) | `data-preset` (`courses` `diamond` `build`), `data-algo` (`kahn` `dfs`), `data-cycle` (`true` `false`) |
| `induction-explainer` (bundle `logic-explainer.js`) | `data-preset` (`sum` `pow2` `div3` `nobase` `prime`) |
| `dpll-explainer` (bundle `logic-explainer.js`) | `data-preset` (`sat` `unit` `unsat` `php`), `data-cnf` (CNF tùy ý) |
| `bits-explainer` (bundle `logic-explainer.js`) | `data-tab` (`twos` `add` `endian` `y2038`), `data-bits` (4/8), `data-value`, `data-a`, `data-b` |
| `cyk-explainer` (bundle `language-explainer.js`) | `data-preset` (`classic` `anbn` `reject`), `data-input`, `data-grammar` |
| `derive-explainer` (bundle `language-explainer.js`) | `data-preset` (`expr-amb` `expr-unamb` `else` `paren`), `data-input`, `data-grammar` |
| `pda-explainer` (bundle `language-explainer.js`) | `data-preset` (`anbn` `ww` `paren`), `data-input` |
| `tm-explainer` (bundle `language-explainer.js`) | `data-preset` (`inc` `anbn` `unary`), `data-input` |
| `infinity-explainer` (bundle `logic-explainer.js`) | `data-tab` (`diagonal` `hilbert` `pairing`), `data-scenario` (`one` `bus` `buses`) |
| `inference-explainer` (bundle `logic-explainer.js`) | `data-preset` (`mp` `mt` `hs` `ds` `res` `aff` `den`), `data-premises`, `data-conclusion` |
| `adder-explainer` (bundle `logic-explainer.js`) | `data-a`, `data-b` (0–15), `data-sub` (`true` `false`) |
| `sim-explainer` (bundle `logic-explainer.js`) | `data-tab` (`birthday` `hash` `queue`), `data-days`, `data-buckets`, `data-keys`, `data-lambda`, `data-service` (ms), `data-servers` |
| `match-explainer` (bundle `graph-explainer.js`) | `data-tab` (`matching` `coloring`), `data-preset`, `data-order` |
| `reduction-explainer` (bundle `complexity-explainer.js`) | `data-tab` (`3sat` `clique` `approx`), `data-cnf`, `data-graph` (`house` `cycle` `star` `matching`) |
| `regex-explainer` (bundle `language-explainer.js`) | `data-tab` (`thompson` `eliminate`), `data-regex`, `data-preset` (`dfa01` `even1` `nfa101`), `data-order` (`forward` `reverse`) |
| `mealy-explainer` (bundle `language-explainer.js`) | `data-preset` (`m11` `add` `mod3`), `data-input` |
| `pumping-explainer` (bundle `language-explainer.js`) | `data-kind` (`regular` `cfl`), `data-lang` (`anbn` `pal` `abstar` | `anbncn` `anbn` `ww`), `data-p` |
| `cfgpda-explainer` (bundle `language-explainer.js`) | `data-preset`, `data-input`, `data-grammar` |
| `crypto-explainer` (bundle `numtheory-explainer.js`) | `data-tab` (`crt` `miller` `dh`), `data-n`, `data-a` |
| `rule-explainer` (bundle `counting-explainer.js`) | `data-preset` (`outfit` `meal` `plate` `pw`) |
| `sort-explainer` (bundle `recurrence-explainer.js`) | `data-tab` (`sort` `search`), `data-algo` (`bubble` `insertion` `selection`), `data-data` |
| `contradiction-explainer` (bundle `logic-explainer.js`) | `data-tab` (`sqrt2` `primes`), `data-a`, `data-b`, `data-primes` |
| `predproof-explainer` (bundle `logic-explainer.js`) | `data-preset` (`socrates` `exists` `ei-twice` `ug-bad`) |

> **Một trang chỉ nên nạp MỘT bundle Svelte.** Hai bundle khác nhau trên cùng một trang mỗi bên mang một bản runtime Svelte và tranh nhau xử lý sự kiện click dùng chung, dẫn đến lỗi ngẫu nhiên (`Cannot add the same private member more than once`). Muốn hai explainer chung trang thì cho chúng cùng một bundle (ví dụ Pascal mount từ `counting-explainer.js`); nhúng cùng một bundle hai lần trên trang chỉ cần một thẻ `<script>`.

## Cấu trúc

- `src/<tên>/` — mỗi explainer: logic thuần (`*.js`, có test), thành phần Svelte, `main.js` (gắn vào `data-demo`)
  - `graph`, `boolean`, `qm`, `pascal` (mount qua bundle counting), `venn`, `relation`, `function`, `counting`, `recurrence`, `automata`, `tree`, `numtheory`, `logic` (induction · dpll · bits · infinity · adder · sim · inference), `complexity` (reduction), `language` (cyk · derive · pda · tm); `graph` có thêm `topo`
- `src/shared/` — `ui.css` (kiểu `.dx`) và `mount.js`
- `entries.mjs` — danh sách bundle; `build.mjs`, `vite.config.js` — cấu hình build
- `tests/` — test đơn vị cho các module thuần (không import Svelte)
- `public/js/graph-explainer.js` (ở gốc repo) — bản vanilla cũ, **giữ làm dự phòng**

## Lưu ý

- `node_modules/` không đưa lên Git; bundle trong `public/js/explainers/` *nên* được commit cùng bài học để GitHub Pages chạy không cần Node.
- Thêm explainer mới: tạo `src/<tên>/main.js`, thêm vào `entries.mjs`, `npm run build -- <tên>`, nhúng vào bài, rồi `node gen-tools-data.mjs`.
