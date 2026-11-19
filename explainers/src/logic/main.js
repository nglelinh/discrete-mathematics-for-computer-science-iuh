import '../shared/ui.css';
import InductionExplainer from './InductionExplainer.svelte';
import DpllExplainer from './DpllExplainer.svelte';
import BitsExplainer from './BitsExplainer.svelte';
import InfinityExplainer from './InfinityExplainer.svelte';
import AdderExplainer from './AdderExplainer.svelte';
import SimExplainer from './SimExplainer.svelte';
import InferenceExplainer from './InferenceExplainer.svelte';
import ContradictionExplainer from './ContradictionExplainer.svelte';
import PredProofExplainer from './PredProofExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-preset: sum|pow2|div3|nobase|prime
mountAll('[data-demo="induction-explainer"]', InductionExplainer, (el) => ({ preset: attr(el, 'preset', 'sum') }));
// data-preset: sat|unit|unsat|php   data-cnf: công thức CNF tùy ý
mountAll('[data-demo="dpll-explainer"]', DpllExplainer, (el) => ({ preset: attr(el, 'preset', 'sat'), cnf: attr(el, 'cnf') }));
// data-tab: twos|add|endian|y2038   data-bits: 4|8   data-value, data-a, data-b
mountAll('[data-demo="bits-explainer"]', BitsExplainer, (el) => ({
  tab: attr(el, 'tab', 'twos'), bits: attr(el, 'bits', '8'), value: attr(el, 'value'), a: attr(el, 'a'), b: attr(el, 'b')
}));
// data-tab: diagonal|hilbert|pairing   data-scenario: one|bus|buses
mountAll('[data-demo="infinity-explainer"]', InfinityExplainer, (el) => ({ tab: attr(el, 'tab', 'diagonal'), scenario: attr(el, 'scenario', 'bus') }));
// data-a, data-b (0–15), data-sub: true|false
mountAll('[data-demo="adder-explainer"]', AdderExplainer, (el) => ({ a: attr(el, 'a', '11'), b: attr(el, 'b', '6'), sub: attr(el, 'sub', 'false') }));
// data-tab: birthday|hash|queue   data-days, data-buckets, data-keys, data-lambda, data-service (ms), data-servers
mountAll('[data-demo="sim-explainer"]', SimExplainer, (el) => ({ tab: attr(el, 'tab', 'birthday'), days: attr(el, 'days', '365'), buckets: attr(el, 'buckets', '30'), keys: attr(el, 'keys', '20'), lambda: attr(el, 'lambda', '40'), service: attr(el, 'service', '100'), servers: attr(el, 'servers', '6') }));
// data-preset: mp|mt|hs|ds|res|aff|den   data-premises (\n phân dòng), data-conclusion
mountAll('[data-demo="inference-explainer"]', InferenceExplainer, (el) => ({ preset: attr(el, 'preset', 'mp'), premises: attr(el, 'premises'), conclusion: attr(el, 'conclusion') }));

// data-tab: sqrt2|primes   data-a, data-b (phân số thử)   data-primes: "2,3,5,7"
mountAll('[data-demo="contradiction-explainer"]', ContradictionExplainer, (el) => ({ tab: attr(el, 'tab', 'sqrt2'), a: attr(el, 'a', '14'), b: attr(el, 'b', '10'), primes: attr(el, 'primes', '2,3,5,7') }));
// data-preset: socrates|exists|ei-twice|ug-bad
mountAll('[data-demo="predproof-explainer"]', PredProofExplainer, (el) => ({ preset: attr(el, 'preset', 'socrates') }));
