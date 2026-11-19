import test from 'node:test';
import assert from 'node:assert/strict';
import { to3SAT, GRAPH_PRESETS, isIndependent, isVertexCover, isClique, complement, subsets, maxIndependent, minVertexCover, approxVCSteps } from '../src/complexity/reductions.js';
import { parseCNF, bruteSat } from '../src/logic/dpll.js';

function rng(seed) { let s = seed; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 2 ** 32); }

test('SAT → 3-SAT: mọi mệnh đề đúng 3 literal và tương đương về khả thỏa', () => {
  const r = rng(3);
  for (let t = 0; t < 120; t++) {
    const nv = 2 + Math.floor(r() * 3), nc = 1 + Math.floor(r() * 4);
    const clauses = [];
    for (let i = 0; i < nc; i++) {
      const k = 1 + Math.floor(r() * 5), c = new Set();
      while (c.size < Math.min(k, nv)) { const v = 1 + Math.floor(r() * nv); c.add(r() < 0.5 ? v : -v); }
      const arr = [...c].filter((l, _, a) => !a.includes(-l));
      if (arr.length) clauses.push(arr);
    }
    if (!clauses.length) continue;
    const names = Array.from({ length: nv }, (_, i) => 'x' + (i + 1));
    const out = to3SAT(clauses, names);
    assert.ok(out.clauses.every((c) => c.length === 3), JSON.stringify(clauses));
    if (out.names.length <= 13) assert.equal(bruteSat(out.clauses, out.names.length), bruteSat(clauses, nv), JSON.stringify(clauses));
  }
  const p = parseCNF('(a) ∧ (a ∨ b) ∧ (a ∨ b ∨ c ∨ d ∨ e)');
  const o = to3SAT(p.clauses, p.names);
  assert.equal(o.clauses.length, 4 + 2 + 3);
});

test('IS ⇔ phủ đỉnh bù ⇔ clique trong đồ thị bù; α + τ = n', () => {
  for (const g of GRAPH_PRESETS) {
    const ids = g.nodes.map((n) => n.id);
    const gc = complement(g);
    for (const S of subsets(ids)) {
      const rest = ids.filter((x) => !S.includes(x));
      assert.equal(isIndependent(g, S), isVertexCover(g, rest));
      assert.equal(isIndependent(g, S), isClique(gc, S));
    }
    assert.equal(maxIndependent(g).length + minVertexCover(g).length, ids.length);
  }
});

test('2-xấp xỉ Vertex Cover hợp lệ, ≤ 2·OPT, các cạnh chọn rời nhau', () => {
  const r = rng(9);
  const gs = [...GRAPH_PRESETS];
  for (let t = 0; t < 120; t++) {
    const n = 3 + Math.floor(r() * 5);
    const nodes = Array.from({ length: n }, (_, i) => ({ id: 'n' + i, x: 0, y: 0 }));
    const edges = [];
    for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) if (r() < 0.4) edges.push(['n' + i, 'n' + j]);
    if (edges.length) gs.push({ nodes, edges });
  }
  for (const g of gs) {
    const st = approxVCSteps(g), fin = st.at(-1);
    assert.ok(isVertexCover(g, fin.cover));
    assert.ok(fin.cover.length <= 2 * fin.opt);
    const ends = fin.chosen.flat();
    assert.equal(new Set(ends).size, ends.length);
  }
  const worst = approxVCSteps(GRAPH_PRESETS.find((p) => p.id === 'matching')).at(-1);
  assert.equal(worst.cover.length, 2 * worst.opt);
});
