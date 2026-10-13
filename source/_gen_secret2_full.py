#!/usr/bin/env python3
"""22.09 Мирослав: слайди Секрету 2 (242–259) як цілі картинки з вшитим текстом через Higgsfield GPT Image 2.5.
   python3 source/_gen_secret2_full.py            # всі
   python3 source/_gen_secret2_full.py 242 245    # вибрані
   Результат: assets/gen-secret2-full/sNNN.png (+ .webp), лог assets/gen-secret2-full/log.json"""
import json, os, sys, subprocess, concurrent.futures as cf, urllib.request, time
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(root, 'assets/gen-secret2-full'); os.makedirs(OUT, exist_ok=True)
R = os.path.join(OUT, 'refs')
STYLE_REFS = [os.path.join(R, 'style-2.webp'), os.path.join(R, 'style-3.webp')]
SASHA = os.path.join(root, 'assets/photo/sasha-bali.jpg')
SITE = os.path.join(root, 'assets/photo/sasha-site-faino.jpg')

BASE = ("Finished presentation slide, square 1:1, Russian-language webinar. Match the visual style of the reference slides exactly: "
        "pure near-black background, only white and electric-yellow (#FDD506) typography, generous margins, lots of air, premium minimal keynote look. "
        "Headline: large, bold, tight geometric sans-serif (Unbounded-like), white, with the key phrase in yellow. Body: clean light sans-serif (Inter-like), white or light grey. "
        "Small labels: uppercase, letter-spaced, grey. A short thin yellow line above the closing statement. Any props are photoreal dark 3D objects with soft warm light and yellow accents, minimal, never cluttered. "
        "Render ALL Russian text EXACTLY as written below, letter by letter, correct punctuation, no extra words, no logos, no watermark, nothing else on the slide. ")

S = {
242: "Headline top-left: «Сломать» white, «невозможно» yellow. Below, three rows, each with a small dark 3D icon on the left (a compass, a padlock, a chat bubble) and text: "
     "row 1 bold white «Ведёт по шагам», grey subline «не даёт перескочить и забыть»; row 2 «Нет кнопки «испортить»», subline «ошибиться негде»; row 3 «Не понял — спроси у него же», subline «не надо гуглить и искать курсы». "
     "Bottom closing statement: «Первый вопрос закрыт.» white, «Второй тяжелее» yellow.",
243: "The teenager on the right half of the slide is the person from the LAST reference photo — keep his exact likeness (face, messy dark hair), calm neutral expression, mouth closed, black t-shirt, half-body portrait on black with warm light. "
     "Headline top-left over two-three lines: «Я взял человека с» white, «худшими вводными,» yellow, «каких смог найти» white. "
     "Body under the headline: «Своего сына Сашу. 14 лет. Ни опыта, ни маркетинга, ни кода.» Then a second paragraph: «Он никогда никому ничего не продавал — и от руки почти не пишет, всё на компьютере».",
244: "Hero slide. Background scene: a row of empty dark glass storefronts with faint warm rim light, receding into darkness, very subtle. "
     "Headline centred-left: «И предложил то, чего сам раньше» white, «не допускал» yellow. Below it, a large quote in yellow bold: «Давай продадим сайты, которых ещё нет» with Russian quotation marks « ». Nothing else on the slide: no accent line, no text at the bottom.",
245: "Headline top-left: «Ниша нашлась» white, «из-за собаки» yellow. Right half: a photoreal small fluffy white dog sitting on a dark grooming table, soft warm light, black background. "
     "Body left: «Знакомая переехала в новый город и хотела записать собаку на груминг. Не смогла нигде.» "
     "Bottom closing in yellow: «У всех салонов сайты такие, что записаться нельзя».",
246: "Headline top-left: «Почему именно» white, «такие ниши» yellow. Below, three dark cards in a row, each with a small dark 3D icon (a shop, two people, a phone with a cross) and text: "
     "card 1 «Бизнес офлайн и работает» + grey «не стартап, а живая точка»; card 2 «Клиенты уже есть» + grey «их не надо искать — их теряют»; card 3 «Сайта нет или он мешает» + grey «записаться невозможно». "
     "Bottom closing: «И шаблон под такую нишу у нас уже готов» with «уже готов» in yellow.",
247: "Headline top-left: «Алгоритм, который я ему» white, «дал» yellow. Below, a clean numbered list with yellow numbers 01–05: "
     "«01 Найди 10 салонов в одном городе», «02 Напиши каждому «можно записаться?»», «03 Когда ответят «хотел через сайт — не вышло»», «04 «Я вам его уже сделал» — обычно беру $1.000, вам бесплатно», «05 Сказал «да» — агент собирает сайт по шаблону». "
     "Small grey line: «Саше хватило первой десятки. Обычно нужно больше — посчитаем в следующем секрете». Bottom closing: «Пять шагов.» white, «Ни одного, где надо уметь продавать» yellow.",
248: "Headline top-left: «Вот что именно» white, «пишем» yellow. Right: a dark phone-style chat, three outgoing dark message bubbles with grey uppercase labels above them and one incoming reply: "
     "label «ПЕРВОЕ СООБЩЕНИЕ» bubble «Добрый день! А к вам можно записать собаку на груминг?»; grey reply bubble labelled «ОТВЕЧАЮТ» «Да, конечно. На какое число?»; "
     "label «ВТОРОЕ» bubble «Я пробовал записаться через сайт — не получилось. Вы так много клиентов теряете?»; label in yellow «ТРЕТЬЕ — РАДИ НЕГО ВСЁ» bubble with yellow border «Я сделал вам новый сайт, где можно записаться за минуту. Обычно беру за такие $1.000 — вам сделал бесплатно. Хотите посмотреть?». Show the chat ONCE, large, as the only element besides the headline. No closing statement, no accent line, no other text at the bottom.",
249: "Headline top-left: «Почему это» white, «срабатывает» yellow. Body: «Вы ничего не продаёте. Вы уже сделали — и отдаёте. Человеку нечего согласовывать, нечего ждать и нечем рисковать.» "
     "Large yellow statement: «Клиент убеждает себя сам». Grey small: «И так можно сколько угодно: сайт агенту стоит копейки. Метод посчитан и повторяем — цифры будут в следующем секрете». "
     "Prop on the right: a dark open hand-sized gift box with a small glowing laptop inside, warm light, minimal.",
250: "The teenager on the right is the person from the LAST reference photo — keep his exact likeness (face, messy dark hair), calm neutral expression, mouth closed, black t-shirt, portrait on black with warm light. Small grey label top-left «КТО ЭТО СДЕЛАЛ», headline «Саша» in white, subline «Первая продажа — меньше чем через сутки» with «меньше чем через сутки» yellow. "
     "Two stat blocks: label «СКОЛЬКО ЗАНЯЛО», big white «Меньше 24 часов», grey «алгоритм я показал один раз»; label «СКОЛЬКО ПРИНЕСЛО», big yellow «$250», grey «дальше его вёл агент, а не я». "
     "Grey line: «$1.000 — сколько стоит работа. $250 — сколько берёт новичок за первую. Эта разница и есть ваш аргумент». Bottom closing in yellow: «Мой сын заработал свои первые деньги раньше, чем я в его возрасте узнал, что так вообще можно».",
251: "Small grey label «ЭКРАН», headline «Вот этот» white «сайт» yellow. Centre: a dark laptop whose screen shows EXACTLY the website from the LAST reference image (a pet grooming website with a white dog), reproduce that screenshot faithfully. "
     "Below: «ФАЙНО!pet — грумінг-салон у Харкові» white, grey «Услуги, цены, работы мастеров, запись ↗». Bottom closing in yellow: «Живой. Можно открыть прямо сейчас».",
252: "Headline top-left: «Вы не продаёте.» white, «Вы отдаёте» yellow. Two columns: left dim grey label «КАК БЫЛО» with three rows and grey dots: «уговорить», «отработать возражения», «дожать сомневающегося»; "
     "right label in yellow «КАК ТЕПЕРЬ» with yellow dots: «отдал готовое», «показал тем, кому подходит», «работаешь только с теми, кто сказал «да»». Thin vertical divider between columns. "
     "Bottom closing: «Услуг у вас безлимит — их делают агенты.» white, «Уговаривать незачем» yellow.",
253: "Headline top-left: «И общаться уметь» white, «не надо» yellow. Body: «Что ответить, как снять сомнение, чем закрыть — переписку ведёт нейронка.» "
     "Bottom closing yellow: «Отдельного навыка продаж здесь просто нет». Prop right: a dark phone with a glowing chat and a small dark AI cube with a yellow glowing edge next to it, minimal.",
254: "Headline top-left: «Сайт — только» white, «первая связка» yellow. Three rows with a small grey label «КОМУ» and text: "
     "row 1 white «Сайт уже хороший» → yellow «ему — AI-SEO, чтобы советовали нейросети»; row 2 «Заявки идут, отвечать некому» → yellow «ему — AI-продавца»; row 3 «Ведёт контент сам» → yellow «ему — контент-завод». Thin yellow arrows between. "
     "Bottom closing: «Формула та же.» white, «Меняется одна переменная» yellow.",
255: "Headline top-left: «И под каждую — своя» white, «модель поиска» yellow. Centre: eight dark rounded pill tags with thin grey borders, white text: «стоматология», «барбершоп», «груминг», «оптика», «кондитерская», «автомойка», «студия маникюра», «кофейня»; the «груминг» pill is yellow with black text. "
     "Bottom closing: «Не «попробуйте разное», а последовательность, которую уже прогнали и знают, чего от неё ждать» with «последовательность» in yellow.",
256: "Headline top-left: «А если ему» white, «не понравится?» yellow, in Russian quotation marks « ». Body: «Правки — это норма, а не провал. Дизайнер переделывает по три раза и берёт за это деньги.» "
     "Bottom closing yellow: «У вас правка занимает минуты, а не дни». Prop right: a small stack of dark paper drafts next to a clean glowing tablet, minimal.",
257: "Headline top-left: «И главное — вы показываете» white, «до оплаты» yellow. Body: «Он видит демо раньше, чем платит.» Bottom closing yellow: «Ситуация «заплатил и разочаровался» просто не возникает». "
     "Prop right: a dark laptop showing a bright website preview in front, and a dim dark bank card far behind it out of focus.",
258: "Hero slide, centred. Headline: «Ни один из них не стал» white, «специалистом» yellow. Below, big yellow bold: «Все просто включили машину». Prop: one large photoreal dark physical power switch with a yellow glowing ON indicator, on black, minimal.",
259: "Headline top-left: «Петля закрыта.» white, «Осталось одно» yellow. Body: «Продавать вы умеете — точнее, уметь и не надо.» Grey: «Остался вопрос, который я слышу чаще всех: а когда это делать и где брать людей?» "
     "Bottom big yellow: «Видите себя внутри? Напишите «вижу»». Prop right: a closed glowing yellow ring on black, minimal.",
}
EXTRA = {243: [SASHA], 250: [SASHA], 251: [SITE]}

def run(n):
    refs = STYLE_REFS + EXTRA.get(n, [])
    cmd = ['higgsfield', 'generate', 'create', 'gpt_image_2_5', '--prompt', BASE + S[n], '--aspect_ratio', '1:1', '--resolution', '2k', '--quality', 'xhigh', '--wait', '--wait-timeout', '20m', '--json']
    for r in refs: cmd += ['--image-references', r]
    t = time.time(); p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        d = json.loads(p.stdout); d = d[0] if isinstance(d, list) else d
    except Exception:
        return n, None, (p.stdout + p.stderr)[-400:]
    url = d.get('result_url') or (d.get('results') or [{}])[0].get('url') if isinstance(d.get('results'), list) else d.get('result_url')
    if not url:
        blob = json.dumps(d); import re
        m = re.search(r'https://[^"\s]+\.(?:png|jpg|webp)', blob); url = m.group(0) if m else None
    if not url: return n, None, json.dumps(d)[:400]
    fn = os.path.join(OUT, f's{n}.png')
    r = subprocess.run(['curl', '-4', '-sS', '-L', '-m', '180', '--retry', '3', '-o', fn, url], capture_output=True, text=True)
    if r.returncode or not os.path.exists(fn) or os.path.getsize(fn) < 10000: return n, None, 'download failed: ' + r.stderr[-200:]
    subprocess.run(['cwebp', '-quiet', '-q', '84', fn, '-o', fn[:-4] + '.webp'])
    return n, fn, f'{time.time()-t:.0f}s'

if __name__ == '__main__':
    ns = [int(a) for a in sys.argv[1:]] or sorted(S)
    log = {}
    with cf.ThreadPoolExecutor(2) as ex:
        for n, fn, info in ex.map(run, ns):
            print(n, 'ok' if fn else 'FAIL', info, flush=True); log[n] = {'file': fn, 'info': info}
    json.dump(log, open(os.path.join(OUT, 'log.json'), 'w'), ensure_ascii=False, indent=1)
