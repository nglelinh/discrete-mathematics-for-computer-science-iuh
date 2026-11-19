import '../shared/ui.css';
import TreeExplainer from './TreeExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-mode: huffman|traversal|bst   data-freqs: "a:5 b:9"   data-keys: "8 3 10 1 6"   data-msg: thông điệp mẫu
mountAll('[data-demo="tree-explainer"]', TreeExplainer, (el) => ({
  mode: attr(el, 'mode', 'huffman'),
  freqs: attr(el, 'freqs'),
  keys: attr(el, 'keys'),
  msg: attr(el, 'msg')
}));
