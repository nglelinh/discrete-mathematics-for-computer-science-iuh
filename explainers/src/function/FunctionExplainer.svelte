<script>
  import { analyze, inverse, compose, PRESETS } from './functions.js';

  let { preset = 'inj', focus = '' } = $props();
  const first = PRESETS.find((p) => p.id === preset) || PRESETS[0];

  let presetId = $state(first.id);
  let nx = $state(first.nx);
  let ny = $state(first.ny);
  let f = $state(first.f.slice());
  let nz = $state(4);
  let g = $state([1, 0, 3, 2, null, null]);
  let compMode = $state(focus === 'compose');
  let selX = $state(null);
  let selY = $state(null);

  const A = $derived(analyze(f, nx, ny));
  const inv = $derived(inverse(f, nx, ny));
  const fx = $derived(f.slice(0, nx));
  const gy = $derived(g.slice(0, ny).map((z) => (z !== null && z !== undefined && z < nz ? z : null)));
  const GA = $derived(analyze(gy, ny, nz));
  const gf = $derived(compose(gy, f, nx));
  const GFA = $derived(analyze(gf, nx, nz));

  const XS = 40, YS = 250, ZS = 460, TOP = 34, GAP = 44;
  const yPos = (i) => TOP + i * GAP;
  const height = $derived(TOP * 2 + Math.max(nx, ny, compMode ? nz : 0) * GAP - GAP / 2);

  function loadPreset(id) {
    const p = PRESETS.find((x) => x.id === id);
    if (!p) return;
    presetId = id; nx = p.nx; ny = p.ny; f = p.f.slice(); selX = null; selY = null;
  }
  function setSize(which, v) {
    v = Math.max(2, Math.min(7, Number(v) || 2));
    if (which === 'x') { nx = v; f = Array.from({ length: v }, (_, i) => (f[i] !== undefined && f[i] !== null && f[i] < ny ? f[i] : null)); }
    if (which === 'y') { ny = v; f = f.map((y) => (y !== null && y < v ? y : null)); }
    if (which === 'z') { nz = v; }
  }
  function clickX(x) { selX = selX === x ? null : x; selY = null; }
  function clickY(y) {
    if (selX === null) return;
    const nf = f.slice();
    nf[selX] = nf[selX] === y ? null : y;
    f = nf;
  }
  function clickYg(y) { selY = selY === y ? null : y; }
  function clickZ(z) {
    if (selY === null) return;
    const ng = g.slice();
    while (ng.length < 7) ng.push(null);
    ng[selY] = ng[selY] === z ? null : z;
    g = ng;
  }
  const collide = (y) => A.collisions.some((c) => c.y === y);
  const hasImage = (y) => A.preimage[y]?.length > 0;
  const xl = (x) => 'x' + (x + 1);
  const yl = (y) => 'y' + (y + 1);
  const zl = (z) => 'z' + (z + 1);
</script>

<div class="dx fex">
  <h4>Explainer hàm số: đơn ánh, toàn ánh, song ánh</h4>
  <p class="dx-help">
    Bấm một phần tử <strong>x</strong> (cột trái) rồi bấm phần tử <strong>y</strong> để vẽ/xóa mũi tên f(x) = y. Mỗi x chỉ có một mũi tên.
    Các tính chất được kiểm tra ngay, kèm <em>lý do cụ thể</em> khi sai.
  </p>

  <div class="dx-bar">
    <label>Mẫu
      <select value={presetId} onchange={(e) => loadPreset(e.currentTarget.value)}>
        {#each PRESETS as p}<option value={p.id}>{p.label}</option>{/each}
      </select>
    </label>
    <label>|X| <input type="number" min="2" max="7" value={nx} onchange={(e) => setSize('x', e.currentTarget.value)} style="width:4rem" /></label>
    <label>|Y| <input type="number" min="2" max="7" value={ny} onchange={(e) => setSize('y', e.currentTarget.value)} style="width:4rem" /></label>
    <button type="button" class="sec" class:on={compMode} onclick={() => (compMode = !compMode)}>Hợp thành g∘f</button>
    {#if compMode}<label>|Z| <input type="number" min="2" max="7" value={nz} onchange={(e) => setSize('z', e.currentTarget.value)} style="width:4rem" /></label>{/if}
  </div>

  <div class="body">
    <svg viewBox={`0 0 ${compMode ? 520 : 300} ${height}`} class="dx-svg" role="img" aria-label="Sơ đồ mũi tên của hàm">
      <defs>
        <marker id="farr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#334155" /></marker>
        <marker id="farr-r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#dc2626" /></marker>
        <marker id="farr-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#2563eb" /></marker>
      </defs>
      <text x={XS} y="16" text-anchor="middle" class="cap">X</text>
      <text x={YS} y="16" text-anchor="middle" class="cap">Y</text>
      {#if compMode}<text x={ZS} y="16" text-anchor="middle" class="cap">Z</text>{/if}
      {#each fx as y, x}
        {#if y !== null}
          <line x1={XS + 18} y1={yPos(x)} x2={YS - 20} y2={yPos(y)} stroke={collide(y) ? '#dc2626' : '#334155'} stroke-width={selX === x ? 3.5 : 2} marker-end={collide(y) ? 'url(#farr-r)' : 'url(#farr)'} />
        {/if}
      {/each}
      {#if compMode}
        {#each gy as z, y}
          {#if z !== null}<line x1={YS + 18} y1={yPos(y)} x2={ZS - 20} y2={yPos(z)} stroke="#2563eb" stroke-width={selY === y ? 3.5 : 2} marker-end="url(#farr-b)" />{/if}
        {/each}
      {/if}
      {#each Array(nx) as _, x}
        <g transform={`translate(${XS},${yPos(x)})`} class="nd" role="button" tabindex="0" onclick={() => clickX(x)} onkeydown={(e) => e.key === 'Enter' && clickX(x)}>
          <circle r="17" fill={f[x] === null ? '#fef9c3' : '#fff'} stroke={selX === x ? '#f59e0b' : '#334155'} stroke-width={selX === x ? 4 : 2} />
          <text y="5" text-anchor="middle" font-size="12" font-weight="700">{xl(x)}</text>
        </g>
      {/each}
      {#each Array(ny) as _, y}
        <g transform={`translate(${YS},${yPos(y)})`} class="nd" role="button" tabindex="0" onclick={() => (compMode && selX === null ? clickYg(y) : clickY(y))} onkeydown={(e) => e.key === 'Enter' && clickY(y)}>
          <circle r="17" fill={collide(y) ? '#fee2e2' : hasImage(y) ? '#dcfce7' : '#fff'} stroke={!hasImage(y) && A.wellDefined ? '#dc2626' : selY === y ? '#f59e0b' : '#334155'} stroke-width={selY === y ? 4 : 2} stroke-dasharray={!hasImage(y) ? '4 3' : null} />
          <text y="5" text-anchor="middle" font-size="12" font-weight="700">{yl(y)}</text>
        </g>
      {/each}
      {#if compMode}
        {#each Array(nz) as _, z}
          <g transform={`translate(${ZS},${yPos(z)})`} class="nd" role="button" tabindex="0" onclick={() => clickZ(z)} onkeydown={(e) => e.key === 'Enter' && clickZ(z)}>
            <circle r="17" fill="#fff" stroke="#2563eb" stroke-width="2" />
            <text y="5" text-anchor="middle" font-size="12" font-weight="700">{zl(z)}</text>
          </g>
        {/each}
      {/if}
    </svg>

    <div class="side">
      <div class="dx-card">
        <header><h5>Kết luận về f</h5><span>xanh = có tạo ảnh · đỏ = va chạm · nét đứt = không được "chạm" tới</span></header>
        <ul class="res">
          <li><span class={A.wellDefined ? 'dx-ok' : 'dx-bad'}>{A.wellDefined ? '✓' : '✗'}</span> <b>Là hàm</b> — {A.wellDefined ? 'mọi x đều có đúng một ảnh.' : `${A.unassigned.map(xl).join(', ')} chưa có mũi tên (cần đúng một).`}</li>
          <li><span class={A.injective ? 'dx-ok' : 'dx-bad'}>{A.injective ? '✓' : '✗'}</span> <b>Đơn ánh</b> — {A.injective ? 'hai x khác nhau luôn cho hai ảnh khác nhau.' : A.wellDefined ? `${A.collisions.map((c) => c.xs.map(xl).join(' và ') + ' cùng ↦ ' + yl(c.y)).join('; ')}.` : 'cần f là hàm trước.'}</li>
          <li><span class={A.surjective ? 'dx-ok' : 'dx-bad'}>{A.surjective ? '✓' : '✗'}</span> <b>Toàn ánh</b> — {A.surjective ? 'mọi y đều là ảnh của một x nào đó.' : A.wellDefined ? `${A.missed.map(yl).join(', ')} không có tạo ảnh.` : 'cần f là hàm trước.'}</li>
          <li><span class={A.bijective ? 'dx-ok' : 'dx-bad'}>{A.bijective ? '✓' : '✗'}</span> <b>Song ánh</b> — {A.bijective ? 'vừa đơn ánh vừa toàn ánh, nên có hàm ngược.' : 'cần cả đơn ánh và toàn ánh.'}</li>
        </ul>
        <p class="dx-k">Tập ảnh f(X) = {'{'}{A.image.map(yl).join(', ')}{'}'} · |f(X)| = {A.image.length}{#if A.wellDefined && nx > ny} · nx &gt; ny ⇒ không thể đơn ánh (chuồng bồ câu){/if}.</p>
        {#if A.bijective}
          <p><b>f⁻¹:</b> {inv.map((x, y) => `${yl(y)} ↦ ${xl(x)}`).join(', ')}</p>
        {:else if A.wellDefined}
          <p class="dx-k">Không có f⁻¹ vì f không phải song ánh.</p>
        {/if}
      </div>

      {#if compMode}
        <div class="dx-card">
          <header><h5>g ∘ f</h5><span>bấm y rồi z để vẽ g (mũi tên xanh)</span></header>
          <p class="mono">{gf.map((z, x) => `${xl(x)} ↦ ${f[x] === null ? '?' : yl(f[x])} ↦ ${z === null ? '?' : zl(z)}`).join('   ')}</p>
          <ul class="res">
            <li>f: {A.injective ? 'đơn ánh' : 'không đơn ánh'}, {A.surjective ? 'toàn ánh' : 'không toàn ánh'} · g: {GA.injective ? 'đơn ánh' : 'không đơn ánh'}, {GA.surjective ? 'toàn ánh' : 'không toàn ánh'}</li>
            <li>g∘f: <span class={GFA.injective ? 'dx-ok' : 'dx-bad'}>{GFA.injective ? 'đơn ánh' : 'không đơn ánh'}</span>, <span class={GFA.surjective ? 'dx-ok' : 'dx-bad'}>{GFA.surjective ? 'toàn ánh' : 'không toàn ánh'}</span></li>
            {#if A.injective && GA.injective}<li class="dx-ok">Đúng với định lý: f, g đơn ánh ⇒ g∘f đơn ánh.</li>{/if}
            {#if GFA.injective && A.wellDefined && !A.injective}<li class="dx-bad">Không thể xảy ra: g∘f đơn ánh thì f phải đơn ánh.</li>{/if}
            {#if GFA.surjective && GA.wellDefined && !GA.surjective}<li class="dx-bad">Không thể xảy ra: g∘f toàn ánh thì g phải toàn ánh.</li>{/if}
          </ul>
        </div>
      {/if}
    </div>
  </div>

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li>Chọn <em>Đơn ánh nhưng không toàn ánh</em>: tìm các y bị bỏ sót (nét đứt). Thêm mũi tên để làm nó thành song ánh — cần đổi |Y| không?</li>
      <li>Đặt |X| = 5, |Y| = 3 và cố vẽ một hàm đơn ánh. Vì sao không thể? (nguyên lý chuồng bồ câu)</li>
      <li>Chọn <em>x² mod 5</em>: nó không đơn ánh — chỉ ra cặp x gây va chạm. Chế độ <em>Hợp thành</em>: dựng g sao cho g∘f vẫn không đơn ánh.</li>
      <li>Với song ánh, đọc f⁻¹, rồi bật <em>Hợp thành</em> để thấy f⁻¹∘f là hàm đồng nhất.</li>
    </ol>
  </details>
</div>

<style>
  .body { display: grid; grid-template-columns: minmax(260px, 1fr) minmax(260px, 1fr); gap: 12px; align-items: start; }
  @media (max-width: 800px) { .body { grid-template-columns: 1fr; } }
  .cap { font-size: 14px; font-weight: 700; fill: #004586; }
  .nd { cursor: pointer; } .nd:focus { outline: none; }
  .side { display: grid; gap: 10px; }
  .res { margin: 0 0 6px; padding-left: 1.1rem; font-size: 0.9rem; display: grid; gap: 4px; }
  .mono { font-family: ui-monospace, Menlo, monospace; font-size: 0.82rem; margin: 0 0 6px; overflow-wrap: anywhere; }
  p { margin: 4px 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
