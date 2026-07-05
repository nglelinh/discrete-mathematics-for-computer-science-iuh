/**
 * Textbook lesson enhancements: MathJax equation layout + reference anchors.
 */
(function () {
  function enhanceEquations() {
    document.querySelectorAll(".textbook-equation").forEach(function (eq) {
      if (eq.dataset.tbEnhanced) return;
      var mjx = eq.querySelector("mjx-container");
      if (mjx && eq.querySelector(".textbook-equation-number")) {
        eq.dataset.tbEnhanced = "1";
      }
    });
  }

  function onReady() {
    enhanceEquations();
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
      MathJax.startup.promise.then(enhanceEquations);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", onReady);
  } else {
    onReady();
  }
})();