import '../shared/ui.css';
import { mount } from 'svelte';
import GraphExplainer from './GraphExplainer.svelte';
import TopoExplainer from './TopoExplainer.svelte';
import MatchExplainer from './MatchExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

const ALGO = new Set(['bfs', 'dfs', 'dijkstra', 'kruskal', 'prim']);

function boot(root = document) {
  const nodes = root.querySelectorAll('[data-demo="graph-explainer"]');
  nodes.forEach((el) => {
    if (el.dataset.mounted === '1') return;
    el.dataset.mounted = '1';
    const raw = (el.getAttribute('data-algorithm') || 'bfs').toLowerCase();
    const algorithm = ALGO.has(raw) ? raw : 'bfs';
    mount(GraphExplainer, { target: el, props: { algorithm } });
  });
}

// data-preset: courses|diamond|build   data-algo: kahn|dfs   data-cycle: true|false
mountAll('[data-demo="topo-explainer"]', TopoExplainer, (el) => ({
  preset: attr(el, 'preset', 'courses'),
  algo: attr(el, 'algo', 'kahn'),
  cycle: attr(el, 'cycle', 'false')
}));

// data-tab: matching|coloring   data-preset: jobs|hall|chain | crown|c5|sched   data-order: index|degree|bad
mountAll('[data-demo="match-explainer"]', MatchExplainer, (el) => ({ tab: attr(el, 'tab', 'matching'), preset: attr(el, 'preset'), order: attr(el, 'order', 'index') }));

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => boot());
} else {
  boot();
}

export { boot };
