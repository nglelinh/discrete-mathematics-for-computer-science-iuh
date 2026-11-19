<script>
  import Stepper from '../shared/Stepper.svelte';
  import { parseCNF, dpllSteps, clauseText, DPLL_PRESETS } from './dpll.js';

  let { preset = 'sat', cnf = '' } = $props();
  let pid = $state(DPLL_PRESETS.some((p) => p.id === preset) ? preset : 'sat');
  let text = $state(cnf || DPLL_PRESETS.find((p) => p.id === pid).text);
  let step = $state(0);
  const parsed = $derived(parseCNF(text));
  const run = $derived(parsed.error ? null : dpllSteps(parsed.clauses, parsed.names));
  const steps = $derived(run ? run.steps : []);
  const s = $derived(steps.length ? steps[Math.min(step, steps.length - 1)] : null);
  function choose(id) { pid = id; text = DPLL_PRESETS.find((p) => p.id === id).text; step = 0; }
  $effect(() => { text; step = 0; });
  const why = { decision: 'quyết định', flip: 'đổi nhánh', unit: 'đơn vị' };
</script>

<div class="dx">
  <h4>SAT solver từng bước: DPLL</h4>
  <p class="dx-help">DPLL = <b>lan truyền đơn vị</b> (mệnh đề chỉ còn 1 literal thì buộc phải đúng) + <b>quyết định</b> (đoán giá trị một biến) + <b>quay lui</b> khi xung đột. Sửa công thức CNF bên dưới nếu muốn (mệnh đề cách nhau bởi “∧” hoặc dấu phẩy; phủ định dùng ¬ hoặc !).</p>
  <div class="dx-bar">
    <label>Ví dụ
      <select value={pid} onchange={(e) => choose(e.currentTarget.value)}>{#each DPLL_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select>
    </label>
  </div>
  <textarea rows="2" style="width:100%" bind:value={text} aria-label="Công thức CNF"></textarea>
  {#if parsed.error}
    <div class="dx-err" style="margin-top:8px">{parsed.error}</div>
  {:else if s}
    <Stepper bind:step total={steps.length} />
    <div class="dx-msg" class:dx-err={s.result === 'unsat'}>{s.msg}</div>
    <div class="dx-row2">
      <div>
        <h5>Mệnh đề</h5>
        <div class="dx-trail" style="flex-direction:column;align-items:stretch">
          {#each parsed.clauses as c, i}
            <span class="dx-pill {s.cstat[i] === 'sat' ? 'good' : s.cstat[i] === 'conflict' ? 'bad' : s.cstat[i] === 'unit' ? 'hot' : ''}">
              {clauseText(c, parsed.names)} <small>{s.cstat[i] === 'sat' ? '✓ thỏa' : s.cstat[i] === 'conflict' ? '✗ xung đột' : s.cstat[i] === 'unit' ? '→ đơn vị' : ''}</small>
            </span>
          {/each}
        </div>
      </div>
      <div>
        <h5>Gán hiện tại (mức quyết định {s.level})</h5>
        <div class="dx-trail">
          {#each s.trail as t}
            <span class="dx-pill {t.why === 'unit' ? '' : 'hot'}">{parsed.names[t.v - 1]}={t.val ? 'T' : 'F'} <small>({why[t.why]})</small></span>
          {:else}<span class="dx-k">(chưa gán)</span>{/each}
        </div>
        {#if s.result}
          <p class={s.result === 'sat' ? 'dx-ok' : 'dx-bad'} style="margin:8px 0 0">
            {s.result === 'sat' ? 'SAT: ' + parsed.names.map((n, i) => `${n}=${run.model[i + 1] ? 'T' : 'F'}`).join(', ') : 'UNSAT: không có phép gán nào thỏa mọi mệnh đề.'}
          </p>
        {/if}
      </div>
    </div>
  {/if}
</div>
