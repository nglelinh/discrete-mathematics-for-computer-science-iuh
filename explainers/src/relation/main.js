import '../shared/ui.css';
import RelationExplainer from './RelationExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-preset: mod2|leq|div|lt|sym|next|empty   data-focus: props|warshall|classes|hasse
mountAll('[data-demo="relation-explainer"]', RelationExplainer, (el) => ({
  preset: attr(el, 'preset', 'mod2'),
  focus: attr(el, 'focus')
}));
