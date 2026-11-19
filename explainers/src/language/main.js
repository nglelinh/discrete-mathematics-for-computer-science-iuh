import '../shared/ui.css';
import CykExplainer from './CykExplainer.svelte';
import DeriveExplainer from './DeriveExplainer.svelte';
import TmExplainer from './TmExplainer.svelte';
import PdaExplainer from './PdaExplainer.svelte';
import RegexExplainer from './RegexExplainer.svelte';
import MealyExplainer from './MealyExplainer.svelte';
import PumpingExplainer from './PumpingExplainer.svelte';
import CfgPdaExplainer from './CfgPdaExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-preset: classic|anbn|reject   data-input: chuỗi (ký hiệu cách nhau bằng khoảng trắng)   data-grammar: văn phạm (\n phân dòng)
const gram = (el) => attr(el, 'grammar').replace(/\\n/g, '\n');
mountAll('[data-demo="cyk-explainer"]', CykExplainer, (el) => ({ preset: attr(el, 'preset', 'classic'), input: attr(el, 'input'), grammar: gram(el) }));
// data-preset: expr-amb|expr-unamb|else|paren
mountAll('[data-demo="derive-explainer"]', DeriveExplainer, (el) => ({ preset: attr(el, 'preset', 'expr-amb'), input: attr(el, 'input'), grammar: gram(el) }));
// data-preset: inc|anbn|unary
mountAll('[data-demo="tm-explainer"]', TmExplainer, (el) => ({ preset: attr(el, 'preset', 'inc'), input: attr(el, 'input') }));
// data-preset: anbn|ww|paren
mountAll('[data-demo="pda-explainer"]', PdaExplainer, (el) => ({ preset: attr(el, 'preset', 'anbn'), input: attr(el, 'input') }));
// data-tab: thompson|eliminate   data-regex   data-preset: dfa01|even1|nfa101   data-order: forward|reverse
mountAll('[data-demo="regex-explainer"]', RegexExplainer, (el) => ({ tab: attr(el, 'tab', 'thompson'), regex: attr(el, 'regex'), preset: attr(el, 'preset'), order: attr(el, 'order', 'forward') }));
// data-preset: m11|add|mod3   data-input
mountAll('[data-demo="mealy-explainer"]', MealyExplainer, (el) => ({ preset: attr(el, 'preset', 'm11'), input: attr(el, 'input') }));
// data-kind: regular|cfl   data-lang: anbn|pal|abstar | anbncn|anbn|ww   data-p
mountAll('[data-demo="pumping-explainer"]', PumpingExplainer, (el) => ({ kind: attr(el, 'kind', 'regular'), lang: attr(el, 'lang'), p: attr(el, 'p', '3') }));
// data-preset: expr-amb|expr-unamb|else|paren   data-input   data-grammar
mountAll('[data-demo="cfgpda-explainer"]', CfgPdaExplainer, (el) => ({ preset: attr(el, 'preset', 'paren'), input: attr(el, 'input'), grammar: attr(el, 'grammar').replace(/\\n/g, '\n') }));
