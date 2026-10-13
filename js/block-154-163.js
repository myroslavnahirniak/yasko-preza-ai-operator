/* 16.09 · display 154–169 + відео/артефакти Влада: replay CSS-driven scenes on enter (s16-* layouts), sound videos, multi-video play, 164 stage sync. */
(function(){
'use strict';
const B=window.Block129;if(!B)return;
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const staticFrame=new URLSearchParams(location.search).has('frame');
const owns=el=>el&&el._b13&&/^s16-/.test(el._b13.layout||'');
const origRender=window.Foundation.render;
window.Foundation.render=function(s,idx){
 const el=origRender(s,idx);const c=s.foundation&&s.foundation.block129;
 if(!el||!c||!/^s16-/.test(c.layout||''))return el;
 if(c.sound)el.classList.add('sound');
 if(c.layout==='s16-mosaic')wireMosaic(el);
 if(c.layout==='s16-cost')fastSmil(el);
 if(c.layout==='s16-case')wireCardVideo(el);
 if(c.layout==='s16-fan'||c.layout==='s16-shelf'||c.layout==='s16-duo'||c.layout==='s16-avafan'||c.layout==='s16-seller')wireTilt(el);
 if(c.layout==='s16-cine')wireCine(el);
 if(c.layout==='s16-frame')wireFrame(el);
 if(c.layout==='s16-codeword'){const em=el.querySelector('.b13-head h1 em');if(em)em.innerHTML=[...em.textContent].map((ch,i)=>'<span style="--d:'+(0.35+i*0.09).toFixed(2)+'s">'+ch+'</span>').join('');}
 if(c.layout==='s16-stages'){
  const v=el.querySelector('.s16-vid video'),cards=[...el.querySelectorAll('.s16-stg>div')];
  if(v&&cards.length){el.querySelector('.s16-stg').classList.add('has-video');
   const seg=Number(c.segment)||3;
   const prog=document.createElement('div');prog.className='s16-prog';prog.innerHTML='<i></i>';el.querySelector('.s16-vid').after(prog);const bar=prog.firstChild;
   const sync=()=>{const i=Math.min(cards.length-1,Math.floor(v.currentTime/seg));cards.forEach((n,k)=>{n.classList.toggle('on',k===i);n.classList.toggle('done',k<i);});if(v.duration)bar.style.width=(v.currentTime/v.duration*100)+'%';};
   v.addEventListener('timeupdate',sync);v.addEventListener('seeked',sync);
   cards.forEach((n,i)=>n.addEventListener('click',()=>{v.currentTime=i*seg+0.05;v.play().catch(()=>{});}));
   v.addEventListener('click',()=>{v.paused?v.play().catch(()=>{}):v.pause();});
  }else cards.forEach(n=>n.classList.add('on'));
 }
 return el;
};
/* live sites in iframes: fit phone scale + gentle auto-scroll while the slide/step is on */
function fitPhone(el){el.querySelectorAll('.s16-phone').forEach(ph=>{const f=ph.querySelector('iframe');if(!f||!ph.clientWidth)return;const k=ph.clientWidth/390;f.style.transform='scale('+k+')';f.style.height=(ph.clientHeight/k)+'px';});
 /* 21.09: demo artifacts render at desktop width (>1000px → sticky panel + sidebar, 1:1 like the artifact in Chrome) and are scaled down into the square */
 el.querySelectorAll('.s16-demo').forEach(d=>{const f=d.querySelector('iframe');if(!f||!d.clientWidth)return;const base=+(d.dataset.w||1100);const k=d.clientWidth/base;f.style.width=base+'px';f.style.height=(d.clientHeight/k)+'px';f.style.transform='scale('+k+')';f.style.transformOrigin='0 0';});}
let autoScroll=null;
function startAutoScroll(f,opts){stopAutoScroll();if(!f)return;const o=Object.assign({speed:0.09,start:0,bounce:true,delay:1200},opts||{});
 const run=()=>{const w=f.contentWindow;try{if(!w||!w.document)return;}catch(e){return;} /* 01.10: чужий домен (напр. ai-operator-holst.vercel.app) — без автопрокрутки */const id=Symbol();autoScroll=id;let dir=1,last=performance.now();
  const maxY=()=>Math.max(0,w.document.documentElement.scrollHeight-w.innerHeight);
  let y=o.start>0&&o.start<1?maxY()*o.start:o.start;w.scrollTo(0,y);
  // the presenter scrolls by hand → the auto-scroll lets go (wheel/touch/scrollbar/keys) until the slide is entered again
  const release=()=>{if(autoScroll===id)autoScroll=null;};
  ['wheel','touchstart','pointerdown','keydown'].forEach(ev=>{w.addEventListener(ev,release,{passive:true});});
  const step=now=>{if(autoScroll!==id)return;if(Math.abs(w.scrollY-y)>40){release();return;}const dt=Math.min(50,now-last);last=now;const max=maxY();y+=dir*dt*o.speed;if(y>=max){y=max;if(o.bounce)dir=-1;}if(y<=0){y=0;dir=1;}w.scrollTo(0,y);requestAnimationFrame(step);};
  setTimeout(()=>{if(autoScroll===id)requestAnimationFrame(step);},o.delay);};
 let ready=false;try{ready=!!(f.contentDocument&&f.contentDocument.readyState==='complete'&&f.contentWindow.location.href!=='about:blank');}catch(e){}
 if(ready)run();else f.addEventListener('load',run,{once:true});}
function stopAutoScroll(){autoScroll=null;}
/* 193 · live site (local copy of roma-kp-site.vercel.app) in a browser window: a step scrolls the site to its chapter; the presenter may also scroll by hand — the step dots follow the chapter under the wheel */
const isLive=el=>owns(el)&&el._b13.layout==='s16-live';
function fitLive(el){el.querySelectorAll('.s16-live .s16-view').forEach(d=>{const f=d.querySelector('iframe');if(!f||!d.clientWidth)return;const base=+(d.dataset.w||1100);const k=d.clientWidth/base;f.style.width=base+'px';f.style.height=(d.clientHeight/k)+'px';f.style.transform='scale('+k+')';});}
function liveApi(el){const f=el.querySelector('.s16-live iframe');try{return f&&f.contentWindow&&f.contentWindow.RomaKP||null;}catch(e){return null;}}
let liveTimer=0,liveBusy=0,liveWait=0;
function liveGoto(el,step,immediate){clearTimeout(liveWait);const f=el.querySelector('.s16-live iframe');if(!f)return;
 if(f.dataset.src){f.src=f.dataset.src;f.removeAttribute('data-src');}
 const go=()=>{const api=liveApi(el);if(!api||!api.isReady()){if(document.contains(f))liveWait=setTimeout(go,150);return;}liveBusy=performance.now()+(immediate?400:2000);api.goto(step,{immediate});};
 go();}
function liveStart(el){clearInterval(liveTimer);if(!isLive(el))return;fitLive(el);liveGoto(el,el._b13Step||0,true);
 liveTimer=setInterval(()=>{if(!document.contains(el)||!el.closest('.slide.on')){clearInterval(liveTimer);return;}if(performance.now()<liveBusy)return;const api=liveApi(el);if(!api||!api.isReady())return;const a=api.active();if(a!==el._b13Step)B.restore(el,a);},250);}
addEventListener('resize',()=>{const el=document.querySelector('.slide.on .b129.b13-v2-s16-live');if(el)fitLive(el);});
function liveFrames(el){if(!owns(el)){stopAutoScroll();return;}
 const phone=el.querySelector('.s16-phone iframe');if(phone){startAutoScroll(phone,{speed:0.09});return;}
 const frame=el.querySelector('.s16-frame .s16-view iframe');if(frame){startAutoScroll(frame,{speed:0.07,start:0,bounce:true,delay:1600});return;}
 const demo=el.querySelector('.s16-step.is-focus .s16-demo iframe');if(demo){startAutoScroll(demo,{speed:0.14,start:0.03,bounce:false,delay:900});return;}
 stopAutoScroll();}
let yearTimers=[];
function runYear(el){yearTimers.forEach(clearTimeout);yearTimers=[];const bars=[...el.querySelectorAll('.s16-bar')],cap=el.querySelector('.s16-cap');if(!bars.length)return;
 bars.forEach(b=>b.querySelectorAll('i').forEach(i=>i.style.height='0'));let m=0;
 const step=()=>{if(m>=bars.length)return;const b=bars[m];if(m===0)b.querySelector('.site').style.height='2.2cqh';b.querySelector('.sell').style.height='3.2cqh';b.querySelector('.seo').style.height='2.2cqh';b.querySelector('.ads').style.height='2.6cqh';if(cap)cap.textContent='месяц '+(m+1)+' из 12';m++;yearTimers.push(setTimeout(step,520));};
 yearTimers.push(setTimeout(step,900));}
/* sales 21.09 · counters: [data-count] counts up from data-from to data-count (dot thousands, $ kept) */
let cntTimers=[];
function fmtCount(n,sample){const neg=n<0;n=Math.abs(Math.round(n));const s=String(n).replace(/\B(?=(\d{3})+(?!\d))/g,'.');return (sample&&sample.trim().startsWith('$')?'$':'')+(neg?'−':'')+s;}
function runCounters(el){cntTimers.forEach(clearTimeout);cntTimers=[];el.querySelectorAll('[data-count]').forEach((n,i)=>{const to=Number(n.dataset.count),from=Number(n.dataset.from||0);if(!to&&to!==0)return;const sample=n.textContent;const t0=performance.now()+900+i*200,dur=1400;const tick=()=>{const k=Math.min(1,(performance.now()-t0)/dur);if(k<0){requestAnimationFrame(tick);return;}const e=1-Math.pow(1-k,3);n.textContent=fmtCount(from+(to-from)*e,sample);if(k<1)requestAnimationFrame(tick);else n.textContent=sample;};n.textContent=fmtCount(from,sample);requestAnimationFrame(tick);});}
function staticCounters(el){el.querySelectorAll('[data-count]').forEach(n=>{const to=Number(n.dataset.count);if(to||to===0)n.textContent=fmtCount(to,n.textContent);});}
/* 176 · codeword chat: after the CSS-staggered messages, keep a slow trickle of viewer messages while the slide is on */
let chatTimers=[];
function clearChat(){chatTimers.forEach(clearTimeout);chatTimers=[];}
/* messages are appended only when their time comes (a hidden message must not take space and push the first one under the top mask) */
const chatPre=el=>{const box=el.querySelector('.s16-msgs');if(!box)return null;if(!el._s16ChatPre)el._s16ChatPre=[...box.querySelectorAll('.s16-msg')].map(m=>m.cloneNode(true));return box;};
function runChat(el){clearChat();const box=chatPre(el);if(!box)return;const pool=['агент','Агент','агент','АГЕНТ','агент','агент'];let n=0;
 const put=m=>{if(!document.contains(box))return;m.style.setProperty('--d','0s');box.append(m);while(box.children.length>10)box.firstChild.remove();};
 box.replaceChildren();let lastAt=0;
 el._s16ChatPre.forEach(src=>{const d=parseFloat(src.style.getPropertyValue('--d'))||0;lastAt=Math.max(lastAt,d);chatTimers.push(setTimeout(()=>put(src.cloneNode(true)),d*1000));});
 const add=()=>{const m=document.createElement('div');m.className='s16-msg';m.innerHTML='<i></i><span></span>';m.lastChild.textContent=pool[n%pool.length];n++;put(m);chatTimers.push(setTimeout(add,900+Math.random()*900));};
 chatTimers.push(setTimeout(add,(lastAt+0.9)*1000));}
function chatStatic(el){const box=chatPre(el);if(box&&el._s16ChatPre)box.replaceChildren(...el._s16ChatPre.map(m=>m.cloneNode(true)));}
/* 21.09 · 186 мозаїка: hover — легкий нахил площини (кроки 0/5) або активної картки (кроки 1–4) за курсором */
function wireMosaic(el){const sc=el.querySelector('.s16-scene');if(!sc||sc._wired)return;sc._wired=true;const plane=sc.querySelector('.s16-plane');let tiltT=0;
 sc.addEventListener('mousemove',e=>{/* 09.10: поки курсор рухається — короткий transition (клас s16-tilting), інакше кожен рух запускав повільні .65 с і нахил «плив» із запізненням */sc.classList.add('s16-tilting');clearTimeout(tiltT);tiltT=setTimeout(()=>sc.classList.remove('s16-tilting'),180);const r=sc.getBoundingClientRect();const dx=(e.clientX-r.left)/r.width-.5,dy=(e.clientY-r.top)/r.height-.5;const st=+el.dataset.b13Step||0;
  if(st>=1&&st<=4){plane.style.transform='';const card=sc.querySelector('.s16-card.k'+st);if(card){card.style.setProperty('--tx',(dx*7).toFixed(2)+'deg');card.style.setProperty('--ty',(-dy*7).toFixed(2)+'deg');}}
  else if(st===0){plane.style.transform='rotateX('+(10-dy*9).toFixed(2)+'deg) rotateY('+(-8+dx*11).toFixed(2)+'deg)';}});
 sc.addEventListener('mouseleave',()=>mosaicReset(el));}
function mosaicReset(el){if(!el._b13||el._b13.layout!=='s16-mosaic')return;const p=el.querySelector('.s16-plane');if(p)p.style.transform='';el.querySelectorAll('.s16-card').forEach(c=>{c.style.removeProperty('--tx');c.style.removeProperty('--ty');});}
/* 21.09 · 188/190: hover — легкий 3D-нахил площини .s16-tilt за курсором (зона — найближчий контейнер) */
function wireTilt(el){el.querySelectorAll('.s16-tilt').forEach(t=>{const zone=t.parentElement;if(zone._tilt)return;zone._tilt=true;
 zone.addEventListener('mousemove',e=>{const r=zone.getBoundingClientRect();const dx=(e.clientX-r.left)/r.width-.5,dy=(e.clientY-r.top)/r.height-.5;t.style.setProperty('--tx',(dx*10).toFixed(2)+'deg');t.style.setProperty('--ty',(-dy*8).toFixed(2)+'deg');});
 zone.addEventListener('mouseleave',()=>{t.style.removeProperty('--tx');t.style.removeProperty('--ty');});});}
/* 21.09 · 191: клік по плеєру — відео на весь слайд зі звуком, ще клік — назад */
function wireCine(el){const p=el.querySelector('.s16-player');if(!p||p._wired)return;p._wired=true;const v=p.querySelector('video');
 p.addEventListener('click',e=>{e.stopPropagation();e.preventDefault();const full=el.classList.toggle('is-full');if(v){v.muted=!full;if(full)v.currentTime=0;v.play().catch(()=>{});}});}
/* 21.09 · 205: артефакт у вікні браузера (s16-frame) — масштаб з data-w, м'який автоскрол; клік по панелі — на весь слайд */
function fitFrame(el){el.querySelectorAll('.s16-frame .s16-view').forEach(d=>{const f=d.querySelector('iframe');if(!f||!d.clientWidth)return;const base=+(d.dataset.w||1100);const k=d.clientWidth/base;f.style.width=base+'px';f.style.height=(d.clientHeight/k)+'px';f.style.transform='scale('+k+')';});}
function wireFrame(el){const bar=el.querySelector('.s16-fbar');if(!bar||bar._wired)return;bar._wired=true;
 bar.addEventListener('click',e=>{e.stopPropagation();e.preventDefault();el.classList.toggle('is-full');fitFrame(el);setTimeout(()=>fitFrame(el),560);});}
addEventListener('resize',()=>{const el=document.querySelector('.slide.on .b129.b13-v2-s16-frame');if(el)fitFrame(el);});
/* 21.09 · 218: живий чат ChatGPT — друк запиту, «думает», стрім відповіді рядок за рядком; static — усе одразу */
let gptTimers=[];
function gptClear(){gptTimers.forEach(clearTimeout);gptTimers=[];}
function gptStatic(el){gptClear();const t=el.querySelector('.typed');if(t)t.textContent=t.dataset.text;el.querySelectorAll('.msgs .ai p').forEach(p=>{p.innerHTML=p.dataset.html;p.classList.add('on');});const th=el.querySelector('.think');if(th)th.classList.remove('on');el.classList.add('typed-done','stream-done');}
function runGpt(el){gptClear();el.classList.remove('typed-done','stream-done');const t=el.querySelector('.typed');const ps=[...el.querySelectorAll('.msgs .ai p')];const th=el.querySelector('.think');if(!t)return;
 t.textContent='';ps.forEach(p=>{p.innerHTML='';p.classList.remove('on');});if(th)th.classList.remove('on');
 const text=t.dataset.text;let i=0,tm=600;
 const typeNext=()=>{i++;t.textContent=text.slice(0,i);if(i<text.length)gptTimers.push(setTimeout(typeNext,11));else{el.classList.add('typed-done');if(th)th.classList.add('on');gptTimers.push(setTimeout(stream,1100));}};
 gptTimers.push(setTimeout(typeNext,tm));
 function stream(){if(th)th.classList.remove('on');let k=0;
  const next=()=>{if(k>=ps.length){el.classList.add('stream-done');return;}const p=ps[k++];const html=p.dataset.html;p.classList.add('on');
   // стрім по словах з збереженням розмітки: показуємо HTML поступово через обрізання тексту, теги додаємо цілком
   const tokens=html.split(/(<[^>]+>|\s+)/).filter(Boolean);let j=0,acc='';
   const word=()=>{if(j>=tokens.length){gptTimers.push(setTimeout(next,260));return;}acc+=tokens[j++];p.innerHTML=acc+(j<tokens.length?'<span class="cur">▍</span>':'');const m=el.querySelector('.msgs');if(m)m.scrollTop=m.scrollHeight;gptTimers.push(setTimeout(word,tokens[j-1].startsWith('<')?0:34));};
   word();};
  next();}}
/* 21.09 · 172 кейс Антона: відео грає без звуку; клік — звук + з початку, ще клік — знову без звуку */
function wireCardVideo(el){el.querySelectorAll('.s16-card video').forEach(v=>{v.muted=true;v.play().catch(()=>{});if(v._wiredSnd)return;v._wiredSnd=true;v.style.cursor='pointer';
 v.addEventListener('click',e=>{e.stopPropagation();e.preventDefault();const on=v.muted;v.muted=!on;if(on)v.currentTime=0;v.play().catch(()=>{});});});}
/* 21.09 · 174 «Ваши расходы»: SMIL-малювання іконок тривало 7 с — стискаємо всю хореографію до 1 с */
function fastSmil(el){el.querySelectorAll('.s16-smil').forEach(svg=>{
 svg.querySelectorAll('animate,animateTransform,animateMotion,set').forEach(a=>{
  const d=a.getAttribute('dur'); if(d&&/^[\d.]+s$/.test(d)&&parseFloat(d)>1) a.setAttribute('dur','1s');
  const b=a.getAttribute('begin'); if(b&&/^[\d.]+s$/.test(b)&&parseFloat(b)>0.2) a.setAttribute('begin','0.1s');});
 const fresh=svg.cloneNode(true); svg.replaceWith(fresh); try{fresh.setCurrentTime(0);}catch(e){}});}
const origEnter=B.enter,origFinish=B.finish;
function settle(el){el.classList.remove('s16-play');el.classList.add('s16-static');if(el._b13&&el._b13.layout==='s16-chatgpt')gptStatic(el);cntTimers.forEach(clearTimeout);cntTimers=[];if(el.querySelector('[data-count]'))staticCounters(el);yearTimers.forEach(clearTimeout);yearTimers=[];clearChat();if(el._b13&&el._b13.layout==='s16-codeword')chatStatic(el);const c=el.querySelector('.s16-year-cap, .s16-cap');if(c&&el._b13&&el._b13.layout==='s16-year')c.textContent='месяц 12 из 12';}
B.enter=function(el,dir){
 origEnter(el,dir);
 clearChat();gptClear();
 if(!owns(el))return;
 // multi-video scenes: play every video (deck autoplays only the first)
 el.querySelectorAll('.s16-pair video,.s16-vid video,.s16-cover video,.s16-team video,.s16-four video,.sl2-media video,.s16-player video,.s16-avafan video,.s16-card video').forEach(v=>{v.muted=true;v.currentTime=0;v.play().catch(()=>{});});
 fitPhone(el);fitFrame(el);liveFrames(el);liveStart(el);
 el.classList.remove('s16-play','s16-static');
 const ads=el.querySelector('.s16-ads-svg,.s16-smil');if(ads&&ads.setCurrentTime){try{ads.pauseAnimations();ads.setCurrentTime((reduced.matches||staticFrame||dir<0)?9:0);ads.unpauseAnimations();}catch(e){}}
 if(reduced.matches||staticFrame||dir<0){settle(el);return;}
 void el.offsetWidth;el.classList.add('s16-play');
 if(el._b13.layout==='s16-chatgpt')runGpt(el);
 if(el._b13.layout==='s16-year')runYear(el);
 if(el._b13.layout==='s16-codeword')runChat(el);
 if(el.querySelector('[data-count]'))runCounters(el);
};
const origAdvance=B.advance;
function stepMedia(el){if(!owns(el))return;el.querySelectorAll('.s16-step').forEach(st=>{const on=st.classList.contains('is-focus');st.querySelectorAll('video').forEach(v=>{if(on){v.muted=!el.classList.contains('sound');v.currentTime=0;v.play().catch(()=>{v.muted=true;v.play().catch(()=>{});});}else if(!v.paused)v.pause();});});}
window.__fitPhone=fitPhone;
B.advance=function(el,dir){const r=origAdvance(el,dir);if(r){fitPhone(el);stepMedia(el);liveFrames(el);if(isLive(el))liveGoto(el,el._b13Step,false);}return r;};
B.finish=function(el){origFinish(el);if(owns(el)){settle(el);fitPhone(el);stepMedia(el);liveFrames(el);if(isLive(el))liveGoto(el,el._b13Step,true);}};
})();

/* Service catalogue jumps use the deck's native subslide state. */
(function(){document.addEventListener('click',function(e){const b=e.target.closest('[data-catalog-go]');if(!b)return;const el=b.closest('.b13-v2-s16-catalog-orbit');if(!el)return;e.preventDefault();e.stopPropagation();window.Block129.restore(el,+b.dataset.catalogGo);if(window.__fitPhone)setTimeout(()=>window.__fitPhone(el),30);el.querySelectorAll('video').forEach(v=>{if(v.closest('.s16-step').classList.contains('is-focus'))v.play().catch(()=>{});else v.pause();});},true);})();
