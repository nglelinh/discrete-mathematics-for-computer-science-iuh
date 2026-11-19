<script>
  import Stepper from '../shared/Stepper.svelte';
  import { INDUCTION_PRESETS, inductionSteps } from './induction.js';

  let { preset = 'sum' } = $props();
  let pid = $state(INDUCTION_PRESETS.some((p) => p.id === preset) ? preset : 'sum');
  let step = $state(0);
  const P = $derived(INDUCTION_PRESETS.find((p) => p.id === pid));
  const steps = $derived(inductionSteps(P));
  const s = $derived(steps[Math.min(step, steps.length - 1)]);
  $effect(() => { pid; step = 0; });

  const COLS = 14, DW = 30, DH = 56, GAP = 10;
  const rows = $derived(Math.ceil(P.count / COLS));
  const W = COLS * (DW + GAP) + GAP;
  const H = $derived(rows * (DH + 34) + 12);
  const cols = $derived(Math.min(COLS, P.count));
  const pos = (i) => ({ x: GAP + (i % COLS) * (DW + GAP), y: 10 + Math.floor(i / COLS) * (DH + 34) });
  const lastFallen = $derived(s.fallen - 1);
  function dstate(i) {
    const n = P.n0 + i;
    if (s.bad === n) return 'bad';
    if (i < s.fallen) return i === lastFallen && s.phase !== 'end' ? 'now' : 'down';
    return 'up';
  }
</script>

<div class="dx">
  <h4>Quy nạp toán học: hiệu ứng domino</h4>
  <p class="dx-help">Mỗi domino là một giá trị n. Bấm <b>Play</b> để xem cơ sở (đẩy domino đầu) và bước quy nạp (domino này đổ kéo domino sau đổ). Hai ví dụ cuối cho thấy điều gì xảy ra khi thiếu cơ sở hoặc chỉ kiểm tra từng trường hợp.</p>
  <div class="dx-bar">
    <label>Mệnh đề P(n)
      <select bind:value={pid}>{#each INDUCTION_PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select>
    </label>
  </div>
  <Stepper bind:step total={steps.length} />
  <div class="dx-msg" class:dx-err={s.phase === 'end' && !P.valid}>{s.msg}</div>
  <svg class="dx-svg" viewBox="0 0 {cols * (DW + GAP) + GAP + 44} {H}" role="img" aria-label="Hàng domino">
    {#each Array(P.count) as _, i}
      {@const p = pos(i)}
      {@const st = dstate(i)}
      <g transform="translate({p.x + DW} {p.y + DH}) rotate({st === 'down' || st === 'now' ? 70 : 0})" style="transition: transform .45s">
        <rect x={-DW} y={-DH} width={DW} height={DH} rx="4" fill={st === 'bad' ? '#fecaca' : st === 'now' ? '#fde68a' : st === 'down' ? '#86efac' : '#e2e8f0'} stroke={st === 'bad' ? '#dc2626' : st === 'now' ? '#f59e0b' : '#475569'} stroke-width="2" />
      </g>
      <text x={p.x + DW / 2} y={p.y + DH + 16} text-anchor="middle" font-size="11" fill="#334155">{P.n0 + i}</text>
    {/each}
  </svg>
  <p class="dx-k">Màu: xám = chưa đổ · vàng = đang đổ · xanh = P(n) đã đúng · đỏ = P(n) sai hoặc không bắt đầu.</p>
</div>
