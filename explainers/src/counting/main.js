import '../shared/ui.css';
import CountingExplainer from './CountingExplainer.svelte';
import PascalExplainer from '../pascal/PascalExplainer.svelte';
import RuleExplainer from './RuleExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-tab: pascal|choose|stars|pigeon   data-n, data-k: giá trị ban đầu
mountAll('[data-demo="counting-explainer"]', CountingExplainer, (el) => ({
  tab: attr(el, 'tab', 'pascal'),
  n: Number(attr(el, 'n', '0')) || 0,
  k: Number(attr(el, 'k', '0')) || 0
}));

// Tam giác Pascal hoạt ảnh dùng chung bundle với counting (một bản runtime Svelte cho mỗi trang).
// data-tab: build|rowsum|sym|hockey   data-rows: 0–14   data-mode: value|binom   data-color: none|mod2
// data-k, data-n: tham số cho thẻ hockey   data-autoplay: "1" để tự chạy
mountAll('[data-demo="pascal-explainer"]', PascalExplainer, (el) => ({
  tab: attr(el, 'tab', 'build'),
  rows: Number(attr(el, 'rows', '6')),
  mode: attr(el, 'mode', 'value'),
  color: attr(el, 'color', 'none'),
  k: Number(attr(el, 'k', '2')),
  n: Number(attr(el, 'n', '5')),
  autoplay: attr(el, 'autoplay') === '1'
}));

// Cây quy tắc cộng/nhân. data-preset: outfit|meal|plate|pw
mountAll('[data-demo="rule-explainer"]', RuleExplainer, (el) => ({ preset: attr(el, 'preset', 'outfit') }));
