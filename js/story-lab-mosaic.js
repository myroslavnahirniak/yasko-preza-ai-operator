/* Isolated concept preview: memories accumulate into one photographic mosaic. */
(function () {
  'use strict';
  var host, root, header, title, body, cards, intro, previous = -1;
  var keys = ['agency', 'team', 'office', 'car', 'paris', 'bali', 'newyork'];
  var layouts = {
    1: {agency:[6,35,57,53],team:[65,35,29,53]},
    2: {agency:[6,35,23,25],team:[6,62,23,26],office:[31,35,63,53]},
    3: {agency:[6,35,23,25],team:[6,62,23,26],office:[31,35,63,53]},
    4: {agency:[60,35,34,18],team:[60,55,34,18],office:[60,75,34,18],car:[6,35,52,58]},
    5: {agency:[48,35,22,19],team:[72,35,22,19],office:[48,56,46,16],car:[48,74,46,16],paris:[6,35,40,55]},
    6: {agency:[74,35,20,12],team:[74,49,20,12],office:[74,63,20,12],car:[74,77,20,13],paris:[48,35,24,55],bali:[6,35,40,55]},
    7: {agency:[71,66,10.5,11],team:[83.5,66,10.5,11],office:[71,79,10.5,11],car:[83.5,79,10.5,11],paris:[48,35,21,55],bali:[71,35,23,29],newyork:[6,35,40,55]},
    8: {agency:[6,32,25,24],team:[33,32,26,24],office:[61,32,33,24],car:[6,58,38,34],paris:[46,58,23,34],bali:[71,58,23,16],newyork:[71,76,23,16]}
  };
  var focus = {1:['agency','team'],2:['office'],3:['office'],4:['car'],5:['paris'],6:['bali'],7:['newyork'],8:keys};
  function mount(target) {
    host = target;
    host.innerHTML = '<div class="mosaic-lab"><div class="mosaic-intro">' + window.StoryLab.intro() + '</div><header class="mosaic-header"><h1 class="lab-title"></h1><p class="lab-body"></p></header><div class="mosaic-canvas"></div></div>';
    root = host.firstElementChild;
    intro = root.querySelector('.mosaic-intro');
    header = root.querySelector('.mosaic-header');
    title = header.querySelector('h1');
    body = header.querySelector('p');
    var canvas = root.querySelector('.mosaic-canvas');
    cards = {};
    keys.forEach(function (key) {
      var card = document.createElement('div');
      card.className = 'mosaic-card mosaic-card-' + key;
      card.style.cssText = 'left:110cqw;top:100cqw;width:24cqw;height:24cqw;opacity:0';
      card.innerHTML = key === 'office' ? window.StoryLab.photo('officeBefore', 'mosaic-office-before') + window.StoryLab.photo('officeAfter', 'mosaic-office-after') : window.StoryLab.photo(key);
      canvas.appendChild(card);
      cards[key] = card;
    });
    previous = -1;
  }
  function update(step, options) {
    if (!root) return;
    var animate = !options || options.animate !== false;
    root.classList.toggle('mosaic-no-motion', !animate);
    root.classList.toggle('mosaic-is-intro', step === 0);
    root.classList.toggle('mosaic-is-final', step === 8);
    root.classList.toggle('mosaic-office-finished', step >= 3);
    intro.setAttribute('aria-hidden', step !== 0 ? 'true' : 'false');
    header.setAttribute('aria-hidden', step === 0 ? 'true' : 'false');
    var content = window.StoryLab.steps[step];
    title.innerHTML = content.title;
    body.textContent = content.body || '';
    if (animate && previous !== step && typeof header.animate === 'function' && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      header.animate([{opacity:0, transform:'translateY(12px)'},{opacity:1, transform:'translateY(0)'}], {duration:420, easing:'cubic-bezier(.2,.7,.2,1)'});
    }
    var layout = layouts[step] || {}, active = focus[step] || [];
    keys.forEach(function (key) {
      var card = cards[key], box = layout[key];
      card.classList.toggle('mosaic-focused', active.indexOf(key) !== -1);
      card.setAttribute('aria-hidden', box ? 'false' : 'true');
      card.style.opacity = box ? '1' : '0';
      if (box) {
        card.style.left = box[0] + 'cqw';
        card.style.top = box[1] + 'cqw';
        card.style.width = box[2] + 'cqw';
        card.style.height = box[3] + 'cqw';
      } else if (step === 0) {
        card.style.left = '110cqw';
        card.style.top = '100cqw';
      } else {
        card.style.left = '108cqw';
      }
    });
    previous = step;
  }
  window.StoryLab.register('mosaic', {mount:mount, update:update});
}());
