import '../shared/ui.css';
import FunctionExplainer from './FunctionExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-preset: inj|surj|bij|sq|inc|bad   data-focus: props|inverse|compose
mountAll('[data-demo="function-explainer"]', FunctionExplainer, (el) => ({
  preset: attr(el, 'preset', 'inj'),
  focus: attr(el, 'focus')
}));
