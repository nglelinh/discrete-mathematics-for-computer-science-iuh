/** Netlist mạch logic (từ AST hoặc từ phủ SOP/POS), tính giá trị và bố cục. */

export function netlistFromAst(ast, names) {
  const nodes = [];
  const inputs = new Map();
  const add = (n) => {
    n.id = nodes.length;
    nodes.push(n);
    return n.id;
  };
  for (const name of names) inputs.set(name, add({ kind: 'in', name, ins: [] }));
  function go(a) {
    switch (a.type) {
      case 'VAR':
        return inputs.get(a.name);
      case 'CONST':
        return add({ kind: 'const', value: a.value, name: String(a.value), ins: [] });
      case 'NOT':
        return add({ kind: 'gate', op: 'NOT', ins: [go(a.arg)] });
      default:
        return add({ kind: 'gate', op: a.type, ins: [go(a.left), go(a.right)] });
    }
  }
  const root = go(ast);
  const out = add({ kind: 'out', name: 'F', ins: [root] });
  return { nodes, out };
}

export function netlistFromCover(cover, names, kind) {
  const nodes = [];
  const add = (n) => {
    n.id = nodes.length;
    nodes.push(n);
    return n.id;
  };
  const inputs = names.map((name) => add({ kind: 'in', name, ins: [] }));
  const nots = new Map();
  const litNode = (i, neg) => {
    if (!neg) return inputs[i];
    if (!nots.has(i)) nots.set(i, add({ kind: 'gate', op: 'NOT', ins: [inputs[i]] }));
    return nots.get(i);
  };
  const inner = kind === 'sop' ? 'AND' : 'OR';
  const outer = kind === 'sop' ? 'OR' : 'AND';
  const terms = [];
  for (const g of cover) {
    const lits = [];
    for (let i = 0; i < g.bits.length; i++) {
      if (g.bits[i] === '-') continue;
      const one = g.bits[i] === '1';
      lits.push(litNode(i, kind === 'sop' ? !one : one));
    }
    if (!lits.length) terms.push(add({ kind: 'const', value: kind === 'sop' ? 1 : 0, name: kind === 'sop' ? '1' : '0', ins: [] }));
    else if (lits.length === 1) terms.push(lits[0]);
    else terms.push(add({ kind: 'gate', op: inner, ins: lits }));
  }
  let root;
  if (!terms.length) root = add({ kind: 'const', value: kind === 'sop' ? 0 : 1, name: kind === 'sop' ? '0' : '1', ins: [] });
  else if (terms.length === 1) root = terms[0];
  else root = add({ kind: 'gate', op: outer, ins: terms });
  const out = add({ kind: 'out', name: 'F', ins: [root] });
  return { nodes, out };
}

export function evalNet(net, env) {
  const memo = new Array(net.nodes.length);
  const val = (id) => {
    if (memo[id] !== undefined) return memo[id];
    const n = net.nodes[id];
    let v;
    if (n.kind === 'in') v = env[n.name] ? 1 : 0;
    else if (n.kind === 'const') v = n.value ? 1 : 0;
    else if (n.kind === 'out') v = val(n.ins[0]);
    else {
      const a = n.ins.map(val);
      switch (n.op) {
        case 'NOT': v = a[0] ? 0 : 1; break;
        case 'AND': v = a.every(Boolean) ? 1 : 0; break;
        case 'OR': v = a.some(Boolean) ? 1 : 0; break;
        case 'XOR': v = a.reduce((x, y) => x ^ y, 0); break;
        case 'IMP': v = a[0] ? a[1] : 1; break;
        case 'IFF': v = a[0] === a[1] ? 1 : 0; break;
        default: v = 0;
      }
    }
    memo[id] = v;
    return v;
  };
  net.nodes.forEach((_, i) => val(i));
  return memo;
}

export function layoutNet(net, { colW = 96, rowGap = 50, padX = 56, padY = 30 } = {}) {
  const level = new Array(net.nodes.length).fill(0);
  net.nodes.forEach((n) => {
    if (n.kind === 'gate' || n.kind === 'out') level[n.id] = 1 + Math.max(...n.ins.map((i) => level[i]));
  });
  const maxL = Math.max(...level);
  const pos = new Array(net.nodes.length);
  const byLevel = [];
  net.nodes.forEach((n) => (byLevel[level[n.id]] ||= []).push(n));
  byLevel.forEach((col, L) => {
    if (!col) return;
    col.forEach((n, k) => {
      n._want = L === 0 || !n.ins.length ? k * rowGap : n.ins.reduce((s, i) => s + pos[i].y, 0) / n.ins.length;
    });
    col.sort((a, b) => a._want - b._want);
    let last = -Infinity;
    col.forEach((n) => {
      let y = Math.max(n._want, last + rowGap);
      last = y;
      pos[n.id] = { x: padX + L * colW, y };
    });
    // đưa cột về gần vị trí mong muốn trung bình
    const shift = col.reduce((s, n) => s + (n._want - pos[n.id].y), 0) / col.length;
    col.forEach((n) => (pos[n.id].y += shift));
  });
  const minY = Math.min(...pos.map((p) => p.y));
  pos.forEach((p) => (p.y += padY - minY));
  const height = Math.max(...pos.map((p) => p.y)) + padY + 6;
  const width = padX * 2 + maxL * colW;
  return { pos, level, width, height };
}
