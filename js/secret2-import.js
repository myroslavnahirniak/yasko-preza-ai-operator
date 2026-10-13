(function(){
window.Secret2Import={render:function(s,idx){
 const sec=document.createElement('section');sec._s=s;sec.className='slide secret2-import';sec.dataset.idx=idx;sec.dataset.lv=s.lv||6;
 const f=document.createElement('iframe');f.title=s.t.replace(/<[^>]*>/g,'');f.dataset.importSrc=s.foundation.importedLocal?('secret2.html?n='+s.foundation.importedHTML+'&clean&embed&v=1009r89'):('source/import-secret2/slide.html?square&clean&v=design3&source='+s.foundation.importedHTML);f.setAttribute('allow','autoplay; fullscreen');sec.appendChild(f);
 /* 09.10: iframe вантажиться заздалегідь, коли дека гідрує сусідні слайди (data-hyd, −1…+3), і не скидається при виході — раніше сторінка вантажилась з нуля в момент переходу (лаг). На вході анімація появи всередині перезапускається. Таких екранів у деці 3, без відео */
 const load=()=>{if(!f.hasAttribute('src'))f.src=f.dataset.importSrc};
 const replay=()=>{try{const d=f.contentDocument;if(d&&d.readyState==='complete')d.getAnimations().forEach(a=>{a.cancel();a.play()})}catch(e){}};
 let was=false;const obs=new MutationObserver(()=>{const on=sec.classList.contains('on');if(on&&!was){if(f.hasAttribute('src'))replay();else load()}else if(sec.dataset.hyd)load();was=on});obs.observe(sec,{attributes:true,attributeFilter:['class','data-hyd']});return sec;
}};
window.addEventListener('message',function(e){if(e.origin!==location.origin||!e.data||e.data.type!=='secret2-import-nav')return;const f=document.querySelector('.secret2-import.on iframe');if(!f||e.source!==f.contentWindow)return;document.dispatchEvent(new KeyboardEvent('keydown',{key:e.data.key,bubbles:true}));});
})();