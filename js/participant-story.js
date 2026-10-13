/* Google135: one slide, five approved scenes. Shared by the deck and its preview. */
(function(){
'use strict';
let serial=0;
const esc=s=>String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const reduced=()=>matchMedia('(prefers-reduced-motion: reduce)').matches;
const svg=(body,box='0 0 600 300')=>'<svg viewBox="'+box+'" aria-hidden="true">'+body+'</svg>';
function serviceGraphic(){
 const id='ps-service-'+(++serial);
 return `<svg class="ps-service-svg" viewBox="0 0 960 410" role="img" aria-label="Задание поступает агенту, агент собирает услугу и передаёт готовый результат" xmlns="http://www.w3.org/2000/svg">
 <defs>
  <linearGradient id="${id}-metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#615641"/><stop offset=".35" stop-color="#2b261d"/><stop offset=".75" stop-color="#17140f"/><stop offset="1" stop-color="#3b3426"/></linearGradient>
  <linearGradient id="${id}-paper" x2=".8" y2="1"><stop stop-color="#302a1e"/><stop offset="1" stop-color="#12100b"/></linearGradient>
  <linearGradient id="${id}-gold" x2="1" y2="1"><stop stop-color="#fff0a5"/><stop offset=".45" stop-color="#fdd506"/><stop offset="1" stop-color="#91730a"/></linearGradient>
  <radialGradient id="${id}-halo"><stop stop-color="#fdd506" stop-opacity=".16"/><stop offset="1" stop-color="#fdd506" stop-opacity="0"/></radialGradient>
 </defs>
 <ellipse class="ps-core-halo" cx="468" cy="201" rx="182" ry="179" fill="url(#${id}-halo)"/>
 <ellipse cx="468" cy="333" rx="137" ry="17" fill="#000" opacity=".55"/>
 <g stroke-linejoin="round">
  <path d="M29 77h140l31 32v196H29z" fill="#080706" stroke="#514730" stroke-width="2"/>
  <path d="M20 68h140l31 32v196H20z" fill="url(#${id}-paper)" stroke="#a69773" stroke-width="2"/>
  <path d="M160 68v32h31" fill="#51462e" stroke="#a69773" stroke-width="2"/>
  <rect x="43" y="91" width="78" height="7" rx="3" fill="#fdd506"/>
  <path d="M44 117h86" stroke="#74684d" stroke-width="3" stroke-linecap="round"/>
  <g fill="none" stroke="#b2a37e" stroke-width="2"><rect x="43" y="145" width="17" height="17" rx="4"/><rect x="43" y="187" width="17" height="17" rx="4"/><rect x="43" y="229" width="17" height="17" rx="4"/></g>
  <g stroke="#8c8066" stroke-width="4" stroke-linecap="round"><path d="M74 149h79m-79 12h53m-53 30h79m-79 12h60m-60 30h79m-79 12h47"/></g>
  <path d="M44 273h105" stroke="#423a2b" stroke-width="3"/>
 </g>
 <path d="M211 191h123m-10-9 10 9-10 9M606 191h91m-10-9 10 9-10 9" stroke="#51452a" stroke-width="2" fill="none" stroke-linecap="round"/>
 <path class="ps-flow-in" d="M211 191h123" stroke="#fdd506" stroke-width="2.5" fill="none" pathLength="1"/>
 <circle class="ps-packet-in" cx="218" cy="191" r="5" fill="#fff0a1"/>
 <g class="ps-core">
  <path d="m350 81 17-15h208l19 17v218l-18 16H367l-17-16z" fill="#15120c" stroke="#7e7052" stroke-width="2"/>
  <path d="M350 81h227v218H350z" fill="url(#${id}-metal)" stroke="#c0b18f" stroke-width="2.5"/>
  <path d="m577 81 17 2v218l-17-2z" fill="#242017" stroke="#776747" stroke-width="1.5"/>
  <path d="M366 93h195M360 98v185" fill="none" stroke="#e8d8b4" stroke-opacity=".35"/>
  <g fill="#100e0a" stroke="#9b8963" stroke-width="1.5"><circle cx="365" cy="96" r="4"/><circle cx="562" cy="96" r="4"/><circle cx="365" cy="284" r="4"/><circle cx="562" cy="284" r="4"/></g>
  <g stroke="#99845b" stroke-width="3" stroke-linecap="round"><path d="M337 112v20m0 14v20m0 14v20m0 14v20m0 14v20M605 112v20m0 14v20m0 14v20m0 14v20m0 14v20"/></g>
  <path d="M464 66V49" stroke="#ab9671" stroke-width="3"/><circle cx="464" cy="43" r="7" fill="url(#${id}-gold)"/>
  <rect x="376" y="111" width="175" height="87" rx="18" fill="#080a09" stroke="#75664b" stroke-width="2"/>
  <path d="M389 118h146" stroke="#c9be9e" stroke-opacity=".16" stroke-width="2"/>
  <g class="ps-eyes" fill="url(#${id}-gold)"><rect x="408" y="135" width="17" height="21" rx="7"/><rect x="501" y="135" width="17" height="21" rx="7"/></g>
  <path d="M443 171q21 12 41 0" stroke="#fdd506" stroke-width="3" stroke-linecap="round" fill="none"/>
  <g class="ps-core-gear" stroke="#ad9b73" stroke-width="2" fill="none"><circle cx="464" cy="238" r="24"/><circle cx="464" cy="238" r="14"/><path d="M464 207v9m0 44v9m-31-31h9m44 0h9m-53-22 7 7m30 30 7 7m0-44-7 7m-30 30-7 7"/></g>
  <circle cx="464" cy="238" r="5" fill="#fdd506"/>
  <g fill="#a79034"><rect class="ps-stage-light ps-light-1" x="391" y="277" width="38" height="5" rx="2"/><rect class="ps-stage-light ps-light-2" x="445" y="277" width="38" height="5" rx="2"/><rect class="ps-stage-light ps-light-3" x="499" y="277" width="38" height="5" rx="2"/></g>
 </g>
 <path class="ps-flow-out" d="M606 191h91" stroke="#fdd506" stroke-width="2.5" fill="none" pathLength="1"/>
 <circle class="ps-packet-out" cx="612" cy="191" r="5" fill="#fff0a1"/>
 <g class="ps-output-frame">
  <rect x="716" y="54" width="213" height="264" rx="13" fill="#080706" stroke="#52462f" stroke-width="2"/>
  <rect x="707" y="45" width="213" height="264" rx="13" fill="url(#${id}-paper)" stroke="#b19b65" stroke-width="2"/>
  <path d="M707 78h213" stroke="#66583d" stroke-width="1.5"/>
  <g fill="#b8a169"><circle cx="725" cy="61" r="3"/><circle cx="737" cy="61" r="3"/><circle cx="749" cy="61" r="3"/></g>
  <path d="M845 61h54" stroke="#6a5c43" stroke-width="3" stroke-linecap="round"/>
  <g class="ps-result-layer ps-result-1"><rect x="727" y="96" width="173" height="68" rx="5" fill="#fdd506" fill-opacity=".14" stroke="#99812c"/><path d="m737 154 34-35 26 23 29-34 42 46" fill="#fdd506" fill-opacity=".17" stroke="#c5a73e" stroke-width="1.5"/><circle cx="878" cy="114" r="7" fill="#fdd506"/></g>
  <g class="ps-result-layer ps-result-2" stroke="#bdaf8e" stroke-linecap="round"><path d="M728 186h132" stroke-width="5"/><path d="M728 202h173m-173 13h137" stroke-width="3" stroke-opacity=".5"/></g>
  <g class="ps-result-layer ps-result-3" fill="#373020" stroke="#75633a"><rect x="727" y="234" width="49" height="39" rx="5"/><rect x="789" y="234" width="49" height="39" rx="5"/><rect x="851" y="234" width="49" height="39" rx="5"/><path d="M736 245h30m32 0h30m32 0h30" stroke="#fdd506" stroke-width="2"/></g>
 </g>
 <g class="ps-result-seal"><circle cx="900" cy="301" r="31" fill="#171308" stroke="#fdd506" stroke-width="2"/><circle cx="900" cy="301" r="25" fill="url(#${id}-gold)"/><path class="ps-result-check" d="m885 301 10 10 20-23" fill="none" stroke="#19150a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" pathLength="1"/></g>
 <g class="ps-svg-label" fill="#cec9c1" text-anchor="middle"><text x="106" y="379">Задача</text><text x="464" y="379">AI-агент</text><text x="813" y="379">Готовая услуга</text></g>
 </svg>`;
}
function cohort(){return svg(Array.from({length:340},(_,i)=>{
 const x=12+i%20*30,y=10+Math.floor(i/20)*17;
 return '<g class="ps-person" style="--ps-delay:'+Math.floor(i/20)*22+'ms"><circle cx="'+x+'" cy="'+y+'" r="6.3" fill="#fdd506" fill-opacity=".19" stroke="#c6a91d" stroke-width=".7"/><circle cx="'+x+'" cy="'+(y-1.6)+'" r="1.7" fill="#fdd506"/><path d="M'+(x-3)+' '+(y+3.2)+'a3 3 0 0 1 6 0" fill="#fdd506"/></g>';
 }).join(''));}
function waffle(){return svg(Array.from({length:100},(_,i)=>'<rect x="'+(10+i%10*29)+'" y="'+(10+Math.floor(i/10)*29)+'" width="20" height="20" rx="5" fill="'+(i<60?'#fdd506':'#3d372d')+'"/>').join(''),'0 0 300 300');}
function ring(){return svg('<circle cx="150" cy="150" r="122" fill="none" stroke="#383024" stroke-width="14"/><circle class="ps-ring" cx="150" cy="150" r="122" fill="none" stroke="#fdd506" stroke-width="14" stroke-linecap="round" pathLength="100" stroke-dasharray="85 100" transform="rotate(-90 150 150)"/><path d="m105 150 32 32 62-68" fill="none" stroke="#fdd506" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>','0 0 300 300');}
function photo(slot,index){
 const s=slot||{},alt=s.alt||'Фото участника '+(index+1);
 const content=s.src?'<img data-src="'+esc(s.src)+'" alt="'+esc(alt)+'">':'<div class="ps-photo-empty">'+svg('<rect x="17" y="18" width="66" height="62" rx="9"/><circle cx="39" cy="39" r="8"/><path d="m24 70 21-22 15 15 10-11 10 18"/>','0 0 100 100')+'<span>Фото добавим</span></div>';
 const tag=s.num?'<figcaption class="ps-tag"><b>'+esc(s.num)+'</b><span>'+esc(s.cap||'')+'</span></figcaption>':''; /* 03.10: вік + підпис на картці (s145) */
 return '<figure class="ps-photo" aria-label="'+esc(alt)+'">'+content+tag+'</figure>';
}
function photoPair(slots){slots=slots||[];if(slots.length===1)return '<div class="ps-photo-pair ps-single">'+photo(slots[0],0)+'</div>';return '<div class="ps-photo-pair">'+[0,1].map(i=>photo(slots[i],i)).join('')+'</div>';}
function parse(s){
 const tmp=document.createElement('div');tmp.innerHTML=s.b;
 const stats=[...tmp.querySelectorAll('.fd-stats>div')].map(el=>({metric:el.querySelector('b').textContent,caption:el.querySelector('span').textContent}));
 const final=tmp.querySelector(':scope>p').textContent;let at=final.indexOf('Включились');if(at<0)at=final.length; /* 01.10: підсумок можна прибрати */
 return {steps:[stats[0],stats[2],stats[1],stats[3]],people:final.slice(0,at).trim(),closing:final.slice(at).trim()};
}
function create(source,config={}){
 const data=parse(source),root=document.createElement('div');root.className='participant-story';
 const photos=config.photos||{};
 /* 01.10: incomeVideo — скрін у мокапі iPhone + слот вертикального скринкасту (з'являється сам, коли файл є) */
 const phone=v=>{const s=(photos.income||[])[0]||{};return '<div class="ps-iphone"><i class="ps-btn a"></i><i class="ps-btn b"></i><i class="ps-btn c"></i><i class="ps-btn d"></i><div class="ps-iscreen">'+(s.src?'<img data-src="'+esc(s.src)+'" alt="'+esc(s.alt||'')+'">':'')+'<video src="'+esc(v)+'" autoplay muted loop playsinline preload="auto" onloadeddata="this.parentNode.classList.add(\'has-video\')"></video></div></div>';};
 const visuals=[cohort(),waffle(),serviceGraphic(),'<div class="ps-income-ring">'+ring()+'</div>'+(photos.incomeVideo?phone(photos.incomeVideo):photoPair(photos.income))];
 const names=['cohort','baseline','service','income'];
 root.innerHTML=data.steps.map((s,i)=>'<section class="ps-panel ps-'+names[i]+(i===3&&photos.incomeVideo?' ps-phone-mode':'')+'" data-ps-step="'+i+'" hidden><div class="ps-copy"><p class="ps-metric'+(i===2?' ps-word':'')+'">'+esc(s.metric)+'</p><p class="ps-caption">'+esc(s.caption)+'</p></div><div class="ps-visual">'+visuals[i]+'</div></section>').join('')+
 '<section class="ps-panel ps-experience" data-ps-step="4" hidden><div class="ps-visual">'+photoPair(photos.experience)+'</div><p class="ps-people">'+esc(data.people)+'</p><p class="ps-closing">'+esc(data.closing).replace('система срабатывает','<em>система срабатывает</em>')+'</p></section>'+
 '<nav class="ps-rail" aria-label="Этапы этого слайда">'+['Участники','До старта','Первая услуга','Первые деньги','Разный опыт'].map((t,i)=>'<button type="button" data-ps-nav="'+i+'">'+t+'</button>').join('')+'</nav>';
 root.addEventListener('click',e=>{
  const b=e.target.closest('[data-ps-nav]');if(!b)return;
  e.stopPropagation();root.dispatchEvent(new CustomEvent('participantstep',{bubbles:true,detail:Number(b.dataset.psNav)}));
 });
 root.addEventListener('keydown',e=>{
  if(!e.target.closest('button'))return;
  if(e.key==='Enter'||e.key===' ')e.stopPropagation();
  else if(/^(Arrow|Page|Home$|End$)/.test(e.key))e.target.blur();
 });
 setStep(root,0,false);return root;
}
function getRoot(host){return host.classList.contains('participant-story')?host:host.querySelector('.participant-story');}
function setStep(host,n,animate=true){
 const root=getRoot(host);if(!root)return;
 n=Math.max(0,Math.min(4,Number(n)||0));root.dataset.psCurrent=n;
 root.querySelectorAll('[data-ps-step]').forEach(panel=>{
  panel.classList.remove('ps-animate');const current=Number(panel.dataset.psStep)===n;
  panel.hidden=!current;panel.classList.toggle('is-active',current);panel.setAttribute('aria-hidden',String(!current));
  if(current){
   panel.querySelectorAll('img[data-src]').forEach(im=>{im.src=im.dataset.src;delete im.dataset.src;});
   if(animate&&!reduced()){void panel.offsetWidth;panel.classList.add('ps-animate');}
  }
 });
 root.querySelectorAll('[data-ps-nav]').forEach(b=>{const k=Number(b.dataset.psNav);b.setAttribute('aria-current',k===n?'step':'false');b.classList.toggle('is-done',k<n);});
}
window.ParticipantStory={create,setStep,serviceGraphic};
})();
