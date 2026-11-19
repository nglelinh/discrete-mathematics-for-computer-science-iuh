import test from 'node:test';
import assert from 'node:assert/strict';
import { TOPO_PRESETS, withCycle, kahnSteps, dfsSteps, finalOrder, isTopoOrder, hasCycleBrute, indegrees } from '../src/graph/topo.js';

function rng(seed) { let s = seed; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 2 ** 32); }
function randomGraph(r, n, p) {
  const nodes = Array.from({ length: n }, (_, i) => ({ id: 'v' + i, label: 'v' + i, x: 0, y: 0 }));
  const edges = [];
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) if (i !== j && r() < p) edges.push(['v' + i, 'v' + j]);
  return { nodes, edges };
}

test('preset: Kahn và DFS cho thứ tự topo hợp lệ trên DAG', () => {
  for (const p of TOPO_PRESETS) {
    const g = withCycle(p, false);
    assert.equal(hasCycleBrute(g), false);
    for (const f of [kahnSteps, dfsSteps]) {
      const st = f(g); const o = finalOrder(st);
      assert.ok(isTopoOrder(g, o), p.id + ' ' + f.name);
    }
  }
});

test('preset + cạnh ngược: cả hai phát hiện chu trình', () => {
  for (const p of TOPO_PRESETS) {
    const g = withCycle(p, true);
    assert.equal(hasCycleBrute(g), true, p.id);
    assert.equal(finalOrder(kahnSteps(g)), null);
    assert.equal(finalOrder(dfsSteps(g)), null);
  }
});

test('ví dụ A,B,C,D: Kahn ra A,B,C,D', () => {
  const g = withCycle(TOPO_PRESETS.find((p) => p.id === 'diamond'), false);
  assert.deepEqual(finalOrder(kahnSteps(g)), ['A', 'B', 'C', 'D']);
  assert.deepEqual(indegrees(g), { A: 0, B: 1, C: 1, D: 2 });
});

test('đồ thị ngẫu nhiên: kết luận chu trình khớp với đối chiếu vét cạn', () => {
  const r = rng(7);
  for (let t = 0; t < 300; t++) {
    const g = randomGraph(r, 2 + Math.floor(r() * 6), 0.1 + r() * 0.3);
    const cyc = hasCycleBrute(g);
    const k = kahnSteps(g), d = dfsSteps(g);
    assert.equal(k[k.length - 1].cycle, cyc);
    assert.equal(d[d.length - 1].cycle, cyc);
    if (!cyc) { assert.ok(isTopoOrder(g, finalOrder(k))); assert.ok(isTopoOrder(g, finalOrder(d))); }
  }
});

test('Kahn: bậc vào không âm và số bước = số đỉnh + 3 trên DAG', () => {
  const g = withCycle(TOPO_PRESETS[0], false);
  const st = kahnSteps(g);
  assert.equal(st.length, g.nodes.length + 3);
  for (const s of st) for (const v of Object.values(s.indeg)) assert.ok(v >= 0);
});
