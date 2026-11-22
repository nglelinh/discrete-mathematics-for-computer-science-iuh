<script>
  import { runQM, parseNums, valuesFrom, PRESETS, DEFAULT_NAMES, termText, coverOf, literals } from './qm.js';
  import { parse, collectVars, evalAst, implicantRects, kmapCells } from '../boolean/logic.js';

  let { preset = 'f1', vars = 0, minterms = '', dc = '', expr = '', names: namesProp = '', start = '' } = $props();

  const p0 = PRESETS.find((x) => x.id === preset) || PRESETS[0];
  const custom = !!(minterms || expr);
  let presetId = $state(custom ? 'custom' : p0.id);
  let n = $state(vars >= 2 && vars <= 6 ? vars : p0.n);
  let inputMode = $state(expr ? 'expr' : 'minterms');
  let onesText = $state(minterms || (custom ? '' : p0.ones));
  let dcText = $state(custom ? dc : dc || p0.dc);
  let exprText = $state(expr || 'ab + ¬a¬c');
  let names = $state(
    namesProp ? namesProp.split(/[\s,]+/).filter(Boolean) : custom ? DEFAULT_NAMES.slice(0, n) : p0.names
  );
  let startVal = $state(start);
  let idx = $state(0);
  let playing = $state(false);
  let hoverPrime = $state(null);

  const HUES = ['#0f766e', '#7c3aed', '#c2410c', '#0369a1', '#be185d', '#4d7c0f', '#b45309', '#1d4ed8'];

  const model = $derived.by(() => {
    try {
      const nn = Math.max(2, Math.min(6, Number(n) || 3));
      let nm = names.length >= nn ? names.slice(0, nn) : DEFAULT_NAMES.slice(0, nn);
      const warn = [];
      const dcs = parseNums(dcText, nn);
      let ones;
      let extra = [];
      if (inputMode === 'expr') {
        const ast = parse(exprText);
        const used = [...collectVars(ast)].sort((a, b) => a.localeCompare(b));
        if (used.length > nn) throw new Error(`Biểu thức dùng ${used.length} biến (${used.join(', ')}) nhưng đang chọn ${nn} biến — tăng số biến.`);
        const pad = DEFAULT_NAMES.filter((x) => !used.includes(x));
        nm = [...used, ...pad].slice(0, nn).sort((a, b) => a.localeCompare(b));
        ones = [];
        for (let m = 0; m < 1 << nn; m++) {
          const env = {};
          nm.forEach((v, i) => (env[v] = (m >> (nn - 1 - i)) & 1));
          if (evalAst(ast, env)) ones.push(m);
        }
        extra = [];
      } else {
        const o = parseNums(onesText, nn);
        ones = o.nums;
        extra = o.errors;
      }
      extra = [...extra, ...dcs.errors];
      const both = ones.filter((m) => dcs.nums.includes(m));
      if (both.length) warn.push(`Ô ${both.join(', ')} vừa là minterm vừa là don't-care — coi là don't-care.`);
      const qm = runQM(nn, ones, dcs.nums, nm);
      return { ok: true, n: nn, names: nm, qm, errors: extra, warn, values: valuesFrom(nn, qm.ones, qm.dcs) };
    } catch (e) {
      return { ok: false, error: e.message || String(e) };
    }
  });

  const qm = $derived(model.ok ? model.qm : null);
  const steps = $derived(qm ? qm.steps : []);
  const last = $derived(Math.max(0, steps.length - 1));
  const at = $derived(Math.min(idx, last));
  const step = $derived(steps[at] || null);
  const primesIdx = $derived(steps.findIndex((s) => s.kind === 'primes'));
  const phase = $derived(step ? step.phase : 1);

  // đưa về bước 0 khi dữ liệu đổi
  let sig = '';
  $effect(() => {
    const s = model.ok ? JSON.stringify([model.n, model.qm.ones, model.qm.dcs, model.names]) : 'err';
    if (s !== sig) {
      sig = s;
      idx = startVal === 'end' && model.ok ? model.qm.steps.length - 1 : Number(startVal) > 0 && model.ok ? Math.min(Number(startVal), model.qm.steps.length - 1) : 0;
      startVal = '';
      playing = false;
    }
  });
  $effect(() => {
    if (!playing) return;
    const t = setTimeout(() => {
      if (idx >= last) playing = false;
      else idx += 1;
    }, 1600);
    return () => clearTimeout(t);
  });

  function applyPreset(id) {
    const p = PRESETS.find((x) => x.id === id);
    if (!p) return;
    presetId = id; n = p.n; names = p.names; inputMode = 'minterms'; onesText = p.ones; dcText = p.dc;
  }
  function setN(v) {
    n = Number(v); names = DEFAULT_NAMES.slice(0, n); presetId = 'custom';
    onesText = parseNums(onesText, n).nums.join(','); dcText = parseNums(dcText, n).nums.join(',');
  }

  // ---- hiển thị cột (phần 1)
  const visibleCols = $derived(
    qm
      ? qm.columns
          .map((col) => col.filter((it) => it.step <= at))
          .filter((c) => c.length)
          .map((col) => {
            const groups = [];
            for (const it of col) {
              let g = groups.find((x) => x.k === it.ones);
              if (!g) groups.push((g = { k: it.ones, items: [] }));
              g.items.push(it);
            }
            return groups.sort((a, b) => a.k - b.k);
          })
      : []
  );
  const combos = $derived(step && step.kind === 'pair' ? step.combos : []);
  const isA = (id) => combos.some((c) => c.a === id || c.b === id);
  const isRes = (id) => combos.some((c) => c.res === id);
  const checked = (it) => it.usedStep !== null && it.usedStep <= at && it.step <= at;
  const isPrime = (it) => primesIdx >= 0 && at >= primesIdx && !it.used;
  const fmtMins = (it) => it.mins.join(',');
  const primeColor = (it) => HUES[qm.primes.indexOf(it) % HUES.length];

  // ---- bảng phủ (phần 2)
  const snapStep = $derived(step && step.phase === 2 && step.activeRows ? step : null);
  const rowState = (r) => {
    const s = snapStep; if (!s) return '';
    if (s.picked.includes(r.id)) return 'picked';
    if (s.petrickRows && s.petrickRows.includes(r.id)) return 'pet';
    if (!s.activeRows.includes(r.id)) return 'gone';
    return '';
  };
  const colCovered = (c) => !!snapStep && qm.chart.rows.some((r) => snapStep.picked.includes(r.id) && r.mins.includes(c));
  const colState = (c) => {
    const s = snapStep; if (!s) return '';
    if (colCovered(c)) return 'cov';
    if (!s.activeCols.includes(c)) return 'gone';
    return '';
  };
  const letters = $derived.by(() => {
    const m = {};
    for (let i = steps.length - 1; i >= 0; i--) if (steps[i].kind === 'petrickSetup' && i <= at) { steps[i].letters.forEach((l) => (m[l.rid] = l.p)); break; }
    return m;
  });
  const dcSet = $derived(new Set(qm ? qm.dcs : []));

  // ---- K-map (≤ 4 biến)
  const CS = 54, OX = 78, OY = 48;
  const km = $derived(model.ok && model.n <= 4 ? kmapCells(model.n, model.values) : null);
  const valAt = (m) => (model.values[m] === 2 ? '×' : model.values[m] ? '1' : '0');
  const primeRects = $derived.by(() => {
    if (!km || !qm) return [];
    const show = at >= primesIdx && primesIdx >= 0;
    if (!show) return [];
    const final = step && step.kind === 'result' ? step.final : null;
    const pickedNow = snapStep ? [...snapStep.picked, ...(snapStep.petrickRows || [])] : [];
    return qm.primes.map((pr, i) => ({
      pr, i,
      rects: implicantRects(pr.bits, model.n),
      color: HUES[i % HUES.length],
      state: final ? (final.includes(pr.id) ? 'final' : 'hide') : pickedNow.includes(pr.id) ? 'picked' : 'faint'
    })).filter((x) => x.state !== 'hide');
  });
  const pairCells = $derived.by(() => {
    if (!combos.length) return { a: new Set(), r: new Set() };
    const a = new Set(), r = new Set();
    for (const c of combos) {
      for (const id of [c.a, c.b]) qm.items.find((x) => x.id === id).mins.forEach((m) => a.add(m));
      qm.items.find((x) => x.id === c.res).mins.forEach((m) => r.add(m));
    }
    return { a, r };
  });
  const hoverRects = $derived(hoverPrime && km ? implicantRects(hoverPrime.bits, model.n) : []);
  const cellXY = (r, c) => [OX + c * CS, OY + r * CS];
  const KW = $derived(km ? OX + km.nCols * CS + 14 : 0);
  const KH = $derived(km ? OY + km.nRows * CS + 14 : 0);

  const resultTerms = $derived(qm && qm.result ? qm.result.terms : []);
  const showResult = $derived(step && (step.kind === 'result' || step.kind === 'empty'));
</script>

<div class="dx qmx">
  <h4>Minh hoạ Quine–McCluskey</h4>
  <p class="dx-help">
    Nhập minterm (và don't-care) hoặc một biểu thức, rồi bấm <b>Bước tiếp</b>. Phần 1 dán các nguyên nhân thành cột để tìm <b>nguyên nhân nguyên tố</b>;
    phần 2 lập <b>bảng phủ</b>, chọn nguyên tố cốt yếu, loại hàng/cột trội, rồi dùng <b>Petrick</b> cho phần còn lại.
  </p>

  <div class="dx-bar">
    <label>Ví dụ
      <select value={presetId} onchange={(e) => applyPreset(e.currentTarget.value)}>
        {#if presetId === 'custom'}<option value="custom">Tự nhập…</option>{/if}
        {#each PRESETS as p}<option value={p.id}>{p.label}</option>{/each}
      </select>
    </label>
    <label>Số biến
      <select value={n} onchange={(e) => setN(e.currentTarget.value)}>{#each [2, 3, 4, 5, 6] as k}<option value={k}>{k}</option>{/each}</select>
    </label>
    <button type="button" class="sec" class:on={inputMode === 'minterms'} onclick={() => { inputMode = 'minterms'; presetId = 'custom'; }}>Nhập minterm</button>
    <button type="button" class="sec" class:on={inputMode === 'expr'} onclick={() => { inputMode = 'expr'; presetId = 'custom'; }}>Nhập biểu thức</button>
  </div>
  <div class="dx-bar">
    {#if inputMode === 'minterms'}
      <label>Σm (F = 1)<input type="text" bind:value={onesText} oninput={() => (presetId = 'custom')} style="width:16rem" placeholder="vd. 1,2,5 hoặc 0-7" /></label>
    {:else}
      <label>F = <input type="text" bind:value={exprText} oninput={() => (presetId = 'custom')} style="width:16rem" placeholder="vd. a∧b ∨ ¬a∧¬c" /></label>
    {/if}
    <label>Σd (don't-care)<input type="text" bind:value={dcText} oninput={() => (presetId = 'custom')} style="width:11rem" placeholder="vd. 0,7" /></label>
    <span class="dx-k">Biến: {model.ok ? model.names.join(' ') : ''} (bit cao → thấp)</span>
  </div>
  {#if !model.ok}<p class="dx-err">{model.error}</p>{/if}
  {#if model.ok}
    {#each model.errors as e}<p class="dx-err">{e}</p>{/each}
    {#each model.warn as w}<p class="dx-k">⚠ {w}</p>{/each}
  {/if}
  {#if inputMode === 'minterms' && PRESETS.find((x) => x.id === presetId)?.note}<p class="dx-k note">{PRESETS.find((x) => x.id === presetId).note}</p>{/if}

  {#if qm}
    <div class="dx-bar ctl">
      <button type="button" class="sec" disabled={at <= 0} onclick={() => { playing = false; idx = 0; }}>⏮</button>
      <button type="button" class="sec" disabled={at <= 0} onclick={() => { playing = false; idx = at - 1; }}>◀ Lùi</button>
      <button type="button" disabled={at >= last} onclick={() => { playing = false; idx = at + 1; }}>Bước tiếp ▶</button>
      <button type="button" class="sec" onclick={() => { if (at >= last) idx = 0; playing = !playing; }}>{playing ? '⏸ Dừng' : '▶ Tự chạy'}</button>
      <button type="button" class="sec" disabled={at >= last} onclick={() => { playing = false; idx = last; }}>Kết quả ⏭</button>
      <span class="dx-k">Bước {at + 1} / {steps.length} · {phase === 1 ? 'Phần 1: nguyên nhân nguyên tố' : 'Phần 2: bảng phủ'}</span>
    </div>
    <div class="prog"><div style={`width:${((at + 1) / steps.length) * 100}%`}></div></div>

    <div class="dx-msg expl" aria-live="polite">
      <b>{step.title}.</b> {step.text}
    </div>

    {#if step.kind !== 'empty'}
      <div class="layout">
        <div class="main">
          <div class="dx-card">
            <header><h5>Phần 1 — Bảng dán</h5><span>✓ = đã được dán (không phải nguyên tố) · dấu «-» = bit bị loại</span></header>
            <div class="cols">
              {#each visibleCols as groups, ci}
                <table class="dx-t qt">
                  <thead><tr><th colspan="3">Cột {ci + 1}</th></tr></thead>
                  <tbody>
                    {#each groups as g}
                      <tr class="gh"><td colspan="3">{g.k} bit 1</td></tr>
                      {#each g.items as it (it.id)}
                        <tr class:ha={isA(it.id)} class:hr={isRes(it.id)} class:pr={isPrime(it)} class:dco={it.dcOnly} style={isPrime(it) ? `--pc:${primeColor(it)}` : ''}
                          onmouseenter={() => isPrime(it) && (hoverPrime = it)} onmouseleave={() => (hoverPrime = null)}>
                          <td class="mn">{fmtMins(it)}{#if it.dcOnly}<sup>d</sup>{/if}</td>
                          <td class="bt dx-mono">{it.bits}</td>
                          <td class="ck">{checked(it) ? '✓' : ''}{#if isPrime(it)}<b title="nguyên nhân nguyên tố">★</b>{/if}</td>
                        </tr>
                      {/each}
                    {/each}
                  </tbody>
                </table>
              {/each}
            </div>
            {#if primesIdx >= 0 && at >= primesIdx}
              <div class="dx-chips pchips">
                {#each qm.primes as pr, i}
                  <span class="dx-chip pchip" style={`border-color:${HUES[i % HUES.length]}`} onmouseenter={() => (hoverPrime = pr)} onmouseleave={() => (hoverPrime = null)} role="presentation">
                    {termText(pr.bits, model.names)}<small class="dx-mono">{pr.bits} · {pr.mins.join(',')}</small>
                  </span>
                {/each}
              </div>
            {/if}
          </div>

          {#if phase === 2}
            <div class="dx-card">
              <header><h5>Phần 2 — Bảng phủ</h5><span>xanh = đã chọn · xám = đã loại · vàng = đang xét</span></header>
              <div class="scroll">
                <table class="dx-t chart">
                  <thead>
                    <tr><th>Nguyên nhân nguyên tố</th>{#each qm.chart.cols as c}<th class={colState(c)} class:hi={snapStep?.hiCols?.includes(c)}>{c}</th>{/each}</tr>
                  </thead>
                  <tbody>
                    {#each qm.chart.rows as r}
                      {@const st = rowState(r)}
                      <tr class={st} class:hi={snapStep?.hiRow === r.id || snapStep?.removedRow === r.id}>
                        <th class="rl">{#if letters[r.id]}<em>{letters[r.id]}</em> {/if}{termText(r.bits, model.names)} <small class="dx-mono">{r.bits}</small>{#if st === 'picked'} ✔{/if}</th>
                        {#each qm.chart.cols as c}
                          <td class={colState(c)} class:hi={snapStep?.hiCols?.includes(c) && r.mins.includes(c)}>{r.mins.includes(c) ? '●' : ''}</td>
                        {/each}
                      </tr>
                    {/each}
                  </tbody>
                </table>
              </div>
              {#if step.kind === 'petrickPick' && step.candidates.length}
                <table class="dx-t cand">
                  <thead><tr><th>Phương án (tích Petrick)</th><th>Số hạng</th><th>Literal</th></tr></thead>
                  <tbody>{#each step.candidates as c, i}<tr class:best={i === 0}><td class="dx-mono">{c.label}</td><td>{c.cost[0]}</td><td>{c.cost[1]}</td></tr>{/each}</tbody>
                </table>
              {/if}
            </div>
          {/if}

          {#if showResult || (qm.result && at >= last)}
            <div class="dx-card res">
              <header><h5>SOP tối tiểu</h5><span>{qm.result.cost[0]} hạng · {qm.result.cost[1]} literal{qm.result.alternatives > 1 ? ` · ${qm.result.alternatives} phương án tối ưu` : ''}</span></header>
              <p class="final dx-mono">F = {qm.result.text}</p>
              <div class="dx-chips">{#each resultTerms as t}<span class="dx-chip">{termText(t, model.names)}<small class="dx-mono">{t}</small></span>{/each}</div>
              <p class="dx-k">{qm.result.verified ? '✓ Đã kiểm tra: phủ đủ mọi minterm bắt buộc và không phủ ô cấm.' : '✗ Kiểm tra thất bại.'}</p>
            </div>
          {/if}
        </div>

        {#if km}
          <div class="side">
            <div class="dx-card">
              <header><h5>So với K-map</h5><span>mỗi khoanh = một nguyên nhân nguyên tố</span></header>
              <svg viewBox="0 0 {KW} {KH}" class="dx-svg" role="img" aria-label="Bản đồ Karnaugh tương ứng">
                <text x={OX - 8} y="16" text-anchor="end" font-size="12" font-weight="700" fill="#0f437a">{km.layout.rowVars.map((i) => model.names[i]).join('')} \ {km.layout.colVars.map((i) => model.names[i]).join('')}</text>
                {#each km.cols as cv, c}<text x={OX + c * CS + CS / 2} y={OY - 8} text-anchor="middle" font-size="12" fill="#475569">{km.cells.find((x) => x.c === c).colGray}</text>{/each}
                {#each km.rows as rv, r}<text x={OX - 10} y={OY + r * CS + CS / 2 + 4} text-anchor="end" font-size="12" fill="#475569">{km.cells.find((x) => x.r === r).rowGray}</text>{/each}
                {#each km.cells as cell}
                  {@const [x, y] = cellXY(cell.r, cell.c)}
                  {@const v = model.values[cell.minterm]}
                  <rect {x} {y} width={CS} height={CS} fill={pairCells.r.has(cell.minterm) ? '#bbf7d0' : pairCells.a.has(cell.minterm) ? '#fde68a' : v === 1 ? '#ecfeff' : v === 2 ? '#f1f5f9' : '#fff'} stroke="#cbd5e1" />
                  <text x={x + CS / 2} y={y + CS / 2 + 5} text-anchor="middle" font-size="18" font-weight="700" fill={v === 1 ? '#0f766e' : v === 2 ? '#7c3aed' : '#94a3b8'}>{valAt(cell.minterm)}</text>
                  <text x={x + 4} y={y + 12} font-size="9" fill="#94a3b8">m{cell.minterm}</text>
                {/each}
                {#each primeRects as g (g.pr.id)}
                  {#each g.rects as rc}
                    {@const [x, y] = cellXY(rc.r0, rc.c0)}
                    <rect x={x + 3 + g.i % 3} y={y + 3 + g.i % 3} width={rc.w * CS - 6 - 2 * (g.i % 3)} height={rc.h * CS - 6 - 2 * (g.i % 3)} rx="9" fill="none" stroke={g.color}
                      stroke-width={g.state === 'faint' ? 1.8 : 3.6} stroke-dasharray={g.state === 'faint' ? '5 4' : ''} opacity={g.state === 'faint' ? 0.65 : 1} />
                  {/each}
                {/each}
                {#each hoverRects as rc}
                  {@const [x, y] = cellXY(rc.r0, rc.c0)}
                  <rect x={x + 1} y={y + 1} width={rc.w * CS - 2} height={rc.h * CS - 2} rx="8" fill="#f59e0b22" stroke="#f59e0b" stroke-width="3" />
                {/each}
              </svg>
              <p class="dx-k">Nét đứt = nguyên nhân nguyên tố; nét liền = đã chọn vào phủ. Rê chuột lên một mục ★ hoặc ô chip để thấy khoanh của nó. Mỗi phép dán ở bảng bên tương ứng việc nối hai ô kề nhau (khác đúng 1 bit).</p>
            </div>
          </div>
        {:else}
          <div class="side"><p class="dx-k">K-map chỉ vẽ cho 2–4 biến. Với {model.n} biến, lưới quá chật — đó chính là lý do cần bảng Quine–McCluskey.</p></div>
        {/if}
      </div>
    {/if}
  {/if}

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li>Chọn <em>F₁ (mục 5b)</em>, bấm tiếp đến hết cột 1: bạn thấy những cặp nào khác đúng một bit? Đối chiếu bảng trong bài.</li>
      <li>Chọn <em>có don't-care (mục 4)</em>: vì sao 0 và 7 giúp tạo nguyên tố lớn hơn nhưng không có cột trong bảng phủ?</li>
      <li>Chọn <em>Lõi vòng → Petrick</em>: bảng phủ không có cột nào chỉ một dấu ●; hãy dự đoán hai phương án 3 hạng trước khi bấm tiếp.</li>
      <li>Thử <em>Sáu biến</em> và để ý chỉ cần bảng — K-map 6 biến sẽ khó nhìn.</li>
      <li>Tự nhập biểu thức <code>a∧b ∨ a∧¬b∧c</code> và kiểm tra kết quả bằng K-map.</li>
    </ol>
  </details>
</div>

<style>
  .layout { display: grid; grid-template-columns: minmax(300px, 1.4fr) minmax(250px, 1fr); gap: 12px; align-items: start; }
  @media (max-width: 860px) { .layout { grid-template-columns: 1fr; } }
  .main, .side { display: flex; flex-direction: column; gap: 10px; min-width: 0; }
  .prog { height: 5px; background: #e2e8f0; border-radius: 4px; margin: -4px 0 8px; overflow: hidden; } .prog div { height: 100%; background: #0f766e; transition: width .25s; }
  .expl { font-size: .93rem; }
  .cols { display: flex; gap: 10px; overflow: auto; max-height: 440px; align-items: flex-start; padding-bottom: 4px; }
  .qt { min-width: 8.5rem; }
  .qt tr.gh td { background: #f1f5f9; color: #475569; font-size: .75rem; text-align: left; font-weight: 700; }
  .qt td.mn { text-align: left; } .qt td.ck { min-width: 2.2rem; color: #0f766e; font-weight: 700; }
  .qt tr.ha td { background: #fde68a; } .qt tr.hr td { background: #bbf7d0; }
  .qt tr.pr td { background: #f0fdf4; box-shadow: inset 0 0 0 0; } .qt tr.pr td.bt { border-left: 4px solid var(--pc); font-weight: 700; } .qt tr.pr td.ck b { color: #b45309; margin-left: 2px; }
  .qt tr.dco td.mn { color: #7c3aed; }
  .pchips { margin-top: 8px; } .pchip { border-width: 2px; }
  .scroll { overflow: auto; max-height: 360px; }
  .chart th.rl { text-align: left; white-space: nowrap; } .chart th.rl small { color: #64748b; margin-left: 4px; font-weight: 400; } .chart th.rl em { color: #7c3aed; font-style: normal; font-weight: 700; margin-right: 2px; }
  .chart td { min-width: 1.8rem; color: #0f766e; }
  .chart tr.picked th, .chart tr.picked td { background: #bbf7d0; } .chart tr.pet th, .chart tr.pet td { background: #ddd6fe; }
  .chart tr.gone th, .chart tr.gone td { color: #94a3b8; background: #f1f5f9; text-decoration: line-through; }
  .chart th.gone, .chart td.gone { background: #f1f5f9; color: #94a3b8; } .chart th.cov, .chart td.cov { background: #dcfce7; }
  .chart tr.hi th, .chart tr.hi td, .chart th.hi, .chart td.hi { background: #fde68a !important; }
  .cand { margin-top: 8px; } .cand tr.best td { background: #bbf7d0; font-weight: 700; }
  .res .final { font-size: 1.1rem; font-weight: 700; color: #0f437a; margin: 4px 0 8px; }
  .note { background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 6px 10px; color: #78350f; }
  .ctl button { white-space: nowrap; }
  .ex { margin-top: 10px; font-size: .9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
  p { margin: 6px 0; font-size: .9rem; }
</style>
