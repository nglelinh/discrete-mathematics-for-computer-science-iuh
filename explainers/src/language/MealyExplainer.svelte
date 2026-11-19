<script>
  import Stepper from '../shared/Stepper.svelte';
  import AutomatonView from '../automata/AutomatonView.svelte';
  import { MEALY_PRESETS, runTransducer, viewMachine } from './mealy.js';

  let { preset = 'm11', input = '' } = $props();
  const p0 = MEALY_PRESETS.find((p) => p.id === preset) || MEALY_PRESETS[0];
  let pid = $state(p0.id);
  let w = $state(input || p0.input);
  let step = $state(0);
  const P = $derived(MEALY_PRESETS.find((p) => p.id === pid));
  function choose(id) { pid = id; w = MEALY_PRESETS.find((p) => p.id === id).input; }
  $effect(() => { pid; w; step = 0; });
  const run = $derived(runTransducer(P, w));
  const VM = $derived(viewMachine(P));
  const k = $derived(Math.min(step, run.steps.length - 1));
  const cur = $derived(run.steps[k]);
  const prev = $derived(k > 0 ? run.steps[k - 1] : null);
  const hot = $derived(prev ? [VM.nameOf(prev.state) + '>' + VM.nameOf(cur.state)] : []);
  const moore = $derived(P.kind === 'moore');
</script>

<div class="dx">
  <h4>Máy Mealy và Moore: đầu vào → đầu ra</h4>
  <p class="dx-help">{P.kind === 'mealy' ? 'Mealy: đầu ra gắn với MỖI CHUYỂN TIẾP (nhãn vào/ra).' : 'Moore: đầu ra gắn với TRẠNG THÁI (ghi sau dấu / trong tên trạng thái), nên có thêm một đầu ra ở trạng thái đầu.'} {P.desc ?? ''}</p>
  <div class="dx-bar"><label>Máy <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each MEALY_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
    <label>Đầu vào <input type="text" bind:value={w} class="dx-mono" style="width:11rem" /></label></div>
  {#if run.error}<div class="dx-err">{run.error}</div>{/if}
  <Stepper bind:step total={run.steps.length} />
  <div class="dx-msg">{#if k === 0}Trạng thái đầu {cur.state}{moore ? `, đầu ra ${cur.out}` : ''}.{:else}Đọc “{cur.read}”: {prev.state} → {cur.state}, đầu ra <b>{cur.out}</b>.{/if}</div>
  <AutomatonView machine={VM} active={[VM.nameOf(cur.state)]} {hot} width={560} height={240} label="Máy trạng thái có đầu ra" />
  <div class="dx-grid2" style="margin-top:8px">
    <div class="dx-card"><h5>Đầu vào</h5><div class="dx-trail dx-mono">{#each run.toks as t, i}<span class="dx-pill {i < cur.pos ? 'good' : i === cur.pos ? 'hot' : ''}">{t}</span>{/each}</div></div>
    <div class="dx-card"><h5>Đầu ra</h5><div class="dx-trail dx-mono">{#each cur.outputs as o}<span class="dx-pill good">{o}</span>{:else}<span class="dx-k">(chưa có)</span>{/each}</div></div>
  </div>
</div>
