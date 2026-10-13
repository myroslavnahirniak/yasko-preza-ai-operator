# Передача справ: преза AI-Оператор через Telegram-бот (06.10.2026)

Ти — сесія Claude, запущена в терміналі з `--channels plugin:telegram@claude-plugins-official`. Мирослав (власник проєкту, пише українською) зараз поза ноутбуком і спілкується з тобою ТІЛЬКИ через бота @CalcB0_bot. Усе, що ти хочеш йому сказати, — через інструмент `reply` (chat_id із вхідного повідомлення, його DM = 503302590). Текст у терміналі він не бачить.

До цього з ним 4 дні працювала сесія в застосунку Claude («AI-Оператор презентація, слайд 124»). Її знання записані тут і в двох файлах нижче.

## Прочитати перед першою відповіддю
1. `preza-ai-operator/EDIT-CHEATSHEET.md` — де що лежить і як правити.
2. `preza-ai-operator/source/google-2026-10-01/CONTEXT-NEXT-CHAT.md` — розділи «Оновлення 03.10», записи 05.10 і «Оновлення 06.10» (найсвіжіше).

## Як працювати через бота
- **Голосові**: `download_attachment` → файл .oga → `mlx_whisper <файл> --model mlx-community/whisper-large-v3-turbo --language uk` (або ru, якщо говорить російською) → прочитати текст. Коротко підтвердь, що зрозумів, і роби.
- **Фото**: якщо в тезі є `image_path` — Read цей файл. Фото з Downloads, які він кидає «замінити слайд на фото», конвертуй у webp у `preza-ai-operator/assets/google-1001/` і став як `s16-poster` (див. 05.10 у CONTEXT).
- **Показати результат**: скрин слайда → `cd preza-ai-operator && URL="http://127.0.0.1:8765/main.html?square&clean&s=N" OUT=shots/edit NAME=xN FIRST=6000 STEPS="" node shots/_cdp_steps.mjs` → `reply` з `files:["/Users/miro/imperial/work/yasko/preza-ai-operator/shots/edit/xN-0.png"]`. Для другої частини — `rest.html?…&s=N` (свої номери з 1).
- **Посилання**: локальні 127.0.0.1 з телефона НЕ відкриваються. Коли просить «виклади» — деплой (нижче) і кидай `https://yasko-preza-1001.vercel.app/?square&clean&s=N` або `/rest?square&clean&s=N`.
- **Довгі задачі**: одразу `react` 👍 або коротке «роблю», потім результат новим `reply` (edit не дає сповіщення).
- Higgsfield CLI (`higgsfield generate create gpt_image_2_5 …`) працює, приклади: `preza-ai-operator/source/google-2026-10-06/_gen_1006.py` (увага: відповідь CLI — JSON-масив). Кожна генерація xhigh 2k ≈ 5 кредитів — кажи йому.

## Поточний стан (06.10, ~17:00)
- Сторінки: `main.html` = перша частина, екрани 1–174 (до «Первый — это чат. Второй — агент»); `rest.html` = друга, екрани 175–416 повної деки (свої номери 1–242). Повна робоча дека — `google180.html`. Генерація main/rest: `python3 source/_parts_1001.py .` (після кожної збірки).
- **НЕ ВИКЛАДЕНО**: друга частина за Google Влада від 06.10 (G324 новий текст, 7 нових слайдів rest 51–61, перестановка Секрету 2, /rest до кінця деки). На проді ще версія 05.10 (`dc-20261005-g`). Мирослав ще не сказав «виклади».
- Локальний сервер: `nohup python3 source/_serve_range.py 8765 > /tmp/preza-8765.log 2>&1 &` (з `preza-ai-operator/`; звичайний http.server ламає відео). Перевірка: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/main.html`.

## Цикл правки (коротко)
1. `python3 source/_slide.py N` — що за слайд (номер = повна дека google180; для main номери ті самі, для rest = N+174).
2. Правка: `python3 source/_edit.py N --reason "…" [--t …] [--b @file] [--b129 '{…}'] --no-build`; CSS — у кінці `css/google-1001.css`, потім бамп `google-1001.css?v=` в `index.html` і `google180.html`.
   - Пастки: багаточастинні oid (Секрет 2 = `g3f9b3adf0b8_0_1774`) — `--part`; легасі-слайди (`editorial`, `life-line`) правити прямо в `overrides.json` без `remove`; не перезаписувати запис oid цілком (там `presentationParts`). Прибрати слайд — `__deckOrder.drop` (ключ `oid#part`, id копії або нового).
3. Збірка: `FOUNDATION_SOURCE=google-2026-09-16/foundation-source-v2.json python3 source/_foundation_prepare.py && python3 source/_build_slides.py && python3 source/_parts_1001.py .` (рядок «!! deckOrder: нема екрана g3f9b3adf0b8_0_2751#0» — норма).
4. Скрин, подивитись самому, потім надіслати.
5. Запис у `CONTEXT-NEXT-CHAT.md` (одним рядком, що і де змінено).

## Деплой (тільки коли він просить)
- Бамп `slides-google180.js?v=dc-ДАТА-літера` в `index.html` і `google180.html` (поточний `dc-20261006-a`) → `python3 source/_parts_1001.py .` → `zsh source/_deploy_1001.sh > /tmp/deploy.log 2>&1` (3–5 хв) → перевірка `curl -s https://yasko-preza-1001.vercel.app/ | grep -o 'slides-google180.js?v=[^"]*'`.
- Старий прод `yasko-preza-v5` НЕ чіпати. Google-деку Влада НЕ чіпати.

## Смак (стисло)
Квадрат 1:1, чорно-жовтий `#FDD506`, без зеленого. Заголовки Unbounded, акцент тільки кольором через `<em>`. Текст з Google дослівно (лише описки). Жовта плашка з чорним текстом = як «Приз №N» / «Секрет №2». Один рух на вхід, далі статика. Після кожної правки — скрин і власна перевірка (обрізання тексту, накладання).
