import '../shared/ui.css';
import ReductionExplainer from './ReductionExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-tab: 3sat|clique|approx   data-cnf: CNF tùy ý   data-graph: house|cycle|star|matching
mountAll('[data-demo="reduction-explainer"]', ReductionExplainer, (el) => ({ tab: attr(el, 'tab', '3sat'), cnf: attr(el, 'cnf'), graph: attr(el, 'graph', 'house') }));
