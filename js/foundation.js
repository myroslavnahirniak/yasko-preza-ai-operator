/* Google 1–180 baseline. Copy remains data; motion never creates extra slides. */
(function(){
'use strict';
function esc(t){return String(t||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');}
function lazy(h){return String(h||'').replace(/\s(src|poster)=(['"])(assets\/)/g,' data-$1=$2$3');}
function plain(h){var el=document.createElement('div');el.innerHTML=h||'';return el.textContent.trim();}
function clean(h){var el=document.createElement('div');el.innerHTML=h||'';el.querySelectorAll('.vizslot,.typing,.need-note').forEach(function(n){n.remove();});return el.innerHTML;}
function accentTitle(h){
 if(/<(em|strong|span|b)\b/.test(h))return h;
 var match=h.match(/(\$[\d.,\s]+(?:[–−-]\$?[\d.,]+)?|\d+[+%]|AI-агент[а-яё]*|AI-Оператор|Claude)/i);
 if(match)return h.replace(match[0],'<em>'+match[0]+'</em>');
 var parts=h.split(/\s+/),n=Math.min(2,Math.max(1,Math.floor(parts.length/4)));
 return parts.slice(0,-n).join(' ')+(parts.length>n?' ':'')+'<em>'+parts.slice(-n).join(' ')+'</em>';
}
function media(src,poster,fit){
 if(/\.(mp4|webm)(?:\?|$)/i.test(src))return '<video data-src="'+esc(src)+'"'+(poster?' data-poster="'+esc(poster)+'"':'')+' muted playsinline preload="none" controls></video>';
 return '<img data-src="'+esc(src)+'" alt="" style="object-fit:'+(fit||'contain')+'">';
}
function courseChangeDiagram(){
 var fragments=[[404,106,13],[431,87,9],[455,128,15],[416,154,10],[470,177,12],[443,219,16],[407,254,11],[477,271,9],[509,111,8],[530,157,11],[507,223,8],[547,267,6],[578,139,6],[575,205,9]];
 return '<figure class="fd-course-diagram"><svg viewBox="0 0 900 430" role="img" aria-label="Курсы обесцениваются с приходом AI: диплом рассыпается на цифровые фрагменты" xmlns="http://www.w3.org/2000/svg" fill="none">'+
 '<defs><linearGradient id="fd-course-paper" x1="100" y1="80" x2="420" y2="330" gradientUnits="userSpaceOnUse"><stop stop-color="#C6C1B9" stop-opacity=".1"/><stop offset="1" stop-color="#C6C1B9" stop-opacity=".015"/></linearGradient><radialGradient id="fd-course-light"><stop stop-color="#FDD506" stop-opacity=".12"/><stop offset="1" stop-color="#FDD506" stop-opacity="0"/></radialGradient></defs>'+
 '<ellipse cx="706" cy="204" rx="190" ry="186" fill="url(#fd-course-light)"/>'+
 '<g transform="rotate(-7 255 205)" stroke="#C6C1B9" stroke-linejoin="round">'+
 '<path d="M103 84L399 78L413 309L116 333Z" stroke-opacity=".15" stroke-width="1.5"/>'+
 '<path d="M99 91H364V111H385V139H369V165H399V187H381V213H402V235H373V255H392V280H366V318H99Z" fill="url(#fd-course-paper)" stroke-opacity=".65" stroke-width="2.5"/>'+
 '<path d="M119 111H344M119 111V298H345" stroke-opacity=".24" stroke-width="1.3"/>'+
 '<path d="M157 145H313" stroke-width="6" stroke-linecap="round" stroke-opacity=".7"/><path d="M145 171H326M145 187H305M145 203H273" stroke-width="3" stroke-linecap="round" stroke-opacity=".33"/>'+
 '<path d="M155 260L147 295L165 285L181 299L182 265" fill="#171510" stroke-opacity=".6" stroke-width="2"/>'+
 '<circle cx="171" cy="248" r="25" fill="#15130F" stroke-opacity=".65" stroke-width="2"/><circle cx="171" cy="248" r="17" stroke-opacity=".3"/>'+
 '<path d="M162 248L169 255L181 240M235 272C249 255 249 282 265 268S274 280 299 266" stroke-opacity=".65" stroke-width="2" stroke-linecap="round"/>'+
 '</g><g class="fd-course-fragments" fill="#FDD506">'+fragments.map(function(v,i){return '<rect class="fd-course-fragment" x="'+v[0]+'" y="'+v[1]+'" width="'+v[2]+'" height="'+v[2]+'" rx="1.5" opacity="'+(.8-i*.035)+'" style="--fragment:'+i+'" transform="rotate('+(i%2?12:-9)+' '+v[0]+' '+v[1]+')"/>';}).join('')+'</g>'+
 '<g class="fd-course-ai" stroke="#FDD506" stroke-width="2.5" stroke-linecap="round"><rect x="622" y="117" width="176" height="176" rx="28" fill="#151207"/><rect x="639" y="134" width="142" height="142" rx="17" stroke-opacity=".2"/>'+
 '<path d="M655 103V89M691 103V78M729 103V89M765 103V78M655 307V321M691 307V332M729 307V321M765 307V332M608 149H594M608 186H581M608 223H594M608 260H581M812 149H826M812 186H839M812 223H826M812 260H839" stroke-opacity=".45"/>'+
 '<text x="710" y="229" text-anchor="middle" stroke="none" fill="#FDD506" class="fd-course-ai-label">AI</text></g>'+
 '<text x="251" y="385" text-anchor="middle" class="fd-course-caption">Курсы</text><path d="M380 377H562M554 369L562 377L554 385" stroke="#C6C1B9" stroke-opacity=".25" stroke-width="2" stroke-linecap="round"/>'+ 
 '<text x="710" y="385" text-anchor="middle" class="fd-course-caption fd-course-caption-accent">Новая реальность</text></svg></figure>';
}
function perspectiveDiagram(){
 return '<figure class="fd-perspective-diagram"><svg viewBox="0 0 880 200" role="img" aria-label="До и после: запутанные линии переходят в ясный маршрут" fill="none" xmlns="http://www.w3.org/2000/svg">'+
 '<g class="fd-perspective-before" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'+
 '<path d="M64 98C105 98 95 37 152 43S245 147 192 144S119 70 172 64S279 146 302 116S259 35 230 57S263 135 320 97H410"/>'+
 '<path d="M64 128C126 153 176 24 220 28S248 142 283 141S365 63 410 98" opacity=".45"/>'+
 '<path d="M92 58C129 17 199 177 251 165S310 63 361 78L410 98" opacity=".28"/>'+
 '<circle cx="64" cy="98" r="5" fill="#0B0907"/>'+ 
 '</g><path class="fd-perspective-spine" d="M334 98H488" stroke="#FDD506" stroke-width="2.6" stroke-linecap="round" pathLength="1"/>'+
 '<g class="fd-perspective-lens"><path d="M439 24L467 40V145L439 161L413 145V40Z" fill="#151207" stroke="#FDD506" stroke-opacity=".32" stroke-width="1.5"/>'+
 '<path d="M439 37V148" stroke="#FDD506" stroke-width="2.6" stroke-linecap="round"/>'+
 '<circle cx="439" cy="98" r="15" fill="#FDD506" fill-opacity=".1"/><circle cx="439" cy="98" r="5" fill="#FDD506"/></g>'+
 '<g class="fd-perspective-after" stroke="#FDD506" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'+
 '<path d="M468 98H810" pathLength="1"/>'+
 '<path d="M488 98C552 98 552 46 614 46H792" pathLength="1"/>'+
 '<path d="M488 98C552 98 552 150 614 150H792" pathLength="1"/>'+
 '<path d="M803 91L810 98L803 105"/><circle cx="792" cy="46" r="5" fill="#FDD506"/><circle cx="792" cy="150" r="5" fill="#FDD506"/>'+ 
 '</g><text x="205" y="197" text-anchor="middle" class="fd-perspective-label">До</text><text x="667" y="197" text-anchor="middle" class="fd-perspective-label fd-perspective-label-after">После</text></svg></figure>';
}
function render(s,idx){
 var f=s.foundation||{},local=f.local===undefined?idx+1:f.local;
 if(local>=27&&local<=32&&window.FoundationPrizes&&!f.sourceOnly)return window.FoundationPrizes.render(s,idx);
 var sec=document.createElement('section'),body=clean(s.b),txt=plain(body),title=s.t||'',layout=f.layout||'editorial';
 sec._s=s;sec.dataset.idx=idx;sec.dataset.lv=s.lv||5;sec.dataset.google=f.google||'';sec.dataset.type=f.type||'content';
 var assets=f.media||[],internal=/(<img|<video|<iframe|class=["'](?:svcshot|qr))/i.test(body);
 if(!assets.length&&!f.omitMedia){
  if(s.kind==='video'&&s.src)assets=[s.src];
  else if(s.kind==='meme'&&s.img)assets=[s.img];
  else if(s.photos&&s.photos.length)assets=s.photos;
  else if(s.bg&&!internal)assets=[s.bg];
 }
 if(['cards','comparison','chat','diagram','timeline'].indexOf(layout)>=0&&txt.length>550)assets=[];
 if(f.type==='minimal'){layout='statement';assets=f.background?[f.background]:[];}
 if(f.sourceOnly)layout='source';
 if(s.kind==='embed'&&s.src)layout='embed';
 if(assets.length&&['statement','source','embed'].indexOf(layout)<0)layout=txt.length>240?'split':'media';
 var variant=String(f.variant||'').split(/\s+/).map(function(v){return v.replace(/[^a-z0-9-]/gi,'');}).filter(Boolean).map(function(v){return 'fd-'+v;}).join(' ');
 sec.className='slide foundation fd-'+layout+' fd-type-'+(f.type||'content')+(variant?' '+variant:'')+(assets.length?' fd-has-media':'')+(f.portrait?' fd-portrait':'')+(txt.length>700?' fd-dense':'')+(title.length>100?' fd-long-title':'');
 var titleMarkup=accentTitle(title);
 if(Array.isArray(f.titleLines)&&f.titleLines.length&&f.titleLines.join(' ')===plain(title))titleMarkup=accentTitle(f.titleLines.map(esc).join('<br> '));
 var h='';
 if(layout==='source'){
  h='<figure class="fd-source">'+media(assets[0]||f.sourceImage,'','contain')+'</figure>';
 }else{
  if(layout==='statement'&&assets.length)h+='<div class="fd-backdrop">'+media(assets[0],'','cover')+'</div>';
  h+='<div class="fd-shell"><header class="fd-header">'+(s.k?'<div class="fd-kicker">'+s.k+'</div>':'')+'<h1 class="split-done">'+titleMarkup+'</h1></header>';
  h+='<div class="fd-content"><div class="fd-body">'+lazy(body)+'</div>';
  if(layout==='embed'){
   var previews=f.demoPreviews||[],host=s.src.replace(/^https?:\/\//,'').replace(/\/$/,'');
   if(previews.length)h+='<div class="fd-demo"><div class="fd-demo-address">'+esc(host)+'</div><a class="fd-demo-preview" href="'+esc(s.src)+'" target="_blank" rel="noopener">'+previews.slice(0,2).map(function(a){return media(a,'','contain');}).join('')+'</a><a class="fd-demo-open" href="'+esc(s.src)+'" target="_blank" rel="noopener">Открыть демонстрацию <span aria-hidden="true">↗</span></a></div>';
   else h+='<div class="fd-embed"><iframe data-src="'+esc(s.src)+'" title="'+esc(plain(title))+'" loading="lazy"></iframe></div>';
  }
  else if(assets.length&&layout!=='statement')h+='<figure class="fd-media fd-media-'+Math.min(assets.length,4)+'">'+assets.slice(0,4).map(function(a){return '<div>'+media(a,s.poster,f.fit)+'</div>';}).join('')+'</figure>';
  else if(f.mediaNeeded&&!internal&&layout!=='statement')h+='<figure class="fd-media fd-empty" aria-label="Место для иллюстрации"><div class="fd-media-light"></div></figure>';
  h+='</div>'+(f.perspectiveDiagram?perspectiveDiagram():'')+(f.courseChangeDiagram?courseChangeDiagram():'')+(s.disc?'<div class="fd-disc">Результаты индивидуальны и не являются типичными</div>':'')+'</div>';
 }
 sec.innerHTML=h;
 if(f.perspectiveDiagram)sec.classList.add('fd-with-perspective');
 if(f.courseChangeDiagram)sec.classList.add('fd-course-change');
 sec.querySelectorAll('a[href]').forEach(function(a){a.addEventListener('click',function(e){e.stopPropagation();});});
 if(f.mediaCrop){var crop=f.mediaCrop,fig=sec.querySelector('.fd-media>div'),im=fig&&fig.querySelector('img');if(im){fig.classList.add('fd-crop');im.style.cssText='position:absolute;width:'+(100/crop.w)+'%;height:'+(100/crop.h)+'%;max-height:none;left:'+(-crop.x/crop.w*100)+'%;top:'+(-crop.y/crop.h*100)+'%;object-fit:fill;border-radius:0';}}
 var bd=sec.querySelector('.fd-body');
 if(bd&&layout==='cards'&&bd.children.length>=3&&Array.from(bd.children).every(function(n){return n.tagName==='P';}))bd.classList.add('fd-paragraph-cards');
 // Every original paragraph/row is visible in the final state; no navigation steps.
 sec.querySelectorAll('.fd-body > *, .fd-body .rt, .fd-body .cmsg, .fd-body .tags span, .fd-body li').forEach(function(el,n){el.style.setProperty('--fd-order',Math.min(n,12));});
 sec.querySelectorAll('.fd-body [style]').forEach(function(el){el.style.removeProperty('font-size');el.style.removeProperty('animation-delay');});
 sec.querySelectorAll('.chatbox.type').forEach(function(el){el.classList.remove('type');});
 // Source placeholders are editor notes, never disguised as verified live metrics.
 sec.querySelectorAll('.cnt[data-to]').forEach(function(el){el.textContent=el.dataset.to+(el.dataset.suffix||'');});
 if(f.type==='motion'&&layout==='timeline'){
  sec.querySelectorAll('.fd-body > p').forEach(function(p){if(p.textContent.indexOf('→')<0)return;var chunks=p.textContent.split('→');p.classList.add('fd-flow');p.innerHTML=chunks.map(function(x){return '<span>'+esc(x.trim())+'</span>';}).join('');});
 }
 return sec;
}
window.Foundation={render:render};
})();
