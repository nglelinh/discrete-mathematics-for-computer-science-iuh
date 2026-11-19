// Máy Mealy (xuất theo chuyển tiếp) và Moore (xuất theo trạng thái).

export const MEALY_PRESETS = [
  {
    id: 'm11', kind: 'mealy', name: 'Mealy: báo “11” (xuất 1 khi vừa đọc hai bit 1 liên tiếp)', input: '0110111',
    start: 's0', states: [{ id: 's0', x: 150, y: 120 }, { id: 's1', x: 400, y: 120 }],
    trans: { s0: { 0: ['s0', '0'], 1: ['s1', '0'] }, s1: { 0: ['s0', '0'], 1: ['s1', '1'] } },
    ref: (w) => [...w].map((c, i) => (c === '1' && w[i - 1] === '1' ? '1' : '0'))
  },
  {
    id: 'add', kind: 'mealy', name: 'Mealy: cộng nối tiếp hai số nhị phân (bit thấp trước)', input: '11 01 10 00',
    desc: 'Mỗi ký hiệu là cặp bit (a b). Trạng thái nhớ c0/c1; xuất bit tổng.',
    start: 'c0', states: [{ id: 'c0', x: 150, y: 120 }, { id: 'c1', x: 400, y: 120 }],
    trans: {
      c0: { '00': ['c0', '0'], '01': ['c0', '1'], '10': ['c0', '1'], '11': ['c1', '0'] },
      c1: { '00': ['c0', '1'], '01': ['c1', '0'], '10': ['c1', '0'], '11': ['c1', '1'] }
    },
    ref: (w) => { let c = 0; return w.split(' ').map((t) => { const s = +t[0] + +t[1] + c; c = s >> 1; return String(s & 1); }); }
  },
  {
    id: 'mod3', kind: 'moore', name: 'Moore: đếm số bit 1 modulo 3 (đầu ra gắn với trạng thái)', input: '1101',
    start: 'm0', states: [{ id: 'm0', x: 90, y: 120, out: '0' }, { id: 'm1', x: 270, y: 120, out: '1' }, { id: 'm2', x: 450, y: 120, out: '2' }],
    trans: { m0: { 0: ['m0'], 1: ['m1'] }, m1: { 0: ['m1'], 1: ['m2'] }, m2: { 0: ['m2'], 1: ['m0'] } },
    ref: (w) => { let c = 0; return ['0', ...[...w].map((x) => { if (x === '1') c++; return String(c % 3); })]; }
  }
];

export const tokens = (p, w) => (w.includes(' ') || p.id === 'add' ? w.trim().split(/\s+/).filter(Boolean) : [...w.trim()]);

/** Trả về bước: { state, read, out, outputs } (Moore xuất cả ở trạng thái đầu). */
export function runTransducer(p, input) {
  const toks = tokens(p, input);
  const outs = [];
  let st = p.start;
  const moore = p.kind === 'moore';
  const steps = [{ state: st, read: null, out: moore ? p.states.find((s) => s.id === st).out : null, outputs: moore ? [p.states.find((s) => s.id === st).out] : [], pos: 0 }];
  if (moore) outs.push(steps[0].out);
  for (let i = 0; i < toks.length; i++) {
    const t = p.trans[st]?.[toks[i]];
    if (!t) return { error: `Ký hiệu “${toks[i]}” không có chuyển tiếp từ ${st}.`, steps, outputs: outs, toks };
    st = t[0];
    const o = moore ? p.states.find((s) => s.id === st).out : t[1];
    outs.push(o);
    steps.push({ state: st, read: toks[i], out: o, outputs: [...outs], pos: i + 1 });
  }
  return { steps, outputs: outs, toks };
}

export function viewMachine(p) {
  const moore = p.kind === 'moore';
  const states = p.states.map((s) => ({ id: moore ? `${s.id}/${s.out}` : s.id, x: s.x, y: s.y }));
  const nm = (id) => (moore ? `${id}/${p.states.find((s) => s.id === id).out}` : id);
  const edges = [];
  for (const [from, row] of Object.entries(p.trans)) {
    const grouped = {};
    for (const [sym, t] of Object.entries(row)) (grouped[t[0]] ||= []).push(moore ? sym : `${sym}/${t[1]}`);
    for (const [to, syms] of Object.entries(grouped)) edges.push({ from: nm(from), to: nm(to), syms });
  }
  return { states, start: nm(p.start), accept: [], edges, nameOf: nm };
}
