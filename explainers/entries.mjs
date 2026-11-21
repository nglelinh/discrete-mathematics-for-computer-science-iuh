// Danh sách bundle: key = mode của Vite, cũng là tên file đầu ra.
export const ENTRIES = {
  'exprtree-explainer': { entry: 'src/exprtree/main.js', name: 'ExprTreeExplainer' },
  'graph-explainer': { entry: 'src/graph/main.js', name: 'GraphExplainer' },
  'boolean-explainer': { entry: 'src/boolean/main.js', name: 'BooleanExplainer' },
  'qm-explainer': { entry: 'src/qm/main.js', name: 'QMExplainer' },
  'venn-explainer': { entry: 'src/venn/main.js', name: 'VennExplainer' },
  'relation-explainer': { entry: 'src/relation/main.js', name: 'RelationExplainer' },
  'function-explainer': { entry: 'src/function/main.js', name: 'FunctionExplainer' },
  'counting-explainer': { entry: 'src/counting/main.js', name: 'CountingExplainer' },
  'recurrence-explainer': { entry: 'src/recurrence/main.js', name: 'RecurrenceExplainer' },
  'automata-explainer': { entry: 'src/automata/main.js', name: 'AutomataExplainer' },
  'tree-explainer': { entry: 'src/tree/main.js', name: 'TreeExplainer' },
  'logic-explainer': { entry: 'src/logic/main.js', name: 'LogicExplainer' },
  'complexity-explainer': { entry: 'src/complexity/main.js', name: 'ComplexityExplainer' },
  'language-explainer': { entry: 'src/language/main.js', name: 'LanguageExplainer' },
  'numtheory-explainer': { entry: 'src/numtheory/main.js', name: 'NumTheoryExplainer' }
};
