/* Покроковий показ для важких текстових слайдів блоку 79–128 (Мирослав, 12.09):
   клік = наступний пункт; поточний яскравий, минулі приглушені, майбутні приховані;
   останній крок показує висновок і всі пункти; скетч у стійці міняється з кроком. */
(function(){
  'use strict';
  function count(scene){ return scene.dataset.auto?1:(Number(scene.dataset.steps)||1); }
  function setStep(scene,n){
    if(scene.dataset.waveSrc && window.WaveCinema){window.WaveCinema.setStep(scene,n);return;}
    var host=scene.closest('.slide')||scene;
    if(scene.dataset.auto){ scene.dataset.step='1'; scene.classList.add('is-final','is-auto'); var i=0; scene.querySelectorAll('[data-step]').forEach(function(el){ el.classList.remove('is-future','is-past'); el.classList.add('is-shown'); el.style.setProperty('--ag-i',String(i++)); el.removeAttribute('aria-hidden'); }); counts(host); return; }
    n=Math.max(1,Math.min(count(scene),Number(n)||1));
    scene.dataset.step=String(n);
    if(scene.dataset.orbit){
      var final=n===count(scene);
      scene.classList.toggle('is-final',final);
      scene.querySelectorAll('[data-step]').forEach(function(el){
        var k=el.dataset.step==='final'?count(scene):Number(el.dataset.step);
        el.classList.toggle('is-current',k===n);
        el.classList.remove('is-future','is-past');
        el.classList.add('is-shown');
        el.removeAttribute('aria-hidden');
      });
      scene.querySelectorAll('[data-orbit-nav]').forEach(function(button){button.setAttribute('aria-pressed',String(Number(button.dataset.orbitNav)===n));});
      if(!scene._orbitBound){
        scene._orbitBound=true;
        scene.addEventListener('click',function(e){var button=e.target.closest('[data-orbit-nav]');if(button){e.stopPropagation();setStep(scene,Number(button.dataset.orbitNav));}});
        scene.addEventListener('keydown',function(e){
          var button=e.target.closest('[data-orbit-nav]');
          if(!button)return;
          if(e.key==='Enter'||e.key===' ')e.stopPropagation();
          else if(/^(Arrow|Page|Home$|End$)/.test(e.key))button.blur();
        });
      }
      return;
    }
    if(scene.dataset.carousel){
      scene.querySelectorAll('[data-card-nav]').forEach(function(nav){
        nav.classList.toggle('is-current',Number(nav.dataset.cardNav)===n);
        nav.classList.toggle('is-done',Number(nav.dataset.cardNav)<n);
      });
      scene.querySelectorAll('.ag-depth-card').forEach(function(card){
        var k=Number(card.dataset.step),active=k===n;
        var offset=n===4?k-2:(k-n+3)%3;
        if(n!==4 && offset===2) offset=-1;
        card.style.setProperty('--card-x',(offset*24)+'cqw');
        card.style.setProperty('--card-y',(n===4?35:active?2:5)+'cqh');
        card.style.setProperty('--card-scale',n===4?'.28':active?'1':'.62');
        card.style.setProperty('--card-turn',(n===4?0:-offset*19)+'deg');
        card.style.zIndex=active?'4':n===4?'3':'1';
        card.classList.toggle('is-current',active);
        var v=card.querySelector('video');
        if(v){v.pause();if(active&&!reduced){
          if(v.dataset.src){v.src=v.dataset.src;delete v.dataset.src;}
          if(v.dataset.poster){v.poster=v.dataset.poster;delete v.dataset.poster;}
          v.currentTime=0;v.muted=true;v.play().catch(function(){});
        }}
      });
      scene.querySelector('.ag-cards-result').setAttribute('aria-hidden',String(n!==4));
      host.classList.toggle('ag-cards-finale',n===4);
      return;
    }
    if(scene.dataset.exclusive){
      scene.querySelectorAll('.ag-reframe-scene').forEach(function(panel){
        var active=Number(panel.dataset.step)===n;
        panel.hidden=!active; panel.setAttribute('aria-hidden',String(!active));
        panel.classList.toggle('is-current',active);
        var video=panel.querySelector('video');
        if(video){
          video.pause();
          if(active && !reduced){
            if(video.dataset.src){video.src=video.dataset.src;delete video.dataset.src;}
            if(video.dataset.poster){video.poster=video.dataset.poster;delete video.dataset.poster;}
            video.currentTime=0;video.muted=true;video.play().catch(function(){});
          }
        }
      });
      host.classList.toggle('ag-reframe-finale',n===count(scene));
      return;
    }
    var total=count(scene), isFinal=n===total && scene.dataset.final==='conclusion';
    scene.classList.toggle('is-final',isFinal);
    scene.querySelectorAll('[data-step]').forEach(function(el){
      var raw=el.dataset.step, k=raw==='final'?total:Number(raw);
      var cur=k===n, past=k<n, future=k>n;
      if(raw==='final'&&!isFinal){ cur=false; past=false; future=true; }
      el.classList.toggle('is-current',cur); el.classList.toggle('is-past',past&&!isFinal); el.classList.toggle('is-future',future);
      el.classList.toggle('is-shown',!future);
      if(el.tagName!=='IMG') el.setAttribute('aria-hidden',String(future));
    });
    var stage=host.querySelector('.ag-sketch-stage,.ag-bg-stage');
    if(stage){ var imgs=stage.querySelectorAll('img[data-step]'), shown=null;
      imgs.forEach(function(im){ var raw=im.dataset.step, k=raw==='final'?total:Number(raw); if(k===n) shown=im; });
      if(!shown&&imgs.length){ imgs.forEach(function(im){ var k=im.dataset.step==='final'?total:Number(im.dataset.step); if(k<=n) shown=im; }); }
      imgs.forEach(function(im){ im.classList.toggle('is-current',im===shown); });
      stage.classList.toggle('is-dim',isFinal&&scene.dataset.finalSketch!=='keep');
    }
  }
  var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function fmt(v){ return '$'+String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g,'.'); }
  function counts(host){
    host.querySelectorAll('.ag-count[data-to]').forEach(function(el){
      var from=Number(el.dataset.from||0), to=Number(el.dataset.to), dur=Number(el.dataset.dur||1600), delay=Number(el.dataset.delay||500);
      if(el._raf) cancelAnimationFrame(el._raf);
      if(reduced){ el.textContent=fmt(to); return; }
      el.textContent=fmt(from); var t0=null;
      function step(ts){ if(!t0){ t0=ts; } var k=Math.max(0,Math.min(1,(ts-t0-delay)/dur)); var e=1-Math.pow(1-k,3); el.textContent=fmt(from+(to-from)*e); if(k<1) el._raf=requestAnimationFrame(step); }
      el._raf=requestAnimationFrame(step);
    });
  }
  function cue(scene){
    if(scene.dataset.waveSrc)return scene.dataset.step==='2'?'Видео. P — пауза, Esc или стрелка влево — вернуть текст. Стрелка вправо — следующий слайд.':'Нажмите на превью или стрелку вправо — развернуть и запустить видео.';
    if(scene.dataset.auto) return '';
    var n=Number(scene.dataset.step||1), total=count(scene);
    var el=scene.querySelector('[data-step="'+n+'"], [data-step="final"].is-current');
    var txt=el?el.innerText.replace(/\s+/g,' ').trim().slice(0,90):'';
    return 'Шаг '+n+'/'+total+'. '+txt+(n<total?' Следующий клик — следующий пункт.':' Следующий клик — следующий слайд.');
  }
  window.AgentSteps={setStep:setStep,stepCount:count,cue:cue};
})();
