/* ============================================================
   AI-Оператор · преза эфира · движок v5 «ЭФИР»
   Навигация: → / пробел / клик / PgDn — вперёд · ← / PgUp — назад
   F — полный экран · N — заметки · D — режиссёрская панель · E — полоса уровня
   W — 16:9 / квадрат · M — версия 60 мин · S — к следующему с пометкой · P — пауза видео
   цифры + Enter — прыжок к слайду · ? — подсказка
   URL: ?s=58 (слайд) · ?mvp (60 мин) · ?wide (16:9) · ?draft (панель) · ?clean (без HUD)
   ============================================================ */
(function(){
'use strict';
var S=window.S, ACTS=window.ACTS, DIR=window.DIR||{}, CTA_URL=window.CTA_URL||'#';
var stage=document.getElementById('stage'), layer=document.getElementById('slides');
var hud=document.getElementById('hud'), bar=document.getElementById('bar'), lvl=document.getElementById('level'),
    actEl=document.getElementById('act'), notesEl=document.getElementById('notes'), overlay=document.getElementById('ctaOverlay'),
    hintEl=document.getElementById('hint'), jumpEl=document.getElementById('jumpbuf');
var q=location.search;
var mvpMode=/[?&]mvp/.test(q);
var view=[], slides=[], i=0, ctaIdx=-1, outTimer=0;

/* палитра актов: [accent, accent2] */
/* бренд Влада — чёрно-жёлтый (правка 03.09: «не чёрно-зелёный»). Акцент один; акты различаются только второй краской aurora */
var Y='#FDD506';
var ACT_ACCENT=[
  [Y,'#FF9F1C'], /* 1 Открытие */
  [Y,'#FF6B3D'], /* 2 История — теплее */
  [Y,'#FFC94D'], /* 3 Главная мысль */
  [Y,'#F5F3EE'], /* 4 Секрет 1 — светлее */
  [Y,'#FF9F1C'], /* 5 Секрет 2 */
  [Y,'#FF6B3D'], /* 6 Секрет 3 */
  [Y,'#FFE27A'], /* 7 Предложение — золото */
  [Y,'#F5F3EE']  /* Финал */
];
var COLD=['#9DB0C6','#5B6B80'];

function esc(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;');}
function lazy(html){ /* assets/… → data-src, чтобы 305 слайдов не грузили всё сразу */
  return String(html||'').replace(/\s(src|poster)=(['"])(assets\/)/g,' data-$1=$2$3');
}
function isQuote(s){ return /^(Узнаёте себя|Скептик|И я так же)/i.test(s.k||''); }

/* ---------- сборка ---------- */
function render(s,idx){
  if(s.foundation && s.foundation.importedHTML && window.Secret2Import) return window.Secret2Import.render(s,idx);
  if(s.lifeStory && window.LifeStory) return window.LifeStory.render(s,idx);
  if(s.routeRoadmap && window.RealityRoute) return window.RealityRoute.render(s,idx);
  if(s.foundation && window.Foundation) return window.Foundation.render(s,idx);
  if(s.opening && window.Opening) return window.Opening.render(s,idx);
  var kind=s.kind||'text', cls=['slide'], h='';
  if(kind!=='text') cls.push(kind);
  if(isQuote(s)) cls.push('quote');
  if(s.fx) cls.push('fx-'+s.fx);
  if(s.theme==='light') cls.push('light');
  if(s.text==='full') cls.push('full');
  if(idx===0) cls.push('title');
  if(kind==='video' && s.src && /payments/.test(s.src)) cls.push('phone');
  var sec=document.createElement('section');
  if(s.lost) sec.setAttribute('data-lost','1');
  sec.dataset.lv=s.lv; sec.dataset.idx=idx;
  var FRAME=(s.layout==='frame')&&!!s.bg, SPLIT=!!s.bg&&!FRAME;
  if(FRAME){ cls.push('frame'); if(s.align==='center') cls.push('center'); if(s.baked) cls.push('baked'); h+="<img class='frameimg' data-src='"+s.bg+"' alt=''"+(s.bgpos?" style='object-position:"+s.bgpos+"'":"")+"><div class='ftext'>"; }
  if(SPLIT){
    cls.push('split'); if(s.bgside==='side'||kind==='meme') cls.push('side');
    h+="<div class='splitphoto'><img class='fill' data-src='"+s.bg+"' alt='' aria-hidden='true'><img class='main' data-src='"+s.bg+"' alt=''"+(s.bgpos?" style='object-position:"+s.bgpos+"'":"")+"></div><div class='splittext'>";
  }
  if(idx===0) h+="<div class='ring2'><i></i><i></i><i></i><i></i></div>";
  if(kind==='video'){
    h+="<video playsinline muted preload='none'"+(s.poster?" data-poster='"+s.poster+"'":"")+" data-src='"+s.src+"'></video>";
    h+="<div class='vscrim'></div><div class='vbeats'>";
    (s.beats||[]).forEach(function(b){ h+="<div class='vbeat' data-t='"+b[0]+"'>"+b[1]+"</div>"; });
    h+="</div><div class='vhint'>→ следующая мысль</div>";
  }
  if(kind==='meme'){
    h+="<div class='memetext'>"+(s.k?"<div class='kick'><i></i>"+s.k+"</div>":"")+(s.t?"<h1>"+s.t+"</h1>":"")+lazy(s.b||"")+"</div>";
    var round=/kruzhok/.test(s.img||'');
    h+="<div class='memefig"+(round?" round":"")+"'"+(s.ar?" style='--ar:"+s.ar+"'":"")+">";
    h+= /\.mp4$/.test(s.img) ? "<video data-src='"+s.img+"' autoplay loop muted playsinline></video>" : "<img data-src='"+s.img+"' alt=''>";
    (s.caps||[]).forEach(function(c){ h+="<span class='memecap' style='left:"+c[0]+"%;top:"+c[1]+"%;width:"+c[2]+"%'>"+c[3]+"</span>"; });
    if(s.bar) h+="<div class='memebar top'>"+s.bar+"</div>";
    if(s.bar2) h+="<div class='memebar bottom'>"+s.bar2+"</div>";
    if(s.src) h+="<span class='memesrc'>"+s.src+"</span>";
    h+="</div>";
  }
  if(s.k && kind!=='meme') h+="<div class='kick'><i></i>"+s.k+"</div>";
  if(s.t && kind!=='video' && kind!=='meme') h+="<h1>"+s.t+"</h1>";
  if(kind==='stack'){
    h+="<div class='stack'>";
    (s.rows||[]).forEach(function(r){ h+="<div class='row'><span>"+r[0]+"</span><span class='money'>$"+Number(r[1]).toLocaleString('en-US')+"</span></div>"; });
    h+="<div class='row total'><span>Итого ценность</span><span class='money stackTotal'>$0</span></div></div>";
  } else if(s.b && kind==='video') h+="<div class='vcap'>"+lazy(s.b)+"</div>";
  else if(s.b && kind!=='meme') h+=lazy(s.b);
  if(s.photos && s.photos.length){
    h+="<div class='pgrid n"+s.photos.length+(s.ptall?' tall':'')+"'>";
    s.photos.forEach(function(p){ h+="<figure><img data-src='"+p+"' alt=''></figure>"; });
    h+="</div>";
  }
  if(s.fx==='prizes') h+="<div class='prizes'>"+[1,2,3].map(function(n){return "<div class='cloche' style='--i:"+(n-1)+"'><u></u><b>Приз №"+n+"</b><i></i></div>";}).join('')+"</div>";
  if(s.fx==='g96'){ var g=''; for(var q=0;q<96;q++) g+="<i style='--i:"+q+"'></i>"; h+="<div class='g96'>"+g+"</div>"; }
  if(s.fx==='button') h+="<div class='onebtn'><i></i><span>Одна кнопка</span></div>";
  if(kind==='embed') h+="<div class='embedwrap'><iframe data-src='"+s.src+"' loading='lazy' title='"+esc(s.t)+"'></iframe><span class='embedhint'>листайте и нажимайте прямо здесь</span></div>";
  if(kind==='cta') h+="<a class='cta-btn' href='"+CTA_URL+"' target='_blank' rel='noopener'>"+(s.cta||"Бронь — $10")+"<span class='cic'>↗</span></a>";
  if(isQuote(s)) h+="<div class='plus'><b>+</b> в чат, если это про вас</div>";
  if(s.viz) h+="<div class='vizslot'>🖼 "+esc(s.viz)+"</div>";
  if(s.disc) h+="<div class='disc'>Результаты индивидуальны и не являются типичными</div>";
  if(SPLIT||FRAME) h+="</div>";
  if(s.st){ sec.classList.add('st-'+s.st[0]); sec.classList.add('has-st'); }
  sec.className+=cls.join(' ').replace(/^/,' ');
  sec.innerHTML=h; sec._s=s;
  [].forEach.call(sec.querySelectorAll('.tags span'),function(el,k){ el.style.setProperty('--i',k); });
  return sec;
}
var EMO={'💰':'coin','💸':'coin','🏷':'tag','🏷️':'tag','⚙️':'gear','⚙':'gear','🎓':'cap','📚':'book','🗂':'folder','🗂️':'folder','🪫':'battery','⏳':'hourglass','⚡':'bolt','📵':'phone','👀':'eye','🚪':'door','🔎':'eye','💬':'chat','🛠':'gear','🛠️':'gear','🎁':'spark','✦':'spark','🔬':'eye','🌐':'spark','🎬':'play','🎯':'tag','📎':'folder'};
function emojiToSvg(sec){
  [].forEach.call(sec.querySelectorAll('.g3 > i, .ch > u, .rt > i, .cc h5, .gift > i, .sh > i, .hm > i, .tn > i, .steps i, .g3 i'),function(el){
    var txt=el.textContent.trim(); var name=EMO[txt]||EMO[txt.replace(/\uFE0F/g,'')];
    if(name && el.children.length===0){ el.innerHTML="<svg class='ico'><use href='#i-"+name+"'/></svg>"; return; }
    if(el.tagName==='H5'){ var m=txt.match(/^(\S+)\s+(.*)$/); if(m&&EMO[m[1]]){ el.innerHTML="<svg class='ico'><use href='#i-"+EMO[m[1]]+"'/></svg> "+esc(m[2]); } }
  });
}
function build(){
  if(window.WaveCinema) window.WaveCinema.dispose(layer);
  layer.innerHTML=""; view=[];
  S.forEach(function(s,idx){
    if(mvpMode && !s.mvp) return;
    view.push(idx);
    var secEl=render(s,idx); emojiToSvg(secEl); layer.appendChild(secEl);
  });
}
function refresh(){
  slides=[].slice.call(layer.querySelectorAll('.slide'));
  ctaIdx=view.findIndex(function(ix){return S[ix].kind==='cta';});
}

/* ---------- ленивые медиа ---------- */
function hydrate(sl){
  if(!sl || sl.dataset.hyd) return;
  if(window.LifeStory) window.LifeStory.hydrate(sl);
  sl.dataset.hyd='1';
  [].forEach.call(sl.querySelectorAll('[data-src]'),function(el){
    el.src=el.dataset.src; el.removeAttribute('data-src');
    if(el.tagName==='VIDEO'){ el.preload='auto'; if(el.dataset.poster){ el.poster=el.dataset.poster; } }
  });
  var sp=sl.querySelector('.splitphoto');
  if(sp && !(sl._s&&sl._s.fit==='cover')){ var im=sp.querySelector('img.main'); var fit=function(){
      var side=sl.classList.contains('side');
      var cw=side?stage.clientWidth*.46:stage.clientWidth, chh=side?stage.clientHeight:stage.clientHeight*.54;
      var ir=im.naturalWidth/im.naturalHeight, cr=cw/chh;
      if(ir&&(ir/cr>1.22||cr/ir>1.22)) sp.classList.add('contain'); };
    if(im.complete&&im.naturalWidth) fit(); else im.addEventListener('load',fit,{once:true}); }
}
function fitGrid(sl){ /* экстремальные пропорции (узкие полоски, скрины) — не кропать */
  [].forEach.call(sl.querySelectorAll('.pgrid figure img'),function(im){
    var f=function(){ var fig=im.parentNode, fr=fig.clientWidth/Math.max(1,fig.clientHeight), ir=im.naturalWidth/Math.max(1,im.naturalHeight);
      if(ir&&(ir/fr>1.6||fr/ir>1.6)){ fig.classList.add('contain'); fig.style.setProperty('--fillbg',"url('"+im.src+"')"); } };
    if(im.complete&&im.naturalWidth) f(); else im.addEventListener('load',f,{once:true}); });
}
function hydrateAround(k){ for(var d=-1;d<=3;d++){ hydrate(slides[k+d]); } }

/* ---------- пословный reveal заголовка ---------- */
function splitWords(h1){
  if(!h1||h1.classList.contains('split-done')) return;
  var n=0;
  (function walk(node){
    [].slice.call(node.childNodes).forEach(function(c){
      if(c.nodeType===3){
        var parts=c.nodeValue.split(/(\s+)/), frag=document.createDocumentFragment();
        parts.forEach(function(p){
          if(!p) return;
          if(/^\s+$/.test(p)){ frag.appendChild(document.createTextNode(p)); return; }
          if(/^[\s,.;:!?…»)\]]+$/.test(p) && frag.lastChild && frag.lastChild.nodeType===1){ frag.lastChild.textContent+=p; return; } /* знаки препинания — к предыдущему слову */
          var sp=document.createElement('span'); sp.className='w'; sp.style.setProperty('--wi',n++); sp.textContent=p; frag.appendChild(sp);
        });
        node.replaceChild(frag,c);
      } else if(c.nodeType===1 && !/^(BR)$/.test(c.tagName)) walk(c);
    });
  })(h1);
  /* «…</b>, не…» — знак препинания из соседнего текстового узла приклеиваем к последнему слову */
  [].forEach.call(h1.querySelectorAll('.w'),function(w){ var nx=w.nextSibling; if(nx&&nx.nodeType===3&&/^[,.;:!?…»)\]]/.test(nx.nodeValue)){ var m=nx.nodeValue.match(/^[,.;:!?…»)\]]+/)[0]; w.textContent+=m; nx.nodeValue=nx.nodeValue.slice(m.length); } });
  h1.classList.add('split-done');
}
function restartWords(h1){
  if(!h1) return;
  [].forEach.call(h1.querySelectorAll('.w'),function(w){ w.style.animation='none'; void w.offsetWidth; w.style.animation=''; });
}

/* ---------- настроение: цвет акта × уровень кривой ---------- */
function mood(s){
  var pal=ACT_ACCENT[s.a]||ACT_ACCENT[0], acc=pal[0], acc2=pal[1];
  if(s.lv<=3){ acc=COLD[0]; acc2=COLD[1]; }
  stage.style.setProperty('--accent',acc);
  stage.style.setProperty('--accent2',acc2);
  stage.style.setProperty('--glow',(0.12+((s.lv-1)/9)*0.88).toFixed(2));
  stage.dataset.mood=s.lv<=3?'low':(s.lv>=9?'peak':'mid');
  stage.dataset.act=s.a;
}

/* ---------- показ ---------- */
function show(n,dir){
  var prev=i;
  var to=Math.max(0,Math.min(slides.length-1,n)); if(to===prev&&n!==prev) return; // 13.10: на краю деки «вперед/назад» не перезапускає слайд
  i=to;
  if(window.LifeStory) window.LifeStory.prepare(slides[prev],slides[i],dir);
  var routeBridge=window.RealityRoute && window.RealityRoute.prepare(slides[prev],slides[i],dir);
  var openingBridge=window.Opening ? window.Opening.prepare(slides[prev],slides[i],dir) : null;
  if(window.RealityRoute) window.RealityRoute.enter(slides[i],dir);
  if(window.Opening) window.Opening.enter(slides[i],dir);
  clearTimeout(outTimer);
  slides.forEach(function(sl,k){
    sl.classList.remove('out');
    if(k===i){ sl.classList.remove('on'); void sl.offsetWidth; sl.classList.add('on'); }
    else if(k===prev && prev!==i){ sl.classList.remove('on'); sl.classList.add('out'); }
    else sl.classList.remove('on');
  });
  outTimer=setTimeout(function(){ slides.forEach(function(sl){ sl.classList.remove('out'); }); },routeBridge?560:480);
  var s=S[view[i]], sl=slides[i];
  hydrateAround(i); fitGrid(sl);
  if(window.Block129) window.Block129.enter(sl,dir);
  var h1=sl.querySelector('h1'); if(!s.opening && !s.routeRoadmap){ splitWords(h1); restartWords(h1); }
  if(window.Opening) window.Opening.play(openingBridge);
  mood(s);
  hud.textContent=(i+1)+" / "+slides.length;
  actEl.textContent=ACTS[s.a]||'';
  bar.style.width=((i+1)/slides.length*100)+"%";
  lvl.style.width=(s.lv*10)+"%";
  overlay.classList.toggle('on', ctaIdx>-1 && i>ctaIdx);
  notesEl.textContent=(s.note||"")+(hiddenText(sl)?("\n📝 "+hiddenText(sl)):"");
  var flags=view.filter(function(ix){return S[ix].st;}).length;
  document.getElementById('stcount').innerHTML="<span style='color:var(--accent)'>"+(view.length-flags)+" готово</span> · "+flags+" с пометкой · S — к следующей";
  [].forEach.call(layer.querySelectorAll('video'),function(v){ if(!sl.contains(v)){ if(!v.paused) v.pause(); } });
  var vd=sl.querySelector('.ag-reframe') ? sl.querySelector('.ag-reframe-scene.is-current video,.ag-depth-card.is-current video') : sl.querySelector('video:not([data-s3-final])');
  if(sl.querySelector('.ag-reframe') && window.matchMedia('(prefers-reduced-motion: reduce)').matches) vd=null;
  if(vd && vd.hasAttribute('data-reduced-poster') && window.matchMedia('(prefers-reduced-motion: reduce)').matches) vd=null;
  if(vd && !(s.opening && window.Opening.reduced.matches)){ if(!sl.classList.contains('meme')) vd.currentTime=0; beatSync(sl);
    /* «кружок» и другие ролики с голосом — со звуком (после клика/клавиши браузер разрешает); при запрете — тихо */
    vd.muted=!(vd.closest('.memefig.round')||sl.classList.contains('sound'));
    var pr=vd.play(); if(pr&&pr.catch) pr.catch(function(err){
      if(!sl.classList.contains('on') || (err && err.name==='AbortError') || (s.opening && window.Opening.reduced.matches)) return;
      vd.muted=true; vd.play().catch(function(){});
    }); }
  /* 22.09: на слайді може бути кілька роликів (напр. 102 — гіфка + стрічка оплат).
     deck.js історично запускав тільки перший. Додаткові стартуємо лише за явним opt-in у розмітці: autoplay+loop. */
  [].forEach.call(sl.querySelectorAll('video[autoplay][loop]'),function(v){ if(v===vd)return; v.muted=true; if(v.paused){ var p2=v.play(); if(p2&&p2.catch) p2.catch(function(){}); } });
  var emb=sl.querySelector('iframe'); if(emb&&emb.dataset.src){ emb.src=emb.dataset.src; delete emb.dataset.src; }
  playChat(sl); updateDir(s); updateCurve(); countUps(); agentsEnergy(s);
  updateOpeningNotes(sl);
  try{ history.replaceState(null,'',location.pathname+q.replace(/([?&])s=\d+/,'$1s='+(i+1)).replace(/^$/,'?s='+(i+1))+(q.indexOf('s=')<0?(q?'&':'?')+'s='+(i+1):'')); }catch(e){}
}
function updateOpeningNotes(sl){
  var cue=(window.Block129 && window.Block129.cue(sl)) || (window.RealityRoute && window.RealityRoute.cue(sl)) || (window.Opening && window.Opening.cue(sl)); if(!cue) return;
  notesEl.textContent=(sl._s.note||'')+'\n'+cue;
  updateDir(sl._s);
  document.getElementById('dirNote').textContent+='\n'+cue;
}
layer.addEventListener('realityroutechange',function(e){ if(e.target===slides[i]) updateOpeningNotes(e.target); });
function next(){
  var s=S[view[i]], sl=slides[i];
  if(window.Block129 && window.Block129.advance(sl,1)){ updateOpeningNotes(sl); return; }
  if(window.RealityRoute && window.RealityRoute.advance(sl,1)){ updateOpeningNotes(sl); return; }
  if(window.Opening && window.Opening.step(sl,1)){ updateOpeningNotes(sl); return; }
  if(s.kind==='video' && beatStep(sl,1)) return;
  var st=sl.querySelector('.stack');
  if(st){
    var hidden=st.querySelector('.row:not(.show):not(.total)');
    if(hidden){ hidden.classList.add('show'); recalc(st); return; }
    var tot=st.querySelector('.row.total:not(.show)');
    if(tot){ tot.classList.add('show'); recalc(st); return; }
  }
  show(i+1,1);
}
function prev(){
  if(window.Block129 && window.Block129.advance(slides[i],-1)){ updateOpeningNotes(slides[i]); return; }
  if(window.RealityRoute && window.RealityRoute.advance(slides[i],-1)){ updateOpeningNotes(slides[i]); return; }
  if(window.Opening && window.Opening.step(slides[i],-1)){ updateOpeningNotes(slides[i]); return; }
  if(S[view[i]].kind==='video' && beatStep(slides[i],-1)) return;
  show(i-1,-1);
}

/* ---------- чат, который печатается ---------- */
var chatTimers=[], chatRAF=0;
function later(fn,ms){ chatTimers.push(setTimeout(fn,ms)); }
function stopChat(){ chatTimers.forEach(clearTimeout); chatTimers=[]; if(chatRAF) cancelAnimationFrame(chatRAF); chatRAF=0; }
function typeInto(el,html,done){
  el.innerHTML=html; var parts=[];
  (function walk(n){[].forEach.call(n.childNodes,function(c){ if(c.nodeType===3){ parts.push({n:c,full:c.nodeValue}); c.nodeValue=''; } else walk(c); });})(el);
  var total=parts.reduce(function(a,p){return a+p.full.length;},0);
  if(!total){ done&&done(); return; }
  var dur=Math.min(2800,Math.max(850,total*17)), t0=0;
  el.classList.add('writing');
  function frame(ts){ if(!t0)t0=ts; var k=Math.min(1,(ts-t0)/dur), left=Math.round(total*k);
    for(var p=0;p<parts.length;p++){ var take=Math.max(0,Math.min(left,parts[p].full.length)); parts[p].n.nodeValue=parts[p].full.slice(0,take); left-=take; }
    if(k<1) chatRAF=requestAnimationFrame(frame); else { el.classList.remove('writing'); done&&done(); } }
  chatRAF=requestAnimationFrame(frame);
}
function playChat(sl){
  stopChat();
  var box=sl&&sl.querySelector('.chatbox.type'); if(!box) return;
  var msgs=[].slice.call(box.children).filter(function(m){return !m.classList.contains('typing');});
  var dots=box.querySelector('.cmsg.typing');
  msgs.forEach(function(m){ if(m._html===undefined) m._html=m.innerHTML; m.classList.remove('shown','writing'); m.innerHTML=m._html; });
  if(dots) dots.classList.remove('shown');
  var k=0;
  function step(){
    if(k>=msgs.length){ if(dots) dots.classList.remove('shown'); return; }
    var m=msgs[k++];
    if(m.classList.contains('me')){ m.classList.add('shown'); later(step,650); return; }
    if(dots){ box.appendChild(dots); dots.classList.add('shown'); }
    later(function(){ if(dots) dots.classList.remove('shown'); m.classList.add('shown'); typeInto(m,m._html,function(){ later(step,520); }); },820);
  }
  later(step,450);
}

/* ---------- видео с битами ---------- */
function beatSync(sl){
  var vd=sl.querySelector('video'); if(!vd) return;
  var bs=[].slice.call(sl.querySelectorAll('.vbeat')); if(!bs.length) return;
  function upd(){ var t=vd.currentTime, act=-1; bs.forEach(function(b,k){ if(t+0.06>=parseFloat(b.dataset.t)) act=k; }); bs.forEach(function(b,k){ b.classList.toggle('on',k===act); }); }
  vd.ontimeupdate=upd; vd.onseeked=upd; upd();
}
function beatStep(sl,dir){
  var vd=sl.querySelector('video'); if(!vd) return false;
  var ts=[].slice.call(sl.querySelectorAll('.vbeat')).map(function(b){return parseFloat(b.dataset.t);}); if(!ts.length) return false;
  var t=vd.currentTime, target=null;
  if(dir>0){ ts.forEach(function(x){ if(target===null && x>t+0.35) target=x; }); } else { ts.forEach(function(x){ if(x<t-0.7) target=x; }); }
  if(target===null) return false;
  [].forEach.call(sl.querySelectorAll('.vbeat'),function(b){ b.classList.toggle('on',parseFloat(b.dataset.t)===target); });
  vd.currentTime=target; if(vd.paused) vd.play().catch(function(){});
  return true;
}

/* ---------- счётчики ---------- */
function countUps(){
  [].forEach.call(slides[i].querySelectorAll('.cnt[data-to]'),function(el){
    var to=parseInt(el.dataset.to),pre=el.dataset.prefix||'',suf=el.dataset.suffix||'',t0=null,dur=1100;
    function step(ts){ if(!t0)t0=ts; var k=Math.min(1,(ts-t0)/dur); k=1-Math.pow(1-k,3); var _n=Math.round(to*k).toLocaleString('en-US');if(el.dataset.sep)_n=_n.replace(/,/g,el.dataset.sep);el.textContent=pre+_n+suf; if(k<1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  });
}
function recalc(st){
  var sum=0; st.querySelectorAll('.row.show .money').forEach(function(m){ if(!m.classList.contains('stackTotal')) sum+=parseInt(m.textContent.replace(/\D/g,''))||0; });
  var t=st.querySelector('.stackTotal'); if(!t) return;
  var from=parseInt(t.textContent.replace(/\D/g,''))||0, t0=null, dur=700;
  function step(ts){ if(!t0)t0=ts; var k=Math.min(1,(ts-t0)/dur); k=1-Math.pow(1-k,3); t.textContent="$"+Math.round(from+(sum-from)*k).toLocaleString('en-US'); if(k<1) requestAnimationFrame(step); }
  requestAnimationFrame(step);
}

/* 22.09 · якщо сторінка відкрилась у фоновій вкладці, Chrome ставить беззвучне відео на паузу (AbortError), а дека не повторює play — повторюємо, коли вкладка стає видимою */
function resumeOnVisible(){ if(document.visibilityState!=='visible') return; var sl=slides[i]; if(!sl) return;
  [].forEach.call(sl.querySelectorAll('video'),function(v){ if(!v.muted || v.ended || !v.paused || v.hasAttribute('controls')) return;
    var st=v.closest('.s16-step'); if(st && !st.classList.contains('is-focus')) return; v.play().catch(function(){}); }); }
document.addEventListener('visibilitychange',resumeOnVisible);
/* ---------- частицы-агенты ---------- */
var cv=document.getElementById('agents'), ctx=cv.getContext('2d'), P=[], energy=.5, accRGB=[77,242,166], dpr=Math.min(2,window.devicePixelRatio||1), reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
function resizeCanvas(){ cv.width=stage.clientWidth*dpr; cv.height=stage.clientHeight*dpr; }
function initParticles(){ P=[]; for(var k=0;k<64;k++) P.push({x:Math.random(),y:Math.random(),vx:(Math.random()-.5)*.0004,vy:(Math.random()-.5)*.0004,r:.8+Math.random()*2.2,ph:Math.random()*6.28,sp:.4+Math.random()*.8}); }
function agentsEnergy(s){ energy=(s.lv-1)/9; }
function parseColor(str){ var m=str.match(/#([0-9a-f]{6})/i); if(m){ var v=parseInt(m[1],16); return [v>>16&255,v>>8&255,v&255]; }
  m=str.match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)/); if(m) return [+m[1],+m[2],+m[3]]; return accRGB; }
var lastCol=0;
function loop(ts){
  if(document.hidden||reduce){ requestAnimationFrame(loop); return; }
  if(ts-lastCol>250){ lastCol=ts; accRGB=parseColor(getComputedStyle(stage).getPropertyValue('--accent')); }
  var W=cv.width,H=cv.height; ctx.clearRect(0,0,W,H);
  var e=.25+energy*.75;
  P.forEach(function(p){
    p.x+=p.vx*e*p.sp*60/60; p.y+=p.vy*e*p.sp; p.ph+=.012*p.sp;
    if(p.x<-.05)p.x=1.05; if(p.x>1.05)p.x=-.05; if(p.y<-.05)p.y=1.05; if(p.y>1.05)p.y=-.05;
    var a=(.25+.35*Math.sin(p.ph))*e, x=p.x*W, y=p.y*H, r=p.r*dpr;
    var g=ctx.createRadialGradient(x,y,0,x,y,r*7);
    g.addColorStop(0,'rgba('+accRGB[0]+','+accRGB[1]+','+accRGB[2]+','+(a*.9)+')');
    g.addColorStop(.35,'rgba('+accRGB[0]+','+accRGB[1]+','+accRGB[2]+','+(a*.25)+')');
    g.addColorStop(1,'rgba('+accRGB[0]+','+accRGB[1]+','+accRGB[2]+',0)');
    ctx.fillStyle=g; ctx.beginPath(); ctx.arc(x,y,r*7,0,6.283); ctx.fill();
  });
  requestAnimationFrame(loop);
}

function hiddenText(sl){
  if(!sl||!document.body.classList.contains('big')||sl.classList.contains('full')) return '';
  var out=[]; [].forEach.call(sl.querySelectorAll('p, ul li'),function(el){ if(getComputedStyle(el).display==='none') out.push(el.textContent.trim()); });
  return out.join(' · ');
}
/* ---------- режиссёрская панель ---------- */
var DIRN=null;
function dirNorm(t){ return String(t||'').replace(/<[^>]+>/g,'').toLowerCase().replace(/[^\wа-яё ]/g,'').replace(/\s+/g,' ').trim(); }
function dirKey(t){ if(!DIRN){ DIRN={}; for(var k in DIR){ DIRN[dirNorm(k)]=k; } } return DIRN[dirNorm(t)]||''; }
var LAB={'new':'Новый слайд','example':'Пример — заменить','need':'Нужно от Влада','todo':'Доработать','edit':'Копирайт изменён'};
function updateDir(s){
  var d=((s.dirk&&DIR[s.dirk])||(s.t&&(DIR[s.t]||DIR[dirKey(s.t)]))||"").split("|");
  document.getElementById('dirPlace').textContent=(d[0]||"")+"  ·  слайд "+(i+1)+" из "+slides.length+"  ·  уровень кривой "+s.lv+"/10";
  document.getElementById('dirTask').textContent=d[1]||"—";
  document.getElementById('dirShow').textContent=d[2]||"—";
  document.getElementById('dirIdea').textContent=d[3]||"—";
  var hid=hiddenText(slides[i]);
  document.getElementById('dirNote').textContent=(s.note?("🗒 Заметка спикера: "+s.note):"")+(hid?("   📝 Текст слайда (в режиме T скрыт): "+hid):"");
  var ds=document.getElementById('dirStatus');
  if(s.st){ ds.className='dirst st-'+s.st[0]; ds.innerHTML="<b>"+(LAB[s.st[0]]||s.st[0])+"</b>"+(s.st[1]?"<span>"+esc(s.st[1])+"</span>":""); }
  else { ds.className='dirst'; ds.innerHTML=''; }
}
var curveSvg=document.getElementById('curveSvg');
function buildCurve(){
  var n=view.length,W=1000,H=64; curveSvg.setAttribute('viewBox','0 0 '+W+' '+H);
  var pts=view.map(function(ix,k){ return (k/(n-1)*W).toFixed(1)+','+(H-6-(S[ix].lv-1)*(H-16)/9).toFixed(1); });
  var html='<defs><linearGradient id="cgrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB454" stop-opacity=".32"/><stop offset="1" stop-color="#FFB454" stop-opacity="0"/></linearGradient></defs>'+
    '<polygon points="0,'+H+' '+pts.join(' ')+' '+W+','+H+'" fill="url(#cgrad)"/><polyline points="'+pts.join(' ')+'" fill="none" stroke="#FFB454" stroke-width="1.6" opacity=".95"/>';
  var prevA=-1;
  view.forEach(function(ix,k){
    if(S[ix].a!==prevA){ prevA=S[ix].a; var x=(k/(n-1)*W).toFixed(1);
      html+='<line x1="'+x+'" y1="0" x2="'+x+'" y2="'+H+'" stroke="rgba(255,255,255,.08)"/><text x="'+(+x+4)+'" y="12" fill="#5a6672" font-size="9" font-family="JetBrains Mono,monospace">'+(S[ix].a+1)+'</text>'; }
    if(S[ix].lv>=10){ var x2=(k/(n-1)*W).toFixed(1); html+='<circle cx="'+x2+'" cy="'+(H-6-9*(H-16)/9).toFixed(1)+'" r="3" fill="#FF5C6C"/>'; }
    if(S[ix].kind==='cta'){ var x3=(k/(n-1)*W).toFixed(1); html+='<circle cx="'+x3+'" cy="8" r="3.5" fill="#4DF2A6"/>'; }
  });
  html+='<line id="curveMark" x1="0" y1="0" x2="0" y2="'+H+'" stroke="#F5F3EE" stroke-width="1.6"/>';
  curveSvg.innerHTML=html;
}
function updateCurve(){ var m=document.getElementById('curveMark'); if(!m) return; var x=(i/(view.length-1)*1000).toFixed(1); m.setAttribute('x1',x); m.setAttribute('x2',x); }
document.getElementById('curveWrap').addEventListener('click',function(e){ var r=this.getBoundingClientRect(); show(Math.round((e.clientX-r.left)/r.width*(view.length-1))); e.stopPropagation(); });

/* ---------- клавиши ---------- */
var jbuf='', jtimer=0;
function setHint(t,ms){ hintEl.textContent=t; hintEl.classList.add('on'); clearTimeout(setHint.t); setHint.t=setTimeout(function(){ hintEl.classList.remove('on'); },ms||2500); }
function keyIs(e,latin,cyr){ var k=e.key.toLowerCase(); return k===latin||k===cyr; }
document.addEventListener('keydown',function(e){
  if(e.metaKey||e.ctrlKey||e.altKey) return;
  var help=document.getElementById('help');
  if(help.classList.contains('on')){ help.classList.remove('on'); return; }
  if(/^\d$/.test(e.key)){ jbuf+=e.key; jumpEl.textContent='→ '+jbuf; clearTimeout(jtimer); jtimer=setTimeout(function(){ jbuf=''; jumpEl.textContent=''; },2200); return; }
  if(e.key==='Enter' && jbuf){ var n=parseInt(jbuf,10); jbuf=''; jumpEl.textContent=''; show(n-1); return; }
  if(e.key==='Escape'){ jbuf=''; jumpEl.textContent=''; return; }
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'||e.key==='ArrowDown'){ e.preventDefault(); next(); }
  else if(e.key==='ArrowLeft'||e.key==='PageUp'||e.key==='ArrowUp'){ e.preventDefault(); prev(); }
  else if(e.key==='Home') show(0);
  else if(e.key==='End') show(slides.length-1);
  else if(keyIs(e,'p','з')){ var v=slides[i].querySelector('video'); if(v){ e.preventDefault(); v.paused?v.play():v.pause(); } }
  else if(keyIs(e,'v','м')){ var vv=slides[i].querySelector('video'); if(vv){ vv.muted=!vv.muted; setHint(vv.muted?'звук выкл':'звук вкл'); } }
  else if(keyIs(e,'t','е')){ document.body.classList.toggle('big'); try{localStorage.setItem('preza.big',document.body.classList.contains('big')?'1':'0');}catch(x){} setHint(document.body.classList.contains('big')?'режим «1 слайд = 1 мысль»':'полный текст'); updateDir(S[view[i]]); updateOpeningNotes(slides[i]); }
  else if(keyIs(e,'f','а')){ document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen(); }
  else if(keyIs(e,'n','т')){ document.body.classList.toggle('show-notes'); }
  else if(keyIs(e,'e','у')){ lvl.classList.toggle('on'); }
  else if(keyIs(e,'d','в')){ document.body.classList.toggle('draft'); try{localStorage.setItem('preza.draft',document.body.classList.contains('draft')?'1':'');}catch(x){} resizeCanvas(); }
  else if(keyIs(e,'w','ц')){ document.body.classList.toggle('wide16'); try{localStorage.setItem('preza.wide',document.body.classList.contains('wide16')?'1':'');}catch(x){} resizeCanvas(); setHint(document.body.classList.contains('wide16')?'16:9':'квадрат'); }
  else if(keyIs(e,'s','ы')){ for(var k=1;k<=view.length;k++){ var idx=(i+k)%view.length; if(S[view[idx]].st){ show(idx); break; } } }
  else if(keyIs(e,'m','ь')){ mvpMode=!mvpMode; document.body.classList.toggle('mvp',mvpMode); var cur=view[i], savedOpening=window.Opening&&window.Opening.snapshot(slides[i]), savedRoute=window.RealityRoute&&window.RealityRoute.snapshot(slides[i]), savedBlock129=window.Block129&&window.Block129.snapshot(slides[i]); build(); refresh(); buildCurve(); var ni=view.indexOf(cur); show(ni>-1?ni:0); if(window.Opening&&savedOpening&&ni>-1){ window.Opening.restoreStep(slides[i],savedOpening); updateOpeningNotes(slides[i]); } if(window.RealityRoute&&savedRoute!=null&&ni>-1){ window.RealityRoute.restore(slides[i],savedRoute); updateOpeningNotes(slides[i]); } if(window.Block129&&savedBlock129!=null&&ni>-1){ window.Block129.restore(slides[i],savedBlock129); updateOpeningNotes(slides[i]); } setHint(mvpMode?'версия 60 мин · '+view.length+' слайдов':'полная версия · '+view.length+' слайдов',3000); }
  else if(e.key==='?'||e.key==='/'||keyIs(e,'h','р')){ help.classList.add('on'); }
});
document.addEventListener('click',function(e){
  if(e.target.closest('a')||e.target.closest('#curveWrap')||e.target.closest('#dirPanel')||e.target.closest('#help')) return;
  if(e.clientX < window.innerWidth*0.25) prev(); else next();
});
window.addEventListener('resize',resizeCanvas);

/* ---------- старт ---------- */
document.body.classList.toggle('mvp',mvpMode);
/* Основной формат вебинара — квадрат. 16:9 только по явному URL, не из старого localStorage. */
document.body.classList.toggle('wide16', /[?&]wide(?:[=&]|$)/.test(q) && !/[?&]square(?:[=&]|$)/.test(q));
if(/[?&]draft/.test(q)) document.body.classList.add('draft'); else if(!/[?&]clean/.test(q)){ try{ if(localStorage.getItem('preza.draft')) document.body.classList.add('draft'); }catch(x){} }
if(/[?&]clean/.test(q)) document.body.classList.add('clean');
if(/[?&]full/.test(q)) document.body.classList.remove('big'); else { try{ if(localStorage.getItem('preza.big')!=='0') document.body.classList.add('big'); }catch(x){ document.body.classList.add('big'); } }
overlay.querySelector('a').href=CTA_URL;
build(); refresh(); buildCurve(); resizeCanvas(); initParticles(); requestAnimationFrame(loop);
var jump=(q.match(/[?&]s=(\d+)/)||[])[1];
show(jump? Math.max(0,Math.min(slides.length-1,parseInt(jump,10)-1)) : 0);
setTimeout(function(){ setHint('? — подсказка по клавишам',3500); },900);
window.go=show;
})();
