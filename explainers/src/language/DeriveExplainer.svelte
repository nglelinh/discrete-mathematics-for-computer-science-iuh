<script>
  import Stepper from '../shared/Stepper.svelte';
  import { parseGrammar, parseTrees, leftmostDerivation, layoutTree, TREE_PRESETS } from './grammar.js';

  let { preset = 'expr-amb', input = '', grammar = '' } = $props();
  const p0 = TREE_PRESETS.find((p) => p.id === preset) || TREE_PRESETS[0];
  let pid = $state(p0.id);
  let text = $state(grammar || p0.text);
  let w = $state(input || p0.input);
  let ti = $state(0);
  let step = $state(0);
  function choose(id) { const p = TREE_PRESETS.find((x) => x.id === id); pid = id; text = p.text; w = p.input; }
  $effect(() => { text; w; ti = 0; step = 0; });
  $effect(() => { ti; step = 0; });

  const g = $derived(parseGrammar(text));
  const toks = $derived(w.trim().split(/\s+/).filter(Boolean));
  const err = $derived(g.error || (!toks.length ? 'Nhập chuỗi (các ký hiệu cách nhau bởi khoảng trắng).' : toks.length > 12 ? 'Tối đa 12 ký hiệu.' : null));
  const res = $derived(err ? null : parseTrees(g, toks));
  const trees = $derived(res ? res.trees : []);
  const tree = $derived(trees[Math.min(ti, trees.length - 1)]);
  const deriv = $derived(tree ? leftmostDerivation(tree) : []);
  const s = $derived(deriv.length ? deriv[Math.min(step, deriv.length - 1)] : null);
  const L = $derived(tree ? layoutTree(tree) : null);
  const CW = 64, RH = 52;
  const W = $derived(L ? L.width * CW + 20 : 0);
  const H = $derived(L ? (L.depth + 1) * RH + 20 : 0);
  const X = (n) => 10 + CW / 2 + n.x * CW;
  const Y = (n) => 22 + n.y * RH;
  const parentOf = $derived(L ? Object.fromEntries(L.links.map(([a, b]) => [b, a])) : {});
  const visible = (n) => parentOf[n.id] === undefined || s.ids.includes(parentOf[n.id]);
  const byId = $derived(L ? Object.fromEntries(L.nodes.map((n) => [n.id, n])) : {});
  const nextExpand = $derived(s && step + 1 < deriv.length ? deriv[step + 1].expand : null);
  const firstVarIdx = $derived(s ? s.form.findIndex((x) => g.isVar && g.isVar(x)) : -1);
</script>

<div class="dx">
  <h4>Dẫn xuất trái nhất và cây phân tích</h4>
  <p class="dx-help">Mỗi bước thay biến <b>ngoài cùng bên trái</b> bằng vế phải của một luật; cây phân tích hiện dần nút được khai triển. Nếu chuỗi có hơn một cây phân tích, văn phạm là <b>nhập nhằng</b> — chuyển giữa các cây để so sánh.</p>
  <div class="dx-bar"><label>Ví dụ <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each TREE_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
    <label>Chuỗi <input type="text" bind:value={w} style="width:15rem;max-width:100%" class="dx-mono" /></label></div>
  <textarea rows="3" style="width:100%" class="dx-mono" bind:value={text} aria-label="Văn phạm"></textarea>
  {#if err}
    <div class="dx-err" style="margin-top:8px">{err}</div>
  {:else if !trees.length}
    <div class="dx-err" style="margin-top:8px">Chuỗi KHÔNG thuộc ngôn ngữ: không có cây phân tích nào.</div>
  {:else}
    <div class="dx-bar" style="margin-top:8px">
      <b class={trees.length > 1 ? 'dx-bad' : 'dx-ok'}>{trees.length > 1 ? `Nhập nhằng: ${res.capped ? '≥ ' : ''}${trees.length} cây phân tích` : 'Duy nhất 1 cây phân tích'}</b>
      {#if trees.length > 1}
        {#each trees as _, i}<button class={ti === i ? 'on' : 'sec'} onclick={() => (ti = i)}>Cây {i + 1}</button>{/each}
      {/if}
    </div>
    <Stepper bind:step total={deriv.length} />
    <div class="dx-msg">{s.rule ? `Bước ${step}: dùng luật ${s.rule}.` : 'Bắt đầu từ ký hiệu khởi đầu ' + g.start + '.'}</div>
    <div class="dx-card" style="margin-bottom:8px"><h5>Dạng câu hiện tại</h5>
      <div class="dx-trail dx-mono" style="font-size:1.05rem">{#each s.form as x, i}<span class="dx-pill {g.isVar(x) ? (i === firstVarIdx ? 'hot' : '') : 'good'}">{x}</span>{/each}</div>
    </div>
    <div style="overflow-x:auto">
      <svg class="dx-svg" viewBox="0 0 {W} {H}" style="min-width:{Math.min(W, 340)}px;max-width:{W}px;margin:0 auto" role="img" aria-label="Cây phân tích">
        {#each L.links as [a, b]}
          {@const A = byId[a]}{@const B = byId[b]}
          <line x1={X(A)} y1={Y(A)} x2={X(B)} y2={Y(B)} stroke={s.ids.includes(a) ? '#475569' : '#e2e8f0'} stroke-width="2" />
        {/each}
        {#each L.nodes as n}
          {@const done = n.leaf ? visible(n) : s.ids.includes(n.id)}
          <circle cx={X(n)} cy={Y(n)} r="17" fill={s.expand === n.id ? '#fde68a' : n.leaf ? '#dcfce7' : done ? '#e0f2fe' : '#fff'} stroke={s.expand === n.id ? '#f59e0b' : done ? '#334155' : '#cbd5e1'} stroke-width={s.expand === n.id ? 3.5 : 2} opacity={visible(n) ? 1 : 0.28} />
          <text x={X(n)} y={Y(n) + 4} text-anchor="middle" font-size={n.sym.length > 3 ? 10 : 12.5} font-weight="700" fill="#0f172a">{n.sym}</text>
        {/each}
      </svg>
    </div>
  {/if}
</div>
