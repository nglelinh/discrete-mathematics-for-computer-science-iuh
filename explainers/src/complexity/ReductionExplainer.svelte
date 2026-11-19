<script>
  import Stepper from '../shared/Stepper.svelte';
  import { parseCNF } from '../logic/dpll.js';
  import { to3SAT, clauseText, GRAPH_PRESETS, isIndependent, isVertexCover, isClique, complement, maxIndependent, minVertexCover, approxVCSteps } from './reductions.js';

  let { tab: tabProp = '3sat', cnf = '', graph = 'house' } = $props();
  let tab = $state(['3sat', 'clique', 'approx'].includes(tabProp) ? tabProp : '3sat');

  // ---- SAT → 3-SAT
  let text = $state(cnf || '(a) ∧ (a ∨ ¬b) ∧ (¬a ∨ b ∨ c ∨ d ∨ e)');
  let sstep = $state(0);
  $effect(() => { text; sstep = 0; });
  const parsed = $derived(parseCNF(text));
  const conv = $derived(parsed.error ? null : to3SAT(parsed.clauses, parsed.names));
  const k3 = $derived(conv ? Math.min(sstep, conv.steps.length) : 0);
  const done3 = $derived(conv ? conv.steps.slice(0, k3) : []);
  const cur3 = $derived(conv && k3 > 0 ? conv.steps[k3 - 1] : null);

  // ---- đồ thị
  let gid = $state(GRAPH_PRESETS.some((p) => p.id === graph) ? graph : 'house');
  let S = $state([]);
  let useComp = $state(false);
  $effect(() => { gid; S = []; });
  const G = $derived(GRAPH_PRESETS.find((p) => p.id === gid));
  const GC = $derived(complement(G));
  const shownG = $derived(useComp ? GC : G);
  const ids = $derived(G.nodes.map((n) => n.id));
  const rest = $derived(ids.filter((x) => !S.includes(x)));
  const isIS = $derived(isIndependent(G, S));
  const isVC = $derived(isVertexCover(G, rest));
  const isCl = $derived(isClique(GC, S));
  const alpha = $derived(maxIndependent(G));
  const tau = $derived(minVertexCover(G));
  const toggle = (id) => { S = S.includes(id) ? S.filter((x) => x !== id) : [...S, id]; };
  const nd = (id) => G.nodes.find((n) => n.id === id);

  // ---- xấp xỉ VC
  let aid = $state(GRAPH_PRESETS.some((p) => p.id === graph) ? graph : 'house');
  let astep = $state(0);
  $effect(() => { aid; astep = 0; });
  const AG = $derived(GRAPH_PRESETS.find((p) => p.id === aid));
  const asteps = $derived(approxVCSteps(AG));
  const as = $derived(asteps[Math.min(astep, asteps.length - 1)]);
  const an = (id) => AG.nodes.find((n) => n.id === id);
</script>

<div class="dx">
  <h4>Quy dẫn đa thức: SAT → 3-SAT · IS ≡ CLIQUE ≡ VC · xấp xỉ Vertex Cover</h4>
  <div class="dx-tabs">
    <button class={tab === '3sat' ? 'on' : 'sec'} onclick={() => (tab = '3sat')}>SAT → 3-SAT</button>
    <button class={tab === 'clique' ? 'on' : 'sec'} onclick={() => (tab = 'clique')}>IS · CLIQUE · VC</button>
    <button class={tab === 'approx' ? 'on' : 'sec'} onclick={() => (tab = 'approx')}>Xấp xỉ Vertex Cover</button>
  </div>

  {#if tab === '3sat'}
    <p class="dx-help">Mỗi mệnh đề dài k được thay bằng các mệnh đề đúng 3 literal (thêm biến mới y). Công thức mới thỏa được ⇔ công thức cũ thỏa được, và chỉ lớn hơn một hệ số tuyến tính. Sửa CNF nếu muốn.</p>
    <textarea rows="2" style="width:100%" class="dx-mono" bind:value={text} aria-label="CNF"></textarea>
    {#if parsed.error}<div class="dx-err" style="margin-top:8px">{parsed.error}</div>
    {:else}
      <Stepper bind:step={sstep} total={conv.steps.length + 1} />
      <div class="dx-msg">{cur3 ? `Mệnh đề ${clauseText(cur3.orig, conv.names)}: ${cur3.rule}` : `Công thức có ${parsed.clauses.length} mệnh đề (độ dài ${parsed.clauses.map((c) => c.length).join(', ')}). Bấm Bước tiếp để chuyển từng mệnh đề.`}</div>
      <div class="dx-row2">
        <div><h5>Mệnh đề gốc</h5><div class="dx-trail" style="flex-direction:column;align-items:stretch">{#each parsed.clauses as c, i}<span class="dx-pill {k3 - 1 === i ? 'hot' : k3 > i ? 'good' : ''}">{clauseText(c, conv.names)}</span>{/each}</div></div>
        <div><h5>3-CNF tương đương ({done3.reduce((a, s) => a + s.produced.length, 0)} mệnh đề)</h5><div class="dx-trail" style="flex-direction:column;align-items:stretch">{#each done3 as s, i}{#each s.produced as c}<span class="dx-pill {k3 - 1 === i ? 'hot' : 'good'}">{clauseText(c, conv.names)}</span>{/each}{:else}<span class="dx-k">(chưa có)</span>{/each}</div></div>
      </div>
    {/if}
  {:else if tab === 'clique'}
    <p class="dx-help">Chọn một tập đỉnh S (bấm vào đỉnh). S là <b>tập độc lập</b> trong G ⇔ V∖S là <b>phủ đỉnh</b> của G ⇔ S là <b>clique</b> trong đồ thị bù Ḡ. Nên ba bài toán quy dẫn lẫn nhau.</p>
    <div class="dx-bar">
      <label>Đồ thị <select bind:value={gid}>{#each GRAPH_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
      <label><input type="checkbox" bind:checked={useComp} /> hiển thị đồ thị bù Ḡ</label>
      <button class="sec" onclick={() => (S = [...alpha])}>Tìm IS lớn nhất</button>
      <button class="sec" onclick={() => (S = [])}>Bỏ chọn</button>
    </div>
    <svg class="dx-svg" viewBox="0 0 540 260" role="img" aria-label="Đồ thị">
      {#each shownG.edges as [a, b]}
        <line x1={nd(a).x} y1={nd(a).y} x2={nd(b).x} y2={nd(b).y} stroke={useComp ? '#a855f7' : '#64748b'} stroke-width="2.5" stroke-dasharray={useComp ? '6 4' : ''} />
      {/each}
      {#each G.nodes as n}
        <g role="button" tabindex="0" aria-label="đỉnh {n.id}" style="cursor:pointer" onclick={() => toggle(n.id)} onkeydown={(e) => (e.key === 'Enter' || e.key === ' ') && toggle(n.id)}>
          <circle cx={n.x} cy={n.y} r="22" fill={S.includes(n.id) ? '#fde68a' : rest.length && isVC && !S.includes(n.id) ? '#dbeafe' : '#fff'} stroke={S.includes(n.id) ? '#d97706' : '#334155'} stroke-width="3" />
          <text x={n.x} y={n.y + 5} text-anchor="middle" font-size="14" font-weight="700">{n.id}</text>
        </g>
      {/each}
    </svg>
    <div class="dx-grid2" style="margin-top:8px">
      <div class="dx-card"><h5>S = {'{'}{S.join(', ')}{'}'} ({S.length} đỉnh)</h5>
        <p style="margin:6px 0" class={isIS ? 'dx-ok' : 'dx-bad'}>{isIS ? '✓' : '✗'} S là tập độc lập trong G</p>
        <p style="margin:6px 0" class={isVC ? 'dx-ok' : 'dx-bad'}>{isVC ? '✓' : '✗'} V∖S = {'{'}{rest.join(', ')}{'}'} là phủ đỉnh của G</p>
        <p style="margin:6px 0" class={isCl ? 'dx-ok' : 'dx-bad'}>{isCl ? '✓' : '✗'} S là clique trong Ḡ</p></div>
      <div class="dx-card"><h5>Giá trị tối ưu</h5>
        <p style="margin:6px 0">α(G) = {alpha.length} (IS lớn nhất: {alpha.join(', ')})<br />τ(G) = {tau.length} (VC nhỏ nhất: {tau.join(', ')})<br /><b>α + τ = {alpha.length + tau.length} = |V| = {ids.length}</b></p></div>
    </div>
  {:else}
    <p class="dx-help">Thuật toán 2-xấp xỉ: cứ lấy một cạnh chưa được phủ và bỏ vào phủ cả hai đầu mút. Các cạnh được chọn rời nhau, mà phủ tối ưu phải chứa ít nhất một đầu mút của mỗi cạnh ấy ⇒ |C| ≤ 2·|OPT|.</p>
    <div class="dx-bar"><label>Đồ thị <select bind:value={aid}>{#each GRAPH_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label></div>
    <Stepper bind:step={astep} total={asteps.length} />
    <div class="dx-msg">{as.msg}</div>
    <svg class="dx-svg" viewBox="0 0 540 260" role="img" aria-label="Đồ thị và phủ đỉnh">
      {#each AG.edges as [a, b]}
        {@const covered = !as.left.some((e) => e[0] === a && e[1] === b)}
        {@const isCh = as.chosen.some((e) => e[0] === a && e[1] === b)}
        <line x1={an(a).x} y1={an(a).y} x2={an(b).x} y2={an(b).y} stroke={isCh ? '#dc2626' : covered ? '#94a3b8' : '#0f172a'} stroke-width={isCh ? 5 : 2.5} stroke-dasharray={covered && !isCh ? '5 4' : ''} />
      {/each}
      {#each AG.nodes as n}
        <circle cx={n.x} cy={n.y} r="22" fill={as.cover.includes(n.id) ? '#fecaca' : '#fff'} stroke={as.edge && as.edge.includes(n.id) ? '#f59e0b' : '#334155'} stroke-width={as.edge && as.edge.includes(n.id) ? 5 : 3} />
        <text x={n.x} y={n.y + 5} text-anchor="middle" font-size="14" font-weight="700">{n.id}</text>
      {/each}
    </svg>
    <p class="dx-k">Đỏ = đỉnh trong phủ C và cạnh đã chọn; nét đứt = cạnh đã được phủ. |C| = {as.cover.length}{as.done ? `, |OPT| = ${as.opt}` : ''}.</p>
  {/if}
</div>
