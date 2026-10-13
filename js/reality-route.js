/* The six-stage reality-show route spans two connected, three-stage pages. */
(function () {
  'use strict';
  var serial = 0;
  var transferSlides = [];
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var points = [19, 50, 81];

  function esc(value) {
    return String(value == null ? '' : value).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function config(sl) { return sl && sl._s && sl._s.routeRoadmap; }
  function road(part) {
    var mask = 'reality-route-mask-' + (++serial);
    var segments = [
      { step: 2, d: 'M19 56 C27 56 26 51 33 51 C40 51 39 56 50 56' },
      { step: 3, d: 'M50 56 C59 56 57 59.5 64 59.5 C73 59.5 71 56 81 56' }
    ];
    /* Both page edges meet at y=52 with a horizontal tangent. */
    if (part === 1) segments.push({ step: 3, d: 'M81 56 C90 56 89 52 100 52' });
    else segments.unshift({ step: 1, d: 'M0 52 C9 52 10 56 19 56' });
    return '<svg class="rr-road" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><defs>' +
      '<mask id="' + mask + '" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><rect width="100" height="100" fill="white"/>' +
      points.map(function (x) { return '<circle cx="' + x + '" cy="56" r="2.9" fill="black"/>'; }).join('') +
      '</mask></defs><g mask="url(#' + mask + ')">' + segments.map(function (segment) {
        return '<path class="rr-guide" d="' + segment.d + '"/><path class="rr-trace" data-route-segment="' + segment.step + '" pathLength="1" d="' + segment.d + '"/>';
      }).join('') + '</g></svg>';
  }
  function render(s, idx) {
    var c = s.routeRoadmap;
    var sec = document.createElement('section');
    sec.className = 'slide reality-route full';
    sec.dataset.idx = idx;
    sec.dataset.lv = s.lv;
    sec.dataset.routePart = c.part;
    sec._s = s;
    sec.setAttribute('aria-label', String(s.t || '').replace(/<[^>]*>/g, ''));
    sec.innerHTML = '<header class="rr-heading">' + (s.k ? '<div class="rr-eyebrow">' + esc(s.k) + '</div>' : '') +
      '<h1 class="rr-title split-done">' + esc(s.t).replace('сегодня', '<span class="rr-accent">сегодня</span>') + '</h1></header>' + road(Number(c.part)) +
      '<ol class="rr-items" start="' + Number(c.items[0].number) + '">' + c.items.map(function (item, i) {
        var number = String(item.number).padStart(2, '0');
        var label = esc(number + ' · ' + item.title);
        return '<li class="rr-item" data-route-item="' + (i + 1) + '" style="--route-x:' + points[i] + 'cqw">' +
          '<button type="button" class="rr-art" data-route-select="' + (i + 1) + '" aria-label="' + label + '"><img data-src="' + esc(item.sketch) + '" alt="" decoding="async"></button>' +
          '<button type="button" class="rr-node" data-route-select="' + (i + 1) + '" aria-label="' + label + '">' + number + '</button>' +
          '<div class="rr-copy"><h2 class="rr-item-title">' + esc(item.title) + '</h2><p class="rr-detail">' + esc(item.detail) + '</p></div></li>';
      }).join('') + '</ol>' + (c.takeaway ? '<p class="rr-takeaway">' + esc(c.takeaway).replace('≈35', '<strong>≈35</strong>').replace(' — ', ' —<br>') + '</p>' : '');
    sec.addEventListener('click', function (event) {
      var button = event.target.closest('[data-route-select]');
      if (!button || !sec.contains(button)) return;
      event.stopPropagation();
      setStep(sec, Number(button.dataset.routeSelect));
      sec.dispatchEvent(new CustomEvent('realityroutechange', { bubbles: true }));
    });
    setStep(sec, bounds(c)[0]);
    return sec;
  }
  /* range [a,b] — копія екрана показує лише пункти a..b (між ними в деці стоять демо-слайди). */
  function bounds(c) { var r = c.range || [1, c.items.length]; return [Number(r[0]), Number(r[1])]; }
  function setStep(sl, n) {
    var c = config(sl);
    if (!c) return;
    n = Math.max(0, Math.min(c.items.length, Number(n) || 0));   /* 0 = ще жодного пункту (для входу з анімацією) */
    sl.dataset.routeStep = n;
    sl.querySelectorAll('[data-route-item]').forEach(function (item) {
      var step = Number(item.dataset.routeItem);
      item.dataset.state = step < n ? 'past' : step === n ? 'active' : 'future';
      item.querySelectorAll('[data-route-select]').forEach(function (button) {
        if (step === n) button.setAttribute('aria-current', 'step');
        else button.removeAttribute('aria-current');
      });
    });
    sl.querySelectorAll('[data-route-segment]').forEach(function (segment) {
      segment.dataset.drawn = String(Number(segment.dataset.routeSegment) <= n);
    });
  }
  /* 03.10: вхід уперед — миттєво стаємо на попередній пункт, одразу лінія домальовується до активного (з 04 на 05…).
     Початок маршруту (пункт 1 на першій сторінці) і вхід назад — без анімації. */
  function enter(sl, dir) {
    var c = config(sl);
    if (!c) return;
    var b = bounds(c);
    clearTimeout(sl._rrTimer);
    if (dir < 0) { setStep(sl, b[1]); return; }
    var from = b[0] - 1;
    if (reduced.matches || (from < 1 && Number(c.part) === 1)) { setStep(sl, b[0]); return; }
    sl.classList.add('rr-instant');
    setStep(sl, from);
    void sl.offsetWidth;
    sl.classList.remove('rr-instant');
    /* слайд стає видимим (.on) уже після enter(): за 20 мс спершу фіксуємо попередній стан (offsetWidth), тоді вмикаємо активний → transition */
    sl._rrTimer = setTimeout(function () { void sl.offsetWidth; setStep(sl, b[0]); }, 20);   /* 03.10: без паузи — рух починається одразу */
  }
  function advance(sl, dir) {
    var c = config(sl);
    if (!c) return false;
    clearTimeout(sl._rrTimer);
    var cur = Number(sl.dataset.routeStep);
    if (dir > 0 && cur < bounds(c)[0]) { setStep(sl, bounds(c)[0]); return true; }   /* клік під час анімації входу — одразу на активний */
    var n = cur + dir;
    if (n < bounds(c)[0] || n > bounds(c)[1]) return false;
    setStep(sl, n);
    return true;
  }
  function cue(sl) {
    var c = config(sl);
    if (!c) return '';
    var item = c.items[Number(sl.dataset.routeStep) - 1];
    return 'Шаг ' + item.number + '/6. ' + item.title + ' — ' + item.detail + '. ' +
      (Number(sl.dataset.routeStep) === bounds(c)[1] ? 'Следующий клик — следующая страница.' : 'Следующий клик — следующий пункт.');
  }
  function prepare(from, to, dir) {
    transferSlides.forEach(function (sl) { sl.classList.remove('rr-forward', 'rr-backward'); });
    transferSlides = [];
    var a = config(from), b = config(to);
    if (!a || !b || from === to || !dir || reduced.matches || Math.abs(Number(a.part) - Number(b.part)) !== 1) return false;
    if ((dir > 0) !== (Number(b.part) > Number(a.part))) return false;
    var direction = dir > 0 ? 'rr-forward' : 'rr-backward';
    from.classList.add(direction);
    to.classList.add(direction);
    transferSlides = [from, to];
    return true;
  }
  function snapshot(sl) { return config(sl) ? Number(sl.dataset.routeStep) : null; }
  function restore(sl, saved) { if (saved != null) setStep(sl, saved); }

  window.RealityRoute = { render: render, enter: enter, advance: advance, cue: cue, prepare: prepare, snapshot: snapshot, restore: restore };
})();
