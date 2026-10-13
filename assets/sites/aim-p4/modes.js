/* 12.10 · режими подачі блоку пакета: ?m=a|b|c|d|e (див. modes.css) */
(function(){
  var pp=document.getElementById('pp'); if(!pp) return;
  var m=(new URLSearchParams(location.search).get('m')||'').toLowerCase(); if(!/^[a-f]$/.test(m)) return;
  if(m==='f'){pp.classList.add('mf');return;} // 13.10 F: поверх sq, свій fit не потрібен
  pp.classList.remove('sq'); pp.classList.add('m'+m);
  var BASE={a:820,b:860,c:900,d:800,e:900}[m];
  function fit(){pp.style.zoom=1;var h=pp.querySelector('.pult').offsetHeight||BASE;var k=Math.min(innerWidth/BASE,innerHeight/h);pp.style.zoom=k;pp.style.marginLeft=Math.max(0,(innerWidth/k-BASE)/2)+'px';}
  fit(); addEventListener('resize',fit); setTimeout(fit,300); setTimeout(fit,1200); window.__aimFit=fit;
  window.__aimBase=BASE;
  var pult=pp.querySelector('.pult'), keys=[].slice.call(pp.querySelectorAll('.pult__key')), caps=[].slice.call(pp.querySelectorAll('.pult__cap')), slides=[].slice.call(pp.querySelectorAll('.pult__slide'));
  var pid=(pult.id||'pult-01').replace('pult-','');
  function open(i){document.dispatchEvent(new CustomEvent('pult:open',{detail:{pult:pid,i:i}}));scrollTo(0,0);setTimeout(fit,60);}
  function cur(){return Math.max(0,keys.findIndex(function(k){return k.classList.contains('is-on')}));}
  if(m==='d'){
    var nav=document.createElement('div'); nav.className='md-nav';
    nav.innerHTML='<button type="button" class="md-p" aria-label="Предыдущий агент">‹</button><span class="md-dots">'+keys.map(function(_,i){return '<i data-i="'+i+'"></i>'}).join('')+'</span><span class="md-cur"></span><button type="button" class="md-n" aria-label="Следующий агент">›</button>';
    pult.appendChild(nav);
    function upd(){var c=cur();nav.querySelectorAll('.md-dots i').forEach(function(d,i){d.classList.toggle('on',i===c)});nav.querySelector('.md-cur').textContent=(c+1)+' / '+keys.length;}
    nav.addEventListener('click',function(e){var c=cur();if(e.target.closest('.md-p'))open((c-1+keys.length)%keys.length);else if(e.target.closest('.md-n'))open((c+1)%keys.length);else if(e.target.dataset&&e.target.dataset.i)open(+e.target.dataset.i);setTimeout(upd,30);});
    new MutationObserver(upd).observe(keys[0].parentNode,{attributes:true,subtree:true,attributeFilter:['class']}); upd();
    // заголовок кадру = номер і назва агента
  }
  if(m==='e'){
    pp.classList.add('ov');
    var grid=document.createElement('div'); grid.className='ov-grid'; grid.style.setProperty('--c',keys.length===2?2:(keys.length===4?2:3));
    grid.innerHTML=keys.map(function(k,i){
      var cap=caps[i]||{}, pane=slides[i]&&slides[i].querySelector('.pult__pane'), bg=pane?(pane.getAttribute('style')||'').match(/--bg:url\(([^)]+)\)/):null;
      var pr=cap.querySelector?cap.querySelector('.pult__price b'):null, earn=cap.querySelector?cap.querySelector('.pult__path--earn p'):null;
      return '<button type="button" class="ov-card" data-i="'+i+'"><span class="ov-img" style="background-image:url('+(bg?bg[1]:'')+')"></span><span class="ov-tx"><span class="ov-n">'+k.querySelector('.pult__num').textContent+'</span><span class="ov-nm">'+k.querySelector('.pult__nm').textContent+'</span>'+(pr?'<span class="ov-pr">'+pr.textContent+'</span>':'')+(earn?'<span class="ov-earn">'+earn.textContent+'</span>':'')+'</span></button>';
    }).join('');
    var back=document.createElement('button'); back.type='button'; back.className='ov-back'; back.textContent='← все агенты';
    pult.querySelector('.pult__head').after(grid); grid.after(back);
    grid.addEventListener('click',function(e){var c=e.target.closest('.ov-card');if(!c)return;pp.classList.remove('ov');open(+c.dataset.i);});
    back.addEventListener('click',function(){pp.classList.add('ov');setTimeout(fit,30);});
  }
})();
