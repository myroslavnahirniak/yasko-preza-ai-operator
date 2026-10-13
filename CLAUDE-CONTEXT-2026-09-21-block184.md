# AI-Оператор · хендоф 21.09.2026 (блок 184–194) — читати ПЕРШИМ, без інших контекст-файлів

Замовник Мирослав (українською), тексти слайдів російською. Режим роботи в цій сесії — **економний**: правки маленькі, читаємо мінімум, скрини лише для нових layout'ів.

## Як вносити правку (5 команд, нічого більше не читати)
1. Знайти слайд: `python3 -c "import json,re;s=open('js/slides-google180.js',encoding='utf-8').read();i=s.index('window.S=')+9;S,_=json.JSONDecoder().raw_decode(s[i:]);n=NNN;x=S[n-1];print(x['googleObjectId'],re.sub('<[^>]+>','',x['t']),(x.get('foundation') or {}).get('block129',{}).get('layout') or (x.get('foundation') or {}).get('variant'))"` (NNN = номер з URL `?s=NNN`).
2. Текст/HTML слайда: `source/overrides.json` → `__visibleGoogleAudit.slides[<oid>].set.t / set.b` (патч-скрипти-приклади: `source/_patch_184_button.py`, `_patch_188_191.py`; правити через json read→write, не вручну).
3. Стилі: `css/block-154-163.css` (s16-* layouts, у кінці файлу), JS: `js/block-154-163.js`. Після зміни CSS/JS — бампнути `?v=` у `index.html` **і** `google180.html` (зараз `s16-20260921j`; slides-файли `?v=block184-20260921b` — бампати після кожної збірки, інакше кеш).
4. Збірка (≈60 с): `FOUNDATION_SOURCE=google-2026-09-16/foundation-source-v2.json python3 source/_foundation_prepare.py && python3 source/_build_slides.py`.
5. Перевірка: Мирослав дивиться сам у `http://127.0.0.1:8765/google180.html?square&clean&s=NNN` (жорстке оновлення). Скрин робити тільки для нового layout'у: `URL=... W=900 H=900 DELAY=5000 OUT=x.png node shots/_cdp_page.mjs` (кроки — `STEPS` JSON, у JS усередині тільки одинарні лапки).

## Що зроблено 21.09 (слайди → layout)
184 `s16-onebutton` (кнопка + 4 предмети, 6 станів) · 185 `s16-statement` (мікрофон, без анімації) · 186 `s16-mosaic` (3D-мозаїка, крок = картка на весь квадрат, hover-нахил, крок 5 — контейнер по центру) · 187 демо-iframe 1100px→scale (`fitPhone` → `.s16-demo`) · 188 `s16-fan` (клас контейнера `.s16-fanwrap`, бо `.s16-fan` зайнятий) · 189 `s16-kpsets` (2 кроки) · 190 `s16-shelf` (hover) · 191 `s16-cine` (відео IMG_7847, клік = на весь слайд) · 192/194 `ag-phone-video` без URL, заголовок по центру.
Картинки: `assets/gen-184-188/*.webp` (GPT Image 2.5), вирізки макетів `assets/vlad-1409/dizayn/*.webp` (креативи, КП, банери, YouTube, Reels — апскейл 2k). Відео: `assets/video/vlad-1409/img-7847-720.mp4`.
Сторінки варіантів: `design-s18N-options.html` на каркасі `design-options-base.js/.css` — робити тільки якщо Мирослав просить «три варіанти».

## Правила смаку (коротко)
Повний текст джерела завжди · відступи 7cqw · один шрифт у заголовку, акцент жовтим `<em>` · нічого не обрізати · фон без Ken Burns, якщо не просили · контейнер відео = пропорція відео, без чорних смуг.

## Обережно
У цій же папці паралельно працює інша сесія (продаюча частина, слайди 303–409): перед записом html/css/js перечитувати файл, overrides патчити read→write одразу. Не деплоїти. Не чіпати Google-презентацію.
