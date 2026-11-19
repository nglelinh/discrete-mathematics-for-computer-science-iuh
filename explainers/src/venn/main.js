import '../shared/ui.css';
import VennExplainer from './VennExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-sets: 2|3   data-expr: biểu thức tô   data-expr-b: biểu thức so sánh   data-focus: shade|compare|ie
mountAll('[data-demo="venn-explainer"]', VennExplainer, (el) => ({
  sets: Number(attr(el, 'sets', '3')) === 2 ? 2 : 3,
  expr: attr(el, 'expr'),
  exprB: attr(el, 'expr-b'),
  focus: attr(el, 'focus')
}));
