// CFG → PDA: đẩy S, với mỗi luật A→α thay A bằng α; với mỗi ký hiệu kết thúc a ở đỉnh thì đọc a và lấy ra.

/** BFS trên (vị trí, ngăn xếp). Trả về đường chấp nhận ngắn nhất hoặc nhánh đi xa nhất. */
export function runCfgPda(g, tokens, cap = 60000) {
  const key = (c) => c.pos + '|' + c.stack.join(' ');
  const start = { pos: 0, stack: [g.start], action: 'Khởi động: đặt ký hiệu khởi đầu ' + g.start + ' lên ngăn xếp (ở trên $).' };
  const parent = new Map([[key(start), null]]);
  const q = [start];
  let found = null, best = start, n = 0;
  while (q.length && n++ < cap) {
    const c = q.shift();
    if (c.pos === tokens.length && c.stack.length === 0) { found = c; break; }
    if (c.pos > best.pos || (c.pos === best.pos && c.stack.length < best.stack.length)) best = c;
    if (!c.stack.length) continue;
    const [top, ...rest] = c.stack;
    const nexts = [];
    if (g.isVar(top)) {
      for (const r of g.rules) if (r.lhs === top) nexts.push({ pos: c.pos, stack: [...r.rhs, ...rest], action: `Mở rộng: lấy ${top} ra, đẩy ${r.rhs.join(' ')} vào (luật ${top} → ${r.rhs.join(' ')}).` });
    } else if (tokens[c.pos] === top) nexts.push({ pos: c.pos + 1, stack: rest, action: `Khớp ký hiệu “${top}”: đọc “${top}” và lấy ra khỏi ngăn xếp.` });
    for (const nx of nexts) {
      if (nx.stack.length > tokens.length - nx.pos) continue; // mỗi ký hiệu sinh ≥ 1 token
      const k = key(nx);
      if (parent.has(k)) continue;
      parent.set(k, c); nx.prev = c; q.push(nx);
    }
  }
  const end = found || best;
  const path = [];
  for (let c = end; c; c = c.prev ?? null) path.unshift(c);
  return { accepted: !!found, path };
}
