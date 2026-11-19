<script>
  import Stepper from '../shared/Stepper.svelte';
  import AutomatonView from '../automata/AutomatonView.svelte';
  import { parseRegex, thompson, machineAt, eliminationSteps, toJsRegExp, REGEX_PRESETS, ELIM_PRESETS } from './regex.js';
  import { accepts } from '../automata/automata.js';

  let { tab: tabProp = 'thompson', regex = '', preset = '', order = 'forward' } = $props();
  let tab = $state(tabProp === 'eliminate' ? 'eliminate' : 'thompson');

  // ---- Thompson
  let text = $state(regex || REGEX_PRESETS[0].text);
  let tstep = $state(0);
  let test = $state('abb');
  $effect(() => { text; tstep = 0; });
  const built = $derived.by(() => { try { const ast = parseRegex(text); return { T: thompson(ast) }; } catch (e) { return { error: e.message }; } });
  const T = $derived(built.T);
  const k = $derived(T ? Math.min(tstep, T.steps.length - 1) : 0);
  const M = $derived(T ? machineAt(T, k) : null);
  const hl = $derived(T ? T.machine.states.filter((s) => s.born === k).map((s) => s.id) : []);
  const full = $derived(T ? machineAt(T, T.steps.length - 1) : null);
  const verdict = $derived(full ? accepts(full, test.trim()) : false);

  // ---- loại trạng thái
  let eid = $state(ELIM_PRESETS.some((p) => p.id === preset) ? preset : 'dfa01');
  let dir = $state(order === 'reverse' ? 'reverse' : 'forward');
  let estep = $state(0);
  $effect(() => { eid; dir; estep = 0; });
  const EP = $derived(ELIM_PRESETS.find((p) => p.id === eid));
  const EM = $derived(EP.make());
  const ord = $derived(dir === 'forward' ? EM.states.map((s) => s.id) : [...EM.states.map((s) => s.id)].reverse());
  const E = $derived(eliminationSteps(EM, ord));
  const es = $derived(E.steps[Math.min(estep, E.steps.length - 1)]);
  const view = $derived.by(() => {
    const maxX = Math.max(...EM.states.map((s) => s.x)), minX = Math.min(...EM.states.map((s) => s.x));
    const shift = 90 - minX + 40;
    const pos = Object.fromEntries(EM.states.map((s) => [s.id, { x: s.x + shift, y: s.y }]));
    pos.S = { x: 40, y: 150 }; pos.F = { x: maxX + shift + 110, y: 150 };
    const states = es.alive.map((id) => ({ id, ...pos[id] }));
    const edges = Object.entries(es.labels).map(([key, label]) => { const [a, b] = key.split('>'); return { from: a, to: b, syms: [label] }; });
    return { m: { states, start: 'S', accept: ['F'], edges }, w: maxX + shift + 170 };
  });
  const regexJs = $derived(E.regex === null ? null : toJsRegExp(E.regex));
</script>

<div class="dx">
  <h4>Biểu thức chính quy ↔ otomat: Thompson và loại trạng thái</h4>
  <div class="dx-tabs">
    <button class={tab === 'thompson' ? 'on' : 'sec'} onclick={() => (tab = 'thompson')}>Regex → ε-NFA (Thompson)</button>
    <button class={tab === 'eliminate' ? 'on' : 'sec'} onclick={() => (tab = 'eliminate')}>Otomat → regex (loại trạng thái)</button>
  </div>

  {#if tab === 'thompson'}
    <p class="dx-help">Mỗi phép toán của regex (ký tự, nối tiếp, hợp |, sao *) có một “khối” otomat chuẩn. Thuật toán ghép các khối từ trong ra ngoài. Cạnh ε là cạnh không đọc ký tự. Dùng chữ/số, <b>|</b> <b>*</b> <b>+</b> <b>?</b> và ngoặc.</p>
    <div class="dx-bar">
      <label>Ví dụ <select onchange={(e) => (text = e.currentTarget.value)}>{#each REGEX_PRESETS as p}<option value={p.text}>{p.name}</option>{/each}</select></label>
      <label>Regex <input type="text" bind:value={text} class="dx-mono" style="width:11rem;max-width:100%" /></label>
    </div>
    {#if built.error}<div class="dx-err">{built.error}</div>
    {:else}
      <Stepper bind:step={tstep} total={T.steps.length} />
      <div class="dx-msg">Bước {k + 1}: {T.steps[k].desc} <span class="dx-k">(khối: {T.steps[k].node})</span></div>
      <div style="overflow-x:auto"><div style="min-width:{Math.min(T.width, 640)}px;max-width:{T.width}px">
        <AutomatonView machine={M} highlight={hl} width={T.width} height={T.height} label="NFA Thompson" />
      </div></div>
      <div class="dx-bar" style="margin-top:8px"><label>Thử chuỗi <input type="text" bind:value={test} class="dx-mono" style="width:9rem" /></label>
        <b class={verdict ? 'dx-ok' : 'dx-bad'}>{verdict ? '✓ NFA chấp nhận' : '✗ NFA từ chối'} “{test}”</b></div>
    {/if}
  {:else}
    <p class="dx-help">Thêm trạng thái đầu S và cuối F, rồi loại từng trạng thái: mọi đường i → q → j được thay bằng cạnh i → j mang nhãn R(i,q)·R(q,q)*·R(q,j) (hợp với nhãn cũ). Cuối cùng cạnh S → F là regex.</p>
    <div class="dx-bar">
      <label>Otomat <select bind:value={eid}>{#each ELIM_PRESETS as p}<option value={p.id}>{p.label}</option>{/each}</select></label>
      <label>Thứ tự loại <select bind:value={dir}><option value="forward">q theo thứ tự tên</option><option value="reverse">ngược lại</option></select></label>
    </div>
    <Stepper bind:step={estep} total={E.steps.length} />
    <div class="dx-msg">{es.msg}</div>
    <div style="overflow-x:auto"><div style="min-width:{Math.min(view.w, 640)}px;max-width:{view.w}px">
      <AutomatonView machine={view.m} highlight={es.removed ? [es.removed] : []} width={view.w} height={300} label="GNFA" />
    </div></div>
    {#if es.done}<p class="dx-ok">Regex: <span class="dx-mono">{E.regex ?? '∅'}</span></p>{/if}
  {/if}
</div>
