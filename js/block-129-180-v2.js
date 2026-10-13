/* Large visual scenes and presenter-controlled focus. Only the explicit block129.v2 IDs opt in. */
(function(){
'use strict';
const original=window.Foundation.render;
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const staticFrame=new URLSearchParams(location.search).has('frame');
const $=(el,s)=>[...el.querySelectorAll(s)];
let active=null, animations=[];
function stop(){animations.forEach(a=>a.cancel());animations=[];}
function motion(el,keyframes,options){
 if(!el||reduced.matches||staticFrame)return;
 // 09.10: свій transform елемента (translate(-50%) для центрування тощо) зберігаємо — інакше на час анімації він зникав і блок стрибав
 const base=getComputedStyle(el).transform;
 if(base&&base!=='none')keyframes=keyframes.map(k=>k.transform?{...k,transform:k.transform+' '+base}:k);
 const a=el.animate(keyframes,{duration:650,easing:'cubic-bezier(.22,.7,.2,1)',...options});
 a.id='block129-scene';
 animations.push(a);return a;
}
function art(c){
 const frame=document.createElement('div');frame.className='b13-art';
 c.art.forEach((a,i)=>{
  const wrap=document.createElement('div');wrap.className='b13-art-frame';wrap.dataset.artIndex=i;
  const im=document.createElement('img');im.dataset.src=a.src;im.alt=a.alt;
  wrap.append(im);frame.append(wrap);
 });return frame;
}
window.Foundation.render=function(s,idx){
 const el=original(s,idx), c=s.foundation&&s.foundation.block129;
 if(!c||!c.v2)return el;
 el.classList.add('b13-v2','b13-v2-'+c.layout);
 el._b13=c;el._b13Step=0;
 if(c.layout==='participant-story'){
  el.querySelector('.b13-body').replaceChildren(window.ParticipantStory.create(s,c));
  el.classList.toggle('ps-static',staticFrame);
  el.addEventListener('participantstep',e=>{e.stopPropagation();stop();setState(el,e.detail,true);});
 }
 if(c.layout==='goal-chain'){
  const body=el.querySelector('.b13-body'),claim=body.querySelector('.goal-thesis'),meaning=body.querySelector('.goal-meaning');
  const icons=[
   '<rect x="7" y="9" width="26" height="23" rx="6"/><path d="M20 4v5M3 18v8m34-8v8M14 25h12"/><circle cx="14" cy="18" r="1"/><circle cx="26" cy="18" r="1"/>',
   '<rect x="5" y="9" width="30" height="26" rx="4"/><path d="M11 5v8m18-8v8M5 17h30m-20 9 4 4 8-9"/>',
   '<circle cx="20" cy="20" r="15"/><circle cx="20" cy="20" r="8"/><path d="m16 20 3 3 7-8"/>'
  ];
  $(body,'.goal-prelude br,.goal-meaning br,.goal-next br').forEach(br=>br.replaceWith(document.createTextNode(' ')));
  const chain=document.createElement('div');chain.className='goal-chain';body.insertBefore(chain,claim);
  [claim,...$(meaning,'p')].forEach((copy,i)=>{
   const row=document.createElement('article');row.className='goal-chain-row';
   row.innerHTML='<svg viewBox="0 0 40 40" aria-hidden="true">'+icons[i]+'</svg>';
   row.append(copy);chain.append(row);
  });
  meaning.remove();
 }
 if(c.art){
  const a=art(c);
  if(c.layout==='visual-compare'){
   const cols=$(el,'.duo .col');$(a,'.b13-art-frame').forEach((im,i)=>{im.classList.add('b13-compare-art');cols[i].prepend(im);});
  }else el.prepend(a);
 }
 if(c.layout==='templates-real'){
  const fan=document.createElement('div');fan.className='b13-template-fan';fan.setAttribute('aria-hidden','true');
  ['2817','2818'].forEach((id,i)=>{
   const img=document.createElement('img');img.dataset.src='assets/google-source/g171-g3f9b3adf0b8_0_'+id+'.png';img.alt='';fan.append(img);
  });el.prepend(fan);
 }
 if(c.layout==='service-table'){
  // Price sits with its service, leaving room for readable demand/competition columns.
  const tr=el.querySelector('thead tr');tr.children[0].innerHTML='Услуга <span>· стоимость</span>';tr.children[1].remove();
  $(el,'tbody tr').forEach(row=>{const cost=row.children[1];const p=document.createElement('span');p.className='b13-price';p.textContent=cost.textContent;row.children[0].append(p);cost.remove();});
 }
 if(c.layout==='roads')el.querySelector('.duo').insertAdjacentHTML('beforebegin','<svg class="b13-road-fork" viewBox="0 0 800 60" aria-hidden="true"><path d="M400 0C400 32 190 15 190 60"/><path class="b13-yellow" d="M400 0C400 32 610 15 610 60"/><circle cx="400" cy="6" r="6"/></svg>');
 if(c.steps){
  el._b13Focus=$(el,c.focus);if(c.reverseFocus)el._b13Focus.reverse();
  el._b13Focus.forEach((n,i)=>{n.classList.add('b13-focus-item');n.dataset.focus=i;});
  const dots=document.createElement('div');dots.className='b13-step-dots';dots.setAttribute('aria-hidden','true');
  c.steps.forEach(()=>dots.append(document.createElement('i')));el.append(dots);
 }
 setState(el,0,false);
 return el;
};
function setState(el,step,animate){
 const c=el._b13;if(!c)return;
 const prior=el._b13Step;el._b13Step=step;el.dataset.b13Step=step;
 if(c.layout==='participant-story')window.ParticipantStory.setStep(el,step,animate&&!staticFrame);
 (el._b13Focus||[]).forEach((n,i)=>{
  const on=i===step;n.classList.toggle('is-focus',on);
  if(animate&&on&&c.layout!=='participant-story'&&c.layout!=='jobs')motion(n,[{opacity:.55,transform:'translateX(-6px)'},{opacity:1,transform:'translateX(0)'}],{duration:420});
 });
 const frames=$(el,'.b13-art>.b13-art-frame');
 frames.forEach((n,i)=>{
  const on=frames.length===1||i===step;n.classList.toggle('is-current',on);
  n.setAttribute('aria-hidden',String(!on));
  if(animate&&on&&prior!==step)motion(n,[{opacity:0,transform:'translateY(12px) scale(.965)'},{opacity:1,transform:'translateY(0) scale(1)'}],{duration:560});
 });
 $(el,'.b13-step-dots i').forEach((n,i)=>n.classList.toggle('is-current',i===step));
 if(c.layout==='waves'){
  $(el,'.b13-waves>path').forEach((p,i)=>{p.style.opacity=i<=step?1:.22;});
  if(animate){const p=$(el,'.b13-waves>path')[step];if(p){const l=p.getTotalLength();motion(p,[{strokeDasharray:l,strokeDashoffset:l},{strokeDasharray:l,strokeDashoffset:0}],{duration:850});}}
 }
}
function enter(el,dir){
 stop();active=el;if(!el||!el._b13)return;
 const c=el._b13,last=(c.steps||[]).length-1;
 setState(el,dir<0||staticFrame?Math.max(0,last):0,false);
 if(c.layout==='participant-story'){
  window.ParticipantStory.setStep(el,el._b13Step,!reduced.matches&&!staticFrame);
  return;
 }
 if(reduced.matches||staticFrame)return;
 motion(el.querySelector('.b13-head'),[{opacity:0,transform:'translateY(14px)'},{opacity:1,transform:'translateY(0)'}],{duration:550});
 const picture=el.querySelector('.b13-art,.b13-template-fan');
 if(picture)motion(picture,[{opacity:0,transform:'translateY(20px) scale(.96)'},{opacity:1,transform:'translateY(0) scale(1)'}],{duration:1050,delay:100});
 const blocks=$(el,'.b13-body>p,.b13-photo,.fd-site-grid>figure,.fd-stats>div,.b13-body>.duo,.b13-body>.b13-market');
 blocks.forEach((n,i)=>motion(n,[{opacity:.3,transform:'translateY(12px)'},{opacity:1,transform:'translateY(0)'}],{delay:130+i*80,duration:620}));
 $(el,'.fd-bars i').forEach((n,i)=>{n.style.transformOrigin='left center';motion(n,[{transform:'scaleX(.04)'},{transform:'scaleX(1)'}],{delay:250+i*230,duration:1200});});
 $(el,'.b13-viz path,.b13-road-fork path').forEach((p,i)=>{
  if(p.classList.contains('b13-wave-fill')||p.classList.contains('b13-map-road'))return;
  const l=p.getTotalLength();motion(p,[{strokeDasharray:l,strokeDashoffset:l},{strokeDasharray:l,strokeDashoffset:0}],{delay:200+Math.min(i,8)*70,duration:1200});
 });
 $(el,'.b13-dotmatrix i.lit').forEach((n,i)=>motion(n,[{opacity:.1,transform:'scale(.45)'},{opacity:1,transform:'scale(1)'}],{delay:250+i*17,duration:420}));
}
function advance(el,direction){
 if(!el||!el._b13||!el._b13.steps)return false;
 const step=el._b13Step+direction;
 if(step<0||step>=el._b13.steps.length)return false;
 stop();setState(el,step,true);return true;
}
function finish(el){if(!el||!el._b13)return;stop();setState(el,Math.max(0,(el._b13.steps||[]).length-1),false);}
function cue(el){return el&&el._b13&&el._b13.steps?'Крок '+(el._b13Step+1)+' / '+el._b13.steps.length+' · '+el._b13.steps[el._b13Step]:'';}
reduced.addEventListener('change',()=>{stop();if(active&&active._b13)setState(active,active._b13Step,false);});
window.Block129={enter,advance,finish,cue,snapshot:el=>el&&el._b13?el._b13Step:null,restore:(el,n)=>{if(el&&el._b13){stop();setState(el,n,false);}}};
})();
