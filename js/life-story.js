/* Source-bound story chapter. One Google page stays one presentation page. */
(function () {
  'use strict';
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var rail, world, trace, currentGoogle = null, lightbox;
  function esc(v) { return String(v == null ? '' : v).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function plain(v) { var el = document.createElement('div'); el.innerHTML = v || ''; return el.textContent; }
  function config(sl) { return sl && sl._s && sl._s.lifeStory; }
  function art(p, eager) {
    var c = p.crop || [0, 0, p.width, p.height], w = c[2], h = c[3];
    var r = ((p.rotate || 0) % 360 + 360) % 360, rw = r === 90 || r === 270 ? h : w, rh = r === 90 || r === 270 ? w : h;
    var tr = r === 90 ? 'translate(' + h + ' 0) rotate(90)' : r === 270 ? 'translate(0 ' + w + ') rotate(-90)' : r === 180 ? 'translate(' + w + ' ' + h + ') rotate(180)' : '';
    return '<svg viewBox="0 0 ' + rw + ' ' + rh + '" preserveAspectRatio="' + (p.position || 'xMidYMid') + ' ' + (p.fit === 'contain' ? 'meet' : 'slice') + '" aria-hidden="true">' +
      '<g transform="' + tr + '"><svg x="0" y="0" width="' + w + '" height="' + h + '" viewBox="' + c.join(' ') + '"><image ' + (eager ? 'href' : 'data-life-href') + '="' + esc(p.src) + '" width="' + p.width + '" height="' + p.height + '"/></svg></g></svg>';
  }
  function headline(s, c) {
    var t = esc(plain(s.t));
    if (c.accent) t = t.replace(esc(c.accent), '<em>' + esc(c.accent) + '</em>');
    (c.breakAfter || []).forEach(function (part) { t = t.replace(esc(part), esc(part) + '<br>'); });
    (c.breakBefore || []).forEach(function (part) { t = t.replace(esc(part), '<br>' + esc(part)); });
    return t;
  }
  function render(s, idx) {
    var c = s.lifeStory, photos = c.photos || [], sec = document.createElement('section');
    sec.className = 'slide life-story full ls-' + c.layout + (c.quiet ? ' ls-quiet' : '') + (c.variant ? ' ls-' + c.variant : '');
    sec.dataset.idx = idx; sec.dataset.lv = s.lv; sec.dataset.google = s.googleNumber; sec._s = s;
    sec.style.setProperty('--ls-title-size', (c.titleSize || 4.5) + 'cqh');
    if (c.columns) sec.style.setProperty('--ls-columns', c.columns);
    var body = s.b || '';
    if (c.quoteAccent) body = body.replace(esc(c.quoteAccent), (c.quoteNewLine ? '<br>' : '') + '<em class="ls-quote-accent">' + esc(c.quoteAccent) + '</em>');
    (c.quoteBreakBefore || []).forEach(function (part) { body = body.replace(esc(part), '<br>' + esc(part)); });
    var copy = c.hideTitle && !s.b && !c.eyebrow ? '' : '<div class="ls-copy">' + (c.eyebrow ? '<div class="ls-eyebrow">' + esc(c.eyebrow) + '</div>' : '') +
      (c.hideTitle ? '' : '<h1 class="ls-title split-done">' + headline(s, c) + '</h1>') + (body ? '<div class="ls-body">' + body + '</div>' : '') + '</div>';
    if (c.hideTitle) sec.setAttribute('aria-label', plain(s.t));
    var gallery = '<div class="ls-gallery ls-count-' + photos.length + '" aria-label="Фотографии этого этапа">' + photos.map(function (p, j) {
      var box = p.crop || [0,0,p.width,p.height], rotated = Math.abs(p.rotate || 0) % 180 === 90;
      var ratio = rotated ? box[3] / box[2] : box[2] / box[3];
      return '<button class="ls-photo ls-' + (p.role || 'photo') + (p.fit === 'contain' ? ' ls-contained' : '') + '" type="button" data-life-photo="' + j + '" aria-label="Увеличить фото ' + (j + 1) + ' из ' + photos.length + '" style="--photo-order:' + j + ';--photo-ratio:' + ratio + '"><span class="ls-photo-frame">' + art(p, false) + '</span></button>';
    }).join('') + (c.badge ? '<span class="ls-photo-badge">' + esc(c.badge) + '</span>' : '') + '</div>';
    if (c.video) gallery = '<div class="ls-gallery ls-film"><video data-src="' + esc(c.video.src) + '" data-poster="' + esc(c.video.poster) + '" playsinline muted loop preload="none"></video></div>';
    if (c.placeholders && !photos.length) gallery = '<div class="ls-gallery ls-count-' + c.placeholders.length + '" aria-label="Места для фотографий">' + c.placeholders.map(function (label) {
      var outline = c.variant === 'photo-slot-wide' ? '<rect x="4" y="9" width="40" height="30" rx="5"/>' : '<rect x="8" y="4" width="32" height="40" rx="5"/>';
      return '<div class="ls-photo ls-placeholder"><div class="ls-photo-frame"><svg viewBox="0 0 48 48" aria-hidden="true">' + outline + '<path d="M17 24h14M24 17v14"/></svg><span>' + esc(label) + '</span><small>' + esc(c.placeholderHint || 'Сторис / пост') + '</small></div></div>';
    }).join('') + '</div>';
    sec.innerHTML = '<div class="ls-content">' + copy + ((photos.length || c.video || c.placeholders) ? gallery : '') + '</div>';
    sec.addEventListener('click', function (event) {
      var button = event.target.closest('[data-life-photo]');
      if (!button) return;
      event.stopPropagation(); openPhoto(photos[Number(button.dataset.lifePhoto)], s.t);
    });
    return sec;
  }
  function closePhoto() { if (lightbox) { lightbox.remove(); lightbox = null; } }
  function openPhoto(photo, title) {
    closePhoto();
    lightbox = document.createElement('div'); lightbox.className = 'ls-lightbox'; lightbox.setAttribute('role', 'dialog'); lightbox.setAttribute('aria-modal', 'true'); lightbox.setAttribute('aria-label', plain(title));
    lightbox.innerHTML = '<div class="ls-lightbox-title">' + esc(plain(title)) + '</div><div class="ls-lightbox-art">' + art(Object.assign({}, photo, {fit:'contain'}), true) + '</div><button type="button" aria-label="Закрыть фотографию">×</button>';
    lightbox.addEventListener('click', function (event) { event.stopPropagation(); closePhoto(); });
    document.getElementById('stage').appendChild(lightbox); lightbox.querySelector('button').focus({preventScroll:true});
  }
  document.addEventListener('keydown', function (event) {
    if (!lightbox && event.key === ' ' && event.target.closest('[data-life-photo], [data-life-google]')) {
      event.preventDefault(); event.stopImmediatePropagation(); event.target.closest('button').click(); return;
    }
    if (!lightbox) return;
    if (['Escape', 'ArrowRight', 'ArrowLeft', ' ', 'Enter'].indexOf(event.key) >= 0) { event.preventDefault(); event.stopImmediatePropagation(); closePhoto(); }
  }, true);
  function buildRail() {
    if (rail) return;
    var seen = {}, entries = window.S.filter(function (s) { if (!s.lifeStory || seen[s.googleNumber]) return false; seen[s.googleNumber] = 1; return true; }), width = 100 + (entries.length - 1) * 28;
    if (!entries.length) return;
    rail = document.createElement('nav'); rail.id = 'life-timeline'; rail.setAttribute('aria-label', 'Линия жизни');
    var d = 'M0 4.5 L50 4.5';
    entries.slice(1).forEach(function (_, j) { var x = 50 + j * 28, bend = j % 2 ? 2.5 : 6.5; d += ' C' + (x+10) + ' 4.5 ' + (x+8) + ' ' + bend + ' ' + (x+14) + ' ' + bend + ' S' + (x+20) + ' 4.5 ' + (x+28) + ' 4.5'; });
    d += ' L' + width + ' 4.5';
    var svg = '<svg viewBox="0 0 ' + width + ' 14" preserveAspectRatio="none" style="width:' + width + 'cqw"><path d="' + d + '"/></svg>';
    rail.innerHTML = '<div class="ls-rail-world" style="width:' + width + 'cqw"><div class="ls-rail-base">' + svg + '</div><div class="ls-rail-progress">' + svg + '</div>' + entries.map(function (s, j) {
      return '<button type="button" class="ls-stop" data-life-google="' + s.googleNumber + '" style="left:' + (50+j*28) + 'cqw"><span class="ls-stop-dot"></span><span class="ls-stop-label">' + esc(s.lifeStory.label) + '</span></button>';
    }).join('') + '</div>';
    world = rail.querySelector('.ls-rail-world'); trace = rail.querySelector('.ls-rail-progress');
    rail.addEventListener('click', function (event) {
      event.stopPropagation(); var button = event.target.closest('[data-life-google]'); if (!button) return;
      var g = Number(button.dataset.lifeGoogle), target = Array.from(document.querySelectorAll('#slides>.slide')).findIndex(function (sl) { return sl._s.googleNumber === g; });
      if (target >= 0 && window.go) window.go(target, g < currentGoogle ? -1 : 1);
    });
    document.getElementById('stage').appendChild(rail);
  }
  function prepare(from, to, dir) {
    closePhoto(); buildRail();
    var a = config(from), c = config(to); if (!rail) return false;
    var continued = !!a && !!c && from !== to;
    rail.classList.toggle('is-visible', !!c);
    if (!c) { currentGoogle = null; return false; }
    var google = to._s.googleNumber, step = Array.from(rail.querySelectorAll('.ls-stop')).findIndex(function (b) { return Number(b.dataset.lifeGoogle) === google; });
    world.classList.toggle('ls-instant', !continued);
    world.style.transform = 'translate3d(' + (-step*28) + 'cqw,0,0)';
    trace.style.width = (50+step*28) + 'cqw';
    rail.querySelectorAll('.ls-stop').forEach(function (button, j) {
      button.classList.toggle('is-current', j === step); button.classList.toggle('is-past', j < step);
      button.tabIndex = Math.abs(j-step) <= 1 ? 0 : -1;
      if (j === step) button.setAttribute('aria-current', 'step'); else button.removeAttribute('aria-current');
    });
    [from,to].forEach(function (sl) { if (config(sl)) sl.style.setProperty('--ls-direction', dir < 0 ? -1 : 1); });
    currentGoogle = google;
    return continued && !reduced.matches;
  }
  function hydrate(sl) {
    if (!config(sl)) return;
    sl.querySelectorAll('[data-life-href]').forEach(function (el) { el.setAttribute('href', el.dataset.lifeHref); el.removeAttribute('data-life-href'); });
  }
  window.LifeStory = {render:render,prepare:prepare,hydrate:hydrate};
})();
