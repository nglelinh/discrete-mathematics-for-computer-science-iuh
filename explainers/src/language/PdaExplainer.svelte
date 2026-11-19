<script>
  import Stepper from '../shared/Stepper.svelte';
  import { PDA_PRESETS, runPDA, tText } from './pda.js';

  let { preset = 'anbn', input = '' } = $props();
  const p0 = PDA_PRESETS.find((p) => p.id === preset) || PDA_PRESETS[0];
  let pid = $state(p0.id);
  let w = $state(input || p0.input);
  let step = $state(0);
  const P = $derived(PDA_PRESETS.find((p) => p.id === pid));
  function choose(id) { pid = id; w = PDA_PRESETS.find((p) => p.id === id).input; }
  $effect(() => { pid; w; step = 0; });

  const word = $derived(w.replace(/\s/g, ''));
  const run = $derived(runPDA(P, word));
  const c = $derived(run.path[Math.min(step, run.path.length - 1)]);
  const last = $derived(step >= run.path.length - 1);
</script>

<div class="dx">
  <h4>Otomat đẩy xuống (PDA): ngăn xếp từng bước</h4>
  <p class="dx-help">{P.desc} Bên dưới là một <b>nhánh tính toán</b> {run.accepted ? 'dẫn tới chấp nhận' : 'đi xa nhất nhưng không chấp nhận'}.</p>
  <div class="dx-bar"><label>PDA <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each PDA_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
    <label>Chuỗi <input type="text" bind:value={w} style="width:11rem" class="dx-mono" /></label></div>
  <Stepper bind:step total={run.path.length} />
  <div class="dx-msg" class:dx-err={last && !run.accepted}>
    {#if c.t}Dùng {tText(c.t)}: {c.t[1] ? 'đọc “' + c.t[1] + '”' : 'không đọc gì (ε)'}{c.t[2] ? ', lấy “' + c.t[2] + '” khỏi ngăn xếp' : ''}{c.t[4] ? ', đẩy “' + c.t[4] + '”' : ''}.{:else}Cấu hình ban đầu: trạng thái {c.state}, ngăn xếp rỗng.{/if}
    {#if last}{run.accepted ? ' ✓ Hết chuỗi ở trạng thái chấp nhận ⇒ NHẬN.' : ' ✗ Không nhánh nào hết chuỗi ở trạng thái chấp nhận ⇒ TỪ CHỐI.'}{/if}
  </div>
  <div class="dx-grid2">
    <div class="dx-card"><h5>Chuỗi vào</h5>
      <div class="dx-trail dx-mono" style="font-size:1.2rem;margin-top:6px">{#each word.split('') as ch, i}<span class="dx-pill {i < c.pos ? 'good' : i === c.pos ? 'hot' : ''}">{ch}</span>{:else}<span class="dx-k">(rỗng)</span>{/each}</div>
      <p style="margin:8px 0 0">Trạng thái: <b class="dx-mono" style="color:#0f766e">{c.state}</b>{P.accept.includes(c.state) ? ' (chấp nhận)' : ''}</p>
    </div>
    <div class="dx-card"><h5>Ngăn xếp (đỉnh ở trên)</h5>
      <div style="display:flex;flex-direction:column;gap:3px;align-items:center;margin-top:6px;min-height:60px">
        {#each c.stack.split('') as ch, i}<div class="dx-mono" style="width:56px;text-align:center;padding:4px 0;border:2px solid {i === 0 ? '#f59e0b' : '#94a3b8'};background:{i === 0 ? '#fef3c7' : '#fff'};font-weight:700">{ch}</div>{:else}<span class="dx-k">(rỗng)</span>{/each}
      </div>
    </div>
  </div>
  <details style="margin-top:8px"><summary>Hàm chuyển</summary><ul class="dx-mono" style="font-size:.85rem">{#each P.trans as t}<li style={c.t === t ? 'background:#fef3c7' : ''}>{tText(t)}</li>{/each}</ul><p class="dx-k">$ là đáy ngăn xếp; ε là bước không đọc/không lấy.</p></details>
</div>
