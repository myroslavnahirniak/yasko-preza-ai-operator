/* A single audience cue; all editorial copy comes from slide overrides. */
(function () {
  'use strict';

  function esc(value) {
    return String(value || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function render(c) {
    var lines = (c.lines || []).map(function (text) {
      return '<span>' + esc(text) + '</span>';
    }).join('');

    return '<div class="participation-copy">' +
      '<h1 class="participation-heading">' + lines + '</h1>' +
      '<div class="participation-instruction">' +
        '<p class="participation-action">' + esc(c.prompt) + '</p>' +
        '<p class="participation-privacy">' + esc(c.support) + '</p>' +
      '</div>' +
    '</div>';
  }

  window.Participation = { render: render };
})();
