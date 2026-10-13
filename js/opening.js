/* Opening scenes: independent text/media layers and speaker-controlled focus. */
(function () {
  'use strict';
  var running = [], restore = [];
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  function esc(value) { return String(value || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;'); }
  function plus() { return '<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M50 12V88M12 50H88"/></svg>'; }
  function line(text, index) { return '<span class="op-line"><span class="op-enter" style="--step:' + index + '">' + text + '</span></span>'; }
  function render(s, idx) {
    var c = s.opening, sec = document.createElement('section');
    sec.className = 'slide opening op-' + c.scene + ' full';
    if (c.video) sec.classList.add('op-has-video');
    if (c.surface === 'ambient') sec.classList.add('op-ambient');
    sec.dataset.idx = idx; sec.dataset.google = s.googleNumber; sec.dataset.lv = s.lv; sec._s = s;
    sec.setAttribute('aria-label', String(s.t).replace(/<[^>]*>/g, ''));
    if (c.background) sec.style.backgroundImage = 'url("' + c.background + '")';
    if (c.background) sec.classList.add('op-background');
    var chapter = c.scene === 'chapter' ? window.ChapterRoadmaps : c.scene === 'chapter-format' ? window.ChapterFormat : c.scene === 'chapter-visual' ? window.ChapterVisuals : null;
    if (chapter) {
      sec.classList.add('op-chapter');
      /* 01.10: bgVideo — фоновий ролик під главою (слайд 8 «реалити-шоу»), ліниве завантаження через hydrate() */
      if (c.bgVideo) sec.classList.add('op-bgv');
      var skin = c.skin;   /* 02.10: варіанти оформлення сцени (слайд 8); 03.10: ?skin=a|b|c — подивитись варіант без зміни деки */
      if (c.bgVideo) { try { var q = new URLSearchParams(location.search).get('skin'); if (/^[a-z]$/.test(q || '')) skin = q; } catch (e) {} }
      if (skin) sec.classList.add('op-skin-' + skin);
      sec.innerHTML = (c.bgVideo ? '<div class="op-bgvideo" aria-hidden="true"><video data-src="' + esc(c.bgVideo.src) + '" data-poster="' + esc(c.bgVideo.poster) + '" autoplay muted loop playsinline preload="none"></video></div>' : '') + chapter.render(c);
      return sec;
    }
    if (c.variant === 'spotlight' && window.S3Variants) {
      sec.classList.remove('op-reveal');
      sec.classList.add('op-spotlight');
      sec.innerHTML = window.S3Variants.spotlight.render(c);
      sec.querySelector('h1').classList.add('split-done');
      return sec;
    }
    if (c.scene === 'participation-cue' && window.Participation) {
      sec.innerHTML = window.Participation.render(c);
      return sec;
    }
    if (c.scene === 'story' && window.StoryScenes) {
      sec.innerHTML = window.StoryScenes.render(c);
      return sec;
    }
    var h = '';
    if (s.bg_photo && /^(intro|feeling|recognition)$/.test(c.scene)) {
      h += '<div class="op-media"><img data-src="' + esc(s.bg_photo) + '" alt="" aria-hidden="true">';
      if (c.video) h += '<video data-src="' + esc(c.video) + '" data-poster="' + esc(s.bg_photo) + '" muted loop playsinline preload="none" aria-hidden="true"></video>';
      h += '</div>';
    }
    if (c.scene === 'participate') h += '<div class="op-plus-large op-enter" data-op-share="plus">' + plus() + '</div>';
    h += '<div class="op-copy">';
    h += '<div class="op-eyebrow' + (c.scene === 'recognition' ? '' : ' op-enter') + '" style="--step:0">';
    if (c.scene === 'recognition') h += '<span class="op-plus-small" data-op-share="plus">' + plus() + '</span>';
    h += esc(c.eyebrow) + '</div>';
    h += '<h1>' + c.lines.map(function (t, k) { return line(t, k + 1); }).join('') + '</h1>';
    if (c.body) h += '<p class="op-body op-enter" style="--step:4">' + c.body + '</p>';
    if (c.support) h += '<p class="op-support op-enter" style="--step:4">' + c.support + '</p>';
    if (c.closing && c.scene !== 'reveal') h += '<div class="op-closing op-enter" style="--step:5">' + (c.scene === 'feeling' ? '<i class="op-light" data-op-share="light"></i>' : '') + c.closing + '</div>';
    if (c.signature) h += '<div class="op-signature op-enter" style="--step:5">' + c.signature + '</div>';
    if (c.participation) h += '<div class="op-participation op-enter" style="--step:6">' + esc(c.participation) + '</div>';
    h += '</div>';
    if (c.items) {
      h += '<div class="op-reveal-stage"><i class="op-rail" data-op-share="light"></i><div class="op-offerings">';
      c.items.forEach(function (item, k) {
        h += '<article class="op-offering" style="--item:' + k + '"><div class="op-object"><img data-src="' + esc(item.art) + '" alt="" aria-hidden="true"></div><h2>' + esc(item.title) + '</h2><p>' + esc(item.detail) + '</p></article>';
      });
      h += '</div>' + (c.closing ? '<div class="op-exchange op-enter" style="--step:6">' + c.closing + '</div>' : '') + '</div>';
    }
    sec.innerHTML = h;
    return sec;
  }
  function cancel() {
    running.forEach(function (a) { a.cancel(); }); running = [];
    restore.forEach(function (fn) { fn(); }); restore = [];
    document.querySelectorAll('.op-shared-flight').forEach(function (el) { el.remove(); });
  }
  function scene(sl) { return sl && sl.querySelector('.s3-spotlight,.chapter-roadmap,.chapter-format,.chapter-visual,.ag-stepper'); }
  function controller(target) {
    if (target.matches('.chapter-roadmap')) return window.ChapterRoadmaps;
    if (target.matches('.chapter-format')) return window.ChapterFormat;
    if (target.matches('.chapter-visual')) return window.ChapterVisuals;
    if (target.matches('.ag-stepper')) return window.AgentSteps;
    return window.S3Variants.spotlight;
  }
  function count(target) {
    var api = controller(target); if (api.stepCount) return api.stepCount(target);
    /* 01.10: без фінальної фрази (closing) у reveal лише пункти — кіт переїхав окремим слайдом */
    var sl = target.closest('.slide'), c = sl && sl._s && sl._s.opening;
    return c && c.items && !c.closing ? c.items.length : 4;
  }
  function enter(sl, dir) {
    var target = scene(sl); if (!target) return;
    var api = controller(target);
    if (dir < 0 && target.matches('.s3-spotlight')) api.setStep(target, 3);
    api.setStep(target, target.matches('.wave-cinema') ? 1 : (dir < 0 ? count(target) : 1));
  }
  function step(sl, dir) {
    var target = scene(sl); if (!target) return false;
    var next = Number(target.dataset.step) + dir;
    if (next < 1 || next > count(target)) return false;
    controller(target).setStep(target, next);
    return true;
  }
  function cue(sl) {
    var target = scene(sl); if (!target) return '';
    var n = Number(target.dataset.step), c = sl._s.opening;
    if (!target.matches('.s3-spotlight')) {
      var api = controller(target), detail = api.cue ? api.cue(target) : '';
      if (target.matches('.chapter-format') || target.matches('.ag-stepper')) return detail;
      return 'Шаг ' + n + '/' + count(target) + '. ' + detail + (n === count(target) ? ' Следующий клик — следующий слайд.' : ' Следующий клик — следующий пункт.');
    }
    var current = n < 4 ? c.items[n - 1].title + ' — ' + c.items[n - 1].detail : c.closing;
    var next = n < 3 ? c.items[n].title : n === 3 && c.closing ? c.closing : 'следующий слайд';
    return 'Шаг ' + n + '/4. Сейчас: ' + current + '. Следующий клик: ' + next + '.';
  }
  function snapshot(sl) {
    var target = scene(sl); return target ? { step: Number(target.dataset.step), focus: Number(target.dataset.focus) } : null;
  }
  function restoreStep(sl, saved) {
    var target = scene(sl); if (!target || !saved) return;
    var api = controller(target);
    if (target.matches('.s3-spotlight') && saved.focus) api.setStep(target, saved.focus);
    api.setStep(target, saved.step);
  }
  function prepare(from, to, dir) {
    cancel();
    document.getElementById('stage').classList.toggle('opening-active', !!to._s.opening);
    to.classList.toggle('op-return', dir < 0);
    var key = from && from !== to && from._s.opening && to._s.opening && dir > 0;
    var source = key && from.querySelector('[data-op-share]');
    var target = source && source.dataset.opShare === 'plus' && to.querySelector('[data-op-share="plus"]');
    return !reduced.matches && target ? { source: source, target: target, rect: source.getBoundingClientRect() } : null;
  }
  function play(bridge) {
    if (!bridge) return;
    var a = bridge.rect, b = bridge.target.getBoundingClientRect();
    if (!a.width || !b.width) return;
    var copy = bridge.source.cloneNode(true);
    copy.removeAttribute('data-op-share'); copy.className.baseVal !== undefined ? copy.setAttribute('class', 'op-shared-flight') : copy.className = 'op-shared-flight';
    var isPlus = bridge.source.dataset.opShare === 'plus';
    copy.style.cssText = 'position:fixed;z-index:40;pointer-events:none;margin:0;display:block;color:#FDD506;background:' + (isPlus ? 'none' : '#FDD506') + ';left:' + a.left + 'px;top:' + a.top + 'px;width:' + a.width + 'px;height:' + a.height + 'px;transform-origin:0 0;';
    document.body.appendChild(copy);
    bridge.source.style.visibility = bridge.target.style.visibility = 'hidden';
    var done = function () { bridge.source.style.visibility = bridge.target.style.visibility = ''; copy.remove(); };
    restore.push(done);
    var animation = copy.animate([{ transform: 'translate(0,0) scale(1,1)' }, { transform: 'translate(' + (b.left - a.left) + 'px,' + (b.top - a.top) + 'px) scale(' + b.width / a.width + ',' + b.height / a.height + ')' }], { duration: 780, easing: 'cubic-bezier(.22,.8,.2,1)', fill: 'both' });
    running.push(animation); animation.onfinish = done;
  }
  window.Opening = { render: render, prepare: prepare, play: play, reduced: reduced, enter: enter, step: step, cue: cue, snapshot: snapshot, restoreStep: restoreStep };
})();
