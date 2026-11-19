<script>
  import Stepper from '../shared/Stepper.svelte';
  import { parseGrammar, TREE_PRESETS } from './grammar.js';
  import { runCfgPda } from './cfgpda.js';

  let { preset = 'paren', input = '', grammar = '' } = $props();
  const p0 = TREE_PRESETS.find((p) => p.id === preset) || TREE_PRESETS[3];
  let pid = $state(p0.id);
  let text = $state(grammar || p0.text);
  let w = $state(input || p0.input);
  let step = $state(0);
  function choose(id) { const p = TREE_PRESETS.find((x) => x.id === id); pid = id; text = p.text; w = p.input; }
  $effect(() => { text; w; step = 0; });
  const g = $derived(parseGrammar(text));
  const toks = $derived(w.trim().split(/\s+/).filter(Boolean));
  const err = $derived(g.error || (toks.length > 10 ? 'Tối đa 10 ký hiệu.' : null));
  const run = $derived(err ? null : runCfgPda(g, toks));
  const k = $derived(run ? Math.min(step, run.path.length - 1) : 0);
  const c = $derived(run ? run.path[k] : null);
</script>

<div class="dx">
  <h4>CFG → PDA: ngăn xếp mô phỏng dẫn xuất trái nhất</h4>
  <p class="dx-help">PDA ba trạng thái: đẩy S; lặp lại — nếu đỉnh ngăn xếp là <b>biến A</b> thì chọn (không tất định) một luật A → α và thay A bằng α; nếu là <b>ký hiệu kết thúc</b> thì phải khớp với ký hiệu đang đọc rồi lấy ra. Nhận khi hết chuỗi và ngăn xếp rỗng. Dưới đây là một nhánh {run?.accepted ? 'chấp nhận' : 'đi xa nhất'}.</p>
  <div class="dx-bar"><label>Ví dụ <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each TREE_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
    <label>Chuỗi <input type="text" bind:value={w} class="dx-mono" style="width:14rem;max-width:100%" /></label></div>
  <textarea rows="3" style="width:100%" class="dx-mono" bind:value={text} aria-label="Văn phạm"></textarea>
  {#if err}<div class="dx-err" style="margin-top:8px">{err}</div>
  {:else}
    <Stepper bind:step total={run.path.length} />
    <div class="dx-msg" class:dx-err={k === run.path.length - 1 && !run.accepted}>{c.action}{#if k === run.path.length - 1}{run.accepted ? ' ✓ Hết chuỗi và ngăn xếp rỗng ⇒ NHẬN.' : ' ✗ Không nhánh nào nhận ⇒ TỪ CHỐI.'}{/if}</div>
    <div class="dx-grid2">
      <div class="dx-card"><h5>Chuỗi vào</h5><div class="dx-trail dx-mono">{#each toks as t, i}<span class="dx-pill {i < c.pos ? 'good' : i === c.pos ? 'hot' : ''}">{t}</span>{/each}</div></div>
      <div class="dx-card"><h5>Ngăn xếp (đỉnh ở trên)</h5>
        <div style="display:flex;flex-direction:column;gap:3px;align-items:center;margin-top:6px;min-height:50px">
          {#each c.stack as s, i}<div class="dx-mono" style="min-width:64px;text-align:center;padding:3px 10px;border:2px solid {i === 0 ? '#f59e0b' : '#94a3b8'};background:{g.isVar(s) ? '#e0f2fe' : '#dcfce7'};font-weight:700">{s}</div>{:else}<span class="dx-k">(rỗng — chỉ còn $)</span>{/each}
        </div></div>
    </div>
    <p class="dx-k">Xanh dương = biến; xanh lá = ký hiệu kết thúc.</p>
  {/if}
</div>
