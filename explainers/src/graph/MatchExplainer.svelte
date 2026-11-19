<script>
  import Stepper from '../shared/Stepper.svelte';
  import { MATCH_PRESETS, kuhnSteps, COLOR_PRESETS, orderOf, greedySteps, chromaticNumber } from './match.js';

  let { tab: tabProp = 'matching', preset = '', order = 'index' } = $props();
  let tab = $state(tabProp === 'coloring' ? 'coloring' : 'matching');

  // ---- ghép cặp
  let mid = $state(MATCH_PRESETS.some((p) => p.id === preset) ? preset : 'jobs');
  let mstep = $state(0);
  const MG = $derived(MATCH_PRESETS.find((p) => p.id === mid));
  const msteps = $derived(kuhnSteps(MG));
  const ms = $derived(msteps[Math.min(mstep, msteps.length - 1)]);
  $effect(() => { mid; mstep = 0; });
  const LX = 120, RX = 440;
  const ly = (id) => MG.left.find((n) => n.id === id).y;
  const ry = (id) => MG.right.find((n) => n.id === id).y;
  const isM = (l, r) => ms.matchL[l] === r;
  const isE = (l, r) => ms.edge && ms.edge[0] === l && ms.edge[1] === r;

  // ---- tô màu
  let cid = $state(COLOR_PRESETS.some((p) => p.id === preset) ? preset : 'crown');
  let kind = $state(['index', 'degree', 'bad'].includes(order) ? order : 'index');
  let cstep = $state(0);
  const CG = $derived(COLOR_PRESETS.find((p) => p.id === cid));
  const hasBad = $derived(!!CG.badOrder);
  const ord = $derived(orderOf(CG, kind === 'bad' && !hasBad ? 'index' : kind));
  const csteps = $derived(greedySteps(CG, ord));
  const cs = $derived(csteps[Math.min(cstep, csteps.length - 1)]);
  const chi = $derived(chromaticNumber(CG));
  $effect(() => { cid; kind; cstep = 0; });
  const PAL = ['#fca5a5', '#93c5fd', '#86efac', '#fde68a', '#d8b4fe', '#fdba74', '#67e8f9'];
  const node = (id) => CG.nodes.find((n) => n.id === id);
</script>

<div class="dx">
  <h4>Đồ thị: ghép cặp (đường tăng) và tô màu tham lam</h4>
  <div class="dx-tabs">
    <button class={tab === 'matching' ? 'on' : 'sec'} onclick={() => (tab = 'matching')}>Ghép cặp cực đại</button>
    <button class={tab === 'coloring' ? 'on' : 'sec'} onclick={() => (tab = 'coloring')}>Tô màu tham lam</button>
  </div>

  {#if tab === 'matching'}
    <p class="dx-help">Thuật toán thử ghép từng đỉnh trái; nếu đỉnh phải đã bị chiếm thì “nhờ” người đang chiếm chuyển chỗ (đi dọc đường xen kẽ). Cạnh xanh đậm = đã ghép, cạnh cam = đang xét.</p>
    <div class="dx-bar"><label>Đồ thị <select bind:value={mid}>{#each MATCH_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label></div>
    <Stepper bind:step={mstep} total={msteps.length} />
    <div class="dx-msg" class:dx-err={ms.done && ms.size < MG.left.length}>{ms.msg}</div>
    <svg class="dx-svg" viewBox="0 0 560 270" role="img" aria-label="Đồ thị hai phía">
      {#each MG.edges as [l, r]}
        <line x1={LX + 24} y1={ly(l)} x2={RX - 24} y2={ry(r)} stroke={isE(l, r) ? '#f59e0b' : isM(l, r) ? '#16a34a' : '#cbd5e1'} stroke-width={isE(l, r) || isM(l, r) ? 5 : 2} />
      {/each}
      {#each MG.left as n}
        <rect x={LX - 42} y={n.y - 16} width="66" height="32" rx="16" fill={ms.root === n.id ? '#fef3c7' : ms.matchL[n.id] ? '#dcfce7' : '#fff'} stroke={ms.root === n.id ? '#f59e0b' : '#475569'} stroke-width="2.5" />
        <text x={LX - 9} y={n.y + 4} text-anchor="middle" font-size="12" font-weight="700">{n.id}</text>
      {/each}
      {#each MG.right as n}
        <rect x={RX - 24} y={n.y - 16} width="66" height="32" rx="16" fill={ms.visited.includes(n.id) ? '#e0f2fe' : ms.matchR[n.id] ? '#dcfce7' : '#fff'} stroke="#475569" stroke-width="2.5" />
        <text x={RX + 9} y={n.y + 4} text-anchor="middle" font-size="12" font-weight="700">{n.id}</text>
      {/each}
    </svg>
    <p class="dx-k">Kích thước ghép hiện tại: <b>{ms.size}</b>. Xanh nhạt bên phải = đã thăm trong lần tìm đường này.</p>
  {:else}
    <p class="dx-help">Mỗi đỉnh nhận màu nhỏ nhất chưa xuất hiện ở các đỉnh kề. Kết quả phụ thuộc <b>thứ tự</b> duyệt: thử “thứ tự xấu” trên đồ thị vương miện để thấy 3 màu dù χ = 2.</p>
    <div class="dx-bar">
      <label>Đồ thị <select bind:value={cid}>{#each COLOR_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
      <label>Thứ tự <select bind:value={kind}><option value="index">Theo tên đỉnh</option><option value="degree">Welsh–Powell (bậc giảm dần)</option>{#if hasBad}<option value="bad">Thứ tự xấu</option>{/if}</select></label>
    </div>
    <Stepper bind:step={cstep} total={csteps.length} />
    <div class="dx-msg">{cs.msg}{#if cs.done} Số màu tối thiểu χ(G) = {chi}{cs.used === chi ? ' ⇒ tham lam tối ưu ở thứ tự này.' : `, tham lam dùng nhiều hơn ${cs.used - chi}.`}{/if}</div>
    <div class="dx-k" style="margin-bottom:4px">Thứ tự duyệt: {ord.join(' → ')}</div>
    <svg class="dx-svg" viewBox="0 0 560 270" role="img" aria-label="Đồ thị cần tô màu">
      {#each CG.edges as [a, b]}<line x1={node(a).x} y1={node(a).y} x2={node(b).x} y2={node(b).y} stroke="#64748b" stroke-width="2" />{/each}
      {#each CG.nodes as n}
        <circle cx={n.x} cy={n.y} r="24" fill={cs.color[n.id] !== undefined ? PAL[cs.color[n.id] % PAL.length] : '#fff'} stroke={cs.cur === n.id ? '#f59e0b' : '#334155'} stroke-width={cs.cur === n.id ? 5 : 2.5} />
        <text x={n.x} y={n.y + 4} text-anchor="middle" font-size="12" font-weight="700">{n.id}</text>
        {#if cs.color[n.id] !== undefined}<text x={n.x + 18} y={n.y - 20} font-size="11" font-weight="700" fill="#0f172a">{cs.color[n.id] + 1}</text>{/if}
      {/each}
    </svg>
  {/if}
</div>
