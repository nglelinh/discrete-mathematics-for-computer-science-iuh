// Otomat đẩy xuống không tất định: tìm đường chấp nhận bằng BFS trên cấu hình (trạng thái, vị trí, ngăn xếp).

/** Chuyển tiếp: [từ, ký hiệu đọc ('' = ε), đỉnh ngăn xếp ('' = ε), tới, chuỗi đẩy vào (ký tự đầu = đỉnh mới)]. */
export const PDA_PRESETS = [
  {
    id: 'anbn', name: 'aⁿbⁿ (n ≥ 0)', input: 'aabb', start: 'q0', accept: ['q3'],
    desc: 'Đẩy một A cho mỗi a; gặp b thì lấy một A ra. Ngăn xếp trống (chỉ còn $) đúng lúc hết chuỗi thì nhận.',
    trans: [
      ['q0', '', '', 'q1', '$'], ['q1', 'a', '', 'q1', 'A'], ['q1', 'b', 'A', 'q2', ''], ['q2', 'b', 'A', 'q2', ''],
      ['q1', '', '$', 'q3', ''], ['q2', '', '$', 'q3', '']
    ],
    oracle: (w) => { const m = /^(a*)(b*)$/.exec(w); return !!m && m[1].length === m[2].length; }
  },
  {
    id: 'ww', name: 'Palindrome chẵn wwᴿ (0/1)', input: '0110', start: 'q0', accept: ['q3'],
    desc: 'Không tất định: PDA đoán “đã tới giữa chuỗi” (bước ε), từ đó đối chiếu từng ký hiệu với đỉnh ngăn xếp.',
    trans: [
      ['q0', '', '', 'q1', '$'],
      ['q1', '0', '', 'q1', '0'], ['q1', '1', '', 'q1', '1'], ['q1', '', '', 'q2', ''],
      ['q2', '0', '0', 'q2', ''], ['q2', '1', '1', 'q2', ''], ['q2', '', '$', 'q3', '']
    ],
    oracle: (w) => w.length % 2 === 0 && w === [...w].reverse().join('')
  },
  {
    id: 'paren', name: 'Ngoặc cân bằng ( )', input: '(()())', start: 'q0', accept: ['q2'],
    desc: 'Gặp “(” thì đẩy, gặp “)” thì lấy ra; kết thúc khi chỉ còn $.',
    trans: [['q0', '', '', 'q1', '$'], ['q1', '(', '', 'q1', '('], ['q1', ')', '(', 'q1', ''], ['q1', '', '$', 'q2', '']],
    oracle: (w) => { let d = 0; for (const c of w) { d += c === '(' ? 1 : c === ')' ? -1 : 99; if (d < 0) return false; } return d === 0; }
  }
];

export function runPDA(pda, input, cap = 20000) {
  const w = input;
  const startCfg = { state: pda.start, pos: 0, stack: '' };
  const key = (c) => `${c.state}|${c.pos}|${c.stack}`;
  const parent = new Map([[key(startCfg), { prev: null, t: null }]]);
  const q = [startCfg];
  let best = startCfg, found = null, n = 0;
  while (q.length && n++ < cap) {
    const c = q.shift();
    if (pda.accept.includes(c.state) && c.pos === w.length) { found = c; break; }
    if (c.pos > best.pos) best = c;
    for (const t of pda.trans) {
      if (t[0] !== c.state) continue;
      if (t[1] !== '' && w[c.pos] !== t[1]) continue;
      if (t[2] !== '' && c.stack[0] !== t[2]) continue;
      const nxt = { state: t[3], pos: c.pos + (t[1] === '' ? 0 : 1), stack: t[4] + c.stack.slice(t[2] === '' ? 0 : 1) };
      if (nxt.stack.length > w.length + 3) continue;
      const k = key(nxt);
      if (parent.has(k)) continue;
      parent.set(k, { prev: c, t });
      q.push(nxt);
    }
  }
  const end = found || best;
  const path = [];
  for (let c = end, e = parent.get(key(end)); c; e = c && parent.get(key(c))) { path.unshift({ ...c, t: e?.t ?? null }); c = e?.prev ?? null; if (!c) break; }
  return { accepted: !!found, path };
}

export const tText = (t) => `δ(${t[0]}, ${t[1] || 'ε'}, ${t[2] || 'ε'}) = (${t[3]}, ${t[4] || 'ε'})`;
