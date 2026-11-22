<script>
  import AutomatonView from './AutomatonView.svelte';
  import { PRESETS, simulate, subsetConstruction, minimizeDFA, alphabetOf, isDFA, isComplete, normSym, EPS } from './automata.js';

  let { preset = 'dfa01', tab: tabProp = 'simulate', input: inputProp = '' } = $props();
  const first = PRESETS.find((p) => p.id === preset) || PRESETS[0];

  let presetId = $state(first.id);
  let machine = $state(first.make());
  let input = $state(inputProp || first.example);
  let idx = $state(0);
  let playing = $state(false);
  let tab = $state(['simulate', 'subset', 'minimize'].includes(tabProp) ? tabProp : 'simulate');
  let editMode = $state('move');
  let pendingFrom = $state(null);
  let pendingEdge = $state(null);
  let symText = $state('0');
  let sIdx = $state(0);
  let hoverKey = $state(null);

  const A = $derived(alphabetOf(machine));
  const sim = $derived(simulate(machine, input));
  const cur = $derived(sim.trace[Math.min(idx, sim.trace.length - 1)]);
  const kind = $derived(isDFA(machine) ? (isComplete(machine) ? 'DFA đầy đủ' : 'DFA chưa đầy đủ') : machine.edges.some((e) => e.syms.includes(EPS)) ? 'ε-NFA' : 'NFA');
  const sub = $derived(subsetConstruction(machine));
  const stepNow = $derived(sIdx > 0 ? sub.steps[Math.min(sIdx, sub.steps.length) - 1] : null);
  const shownRows = $derived(sIdx === 0 ? 1 : sub.steps[Math.min(sIdx, sub.steps.length) - 1].rowsAfter);
  const partial = $derived.by(() => {
    const full = sub.dfa;
    const keep = new Set(full.states.slice(0, shownRows).map((s) => s.id));
    const done = new Set(sub.steps.slice(0, sIdx).map((s) => s.key));
    return {
      ...full,
      states: full.states.filter((s) => keep.has(s.id)),
      edges: full.edges.filter((e) => done.has(e.from) && keep.has(e.to))
    };
  });
  const dfaW = $derived(Math.max(560, Math.max(...sub.dfa.states.map((s) => s.x)) + 90));
  const minim = $derived(isDFA(machine) && isComplete(machine) ? minimizeDFA(machine) : minimizeDFA(sub.dfa));
  const minSource = $derived(isDFA(machine) && isComplete(machine) ? 'máy hiện tại' : 'DFA sinh từ NFA');
  const minW = $derived(Math.max(560, Math.max(...minim.machine.states.map((s) => s.x)) + 90));
  const subActive = $derived(stepNow ? sub.rows.find((r) => r.key === stepNow.key)?.set || [] : sub.rows[0].set);
  const hoverSet = $derived(hoverKey ? sub.rows.find((r) => r.key === hoverKey)?.set || [] : []);
  const hotEdges = $derived.by(() => {
    if (!cur || !cur.from) return [];
    const out = [];
    machine.edges.forEach((e) => { if (cur.from.includes(e.from) && e.syms.includes(cur.sym)) out.push(e.from + '>' + e.to); });
    return out;
  });
  const badChars = $derived([...new Set([...input].filter((c) => A.length && !A.includes(c)))]);

  $effect(() => {
    if (!playing) return;
    const t = setTimeout(() => {
      if (idx >= sim.trace.length - 1) playing = false;
      else idx += 1;
    }, 700);
    return () => clearTimeout(t);
  });
  $effect(() => { input; machine.edges.length; machine.states.length; idx = 0; playing = false; });

  function loadPreset(id) {
    const p = PRESETS.find((x) => x.id === id);
    if (!p) return;
    presetId = id; machine = p.make(); input = p.example; idx = 0; sIdx = 0; pendingFrom = null; pendingEdge = null;
    symText = p.alpha[0];
  }
  function onNode(id) {
    if (editMode === 'accept') {
      machine.accept = machine.accept.includes(id) ? machine.accept.filter((x) => x !== id) : [...machine.accept, id];
    } else if (editMode === 'start') machine.start = id;
    else if (editMode === 'delete') {
      if (machine.states.length <= 1) return;
      machine.states = machine.states.filter((s) => s.id !== id);
      machine.edges = machine.edges.filter((e) => e.from !== id && e.to !== id);
      machine.accept = machine.accept.filter((x) => x !== id);
      if (machine.start === id) machine.start = machine.states[0].id;
    } else if (editMode === 'edge') {
      if (pendingFrom === null) pendingFrom = id;
      else { pendingEdge = { from: pendingFrom, to: id }; pendingFrom = null; }
    }
  }
  function onCanvas(x, y) {
    if (editMode !== 'state') return;
    let i = machine.states.length;
    while (machine.states.some((s) => s.id === 'q' + i)) i++;
    machine.states = [...machine.states, { id: 'q' + i, x, y }];
  }
  function onEdge(e) {
    if (editMode === 'delete') machine.edges = machine.edges.filter((x) => !(x.from === e.from && x.to === e.to));
  }
  function onMove(id, x, y) {
    const s = machine.states.find((q) => q.id === id);
    if (s) { s.x = x; s.y = y; }
  }
  function addEdge() {
    if (!pendingEdge) return;
    const syms = [...new Set(symText.split(/[,\s]+/).filter(Boolean).map(normSym))];
    if (!syms.length) return;
    const ex = machine.edges.find((e) => e.from === pendingEdge.from && e.to === pendingEdge.to);
    if (ex) ex.syms = [...new Set([...ex.syms, ...syms])];
    else machine.edges = [...machine.edges, { from: pendingEdge.from, to: pendingEdge.to, syms }];
    pendingEdge = null;
  }
  const setStr = (s) => (s.length ? '{' + s.join(', ') + '}' : '∅');
  const modes = { move: 'Kéo', state: 'Thêm trạng thái', edge: 'Thêm chuyển', start: 'Đặt đầu', accept: 'Đổi chấp nhận', delete: 'Xóa' };
</script>

<div class="dx aex">
  <h4>Minh hoạ otomat hữu hạn</h4>
  <p class="dx-help">
    Máy hiện tại là <b>{kind}</b> trên bảng chữ {'{'}{A.join(', ')}{'}'}. Chạy từng ký tự, xem <em>tập</em> trạng thái đang "sống",
    chuyển NFA sang DFA bằng <b>xây dựng tập con</b> và tối thiểu hóa DFA. Có thể sửa máy: kéo, thêm trạng thái / chuyển, đổi trạng thái chấp nhận.
  </p>

  <div class="dx-tabs">
    <button type="button" class="sec" class:on={tab === 'simulate'} onclick={() => (tab = 'simulate')}>Mô phỏng</button>
    <button type="button" class="sec" class:on={tab === 'subset'} onclick={() => (tab = 'subset')}>NFA → DFA (tập con)</button>
    <button type="button" class="sec" class:on={tab === 'minimize'} onclick={() => (tab = 'minimize')}>Tối thiểu hóa</button>
    <label>Máy mẫu
      <select value={presetId} onchange={(e) => loadPreset(e.currentTarget.value)}>
        {#each PRESETS as p}<option value={p.id}>{p.label}</option>{/each}
      </select>
    </label>
  </div>

  <div class="grid">
    <div>
      <div class="dx-bar">
        {#each Object.entries(modes) as [id, label]}
          <button type="button" class="sec" class:on={editMode === id} onclick={() => { editMode = id; pendingFrom = null; }}>{label}</button>
        {/each}
      </div>
      {#if pendingEdge}
        <div class="dx-bar pe">
          <span>Chuyển {pendingEdge.from} → {pendingEdge.to} với ký hiệu:</span>
          <input type="text" bind:value={symText} style="width:6rem" placeholder="0,1 hoặc e" />
          <button type="button" onclick={addEdge}>Thêm</button>
          <button type="button" class="sec" onclick={() => (pendingEdge = null)}>Hủy</button>
        </div>
      {:else if pendingFrom}
        <p class="dx-k">Đã chọn {pendingFrom} — bấm trạng thái đích.</p>
      {/if}
      <AutomatonView {machine} active={tab === 'simulate' ? cur.set : tab === 'subset' ? subActive : []} highlight={hoverSet} hot={tab === 'simulate' ? hotEdges : []}
        {editMode} pending={pendingFrom} label="Máy trạng thái hữu hạn" {onNode} {onCanvas} {onEdge} {onMove} />
      <p class="dx-k">Viền đôi = chấp nhận · mũi tên vào = trạng thái đầu · nhãn ε = chuyển rỗng (gõ <code>e</code>) · chế độ <b>Xóa</b> cũng xóa được cạnh bằng cách bấm nhãn.</p>
    </div>

    <div>
      {#if tab === 'simulate'}
        <div class="dx-card">
          <header><h5>Chuỗi vào</h5><span>{sim.accept ? '' : ''}</span></header>
          <div class="dx-bar">
            <input type="text" bind:value={input} spellcheck="false" style="flex:1;min-width:8rem" />
            <button type="button" class="sec" disabled={idx <= 0} onclick={() => { playing = false; idx = Math.max(0, idx - 1); }}>◀</button>
            <button type="button" onclick={() => { if (idx >= sim.trace.length - 1) idx = 0; playing = !playing; }}>{playing ? 'Dừng' : 'Chạy'}</button>
            <button type="button" class="sec" disabled={idx >= sim.trace.length - 1} onclick={() => { playing = false; idx = Math.min(sim.trace.length - 1, idx + 1); }}>▶</button>
          </div>
          {#if badChars.length}<p class="dx-bad">Ký tự {badChars.join(', ')} không có trong bảng chữ — máy sẽ kẹt (∅).</p>{/if}
          <div class="tape">
            {#each [...input] as c, i}<span class:done={i < idx} class:now={i === idx}>{c}</span>{/each}
            {#if !input}<em class="dx-k">(chuỗi rỗng ε)</em>{/if}
          </div>
          <p class="dx-msg">
            {#if idx === 0}Bắt đầu: tập trạng thái = ε-closure({'{'}{machine.start}{'}'}) = <b>{setStr(cur.set)}</b>.
            {:else}Đọc <b>{cur.sym}</b>: từ {setStr(cur.from)} đi được tới {setStr(cur.moved)}{#if machine.edges.some((e) => e.syms.includes(EPS))}, sau ε-closure: <b>{setStr(cur.set)}</b>{/if}.{/if}
            {#if idx === sim.trace.length - 1}
              <br />Hết chuỗi: {cur.set.some((s) => machine.accept.includes(s)) ? '✓ có trạng thái chấp nhận → CHẤP NHẬN' : '✗ không có trạng thái chấp nhận → TỪ CHỐI'}.
            {/if}
          </p>
          <table class="dx-t"><thead><tr><th>Sau</th><th>Tập trạng thái</th></tr></thead>
            <tbody>{#each sim.trace.slice(0, idx + 1) as t}<tr><td>{t.pos === 0 ? 'ε' : input.slice(0, t.pos)}</td><td>{setStr(t.set)}</td></tr>{/each}</tbody>
          </table>
        </div>
      {/if}

      {#if tab === 'subset'}
        <div class="dx-card">
          <header><h5>Bảng xây dựng tập con</h5><span>{sub.rows.length} trạng thái DFA{sub.rows.length > machine.states.length ? ` (từ ${machine.states.length} của NFA)` : ''}</span></header>
          <div class="dx-bar">
            <button type="button" class="sec" disabled={sIdx <= 0} onclick={() => (sIdx = Math.max(0, sIdx - 1))}>◀</button>
            <span>Bước {sIdx} / {sub.steps.length}</span>
            <button type="button" class="sec" disabled={sIdx >= sub.steps.length} onclick={() => (sIdx = Math.min(sub.steps.length, sIdx + 1))}>▶</button>
            <button type="button" class="sec" onclick={() => (sIdx = sub.steps.length)}>Xong</button>
          </div>
          <p class="dx-msg">
            {#if !stepNow}Trạng thái đầu của DFA = ε-closure({'{'}{machine.start}{'}'}) = <b>{setStr(sub.rows[0].set)}</b>. Bấm ▶ để xử lý từng tập.
            {:else}Xử lý {setStr(sub.rows.find((r) => r.key === stepNow.key).set)}:
              {#each A as a}<br />· đọc <b>{a}</b>: move = {setStr(stepNow.results[a].moved)}{#if stepNow.results[a].closure.length !== stepNow.results[a].moved.length}, ε-closure = {setStr(stepNow.results[a].closure)}{/if} → <b>{stepNow.results[a].key}</b>{/each}
              {#if stepNow.fresh.length}<br />Tập mới phát hiện: <b>{stepNow.fresh.join(' ; ')}</b>.{/if}
            {/if}
          </p>
          <table class="dx-t">
            <thead><tr><th>Tập (trạng thái DFA)</th>{#each sub.alphabet as a}<th>{a}</th>{/each}<th>CN?</th></tr></thead>
            <tbody>
              {#each sub.rows.slice(0, shownRows) as r, i}
                {@const done = sub.steps.slice(0, sIdx).some((s) => s.key === r.key)}
                <tr class:cur={stepNow && stepNow.key === r.key} onmouseenter={() => (hoverKey = r.key)} onmouseleave={() => (hoverKey = null)}>
                  <td>{i === 0 ? '→ ' : ''}{r.key}</td>
                  {#each sub.alphabet as a}<td>{done ? r.trans[a] : '…'}</td>{/each}
                  <td>{r.accept ? '✓' : ''}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      {/if}

      {#if tab === 'minimize'}
        <div class="dx-card">
          <header><h5>Tối thiểu hóa DFA</h5><span>nguồn: {minSource}</span></header>
          <p class="dx-msg">
            {minim.groups.length < (isDFA(machine) && isComplete(machine) ? machine.states.length : sub.dfa.states.length)
              ? `Gộp được: ${isDFA(machine) && isComplete(machine) ? machine.states.length : sub.dfa.states.length} → ${minim.groups.length} trạng thái.`
              : `Đã tối thiểu: ${minim.groups.length} trạng thái (không gộp được).`}
            Các nhóm tương đương (cùng hành vi trên mọi chuỗi): {minim.groups.map((g) => '{' + g.join(', ') + '}').join(' · ')}. Số vòng tinh chỉnh: {minim.rounds}.
          </p>
        </div>
      {/if}
    </div>
  </div>

  {#if tab === 'subset'}
    <div class="dx-card ext">
      <header><h5>DFA đang được xây</h5><span>rê chuột lên một hàng của bảng để thấy các trạng thái NFA tương ứng (xanh nhạt)</span></header>
      <AutomatonView machine={partial} active={subActive.length ? [stepNow ? stepNow.key : sub.rows[0].key] : []} width={dfaW} height={340} label="DFA từ xây dựng tập con" />
    </div>
  {/if}
  {#if tab === 'minimize'}
    <div class="dx-card ext">
      <header><h5>DFA tối thiểu</h5><span>mỗi trạng thái là một nhóm tương đương</span></header>
      <AutomatonView machine={minim.machine} width={minW} height={340} label="DFA tối thiểu" />
    </div>
  {/if}

  <details class="ex">
    <summary>Thực hành có hướng dẫn</summary>
    <ol>
      <li><b>Mô phỏng:</b> chọn <em>DFA kết thúc bằng 01</em>, nhập <code>1101</code> và chạy từng ký tự; dự đoán trạng thái tiếp theo trước khi bấm ▶.</li>
      <li>Chọn <em>NFA chứa 101</em>: tập trạng thái có thể có nhiều phần tử — vì sao NFA "đoán" được chỗ bắt đầu 101?</li>
      <li><b>Tập con:</b> chọn <em>ký tự thứ 3 từ cuối là 1</em> (NFA 4 trạng thái) và bấm ▶ đến hết: DFA có 8 trạng thái — ví dụ cho sự bùng nổ 2ⁿ.</li>
      <li><b>ε-NFA:</b> chọn <em>a*b*</em> và để ý ε-closure ở bước đầu.</li>
      <li><b>Tối thiểu hóa:</b> sau khi chuyển <em>NFA chứa 101</em> sang DFA, xem các nhóm trạng thái được gộp.</li>
      <li>Tự vẽ: thêm trạng thái, thêm chuyển, đặt trạng thái chấp nhận để nhận chuỗi có độ dài chia hết cho 3.</li>
    </ol>
  </details>
</div>

<style>
  .grid { display: grid; grid-template-columns: minmax(300px, 1.25fr) minmax(260px, 1fr); gap: 12px; align-items: start; }
  @media (max-width: 800px) { .grid { grid-template-columns: 1fr; } }
  .ext { margin-top: 12px; }
  .pe { background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 6px 8px; }
  .tape { display: flex; gap: 4px; flex-wrap: wrap; margin: 6px 0; font-family: ui-monospace, Menlo, monospace; }
  .tape span { min-width: 1.8rem; text-align: center; padding: 4px 6px; border: 1px solid #cbd5e1; border-radius: 6px; background: #fff; }
  .tape span.done { background: #ccfbf1; border-color: #0f766e; } .tape span.now { background: #fde68a; border-color: #d97706; }
  tr.cur { background: #fef9c3; }
  p { margin: 6px 0; font-size: 0.9rem; }
  .ex { margin-top: 10px; font-size: 0.9rem; color: #334155; } .ex summary { cursor: pointer; font-weight: 650; color: #004586; }
</style>
