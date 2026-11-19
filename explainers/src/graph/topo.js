// Sắp xếp topo: Kahn (bậc vào + hàng đợi) và DFS (thứ tự hậu tự đảo). Hàm thuần, có test.

export const TOPO_PRESETS = [
  {
    id: 'courses', name: 'Lịch môn học',
    nodes: [
      { id: 'LT', label: 'Lập trình', x: 90, y: 60 }, { id: 'TRR', label: 'Toán rời rạc', x: 90, y: 200 },
      { id: 'CTDL', label: 'CTDL', x: 260, y: 60 }, { id: 'GT', label: 'Giải thuật', x: 260, y: 200 },
      { id: 'CSDL', label: 'CSDL', x: 430, y: 60 }, { id: 'DA', label: 'Đồ án', x: 430, y: 200 }
    ],
    edges: [['LT', 'CTDL'], ['TRR', 'GT'], ['CTDL', 'GT'], ['CTDL', 'CSDL'], ['GT', 'DA'], ['CSDL', 'DA']],
    cycleEdge: ['GT', 'CTDL']
  },
  {
    id: 'diamond', name: 'Ví dụ A,B,C,D trong bài',
    nodes: [
      { id: 'A', label: 'A', x: 260, y: 40 }, { id: 'B', label: 'B', x: 140, y: 130 },
      { id: 'C', label: 'C', x: 380, y: 130 }, { id: 'D', label: 'D', x: 260, y: 220 }
    ],
    edges: [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']],
    cycleEdge: ['D', 'A']
  },
  {
    id: 'build', name: 'Build: phụ thuộc gói',
    nodes: [
      { id: 'cfg', label: 'config', x: 70, y: 130 }, { id: 'lib', label: 'lib', x: 200, y: 50 },
      { id: 'util', label: 'utils', x: 200, y: 210 }, { id: 'core', label: 'core', x: 340, y: 130 },
      { id: 'app', label: 'app', x: 480, y: 60 }, { id: 'test', label: 'test', x: 480, y: 200 }
    ],
    edges: [['cfg', 'lib'], ['cfg', 'util'], ['lib', 'core'], ['util', 'core'], ['core', 'app'], ['core', 'test']],
    cycleEdge: ['app', 'lib']
  }
];

export function withCycle(p, on) {
  return { nodes: p.nodes, edges: on ? [...p.edges, p.cycleEdge] : p.edges };
}

const ids = (g) => g.nodes.map((n) => n.id);
const outs = (g, u) => g.edges.filter((e) => e[0] === u).map((e) => e[1]);
const name = (g, id) => g.nodes.find((n) => n.id === id)?.label ?? id;

export function indegrees(g) {
  const d = Object.fromEntries(ids(g).map((i) => [i, 0]));
  for (const [, v] of g.edges) d[v]++;
  return d;
}

/** Kahn: trả về danh sách bước { indeg, queue, order, cur, removed:[u>v], msg, done, cycle }. */
export function kahnSteps(g) {
  const indeg = indegrees(g);
  const snap = (extra) => ({ indeg: { ...indeg }, queue: [...queue], order: [...order], cur: null, removed: [...removed], done: false, cycle: false, ...extra });
  const queue = [];
  const order = [];
  const removed = [];
  const steps = [];
  steps.push(snap({ msg: 'Tính bậc vào (số cạnh đi vào) của mọi đỉnh.' }));
  for (const i of ids(g)) if (indeg[i] === 0) queue.push(i);
  steps.push(snap({ msg: queue.length ? `Đưa các đỉnh bậc vào 0 vào hàng đợi: ${queue.map((q) => name(g, q)).join(', ')}.` : 'Không có đỉnh nào bậc vào 0 ⇒ chắc chắn có chu trình.' }));
  while (queue.length) {
    const u = queue.shift();
    order.push(u);
    const notes = [];
    for (const v of outs(g, u)) {
      removed.push(u + '>' + v);
      indeg[v]--;
      notes.push(`${name(g, v)}: ${indeg[v] + 1}→${indeg[v]}${indeg[v] === 0 ? ' (vào hàng đợi)' : ''}`);
      if (indeg[v] === 0) queue.push(v);
    }
    steps.push(snap({ cur: u, msg: `Lấy ${name(g, u)} ra, ghi vào kết quả.` + (notes.length ? ' Xóa các cạnh đi ra, giảm bậc vào: ' + notes.join('; ') + '.' : ' Không có cạnh đi ra.') }));
  }
  const n = g.nodes.length;
  const cycle = order.length < n;
  steps.push(snap({
    done: true, cycle,
    msg: cycle
      ? `Chỉ xuất được ${order.length}/${n} đỉnh ⇒ CÓ CHU TRÌNH. Các đỉnh còn lại luôn có bậc vào > 0.`
      : `Xuất đủ ${n}/${n} đỉnh ⇒ đồ thị là DAG. Thứ tự topo: ${order.map((o) => name(g, o)).join(' → ')}.`
  }));
  return steps;
}

/** DFS: màu trắng(0)/xám(1)/đen(2); thứ tự topo = hậu tự đảo; cạnh tới đỉnh xám ⇒ chu trình. */
export function dfsSteps(g) {
  const color = Object.fromEntries(ids(g).map((i) => [i, 0]));
  const post = [];
  const stack = [];
  const steps = [];
  let found = null;
  const snap = (extra) => ({ color: { ...color }, post: [...post], stack: [...stack], cur: null, edge: null, done: false, cycle: !!found, ...extra });
  steps.push(snap({ msg: 'Mọi đỉnh trắng (chưa thăm). Duyệt DFS lần lượt từng đỉnh chưa thăm.' }));
  function visit(u) {
    color[u] = 1; stack.push(u);
    steps.push(snap({ cur: u, msg: `Thăm ${name(g, u)}: tô xám (đang nằm trên ngăn xếp đệ quy).` }));
    for (const v of outs(g, u)) {
      if (found) return;
      if (color[v] === 0) {
        steps.push(snap({ cur: u, edge: [u, v], msg: `Cạnh ${name(g, u)}→${name(g, v)}: ${name(g, v)} còn trắng, đi sâu vào.` }));
        visit(v);
        if (found) return;
      } else if (color[v] === 1) {
        found = [u, v];
        steps.push(snap({ cur: u, edge: [u, v], cycle: true, msg: `Cạnh ${name(g, u)}→${name(g, v)} trỏ tới đỉnh XÁM ${name(g, v)} (cạnh ngược) ⇒ có chu trình, dừng.` }));
        return;
      } else {
        steps.push(snap({ cur: u, edge: [u, v], msg: `Cạnh ${name(g, u)}→${name(g, v)}: ${name(g, v)} đã đen (xong), bỏ qua.` }));
      }
    }
    color[u] = 2; stack.pop(); post.push(u);
    steps.push(snap({ cur: u, msg: `Xong ${name(g, u)}: tô đen và ghi vào danh sách hậu tự (vị trí ${post.length}).` }));
  }
  for (const i of ids(g)) {
    if (found) break;
    if (color[i] === 0) visit(i);
  }
  const order = [...post].reverse();
  steps.push(snap({
    done: true, cycle: !!found,
    msg: found ? 'Có chu trình nên không tồn tại thứ tự topo.' : `Đảo danh sách hậu tự ⇒ thứ tự topo: ${order.map((o) => name(g, o)).join(' → ')}.`
  }));
  return steps;
}

export function finalOrder(steps) {
  const last = steps[steps.length - 1];
  if (last.cycle) return null;
  return last.post ? [...last.post].reverse() : last.order;
}

export function isTopoOrder(g, order) {
  if (!order || order.length !== g.nodes.length || new Set(order).size !== g.nodes.length) return false;
  const pos = Object.fromEntries(order.map((v, i) => [v, i]));
  return g.edges.every(([u, v]) => pos[u] < pos[v]);
}

/** Kiểm tra DAG bằng cách thử mọi đỉnh có tới được chính nó (dùng làm chuẩn đối chiếu trong test). */
export function hasCycleBrute(g) {
  for (const s of ids(g)) {
    const seen = new Set(); const st = [...outs(g, s)];
    while (st.length) {
      const x = st.pop();
      if (x === s) return true;
      if (seen.has(x)) continue;
      seen.add(x); st.push(...outs(g, x));
    }
  }
  return false;
}
