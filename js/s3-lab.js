(function () {
  'use strict';
  var variants = {
    spotlight: { title: 'Предмет у фокусі', description: 'Порядок завжди той самий: заробіток, продаж, агенти. Клік збільшує предмет на його місці. У фіналі головним стає прохання Влада.' }
  };
  var params = new URLSearchParams(location.search);
  var variant = 'spotlight';
  var step = Math.min(4, Math.max(1, Number(params.get('step')) || 1));
  var canvas = document.getElementById('canvas'), timer = 0, raf = 0, playing = false;
  var source = window.S.find(function (s) { return s.opening && s.opening.scene === 'reveal'; });
  var c = source.opening;
  function stop() { clearTimeout(timer); timer = 0; playing = false; }
  function sync() {
    document.getElementById('variantTitle').textContent = variants[variant].title;
    document.getElementById('description').textContent = variants[variant].description;
    document.getElementById('stepLabel').textContent = step < 4 ? 'Елемент ' + step + ' із 3' : 'Завершальна репліка';
    document.getElementById('back').disabled = step === 1;
    document.getElementById('next').disabled = step === 4;
    document.getElementById('next').firstChild.textContent = step === 3 ? 'До прохання ' : step === 4 ? 'Фінал ' : 'Наступний елемент ';
    document.getElementById('play').setAttribute('aria-pressed', String(playing));
    document.querySelector('#play span').textContent = playing ? 'Пауза' : 'Автопоказ';
    canvas.setAttribute('aria-label', 'Слайд 3. ' + (step < 4 ? c.items[step - 1].title + ', ' + c.items[step - 1].detail + '. Натисніть для наступного кроку.' : c.closing + '. Завершальна репліка.'));
    params.set('variant', variant); params.set('step', step);
    history.replaceState(null, '', location.pathname + '?' + params.toString());
  }
  function render(entrance) {
    cancelAnimationFrame(raf);
    canvas.innerHTML = window.S3Variants[variant].render(c);
    var scene = canvas.firstElementChild;
    window.S3Variants[variant].setStep(scene, entrance ? 0 : step);
    if (entrance) { void scene.offsetWidth; raf = requestAnimationFrame(function () { window.S3Variants[variant].setStep(scene, step); }); }
    sync();
  }
  function setStep(n, manual) {
    cancelAnimationFrame(raf);
    if (manual) stop();
    step = Math.min(4, Math.max(1, n));
    window.S3Variants[variant].setStep(canvas.firstElementChild, step);
    if (step === 4) stop();
    sync();
  }
  function schedule() {
    if (!playing) return;
    timer = setTimeout(function () { setStep(step + 1, false); schedule(); }, 2600);
  }
  document.getElementById('next').onclick = function () { setStep(step + 1, true); };
  document.getElementById('back').onclick = function () { setStep(step - 1, true); };
  document.getElementById('all').onclick = function () { setStep(4, true); };
  document.getElementById('restart').onclick = function () { stop(); step = 1; render(true); };
  document.getElementById('play').onclick = function () {
    if (playing) { stop(); sync(); return; }
    stop(); step = 1; playing = true; render(true); schedule();
  };
  document.getElementById('fullscreen').onclick = function () { if (canvas.requestFullscreen) canvas.requestFullscreen().catch(function () {}); };
  canvas.onclick = function () { setStep(step + 1, true); };
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') { e.preventDefault(); setStep(step + 1, true); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); setStep(step - 1, true); }
    if (e.key === ' ' && !e.target.closest('button,a')) { e.preventDefault(); setStep(step + 1, true); }
    if (e.key === 'Home') { e.preventDefault(); setStep(1, true); }
    if (e.key === 'End') { e.preventDefault(); setStep(4, true); }
  });
  document.addEventListener('visibilitychange', function () { if (document.hidden) { stop(); sync(); } });
  render(step === 1);
})();
