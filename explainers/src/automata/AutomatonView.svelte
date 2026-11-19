<script>
  let {
    machine,
    active = [],
    hot = [],
    highlight = [],
    editMode = 'move',
    pending = null,
    width = 560,
    height = 300,
    label = 'Otomat',
    onNode = () => {},
    onCanvas = () => {},
    onEdge = () => {},
    onMove = () => {}
  } = $props();

  let svg = $state(null);
  let drag = $state(null);
  const pos = $derived(Object.fromEntries(machine.states.map((s) => [s.id, s])));
  const hasRev = (e) => e.from !== e.to && machine.edges.some((o) => o.from === e.to && o.to === e.from);

  function geom(e) {
    const a = pos[e.from], b = pos[e.to];
    if (!a || !b) return null;
    if (e.from === e.to) {
      return { d: `M ${a.x - 10} ${a.y - 17} C ${a.x - 34} ${a.y - 62}, ${a.x + 34} ${a.y - 62}, ${a.x + 10} ${a.y - 17}`, lx: a.x, ly: a.y - 60 };
    }
    const dx = b.x - a.x, dy = b.y - a.y, len = Math.hypot(dx, dy) || 1;
    const ux = dx / len, uy = dy / len;
    const off = hasRev(e) ? 24 : 0;
    const sx = a.x + ux * 20, sy = a.y + uy * 20, ex = b.x - ux * 22, ey = b.y - uy * 22;
    const mx = (sx + ex) / 2 - uy * off * 2, my = (sy + ey) / 2 + ux * off * 2;
    return { d: `M ${sx} ${sy} Q ${mx} ${my} ${ex} ${ey}`, lx: (sx + 2 * mx + ex) / 4 - uy * 0, ly: (sy + 2 * my + ey) / 4 - (off ? 0 : 8) };
  }
  const edges = $derived(machine.edges.map((e) => ({ ...e, g: geom(e), key: e.from + '>' + e.to })));

  function toSvg(ev) {
    const pt = svg.createSVGPoint();
    pt.x = ev.clientX; pt.y = ev.clientY;
    const p = pt.matrixTransform(svg.getScreenCTM().inverse());
    return { x: p.x, y: p.y };
  }
  function down(ev, s) {
    ev.stopPropagation();
    drag = { id: s.id, x0: ev.clientX, y0: ev.clientY, moved: false };
    svg.setPointerCapture?.(ev.pointerId);
  }
  function movePtr(ev) {
    if (!drag) return;
    if (Math.hypot(ev.clientX - drag.x0, ev.clientY - drag.y0) > 4) drag.moved = true;
    if (drag.moved && editMode === 'move') {
      const p = toSvg(ev);
      onMove(drag.id, Math.max(24, Math.min(width - 24, p.x)), Math.max(30, Math.min(height - 20, p.y)));
    }
  }
  function up() {
    if (drag && !drag.moved) onNode(drag.id);
    drag = null;
  }
  function canvasClick(ev) {
    if (ev.target !== svg && !ev.target.classList?.contains('bg')) return;
    const p = toSvg(ev);
    onCanvas(p.x, p.y);
  }
</script>

<svg bind:this={svg} viewBox="0 0 {width} {height}" class="dx-svg av" role="img" aria-label={label}
  onpointermove={movePtr} onpointerup={up} onclick={canvasClick}>
  <defs>
    <marker id="aarr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#334155" /></marker>
    <marker id="aarr-h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#f59e0b" /></marker>
  </defs>
  <rect class="bg" x="0" y="0" {width} {height} fill="transparent" />
  {#each edges as e (e.key)}
    {#if e.g}
      {@const isHot = hot.includes(e.key)}
      <path d={e.g.d} fill="none" stroke={isHot ? '#f59e0b' : '#334155'} stroke-width={isHot ? 3.2 : 1.8} marker-end={isHot ? 'url(#aarr-h)' : 'url(#aarr)'} />
      <g role="button" tabindex="0" class="lab" onclick={(ev) => { ev.stopPropagation(); onEdge(e); }} onkeydown={(ev) => ev.key === 'Enter' && onEdge(e)}>
        <rect x={e.g.lx - 4 - e.syms.join(',').length * 3.4} y={e.g.ly - 10} width={8 + e.syms.join(',').length * 6.8} height="16" rx="5" fill="#fff" stroke={isHot ? '#f59e0b' : '#cbd5e1'} />
        <text x={e.g.lx} y={e.g.ly + 2} text-anchor="middle" font-size="12" font-weight="650" fill="#0f172a">{e.syms.join(',')}</text>
      </g>
    {/if}
  {/each}
  {#each machine.states as s (s.id)}
    {@const on = active.includes(s.id)}
    {@const hl = highlight.includes(s.id)}
    {@const isAcc = machine.accept.includes(s.id)}
    {@const w = Math.max(20, s.id.length * 3.6 + 12)}
    <g transform={`translate(${s.x},${s.y})`} class="st" role="button" tabindex="0" onpointerdown={(ev) => down(ev, s)} onkeydown={(ev) => ev.key === 'Enter' && onNode(s.id)}>
      {#if machine.start === s.id}
        <line x1={-w - 28} y1="0" x2={-w - 2} y2="0" stroke="#334155" stroke-width="2" marker-end="url(#aarr)" />
      {/if}
      <ellipse rx={w} ry="19" fill={on ? '#fde68a' : hl ? '#bae6fd' : '#fff'} stroke={pending === s.id ? '#f59e0b' : on ? '#d97706' : '#334155'} stroke-width={on || pending === s.id ? 3.5 : 2} />
      {#if isAcc}<ellipse rx={w - 5} ry="14" fill="none" stroke={on ? '#d97706' : '#334155'} stroke-width="1.6" />{/if}
      <text y="4" text-anchor="middle" font-size={s.id.length > 7 ? 10 : 12} font-weight="700">{s.id}</text>
    </g>
  {/each}
</svg>

<style>
  .av { touch-action: none; user-select: none; }
  .st { cursor: grab; } .lab { cursor: pointer; }
  .st:focus, .lab:focus { outline: none; }
</style>
