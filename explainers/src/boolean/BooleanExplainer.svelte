<script>
  import KMap from './KMap.svelte';
  import Circuit from './Circuit.svelte';
  import ComparePanel from './ComparePanel.svelte';
  import { PRESET_EXPR, VAR_NAMES, parse, prettyAst } from './logic.js';
  import {
    DC, resolveVars, valuesFor, assignOf, envOf, minimize, groupsFor, posLabel, sopText,
    canonicalForms, compareValues
  } from './logic2.js';
  import { netlistFromAst, netlistFromCover } from './circuit.js';

  let { vars = 3, focus = '', expr = '', exprB = '', dc = '', mode = 'single', form = 'sop', circuit = 'ast' } = $props();

  const init = (() => (vars === 2 || vars === 4 ? vars : 3))();
  const defaultExpr = (n) => (n === 2 ? 'p ∧ q' : n === 4 ? '(p ∧ q) ∨ (¬r ∧ s)' : '(p ∧ q) → r');
  const defaultB = (n) => (n === 2 ? '¬p ∨ ¬q' : n === 4 ? '(p ∧ q) ∨ s' : '¬p ∨ ¬q ∨ r');

  let nVars = $state(init);
  let exprText = $state(expr || defaultExpr(init));
  let exprDraft = $state(expr || defaultExpr(init));
  let exprBText = $state(exprB || defaultB(init));
  let exprBDraft = $state(exprB || defaultB(init));
  let overrides = $state(null);
  let viewMode = $state(mode === 'compare' ? 'compare' : 'single');
  let kform = $state(form === 'pos' ? 'pos' : 'sop');
  let circuitKind = $state(['ast', 'sop', 'pos'].includes(circuit) ? circuit : 'ast');
  let probe = $state(0);
  let hovered = $state(null);
  let highlighted = $state(-1);

  // don't-care ban đầu từ data-dc
  const dcInit = dc ? dc.split(',').map((s) => Number(s.trim())).filter((x) => Number.isInteger(x)) : [];
  let dcPending = $state(dcInit);

  const tryParse = (src) => {
    try { return { ast: parse(src) }; } catch (e) { return { error: e.message }; }
  };
  const pa = $derived(tryParse(exprText));
  const pb = $derived(viewMode === 'compare' ? tryParse(exprBText) : { ast: null });

  const resolved = $derived.by(() => {
    try {
      return { names: resolveVars(nVars, [pa.ast, pb.ast]) };
    } catch (e) {
      return { names: VAR_NAMES.slice(0, nVars), error: e.message };
    }
  });
  const names = $derived(resolved.names);
  const error = $derived(pa.error || pb.error || resolved.error || '');

  const exprValues = $derived.by(() => {
    const base = pa.ast && !resolved.error ? valuesFor(nVars, pa.ast, names) : Array(1 << nVars).fill(0);
    if (dcPending.length && !overrides) {
      const v = base.slice();
      for (const m of dcPending) if (m >= 0 && m < v.length) v[m] = DC;
      return v;
    }
    return base;
  });
  const values = $derived(overrides && overrides.length === 1 << nVars ? overrides : exprValues);
  const valuesB = $derived(pb.ast && !resolved.error ? valuesFor(nVars, pb.ast, names) : Array(1 << nVars).fill(0));
  const custom = $derived(!!overrides || (dcPending.length > 0 && values.includes(DC)));

  const sop = $derived(minimize(values, nVars, 'sop'));
  const pos = $derived(minimize(values, nVars, 'pos'));
  const sopStr = $derived(sopText(sop.cover, names));
  const posStr = $derived(posLabel(pos.cover, names));
  const canon = $derived(canonicalForms(values, names));
  const active = $derived(kform === 'pos' ? pos : sop);
  const groups = $derived(groupsFor(active, names, nVars));
  const hasDc = $derived(values.includes(DC));

  const effCircuit = $derived(circuitKind === 'ast' && (!pa.ast || custom || resolved.error) ? 'sop' : circuitKind);
  const net = $derived(
    effCircuit === 'ast' ? netlistFromAst(pa.ast, names) : netlistFromCover((effCircuit === 'pos' ? pos : sop).cover, names, effCircuit)
  );
  const env = $derived(envOf(Math.min(probe, (1 << nVars) - 1), names));
  const cmp = $derived(compareValues(values.map((v) => (v === DC ? 0 : v)), valuesB));

  function applyExpr() {
    exprText = exprDraft.trim();
    exprBText = exprBDraft.trim();
    overrides = null;
    dcPending = [];
    highlighted = -1;
  }
  function changeVars(n) {
    nVars = n;
    exprText = exprDraft = defaultExpr(n);
    exprBText = exprBDraft = defaultB(n);
    overrides = null;
    dcPending = [];
    highlighted = -1;
    probe = 0;
  }
  function loadPreset(e) {
    exprText = exprDraft = e;
    overrides = null;
    dcPending = [];
  }
  function loadPair(i) {
    const p = PAIRS[i];
    if (!p) return;
    nVars = p.n;
    viewMode = 'compare';
    exprText = exprDraft = p.a;
    exprBText = exprBDraft = p.b;
    overrides = null;
    dcPending = [];
  }
  const PAIRS = [
    { label: 'De Morgan: ¬(p ∧ q) ≡ ¬p ∨ ¬q', n: 2, a: '¬(p ∧ q)', b: '¬p ∨ ¬q' },
    { label: 'Phản đảo: p → q ≡ ¬q → ¬p', n: 2, a: 'p → q', b: '¬q → ¬p' },
    { label: 'Đảo: p → q ≢ q → p', n: 2, a: 'p → q', b: 'q → p' },
    { label: 'Phân phối: p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)', n: 3, a: 'p ∨ (q ∧ r)', b: '(p ∨ q) ∧ (p ∨ r)' },
    { label: 'Hấp thụ: p ∨ (p ∧ q) ≡ p', n: 2, a: 'p ∨ (p ∧ q)', b: 'p' },
    { label: 'Sai thường gặp: ¬(p ∨ q) ≢ ¬p ∨ ¬q', n: 2, a: '¬(p ∨ q)', b: '¬p ∨ ¬q' }
  ];
  function cycle(m) {
    const base = values.slice();
    base[m] = (base[m] + 1) % 3;
    overrides = base;
    probe = m;
    highlighted = -1;
  }
  function toggleProbe(name) {
    const i = names.indexOf(name);
    if (i < 0) return;
    probe = probe ^ (1 << (nVars - 1 - i));
  }
  const shown = (v) => (v === DC ? '×' : String(v));
  function cellGroups(m) {
    return groups.filter((g) => g.covered.has(m));
  }
</script>

<div class="dx bex" class:f-table={focus === 'table'} class:f-circuit={focus === 'circuit'} class:f-kmap={focus === 'kmap'}>
  <h4>Explainer logic &amp; đại số Boole</h4>
  <p class="dx-help">
    Ba khung nhìn liên kết: <strong>bảng chân trị ↔ bản đồ Karnaugh ↔ mạch</strong>. Sửa biểu thức, hoặc bấm ô F / ô K-map để đổi
    <strong>0 → 1 → ×</strong> (× = don't care). Chọn dạng tối tiểu <strong>SOP</strong> (phủ các ô 1) hoặc <strong>POS</strong> (phủ các ô 0).
    Bấm tên biến trên mạch (hoặc một hàng) để xem tín hiệu chạy qua từng cổng.
  </p>

  <div class="dx-tabs">
    <button type="button" class="sec" class:on={viewMode === 'single'} onclick={() => (viewMode = 'single')}>Một hàm</button>
    <button type="button" class="sec" class:on={viewMode === 'compare'} onclick={() => (viewMode = 'compare')}>So sánh hai biểu thức</button>
    <span class="dx-k">Số biến</span>
    {#each [2, 3, 4] as k}
      <button type="button" class="sec" class:on={nVars === k} onclick={() => changeVars(k)}>{k}</button>
    {/each}
  </div>

  <div class="dx-bar">
    <label class="grow">{viewMode === 'compare' ? 'A =' : 'F ='}
      <input type="text" bind:value={exprDraft} spellcheck="false" placeholder="ví dụ (p ∧ q) → r" onkeydown={(e) => e.key === 'Enter' && applyExpr()} />
    </label>
    {#if viewMode === 'compare'}
      <label class="grow">B =
        <input type="text" bind:value={exprBDraft} spellcheck="false" placeholder="biểu thức thứ hai" onkeydown={(e) => e.key === 'Enter' && applyExpr()} />
      </label>
    {/if}
    <button type="button" onclick={applyExpr}>Áp dụng</button>
    {#if viewMode === 'single'}
      <label>Mẫu
        <select onchange={(e) => { if (e.currentTarget.value) loadPreset(e.currentTarget.value); e.currentTarget.value = ''; }}>
          <option value="">Chọn…</option>
          {#each PRESET_EXPR[nVars] || [] as p}<option value={p.expr}>{p.label}</option>{/each}
        </select>
      </label>
    {:else}
      <label>Cặp mẫu
        <select onchange={(e) => { if (e.currentTarget.value !== '') loadPair(Number(e.currentTarget.value)); e.currentTarget.value = ''; }}>
          <option value="">Chọn…</option>
          {#each PAIRS as p, i}<option value={i}>{p.label}</option>{/each}
        </select>
      </label>
    {/if}
  </div>

  {#if error}
    <p class="dx-err">{error}</p>
  {:else if viewMode === 'single'}
    <p class="status">
      {#if custom}<strong>Hàm tùy chỉnh</strong> (đã sửa bảng / K-map){:else}F = <strong>{prettyAst(pa.ast)}</strong>{/if}
      {#if custom}<button type="button" class="sec mini" onclick={applyExpr}>Khôi phục biểu thức</button>{/if}
      <br />
      SOP tối tiểu: <strong>{sopStr}</strong> · POS tối tiểu: <strong>{posStr}</strong>
      {#if hasDc}· <em>có don't-care (×) nên dạng tối tiểu có thể gọn hơn</em>{/if}
    </p>
  {/if}

  {#if viewMode === 'compare'}
    {#if !error}
      <ComparePanel
        n={nVars} {names} va={values.map((v) => (v === DC ? 0 : v))} vb={valuesB}
        diff={cmp.diff} equivalent={cmp.equivalent} aImpB={cmp.aImpB} bImpA={cmp.bImpA}
        sopA={sopStr} sopB={sopText(minimize(valuesB, nVars, 'sop').cover, names)}
      />
    {/if}
  {:else}
    <div class="grid">
      <section class="dx-card" class:pulse={focus === 'table'}>
        <header><h5>Bảng chân trị</h5><span>bấm F để đổi 0 → 1 → ×</span></header>
        <div class="tw">
          <table class="dx-t">
            <thead><tr><th>m</th>{#each names as v}<th>{v}</th>{/each}<th>F</th></tr></thead>
            <tbody>
              {#each values as val, m}
                {@const gs = cellGroups(m)}
                <tr
                  class:on={hovered === m}
                  class:one={val === 1}
                  class:dcr={val === DC}
                  class:probe={probe === m}
                  style={gs[0] && highlighted >= 0 && groups[highlighted]?.covered.has(m) ? `background:${groups[highlighted].color}22` : gs[0] ? `box-shadow: inset 3px 0 0 ${gs[0].color}` : ''}
                  onmouseenter={() => (hovered = m)}
                  onmouseleave={() => (hovered = null)}
                  onclick={() => (probe = m)}
                >
                  <td class="m">m{m}</td>
                  {#each assignOf(m, nVars) as b}<td>{b}</td>{/each}
                  <td><button type="button" class="bit" class:one={val === 1} class:dcb={val === DC} onclick={(e) => { e.stopPropagation(); cycle(m); }}>{shown(val)}</button></td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      </section>

      <section class="dx-card" class:pulse={focus === 'kmap'}>
        <header><h5>Bản đồ Karnaugh ({kform === 'pos' ? 'nhóm ô 0 → POS' : 'nhóm ô 1 → SOP'})</h5><span>bấm ô để đổi 0 → 1 → ×</span></header>
        <div class="dx-tabs">
          <button type="button" class="sec" class:on={kform === 'sop'} onclick={() => { kform = 'sop'; highlighted = -1; }}>SOP</button>
          <button type="button" class="sec" class:on={kform === 'pos'} onclick={() => { kform = 'pos'; highlighted = -1; }}>POS</button>
        </div>
        <KMap n={nVars} {values} {names} {groups} {hovered} {highlighted} {probe}
          onToggle={cycle} onHover={(m) => (hovered = m)} />
        <div class="gl">
          {#if !groups.length}
            <span class="dx-k">Không có nhóm ({kform === 'sop' ? 'F = 0' : 'F = 1'}).</span>
          {:else}
            {#each groups as g, i}
              <button type="button" class="gchip" class:gon={highlighted === i} style={`--g:${g.color}`}
                onmouseenter={() => (highlighted = i)} onmouseleave={() => (highlighted = -1)}
                onclick={() => (highlighted = highlighted === i ? -1 : i)}>{kform === 'pos' ? '(' + g.label + ')' : g.label}</button>
            {/each}
          {/if}
        </div>
      </section>

      <section class="dx-card wide" class:pulse={focus === 'circuit'}>
        <header>
          <h5>Mạch logic</h5>
          <span>vòng tròn nhỏ = phủ định · xanh = tín hiệu 1 với tổ hợp đang chọn</span>
        </header>
        <div class="dx-tabs">
          <button type="button" class="sec" class:on={effCircuit === 'ast'} disabled={!pa.ast || custom} title={custom ? 'Hàm đã bị sửa nên không còn biểu thức gốc' : ''} onclick={() => (circuitKind = 'ast')}>Từ biểu thức gốc</button>
          <button type="button" class="sec" class:on={effCircuit === 'sop'} onclick={() => (circuitKind = 'sop')}>SOP tối tiểu (AND–OR)</button>
          <button type="button" class="sec" class:on={effCircuit === 'pos'} onclick={() => (circuitKind = 'pos')}>POS tối tiểu (OR–AND)</button>
          <span class="dx-k">Đang xét: {names.map((v, i) => `${v}=${assignOf(probe, nVars)[i]}`).join(', ')} (m{probe})</span>
        </div>
        <Circuit {net} {env} onToggle={toggleProbe} />
      </section>

      <section class="dx-card wide">
        <header><h5>Dạng chuẩn tắc</h5><span>từ bảng chân trị hiện tại</span></header>
        <div class="canon">
          <div><b>Tổng các minterm (DNF đầy đủ):</b> <span class="dx-mono">{canon.sigma}</span></div>
          <div class="long dx-mono">{canon.dnf}</div>
          <div><b>Tích các maxterm (CNF đầy đủ):</b> <span class="dx-mono">{canon.pi}</span></div>
          <div class="long dx-mono">{canon.cnf}</div>
        </div>
      </section>
    </div>
  {/if}
</div>

<style>
  .grow { flex: 1 1 220px; }
  .grow input { flex: 1; min-width: 8rem; }
  .status { margin: 0 0 10px; padding: 8px 10px; background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; color: #0c4a6e; font-size: 0.9rem; line-height: 1.5; }
  .mini { padding: 3px 8px !important; font-size: 0.78rem !important; margin-left: 8px; }
  .grid { display: grid; grid-template-columns: minmax(200px, 0.9fr) minmax(260px, 1.1fr); gap: 12px; }
  .wide { grid-column: 1 / -1; }
  @media (max-width: 800px) { .grid { grid-template-columns: 1fr; } .wide { grid-column: auto; } }
  .pulse { box-shadow: 0 0 0 2px #bae6fd; }
  .tw { overflow: auto; }
  tr.on { background: #fef9c3; }
  tr.one { background: #f0fdfa; }
  tr.dcr { background: #fffbeb; }
  tr.probe td.m { font-weight: 700; color: #0369a1; }
  tr { cursor: pointer; }
  td.m { color: #64748b; font-size: 0.78rem; }
  .bit { min-width: 1.8rem; padding: 2px 0 !important; border-radius: 6px; background: #fff !important; color: #0f172a !important; border-color: #cbd5e1 !important; }
  .bit.one { background: #0f766e !important; color: #fff !important; border-color: #0f766e !important; }
  .bit.dcb { background: #fde68a !important; color: #78350f !important; border-color: #f59e0b !important; }
  .gl { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; min-height: 1.8rem; }
  .gchip { background: #fff !important; color: var(--g) !important; border: 1.5px solid var(--g) !important; font-weight: 650; font-size: 0.82rem !important; padding: 4px 8px !important; }
  .gchip.gon { background: var(--g) !important; color: #fff !important; }
  .canon { font-size: 0.88rem; display: grid; gap: 4px; }
  .canon .long { color: #475569; font-size: 0.8rem; overflow-wrap: anywhere; margin-bottom: 6px; }
</style>
