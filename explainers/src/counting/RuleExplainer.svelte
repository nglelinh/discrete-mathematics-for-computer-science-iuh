<script>
  import Stepper from '../shared/Stepper.svelte';
  import { RULE_PRESETS, postOrder, enumerate, overlapDemo } from './rule.js';

  let { preset = 'outfit' } = $props();
  let pid = $state(RULE_PRESETS.some((p) => p.id === preset) ? preset : 'outfit');
  let step = $state(0);
  $effect(() => { pid; step = 0; });
  const P = $derived(RULE_PRESETS.find((p) => p.id === pid));
  const po = $derived(postOrder(P.tree));
  const revealed = $derived(new Set(po.slice(0, step + 1).map((x) => x.path)));
  const cur = $derived(po[Math.min(step, po.length - 1)]);
  const list = $derived(step === po.length - 1 ? enumerate(P.tree) : []);
  const val = (path) => po.find((x) => x.path === path).value;

  let n = $state(30), a = $state(2), b = $state(3);
  const ov = $derived(overlapDemo(n, a, b));
  const why = (node) => node.t === 'prod' ? 'Quy tắc NHÂN: các bước nối tiếp (và) ⇒ nhân số cách.' : node.t === 'sum' ? 'Quy tắc CỘNG: các trường hợp rời nhau (hoặc) ⇒ cộng số cách.' : 'Lá: số lựa chọn cơ bản.';
</script>

{#snippet nodeView(node, path)}
  <div class="rl-node {node.t}" class:rl-cur={cur.path === path}>
    <div class="rl-head"><span class="rl-tag">{node.t === 'leaf' ? '•' : node.t === 'prod' ? '×  và' : '+  hoặc'}</span> {node.label}
      <b class="rl-val">{revealed.has(path) ? (node.t === 'leaf' ? node.n : val(path)) : '?'}</b></div>
    {#if node.t !== 'leaf'}
      <div class="rl-kids">{#each node.kids as k, i}{@render nodeView(k, path + '.' + i)}{/each}</div>
    {/if}
  </div>
{/snippet}

<div class="dx">
  <h4>Cây đếm: khi nào cộng, khi nào nhân?</h4>
  <p class="dx-help">Tự hỏi: các lựa chọn xảy ra <b>nối tiếp, cùng lúc</b> (chọn áo <i>và</i> quần <i>và</i> giày) ⇒ <b>nhân</b>; hay là <b>các trường hợp thay thế nhau, không chung kết quả</b> (cơm <i>hoặc</i> phở) ⇒ <b>cộng</b>. Bấm Bước tiếp để tính từ lá lên gốc.</p>
  <div class="dx-bar"><label>Bài toán <select bind:value={pid}>{#each RULE_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label></div>
  <Stepper bind:step total={po.length} />
  <div class="dx-msg">{why(cur.node)} <b>{cur.node.label}</b>{cur.node.t === 'leaf' ? ` = ${cur.node.n}` : ` = ${cur.node.kids.map((k) => val(k === undefined ? '' : po.find((x) => x.node === k).path)).join(cur.node.t === 'prod' ? ' × ' : ' + ')} = ${cur.value}`}.</div>
  <div class="rl-tree">{@render nodeView(P.tree, '0')}</div>
  {#if list.length}<details open={list.length <= 30}><summary>Liệt kê {list.length} kết quả</summary><div class="dx-trail dx-mono" style="max-height:140px;overflow:auto">{#each list.slice(0, 120) as x}<span class="dx-pill">{x}</span>{/each}{#if list.length > 120}<span class="dx-k">…</span>{/if}</div></details>{/if}

  <h5 style="margin-top:14px">Cẩn thận: quy tắc cộng cần các trường hợp RỜI NHAU</h5>
  <p class="dx-help">Đếm số trong 1..N chia hết cho a <i>hoặc</i> b. Cộng thẳng đếm hai lần các số chia hết cho cả hai.</p>
  <div class="dx-bar">
    <label>N = <b>{n}</b> <input type="range" min="10" max="100" bind:value={n} /></label>
    <label>a <select bind:value={a}>{#each [2, 3, 4, 5, 6] as x}<option value={x}>{x}</option>{/each}</select></label>
    <label>b <select bind:value={b}>{#each [3, 4, 5, 6, 7, 9] as x}<option value={x}>{x}</option>{/each}</select></label>
  </div>
  <div class="dx-msg">chia hết {a}: {ov.A} · chia hết {b}: {ov.B} · cả hai (bội của {ov.lcm}): {ov.AB}.<br />Cộng thẳng: {ov.A} + {ov.B} = <b class={ov.naive === ov.union ? '' : 'dx-bad'}>{ov.naive}</b>{ov.naive === ov.union ? '' : ' (thừa!)'} · Loại trùng: {ov.A} + {ov.B} − {ov.AB} = <b class="dx-ok">{ov.union}</b> · Đếm vét cạn: {ov.brute} ✓</div>
</div>

<style>
  .rl-tree { overflow-x: auto; padding: 4px 2px; }
  .rl-node { border: 2px solid #cbd5e1; border-radius: 10px; padding: 6px 8px; margin: 4px 0; background: #fff; min-width: 0; }
  .rl-node.prod { border-color: #2563eb; background: #eff6ff; }
  .rl-node.sum { border-color: #16a34a; background: #f0fdf4; }
  .rl-node.leaf { border-style: dashed; background: #f8fafc; }
  .rl-cur { box-shadow: 0 0 0 3px #f59e0b; }
  .rl-head { display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap; }
  .rl-tag { font-weight: 700; font-size: .78rem; color: #475569; }
  .rl-val { margin-left: auto; font-size: 1.05rem; }
  .rl-kids { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
  .rl-kids > .rl-node { flex: 1 1 130px; }
</style>
