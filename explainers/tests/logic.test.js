import test from 'node:test';
import assert from 'node:assert/strict';
import { INDUCTION_PRESETS, inductionSteps } from '../src/logic/induction.js';
import { parseCNF, dpllSteps, evalCNF, bruteSat, DPLL_PRESETS } from '../src/logic/dpll.js';
import { bitsOf, fromBits, toSigned, fromSigned, negateStages, addSteps, range, bytesOf, valueOfBytes, y2038 } from '../src/logic/bits.js';

function rng(seed) { let s = seed; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 2 ** 32); }

test('quy nạp: các mệnh đề hợp lệ đúng với mọi n nhỏ', () => {
  for (const id of ['sum', 'pow2', 'div3']) {
    const p = INDUCTION_PRESETS.find((x) => x.id === id);
    for (let n = p.n0; n <= 300; n++) assert.ok(p.holds(BigInt(n)), id + ' ' + n);
    const st = inductionSteps(p);
    assert.equal(st[st.length - 1].fallen, p.count);
    assert.equal(st[st.length - 1].bad, null);
  }
});
test('quy nạp: n²+n+41 gãy đầu tiên tại n = 40; thiếu cơ sở không đổ domino nào', () => {
  const p = INDUCTION_PRESETS.find((x) => x.id === 'prime');
  for (let n = 0; n < 40; n++) assert.ok(p.holds(BigInt(n)));
  assert.ok(!p.holds(40n));
  const st = inductionSteps(p);
  assert.equal(st[st.length - 1].bad, 40);
  const nb = inductionSteps(INDUCTION_PRESETS.find((x) => x.id === 'nobase'));
  assert.equal(nb[nb.length - 1].fallen, 0);
});

test('DPLL: parse và preset', () => {
  const r = parseCNF('(p ∨ ¬q) ∧ (q ∨ r)');
  assert.deepEqual(r.names, ['p', 'q', 'r']);
  assert.deepEqual(r.clauses, [[1, -2], [2, 3]]);
  assert.ok(parseCNF('p, !!q').clauses[1][0] === 2);
  assert.ok(parseCNF('p ?? q').error);
  const expect = { sat: true, unit: true, unsat: false, php: false };
  for (const pr of DPLL_PRESETS) {
    const c = parseCNF(pr.text);
    const res = dpllSteps(c.clauses, c.names);
    assert.equal(res.sat, expect[pr.id], pr.id);
    assert.equal(res.steps[res.steps.length - 1].result, expect[pr.id] ? 'sat' : 'unsat');
    if (res.sat) assert.ok(evalCNF(c.clauses, res.model));
  }
});
test('DPLL khớp vét cạn trên 3-CNF ngẫu nhiên', () => {
  const r = rng(11);
  for (let t = 0; t < 250; t++) {
    const nv = 3 + Math.floor(r() * 4), nc = 3 + Math.floor(r() * 12);
    const clauses = [];
    for (let i = 0; i < nc; i++) {
      const c = new Set();
      while (c.size < 3) { const v = 1 + Math.floor(r() * nv); c.add(r() < 0.5 ? v : -v); }
      clauses.push([...c].filter((l, _, arr) => !arr.includes(-l)));
    }
    const names = Array.from({ length: nv }, (_, i) => 'x' + (i + 1));
    const res = dpllSteps(clauses.filter((c) => c.length), names);
    assert.equal(res.sat, bruteSat(clauses.filter((c) => c.length), nv));
    if (res.sat) assert.ok(evalCNF(clauses.filter((c) => c.length), res.model));
  }
});

test('bù hai: bit ↔ giá trị, số đối bằng đảo bit + 1', () => {
  for (const n of [4, 8]) {
    const { min, max } = range(n);
    for (let x = min; x <= max; x++) {
      const u = fromSigned(x, n);
      assert.equal(toSigned(u, n), x);
      assert.equal(fromBits(bitsOf(u, n)), u);
      const [, inv, neg] = negateStages(u, n);
      assert.equal(toSigned(neg, n), x === min ? min : -x);
      assert.equal(inv + 1n & ((1n << BigInt(n)) - 1n), neg);
    }
  }
});
test('cộng có nhớ: đúng mod 2ⁿ và cờ tràn đúng với phạm vi số có dấu', () => {
  const n = 8; const { min, max } = range(n);
  for (let x = -128; x <= 127; x += 5) for (let y = -128; y <= 127; y += 7) {
    const r = addSteps(fromSigned(x, n), fromSigned(y, n), n);
    assert.equal(toSigned(r.result, n), BigInt.asIntN(8, BigInt(x + y)));
    const real = BigInt(x + y);
    assert.equal(r.overflow, real < min || real > max, `${x}+${y}`);
  }
});
test('endianness và Y2038', () => {
  assert.deepEqual(bytesOf(0x12345678, 'big'), [0x12, 0x34, 0x56, 0x78]);
  assert.deepEqual(bytesOf(0x12345678, 'little'), [0x78, 0x56, 0x34, 0x12]);
  for (const o of ['big', 'little']) assert.equal(valueOfBytes(bytesOf(0xdeadbeef, o), o), 0xdeadbeefn);
  assert.equal(y2038(0).wrapped, 2147483647n);
  assert.equal(y2038(0).wrappedDate, '2038-01-19 03:14:07 UTC');
  assert.equal(y2038(1).wrapped, -2147483648n);
  assert.equal(y2038(1).wrappedDate, '1901-12-13 20:45:52 UTC');
});
