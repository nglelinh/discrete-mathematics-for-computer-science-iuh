import '../shared/ui.css';
import ExprTree from './ExprTree.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-formula: công thức ban đầu (mặc định ((p ∨ q) → ¬r) ↔ p)
mountAll('[data-demo="exprtree-explainer"]', ExprTree, (el) => ({ formula: attr(el, 'formula', '((p ∨ q) → ¬r) ↔ p') }));
