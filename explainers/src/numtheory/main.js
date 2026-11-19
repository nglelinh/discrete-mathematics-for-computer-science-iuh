import '../shared/ui.css';
import NumTheoryExplainer from './NumTheoryExplainer.svelte';
import CryptoExplainer from './CryptoExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-tab: euclid|modular|fastexp|sieve|rsa   data-a, data-b: số đầu vào cho tab euclid/modular
mountAll('[data-demo="numtheory-explainer"]', NumTheoryExplainer, (el) => ({
  tab: attr(el, 'tab', 'euclid'),
  a: attr(el, 'a'),
  b: attr(el, 'b')
}));

// data-tab: crt|miller|dh   data-n, data-a (cho miller)
mountAll('[data-demo="crypto-explainer"]', CryptoExplainer, (el) => ({ tab: attr(el, 'tab', 'crt'), n: attr(el, 'n', '561'), a: attr(el, 'a', '2') }));
