<script>
  import Stepper from '../shared/Stepper.svelte';
  import { SQRT2_STEPS, fractionTest, nearMisses, euclidStep, isPrimeNum } from './contradiction.js';

  let { tab: tabProp = 'sqrt2', a: aProp = '14', b: bProp = '10', primes = '2,3,5,7' } = $props();
  let tab = $state(tabProp === 'primes' ? 'primes' : 'sqrt2');
  let step = $state(0);
  let a = $state(Number(aProp) || 14), b = $state(Number(bProp) || 10);
  const test = $derived(fractionTest(Number(a), Number(b)));
  const near = nearMisses(8);
  const kindLabel = { assume: 'Giả sử', setup: 'Thiết lập', derive: 'Suy ra', contradiction: 'MÂU THUẪN', conclude: 'Kết luận' };

  let text = $state(primes);
  let pstep = $state(0);
  $effect(() => { text; pstep = 0; });
  const list = $derived([...new Set(text.split(/[,\s]+/).map(Number).filter((x) => Number.isInteger(x)))]);
  const err = $derived(list.length < 1 || list.length > 7 ? 'Nhập 1–7 số nguyên tố.' : list.some((x) => !isPrimeNum(x)) ? 'Mọi số phải là số nguyên tố.' : list.reduce((p, x) => p * x, 1) > 1e12 ? 'Tích quá lớn.' : null);
  const e = $derived(err ? null : euclidStep(list));
  const plines = $derived(e ? [
    `Giả sử chỉ có hữu hạn số nguyên tố, và đây là tất cả: ${list.join(', ')}.`,
    `Đặt N = (${list.join(' · ')}) + 1 = ${e.N}.`,
    `N chia cho mỗi số trong danh sách đều dư 1: ${e.remainders.map((r) => `${e.N} mod ${r.p} = ${r.r}`).join('; ')}. Vậy không số nào trong danh sách chia hết N.`,
    `N > 1 nên có ước nguyên tố nhỏ nhất q = ${e.q}${e.q === e.N ? ' (chính N là nguyên tố)' : ''}.`,
    `q = ${e.q} không nằm trong danh sách (vì không chia hết N) ⇒ MÂU THUẪN với “danh sách là mọi số nguyên tố”. Vậy có vô hạn số nguyên tố. ∎`] : []);
</script>

<div class="dx">
  <h4>Chứng minh phản chứng từng bước</h4>
  <div class="dx-tabs">
    <button class={tab === 'sqrt2' ? 'on' : 'sec'} onclick={() => (tab = 'sqrt2')}>√2 là số vô tỷ</button>
    <button class={tab === 'primes' ? 'on' : 'sec'} onclick={() => (tab = 'primes')}>Vô hạn số nguyên tố</button>
  </div>
  {#if tab === 'sqrt2'}
    <Stepper bind:step total={SQRT2_STEPS.length} />
    <ol class="ct-list">
      {#each SQRT2_STEPS as s, i}{#if i <= step}<li class="ct {s.kind}" class:cur={i === step}><b class="ct-tag">{kindLabel[s.kind]}</b> {s.text}</li>{/if}{/each}
    </ol>
    <h5 style="margin-top:12px">Thử một phân số a/b: có bao giờ a² = 2b² không?</h5>
    <div class="dx-bar"><label>a <input type="number" bind:value={a} style="width:5rem" /></label><label>b <input type="number" bind:value={b} style="width:5rem" /></label></div>
    {#if test.error}<div class="dx-err">{test.error}</div>
    {:else}
      <div class="dx-msg">{a}/{b}{test.g > 1 ? ` rút gọn: ${test.ra}/${test.rb}` : ' đã tối giản'}: a² = {test.sq}, 2b² = {test.dbl} ⇒ chênh <b class="dx-bad">{test.diff}</b> ≠ 0. a {test.aEven ? 'chẵn' : 'lẻ'}, b {test.bEven ? 'chẵn' : 'lẻ'}{test.aEven && test.bEven ? ' (cùng chẵn: không thể tối giản)' : ''}.</div>
    {/if}
    <div style="overflow-x:auto"><table class="dx-t dx-mono"><thead><tr><th>b</th>{#each near as m}<th>{m.b}</th>{/each}</tr></thead>
      <tbody><tr><td>a ≈ b√2</td>{#each near as m}<td>{m.a}</td>{/each}</tr><tr><td>a² − 2b²</td>{#each near as m}<td class="dx-bad">{m.diff}</td>{/each}</tr></tbody></table></div>
    <p class="dx-k">Không bao giờ bằng 0: đúng như chứng minh.</p>
  {:else}
    <p class="dx-help">Nhập một danh sách số nguyên tố, coi như “tất cả”, rồi để chứng minh của Euclid tìm số nguyên tố bị thiếu.</p>
    <div class="dx-bar"><label>Danh sách <input type="text" bind:value={text} class="dx-mono" style="width:12rem;max-width:100%" /></label></div>
    {#if err}<div class="dx-err">{err}</div>
    {:else}
      <Stepper bind:step={pstep} total={plines.length} />
      <ol class="ct-list">{#each plines as l, i}{#if i <= pstep}<li class="ct {i === plines.length - 1 ? 'contradiction' : 'derive'}" class:cur={i === pstep}>{l}</li>{/if}{/each}</ol>
      {#if pstep === plines.length - 1}<p class="dx-ok">Số nguyên tố mới: <b>{e.q}</b>{e.q === e.N ? '' : ` (N = ${e.N} = ${e.q} × ${e.N / e.q})`}.</p>{/if}
    {/if}
  {/if}
</div>

<style>
  .ct-list { list-style: none; padding: 0; margin: 8px 0; display: flex; flex-direction: column; gap: 6px; }
  .ct { border-left: 4px solid #94a3b8; background: #f8fafc; padding: 6px 10px; border-radius: 6px; }
  .ct.cur { box-shadow: 0 0 0 2px #f59e0b; }
  .ct.assume { border-color: #2563eb; background: #eff6ff; }
  .ct.contradiction { border-color: #dc2626; background: #fef2f2; font-weight: 600; }
  .ct.conclude { border-color: #16a34a; background: #f0fdf4; }
  .ct-tag { font-size: .75rem; margin-right: 6px; color: #475569; }
</style>
