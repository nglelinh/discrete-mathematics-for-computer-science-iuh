<script>
  import { onMount, untrack } from 'svelte';
  import * as d3 from 'd3';
  import {
    ALGOS,
    PSEUDO,
    PRESETS,
    cloneGraph,
    buildSteps,
    hasEdge,
    nextNodeId,
    nextEdgeId,
    fmtVal
  } from './algorithms.js';

  let { algorithm = 'bfs' } = $props();

  const W = 680;
  const H = 380;
  const R = 20;
  const COLORS = {
    idle: { fill: '#ffffff', stroke: '#64748b' },
    current: { fill: '#f59e0b', stroke: '#b45309' },
    visited: { fill: '#0f766e', stroke: '#115e59' },
    frontier: { fill: '#38bdf8', stroke: '#0369a1' }
  };
  const EDGE = {
    idle: { stroke: '#94a3b8', width: 2, dash: 'none', opacity: 0.9 },
    active: { stroke: '#f59e0b', width: 4.5, dash: '8 5', opacity: 1 },
    tree: { stroke: '#0f766e', width: 4, dash: 'none', opacity: 1 },
    rejected: { stroke: '#cbd5e1', width: 2, dash: '5 4', opacity: 0.75 }
  };

  let algo = $state(algorithm);
  let source = $state('A');
  let presetKey = $state('mau');
  let graph = $state(cloneGraph(PRESETS.mau.graph()));
  let stepIndex = $state(0);
  let playing = $state(false);
  let speed = $state(1);
  let editMode = $state('drag');
  let forceOn = $state(false);
  let pendingFrom = $state(null);
  let selectedEdge = $state(null);
  let weightDraft = $state(1);
  let svgEl = $state(null);

  const simNodes = [];
  const simLinks = [];
  let simulation = null;
  let zoomBehavior = null;
  let tokenTimer = 0;

  const steps = $derived(buildSteps(graph, algo, source));
  const step = $derived(steps[Math.min(stepIndex, Math.max(0, steps.length - 1))] || steps[0]);
  const pseudo = $derived(PSEUDO[algo] || []);
  const needsSource = $derived(algo !== 'kruskal');
  const duration = $derived(Math.max(80, 700 / speed));

  $effect(() => {
    // Keep source valid when the graph changes.
    if (!graph.nodes.some((n) => n.id === source)) {
      source = graph.nodes[0]?.id || 'A';
    }
  });

  let lastTopoKey = '';
  $effect(() => {
    // Reset playback only when algorithm, source, or topology/weights change
    // (not when a node is merely dragged).
    const key =
      algo +
      '|' +
      source +
      '|' +
      graph.nodes.map((n) => n.id).join(',') +
      '|' +
      graph.edges.map((e) => `${e.id}:${e.u}:${e.v}:${e.w}`).join('|');
    if (key === lastTopoKey) return;
    lastTopoKey = key;
    stepIndex = 0;
    playing = false;
  });

  $effect(() => {
    if (!playing) return;
    const id = setTimeout(() => {
      if (stepIndex >= steps.length - 1) {
        playing = false;
        return;
      }
      stepIndex += 1;
    }, duration + 80);
    return () => clearTimeout(id);
  });

  $effect(() => {
    if (!svgEl) return;
    const el = svgEl;
    setupSvg(el);
    untrack(() => {
      syncTopology();
      applyLayoutForces();
      render(true);
    });
    return () => {
      if (simulation) simulation.stop();
    };
  });

  $effect(() => {
    // Re-bind when topology changes.
    graph.nodes.map((n) => n.id).join(',');
    graph.edges.map((e) => e.id + e.u + e.v).join(',');
    if (!svgEl) return;
    syncTopology();
    render(true);
  });

  $effect(() => {
    forceOn;
    if (!svgEl) return;
    applyLayoutForces();
  });

  $effect(() => {
    step;
    selectedEdge;
    pendingFrom;
    if (!svgEl) return;
    render(false);
  });

  function setupSvg(svg) {
    const sel = d3.select(svg);
    sel.selectAll('*').remove();
    const defs = sel.append('defs');
    const shadow = defs.append('filter').attr('id', 'gex-shadow').attr('x', '-40%').attr('y', '-40%').attr('width', '180%').attr('height', '180%');
    shadow.append('feDropShadow').attr('dx', 0).attr('dy', 1.2).attr('stdDeviation', 1.6).attr('flood-color', '#0f172a').attr('flood-opacity', 0.22);
    const glow = defs.append('filter').attr('id', 'gex-glow');
    glow.append('feGaussianBlur').attr('stdDeviation', 2.2).attr('result', 'b');
    const merge = glow.append('feMerge');
    merge.append('feMergeNode').attr('in', 'b');
    merge.append('feMergeNode').attr('in', 'SourceGraphic');

    const root = sel.append('g').attr('class', 'gex-zoom');
    const grid = root.append('g').attr('class', 'gex-grid');
    for (let x = 0; x <= W; x += 40) {
      grid.append('line').attr('x1', x).attr('x2', x).attr('y1', 0).attr('y2', H).attr('stroke', '#e2e8f0').attr('stroke-width', x % 160 === 0 ? 1.1 : 0.6);
    }
    for (let y = 0; y <= H; y += 40) {
      grid.append('line').attr('y1', y).attr('y2', y).attr('x1', 0).attr('x2', W).attr('stroke', '#e2e8f0').attr('stroke-width', y % 160 === 0 ? 1.1 : 0.6);
    }
    root.append('g').attr('class', 'gex-edges');
    root.append('g').attr('class', 'gex-tokens');
    root.append('g').attr('class', 'gex-nodes');

    zoomBehavior = d3
      .zoom()
      .scaleExtent([0.6, 2.4])
      .on('zoom', (event) => {
        root.attr('transform', event.transform);
      });
    sel.call(zoomBehavior);
    sel.on('dblclick.zoom', null);

    sel.on('click', (event) => {
      if (event.target !== svg && !event.target.classList.contains('gex-grid') && event.target.tagName !== 'line') return;
      if (editMode === 'add-node') {
        const [x, y] = d3.pointer(event, root.node());
        addNodeAt(x, y);
      } else {
        pendingFrom = null;
        selectedEdge = null;
      }
    });
  }

  function syncTopology() {
    const byId = new Map(simNodes.map((n) => [n.id, n]));
    simNodes.length = 0;
    for (const n of graph.nodes) {
      const prev = byId.get(n.id);
      simNodes.push({
        id: n.id,
        x: prev?.x ?? n.x,
        y: prev?.y ?? n.y,
        fx: forceOn ? prev?.fx ?? null : (prev?.x ?? n.x),
        fy: forceOn ? prev?.fy ?? null : (prev?.y ?? n.y)
      });
    }
    const lookup = new Map(simNodes.map((n) => [n.id, n]));
    simLinks.length = 0;
    for (const e of graph.edges) {
      const s = lookup.get(e.u);
      const t = lookup.get(e.v);
      if (s && t) simLinks.push({ id: e.id, source: s, target: t, w: e.w });
    }
    if (!simulation) {
      simulation = d3
        .forceSimulation(simNodes)
        .force('link', d3.forceLink(simLinks).id((d) => d.id).distance(110).strength(0.35))
        .force('charge', d3.forceManyBody().strength(-260))
        .force('center', d3.forceCenter(W / 2, H / 2).strength(0.05))
        .force('collide', d3.forceCollide(R + 14))
        .force('x', d3.forceX(W / 2).strength(0.02))
        .force('y', d3.forceY(H / 2).strength(0.02))
        .on('tick', () => renderPositions());
    } else {
      simulation.nodes(simNodes);
      simulation.force('link').links(simLinks);
    }
  }

  function applyLayoutForces() {
    if (!simulation) return;
    for (const n of simNodes) {
      if (forceOn) {
        n.fx = null;
        n.fy = null;
      } else {
        n.fx = n.x;
        n.fy = n.y;
      }
    }
    simulation.alpha(forceOn ? 0.7 : 0).restart();
    if (!forceOn) simulation.stop();
    renderPositions();
  }

  function persistPositions() {
    const pos = new Map(simNodes.map((n) => [n.id, n]));
    graph = {
      nodes: graph.nodes.map((n) => {
        const p = pos.get(n.id);
        return p ? { ...n, x: p.x, y: p.y } : n;
      }),
      edges: graph.edges.map((e) => ({ ...e }))
    };
  }

  function renderPositions() {
    if (!svgEl) return;
    const root = d3.select(svgEl).select('g.gex-zoom');
    root
      .selectAll('g.gex-edge')
      .attr('transform', (d) => {
        return 'translate(0,0)';
      })
      .each(function (d) {
        const x1 = d.source.x;
        const y1 = d.source.y;
        const x2 = d.target.x;
        const y2 = d.target.y;
        d3.select(this).select('line.gex-e').attr('x1', x1).attr('y1', y1).attr('x2', x2).attr('y2', y2);
        d3.select(this).select('line.gex-e-hit').attr('x1', x1).attr('y1', y1).attr('x2', x2).attr('y2', y2);
        const mx = (x1 + x2) / 2;
        const my = (y1 + y2) / 2;
        d3.select(this).select('g.gex-w').attr('transform', `translate(${mx},${my})`);
      });
    root.selectAll('g.gex-node').attr('transform', (d) => `translate(${d.x},${d.y})`);
  }

  function render(rebuild) {
    if (!svgEl) return;
    const root = d3.select(svgEl).select('g.gex-zoom');
    const edgesG = root.select('g.gex-edges');
    const nodesG = root.select('g.gex-nodes');
    const tokensG = root.select('g.gex-tokens');
    const st = step || { nodes: {}, edges: {} };
    const dur = rebuild ? 0 : duration;

    const edgeSel = edgesG.selectAll('g.gex-edge').data(simLinks, (d) => d.id);
    edgeSel.exit().remove();
    const edgeEnter = edgeSel.enter().append('g').attr('class', 'gex-edge');
    edgeEnter
      .append('line')
      .attr('class', 'gex-e-hit')
      .attr('stroke', 'transparent')
      .attr('stroke-width', 14)
      .style('cursor', 'pointer');
    edgeEnter.append('line').attr('class', 'gex-e').attr('stroke-linecap', 'round');
    const wG = edgeEnter.append('g').attr('class', 'gex-w');
    wG.append('rect').attr('rx', 6).attr('ry', 6).attr('x', -12).attr('y', -10).attr('width', 24).attr('height', 18);
    wG.append('text').attr('text-anchor', 'middle').attr('dy', '0.35em').attr('font-size', 11).attr('font-weight', 700);

    const edgeAll = edgeEnter.merge(edgeSel);
    edgeAll.each(function (d) {
      const status = selectedEdge === d.id ? 'active' : st.edges[d.id] || 'idle';
      const style = EDGE[status] || EDGE.idle;
      const line = d3.select(this).select('line.gex-e');
      line
        .transition()
        .duration(dur)
        .attr('stroke', style.stroke)
        .attr('stroke-width', style.width)
        .attr('stroke-dasharray', style.dash === 'none' ? null : style.dash)
        .attr('opacity', style.opacity);
      const label = String(d.w);
      const tw = Math.max(22, 8 * label.length + 10);
      const wg = d3.select(this).select('g.gex-w');
      wg.select('rect')
        .attr('x', -tw / 2)
        .attr('width', tw)
        .attr('fill', status === 'tree' ? '#ccfbf1' : status === 'active' ? '#fef3c7' : '#fff')
        .attr('stroke', style.stroke);
      wg.select('text').attr('fill', '#0f172a').text(label);
    });
    edgeAll
      .on('click', (event, d) => {
        event.stopPropagation();
        onEdgeClick(d.id);
      })
      .on('dblclick', (event, d) => {
        event.stopPropagation();
        selectedEdge = d.id;
        weightDraft = d.w;
      });

    const nodeSel = nodesG.selectAll('g.gex-node').data(simNodes, (d) => d.id);
    nodeSel.exit().remove();
    const nodeEnter = nodeSel.enter().append('g').attr('class', 'gex-node').style('cursor', 'pointer');
    nodeEnter.append('circle').attr('r', R).attr('filter', 'url(#gex-shadow)');
    nodeEnter
      .append('text')
      .attr('class', 'gex-id')
      .attr('text-anchor', 'middle')
      .attr('dy', '0.35em')
      .attr('font-weight', 750)
      .attr('font-size', 14)
      .attr('pointer-events', 'none');

    const nodeAll = nodeEnter.merge(nodeSel);
    nodeAll.each(function (d) {
      const status = pendingFrom === d.id ? 'frontier' : st.nodes[d.id] || 'idle';
      const style = COLORS[status] || COLORS.idle;
      const c = d3.select(this).select('circle');
      c.transition()
        .duration(dur)
        .attr('fill', style.fill)
        .attr('stroke', style.stroke)
        .attr('stroke-width', status === 'current' ? 4 : 2.4);
      const fillText = status === 'visited' || status === 'current' ? '#fff' : '#0f172a';
      d3.select(this).select('text.gex-id').attr('fill', fillText).text(d.id);
    });

    const drag = d3
      .drag()
      .on('start', (event, d) => {
        if (editMode !== 'drag') return;
        if (forceOn && simulation) {
          if (!event.active) simulation.alphaTarget(0.28).restart();
        }
        d.fx = d.x;
        d.fy = d.y;
      })
      .on('drag', (event, d) => {
        if (editMode !== 'drag') return;
        d.fx = event.x;
        d.fy = event.y;
        d.x = event.x;
        d.y = event.y;
        renderPositions();
      })
      .on('end', (event, d) => {
        if (editMode !== 'drag') return;
        if (forceOn && simulation) {
          if (!event.active) simulation.alphaTarget(0);
          d.fx = null;
          d.fy = null;
        } else {
          d.fx = d.x;
          d.fy = d.y;
        }
        persistPositions();
      });
    nodeAll.call(drag);
    nodeAll.on('click', (event, d) => {
      event.stopPropagation();
      onNodeClick(d.id);
    });

    renderPositions();
    animateToken(tokensG, st, dur);
  }

  function animateToken(tokensG, st, dur) {
    tokensG.selectAll('*').remove();
    const activeId = Object.keys(st.edges || {}).find((id) => st.edges[id] === 'active');
    if (!activeId) return;
    const link = simLinks.find((l) => l.id === activeId);
    if (!link) return;
    const token = tokensG
      .append('circle')
      .attr('r', 6)
      .attr('fill', '#f59e0b')
      .attr('stroke', '#fff')
      .attr('stroke-width', 1.5)
      .attr('filter', 'url(#gex-glow)')
      .attr('cx', link.source.x)
      .attr('cy', link.source.y);
    token
      .transition()
      .duration(dur)
      .ease(d3.easeCubicInOut)
      .attr('cx', link.target.x)
      .attr('cy', link.target.y);
  }

  function onNodeClick(id) {
    if (editMode === 'delete') {
      deleteNode(id);
      return;
    }
    if (editMode === 'add-edge') {
      if (!pendingFrom) {
        pendingFrom = id;
        return;
      }
      if (pendingFrom !== id && !hasEdge(graph, pendingFrom, id)) {
        graph = {
          nodes: graph.nodes.map((n) => ({ ...n })),
          edges: [...graph.edges, { id: nextEdgeId(graph), u: pendingFrom, v: id, w: 1 }]
        };
      }
      pendingFrom = null;
      return;
    }
    if (needsSource) source = id;
  }

  function onEdgeClick(id) {
    const e = graph.edges.find((x) => x.id === id);
    if (!e) return;
    if (editMode === 'delete') {
      graph = { nodes: graph.nodes.map((n) => ({ ...n })), edges: graph.edges.filter((x) => x.id !== id) };
      selectedEdge = null;
      return;
    }
    selectedEdge = id;
    weightDraft = e.w;
  }

  function addNodeAt(x, y) {
    const id = nextNodeId(graph);
    graph = {
      nodes: [...graph.nodes, { id, x, y }],
      edges: graph.edges.map((e) => ({ ...e }))
    };
  }

  function deleteNode(id) {
    graph = {
      nodes: graph.nodes.filter((n) => n.id !== id),
      edges: graph.edges.filter((e) => e.u !== id && e.v !== id)
    };
    if (source === id) source = graph.nodes[0]?.id || 'A';
    pendingFrom = null;
  }

  function applyWeight() {
    if (!selectedEdge) return;
    const w = Number(weightDraft);
    if (!Number.isFinite(w)) return;
    graph = {
      nodes: graph.nodes.map((n) => ({ ...n })),
      edges: graph.edges.map((e) => (e.id === selectedEdge ? { ...e, w } : { ...e }))
    };
  }

  function loadPreset(key) {
    presetKey = key;
    const p = PRESETS[key];
    if (!p) return;
    forceOn = false;
    graph = cloneGraph(p.graph());
    source = graph.nodes[0]?.id || 'A';
    selectedEdge = null;
    pendingFrom = null;
    if (svgEl) {
      d3.select(svgEl).call(zoomBehavior.transform, d3.zoomIdentity);
    }
  }

  function resetView() {
    stepIndex = 0;
    playing = false;
  }

  function toggleForce() {
    forceOn = !forceOn;
    if (!forceOn) persistPositions();
  }

  onMount(() => {
    return () => {
      if (simulation) simulation.stop();
      clearTimeout(tokenTimer);
    };
  });
</script>

<div class="gex">
  <h4>Minh hoạ thuật toán đồ thị</h4>
  <p class="gex-help">
    Chọn thuật toán, quan sát từng bước trên đồ thị (màu sắc, cạnh cây, mã giả được tô), theo dõi hàng đợi / ngăn xếp / hàng đợi ưu tiên ở bảng bên dưới.
    Có thể kéo đỉnh, bật bố cục lực, hoặc sửa đồ thị rồi chạy lại.
  </p>

  <div class="gex-toolbar">
    <label>Thuật toán
      <select bind:value={algo}>
        {#each Object.entries(ALGOS) as [id, label]}
          <option value={id}>{label}</option>
        {/each}
      </select>
    </label>
    {#if needsSource}
      <label>Nguồn
        <select bind:value={source}>
          {#each graph.nodes as n}
            <option value={n.id}>{n.id}</option>
          {/each}
        </select>
      </label>
    {/if}
    <label>Đồ thị mẫu
      <select value={presetKey} onchange={(e) => loadPreset(e.currentTarget.value)}>
        {#each Object.entries(PRESETS) as [id, p]}
          <option value={id}>{p.label}</option>
        {/each}
      </select>
    </label>
    <button type="button" class="gex-sec" class:gex-on={forceOn} onclick={toggleForce}>
      {forceOn ? 'Đang bố cục lực' : 'Bật bố cục lực'}
    </button>
  </div>

  <div class="gex-toolbar">
    <span class="gex-k">Chế độ</span>
    <button type="button" class="gex-sec" class:gex-on={editMode === 'drag'} onclick={() => (editMode = 'drag')}>Kéo đỉnh</button>
    <button type="button" class="gex-sec" class:gex-on={editMode === 'add-node'} onclick={() => (editMode = 'add-node')}>Thêm đỉnh</button>
    <button type="button" class="gex-sec" class:gex-on={editMode === 'add-edge'} onclick={() => (editMode = 'add-edge')}>Thêm cạnh</button>
    <button type="button" class="gex-sec" class:gex-on={editMode === 'delete'} onclick={() => (editMode = 'delete')}>Xóa</button>
    {#if selectedEdge}
      <label>Trọng số
        <input type="number" min="0" step="1" bind:value={weightDraft} style="width:4.5rem" />
      </label>
      <button type="button" class="gex-sec" onclick={applyWeight}>Cập nhật</button>
    {/if}
  </div>

  <div class="gex-controls">
    <button type="button" class="gex-sec" onclick={resetView}>Về đầu</button>
    <button type="button" class="gex-sec" disabled={stepIndex <= 0} onclick={() => { playing = false; stepIndex = Math.max(0, stepIndex - 1); }}>◀ Bước trước</button>
    <button type="button" onclick={() => (playing = !playing)}>{playing ? 'Tạm dừng' : 'Phát'}</button>
    <button type="button" class="gex-sec" disabled={stepIndex >= steps.length - 1} onclick={() => { stepIndex = Math.min(steps.length - 1, stepIndex + 1); }}>Bước sau ▶</button>
    <label>Tốc độ
      <input type="range" min="0.4" max="3" step="0.1" bind:value={speed} />
      <span class="gex-k">{speed.toFixed(1)}×</span>
    </label>
    <span class="gex-k">Bước {stepIndex + 1} / {steps.length}</span>
  </div>

  <div class="gex-body">
    <div class="gex-canvas">
      <svg bind:this={svgEl} viewBox="0 0 {W} {H}" role="img" aria-label="Đồ thị tương tác"></svg>
      <div class="gex-legend">
        <span><i class="sw current"></i>đang xét</span>
        <span><i class="sw frontier"></i>biên / mới</span>
        <span><i class="sw visited"></i>đã xong / trong S</span>
        <span><i class="sw tree"></i>cạnh cây</span>
        <span><i class="sw rejected"></i>bỏ qua</span>
      </div>
    </div>
    <aside class="gex-pseudo">
      <div class="gex-pseudo-title">Mã giả</div>
      <ol>
        {#each pseudo as line, i}
          <li class:on={step && step.line === i}>{line}</li>
        {/each}
      </ol>
    </aside>
  </div>

  <p class="gex-msg">{step?.msg || ''}</p>

  <div class="gex-panels">
    {#if algo === 'bfs'}
      <div class="gex-panel">
        <div class="gex-panel-title">Hàng đợi Q</div>
        <div class="gex-chips">
          {#if !step?.queue?.length}
            <span class="gex-empty">rỗng</span>
          {:else}
            {#each step.queue as id, i}
              <span class="chip q" class:head={i === 0}>{id}{#if i === 0}<small>đầu</small>{/if}</span>
            {/each}
          {/if}
        </div>
      </div>
    {:else if algo === 'dfs'}
      <div class="gex-panel">
        <div class="gex-panel-title">Ngăn xếp (lời gọi đệ quy)</div>
        <div class="gex-chips">
          {#if !step?.stack?.length}
            <span class="gex-empty">rỗng</span>
          {:else}
            {#each step.stack as id, i}
              <span class="chip s" class:head={i === step.stack.length - 1}>{id}{#if i === step.stack.length - 1}<small>đỉnh</small>{/if}</span>
            {/each}
          {/if}
        </div>
      </div>
    {:else if algo === 'dijkstra'}
      <div class="gex-panel">
        <div class="gex-panel-title">Hàng đợi ưu tiên (đỉnh ngoài S, khóa = d)</div>
        <div class="gex-chips">
          {#if !step?.pq?.length}
            <span class="gex-empty">rỗng</span>
          {:else}
            {#each step.pq as item, i}
              <span class="chip q" class:head={i === 0}>{item.id}<small>{fmtVal(item.key)}</small></span>
            {/each}
          {/if}
        </div>
      </div>
    {:else if algo === 'prim'}
      <div class="gex-panel">
        <div class="gex-panel-title">Cạnh ứng viên ra khỏi S (ưu tiên theo w)</div>
        <div class="gex-chips">
          {#if !step?.pq?.length}
            <span class="gex-empty">không còn</span>
          {:else}
            {#each step.pq as item, i}
              <span class="chip q" class:head={i === 0}>{item.edge}<small>w={fmtVal(item.key)}</small></span>
            {/each}
          {/if}
        </div>
      </div>
    {:else if algo === 'kruskal'}
      <div class="gex-panel">
        <div class="gex-panel-title">Danh sách cạnh đã sắp (tổng MST: {step?.mstWeight ?? 0})</div>
        <ol class="gex-elist">
          {#each step?.edgeList || [] as e}
            <li class={e.status}>{e.u}—{e.v} <b>({e.w})</b>
              {#if e.status === 'tree'}✓{:else if e.status === 'rejected'}✗{/if}
            </li>
          {/each}
        </ol>
      </div>
    {/if}

    {#if algo === 'bfs' || algo === 'dijkstra'}
      <div class="gex-panel">
        <div class="gex-panel-title">{algo === 'bfs' ? 'Khoảng cách d(v) (số cạnh)' : 'Bảng khoảng cách d(v)'}</div>
        <table>
          <thead>
            <tr>
              <th>v</th>
              {#each graph.nodes as n}<th>{n.id}</th>{/each}
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>d</td>
              {#each graph.nodes as n}
                <td>{fmtVal(step?.dist?.[n.id])}</td>
              {/each}
            </tr>
          </tbody>
        </table>
      </div>
    {/if}

    {#if algo === 'dijkstra' || algo === 'prim'}
      <div class="gex-panel">
        <div class="gex-panel-title">Tập S {#if step?.mstWeight != null && algo === 'prim'}· tổng = {step.mstWeight}{/if}</div>
        <div class="gex-chips">
          {#if !step?.setS?.length}
            <span class="gex-empty">∅</span>
          {:else}
            {#each step.setS as id}
              <span class="chip v">{id}</span>
            {/each}
          {/if}
        </div>
      </div>
    {/if}

    {#if algo === 'kruskal' && step?.components}
      <div class="gex-panel">
        <div class="gex-panel-title">Thành phần (đại diện Union–Find)</div>
        <div class="gex-chips">
          {#each graph.nodes as n}
            <span class="chip v">{n.id}→{step.components[n.id] ?? n.id}</span>
          {/each}
        </div>
      </div>
    {/if}
  </div>
</div>

<style>
  .gex {
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px 18px 18px;
    background: #fff;
    margin: 14px 0;
    font-family: system-ui, -apple-system, sans-serif;
    color: #0f172a;
  }
  h4 {
    margin: 0 0 6px;
    font-size: 1.08rem;
    color: #004586;
  }
  .gex-help {
    margin: 0 0 10px;
    color: #64748b;
    font-size: 0.92rem;
    line-height: 1.45;
  }
  .gex-toolbar,
  .gex-controls {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
    margin: 0 0 10px;
  }
  label {
    font-size: 0.9rem;
    display: flex;
    gap: 6px;
    align-items: center;
  }
  select,
  input[type='number'] {
    padding: 6px 8px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    background: #fff;
  }
  button {
    padding: 7px 12px;
    border: 1px solid #007bff;
    background: #007bff;
    color: #fff;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
  }
  button.gex-sec {
    background: #fff;
    color: #0f437a;
    border-color: #94a3b8;
  }
  button.gex-on {
    background: #0f766e;
    border-color: #0f766e;
    color: #fff;
  }
  button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  .gex-k {
    color: #64748b;
    font-size: 0.88rem;
  }
  .gex-body {
    display: grid;
    grid-template-columns: 1.45fr 0.85fr;
    gap: 12px;
    align-items: stretch;
  }
  @media (max-width: 800px) {
    .gex-body {
      grid-template-columns: 1fr;
    }
  }
  .gex-canvas {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    background: linear-gradient(180deg, #f8fafc, #fff);
    overflow: hidden;
  }
  svg {
    display: block;
    width: 100%;
    height: auto;
    background: transparent;
  }
  .gex-legend {
    display: flex;
    flex-wrap: wrap;
    gap: 8px 12px;
    padding: 6px 10px 8px;
    font-size: 0.8rem;
    color: #475569;
  }
  .gex-legend .sw {
    display: inline-block;
    width: 11px;
    height: 11px;
    border-radius: 50%;
    margin-right: 5px;
    vertical-align: -1px;
    border: 1px solid #64748b;
  }
  .sw.current { background: #f59e0b; border-color: #b45309; }
  .sw.frontier { background: #38bdf8; border-color: #0369a1; }
  .sw.visited { background: #0f766e; border-color: #115e59; }
  .sw.tree { background: #0f766e; border-radius: 2px; }
  .sw.rejected { background: #cbd5e1; border-radius: 2px; }
  .gex-pseudo {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    background: #0b1220;
    color: #e2e8f0;
    padding: 10px 12px;
    overflow: auto;
    min-height: 220px;
  }
  .gex-pseudo-title {
    font-size: 0.78rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #93c5fd;
    margin-bottom: 6px;
  }
  ol {
    margin: 0;
    padding: 0;
    list-style: none;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.82rem;
    line-height: 1.45;
  }
  ol li {
    padding: 3px 8px;
    border-radius: 6px;
    color: #cbd5e1;
    white-space: pre-wrap;
  }
  ol li.on {
    background: #1e3a5f;
    color: #fff;
    box-shadow: inset 3px 0 0 #38bdf8;
  }
  .gex-msg {
    margin: 10px 0 8px;
    padding: 8px 10px;
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-radius: 8px;
    color: #0c4a6e;
    font-size: 0.92rem;
    line-height: 1.45;
    min-height: 2.6em;
  }
  .gex-panels {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 10px;
  }
  .gex-panel {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 8px 10px 10px;
    background: #f8fafc;
  }
  .gex-panel-title {
    font-size: 0.8rem;
    font-weight: 650;
    color: #004586;
    margin-bottom: 6px;
  }
  .gex-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    align-items: center;
    min-height: 2rem;
  }
  .chip {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-width: 2rem;
    padding: 4px 8px;
    border-radius: 8px;
    background: #fff;
    border: 1px solid #cbd5e1;
    font-weight: 650;
    font-size: 0.92rem;
  }
  .chip small {
    font-weight: 500;
    font-size: 0.68rem;
    color: #64748b;
  }
  .chip.q { border-color: #38bdf8; background: #e0f2fe; }
  .chip.s { border-color: #c4b5fd; background: #ede9fe; }
  .chip.v { border-color: #99f6e4; background: #ccfbf1; }
  .chip.head { box-shadow: 0 0 0 2px #0f766e33; }
  .gex-empty { color: #94a3b8; font-size: 0.88rem; }
  table {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.85rem;
    background: #fff;
  }
  th, td {
    border: 1px solid #e2e8f0;
    padding: 3px 6px;
    text-align: center;
  }
  th { background: #f1f5f9; color: #334155; font-weight: 650; }
  .gex-elist {
    margin: 0;
    padding-left: 1.1rem;
    font-size: 0.88rem;
  }
  .gex-elist li.tree { color: #0f766e; font-weight: 650; }
  .gex-elist li.rejected { color: #94a3b8; text-decoration: line-through; }
  .gex-elist li.active { color: #b45309; font-weight: 650; }
</style>
