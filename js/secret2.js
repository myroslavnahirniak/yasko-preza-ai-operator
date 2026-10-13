/* Секрет 2 · оформлення в стилі деки. Ізольований рендерер: не чіпає основну деку, дані і глобальні стилі.
   Текст — дослівно з v5 (js/secret2-data.js). Один слайд = одна функція розмітки. */
(function () {
  'use strict';
  const G = 'assets/';
  const FULL = new Set([242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259]);
  const FULL_V = '20260922b';
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const wrap = (n, kind, content) => `<div class="s2 ${kind.split(' ').map(k => 's2-k-' + k.replace(/^s2-/, '')).join(' ')}" data-v5="${n}">${content}</div>`;
  const head = (eyebrow, title, cls) => `<header class="s2-head${cls ? ' ' + cls : ''}">${eyebrow ? `<p class="s2-eyebrow">${eyebrow}</p>` : ''}<h1>${title}</h1></header>`;
  const bg = (src, mode, alt) => `<img class="s2-bg s2-bg-${mode || 'full'}" src="${G}${src}" alt="${esc(alt || '')}"><i class="s2-scrim s2-scrim-${mode || 'full'}" aria-hidden="true"></i>`;
  const bottom = (html) => `<footer class="s2-bottom">${html}</footer>`;
  const ph = (text) => `<div class="s2-ph" role="img" aria-label="${esc(text)}"><span>визуал позже</span><small>${esc(text)}</small></div>`;
  /* іконки: штрих 1.4, колір #B3A996 (задається в CSS) */
  const I = {
    target: '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
    puzzle: '<path d="M9 3.5h3v2.2a1.8 1.8 0 1 0 3 0V3.5h4.5V8h-2.2a1.8 1.8 0 1 0 0 3H19.5v9.5H15v-2.2a1.8 1.8 0 1 0-3 0v2.2H4.5V11h2.2a1.8 1.8 0 1 0 0-3H4.5V3.5H9Z"/>',
    pin: '<path d="M12 21.5s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11Z"/><circle cx="12" cy="10.5" r="2.4"/>',
    gift: '<rect x="3.5" y="9" width="17" height="12" rx="1.2"/><path d="M12 9v12M3.5 13.5h17M12 9c-2.5 0-5-1.2-5-3a2 2 0 0 1 4-.5c.4.9 1 2.4 1 3.5Zm0 0c2.5 0 5-1.2 5-3a2 2 0 0 0-4-.5c-.4.9-1 2.4-1 3.5Z"/>',
    compass: '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z"/>',
    lock: '<rect x="5" y="10.5" width="14" height="10" rx="1.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
    chat: '<path d="M4 5.5h16v10H9l-5 4v-14Z"/>',
    shop: '<path d="M4 9.5 5.5 4h13L20 9.5M4 9.5v11h16v-11M4 9.5c0 1.4 1.2 2.5 2.7 2.5s2.6-1.1 2.6-2.5c0 1.4 1.2 2.5 2.7 2.5s2.7-1.1 2.7-2.5c0 1.4 1.1 2.5 2.6 2.5S20 10.9 20 9.5M9.5 20.5v-6h5v6"/>',
    users: '<circle cx="9" cy="8.5" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5M15.5 5.5a3.2 3.2 0 0 1 0 6.4M17.5 14.7c2.2.6 3.5 2.4 3.5 5.3"/>',
    phoneOff: '<rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M4 4l16 16"/>',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
    brush: '<path d="M14 3.5 20.5 10 10 20.5 3.5 14 14 3.5Z"/><path d="m7 17 6-6"/>',
    film: '<rect x="3" y="4.5" width="18" height="15" rx="1.5"/><path d="M7 4.5v15M17 4.5v15M3 9h4M3 15h4M17 9h4M17 15h4"/>',
    pen: '<path d="m4 20 1-4L16.5 4.5a2.1 2.1 0 0 1 3 3L8 19l-4 1Z"/><path d="m14.5 6.5 3 3"/>',
    seo: '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5M8 10.5h5M10.5 8v5"/>',
    seller: '<circle cx="12" cy="8" r="3.5"/><path d="M5 20.5c0-3.8 3.1-6.5 7-6.5s7 2.7 7 6.5"/>',
    check: '<path d="m5 12.5 4.5 4.5L19 7.5"/>'
  };
  const icon = (name) => `<svg class="s2-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${I[name]}</svg>`;
  const rows = (items, cls) => `<div class="s2-rows${cls ? ' ' + cls : ''}">${items.map(([a, b, c], i) => `<div class="s2-row${c === 'pay' ? ' is-key' : ''}"><i>${a.length > 3 ? icon(a) : a}</i><div><b>${b}</b>${c && c !== 'pay' ? `<span>${c}</span>` : ''}</div></div>`).join('')}</div>`;
  const cols = (a, b, opts = {}) => `<div class="s2-cols${opts.cls ? ' ' + opts.cls : ''}"><section class="${opts.bad ? 'is-bad' : ''}"><h5>${a[0]}</h5>${a.slice(1).map(x => `<p>${x}</p>`).join('')}</section><section class="${opts.good ? 'is-good' : ''}"><h5>${b[0]}</h5>${b.slice(1).map(x => `<p>${x}</p>`).join('')}</section></div>`;

  const SITE = 'https://fainopet.vercel.app/';
  const browser = (inner, url) => `<div class="s2-browser"><div class="s2-browser-bar"><i></i><i></i><i></i><span>${esc(url || '')}</span></div><div class="s2-browser-body">${inner}</div></div>`;

  const R = {
    228: (n) => wrap(n, 'hero', bg('gen-b243/s245-door.webp', 'full', 'Приоткрытая дверь, из-за которой льётся тёплый свет') +
      head('Секрет №2', 'Как получить первого клиента, даже если вы никогда ничего <em>не продавали</em>', 's2-head-hero') +
      bottom('<p class="s2-lead">Секрет №2 — про то, что умение продавать больше не нужно. Нужна конструкция, которая продаёт вместо вас</p>')),

    229: (n) => wrap(n, 'objection', bg('gen-b243/s243-listen.webp', 'right', 'Влад сидит на стуле и слушает') +
      head('Возражение', '«Услуги я понял.<br>А клиентов где <em>взять</em>?»') +
      /* 08.10 Мирослав (Google G328): без пункту «на базаре», цитата про Сашу — окремим слайдом (new-g329) */
      `<div class="s2-obj">${[['01', 'Я не умею продавать'], ['02', 'Я вчера про эти услуги узнал']].map(([a, b]) => `<div class="s2-obj-card"><i>${a}</i><p>${b}</p></div>`).join('')}</div>`),

    230: (n) => wrap(n, 'bazaar', /* 08.10 дзвінок з Владом (Google G328): лише дві картинки — без заголовка, підписів і рядка внизу */
      `<div class="s2-pair s2-pair-cap s2-pair-bare"><figure><img src="${G}gen-s246-bazaar/bazaar.webp" alt="Мужик за прилавком на базаре с табличкой «САЙТЫ»"></figure><figure><img src="${G}gen-s246-bazaar/doors.webp" alt="Он же звонит в двери по подъездам"></figure></div>`),

    231: (n) => wrap(n, 'two', bg('gen-b228/s231-two-doors.webp', 'bottom', 'Человек перед двумя дверями: за одной — ноутбук и работа, за другой — клиент') +
      head('', 'На самом деле вопроса <em>два</em>') +
      cols(['Первый', 'А у меня получится это <b>сделать</b>?'], ['Второй', 'А у меня получится это <b>продать</b>, если я не маркетолог?'], { cls: 's2-cols-big' }) +
      bottom('<p class="s2-mut">Отвечаю по порядку. Второй тяжелее</p>')),

    232: (n) => wrap(n, 'full', `<img class="s2-full" src="${G}secret2-full/s232-svazka1.webp" alt="Слайд 232 — готовая картинка Влада">`),

    233: (n) => wrap(n, 'full', `<img class="s2-full" src="${G}secret2-full/s233-svazka2.webp" alt="Слайд 233 — готовая картинка Влада">`),

    234: (n) => wrap(n, 'four', bg('gen-b228/s235-doc.webp', 'right', 'Папка-шаблон с жёлтой закладкой') +
      head('Как именно', 'Как — это четыре <em>решения</em>') +
      `<div class="s2-tiles">${[['target', 'Одна ниша', 'не распыляемся — берём одну и знаем её'], ['puzzle', 'Один шаблон', 'второй сайт занимает минуты'], ['pin', 'Топ-локации', 'города, где покупают чаще'], ['gift', 'Бесплатный сайт', 'показываем до оплаты — уговаривать нечего']].map(([ic, b, s], k) => `<section${k === 3 ? ' class="is-key"' : ''}>${icon(ic)}<b>${b}</b><span>${s}</span></section>`).join('')}</div>` +
      bottom('<p class="s2-mut">Четыре решения принимаются один раз — дальше повторяется</p>')),

    235: (n) => {
      const services = [['globe', 'AI-сайты'], ['brush', 'AI-дизайн'], ['film', 'AI-видео'], ['pen', 'Контент'], ['target', 'AI-таргет'], ['seo', 'AI-SEO'], ['seller', 'AI-продавец']];
      let grid = '<div class="s2-catalog-box"><div class="s2-catalog s2-catalog-cols">';
      services.forEach(([ic, name], c) => {
        grid += `<div class="s2-cat-col"><section class="s2-cat-head">${icon(ic)}<b>${name}</b></section>`;
        for (let r = 0; r < 3; r++) grid += `<section class="s2-cat-slot${r === 0 && c === 0 ? ' is-open' : ''}"><span>связка</span></section>`;
        grid += '</div>';
      });
      grid += '</div></div>';
      return wrap(n, 'catalog', bg('gen-b228/s235-cells.webp', 'bottom', 'Тёмная стена из одинаковых подсвеченных ячеек') +
        head('Сколько их всего', 'Это одна связка. У нас их больше <em>двадцати</em>') + grid +
        bottom('<p class="s2-lead">Семь услуг — и под каждую свои связки: кому продавать, где искать, как подойти</p><p class="s2-mut">Открыта одна. Остальные лежат готовые — их не надо придумывать</p>'));
    },

    236: (n) => wrap(n, 'versus', bg('gen-b228/s234-split-b.webp', 'bottom', 'Два одинаковых стола: пустой и со светящейся коробкой') +
      head('', 'Биржа против салона <em>груминга</em>') +
      cols(['Биржа', 'тысячи исполнителей на один заказ', 'выигрывает тот, кто дешевле', 'вы — строка в списке'], ['Салон, который теряет клиентов', 'конкурентов ноль', 'сравнивать не с кем', 'вы — единственный, кто написал'], { bad: true, good: true }) +
      bottom('<p class="s2-acc">Услуга одна и та же. Меняется только «где находим»</p>')),

    237: (n) => wrap(n, 'full', `<img class="s2-full" src="${G}secret2-full/s237-dontlove.webp" alt="Слайд 237 — готовая картинка Влада">`),

    238: (n) => wrap(n, 'full', `<img class="s2-full" src="${G}secret2-full/s238-strategy.webp" alt="Слайд 238 — готовая картинка Влада">`),

    239: (n) => wrap(n, 'full', `<img class="s2-full" src="${G}secret2-full/s239-ichnain.webp" alt="Слайд 239 — готовая картинка Влада">`),

    240: (n) => wrap(n, 'fields', head('Экран', 'Ваша работа — заполнить три <em>поля</em>') +
      `<div class="s2-mock">${[['', ['Что', 'Кому', 'Как']], ['is-filled', ['AI-сайты от $250', 'Локальному бизнесу без сайта', 'Показываем готовое']]].map(([cls, f]) => `<section class="${cls}"><header><i></i><i></i><i></i></header>${f.map((v, k) => `<label><span>${['Что', 'Кому', 'Как'][k]}</span><div>${cls ? v : ''}</div></label>`).join('')}<button type="button" tabindex="-1">Собрать сайт</button></section>`).join('<svg class="s2-mock-arrow" viewBox="0 0 40 24" fill="none" aria-hidden="true"><path d="M2 12h32M26 4l8 8-8 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')}</div>` +
      bottom('<p class="s2-mut">Реальный агент. Слева пустой шаблон, справа заполненный. Кнопки, которая что-то испортит, здесь не существует</p>')),

    241: (n) => wrap(n, 'full', /* 09.10 Мирослав: справа — сайт VIP CAR (кейс прокату авто), не грумінг; source/_img_1009_r89.py */ `<img class="s2-full" src="${G}gen-s2-1009/r089-empty-vipcar.webp" alt="Пустой шаблон и готовый сайт проката авто VIP CAR">`),

    242: (n) => wrap(n, 'safe', bg('gen-b228/s240-late-b.webp', 'right', 'Тёмный коридор, одна дверь открыта и светится') +
      head('', 'Сломать <em>невозможно</em>') +
      rows([['compass', 'Ведёт по шагам', 'не даёт перескочить и забыть'], ['lock', 'Нет кнопки «испортить»', 'ошибиться негде'], ['chat', 'Не понял — спроси у него же', 'не надо гуглить и искать курсы']]) +
      bottom('<p class="s2-acc">Первый вопрос закрыт. Второй тяжелее</p>')),

    243: (n) => wrap(n, 'sasha', `<figure class="s2-photo-right"><img src="${G}photo/sasha-bali.jpg" alt="Саша, 14 лет"></figure>` +
      head('', 'Я взял человека с худшими вводными, каких смог <em>найти</em>') +
      '<p class="s2-lead">Своего сына Сашу. 14 лет. Ни опыта, ни маркетинга, ни кода.</p>' +
      bottom('<p class="s2-mut">Он никогда никому ничего не продавал — и от руки почти не пишет, всё на компьютере</p>')),

    244: (n) => wrap(n, 'hero s2-quote', bg('gen-b228/s229-repeat.webp', 'full', 'Ряд пустых светящихся витрин') +
      head('', 'И предложил то, чего сам раньше <em>не допускал</em>', 's2-head-hero') +
      bottom('<p class="s2-big">«Давай продадим сайты, которых ещё нет»</p>')),

    245: (n) => wrap(n, 'dog', bg('gen-b228/s240-late-a.webp', 'bottom', 'Пустая улица нового города перед рассветом') +
      head('', 'Ниша нашлась из-за <em>собаки</em>') +
      '<p class="s2-lead s2-lead-wide">Знакомая переехала в новый город и хотела записать собаку на груминг. Не смогла нигде.</p>' +
      bottom('<p class="s2-acc">У всех салонов сайты такие, что записаться нельзя</p>')),

    246: (n) => wrap(n, 'niche', bg('gen-b228/s229-repeat-b.webp', 'right', 'Светящаяся витрина офлайн-бизнеса') +
      head('', 'Почему именно такие <em>ниши</em>') +
      rows([['shop', 'Бизнес офлайн и работает', 'не стартап, а живая точка'], ['users', 'Клиенты уже есть', 'их не надо искать — их теряют'], ['phoneOff', 'Сайта нет или он мешает', 'записаться невозможно']]) +
      bottom('<p class="s2-acc">И шаблон под такую нишу у нас уже готов</p>')),

    247: (n) => wrap(n, 'algo', head('', 'Алгоритм, который я ему <em>дал</em>') +
      `<ol class="s2-steps">${[['Найди 10 салонов', 'в одном городе'], ['Напиши каждому', '«можно записаться?»'], ['Когда ответят', '«хотел через сайт — не вышло»'], ['«Я вам его уже сделал»', 'обычно беру $1.000, вам бесплатно'], ['Сказал «да»', 'агент собирает сайт по шаблону']].map(([b, s], k) => `<li${k === 4 ? ' class="is-key"' : ''}><i>0${k + 1}</i><div><b>${b}</b><span>${s}</span></div></li>`).join('')}</ol>` +
      bottom('<p class="s2-mut">Саше хватило первой десятки. Обычно нужно больше — посчитаем в следующем секрете</p><p class="s2-acc">Пять шагов. Ни одного, где надо уметь продавать</p>')),

    248: (n) => wrap(n, 'chat', bg('gen-b243/s264-night-a.webp', 'right', 'Смартфон на тумбочке ночью') +
      head('', 'Вот что именно <em>пишем</em>') +
      `<div class="s2-chat">${[['me', 'Первое сообщение', 'Добрый день! А к вам можно записать собаку на груминг?'], ['them', 'Отвечают', 'Да, конечно. На какое число?'], ['me', 'Второе', 'Я пробовал записаться через сайт — не получилось. Вы так много клиентов теряете?'], ['me key', 'Третье — ради него всё', 'Я сделал вам новый сайт, где можно записаться за минуту. Обычно беру за такие $1.000 — вам сделал бесплатно. Хотите посмотреть?']].map(([c, l, t]) => `<div class="s2-msg ${c}"><i>${l}</i><p>${t}</p></div>`).join('')}</div>`),

    249: (n) => wrap(n, 'why', bg('gen-b228/s235-doc-pad.webp', 'right', 'Папка с готовой работой на тёмном фоне') +
      head('', 'Почему это <em>срабатывает</em>') +
      '<p class="s2-lead">Вы ничего не продаёте. Вы уже сделали — и отдаёте. Человеку нечего согласовывать, нечего ждать и нечем рисковать.</p><p class="s2-acc">Клиент убеждает себя сам</p>' +
      bottom('<p class="s2-mut">И так можно сколько угодно: сайт агенту стоит копейки. Метод посчитан и повторяем — цифры будут в следующем секрете</p>')),

    250: (n) => wrap(n, 'result', `<figure class="s2-photo-right s2-photo-sasha"><img src="${G}photo/sasha.webp" alt="Саша и Влад с ноутбуком"></figure>` +
      head('Кто это сделал', '<em>Саша</em>') +
      '<p class="s2-mut">Первая продажа — меньше чем через сутки</p>' +
      `<div class="s2-kpi"><section><h5>Сколько заняло</h5><b>Меньше 24 часов</b><span>алгоритм я показал один раз</span></section><section><h5>Сколько принесло</h5><b>$250</b><span>дальше его вёл агент, а не я</span></section></div>` +
      '<p class="s2-anchor"><b>$1.000</b> — сколько стоит работа. <b>$250</b> — сколько берёт новичок за первую. Эта разница и есть ваш аргумент</p>' +
      bottom('<p class="s2-acc">Мой сын заработал свои первые деньги раньше, чем я в его возрасте узнал, что так вообще можно</p>')),

    251: (n) => wrap(n, 'site', head('', 'Вот этот <em>сайт</em>') +
      `<a class="s2-live" href="${SITE}" target="_blank" rel="noopener">${browser(`<img class="s2-live-poster" src="${G}photo/sasha-site-faino.jpg" alt="Сайт ФАЙНО!pet"><iframe data-src="${SITE}" title="Сайт ФАЙНО!pet — грумінг-салон у Харкові" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" sandbox="allow-scripts allow-same-origin"></iframe>`, 'fainopet.vercel.app')}</a>` +
      bottom('<p class="s2-lead">ФАЙНО!pet — грумінг-салон у Харкові<br><span class="s2-mut">Услуги, цены, работы мастеров, запись ↗</span></p><p class="s2-acc">Живой. Можно открыть прямо сейчас</p>')),

    252: (n) => wrap(n, 'versus', bg('gen-b228/s231-desk.webp', 'bottom', 'Конверт, оставленный на столе') +
      head('', 'Вы не продаёте. Вы <em>отдаёте</em>') +
      cols(['Как было', 'уговорить', 'отработать возражения', 'дожать сомневающегося'], ['Как теперь', 'отдал готовое', 'показал тем, кому подходит', 'работаешь только с теми, кто сказал «да»'], { bad: true, good: true }) +
      bottom('<p class="s2-acc">Услуг у вас безлимит — их делают агенты. Уговаривать незачем</p>')),

    253: (n) => wrap(n, 'thesis', bg('gen-b243/s264-night-b.webp', 'full', 'Окно ночного города изнутри, ноутбук на подоконнике') +
      head('', 'И общаться уметь <em>не надо</em>', 's2-head-hero') +
      bottom('<p class="s2-lead">Что ответить, как снять сомнение, чем закрыть — переписку ведёт нейронка.</p><p class="s2-acc">Отдельного навыка продаж здесь просто нет</p>')),

    254: (n) => wrap(n, 'chain s2-chain-more', bg('gen-s248/three-systems-office.png', 'bottom', 'Три светящихся панели над столом') +
      head('', 'Сайт — только первая <em>связка</em>') +
      `<div class="s2-chain s2-chain-v">` + [['Кому', 'Сайт уже хороший', 'ему — AI-SEO, чтобы советовали нейросети'], ['Кому', 'Заявки идут, отвечать некому', 'ему — AI-продавца'], ['Кому', 'Ведёт контент сам', 'ему — контент-завод']].map(([i, b, s], k) => `<section class="s2-chain-node${k === 2 ? ' is-key' : ''}"><i>${i}</i><b>${b}</b><span>${s}</span></section>`).join('') + '</div>' +
      bottom('<p class="s2-acc">Формула та же. Меняется одна переменная</p>')),

    255: (n) => wrap(n, 'tags', bg('gen-b228/s229-repeat-c.webp', 'bottom', 'Ряд одинаковых светящихся павильонов') +
      head('', 'И под каждую — своя модель <em>поиска</em>') +
      `<div class="s2-tags">${['стоматология', 'барбершоп', 'груминг', 'оптика', 'кондитерская', 'автомойка', 'студия маникюра', 'кофейня'].map((t, k) => `<span${k === 2 ? ' class="is-key"' : ''}>${t}</span>`).join('')}</div>` +
      bottom('<p class="s2-lead">Не «попробуйте разное», а последовательность, которую уже прогнали и знают, чего от неё ждать</p>')),

    256: (n) => wrap(n, 'objection s2-objection-late', bg('gen-b243/s261-drafts.webp', 'bottom', 'Три скомканных листа и один чистый на столе дизайнера') +
      head('Возражение', '«А если ему не <em>понравится</em>?»') +
      '<p class="s2-lead s2-lead-wide">Правки — это норма, а не провал. Дизайнер переделывает по три раза и берёт за это деньги.</p>' +
      bottom('<p class="s2-acc">У вас правка занимает минуты, а не дни</p>')),

    257: (n) => wrap(n, 'demo', bg('gen-b228/s229-repeat-v2.webp', 'full', 'Витрина, в которую смотрят до покупки') +
      head('', 'И главное — вы показываете <em>до оплаты</em>', 's2-head-hero') +
      bottom('<p class="s2-lead">Он видит демо раньше, чем платит.</p><p class="s2-acc">Ситуация «заплатил и разочаровался» просто не возникает</p>')),

    258: (n) => wrap(n, 'hero s2-switch', bg('gen-b243/s260-switch-b.webp', 'full', 'Большая жёлтая кнопка пуска на тёмной панели') +
      head('', 'Ни один из них не стал <em>специалистом</em>', 's2-head-hero') +
      bottom('<p class="s2-big">Все просто включили машину</p>')),

    259: (n) => wrap(n, 'close', bg('gen-b243/s264-night-b.webp', 'right', 'Ночное окно, вид изнутри') +
      head('', 'Петля закрыта. Осталось <em>одно</em>') +
      '<p class="s2-lead">Продавать вы умеете — точнее, уметь и не надо.</p><p class="s2-acc">Остался вопрос, который я слышу чаще всех: а когда это делать и где брать людей?</p>' +
      bottom('<div class="s2-trial"><span>Видите себя внутри? Напишите</span><b>«вижу»</b></div>'))
  };

  window.Secret2 = {
    render(d) {
      const n = Number(d.n);
      /* 22.09 Мирослав: 242–259 — цілі слайди-картинки з вшитим текстом (GPT Image 2.5), assets/gen-secret2-full/sNNN.webp */
      if (FULL.has(n)) return wrap(n, 'full', `<img class="s2-full" src="${G}gen-secret2-full/s${n}.webp?v=${FULL_V}" alt="${esc(d.t)}">`);
      const fn = R[n];
      return fn ? fn(n, d) : wrap(n, 'todo', head('', esc(d.t)) + ph('слайд ещё не оформлен'));
    }
  };
})();
