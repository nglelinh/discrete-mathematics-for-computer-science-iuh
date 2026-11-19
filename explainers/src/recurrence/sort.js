// Sắp xếp (bubble, insertion, selection) và tìm kiếm (tuần tự, nhị phân) từng bước, có đếm so sánh / hoán đổi.
export const SORTS = { bubble: 'Bubble sort', insertion: 'Insertion sort', selection: 'Selection sort' };

export function sortSteps(kind, input) {
  const a = [...input], n = a.length;
  let comps = 0, swaps = 0;
  const steps = [{ arr: [...a], hi: [], op: 'start', msg: 'Mảng ban đầu.', comps, swaps, sorted: 0 }];
  const cmp = (i, j, msg) => { comps++; steps.push({ arr: [...a], hi: [i, j], op: 'compare', msg: `So sánh a[${i}]=${a[i]} với a[${j}]=${a[j]}. ${msg}`, comps, swaps }); };
  const swap = (i, j) => { [a[i], a[j]] = [a[j], a[i]]; swaps++; steps.push({ arr: [...a], hi: [i, j], op: 'swap', msg: `Hoán đổi a[${i}] ↔ a[${j}].`, comps, swaps }); };
  if (kind === 'bubble') {
    for (let i = 0; i < n - 1; i++) for (let j = 0; j < n - i - 1; j++) { cmp(j, j + 1, a[j] > a[j + 1] ? 'Sai thứ tự.' : 'Đúng thứ tự.'); if (a[j] > a[j + 1]) swap(j, j + 1); }
  } else if (kind === 'insertion') {
    for (let i = 1; i < n; i++) for (let j = i; j > 0; j--) { const bad = a[j - 1] > a[j]; cmp(j - 1, j, bad ? 'Lớn hơn ⇒ lùi phần tử về trước.' : 'Đã đúng chỗ.'); if (!bad) break; swap(j - 1, j); }
  } else {
    for (let i = 0; i < n - 1; i++) {
      let m = i;
      for (let j = i + 1; j < n; j++) { cmp(j, m, a[j] < a[m] ? `Nhỏ nhất mới.` : 'Giữ nguyên.'); if (a[j] < a[m]) m = j; }
      if (m !== i) swap(i, m);
    }
  }
  steps.push({ arr: [...a], hi: [], op: 'done', msg: `Xong: ${comps} lần so sánh, ${swaps} lần hoán đổi.`, comps, swaps });
  return { steps, result: a, comps, swaps };
}

export function searchSteps(kind, arr, target) {
  const steps = [];
  const n = arr.length;
  if (kind === 'linear') {
    for (let i = 0; i < n; i++) {
      const hit = arr[i] === target;
      steps.push({ lo: 0, hi: n - 1, mid: i, comps: i + 1, msg: `So sánh a[${i}]=${arr[i]} với ${target}: ${hit ? 'bằng ⇒ tìm thấy.' : 'khác.'}`, found: hit ? i : null });
      if (hit) return { steps, index: i, comps: i + 1 };
    }
    steps.push({ lo: 0, hi: n - 1, mid: -1, comps: n, msg: `Duyệt hết, không có ${target}.`, found: -1 });
    return { steps, index: -1, comps: n };
  }
  let lo = 0, hi = n - 1, comps = 0;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1; comps++;
    const v = arr[mid];
    const msg = v === target ? `a[${mid}]=${v} = ${target} ⇒ tìm thấy.` : v < target ? `a[${mid}]=${v} < ${target} ⇒ bỏ nửa trái, lo = ${mid + 1}.` : `a[${mid}]=${v} > ${target} ⇒ bỏ nửa phải, hi = ${mid - 1}.`;
    steps.push({ lo, hi, mid, comps, msg, found: v === target ? mid : null });
    if (v === target) return { steps, index: mid, comps };
    if (v < target) lo = mid + 1; else hi = mid - 1;
  }
  steps.push({ lo, hi, mid: -1, comps, msg: `lo > hi ⇒ không có ${target}.`, found: -1 });
  return { steps, index: -1, comps };
}
