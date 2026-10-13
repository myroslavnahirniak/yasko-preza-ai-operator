/* User-controlled preview → full-slide film, scoped to the approved wave slide. */
(function(){
  'use strict';
  var reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
  function resetVideo(scene){
    clearTimeout(scene._waveStart);
    scene.querySelectorAll('video').forEach(function(v){v.pause();v.removeAttribute('src');v.load();v.remove();});
  }
  function play(scene){
    var host=scene.closest('.slide');
    if(!host.isConnected||!host.classList.contains('on')||scene.dataset.step!=='2')return;
    var box=scene.querySelector('.wc-player'),launch=scene.querySelector('.wc-launch');
    var video=document.createElement('video');
    video.src=scene.dataset.waveSrc;video.poster=scene.dataset.wavePoster;
    video.playsInline=true;video.preload='auto';video.muted=false;
    video.setAttribute('aria-label','Волна — видео');
    video.addEventListener('playing',function(){scene.classList.add('wc-playing');});
    video.addEventListener('click',function(e){
      e.stopPropagation();
      if(video.ended)video.currentTime=0;
      if(video.paused)video.play().catch(function(){});else video.pause();
    });
    box.appendChild(video);
    function retry(){
      launch.disabled=false;launch.tabIndex=0;launch.removeAttribute('aria-hidden');
      scene.classList.add('wc-retry');
      launch.querySelector('.wc-play-label').textContent='Запустить видео';
    }
    video.addEventListener('error',retry);
    video.play().catch(function(e){if(e.name!=='AbortError'&&scene.dataset.step==='2')retry();});
  }
  function setStep(scene,n){
    n=Math.max(1,Math.min(2,Number(n)||1));
    var host=scene.closest('.slide'),launch=scene.querySelector('.wc-launch');
    if(!scene._waveBound){
      scene._waveBound=true;
      launch.addEventListener('click',function(e){
        e.stopPropagation();
        if(scene.classList.contains('wc-retry')){
          var v=scene.querySelector('video');
          scene.classList.remove('wc-retry');launch.disabled=true;launch.tabIndex=-1;launch.setAttribute('aria-hidden','true');
          if(v)v.play().catch(function(){scene.classList.add('wc-retry');launch.disabled=false;launch.tabIndex=0;launch.removeAttribute('aria-hidden');});
        }else setStep(scene,2);
        host.dispatchEvent(new CustomEvent('realityroutechange',{bubbles:true}));
      });
      launch.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' ')e.stopPropagation();});
    }
    resetVideo(scene);
    scene.dataset.step=String(n);scene.classList.remove('wc-playing','wc-retry');
    host.classList.toggle('wc-expanded',n===2);
    host.querySelector('.fd-header').setAttribute('aria-hidden',String(n===2));
    scene.querySelector('.wc-caption').setAttribute('aria-hidden',String(n===2));
    launch.disabled=n===2;launch.tabIndex=n===2?-1:0;
    launch.setAttribute('aria-hidden',String(n===2));
    launch.querySelector('.wc-play-label').textContent='Смотреть видео';
    if(n===2)scene._waveStart=setTimeout(function(){play(scene);},reduced.matches?0:720);
  }
  document.addEventListener('keydown',function(e){
    if(e.key!=='Escape')return;
    var scene=document.querySelector('.slide.on .wave-cinema[data-step="2"]');
    if(scene){e.preventDefault();e.stopImmediatePropagation();setStep(scene,1);}
  },true);
  window.WaveCinema={setStep:setStep,dispose:function(root){root.querySelectorAll('.wave-cinema[data-wave-src]').forEach(resetVideo);}};
})();
