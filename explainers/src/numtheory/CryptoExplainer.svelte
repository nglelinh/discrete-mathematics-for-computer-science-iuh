<script>
  import Stepper from '../shared/Stepper.svelte';
  import { crtSolve, millerRabinSteps, isProbablePrime, dhSteps, modPow } from './crypto.js';

  let { tab: tabProp = 'crt', n: nProp = '561', a: aProp = '2' } = $props();
  let tab = $state(['crt', 'miller', 'dh'].includes(tabProp) ? tabProp : 'crt');
  const int = (v, lo, hi, d) => { const x = Math.floor(Number(v)); return Number.isFinite(x) ? Math.max(lo, Math.min(hi, x)) : d; };

  // ---- CRT
  let eq = $state([[3, 2], [5, 3], [7, 2]]);
  let cs = $state(0);
  $effect(() => { JSON.stringify(eq); cs = 0; });
  const crt = $derived(crtSolve(eq.map((e) => int(e[1], 0, 9999, 0)), eq.map((e) => int(e[0], 2, 9999, 2))));

  // ---- Miller–Rabin
  let n = $state(int(nProp, 5, 2000000000, 561));
  let base = $state(int(aProp, 2, 1000000, 2));
  let ms = $state(0);
  $effect(() => { n; base; ms = 0; });
  const mr = $derived(millerRabinSteps(n, base));
  const mrTotal = $derived(mr.error ? 1 : mr.seq.length + 2);
  const quick = $derived([2, 3, 5, 7].map((b) => ({ b, r: millerRabinSteps(n, b) })));
  const verdict = $derived(n % 2 === 0 ? 'chẵn ⇒ hợp số' : isProbablePrime(n, [2, 3, 5, 7, 11, 13, 17]) ? 'rất có thể nguyên tố' : 'hợp số');

  // ---- Diffie–Hellman
  let dp = $state(23), dg = $state(5), da = $state(6), db = $state(15), ds = $state(0);
  $effect(() => { dp; dg; da; db; ds = 0; });
  const pOk = $derived(dp >= 5 && dp <= 100003 && isProbablePrime(dp));
  const dh = $derived(pOk ? dhSteps(dp, int(dg, 2, dp - 1, 2), int(da, 2, dp - 2, 2), int(db, 2, dp - 2, 2)) : null);
  const dhMsgs = $derived(dh ? [
    `Công khai: p = ${dh.p}, g = ${dh.g}. Eve và mọi người đều thấy.`,
    `Alice chọn bí mật a = ${dh.a}, gửi A = g^a mod p = ${dh.g}^${dh.a} mod ${dh.p} = ${dh.A}.`,
    `Bob chọn bí mật b = ${dh.b}, gửi B = g^b mod p = ${dh.g}^${dh.b} mod ${dh.p} = ${dh.B}.`,
    `Alice tính B^a mod p = ${dh.B}^${dh.a} mod ${dh.p} = ${dh.sA}.  Bob tính A^b mod p = ${dh.A}^${dh.b} mod ${dh.p} = ${dh.sB}.`,
    `${dh.equal ? '✓ Hai bên cùng có K = ' + dh.sA : '✗ không khớp'} (vì (g^a)^b = (g^b)^a = g^{ab}).`,
    `Eve chỉ biết p, g, A, B. Cô thử g¹, g², … cho tới khi trúng A: cần ${dh.eve.tries} phép thử (a = ${dh.eve.found}) ⇒ K = ${dh.eve.secret}. Với p nhỏ thì phá được; với p ~ 2048 bit thì không khả thi.`
  ] : []);
  function addEq() { if (eq.length < 4) eq = [...eq, [11, 1]]; }
  function delEq() { if (eq.length > 2) eq = eq.slice(0, -1); }
</script>

<div class="dx">
  <h4>Số học cho mật mã: CRT, Miller–Rabin, Diffie–Hellman</h4>
  <div class="dx-tabs">
    <button class={tab === 'crt' ? 'on' : 'sec'} onclick={() => (tab = 'crt')}>Định lý số dư Trung Hoa</button>
    <button class={tab === 'miller' ? 'on' : 'sec'} onclick={() => (tab = 'miller')}>Miller–Rabin</button>
    <button class={tab === 'dh' ? 'on' : 'sec'} onclick={() => (tab = 'dh')}>Diffie–Hellman</button>
  </div>

  {#if tab === 'crt'}
    <p class="dx-help">Giải hệ x ≡ aᵢ (mod mᵢ) với các mᵢ đôi một nguyên tố cùng nhau: x = Σ aᵢ·Mᵢ·yᵢ mod M, với M = ∏mᵢ, Mᵢ = M/mᵢ, yᵢ = Mᵢ⁻¹ mod mᵢ.</p>
    <div class="dx-bar" style="flex-wrap:wrap">
      {#each eq as e, i}<label>x ≡ <input type="number" min="0" bind:value={e[1]} style="width:4.5rem" /> (mod <input type="number" min="2" bind:value={e[0]} style="width:4.5rem" />)</label>{/each}
      <button class="sec" onclick={addEq} disabled={eq.length >= 4}>＋ thêm</button><button class="sec" onclick={delEq} disabled={eq.length <= 2}>− bớt</button>
    </div>
    {#if crt.error}<div class="dx-err">{crt.error}</div>
    {:else}
      <Stepper bind:step={cs} total={crt.steps.length + 2} />
      <div class="dx-msg">
        {#if cs === 0}M = {crt.steps.map((s) => s.mi).join(' · ')} = <b>{crt.M}</b>. Nghiệm duy nhất trong [0, {crt.M}).
        {:else if cs <= crt.steps.length}{@const s = crt.steps[cs - 1]}Phương trình {cs}: M{cs} = {crt.M}/{s.mi} = {s.Mi}; y{cs} = {s.Mi}⁻¹ mod {s.mi} = {s.yi}; số hạng a·M·y = {s.ai}·{s.Mi}·{s.yi} = <b>{s.term}</b>.
        {:else}Tổng = {crt.steps.map((s) => s.term).join(' + ')} = {crt.sum}; x = {crt.sum} mod {crt.M} = <b>{crt.x}</b>.{/if}
      </div>
      <div style="overflow-x:auto"><table class="dx-t dx-mono"><thead><tr><th>i</th><th>aᵢ</th><th>mᵢ</th><th>Mᵢ</th><th>yᵢ</th><th>aᵢMᵢyᵢ</th></tr></thead>
        <tbody>{#each crt.steps as s, i}{#if i < cs}<tr><td>{i + 1}</td><td>{s.ai}</td><td>{s.mi}</td><td>{s.Mi}</td><td>{s.yi}</td><td>{s.term}</td></tr>{/if}{/each}</tbody></table></div>
      {#if cs === crt.steps.length + 1}<p class="dx-ok">Kiểm tra: {#each crt.check as c}<span class="dx-mono">{crt.x} mod {c.mi} = {c.ai} {c.ok ? '✓' : '✗'}</span>{' · '}{/each}</p>{/if}
    {/if}

  {:else if tab === 'miller'}
    <p class="dx-help">Viết n − 1 = 2ˢ·d (d lẻ), tính a^d, rồi bình phương liên tiếp. n “qua” cơ sở a nếu dãy bắt đầu bằng 1 hoặc chứa −1 (≡ n−1) trước khi hết. Nếu không: a là <b>nhân chứng</b> n là hợp số.</p>
    <div class="dx-bar">
      <label>Ví dụ <select onchange={(e) => { const [x, y] = e.currentTarget.value.split(','); n = +x; base = +y; }}>
        <option value="561,2">561 (Carmichael)</option><option value="2047,2">2047 (giả nguyên tố mạnh, a = 2)</option><option value="2047,3">2047, a = 3</option><option value="221,174">221 (a nói dối)</option><option value="1000003,2">1000003 (nguyên tố)</option><option value="1000001,2">1000001 = 101·9901</option></select></label>
      <label>n <input type="number" bind:value={n} min="5" max="2000000000" style="width:8.5rem" /></label>
      <label>a <input type="number" bind:value={base} min="2" style="width:6rem" /></label>
    </div>
    {#if mr.error}<div class="dx-err">{mr.error}</div>
    {:else}
      <Stepper bind:step={ms} total={mrTotal} />
      <div class="dx-msg">
        {#if ms === 0}Kiểm tra n = {n} với cơ sở a = {base}.
        {:else if ms === 1}n − 1 = {n - 1} = 2<sup>{mr.s}</sup> · {mr.d} (s = {mr.s}, d = {mr.d}).
        {:else}{@const r = ms - 2}{#if r < mr.seq.length}{r === 0 ? `x₀ = a^d mod n = ${base}^${mr.d} mod ${n} = ` : `x${r} = x${r - 1}² mod n = `}<b>{mr.seq[r]}</b>{mr.seq[r] === 1 && r === 0 ? ' = 1 ⇒ qua.' : ''}{mr.seq[r] === n - 1 && r < mr.s ? ' = n−1 ⇒ qua.' : ''}{:else}…{/if}{/if}
      </div>
      <div class="dx-trail dx-mono">{#each mr.seq as v, r}{#if ms >= r + 2}<span class="dx-pill {v === 1 || v === n - 1 ? 'hot' : ''}">x{r} = {v}</span>{/if}{/each}</div>
      {#if ms === mrTotal - 1}<p class={mr.pass ? 'dx-ok' : 'dx-bad'}>{mr.pass ? `n = ${n} QUA cơ sở ${base} (có thể nguyên tố${verdict.startsWith('hợp') ? ', nhưng thực ra là hợp số: a nói dối' : ''}).` : `n = ${n} TRƯỢT: a = ${base} là nhân chứng ⇒ n chắc chắn là hợp số.`}</p>{/if}
      <h5>Thử nhanh các cơ sở 2, 3, 5, 7</h5>
      <div class="dx-trail">{#each quick as q}<span class="dx-pill {q.r.error ? '' : q.r.pass ? 'good' : 'hot'}">a={q.b}: {q.r.error ? '—' : q.r.pass ? 'qua' : 'trượt'}</span>{/each}</div>
      <p class="dx-k">Kết luận (nhiều cơ sở): n {verdict}.</p>
    {/if}

  {:else}
    <p class="dx-help">Alice và Bob thống nhất khóa K qua kênh công khai nhờ tính khó của logarit rời rạc. Dưới đây dùng p nhỏ để Eve phá được; p thật có ≥ 2048 bit.</p>
    <div class="dx-bar" style="flex-wrap:wrap">
      <label>p <input type="number" bind:value={dp} min="5" max="100003" style="width:6.5rem" /></label>
      <label>g <input type="number" bind:value={dg} min="2" style="width:5rem" /></label>
      <label>a (Alice) <input type="number" bind:value={da} min="2" style="width:5rem" /></label>
      <label>b (Bob) <input type="number" bind:value={db} min="2" style="width:5rem" /></label>
    </div>
    {#if !pOk}<div class="dx-err">p phải là số nguyên tố trong [5, 100003].</div>
    {:else}
      <Stepper bind:step={ds} total={dhMsgs.length} />
      <div class="dx-msg">{dhMsgs[Math.min(ds, dhMsgs.length - 1)]}</div>
      <div class="dx-grid2">
        <div class="dx-card"><h5>Alice</h5><div class="dx-mono">bí mật a = {ds >= 1 ? dh.a : '?'}<br />gửi A = {ds >= 1 ? dh.A : '?'}<br />K = {ds >= 3 ? dh.sA : '?'}</div></div>
        <div class="dx-card"><h5>Bob</h5><div class="dx-mono">bí mật b = {ds >= 2 ? dh.b : '?'}<br />gửi B = {ds >= 2 ? dh.B : '?'}<br />K = {ds >= 3 ? dh.sB : '?'}</div></div>
      </div>
      <p class="dx-k">g = {dh.g} có thể không phải căn nguyên thủy; vẫn đúng, chỉ là tập khóa nhỏ hơn.</p>
    {/if}
  {/if}
</div>
