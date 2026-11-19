import '../shared/ui.css';
import QMExplainer from './QMExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-preset: f1|dc3|four|cyclic|five|six     data-vars: 2–6     data-minterms: "5,6,7,9-11"     data-dc: "0,7"
// data-expr: biểu thức (thay cho minterm)       data-names: "w,x,y,z"     data-start: số bước, hoặc "end"
mountAll('[data-demo="qm-explainer"]', QMExplainer, (el) => ({
  preset: attr(el, 'preset', 'f1'),
  vars: Number(attr(el, 'vars', '0')) || 0,
  minterms: attr(el, 'minterms'),
  dc: attr(el, 'dc'),
  expr: attr(el, 'expr'),
  names: attr(el, 'names'),
  start: attr(el, 'start')
}));
