import '../shared/ui.css';
import AutomataExplainer from './AutomataExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-preset: dfa01|even1|nfa101|nfa3|enfa|empty   data-tab: simulate|subset|minimize   data-input: chuỗi mẫu
mountAll('[data-demo="automata-explainer"]', AutomataExplainer, (el) => ({
  preset: attr(el, 'preset', 'dfa01'),
  tab: attr(el, 'tab', 'simulate'),
  input: attr(el, 'input')
}));
