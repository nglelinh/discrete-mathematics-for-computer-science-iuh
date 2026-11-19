<script>
  import Stepper from '../shared/Stepper.svelte';
  import { TM_PRESETS, runTM } from './tm.js';

  let { preset = 'inc', input = '' } = $props();
  const p0 = TM_PRESETS.find((p) => p.id === preset) || TM_PRESETS[0];
  let pid = $state(p0.id);
  let w = $state(input || p0.input);
  let step = $state(0);
  const P = $derived(TM_PRESETS.find((p) => p.id === pid));
  function choose(id) { pid = id; w = TM_PRESETS.find((p) => p.id === id).input; }
  $effect(() => { pid; w; step = 0; });

  const run = $derived(runTM(P, w.replace(/\s/g, '')));
  const cfg = $derived(run.configs[Math.min(step, run.configs.length - 1)]);
  const last = $derived(step >= run.configs.length - 1);
  const ruleKey = (r) => r.join('|');
  const isCur = (r) => cfg.rule && ruleKey(cfg.rule) === ruleKey(r);
  // chỉ hiển thị cửa sổ băng quanh đầu đọc, kèm các ô trống ở hai bên
  const cells = $derived.by(() => {
    const out = [];
    for (let i = cfg.head - 6; i <= cfg.head + 6; i++) out.push({ i, ch: cfg.tape[i] ?? '_' });
    return out;
  });
</script>

<div class="dx">
  <h4>Máy Turing từng bước</h4>
  <p class="dx-help">{P.desc} Mỗi bước: đọc ký hiệu dưới đầu đọc, tra bảng chuyển, <b>ghi</b>, <b>di chuyển</b> (L/R/S) và đổi trạng thái.</p>
  <div class="dx-bar"><label>Máy <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each TM_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
    <label>Đầu vào <input type="text" bind:value={w} style="width:9rem" class="dx-mono" /></label></div>
  <Stepper bind:step total={run.configs.length} />
  <div class="dx-msg" class:dx-err={last && run.status !== 'accept'}>
    {#if step === 0}Cấu hình ban đầu: trạng thái {cfg.state}, đầu đọc ở ô đầu băng.
    {:else}δ({cfg.rule[0]}, {cfg.rule[1]}) = ({cfg.rule[2]}, ghi {cfg.rule[3]}, {cfg.rule[4]}) → trạng thái {cfg.state}.{/if}
    {#if last}{run.status === 'accept' ? ' DỪNG và CHẤP NHẬN. Băng còn lại: “' + run.output + '”.' : run.status === 'reject' ? ' Không có luật cho (' + cfg.state + ', ' + (cfg.tape[cfg.head] ?? '_') + ') ⇒ TỪ CHỐI.' : ' Quá số bước tối đa.'}{/if}
  </div>
  <div style="overflow-x:auto">
    <div style="display:flex;gap:3px;width:max-content;margin:0 auto;padding-top:6px">
      {#each cells as c}
        <div style="text-align:center">
          <div class="dx-mono" style="width:38px;height:42px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;font-weight:700;border:2px solid {c.i === cfg.head ? '#f59e0b' : '#94a3b8'};background:{c.i === cfg.head ? '#fef3c7' : c.ch === '_' ? '#f8fafc' : '#fff'};color:{c.ch === '_' ? '#94a3b8' : '#0f172a'}">{c.ch}</div>
          <div style="height:18px;color:#d97706;font-size:.85rem">{c.i === cfg.head ? '▲ ' + cfg.state : ''}</div>
        </div>
      {/each}
    </div>
  </div>
  <details style="margin-top:8px"><summary>Bảng chuyển trạng thái</summary>
    <table class="dx-t dx-mono" style="margin-top:6px"><thead><tr><th>Trạng thái</th><th>Đọc</th><th>→ Trạng thái</th><th>Ghi</th><th>Di chuyển</th></tr></thead>
      <tbody>{#each P.rules as r}<tr style={isCur(r) ? 'background:#fef3c7' : ''}>{#each r as x}<td>{x}</td>{/each}</tr>{/each}</tbody></table>
    <p class="dx-k">“_” là ô trống; qA là trạng thái chấp nhận; thiếu luật ⇒ từ chối.</p></details>
</div>
