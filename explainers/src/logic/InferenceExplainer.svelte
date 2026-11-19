<script>
  import Stepper from '../shared/Stepper.svelte';
  import { INFERENCE_PRESETS, checkArgument } from './inference.js';

  let { preset = 'mp', premises = '', conclusion = '' } = $props();
  const p0 = INFERENCE_PRESETS.find((p) => p.id === preset) || INFERENCE_PRESETS[0];
  let pid = $state(p0.id);
  let prem = $state(premises ? premises.replace(/\\n/g, '\n') : p0.premises);
  let conc = $state(conclusion || p0.conclusion);
  let step = $state(0);
  function choose(id) { const p = INFERENCE_PRESETS.find((x) => x.id === id); pid = id; prem = p.premises; conc = p.conclusion; }
  $effect(() => { prem; conc; step = 0; });
  const res = $derived(checkArgument(prem, conc));
  const total = $derived(res.error ? 1 : res.rows.length + 1);
  const k = $derived(Math.min(step, total - 1));
  const shown = (i) => i < k;
  const cur = $derived(!res.error && k > 0 && k <= res.rows.length ? res.rows[k - 1] : null);
  const T = (v) => (v ? 'T' : 'F');
  const bad = $derived(!res.error ? res.rows.slice(0, k).filter((r) => r.bad).length : 0);
  const msg = $derived(res.error ? res.error : k === 0
    ? 'Quy tắc suy diễn hợp lệ ⇔ ở MỌI dòng bảng chân trị mà tất cả tiền đề cùng đúng (dòng quan trọng), kết luận cũng đúng. Bấm Bước tiếp để duyệt từng dòng.'
    : k <= res.rows.length
      ? (cur.bad ? `PHẢN VÍ DỤ: ${res.vars.map((v) => v + '=' + T(cur.env[v])).join(', ')} làm mọi tiền đề đúng nhưng kết luận sai ⇒ KHÔNG hợp lệ.`
        : cur.critical ? `Dòng quan trọng (mọi tiền đề đúng): kết luận cũng đúng ✓.` : 'Có tiền đề sai ⇒ dòng này không ràng buộc gì, bỏ qua.')
      : res.valid ? 'Mọi dòng quan trọng đều có kết luận đúng ⇒ HỢP LỆ.' : `Có ${bad} phản ví dụ ⇒ KHÔNG HỢP LỆ (ngụy biện).`);
</script>

<div class="dx">
  <h4>Kiểm tra quy tắc suy diễn bằng bảng chân trị</h4>
  <p class="dx-help">Mỗi tiền đề một dòng (dùng ¬ ∧ ∨ → ↔ ⊕ hoặc ! &amp; | -&gt;). Dòng <span style="background:#dcfce7;padding:0 4px">xanh</span> = mọi tiền đề đúng; dòng <span style="background:#fee2e2;padding:0 4px">đỏ</span> = phản ví dụ.</p>
  <div class="dx-bar"><label>Ví dụ <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each INFERENCE_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label></div>
  <div class="dx-grid2">
    <label style="display:block">Tiền đề<textarea rows="3" style="width:100%" bind:value={prem} class="dx-mono"></textarea></label>
    <label style="display:block">Kết luận<input type="text" style="width:100%" bind:value={conc} class="dx-mono" /></label>
  </div>
  {#if res.error}
    <div class="dx-err" style="margin-top:8px">{res.error}</div>
  {:else}
    <Stepper bind:step total={total} />
    <div class="dx-msg" class:dx-err={k === total - 1 && !res.valid}>{msg}</div>
    <div style="overflow-x:auto"><table class="dx-t dx-mono" style="margin:0 auto">
      <thead><tr>{#each res.vars as v}<th>{v}</th>{/each}{#each Array(res.count) as _, i}<th>Tiền đề {i + 1}</th>{/each}<th>Kết luận</th></tr></thead>
      <tbody>{#each res.rows as r, i}
        <tr style="background:{shown(i) ? (r.bad ? '#fee2e2' : r.critical ? '#dcfce7' : '#fff') : '#f8fafc'};outline:{k - 1 === i ? '3px solid #f59e0b' : 'none'};color:{shown(i) ? '#0f172a' : '#cbd5e1'}">
          {#each res.vars as v}<td>{T(r.env[v])}</td>{/each}
          {#each r.pv as x}<td>{shown(i) ? T(x) : '·'}</td>{/each}
          <td style="font-weight:700">{shown(i) ? T(r.cv) : '·'}</td></tr>
      {/each}</tbody></table></div>
    {#if k === total - 1}<p class={res.valid ? 'dx-ok' : 'dx-bad'}>{res.valid ? '✓ Hợp lệ' : '✗ Không hợp lệ'}</p>{/if}
  {/if}
</div>
