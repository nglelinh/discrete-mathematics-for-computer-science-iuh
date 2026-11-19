<script>
  import { easeCubicInOut } from 'd3-ease';
  import { interpolateNumber } from 'd3-interpolate';
  import { buildTimeline, totalSteps, stepIndex, cellOfStep, stepInfo, explainStep, rowSum, symmetryPairs, hockey, isOdd, oddCount, RATES } from './pascal.js';

  let { tab: tabProp = 'build', rows: rowsProp = 6, mode: modeProp = 'value', color: colorProp = 'none', k: kProp = 2, n: nProp = 5, autoplay = false } = $props();

  const clampN = (v) => Math.max(0, Math.min(14, Math.round(Number(v)) || 0));
  let tab = $state(['build', 'rowsum', 'sym', 'hockey'].includes(tabProp) ? tabProp : 'build');
  let N = $state(clampN(rowsProp));
  let mode = $state(modeProp === 'binom' ? 'binom' : 'value');
  let color = $state(colorProp === 'mod2' ? 'mod2' : 'none');
  let speed = $state(3);
  let time = $state(0);
  let target = $state(0);
  let playing = $state(false);
  let sel = $state(null);
  let selRow = $state(Math.min(clampN(rowsProp), 5));
  let hk = $state(Math.max(0, Number(kProp) || 0));
  let hn = $state(Math.max(0, Number(nProp) || 0));
  let auto = $state(autoplay);

  const TL = $derived(buildTimeline(N));
  const total = $derived(totalSteps(N));
  const T = $derived(tab === 'build' ? Math.min(time, total) : total);
  const info = $derived(stepInfo(T, total));
  const curStep = $derived(sel ? TL.steps[stepIndex(sel.r, sel.k)] : info.cs >= 0 ? TL.steps[info.cs] : null);
  const flying = $derived(tab === 'build' && !sel && info.cs >= 0 && info.cp < 1);
  const rowIdx = $derived(Math.min(selRow, N));
  const HN = $derived(Math.max(0, Math.min(hn, N - 1)));
  const HK = $derived(Math.max(0, Math.min(hk, HN)));
  const hk_ = $derived(N >= 1 ? hockey(HN, HK) : null);

  // ---- bố cục
  const CW = $derived(mode === 'binom' ? 62 : 42);
  const RH = 46;
  const BW = $derived(mode === 'binom' ? 58 : 38);
  const BH = 28;
  const W = $derived((N + 1) * CW + 30);
  const H = $derived((N + 1) * RH + 22);
  const px = (r, k) => W / 2 + (k - r / 2) * CW;
  const py = (r) => 26 + r * RH;

  const shown = (i) => (tab !== 'build' ? true : i < info.done || (info.cs === i && info.cp >= 0.85) || (info.cs >= 0 && i === info.cs && info.cp === 1));
  const label = (s) => (mode === 'binom' ? `C(${s.r},${s.k})` : String(s.v));
  const HUES = ['#0f766e', '#7c3aed', '#c2410c', '#0369a1', '#be185d', '#4d7c0f', '#b45309'];

  // ---- trạng thái tô màu mỗi ô
  function cellRole(s) {
    if (tab === 'build') {
      if (curStep && s.r === curStep.r && s.k === curStep.k) return 'child';
      if (curStep && curStep.parents.some((p) => p.r === s.r && p.k === s.k)) return 'parent';
    } else if (tab === 'rowsum') {
      if (s.r === rowIdx) return 'row';
    } else if (tab === 'sym') {
      if (s.r === rowIdx) return 'pair';
    } else if (tab === 'hockey' && hk_) {
      if (hk_.cells.some((c) => c.r === s.r && c.k === s.k)) return 'parent';
      if (s.r === hk_.target.r && s.k === hk_.target.k) return 'child';
    }
    if (sel && s.r === sel.r && s.k === sel.k) return 'child';
    return '';
  }
  const pairHue = (s) => HUES[Math.min(s.k, s.r - s.k) % HUES.length];

  // ---- bay giá trị: vị trí phần tử cha → ô con
  const ghosts = $derived.by(() => {
    if (!flying || !curStep) return [];
    const t = easeCubicInOut(Math.min(1, info.cp / 0.85));
    return curStep.parents.map((p, i) => {
      const cx = interpolateNumber(px(p.r, p.k), px(curStep.r, curStep.k))(t);
      const cy = interpolateNumber(py(p.r), py(curStep.r))(t);
      return { x: cx, y: cy, v: p.v, i, fade: info.cp > 0.8 ? Math.max(0, 1 - (info.cp - 0.8) / 0.05) : 1 };
    });
  });
  const lineOp = $derived(flying ? Math.min(1, info.cp * 4) * (info.cp > 0.85 ? 1 - (info.cp - 0.85) / 0.15 * 0.5 : 1) : 0.55);
  const pop = $derived(flying && info.cp >= 0.85 ? 1 + 0.25 * Math.sin(((info.cp - 0.85) / 0.15) * Math.PI) : 1);

  // ---- vòng lặp hoạt ảnh
  $effect(() => {
    if (!(playing || time !== target)) return;
    let raf = 0, last = performance.now();
    const tick = (now) => {
      const dt = Math.min(0.1, (now - last) / 1000);
      last = now;
      if (playing) target = total;
      if (time < target) time = Math.min(target, time + dt * RATES[speed - 1]);
      else if (time > target) time = target;
      if (playing && time >= total) playing = false;
      if (playing || time !== target) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  });
  $effect(() => { if (auto) { auto = false; tab = 'build'; time = 0; target = 0; playing = true; } });
  $effect(() => { if (time > total) { time = total; } if (target > total) target = total; });

  function play() { sel = null; tab = 'build'; if (time >= total) { time = 0; target = 0; } playing = !playing; if (!playing) target = time; }
  function fwd() { sel = null; tab = 'build'; playing = false; target = Math.min(total, Math.floor(time) + 1); }
  function back() { sel = null; playing = false; const f = Math.floor(time); const v = time > f ? f : Math.max(0, f - 1); time = v; target = v; }
  function reset() { sel = null; playing = false; time = 0; target = 0; }
  function nextRow() {
    sel = null; tab = 'build'; playing = false;
    const f = Math.floor(time);
    let e = total;
    for (let r = 0; r <= N; r++) { const x = totalSteps(r); if (x > f) { e = x; break; } }
    target = e;
  }
  function setN(v) { N = clampN(v); selRow = Math.min(selRow, N); }
  function clickCell(s) {
    if (!shown(stepIndex(s.r, s.k))) return;
    if (sel && sel.r === s.r && sel.k === s.k) { sel = null; return; }
    playing = false; target = time;
    sel = { r: s.r, k: s.k };
    if (tab === 'rowsum' || tab === 'sym') selRow = s.r;
    if (tab === 'hockey') { hk = s.k; hn = Math.min(Math.max(s.r, s.k), Math.max(0, N - 1)); }
  }
  const sumText = (arr) => arr.map(String).join(' + ');
  const altText = (arr) => arr.map((v, i) => (i === 0 ? String(v) : `${i % 2 ? '−' : '+'} ${v}`)).join(' ');
  const rs = $derived(rowSum(rowIdx));
  const sp = $derived(symmetryPairs(rowIdx));
  const buildDone = $derived(Math.min(N, Math.max(0, info.cs >= 0 ? TL.steps[info.cs].r : -1)));
  const subtitle = $derived(`Đã dựng ${info.cs >= 0 ? TL.steps[info.cs].r + 1 : 0} / ${N + 1} hàng · ô ${Math.min(info.done + (info.cp < 1 ? 1 : 0), total)} / ${total}`);
</script>

<div class="dx pex">
  <h4>Tam giác Pascal: cộng từ đỉnh xuống</h4>
  <p class="dx-help">
    Mỗi ô bằng <b>tổng hai ô ngay phía trên</b> (ô ở mép chỉ có một ô cha và luôn bằng 1). Bấm <b>Play</b> để xem từng giá trị trượt xuống và cộng lại,
    hoặc <b>Bước tiếp</b> để đi từng ô. Bấm một ô đã hiện để xem hai ô cha của nó.
  </p>

  <div class="dx-tabs">
    <button type="button" class="sec" class:on={tab === 'build'} onclick={() => { tab = 'build'; sel = null; }}>Xây từ đỉnh xuống</button>
    <button type="button" class="sec" class:on={tab === 'rowsum'} onclick={() => { tab = 'rowsum'; playing = false; target = time; }}>Tổng hàng 2ⁿ</button>
    <button type="button" class="sec" class:on={tab === 'sym'} onclick={() => { tab = 'sym'; playing = false; target = time; }}>Đối xứng</button>
    <button type="button" class="sec" class:on={tab === 'hockey'} onclick={() => { tab = 'hockey'; playing = false; target = time; }}>Cây gậy khúc côn cầu</button>
  </div>

  {#if tab === 'build'}
    <div class="dx-bar ctl">
      <button type="button" class="sec" onclick={reset} aria-label="Về đầu">⏮ Về đầu</button>
      <button type="button" class="sec" onclick={back} disabled={time <= 0}>◀ Lùi</button>
      <button type="button" onclick={play}>{playing ? '⏸ Dừng' : '▶ Play'}</button>
      <button type="button" class="sec" onclick={fwd} disabled={time >= total}>Bước tiếp ▶</button>
      <button type="button" class="sec" onclick={nextRow} disabled={time >= total}>Hàng tiếp ⏭</button>
    </div>
  {/if}
  <div class="dx-bar">
    <label>Số hàng (n = 0…{N})
      <input type="range" min="0" max="14" value={N} oninput={(e) => setN(e.currentTarget.value)} />
      <b>{N}</b>
    </label>
    {#if tab === 'build'}
      <label>Tốc độ <input type="range" min="1" max="5" bind:value={speed} /></label>
    {/if}
    <label>Hiển thị
      <select bind:value={mode}><option value="value">Giá trị</option><option value="binom">C(n,k)</option></select>
    </label>
    <label>Tô màu
      <select bind:value={color}><option value="none">Không</option><option value="mod2">Chẵn / lẻ (mod 2)</option></select>
    </label>
  </div>

  {#if tab === 'rowsum' || tab === 'sym'}
    <div class="dx-bar"><label>Hàng n = <input type="range" min="0" max={N} value={rowIdx} oninput={(e) => { selRow = Number(e.currentTarget.value); sel = null; }} /> <b>{rowIdx}</b></label></div>
  {/if}
  {#if tab === 'hockey'}
    <div class="dx-bar">
      <label>k = <input type="number" min="0" max={Math.max(0, N - 1)} value={HK} oninput={(e) => (hk = Number(e.currentTarget.value) || 0)} style="width:4rem" /></label>
      <label>n = <input type="number" min="0" max={Math.max(0, N - 1)} value={HN} oninput={(e) => (hn = Number(e.currentTarget.value) || 0)} style="width:4rem" /></label>
      <span class="dx-k">(n phải ≥ k và ≤ {Math.max(0, N - 1)}; tăng số hàng nếu cần)</span>
    </div>
  {/if}

  <div class="msg dx-msg" aria-live="polite">
    {#if tab === 'build'}
      {#if curStep && curStep.parents.length === 2}
        <span class="eq"><b class="pa">{curStep.parents[0].v}</b> + <b class="pb">{curStep.parents[1].v}</b> = <b class="pc">{flying && info.cp < 0.85 ? '?' : curStep.v}</b></span>
      {:else if curStep}
        <span class="eq"><b class="pa">{curStep.parents[0]?.v ?? ''}</b>{curStep.parents.length ? ' → ' : ''}<b class="pc">{curStep.v}</b></span>
      {/if}
      {sel ? `(đang xem ô đã chọn) ` : ''}{flying && info.cp < 0.85 && curStep ? (curStep.parents.length === 2 ? `Hàng ${curStep.r}, ô ${curStep.k}: hai ô cha ${curStep.parents[0].v} và ${curStep.parents[1].v} đang trượt xuống để cộng lại…` : `Hàng ${curStep.r}, ô ${curStep.k}: ô cha duy nhất đang trượt xuống…`) : explainStep(curStep)}
      <span class="dx-k"> {subtitle}</span>
    {:else if tab === 'rowsum'}
      <b>Hàng n = {rowIdx}:</b> {sumText(rs.row)} = <b>{rs.sum}</b> = 2<sup>{rowIdx}</sup>.
      {#if rowIdx >= 1}<br />Tổng xen kẽ: {altText(rs.row)} = <b>{rs.alt}</b> (vì (1 − 1)ⁿ = 0).{/if}
      <br /><span class="dx-k">Mỗi hàng gấp đôi hàng trên: 2ⁿ = 2·2ⁿ⁻¹, vì mỗi ô con nhận giá trị từ hai ô cha — mỗi ô cha được dùng đúng hai lần.</span>
    {:else if tab === 'sym'}
      <b>Hàng n = {rowIdx}:</b> C(n,k) = C(n,n−k).
      {#each sp as p}<span class="pair" style={`border-color:${HUES[p.k % HUES.length]}`}>{p.self ? `C(${rowIdx},${p.k})` : `C(${rowIdx},${p.k}) = C(${rowIdx},${p.mirror})`} = <b>{p.v}</b></span>{/each}
      <br /><span class="dx-k">Chọn k người ở lại ⇔ chọn n−k người ra về: hai cách đếm cho cùng một số.</span>
    {:else if tab === 'hockey'}
      {#if hk_}
        <b>Σ<sub>i={HK}…{HN}</sub> C(i,{HK}) = C({HN + 1},{HK + 1})</b><br />
        {hk_.cells.map((c) => `C(${c.r},${HK})`).join(' + ')} = {sumText(hk_.cells.map((c) => c.v))} = <b>{hk_.sum}</b> = C({HN + 1},{HK + 1}) {hk_.sum === hk_.target.v ? '✓' : '✗'}
        <br /><span class="dx-k">Các ô vàng nằm dọc một đường chéo (cán gậy); ô xanh lục ở ngay phía dưới-bên cạnh là "lưỡi gậy" bằng tổng.</span>
      {:else}Tăng số hàng lên ít nhất 1 để thử.{/if}
    {/if}
    {#if color === 'mod2'}
      <br /><span class="dx-k">Ô lẻ (đậm) tạo thành tam giác Sierpiński{rowIdx >= 0 && tab !== 'build' ? `; hàng ${rowIdx} có ${oddCount(rowIdx)} ô lẻ = 2^(số bit 1 của ${rowIdx})` : ''}.</span>
    {/if}
  </div>

  <svg viewBox="0 0 {W} {H}" class="dx-svg ptri" role="img" aria-label="Tam giác Pascal">
    <!-- mốc hàng -->
    {#each Array.from({ length: N + 1 }, (_, r) => r) as r}
      <text x="4" y={py(r) + 4} font-size="10" fill="#94a3b8">n={r}</text>
    {/each}
    <!-- đường nối cha → con -->
    {#if curStep && (tab === 'build' || sel)}
      {#each curStep.parents as p}
        <line x1={px(p.r, p.k)} y1={py(p.r) + BH / 2} x2={px(curStep.r, curStep.k)} y2={py(curStep.r) - BH / 2} stroke="#f59e0b" stroke-width="3" opacity={lineOp} stroke-linecap="round" />
      {/each}
    {/if}
    {#if tab === 'sym'}
      {#each sp.filter((p) => !p.self) as p}
        <path d={`M ${px(rowIdx, p.k)} ${py(rowIdx) + BH / 2 + 2} Q ${W / 2} ${py(rowIdx) + BH / 2 + 8 + (rowIdx - 2 * p.k) * 5} ${px(rowIdx, p.mirror)} ${py(rowIdx) + BH / 2 + 2}`} fill="none" stroke={HUES[p.k % HUES.length]} stroke-width="2.5" />
      {/each}
      <line x1={W / 2} y1="10" x2={W / 2} y2={H - 8} stroke="#94a3b8" stroke-dasharray="4 4" />
    {/if}
    <!-- ô -->
    {#each TL.steps as s (s.r + '-' + s.k)}
      {@const i = stepIndex(s.r, s.k)}
      {@const vis = shown(i)}
      {@const role = cellRole(s)}
      {@const odd = color === 'mod2' && isOdd(s.r, s.k)}
      <g class="cell" class:vis role="button" tabindex={vis ? 0 : -1} aria-label={`C(${s.r},${s.k}) = ${s.v}`}
        transform={`translate(${px(s.r, s.k)},${py(s.r)}) scale(${role === 'child' && flying && info.cs === i ? pop : 1})`}
        onclick={() => clickCell(s)} onkeydown={(e) => (e.key === 'Enter' || e.key === ' ') && clickCell(s)}>
        <rect x={-BW / 2} y={-BH / 2} width={BW} height={BH} rx="8"
          fill={!vis ? '#f8fafc' : role === 'child' ? '#bbf7d0' : role === 'parent' ? '#fde68a' : role === 'row' ? '#ccfbf1' : role === 'pair' ? '#ede9fe' : odd ? '#0f766e' : '#fff'}
          stroke={role === 'child' ? '#15803d' : role === 'parent' ? '#d97706' : role === 'pair' ? pairHue(s) : !vis ? '#e2e8f0' : '#94a3b8'}
          stroke-width={role ? 2.6 : 1.4} stroke-dasharray={vis ? '' : '3 3'} />
        {#if vis}
          <text y="4.5" text-anchor="middle" font-size={mode === 'binom' ? 11 : s.v >= 1000n ? 11 : 13} font-weight="700" fill={odd && !role ? '#fff' : '#0f172a'}
            opacity={tab === 'build' && info.cs === i && info.cp < 1 ? Math.max(0, (info.cp - 0.85) / 0.15) : 1}>{label(s)}</text>
        {/if}
      </g>
    {/each}
    <!-- giá trị đang trượt xuống -->
    {#each ghosts as g (g.i)}
      <g transform={`translate(${g.x},${g.y})`} opacity={g.fade} pointer-events="none">
        <rect x={-BW / 2 + 3} y={-BH / 2 + 3} width={BW - 6} height={BH - 6} rx="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5" />
        <text y="4.5" text-anchor="middle" font-size="12.5" font-weight="800" fill="#fff">{g.v}</text>
      </g>
    {/each}
  </svg>

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li>Đặt số hàng = 5 và bấm <b>Bước tiếp</b>: ở hàng 4, dự đoán 6 = 3 + 3 trước khi ô hiện ra.</li>
      <li>Vì sao hai ô ở mép luôn là 1? Bấm ô mép và đọc giải thích (chỉ có một ô cha).</li>
      <li>Thẻ <b>Tổng hàng</b>: kéo n từ 0 đến 10 và nhận ra tổng gấp đôi sau mỗi hàng.</li>
      <li>Thẻ <b>Đối xứng</b>: chọn n lẻ rồi n chẵn — ô giữa chỉ có khi n chẵn.</li>
      <li>Thẻ <b>Cây gậy khúc côn cầu</b>: k = 2, n = 5 cho 1 + 3 + 6 + 10 = 20 = C(6,3); thử k = 1.</li>
      <li>Tô màu <b>mod 2</b> với 14 hàng: nhận ra hình Sierpiński.</li>
    </ol>
  </details>
</div>

<style>
  .msg { line-height: 1.55; }
  .eq { display: inline-block; font-size: 1.15rem; margin-right: 8px; padding: 1px 8px; background: #fff; border-radius: 8px; border: 1px solid #bae6fd; }
  .eq .pa, .eq .pb { color: #b45309; } .eq .pc { color: #15803d; }
  .pair { display: inline-block; margin: 2px 6px 2px 0; padding: 0 6px; border-left: 4px solid; background: #fff; border-radius: 4px; font-size: .86rem; }
  .ptri { max-height: 640px; touch-action: manipulation; }
  .cell.vis { cursor: pointer; } .cell:focus { outline: none; }
  .ctl button { white-space: nowrap; }
  input[type=range] { vertical-align: middle; max-width: 9rem; }
  .ex { margin-top: 10px; font-size: .9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
  p { margin: 6px 0; font-size: .9rem; }
  @media (max-width: 520px) { .ctl button { padding: 7px 9px; font-size: .85rem; } }
</style>
