<script>
  import Stepper from '../shared/Stepper.svelte';
  import { parseGrammar, checkCNF, cykSteps, CYK_PRESETS } from './grammar.js';

  let { preset = 'classic', input = '', grammar = '' } = $props();
  const p0 = CYK_PRESETS.find((p) => p.id === preset) || CYK_PRESETS[0];
  let pid = $state(p0.id);
  let text = $state(grammar || p0.text);
  let w = $state(input || p0.input);
  let step = $state(0);
  function choose(id) { const p = CYK_PRESETS.find((x) => x.id === id); pid = id; text = p.text; w = p.input; }
  $effect(() => { text; w; step = 0; });

  const g = $derived(parseGrammar(text));
  const toks = $derived(w.trim().split(/\s+/).filter(Boolean));
  const err = $derived(g.error || checkCNF(g) || (toks.length ? (toks.length > 9 ? 'Tối đa 9 ký hiệu.' : null) : 'Nhập chuỗi (các ký hiệu cách nhau bởi khoảng trắng).'));
  const run = $derived(err ? null : cykSteps(g, toks));
  const steps = $derived(run ? run.steps : []);
  const s = $derived(run ? steps[Math.min(step, steps.length - 1)] : null);
  const n = $derived(toks.length);
  const is = (c, i, len) => c && c[0] === i && c[1] === len;
</script>

<div class="dx">
  <h4>CYK: bảng phân tích cho văn phạm dạng chuẩn Chomsky</h4>
  <p class="dx-help">Ô (i, ℓ) chứa các biến sinh ra đoạn con dài ℓ bắt đầu ở vị trí i. Mỗi ô được điền bằng cách thử mọi điểm chia: ô trái (xanh) × ô phải (xanh) → luật A → BC. Có thể sửa văn phạm (mỗi dòng một biến, dạng A → B C | a) và chuỗi.</p>
  <div class="dx-bar"><label>Ví dụ <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each CYK_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
    <label>Chuỗi <input type="text" bind:value={w} style="width:11rem" class="dx-mono" /></label></div>
  <textarea rows="4" style="width:100%" class="dx-mono" bind:value={text} aria-label="Văn phạm"></textarea>
  {#if err}
    <div class="dx-err" style="margin-top:8px">{err}</div>
  {:else if s}
    <Stepper bind:step total={steps.length} />
    <div class="dx-msg" class:dx-err={s.done && !s.accepted}>{s.msg}</div>
    <div style="overflow-x:auto;padding-bottom:4px">
      <div style="width:max-content;margin:0 auto">
        {#each Array(n) as _, r}
          {@const len = n - r}
          <div style="display:flex;margin-bottom:3px;align-items:center">
            <span class="dx-k" style="width:44px;flex:none;font-size:.78rem;white-space:nowrap">ℓ = {len}</span>
            <div style="width:{(len - 1) * 28}px;flex:none"></div>
            {#each Array(n - len + 1) as __, i}
              {@const cs = s.cells[i + ',' + len]}
              <div style="width:52px;min-height:34px;margin-right:4px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:600;border:2px solid {is(s.cur, i, len) ? '#f59e0b' : (s.split && (is(s.split.left, i, len) || is(s.split.right, i, len))) ? '#2563eb' : '#cbd5e1'};background:{is(s.cur, i, len) ? '#fef3c7' : (s.split && (is(s.split.left, i, len) || is(s.split.right, i, len))) ? '#dbeafe' : cs ? '#fff' : '#f1f5f9'}">
                {cs ? (cs.length ? cs.join(',') : '∅') : ''}
              </div>
            {/each}
          </div>
        {/each}
        <div style="display:flex;margin-top:4px;padding-left:44px">
          {#each toks as t, i}<div style="width:52px;margin-right:4px;text-align:center" class="dx-mono"><b>{t}</b><br /><small class="dx-k">{i + 1}</small></div>{/each}
        </div>
      </div>
    </div>
    {#if s.done}<p class={s.accepted ? 'dx-ok' : 'dx-bad'}>{s.accepted ? '✓ Chấp nhận' : '✗ Từ chối'}</p>{/if}
  {/if}
</div>
