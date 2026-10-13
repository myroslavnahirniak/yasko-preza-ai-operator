(function(){
'use strict';
const assets={
 intro:{src:'assets/photo/vlad/v038-1.jpg',size:[828,1800],crop:[0,105,828,1425]},
 agency:{src:'assets/photo/vlad/v039-1.jpg',size:[1600,1351],crop:[200,285,1260,945]},
 team:{src:'assets/photo/vlad/v039-2.jpg',size:[1276,956]},
 officeBefore:{src:'assets/photo/vlad/v040-1.jpg',size:[800,671],crop:[0,0,620,671]},
 officeAfter:{src:'assets/photo/vlad/v040-2.jpg',size:[1600,1600],crop:[120,75,1200,1300]},
 car:{src:'assets/photo/vlad2/m044_1.jpg',size:[1800,880],crop:[28,120,786,732]},
 paris:{src:'assets/google-source/g045-g3fadf66108e_0_318.png',size:[1227,1545]},
 bali:{src:'assets/google-source/g045-g3fadf66108e_0_319.png',size:[1537,1524]},
 newyork:{src:'assets/google-source/g045-g3fadf66108e_0_320.png',size:[1225,1403]}
};
const steps=[
 {key:'intro',label:'Пролог',title:'Мне 30.<br>У меня<br>ничего <em>нет</em>',body:'Ни источника дохода, ни денег, ни возможности работать, ни понимания, что делать дальше.'},
 {key:'agency',label:'Агентство',title:'Мне 20.<br>У меня своё <em>агентство</em>',body:'Гением не был — просто рано замечал тренды и первым в них заходил. Как случилось с SMM.'},
 {key:'officeBefore',label:'Офіс · до',title:'Крутой <em>офис</em>',body:''},
 {key:'officeAfter',label:'Офіс · після',title:'Крутой <em>офис</em>',body:'100+ сотрудников'},
 {key:'car',label:'Машина',title:'И на это покупалось всё,<br>о чём <em>мечталось</em>',body:'Первая машина.'},
 {key:'paris',label:'Подорожі · 1',title:'<em>Путешествия</em>',body:'Когда хотелось — тогда и летели'},
 {key:'bali',label:'Подорожі · 2',title:'<em>Путешествия</em>',body:'Когда хотелось — тогда и летели'},
 {key:'newyork',label:'Подорожі · 3',title:'<em>Путешествия</em>',body:'Когда хотелось — тогда и летели'},
 {key:'final',label:'Вся історія',title:'Всё, о чём <em>мечталось</em>',body:''}
];
const notes={scene:'Постійна композиція. У блоці офісу наступний клік перетворює порожнє приміщення на готове.',mosaic:'Кожний наступний епізод залишає попередній у кадрі. Наприкінці видно всю мозаїку.',road:'Фотографії з’єднані однією лінією. Можна рухатися стрілками або натискати на зупинки.',camera:'Фото наближається і відкриває наступний кадр. У подорожах змінюється напрям руху камери.'};
const modules={},hosts={};let selected='scene',current=1;
function photo(key,cls=''){const a=assets[key],v=a.crop||[0,0,...a.size];return `<div class="lab-photo ${cls}" data-photo="${key}"><svg viewBox="${v.join(' ')}" preserveAspectRatio="${key==='car'?'xMidYMin':'xMidYMid'} slice" role="img" aria-label="Архивное фото Влада"><image href="${a.src}" width="${a.size[0]}" height="${a.size[1]}"/></svg></div>`;}
function intro(){return `<section class="lab-intro">${photo('intro','intro-photo')}<svg class="intro-ring" viewBox="0 105 828 1425" aria-hidden="true"><ellipse cx="414" cy="174" rx="192" ry="55" transform="rotate(-3 414 174)"/></svg><div class="intro-copy"><h2 class="lab-title">${steps[0].title}</h2><p class="lab-body">${steps[0].body}</p><p class="lab-body intro-last">Сейчас расскажу, как я там оказался и что меня оттуда вытащило</p></div></section>`;}
function refresh(animate=true){
 animate=animate&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 for(const [key,el] of Object.entries(hosts))el.hidden=key!==selected;
 if(!hosts[selected]){const h=document.createElement('div');h.className='lab-module lab-'+selected;document.getElementById('canvas').append(h);hosts[selected]=h;modules[selected].mount(h);}
 hosts[selected].dataset.step=current;modules[selected].update(current,{animate});
 document.querySelectorAll('[data-variant]').forEach(b=>{const on=b.dataset.variant===selected;b.classList.toggle('active',on);b.setAttribute('aria-pressed',String(on));});
 document.querySelectorAll('[data-step]').forEach(b=>{b.classList.toggle('active',+b.dataset.step===current);b.setAttribute('aria-current',+b.dataset.step===current?'step':'false');});
 document.getElementById('variant-note').textContent=notes[selected];document.getElementById('progress-label').textContent=`${String(current+1).padStart(2,'0')} / ${steps.length} · ${steps[current].label}`;
 document.getElementById('previous').disabled=current===0;document.getElementById('next').disabled=current===steps.length-1;
 history.replaceState(null,'',`?style=${selected}&step=${current}`);
}
function goStep(n){current=Math.max(0,Math.min(steps.length-1,n));refresh();}
function choose(key){if(!modules[key])return;selected=key;refresh(false);}
window.StoryLab={assets,steps,photo,intro,register:(key,module)=>modules[key]=module,goStep,
start(){const q=new URLSearchParams(location.search);if(modules[q.get('style')])selected=q.get('style');if(q.has('step'))current=Math.max(0,Math.min(8,parseInt(q.get('step'),10)||0));
 document.getElementById('steps').innerHTML=steps.map((s,i)=>`<button data-step="${i}" aria-label="${s.label}" title="${s.label}"></button>`).join('');
 document.querySelectorAll('[data-step]').forEach(b=>b.onclick=()=>goStep(+b.dataset.step));document.querySelectorAll('[data-variant]').forEach(b=>b.onclick=()=>choose(b.dataset.variant));
 document.getElementById('next').onclick=()=>goStep(current+1);document.getElementById('previous').onclick=()=>goStep(current-1);document.getElementById('replay').onclick=()=>goStep(0);
 document.getElementById('canvas').onclick=e=>{if(e.target.closest('button,a,input'))return;goStep(current===8?0:current+1);};
 document.addEventListener('keydown',e=>{if(e.target.matches('input,textarea,select'))return;if(e.key==='ArrowRight'||e.key===' '){e.preventDefault();goStep(current+1);}else if(e.key==='ArrowLeft'){e.preventDefault();goStep(current-1);}else if(e.key.toLowerCase()==='r')goStep(0);else if('1234'.includes(e.key)&&e.key.length===1)choose(['scene','mosaic','road','camera'][+e.key-1]);});
 document.getElementById('fullscreen').onclick=()=>document.fullscreenElement?document.exitFullscreen():document.querySelector('.lab-view').requestFullscreen();refresh(false);
}};
})();
