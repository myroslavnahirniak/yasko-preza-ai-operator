/* 12.10 · пакети агентів (.pk): клік по вкладці — інший агент; відео грає лише в активній панелі й лише на активному слайді.
   Дека гортає кліком по документу, тож клік по вкладці перехоплюємо на window (capture). */
(function(){
  function sync(sl){var on=sl.classList.contains('on');sl.querySelectorAll('.pk-ag').forEach(function(p){var v=p.querySelector('video');if(!v)return;if(on&&p.classList.contains('on')){if(v.preload==='none')v.preload='auto';v.muted=true;var r=v.play();if(r&&r.catch)r.catch(function(){});}else if(!v.paused)v.pause();});}
  function pick(pk,i){pk.querySelectorAll('.pk-tab').forEach(function(b){b.classList.toggle('on',+b.dataset.i===i)});pk.querySelectorAll('.pk-ag').forEach(function(p){p.classList.toggle('on',+p.dataset.i===i)});var sl=pk.closest('.slide');if(sl)sync(sl);}
  window.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('.pk-tab');if(!t)return;e.stopPropagation();e.preventDefault();pick(t.closest('.pk'),+t.dataset.i);},true);
  var seen=new WeakSet();
  function arm(){document.querySelectorAll('.slide').forEach(function(sl){if(seen.has(sl)||!sl.querySelector('.pk'))return;seen.add(sl);new MutationObserver(function(){sync(sl)}).observe(sl,{attributes:true,attributeFilter:['class']});sync(sl);});}
  arm(); setInterval(arm,1500);
}());
