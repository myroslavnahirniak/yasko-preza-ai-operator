/* Shared vector animatic for p111/p112 and solid SVG objects for Google144. */
(function(){
'use strict';
let serial=0;
const esc=s=>String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
function materials(id){return `<defs>
 <linearGradient id="${id}-metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#7a756a"/><stop offset=".28" stop-color="#38362f"/><stop offset=".7" stop-color="#151613"/><stop offset="1" stop-color="#484335"/></linearGradient>
 <linearGradient id="${id}-edge" x2="1" y2="1"><stop stop-color="#f7efd7"/><stop offset=".35" stop-color="#8a816c"/><stop offset="1" stop-color="#383329"/></linearGradient>
 <linearGradient id="${id}-gold" x2=".8" y2="1"><stop stop-color="#fff4ac"/><stop offset=".35" stop-color="#fdd506"/><stop offset=".8" stop-color="#b58b06"/><stop offset="1" stop-color="#6c5108"/></linearGradient>
 <linearGradient id="${id}-glass" x2=".7" y2="1"><stop stop-color="#322d20"/><stop offset=".5" stop-color="#0d100e"/><stop offset="1" stop-color="#191c16"/></linearGradient>
 <linearGradient id="${id}-side"><stop stop-color="#161712"/><stop offset="1" stop-color="#494331"/></linearGradient>
 <radialGradient id="${id}-light"><stop stop-color="#fdd506" stop-opacity=".23"/><stop offset="1" stop-color="#fdd506" stop-opacity="0"/></radialGradient>
 </defs>`;}
function plinth(id){return `<ellipse cx="150" cy="246" rx="139" ry="23" fill="#000" opacity=".65"/><path d="m10 203 140-51 140 51v23l-140 53L10 226z" fill="#14140f" stroke="#70644b"/><path d="m10 203 140-51 140 51-140 51z" fill="url(#${id}-metal)" stroke="#b2a487"/><path d="M150 254v25m-140-53 140 53 140-53" fill="none" stroke="#524933"/><path d="m25 208 125 47 125-47" fill="none" stroke="#fdd506" stroke-opacity=".5" stroke-width="2"/>`;}
function robot(id,small=false){return `<g class="op-robot" ${small?'transform="translate(48 60) scale(.68)"':''}>
 <ellipse cx="150" cy="221" rx="66" ry="14" fill="#000" opacity=".6"/>
 <path d="M101 172h99l-6 35-36 15-50-12z" fill="url(#${id}-metal)" stroke="#a99f88" stroke-width="1.3"/>
 <path d="m187 137 24 15 13 39-17 11-24-28" fill="url(#${id}-side)" stroke="#82765b"/>
 <g class="op-hand"><path d="m106 140-24 8-8 40 18 13 27-30" fill="url(#${id}-metal)" stroke="#b0a38a"/><circle cx="87" cy="182" r="13" fill="url(#${id}-metal)" stroke="#d3c8ac"/><path d="m80 184 15-4" stroke="#fdd506" stroke-width="3"/></g>
 <rect x="110" y="126" width="84" height="75" rx="20" fill="url(#${id}-metal)" stroke="#afa48b" stroke-width="1.4"/>
 <circle cx="151" cy="162" r="20" fill="#12150f" stroke="#807449"/><circle class="op-core" cx="151" cy="162" r="11" fill="url(#${id}-gold)"/>
 <path d="M121 188h58" stroke="#706746" stroke-width="3"/>
 <path d="M144 40V28" stroke="#d4c8a2" stroke-width="3"/><circle cx="144" cy="23" r="6" fill="url(#${id}-gold)"/>
 <path d="m91 52 16-12h94l18 16v65l-18 14h-95l-15-15z" fill="url(#${id}-side)" stroke="#8c7f64"/>
 <rect x="88" y="48" width="119" height="79" rx="24" fill="url(#${id}-metal)" stroke="url(#${id}-edge)" stroke-width="2"/>
 <rect x="99" y="59" width="97" height="56" rx="17" fill="#080c09" stroke="#8d846c"/>
 <path d="M111 65h72" stroke="#e6dec4" stroke-opacity=".16"/>
 <g class="op-eyes" fill="url(#${id}-gold)"><rect x="119" y="76" width="10" height="16" rx="5"/><rect x="166" y="76" width="10" height="16" rx="5"/></g>
 <path d="M139 98q10 6 19 0" fill="none" stroke="#fdd506" stroke-width="2" stroke-linecap="round"/>
 <path d="M82 73v27m131-27v27" stroke="#b49b64" stroke-width="5" stroke-linecap="round"/>
 </g>`;}
function screen(id,type){
 let inner='';
 if(type===0)inner=`<rect x="25" y="45" width="158" height="60" rx="5" fill="#bfa122" fill-opacity=".22"/><path d="M37 65h61m-61 12h45" stroke="#eee3c0" stroke-width="4" stroke-linecap="round"/><rect x="37" y="88" width="37" height="7" rx="3" fill="#fdd506"/><path d="m122 92 19-31 23 31z" fill="url(#${id}-gold)"/><circle cx="152" cy="59" r="7" fill="#f5e5a3"/><g class="op-result"><rect x="25" y="117" width="46" height="36" rx="5" fill="#544c2e"/><rect x="81" y="117" width="46" height="36" rx="5" fill="#544c2e"/><rect x="137" y="117" width="46" height="36" rx="5" fill="#544c2e"/></g><path d="M25 166h158" stroke="#8f856e" stroke-width="3"/>`;
 if(type===1)inner=`<rect x="25" y="44" width="158" height="128" rx="6" fill="#231f13"/><ellipse cx="103" cy="143" rx="41" ry="10" fill="#050603"/><path d="m73 90 31-16 32 16v46l-32 17-31-17z" fill="url(#${id}-gold)" stroke="#f7e397"/><path d="m73 90 31 16 32-16m-32 16v47" stroke="#7e6414"/><path d="M37 59h58m-58 9h35" stroke="#d4c9a6" stroke-width="3"/><g class="op-result" fill="none" stroke="#fdd506" stroke-width="2"><path d="M64 83v-8h10m64 0h9v9m0 55v9h-9m-64 0H64v-9"/><path d="m157 54 3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/></g>`;
 if(type===2)inner=`<rect x="25" y="48" width="107" height="33" rx="10" fill="#3c382a"/><path d="M37 60h68m-68 10h43" stroke="#cec4a9" stroke-width="3"/><rect x="65" y="92" width="118" height="38" rx="10" fill="#fdd506" fill-opacity=".18" stroke="#8c7425"/><path d="M78 106h79m-79 11h53" stroke="#fdd506" stroke-width="3"/><g class="op-result"><rect x="25" y="142" width="90" height="27" rx="10" fill="#3c382a"/><circle cx="45" cy="155" r="3" fill="#b7a97d"/><circle cx="57" cy="155" r="3" fill="#b7a97d"/><circle cx="69" cy="155" r="3" fill="#b7a97d"/><circle cx="162" cy="154" r="14" fill="url(#${id}-gold)"/><path d="m155 154 5 5 10-11" stroke="#28210c" stroke-width="2" fill="none"/></g>`;
 return `<g class="op-screen"><path d="M20 8h179l14 12v160l-14 12H20z" fill="#171712" stroke="#756b50"/><rect x="8" y="8" width="191" height="184" rx="12" fill="url(#${id}-glass)" stroke="url(#${id}-edge)" stroke-width="1.7"/><path d="M8 32h191" stroke="#6f6246"/><g fill="#b6a678"><circle cx="22" cy="21" r="2.5"/><circle cx="32" cy="21" r="2.5"/><circle cx="42" cy="21" r="2.5"/></g>${inner}<path class="op-scan" d="M25 43h158" stroke="#fdd506" stroke-width="2" opacity="0"/></g>`;
}
function studio(){
 const id='op-studio-'+(++serial);
 const nodes=[{x:42,y:590},{x:353,y:535},{x:664,y:590}];
 return `<svg class="op-studio-svg" viewBox="0 0 1000 1000" role="img" aria-label="Три AI-агента создают сайт, рекламный креатив и чат-бота" xmlns="http://www.w3.org/2000/svg">${materials(id)}
 <ellipse cx="500" cy="690" rx="580" ry="390" fill="url(#${id}-light)"/>
 <path d="M0 846 500 658l500 188M0 918l500-188 500 188M150 1000l350-134 350 134M98 778l402 152 402-152M282 706l218 81 218-81" stroke="#746640" stroke-opacity=".11" fill="none"/>
 <path d="M188 824 500 740 813 824 500 932z" stroke="#a98b24" stroke-opacity=".5" stroke-width="2" fill="none"/>
 <circle class="op-orbit" r="5" fill="#fdd506"/>
 ${nodes.map((p,i)=>`<g class="op-station op-station-${i}" transform="translate(${p.x} ${p.y})"><ellipse class="op-aura" cx="150" cy="162" rx="160" ry="190" fill="url(#${id}-light)"/>${plinth(id)}<g transform="translate(36 -107) rotate(-5 106 100)">${screen(id,i)}</g><g transform="translate(0 45)">${robot(id)}</g></g>`).join('')}
 </svg>`;
}
function demand(id){return `<ellipse cx="160" cy="192" rx="112" ry="22" fill="#000" opacity=".5"/>
 <path d="m25 164 130-45 140 45-133 48z" fill="url(#${id}-metal)" stroke="#b2a487"/>
 <path d="m25 164 137 48v12L25 177zm137 48 133-48v13l-133 47" fill="#27261c" stroke="#736346"/>
 ${[0,1,2].map((n)=>{const x=65+n*63,h=42+n*33,y=167-n*10;return `<g class="op-demand-bar" style="--op-n:${n}"><path d="m${x} ${y-h} 27-11 24 10-27 12z" fill="url(#${id}-gold)"/><path d="m${x} ${y-h} 24 11v${h}l-24-12z" fill="${n===2?'#d5ab0c':'#77632a'}"/><path d="m${x+24} ${y-h+11} 27-12v${h}l-27 12z" fill="${n===2?'#8e6d09':'#423a22'}"/></g>`;}).join('')}
 <path d="M45 93 117 64l49 9 73-53m-35 5 35-5-3 33" stroke="url(#${id}-gold)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;}
function market(id){return `<ellipse cx="160" cy="190" rx="120" ry="22" fill="#000" opacity=".55"/>
 <path d="m23 153 126-51 143 51-133 57z" fill="url(#${id}-metal)" stroke="#b2a487"/><path d="m23 153 136 57 133-57v15l-133 57-136-57z" fill="#232119" stroke="#6f6040"/>
 ${[[49,111,49],[106,90,68],[207,122,43]].map(([x,y,h])=>`<path d="m${x} ${y-h} 25-9 23 10v${h}l-23 11-25-12z" fill="url(#${id}-metal)" stroke="#9d9279"/><path d="m${x} ${y-h} 25 11 23-10m-23 10v${h}" stroke="#675e4a" fill="none"/>`).join('')}
 <path class="op-market-slot" d="m122 155 43-17 42 17-43 20z" fill="#fdd506" fill-opacity=".12" stroke="#fdd506" stroke-width="2"/>
 <path d="m122 155 0-30 43-17 42 17v30M165 108v30" fill="none" stroke="#fdd506" stroke-opacity=".5" stroke-dasharray="4 5"/>
 <path d="M163 70v25m-12-12h24" stroke="url(#${id}-gold)" stroke-width="6" stroke-linecap="round"/>`;}
function opportunityObject(type){
 const id='op-object-'+(++serial);
 return `<svg class="op-object" viewBox="0 0 320 240" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">${materials(id)}<ellipse cx="160" cy="130" rx="156" ry="112" fill="url(#${id}-light)"/>${type===0?demand(id):type===1?market(id):`<g transform="translate(10 -3)">${plinth(id)}<g transform="translate(18 -6) scale(.89)">${robot(id)}</g></g>`}</svg>`;
}
window.OpportunityStudio={studio,opportunityObject};
if(!window.Foundation)return;
const original=window.Foundation.render;
window.Foundation.render=function(s,idx){
 const el=original(s,idx),c=s.foundation&&s.foundation.block129;
 if(!c||!['studio-loop','studio-quote','opportunity-3d'].includes(c.layout))return el;
 el.classList.add('op-designed');
 if(c.layout==='opportunity-3d'){
  el.querySelectorAll('.route .rt').forEach((row,i)=>{
   const number=row.querySelector('i');number.setAttribute('aria-label','Условие '+(i+1));
   const visual=document.createElement('div');visual.className='op-condition-visual';visual.innerHTML=opportunityObject(i);row.prepend(visual);
  });
 }else{
  const media=document.createElement('div');media.className='op-studio-backdrop';
  media.innerHTML=c.video?'<video data-src="'+esc(c.video)+'" '+(c.poster?'data-poster="'+esc(c.poster)+'" ':'')+'data-reduced-poster muted loop playsinline preload="none" aria-label="AI-агенты выполняют разные услуги"></video>':studio();
  el.prepend(media);
 }
 return el;
};
})();
