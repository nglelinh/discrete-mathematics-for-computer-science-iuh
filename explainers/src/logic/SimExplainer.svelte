<script>
  import Stepper from '../shared/Stepper.svelte';
  import { rng, birthdayProb, minPeople, simulateBirthday, expectedOccupied, hashInserts, simulateQueue } from './sim.js';

  let { tab: tabProp = 'birthday', days = 365, buckets = 30, keys = 20, lambda = 40, service = 100, servers = 6 } = $props();
  let tab = $state(['birthday', 'hash', 'queue'].includes(tabProp) ? tabProp : 'birthday');

  // ---- ngày sinh
  let D = $state(Math.max(2, Number(days) || 365));
  let n = $state(23);
  let simRes = $state(null);
  let simSeed = $state(1);
  const prob = $derived(birthdayProb(n, D));
  const half = $derived(minPeople(0.5, D));
  const curve = $derived(Array.from({ length: Math.min(D, 100) + 1 }, (_, i) => [i, birthdayProb(i, D)]));
  $effect(() => { n; D; simRes = null; });
  function runSim() { simSeed += 1; simRes = simulateBirthday(n, D, 2000, rng(simSeed)); }
  const cx = (i) => 30 + (i / Math.max(1, Math.min(D, 100))) * 520;
  const cy = (p) => 160 - p * 140;

  // ---- băm
  let M = $state(Math.max(2, Math.min(100, Number(buckets) || 30)));
  let K = $state(Math.max(1, Math.min(80, Number(keys) || 20)));
  let hseed = $state(7);
  let hstep = $state(0);
  $effect(() => { M; K; hseed; hstep = 0; });
  const H = $derived(hashInserts(K, M, rng(hseed)));
  const hs = $derived(hstep === 0 ? null : H.steps[Math.min(hstep, H.steps.length) - 1]);
  const view = $derived(hs ? hs.snapshot : Array.from({ length: M }, () => []));
  const hmsg = $derived(!hs ? `${K} khóa sẽ được băm ngẫu nhiên vào ${M} ngăn. Kỳ vọng số ngăn có khóa: ${expectedOccupied(K, M).toFixed(1)}, tức khoảng ${(K - expectedOccupied(K, M)).toFixed(1)} khóa phải “đụng” ngăn đã có.`
    : `Khóa ${hs.key} → ngăn ${hs.bucket + 1}${hs.collided ? ': VA CHẠM (ngăn đã có khóa)' : ': ngăn trống'}. Đã có ${hs.occupied}/${M} ngăn bị chiếm; số va chạm tới giờ = ${hs.key - hs.occupied}.`);

  // ---- hàng đợi
  let lam = $state(Number(lambda) || 40);
  let svc = $state(Number(service) || 100);
  let cc = $state(Number(servers) || 6);
  const Q = $derived(simulateQueue({ lambda: lam, service: svc / 1000, c: cc, T: 120, seed: 4 }));
  const need = $derived(lam * svc / 1000);
  const maxIn = $derived(Math.max(1, ...Q.samples.map((s) => s.inSystem)));
  const qx = (i) => 30 + (i / 59) * 520;
  const qy = (v) => 150 - (v / maxIn) * 125;
</script>

<div class="dx">
  <h4>Mô phỏng xác suất: ngày sinh · va chạm băm · hàng đợi</h4>
  <div class="dx-tabs">
    <button class={tab === 'birthday' ? 'on' : 'sec'} onclick={() => (tab = 'birthday')}>Nghịch lý ngày sinh</button>
    <button class={tab === 'hash' ? 'on' : 'sec'} onclick={() => (tab = 'hash')}>Va chạm băm</button>
    <button class={tab === 'queue' ? 'on' : 'sec'} onclick={() => (tab = 'queue')}>Hàng đợi / Little</button>
  </div>

  {#if tab === 'birthday'}
    <p class="dx-help">Xác suất ít nhất hai người trùng ngày sinh: P(n) = 1 − Π (d−i)/d. Kéo thanh trượt rồi bấm “Mô phỏng” để so với thực nghiệm.</p>
    <div class="dx-bar">
      <label>Số ngày d <input type="number" min="2" max="100000" bind:value={D} style="width:6rem" /></label>
      <label>Số người n = <b>{n}</b> <input type="range" min="1" max="100" bind:value={n} /></label>
      <button onclick={runSim}>🎲 Mô phỏng 2000 lần</button>
    </div>
    <div class="dx-msg">Với n = {n}, d = {D}: P(trùng) = <b>{(prob * 100).toFixed(2)}%</b>{simRes !== null ? ` · mô phỏng: ${(simRes * 100).toFixed(1)}%` : ''}. Cần <b>{half}</b> người để P ≥ 50%.</div>
    <svg class="dx-svg" viewBox="0 0 580 185" role="img" aria-label="Đường xác suất">
      <line x1="30" y1={cy(0.5)} x2="550" y2={cy(0.5)} stroke="#cbd5e1" stroke-dasharray="5 4" /><text x="552" y={cy(0.5) + 4} font-size="11" fill="#64748b">50%</text>
      <polyline fill="none" stroke="#2563eb" stroke-width="2.5" points={curve.map(([i, p]) => cx(i) + ',' + cy(p)).join(' ')} />
      {#if n <= Math.min(D, 100)}<circle cx={cx(n)} cy={cy(prob)} r="6" fill="#f59e0b" stroke="#92400e" stroke-width="2" />{/if}
      <text x="30" y="178" font-size="11" fill="#64748b">n = 0</text><text x="520" y="178" font-size="11" fill="#64748b">n = {Math.min(D, 100)}</text>
    </svg>
  {:else if tab === 'hash'}
    <p class="dx-help">Mỗi khóa được băm ngẫu nhiên vào một ngăn. Va chạm xuất hiện sớm hơn trực giác: số ngăn trống không giảm tuyến tính.</p>
    <div class="dx-bar">
      <label>Số ngăn m = <b>{M}</b> <input type="range" min="2" max="100" bind:value={M} /></label>
      <label>Số khóa n = <b>{K}</b> <input type="range" min="1" max="80" bind:value={K} /></label>
      <button class="sec" onclick={() => (hseed += 1)}>🎲 Hạt khác</button>
    </div>
    <Stepper bind:step={hstep} total={K + 1} />
    <div class="dx-msg">{hmsg}</div>
    <div style="display:flex;flex-wrap:wrap;gap:4px">
      {#each view as bk, i}
        <div style="width:34px;text-align:center"><div style="min-height:{Math.max(36, bk.length * 16 + 8)}px;border:2px solid {hs && hs.bucket === i ? '#f59e0b' : '#cbd5e1'};border-radius:5px;background:{bk.length > 1 ? '#fee2e2' : bk.length ? '#dcfce7' : '#f8fafc'};font-size:.62rem;display:flex;flex-direction:column;justify-content:flex-end">{#each bk as key}<div style="line-height:16px">{key}</div>{/each}</div><small class="dx-k" style="font-size:.6rem">{i + 1}</small></div>
      {/each}
    </div>
    <p class="dx-k" style="margin-top:6px">Đỏ = ngăn có ≥ 2 khóa (va chạm). Kỳ vọng số ngăn có khóa sau n khóa: m(1 − (1 − 1/m)ⁿ).</p>
  {:else}
    <p class="dx-help">Little’s law: số yêu cầu trung bình đang trong hệ thống L = λ·W. Đó là số kết nối cần có; ít hơn thì hàng đợi tích lại. Mô phỏng 120 giây, thời gian phục vụ phân phối mũ.</p>
    <div class="dx-bar">
      <label>λ = <b>{lam}</b> req/s <input type="range" min="1" max="100" bind:value={lam} /></label>
      <label>W = <b>{svc}</b> ms <input type="range" min="10" max="500" step="10" bind:value={svc} /></label>
      <label>Pool c = <b>{cc}</b> <input type="range" min="1" max="60" bind:value={cc} /></label>
    </div>
    <div class="dx-msg">L = λ·W = {lam} × {svc / 1000} = <b>{need.toFixed(1)}</b> kết nối trung bình. Pool c = {cc} ⇒ tải ρ = L/c = {(need / cc * 100).toFixed(0)}% {need / cc >= 1 ? '(QUÁ TẢI: hàng đợi tăng vô hạn)' : need / cc > 0.85 ? '(rất cao, hàng đợi dài)' : '(ổn)'}.</div>
    <div class="dx-grid2">
      <div class="dx-card"><h5>Kết quả mô phỏng</h5><p style="margin:6px 0">Chờ trung bình: <b>{(Q.avgWait * 1000).toFixed(0)} ms</b> · p95: <b>{(Q.p95Wait * 1000).toFixed(0)} ms</b><br />Sử dụng pool: <b>{(Q.utilization * 100).toFixed(0)}%</b> · trong hệ thống: <b>{Q.avgInSystem.toFixed(1)}</b> (≈ λ·W)</p></div>
    </div>
    <svg class="dx-svg" viewBox="0 0 580 175" role="img" aria-label="Số yêu cầu theo thời gian" style="margin-top:8px">
      <polyline fill="none" stroke="#2563eb" stroke-width="2" points={Q.samples.map((s, i) => qx(i) + ',' + qy(s.inSystem)).join(' ')} />
      <polyline fill="none" stroke="#dc2626" stroke-width="2" points={Q.samples.map((s, i) => qx(i) + ',' + qy(s.queued)).join(' ')} />
      <line x1="30" y1={qy(cc)} x2="550" y2={qy(cc)} stroke="#16a34a" stroke-dasharray="5 4" />
      <text x="34" y="14" font-size="11" fill="#2563eb">xanh dương: đang trong hệ thống</text><text x="230" y="14" font-size="11" fill="#dc2626">đỏ: đang xếp hàng</text><text x="380" y="14" font-size="11" fill="#16a34a">gạch xanh lá: pool c</text>
    </svg>
  {/if}
</div>
