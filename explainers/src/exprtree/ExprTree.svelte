<script>
  import { parse, collectVars, layout, flatten, evaluateTree } from './parser.js';

  let { formula = '((p ∨ q) → ¬r) ↔ p' } = $props();
  const PRESETS = [
    ['((p ∨ q) → ¬r) ↔ p', 'Ví dụ trong bài'],
    ['¬(p ∧ q) ↔ (¬p ∨ ¬q)', 'De Morgan'],
    ['p ∨ (q ∧ r)', 'Phân phối (vế trái)'],
    ['p → q → r', '→ kết hợp phải'],
    ['p ∨ ¬p', 'Luật bù']
  ];
  const OPS = ['¬', '∧', '∨', '→', '↔'];
  const OP_NAME = { '¬': 'phủ định', '∧': 'và', '∨': 'hoặc', '→': 'kéo theo', '↔': 'tương đương' };

  let text = $state(formula);
  let inputEl;
  let env = $state({});
  let step = $state(null); // null: hiện đủ; số: đã tính step nút đầu của thứ tự hậu tự

  const parsed = $derived.by(() => {
    try { return { ast: parse(text), err: '' }; } catch (e) { return { ast: null, err: e.message }; }
  });
  // Giữ lại cây cuối cùng hợp lệ để khung vẽ không nhảy khi đang gõ dở.
  let last = $state(null);
  $effect(() => { if (parsed.ast) last = parsed.ast; });
  const ast = $derived(parsed.ast ?? last);
  const vars = $derived(ast ? collectVars(ast) : []);
  const lay = $derived(ast ? layout(ast) : null);
  const nodes = $derived(lay ? flatten(lay.root) : []);
  const ev = $derived(lay ? evaluateTree(lay.root, Object.fromEntries(vars.map((v) => [v, env[v] ?? true]))) : null);
  const shown = $derived.by(() => {
    if (!ev) return new Set();
    if (step === null) return new Set(ev.order);
    return new Set(ev.order.slice(0, step));
  });
  $effect(() => { parsed.ast; step = null; });

  const DX = 74, DY = 78, PADX = 40, PADY = 34;
  const W = $derived(lay ? Math.max(260, (lay.leaves - 1) * DX + PADX * 2) : 260);
  const H = $derived(lay ? lay.depth * DY + PADY * 2 + 22 : 120);
  const px = (n) => PADX + n.x * DX;
  const py = (n) => PADY + n.depth * DY;

  const total = $derived(ev ? ev.order.length : 0);
  const stale = $derived(!!parsed.err);
  const rootVal = $derived(ev && shown.has(lay.root.id) ? ev.val[lay.root.id] : null);

  function insert(s) {
    const el = inputEl;
    const a = el?.selectionStart ?? text.length, b = el?.selectionEnd ?? text.length;
    text = text.slice(0, a) + s + text.slice(b);
    queueMicrotask(() => { el?.focus(); el?.setSelectionRange(a + s.length, a + s.length); });
  }
  const setVar = (v, val) => { env = { ...env, [v]: val }; };
  const nextStep = () => { step = step === null ? 1 : Math.min(total, step + 1); };
  const label = (n) => (n.type === 'var' ? n.name : n.type === 'const' ? (n.value ? 'T' : 'F') : n.op);
  const fill = (n) => {
    if (!shown.has(n.id)) return 'var(--et-idle)';
    return ev.val[n.id] ? 'var(--et-true)' : 'var(--et-false)';
  };
  const cur = (n) => step !== null && step > 0 && ev.order[step - 1] === n.id;

  const msg = $derived.by(() => {
    if (!ev) return '';
    if (step === null) return `Giá trị của cả công thức: ${ev.val[lay.root.id] ? 'Đúng (T)' : 'Sai (F)'}. Đổi giá trị các biến để xem màu từng nút thay đổi, hoặc bấm “Tính từng bước”.`;
    if (step === 0) return 'Chưa tính gì. Bấm “Bước tiếp” để tính nút đầu tiên (một lá ở dưới cùng bên trái).';
    const n = nodes.find((x) => x.id === ev.order[step - 1]);
    const tv = (x) => (ev.val[x.id] ? 'T' : 'F');
    if (n.type !== 'op') return `Lá ${label(n)} nhận giá trị ${tv(n)}.`;
    const ch = n.kids.map((k) => `${tv(k)}`).join(', ');
    return `Nút ${n.op} (${OP_NAME[n.op]}) lấy giá trị của ${n.kids.length === 1 ? 'nút con' : 'hai nút con'} (${ch}) nên cho ${tv(n)}.${n === lay.root ? ' Đây là liên kết chính, nên cũng là giá trị cả công thức.' : ''}`;
  });
</script>

<div class="dx et">
  <h4>Cây biểu thức Boolean</h4>
  <p class="dx-help">Gõ một công thức, hoặc chọn công thức mẫu. Mỗi phép toán là một nút trong, mỗi biến là một lá. Phép toán ở gốc là <b>liên kết chính</b>, tức phép toán được thực hiện sau cùng.</p>

  <div class="dx-bar">
    {#each PRESETS as [f, name]}
      <button class={text === f ? 'on' : 'sec'} onclick={() => (text = f)} title={f}>{name}</button>
    {/each}
  </div>

  <div class="dx-bar">
    <input type="text" class="dx-mono et-in" bind:value={text} bind:this={inputEl} aria-label="Công thức logic" spellcheck="false" autocomplete="off" placeholder="Ví dụ: (p ∨ q) → ¬r" />
  </div>
  <div class="dx-bar">
    <span class="dx-k">Chèn ký hiệu:</span>
    {#each OPS as o}<button class="sec et-sym" onclick={() => insert(o)} aria-label={OP_NAME[o]}>{o}</button>{/each}
    <button class="sec et-sym" onclick={() => insert('(')}>(</button>
    <button class="sec et-sym" onclick={() => insert(')')}>)</button>
    <span class="dx-k">Cũng gõ được: ! ~ &amp; | -&gt; &lt;-&gt;</span>
  </div>

  {#if parsed.err}
    <div class="dx-err" role="alert">⚠ {parsed.err}{last ? ' Hình bên dưới vẫn là cây của công thức hợp lệ gần nhất.' : ''}</div>
  {/if}

  {#if ast}
    <div class="dx-bar">
      <b>Giá trị các biến:</b>
      {#each vars as v}
        {@const val = env[v] ?? true}
        <span class="et-var">
          <span class="dx-mono">{v}</span>
          <button class={val ? 'on' : 'sec'} onclick={() => setVar(v, true)} aria-pressed={val}>T</button>
          <button class={!val ? 'et-f' : 'sec'} onclick={() => setVar(v, false)} aria-pressed={!val}>F</button>
        </span>
      {/each}
    </div>

    <div class="dx-bar">
      <button class={step !== null ? 'sec' : ''} onclick={() => (step = 0)}>▶ Tính từng bước</button>
      <button class="sec" disabled={step === null || step >= total} onclick={nextStep}>Bước tiếp ▶</button>
      <button class="sec" disabled={step === null || step <= 0} onclick={() => (step = Math.max(0, step - 1))}>◀ Lùi</button>
      <button class="sec" disabled={step === null} onclick={() => (step = null)}>Hiện tất cả</button>
      {#if step !== null}<span class="dx-k">Đã tính {step} / {total} nút</span>{/if}
    </div>

    <div style="overflow-x:auto" class={stale ? 'et-stale' : ''}>
      <svg class="dx-svg" viewBox="0 0 {W} {H}" style="min-width:{Math.min(W, 520)}px;max-height:420px" role="img" aria-label="Cây cú pháp của công thức">
        {#each nodes as n}
          {#each n.kids as c}
            <line x1={px(n)} y1={py(n)} x2={px(c)} y2={py(c)} stroke="var(--et-edge)" stroke-width="2" />
          {/each}
        {/each}
        {#each nodes as n (n.id)}
          {@const isRoot = n.id === lay.root.id}
          <g transform="translate({px(n)},{py(n)})">
            {#if isRoot && n.type === 'op'}
              <circle r="29" fill="none" stroke="var(--et-main)" stroke-width="2.5" stroke-dasharray="5 4" />
            {/if}
            {#if cur(n)}<circle r="26" fill="none" stroke="var(--et-cur)" stroke-width="4" />{/if}
            {#if n.type === 'op'}
              <circle r="22" fill={fill(n)} stroke="var(--et-edge)" stroke-width="2" />
            {:else}
              <rect x="-20" y="-17" width="40" height="34" rx="9" fill={fill(n)} stroke="var(--et-edge)" stroke-width="2" />
            {/if}
            <text text-anchor="middle" dy="6" font-size="20" font-weight="700" fill="var(--et-text)" class="et-node">{label(n)}</text>
            {#if shown.has(n.id)}
              <text text-anchor="middle" y={n.type === 'op' ? 42 : 36} font-size="12" font-weight="800" fill={ev.val[n.id] ? 'var(--et-true-ink)' : 'var(--et-false-ink)'}>{ev.val[n.id] ? 'T' : 'F'}</text>
            {/if}
          </g>
        {/each}
        {#if lay.root.type === 'op'}
          <text x={px(lay.root) + 36} y={py(lay.root) - 20} font-size="12" fill="var(--et-main)" font-weight="700">liên kết chính</text>
        {/if}
      </svg>
    </div>

    <div class="dx-msg" aria-live="polite">{msg}</div>
    <div class="dx-bar et-legend">
      <span><i class="et-sw" style="background:var(--et-true)"></i> Đúng (T)</span>
      <span><i class="et-sw" style="background:var(--et-false)"></i> Sai (F)</span>
      <span><i class="et-sw" style="background:var(--et-idle)"></i> Chưa tính</span>
      <span><i class="et-sw dash"></i> Liên kết chính</span>
      {#if rootVal !== null}<b class={rootVal ? 'dx-ok' : 'dx-bad'}>Kết quả: {rootVal ? 'T' : 'F'}</b>{/if}
    </div>
  {/if}
</div>

<style>
  .et { --et-true:#bbf7d0; --et-false:#fecaca; --et-idle:#f1f5f9; --et-edge:#64748b; --et-text:#0f172a; --et-main:#c2410c; --et-cur:#f59e0b; --et-true-ink:#166534; --et-false-ink:#991b1b; }
  .et-in { flex:1 1 280px; min-width:0; font-size:1.05rem !important; }
  .et-sym { min-width:2.2rem; font-size:1.05rem !important; padding:4px 8px !important; }
  .et-var { display:inline-flex; gap:4px; align-items:center; padding:3px 8px; border:1px solid #cbd5e1; border-radius:10px; background:#fff; }
  .et button.et-f { background:#b91c1c; border-color:#b91c1c; color:#fff; }
  .et-stale { opacity:.6; }
  .et-node { font-family:ui-monospace,Menlo,Consolas,monospace; user-select:none; }
  .et-legend { gap:14px; font-size:.85rem; color:#475569; }
  .et-sw { display:inline-block; width:12px; height:12px; border-radius:3px; border:1px solid #64748b; vertical-align:-1px; margin-right:4px; }
  .et-sw.dash { background:none; border:2px dashed #c2410c; border-radius:50%; }
</style>
