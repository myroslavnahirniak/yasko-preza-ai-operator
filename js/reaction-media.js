(function () {
  'use strict';

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (char) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char];
    });
  }

  function placeholder(alt) {
    return '<div class="reaction-media__empty" role="img" aria-label="' + esc(alt || 'Место для GIF') + '">' +
      '<svg class="reaction-media__icon" viewBox="0 0 48 40" fill="none" aria-hidden="true">' +
        '<rect x="4" y="5" width="40" height="30" rx="2" stroke="currentColor" stroke-width="1.5"/>' +
        '<path d="M12 5V35M36 5V35M4 13H12M4 21H12M4 29H12M36 13H44M36 21H44M36 29H44" stroke="currentColor" stroke-width="1.5"/>' +
        '<path d="M21 14L29 20L21 26V14Z" fill="currentColor"/>' +
      '</svg>' +
      '<span class="reaction-media__label" aria-hidden="true">GIF</span>' +
    '</div>';
  }

  function render(config) {
    var c = config || {};
    var src = String(c.src || '');
    var poster = String(c.poster || '');
    var fit = c.fit === 'contain' ? 'contain' : 'cover';
    var isVideo = /\.(mp4|webm)(?:[?#]|$)/i.test(src);
    var isGif = /\.gif(?:[?#]|$)/i.test(src);
    var hasStill = !!(poster && (isVideo || isGif));
    var classes = 'reaction-media__frame reaction-media__frame--' + fit;
    if (!src) return '<div class="' + classes + ' reaction-media__frame--empty">' + placeholder(c.alt) + '</div>';
    if (hasStill) classes += ' reaction-media__frame--has-still';

    var h = '<div class="' + classes + '">';
    if (isVideo) {
      h += '<video class="reaction-media__asset" data-src="' + esc(src) + '"' +
        (poster ? ' data-poster="' + esc(poster) + '"' : '') +
        (c.alt ? ' aria-label="' + esc(c.alt) + '"' : ' aria-hidden="true"') +
        ' muted loop playsinline preload="none"></video>';
    } else {
      h += '<img class="reaction-media__asset" data-src="' + esc(src) + '" alt="' + esc(c.alt || '') + '" decoding="async">';
    }
    if (hasStill) {
      h += '<img class="reaction-media__still" data-src="' + esc(poster) + '" alt="' + esc(c.alt || '') + '" decoding="async">';
    }
    return h + '</div>';
  }

  window.ReactionMedia = { render: render };
}());
