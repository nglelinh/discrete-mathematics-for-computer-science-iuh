<script>
  import {
    makeMatrix, cloneM, properties, reflexiveClosure, symmetricClosure, warshallSteps,
    equivalenceClasses, hasse, PRESETS
  } from './relations.js';

  let { preset = 'mod2', focus = '' } = $props();

  const first = PRESETS.find((p) => p.id === preset) || PRESETS[0];
  let presetId = $state(first.id);
  let labels = $state(first.labels.slice());
  let M = $state(makeMatrix(first.labels.length, first.f));
  let witnessKey = $state(null);
  let wk = $state(focus === 'warshall' ? 0 : null); // null = đang xem R; số = W_k
  let pending = $state(null);
  let flash = $state([]);
  let note = $state('');

  const n = $derived(M.length);
  const P = $derived(properties(M, labels));
  const steps = $derived(warshallSteps(M));
  const view = $derived(wk === null ? M : steps[Math.min(wk, steps.length - 1)].M);
  const addedNow = $derived(wk === null ? flash : steps[Math.min(wk, steps.length - 1)].added);
  const witness = $derived(witnessKey && P[witnessKey] && !P[witnessKey].ok ? P[witnessKey].witness : null);
  const classes = $derived(P.equivalence.ok ? equivalenceClasses(M) : []);
  const H = $derived(P.partialOrder.ok ? hasse(M) : null);
  const classOf = $derived.by(() => {
    const c = new Array(n).fill(-1);
    classes.forEach((cl, i) => cl.forEach((x) => (c[x] = i)));
    return c;
  });
  const PAL = ['#2563eb', '#ea580c', '#16a34a', '#9333ea', '#db2777', '#0891b2'];

  const R = 112, CX = 160, CY = 150;
  const pt = (i) => {
    const a = (-Math.PI / 2) + (2 * Math.PI * i) / n;
    return { x: CX + R * Math.cos(a), y: CY + R * Math.sin(a) };
  };
  function edgePath(i, j) {
    const a = pt(i), b = pt(j);
    if (i === j) {
      const dx = a.x - CX, dy = a.y - CY, len = Math.hypot(dx, dy) || 1;
      const ux = dx / len, uy = dy / len;
      const cx = a.x + ux * 30, cy = a.y + uy * 30;
      return { d: `M ${a.x + ux * 14 - uy * 8} ${a.y + uy * 14 + ux * 8} C ${cx - uy * 24} ${cy + ux * 24}, ${cx + uy * 24} ${cy - ux * 24}, ${a.x + ux * 14 + uy * 8} ${a.y + uy * 14 - ux * 8}` };
    }
    const dx = b.x - a.x, dy = b.y - a.y, len = Math.hypot(dx, dy);
    const ux = dx / len, uy = dy / len;
    const sx = a.x + ux * 17, sy = a.y + uy * 17, ex = b.x - ux * 19, ey = b.y - uy * 19;
    const both = view[j][i];
    const off = both ? 16 : 0;
    const mx = (sx + ex) / 2 - uy * off, my = (sy + ey) / 2 + ux * off;
    return { d: `M ${sx} ${sy} Q ${mx} ${my} ${ex} ${ey}` };
  }
  const edges = $derived.by(() => {
    const out = [];
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) if (view[i][j]) out.push({ i, j, ...edgePath(i, j) });
    return out;
  });
  const isIn = (list, i, j) => list.some(([a, b]) => a === i && b === j);

  function loadPreset(id) {
    const p = PRESETS.find((x) => x.id === id);
    if (!p) return;
    presetId = id; labels = p.labels.slice(); M = makeMatrix(p.labels.length, p.f);
    witnessKey = null; wk = null; flash = []; note = ''; pending = null;
  }
  function resize(d) {
    const m = n + d;
    if (m < 2 || m > 6) return;
    const base = 'abcdef';
    const N = makeMatrix(m, (i, j) => (i < n && j < n ? M[i][j] : false));
    if (d > 0) labels = [...labels, String.fromCharCode(97 + labels.length)];
    else labels = labels.slice(0, m);
    M = N; wk = null; witnessKey = null; flash = []; pending = null;
  }
  function toggle(i, j) {
    if (wk !== null) return;
    const N = cloneM(M); N[i][j] = !N[i][j]; M = N; flash = []; note = '';
  }
  function clickNode(i) {
    if (wk !== null) return;
    if (pending === null) pending = i;
    else { toggle(pending, i); pending = null; }
  }
  function closure(kind) {
    wk = null;
    const r = kind === 'ref' ? reflexiveClosure(M) : symmetricClosure(M);
    M = r.R; flash = r.added;
    note = r.added.length ? `Đã thêm ${r.added.length} cặp: ${r.added.map(([i, j]) => `(${labels[i]}, ${labels[j]})`).join(', ')}.` : 'Quan hệ đã có tính chất này — không cần thêm cặp nào.';
  }
  function applyWarshall() {
    const s = steps[steps.length - 1];
    const cnt = s.M.flat().filter(Boolean).length - M.flat().filter(Boolean).length;
    M = cloneM(s.M); wk = null; flash = [];
    note = cnt ? `Đã áp dụng bao đóng bắc cầu: thêm ${cnt} cặp.` : 'Quan hệ đã bắc cầu.';
  }
  const names = { reflexive: 'Phản xạ', irreflexive: 'Bất phản xạ', symmetric: 'Đối xứng', antisymmetric: 'Phản đối xứng', asymmetric: 'Bất đối xứng', transitive: 'Bắc cầu' };
  const lvlCount = $derived(H ? Math.max(...H.level) + 1 : 0);
  const hp = (i) => {
    const lv = H.level[i];
    const same = [...Array(n).keys()].filter((x) => H.level[x] === lv);
    const idx = same.indexOf(i);
    return { x: 20 + ((idx + 1) * 280) / (same.length + 1), y: 20 + (lvlCount - 1 - lv) * (Math.min(60, 200 / Math.max(1, lvlCount - 1 || 1))) };
  };
</script>

<div class="dx rex">
  <h4>Explainer quan hệ hai ngôi</h4>
  <p class="dx-help">
    Cùng một quan hệ được xem ba cách: <strong>ma trận</strong>, <strong>đồ thị có hướng</strong> và <strong>danh sách tính chất</strong>.
    Bấm ô ma trận (hoặc bấm lần lượt hai đỉnh) để thêm/bớt cặp. Bấm một tính chất bị sai để thấy <em>phản ví dụ</em> được tô đỏ.
  </p>

  <div class="dx-bar">
    <label>Mẫu
      <select value={presetId} onchange={(e) => loadPreset(e.currentTarget.value)}>
        {#each PRESETS as p}<option value={p.id}>{p.label}</option>{/each}
      </select>
    </label>
    <button type="button" class="sec" onclick={() => resize(-1)} disabled={n <= 2}>− phần tử</button>
    <button type="button" class="sec" onclick={() => resize(1)} disabled={n >= 6}>+ phần tử</button>
    <button type="button" class="sec" onclick={() => closure('ref')}>Bao đóng phản xạ</button>
    <button type="button" class="sec" onclick={() => closure('sym')}>Bao đóng đối xứng</button>
    <button type="button" class="sec" class:on={wk !== null} onclick={() => (wk = wk === null ? 0 : null)}>Warshall từng bước</button>
  </div>

  {#if wk !== null}
    <div class="dx-bar ws">
      <button type="button" class="sec" disabled={wk <= 0} onclick={() => (wk = Math.max(0, wk - 1))}>◀</button>
      <span>W<sub>{wk}</sub>{wk === 0 ? ' = R (ma trận ban đầu)' : ` — cho phép đi qua đỉnh trung gian ${labels.slice(0, wk).join(', ')}`}</span>
      <button type="button" class="sec" disabled={wk >= n} onclick={() => (wk = Math.min(n, wk + 1))}>▶</button>
      <button type="button" onclick={applyWarshall}>Dùng bao đóng bắc cầu</button>
    </div>
    <p class="dx-msg">
      {#if wk === 0}Bắt đầu: W₀ = R. Bước k xét đỉnh trung gian thứ k: nếu <b>i → k</b> và <b>k → j</b> thì thêm <b>i → j</b>.
      {:else if addedNow.length}Qua đỉnh <b>{labels[wk - 1]}</b> thêm: {addedNow.map(([i, j]) => `(${labels[i]}, ${labels[j]})`).join(', ')} (ô xanh).
      {:else}Qua đỉnh <b>{labels[wk - 1]}</b> không thêm cặp mới nào.{/if}
    </p>
  {:else if note}
    <p class="dx-msg">{note}</p>
  {/if}

  <div class="cols">
    <div class="dx-card">
      <header><h5>Ma trận {wk === null ? 'R' : `W${wk}`}</h5><span>{wk === null ? 'bấm ô để đổi' : 'chỉ xem'}</span></header>
      <table class="dx-t mat">
        <thead><tr><th></th>{#each labels as l}<th>{l}</th>{/each}</tr></thead>
        <tbody>
          {#each view as row, i}
            <tr>
              <th>{labels[i]}</th>
              {#each row as v, j}
                <td>
                  <button type="button" class="cell" class:one={v} class:add={isIn(addedNow, i, j)} class:bad={witness && isIn(witness.cells, i, j)} onclick={() => toggle(i, j)}>{v ? 1 : 0}</button>
                </td>
              {/each}
            </tr>
          {/each}
        </tbody>
      </table>
    </div>

    <div class="dx-card">
      <header><h5>Đồ thị có hướng</h5><span>{pending !== null ? `đã chọn ${labels[pending]} — bấm đỉnh đích` : 'bấm 2 đỉnh để nối'}</span></header>
      <svg viewBox="0 0 320 300" class="dx-svg" role="img" aria-label="Đồ thị có hướng của quan hệ">
        <defs>
          <marker id="rarr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#475569" /></marker>
          <marker id="rarr-g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#16a34a" /></marker>
          <marker id="rarr-r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#dc2626" /></marker>
        </defs>
        {#each edges as e (e.i + '-' + e.j)}
          {@const bad = witness && isIn(witness.cells, e.i, e.j)}
          {@const add = isIn(addedNow, e.i, e.j)}
          <path d={e.d} fill="none" stroke={bad ? '#dc2626' : add ? '#16a34a' : '#475569'} stroke-width={bad || add ? 3 : 1.8} marker-end={`url(#${bad ? 'rarr-r' : add ? 'rarr-g' : 'rarr'})`} />
        {/each}
        {#each labels as l, i}
          {@const p = pt(i)}
          <g transform={`translate(${p.x},${p.y})`} class="nd" role="button" tabindex="0" onclick={() => clickNode(i)} onkeydown={(e) => e.key === 'Enter' && clickNode(i)}>
            <circle r="16" fill={classes.length ? PAL[classOf[i] % PAL.length] + '33' : '#fff'} stroke={pending === i ? '#f59e0b' : classes.length ? PAL[classOf[i] % PAL.length] : '#334155'} stroke-width={pending === i ? 4 : 2.2} />
            <text y="5" text-anchor="middle" font-size="13" font-weight="700">{l}</text>
          </g>
        {/each}
      </svg>
    </div>

    <div class="dx-card">
      <header><h5>Tính chất của R</h5><span>bấm ✗ để xem phản ví dụ</span></header>
      <ul class="props">
        {#each Object.keys(names) as key}
          <li>
            <button type="button" class="sec pr" class:sel={witnessKey === key} onclick={() => (witnessKey = witnessKey === key ? null : key)}>
              <span class={P[key].ok ? 'dx-ok' : 'dx-bad'}>{P[key].ok ? '✓' : '✗'}</span> {names[key]}
            </button>
          </li>
        {/each}
      </ul>
      {#if witness}<p class="dx-msg">{witness.msg}</p>{:else if witnessKey}<p class="dx-msg">Tính chất này đúng — không có phản ví dụ.</p>{/if}
      <p class="verdict">
        {#if P.equivalence.ok}<span class="dx-ok">Quan hệ tương đương</span> (phản xạ + đối xứng + bắc cầu).
        {:else if P.partialOrder.ok}<span class="dx-ok">Thứ tự riêng phần</span> (phản xạ + phản đối xứng + bắc cầu).
        {:else}Chưa phải quan hệ tương đương hay thứ tự riêng phần.{/if}
      </p>
    </div>
  </div>

  {#if classes.length}
    <div class="dx-card extra">
      <header><h5>Các lớp tương đương</h5><span>{classes.length} lớp — chia tập thành các khối rời nhau</span></header>
      <div class="dx-chips">
        {#each classes as cl, i}
          <span class="dx-chip" style={`border-color:${PAL[i % PAL.length]}`}>[{labels[cl[0]]}] = {'{'}{cl.map((x) => labels[x]).join(', ')}{'}'}</span>
        {/each}
      </div>
    </div>
  {/if}
  {#if H}
    <div class="dx-card extra">
      <header><h5>Sơ đồ Hasse</h5><span>bỏ khuyên và các cạnh suy ra từ bắc cầu</span></header>
      <svg viewBox="0 0 320 {40 + Math.max(0, lvlCount - 1) * 60 + 20}" class="dx-svg" role="img" aria-label="Sơ đồ Hasse">
        {#each H.cover as [a, b]}
          <line x1={hp(a).x} y1={hp(a).y} x2={hp(b).x} y2={hp(b).y} stroke="#475569" stroke-width="2" />
        {/each}
        {#each labels as l, i}
          <g transform={`translate(${hp(i).x},${hp(i).y})`}>
            <circle r="15" fill={H.minimal.includes(i) ? '#dcfce7' : H.maximal.includes(i) ? '#fee2e2' : '#fff'} stroke="#334155" stroke-width="2" />
            <text y="5" text-anchor="middle" font-size="13" font-weight="700">{l}</text>
          </g>
        {/each}
      </svg>
      <p class="dx-k">Xanh = phần tử cực tiểu ({H.minimal.map((x) => labels[x]).join(', ')}) · Đỏ = cực đại ({H.maximal.map((x) => labels[x]).join(', ')}).</p>
    </div>
  {/if}

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li>Chọn mẫu <em>Đồng dư mod 2</em>: kiểm tra ba tính chất rồi xem các lớp tương đương. Thử bỏ một cặp — tính chất nào hỏng đầu tiên?</li>
      <li>Chọn <em>Kế tiếp i → i+1</em>: nó chưa bắc cầu. Bấm <em>Warshall từng bước</em> và dự đoán cặp nào được thêm ở mỗi bước.</li>
      <li>Chọn <em>Ước số</em>: đọc sơ đồ Hasse, chỉ ra phần tử cực tiểu/cực đại và hai phần tử không so sánh được.</li>
      <li>Chọn <em>Bạn bè</em>: nó đối xứng nhưng không bắc cầu — dùng bao đóng để "sửa" rồi xem tính chất nào còn lại.</li>
    </ol>
  </details>
</div>

<style>
  .cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px; }
  .extra { margin-top: 12px; }
  .ws { background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 6px 8px; }
  .mat th { width: 2rem; }
  .cell { min-width: 1.9rem; padding: 3px 0 !important; background: #fff !important; color: #64748b !important; border-color: #e2e8f0 !important; border-radius: 4px !important; }
  .cell.one { background: #0f766e !important; color: #fff !important; border-color: #0f766e !important; }
  .cell.add { background: #16a34a !important; color: #fff !important; box-shadow: 0 0 0 2px #bbf7d0; }
  .cell.bad { background: #dc2626 !important; color: #fff !important; box-shadow: 0 0 0 2px #fecaca; }
  .nd { cursor: pointer; } .nd:focus { outline: none; }
  .props { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }
  .pr { width: 100%; text-align: left; } .pr.sel { box-shadow: 0 0 0 2px #38bdf8; }
  .verdict { margin: 8px 0 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
