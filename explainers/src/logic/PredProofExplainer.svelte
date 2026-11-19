<script>
  import Stepper from '../shared/Stepper.svelte';
  import { PROOFS, counterexample, countModels } from './predproof.js';

  let { preset = 'socrates' } = $props();
  let pid = $state(PROOFS.some((p) => p.id === preset) ? preset : 'socrates');
  let step = $state(0);
  $effect(() => { pid; step = 0; });
  const P = $derived(PROOFS.find((p) => p.id === pid));
  const ce = $derived(counterexample(P));
  const nm = $derived(countModels(P));
  const total = $derived(P.lines.length + 1);
  const k = $derived(Math.min(step, total - 1));
  const first = $derived(P.lines.findIndex((l) => l.ok === false));
</script>

<div class="dx">
  <h4>Suy luận vị từ từng dòng: UI · UG · EI · EG</h4>
  <p class="dx-help">{P.note} Mỗi dòng ghi quy tắc đã dùng. Dòng đỏ vi phạm điều kiện của quy tắc; cuối cùng ta kiểm tra bằng mọi mô hình có ≤ 3 phần tử.</p>
  <div class="dx-bar"><label>Chứng minh <select bind:value={pid}>{#each PROOFS as p}<option value={p.id}>{p.name}</option>{/each}</select></label></div>
  <Stepper bind:step {total} />
  <div style="overflow-x:auto"><table class="dx-t pp-t"><thead><tr><th>#</th><th>Mệnh đề</th><th>Lý do</th></tr></thead>
    <tbody>
      {#each P.lines as l, i}{#if i < k}
        <tr class:pp-bad={l.ok === false} class:pp-cur={i === k - 1}><td>{i + 1}</td><td class="dx-mono">{l.t}</td>
          <td style="text-align:left">{l.rule}{#if l.why}<div class="pp-why">⚠ {l.why}</div>{/if}</td></tr>
      {/if}{/each}
    </tbody></table></div>
  {#if k === total - 1}
    <div class="dx-msg" class:dx-err={!P.valid}>
      {#if P.valid}Mọi bước đúng quy tắc ⇒ chứng minh hợp lệ. Kiểm tra: trong {nm} mô hình (≤ 3 phần tử) thỏa các tiền đề, kết luận đều đúng ✓.
      {:else}Chứng minh sai ở dòng {first + 1}. Kết luận thật sự không suy ra được; phản ví dụ: miền {ce.n} phần tử, P = {'{'}{ce.P.map((x, i) => (x ? i + 1 : null)).filter(Boolean).join(', ')}{'}'}, Q = {'{'}{ce.Q.map((x, i) => (x ? i + 1 : null)).filter(Boolean).join(', ')}{'}'}, c = {ce.c + 1}: các tiền đề đúng mà kết luận sai.{/if}
    </div>
    {#if ce}<div class="dx-trail">{#each Array(ce.n) as _, i}<span class="dx-pill {ce.c === i ? 'hot' : ''}">phần tử {i + 1}: P {ce.P[i] ? '✓' : '✗'} · Q {ce.Q[i] ? '✓' : '✗'}{ce.c === i ? ' · c' : ''}</span>{/each}</div>{/if}
  {:else if k === 0}<div class="dx-msg">Bấm Bước tiếp để thêm từng dòng của chứng minh.</div>
  {:else}<div class="dx-msg" class:dx-err={P.lines[k - 1].ok === false}>Dòng {k}: {P.lines[k - 1].rule}{P.lines[k - 1].ok === false ? ' ⇒ ' + P.lines[k - 1].why : ''}</div>{/if}
</div>

<style>
  .pp-t td:nth-child(2) { text-align: left; }
  .pp-bad td { background: #fee2e2; }
  .pp-cur td { box-shadow: inset 0 0 0 2px #f59e0b; }
  .pp-why { color: #b91c1c; font-size: .8rem; margin-top: 2px; }
</style>
