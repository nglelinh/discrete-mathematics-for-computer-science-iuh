/** Otomat hữu hạn: DFA / NFA / ε-NFA. Máy: { states:[{id,x,y}], start, accept:[id], edges:[{from,to,syms:[...]}] } */

export const EPS = 'ε';

export function normSym(s) {
  const t = String(s).trim();
  return t === 'e' || t === 'eps' || t === 'ε' || t === '' ? EPS : t[0];
}

export function alphabetOf(M) {
  const a = new Set();
  M.edges.forEach((e) => e.syms.forEach((s) => s !== EPS && a.add(s)));
  return [...a].sort();
}

export function delta(M, id, sym) {
  const out = [];
  M.edges.forEach((e) => { if (e.from === id && e.syms.includes(sym)) out.push(e.to); });
  return out;
}

const uniqSorted = (xs, order) => [...new Set(xs)].sort((a, b) => order.indexOf(a) - order.indexOf(b));

export function epsClosure(M, set) {
  const order = M.states.map((s) => s.id);
  const seen = new Set(set);
  const stack = [...set];
  while (stack.length) {
    const u = stack.pop();
    for (const v of delta(M, u, EPS)) if (!seen.has(v)) { seen.add(v); stack.push(v); }
  }
  return uniqSorted([...seen], order);
}

export function move(M, set, sym) {
  const order = M.states.map((s) => s.id);
  return uniqSorted(set.flatMap((u) => delta(M, u, sym)), order);
}

/** Mô phỏng từng ký tự: trả về mỗi bước tập trạng thái hiện hành (đã đóng ε). */
export function simulate(M, input) {
  let cur = epsClosure(M, [M.start]);
  const trace = [{ pos: 0, set: cur, sym: null, from: null }];
  for (let i = 0; i < input.length; i++) {
    const a = input[i];
    const moved = move(M, cur, a);
    const next = epsClosure(M, moved);
    trace.push({ pos: i + 1, set: next, sym: a, from: cur, moved });
    cur = next;
  }
  const acc = cur.some((s) => M.accept.includes(s));
  return { trace, accept: acc, final: cur };
}

export function accepts(M, input) {
  return simulate(M, input).accept;
}

export function isDFA(M) {
  if (M.edges.some((e) => e.syms.includes(EPS))) return false;
  const seen = new Set();
  for (const e of M.edges) for (const s of e.syms) {
    const key = e.from + '|' + s;
    if (seen.has(key)) return false;
    seen.add(key);
  }
  return true;
}
export function isComplete(M) {
  const A = alphabetOf(M);
  return M.states.every((st) => A.every((a) => delta(M, st.id, a).length > 0));
}

const keyOf = (set) => (set.length ? set.join(',') : '∅');

/** Chuyển NFA → DFA bằng xây dựng tập con. Trả về các bước, bảng và máy DFA. */
export function subsetConstruction(M) {
  const A = alphabetOf(M);
  const startSet = epsClosure(M, [M.start]);
  const rows = [];
  const index = new Map();
  const queue = [];
  const addRow = (set) => {
    const key = keyOf(set);
    if (!index.has(key)) {
      index.set(key, rows.length);
      rows.push({ key, set, trans: {}, accept: set.some((s) => M.accept.includes(s)), discoveredBy: null });
      queue.push(key);
    }
    return key;
  };
  addRow(startSet);
  const steps = [];
  while (queue.length) {
    const key = queue.shift();
    const row = rows[index.get(key)];
    const results = {};
    const fresh = [];
    for (const a of A) {
      const moved = move(M, row.set, a);
      const closure = epsClosure(M, moved);
      const before = rows.length;
      const k2 = addRow(closure);
      if (rows.length > before) { fresh.push(k2); rows[index.get(k2)].discoveredBy = `${row.key} —${a}→`; }
      row.trans[a] = k2;
      results[a] = { moved, closure, key: k2 };
    }
    steps.push({ key, results, fresh, rowsAfter: rows.length });
  }
  // máy DFA
  const layer = new Map([[rows[0].key, 0]]);
  rows.forEach((r) => A.forEach((a) => { const t = r.trans[a]; if (!layer.has(t)) layer.set(t, (layer.get(r.key) || 0) + 1); }));
  const perLayer = {};
  const states = rows.map((r) => {
    const L = layer.get(r.key) || 0;
    perLayer[L] = (perLayer[L] || 0) + 1;
    return { id: r.key, x: 70 + L * 150, y: 0, layer: L, slot: perLayer[L] - 1 };
  });
  states.forEach((s) => { const n = perLayer[s.layer]; s.y = 40 + ((s.slot + 0.5) * 300) / n; });
  const edgeMap = new Map();
  rows.forEach((r) => A.forEach((a) => {
    const t = r.trans[a];
    const k = r.key + '>' + t;
    if (!edgeMap.has(k)) edgeMap.set(k, { from: r.key, to: t, syms: [] });
    edgeMap.get(k).syms.push(a);
  }));
  const dfa = {
    states: states.map(({ id, x, y }) => ({ id, x, y })),
    start: rows[0].key,
    accept: rows.filter((r) => r.accept).map((r) => r.key),
    edges: [...edgeMap.values()]
  };
  return { alphabet: A, rows, steps, dfa };
}

/** Tối thiểu hóa DFA đầy đủ bằng tinh chỉnh phân hoạch (Moore). */
export function minimizeDFA(D) {
  const A = alphabetOf(D);
  const ids = D.states.map((s) => s.id);
  const to = (s, a) => delta(D, s, a)[0];
  // chỉ giữ trạng thái đạt tới được
  const reach = new Set([D.start]);
  const st = [D.start];
  while (st.length) { const u = st.pop(); for (const a of A) { const v = to(u, a); if (v !== undefined && !reach.has(v)) { reach.add(v); st.push(v); } } }
  let cls = new Map();
  ids.filter((s) => reach.has(s)).forEach((s) => cls.set(s, D.accept.includes(s) ? 1 : 0));
  const rounds = [];
  for (;;) {
    const sig = new Map();
    const next = new Map();
    for (const [s] of cls) {
      const key = cls.get(s) + '|' + A.map((a) => cls.get(to(s, a))).join(',');
      if (!sig.has(key)) sig.set(key, sig.size);
      next.set(s, sig.get(key));
    }
    rounds.push(new Map(next));
    const same = new Set(next.values()).size === new Set(cls.values()).size;
    cls = next;
    if (same) break;
  }
  const groups = new Map();
  for (const [s, c] of cls) { if (!groups.has(c)) groups.set(c, []); groups.get(c).push(s); }
  const list = [...groups.values()];
  const name = (g) => '{' + g.join(',') + '}';
  const gOf = (s) => list.find((g) => g.includes(s));
  const states = list.map((g, i) => {
    const o = D.states.find((x) => x.id === g[0]);
    return { id: name(g), x: o.x, y: o.y };
  });
  const edgeMap = new Map();
  list.forEach((g) => A.forEach((a) => {
    const t = name(gOf(to(g[0], a)));
    const k = name(g) + '>' + t;
    if (!edgeMap.has(k)) edgeMap.set(k, { from: name(g), to: t, syms: [] });
    edgeMap.get(k).syms.push(a);
  }));
  const min = {
    states,
    start: name(gOf(D.start)),
    accept: list.filter((g) => D.accept.includes(g[0])).map(name),
    edges: [...edgeMap.values()]
  };
  return { groups: list, machine: min, rounds: rounds.length, removed: ids.filter((s) => !reach.has(s)) };
}

export function stringsUpTo(alphabet, maxLen) {
  const out = [''];
  let layer = [''];
  for (let l = 1; l <= maxLen; l++) {
    const next = [];
    for (const w of layer) for (const a of alphabet) next.push(w + a);
    out.push(...next);
    layer = next;
  }
  return out;
}

const S = (ids) => ids.map((id, i) => ({ id, x: 0, y: 0 }));
function place(M, pts) { M.states.forEach((s, i) => { s.x = pts[i][0]; s.y = pts[i][1]; }); return M; }

export const PRESETS = [
  { id: 'dfa01', label: 'DFA: kết thúc bằng "01"', alpha: '01', example: '1101',
    make: () => place({ states: S(['q0', 'q1', 'q2']), start: 'q0', accept: ['q2'], edges: [
      { from: 'q0', to: 'q1', syms: ['0'] }, { from: 'q0', to: 'q0', syms: ['1'] },
      { from: 'q1', to: 'q1', syms: ['0'] }, { from: 'q1', to: 'q2', syms: ['1'] },
      { from: 'q2', to: 'q1', syms: ['0'] }, { from: 'q2', to: 'q0', syms: ['1'] }] }, [[90, 150], [250, 150], [410, 150]]) },
  { id: 'even1', label: 'DFA: số lượng chữ số 1 là chẵn', alpha: '01', example: '10110',
    make: () => place({ states: S(['chan', 'le']), start: 'chan', accept: ['chan'], edges: [
      { from: 'chan', to: 'chan', syms: ['0'] }, { from: 'chan', to: 'le', syms: ['1'] },
      { from: 'le', to: 'le', syms: ['0'] }, { from: 'le', to: 'chan', syms: ['1'] }] }, [[130, 150], [350, 150]]) },
  { id: 'nfa101', label: 'NFA: chứa chuỗi con "101"', alpha: '01', example: '0010110',
    make: () => place({ states: S(['q0', 'q1', 'q2', 'q3']), start: 'q0', accept: ['q3'], edges: [
      { from: 'q0', to: 'q0', syms: ['0', '1'] }, { from: 'q0', to: 'q1', syms: ['1'] },
      { from: 'q1', to: 'q2', syms: ['0'] }, { from: 'q2', to: 'q3', syms: ['1'] },
      { from: 'q3', to: 'q3', syms: ['0', '1'] }] }, [[70, 150], [210, 150], [350, 150], [490, 150]]) },
  { id: 'nfa3', label: 'NFA: ký tự thứ 3 từ cuối là 1 (DFA có 8 trạng thái)', alpha: '01', example: '0100',
    make: () => place({ states: S(['q0', 'q1', 'q2', 'q3']), start: 'q0', accept: ['q3'], edges: [
      { from: 'q0', to: 'q0', syms: ['0', '1'] }, { from: 'q0', to: 'q1', syms: ['1'] },
      { from: 'q1', to: 'q2', syms: ['0', '1'] }, { from: 'q2', to: 'q3', syms: ['0', '1'] }] }, [[70, 150], [210, 150], [350, 150], [490, 150]]) },
  { id: 'enfa', label: 'ε-NFA: a*b* (có chuyển ε)', alpha: 'ab', example: 'aabb',
    make: () => place({ states: S(['p', 'r']), start: 'p', accept: ['r'], edges: [
      { from: 'p', to: 'p', syms: ['a'] }, { from: 'p', to: 'r', syms: ['ε'] }, { from: 'r', to: 'r', syms: ['b'] }] }, [[150, 150], [350, 150]]) },
  { id: 'empty', label: 'Trống (tự vẽ)', alpha: '01', example: '01',
    make: () => place({ states: S(['q0']), start: 'q0', accept: [], edges: [] }, [[100, 150]]) }
];
