(function () {
  'use strict';
  var raw=window.FOUNDATION_REVIEW;
  var slides=(Array.isArray(raw)?raw:(raw && raw.slides)||[]).slice().sort(function(a,b){return Number(a.displayNumber||a.google)-Number(b.displayNumber||b.google);});
  var types={content:{label:'Контентні',singular:'Контент',description:'Текст, фото та докази'},minimal:{label:'Мінімальні',singular:'Мінімальна теза',description:'Одна думка, тихий фон'},motion:{label:'Анімація',singular:'Анімація',description:'Рух пояснює дію'},video:{label:'Відео',singular:'Відео',description:'Ключові сцени та демонстрації'}};
  var params=new URLSearchParams(location.search),state={type:types[params.get('type')]?params.get('type'):'all',query:params.get('q')||'',media:params.get('media')==='needed'};
  var grid=document.getElementById('review-grid'),search=document.getElementById('review-search'),media=document.getElementById('review-media'),typeBar=document.getElementById('review-types'),count=document.getElementById('review-count');
  function node(tag,cls,txt){var n=document.createElement(tag);if(cls)n.className=cls;if(txt!=null)n.textContent=txt;return n;}
  function normalize(s){return String(s||'').toLocaleLowerCase().replace(/ё/g,'е').replace(/’/g,"'");}
  function safeUrl(value,fallback){var s=String(value||'');return /^(?:https?:|file:)/i.test(s)||(!/^[a-z][a-z\d+.-]*:/i.test(s)&&!s.startsWith('//'))?s||fallback:fallback;}
  function statusInfo(item){
    var text=String(item.mediaStatus||'none'),n=normalize(text);
    if(/^(none|not-needed|n\/a)$/.test(n)||/(не потріб|непотріб)/.test(n))return {label:'Без додаткових медіа',kind:'none',raw:text};
    if(/^(needed|missing|pending|needs-media|to-add)$/.test(n)||/(потріб|потрібн|нужн|додат|очіку|ожида|заміни|замінит)/.test(n))return {label:'Потрібні медіа',kind:'needed',raw:text};
    if(/^(optional|suggested)$/.test(n)||/(за бажанням|опці|можна додати)/.test(n))return {label:'Медіа за бажанням',kind:'optional',raw:text};
    if(/^(ready|existing|available|done)$/.test(n)||/(готов|наявн)/.test(n))return {label:'Медіа готові',kind:'ready',raw:text};
    return {label:text,kind:'unknown',raw:text};
  }
  var totals={};Object.keys(types).forEach(function(t){totals[t]=slides.filter(function(s){return s.type===t;}).length;});
  var stats=document.getElementById('review-stats');
  Object.keys(types).forEach(function(t){var box=node('div','review-stat'),top=node('div','review-stat-top');top.appendChild(node('span','review-stat-number',totals[t]));top.appendChild(node('span','review-stat-name',types[t].label));box.appendChild(top);box.appendChild(node('p','',types[t].description));stats.appendChild(box);});
  ['all'].concat(Object.keys(types)).forEach(function(t){var button=node('button','review-filter',t==='all'?'Усі слайди':types[t].label);button.type='button';button.dataset.type=t;button.appendChild(node('span','review-filter-count',t==='all'?slides.length:totals[t]));button.addEventListener('click',function(){state.type=t;render();});typeBar.appendChild(button);});
  function card(item){
    var type=types[item.type]||types.content,status=statusInfo(item),article=node('article','review-card type-'+item.type),url=safeUrl(item.url,'index.html?square&clean&s='+item.local),preview=node('a','review-preview');
    var sourceLabel='Google '+item.google+(item.presentationPartCount?' · частина '+item.presentationPart+'/'+item.presentationPartCount:'');
    preview.href=url;preview.target='_blank';preview.rel='noopener';preview.setAttribute('aria-label','Відкрити '+sourceLabel+': '+item.title);
    var fallback=node('div','review-preview-fallback');fallback.appendChild(node('span','review-preview-number',String(item.displayNumber||item.google).padStart(3,'0')));fallback.appendChild(node('span','review-preview-title',item.title));preview.appendChild(fallback);
    if(item.thumbnail){var image=node('img','review-thumbnail');image.loading='lazy';image.decoding='async';image.alt='Прев’ю слайда '+item.google;image.src=safeUrl(item.thumbnail,'');image.addEventListener('load',function(){preview.classList.add('has-thumbnail');});image.addEventListener('error',function(){image.remove();preview.classList.remove('has-thumbnail');});preview.appendChild(image);}
    preview.appendChild(node('span','review-preview-open','Відкрити ↗'));article.appendChild(preview);
    var body=node('div','review-card-body'),meta=node('div','review-card-meta');meta.appendChild(node('span','review-google',sourceLabel));if(item.displayNumber&&(item.presentationPartCount||item.displayNumber!==item.google))meta.appendChild(node('span','review-local','перегляд '+item.displayNumber));else if(item.local)meta.appendChild(node('span','review-local','лок. '+item.local));body.appendChild(meta);body.appendChild(node('h2','review-card-title',item.title));
    var badges=node('div','review-card-badges');badges.appendChild(node('span','review-type-badge',type.singular));badges.appendChild(node('span','review-status status-'+status.kind,status.label));body.appendChild(badges);
    if(item.reviewNote)badges.appendChild(node('span','review-status status-needed','Потребує уваги'));
    if(item.mediaBrief||item.animationBrief||item.reviewNote){var details=node('details','review-card-details');details.appendChild(node('summary','','Медіа та рух'));if(item.reviewNote){details.appendChild(node('h3','','До ефіру'));details.appendChild(node('p','',item.reviewNote));}if(item.mediaBrief){details.appendChild(node('h3','','Медіа'));details.appendChild(node('p','',item.mediaBrief));}if(item.animationBrief){details.appendChild(node('h3','','Анімація'));details.appendChild(node('p','',item.animationBrief));}body.appendChild(details);}
    article.appendChild(body);return article;
  }
  function render(){
    var q=normalize(state.query).trim(),words=q.split(/\s+/).filter(Boolean);
    var filtered=slides.filter(function(item){if(state.type!=='all'&&item.type!==state.type)return false;if(state.media&&statusInfo(item).kind!=='needed'&&!item.reviewNote)return false;if(!words.length)return true;var hay=normalize([item.google,item.displayNumber,item.local,item.title,item.mediaBrief,item.animationBrief,item.reviewNote].join(' '));return words.every(function(w){return hay.indexOf(w)!==-1;});});
    var fragment=document.createDocumentFragment();filtered.forEach(function(item){fragment.appendChild(card(item));});grid.replaceChildren(fragment);
    count.textContent='Показано '+filtered.length+' із '+slides.length+' слайдів';
    document.getElementById('review-empty').hidden=filtered.length!==0;document.getElementById('review-reset').hidden=!(state.type!=='all'||state.media||state.query);
    [].forEach.call(typeBar.querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',String(b.dataset.type===state.type));});
    var p=new URLSearchParams();if(state.type!=='all')p.set('type',state.type);if(state.query)p.set('q',state.query);if(state.media)p.set('media','needed');
    try{history.replaceState(null,'',location.pathname+(p.toString()?'?'+p:''));}catch(ignore){}
  }
  search.value=state.query;media.checked=state.media;
  var timer;
  search.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(function(){state.query=search.value;render();},100);});
  media.addEventListener('change',function(){state.media=media.checked;render();});
  document.getElementById('review-reset').addEventListener('click',function(){state={type:'all',query:'',media:false};search.value='';media.checked=false;render();});
  document.addEventListener('keydown',function(event){if((event.metaKey||event.ctrlKey)&&event.key.toLowerCase()==='k'){event.preventDefault();search.focus();search.select();}});
  var start=slides.find(function(s){return s.google===2;})||slides[0];
  if(start&&start.url)document.getElementById('open-deck').href=safeUrl(start.url,'google180.html?square&clean&s=2');
  render();
})();
