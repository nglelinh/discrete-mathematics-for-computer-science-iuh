import '../shared/ui.css';
import BooleanExplainer from './BooleanExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-vars: 2|3|4   data-expr: biểu thức A   data-expr-b: biểu thức B (chế độ so sánh)
// data-focus: table|circuit|kmap   data-dc: "3,5" (ô don't-care)   data-mode: single|compare
// data-form: sop|pos (dạng tối tiểu hiển thị)   data-circuit: ast|sop|pos
mountAll('[data-demo="boolean-explainer"]', BooleanExplainer, (el) => {
  const n = Number(attr(el, 'vars', '3'));
  return {
    vars: n === 2 || n === 4 ? n : 3,
    focus: attr(el, 'focus'),
    expr: attr(el, 'expr'),
    exprB: attr(el, 'expr-b'),
    dc: attr(el, 'dc'),
    mode: attr(el, 'mode', 'single'),
    form: attr(el, 'form', 'sop'),
    circuit: attr(el, 'circuit', 'ast')
  };
});
