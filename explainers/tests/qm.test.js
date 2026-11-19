import test from 'node:test';
import assert from 'node:assert/strict';
import { runQM, parseNums, coverOf, literals, bitsOf, PRESETS, sopText } from '../src/qm/qm.js';

// ---------- vét cạn độc lập: mọi khối (cube) hợp lệ → nguyên tố → tập phủ nhỏ nhất ----------
function cubes(n) {
  let list = [''];
  for (let i = 0; i < n; i++) list = list.flatMap((s) => [s + '0', s + '1', s + '-']);
  return list;
}
function bruteMin(n, ones, dcs) {
  const allowed = new Set([...ones, ...dcs]);
  if (!ones.length) return [0, 0];
  const valid = cubes(n).filter((c) => coverOf(c).every((m) => allowed.has(m)));
  const sub = (a, b) => coverOf(a).every((m) => coverOf(b).includes(m)); // a ⊆ b
  const primes = valid.filter((c) => !valid.some((d) => d !== c && sub(c, d)));
  const need = ones.map((m) => 1n << BigInt(ones.indexOf(m)));
  const mask = primes.map((p) => coverOf(p).reduce((s, m) => (ones.includes(m) ? s | (1n << BigInt(ones.indexOf(m))) : s), 0n));
  const full = (1n << BigInt(ones.length)) - 1n;
  let best = null;
  const lits = primes.map(literals);
  const rec = (i, cov, cnt, lit) => {
    if (best && (cnt > best[0] || (cnt === best[0] && lit >= best[1]))) return;
    if (cov === full) { best = [cnt, lit]; return; }
    if (i >= primes.length) return;
    rec(i + 1, cov | mask[i], cnt + 1, lit + lits[i]);
    rec(i + 1, cov, cnt, lit);
  };
  rec(0, 0n, 0, 0);
  void need;
  return best;
}

let seed = 12345;
const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
function randomFn(n, pOne, pDc) {
  const ones = [], dcs = [];
  for (let m = 0; m < 1 << n; m++) { const r = rnd(); if (r < pOne) ones.push(m); else if (r < pOne + pDc) dcs.push(m); }
  return { ones, dcs };
}
const coveredBy = (terms) => new Set(terms.flatMap(coverOf));

test('QM khớp vét cạn: chi phí tối thiểu (số hạng, literal) với hàm ngẫu nhiên 2–4 biến (có don\'t-care)', () => {
  let usedPetrick = 0, usedDom = 0;
  for (let t = 0; t < 600; t++) {
    const n = 2 + (t % 3);
    const { ones, dcs } = randomFn(n, 0.2 + rnd() * 0.5, rnd() * 0.25);
    const r = runQM(n, ones, dcs);
    const cover = coveredBy(r.result.terms);
    for (const m of ones) assert.ok(cover.has(m), `thiếu minterm ${m}`);
    const allowed = new Set([...ones, ...dcs]);
    for (const m of cover) assert.ok(allowed.has(m), `phủ thừa ${m}`);
    assert.ok(r.result.verified);
    assert.deepEqual(r.result.cost, bruteMin(n, ones, dcs), `n=${n} ones=${ones} dc=${dcs}`);
    if (r.steps.some((s) => s.kind === 'petrickSetup')) usedPetrick++;
    if (r.steps.some((s) => s.kind === 'rowDom' || s.kind === 'colDom')) usedDom++;
  }
  assert.ok(usedPetrick > 5, 'cần có ca dùng Petrick: ' + usedPetrick);
  assert.ok(usedDom > 20, 'cần có ca dùng trội: ' + usedDom);
});

test('QM 5 biến khớp vét cạn (mẫu ngẫu nhiên)', () => {
  for (let t = 0; t < 25; t++) {
    const { ones, dcs } = randomFn(5, 0.3 + rnd() * 0.25, rnd() * 0.1);
    const r = runQM(5, ones, dcs);
    assert.ok(r.result.verified);
    assert.deepEqual(r.result.cost, bruteMin(5, ones, dcs), `ones=${ones} dc=${dcs}`);
  }
});

test('QM 6 biến: phủ đúng và mọi tích đều là nguyên nhân nguyên tố từ cột dán', () => {
  for (let t = 0; t < 15; t++) {
    const { ones, dcs } = randomFn(6, 0.25 + rnd() * 0.3, rnd() * 0.1);
    const r = runQM(6, ones, dcs);
    assert.ok(r.result.verified);
    const primeBits = new Set(r.primes.map((p) => p.bits));
    for (const term of r.result.terms) assert.ok(primeBits.has(term));
    // không còn cặp nào dán được giữa các nguyên tố (độc lập tính chất tối đại)
    const allowed = new Set([...ones, ...dcs]);
    for (const p of r.primes) assert.ok(p.mins.every((m) => allowed.has(m)));
  }
});

test('nguyên nhân nguyên tố = đúng tập khối tối đại (so với vét cạn)', () => {
  for (let t = 0; t < 120; t++) {
    const n = 3 + (t % 2);
    const { ones, dcs } = randomFn(n, 0.3 + rnd() * 0.4, rnd() * 0.2);
    if (!ones.length) continue;
    const allowed = new Set([...ones, ...dcs]);
    const valid = cubes(n).filter((c) => coverOf(c).every((m) => allowed.has(m)));
    const sub = (a, b) => coverOf(a).every((m) => coverOf(b).includes(m));
    const primes = valid.filter((c) => !valid.some((d) => d !== c && sub(c, d))).sort();
    assert.deepEqual(runQM(n, ones, dcs).primes.map((p) => p.bits).sort(), primes);
  }
});

test('ví dụ trong bài: F1 (5,6,7,9,11,15) có đúng 5 nguyên nhân nguyên tố và phủ cuối cùng gồm 4 hạng', () => {
  const p = PRESETS.find((x) => x.id === 'f1');
  const r = runQM(p.n, parseNums(p.ones, p.n).nums, [], p.names);
  assert.deepEqual(r.primes.map((x) => x.bits).sort(), ['-111', '011-', '01-1', '1-11', '10-1'].sort());
  assert.equal(r.result.cost[0], 4);
  assert.ok(r.steps.some((s) => s.kind === 'essential'));
});

test('ví dụ bốn biến của mục 5 (đã sửa trong bài): bd + cd + ¬b¬d; ¬b¬d và bd cốt yếu', () => {
  const r = runQM(4, [0, 2, 3, 5, 7, 8, 10, 11, 13, 15], [], ['a', 'b', 'c', 'd']);
  assert.deepEqual(r.result.cost, [3, 6]);
  assert.deepEqual(r.result.terms.sort(), ['--11', '-0-0', '-1-1'].sort());
  assert.deepEqual(r.primes.map((x) => x.bits).sort(), ['--11', '-01-', '-0-0', '-1-1'].sort());
  assert.deepEqual(r.steps.filter((x) => x.kind === 'essential').map((x) => x.rid).slice(0, 2).sort(), ['c0:-0-0', 'c0:-1-1'].map((id) => r.primes.find((p) => p.bits === id.slice(3)).id).sort());
  assert.equal(PRESETS.find((p) => p.id === 'four').note.startsWith('Khớp với bài'), true);
  // cd + ¬b¬d không phủ hết: thiếu 5 và 13
  const only = new Set(['--11', '-0-0'].flatMap(coverOf));
  assert.deepEqual([5, 13].filter((m) => !only.has(m)), [5, 13]);
});

test('ví dụ don\'t-care 3 biến: 1,2,5 với d 0,7 → hai hạng', () => {
  const r = runQM(3, [1, 2, 5], [0, 7], ['a', 'b', 'c']);
  assert.equal(r.result.cost[0], 2);
  assert.ok(r.result.verified);
  // bảng phủ không có cột don't-care
  assert.deepEqual(r.chart.cols, [1, 2, 5]);
  // vẫn đúng theo bài: có cover ¬a¬c + ¬b c (cost 4) hoặc tương đương tối ưu
  assert.equal(r.result.cost[1], 4);
});

test('hàm hằng và biên', () => {
  assert.equal(runQM(3, [], [1, 2], ['a', 'b', 'c']).result.text, '0');
  const all = runQM(3, [0, 1, 2, 3, 4, 5, 6, 7], []);
  assert.deepEqual(all.result.terms, ['---']);
  assert.equal(all.result.text, '1');
  const withDc = runQM(2, [0, 3], [1, 2]);
  assert.deepEqual(withDc.result.terms, ['--']);
});

test('lõi vòng (0,1,2,5,6,7) dùng Petrick và có đúng 2 phương án tối ưu', () => {
  const r = runQM(3, [0, 1, 2, 5, 6, 7], []);
  assert.ok(r.steps.some((s) => s.kind === 'petrickSetup'));
  assert.ok(r.steps.some((s) => s.kind === 'petrickPick'));
  assert.deepEqual(r.result.cost, [3, 6]);
  assert.equal(r.result.alternatives, 2);
});

test('mọi preset chạy đúng, các bước có tiêu đề/nội dung và dấu ✓ khớp', () => {
  for (const p of PRESETS) {
    const r = runQM(p.n, parseNums(p.ones, p.n).nums, parseNums(p.dc, p.n).nums, p.names);
    assert.ok(r.result.verified, p.id);
    assert.ok(r.steps.length > 3);
    for (const s of r.steps) { assert.ok(s.title && s.text && (s.phase === 1 || s.phase === 2)); }
    for (const it of r.items) assert.equal(it.used, r.items.some((x) => x.col === it.col + 1 && it.mins.every((m) => x.mins.includes(m)) && x.mins.length === it.mins.length * 2));
    assert.equal(r.steps.at(-1).kind, 'result');
  }
});

test('parseNums: khoảng, trùng lặp, lỗi', () => {
  assert.deepEqual(parseNums('1, 5-7 7 12', 4).nums, [1, 5, 6, 7, 12]);
  assert.equal(parseNums('16', 4).errors.length, 1);
  assert.equal(parseNums('x', 4).errors.length, 1);
  assert.equal(bitsOf(5, 4), '0101');
  assert.equal(sopText(['01-'], ['a', 'b', 'c']), '¬ab');
});
