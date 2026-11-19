import test from 'node:test';
import assert from 'node:assert/strict';
import { MATCH_PRESETS, kuhnSteps, bruteMaxMatching, COLOR_PRESETS, orderOf, greedySteps, chromaticNumber, isProper, degree } from '../src/graph/match.js';

function rng(seed) { let s = seed; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 2 ** 32); }

test('ghép cặp: Kuhn đạt kích thước cực đại (so với vét cạn) và hợp lệ', () => {
  const r = rng(5);
  const graphs = [...MATCH_PRESETS];
  for (let t = 0; t < 200; t++) {
    const nl = 2 + Math.floor(r() * 5), nr = 2 + Math.floor(r() * 5);
    const left = Array.from({ length: nl }, (_, i) => ({ id: 'l' + i, y: 0 })), right = Array.from({ length: nr }, (_, i) => ({ id: 'r' + i, y: 0 }));
    const edges = [];
    for (const l of left) for (const q of right) if (r() < 0.4) edges.push([l.id, q.id]);
    graphs.push({ left, right, edges });
  }
  for (const g of graphs) {
    const st = kuhnSteps(g);
    const fin = st[st.length - 1];
    assert.equal(fin.size, bruteMaxMatching(g));
    for (const [l, q] of Object.entries(fin.matchL)) { assert.equal(fin.matchR[q], l); assert.ok(g.edges.some((e) => e[0] === l && e[1] === q)); }
    assert.equal(new Set(Object.values(fin.matchL)).size, fin.size);
  }
  assert.equal(kuhnSteps(MATCH_PRESETS[0]).at(-1).size, 4);
  assert.equal(kuhnSteps(MATCH_PRESETS[1]).at(-1).size, 2);
  assert.equal(kuhnSteps(MATCH_PRESETS[2]).at(-1).size, 4);
});

test('tô màu tham lam: hợp lệ, ≥ χ, ≤ Δ+1; thứ tự xấu dùng nhiều màu hơn', () => {
  for (const p of COLOR_PRESETS) {
    const chi = chromaticNumber(p);
    const maxDeg = Math.max(...p.nodes.map((n) => degree(p, n.id)));
    for (const kind of ['index', 'degree', 'bad']) {
      const st = greedySteps(p, orderOf(p, kind));
      const fin = st.at(-1);
      assert.ok(isProper(p, st.at(-1).color) && Object.keys(fin.color).length === p.nodes.length, p.id + kind);
      assert.ok(fin.used >= chi && fin.used <= maxDeg + 1);
    }
  }
  const crown = COLOR_PRESETS[0];
  assert.equal(chromaticNumber(crown), 2);
  assert.equal(greedySteps(crown, orderOf(crown, 'bad')).at(-1).used, 3);
  assert.equal(greedySteps(crown, orderOf(crown, 'degree')).at(-1).used, 2);
  assert.equal(chromaticNumber(COLOR_PRESETS[1]), 3);
});
