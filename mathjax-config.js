window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['ams', 'newcommand', 'configmacros']},
    macros: {
      // Logic symbols
      land: '\\wedge',
      lor: '\\vee',
      lnot: '\\neg',
      limpl: '\\rightarrow',
      liff: '\\leftrightarrow',
      
      // Set theory
      N: '\\mathbb{N}',
      Z: '\\mathbb{Z}',
      Q: '\\mathbb{Q}',
      R: '\\mathbb{R}',
      C: '\\mathbb{C}',
      
      // Common operators
      floor: ['\\lfloor #1 \\rfloor', 1],
      ceil: ['\\lceil #1 \\rceil', 1],
      abs: ['\\left| #1 \\right|', 1],
      
      // Graph theory
      deg: '\\text{deg}',
      
      // Probability
      Pr: '\\text{Pr}',
      E: '\\text{E}',
      Var: '\\text{Var}',
      
      // Complexity
      O: '\\mathcal{O}',
      Theta: '\\Theta',
      Omega: '\\Omega'
    }
  },
  options: {
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process'
  },
  startup: {
    ready: function () {
      MathJax.startup.defaultReady();
      console.log('MathJax is loaded and ready for Discrete Mathematics!');
    }
  }
};
