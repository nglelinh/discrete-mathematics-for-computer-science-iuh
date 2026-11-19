import test from 'node:test';
import assert from 'node:assert/strict';
import { makeMatrix, properties, warshallSteps, transitiveClosure, symmetricClosure, reflexiveClosure, equivalenceClasses, hasse, PRESETS } from '../src/relation/relations.js';
import { analyze, inverse, compose, PRESETS as FP } from '../src/function/functions.js';

let seed = 99;
const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
const randM = (n, p = 0.3) => makeMatrix(n, () => rnd() < p);
const names = (n) => Array.from({ length: n }, (_, i) => String(i));

test('tính chất khớp định nghĩa; phản ví dụ đúng là phản ví dụ', () => {
  for (let t = 0; t < 400; t++) {
    const n = 2 + Math.floor(rnd() * 4);
    const M = randM(n, rnd());
    const P = properties(M, names(n));
    let refl = true, irr = true, sym = true, anti = true, asym = true, tr = true;
    for (let i = 0; i < n; i++) {
      if (!M[i][i]) refl = false;
      if (M[i][i]) irr = false;
      for (let j = 0; j < n; j++) {
        if (M[i][j] && !M[j][i]) sym = false;
        if (M[i][j] && M[j][i] && i !== j) anti = false;
        if (M[i][j] && M[j][i]) asym = false;
        for (let k = 0; k < n; k++) if (M[i][j] && M[j][k] && !M[i][k]) tr = false;
      }
    }
    assert.equal(P.reflexive.ok, refl); assert.equal(P.irreflexive.ok, irr); assert.equal(P.symmetric.ok, sym);
    assert.equal(P.antisymmetric.ok, anti); assert.equal(P.asymmetric.ok, asym); assert.equal(P.transitive.ok, tr);
    for (const key of ['reflexive', 'irreflexive', 'symmetric', 'antisymmetric', 'asymmetric', 'transitive']) {
      if (!P[key].ok) assert.ok(P[key].witness && P[key].witness.cells.length, key);
    }
    if (!P.transitive.ok) {
      const [[i, j], [, k]] = P.transitive.witness.cells;
      assert.ok(M[i][j] && M[j][k] && !M[i][k]);
    }
  }
});

test('Warshall = bao đóng bắc cầu tính bằng lũy thừa lặp', () => {
  for (let t = 0; t < 200; t++) {
    const n = 2 + Math.floor(rnd() * 5);
    const M = randM(n, 0.25);
    let R = M.map((r) => r.slice());
    for (let it = 0; it < n; it++) {
      const N = R.map((r) => r.slice());
      for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) for (let k = 0; k < n; k++) if (R[i][k] && R[k][j]) N[i][j] = true;
      R = N;
    }
    assert.deepEqual(transitiveClosure(M), R);
    const steps = warshallSteps(M);
    assert.equal(steps.length, n + 1);
    assert.equal(properties(steps[n].M, names(n)).transitive.ok, true);
  }
});

test('bao đóng phản xạ/đối xứng cho tính chất tương ứng', () => {
  for (let t = 0; t < 100; t++) {
    const n = 3 + Math.floor(rnd() * 3);
    const M = randM(n);
    assert.equal(properties(reflexiveClosure(M).R, names(n)).reflexive.ok, true);
    assert.equal(properties(symmetricClosure(M).R, names(n)).symmetric.ok, true);
  }
});

test('preset: mod 2 là tương đương với 2 lớp; ước số là thứ tự riêng phần; bạn bè không bắc cầu', () => {
  const build = (id) => { const p = PRESETS.find((x) => x.id === id); return { M: makeMatrix(p.labels.length, p.f), labels: p.labels }; };
  const a = build('mod2');
  assert.equal(properties(a.M, a.labels).equivalence.ok, true);
  assert.equal(equivalenceClasses(a.M).length, 2);
  const b = build('div');
  assert.equal(properties(b.M, b.labels).partialOrder.ok, true);
  assert.equal(properties(b.M, b.labels).equivalence.ok, false);
  const h = hasse(b.M);
  assert.deepEqual(h.minimal, [0]); assert.deepEqual(h.maximal, [5]);
  assert.equal(h.cover.length, 7); // 1-2,1-3,2-4,2-6,3-6,4-12,6-12
  const c = build('sym');
  assert.equal(properties(c.M, c.labels).transitive.ok, false);
});

test('hàm: đơn ánh / toàn ánh / song ánh, nghịch đảo, hợp thành', () => {
  const [inj, surj, bij, , inc, bad] = FP.filter((p) => ['inj', 'surj', 'bij', 'sq', 'inc', 'bad'].includes(p.id));
  let a = analyze(inj.f, inj.nx, inj.ny); assert.ok(a.injective && !a.surjective && a.missed.length === 2);
  a = analyze(surj.f, surj.nx, surj.ny); assert.ok(!a.injective && a.surjective && a.collisions.length === 2);
  a = analyze(bij.f, bij.nx, bij.ny); assert.ok(a.bijective);
  a = analyze(bad.f, bad.nx, bad.ny); assert.ok(!a.wellDefined && a.unassigned.length === 1);
  const g = inverse(inc.f, 5, 5);
  assert.deepEqual(compose(g, inc.f, 5), [0, 1, 2, 3, 4]);
  assert.equal(inverse(inj.f, 3, 5), null);
  // đơn ánh ∘ đơn ánh là đơn ánh
  for (let t = 0; t < 200; t++) {
    const f = Array.from({ length: 3 }, () => Math.floor(rnd() * 5));
    const gg = Array.from({ length: 5 }, () => Math.floor(rnd() * 6));
    if (analyze(f, 3, 5).injective && analyze(gg, 5, 6).injective) assert.ok(analyze(compose(gg, f, 3), 3, 6).injective);
    if (analyze(f, 3, 5).surjective && analyze(gg, 5, 6).surjective) assert.ok(analyze(compose(gg, f, 3), 3, 6).surjective);
  }
});
