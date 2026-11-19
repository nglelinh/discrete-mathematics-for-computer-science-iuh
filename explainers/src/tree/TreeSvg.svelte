<script>
  let { layout, hot = [], done = [], label = (n) => n.key, edgeLabels = false, newId = null, ariaLabel = 'Cây', r = 18 } = $props();
  const pad = 30;
  const W = $derived(layout.width + pad * 2);
  const H = $derived(layout.height + pad * 2 + 6);
</script>

<svg viewBox="0 0 {Math.max(W, 200)} {Math.max(H, 90)}" class="dx-svg" role="img" aria-label={ariaLabel} style="max-height:360px">
  <g transform={`translate(${pad},${pad})`}>
    {#each layout.links as l}
      <line x1={l.from.x} y1={l.from.y} x2={l.to.x} y2={l.to.y} stroke={hot.includes(l.to.n.id) && hot.includes(l.from.n.id) ? '#d97706' : '#64748b'} stroke-width={hot.includes(l.to.n.id) && hot.includes(l.from.n.id) ? 3 : 1.6} />
      {#if edgeLabels}
        <g>
          <circle cx={(l.from.x + l.to.x) / 2} cy={(l.from.y + l.to.y) / 2} r="8" fill="#fff" stroke="#cbd5e1" />
          <text x={(l.from.x + l.to.x) / 2} y={(l.from.y + l.to.y) / 2 + 4} text-anchor="middle" font-size="11" font-weight="700" fill="#0f766e">{l.bit}</text>
        </g>
      {/if}
    {/each}
    {#each layout.nodes as o (o.n.id)}
      <g transform={`translate(${o.x},${o.y})`}>
        <circle {r} fill={newId === o.n.id ? '#bbf7d0' : hot.includes(o.n.id) ? '#fde68a' : done.includes(o.n.id) ? '#ccfbf1' : '#fff'} stroke={hot.includes(o.n.id) ? '#d97706' : '#334155'} stroke-width={hot.includes(o.n.id) ? 3 : 1.8} />
        <text y="4" text-anchor="middle" font-size="12" font-weight="700">{label(o.n)}</text>
      </g>
    {/each}
  </g>
</svg>
