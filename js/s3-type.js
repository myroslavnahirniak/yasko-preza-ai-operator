/* Slide 3 study: typographic focus, driven by the preview controller. */
(function () {
  'use strict';
  function esc(value) {
    return String(value || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function symbol(index) {
    var shapes = [
      '<path d="M22 103h34v55H22zm51-36h34v91H73zm51-45h34v136h-34z" fill="currentColor"/>',
      '<path d="M21 59v59l61 42 77-94-63-45z" fill="currentColor"/><circle cx="66" cy="65" r="13" class="s3t-cut"/><path d="m91 113 23-29" class="s3t-tagline"/>',
      '<path d="M54 97 88 51l40 57M52 107h70" fill="none" stroke="currentColor" stroke-width="13"/><circle cx="89" cy="42" r="24" fill="currentColor"/><rect x="16" y="87" width="49" height="49" fill="currentColor"/><path d="m138 78 30 57h-60z" fill="currentColor"/>'
    ];
    return '<svg viewBox="0 0 180 180" aria-hidden="true" focusable="false">' + shapes[index] + '</svg>';
  }
  window.S3Variants = window.S3Variants || {};
  window.S3Variants.type = {
    render: function (c) {
      var rows = c.items.map(function (item, index) {
        return '<article class="s3t-row s3t-row-' + (index + 1) + '">' +
          '<div class="s3t-band" aria-hidden="true"></div>' +
          '<span class="s3t-number" aria-hidden="true">0' + (index + 1) + '</span>' +
          '<div class="s3t-claim"><h2>' + esc(item.title) + '</h2><p>' + esc(item.detail) + '</p></div>' +
          '<div class="s3t-symbol">' + symbol(index) + '</div>' +
          '</article>';
      }).join('');
      return '<div class="s3-design s3-type" data-step="1">' +
        '<header class="s3t-header"><h1>' + c.lines.map(function (line) { return '<span>' + line + '</span>'; }).join('') + '</h1></header>' +
        '<div class="s3t-claims">' + rows + '</div>' +
        '<p class="s3t-closing">' + esc(c.closing) + '</p>' +
        '</div>';
    }
  };
})();
