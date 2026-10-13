/* Source-bound camera scene. Other Block129 slides keep their original controller. */
(function(){
'use strict';
const render=window.Foundation.render, block=window.Block129;
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const staticFrame=new URLSearchParams(location.search).has('frame');
const positions=[[0,0,0,0],[42,110,-25,-24],[-20,220,-50,24]];
const introPose=[12,125,-25,.205,9,8];
const lastStep=positions.length-1;
const paths=[[[10,33,0],[10,55,-8],[42,67,-20],[42,78,-25]],[[42,143,-25],[42,166,-32],[-20,181,-44],[-20,188,-50]]];
let active=null;
const cfg=el=>(el._s&&el._s.foundation&&el._s.foundation.block129)||{};
const startOf=el=>Math.max(0,Math.min(lastStep,+cfg(el).s133Start||0));
const locked=el=>!!cfg(el).s133Lock;
const owns=el=>!!(el&&el._s133);
function camera(step){
 return cameraTransform([...positions[step].slice(0,3),1,0,-positions[step][3]]);
}
function cameraTransform(p){
 return `scale(${p[3]}) rotateX(${p[4]}deg) rotateY(${p[5]}deg) translate3d(${-p[0]}cqw,${-p[1]}cqw,${-p[2]}cqw)`;
}
function cancel(el){if(owns(el)&&el._s133.motion){el._s133.motion.cancel();el._s133.motion=null;}}
function move(el,step,animate,from){
 const state=el._s133;
 const current=from||getComputedStyle(state.world).transform;
 cancel(el);
 state.step=Math.max(0,Math.min(lastStep,step));
 el.dataset.level=state.step;
 state.world.style.transform=camera(state.step);
 state.cards.forEach((card,i)=>{
  card.classList.toggle('is-current',i===state.step);
  card.setAttribute('aria-hidden',String(i!==state.step));
 });
 el.querySelectorAll('[data-level]').forEach(button=>button.setAttribute('aria-pressed',String(Number(button.dataset.level)===state.step)));
 state.status.textContent=`Секрет 0${state.step+1} / 03`;
 const duration=from?1750:1250;
 el.style.setProperty('--sl133-delay',duration+'ms');
 if(animate&&!reduced.matches&&!staticFrame){
  const animation=state.world.animate([{transform:current},{transform:camera(state.step)}],{duration,easing:'cubic-bezier(.5,0,.15,1)'});
  state.motion=animation;
  animation.onfinish=()=>{if(state.motion===animation)state.motion=null;};
 }
}
window.Foundation.render=function(s,idx){
 const el=render(s,idx);
 if(s.foundation?.block129?.layout!=='secrets-levels')return el;
 el.classList.add('s133-levels');
 const world=el.querySelector('.sl133-world');
 const cards=[...el.querySelectorAll('.sl133-station')];
 const connectors=el.querySelector('.sl133-connectors');
 paths.forEach(points=>points.slice(0,-1).forEach((p,i)=>{
  const next=points[i+1],dx=next[0]-p[0],dy=next[1]-p[1],dz=next[2]-p[2],xy=Math.hypot(dx,dy);
  const line=document.createElement('div');line.className='sl133-link';line.style.width=Math.hypot(xy,dz)+'cqw';
  line.style.transform=`translate3d(${p[0]}cqw,${p[1]}cqw,${p[2]}cqw) rotateZ(${Math.atan2(dy,dx)*180/Math.PI}deg) rotateY(${-Math.atan2(dz,xy)*180/Math.PI}deg)`;
  connectors.append(line);
 }));
 cards.forEach((card,i)=>{const p=positions[i];card.style.transform=`translate3d(${p[0]}cqw,${p[1]}cqw,${p[2]}cqw) translate(-50%,-50%) rotateY(${p[3]}deg)`;});
 el._s133={step:0,world,cards,status:el.querySelector('.sl133-status'),motion:null};
 el.querySelectorAll('[data-level]').forEach(button=>{
  button.addEventListener('click',e=>{e.stopPropagation();move(el,Number(button.dataset.level),true);});
  button.addEventListener('keydown',e=>{
   if(e.key===' '||e.key==='Enter')e.stopPropagation();
   else if(['ArrowRight','ArrowLeft','ArrowUp','ArrowDown','PageDown','PageUp'].includes(e.key))button.blur();
  });
 });
 move(el,0,false);
 return el;
};
window.Block129={
 ...block,
 enter(el,dir){
  if(active)cancel(active);active=owns(el)?el:null;
  block.enter(el,dir);
  if(!owns(el))return;
  /* 08.10: копія сцени, що стоїть на одній станції (напр. «Секрет №2» = станція 02): прольот від попередньої станції, кроків нема */
  const st=startOf(el);
  if(st>0){move(el,st,dir>=0&&!staticFrame,dir>=0?camera(st-1):null);return;}
  move(el,dir<0||staticFrame?lastStep:0,dir>=0,dir>=0?cameraTransform(introPose):null);
 },
 advance(el,direction){
  if(!owns(el))return block.advance(el,direction);
  if(locked(el))return false;
  const step=el._s133.step+direction;
  if(step<0||step>lastStep)return false;
  move(el,step,true);return true;
 },
 finish(el){if(owns(el))move(el,locked(el)?startOf(el):lastStep,false);else block.finish(el);},
 cue(el){return owns(el)?`Крок ${el._s133.step+1} / 3 · ${el._s.foundation.block129.steps[el._s133.step]}`:block.cue(el);},
 snapshot(el){return owns(el)?el._s133.step:block.snapshot(el);},
 restore(el,n){if(owns(el))move(el,n,false);else block.restore(el,n);}
};
reduced.addEventListener('change',()=>{if(active)move(active,active._s133.step,false);});
})();
