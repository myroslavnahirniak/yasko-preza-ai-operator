/* Source pages 15–28 from «Секрез 3 финал.pptx».
   Isolated renderer: no mutation of source data, main deck, notes or global styles. */
(function () {
  'use strict';
  const base = 'assets/secret3-final/';
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const image = (d, name) => esc((d.images || []).find(x => x.src && x.src.split('/').pop() === name)?.src || base + name);
  const heading = (eyebrow, title) => `${eyebrow ? `<p class="sf-b-eyebrow">${eyebrow}</p>` : ''}<h2 class="sf-b-heading">${title}</h2>`;
  const disclaimer = '<p class="sf-b-disclaimer">Результаты индивидуальны и не являются типичными</p>';
  const wrapper = (n, kind, content) => `<div class="sf-b sf-b-${kind}" data-sf-source="${n}">${content}</div>`;
  function results(n) {
    const active = n === 17 ? 1 : n === 19 ? 2 : 3;
    const rows = [
      ['КЛИЕНТ 1', '$240', 'сайты — лёгкий вход'],
      ['КЛИЕНТ 2', '$3.500', 'AI-видео — услуга из топ-7'],
      ['КЛИЕНТ 3', '$40.000', 'контракт на год']
    ];
    const eyebrow = ['ПЕРВЫЙ КЛИЕНТ','ВТОРОЙ КЛИЕНТ','ТРЕТИЙ КЛИЕНТ'][active-1];
    const faces = rows.map((r,i) => {
      const st = i+1 < active ? 'is-past' : i+1 === active ? 'is-now' : 'is-future';
      return `<section class="sf-r-face sf-r-face-${i+1} ${st}"${st === 'is-future' ? ' aria-hidden="true"' : ''}><p class="sf-b-client">${r[0]}</p><p class="sf-b-amount">${r[1]}</p><p class="sf-b-result-service">${r[2]}</p></section>`;
    }).join('');
    const art = 'assets/gen-rest-1006/r116-illustration-v2.webp';
    return wrapper(n, `results sf-b-stairs-slide sf-r-podium sf-r-active-${active}`,
      `<div class="sf-r-podium-art" aria-hidden="true"><img class="sf-r-pa-base" src="${art}" alt=""><img class="sf-r-pa-past" src="${art}" alt=""><img class="sf-r-pa-future" src="${art}" alt=""></div>` +
      heading(eyebrow, 'Этот ритм привёл его <em>сюда</em>') +
      `<div class="sf-r-faces">${faces}</div>` +
      (active === 3 ? '<blockquote class="sf-b-result-quote">«Это было лучшее решение — благодаря этому сейчас вообще всё поменялось»</blockquote>' : '') + disclaimer);
  }
  // 06.10 rest-redo (rest 120 = n21): фінальний стан драбини на тлі постаментів r116-illustration-v2; 1–2 приглушені, 3 — повне золото
  function podium(n) {
    const rows = [
      ['КЛИЕНТ 1', '$240', 'сайты — лёгкий вход'],
      ['КЛИЕНТ 2', '$3.500', 'AI-видео — услуга из топ-7'],
      ['КЛИЕНТ 3', '$40.000', 'контракт на год']
    ];
    const pods = rows.map((r,i) => `<section class="sf-b-pod sf-b-pod-${i+1} ${i === 2 ? 'is-now' : 'is-past'}"><p class="sf-b-pod-client">${r[0]}</p><p class="sf-b-pod-amount">${r[1]}</p><p class="sf-b-pod-service">${r[2]}</p></section>`).join('');
    return wrapper(n, 'podium', '<figure class="sf-b-pod-bg" aria-hidden="true"><img src="assets/gen-rest-1006/r116-illustration-v2.webp" alt=""></figure><div class="sf-b-pod-dim" aria-hidden="true"></div>' +
      heading('ТРЕТИЙ КЛИЕНТ', 'Этот ритм привёл его <em>сюда</em>') + pods +
      '<blockquote class="sf-b-pod-quote">«Это было лучшее решение — благодаря этому сейчас вообще всё поменялось»</blockquote>' + disclaimer);
  }
  function funnel(n) {
    const success = n === 25;
    const values = success ? ['20','15','15','2','1'] : ['15','≈13','≈8','0','0'];
    const counts = success ? [20,15,15,2,1] : [15,13,8,0,0];
    const labels = ['найдено','написал','ответили','захотели демо', success ? 'купил' : 'купили'];
    const title = success ? 'Вторая попытка: <em>Киев, окна</em>' : 'Вначале ничего<br><em>не получилось</em>';
    const eyebrow = success ? '🇺🇦 ОКНА И ОСТЕКЛЕНИЕ · КИЕВ · ПРОГОН 12 СЕНТЯБРЯ' : '🇬🇧 КРОВЛЯ И ФАСАДЫ · ЛИДС';
    const text = success ? 'Отвечают все. Двое захотели демо. «Конверсія Вікон» <em>купила сайт за 10 000 грн</em>. «Лінія Вікон» демо посмотрели — решения пока нет' : 'Отвечали охотно, но на «можно записаться на замер» реагировали как на обычную заявку. К сайту не повернул никто — рынок тугой, откликается слабо';
    // 06.10 rest-redo (rest 123/124): золотий wireframe-стиль стовпчиків; 24 — скетч-робот на даху, 25 — мініатюра проданого сайту над «1 купил»
    const extra = success
      ? '<figure class="sf-b-funnel-site"><span class="sf-b-funnel-site-bar" aria-hidden="true"><i></i><i></i><i></i></span><img src="assets/gen-rest-1006/r124-konverkon-shot.webp" alt="Сайт «Конверсія Вікон», проданный Василием"></figure><span class="sf-b-funnel-link" aria-hidden="true"></span>'
      : '<figure class="sf-b-funnel-robot" aria-hidden="true"><img src="assets/gen-rest-1006/r123-illustration-v1.webp" alt=""></figure>';
    return wrapper(n, `funnel sf-b-funnel-gold ${success ? 'sf-b-funnel-success' : 'sf-b-funnel-zero'}`, heading(eyebrow,title) + extra +
      `<div class="sf-b-funnel-chart" role="img" aria-label="${esc(values.map((v,i)=>`${labels[i]}: ${v}`).join('; '))}">${values.map((v,i)=>`<div class="sf-b-funnel-col${i>2 ? ' sf-b-funnel-outcome' : ''}" style="--bar:${(counts[i]/counts[0]*20).toFixed(2)}cqw"><p class="sf-b-funnel-number">${v}</p><div class="sf-b-funnel-bar" aria-hidden="true"></div><p class="sf-b-funnel-label">${labels[i]}</p></div>`).join('')}</div><p class="sf-b-funnel-story">${text}</p>`);
  }
  function render(d) {
    const n = Number(d.n);
    switch (n) {
      case 15: return wrapper(n, 'portrait', `<div class="sf-b-case-container"><h2 class="sf-b-heading">Василий стартовал<br>не с нуля, <em>а с минуса</em></h2><div class="sf-b-biography"><p>30 лет, скульптор и музыкант, живёт в Черногории</p><p>Был в оккупация в Буче, долгое время получал деньги только от родителей</p></div><figure class="sf-b-portrait-photo"><img src="${image(d,'image16.png')}" alt="Василий — фотография из исходной презентации"></figure></div>`);
      case 16: return wrapper(n, 'testimonial', heading('','и включил <em>охотника</em>')  /* 09.10 Google G404: «Взял две ниши…» — окремий екран перед цим (new-c403), без «ЕГО СЛОВА» */ + `<div class="sf-b-testimonial"><div class="sf-b-person"><span class="sf-b-avatar"><img src="${image(d,'image11.png')}" alt=""></span><div><p>Vasily</p><span>был(а) недавно</span></div></div><blockquote>Я сделал всего 15 рассылок и, параллельно что-то другое делал. Поэтому так налегке, можно сказать</blockquote></div><p class="sf-b-testimonial-end">По <em>15 сообщений</em> в день.<br>Два дня подряд</p>`);  /* 08.10 Мирослав: повернуто оформлення до переробки 06.10 (без телефона) */
      case 17: case 19: return results(n);
      case 21: return podium(n);
      case 18: return wrapper(n, 'site', heading('ЧТО ОН ПРОДАЛ','Вот сайт,<br>который он <em>продал</em>') + `<p class="sf-b-site-price">10 000 грн <span>≈ $240</span></p><div class="sf-b-site-frame"><img class="sf-b-site-poster" src="assets/secret3-final/image18.jpg" alt="Скриншот сайта Конверсія Вікон из исходной презентации"><iframe data-src="https://konverkon.vercel.app/" title="Сайт «Конверсія Вікон», проданный Василием" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe></div>${disclaimer}<a class="sf-b-site-link" href="https://konverkon.vercel.app/" target="_blank" rel="noopener noreferrer">https://konverkon.vercel.app/</a>`);
      case 20: return wrapper(n, 'film', `<div class="sf-b-film-stage"><video controls playsinline preload="auto" poster="assets/secret3-final/full-film-poster.jpg"><source src="assets/secret3-final/full-film-720p-fs.mp4" type="video/mp4"></video></div>`);
      case 22: return wrapper(n, 'vquote', '<figure class="sf-b-vq-photo"><img src="assets/gen-rest-1006/r121-vasily-2x.webp" alt="Василий"></figure><blockquote class="sf-b-big-quote sf-b-vq-text"><span class="sf-b-vq-mark" aria-hidden="true">“</span><p>Я иногда даже не читаю: что пишет клиент, я ему просто перекидаю сообщение от клиента, он как-то отвечает и всё.</p><p>И теперь ощущение, что <em>всё возможно</em> и всё можно реализовать, и абсолютно не вопрос, что либо сделать сейчас,<span class="sf-b-vq-close" aria-hidden="true">”</span></p></blockquote>'); // 06.10 rest-redo rest 121: фото Василия + цитата
      case 23: return wrapper(n, 'leeds sf-b-leeds-map', heading('ЧТО ОН ВЫБРАЛ','Первая попытка:<br><em>Лидс, кровля и фасады</em>') + `<div class="sl-map-panel"><figure class="sl-map"><img src="assets/gen-184-188/s226-uk-map.webp" alt="Карта Великобритании с отметкой Лидса"></figure><span class="sl-map-label">Лидс</span><div class="sl-map-country">Великобритания</div></div><section class="sl-niche-card"><svg class="sl-roof" viewBox="0 0 120 120" fill="none" aria-hidden="true"><path d="M20 62 60 28 100 62" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M32 69v25h56V69M78 39V26h12v23" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="sl-card-kicker">ниша из списка</span><h3>Кровля<br>и фасады</h3><div class="sl-city-detail"><p>Великобритания · Лидс</p><span>город на севере Англии</span></div><div class="sl-population"><strong>≈ 800 тыс.</strong><span>жителей</span></div></section>`);
      case 24: case 25: return funnel(n);
      case 26: return wrapper(n, 'arithmetic sf-b-arithmetic-stairs', '<figure class="sf-b-labeled-stairs"><img src="assets/gen-s229-thousand/stairs-labeled-v2.png" alt="День 1 — $250; день 2 — $500; день 3 — $750; день 4 — $1.000, первая тысяча; день 5 — $1.250"></figure>' + heading('СЧИТАЕМ ПО-ЧЕСТНОМУ','Первая тысяча —<br><em>за четыре дня</em>') + '<p class="sf-b-formula">30 сообщений в день → одна продажа → $250</p><p class="sf-b-scenario">Расчёт при одной продаже в день</p>');
      case 27: return wrapper(n, 'month sf-b-month-focus', heading('ЕСЛИ ДЕРЖАТЬ РИТМ','А что будет <em>за месяц</em>') + '<div class="sf-b-month-focus-card"><p class="sf-b-month-amount">$5.000</p></div><p class="sf-b-month-rule">20 рабочих дней ·<br>по одной продаже в день</p><p class="sf-b-scenario">Расчёт при одной продаже в день</p>');
      case 28: return wrapper(n, 'poster sf-b-poster-full', '<img class="sf-b-poster-img" src="assets/gen-rest-1006/r126-calendar-a10.webp" alt="Календарь, где каждый день — пропущенный клиент, и песочные часы"><i class="r126-scrim" aria-hidden="true"></i><h1 class="r126-title">Месяц «я подумаю» = <em>20 пропущенных клиентов</em> на «полуавтомате»</h1><p class="r126-box">Посчитай свою <b>цену ожидания</b></p>'); // 08.10 Мирослав: фон a10, текст живим одним шрифтом, «Посчитай…» у жовтому контейнері
      default: return '';
    }
  }
  window.Secret3B = Object.freeze({ render });
}());
/* 09.10 Мирослав · rest 133 (case 20, фільм): стартує одразу при вході на слайд — зі звуком (після клавіші/кліку браузер дозволяє),
   при забороні — без звуку; при виході пауза. Файл перепаковано з faststart (moov на початку) і preload=auto — грузиться заздалегідь. */
(function(){
  var tries=0;
  function arm(){
    var v=document.querySelector('.sf-b-film-stage video'); if(!v){ if(++tries<60) setTimeout(arm,500); return; }
    var sl=v.closest('.slide'); if(!sl) return; var was=false;
    function sync(){ var on=sl.classList.contains('on');
      if(on&&!was){ if(v.ended) v.currentTime=0; v.muted=false; var p=v.play(); if(p&&p.catch) p.catch(function(){ if(!sl.classList.contains('on')) return; v.muted=true; v.play().catch(function(){}); }); }
      else if(!on&&was){ v.pause(); }
      was=on; }
    new MutationObserver(sync).observe(sl,{attributes:true,attributeFilter:['class']}); sync();
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',arm); else arm();
}());
