<script>
  import Stepper from '../shared/Stepper.svelte';
  import { rippleSteps } from './adder.js';

  let { a = 11, b = 6, sub = false } = $props();
  const N = 4;
  let A = $state(Number(a) & 15);
  let B = $state(Number(b) & 15);
  let isSub = $state(sub === true || sub === 'true');
  let step = $state(0);
  $effect(() => { A; B; isSub; step = 0; });
  const r = $derived(rippleSteps(A, B, N, isSub));
  const k = $derived(Math.min(step, N + 1));
  const done = $derived(Math.min(k, N));
  const bits = (x) => Array.from({ length: N }, (_, i) => (x >> (N - 1 - i)) & 1);
  const flip = (which, i) => { const m = 1 << (N - 1 - i); if (which === 'A') A ^= m; else B ^= m; };
  const BW = 112, GAPX = 18, W = N * (BW + GAPX) + 30;
  const bx = (i) => 10 + (N - 1 - i) * (BW + GAPX); // tầng 0 (LSB) ở bên phải
  const msg = $derived(k === 0
    ? `Cộng ${A} ${isSub ? '−' : '+'} ${B} (4 bit). ${isSub ? 'Phép trừ: đảo mọi bit của B (XOR với 1) và đặt nhớ vào Cin₀ = 1 (a − b = a + ~b + 1).' : 'Tầng 0 (bit thấp nhất) có Cin = 0.'}`
    : k <= N
      ? (() => { const s = r.stages[k - 1]; return `Tầng ${k - 1}: a=${s.a}, b=${s.b}, Cin=${s.cin} ⇒ Sum = a⊕b⊕Cin = ${s.sum}, Cout = ab + Cin(a⊕b) = ${s.cout}. Cout này là Cin của tầng ${k}.`; })()
      : `Kết quả ${bits(r.result).join('')} = ${r.result} (không dấu) = ${r.signed} (có dấu). ${r.overflow ? 'TRÀN SỐ có dấu (nhớ vào bit dấu ≠ nhớ ra).' : 'Không tràn.'} Nhớ phải đi qua cả ${N} tầng nên độ trễ ≈ ${r.delay} tầng cổng (tăng theo n).`);
</script>

<div class="dx">
  <h4>Bộ cộng lan truyền mang (ripple-carry) 4 bit</h4>
  <p class="dx-help">Bấm vào bit của A, B để đổi. Bấm Bước tiếp để xem từng bộ cộng đầy đủ tính Sum và Cout rồi chuyền nhớ sang trái. Chuyển sang <b>Trừ</b> để thấy cùng mạch làm phép trừ bù hai.</p>
  <div class="dx-bar">
    <button class={!isSub ? 'on' : 'sec'} onclick={() => (isSub = false)}>Cộng A + B</button>
    <button class={isSub ? 'on' : 'sec'} onclick={() => (isSub = true)}>Trừ A − B</button>
  </div>
  {#each [['A', A], ['B', B]] as [nm, v]}
    <div class="dx-bar" style="margin-bottom:4px"><b style="width:1.2rem">{nm}</b>
      {#each bits(v) as bit, i}<button class="sec" style="min-width:2.3rem;{bit ? 'background:#dbeafe;border-color:#2563eb' : ''}" aria-label="{nm} bit {i}" onclick={() => flip(nm, i)}>{bit}</button>{/each}
      <span class="dx-k">= {v}</span></div>
  {/each}
  <Stepper bind:step total={N + 2} />
  <div class="dx-msg">{msg}</div>
  <div style="overflow-x:auto">
    <svg class="dx-svg" viewBox="0 0 {W} 250" style="min-width:{Math.min(W, 560)}px" role="img" aria-label="Bốn bộ cộng đầy đủ nối tiếp">
      {#each r.stages as s, idx}
        {@const x = bx(idx)}
        {@const on = done > idx}
        {@const cur = k - 1 === idx}
        <rect x={x} y="70" width={BW} height="80" rx="8" fill={cur ? '#fef3c7' : on ? '#ecfdf5' : '#fff'} stroke={cur ? '#f59e0b' : on ? '#16a34a' : '#94a3b8'} stroke-width="2.5" />
        <text x={x + BW / 2} y="92" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">FA bit {idx}</text>
        <text x={x + BW / 2} y="114" text-anchor="middle" font-size="12" fill="#64748b">a={s.a} b={s.b}</text>
        <text x={x + BW / 2} y="136" text-anchor="middle" font-size="13" font-weight="700" fill={on ? '#0f766e' : '#cbd5e1'}>{on ? `Σ=${s.sum}  Cout=${s.cout}` : 'chưa tính'}</text>
        <line x1={x + 30} y1="40" x2={x + 30} y2="70" stroke="#64748b" stroke-width="2" /><text x={x + 30} y="32" text-anchor="middle" font-size="12" font-weight="700">{s.a}</text>
        <line x1={x + 82} y1="40" x2={x + 82} y2="70" stroke="#64748b" stroke-width="2" /><text x={x + 82} y="32" text-anchor="middle" font-size="12" font-weight="700">{s.b}</text>
        {#if isSub}<text x={x + 98} y="48" font-size="9" fill="#b45309">{s.bRaw}⊕1</text>{/if}
        <line x1={x + BW / 2} y1="150" x2={x + BW / 2} y2="185" stroke={on ? '#16a34a' : '#cbd5e1'} stroke-width="2.5" />
        <text x={x + BW / 2} y="206" text-anchor="middle" font-size="18" font-weight="800" fill={on ? '#0f766e' : '#cbd5e1'}>{on ? s.sum : '·'}</text>
        {#if idx > 0}
          <path d="M {bx(idx - 1)} 110 L {x + BW} 110" stroke={done > idx - 1 ? '#ea580c' : '#cbd5e1'} stroke-width="3" fill="none" />
          <text x={x + BW + GAPX / 2} y="104" text-anchor="middle" font-size="11" fill={done > idx - 1 ? '#ea580c' : '#cbd5e1'} font-weight="700">{done > idx - 1 ? r.stages[idx - 1].cout : ''}</text>
        {/if}
      {/each}
      <text x={bx(0) + BW + 2} y="104" font-size="11" fill="#ea580c" font-weight="700">Cin={isSub ? 1 : 0}</text>
      <text x="10" y="236" font-size="12" fill="#64748b">Kết quả: {k >= N + 1 ? bits(r.result).join('') + ` (Cout = ${r.cout})` : '…'}</text>
    </svg>
  </div>
</div>
