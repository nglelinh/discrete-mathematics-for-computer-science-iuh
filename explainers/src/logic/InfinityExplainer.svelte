<script>
  import Stepper from '../shared/Stepper.svelte';
  import { cantorPair, unpair, diagonalFlip, randomRows, HILBERT, hotelAfter } from './infinity.js';

  let { tab: tabProp = 'diagonal', scenario = 'bus' } = $props();
  let tab = $state(['diagonal', 'hilbert', 'pairing'].includes(tabProp) ? tabProp : 'diagonal');

  // ---- đường chéo Cantor
  const N = 6;
  let seed = $state(3);
  let rows = $state(randomRows(N, 3));
  let dstep = $state(0);
  const d = $derived(diagonalFlip(rows));
  const k = $derived(Math.min(dstep, N + 1));
  function reroll() { seed += 1; rows = randomRows(N, seed); dstep = 0; }
  function toggle(i, j) { rows[i][j] = 1 - rows[i][j]; dstep = 0; }
  const dmsg = $derived(k === 0
    ? 'Giả sử có thể liệt kê MỌI dãy nhị phân vô hạn thành danh sách s₁, s₂, s₃, … (bảng dưới chỉ hiện 6 chữ số đầu). Ta sẽ dựng dãy d không có trong danh sách.'
    : k <= N
      ? `Chữ số thứ ${k} của d = đảo chữ số thứ ${k} của s${k} (${rows[k - 1][k - 1]} → ${d[k - 1]}). Vậy d khác s${k} ở vị trí ${k}.`
      : 'd khác mọi dãy sᵢ (ở đúng vị trí i) nên d KHÔNG có trong danh sách — mâu thuẫn. Vậy tập các dãy nhị phân vô hạn là KHÔNG ĐẾM ĐƯỢC.');

  // ---- khách sạn Hilbert
  let sid = $state(HILBERT.some((s) => s.id === scenario) ? scenario : 'bus');
  let hstep = $state(0);
  $effect(() => { sid; hstep = 0; });
  const R = 14;
  const SC = $derived(HILBERT.find((s) => s.id === sid));
  const after = $derived(hotelAfter(SC, R));
  const oldOnly = $derived.by(() => {
    const out = Array(R).fill(null);
    for (let n = 1; n <= 3 * R; n++) { const r = SC.oldRoom(n); if (r <= R) out[r - 1] = 'a' + n; }
    return out;
  });
  const hrow = $derived(hstep === 0 ? Array.from({ length: R }, (_, i) => 'a' + (i + 1)) : hstep === 1 ? oldOnly : after);
  const hmsg = $derived(hstep === 0 ? 'Khách sạn có vô hạn phòng, phòng nào cũng có khách (a1, a2, …).' : hstep === 1 ? 'Khách cũ chuyển phòng: a1→' + SC.oldRoom(1) + ', a2→' + SC.oldRoom(2) + ', a3→' + SC.oldRoom(3) + ', …' : SC.explain);

  // ---- ghép cặp ℕ×ℕ
  let pstep = $state(0);
  const G = 7, TOT = 28;
  const cur = $derived(unpair(Math.min(pstep, TOT - 1)));
  const pmsg = $derived(`Số thứ tự ${Math.min(pstep, TOT - 1)} ↔ cặp (${cur[0]}, ${cur[1]}), vì ⟨i, j⟩ = (i+j)(i+j+1)/2 + j = ${cantorPair(cur[0], cur[1])}. Đi hết từng đường chéo i+j = const thì mọi cặp đều có số thứ tự ⇒ ℕ×ℕ đếm được (và ℚ cũng vậy).`);
</script>

<div class="dx">
  <h4>Vô hạn: đường chéo Cantor · khách sạn Hilbert · ghép cặp</h4>
  <div class="dx-tabs">
    <button class={tab === 'diagonal' ? 'on' : 'sec'} onclick={() => (tab = 'diagonal')}>Đường chéo Cantor</button>
    <button class={tab === 'hilbert' ? 'on' : 'sec'} onclick={() => (tab = 'hilbert')}>Khách sạn Hilbert</button>
    <button class={tab === 'pairing' ? 'on' : 'sec'} onclick={() => (tab = 'pairing')}>Ghép cặp ℕ×ℕ</button>
  </div>

  {#if tab === 'diagonal'}
    <p class="dx-help">Bấm vào chữ số để đổi, hoặc tạo dãy ngẫu nhiên khác. Dãy d luôn khác mọi dòng, dù bảng là gì.</p>
    <div class="dx-bar"><button class="sec" onclick={reroll}>🎲 Bảng khác</button></div>
    <Stepper bind:step={dstep} total={N + 2} />
    <div class="dx-msg">{dmsg}</div>
    <div style="overflow-x:auto"><table class="dx-t dx-mono" style="margin:0 auto">
      <tbody>
        {#each rows as r, i}
          <tr><th>s{i + 1}</th>{#each r as v, j}<td><button class="sec" style="padding:2px 8px;min-width:2rem;{i === j && k > i ? 'background:#fde68a;border-color:#f59e0b' : ''}" onclick={() => toggle(i, j)}>{v}</button></td>{/each}<td>…</td></tr>
        {/each}
        <tr><th style="color:#b91c1c">d</th>{#each d as v, j}<td style="font-weight:700;color:#b91c1c;background:{k > j ? '#fee2e2' : '#f8fafc'}">{k > j ? v : '?'}</td>{/each}<td>…</td></tr>
      </tbody></table></div>
  {:else if tab === 'hilbert'}
    <p class="dx-help">Khách sạn vô hạn phòng đã kín khách vẫn nhận thêm khách. Chọn kịch bản rồi bấm Bước tiếp.</p>
    <div class="dx-bar"><label>Kịch bản <select bind:value={sid}>{#each HILBERT as s}<option value={s.id}>{s.name}</option>{/each}</select></label></div>
    <Stepper bind:step={hstep} total={3} />
    <div class="dx-msg">{hmsg}</div>
    <div style="overflow-x:auto"><div style="display:flex;gap:4px;width:max-content;margin:0 auto">
      {#each hrow as who, i}
        <div style="text-align:center"><small class="dx-k">phòng {i + 1}</small>
          <div class="dx-mono" style="width:46px;height:40px;display:flex;align-items:center;justify-content:center;border:2px solid {who ? (who[0] === 'b' ? '#16a34a' : '#475569') : '#cbd5e1'};background:{who ? (who[0] === 'b' ? '#dcfce7' : '#e0f2fe') : '#f8fafc'};border-radius:6px;font-size:.78rem;font-weight:700">{who ?? ''}</div></div>
      {/each}
    </div></div>
    <p class="dx-k">Xanh dương = khách cũ aₙ, xanh lá = khách mới. Ô trống = phòng chưa có ai trong lúc dời.</p>
  {:else}
    <p class="dx-help">Đánh số các cặp (i, j) theo từng đường chéo: mỗi cặp nhận đúng một số tự nhiên và ngược lại.</p>
    <Stepper bind:step={pstep} total={TOT} />
    <div class="dx-msg">{pmsg}</div>
    <div style="overflow-x:auto"><table class="dx-t dx-mono" style="margin:0 auto"><thead><tr><th>i＼j</th>{#each Array(G) as _, j}<th>{j}</th>{/each}</tr></thead>
      <tbody>{#each Array(G) as _, i}<tr><th>{i}</th>{#each Array(G) as __, j}{@const n = cantorPair(i, j)}<td style="background:{cur[0] === i && cur[1] === j ? '#fde68a' : n < pstep ? '#dcfce7' : '#fff'};font-weight:{cur[0] === i && cur[1] === j ? 800 : 500};color:{n <= pstep ? '#0f172a' : '#cbd5e1'}">{n}</td>{/each}</tr>{/each}</tbody></table></div>
  {/if}
</div>
