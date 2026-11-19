<script>
  import {
    parseSet, regionTable, regionLabel, unionOfRegions, parseElements, evaluateOnElements,
    inclusionExclusion, sameSetFamily, IDENTITIES
  } from './sets.js';

  let { sets: setsProp = 3, expr = '', exprB = '', focus = '' } = $props();

  const W = 560;
  const H = 380;
  const COLORS = ['#2563eb', '#ea580c', '#16a34a'];
  const NAMES = ['A', 'B', 'C'];

  let k = $state(setsProp === 2 ? 2 : 3);
  let exprDraft = $state(expr || (setsProp === 2 ? "A ∩ B'" : "(A ∪ B) ∩ C'"));
  let exprText = $state(exprDraft);
  let bDraft = $state(exprB || (setsProp === 2 ? "A' ∪ B'" : '(A ∩ C′) ∪ (B ∩ C′)'));
  let bText = $state(bDraft);
  let mode = $state(focus === 'compare' ? 'compare' : 'shade');
  let univText = $state('1..12');
  let setText = $state(['1,2,3,4,5', '4,5,6,7', '5,7,8,9']);
  let manual = $state(null);
  let hover = $state(-1);
  let canvas = $state(null);

  const parsed = $derived.by(() => {
    try { return { ast: parseSet(exprText) }; } catch (e) { return { error: e.message }; }
  });
  const parsedB = $derived.by(() => {
    try { return { ast: parseSet(bText) }; } catch (e) { return { error: e.message }; }
  });
  const elems = $derived.by(() => {
    try {
      const U0 = parseElements(univText);
      const S = [];
      for (let i = 0; i < k; i++) S.push(parseElements(setText[i]));
      const U = [...new Set([...U0, ...S.flat()])];
      return { U, S };
    } catch (e) {
      return { error: e.message, U: [], S: Array.from({ length: k }, () => []) };
    }
  });
  const sel = $derived(manual && manual.length === 1 << k ? manual : parsed.ast ? regionTable(parsed.ast, k) : Array(1 << k).fill(false));
  const result = $derived(
    parsed.ast && !elems.error && !manual ? evaluateOnElements(parsed.ast, k, elems.U, elems.S).result : null
  );
  const selElems = $derived.by(() => {
    if (elems.error) return [];
    const maskOf = (e) => elems.S.reduce((m, s, i) => m | (s.includes(e) ? 1 << i : 0), 0);
    return elems.U.filter((e) => sel[maskOf(e)]);
  });
  const resultB = $derived(
    parsedB.ast && !elems.error ? evaluateOnElements(parsedB.ast, k, elems.U, elems.S).result : null
  );
  const cmp = $derived(parsed.ast && parsedB.ast ? sameSetFamily(parsed.ast, parsedB.ast, k) : null);
  const ie = $derived(elems.error ? null : inclusionExclusion(elems.S.slice(0, k)));
  const regionExpr = $derived(unionOfRegions(sel, k));

  // hình học
  const circles = $derived(
    k === 2
      ? [{ x: 215, y: 190, r: 120 }, { x: 345, y: 190, r: 120 }]
      : [{ x: 220, y: 150, r: 108 }, { x: 340, y: 150, r: 108 }, { x: 280, y: 255, r: 108 }]
  );
  const maskAt = (x, y) =>
    circles.reduce((m, c, i) => m | ((x - c.x) ** 2 + (y - c.y) ** 2 <= c.r * c.r ? 1 << i : 0), 0);

  // vị trí phần tử trong từng vùng
  const placed = $derived.by(() => {
    const spots = new Map();
    for (let y = 22; y < H - 22; y += 13) {
      for (let x = 22; x < W - 22; x += 13) {
        const m = maskAt(x, y);
        const edge = Math.min(...circles.map((c) => Math.abs(Math.hypot(x - c.x, y - c.y) - c.r)));
        if (edge < 11) continue;
        if (m === 0 && x > 120 && x < 440 && y > 40 && y < H - 50 && circles.some((c) => Math.hypot(x - c.x, y - c.y) < c.r + 40)) continue;
        if (!spots.has(m)) spots.set(m, []);
        spots.get(m).push({ x, y, edge });
      }
    }
    const used = new Map();
    const out = [];
    if (elems.error) return out;
    const maskOf = (e) => elems.S.reduce((m, s, i) => m | (s.includes(e) ? 1 << i : 0), 0);
    for (const e of elems.U) {
      const m = maskOf(e);
      const list = (spots.get(m) || []).slice().sort((a, b) => b.edge - a.edge);
      const idx = used.get(m) || 0;
      used.set(m, idx + 1);
      const p = list[idx % Math.max(1, list.length)] || { x: 40, y: 40 };
      out.push({ e, x: p.x + (idx >= list.length ? 6 : 0), y: p.y, m });
    }
    return out;
  });

  $effect(() => {
    if (!canvas) return;
    draw(canvas, sel, hover, placed);
  });

  function draw(cv, selection, hv, dots) {
    const ctx = cv.getContext('2d');
    const img = ctx.createImageData(W, H);
    const rgb = [15, 118, 110];
    for (let y = 0; y < H; y++) {
      for (let x = 0; x < W; x++) {
        const m = maskAt(x + 0.5, y + 0.5);
        const o = (y * W + x) * 4;
        let r = 255, g = 255, b = 255;
        if (selection[m]) { r = 153; g = 230; b = 218; }
        if (m === hv) { r = Math.round(r * 0.9); g = Math.round(g * 0.9); b = Math.round(b * 0.8); }
        img.data[o] = r; img.data[o + 1] = g; img.data[o + 2] = b; img.data[o + 3] = 255;
      }
    }
    ctx.putImageData(img, 0, 0);
    ctx.lineWidth = 1.2;
    ctx.strokeStyle = '#94a3b8';
    ctx.strokeRect(6, 6, W - 12, H - 12);
    ctx.fillStyle = '#64748b';
    ctx.font = '600 13px system-ui, sans-serif';
    ctx.fillText('U', 14, 24);
    circles.forEach((c, i) => {
      ctx.beginPath();
      ctx.arc(c.x, c.y, c.r, 0, Math.PI * 2);
      ctx.lineWidth = 2.6;
      ctx.strokeStyle = COLORS[i];
      ctx.stroke();
    });
    ctx.font = '700 17px system-ui, sans-serif';
    const lab = k === 2 ? [[140, 80], [420, 80]] : [[150, 55], [410, 55], [280, 372]];
    lab.forEach(([x, y], i) => { ctx.fillStyle = COLORS[i]; ctx.fillText(NAMES[i], x, y); });
    ctx.font = '600 12px system-ui, sans-serif';
    ctx.textAlign = 'center';
    for (const d of dots) {
      ctx.fillStyle = selection[d.m] ? '#0f766e' : '#334155';
      ctx.beginPath();
      ctx.arc(d.x, d.y - 4, 2.6, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillText(d.e, d.x, d.y + 10);
    }
    ctx.textAlign = 'start';
  }

  function pointer(ev) {
    const r = canvas.getBoundingClientRect();
    return { x: ((ev.clientX - r.left) / r.width) * W, y: ((ev.clientY - r.top) / r.height) * H };
  }
  function onMove(ev) { const p = pointer(ev); hover = maskAt(p.x, p.y); }
  function onClick(ev) {
    const p = pointer(ev);
    const m = maskAt(p.x, p.y);
    const next = sel.slice();
    next[m] = !next[m];
    manual = next;
  }
  function apply() {
    exprText = exprDraft.trim();
    bText = bDraft.trim();
    manual = null;
  }
  function setK(n) { k = n; manual = null; }
  function loadIdentity(i) {
    const id = IDENTITIES[i];
    if (!id) return;
    k = id.k;
    exprDraft = exprText = id.a;
    bDraft = bText = id.b;
    mode = 'compare';
    manual = null;
  }
  const list = (a) => '{' + a.join(', ') + '}';
</script>

<div class="dx vex">
  <h4>Explainer tập hợp &amp; biểu đồ Venn</h4>
  <p class="dx-help">
    Nhập biểu thức (∪ ∩ \ Δ, bù <code>′</code> hoặc <code>¬</code>) để tô vùng tương ứng và xem tập kết quả trên dữ liệu bên dưới.
    Hoặc <strong>bấm thẳng vào các vùng</strong> trên hình — công cụ sinh biểu thức "hợp các vùng" cho bạn.
  </p>

  <div class="dx-tabs">
    <button type="button" class="sec" class:on={mode === 'shade'} onclick={() => (mode = 'shade')}>Tô vùng &amp; kết quả</button>
    <button type="button" class="sec" class:on={mode === 'compare'} onclick={() => (mode = 'compare')}>So sánh hai biểu thức</button>
    <button type="button" class="sec" class:on={mode === 'ie'} onclick={() => (mode = 'ie')}>Bao hàm–loại trừ</button>
    <span class="dx-k">Số tập</span>
    <button type="button" class="sec" class:on={k === 2} onclick={() => setK(2)}>2</button>
    <button type="button" class="sec" class:on={k === 3} onclick={() => setK(3)}>3</button>
  </div>

  <div class="dx-bar">
    <label class="grow">{mode === 'compare' ? 'X =' : 'Biểu thức'}
      <input type="text" bind:value={exprDraft} spellcheck="false" onkeydown={(e) => e.key === 'Enter' && apply()} />
    </label>
    {#if mode === 'compare'}
      <label class="grow">Y =
        <input type="text" bind:value={bDraft} spellcheck="false" onkeydown={(e) => e.key === 'Enter' && apply()} />
      </label>
      <label>Đẳng thức mẫu
        <select onchange={(e) => { if (e.currentTarget.value !== '') loadIdentity(Number(e.currentTarget.value)); e.currentTarget.value = ''; }}>
          <option value="">Chọn…</option>
          {#each IDENTITIES as id, i}<option value={i}>{id.label}</option>{/each}
        </select>
      </label>
    {/if}
    <button type="button" onclick={apply}>Áp dụng</button>
  </div>

  {#if parsed.error}<p class="dx-err">{parsed.error}</p>{/if}
  {#if mode === 'compare' && parsedB.error}<p class="dx-err">Y: {parsedB.error}</p>{/if}
  {#if elems.error}<p class="dx-err">{elems.error}</p>{/if}

  <div class="body">
    <div>
      <canvas bind:this={canvas} width={W} height={H} class="cv" onmousemove={onMove} onmouseleave={() => (hover = -1)} onclick={onClick}></canvas>
      <p class="dx-k">Di chuột để xem vùng: <strong>{hover >= 0 ? regionLabel(hover, k) : '—'}</strong></p>
    </div>
    <div class="side">
      <div class="dx-card">
        <header><h5>Dữ liệu</h5><span>sửa để thấy phần tử đổi vùng</span></header>
        <label>U <input type="text" bind:value={univText} /></label>
        {#each Array(k) as _, i}
          <label><b style={`color:${COLORS[i]}`}>{NAMES[i]}</b> <input type="text" bind:value={setText[i]} /></label>
        {/each}
      </div>
      <div class="dx-card">
        <header><h5>Kết quả</h5><span>{manual ? 'từ các vùng đã bấm' : 'từ biểu thức'}</span></header>
        {#if mode === 'compare'}
          {#if cmp}
            <p class={cmp.equal ? 'dx-ok' : 'dx-bad'}>
              {cmp.equal ? '✓ X = Y với mọi tập A, B, C (cùng tập vùng Venn).' : `✗ X ≠ Y: khác nhau ở ${cmp.diff.length} vùng — ${cmp.diff.map((m) => regionLabel(m, k)).join('; ')}.`}
            </p>
          {/if}
          <p>X = <span class="dx-mono">{result ? list(result) : '—'}</span></p>
          <p>Y = <span class="dx-mono">{resultB ? list(resultB) : '—'}</span></p>
        {:else}
          <p>Tập kết quả: <span class="dx-mono">{list(selElems)}</span> · |kết quả| = <strong>{selElems.length}</strong></p>
          <p class="dx-k">Hợp các vùng: <span class="dx-mono">{regionExpr}</span></p>
        {/if}
      </div>
      {#if mode === 'ie' && ie}
        <div class="dx-card">
          <header><h5>|A ∪ {k === 3 ? 'B ∪ C' : 'B'}| bằng bao hàm–loại trừ</h5></header>
          <p class="dx-mono">
            {#each ie.terms as t, i}{i ? (t.sign > 0 ? ' + ' : ' − ') : t.sign > 0 ? '' : '− '}{t.label}{/each}
          </p>
          <p class="dx-mono">
            = {#each ie.terms as t, i}{i ? (t.sign > 0 ? ' + ' : ' − ') : t.sign > 0 ? '' : '− '}{t.size}{/each} = <strong>{ie.total}</strong>
          </p>
          <p class={ie.total === ie.actual ? 'dx-ok' : 'dx-bad'}>
            Đếm trực tiếp |hợp| = {ie.actual} {ie.total === ie.actual ? '✓ khớp' : '✗ không khớp'}
          </p>
        </div>
      {/if}
    </div>
  </div>

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li>Nhập <code>A ∩ B′</code>, rồi <code>A \ B</code>. Hai vùng tô có giống nhau không? Vào chế độ <em>So sánh</em> để kiểm chứng.</li>
      <li>Chọn mẫu <em>De Morgan</em>: dự đoán trước hai vế có bằng nhau không, rồi so với kết quả.</li>
      <li>Thử <em>Sai thường gặp</em>: tìm vùng làm hai vế khác nhau và gán phần tử vào vùng đó làm phản ví dụ.</li>
      <li>Bấm tay vào 3 vùng bất kỳ, đọc biểu thức "hợp các vùng", rồi nhập lại dạng gọn hơn.</li>
      <li>Chế độ <em>Bao hàm–loại trừ</em>: đổi tập A, B, C để hai cách đếm luôn khớp.</li>
    </ol>
  </details>
</div>

<style>
  .grow { flex: 1 1 220px; } .grow input { flex: 1; min-width: 8rem; }
  .body { display: grid; grid-template-columns: minmax(280px, 1.2fr) minmax(240px, 1fr); gap: 12px; align-items: start; }
  @media (max-width: 800px) { .body { grid-template-columns: 1fr; } }
  .cv { width: 100%; height: auto; border: 1px solid #e2e8f0; border-radius: 10px; cursor: pointer; display: block; background: #fff; }
  .side { display: grid; gap: 10px; }
  .side label { margin: 3px 0; } .side label input { flex: 1; min-width: 0; }
  p { margin: 4px 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
