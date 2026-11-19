<script>
  import KMap from './KMap.svelte';
  import { assignOf } from './logic2.js';

  let { n, names, va, vb, diff, equivalent, aImpB, bImpA, labelA, labelB, sopA, sopB } = $props();
  const diffMask = $derived(va.map((v, i) => (diff.includes(i) ? 1 : 0)));
  const rows = $derived(va.map((v, i) => ({ m: i, assign: assignOf(i, n), a: v, b: vb[i], bad: diff.includes(i) })));
</script>

<div class="cmp">
  {#if equivalent}
    <p class="verdict ok">✓ A ≡ B: hai biểu thức cho cùng bảng chân trị trên mọi {1 << n} hàng — tương đương logic.</p>
  {:else}
    <p class="verdict bad">
      ✗ A ≢ B: khác nhau ở {diff.length} hàng (m{diff.join(', m')}).
      {#if aImpB}Tuy nhiên A ⇒ B (mọi hàng A đúng thì B cũng đúng).{:else if bImpA}Tuy nhiên B ⇒ A.{:else}Cũng không có chiều kéo theo nào đúng với mọi hàng.{/if}
    </p>
  {/if}
  <div class="grid">
    <div class="tw">
      <table class="dx-t">
        <thead><tr><th>m</th>{#each names as v}<th>{v}</th>{/each}<th>A</th><th>B</th><th>A↔B</th></tr></thead>
        <tbody>
          {#each rows as r}
            <tr class:bad={r.bad}>
              <td>m{r.m}</td>{#each r.assign as b}<td>{b}</td>{/each}
              <td>{r.a}</td><td>{r.b}</td><td>{r.bad ? '✗' : '✓'}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
    <div class="kms">
      <KMap {n} values={va} {names} readonly title={`K-map A: ${sopA}`} />
      <KMap {n} values={vb} {names} readonly title={`K-map B: ${sopB}`} />
      <KMap {n} values={diffMask} {names} readonly title="Khác biệt A ⊕ B (ô 1 = hai bên lệch)" />
    </div>
  </div>
</div>

<style>
  .verdict { margin: 0 0 10px; padding: 8px 10px; border-radius: 8px; font-size: 0.92rem; }
  .verdict.ok { background: #f0fdfa; border: 1px solid #99f6e4; color: #115e59; }
  .verdict.bad { background: #fef2f2; border: 1px solid #fecaca; color: #991b1b; }
  .grid { display: grid; grid-template-columns: minmax(220px, 0.8fr) 1.4fr; gap: 12px; }
  @media (max-width: 800px) { .grid { grid-template-columns: 1fr; } }
  .kms { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }
  tr.bad { background: #fee2e2; }
</style>
