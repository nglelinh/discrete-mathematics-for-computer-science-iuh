<script>
  import { kmapCells, kmapLayout, bitstr } from './logic.js';

  let {
    n,
    values,
    names,
    groups = [],
    hovered = null,
    highlighted = -1,
    probe = null,
    readonly = false,
    title = '',
    onToggle = () => {},
    onHover = () => {},
    onProbe = () => {}
  } = $props();

  const kmap = $derived(kmapCells(n, values));
  const layout = $derived(kmapLayout(n));
  const rowLabel = $derived(layout.rowVars.map((i) => names[i]).join(''));
  const colLabel = $derived(layout.colVars.map((i) => names[i]).join(''));
  const shown = (v) => (v === 2 ? '×' : String(v));
  const hit = (m) => groups.filter((g) => g.covered.has(m));
</script>

<div class="km">
  {#if title}<div class="km-title">{title}</div>{/if}
  <div class="kmap" style={`--cols:${kmap.nCols}; --rows:${kmap.nRows}`}>
    <div class="corner"><span class="row-l">{rowLabel}</span><span class="col-l">{colLabel}</span></div>
    {#each kmap.cols as colVal, c}
      <div class="hd" style={`grid-column:${c + 2};grid-row:1`}>{bitstr(colVal, layout.colBits)}</div>
    {/each}
    {#each kmap.rows as rowVal, r}
      <div class="hd" style={`grid-column:1;grid-row:${r + 2}`}>{bitstr(rowVal, layout.rowBits)}</div>
    {/each}
    <div class="board" style={`grid-column:2 / span ${kmap.nCols}; grid-row:2 / span ${kmap.nRows}; --cols:${kmap.nCols}; --rows:${kmap.nRows}`}>
      {#each kmap.cells as cell}
        {@const gs = hit(cell.minterm)}
        <button
          type="button"
          class="kcell"
          class:one={cell.value === 1}
          class:dc={cell.value === 2}
          class:hot={hovered === cell.minterm}
          class:probe={probe === cell.minterm}
          class:hl={highlighted >= 0 && groups[highlighted]?.covered.has(cell.minterm)}
          disabled={false}
          style={gs[0] ? `--g:${gs[0].color}` : ''}
          onmouseenter={() => onHover(cell.minterm)}
          onmouseleave={() => onHover(null)}
          onclick={() => (readonly ? onProbe(cell.minterm) : onToggle(cell.minterm))}
        >
          <em>m{cell.minterm}</em>
          <strong>{shown(cell.value)}</strong>
        </button>
      {/each}
      <svg class="overlay" viewBox="0 0 {kmap.nCols} {kmap.nRows}" preserveAspectRatio="none">
        {#each groups as g, gi}
          {#each g.rects as rect}
            <rect
              x={rect.c0 + 0.08}
              y={rect.r0 + 0.08}
              width={rect.w - 0.16}
              height={rect.h - 0.16}
              rx="0.12"
              fill="none"
              stroke={g.color}
              stroke-width={highlighted === gi || highlighted < 0 ? 0.12 : 0.07}
              opacity={highlighted === gi || highlighted < 0 ? 0.95 : 0.35}
            />
          {/each}
        {/each}
      </svg>
    </div>
  </div>
</div>

<style>
  .km { min-width: 0; }
  .km-title { font-size: 0.8rem; font-weight: 650; color: #004586; margin-bottom: 4px; }
  .kmap { display: grid; grid-template-columns: 42px repeat(var(--cols), 1fr); grid-template-rows: 28px repeat(var(--rows), 1fr); max-width: 420px; }
  .corner { position: relative; }
  .corner .col-l { position: absolute; right: 2px; top: 0; font-size: 0.72rem; color: #0369a1; }
  .corner .row-l { position: absolute; left: 0; bottom: 0; font-size: 0.72rem; color: #0369a1; }
  .hd { font-size: 0.75rem; color: #334155; display: flex; align-items: center; justify-content: center; font-family: ui-monospace, Menlo, Consolas, monospace; }
  .board { position: relative; display: grid; grid-template-columns: repeat(var(--cols), 1fr); grid-template-rows: repeat(var(--rows), 1fr); border: 1px solid #cbd5e1; background: #fff; }
  .kcell { position: relative; z-index: 1; aspect-ratio: 1; min-height: 44px; border: 1px solid #e2e8f0; border-radius: 0; background: #fff; color: #0f172a; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0; cursor: pointer; font-family: inherit; }
  .kcell em { font-style: normal; font-size: 0.65rem; color: #94a3b8; }
  .kcell strong { font-size: 1.05rem; }
  .kcell.one { background: #ccfbf1; }
  .kcell.dc { background: repeating-linear-gradient(45deg, #fef3c7, #fef3c7 5px, #fde68a 5px, #fde68a 10px); }
  .kcell.hot { background: #fef9c3; }
  .kcell.probe { outline: 2px solid #0369a1; outline-offset: -3px; }
  .kcell.hl { background: color-mix(in srgb, var(--g) 22%, #fff); }
  .overlay { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 2; pointer-events: none; }
</style>
