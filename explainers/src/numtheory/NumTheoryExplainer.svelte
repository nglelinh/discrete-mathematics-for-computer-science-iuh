<script>
  import { extendedEuclid, euclidSteps, mod, modInverse, gcd, solveLinearCongruence, modPowSteps, modPow, sieve, factorize, phi, rsaKeys, rsaEncrypt, rsaDecrypt, modTable } from './numtheory.js';

  let { tab: tabProp = 'euclid', a: aProp = '', b: bProp = '' } = $props();
  const TABS = { euclid: 'Euclid & Bézout', modular: 'Đồng dư', fastexp: 'Lũy thừa nhanh', sieve: 'Sàng nguyên tố', rsa: 'RSA đồ chơi' };
  let tab = $state(TABS[tabProp] ? tabProp : 'euclid');
  const num = (s, d) => { const v = Math.trunc(Number(s)); return Number.isFinite(v) ? v : d; };

  // Euclid
  let ea = $state(aProp || '252'), eb = $state(bProp || '198');
  const A = $derived(Math.max(0, Math.min(1e9, num(ea, 0)))), B = $derived(Math.max(0, Math.min(1e9, num(eb, 0))));
  const eu = $derived(A || B ? extendedEuclid(A, B) : null);
  const plain = $derived(euclidSteps(A, B));
  let eShow = $state(99);

  // Modular
  let mn = $state(aProp ? Math.max(2, Math.min(30, num(aProp, 12))) : 12);
  let mop = $state('+');
  let mval = $state(7);
  let ca = $state('5'), cc = $state('3');
  const N = $derived(Math.max(2, Math.min(24, num(mn, 12))));
  const table = $derived(modTable(N, mop));
  const units = $derived(Array.from({ length: N }, (_, i) => i).filter((i) => gcd(i, N) === 1));
  const lin = $derived(solveLinearCongruence(mod(num(ca, 1), N), mod(num(cc, 0), N), N));

  // Fast exp
  let fb = $state('7'), fe = $state('13'), fm = $state('11');
  const FM = $derived(Math.max(2, Math.min(1e6, num(fm, 11))));
  const fp = $derived(modPowSteps(mod(num(fb, 2), FM), Math.max(1, Math.min(1e6, num(fe, 1))), FM));

  // Sieve
  let sn = $state(60), sk = $state(0);
  const SN = $derived(Math.max(10, Math.min(200, num(sn, 60))));
  const sv = $derived(sieve(SN));
  const crossedUpTo = $derived.by(() => {
    const m = new Map();
    sv.steps.slice(0, sk).forEach((s, i) => s.crossed.forEach((x) => m.set(x, s.p)));
    return m;
  });
  $effect(() => { if (sk > sv.steps.length) sk = sv.steps.length; });

  // RSA
  let rp = $state('61'), rq = $state('53'), re = $state('17'), rm = $state('65');
  const keys = $derived(rsaKeys(num(rp, 0), num(rq, 0), num(re, 0)));
  const M = $derived(keys.error ? null : Math.max(0, Math.min(keys.n - 1, num(rm, 0))));
  const cipher = $derived(keys.error ? null : rsaEncrypt(M, keys));
  const plainBack = $derived(keys.error ? null : rsaDecrypt(cipher, keys));
  const wrongDecrypt = $derived(keys.error || keys.n < 3 ? null : rsaDecrypt(cipher, { ...keys, d: keys.d + 1 }));

  const cp = (i, n, R) => [R + R * Math.sin((2 * Math.PI * i) / n), R - R * Math.cos((2 * Math.PI * i) / n)];
</script>

<div class="dx nex">
  <h4>Minh hoạ lý thuyết số</h4>
  <div class="dx-tabs">
    {#each Object.entries(TABS) as [id, l]}<button type="button" class="sec" class:on={tab === id} onclick={() => (tab = id)}>{l}</button>{/each}
  </div>

  {#if tab === 'euclid'}
    <p class="dx-help">Mỗi dòng: <code>a = q·b + r</code>. Dừng khi dư bằng 0 — ước chung lớn nhất là dư khác 0 cuối cùng. Chạy ngược (Euclid mở rộng) cho <b>Bézout</b>: <code>gcd = s·a + t·b</code>.</p>
    <div class="dx-bar">
      <label>a<input type="text" bind:value={ea} style="width:6rem" /></label>
      <label>b<input type="text" bind:value={eb} style="width:6rem" /></label>
      <button type="button" class="sec" onclick={() => (eShow = Math.max(1, Math.min(eShow, plain.steps.length) - 1))}>◀</button>
      <button type="button" onclick={() => (eShow = Math.min(plain.steps.length, Math.min(eShow, plain.steps.length) + 1))}>Bước tiếp ▶</button>
      <button type="button" class="sec" onclick={() => (eShow = 99)}>Hiện hết</button>
    </div>
    {#if eu}
      <table class="dx-t"><thead><tr><th>#</th><th>a = q·b + r</th><th>s</th><th>t</th></tr></thead>
        <tbody>
          {#each plain.steps.slice(0, Math.min(eShow, plain.steps.length)) as s, i}
            <tr><td>{i + 1}</td><td>{s.a} = {s.q}·{s.b} + {s.r}</td><td>{eu.rows[i + 2]?.s ?? ''}</td><td>{eu.rows[i + 2]?.t ?? ''}</td></tr>
          {/each}
        </tbody></table>
      {#if eShow >= plain.steps.length}
        <p class="dx-msg">gcd({A}, {B}) = <b>{eu.g}</b> sau {plain.steps.length} bước. Bézout: <b>{eu.x}·{A} + {eu.y}·{B} = {eu.x * A + eu.y * B}</b> {eu.x * A + eu.y * B === eu.g ? '✓' : '✗'}.
          {#if eu.g === 1} Vì gcd = 1, nghịch đảo của {A} modulo {B} là <b>{modInverse(A, B) ?? '—'}</b>.{/if}
          <br />lcm = {eu.g ? (A / eu.g) * B : 0} · {A} = {factorize(Math.max(A, 2)).map(([p, e]) => (e > 1 ? `${p}^${e}` : p)).join('·')}, {B} = {factorize(Math.max(B, 2)).map(([p, e]) => (e > 1 ? `${p}^${e}` : p)).join('·')}</p>
      {/if}
    {:else}<p class="dx-bad">Nhập ít nhất một số dương.</p>{/if}
  {/if}

  {#if tab === 'modular'}
    <p class="dx-help">Số học đồng dư là số học trên "mặt đồng hồ" n giờ. <b>a có nghịch đảo mod n ⇔ gcd(a, n) = 1</b> — các số đó chiếm φ(n) = {phi(N)} phần tử.</p>
    <div class="dx-bar">
      <label>Modulo n (2–24)<input type="number" min="2" max="24" bind:value={mn} style="width:4.5rem" /></label>
      <button type="button" class="sec" class:on={mop === '+'} onclick={() => (mop = '+')}>Bảng cộng</button>
      <button type="button" class="sec" class:on={mop === '*'} onclick={() => (mop = '*')}>Bảng nhân</button>
    </div>
    <div class="two">
      <div>
        <svg viewBox="-10 -10 {2 * 90 + 20} {2 * 90 + 20}" class="dx-svg" style="max-height:260px" role="img" aria-label="Mặt đồng hồ modulo">
          <circle cx="90" cy="90" r="90" fill="#f8fafc" stroke="#cbd5e1" />
          {#each Array.from({ length: N }, (_, i) => i) as i}
            {@const [x, y] = cp(i, N, 76)}
            <g role="button" tabindex="0" style="cursor:pointer" onclick={() => (mval = i)} onkeydown={(e) => e.key === 'Enter' && (mval = i)}>
              <circle cx={x + 14} cy={y + 14} r="12" fill={mod(mval, N) === i ? '#fde68a' : units.includes(i) ? '#ccfbf1' : '#fff'} stroke="#334155" />
              <text x={x + 14} y={y + 18} text-anchor="middle" font-size="11" font-weight="700">{i}</text>
            </g>
          {/each}
          <text x="90" y="86" text-anchor="middle" font-size="12">mod {N}</text>
          <text x="90" y="104" text-anchor="middle" font-size="12" font-weight="700">{mval} ≡ {mod(mval, N)}</text>
        </svg>
        <div class="dx-bar"><label>Số nguyên a<input type="number" bind:value={mval} style="width:6rem" /></label></div>
        <p class="dx-msg">{mval} = {Math.floor(mval / N)}·{N} + {mod(mval, N)}, nên {mval} ≡ <b>{mod(mval, N)}</b> (mod {N}). Ô xanh lục = có nghịch đảo: {units.join(', ')}.
          {#if units.includes(mod(mval, N)) && N > 1}<br />Nghịch đảo của {mod(mval, N)} là <b>{modInverse(mval, N)}</b>.{/if}</p>
      </div>
      <div class="scroll">
        <table class="dx-t tbl">
          <thead><tr><th>{mop === '+' ? '+' : '×'}</th>{#each table[0] as _, j}<th>{j}</th>{/each}</tr></thead>
          <tbody>{#each table as row, i}<tr><th>{i}</th>{#each row as v, j}<td class:hl={i === mod(mval, N) || j === mod(mval, N)} class:one={v === 1 && mop === '*'} class:zero={v === 0 && mop === '*' && i && j}>{v}</td>{/each}</tr>{/each}</tbody>
        </table>
      </div>
    </div>
    <div class="dx-card">
      <header><h5>Giải <code>a·x ≡ c (mod {N})</code></h5></header>
      <div class="dx-bar"><label>a<input type="text" bind:value={ca} style="width:4rem" /></label><label>c<input type="text" bind:value={cc} style="width:4rem" /></label></div>
      <p class="dx-msg">g = gcd({mod(num(ca, 1), N)}, {N}) = {lin.g}.
        {#if lin.solutions.length}Có {lin.solutions.length} nghiệm trong [0, {N}): <b>x ∈ {'{'}{lin.solutions.join(', ')}{'}'}</b>.{:else}g không chia hết {mod(num(cc, 0), N)} ⇒ <b>vô nghiệm</b>.{/if}</p>
    </div>
  {/if}

  {#if tab === 'fastexp'}
    <p class="dx-help">Tính <code>b^e mod m</code> bằng cách viết e theo nhị phân và bình phương liên tiếp: chỉ O(log e) phép nhân. Mỗi bit 1 nhân kết quả với lũy thừa-bình-phương hiện tại.</p>
    <div class="dx-bar">
      <label>b<input type="text" bind:value={fb} style="width:5rem" /></label>
      <label>e<input type="text" bind:value={fe} style="width:5rem" /></label>
      <label>m<input type="text" bind:value={fm} style="width:5rem" /></label>
    </div>
    <p class="dx-msg">e = {Math.max(1, num(fe, 1))} = <code>{fp.bits}</code>₂ — {fp.bits.length} bit nên cần {fp.bits.length} phép bình phương thay vì {Math.max(1, num(fe, 1)) - 1} phép nhân.</p>
    <table class="dx-t"><thead><tr><th>Bit (thấp→cao)</th><th>b^(2^i) mod m</th><th>Kết quả trước</th><th>Kết quả sau</th></tr></thead>
      <tbody>{#each fp.rows as r}<tr class:hl={r.mult}><td>{r.bit}</td><td>{r.sq}</td><td>{r.before}</td><td>{r.mult ? `${r.before}·${r.sq} mod ${FM} = ` : '(giữ)'} <b>{r.result}</b></td></tr>{/each}</tbody></table>
    <p class="dx-msg">⇒ {mod(num(fb, 2), FM)}^{Math.max(1, num(fe, 1))} mod {FM} = <b>{fp.result}</b> (kiểm tra BigInt: {String(modPow(mod(num(fb, 2), FM), Math.max(1, num(fe, 1)), FM))}).</p>
  {/if}

  {#if tab === 'sieve'}
    <p class="dx-help">Với mỗi số nguyên tố p ≤ √n còn chưa bị gạch, gạch các bội từ p² trở đi. Các số còn lại là nguyên tố.</p>
    <div class="dx-bar">
      <label>n (10–200)<input type="number" min="10" max="200" bind:value={sn} oninput={() => (sk = 0)} style="width:5rem" /></label>
      <button type="button" class="sec" disabled={sk <= 0} onclick={() => (sk -= 1)}>◀</button>
      <button type="button" disabled={sk >= sv.steps.length} onclick={() => (sk += 1)}>Gạch bội của p tiếp ▶</button>
      <button type="button" class="sec" onclick={() => (sk = sv.steps.length)}>Xong</button>
    </div>
    <div class="grid">
      {#each Array.from({ length: SN - 1 }, (_, i) => i + 2) as v}
        {@const by = crossedUpTo.get(v)}
        {@const isP = sk >= sv.steps.length && !sv.comp[v]}
        {@const cur = sk > 0 && sv.steps[sk - 1].p === v}
        <span class="cell" class:cr={by} class:pr={isP} class:cur>{v}</span>
      {/each}
    </div>
    <p class="dx-msg">{#if sk === 0}Chưa gạch gì. Các p cần xét: {sv.steps.map((s) => s.p).join(', ')} (p² ≤ {SN}).
      {:else}Vừa gạch các bội của <b>{sv.steps[sk - 1].p}</b> bắt đầu từ {sv.steps[sk - 1].p ** 2}: {sv.steps[sk - 1].crossed.join(', ') || '(không có số mới)'}.{/if}
      {#if sk >= sv.steps.length}<br />Có <b>{sv.primes.length}</b> số nguyên tố ≤ {SN}: {sv.primes.join(', ')}.{/if}</p>
  {/if}

  {#if tab === 'rsa'}
    <p class="dx-help">Chỉ để học: chọn hai số nguyên tố nhỏ p, q; n = pq; công khai (n, e); bí mật d = e⁻¹ mod φ(n). Mã hóa <code>c = mᵉ mod n</code>, giải mã <code>m = cᵈ mod n</code>. Số thật dùng hàng trăm chữ số — đừng dùng số nhỏ cho bảo mật!</p>
    <div class="dx-bar">
      <label>p<input type="text" bind:value={rp} style="width:5rem" /></label>
      <label>q<input type="text" bind:value={rq} style="width:5rem" /></label>
      <label>e<input type="text" bind:value={re} style="width:5rem" /></label>
      <label>Bản rõ m<input type="text" bind:value={rm} style="width:6rem" /></label>
    </div>
    {#if keys.error}<p class="dx-bad">{keys.error}</p>
    {:else}
      <table class="dx-t"><tbody>
        <tr><th>n = p·q</th><td>{keys.p}·{keys.q} = <b>{keys.n}</b></td></tr>
        <tr><th>φ(n) = (p−1)(q−1)</th><td>{keys.p - 1}·{keys.q - 1} = <b>{keys.phi}</b></td></tr>
        <tr><th>Khóa công khai (n, e)</th><td>({keys.n}, <b>{keys.e}</b>) &nbsp; gcd(e, φ) = {gcd(keys.e, keys.phi)}</td></tr>
        <tr><th>Khóa bí mật d</th><td>d = e⁻¹ mod φ = <b>{keys.d}</b> (kiểm tra: {keys.e}·{keys.d} mod {keys.phi} = {mod(keys.e * keys.d, keys.phi)})</td></tr>
        <tr><th>Mã hóa</th><td>c = {M}^{keys.e} mod {keys.n} = <b>{cipher}</b></td></tr>
        <tr><th>Giải mã</th><td>m = {cipher}^{keys.d} mod {keys.n} = <b>{plainBack}</b> {plainBack === M ? '✓' : '✗'}</td></tr>
      </tbody></table>
      <p class="dx-msg">Kẻ tấn công chỉ biết n = {keys.n}: phải phân tích thành {factorize(keys.n).map(([p]) => p).join(' × ')} — dễ với số nhỏ, bất khả thi với số hàng trăm chữ số. Nếu đoán sai d (d+1) sẽ giải ra {wrongDecrypt}, không phải {M}.</p>
    {/if}
  {/if}

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li><b>Euclid:</b> tính gcd(252, 198), rồi kiểm tra hệ thức Bézout; thử hai số nguyên tố cùng nhau (ví dụ 35 và 12) và đọc nghịch đảo.</li>
      <li><b>Đồng dư:</b> đặt n = 12 và xem hàng của số 4 trong bảng nhân: vì sao không có số 1? (gcd(4,12) ≠ 1). Giải 4x ≡ 6 (mod 12).</li>
      <li><b>Lũy thừa nhanh:</b> tính 7¹³ mod 11 và đếm số phép nhân so với 12 phép nhân thường.</li>
      <li><b>Sàng:</b> chọn n = 100; vì sao chỉ cần p đến 7?</li>
      <li><b>RSA:</b> giữ p = 61, q = 53, e = 17; mã hóa m = 65 rồi giải mã; thử p = 10 để xem thông báo lỗi.</li>
    </ol>
  </details>
</div>

<style>
  .two { display: grid; grid-template-columns: minmax(240px, 1fr) minmax(260px, 1.2fr); gap: 12px; align-items: start; }
  @media (max-width: 760px) { .two { grid-template-columns: 1fr; } }
  .scroll { overflow: auto; max-height: 360px; }
  .tbl td, .tbl th { text-align: center; padding: 2px 6px; min-width: 1.5rem; }
  td.hl, tr.hl td { background: #fef9c3; } td.one { background: #bbf7d0; font-weight: 700; } td.zero { color: #b91c1c; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(2.4rem, 1fr)); gap: 3px; margin: 8px 0; }
  .cell { text-align: center; padding: 4px 0; border: 1px solid #cbd5e1; border-radius: 6px; background: #fff; font-size: 0.85rem; }
  .cell.cr { background: #e2e8f0; color: #94a3b8; text-decoration: line-through; }
  .cell.pr { background: #bbf7d0; border-color: #0f766e; font-weight: 700; } .cell.cur { background: #fde68a; border-color: #d97706; }
  p { margin: 6px 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
