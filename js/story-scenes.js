/* Opening 6–15: a readable thought and a reserved reaction clip. */
(function () {
  'use strict';
  function esc(value) {
    return String(value || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function render(c) {
    var copy = c.eyebrow ? '<div class="story-eyebrow">' + esc(c.eyebrow) + '</div>\n' : '';
    if (c.typography === 'quote') {
      var quote = [c.lead ? esc(c.lead) : '', (c.lines || []).join(' '), c.tail ? esc(c.tail) : '', c.closing ? esc(c.closing) : ''].filter(Boolean).join(' ');
      if (c.quoteParagraphs) quote = c.quoteParagraphs.map(function (p) { return '<span class="story-quote-paragraph">' + p + '</span>'; }).join(' ');
      copy += '<h1 class="story-title story-quote split-done">' + quote + '</h1>\n';
    } else {
    if (c.lead) copy += '<p class="story-lead">' + esc(c.lead) + '</p>\n';
    copy += '<h1 class="story-title split-done">' + (c.lines || []).map(function (line) {
      return '<span>' + line + '</span>';
    }).join(' ') + '</h1>\n';
    if (c.tail) copy += '<p class="story-tail">' + esc(c.tail) + '</p>\n';
    if (c.closing) copy += '<p class="story-closing">' + esc(c.closing) + '</p>\n';
    }
    return '<div class="story-composition story-' + esc(c.tone || 'recognition') + (c.typography === 'quote' ? ' story-unified' : '') + (c.quoteParagraphs ? ' story-two-quotes' : '') + (c.textOnly ? ' story-text-only' : '') + (c.image ? ' story-with-image' : '') + '">' +
      (c.image ? '<div class="story-art"><img data-src="' + esc(c.image) + '" alt="' + esc(c.imageAlt) + '"></div>' : '') +
      '<div class="story-copy">' + copy + '</div>' +
      (c.textOnly ? '' : '<div class="reaction-media">' + window.ReactionMedia.render(c.media || {}) + '</div>') +
    '</div>';
  }
  window.StoryScenes = { render: render };
})();
