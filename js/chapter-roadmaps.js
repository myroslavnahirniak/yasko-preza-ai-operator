/* Stationary, click-led roadmaps for the transition out of audience recognition. */
(function () {
  'use strict';
  var pathSerial = 0;
  function esc(value) {
    return String(value == null ? '' : value).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function heading(lines) {
    return '<h1 class="chapter-title split-done">' + (lines || []).map(function (line) {
      return '<span>' + line + '</span>';
    }).join(' ') + '</h1>';
  }
  function illustration(name) {
    var art = {
      school: '<path class="road-art-wash" d="M16 66V32L48 13l32 19v34Z"/><path d="M10 67h76M18 65V33l30-19 30 19v32M11 36l37-24 37 24M40 66V49h16v17M27 40h7v7h-7ZM62 40h7v7h-7Z"/><circle cx="48" cy="32" r="6"/><path d="M48 28v5h4M48 12V4h15v7H48"/>',
      study: '<path class="road-art-wash" d="M12 34q18-8 35 2 18-10 37-2v30q-19-5-37 2-17-7-35-2Z"/><path d="M12 34q18-8 35 2 18-10 37-2v30q-19-5-37 2-17-7-35-2ZM47 37v28M20 43l17 2M20 51l17 2M58 44l16-2M58 52l16-2M24 23l24-12 25 12-25 12-24-12ZM72 24v15"/>',
      portfolio: '<rect class="road-art-wash" x="14" y="27" width="65" height="39" rx="3"/><path d="M14 40v23a3 3 0 0 0 3 3h59a3 3 0 0 0 3-3V39M14 42V29a3 3 0 0 1 3-3h59a3 3 0 0 1 3 3v13l-26 7H40l-26-7ZM35 26V17h24v9M40 45h13v9H40"/><path d="M70 9h16v24M74 15h7M74 21h7"/>',
      orders: '<path class="road-art-wash" d="M17 10h40l10 11v43H17Z"/><path d="M17 65V10h39l11 11v15M56 10v12h11M26 29h28M26 39h21M26 49h16M23 65h25"/><circle cx="69" cy="56" r="16"/><path d="M69 46v20M75 49h-8a4 4 0 0 0 0 8h4a4 4 0 0 1 0 8h-8"/>',
      money: '<path class="road-art-wash" d="M12 25h72v38H12Z"/><path d="M12 25h72v38H12ZM19 25v7h-7M77 25v7h7M19 63v-7h-7M77 63v-7h7M20 18h58M28 11h42M23 44h6M67 44h6"/><circle cx="48" cy="44" r="12"/><path d="M44 45l3 3 6-8"/>'
    };
    return '<svg viewBox="0 0 96 80" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (art[name] || '') + '</svg>';
  }
  function path(kind, items) {
    var personal = kind === 'roadmap15';
    var points = personal ? [[82, 39], [74, 59], [85, 79]] : [[10, 32], [10, 44], [10, 56], [10, 68], [10, 80]];
    var segments = personal ? [
      'M82 39 C94 40 94 49 81 51 C70 52 66 56 74 59',
      'M74 59 C78 66 94 62 89 70 C87 74 81 76 85 79'
    ] : [
      'M10 32 C10 37 15 37 15 39 C15 42 10 40 10 44',
      'M10 44 C10 49 5 49 5 51 C5 54 10 52 10 56',
      'M10 56 C10 61 15 61 15 63 C15 66 10 64 10 68',
      'M10 68 C10 73 5 73 5 75 C5 78 10 76 10 80'
    ];
    var maskId = 'chapter-node-mask-' + (++pathSerial);
    var html = '<svg class="chapter-path" viewBox="0 0 100 100" fill="none" aria-hidden="true"><defs><mask id="' + maskId + '" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><rect width="100" height="100" fill="white"/>' + points.map(function (xy) {
      return '<circle cx="' + xy[0] + '" cy="' + xy[1] + '" r="2.6" fill="black"/>';
    }).join('') + '</mask></defs><g mask="url(#' + maskId + ')">';
    segments.forEach(function (d, i) {
      html += '<path class="chapter-guide" d="' + d + '"/>';
      html += '<path class="chapter-trace" data-road-segment="' + (i + 2) + '" pathLength="1" d="' + d + '"/>';
    });
    html += '</g>';
    points.forEach(function (xy, i) {
      html += '<g class="chapter-node" data-road-node="' + (i + 1) + '" data-state="' + (i ? 'future' : 'active') + '"><circle cx="' + xy[0] + '" cy="' + xy[1] + '" r="2.45"/><text x="' + xy[0] + '" y="' + (xy[1] + .12) + '">' + esc(items[i].marker || (i + 1)) + '</text></g>';
    });
    return html + '</svg>';
  }
  function render(c) {
    if (c.kind === 'bridge16') {
      var media = c.media && c.media.src ? c.media : null;
      return '<div class="chapter-roadmap chapter-bridge' + (media ? ' chapter-bridge-has-media' : '') + '" data-step="1" data-steps="1">' +
        '<div class="chapter-bridge-copy"><span class="chapter-rule" aria-hidden="true"></span>' + heading(c.lines) +
        '<p class="chapter-bridge-support">' + esc(c.support) + '</p></div>' +
        (media ? '<figure class="chapter-bridge-media"><img data-src="' + esc(media.src) + '" alt="' + esc(media.alt) + '" decoding="async"></figure>' : '') + '</div>';
    }
    var items = c.items || [];
    var count = items.length + (c.summary ? 1 : 0);
    var html = '<div class="chapter-roadmap chapter-' + esc(c.kind) + '" data-step="1" data-steps="' + count + '">' +
      '<header class="chapter-heading">' + (c.eyebrow ? '<div class="chapter-eyebrow">' + esc(c.eyebrow) + '</div>' : '') + heading(c.lines) + '</header>' +
      '<div class="chapter-route">' + path(c.kind, items) + '<ol class="chapter-items">';
    items.forEach(function (item, i) {
      html += '<li class="chapter-item chapter-item-' + (i + 1) + '" data-road-step="' + (i + 1) + '" data-state="' + (i ? 'future' : 'active') + '" aria-hidden="' + Boolean(i) + '">' +
        '<p class="chapter-item-title">' + item.text + '</p>' + (item.detail ? '<p class="chapter-item-detail">' + esc(item.detail) + '</p>' : '') + '</li>';
    });
    html += '</ol>';
    if (items.some(function (item) { return item.photo; })) {
      html += '<div class="chapter-photos">' + items.map(function (item, i) {
        if (!item.photo) return '';
        var photo = item.photo;
        var crop = photo.crop;
        var imageStyle = crop ? 'width:' + (100 * crop.sourceWidth / crop.width) + '%;height:' + (100 * crop.sourceHeight / crop.height) + '%;left:' + (-100 * crop.x / crop.width) + '%;top:' + (-100 * crop.y / crop.height) + '%;' : '';
        return '<figure class="chapter-photo chapter-photo-' + (i + 1) + '" data-road-photo="' + (i + 1) + '" data-state="' + (i ? 'future' : 'active') + '" aria-hidden="' + Boolean(i) + '"><div class="chapter-photo-crop"><img data-src="' + esc(photo.src) + '" alt="' + esc(photo.alt) + '" style="' + imageStyle + '"></div></figure>';
      }).join('') + '</div>';
    }
    if (items.some(function (item) { return item.illustration || item.sketch; })) {
      html += '<div class="chapter-illustrations' + (c.illustrationStyle === 'sketch' ? ' chapter-sketches' : '') + '" aria-hidden="true">' + items.map(function (item, i) {
        return '<div class="chapter-illustration chapter-illustration-' + (i + 1) + '" data-road-art="' + (i + 1) + '" data-state="' + (i ? 'future' : 'active') + '">' + (item.sketch ? '<img data-src="' + esc(item.sketch) + '" alt="">' : illustration(item.illustration)) + '</div>';
      }).join('') + '</div>';
    }
    html += '</div>';
    if (c.summary) {
      html += '<div class="chapter-summary" aria-hidden="true"><p class="chapter-summary-lead">' + esc(c.summary.lead) + '</p>' +
        '<p class="chapter-summary-old">' + c.summary.old + '</p>' +
        (c.summary.now ? '<p class="chapter-summary-now">' + c.summary.now + '</p>' : '') + '</div>';
    }
    return html + '</div>';
  }
  function root(scene) {
    return scene && (scene.matches('.chapter-roadmap') ? scene : scene.querySelector('.chapter-roadmap'));
  }
  function stepCount(scene) {
    var el = root(scene);
    return el ? Number(el.dataset.steps) || 1 : 1;
  }
  function setStep(scene, n) {
    var el = root(scene);
    if (!el) return;
    n = Math.max(1, Math.min(stepCount(el), Number(n) || 1));
    el.dataset.step = String(n);
    var summary = el.querySelector('.chapter-summary');
    var finale = Boolean(summary && n === stepCount(el));
    el.classList.toggle('chapter-final', finale);
    el.querySelectorAll('[data-road-step]').forEach(function (item) {
      var i = Number(item.dataset.roadStep);
      item.dataset.state = i < n ? 'past' : i === n ? 'active' : 'future';
      item.setAttribute('aria-hidden', String(i > n || finale));
    });
    el.querySelectorAll('[data-road-node]').forEach(function (node) {
      var i = Number(node.dataset.roadNode);
      node.dataset.state = i < n ? 'past' : i === n ? 'active' : 'future';
    });
    el.querySelectorAll('[data-road-art]').forEach(function (art) {
      var i = Number(art.dataset.roadArt);
      art.dataset.state = i < n ? 'past' : i === n ? 'active' : 'future';
    });
    el.querySelectorAll('[data-road-photo]').forEach(function (photo) {
      var i = Number(photo.dataset.roadPhoto);
      photo.dataset.state = i < n ? 'past' : i === n ? 'active' : 'future';
      photo.setAttribute('aria-hidden', String(i > n || finale));
    });
    el.querySelectorAll('[data-road-segment]').forEach(function (segment) {
      segment.dataset.drawn = String(Number(segment.dataset.roadSegment) <= n);
    });
    if (summary) summary.setAttribute('aria-hidden', String(!finale));
  }
  window.ChapterRoadmaps = { render: render, setStep: setStep, stepCount: stepCount };
})();
