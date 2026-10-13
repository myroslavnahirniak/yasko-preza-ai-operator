/* Scoped renderer: only source IDs explicitly selected in overrides use this design. */
(function(){
'use strict';
const original=window.Foundation.render;
const esc=s=>String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const lazy=h=>String(h||'').replace(/\s(src|poster)=(['"])(assets\/)/g,' data-$1=$2$3');
window.Foundation.render=function(s,idx){
 const c=s.foundation&&s.foundation.block129;
 if(!c)return original(s,idx);
 const el=document.createElement('section');
 el.className='slide foundation b129 b13-'+c.kind+' b13-g'+s.googleNumber;
 el.dataset.idx=idx;el.dataset.google=s.googleNumber;el.dataset.lv=s.lv;el._s=s;
 if(s.t.replace(/<[^>]+>/g,'').length>76)el.classList.add('b13-long');
 const address=c.demoURL?'<a class="b13-demo-link" href="'+esc(c.demoURL)+'" target="_blank" rel="noopener">'+esc(c.demoURL.replace(/^https?:\/\//,'').replace(/\/$/,''))+' <span aria-hidden="true">↗</span></a>':'';
 el.innerHTML='<div class="b13-shell">'+(s.t||c.eyebrow?'<header class="b13-head">'+(c.eyebrow?'<p class="b13-eyebrow">'+esc(c.eyebrow)+'</p>':'')+(s.t?'<h1 class="split-done">'+s.t+'</h1>':'')+'</header>':'')+'<div class="b13-body">'+lazy(s.b)+'</div>'+address+'</div>'+(s.disc?'<div class="b13-disclaimer">Результаты индивидуальны и не являются гарантией</div>':'');
 el.querySelectorAll('a').forEach(a=>a.addEventListener('click',e=>e.stopPropagation()));
 el.querySelectorAll('.fd-bars>div').forEach((row,i)=>row.insertAdjacentHTML('beforeend','<b class="b13-bar-value">'+(i?'1×':'8×')+'</b>'));
 el.querySelectorAll('.fd-table td:nth-child(4),.fd-table td:nth-child(5)').forEach(td=>{const v=Number(td.textContent);if(v)td.style.setProperty('--score',v/10);});
 return el;
};
})();
