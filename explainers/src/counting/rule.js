// Cây đếm: quy tắc nhân (và — từng bước nối tiếp) và quy tắc cộng (hoặc — các trường hợp rời nhau).
const leaf = (label, n) => ({ t: 'leaf', label, n });
const prod = (label, kids) => ({ t: 'prod', label, kids });
const sum = (label, kids) => ({ t: 'sum', label, kids });

export const RULE_PRESETS = [
  { id: 'outfit', name: 'Chọn trang phục: áo, quần, giày (và)', tree: prod('Trang phục', [leaf('áo', 3), leaf('quần', 2), leaf('giày', 4)]) },
  { id: 'meal', name: 'Chọn 1 món: cơm hoặc phở hoặc bún (hoặc)', tree: sum('Món ăn', [leaf('cơm', 3), leaf('phở', 4), leaf('bún', 2)]) },
  { id: 'plate', name: 'Biển số: 2 loại, mỗi loại là một tích (hoặc + và)', tree: sum('Biển số', [prod('Loại A: 1 chữ + 2 số', [leaf('chữ (A–E)', 5), leaf('số', 10), leaf('số', 10)]), prod('Loại B: 3 số', [leaf('số', 10), leaf('số', 10), leaf('số', 10)])]) },
  { id: 'pw', name: 'Mật khẩu: 1 chữ hoa rồi 2 ký tự bất kỳ trong 2 nhóm', tree: prod('Mật khẩu', [leaf('chữ hoa', 4), sum('ký tự 2', [leaf('chữ thường', 3), leaf('chữ số', 5)]), sum('ký tự 3', [leaf('chữ thường', 3), leaf('chữ số', 5)])]) }
];

export function evalTree(node) {
  if (node.t === 'leaf') return node.n;
  const vs = node.kids.map(evalTree);
  return node.t === 'prod' ? vs.reduce((a, b) => a * b, 1) : vs.reduce((a, b) => a + b, 0);
}
/** Liệt kê mọi kết quả (chuỗi nhãn) — dùng làm oracle và để minh họa. */
export function enumerate(node) {
  if (node.t === 'leaf') return Array.from({ length: node.n }, (_, i) => `${node.label}${i + 1}`);
  const parts = node.kids.map(enumerate);
  if (node.t === 'sum') return parts.flat();
  return parts.reduce((acc, p) => acc.flatMap((a) => p.map((b) => (a ? a + '·' + b : b))), ['']);
}
/** Thứ tự duyệt hậu tự (con trước cha) kèm giá trị. */
export function postOrder(node, path = '0', out = []) {
  if (node.t !== 'leaf') node.kids.forEach((k, i) => postOrder(k, path + '.' + i, out));
  out.push({ path, node, value: evalTree(node) });
  return out;
}

/** Bao hàm–loại trừ cho "chia hết cho a hoặc b" trong 1..n. */
export function overlapDemo(n, a, b) {
  const A = Math.floor(n / a), B = Math.floor(n / b);
  const lcm = (a * b) / gcd(a, b), AB = Math.floor(n / lcm);
  let brute = 0;
  for (let i = 1; i <= n; i++) if (i % a === 0 || i % b === 0) brute++;
  return { A, B, AB, naive: A + B, union: A + B - AB, brute, lcm };
}
const gcd = (x, y) => (y ? gcd(y, x % y) : x);
