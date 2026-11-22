<script>
  import TreeSvg from './TreeSvg.svelte';
  import {
    parseFreqs, huffman, encode, decode, layoutForest, HUFFMAN_PRESETS,
    buildBST, insert, search, remove, parseKeys, ORDERS, height, size
  } from './tree.js';

  let { mode = 'huffman', freqs = '', keys = '', msg = '' } = $props();

  let tab = $state(['huffman', 'traversal', 'bst'].includes(mode) ? mode : 'huffman');

  // ---- Huffman
  let ftext = $state(freqs || HUFFMAN_PRESETS[0].text);
  let message = $state(msg || HUFFMAN_PRESETS[0].msg);
  let hstep = $state(0);
  const fr = $derived(parseFreqs(ftext));
  const H = $derived(huffman(fr));
  const hs = $derived(Math.min(hstep, H.steps.length));
  const forest = $derived(hs === 0 ? H.initial : H.steps[hs - 1].forest);
  const hLayout = $derived(layoutForest(forest, { dx: 44, dy: 58, gap: 22 }));
  const lastStep = $derived(hs > 0 ? H.steps[hs - 1] : null);
  const hHot = $derived(lastStep ? [lastStep.a.id, lastStep.b.id, lastStep.parent.id] : []);
  const finished = $derived(H.steps.length > 0 && hs === H.steps.length);
  const bitsOut = $derived(encode(H.codes, message));
  const roundTrip = $derived(bitsOut !== null ? decode(H.root, bitsOut) : null);
  const hLabel = (n) => (n.sym !== null ? `${n.sym}` : `${n.freq}`);

  // ---- BST / duyệt
  let ktext = $state(keys || '8 3 10 1 6 14 4 7 13');
  let root = $state(buildBST(parseKeys(keys || '8 3 10 1 6 14 4 7 13')));
  let order = $state('in');
  let tstep = $state(0);
  let opVal = $state('5');
  let opMsg = $state('Chèn, tìm hoặc xóa một khóa. Đường đi so sánh sẽ được tô màu.');
  let hotPath = $state([]);
  let newId = $state(null);
  const bLayout = $derived(layoutForest(root ? [root] : [], { dx: 44, dy: 58, gap: 10 }));
  const seq = $derived(ORDERS[order].fn(root));
  const visited = $derived(seq.slice(0, tstep).map((n) => n.id));
  const curNode = $derived(tstep > 0 ? [seq[tstep - 1].id] : []);

  function rebuild() { root = buildBST(parseKeys(ktext)); tstep = 0; hotPath = []; newId = null; }
  function doInsert() {
    const k = Number(opVal); if (!Number.isFinite(k)) return;
    const r = insert(root, k); root = r.root; hotPath = r.path; newId = null;
    if (r.added) {
      const n = (function find(x) { return x.key === k ? x : find(k < x.key ? x.left : x.right); })(root);
      hotPath = [...r.path, n.id]; newId = n.id;
      opMsg = `Chèn ${k}: so sánh dọc đường đi rồi gắn thành con ${r.side === 'left' ? 'trái' : 'phải'} của ${r.path.length ? '' : '(gốc mới)'}${r.path.length ? r.path.length + ' nút trên đường' : ''}.`;
    } else opMsg = `${k} đã có trong cây — BST không chứa khóa trùng.`;
    tstep = 0;
  }
  function doSearch() {
    const k = Number(opVal); if (!Number.isFinite(k)) return;
    const r = search(root, k); hotPath = r.path; newId = null;
    opMsg = r.found ? `Tìm thấy ${k} sau ${r.path.length} phép so sánh (≤ chiều cao ${height(root)}).` : `Không có ${k}: đi hết ${r.path.length} nút rồi gặp nhánh rỗng.`;
  }
  function doDelete() {
    const k = Number(opVal); if (!Number.isFinite(k)) return;
    const p = search(root, k);
    const r = remove(root, k); root = r.root; hotPath = []; newId = null; tstep = 0;
    opMsg = !p.found ? `Không có ${k} để xóa.`
      : r.kind === 'leaf' ? `Xóa ${k}: là lá nên gỡ thẳng.`
      : r.kind === 'one' ? `Xóa ${k}: có một con nên nối con đó lên thay.`
      : `Xóa ${k}: có hai con nên thay bằng khóa nhỏ nhất của cây con phải (kế thừa trung thứ tự), rồi xóa nút đó.`;
  }
  $effect(() => { if (tstep > seq.length) tstep = seq.length; });
  const treeStats = $derived(`${size(root)} nút · chiều cao ${height(root)}`);
</script>

<div class="dx tex">
  <h4>Minh hoạ cây: Huffman, duyệt cây, BST</h4>
  <div class="dx-tabs">
    <button type="button" class="sec" class:on={tab === 'huffman'} onclick={() => (tab = 'huffman')}>Mã Huffman</button>
    <button type="button" class="sec" class:on={tab === 'traversal'} onclick={() => (tab = 'traversal')}>Duyệt cây</button>
    <button type="button" class="sec" class:on={tab === 'bst'} onclick={() => (tab = 'bst')}>Cây tìm kiếm nhị phân</button>
  </div>

  {#if tab === 'huffman'}
    <p class="dx-help">Mỗi bước: lấy hai cây có <b>trọng số nhỏ nhất</b> và gộp thành cây mới (trái = bit 0, phải = bit 1). Lặp đến khi còn một cây — các mã thu được là <b>tiền tố tự do</b> và tối ưu.</p>
    <div class="dx-bar">
      <label>Tần suất (<code>ký_tự:số</code>)<input type="text" bind:value={ftext} oninput={() => (hstep = 0)} style="width:15rem" /></label>
      <label>Mẫu
        <select onchange={(e) => { const p = HUFFMAN_PRESETS[+e.currentTarget.value]; ftext = p.text; message = p.msg; hstep = 0; }}>
          {#each HUFFMAN_PRESETS as p, i}<option value={i}>{p.label}</option>{/each}
        </select>
      </label>
    </div>
    {#if H.root}
      <div class="dx-bar">
        <button type="button" class="sec" disabled={hs <= 0} onclick={() => (hstep = hs - 1)}>◀ Lùi</button>
        <span>Bước {hs} / {H.steps.length}</span>
        <button type="button" disabled={hs >= H.steps.length} onclick={() => (hstep = hs + 1)}>Gộp tiếp ▶</button>
        <button type="button" class="sec" onclick={() => (hstep = H.steps.length)}>Xong</button>
      </div>
      <p class="dx-msg">
        {#if !lastStep}Bắt đầu: mỗi ký tự là một cây một nút, xếp theo trọng số: {forest.map((t) => `${t.sym}(${t.freq})`).join(', ')}.
        {:else}Gộp hai nhỏ nhất <b>{lastStep.a.sym !== null ? lastStep.a.sym + '(' + lastStep.a.freq + ')' : 'cây ' + lastStep.a.freq}</b> và <b>{lastStep.b.sym !== null ? lastStep.b.sym + '(' + lastStep.b.freq + ')' : 'cây ' + lastStep.b.freq}</b> thành nút trọng số <b>{lastStep.parent.freq}</b>. Còn {forest.length} cây.{/if}
      </p>
      <TreeSvg layout={hLayout} hot={hHot} label={hLabel} edgeLabels={true} ariaLabel="Rừng Huffman" />
      {#if finished || H.steps.length === 0}
        <div class="two">
          <table class="dx-t"><thead><tr><th>Ký tự</th><th>Tần suất</th><th>Mã</th><th>Độ dài</th></tr></thead>
            <tbody>{#each fr as f}<tr><td>{f.sym}</td><td>{f.freq}</td><td><code>{H.codes[f.sym]}</code></td><td>{H.codes[f.sym]?.length}</td></tr>{/each}</tbody></table>
          <div class="dx-card">
            <p class="dx-msg">Tổng bit Huffman: <b>{H.bits}</b> (trung bình {H.avg.toFixed(3)} bit/ký tự).<br />
              Mã độ dài cố định {H.fixedLen} bit: <b>{H.fixedBits}</b> bit → tiết kiệm <b>{H.fixedBits ? (100 * (1 - H.bits / H.fixedBits)).toFixed(1) : 0}%</b>.</p>
            <label>Thông điệp<input type="text" bind:value={message} style="width:100%" /></label>
            {#if bitsOut === null}<p class="dx-bad">Có ký tự không nằm trong bảng mã.</p>
            {:else}<p class="dx-msg">Mã hóa ({bitsOut.length} bit): <code class="bits">{bitsOut}</code><br />Giải mã lại: <b>{roundTrip}</b> {roundTrip === message ? '✓' : '✗'}</p>{/if}
          </div>
        </div>
      {/if}
    {:else}<p class="dx-bad">Nhập ít nhất một cặp ký_tự:số.</p>{/if}
  {/if}

  {#if tab !== 'huffman'}
    <div class="dx-bar">
      <label>Khóa (chèn lần lượt vào BST)<input type="text" bind:value={ktext} style="width:14rem" /></label>
      <button type="button" onclick={rebuild}>Dựng lại cây</button>
      <span class="dx-k">{treeStats}</span>
    </div>
  {/if}

  {#if tab === 'traversal'}
    <p class="dx-help">Ba cách duyệt theo vị trí của nút gốc N so với trái L và phải R. Với BST, <b>trung thứ tự cho dãy tăng dần</b>. Duyệt theo mức chính là BFS.</p>
    <div class="dx-bar">
      {#each Object.entries(ORDERS) as [id, o]}
        <button type="button" class="sec" class:on={order === id} onclick={() => { order = id; tstep = 0; }}>{o.label}</button>
      {/each}
    </div>
    <div class="dx-bar">
      <button type="button" class="sec" disabled={tstep <= 0} onclick={() => (tstep -= 1)}>◀</button>
      <button type="button" disabled={tstep >= seq.length} onclick={() => (tstep += 1)}>Thăm nút tiếp ▶</button>
      <button type="button" class="sec" onclick={() => (tstep = seq.length)}>Xong</button>
      <button type="button" class="sec" onclick={() => (tstep = 0)}>Đặt lại</button>
    </div>
    <TreeSvg layout={bLayout} hot={curNode} done={visited} ariaLabel="Cây nhị phân" />
    <p class="dx-msg">Thứ tự đã thăm: <b>{seq.slice(0, tstep).map((n) => n.key).join(' → ') || '(chưa)'}</b>{#if tstep === seq.length && seq.length}<br />Kết quả: {seq.map((n) => n.key).join(', ')}{/if}</p>
  {/if}

  {#if tab === 'bst'}
    <p class="dx-help">Mỗi phép chèn/tìm/xóa đi dọc <b>một đường</b> từ gốc: nhỏ hơn thì sang trái, lớn hơn sang phải — nên tốn O(chiều cao). Thử chèn dãy đã sắp (1 2 3 4 5 6) để thấy cây suy biến.</p>
    <div class="dx-bar">
      <label>Khóa<input type="text" bind:value={opVal} style="width:5rem" /></label>
      <button type="button" onclick={doInsert}>Chèn</button>
      <button type="button" class="sec" onclick={doSearch}>Tìm</button>
      <button type="button" class="sec" onclick={doDelete}>Xóa</button>
    </div>
    <TreeSvg layout={bLayout} hot={hotPath} {newId} ariaLabel="Cây tìm kiếm nhị phân" />
    <p class="dx-msg">{opMsg}</p>
  {/if}

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li><b>Huffman:</b> với mẫu CLRS, đoán trước hai cây nào được gộp ở mỗi bước rồi bấm kiểm tra; mã của <code>a</code> (tần suất 45) dài bao nhiêu bit?</li>
      <li>Đổi mọi tần suất thành bằng nhau: cây thành gần đầy đủ và Huffman ≈ mã độ dài cố định.</li>
      <li><b>Duyệt cây:</b> so sánh trung thứ tự với dãy khóa đã sắp; thử tiền thứ tự để thấy gốc luôn đứng đầu.</li>
      <li><b>BST:</b> chèn 1 2 3 4 5 6 vào cây rỗng (xóa ô khóa rồi "Dựng lại cây"), quan sát chiều cao = n.</li>
      <li>Xóa nút có hai con (ví dụ gốc) và giải thích vì sao khóa nhỏ nhất của cây con phải thay thế được.</li>
    </ol>
  </details>
</div>

<style>
  .two { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 8px; align-items: start; }
  @media (max-width: 760px) { .two { grid-template-columns: 1fr; } }
  .bits { word-break: break-all; background: #f1f5f9; padding: 1px 4px; border-radius: 4px; }
  p { margin: 6px 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
