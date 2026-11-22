<script>
  import { binom, perm, fact, pascalRow, combinations, permutations, compositions, countCompositions, starsBars, pigeonBound, maxLoad } from './counting.js';

  let { tab: tabProp = 'pascal', n: nProp = 0, k: kProp = 0 } = $props();
  const TABS = { pascal: 'Tam giác Pascal', choose: 'Hoán vị & tổ hợp', stars: 'Sao và vạch', pigeon: 'Chuồng bồ câu' };

  let tab = $state(TABS[tabProp] ? tabProp : 'pascal');
  // Pascal
  let pn = $state(nProp && tabProp === 'pascal' ? nProp : 6);
  let sel = $state([nProp && tabProp === 'pascal' ? nProp : 6, kProp && tabProp === 'pascal' ? kProp : 2]);
  // Choose
  let cn = $state(nProp && tabProp === 'choose' ? nProp : 5);
  let ck = $state(kProp && tabProp === 'choose' ? kProp : 3);
  let ordered = $state(false);
  // Stars & bars
  let sn = $state(nProp && tabProp === 'stars' ? nProp : 6);
  let sk = $state(kProp && tabProp === 'stars' ? kProp : 3);
  let lower = $state(0);
  let sIdx = $state(0);
  // Pigeon
  let pg = $state(nProp && tabProp === 'pigeon' ? nProp : 10);
  let holes = $state(kProp && tabProp === 'pigeon' ? kProp : 4);
  let place = $state([]);

  const rows = $derived(Array.from({ length: pn + 1 }, (_, i) => pascalRow(i)));
  const selVal = $derived(binom(sel[0], sel[1]));
  const parents = $derived(sel[0] > 0 && sel[1] > 0 && sel[1] < sel[0] ? [binom(sel[0] - 1, sel[1] - 1), binom(sel[0] - 1, sel[1])] : null);
  const subsets = $derived(combinations(Math.min(sel[0], 7), Math.min(sel[1], 7), 40));

  const ckk = $derived(Math.min(ck, cn));
  const list = $derived(ordered ? permutations(cn, ckk, 120) : combinations(cn, ckk, 120));
  const total = $derived(ordered ? perm(cn, ckk) : binom(cn, ckk));

  const sols = $derived(compositions(sn, sk, lower, 400));
  const solTotal = $derived(countCompositions(sn, sk, lower));
  const curSol = $derived(sols[Math.min(sIdx, Math.max(0, sols.length - 1))] || []);
  const rest = $derived(Math.max(0, sn - lower * sk));

  const counts = $derived.by(() => {
    const c = Array(holes).fill(0);
    place.forEach((h) => { if (h < holes) c[h]++; });
    return c;
  });
  const bound = $derived(pigeonBound(pg, holes));
  const placed = $derived(place.filter((h) => h < holes).length);

  function pick(i, k) { sel = [i, k]; }
  function setPn(v) { pn = Math.max(0, Math.min(12, Number(v) || 0)); if (sel[0] > pn) sel = [pn, Math.min(sel[1], pn)]; }
  function addPigeon(h) { if (placed < pg) place = [...place.filter((x) => x < holes), h]; }
  function undo() { place = place.slice(0, -1); }
  function randomize() {
    place = Array.from({ length: pg }, () => Math.floor(Math.random() * holes));
  }
  function spread() {
    place = Array.from({ length: pg }, (_, i) => i % holes);
  }
  const str = (x) => x.toString();
</script>

<div class="dx cex">
  <h4>Minh hoạ đếm: tổ hợp, sao–vạch, chuồng bồ câu</h4>
  <div class="dx-tabs">
    {#each Object.entries(TABS) as [id, label]}
      <button type="button" class="sec" class:on={tab === id} onclick={() => (tab = id)}>{label}</button>
    {/each}
  </div>

  {#if tab === 'pascal'}
    <p class="dx-help">Mỗi ô là C(n, k) = C(n−1, k−1) + C(n−1, k): số tập con k phần tử của tập n phần tử. Bấm một ô để xem hai "cha" của nó và các tập con tương ứng.</p>
    <div class="dx-bar">
      <label>n = <input type="number" min="0" max="12" value={pn} onchange={(e) => setPn(e.currentTarget.value)} style="width:4.5rem" /></label>
      <span class="dx-k">Tổng hàng n = 2ⁿ = {(2n ** BigInt(pn)).toString()}… (mỗi phần tử chọn hoặc không chọn)</span>
    </div>
    <div class="tri">
      {#each rows as row, i}
        <div class="trow">
          {#each row as v, j}
            <button type="button" class="pc" class:s={sel[0] === i && sel[1] === j} class:p={parents && sel[0] - 1 === i && (sel[1] - 1 === j || sel[1] === j)} onclick={() => pick(i, j)}>{str(v)}</button>
          {/each}
        </div>
      {/each}
    </div>
    <p class="dx-msg">
      C({sel[0]}, {sel[1]}) = <b>{str(selVal)}</b>
      {#if parents} = C({sel[0] - 1}, {sel[1] - 1}) + C({sel[0] - 1}, {sel[1]}) = {str(parents[0])} + {str(parents[1])}
        <br />Ý nghĩa: tập con chứa phần tử cuối ({str(parents[0])} cách) hoặc không chứa ({str(parents[1])} cách).
      {:else} — ô biên của tam giác (bằng 1).{/if}
      {#if sel[0] <= 7}<br />Các tập con của {'{'}1..{sel[0]}{'}'} có {sel[1]} phần tử: {subsets.map((s) => '{' + s.join(',') + '}').join(' ')}{/if}
    </p>
  {/if}

  {#if tab === 'choose'}
    <p class="dx-help">Chọn k trong n phần tử. <b>Chỉnh hợp</b> P(n,k) tính thứ tự; <b>tổ hợp</b> C(n,k) = P(n,k)/k! không tính thứ tự — mỗi tổ hợp tương ứng k! chỉnh hợp.</p>
    <div class="dx-bar">
      <label>n <input type="number" min="1" max="8" bind:value={cn} style="width:4rem" /></label>
      <label>k <input type="number" min="0" max={cn} bind:value={ck} style="width:4rem" /></label>
      <button type="button" class="sec" class:on={!ordered} onclick={() => (ordered = false)}>Tổ hợp (không thứ tự)</button>
      <button type="button" class="sec" class:on={ordered} onclick={() => (ordered = true)}>Chỉnh hợp (có thứ tự)</button>
    </div>
    <p class="dx-msg">
      P({cn},{ckk}) = {cn}!/{cn - ckk}! = <b>{str(perm(cn, ckk))}</b> · C({cn},{ckk}) = P/{ckk}! = {str(perm(cn, ckk))}/{str(fact(ckk))} = <b>{str(binom(cn, ckk))}</b>
      · đang liệt kê <b>{ordered ? 'chỉnh hợp' : 'tổ hợp'}</b>: {str(total)} kết quả{list.length < Number(total) ? ` (hiện ${list.length} đầu)` : ''}.
    </p>
    <div class="dx-chips">
      {#each list as it}<span class="dx-chip mono">{ordered ? it.join('') : '{' + it.join(',') + '}'}</span>{/each}
    </div>
  {/if}

  {#if tab === 'stars'}
    <p class="dx-help">Chia n vật giống nhau vào k hộp = xếp n ngôi sao và k−1 vạch ngăn: số cách C(n+k−1, k−1). Kéo thanh trượt để duyệt từng nghiệm của x₁ + … + x<sub>k</sub> = n.</p>
    <div class="dx-bar">
      <label>n (sao) <input type="number" min="0" max="12" bind:value={sn} style="width:4rem" /></label>
      <label>k (hộp) <input type="number" min="1" max="6" bind:value={sk} style="width:4rem" /></label>
      <button type="button" class="sec" class:on={lower === 0} onclick={() => { lower = 0; sIdx = 0; }}>xᵢ ≥ 0</button>
      <button type="button" class="sec" class:on={lower === 1} onclick={() => { lower = 1; sIdx = 0; }}>xᵢ ≥ 1</button>
    </div>
    <p class="dx-msg">
      Số nghiệm = C({rest + sk - 1}, {sk - 1}) = <b>{str(solTotal)}</b>
      {#if lower === 1}· đã đặt sẵn 1 vật vào mỗi hộp, còn {rest} vật chia tự do{/if}.
    </p>
    {#if sols.length}
      <label class="sl">Nghiệm thứ <b>{Math.min(sIdx, sols.length - 1) + 1}</b> / {sols.length}{Number(solTotal) > sols.length ? '+' : ''}
        <input type="range" min="0" max={sols.length - 1} bind:value={sIdx} />
      </label>
      <div class="sb"><span class="dx-mono">{starsBars(curSol) || '(trống)'}</span></div>
      <p class="dx-mono">({curSol.join(', ')}) — tổng = {curSol.reduce((a, b) => a + b, 0)}</p>
      <div class="dx-chips">
        {#each sols.slice(0, 80) as s, i}
          <button type="button" class="sec chip" class:on={i === Math.min(sIdx, sols.length - 1)} onclick={() => (sIdx = i)}>{s.join(',')}</button>
        {/each}
      </div>
    {:else}
      <p class="dx-bad">Không có nghiệm: n nhỏ hơn tổng cận dưới.</p>
    {/if}
  {/if}

  {#if tab === 'pigeon'}
    <p class="dx-help">Có <b>{pg}</b> bồ câu và <b>{holes}</b> chuồng. Hãy bấm vào chuồng để thả từng con sao cho <em>chuồng đông nhất càng ít con càng tốt</em> — rồi xem có phá được cận ⌈n/k⌉ không.</p>
    <div class="dx-bar">
      <label>Số bồ câu n <input type="number" min="1" max="30" bind:value={pg} onchange={() => (place = [])} style="width:4.5rem" /></label>
      <label>Số chuồng k <input type="number" min="1" max="10" bind:value={holes} onchange={() => (place = [])} style="width:4.5rem" /></label>
      <button type="button" class="sec" onclick={undo} disabled={!place.length}>Hoàn tác</button>
      <button type="button" class="sec" onclick={() => (place = [])}>Xóa hết</button>
      <button type="button" class="sec" onclick={randomize}>Thả ngẫu nhiên</button>
      <button type="button" class="sec" onclick={spread}>Dàn đều</button>
    </div>
    <div class="holes">
      {#each counts as c, h}
        <button type="button" class="hole" class:full={c >= bound && placed === pg && c === maxLoad(counts)} onclick={() => addPigeon(h)}>
          <span class="hn">Chuồng {h + 1}</span>
          <span class="birds">{'●'.repeat(Math.min(c, 20))}</span>
          <b>{c}</b>
        </button>
      {/each}
    </div>
    <p class="dx-msg">
      Đã thả {placed}/{pg}. Chuồng đông nhất: <b>{maxLoad(counts)}</b> con. Cận chuồng bồ câu: ⌈{pg}/{holes}⌉ = <b>{bound}</b>.
      {#if placed === pg}
        {#if maxLoad(counts) >= bound}<span class="dx-ok">✓ Đúng nguyên lý: luôn có chuồng ≥ {bound} con — không cách nào tránh được.</span>{:else}Lỗi hiển thị.{/if}
      {:else}Tiếp tục thả…{/if}
    </p>
  {/if}

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li><b>Pascal:</b> chọn n = 6; bấm C(6,2) và chứng minh bằng lời vì sao bằng tổng hai ô cha. Kiểm tra tổng hàng = 2⁶.</li>
      <li><b>Hoán vị & tổ hợp:</b> n = 5, k = 3: đếm số chỉnh hợp trong mỗi nhóm cùng tập (k! = 6) rồi so với P/C.</li>
      <li><b>Sao–vạch:</b> số nghiệm nguyên không âm của x₁+x₂+x₃ = 6? Đổi sang xᵢ ≥ 1 — công thức thay đổi thế nào?</li>
      <li><b>Chuồng bồ câu:</b> 13 con, 12 chuồng — thử mọi cách thả để không có chuồng nào có 2 con.</li>
    </ol>
  </details>
</div>

<style>
  .tri { display: flex; flex-direction: column; align-items: center; gap: 3px; overflow-x: auto; padding: 6px 0; }
  .trow { display: flex; gap: 3px; }
  .pc { min-width: 2.3rem; padding: 3px 4px !important; background: #fff !important; color: #0f172a !important; border-color: #cbd5e1 !important; font-size: 0.78rem !important; }
  .pc.s { background: #0f766e !important; color: #fff !important; border-color: #0f766e !important; }
  .pc.p { background: #fef3c7 !important; border-color: #f59e0b !important; }
  .mono { font-family: ui-monospace, Menlo, monospace; }
  .sl { display: flex; gap: 10px; margin: 8px 0; } .sl input { flex: 1; }
  .sb { font-size: 1.4rem; letter-spacing: 2px; padding: 8px 12px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; margin: 6px 0; overflow-x: auto; }
  .chip { padding: 3px 8px !important; font-size: 0.8rem !important; }
  .holes { display: grid; grid-template-columns: repeat(auto-fit, minmax(90px, 1fr)); gap: 8px; margin: 8px 0; }
  .hole { display: flex; flex-direction: column; gap: 4px; align-items: center; min-height: 100px; background: #fffbeb !important; color: #78350f !important; border: 2px solid #f59e0b !important; border-radius: 10px !important; }
  .hole.full { background: #fee2e2 !important; border-color: #dc2626 !important; }
  .hn { font-size: 0.75rem; } .birds { color: #0369a1; font-size: 0.8rem; word-break: break-all; text-align: center; flex: 1; }
  p { margin: 6px 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
