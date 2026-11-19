<script>
  import { layoutNet, evalNet } from './circuit.js';

  let { net, env = null, onToggle = () => {} } = $props();

  const lay = $derived(layoutNet(net));
  const vals = $derived(env ? evalNet(net, env) : null);
  const W = 44;
  const H = 34;

  function pinY(node, k) {
    const m = node.ins.length;
    if (m <= 1) return lay.pos[node.id].y;
    const span = Math.min(H - 8, 12 * (m - 1));
    return lay.pos[node.id].y - span / 2 + (span * k) / (m - 1);
  }
  function wires() {
    const out = [];
    for (const n of net.nodes) {
      n.ins.forEach((src, k) => {
        const a = lay.pos[src];
        const b = lay.pos[n.id];
        const x1 = a.x + (net.nodes[src].kind === 'in' ? 10 : W / 2);
        const y1 = a.y;
        const x2 = b.x - (n.kind === 'out' ? 12 : W / 2);
        const y2 = pinY(n, k);
        const dx = Math.max(18, (x2 - x1) / 2);
        out.push({
          key: `${src}-${n.id}-${k}`,
          d: `M ${x1} ${y1} C ${x1 + dx} ${y1}, ${x2 - dx} ${y2}, ${x2} ${y2}`,
          v: vals ? vals[src] : null
        });
      });
    }
    return out;
  }
  const ws = $derived(wires());
  const sym = { AND: 'AND', OR: 'OR', XOR: 'XOR', NOT: 'NOT', IMP: '→', IFF: '↔' };
</script>

<svg class="circuit" viewBox="0 0 {lay.width} {lay.height}" role="img" aria-label="Sơ đồ mạch logic">
  {#each ws as w (w.key)}
    <path d={w.d} fill="none" stroke={w.v === null ? '#64748b' : w.v ? '#0f766e' : '#cbd5e1'} stroke-width={w.v ? 2.6 : 1.8} />
  {/each}
  {#each net.nodes as n (n.id)}
    {@const p = lay.pos[n.id]}
    {#if n.kind === 'in'}
      <g transform={`translate(${p.x},${p.y})`} class="inp" role="button" tabindex="0" onclick={() => onToggle(n.name)} onkeydown={(e) => (e.key === 'Enter' || e.key === ' ') && onToggle(n.name)}>
        <circle r="10" fill={vals ? (vals[n.id] ? '#0f766e' : '#fff') : '#fff'} stroke="#334155" stroke-width="1.6" />
        <text y="4" text-anchor="middle" font-size="12" font-weight="700" fill={vals && vals[n.id] ? '#fff' : '#0f172a'}>{n.name}</text>
        {#if vals}<text x="-16" y="4" text-anchor="end" font-size="11" fill="#64748b">{vals[n.id]}</text>{/if}
      </g>
    {:else if n.kind === 'const'}
      <g transform={`translate(${p.x},${p.y})`}>
        <rect x="-12" y="-10" width="24" height="20" rx="5" fill="#fff" stroke="#64748b" />
        <text y="4" text-anchor="middle" font-size="12" font-weight="700">{n.name}</text>
      </g>
    {:else if n.kind === 'out'}
      <g transform={`translate(${p.x},${p.y})`}>
        <circle r="12" fill={vals ? (vals[n.id] ? '#0f766e' : '#fff') : '#eff6ff'} stroke="#004586" stroke-width="2" />
        <text y="4" text-anchor="middle" font-size="12" font-weight="750" fill={vals && vals[n.id] ? '#fff' : '#004586'}>F</text>
        {#if vals}<text x="18" y="4" font-size="12" font-weight="700" fill="#004586">= {vals[n.id]}</text>{/if}
      </g>
    {:else}
      {@const on = vals ? vals[n.id] : null}
      {@const stroke = on === null ? '#004586' : on ? '#0f766e' : '#94a3b8'}
      {@const fill = on ? '#ccfbf1' : '#f8fafc'}
      <g transform={`translate(${p.x},${p.y})`}>
        {#if n.op === 'AND'}
          <path d="M -22 -17 H 0 A 17 17 0 0 1 0 17 H -22 Z" {fill} {stroke} stroke-width="2" />
        {:else if n.op === 'OR' || n.op === 'XOR'}
          <path d="M -22 -17 Q -10 0 -22 17 Q 8 17 22 0 Q 8 -17 -22 -17 Z" {fill} {stroke} stroke-width="2" />
          {#if n.op === 'XOR'}<path d="M -28 -17 Q -16 0 -28 17" fill="none" {stroke} stroke-width="2" />{/if}
        {:else if n.op === 'NOT'}
          <path d="M -16 -13 L 10 0 L -16 13 Z" {fill} {stroke} stroke-width="2" />
          <circle cx="14" r="4" fill="#fff" {stroke} stroke-width="2" />
        {:else}
          <rect x="-20" y="-14" width="40" height="28" rx="7" {fill} {stroke} stroke-width="2" />
        {/if}
        <text x={n.op === 'NOT' ? -4 : 0} y="4" text-anchor="middle" font-size={n.op === 'IMP' || n.op === 'IFF' ? 14 : 9} font-weight="650" fill={stroke}>{n.op === 'NOT' ? '' : sym[n.op]}</text>
      </g>
    {/if}
  {/each}
</svg>

<style>
  .circuit { width: 100%; height: auto; max-height: 460px; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; display: block; min-height: 160px; }
  .inp { cursor: pointer; }
  .inp:focus { outline: none; }
  .inp:focus circle { stroke: #0369a1; stroke-width: 3; }
</style>
