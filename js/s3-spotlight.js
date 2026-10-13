(function () {
  'use strict';
  window.S3Variants = window.S3Variants || {};
  var serial = 0;
  function esc(value) { return String(value || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function sculpture(kind, key) {
    var id = 's3sp-' + key + '-' + kind;
    var defs = '<defs>' +
      '<linearGradient id="' + id + '-metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#F9F4D1"/><stop offset=".22" stop-color="#84711B"/><stop offset=".49" stop-color="#201C11"/><stop offset=".78" stop-color="#B8960C"/><stop offset="1" stop-color="#FDD506"/></linearGradient>' +
      '<linearGradient id="' + id + '-dark" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#49453B"/><stop offset=".42" stop-color="#1C1A15"/><stop offset="1" stop-color="#0B0907"/></linearGradient>' +
      '<linearGradient id="' + id + '-gold" x1="0" y1="0" x2=".8" y2="1"><stop stop-color="#FFF4A5"/><stop offset=".3" stop-color="#FDD506"/><stop offset="1" stop-color="#715906"/></linearGradient>' +
      '<linearGradient id="' + id + '-side" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#12100A"/><stop offset=".45" stop-color="#BA980A"/><stop offset=".68" stop-color="#FDD506"/><stop offset="1" stop-color="#493905"/></linearGradient>' +
      '<radialGradient id="' + id + '-light"><stop stop-color="#FDD506" stop-opacity=".28"/><stop offset="1" stop-color="#FDD506" stop-opacity="0"/></radialGradient>' +
      '<filter id="' + id + '-glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="8"/></filter>' +
      '</defs>';
    var shapes = '';
    if (kind === 0) {
      shapes = '<ellipse cx="255" cy="408" rx="172" ry="52" fill="url(#' + id + '-light)"/>' +
        '<g transform="rotate(-10 250 250)">' +
        [0, 1, 2].map(function (i) {
          var y = 325 - i * 49;
          return '<path d="M107 ' + y + 'v32c0 34 63 61 141 61s141-27 141-61v-32" fill="url(#' + id + '-side)" stroke="#9C811A" stroke-width="1.4"/><ellipse cx="248" cy="' + y + '" rx="141" ry="61" fill="url(#' + id + '-metal)" stroke="#F9E77E" stroke-width="2"/><ellipse cx="248" cy="' + y + '" rx="119" ry="46" fill="url(#' + id + '-dark)" stroke="#BFA841" stroke-width="1.2"/>';
        }).join('') +
        '<path d="M159 234l56 9 51-33 58 7" fill="none" stroke="#FDD506" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/><path d="M303 200l22 18-29 10" fill="none" stroke="#FDD506" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>' +
        '<path d="M123 288c19 23 74 42 130 40M125 339c28 21 63 33 91 36" fill="none" stroke="#F7DF66" stroke-width="2" opacity=".6"/>' +
        '</g>';
    } else if (kind === 1) {
      shapes = '<ellipse cx="251" cy="421" rx="183" ry="53" fill="url(#' + id + '-light)"/>' +
        '<path d="M100 207l161-70 154 63-159 76z" fill="url(#' + id + '-dark)" stroke="#514B39" stroke-width="2"/>' +
        '<path d="M100 207v164l156 68V276z" fill="url(#' + id + '-dark)" stroke="#7C7045" stroke-width="2"/>' +
        '<path d="M256 276l159-76v166l-159 73z" fill="#100F0C" stroke="#6A5D32" stroke-width="2"/>' +
        '<path d="M164 176l91-43 89 37v184l-89 43-91-39z" fill="#FDD506" opacity=".34" filter="url(#' + id + '-glow)"/>' +
        '<path d="M174 99l91-40 89 40v188l-91 40-89-40z" fill="url(#' + id + '-gold)" stroke="#FFF3A8" stroke-width="2"/>' +
        '<path d="M190 120l72-32 76 31v147l-76 34-72-33z" fill="url(#' + id + '-dark)" stroke="#D8BD44" stroke-width="1.4"/>' +
        '<path d="M220 171l31 29 57-30" fill="none" stroke="#FDD506" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>' +
        '<path d="M100 207l156 69 159-76M256 276v162" stroke="#FDD506" stroke-width="3" fill="none"/>' +
        '<path d="M100 207l-36 67 149 69 43-67M256 276l52 57 144-75-37-58" fill="url(#' + id + '-dark)" stroke="#BEA952" stroke-width="2"/>' +
        '<path d="M111 209l142 62M265 275l135-64" stroke="#FFF3AD" stroke-width="2" fill="none"/>';
    } else {
      shapes = '<ellipse cx="250" cy="420" rx="184" ry="54" fill="url(#' + id + '-light)"/>' +
        '<g transform="translate(0 28)">' +
        '<path d="M81 293l163-84 175 82v33l-174 89-164-83z" fill="url(#' + id + '-dark)" stroke="#716946" stroke-width="2"/>' +
        '<path d="M81 293l163-84 175 82-174 87z" fill="url(#' + id + '-metal)" stroke="#C9B76B" stroke-width="2"/>' +
        '<path d="M112 222l133-68 142 67v35l-142 73-133-69z" fill="url(#' + id + '-side)" stroke="#D8B924" stroke-width="2"/>' +
        '<path d="M112 222l133-68 142 67-142 74z" fill="url(#' + id + '-dark)" stroke="#FDE260" stroke-width="2"/>' +
        '<path d="M143 150l102-52 109 52v52l-109 54-102-52z" fill="#FDD506" opacity=".7" filter="url(#' + id + '-glow)"/>' +
        '<path d="M143 150l102-52 109 52v52l-109 54-102-52z" fill="url(#' + id + '-gold)" stroke="#FFF1A1" stroke-width="2"/>' +
        '<path d="M143 150l102 50 109-50" stroke="#FFF4B5" stroke-width="2" fill="none"/><path d="M245 200v56" stroke="#B08A0A" stroke-width="2"/>' +
        '<path d="M206 151l38-20 42 20-41 21z" fill="#19160C"/><path d="M181 183l20 10M290 198l23-12M144 272l29 14M319 287l32-17" stroke="#FDD506" stroke-width="4" stroke-linecap="round"/>' +
        '</g>';
    }
    return '<svg viewBox="0 0 500 500" aria-hidden="true" focusable="false">' + defs + shapes + '</svg>';
  }
  window.S3Variants.spotlight = {
    setStep: function (scene, step) {
      if (step >= 1 && step <= 3) scene.dataset.focus = step;
      scene.dataset.step = step;
      var final = step === 4;
      scene.querySelector('.sp-content').setAttribute('aria-hidden', String(final));
      scene.querySelector('.sp-closing').setAttribute('aria-hidden', String(!final));
      var video = scene.querySelector('[data-s3-final]');
      if (video) {
        if (final && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
          video.muted = true;
          video.currentTime = 0;
          video.play().catch(function () {});
        } else video.pause();
      }
    },
    render: function (c) {
      var key = ++serial;
      var closing = String(c.closing || '').split(/\s+—\s+/);
      var ask = closing.slice(1).join(' — ');
      var meme = c.finalMedia ? '<div class="sp-final-media"><video data-s3-final src="' + esc(c.finalMedia.src) + '" poster="' + esc(c.finalMedia.poster) + '" aria-label="' + esc(c.finalMedia.alt) + '" muted loop playsinline preload="none"></video><img class="sp-final-still" src="' + esc(c.finalMedia.poster) + '" alt="' + esc(c.finalMedia.alt) + '"></div>' : '';
      return '<div class="s3-design s3-spotlight' + (meme ? ' sp-has-meme' : '') + '" data-step="1" data-focus="1">' +
        '<div class="sp-content">' +
        '<div class="sp-ambient" aria-hidden="true"></div>' +
        '<h1 class="sp-header">' + c.lines.join('<br>') + '</h1>' +
        '<div class="sp-sculptures">' + c.items.map(function (item, i) {
          return '<article class="sp-item sp-item-' + (i + 1) + '"><div class="sp-art">' + sculpture(i, key) + '</div><div class="sp-caption"><h2>' + item.title + '</h2><p>' + item.detail + '</p></div></article>';
        }).join('') + '</div>' +
        '<div class="sp-dots" aria-hidden="true"><i></i><i></i><i></i></div>' +
        '</div><div class="sp-closing" aria-hidden="true"><span class="sp-lead">' + esc(closing[0]) + '</span>' +
        (ask ? '<span class="sp-ask">' + esc(ask.charAt(0).toUpperCase() + ask.slice(1)) + '</span>' : '') + meme + '</div></div>';
    }
  };
}());
