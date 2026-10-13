/* Independent storytelling exploration 03 — a continuous, presenter-controlled route. */
(function () {
  'use strict';
  var root, world, title, body, intro, progress, overview, previous = -1;
  var keys = ['agency', 'officeBefore', 'officeAfter', 'car', 'paris', 'bali', 'newyork'];
  var chapters = ['Агентство', 'Начало', 'Команда', 'Первая машина', 'Париж', 'Бали', 'Нью-Йорк'];
  var positions = keys.map(function (_, i) { return 50 + i * 78; });
  function path() {
    var d = 'M -300 850';
    positions.forEach(function (x, i) {
      var previousX = i ? positions[i - 1] * 10 : -300;
      d += ' C ' + (previousX + 270) + ' 850 ' + (x * 10 - 240) + ' 885 ' + x * 10 + ' 850';
    });
    return d + ' C 5550 820 5780 850 6000 850';
  }
  window.StoryLab.register('road', {
    mount: function (host) {
      root = host;
      root.classList.add('road-demo');
      root.innerHTML = '<div class="road-intro">' + window.StoryLab.intro() + '</div>' +
        '<div class="road-scene"><div class="road-copy"><h1 class="lab-title"></h1><p class="lab-body"></p></div>' +
        '<div class="road-window"><div class="road-world"><svg class="road-track" viewBox="0 0 6000 1000" aria-hidden="true"><path class="road-track-base" d="' + path() + '"/><path class="road-track-progress" pathLength="1000" d="' + path() + '"/></svg>' +
        keys.map(function (key, i) {
          return '<div class="road-episode" data-chapter="' + i + '" style="left:' + (positions[i] - 35) + 'cqw">' + window.StoryLab.photo(key, 'road-art') + '</div>' +
            '<button class="road-node" data-step="' + (i + 1) + '" style="left:' + positions[i] + 'cqw" aria-label="' + chapters[i] + '"><span class="road-node-dot"></span><span class="road-node-label">' + chapters[i] + '</span></button>';
        }).join('') + '</div></div>' +
        '<div class="road-overview"><svg class="road-overview-path" viewBox="0 0 1000 1000" aria-hidden="true"><path d="M240 380 H750 Q850 380 850 520 T750 640 H240"/></svg>' +
        ['agency', 'officeAfter', 'car', 'paris'].map(function (key, i) {
          return '<button class="road-memory road-memory-' + i + '" data-step="' + [1,3,4,5][i] + '">' + window.StoryLab.photo(key, 'road-memory-photo') + '<span>' + ['Агентство', 'Команда', 'Первая машина', 'Путешествия'][i] + '</span></button>';
        }).join('') + '</div></div>';
      world = root.querySelector('.road-world');
      title = root.querySelector('.road-copy .lab-title');
      body = root.querySelector('.road-copy .lab-body');
      intro = root.querySelector('.road-intro');
      progress = root.querySelector('.road-track-progress');
      overview = root.querySelector('.road-overview');
      root.querySelectorAll('[data-step]').forEach(function (node) {
        node.addEventListener('click', function (event) { event.stopPropagation(); window.StoryLab.goStep(Number(node.dataset.step)); });
      });
    },
    update: function (step, options) {
      if (!root) return;
      var animate = !(options && options.animate === false);
      root.classList.toggle('road-no-motion', !animate);
      root.classList.toggle('road-at-intro', step === 0);
      root.classList.toggle('road-at-final', step === 8);
      intro.setAttribute('aria-hidden', String(step !== 0));
      overview.setAttribute('aria-hidden', String(step !== 8));
      var data = window.StoryLab.steps[step];
      title.innerHTML = data.title;
      body.textContent = data.body || '';
      var index = Math.max(0, Math.min(6, step - 1));
      world.style.transform = 'translate3d(' + (-index * 78) + 'cqw,0,0)';
      progress.style.strokeDashoffset = String(1000 * (1 - (positions[index] + 30) / 600));
      root.querySelectorAll('.road-episode').forEach(function (el, i) {
        el.classList.toggle('is-current', i === index);
        el.classList.toggle('is-neighbor', Math.abs(i - index) === 1);
      });
      root.querySelectorAll('.road-node').forEach(function (el, i) {
        el.classList.toggle('is-current', i === index);
        el.classList.toggle('is-past', i < index);
        if (i === index) el.setAttribute('aria-current', 'step'); else el.removeAttribute('aria-current');
      });
      if (animate && previous !== step && step > 0 && step < 8) {
        root.querySelector('.road-copy').animate([{ opacity: .2, transform: 'translateY(1.2cqw)' }, { opacity: 1, transform: 'translateY(0)' }], { duration: 380, easing: 'ease-out' });
      }
      previous = step;
    }
  });
})();
