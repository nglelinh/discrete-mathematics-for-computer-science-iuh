<script>
  import Stepper from '../shared/Stepper.svelte';
  import { SORTS, sortSteps, searchSteps } from './sort.js';

  let { tab: tabProp = 'sort', algo = 'bubble', data = '5,2,9,1,7,3' } = $props();
  let tab = $state(tabProp === 'search' ? 'search' : 'sort');
  let kind = $state(SORTS[algo] ? algo : 'bubble');
  let text = $state(data);
  let step = $state(0);
  let skind = $state('binary');
  let target = $state(7);
  let sstep = $state(0);
  const parse = (t) => t.split(/[,\s]+/).map(Number).filter((x) => Number.isFinite(x)).slice(0, 10);
  const arr = $derived(parse(text));
  $effect(() => { text; kind; step = 0; });
  $effect(() => { text; skind; target; sstep = 0; });
  const run = $derived(sortSteps(kind, arr));
  const s = $derived(run.steps[Math.min(step, run.steps.length - 1)]);
  const sorted = $derived([...new Set(arr)].sort((a, b) => a - b));
  const sr = $derived(searchSteps(skind, sorted, Number(target)));
  const ss = $derived(sr.steps[Math.min(sstep, sr.steps.length - 1)]);
  const mx = $derived(Math.max(1, ...arr.map(Math.abs)));
  function shuffle() { const r = Array.from({ length: 8 }, () => 1 + Math.floor(Math.random() * 9)); text = r.join(','); }
  const bar = (v, m) => Math.max(8, Math.round((Math.abs(v) / m) * 100));
</script>

<div class="dx">
  <h4>Sắp xếp và tìm kiếm: đếm từng phép so sánh</h4>
  <div class="dx-tabs">
    <button class={tab === 'sort' ? 'on' : 'sec'} onclick={() => (tab = 'sort')}>Sắp xếp</button>
    <button class={tab === 'search' ? 'on' : 'sec'} onclick={() => (tab = 'search')}>Tìm kiếm</button>
  </div>
  <div class="dx-bar"><label>Dãy số (≤ 10, ngăn bằng dấu phẩy) <input type="text" bind:value={text} class="dx-mono" style="width:12rem;max-width:100%" /></label><button class="sec" onclick={shuffle}>🎲 Ngẫu nhiên</button></div>

  {#if tab === 'sort'}
    <div class="dx-bar"><label>Thuật toán <select bind:value={kind}>{#each Object.entries(SORTS) as [k, v]}<option value={k}>{v}</option>{/each}</select></label></div>
    <Stepper bind:step total={run.steps.length} />
    <div class="dx-msg">{s.msg}</div>
    <div class="st-bars" role="img" aria-label="Các cột của dãy">
      {#each s.arr as v, i}<div class="st-col"><div class="st-bar {s.hi.includes(i) ? (s.op === 'swap' ? 'swap' : 'cmp') : s.op === 'done' ? 'done' : ''}" style="height:{bar(v, mx)}px"></div><b class="dx-mono">{v}</b></div>{/each}
    </div>
    <div class="dx-trail"><span class="dx-pill hot">so sánh: {s.comps}</span><span class="dx-pill">hoán đổi: {s.swaps}</span>
      <span class="dx-k">n = {arr.length}: n(n−1)/2 = {(arr.length * (arr.length - 1)) / 2}</span></div>
  {:else}
    <div class="dx-bar"><label>Cách tìm <select bind:value={skind}><option value="binary">Nhị phân</option><option value="linear">Tuần tự</option></select></label>
      <label>Cần tìm <input type="number" bind:value={target} style="width:5rem" /></label></div>
    <p class="dx-help">Tìm trên dãy đã loại trùng và sắp xếp: <span class="dx-mono">{sorted.join(', ')}</span>.</p>
    <Stepper bind:step={sstep} total={sr.steps.length} />
    <div class="dx-msg">{ss.msg}</div>
    <div class="dx-trail">{#each sorted as v, i}<span class="dx-pill {ss.mid === i ? 'hot' : (skind === 'binary' && (i < ss.lo || i > ss.hi)) ? '' : 'good'}" style={skind === 'binary' && (i < ss.lo || i > ss.hi) ? 'opacity:.35' : ''}>{v}</span>{/each}</div>
    <div class="dx-trail" style="margin-top:6px"><span class="dx-pill hot">so sánh: {ss.comps}</span><span class="dx-k">n = {sorted.length}: tuần tự ≤ {sorted.length}, nhị phân ≤ {Math.floor(Math.log2(Math.max(1, sorted.length))) + 1}</span></div>
  {/if}
</div>

<style>
  .st-bars { display: flex; gap: 6px; align-items: flex-end; height: 130px; margin: 8px 0; overflow-x: auto; }
  .st-col { display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 2px; min-width: 26px; flex: 1; }
  .st-bar { width: 100%; background: #94a3b8; border-radius: 4px 4px 0 0; }
  .st-bar.cmp { background: #f59e0b; }
  .st-bar.swap { background: #dc2626; }
  .st-bar.done { background: #16a34a; }
</style>
