/* A single automatic process, confined to the illustration area. */
(function () {
  'use strict';
  var serial = 0;
  function render(description) {
    var id = 'rules-run-' + (++serial);
    var label = String(description || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
    return '<div class="cv-workflow" role="img" aria-label="' + label + '">' +
      '<svg viewBox="0 0 840 240" fill="none" aria-hidden="true">' +
      '<defs><linearGradient id="' + id + '-scan" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#FDD506" stop-opacity="0"/><stop offset="1" stop-color="#FDD506" stop-opacity=".16"/></linearGradient>' +
      '<clipPath id="' + id + '-clip"><rect x="327" y="39" width="154" height="160" rx="15"/></clipPath></defs>' +
      '<g class="wf-links"><path class="wf-guide" d="M208 120h37l12-12h29l12 12h29M481 120h28l12 12h28l12-12h31"/>' +
      '<path class="wf-trace wf-trace-in" pathLength="1" d="M208 120h37l12-12h29l12 12h29"/>' +
      '<path class="wf-trace wf-trace-out" pathLength="1" d="M481 120h28l12 12h28l12-12h31"/>' +
      '<circle class="wf-port" cx="208" cy="120" r="3"/><circle class="wf-port" cx="592" cy="120" r="3"/></g>' +
      '<g class="wf-input"><rect class="wf-card" x="24" y="60" width="184" height="124" rx="13"/>' +
      '<path class="wf-input-mark" d="M43 80h12m-12 5h7"/>' +
      '<path class="wf-textline wf-type-1" pathLength="1" d="M45 105h138"/>' +
      '<path class="wf-textline wf-type-2" pathLength="1" d="M45 124h107"/>' +
      '<path class="wf-textline wf-type-3" pathLength="1" d="M45 143h77"/>' +
      '<g class="wf-send"><circle cx="179" cy="156" r="13"/><path d="M173 156h12m-5-5 5 5-5 5"/></g></g>' +
      '<g class="wf-engine"><rect class="wf-engine-frame" x="327" y="39" width="154" height="160" rx="15"/>' +
      '<path class="wf-pins" d="M349 31v8m22-8v8m22-8v8m22-8v8m22-8v8m22-8v8M349 199v8m22-8v8m22-8v8m22-8v8m22-8v8m22-8v8M319 60h8m-8 23h8m-8 23h8m-8 23h8m-8 23h8m-8 23h8M481 60h8m-8 23h8m-8 23h8m-8 23h8m-8 23h8m-8 23h8"/>' +
      '<g clip-path="url(#' + id + '-clip)"><rect class="wf-scan" x="327" y="40" width="154" height="49" fill="url(#' + id + '-scan)"/></g>' +
      '<rect class="wf-core" x="351" y="64" width="106" height="91" rx="9"/>' +
      '<text class="wf-ai" x="404" y="124">AI</text>' +
      '<g class="wf-activity"><rect class="wf-meter wf-meter-1" x="369" y="171" width="16" height="5" rx="2"/><rect class="wf-meter wf-meter-2" x="396" y="171" width="16" height="5" rx="2"/><rect class="wf-meter wf-meter-3" x="423" y="171" width="16" height="5" rx="2"/></g></g>' +
      '<g class="wf-output"><path class="wf-page-back" d="M605 53h151v132H605Z"/>' +
      '<path class="wf-page" d="M594 41h127l37 37v118H594V41Z"/>' +
      '<path class="wf-fold" d="M721 41v37h37"/>' +
      '<path class="wf-result-title" pathLength="1" d="M613 67h77"/>' +
      '<path class="wf-result-row wf-result-row-1" pathLength="1" d="M641 105h92"/>' +
      '<path class="wf-result-row wf-result-row-2" pathLength="1" d="M641 136h74"/>' +
      '<path class="wf-result-row wf-result-row-3" pathLength="1" d="M641 167h88"/>' +
      '<path class="wf-check wf-check-1" pathLength="1" d="m612 104 7 7 12-14"/>' +
      '<path class="wf-check wf-check-2" pathLength="1" d="m612 135 7 7 12-14"/>' +
      '<path class="wf-check wf-check-3" pathLength="1" d="m612 166 7 7 12-14"/></g>' +
      '<g class="wf-payment"><rect x="679" y="171" width="132" height="53" rx="12"/>' +
      '<circle class="wf-coin" cx="709" cy="197" r="15"/><path class="wf-currency" d="M709 186v22m5-18h-8a4 4 0 0 0 0 8h5a4 4 0 0 1 0 8h-8"/>' +
      '<path class="wf-pay-check" pathLength="1" d="m748 197 10 10 21-24"/></g>' +
      '</svg></div>';
  }
  window.RulesMotion = { render: render };
})();
