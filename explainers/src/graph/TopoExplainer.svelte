<script>
  import Stepper from '../shared/Stepper.svelte';
  import { TOPO_PRESETS, withCycle, kahnSteps, dfsSteps } from './topo.js';

  let { preset = 'courses', algo = 'kahn', cycle = false } = $props();
  let pid = $state(TOPO_PRESETS.some((p) => p.id === preset) ? preset : 'courses');
  let method = $state(algo === 'dfs' ? 'dfs' : 'kahn');
  let withLoop = $state(cycle === true || cycle === 'true' || cycle === '1');
  let step = $state(0);

  const P = $derived(TOPO_PRESETS.find((p) => p.id === pid));
  const g = $derived(withCycle(P, withLoop));
  const steps = $derived(method === 'kahn' ? kahnSteps(g) : dfsSteps(g));
  const s = $derived(steps[Math.min(step, steps.length - 1)]);
  const node = (id) => g.nodes.find((n) => n.id === id);
  const lab = (id) => node(id)?.label ?? id;

  $effect(() => { pid; method; withLoop; step = 0; });

  const W = 560, H = 260, R = 25;
  function edgePath(u, v) {
    const a = node(u), b = node(v);
    const dx = b.x - a.x, dy = b.y - a.y, d = Math.hypot(dx, dy) || 1;
    const sx = a.x + (dx / d) * R, sy = a.y + (dy / d) * R, ex = b.x - (dx / d) * (R + 5), ey = b.y - (dy / d) * (R + 5);
    return { sx, sy, ex, ey };
  }
  function fill(id) {
    if (method === 'kahn') {
      if (s.order.includes(id)) return s.cur === id ? '#fde68a' : '#bbf7d0';
      if (s.queue.includes(id)) return '#bae6fd';
      if (s.done && s.cycle && s.indeg[id] > 0) return '#fecaca';
      return '#fff';
    }
    if (s.color[id] === 1) return '#cbd5e1';
    if (s.color[id] === 2) return '#86efac';
    return '#fff';
  }
  function edgeCls(u, v) {
    if (method === 'kahn') return s.removed.includes(u + '>' + v) ? 'gone' : s.cur === u ? 'hot' : '';
    if (s.edge && s.edge[0] === u && s.edge[1] === v) return s.cycle ? 'bad' : 'hot';
    return '';
  }
</script>

<div class="dx">
  <h4>Sắp xếp topo: {method === 'kahn' ? 'Kahn (bậc vào + hàng đợi)' : 'DFS (hậu tự đảo)'}</h4>
  <p class="dx-help">Chọn thuật toán rồi bấm <b>Play</b> hoặc <b>Bước tiếp</b>. Bật “thêm cạnh tạo chu trình” để thấy vì sao đồ thị có chu trình thì không có thứ tự topo.</p>
  <div class="dx-bar">
    <label>Đồ thị
      <select bind:value={pid}>{#each TOPO_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select>
    </label>
    <span class="dx-tabs" style="margin:0">
      <button class={method === 'kahn' ? 'on' : 'sec'} onclick={() => (method = 'kahn')}>Kahn</button>
      <button class={method === 'dfs' ? 'on' : 'sec'} onclick={() => (method = 'dfs')}>DFS</button>
    </span>
    <label><input type="checkbox" bind:checked={withLoop} /> thêm cạnh tạo chu trình ({P.cycleEdge.map(lab).join('→')})</label>
  </div>
  <Stepper bind:step total={steps.length} />
  <div class="dx-msg" class:dx-err={s.done && s.cycle}>{s.msg}</div>
  <svg class="dx-svg" viewBox="0 0 {W} {H}" role="img" aria-label="Đồ thị có hướng">
    <defs>
      {#each ['#64748b', '#f59e0b', '#dc2626', '#cbd5e1'] as c, i}
        <marker id="tp-arrow{i}-{pid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill={c} /></marker>
      {/each}
    </defs>
    {#each g.edges as [u, v]}
      {@const e = edgePath(u, v)}
      {@const c = edgeCls(u, v)}
      <line x1={e.sx} y1={e.sy} x2={e.ex} y2={e.ey} stroke={c === 'hot' ? '#f59e0b' : c === 'bad' ? '#dc2626' : c === 'gone' ? '#cbd5e1' : '#64748b'} stroke-width={c === 'hot' || c === 'bad' ? 3.5 : 2} stroke-dasharray={c === 'gone' ? '5 4' : ''} marker-end="url(#tp-arrow{c === 'hot' ? 1 : c === 'bad' ? 2 : c === 'gone' ? 3 : 0}-{pid})" />
    {/each}
    {#each g.nodes as n}
      <circle cx={n.x} cy={n.y} r={R} fill={fill(n.id)} stroke={s.cur === n.id ? '#f59e0b' : '#475569'} stroke-width={s.cur === n.id ? 4 : 2} />
      <text x={n.x} y={n.y + 4} text-anchor="middle" font-size={n.label.length > 6 ? 10 : 12} font-weight="700" fill="#0f172a">{n.label}</text>
      {#if method === 'kahn'}
        <g><rect x={n.x + 14} y={n.y - 40} width="30" height="17" rx="8" fill="#0f172a" /><text x={n.x + 29} y={n.y - 27.5} text-anchor="middle" font-size="11" fill="#fff">in {s.indeg[n.id]}</text></g>
      {/if}
    {/each}
  </svg>
  <div class="dx-row2">
    {#if method === 'kahn'}
      <div><h5>Hàng đợi (bậc vào 0)</h5><div class="dx-trail">{#each s.queue as q}<span class="dx-pill hot">{lab(q)}</span>{:else}<span class="dx-k">(trống)</span>{/each}</div></div>
      <div><h5>Kết quả đã xuất</h5><div class="dx-trail">{#each s.order as o, i}<span class="dx-pill good">{i + 1}. {lab(o)}</span>{:else}<span class="dx-k">(chưa có)</span>{/each}</div></div>
    {:else}
      <div><h5>Ngăn xếp đệ quy (xám)</h5><div class="dx-trail">{#each s.stack as q}<span class="dx-pill">{lab(q)}</span>{:else}<span class="dx-k">(trống)</span>{/each}</div></div>
      <div><h5>Hậu tự (đen){s.done && !s.cycle ? ' – đảo lại = thứ tự topo' : ''}</h5><div class="dx-trail">{#each (s.done && !s.cycle ? [...s.post].reverse() : s.post) as o, i}<span class="dx-pill good">{i + 1}. {lab(o)}</span>{:else}<span class="dx-k">(chưa có)</span>{/each}</div></div>
    {/if}
  </div>
</div>
