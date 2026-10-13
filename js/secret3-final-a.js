/* Secret 3 definitive source, 2026-09-21. Slides 1–13, editable audience copy. */
(function(){
  'use strict';
  const esc = value => String(value == null ? '' : value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const sourceMedia = 'assets/secret3-final/';
  const asset = (data, key, fallback) => esc(data[key] || fallback);
  const icon = (name) => {
    const shapes={
      map:'<path d="M7 8 21 3l14 5 14-5v43l-14 5-14-5-14 5Z"/><path d="M21 3v43M35 8v43"/><circle cx="35" cy="23" r="8"/><path d="m31 30 4 6 4-6"/>',
      find:'<circle cx="25" cy="23" r="15"/><path d="m36 35 13 13M18 23h14M25 16v14"/>',
      site:'<rect x="5" y="7" width="46" height="41" rx="4"/><path d="M5 18h46M13 12h1m6 0h1m6 0h1M13 27h30M13 33h16M13 39h22"/>',
      chat:'<path d="M8 7h40v31H24L11 49V38H8Z"/><path d="M17 18h22M17 26h17"/>',
      agent:'<rect x="12" y="13" width="32" height="31" rx="8"/><path d="M28 4v9M5 23v12m46-12v12M20 36h16"/><circle cx="21" cy="25" r="2"/><circle cx="35" cy="25" r="2"/>',
      list:'<rect x="10" y="5" width="36" height="46" rx="4"/><path d="m17 17 3 3 5-6m-8 17 3 3 5-6m4-11h10m-10 14h10m-22 13h22"/>',
      moon:'<path d="M43 37A21 21 0 0 1 20 5a22 22 0 1 0 23 32Z"/>',
      arrow:'<path d="M7 28h40M34 15l13 13-13 13"/>',
      star:'<path d="m28 5 6.8 14 15.5 2.2-11.2 11 2.6 15.4L28 40.3l-13.7 7.3 2.6-15.4-11.2-11L21.2 19Z"/>'
    };
    return '<svg class="sf-a-icon" viewBox="0 0 56 56" aria-hidden="true">'+(shapes[name]||shapes.agent)+'</svg>';
  };
  const head=(kicker,title,sub='')=>'<header class="sf-a-header">'+(kicker?'<p class="sf-a-kicker">'+kicker+'</p>':'')+'<h1>'+title+'</h1>'+(sub?'<p class="sf-a-sub">'+sub+'</p>':'')+'</header>';
  const wrap=(n,body,extra='')=>'<div class="sf-a sf-a'+n+' '+extra+'">'+body+'</div>';
  const miniMap=()=>'<div class="sf-a-map" aria-hidden="true"><i class="sf-a-road sf-a-road1"></i><i class="sf-a-road sf-a-road2"></i><i class="sf-a-road sf-a-road3"></i><i class="sf-a-pin sf-a-pin1"></i><i class="sf-a-pin sf-a-pin2"></i><i class="sf-a-pin sf-a-pin3"></i></div>';
  const sourceCrop=(file,type,alt)=>'<div class="sf-a-crop sf-a-crop-'+type+'"><img src="'+sourceMedia+file+'" alt="'+esc(alt)+'"></div>';
  const flow=(n)=>{
    const count=n-2;
    const row1='<article class="sf-a-flow-row sf-a-flow-find"><b class="sf-a-step-number">1</b><p>Найти тех, кто с<br>наибольшей вероятностью<br><em>купит у нас эту услугу</em></p>'+(count>=1?'<div class="sf-a-flow-visual sf-r-mapcard"><img src="assets/gen-rest-1006/r100-illustration-v1.webp" alt="Карта города с золотыми метками"></div>':'<div class="sf-a-flow-visual">'+miniMap()+'<div class="sf-a-shortlist" aria-hidden="true"><i></i><i></i><i></i></div>'+icon('find')+'</div>')+'</article>';
    const row2='<article class="sf-a-flow-row sf-a-flow-write"><b class="sf-a-step-number">2</b><p><em>Написать им</em></p><div class="sf-r-phonetop"><i class="sf-r-island" aria-hidden="true"></i><div class="sf-r-bubble">Здравствуйте! Заметил, что записаться к вам можно только по телефону…<span class="sf-r-ticks" aria-hidden="true"></span></div></div></article>';
    const row3='<article class="sf-a-flow-row sf-a-flow-delegate"><b class="sf-a-step-number">3</b><p>Не делать это <em>своими руками :)</em></p><figure class="sf-r-robot" aria-hidden="true"><img src="assets/gen-rest-1006/r102-robot-sketch.webp" alt=""></figure></article>';
    const mark=(r,i)=>r.replace('class="sf-a-flow-row','class="sf-a-flow-row '+(i===count?'sf-a-new':i>count?'sf-a-ghost':'sf-a-kept'));
    return wrap(n,head('СВЯЗКА ЕСТЬ — ЧТО ДАЛЬШЕ','Осталось <em>только</em>')+'<div class="sf-a-flow sf-a-flow-'+count+'">'+mark(row1,1)+(count>1?mark(row2,2):mark(row2,2).replace('<article ','<article aria-hidden="true" '))+(count>2?mark(row3,3):count>=1?mark(row3,3).replace('<article ','<article aria-hidden="true" '):'')+'</div>',count>1?'sf-a-cont':'');
  };
  const demo=(d,n)=>{
    const night=n===10,url=night?'https://ai-hunter-sigma.vercel.app':'https://worknothunt.xyz/';
    const preview=night?(d.preview || ''):(d.preview || sourceMedia+'image22.png');
    const visual=night?'<video data-sf-autoplay class="sf-a-demo-preview sf-a-demo-cover" src="assets/video/secret3-hunter.mp4" poster="assets/video/secret3-hunter-poster.jpg" autoplay muted loop playsinline preload="auto" aria-label="AI-охотник — видео"></video>':preview?'<img class="sf-a-demo-preview" src="'+esc(preview)+'" alt="Превью сервиса из исходной презентации">':'<div class="sf-a-demo-poster"><img src="'+asset(d,'hunter','assets/secret3-final/hunter.png')+'" alt="AI-охотник"></div>';
    return wrap(n,head(night?'AI-ОХОТНИК · НОЧНАЯ СМЕНА':'ЭКРАН · ДАШБОРД',night?'Не трать время<br>на <em>поиск клиентов</em>':'ЩА ПОКАЖУ<br><em>КАК ЭТО РАБОТАЕТ</em>',night?'Пусть охотник принесёт тебе готовую добычу.':'Дальше он идёт сам — и показывает каждый шаг на экране')+'<a class="sf-a-demo-window" href="'+url+'" target="_blank" rel="noopener noreferrer" aria-label="Открыть демо в новой вкладке"><span class="sf-a-browser-top"><i></i><i></i><i></i><span>'+url.replace('https://','').replace(/\/$/,'')+'</span></span>'+visual+'</a><div class="sf-a-demo-footer"><span>'+url+(night?' .':'')+'</span><a class="sf-a-demo-link" href="'+url+'" target="_blank" rel="noopener noreferrer">Открыть демо '+icon('arrow')+'</a></div>',night?'sf-a-cont sf-a-still':'');
  };
  const ROAD_STEPS=[['Изучает Google Карты','находит всех, кто подходит под наводку','Google Карты','assets/gen-184-188/s275-maps.webp'],['Проверяет каждого','сайт, отзывы, соцсети — у кого что хромает','Проверяет','assets/gen-184-188/s275-check.webp'],['Отдаёт список','тех, кто купит с наибольшей вероятностью','Список','assets/gen-184-188/s275-list.webp'],['Готовит сообщение','личное, каждому — из фактов о нём','Сообщение','assets/gen-184-188/s275-message.webp']];
  const road=(n,step)=>{
    const cur=ROAD_STEPS[step-1];
    const rail=ROAD_STEPS.map((r,i)=>`<div class="sr-stop ${i+1===step?'is-current':i+1<step?'is-done':''}"><span>${String(i+1).padStart(2,'0')}</span><p>${r[2]}</p></div>`).join('');
    return wrap(n,head('АЛГОРИТМ','Что он делает <em>с наводкой</em>')+
      `<div class="sr-rail" aria-label="Этап ${step} из 4">${rail}</div>`+
      `<figure class="sr-scene"><img src="${cur[3]}" alt="Иллюстрация этапа: ${cur[0]}"></figure>`+
      `<div class="sr-caption"><span class="sr-number">${String(step).padStart(2,'0')}</span><div><h2>${cur[0]}</h2><p>${cur[1]}</p></div></div>`+
      (step===4?'<div class="sr-conclusion"><img src="assets/gen-184-188/s278-vlad-says.webp" alt="Влад"><p>Все четыре шага — <em>без вас.</em></p></div>':''),'sf-refined-route sf-a-cont');
  };
  function render(d,conf){
    const n=Number(d.n);
    if(n===9&&conf&&conf.step)return road(n,Number(conf.step));
    if(n>=3&&n<=5)return flow(n);
    if(n===10||n===11)return demo(d,n);
    switch(n){
      case 1:return wrap(n,head('СЕКРЕТ №3','Откуда берётся<br>первый клиент уже<br><em>через 24 часа</em>')+'<div class="sf-a-hero-scene"><span class="sf-a-day-ring" aria-hidden="true"></span><img src="'+asset(d,'hunter','assets/secret3-final/hunter.png')+'" alt="AI-охотник работает ночью"></div><p class="sf-a-hero-support">если у вас есть только<br><strong>один свободный вечер</strong><br>и <em>$20 в кармане</em></p>');
      case 2:return wrap(n,head('СВЯЗКА · ИЗ ВТОРОГО СЕКРЕТА','1 из рабочих связок<br><em>вы уже знаете</em>','Кому, что и как продавать')+'<div class="sf-a-offer-rows"><article class="sf-a-offer-row"><span class="sf-a-row-label">КОМУ</span><div class="sf-a-offer-copy"><h2>бизнесу с Google Maps</h2><p>есть отзывы — нет сайта или он старый</p></div><div class="sf-a-offer-mini sf-a-clinic">'+miniMap()+'<p>Стоматология · <span class="sf-a-star" aria-label="звезда">'+icon('star')+'</span> 4.7 · сайта нет</p></div></article><article class="sf-a-offer-row"><span class="sf-a-row-label">ЧТО</span><div class="sf-a-offer-copy"><h2>сайты</h2><p>от <em>$250</em>, собирает агент</p></div><div class="sf-a-offer-mini sf-a-site-example">'+sourceCrop('image9.jpg','site','Пример сайта из исходного слайда')+'</div></article><article class="sf-a-offer-row"><span class="sf-a-row-label">КАК</span><div class="sf-a-offer-copy"><h2>через бесплатное демо</h2><p>сначала показать — потом продать</p></div><div class="sf-a-offer-mini sf-a-chat-example"><p>Собрал сайт под вашу клинику. Показать? Это бесплатно</p><p>Показывайте</p></div></article></div>');
      case 6:return wrap(n,head('ДЕНЬГИ НА СТАРТ','')+'<blockquote class="sf-a-vasily-quote">«После работы я никакой,<br>имел я в рот еще сидеть<br><em>искать клиентов</em>»</blockquote><div class="sf-a-vasily-context"><p>Сказал мне скульптор Василий, который работал по <strong>10 часов без выходных</strong> и закрыл клиента на <em>$40.000 услуг за год.</em></p>'+'<figure class="sf-r-meme"><div class="sf-r-meme-frame"><video src="assets/memes/posle-raboty.mp4" data-sf-autoplay autoplay muted loop playsinline preload="auto" aria-label="Мем: после работы падает на кровать"></video></div><figcaption class="sf-r-meme-bar">21:00. «ЗАВТРА ТОЧНО НАЧНУ»</figcaption></figure></div>');
      case 7:return wrap(n,head('','ПОЭТОМУ Я СОЗДАЛ<br><em>AI-ОХОТНИКА</em>')+'<div class="sf-a-hvideo" role="button" aria-label="Смотреть видео на весь экран"><video src="assets/video/secret3-hunter.mp4" poster="assets/video/secret3-hunter-poster.jpg" playsinline preload="metadata" muted loop></video><span class="sf-a-play" aria-hidden="true"><i></i></span></div>');
      case 8:return wrap(n,'<img class="sf-a8-photo sf-a8-poster" src="assets/secret3-final/hunter-scope-v1-4k.webp" alt="Всё, что нужно охотнику — наводка: локация Киев · Оболонь, ниша установка окон, услуга сайт">');
      case 9:{
        const rows=[['Изучает Google Карты','находит всех, кто подходит под наводку','map'],['Проверяет каждого','сайт, отзывы, соцсети — у кого что хромает','find'],['Отдаёт список','тех, кто купит с наибольшей вероятностью','list'],['Готовит сообщение','личное, каждому — из фактов о нём','chat']];
        return wrap(n,head('АЛГОРИТМ','Что он делает<br><em>с наводкой</em>')+'<div class="sf-a-algorithm">'+rows.map((r,i)=>'<article class="sf-a-algo-row"><span class="sf-a-algo-number">'+(i+1)+'</span><div><h2>'+r[0]+'</h2><p>'+r[1]+'</p></div>'+icon(r[2])+'</article>').join('')+'</div><p class="sf-a-algo-conclusion">Все четыре шага — <em>без вас.</em></p>');
      }
      case 12:return wrap(n,head('ЕСЛИ ДЕЛАТЬ РУКАМИ','Руками эта работа —<br><em>8 часов в день</em>')+'<div class="sf-a-workday"><div class="sf-a-timebar" role="img" aria-label="8 часов: 5 часов поиска, 1 час разбора, 2 часа сообщений"><span class="sf-a-hours5"></span><span class="sf-a-hours1"></span><span class="sf-a-hours2"></span></div><div class="sf-a-time-labels"><div><span class="sf-a-hour-dot sf-a-dot5"></span><p>Найти, кому писать</p><strong>5 часов</strong></div><div><span class="sf-a-hour-dot sf-a-dot1"></span><p>Разобрать каждого: сайт, отзывы</p><strong>1 час</strong></div><div><span class="sf-a-hour-dot sf-a-dot2"></span><p>Написать каждому лично</p><strong>2 часа</strong></div></div></div><div class="sf-r-daynight"><figure class="sf-r-day"><img src="assets/gen-rest-1006/r112-office-day.webp" alt="Офис днём: люди ищут клиентов руками"></figure><figure class="sf-r-night"><img src="assets/gen-rest-1006/r112-night-office.webp" alt="Ночной офис: роботы работают, кресло человека пустое"></figure><p class="sf-r-daynight-text">Всё это делает охотник — <em>ночью, пока вы спите</em></p></div>');
      case 13:return wrap(n,head('ПОМНИТЕ ПРОДАВЦА?','А теперь вспомните<br><em>AI-продавца</em>','Того самого, который живёт в Telegram, WhatsApp и Instagram')+'<div class="sf-r-handoff"><figure class="sf-r-hunter"><div class="sf-r-hunter-pic"><img src="assets/gen-1009/vlad/hunter.webp" alt="Влад — охотник с луком"></div><figcaption>Охотник</figcaption></figure><div class="sf-r-bridge" aria-hidden="true"><i class="sf-r-fly"></i><i class="sf-r-fly"></i><i class="sf-r-fly"></i><i class="sf-r-fly"></i><svg viewBox="0 0 120 24" fill="none"><path d="M2 12h112M102 2l12 10-12 10"/></svg></div><div class="sf-r-seller"><div class="sf-r-seller-row"><div class="g1001-iphone sf-r-iphone"><i class="g1001-btn a"></i><i class="g1001-btn b"></i><i class="g1001-btn c"></i><i class="g1001-btn d"></i><div class="g1001-iscreen"><img src="assets/vlad-1409/video/tg-seller-voice-poster.jpg" alt="AI-продавец отвечает клиенту в Telegram"></div></div><div class="sf-r-logos"><img src="assets/logo/telegram.svg" alt="Telegram"><img src="assets/logo/whatsapp.svg" alt="WhatsApp"><img src="assets/logo/instagram.svg" alt="Instagram"></div></div><span class="sf-r-seller-label">AI-продавец</span></div></div><p class="sf-a-handoff-question">Что будет, если все диалоги, которые собрал охотник, <em>передать сразу ему?</em></p>');
      default:return '';
    }
  }

  /* 21.09 · 273: клік по відео — на весь слайд зі звуком, ще клік — назад */
  document.addEventListener('click',e=>{const box=e.target.closest&&e.target.closest('.sf-a-hvideo');if(!box)return;e.preventDefault();e.stopPropagation();const sl=box.closest('.slide');const v=box.querySelector('video');const full=sl.classList.toggle('is-full');v.muted=!full;if(full){v.currentTime=0;}v.play().catch(()=>{});},true);
  window.Secret3A={render};
})();
