/* Slides 21–24: finite focus changes, fixed positions and native SVG. */
(function () {
  'use strict';

  function esc(value) {
    return String(value || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  var drawings = {
    quiet: '<rect x="25" y="13" width="40" height="67" rx="5"/><path d="M40 21h10M40 72h10M14 20l66 66"/><path d="M15 41v18M8 46v8M76 34v18M83 39v8"/>',
    watch: '<rect x="11" y="16" width="78" height="53" rx="5"/><path d="M36 82h28M50 69v13"/><path d="M28 42s9-12 22-12 22 12 22 12-9 12-22 12-22-12-22-12Z"/><circle cx="50" cy="42" r="6"/>',
    door: '<path d="M22 86V14h54v72M14 86h70M30 86V22l37-7v71"/><circle cx="58" cy="52" r="2"/>',
    tv: '<rect x="11" y="29" width="78" height="51" rx="7"/><path d="M34 13l16 16 16-16M27 88h46"/><path d="m43 43 19 12-19 12Z"/>',
    play: '<rect x="9" y="22" width="82" height="56" rx="15"/><path d="m42 36 22 14-22 14Z"/>',
    clock: '<circle cx="50" cy="50" r="37"/><path d="M50 27v25l16 10"/><path d="M50 13v5M87 50h-5M50 87v-5M13 50h5"/>',
    stop: '<path d="m34 10 32 0 24 24v32L66 90H34L10 66V34Z"/><path d="M28 50h44"/>',
    site: '<rect x="10" y="15" width="80" height="69" rx="4"/><path d="M10 32h80M19 24h1M26 24h1M33 24h1M20 43h29v29H20ZM58 46h22M58 57h16M58 68h20"/>',
    listing: '<rect x="19" y="12" width="62" height="76" rx="4"/><path d="M31 26h38v23H31ZM31 62h38M31 73h25"/><path d="m40 42 9-9 8 7 6-4"/>',
    ads: '<path d="m15 42 58-21v58L15 58ZM73 36l14-4v36l-14-4M25 62l7 22h14l-8-27M12 42v16"/>',
    voice: '<rect x="38" y="13" width="24" height="47" rx="12"/><path d="M25 46v4a25 25 0 0 0 50 0v-4M50 75v13M37 88h26M13 35v23M87 35v23"/>',
    seller: '<rect x="20" y="24" width="60" height="47" rx="10"/><path d="M50 12v12M39 84h22M50 71v13M9 38v18M91 38v18M38 57c7 5 17 5 24 0"/><circle cx="38" cy="43" r="2"/><circle cx="62" cy="43" r="2"/>'
  };

  function icon(name, extra) {
    return '<svg class="cf-icon ' + (extra || '') + '" viewBox="0 0 100 100" fill="none" aria-hidden="true">' + (drawings[name] || drawings.site) + '</svg>';
  }

  function heading(c) {
    return '<h1 class="cf-heading split-done">' + (c.lines || []).map(function (line) {
      return '<span>' + line + '</span>';
    }).join('') + '</h1>';
  }

  function progress(count) {
    var out = '<div class="cf-progress" aria-hidden="true">';
    for (var i = 1; i <= count; i++) out += '<i data-progress="' + i + '"' + (i === 1 ? ' class="is-current"' : '') + '></i>';
    return out + '</div>';
  }

  function rail(items, className) {
    return '<div class="cf-rail ' + className + '" aria-hidden="true">' + items.map(function (item, i) {
      return '<div class="cf-symbol' + (i === 0 ? ' is-current' : '') + '" data-symbol="' + (i + 1) + '">' + (item.sketch ? '<img class="cf-sketch" data-src="' + esc(item.sketch) + '" alt="">' : icon(item.icon)) + '</div>';
    }).join('') + '</div>';
  }

  function panels(items, className, pill) {
    var pad = function (n) { return (n < 10 ? '0' : '') + n; };
    return '<div class="cf-panels ' + className + '">' + items.map(function (item, i) {
      /* 03.10 pill: іконка кроку і лічильник у капсулі з назвою (видно лише там, де CSS їх вмикає — s8 варіант A) */
      var title = pill ? '<span class="cf-pill-ic">' + icon(item.icon) + '</span><span class="cf-pill-t">' + esc(item.title) + '</span><small class="cf-pill-n">' + pad(i + 1) + ' / ' + pad(items.length) + '</small>' : esc(item.title);
      return '<div class="cf-panel' + (i === 0 ? ' is-current' : '') + '" data-panel="' + (i + 1) + '" data-cue="' + esc(item.title) + '" aria-hidden="' + (i === 0 ? 'false' : 'true') + '"><h2>' + title + '</h2>' + (item.body ? '<p>' + esc(item.body) + '</p>' : '') + '</div>';
    }).join('') + '</div>';
  }

  function rules(c) {
    return heading(c) + rail(c.items, 'cf-rules-rail') + panels(c.items, 'cf-rules-panels') +
      '<div class="cf-guarantee" data-panel="4" data-cue="' + esc(c.guarantee.lead) + '" aria-hidden="true"><p class="cf-guarantee-lead">' + esc(c.guarantee.lead) + '</p><p class="cf-guarantee-body">' + (c.guarantee.bodyLines ? c.guarantee.bodyLines.map(function(line){return '<span>' + esc(line) + '</span>';}).join(' ') : esc(c.guarantee.body)) + '</p></div>' + progress(4);
  }

  function attention(c) {
    if (c.image) return '<div class="cf-attention-photo"><img data-src="' + esc(c.image) + '" alt="" aria-hidden="true"></div>' +
      '<div class="cf-attention-copy">' + (c.eyebrow ? '<p class="cf-eyebrow">' + esc(c.eyebrow) + '</p>' : '') + heading(c) + '<p class="cf-support">' + esc(c.body) + '</p></div>';
    return heading(c) + '<div class="cf-attention-visual" aria-hidden="true"><svg class="cf-connection" viewBox="0 0 100 44" fill="none"><path d="M22 22H78"/></svg><div class="cf-distraction cf-tv">' + icon('tv') + '</div><div class="cf-time">' + icon('clock') + '</div><div class="cf-distraction cf-play">' + icon('play') + '</div></div><p class="cf-support">' + esc(c.body) + '</p>';
  }

  function pause(c) {
    return (c.image ? '<div class="cf-pause-photo"><img data-src="' + esc(c.image) + '" alt="" aria-hidden="true"></div>' : '') + heading(c);
  }

  function live(c) {
    return heading(c) + '<p class="cf-live-intro">' + esc(c.body) + '</p>' + rail(c.items, 'cf-live-rail') + panels(c.items, 'cf-live-panels', true) + progress(c.items.length);
  }

  function servicePrice(c) {
    var labels = (c.serviceLabels || []).map(function(label) {
      return '<div class="cf-service-label" style="left:' + Number(label.x) + 'cqw;width:' + Number(label.width) + 'cqw">' + label.lines.map(function(line){return '<span>' + esc(line) + '</span>';}).join('') + '</div>';
    }).join('');
    return '<div class="cf-prize-photo"><img data-src="' + esc(c.image) + '" alt="' + esc(c.imageAlt || '') + '"></div><div class="cf-price-copy">' + heading(c) + '<p class="cf-service-price">' + esc(c.price) + '</p><p class="cf-price-support">' + c.bodyLines.map(function(line){return '<span>'+esc(line)+'</span>';}).join(' ') + '</p></div>' + (labels ? '<div class="cf-service-labels">' + labels + '</div>' : '');
  }

  function prizes(c) {
    return '<div class="cf-prize-photo"><img data-src="' + esc(c.image) + '" alt="" aria-hidden="true"></div><div class="cf-prize-copy"><p class="cf-prize-eyebrow">' + esc(c.eyebrow) + '</p>' + heading(c) + '</div>';
  }

  function render(c) {
    var variants = { rules: rules, attention: attention, pause: pause, live: live, prizes: prizes, 'service-price': servicePrice };
    var variant = variants[c.variant] ? c.variant : 'attention';
    var count = variant === 'rules' ? 4 : (variant === 'live' ? c.items.length : 1);
    return '<div class="chapter-format cf-' + variant + (variant === 'attention' && c.image ? ' cf-attention-cinematic' : '') + '" data-step="1" data-count="' + count + '">' + variants[variant](c) + '</div>';
  }

  function stepCount(scene) {
    return scene ? Number(scene.dataset.count || 1) : 1;
  }

  function setStep(scene, n) {
    if (!scene) return;
    n = Math.max(1, Math.min(stepCount(scene), Number(n) || 1));
    scene.dataset.step = String(n);
    scene.querySelectorAll('[data-symbol]').forEach(function (item) {
      item.classList.toggle('is-current', Number(item.dataset.symbol) === n);
    });
    scene.querySelectorAll('[data-panel]').forEach(function (item) {
      var active = Number(item.dataset.panel) === n;
      item.classList.toggle('is-current', active);
      item.setAttribute('aria-hidden', active ? 'false' : 'true');
    });
    scene.querySelectorAll('[data-progress]').forEach(function (item) {
      item.classList.toggle('is-current', Number(item.dataset.progress) === n);
      item.classList.toggle('is-complete', Number(item.dataset.progress) < n);
    });
  }

  function cue(scene) {
    if (!scene || stepCount(scene) === 1) return '';
    var current = Number(scene.dataset.step || 1);
    var now = scene.querySelector('[data-panel="' + current + '"]');
    var next = scene.querySelector('[data-panel="' + (current + 1) + '"]');
    return 'Шаг ' + current + '/' + stepCount(scene) + '. Сейчас: ' + (now ? now.dataset.cue : '') + '. Следующий клик: ' + (next ? next.dataset.cue : 'следующий слайд') + '.';
  }

  window.ChapterFormat = { render: render, setStep: setStep, stepCount: stepCount, cue: cue };
})();
