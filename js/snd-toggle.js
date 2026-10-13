/* 13.10 · кнопка звуку на відео слайда (.snd-btn): вмикає / вимикає звук першого відео цього слайда.
   Дека гортає кліком по документу, тож клік перехоплюємо на window (capture). */
(function(){
  function upd(b,v){b.classList.toggle('off',!!v.muted);b.setAttribute('aria-label',v.muted?'Включить звук':'Выключить звук');}
  window.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.snd-btn');if(!b)return;e.stopPropagation();e.preventDefault();
    var sl=b.closest('.slide'),v=sl&&sl.querySelector('video');if(!v)return;v.muted=!v.muted;if(!v.muted&&v.paused){var r=v.play();if(r&&r.catch)r.catch(function(){});}upd(b,v);},true);
  setInterval(function(){document.querySelectorAll('.slide.on .snd-btn').forEach(function(b){var v=b.closest('.slide').querySelector('video');if(v)upd(b,v);});},700);
}());
