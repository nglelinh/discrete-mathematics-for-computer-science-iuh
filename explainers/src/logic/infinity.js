// Tập vô hạn: đường chéo Cantor, khách sạn Hilbert, ghép cặp ℕ×ℕ.

export const cantorPair = (i, j) => ((i + j) * (i + j + 1)) / 2 + j;
export function unpair(n) {
  let w = Math.floor((Math.sqrt(8 * n + 1) - 1) / 2);
  while ((w * (w + 1)) / 2 > n) w--;
  while (((w + 1) * (w + 2)) / 2 <= n) w++;
  const j = n - (w * (w + 1)) / 2;
  return [w - j, j];
}

export const diagonalFlip = (rows) => rows.map((r, i) => 1 - r[i]);
export const differsFromAll = (rows, d) => rows.every((r, i) => r[i] !== d[i]);
export function randomRows(n, seed = 1) {
  let s = seed >>> 0;
  const rnd = () => ((s = (s * 1664525 + 1013904223) >>> 0) / 2 ** 32);
  return Array.from({ length: n }, () => Array.from({ length: n }, () => (rnd() < 0.5 ? 0 : 1)));
}

/** Ba kịch bản khách sạn Hilbert. oldRoom(n): phòng mới của khách cũ thứ n (n ≥ 1); newRoom: phòng của khách mới. */
export const HILBERT = [
  { id: 'one', name: '1 khách mới', oldRoom: (n) => n + 1, newGuests: [{ label: 'b', room: 1 }],
    explain: 'Mỗi khách ở phòng n dời sang phòng n+1. Phòng 1 trống cho khách mới: ∞ + 1 = ∞.', newRoom: () => 1 },
  { id: 'bus', name: 'Vô hạn khách (1 xe buýt)', oldRoom: (n) => 2 * n, newRoom: (k) => 2 * k - 1,
    explain: 'Khách ở phòng n dời sang phòng 2n (các phòng chẵn). Khách thứ k trên xe buýt vào phòng lẻ 2k−1: ∞ + ∞ = ∞.' },
  { id: 'buses', name: 'Vô hạn xe buýt', oldRoom: (n) => cantorPair(0, n - 1) + 1, newRoom: (k, b) => cantorPair(b, k - 1) + 1,
    explain: 'Coi khách cũ là “xe số 0”. Ghế k của xe b vào phòng ⟨b, k−1⟩ + 1 theo cách đánh số đường chéo Cantor: ∞ · ∞ = ∞ (đếm được).' }
];

/** Ai ở phòng r sau khi sắp xếp lại (chỉ xét r ≤ R)? Trả về mảng R phần tử {who:'a3'|'b2'|'b1.4'}. */
export function hotelAfter(sc, R, span = 60) {
  const rooms = Array(R).fill(null);
  for (let n = 1; n <= span * 3; n++) { const r = sc.oldRoom(n); if (r <= R) rooms[r - 1] = rooms[r - 1] ? 'XUNG ĐỘT' : 'a' + n; }
  if (sc.id === 'one') { if (rooms[0]) rooms[0] = 'XUNG ĐỘT'; else rooms[0] = 'b1'; }
  else if (sc.id === 'bus') for (let k = 1; k <= span * 3; k++) { const r = sc.newRoom(k); if (r <= R) rooms[r - 1] = rooms[r - 1] ? 'XUNG ĐỘT' : 'b' + k; }
  else for (let b = 1; b <= span; b++) for (let k = 1; k <= span; k++) { const r = sc.newRoom(k, b); if (r <= R) rooms[r - 1] = rooms[r - 1] ? 'XUNG ĐỘT' : `b${b}.${k}`; }
  return rooms;
}
