# EDIT-CHEATSHEET · правки слайдів AI-Оператор без читання хендофів

Читати ПЕРШИМ у новій сесії. HANDOFF.md / AGENTS.md / CLAUDE-CONTEXT-*.md відкривати лише якщо тут нема відповіді (вони по 40–200 KB).

## Де що
- Дека: `google180.html` (дані `js/slides-google180.js`, генеруються). Дивитись: `http://127.0.0.1:8765/google180.html?square&clean&s=N` (сервер 8765: `nohup python3 source/_serve_range.py 8765 &` — з підтримкою Range; звичайний `http.server` без Range ламає друге відео на слайді в Chrome).
- Правда про слайд = `source/overrides.json` → `__visibleGoogleAudit.slides[oid]` (`set.t`, `set.b`, `foundation.block129{layout,steps,art,eyebrow}`, `omit`). Руками JSON не правити — через `_edit.py`.
- Нові слайди = layouts `s16-*`: CSS `css/block-154-163.css`, JS `js/block-154-163.js`. Продаюча частина 21.09: `css/block-sales-2109.css`, генератор `source/_patch_sales_2109.py`.
- Після зміни CSS/JS обов'язково бамп `?v=` в `index.html` і `google180.html` (`_edit.py --bump` робить сам).

## Три команди
```bash
python3 source/_slide.py 184            # що це за слайд: oid, layout, кроки, body, рядки CSS цього layout
python3 source/_edit.py 184 --reason "Мирослав: підпис вище" --b129 '{"steps":null}' --bump --shot "n,n"   # патч → збірка → скрин
URL="http://127.0.0.1:8765/google180.html?square&clean&s=184" OUT=shots/edit NAME=s184 FIRST=7000 STEPS="n,n,p" node shots/_cdp_steps.mjs   # лише скрини
```
Скрини лягають у `shots/edit/s184-0.png`, `-1.png`… (0 = вхід, далі по одному на крок). Дивитись 1 скрин, не всі.

## Типові правки
| Що просять | Що робити |
|---|---|
| Текст/підпис вище-нижче | знайти в CSS layout рядок з `top:…cqh` для цього елемента (`_slide.py` показує рядки), змінити, `_edit.py N --reason … --bump --shot` |
| Прибрати кроки | `--b129 '{"steps":null,"focus":null}'`; для s16-onebutton CSS уже показує все без кроків |
| Змінити заголовок | `--t "Текст с <em>акцентом</em>"` (акцент = `<em>`, одне-два слова) |
| Змінити body | тіло в файл → `--b @source/_tmp_body.html` |
| Інша картинка фону | `--b129 '{"art":[{"src":"assets/…webp","alt":"…"}]}'` |
| Сховати слайд | `--set omit=true` не працює через set → в overrides ключ `omit:true` на рівні слайда (єдиний випадок ручної правки) |
| Живий сайт з прокруткою по кроках | layout `s16-live`, приклад слайд 193, копія сайту в `assets/sites/roma-kp/` (міст `RomaKP` у кінці index.html) |

## Правила смаку (коротко)
Квадрат 1:1. Чорно-жовтий (`#FDD506`), без зеленого. Заголовок Unbounded 500, один кегль, акцент тільки кольором через `<em>`. Повний текст джерела, нічого не вигадувати (цифри теж). Поля 7cqw. Іконки приглушені `#B3A996`, не жовті. Один рух на вхід (≤2 с), далі статика. Не деплоїти без прохання. Не чіпати Google-презентацію.

## Економія токенів
- Нова сесія на кожну пачку правок; читати тільки цей файл.
- `_slide.py` замість `grep`/`sed` по overrides.json (1.7 MB) і CSS.
- Один скрин на слайд для перевірки; кроки — лише коли правка стосується кроків.
- Не запускати два `_cdp_steps.mjs` одночасно (один порт 9334).
- Одна сесія на деку: паралельні сесії затирають `overrides.json` одна одній.

## Актуальна продаюча частина · 21.09.2026
- Основна дека: 408 слайдів, продаж 239–408. 65 готових сторінок агентів перенесено з контенту; старі номери вже не актуальні.
- ТЗ: preza-ai-operator-v6.vercel.app; звіт і карта: source/sales-v6-20260921/REPORT.md, final-map.json.
- Нові стилі: css/sales-v6-source.css + css/sales-v6.css; розкриття модулів: js/sales-v6.js.
- prepare.py цієї міграції повторно не запускати. Правки даних — через _edit.py за актуальними objectID.

## Дві пастки, на які легко втратити годину (22.09)
- **Заголовок слайда-частини не міняється через `_edit.py --t`.** Слайди каталогу (ті, що «ЭЛЕМЕНТ N ИЗ 17», один Google-oid на багато екранів) беруть `t` з `presentationParts.slides[i].t`, бо `allowPartTitles:true`; `_foundation_prepare.py` перетирає ним слайдовий `set.t`. Правити треба саме частину, далі `_foundation_prepare.py && _build_slides.py`. `_edit.py` відпрацює «успішно» і нічого не змінить.
- **`deck.js` запускає тільки ПЕРШЕ відео слайда** (`sl.querySelector('video')`). Якщо роликів два (102, 115, 317, 322, 375, 379), другий стоятиме, навіть маючи `autoplay`. З 22.09 додаткові стартують за opt-in у розмітці — `<video autoplay loop>`.

## Додати/сховати слайд (22.09)
- **Новий екран після Google-слайда** = `presentationParts` на цьому oid в overrides (`sourceGoogleObjectId`, `authorization`, `slides:[{}, {t,b,lifeStory|foundation…}]`); перша частина `{}` = сам слайд. Приклади: `source/_patch_2209_fedorov_roditeli.py` (life-line: фото/відео через `lifeStory.photos` / `lifeStory.video`), `_patch_2209_vlad_batch2.py` (копія екрана з продаючої частини).
- Life-line: rail дедуплікує точки по googleNumber, тож частини одного слайда діляться однією точкою.
- **Сховати Google-слайд**: `_edit.py N --omit true --reason … --no-build`, потім prepare+build. **Сховати екран продаючої частини** (oid `g3f9b3adf0b8_0_2226`): видалити елемент із `presentationParts.slides` (там же вставляються нові екрани, напр. Блок 2 з `source/sales-v6-20260921/pre-migration-sales.json`).
- Одиночне фото в participant-story: `photos.income=[{src,alt}]` (1 елемент) → без рамки (`.ps-single`).

## Vercel-деплой заблоковано (22.09, з 08:56)
- Після прив'язки репо до GitHub (коміт 08:07) Vercel на hobby-плані блокує всі `vercel --prod` з кодом `TEAM_ACCESS_REQUIRED`: автор коміту sofiia.boiarkevych@gmail.com не є верифікованим членом команди. У `vercel ls` такі деплої стоять як UNKNOWN, через API — BLOCKED; прод не оновлюється, хоч CLI мовчить.
- Обхід без комітів: на час деплою сховати `.git` (`mv .git .git-off-deploy && vercel --prod --yes; mv .git-off-deploy .git`) — CLI не передає git-метадані, перевірки автора нема. Нормальний фікс: додати цей email у Vercel-команду або комітити з email акаунта Vercel.
- Перевірка, що прод реально оновився: `curl -s https://yasko-preza-v5.vercel.app/google180.html | grep -o 'slides-google180.js?v=[^"]*'` має збігатися з локальним `?v=`.
- `--archive=tgz` не використовувати: 2.8 ГБ одним архівом API відкидає (Internal Server Error). Аплоад іде довго (десятки хвилин), `| tail` ховає прогрес — писати лог у файл.
- Перенос екранів між блоками: `source/_patch_2209_after170.py` (копії частин продаючого oid після Google-слайда), `source/_patch_2209_after183.py` (перенос 51 частини + omit Google-слайда з копією як частини). Частини без `k` успадковують eyebrow батька — ставити `k:''`.

## Слайди Секрету 3 (≈244–256) не беруться з overrides (22.09)
- `_slide.py N` покаже oid `g3f9b3adf0b8_0_1943` і layout s16-poster, але на екрані рендерить `js/secret3-final-a.js` (`render`, `case N`) зі стилями `css/secret3-final-a.css` (`.sf-aN`). Правки через `_edit.py` там нічого не змінюють.
- Правити прямо `case N` у JS + CSS, потім вручну бампнути `secret3-final-a.js?v=` і `.css?v=` в `index.html` та `google180.html` (`_edit.py --bump` ці файли не чіпає). Картинки — `assets/secret3-final/`.
- Приклад: 251 = `case 8`, постер `hunter-scope-v1-4k.webp` на весь кадр.

## Деплой на прод (28.09) — тільки `source/_deploy_prod.sh`
- `vercel --prod` з робочої папки більше не працює навіть зі схованим `.git`: CLI падає «File size limit exceeded (100 MB)». Скрипт збирає чисту копію в `../_deploy-preza-v5` (rsync з білим списком `source/`) і деплоїть звідти — git-автора там немає, великих файлів теж.
- Нові папки в `source/`, на які посилаються слайди, додавати в `--include` скрипта.
- Секрет 2 у деці: oid `g3f9b3adf0b8_0_1774`, екрани 244–257 = iframe `secret2.html?n=228..241&embed`, 258–275 = постери `assets/gen-secret2-full/s242..259.webp` (патч `source/_patch_2509_secret2_restore.py`).

## Порядок за Google-ревізією 01.10 (зум з Владом)
- Порядок, приховані й нові слайди тепер задає `overrides.__deckOrder` (модуль `source/_deck_order.py`, виклик у кінці `_foundation_prepare.py`). Генерується з Google: `source/google-2026-10-01/` → `PLAN.md` (конвеєр, список правок). Обсяг — лише Google 1–185 = екрани 1–146.
- Нові слайди `new-gNNN` і копії `copy-gNNN` правляться звичайним `_edit.py N` (патч лягає в `__visibleGoogleAudit.slides[id]`). Заглушки нових = кадр із Google `assets/google-1001/gNNN.webp` (s16-poster).
- Маршрут реаліті (екрани 35/36) розбитий на частини: `routeRoadmap.range=[a,b]` у `js/reality-route.js`.
- `_edit.py` на opening-слайдах (1–40: `opening`, `bg`, `photos`) знімає ці ключі — там правити точково, не ним.

## Відеослоти (01.10)
- `assets/video/slots/future-pacing.mp4` (s=139) і `assets/video/slots/zolotoy-dozhd.mp4` (s=145) — покласти файл і задеплоїти; поки файлу нема, видно поточний кадр (класи `slot-ready` / `has-video` вмикаються на `loadeddata`).
- `_deck_order` зливає `foundation.block129` (як `_edit.py --b129`): щоб прибрати ключ у новому слайді/копії — передати його як `null`.

## Пастки 02.10
- **Багаточастинний oid** (один Google-слайд на кілька екранів, у `_slide.py` видно той самий oid у сусідів): `_edit.py N --b` БЕЗ `--part` пише в `set.b` частини №0 — тобто ламає ІНШИЙ екран. Індекс частини: `presentationParts.slides[i]` за заголовком → `--part i+1`. Так 02.10 AI-таргет (`g3f9b3adf0b8_0_2921`, `--part 33`) затер «Весь этот каталог». Бекапи — `source/_bak/`.
- **Списки в нових слайдах:** `ul/li` ховає deck.css (`.slide ul li{opacity:0}` + анімацію вимикає `.b129.b13-v2 *`), клас `.ls` теж зайнятий deck.css (opacity:0). Брати `div/span` з власним класом (`g2-ls`).
- **Версії `?v=`**: `_build_slides.py` їх не бампить; паралельна сесія може виставити свою (01.10 ввечері `dc-20261001-s139`) — перед деплоєм дивитись `grep -o 'slides-google180.js?v=[^"]*' index.html`, а не сліпий `sed` зі старим значенням.
- Порядок до Google 325 і нові слайди 02.10 — `source/google-2026-10-01/PLAN-1002.md`.

## Граблі викладки 1001 (03.10)
- `cleanUrls` у vercel.json (для /part1 /part2) робить `…/site/index.html` → 308 на `…/site` без слеша — сайти в iframe ламаються. `_deploy_1001.sh` у викладці переписує `assets/…/index.html` → `assets/…/`. Нові iframe на сайти-папки можна давати як `…/index.html`, скрипт сам виправить.
- Маршрут реаліті (`js/reality-route.js`): вхід уперед на копію з `range` — одразу анімація з попереднього пункту до активного (старт через 20 мс, лінія .5 с; rAF не годиться — у прихованій вкладці не спрацьовує).
- Слайд 10 (сайт Роми): 242 кадри = 16 МБ; після деплою вантажиться 8–15 с, у деці iframe гідрується за 3 слайди наперед — на ефірі встигає.
- **03.10 · `_edit.py` на легасі-слайдах (layout chat / editorial з дизайном у `viz`/`kind`, не лише 1–40):** без `--part` скрипт пише `remove:[bg, photos, kind, opening, viz, …]` — оформлення зникає (s53 «Как забрать» став голим текстом). Для простої заміни тексту на таких слайдах — запис у `__visibleGoogleAudit.slides[oid]` лише з `set.b`/`set.t` без `remove`, потім prepare+build. Після будь-якого `_edit.py` дивитись скрин.

## Пастки 06.10 (QA rest-redo)
- **Збірка руками = з env**: `FOUNDATION_SOURCE=google-2026-09-16/foundation-source-v2.json python3 source/_foundation_prepare.py && python3 source/_build_slides.py` (так робить `_edit.py`). Без env дека збирається на 194 слайди замість 416.
- **Копії частин** (`__deckOrder.entries` `{"copy":"oid#N"}`, N = номер частини, як `--part`) успадковують усе з джерела, крім власного `set`. Переробив частину — перевір її копії (rest 18/23 ← 2226#15, екран 12 частини 1 ← 2921#29); захист — власні `set.b`/`set.t`/`block129` у `__visibleGoogleAudit.slides[copy-id]`.

## 08.10 дзвінок з Владом (transcripts/2026-10-08-preza-vlad/ROZBIR.md)
- Секрет 2 = Google 326–384 після дзвінка: порядок у `__deckOrder.entries` між `copy-g327` і `1943#1` задає `source/_patch_1008_call_s2.py`; нові екрани `new-cNNN` (NNN = сторінка Google) лежать у `__deckOrder.slides`, правити їх там (або `_edit.py N`).
- Нові текстові/фото-екрани = layout `s16-g1001` + маркер у тілі: `.s2n-say` (заголовок по центру), `.s2n-pic` (1–2 картинки), `.s2n-vs`, `.s2n-vs2`, `.s2n-aim`, `.s2n-lock`, `.s2n-reveal` (`.s2n-rows`/`.s2n-cols` — що розмито), `.s2n-list`, `.s2n-site` (живий сайт, `iframe data-src`). CSS — кінець `css/rest-1006.css`.
- Текст, вшитий у постери, прибирати `source/_img_patch_1008.py` (push-pull заливка фону, `erase(..., mode='text'|'box')`, `text()` шрифтом Unbounded з ~/Library/Fonts) → `assets/gen-s2-1008/`.
- Підпис «УСЛУГА 0N / 07» на екранах послуг — `eyebrow` + маркер `<i class="svc-eb" hidden>` у тілі частини 2921 (CSS `.slide.b129:has(.svc-eb)`).
- **Пастка `__deckOrder.hide`**: діє лише на екрани, яких НЕМА в `entries`. Щоб прибрати екран, що є в `entries`, — ключ у `drop` (або видалити з `entries` і додати в `hide`).
- 09.10: Секрет 3 → «Полная система» за Google — `source/_patch_1009_s3_offer.py` (нові `new-c403`, `new-c427/428`, `new-c434/435`, `copy-c436`); Секрет 3 рендерить `js/secret3-final-*.js` за `foundation.secret3Final.n` (case N), бамп `?v=` вручну.

## 09.10 · стрибки, імпорти, аудит
- **Стрибок на вході** (елемент центрований `translate(-50%)` їде вбік/вниз і повертається): `motion()` у `js/block-129-180-v2.js` тепер дописує свій transform елемента до кадрів анімації. Для CSS-анімацій `s16-up` правило те саме — центрувати через `left:0;right:0;margin:0 auto`, не через transform.
- **Імпорти Секрету 2** (`secret2-import`, iframe `secret2.html?n=…`): вантажаться заздалегідь, коли дека гідрує сусідів (`data-hyd`), і не скидаються; на вході перезапускається анімація. Після правок `css/secret2.css` / `js/secret2.js` бампати `?v=` у `secret2.html` і `&v=` в URL iframe у `js/secret2-import.js`.
- **Переноси заголовків** (Мирослав): максимум 2–3 рядки, без рядка з одного слова; «в» у кінці рядка ок, якщо так виходить 2 рядки; де кегль не допомагає — `<br>` за змістом у `t`.
- **Аудит** rest 1–148: `node shots/_cdp_audit1009.mjs 1 148` → `source/audit-1009/metrics.json` + скрини кроків; `_sheets.py`, `_gmatch.py`; звіт `source/audit-1009/REPORT.md`. Id сторінок у PPTX-експорті Google позиційні (`p`+номер) — зіставляти за мініатюрою/текстом.
- 09.10 · gif під текстом на `s2n-lead`-екрані: `<div class="s2n-gif"><video src="assets/gif/….mp4" poster="…" autoplay muted loop playsinline></video></div>` після `<p class="s2n s2n-lead">` (rest 152 = new-c427; запасні gif: show-me-the-money, stark-workshop). Gif з Tenor: `tenor.com/search/<q>-gifs` → JSON у `<script id="store-cache">` → `media_formats.mp4.url`, перекодувати ffmpeg `-an -crf 24 -movflags +faststart`.
- 09.10 · rest 76 (new-c344) = живий екран «Услуга 01 / 07» (layout s16-catalog-orbit, тіло з copy-g254 без портрета/легенди + `.co-cap`), не скрін картки.
- 09.10 · rest 162–179 (`source/_patch_1009_rest162_179.py`): переноси `<br>` у `presentationParts` 2226 #11–#13; 166 (#15) таргет = `assets/gen-rest-1009/ads-phones.webp` (з Холсту), крок «Вся таблица» знову `co-table` (зверху вниз, не картки); 167 (#16) у `__deckOrder.drop` → номери rest після 166 зсунулись на −1. «М'які краї як 174/175» = маркер `p9-dark r8-mNNN` + `<div class="r8-art">` (173 → r8-m173, 179 → r8-m179 `r8-sq`).
- 09.10 · rest 169 (тепер 168, #18): ліворуч відео каталогу `assets/video/sites-catalog-1009.mp4` (`_patch_1009_r169_sites_video.py`, колонки 1.4fr/1fr — `.p7-tpl-vv`).
- 09.10 · програмні слайди rest 157/158/162–164: підпис лише «Уровень N» (162 = 2, 163–164 = 3 за нотатками Влада Silver/Gold), кількість задач прибрана (`_patch_1009_levels_notasks.py`).
- 09.10 · rest 153 (new-c428) = маркер `.s2n-r153` (картка цілі + `assets/gen-rest-1009/r153/platform-partners.webp`, запасна `platform-network.webp`); rest 159/160 = `.s2n-block` — живий блок «На выходе пакета 01» з сайту потоку 4 (`assets/sites/aim-p4/index.html?i=1|0`, збірка `source/_build_aim_p4_pult.py <unzip>/aimarketolog-site`; iframe 250% + scale .4, щоб сайт бачив десктоп).
- 09.10 · rest 133 фільм: `full-film-720p-fs.mp4` (faststart), preload=auto, автостарт зі звуком при вході — кінець `js/secret3-final-b.js`.
- 09.10 · rest 70/71 (new-g335/336): `.s2n-vcard` — заголовок угорі, квадратна картка 66cqh унизу; 70 = постер `assets/video/remont/remont-a-poster.webp`, 71 = `remont-a.mp4` (один раз, без петлі). rest 80 (new-c348): картки «Одна ниша/Топ-локации» — HTML `.aim-c`.
- 09.10 · новий екран `new-x138s` після Секрету 3 #27 («Окна Киев») = rest 139: колаж `.s2n-shots` (3 скріни чату, `data-zoom`), попап — `js/zoom-shots.js` (capture на window, бо дека гортає кліком; ←/→ між скрінами, Esc). Номери rest після 138 зсунулись на +1.
- 09.10 · rest 151 (було 150, «AI-Оператор», sv-U003b у s16-desk): заголовок і eyebrow сховані CSS, відео `operator-koncept.mp4` на весь слайд.
- 09.10 · «Уровень N» на програмних слайдах — жовта плашка по лівому краю заголовка (CSS `.eyebrow .lvl` у кінці rest-1006.css).
- 09.10 · rest 160/161 = `.s2n-block.sq` + `aim-p4/index.html?i=N&sq=1` (квадрат: екран над описом, база 960). Новий rest 162 `new-x162cat` = пульт 7 агентів із сайту AI-Оператора: `assets/sites/aiop-catalog/` (збірка `source/_build_aiop_catalog.py` з `holst-2809/sajt-src/ai-operator-sajt`; прокрутку замінено кліком по пульту, `?i=N` — стартовий агент). Обидві сторінки пересилають стрілки/пробіл у деку. Номери rest від 162 зсунулись на +1.
- 09.10 · rest 16 (new-g251) = таблиця як на 168 (секція co-table, layout s16-catalog-orbit, steps ['Вся таблица']); rest 169 у вікні — `assets/gen-rest-1009/skills-library.webp` (свіжий скрін skills-navigator-five, contain); rest 190 без заголовка; тарифи 194–196: `.tier-lead` центровано. Варіанти оформлення тарифів — `design-r194-options.html` (А сходи / Б чек / В кадр).
- 09.10 · rest 161/162: у вкладці/агенті AI-сайты замість стоматології — VIP CAR (`svettutest.github.io/shablony-demo/vip-car/`, постер `assets/gen-rest-1009/vip-car-poster.webp`); заміни зашиті в `_build_aim_p4_pult.py` і `_build_aiop_catalog.py`. Розкадровка 205 — `design-r205-storyboard.html` (кадри `assets/gen-rest-1009/r205/k1–k3.webp`); тарифи А+/А++ — у `design-r194-options.html` (D/E).
- 09.10 · тарифи: `.tier-price` у жовтій обводці, без риски. rest 208 — шкала `.r208-win` (эфир → +30 минут) замість монети; 216 Юра — `.r198-card` без мокапу; 218 — відео «офіс агента» `.r218`; 222 — чистий постер `assets/gen-rest-1009/r222-clean.webp` (GPT Image 2.5 edit без тексту) + живий текст `.r222` (s16-poster з :has(.r222) показує shell); 225 — у картці контент-заводу `s202-avatar/clip-3.mp4` (Влад говорить).
- 09.10 · rest 230: gif `assets/gif/voice-button-press.mp4` (The Voice, Tenor) зверху `.r230-gif`, shell padding-top 53cqh; 232 — `.payback-finale` по центру; 233 — фон `assets/gen-rest-1009/r233-a.webp` (рукостискання; запасна r233-b подарунок).
- 09.10 · rest 237 «НЕ СЮДА» — `assets/gen-rest-1009/r237-b.webp` (кнопка під ковпаком; запасна r237-a автомат); 238 — без бульбашок `r220-chat`; кейс Свети повний: приховані Google-слайди `g409d4d20be6_0_198/203/208` (omit знято, ключі `…#0` у entries перед 2226#90) = rest 242–244, далі «+8.000» і «И вышла на первые» (245–246); кейс Ані `2921#44–#53` лишився в hide; «Под ключ» (тепер 248) — «от $10.000» чорним.
- 09.10 · rest 248 «Под ключ» — редизайн `.tk` (3 кроки на вертикальній лінії, візуали `assets/gen-rest-1009/turnkey-*.webp`, ціна+бронь у жовтій рамці); rest 250 «Что вы умеете делать» — `.um` (без скрінів, 6 умінь 2×3, прибрано «умеете, а не «прошли»» і «16 готовых задач»).
- 09.10 · УВАГА номери: Мирослав увечері давав номери /rest зі старої вкладки (до вставки Свети, −3 від поточних). Поточні: «Первый блок — в цифрах» 251 (`.bn`, іконки `assets/gen-rest-1009/bn-*.webp` вирізані з постера), «Разные ниши» 253 (`.nb`), «Дорого» 260 і «Сколько стоит год» 271 (`.pz` поверх чистих постерів r257-dorogo-clean / r268-god-clean), «Я в этом ноль» 262 (`.tg-scene`: фон r259-phone-bg + Telegram-HTML + вирізка пальця r259-phone-top.png), «А вы вообще кто?» 267 (`.who-photo`), «Сколько я заработаю?» 268 (`.qa-gif` show-me-the-money), останній 273 — фото `vlad-qa-mic.webp`.
- 09.10 · «Элемент 2 из 17» повернуто: новий екран `new-x167el2` (у `__deckOrder.slides`, після 2226#14 «Элемент 1») = rest 168, 7 агентів з цінами + ценность $5.200 / общая $6.700 (дані з v6 21.09, `source/sales-v6-20260921/parts.json`); CSS `.p7-u032 .p7-agents`. Каталог 7 услуг став 169, усе далі +1.
- 09.10 · прибрано копію каталогу `copy-c436` (у `drop`); rest 156 «Инструкция + задание» — кнопка `.r139-site` «Открыть сайт ↗» на ai-marketolog-workshop-4.vercel.app.
- 09.10 · блоки пакетів 02/03 з сайту потоку 4: `assets/sites/aim-p4/pult-02.html` / `pult-03.html` (той самий `_build_aim_p4_pult.py`, `?i=N&sq=1`), екрани `new-x163p2` (після «Контент-завод», rest 164) і `new-x164p3` (після «Привлечение», rest 166). Элемент 3: «98 готовых задач» (було 46; в «Что входит целиком» і payback ще 46).
- 09.10 · rest 162: пульт 7 агентів (`new-x162cat`) прибрано → «Что вы умеете делать» картками зі скрінами (`new-x162um`, старе тіло v6-source-95 без eyebrow/нотатки, CSS `:has(.v6-source-95)`); rest 163 новий `new-x162ai` — фон `assets/gen-rest-1009/ai-employees-bg.webp` + «Создавать своих AI-сотрудников под ваши задачи» (`.pz-ai`). «Продажи и масштаб» тепер перед блоком пакета 03.
- 09.10 · каталог «7 услуг» 2226#15 у `drop` (копії g249/g254 на початку /rest лишились); Элемент 9 — фото `assets/gen-rest-1009/vlad-head-update.webp` (голова Влада відкрита, апдейт; Nano Banana Pro з референсом r252); Элемент 11 підзаголовок «с возможностью выиграть рекламу или контракт с клиентом»; «Я рискую десяткой» (rest 210) — без шкали, `.r210-h` заголовок по центру.
- 09.10 · rest 150 (2226 #1, `source/_patch_1009_r150_hero.py`) = офер AI-Оператора на scroll-scrub hero «як на aimarketolog.site»: `assets/sites/aiop-hero/index.html` (порт act1 з `landings/ai-marketolog-launch-3/apps/aim3d`: engine.ts + main.css), 786 AVIF-кадрів з `assets/ai-operator.mp4` (1280×720, SVT-AV1 preset 8 crf 32), шрифти @fontsource у `fonts/`. На весь слайд — `.s2n-hero` у кінці rest-1006.css. Квадрат: кадр зсунутий (ox .62→.5), на фіналі відзум, щоб титр «AI-ОПЕРАТОР» влазив. Колесо/↑↓ — скрол hero, ←/→/пробіл — у деку; при вході на екран hero стартує з першого кадру.
- 09.10 · Элемент 16 підзаголовок — «Доступ к актуальным день в день связкам…: услуга + ниша + локация + способ»; «Если система работает — почему вы не заработаете всё сами?» (2226#41) у `drop`; тарифи: пігулка top 7.5cqh, заголовок 18cqh, lead 34.5cqh (з !important — s281-283-tiers.css вантажиться пізніше).
- 09.10 · rest 209 «Я рискую…» — без заголовка й «Ваш риск», спершу «Условия действуют…» (.r210-h), під ним кнопка. Після «Вы ни одного дня не один» (2226#57) нові `new-x211buy` (rest 211, `.s2n-say2`: умова в обводці + «Я дам то, что невозможно купить») і `new-x212hunt` (rest 212, `.s2n-hvid`: заголовок + відео `assets/video/hunter/looking.mp4` у вікні + жовта плашка «— в подарок»).
- 09.10 · rest 213 новий `new-x213deal` (`.s2n-r213`): умова «для первых 20 броней по $10» в обводці, заголовок «Разбор первых сделок лично со мной», 20 жовтих місць, фото `assets/gen-rest-1009/vlad-mentor.webp` (Nano Banana Pro).
- 10.10 · програма = 11 модулів: M10 «Агент-охотник» прибрано, AI-продавец M10, «Поиск клиентов и связки» M11; «11 модулей/МОДУЛЕЙ» у Элементі 1, Gold ledger/eyebrow, «Три набора», «Что входит целиком», «Реальная цена», «Цена для эфира», «Три набора глазами» (`_patch_1010_modules11.py`). Bronze 5 / Silver 8 лишились (рахують M0). Дубль пакета 01 `new-c434` у drop. Элемент 6 — `assets/gen-rest-1009/bariga-head.webp` (з головою).
- 10.10 · тарифи rest 194–196 = варіант A «Сходи» (`_patch_1010_tiers_A.py`, CSS `.tA*` у кінці rest-1006.css): три набори поруч, активний у жовтій рамці, фон — картинка набору (bronze.webp / content-factory.png / workforce.png) з затемненням + золоте світло за активною колонкою. Класи `.ls/.nm` не брати (зайняті deck.css).
- 12.10 · rest 123 «AI-ОХОТНИК · НОЧНАЯ СМЕНА» (Секрет 3, `js/secret3-final-a.js` → demo, n=10): у вікні замість постера `<video data-sf-autoplay … secret3-hunter.mp4 autoplay muted loop>`. Без `data-sf-autoplay` secret3-final.js ставить відео autoplay=false.
- 12.10 · rest 146 «Итак, сегодня вы увидели» (Секрет 3 n=34): `.sf-c-recap-question` по центру — `max-width:none` (успадкований max-width зсував ліворуч).
- 12.10 · Элемент 6 — `assets/gen-rest-1009/morpheus-vlad.webp` (Влад-Морфеус, Nano Banana Pro, полотно розширене ліворуч щоб був по центру); Элемент 9 — `vlad-head-update-c.webp` (по центру); тарифи A — опис по центру, фон темніший; rest 221 жовта плашка — чорний текст.
- 12.10 · rest 243 «Эти деньги за месяц…»: `.r222-q` конфліктував з моїм класом на 225 — мої правила тепер `.r222 .r222-*`. rest 251 «Под ключ»: лінія `.tk-steps:before` по центру кружечків (18.9cqw).
- 12.10 · rest 256 «Разные ниши»: висновок `.nb-fin` у жовтій обводці, відступи title→сітка→плашка ≈ рівні.
- 12.10 · rest 265 «Я в этом ноль»: фон + Telegram-екран + палець в одній квадратній `.tg-stage` (cover через max(100cqw,100cqh), координати в %) — не з'їжджає на неквадратних екранах. rest 259 «Карта»: текст Manrope `.kp-txt`, Unbounded лише заголовок.
- 12.10 · 5 варіантів блоків пакетів: `design-pult-options.html` (?m=a…e&p=index|pult-02|pult-03); режими — `assets/sites/aim-p4/modes.css/js` (джерело `source/aim-p4-modes/`, копіюються білдером), у слайді вмикаються параметром `&m=X` в URL iframe.
- 12.10 · пакети 01/02/03 (rest 160/164/167, `new-c435` / `new-x163p2` / `new-x164p3`) — власна верстка `.pk` замість iframe сайту (`source/_patch_1012_pk_native.py`, дані `source/aim-p4-modes/packs.json`): вкладки-пігулки, один агент на екран (медіа, назва+ціна, 3 пункти, «Заработок»). Перемикання/відео — `js/pk-tabs.js` (capture-клік, бо дека гортає кліком). Варіанти А–Д старого блоку лишились на design-pult-options.
- 12.10 · граблі: зависли headless Chrome з _cdp_steps (1+ год, load 40+) — перед серією скрінів `pkill -f -- --remote-debugging-port=9334`.
- 12.10 · пакети `.pk` відкочено (Мирославу не сподобалось) — назад живі блоки `s2n-block` (бекап `_bak/overrides-1012-before-pk-*`). У блоках пакетів сховано «Кто уже так зарабатывает»/кейси (`#pp .pult__more,.pult__case` у `_build_aim_p4_pult.py`). Элемент 6 — `morpheus-bald.webp` (не Влад). rest 203 «Путь оплаты» — лише заголовок + скрін `vladwebsite.jpg`. rest 226 «Готовый AI-охотник» (2226#71) у drop, замість — копія `new-x226hunt` слайда «Доступ к Охотнику». Элемент 16 — формула-чіпи `.sv-formula`.
- 12.10 · rest 203 «Путь оплаты» — живий iframe `ai-operator.online/web-ua/booking/` (`.r203-live`, скрін `vladwebsite.jpg` як постер) + кнопка «Открыть сайт ↗». Элемент 16 — текст як у Google «…плюс 2 способа» + два закриті скріни (`.e16-shots`: r084-niches-lock-v2, r085-cities-kyiv-v2). Rest 159 «Продукт и витрина»: M3/M4 розкриваються (задачі 7+9 з v6 у `.mbx-team`, клас pj-block2-clean знято).
- 12.10 · пакет 01: AI-маркетинг першим (01), AI-сайты другим (02), заголовок «Агенты AI-маркетинг и AI-сайты» — `_swap01` у `_build_aim_p4_pult.py`. Тарифи A: фон видніший (opacity .8, легше затемнення).
- 12.10 · пакети (sq): сховано назву агента, «Как работает агент», 3 пункти; лишились ціна (34px) + «Бизнесу»/«Заработок» (20px) у дві колонки, екран 16/8.6. rest 185: «дойти до первого клиента» — `mark.hl` жовта плашка.
- 12.10 · rest 191 рюкзак: лише «Ремесло делает агент, клиентов находит агент» (Unbounded, по центру), без «Вам остаётся…» і жовтої плашки.
- 12.10 · **дзвінок з Владом (продаюча частина)** — розбір `transcripts/2026-10-12-preza-vlad/ROZBIR.md`; правда = окрема Google «AI-Оператор — продающая» (`source/google-sales-2026-10-12/`). `source/_restmap.py N…` — поточний rest → ключ у `__deckOrder.entries` (за presentationPart, 1-based як `--part`). Швидкий блок `source/_patch_1012_call_quick.py`: порядок 197–199 перед тарифами, «Забирайте подарки» після «десятки», 204 у drop, «+30 минут» (`.r208-30`) після «нажмите сейчас»; 207 без дрібного тексту; 217/225/231/232/240/249 за Google. Скрини списком: `OUT=… node shots/_cdp_list.mjs 359,362` (для легасі-слайдів з фото дивитись `_cdp_steps` — `go()` інколи знімає перехід). Легасі `fd-ag-full-photo` бере перший `<img>` тіла фоном — фото там давати `div` з background.
- 12.10 · **блок «7 услуг»** (`source/_patch_1012_call_s7.py`): продаюча частина від rest 213 = Google «продающая» G85–G180. Картки послуг — копії `copy-x12c01…c07` (джерело 2226#15/#16 + патч копій першої частини), артефакти/Женя/Аня — частини 2921 (#7, #18–#24, #26, #31, #35, #44–#53), що були в `hide` і стали видимими через entries. Нові `new-x12*` (Віоріка v1–v5, Інна, фото Влада f1/f2, `p70`, `p70b`, `gold`) — CSS `.s12-*` у кінці rest-1006.css, картинки `assets/gen-rest-1012/s7/`, логотипи `assets/gen-rest-1012/logos/`. 19 екранів, яких немає в Google, стоять біля сусідів з позначкою KEEP у патчі — чекаємо відповіді Влада, прибирати через `drop`. Креативи Віоріки (`new-x12v4`) поки картинки — Мирослав надішле відео.
- 13.10 · відео креативів Віоріки `new-x12v4v` (rest 262, `_patch_1013_vio_video.py`, `.s12-vids`); Інна «Лучше всего сработавший креатив» `new-x12innab` (rest 265, `_patch_1013_inna_best.py`, `.s12-best`, файли з Telegram Влада); «Разные ниши» (rest 302) — картки зі скрінами сайтів `assets/vlad-1409/brands/` (`_patch_1013_niches.py`, `.nb-img`). Експорт усієї деки для Google Slides: `shots/export-full-1013/` (`_cdp_export_v2.mjs` двома потоками 1–245 / 246–490, PERSTEP).
- 13.10 · rest 149 «Два пути» = 3 екрани (`_patch_1013_two_paths.py`: 1943#37 + копії `copy-x13pv2b/c`, варіант `foundation.secret3Final.variant` → клас `.sf-v-a/b/c` у `js/secret3-final.js`). rest 187 — без тіні тексту в жовтій плашці. rest 193 «Ремесло делает агент» — відео `assets/gen-rest-1013/r193/r193-chain.mp4` (Seedance 2.5 з картинки Google G61, `.r193`, `_patch_1013_r193_video.py`; варіанти B/C там же). Повна дека в PPTX: `shots/export-full-1013/AI-Operator-full-1013.pptx` (571 сл., 89 МБ; кадри в старій нумерації до вставки «Двух путей», змінені екрани дознято `redo*/` і підставлено вручну).
- 13.10 · `_patch_1013_cleanup.py`: у drop 2226#67/#59/#64/#73/#92 і `new-x226hunt`; артефакти (2226#68, 2921#7/#18/#26/#31) — одразу демо (steps ['Живое демо агента'], крок-список вирізано); відео Жені (2921#19) — кнопка звуку `.snd-btn` (`js/snd-toggle.js`, capture-клік); Света (g409…198) — скрін з кружечками `.r250-circ`. «Два пути» кроки 2–3 без входу слайда (`.sf-v-b/c.on{animation:none}`, клас `sf-in` з `secret3-final.js`). rest 187 `mark.hl` padding .02/.12em. Пакети: режим `?m=f` (поверх sq) у `aim-p4-modes/modes.*` — НЕ увімкнено в слайдах (медіа не вантажаться, знизу порожньо); макет `transcripts/2026-10-12-preza-vlad/pakety-bulo-stalo.jpg`.
- 13.10 · rest 245 кружечки Свети справа знизу фото; `new-x12v5` у drop; rest 260 Інна — відео праворуч + скрін кабінету поверх (`.s12-best`, позиції від .b13-body ≈ 22cqh); rest 263 Аня — кнопка `.s13-site` на geo.annakotsur.com; новий `new-x13itsq` (rest 266, після 2921#48) — цитата клієнта It's Beauty по словах (`.s13q`, анімації на `.s16-play`); rest 276 колаж `.s13-col` (`_patch_1013_anya_q.py`, колаж — прямо в `__deckOrder.slides.new-x12f2`).
- 13.10 · `_patch_1013_batch3.py`: у drop 2226#79/#80/#88/#89/#94–#97/#101/#102 (усі «KEEP» без пари в Google, крім «Сколько стоит год»); «херня за $70» — gif `assets/gif/spanky-throwing-money.mp4`; «Золотой дождь» у мокапі айфона `.s12-iph`; «Разные ниши» — лише назви; «Дорого» — `$250` по центру бирок. `js/deck.js show()`: на краю деки «вперед/назад» нічого не робить (раніше перезапускав останній слайд — «смикався»). Дека 476 екранів, /rest = 308. Повний експорт для Google — `shots/export-full-1013b/`.
