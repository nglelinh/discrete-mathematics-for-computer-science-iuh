<script>
  import { terms, solveClosed, divideConquer, fibTree, fmt } from './recurrence.js';

  let { mode: modeProp = 'linear', preset = 'fib' } = $props();
  const PRE = {
    fib: { label: 'Fibonacci: aₙ = aₙ₋₁ + aₙ₋₂', c1: 1, c2: 1, k: 0, a0: 0, a1: 1 },
    hanoi: { label: 'Tháp Hà Nội: hₙ = 2hₙ₋₁ + 1', c1: 2, c2: 0, k: 1, a0: 0, a1: 1 },
    two: { label: 'aₙ = 3aₙ₋₁ − 2aₙ₋₂', c1: 3, c2: -2, k: 0, a0: 1, a1: 3 },
    double: { label: 'Nghiệm kép: aₙ = 4aₙ₋₁ − 4aₙ₋₂', c1: 4, c2: -4, k: 0, a0: 1, a1: 2 },
    complex: { label: 'Nghiệm phức: aₙ = aₙ₋₁ − aₙ₋₂', c1: 1, c2: -1, k: 0, a0: 1, a1: 1 },
    nonhom: { label: 'Không thuần nhất: aₙ = 3aₙ₋₁ − 2aₙ₋₂ + 1', c1: 3, c2: -2, k: 1, a0: 0, a1: 2 }
  };
  const p0 = PRE[preset] || PRE.fib;

  let mode = $state(['linear', 'dc', 'fib'].includes(modeProp) ? modeProp : 'linear');
  let presetId = $state(PRE[preset] ? preset : 'fib');
  let c1 = $state(p0.c1), c2 = $state(p0.c2), k = $state(p0.k), a0 = $state(p0.a0), a1 = $state(p0.a1);
  let N = $state(12);
  // chia để trị
  let da = $state(2), db = $state(2), dd = $state(1), dm = $state(4);
  // fib
  let fn = $state(5), memo = $state(false);

  const effA1 = $derived(c2 === 0 ? c1 * a0 + k : a1);
  const seq = $derived(terms(c1, c2, k, a0, effA1, N));
  const sol = $derived(solveClosed(c1, c2, k, a0, effA1));
  const closed = $derived(seq.map((_, n) => sol.value(n)));
  const match = $derived(seq.every((v, n) => Math.abs(v - closed[n]) <= 1e-6 * Math.max(1, Math.abs(v))));
  const dc = $derived(divideConquer(da, db, dd, dm));
  const tree = $derived(fibTree(fn));

  function loadPreset(id) {
    const p = PRE[id]; if (!p) return;
    presetId = id; c1 = p.c1; c2 = p.c2; k = p.k; a0 = p.a0; a1 = p.a1;
  }
  // chart
  const CW = 560, CH = 170;
  const maxAbs = $derived(Math.max(1, ...seq.map((v) => Math.abs(v))));
  const barW = $derived((CW - 40) / seq.length);
  const hasNeg = $derived(seq.some((v) => v < 0));
  const zeroY = $derived(hasNeg ? CH / 2 : CH - 18);
  const scale = $derived((hasNeg ? CH / 2 - 22 : CH - 36) / maxAbs);

  // bố cục cây fib
  const layout = $derived.by(() => {
    const nodes = [];
    let leaf = 0;
    const first = new Map();
    function go(nd, depth) {
      const kids = nd.kids.map((c) => go(c, depth + 1));
      const x = kids.length ? (kids[0].x + kids[kids.length - 1].x) / 2 : leaf++ * 34;
      const key = nd.n;
      const dupMemo = memo && first.has(key);
      if (!first.has(key)) first.set(key, nd.id);
      const out = { id: nd.id, n: nd.n, x, y: depth * 50, kids, dup: nd.dup, cut: dupMemo };
      if (dupMemo) out.kids = [];
      nodes.push(out);
      return out;
    }
    const root = go(tree.root, 0);
    const memoCalls = nodes.length;
    return { root, nodes, w: Math.max(1, leaf) * 34, h: (Math.max(...nodes.map((n) => n.y)) + 40), memoCalls };
  });
  function edges(nd, out = []) { nd.kids.forEach((c) => { out.push([nd, c]); edges(c, out); }); return out; }
  const maxLevelSum = $derived(Math.max(...dc.levels.map((l) => l.sum)));
</script>

<div class="dx rcx">
  <h4>Minh hoạ truy hồi</h4>
  <div class="dx-tabs">
    <button type="button" class="sec" class:on={mode === 'linear'} onclick={() => (mode = 'linear')}>Dãy tuyến tính (cấp 2)</button>
    <button type="button" class="sec" class:on={mode === 'dc'} onclick={() => (mode = 'dc')}>Chia để trị T(n) = aT(n/b) + nᵈ</button>
    <button type="button" class="sec" class:on={mode === 'fib'} onclick={() => (mode = 'fib')}>Cây gọi đệ quy fib(n)</button>
  </div>

  {#if mode === 'linear'}
    <p class="dx-help">Nhập hệ số của aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + k và điều kiện đầu. Công cụ liệt kê các số hạng, giải phương trình đặc trưng, rồi <b>so công thức đóng với giá trị truy hồi</b> từng số hạng.</p>
    <div class="dx-bar">
      <label>Mẫu
        <select value={presetId} onchange={(e) => loadPreset(e.currentTarget.value)}>
          {#each Object.entries(PRE) as [id, p]}<option value={id}>{p.label}</option>{/each}
        </select>
      </label>
      <label>c₁ <input type="number" bind:value={c1} step="1" style="width:4.5rem" /></label>
      <label>c₂ <input type="number" bind:value={c2} step="1" style="width:4.5rem" /></label>
      <label>k <input type="number" bind:value={k} step="1" style="width:4.5rem" /></label>
      <label>a₀ <input type="number" bind:value={a0} step="1" style="width:4.5rem" /></label>
      <label>a₁ <input type="number" value={effA1} disabled={c2 === 0} onchange={(e) => (a1 = Number(e.currentTarget.value))} step="1" style="width:4.5rem" /></label>
      <label>Số hạng <input type="range" min="5" max="20" bind:value={N} /> <span class="dx-k">{N}</span></label>
    </div>
    <div class="dx-grid2">
      <div class="dx-card">
        <header><h5>Phương trình đặc trưng</h5><span>{sol.kind === 'order1' ? 'cấp 1' : sol.kind === 'distinct' ? 'hai nghiệm thực khác nhau' : sol.kind === 'double' ? 'nghiệm kép' : 'nghiệm phức'}</span></header>
        <p class="dx-mono">{sol.charEq}</p>
        <p>Δ = c₁² + 4c₂ = {fmt(sol.disc)} →
          {#if sol.kind === 'distinct'}r₁ = {fmt(sol.roots[0])}, r₂ = {fmt(sol.roots[1])}
          {:else if sol.kind === 'double'}r = {fmt(sol.roots[0])} (kép)
          {:else if sol.kind === 'complex'}r = {fmt(sol.roots[0].rho)}·e<sup>±i·{fmt(sol.roots[0].theta)}</sup>
          {:else}r = {fmt(sol.roots[0])}{/if}
        </p>
        {#if k !== 0}<p class="dx-k">Hằng k ≠ 0 ⇒ thêm nghiệm riêng {sol.part.type === 'const' ? 'hằng số' : sol.part.type === 'lin' ? 'dạng p·n (vì 1 là nghiệm đặc trưng)' : 'dạng p·n² (1 là nghiệm kép)'}.</p>{/if}
        <p class="formula">{sol.formula}</p>
        <p class={match ? 'dx-ok' : 'dx-bad'}>{match ? `✓ Công thức đóng khớp truy hồi ở mọi n = 0…${N}.` : '✗ Có số hạng không khớp (kiểm tra hệ số).'}</p>
      </div>
      <div class="dx-card">
        <header><h5>Các số hạng</h5><span>cột trái: truy hồi · phải: công thức đóng</span></header>
        <div class="tw">
          <table class="dx-t">
            <thead><tr><th>n</th><th>aₙ (truy hồi)</th><th>công thức đóng</th><th></th></tr></thead>
            <tbody>
              {#each seq as v, n}
                <tr><td>{n}</td><td>{fmt(v)}</td><td>{fmt(closed[n])}</td><td>{Math.abs(v - closed[n]) <= 1e-6 * Math.max(1, Math.abs(v)) ? '✓' : '✗'}</td></tr>
              {/each}
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <svg viewBox="0 0 {CW} {CH}" class="dx-svg" role="img" aria-label="Biểu đồ các số hạng">
      <line x1="20" x2={CW - 10} y1={zeroY} y2={zeroY} stroke="#94a3b8" />
      {#each seq as v, n}
        {@const h = v * scale}
        <rect x={24 + n * barW} y={h >= 0 ? zeroY - h : zeroY} width={Math.max(2, barW - 4)} height={Math.abs(h)} fill={v >= 0 ? '#0f766e' : '#dc2626'} opacity="0.85" />
        <circle cx={24 + n * barW + (barW - 4) / 2} cy={zeroY - closed[n] * scale} r="3" fill="#f59e0b" />
        <text x={24 + n * barW + (barW - 4) / 2} y={CH - 4} text-anchor="middle" font-size="9" fill="#64748b">{n}</text>
      {/each}
    </svg>
    <p class="dx-k">Cột = giá trị truy hồi · chấm cam = công thức đóng (trùng khít khi đúng).</p>
  {/if}

  {#if mode === 'dc'}
    <p class="dx-help">T(n) = a·T(n/b) + nᵈ với n = bᵐ. Mỗi tầng i có aⁱ bài toán con cỡ n/bⁱ. So sánh <b>a</b> với <b>bᵈ</b> để biết tầng nào "nặng" nhất (định lý Master).</p>
    <div class="dx-bar">
      <label>a <input type="number" min="1" max="5" bind:value={da} style="width:4rem" /></label>
      <label>b <input type="number" min="2" max="4" bind:value={db} style="width:4rem" /></label>
      <label>d <input type="number" min="0" max="3" bind:value={dd} style="width:4rem" /></label>
      <label>m (n = bᵐ) <input type="number" min="1" max="6" bind:value={dm} style="width:4rem" /></label>
      <button type="button" class="sec" onclick={() => { da = 2; db = 2; dd = 1; dm = 4; }}>Sắp xếp trộn</button>
      <button type="button" class="sec" onclick={() => { da = 1; db = 2; dd = 0; dm = 5; }}>Tìm nhị phân</button>
      <button type="button" class="sec" onclick={() => { da = 3; db = 2; dd = 1; dm = 4; }}>Karatsuba (3,2,1)</button>
    </div>
    <div class="dx-card">
      <header><h5>Chi phí theo tầng (n = {db ** dm})</h5><span>độ dài thanh ∝ tổng chi phí của tầng</span></header>
      <table class="dx-t">
        <thead><tr><th>Tầng</th><th>Số nút</th><th>Cỡ mỗi nút</th><th>Chi phí mỗi nút</th><th>Tổng tầng</th><th></th></tr></thead>
        <tbody>
          {#each dc.levels as l}
            <tr><td>{l.i}{l.leaf ? ' (lá)' : ''}</td><td>{l.nodes}</td><td>{l.size}</td><td>{l.each}</td><td><b>{l.sum}</b></td>
              <td class="bar"><i style={`width:${(l.sum / maxLevelSum) * 100}%`}></i></td></tr>
          {/each}
        </tbody>
      </table>
      <p>T(n) = tổng các tầng = <b>{dc.total}</b> · so sánh a = {da} với b<sup>d</sup> = {dc.crit}:
        {#if dc.cls === 'root'}a &lt; bᵈ ⇒ tầng gốc nặng nhất{:else if dc.cls === 'balanced'}a = bᵈ ⇒ các tầng cân bằng{:else}a &gt; bᵈ ⇒ các lá nặng nhất{/if}
        ⇒ <b>T(n) = {dc.theta}</b>.</p>
    </div>
  {/if}

  {#if mode === 'fib'}
    <p class="dx-help">Cây gọi của <code>fib(n) = fib(n−1) + fib(n−2)</code>. Nút cam là <em>lời gọi lặp</em> (bài toán đã được tính ở nơi khác). Bật ghi nhớ (memo) để cắt các nhánh lặp.</p>
    <div class="dx-bar">
      <label>n <input type="range" min="1" max="8" bind:value={fn} /> <b>{fn}</b></label>
      <button type="button" class="sec" class:on={memo} onclick={() => (memo = !memo)}>{memo ? 'Đang dùng memo' : 'Bật memo'}</button>
    </div>
    <p class="dx-msg">
      Số lời gọi: <b>{memo ? layout.memoCalls : tree.calls}</b>{memo ? ` (thay vì ${tree.calls})` : ''} · lời gọi lặp (không memo): {tree.dupCalls} / {tree.calls} · số bài toán con khác nhau: {tree.distinct}.
      Không memo, số lời gọi tăng như φⁿ; có memo chỉ còn tuyến tính theo n.
    </p>
    <div class="ft">
      <svg viewBox={`-20 -20 ${layout.w + 40} ${layout.h + 30}`} class="dx-svg" role="img" aria-label="Cây gọi fib">
        {#each edges(layout.root) as [a, b]}<line x1={a.x} y1={a.y} x2={b.x} y2={b.y} stroke="#94a3b8" />{/each}
        {#each layout.nodes as nd (nd.id)}
          <g transform={`translate(${nd.x},${nd.y})`}>
            <circle r="13" fill={nd.cut ? '#e2e8f0' : nd.dup ? '#fed7aa' : '#fff'} stroke={nd.dup ? '#ea580c' : '#334155'} stroke-width="1.8" />
            <text y="4" text-anchor="middle" font-size="11" font-weight="700">{nd.n}</text>
          </g>
        {/each}
      </svg>
    </div>
  {/if}

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li>Chọn <em>Fibonacci</em>: đọc nghiệm đặc trưng (tỉ lệ vàng), rồi so với bảng số hạng.</li>
      <li>Chọn <em>Tháp Hà Nội</em>: đổi hằng k, quan sát nghiệm riêng đổi theo; dự đoán công thức đóng 2ⁿ − 1.</li>
      <li>Chọn <em>nghiệm kép</em> và <em>nghiệm phức</em>: công thức đóng có dạng gì? Dãy phức dao động thế nào trên biểu đồ?</li>
      <li><em>Chia để trị</em>: đổi (a,b,d) để lần lượt thấy ba trường hợp của Master; tầng nào nặng nhất?</li>
      <li><em>Cây fib</em>: tăng n đến 8, đếm lời gọi lặp; bật memo và so sánh.</li>
    </ol>
  </details>
</div>

<style>
  .formula { font-family: ui-monospace, Menlo, monospace; background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 8px 10px; font-size: 0.88rem; overflow-wrap: anywhere; }
  .tw { max-height: 280px; overflow: auto; }
  .bar { width: 40%; } .bar i { display: block; height: 10px; background: #0f766e; border-radius: 3px; }
  .ft { overflow-x: auto; }
  p { margin: 6px 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
