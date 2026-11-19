<script>
  import Stepper from '../shared/Stepper.svelte';
  import { PUMP_LANGS, evaluate, pump, IS } from './pumping.js';

  let { kind: kindProp = 'regular', lang = '', p: pProp = 3 } = $props();
  const kind = kindProp === 'cfl' ? 'cfl' : 'regular';
  const langs = PUMP_LANGS[kind];
  let lid = $state(langs.some((l) => l.id === lang) ? lang : langs[0].id);
  let P = $state(Math.max(1, Math.min(kind === 'cfl' ? 4 : 7, Number(pProp) || 3)));
  let step = $state(0);
  $effect(() => { lid; P; step = 0; });
  const L = $derived(langs.find((l) => l.id === lid));
  const w = $derived(L.word(P));
  const all = $derived(evaluate(L, kind, w, P));
  const k = $derived(Math.min(step, Math.max(0, all.length - 1)));
  const cur = $derived(all[k]);
  const seen = $derived(all.slice(0, k + 1));
  const survivors = $derived(seen.filter((r) => r.survives).length);
  const totalSurv = $derived(all.filter((r) => r.survives).length);
  const names = kind === 'cfl' ? ['u', 'v', 'x', 'y', 'z'] : ['x', 'y', 'z'];
  const pumpedIdx = kind === 'cfl' ? [1, 3] : [1];
  function nextSurv() { const j = all.findIndex((r, i) => i > k && r.survives); if (j >= 0) step = j; }
  const conclusion = $derived(totalSurv === 0
    ? `Không có cách chia hợp lệ nào bơm được (${all.length} cách) ⇒ w = “${w}” là phản chứng: L KHÔNG ${kind === 'regular' ? 'chính quy' : 'phi ngữ cảnh'}.`
    : `Có ${totalSurv}/${all.length} cách chia mà mọi xyⁱz vẫn thuộc L ⇒ w này không loại được L (đúng như mong đợi vì L ${kind === 'regular' ? 'chính quy' : 'phi ngữ cảnh'}; với p đủ lớn thì luôn có cách bơm).`);
</script>

<div class="dx">
  <h4>Trò chơi bổ đề bơm ({kind === 'regular' ? 'ngôn ngữ chính quy' : 'ngôn ngữ phi ngữ cảnh'})</h4>
  <p class="dx-help">Đối thủ chọn p, bạn chọn chuỗi w ∈ L với |w| ≥ p. Đối thủ chia w = {kind === 'regular' ? 'xyz với |xy| ≤ p, |y| ≥ 1' : 'uvxyz với |vxy| ≤ p, |vy| ≥ 1'}; bạn thắng nếu có i để {kind === 'regular' ? 'xyⁱz' : 'uvⁱxyⁱz'} ∉ L. Bấm Bước tiếp để duyệt từng cách chia.</p>
  <div class="dx-bar">
    <label>Ngôn ngữ <select bind:value={lid}>{#each langs as l}<option value={l.id}>{l.name}</option>{/each}</select></label>
    <label>p = <b>{P}</b> <input type="range" min="1" max={kind === 'cfl' ? 4 : 7} bind:value={P} /></label>
  </div>
  <div class="dx-msg">w = <span class="dx-mono">{w}</span> (|w| = {w.length}). Số cách chia: <b>{all.length}</b>.</div>
  {#if cur}
    <Stepper bind:step total={all.length} />
    <div class="dx-bar"><button class="sec" onclick={nextSurv} disabled={!all.some((r, i) => i > k && r.survives)}>⏭ Cách bơm được kế tiếp</button>
      <span class="dx-k">Đã xét {k + 1}/{all.length} · bơm được: {survivors}</span></div>
    <div style="overflow-x:auto"><div class="dx-trail dx-mono" style="font-size:1.1rem;min-height:2.6rem">
      {#each cur.parts as part, i}
        <span style="padding:3px 8px;border-radius:6px;border:2px solid {pumpedIdx.includes(i) ? '#f59e0b' : '#94a3b8'};background:{pumpedIdx.includes(i) ? '#fef3c7' : '#f8fafc'}"><small class="dx-k">{names[i]}</small> {part || 'ε'}</span>
      {/each}
    </div></div>
    <table class="dx-t dx-mono" style="margin-top:8px"><thead><tr><th>i</th><th>chuỗi sau khi bơm</th><th>∈ L?</th></tr></thead>
      <tbody>{#each IS as i}{@const s = pump(cur.parts, kind, i)}<tr><td>{i}</td><td style="text-align:left;max-width:240px;overflow-wrap:anywhere">{s || 'ε'}</td><td class={cur.res[i] ? 'dx-ok' : 'dx-bad'}>{cur.res[i] ? '✓ thuộc' : '✗ ngoài L'}</td></tr>{/each}</tbody></table>
    <p class={cur.survives ? 'dx-ok' : 'dx-bad'}>{cur.survives ? 'Cách chia này bơm được với mọi i đã thử.' : `Cách chia này thua: i = ${cur.res.findIndex((x) => !x)} đưa chuỗi ra ngoài L.`}</p>
    {#if k === all.length - 1}<div class="dx-msg">{conclusion}</div>{/if}
  {/if}
</div>
