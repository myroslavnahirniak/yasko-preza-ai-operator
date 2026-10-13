#!/usr/bin/env python3
"""Собирает passport.html — паспорт стиля презентации (5 вариантов, 10 слайдов, референсы). Картинки — data URI."""
import base64, os
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(here)
def img(name):
    p=os.path.join(root,'shots','passport',name)
    return 'data:image/jpeg;base64,'+base64.b64encode(open(p,'rb').read()).decode()
IM={k:img(v) for k,v in {'gold':'vlad-gold.jpg','studio':'vlad-studio.jpg','office':'office.jpg',**{f's{n:02d}':f's{n:02d}.jpg' for n in range(1,11)}}.items()}

ICONS='''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-coin" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5c0-1 1-1.7 2.5-1.7s2.5.7 2.5 1.7-1 1.5-2.5 1.9-2.5.9-2.5 1.9 1 1.7 2.5 1.7 2.5-.7 2.5-1.7"/></symbol>
<symbol id="i-tag" viewBox="0 0 24 24"><path d="M3 12V5a2 2 0 0 1 2-2h7l9 9-9 9-9-9Z"/><circle cx="8" cy="8" r="1.4"/></symbol>
<symbol id="i-gear" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/></symbol>
<symbol id="i-cap" viewBox="0 0 24 24"><path d="M2.5 9.5 12 5l9.5 4.5L12 14 2.5 9.5Z"/><path d="M6 11.5V16c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5v-4.5M21.5 9.5V15"/></symbol>
<symbol id="i-book" viewBox="0 0 24 24"><path d="M4 4.5h6.5a2 2 0 0 1 2 2V20a1.5 1.5 0 0 0-1.5-1.5H4V4.5ZM20 4.5h-6.5a2 2 0 0 0-2 2V20a1.5 1.5 0 0 1 1.5-1.5H20V4.5Z"/></symbol>
<symbol id="i-folder" viewBox="0 0 24 24"><path d="M3 6.5a2 2 0 0 1 2-2h4.5l2 2H19a2 2 0 0 1 2 2V18a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6.5Z"/></symbol>
<symbol id="i-battery" viewBox="0 0 24 24"><rect x="2.5" y="8" width="16" height="9" rx="1.5"/><path d="M21.5 11v3M5.5 11v3"/></symbol>
<symbol id="i-hourglass" viewBox="0 0 24 24"><path d="M6 3h12M6 21h12M7.5 3v3.5c0 2.2 3 3.6 3 5.5s-3 3.3-3 5.5V21M16.5 3v3.5c0 2.2-3 3.6-3 5.5s3 3.3 3 5.5V21"/></symbol>
<symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13 2.5 5 13.5h6l-1 8 9-11.5h-6l1-7.5Z"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M4 4l16 16"/></symbol>
<symbol id="i-eye" viewBox="0 0 24 24"><path d="M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6Z"/><circle cx="12" cy="12" r="2.6"/></symbol>
<symbol id="i-door" viewBox="0 0 24 24"><path d="M5 21V4.5a1.5 1.5 0 0 1 1.5-1.5h11A1.5 1.5 0 0 1 19 4.5V21M3 21h18"/><circle cx="14.5" cy="12.5" r="1"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path d="M7 4.5v15l12-7.5-12-7.5Z"/></symbol>
<symbol id="i-spark" viewBox="0 0 24 24"><path d="M12 2.5c.6 5 2.5 6.9 7.5 7.5-5 .6-6.9 2.5-7.5 7.5-.6-5-2.5-6.9-7.5-7.5 5-.6 6.9-2.5 7.5-7.5Z"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24"><path d="M4 5.5h16v10H9l-5 4v-14Z"/></symbol>
</defs></svg>'''

def mocks(v, photo_title):
    return f'''
<div class="mockrow">
  <figure class="mock {v} m-title"><span class="disc"></span><span class="big">AI</span><span class="card"></span><img class="photo" src="{photo_title}" alt=""><div class="txt"><span class="eyebrow">Реалити-шоу AI-агентов</span><h4>Как заработать первые <b>$1.000</b> на AI в 2026</h4><span class="by">Влад Яско · система AI-Оператор</span></div><figcaption>#1 · титул · вау</figcaption></figure>
  <figure class="mock {v} m-quote"><span class="eyebrow">Узнаёте себя?</span><p class="q">«Мир рванул вперёд, а я стою на месте. Меня что, скоро заменят?»</p><span class="plus"><svg><use href="#i-plus"/></svg>в чат, если это про вас</span><span class="pills"><i>Мир</i><i>рванул</i><i>→</i></span><figcaption>#5 · цитата · контент</figcaption></figure>
  <figure class="mock {v} m-content"><h4>Я сегодня выкладываю всё как есть</h4><div class="cards"><div><svg><use href="#i-coin"/></svg><b>На чём зарабатываю</b><span>я и моя команда</span></div><div><svg><use href="#i-tag"/></svg><b>Что продаём</b><span>и за сколько</span></div><div><svg><use href="#i-gear"/></svg><b>Чем это делаем</b><span>какими агентами</span></div></div><p class="acc">Взамен прошу одно — быть включённым</p><figcaption>#3 · три тезиса · контент</figcaption></figure>
</div>'''

SLIDES=[
 (1,'wow','Как заработать первые $1.000 на AI в 2026','Портрет Влада (поки чорно-золотий з лендингу, далі — фото від Стаса) + орбіти агентів і aurora, що «дихає», поки люди підключаються.','Повільні орбіти, слова заголовка проявляються, більше нічого.','Живе фото по пояс на чорному (Стас).'),
 (2,'wow','Знаете это чувство: появилось что-то новое — а ты мимо','Емоційний кадр на весь екран: перон, поїзд пішов, один стоїть (Soul Влада або гіфка). Заголовок поверх, «Сегодня я — этот человек» приходить окремим кліком.','Кросфейд кадру → рядок заголовка → пауза → акцентний рядок.','Кадр за метапромтом #2 або гіфка.'),
 (3,'content','Я сегодня выкладываю всё как есть','Три тези як три SVG-картки (монета · тег · шестерня), без емодзі. Одна акцентна строка внизу.','Картки виїжджають одна за одною (3 × 120 мс), далі спокій.','— (все є).'),
 (4,'content','Сейчас перечислю, кому я сегодня полезен','Механіка «+». Замість абзаців — великий жовтий плюс, який пульсує, і один рядок «анонімно, ніхто не побачить».','Пульс плюса 2 с, безперервно — це підказка залу.','—'),
 (5,'wow','«Мир рванул вперёд, а я стою на месте. Меня что, скоро заменят?»','Перша цитата серії — з візуальним якорем: таймлапс міста/гіфка «всі рухаються, він стоїть» на фоні, цитата поверх.','Відео/гіфка в лупі, цитата проявляється рядками.','Гіфка або кадр (метапромт #5).'),
 (6,'content','«В рилсах все рассказывают… А я пользуюсь ChatGPT как гуглом»','Мем-формат: ліворуч телефон з рілсами, праворуч вікно ChatGPT із запитом про погоду. Цитата над ними.','Два кадри з’являються по черзі, як «vs».','Два скріни (робимо самі).'),
 (7,'content','«Годы и бабки вложил в профессию — а расти некуда, и тех денег не хватает»','Мінімальний шаблон серії: лапки-глиф, цитата, мітка, «+ в чат». Без картинки — ритм після двох візуальних.','Тільки проявлення тексту.','—'),
 (8,'content','«Курсы купил, все прошёл — а клиентов и денег так и не увидел»','Той самий шаблон + один SVG-якір (полиця сертифікатів → порожній гаманець) у кутку, дрібно.','Проявлення тексту.','SVG робимо самі.'),
 (9,'content','«Всё, что нахожу, — либо развод, либо для технических задротов»','Шаблон серії. Можлива інверсія (жовтий слайд) як ритмічний удар перед експертом.','Проявлення тексту; інверсія — миттєва.','—'),
 (10,'content','«Я эксперт или у меня свой бизнес… а как, нормально никто не показывает»','Шаблон серії, найдовша цитата — шрифт на ступінь менший, дві колонки не робимо.','Проявлення тексту.','—'),
]
TYPE={'wow':'Вау','video':'Відео','content':'Контент'}
def slide_cards():
    out=[]
    for n,t,title,vis,anim,asset in SLIDES:
        out.append(f'''<article class="slide-card">
  <img src="{IM[f's{n:02d}']}" alt="Слайд {n} зараз" loading="lazy">
  <div class="sc-body">
    <div class="sc-head"><span class="num">#{n}</span><span class="type t-{t}">{TYPE[t]}</span></div>
    <h4>{title}</h4>
    <dl><dt>Візуал</dt><dd>{vis}</dd><dt>Анімація</dt><dd>{anim}</dd><dt>Потрібно</dt><dd>{asset}</dd></dl>
  </div></article>''')
    return '\n'.join(out)

HTML='''<meta charset="utf-8"><title>Паспорт стилю AI-Оператор</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{--bg:#0B0907;--bg2:#141110;--panel:#1A1614;--line:#2B2521;--line2:#3B332D;--ink:#F5EFE0;--ink2:#CFC6B4;--mut:#A39B8B;--acc:#FDD506;--acc-ink:#0B0900;--red:#FF5C6C;
  --fd:"Unbounded","Manrope",sans-serif;--fb:"Manrope",-apple-system,"Segoe UI",sans-serif;--fm:"JetBrains Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#FBF7EC;--bg2:#F3EDDD;--panel:#FFFFFF;--line:#E4DCC8;--line2:#CFC5AE;--ink:#161310;--ink2:#3E3730;--mut:#6E6558;--acc:#F2C300;--acc-ink:#0B0900}}
:root[data-theme="light"]{--bg:#FBF7EC;--bg2:#F3EDDD;--panel:#FFFFFF;--line:#E4DCC8;--line2:#CFC5AE;--ink:#161310;--ink2:#3E3730;--mut:#6E6558;--acc:#F2C300;--acc-ink:#0B0900}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--fb);line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--ink);text-decoration-color:var(--acc);text-underline-offset:3px}
.wrap{max-width:1120px;margin:0 auto;padding:56px 24px 120px}
.eyebrow{font-family:var(--fm);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--acc)}
h1{font-family:var(--fd);font-weight:800;font-size:clamp(30px,5vw,58px);line-height:1;letter-spacing:-.03em;margin:14px 0 18px;text-wrap:balance}
h2{font-family:var(--fd);font-weight:700;font-size:clamp(22px,3vw,34px);line-height:1.1;letter-spacing:-.02em;margin:0 0 10px;text-wrap:balance}
h3{font-family:var(--fd);font-weight:700;font-size:18px;margin:0 0 6px;letter-spacing:-.01em}
p{margin:0;max-width:68ch}
.lead{font-size:19px;color:var(--ink2);max-width:60ch}
section{padding:56px 0 0;border-top:1px solid var(--line);margin-top:56px}
section:first-of-type{border-top:0;margin-top:0;padding-top:24px}
.sec-head{display:grid;grid-template-columns:1fr;gap:6px;margin-bottom:26px}
.sec-head p{color:var(--mut);max-width:70ch}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
@media(max-width:820px){.grid3,.grid2{grid-template-columns:1fr}}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 20px 18px}
.tile h3{display:flex;align-items:center;gap:10px}
.tile p{color:var(--ink2);font-size:15px}
.tile .rule{font-family:var(--fm);font-size:12px;color:var(--mut);margin-top:12px;letter-spacing:.04em}
.kv{display:grid;grid-template-columns:150px 1fr;gap:8px 18px;font-size:15px}
.kv dt{color:var(--mut);font-family:var(--fm);font-size:12px;letter-spacing:.08em;text-transform:uppercase;padding-top:3px}
.kv dd{margin:0;color:var(--ink2)}
.swatches{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0 4px}
.sw{display:flex;align-items:center;gap:8px;font-family:var(--fm);font-size:12px;color:var(--mut)}
.sw i{width:26px;height:26px;border-radius:8px;border:1px solid var(--line2);display:inline-block}
/* референсы */
.ref{display:grid;grid-template-columns:1fr;gap:10px}
.ref h3 a{text-decoration:none;border-bottom:2px solid var(--acc)}
.ref ul{margin:0;padding-left:18px;color:var(--ink2);font-size:15px}
.ref .take{font-size:14px;color:var(--ink);background:color-mix(in srgb,var(--acc) 12%,transparent);border-left:3px solid var(--acc);padding:8px 12px;border-radius:0 8px 8px 0}
/* иконки */
.iconrow{display:grid;grid-template-columns:repeat(8,1fr);gap:10px}
@media(max-width:820px){.iconrow{grid-template-columns:repeat(4,1fr)}}
.iconrow div{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px 8px 10px;display:flex;flex-direction:column;align-items:center;gap:8px;font-family:var(--fm);font-size:11px;color:var(--mut)}
.iconrow svg{width:28px;height:28px;fill:none;stroke:var(--acc);stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}
/* варианты */
.variant{margin-top:34px;padding-top:30px;border-top:1px dashed var(--line2)}
.variant:first-of-type{border-top:0;padding-top:0}
.vhead{display:grid;grid-template-columns:1.1fr .9fr;gap:24px;align-items:start;margin-bottom:18px}
@media(max-width:820px){.vhead{grid-template-columns:1fr}}
.vhead .num{font-family:var(--fm);font-size:12px;color:var(--acc);letter-spacing:.2em}
.vhead p{color:var(--ink2);font-size:15px}
.tokens{font-family:var(--fm);font-size:12.5px;color:var(--mut);display:grid;grid-template-columns:auto 1fr;gap:4px 14px}
.tokens b{color:var(--ink);font-weight:500}
.mockrow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
@media(max-width:820px){.mockrow{grid-template-columns:1fr}}
.mock{position:relative;aspect-ratio:1;margin:0;overflow:hidden;border-radius:6px;container-type:size;border:1px solid var(--line);
  display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:7cqw;gap:3.2cqw;font-family:var(--fb);color:#fff;background:#000}
.mock figcaption{position:absolute;left:0;right:0;bottom:0;padding:2cqw 3cqw;font-family:var(--fm);font-size:2.8cqw;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.55);text-align:left;background:linear-gradient(transparent,rgba(0,0,0,.55))}
.mock .eyebrow{font-size:3cqw;letter-spacing:.18em}
.mock h4{font-family:var(--fd);font-weight:700;font-size:7.6cqw;line-height:1.06;letter-spacing:-.03em;margin:0;text-wrap:balance}
.mock .by{font-family:var(--fm);font-size:2.9cqw;letter-spacing:.12em;text-transform:uppercase;opacity:.7}
.mock .q{font-family:var(--fb);font-weight:700;font-size:7cqw;line-height:1.16;letter-spacing:-.025em;max-width:20ch}
.mock .plus{display:inline-flex;align-items:center;gap:1.8cqw;font-family:var(--fm);font-size:3cqw;letter-spacing:.12em;text-transform:uppercase;opacity:.8}
.mock .plus svg{width:6cqw;height:6cqw;border-radius:50%;padding:1cqw;background:var(--m-acc,#FDD506);stroke:#000;stroke-width:2.5;fill:none}
.mock .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:2.4cqw;width:100%}
.mock .cards div{display:flex;flex-direction:column;align-items:center;gap:1.6cqw;padding:4.5cqw 2cqw;font-size:3.4cqw;line-height:1.2}
.mock .cards b{font-weight:700;font-size:3.7cqw}
.mock .cards span{opacity:.6;font-size:3cqw}
.mock .cards svg{width:11cqw;height:11cqw;fill:none;stroke:var(--m-acc,#FDD506);stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}
.mock .acc{color:var(--m-acc,#FDD506);font-weight:700;font-size:3.9cqw}
.mock .photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 15%}
.mock .txt{position:relative;z-index:2;display:flex;flex-direction:column;gap:3cqw;align-items:center}
.mock .disc,.mock .big,.mock .card,.mock .pills{display:none}
.v1 .disc,.v2 .big,.v4 .card,.v4 .pills{display:block}.v4 .pills{display:flex}
/* V1 Glow — Velocity / Kontour / Formix: тёплый чёрный, свет снизу, стеклянные карточки, портрет на диске */
.v1{--m-acc:#FDD506;background:#0E0906;background-image:radial-gradient(70cqw 40cqw at 50% 112%,rgba(253,190,6,.55),rgba(253,190,6,.12) 45%,transparent 70%)}
.v1.m-title{padding:0;display:grid;grid-template-columns:52% 48%;text-align:left}
.v1.m-title .txt{align-items:flex-start;padding:8cqw 0 8cqw 8cqw;justify-content:center}
.v1.m-title h4{font-size:6.3cqw}
.v1 h4 b{color:#FDD506}
.v1.m-title .disc{position:absolute;right:-8cqw;top:12cqw;width:62cqw;height:62cqw;border-radius:50%;background:radial-gradient(circle at 40% 35%,#FFE45C,#F2B800 60%,#8a6600);box-shadow:0 0 30cqw rgba(253,190,6,.45)}
.v1.m-title .photo{position:absolute;inset:auto;right:-6cqw;bottom:0;width:62cqw;height:82cqw;object-fit:cover;object-position:50% 0;-webkit-mask:linear-gradient(90deg,transparent 0,#000 26%);mask:linear-gradient(90deg,transparent 0,#000 26%);filter:contrast(1.05)}
.v1 .eyebrow{color:#FDD506;border:1px solid rgba(253,213,6,.35);border-radius:100px;padding:1.2cqw 2.6cqw;background:rgba(253,213,6,.08)}
.v1 .cards div{border-radius:3.4cqw;border:1px solid rgba(255,255,255,.08);background:linear-gradient(180deg,rgba(255,255,255,.03),rgba(253,190,6,.22));box-shadow:inset 0 -6cqw 8cqw -6cqw rgba(253,190,6,.55)}
.v1 .cards svg{width:12cqw;height:12cqw;padding:2.6cqw;border-radius:50%;background:radial-gradient(circle,rgba(253,213,6,.35),transparent 70%);stroke:#FDD506}
.v1 .plus{color:#FDD506;border:1px solid rgba(253,213,6,.4);border-radius:100px;padding:1.4cqw 3cqw;box-shadow:0 0 8cqw rgba(253,190,6,.35)}
.v1.m-quote::before{content:"";position:absolute;left:50%;top:50%;width:80cqw;height:80cqw;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,rgba(253,190,6,.18),transparent 60%)}
/* V2 Giant Type — Kensei / Kontour: гигантское слово, портрет режет текст, чёрный + жёлтый, мета мелким моно */
.v2{--m-acc:#FDD506;background:#000}
.v2.m-title{padding:0;justify-content:flex-end;align-items:flex-start;text-align:left}
.v2.m-title .big{position:absolute;left:-2cqw;bottom:-4cqw;font-family:var(--fd);font-weight:800;font-size:34cqw;line-height:.85;letter-spacing:-.06em;color:#FDD506;z-index:1}
.v2.m-title .photo{position:absolute;inset:auto;right:2cqw;bottom:0;width:58cqw;height:78cqw;object-fit:cover;object-position:50% 0;z-index:2;filter:grayscale(1) contrast(1.1);-webkit-mask:linear-gradient(180deg,#000 80%,transparent);mask:linear-gradient(180deg,#000 80%,transparent)}
.v2.m-title .txt{align-items:flex-start;padding:7cqw;z-index:3;position:absolute;left:0;top:0}
.v2.m-title h4{font-size:5.4cqw;max-width:13ch;color:#fff}
.v2.m-title .by{color:#888}
.v2 .eyebrow{color:#888}
.v2.m-quote{background:#F4F1EA;color:#000;align-items:flex-start;text-align:left}
.v2.m-quote .eyebrow{color:#000}
.v2.m-quote .q{font-family:var(--fd);font-weight:700;font-size:7cqw;letter-spacing:-.04em;line-height:1.02;max-width:14ch}
.v2.m-quote .q::before{content:"";display:inline-block;width:2.4cqw;height:2.4cqw;border-radius:50%;background:#FDD506;margin-right:2cqw;vertical-align:middle}
.v2 .plus{color:#000;opacity:.7}.v2 .plus svg{background:#000;stroke:#FDD506}
.v2.m-content h4{font-size:5.4cqw;text-align:left;align-self:flex-start;max-width:14ch}
.v2 .cards{grid-template-columns:1fr 1fr;grid-auto-rows:1fr}
.v2 .cards div{align-items:flex-start;text-align:left;border:1px solid #2a2a2a;border-radius:2.2cqw;background:#0d0d0d;padding:3cqw}
.v2 .cards div:first-child{grid-column:span 2;flex-direction:row;align-items:center;background:#FDD506;color:#000;border-color:#FDD506}
.v2 .cards div:first-child svg{stroke:#000}.v2 .cards div:first-child span{color:#3a3000;opacity:1}
.v2 .cards svg{stroke:#FDD506}
.v2 .acc{align-self:flex-start;text-align:left;font-family:var(--fm);font-size:2.5cqw;letter-spacing:.14em;text-transform:uppercase;color:#888}
/* V3 Keynote Black — Apple / OpenAI: чистый чёрный, белый Unbounded, жёлтое одно слово */
.v3{--m-acc:#FDD506;background:#000}
.v3.m-title{justify-content:flex-end;align-items:flex-start;text-align:left;padding:8cqw}
.v3.m-title .photo{filter:grayscale(1) contrast(1.05);opacity:.9;-webkit-mask:linear-gradient(180deg,#000 40%,transparent 92%);mask:linear-gradient(180deg,#000 40%,transparent 92%)}
.v3.m-title .txt{align-items:flex-start}
.v3.m-title h4{font-size:7.4cqw;max-width:11ch}
.v3 h4 b{color:#FDD506}
.v3 .eyebrow{color:#9a9a9a}
.v3 .q{font-size:7.2cqw}
.v3.m-quote::before{content:"“";font-family:var(--fd);font-size:20cqw;line-height:.6;color:#FDD506;font-weight:800;margin-bottom:-2cqw}
.v3 .cards div{border-top:1px solid #333}
/* V4 Paper — Zenrixa / Material Expressive: светлая бумага, пилюли, чёрный текст, портрет в чёрной карточке */
.v4{--m-acc:#0B0900;background:#F3EFE6;color:#0B0900}
.v4 .eyebrow{color:#0B0900;background:#FDD506;border-radius:100px;padding:1.2cqw 2.6cqw}
.v4.m-title{padding:0;justify-content:flex-end;align-items:flex-start;text-align:left}
.v4.m-title .card{position:absolute;right:6cqw;top:6cqw;width:46cqw;height:52cqw;border-radius:5cqw;background:#0B0900;overflow:hidden}
.v4.m-title .photo{position:absolute;inset:auto;right:6cqw;top:6cqw;width:46cqw;height:52cqw;border-radius:5cqw;object-position:50% 0;filter:contrast(1.05)}
.v4.m-title .txt{align-items:flex-start;padding:0 8cqw 8cqw}
.v4.m-title h4{font-size:6.6cqw;max-width:12ch;font-family:var(--fb);font-weight:700;letter-spacing:-.04em}
.v4 h4 b{color:#B08900}
.v4 .by{color:#6a6250}
.v4 .q{color:#0B0900;font-family:var(--fb);font-weight:600;font-size:7cqw;letter-spacing:-.03em}
.v4.m-quote .pills{display:flex;gap:1.2cqw;margin-top:2cqw}
.v4.m-quote .pills i{font-style:normal;font-size:3.2cqw;padding:1.8cqw 3.6cqw;border-radius:100px;background:#fff;border:1px solid #ddd6c6}
.v4.m-quote .pills i:nth-child(2){background:#FDD506;border-color:#FDD506}.v4.m-quote .pills i:nth-child(3){background:#0B0900;color:#fff;border-color:#0B0900}
.v4 .plus svg{background:#0B0900;stroke:#FDD506}
.v4 .cards div{background:#fff;border-radius:100px;padding:5cqw 2cqw;box-shadow:0 1.5cqw 4cqw rgba(60,40,0,.10)}
.v4 .cards div:nth-child(2){background:#FDD506}.v4 .cards div:nth-child(3){background:#0B0900;color:#fff}
.v4 .cards div:nth-child(3) svg{stroke:#FDD506}
.v4 .cards svg{stroke:#0B0900}
.v4 .cards span{opacity:.55}
.v4 .acc{color:#0B0900;font-weight:600}
/* V5 Film — кино: кадр на весь экран, зерно, текст снизу слева, жёлтая линия */
.v5{--m-acc:#FDD506;background:#000;justify-content:flex-end;align-items:flex-start;text-align:left;padding:7cqw}
.v5 .photo{filter:saturate(.75) contrast(1.08) brightness(.8);opacity:1}
.v5::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05) 30%,rgba(0,0,0,.85) 100%);pointer-events:none}
.v5 .txt,.v5 .eyebrow,.v5 .q,.v5 .plus,.v5 h4,.v5 .cards,.v5 .acc{position:relative;z-index:2}
.v5 .txt{align-items:flex-start}
.v5 h4{font-family:var(--fb);font-weight:700;font-size:6cqw;letter-spacing:-.03em}
.v5 h4 b{color:#FDD506}
.v5 .eyebrow{color:#FDD506;border-left:.8cqw solid #FDD506;padding-left:2cqw}
.v5.m-quote{background:#000 url(OFFICE) center/cover;justify-content:flex-end;align-items:flex-start}
.v5.m-quote .q{font-size:6.2cqw;max-width:22ch}
.v5.m-content{background:#000 url(OFFICE) center/cover}
.v5 .cards{grid-template-columns:1fr;gap:1.2cqw;text-align:left}
.v5 .cards div{flex-direction:row;align-items:center;gap:2.6cqw;padding:1.4cqw 0;border-top:1px solid rgba(255,255,255,.25);justify-content:flex-start}
.v5 .cards div svg{width:5.5cqw;height:5.5cqw;flex:0 0 auto}
.v5 .cards b{font-size:4cqw}
.v5 .acc{font-family:var(--fm);font-size:2.6cqw;letter-spacing:.14em;text-transform:uppercase}
/* 10 слайдов */
.slides{display:grid;grid-template-columns:1fr;gap:14px}
.slide-card{display:grid;grid-template-columns:200px 1fr;gap:20px;background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden}
@media(max-width:820px){.slide-card{grid-template-columns:1fr}}
.slide-card img{width:100%;height:100%;object-fit:cover;aspect-ratio:1;display:block}
.sc-body{padding:18px 20px 18px 0}
@media(max-width:820px){.sc-body{padding:0 18px 18px}}
.sc-head{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.num{font-family:var(--fm);font-size:12px;color:var(--mut);letter-spacing:.1em}
.type{font-family:var(--fm);font-size:11px;letter-spacing:.14em;text-transform:uppercase;padding:3px 9px;border-radius:100px;border:1px solid var(--line2);color:var(--ink2)}
.t-wow{background:var(--acc);color:var(--acc-ink);border-color:transparent;font-weight:500}
.t-video{border-color:var(--acc);color:var(--acc)}
.slide-card h4{font-family:var(--fd);font-weight:700;font-size:16px;line-height:1.2;margin:0 0 10px;letter-spacing:-.01em}
.slide-card dl{display:grid;grid-template-columns:86px 1fr;gap:4px 12px;margin:0;font-size:14px}
.slide-card dt{font-family:var(--fm);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);padding-top:2px}
.slide-card dd{margin:0;color:var(--ink2)}
/* чеклист */
.check{list-style:none;padding:0;margin:0;display:grid;gap:8px}
.check li{display:grid;grid-template-columns:22px 1fr;gap:12px;align-items:start;font-size:15px;color:var(--ink2)}
.check li::before{content:"";width:18px;height:18px;border:1.5px solid var(--acc);border-radius:5px;margin-top:2px}
.note{font-family:var(--fm);font-size:12.5px;color:var(--mut);margin-top:10px}
.pill{display:inline-block;font-family:var(--fm);font-size:11px;letter-spacing:.12em;text-transform:uppercase;border:1px solid var(--line2);border-radius:100px;padding:3px 9px;color:var(--mut);margin-right:6px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
ICONS_HERE
<div class="wrap">

<section>
  <div class="eyebrow">Преза ефіру «AI-Оператор» · v6 · 08.09.2026</div>
  <h1>Паспорт стилю<br>і перші десять слайдів</h1>
  <p class="lead">Що затвердити: один із п'яти напрямів дизайну, три типи слайдів, правила анімації, фото і персонажа, набір іконок замість емодзі. Далі — перші десять слайдів із пропозицією по кожному.</p>
  <div class="swatches"><span class="sw"><i style="background:#0B0907"></i>#0B0907 фон</span><span class="sw"><i style="background:#FDD506"></i>#FDD506 акцент</span><span class="sw"><i style="background:#F5EFE0"></i>#F5EFE0 текст</span><span class="sw"><i style="background:#A39B8B"></i>#A39B8B приглушений</span><span class="sw"><i style="background:#FF5C6C"></i>#FF5C6C тривога</span></div>
  <p class="note">Бренд Влада — чорний + жовтий. Зеленого немає. Усі п'ять варіантів нижче тримають цю пару, різниця — у характері.</p>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">01 · Три типи слайдів</div><h2>Кожен слайд знає, навіщо він</h2><p>Тип задає, скільки на слайді дизайну. Ритм: вау-слайд кожні 5–10 слайдів, там, де є що показати. Між ними — тиша.</p></div>
  <div class="grid3">
    <div class="tile"><h3><span class="type t-wow">Вау</span></h3><p>Кадр або сцена, яку хочеться сфотографувати. Один оркестрований момент при появі (2–4 с), потім спокій. Портрет, кадр із Soul, стоп-скролл відео, інверсний жовтий слайд.</p><div class="rule">≈ 1 на 5–10 слайдів · лише там, де є образ</div></div>
    <div class="tile"><h3><span class="type t-video">Відео</span></h3><p>Відео головне, дизайн мовчить: чорна рамка, підпис знизу ліворуч, жодних ефектів поверх. Перевірка: чи потрібна ця анімація глядачу? Якщо ні — прибираємо.</p><div class="rule">мінімалізм як у Apple · 0 зайвих рухів</div></div>
    <div class="tile"><h3><span class="type">Контент</span></h3><p>Заголовок як єдина думка, до одного акцентного рядка, іконки лише SVG. Фото Влада з Google-презентації — на весь екран або половину, не «в куточку».</p><div class="rule">один слайд = одна думка · текст читається з WebinarStars</div></div>
  </div>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">02 · Референси</div><h2>У кого підглядаємо і що беремо</h2><p>Не копіюємо стиль — беремо принцип. Посилання клікабельні.</p></div>
  <div class="grid2">
    <div class="tile ref"><h3><a href="https://blog.google/innovation-and-ai/technology/ai/io-2026-keynote-moment-videos/" target="_blank" rel="noopener">Google I/O '26 · Neural Expressive</a></h3><ul><li>Плавні «текучі» анімації, насичений колір, нова типографіка</li><li>Світла/темна тема з градієнтним накладанням, підсвітка окремих слів омбре</li><li>Material 3 Expressive: пружинна фізика руху, 35 форм, морфінг форм</li></ul><div class="take">Беремо: підсвітку ключового слова градієнтом, пружинну появу карток, морфінг форми на відкритті акту (варіант «Папір»).</div></div>
    <div class="tile ref"><h3><a href="https://openai.com/devday/" target="_blank" rel="noopener">OpenAI DevDay '25</a></h3><ul><li>Чорний і білий як основа бренду, багато повітря, великий шрифт</li><li>Арт-дирекція всього: від сцени до моушену на екрані (D&AD Yellow Pencil 2026)</li><li>Демо і продукт у центрі, слайд не сперечається зі спікером</li></ul><div class="take">Беремо: одна думка на екрані, кадр не переказує голос, стриманість руху (варіант «Keynote»).</div></div>
    <div class="tile ref"><h3><a href="https://apple-summary-slides.vercel.app/all" target="_blank" rel="noopener">Apple WWDC '26 · bento-слайди</a></h3><ul><li>Чорний фон, білий великий текст, один продукт на слайд</li><li>Bento-підсумки: сітка з кількох плиток різного розміру</li><li>Рух — лише fade і масштаб, 0.3–0.6 с</li></ul><div class="take">Беремо: bento для стеку цінності й оффера, переходи crossfade, «нічого зайвого» на відео-слайдах.</div></div>
    <div class="tile ref"><h3><a href="https://www.figma.com/blog/the-visual-identity-behind-config-2026/" target="_blank" rel="noopener">Figma Config '26</a></h3><ul><li>Розмиті градієнтні плями, зернисті «крапкові» частинки, скетчеві лінії</li><li>Дизеринг (пуантилізм) на портретах спікерів — цифрове, але «людське»</li><li>Статика і моушен робилися паралельно, анімації навмисно «колажні»</li></ul><div class="take">Беремо: aurora-плями і частинки (уже є), зерно/дизеринг на фото історії, «незакінчену» текстуру замість глянцю.</div></div>
  </div>
  <h3 style="margin-top:28px">Твої референси з Pinterest</h3>
  <div class="grid3" style="margin-top:12px">
    <div class="tile"><h3>Velocity</h3><p>Темно-коричневий чорний, помаранчеве світло з-під карток, світні іконки-кулі, скло. Найближчий до нашої пари чорний + жовтий.</p><div class="rule">→ Glow: світло знизу, підсвітка карток</div></div>
    <div class="tile"><h3>Kontour Studios</h3><p>Вогняний градієнт, гігантське «STUDIOS» позаду силуету, білі й помаранчеві стат-картки, uppercase з лігатурами.</p><div class="rule">→ Гігантський шрифт + стат-картки для цифр</div></div>
    <div class="tile"><h3>Formix</h3><p>Портрет у профіль на помаранчевому диску, акцентні слова в заголовку, нумеровані послуги 01–05, помаранчевий блок-цитата.</p><div class="rule">→ титул на диску, нумерація послуг</div></div>
    <div class="tile"><h3>Zenrixa</h3><p>Світло-сірий мінімалізм, великий гротеск, силует із помаранчевими окулярами, слова-пілюлі «We · Create · → · Future».</p><div class="rule">→ Папір: пілюлі, світла тема для зміни ритму</div></div>
    <div class="tile"><h3>Digital Kensei</h3><p>Чорний / білий / червоний, слово на весь екран, картинки всередині тексту, bento-статистика на чорному.</p><div class="rule">→ Гігантський шрифт, чергування чорних і світлих секцій</div></div>
    <div class="tile"><h3>Фіолетовий web3-колаж</h3><p>3D-кристали, промені, скляні панелі на чорному. Красиво, але це чужий колір і «крипто»-асоціації — беремо лише прийом скла і променя, не палітру.</p><div class="rule">→ скляні картки, промінь світла в Glow</div></div>
  </div>
  <div class="tile" style="margin-top:12px"><h3><a href="https://www.youtube.com/watch?v=wYSncx9zLIU&t=893s" target="_blank" rel="noopener">Google I/O ’26 Keynote · з 14:53</a></h3><p>Те, що тобі зайшло в цьому фрагменті, — принцип, а не палітра: тексти й картки в’їжджають із пружинною фізикою і завмирають, кольорові плями світла морфяться за спікером, кадр міняється тільки коли міняється думка, демо-екрани стоять у рамці пристрою. Це один-в-один наші правила з розділу 06: одна дія на слайд, потім спокій. Беремо пружинну появу карток для Glow і морфінг плям для відкриття актів.</p></div>
  <p class="note" style="margin-top:14px">Ще для перегляду: <a href="https://www.figma.com/community/file/1150817983915754582/all-apple-event-summary-slides-2019-2026" target="_blank" rel="noopener">усі підсумкові слайди Apple 2019–2026 (Figma)</a> · <a href="https://www.youtube.com/watch?v=2ZCc4k_IV5w" target="_blank" rel="noopener">кейноут Config 2026</a> · <a href="https://www.youtube.com/watch?v=hS1YqcewH0c" target="_blank" rel="noopener">кейноут DevDay 2025</a>. Твої референси розібрані вище — вони й задали варіанти 1, 2 і 4.</p>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">03 · П'ять варіантів</div><h2>Один і той самий контент, п'ять характерів</h2><p>Кожен варіант показаний трьома слайдами з перших десяти: титул, цитата «Узнаёте себя?» і три тези. Квадрат — бо в ефірі преза стоїть поряд із відео спікера.</p></div>

  <div class="variant">
    <div class="vhead"><div><div class="num">ВАРІАНТ 1 · за твоїми референсами</div><h3>Glow</h3><p>Velocity, Kontour, Formix одним словом: тепле світло знизу на чорному, скляні картки з підсвіткою, портрет на жовтому диску. Це наш чорно-жовтий світ у найдорожчому виконанні. Емоційна крива живе в яскравості світла.</p></div>
    <dl class="tokens"><span>фон</span><b>#0E0906 + світло знизу</b><span>текст</span><b>#FFFFFF · Unbounded 700</b><span>акцент</span><b>#FDD506 диск, слово, підсвітка</b><span>фото</span><b>кольорове, на диску або в кадрі</b><span>рух</span><b>світло «дихає», картки загоряються по черзі</b><span>іконки</span><b>SVG у світних колах</b></dl></div>
    MOCKS_V1
  </div>

  <div class="variant">
    <div class="vhead"><div><div class="num">ВАРІАНТ 2 · за твоїми референсами</div><h3>Гігантський шрифт</h3><p>Kensei і Kontour: слово на весь екран, портрет ріже текст, чорні й світлі секції чергуються, мета дрібним моно. Найсміливіший і найбільш «журнальний». Ідеально для титулів актів і цифр, гірше для довгих цитат.</p></div>
    <dl class="tokens"><span>фон</span><b>#000000 ⇄ #F4F1EA</b><span>текст</span><b>Unbounded 800, до 34 % висоти кадру</b><span>акцент</span><b>#FDD506 слово-гігант, жовта крапка</b><span>фото</span><b>ч/б, ріже текст</b><span>рух</span><b>слово в’їжджає знизу, фото поверх — і стоп</b><span>іконки</span><b>SVG у bento-картках</b></dl></div>
    MOCKS_V2
  </div>

  <div class="variant">
    <div class="vhead"><div><div class="num">ВАРІАНТ 3 · Apple / OpenAI</div><h3>Keynote Black</h3><p>Чистий чорний, білий Unbounded на весь екран, жовтий лише на одному слові. Фото чорно-біле на весь кадр. Дорого через точність, а не через ефекти. Найлегший у виробництві.</p></div>
    <dl class="tokens"><span>фон</span><b>#000000</b><span>текст</span><b>#FFFFFF · Unbounded 700</b><span>акцент</span><b>одне слово #FDD506</b><span>фото</span><b>ч/б, повний кадр, чорний градієнт</b><span>рух</span><b>fade + масштаб 0.4 с, без частинок</b><span>іконки</span><b>лінійні SVG білі</b></dl></div>
    MOCKS_V3
  </div>

  <div class="variant">
    <div class="vhead"><div><div class="num">ВАРІАНТ 4 · Zenrixa / Google I/O</div><h3>Папір</h3><p>Світлий теплий папір, чорний текст, слова-пілюлі, портрет у чорній картці, жовтий як фарба. Дух Material Expressive: пружини, морфінг форм. Може бути другою темою для контентних блоків і титулів Секретів, щоб зал відчував зміну ритму.</p></div>
    <dl class="tokens"><span>фон</span><b>#F3EFE6</b><span>текст</span><b>#0B0900 · Manrope 700</b><span>акцент</span><b>#FDD506 пілюлі й картки</b><span>фото</span><b>кольорове в чорній картці</b><span>рух</span><b>пружинна поява, морфінг пілюль</b><span>іконки</span><b>SVG чорні на білих пілюлях</b></dl></div>
    MOCKS_V4
  </div>

  <div class="variant">
    <div class="vhead"><div><div class="num">ВАРІАНТ 5 · кіно</div><h3>Film</h3><p>Кадр на весь екран із зерном і темним градієнтом, текст невеликий знизу ліворуч, жовта лінія-маркер. Дизайн зникає, лишається кіно. Ідеально для історії й відео-слайдів, слабше для таблиць і цін.</p></div>
    <dl class="tokens"><span>фон</span><b>фото/відео + градієнт</b><span>текст</span><b>#FFFFFF · Manrope 700</b><span>акцент</span><b>жовта лінія-маркер</b><span>фото</span><b>кіно-грейд, зерно 6 %, повний кадр</b><span>рух</span><b>повільний зум 20 с, crossfade</b><span>іконки</span><b>SVG у списку, без карток</b></dl></div>
    MOCKS_V5
  </div>
  <p class="note" style="margin-top:22px">Моя рекомендація: основа — <b>Glow</b> (це твої референси + наш бренд; поточна Aurora переходить у нього за день), титули актів і цифри — <b>Гігантський шрифт</b>, історія та відео — <b>Film</b>, зміна ритму — <b>Папір</b>. Keynote Black — запасний, якщо захочеться максимально стримано. Blueprint з лендингу свідомо не беремо, щоб преза і сайт не зливалися.</p>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">04 · Іконки</div><h2>Без емодзі. Лінійні SVG, одна товщина</h2><p>Штрих 1.75, скруглені кінці, жовтий або білий залежно від варіанта. Набір розширюється під контент: кожна іконка — одне поняття зі слайда.</p></div>
  <div class="iconrow">
    <div><svg><use href="#i-coin"/></svg>заробіток</div><div><svg><use href="#i-tag"/></svg>ціна</div><div><svg><use href="#i-gear"/></svg>агенти</div><div><svg><use href="#i-cap"/></svg>школа</div><div><svg><use href="#i-book"/></svg>навчання</div><div><svg><use href="#i-folder"/></svg>стаж</div><div><svg><use href="#i-battery"/></svg>дешеві замовлення</div><div><svg><use href="#i-hourglass"/></svg>роки</div>
    <div><svg><use href="#i-bolt"/></svg>включив агента</div><div><svg><use href="#i-phone"/></svg>прибрати телефон</div><div><svg><use href="#i-eye"/></svg>дивитися</div><div><svg><use href="#i-door"/></svg>не турбувати</div><div><svg><use href="#i-plus"/></svg>+ в чат</div><div><svg><use href="#i-play"/></svg>відео</div><div><svg><use href="#i-spark"/></svg>AI</div><div><svg><use href="#i-chat"/></svg>переписка</div>
  </div>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">05 · Фото і персонаж</div><h2>Один герой, один світ</h2></div>
  <div class="grid2">
    <div class="tile"><h3>Влад</h3><dl class="kv"><dt>Образ</dt><dd>Чорний одяг, прямий погляд, без посмішки «на камеру». Один і той самий Soul у всіх генераціях (Higgsfield soul_2).</dd><dt>Титул</dt><dd>Портрет по пояс від Стаса на чорному. До нього — чорно-золотий портрет із лендингу.</dd><dt>Історія</dt><dd>Реальні фото з Google-презентації на весь екран; тепле зерно на підйомі, холодне знебарвлення на дні (робить дека сама за рівнем кривої).</dd><dt>Заборонено</dt><dd>Стокові люди, «неоновий кіборг», емодзі, фото «в куточку».</dd></dl></div>
    <div class="tile"><h3>Агенти</h3><dl class="kv"><dt>Мотив</dt><dd>Золоті wireframe-фігури за роботою — як на портреті з лендингу. Це і є «персонаж» агента: не робот, а світна людина-схема.</dd><dt>Ролі</dt><dd>Охотник · Продавец · Исполнитель — три пози тієї самої фігури, ті самі кольори. Генеруються одним промтом-серією.</dd><dt>Де</dt><dd>Титул (фон), «96 агентів», «штат», Секрет 3, оффер.</dd><dt>Гіфки</dt><dd>Лише на серії «Узнаёте себя?» і мемах — зберігаємо mp4, показуємо в рамці, без зайвих ефектів.</dd></dl></div>
  </div>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">06 · Анімація</div><h2>Правила руху</h2></div>
  <div class="grid3">
    <div class="tile"><h3>Одна дія на слайд</h3><p>Слайд робить один рух при появі й завмирає. Крім вау-слайдів, де рух і є змістом (орбіти, відео, кришки призів).</p></div>
    <div class="tile"><h3>300–700 мс, ease-out</h3><p>Без пружин і відскоків у темній основі. Слова заголовка проявляються з інтервалом 50 мс. Переходи між слайдами — crossfade 450 мс.</p></div>
    <div class="tile"><h3>Відео мовчить</h3><p>На відео-слайдах анімації немає: підпис знизу, чорний градієнт, усе. Звук вмикається окремо (V) лише там, де голос — частина доказу.</p></div>
    <div class="tile"><h3>Перевірка користувачем</h3><p>Кожна анімація відповідає на «навіщо це глядачу?». Немає відповіді — прибираємо. Ефект заради ефекту робить презу «згенерованою».</p></div>
    <div class="tile"><h3>Зміна акту — інверсія</h3><p>Жовтий слайд із чорним текстом як удар: титули Секретів, «вебінару не буде», Велика ідея. Не частіше 1 на 20 слайдів.</p></div>
    <div class="tile"><h3>Аурора дихає повільно</h3><p>Фон рухається 30 с на цикл — око не помічає, але картинка жива. Частинок ≤ 64, яскравість — від рівня кривої.</p></div>
  </div>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">07 · Перші десять слайдів</div><h2>Що є зараз і що пропоную</h2><p>Скрін — поточний стан v6 (квадрат). Тип, візуал, анімація і що потрібно від Влада — по кожному.</p></div>
  <div class="slides">SLIDES_HERE</div>
</section>

<section>
  <div class="sec-head"><div class="eyebrow">08 · Затвердити</div><h2>Рішення для цього кола</h2></div>
  <ul class="check">
    <li>Основний варіант стилю: 1 Glow · 2 Гігантський шрифт · 3 Keynote Black · 4 Папір · 5 Film (або комбінація, як у рекомендації)</li>
    <li>Портрет для титулу: чорно-золотий з лендингу до фото від Стаса — так?</li>
    <li>Серія «Узнаёте себя?»: два з шести з візуалом (гіфка/мем), решта — чистий текст?</li>
    <li>Іконки: лінійний набір вище — ок? Тоді міняю всі емодзі в деці</li>
    <li>Ритм: вау-слайд кожні 5–10, інверсія не частіше 1 на 20</li>
    <li>Pinterest-референси від Мирослава → шостий варіант або правки до обраного</li>
  </ul>
  <p class="note" style="margin-top:16px">Жива дека: yasko-preza-v5.vercel.app · клавіші ? · D — панель режисера · T — повний текст · W — 16:9</p>
</section>

</div>
'''
html=HTML.replace('ICONS_HERE',ICONS).replace('SLIDES_HERE',slide_cards())
html=html.replace('MOCKS_V1',mocks('v1',IM['gold'])).replace('MOCKS_V2',mocks('v2',IM['gold'])).replace('MOCKS_V3',mocks('v3',IM['studio'])).replace('MOCKS_V4',mocks('v4',IM['gold'])).replace('MOCKS_V5',mocks('v5',IM['gold']))
html=html.replace('url(OFFICE)','url('+IM['office']+')')
out=os.path.join(root,'passport.html'); open(out,'w',encoding='utf-8').write(html)
print("passport.html:",len(html)//1024,"KB")
