import '../shared/ui.css';
import RecurrenceExplainer from './RecurrenceExplainer.svelte';
import SortExplainer from './SortExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// data-mode: linear|dc|fib   data-preset: fib|hanoi|two|double|complex|nonhom
mountAll('[data-demo="recurrence-explainer"]', RecurrenceExplainer, (el) => ({
  mode: attr(el, 'mode', 'linear'),
  preset: attr(el, 'preset', 'fib')
}));

// data-tab: sort|search   data-algo: bubble|insertion|selection   data-data: "5,2,9,1,7,3"
mountAll('[data-demo="sort-explainer"]', SortExplainer, (el) => ({ tab: attr(el, 'tab', 'sort'), algo: attr(el, 'algo', 'bubble'), data: attr(el, 'data', '5,2,9,1,7,3') }));
