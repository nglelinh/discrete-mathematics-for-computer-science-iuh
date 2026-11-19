<script>
  import Stepper from '../shared/Stepper.svelte';
  import { bitsOf, fromBits, toSigned, fromSigned, negateStages, addSteps, range, bytesOf, valueOfBytes, y2038 } from './bits.js';

  let { tab: tabProp = 'twos', bits: bitsProp = 8, value = '', a = '', b = '' } = $props();
  let tab = $state(['twos', 'add', 'endian', 'y2038'].includes(tabProp) ? tabProp : 'twos');
  let n = $state(Number(bitsProp) === 4 ? 4 : 8);
  let u = $state(fromSigned(Number(value) || 5, 8));
  let stage = $state(0);
  let addA = $state(Number(a) || 100);
  let addB = $state(Number(b) || 50);
  let addStep = $state(0);
  let hex = $state('12345678');
  let order = $state('little');
  let off = $state(0);

  const R = $derived(range(n));
  $effect(() => { n; u = fromSigned(toSigned(u, 8), n); stage = 0; addA = Math.max(Number(R.min), Math.min(Number(R.max), addA)); addB = Math.max(Number(R.min), Math.min(Number(R.max), addB)); });

  // ---- bù hai
  const stages = $derived(negateStages(u, n));
  const shownU = $derived(stages[stage]);
  const bitsNow = $derived(bitsOf(shownU, n));
  const weights = $derived(Array.from({ length: n }, (_, i) => (i === 0 ? -(2 ** (n - 1)) : 2 ** (n - 1 - i))));
  function flip(i) {
    const base = stage === 0 ? u : stages[0];
    u = base ^ (1n << BigInt(n - 1 - i)); stage = 0;
  }
  const stageMsg = $derived([
    `Số gốc: ${toSigned(stages[0], n)} (không dấu ${stages[0]}). Bit trọng số lớn nhất mang giá trị âm −${2 ** (n - 1)}.`,
    `Bước 1 — đảo mọi bit (bù một): ${bitsOf(stages[1], n).join('')} = ${toSigned(stages[1], n)} (tức −(x+1)).`,
    `Bước 2 — cộng 1: ${bitsOf(stages[2], n).join('')} = ${toSigned(stages[2], n)}. ${toSigned(stages[0], n) === R.min ? 'Chú ý: −' + (-R.min) + ' không có số đối trong ' + n + ' bit (tràn), nên kết quả vẫn là chính nó.' : 'Đó là số đối −(' + toSigned(stages[0], n) + ') ✓'}`
  ][stage]);

  // ---- cộng
  const sum = $derived(addSteps(fromSigned(addA, n), fromSigned(addB, n), n));
  const aS = $derived(Math.min(addStep, n));
  $effect(() => { addA; addB; n; addStep = 0; });
  const doneBits = $derived(aS === 0 ? [] : sum.steps.slice(0, aS));
  const addMsg = $derived(aS === 0
    ? `Cộng ${addA} + ${addB} trong ${n} bit: cộng từng cột từ phải sang trái, có nhớ.`
    : aS < n
      ? `Cột ${aS} (từ phải): ${doneBits[aS - 1].a} + ${doneBits[aS - 1].b} + nhớ ${doneBits[aS - 1].cin} = ${doneBits[aS - 1].a + doneBits[aS - 1].b + doneBits[aS - 1].cin} ⇒ viết ${doneBits[aS - 1].sum}, nhớ ${doneBits[aS - 1].cout}.`
      : `Kết quả ${n} bit = ${toSigned(sum.result, n)}. ${sum.overflow ? 'TRÀN SỐ: nhớ vào bit dấu ≠ nhớ ra khỏi bit dấu, kết quả sai so với ' + (addA + addB) + '.' : 'Không tràn: kết quả đúng ' + (addA + addB) + '.'}`);

  // ---- endianness
  const hv = $derived(/^[0-9a-fA-F]{1,8}$/.test(hex) ? BigInt('0x' + hex) : null);
  const bytes = $derived(hv === null ? [] : bytesOf(hv, order));
  const hx = (x) => x.toString(16).toUpperCase().padStart(2, '0');

  // ---- y2038
  const Y = $derived(y2038(off));
</script>

<div class="dx">
  <h4>Biểu diễn nhị phân: bù hai · cộng có nhớ · thứ tự byte · Y2038</h4>
  <div class="dx-tabs">
    <button class={tab === 'twos' ? 'on' : 'sec'} onclick={() => (tab = 'twos')}>Bù hai</button>
    <button class={tab === 'add' ? 'on' : 'sec'} onclick={() => (tab = 'add')}>Cộng &amp; tràn số</button>
    <button class={tab === 'endian' ? 'on' : 'sec'} onclick={() => (tab = 'endian')}>Endianness</button>
    <button class={tab === 'y2038' ? 'on' : 'sec'} onclick={() => (tab = 'y2038')}>Y2038</button>
  </div>

  {#if tab === 'twos' || tab === 'add'}
    <div class="dx-bar"><label>Số bit <select bind:value={n}><option value={8}>8 bit</option><option value={4}>4 bit</option></select></label>
      <span class="dx-k">Khoảng biểu diễn: {R.min} … {R.max}</span></div>
  {/if}

  {#if tab === 'twos'}
    <p class="dx-help">Bấm vào một bit để đổi 0/1. Bit đầu có trọng số <b>âm</b>. Dùng <b>Bước tiếp</b> để thấy cách lấy số đối: đảo bit rồi cộng 1.</p>
    <Stepper bind:step={stage} total={3} />
    <div class="dx-msg">{stageMsg}</div>
    <div style="display:flex;gap:4px;flex-wrap:wrap">
      {#each bitsNow as bit, i}
        <button class="sec" style="min-width:2.4rem;padding:6px 4px;display:flex;flex-direction:column;align-items:center;{bit ? 'background:#dbeafe;border-color:#2563eb' : ''}" aria-label="bit {i}" onclick={() => flip(i)}>
          <small class="dx-k">{weights[i]}</small><b style="font-size:1.15rem">{bit}</b>
        </button>
      {/each}
    </div>
    <p style="margin:10px 0 0">Không dấu: <b>{shownU}</b> · Có dấu (bù hai): <b class="dx-ok">{toSigned(shownU, n)}</b> · Hex: <b class="dx-mono">0x{shownU.toString(16).toUpperCase().padStart(n / 4, '0')}</b></p>
  {:else if tab === 'add'}
    <p class="dx-help">Phép cộng nhị phân bù hai dùng đúng mạch cộng không dấu; tràn xảy ra khi kết quả ra ngoài khoảng biểu diễn.</p>
    <div class="dx-bar">
      <label>A <input type="number" bind:value={addA} min={Number(R.min)} max={Number(R.max)} style="width:5.5rem" /></label>
      <label>B <input type="number" bind:value={addB} min={Number(R.min)} max={Number(R.max)} style="width:5.5rem" /></label>
      {#if n === 8}<button class="sec" onclick={() => { addA = 127; addB = 1; }}>127 + 1</button><button class="sec" onclick={() => { addA = -100; addB = -50; }}>−100 + (−50)</button>{/if}
    </div>
    <Stepper bind:step={addStep} total={n + 1} />
    <div class="dx-msg" class:dx-err={aS === n && sum.overflow}>{addMsg}</div>
    <div class="dx-mono" style="overflow-x:auto;font-size:1.05rem;line-height:1.8">
      <div>nhớ&nbsp;&nbsp;{#each Array(n) as _, i}<span style="display:inline-block;width:1.4rem;text-align:center;color:#c2410c">{(n - 1 - i) < aS ? sum.steps[n - 1 - i].cin : ''}</span>{/each}</div>
      <div>A&nbsp;&nbsp;&nbsp;&nbsp;{#each bitsOf(fromSigned(addA, n), n) as x}<span style="display:inline-block;width:1.4rem;text-align:center">{x}</span>{/each} <small class="dx-k">= {addA}</small></div>
      <div>B&nbsp;&nbsp;&nbsp;&nbsp;{#each bitsOf(fromSigned(addB, n), n) as x}<span style="display:inline-block;width:1.4rem;text-align:center">{x}</span>{/each} <small class="dx-k">= {addB}</small></div>
      <div style="border-top:2px solid #334155;width:fit-content">A+B&nbsp;&nbsp;{#each Array(n) as _, i}<span style="display:inline-block;width:1.4rem;text-align:center;{(n - 1 - i) === aS - 1 ? 'background:#fde68a;border-radius:4px' : ''}">{(n - 1 - i) < aS ? sum.steps[n - 1 - i].sum : '·'}</span>{/each} {#if aS === n}<small class="dx-k">= {toSigned(sum.result, n)}</small>{/if}</div>
    </div>
  {:else if tab === 'endian'}
    <p class="dx-help">Số 32 bit gồm 4 byte. <b>Big-endian</b> ghi byte lớn nhất ở địa chỉ thấp; <b>little-endian</b> (x86, ARM thường dùng) ghi byte nhỏ nhất ở địa chỉ thấp.</p>
    <div class="dx-bar">
      <label>Giá trị hex (tối đa 8 chữ số) 0x<input type="text" bind:value={hex} maxlength="8" style="width:7rem" class="dx-mono" /></label>
      <button class={order === 'big' ? 'on' : 'sec'} onclick={() => (order = 'big')}>Big-endian</button>
      <button class={order === 'little' ? 'on' : 'sec'} onclick={() => (order = 'little')}>Little-endian</button>
    </div>
    {#if hv === null}
      <div class="dx-err">Nhập 1–8 chữ số hex (0–9, A–F).</div>
    {:else}
      <div class="dx-msg">0x{hv.toString(16).toUpperCase().padStart(8, '0')} = {hv} ghi vào bộ nhớ theo thứ tự {order === 'big' ? 'big-endian: byte cao nhất 0x' + hx(bytes[0]) + ' đứng đầu' : 'little-endian: byte thấp nhất 0x' + hx(bytes[0]) + ' đứng đầu'}.</div>
      <div style="display:flex;gap:6px;flex-wrap:wrap">
        {#each bytes as by, i}
          <div class="dx-card" style="text-align:center;min-width:4.4rem"><small class="dx-k">0x{(0x1000 + i).toString(16)}</small><div class="dx-mono" style="font-size:1.25rem;font-weight:700;color:#0f766e">{hx(by)}</div><small class="dx-k">{by.toString(2).padStart(8, '0')}</small></div>
        {/each}
      </div>
      <p class="dx-k" style="margin-top:8px">Đọc lại bằng thứ tự {order === 'big' ? 'little' : 'big'}-endian sẽ ra 0x{valueOfBytes(bytes, order === 'big' ? 'little' : 'big').toString(16).toUpperCase().padStart(8, '0')} — sai! Hai bên trao đổi dữ liệu phải thống nhất thứ tự byte.</p>
    {/if}
  {:else}
    <p class="dx-help">Unix time lưu số giây từ 1970-01-01 trong số nguyên 32 bit có dấu. Kéo thanh trượt qua giới hạn 2³¹−1.</p>
    <div class="dx-bar"><label>Giây = 2³¹ − 1 + <b>{off}</b> <input type="range" min="-5" max="5" bind:value={off} /></label></div>
    <div class="dx-grid2">
      <div class="dx-card"><h5>Số học thật</h5><p class="dx-mono" style="margin:6px 0">{Y.secs} giây</p><p style="margin:0">{Y.realDate}</p></div>
      <div class="dx-card" style="border-color:{Y.wrapped < 0n ? '#dc2626' : '#e2e8f0'}"><h5>Lưu trong int32</h5><p class="dx-mono" style="margin:6px 0">{Y.wrapped} giây</p><p style="margin:0" class={Y.wrapped < 0n ? 'dx-bad' : ''}>{Y.wrappedDate}</p></div>
    </div>
    <p class="dx-k" style="margin-top:8px">{Y.wrapped < 0n ? 'Tràn: bit dấu bật lên ⇒ đồng hồ nhảy về năm 1901.' : 'Chưa tràn: giá trị vẫn nằm trong int32.'}</p>
  {/if}
</div>
