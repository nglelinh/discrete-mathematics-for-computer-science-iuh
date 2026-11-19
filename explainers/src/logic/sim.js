// Mô phỏng xác suất: nghịch lý ngày sinh, va chạm băm, hàng đợi (Little's law).

export function rng(seed = 1) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function birthdayProb(n, d = 365) {
  let q = 1;
  for (let i = 0; i < n; i++) q *= Math.max(0, d - i) / d;
  return 1 - q;
}
export function minPeople(p, d = 365) {
  for (let n = 0; n <= d + 1; n++) if (birthdayProb(n, d) >= p) return n;
  return d + 1;
}
export function simulateBirthday(n, d, trials, rand) {
  let hit = 0;
  for (let t = 0; t < trials; t++) {
    const seen = new Set();
    let dup = false;
    for (let i = 0; i < n && !dup; i++) { const x = Math.floor(rand() * d); if (seen.has(x)) dup = true; seen.add(x); }
    if (dup) hit++;
  }
  return hit / trials;
}

export const expectedOccupied = (n, m) => m * (1 - Math.pow(1 - 1 / m, n));
export function hashInserts(n, m, rand) {
  const buckets = Array.from({ length: m }, () => []);
  const steps = [];
  for (let k = 0; k < n; k++) {
    const b = Math.floor(rand() * m);
    const collided = buckets[b].length > 0;
    buckets[b].push(k + 1);
    steps.push({ key: k + 1, bucket: b, collided, occupied: buckets.filter((x) => x.length).length, snapshot: buckets.map((x) => [...x]) });
  }
  return { steps, buckets };
}

/** Hàng đợi c máy chủ: đến theo Poisson(lambda /s), phục vụ mũ trung bình `service` giây. */
export function simulateQueue({ lambda, service, c, T = 200, seed = 1 }) {
  const rand = rng(seed);
  const exp = (mean) => -Math.log(1 - rand()) * mean;
  const free = Array(c).fill(0);
  const jobs = [];
  let t = 0;
  for (;;) {
    t += exp(1 / lambda);
    if (t > T) break;
    let k = 0;
    for (let i = 1; i < c; i++) if (free[i] < free[k]) k = i;
    const start = Math.max(t, free[k]);
    const end = start + exp(service);
    free[k] = end;
    jobs.push({ arrive: t, start, end });
  }
  const n = jobs.length;
  const waits = jobs.map((j) => j.start - j.arrive).sort((x, y) => x - y);
  const avgWait = n ? waits.reduce((a, b) => a + b, 0) / n : 0;
  const busy = jobs.reduce((a, j) => a + (Math.min(j.end, T) - Math.min(j.start, T)), 0);
  const horizon = Math.max(T, ...jobs.map((j) => j.end));
  const sojourn = jobs.reduce((a, j) => a + (j.end - j.arrive), 0);
  const samples = Array.from({ length: 60 }, (_, i) => {
    const x = (i / 59) * T;
    return { t: x, inSystem: jobs.filter((j) => j.arrive <= x && j.end > x).length, queued: jobs.filter((j) => j.arrive <= x && j.start > x).length };
  });
  return {
    n, avgWait, p95Wait: waits[Math.floor(0.95 * (n - 1))] ?? 0, maxWait: waits[n - 1] ?? 0,
    utilization: busy / (c * T),
    avgInSystem: sojourn / horizon, avgSojourn: n ? sojourn / n : 0, throughput: n / horizon, samples
  };
}
