#!/usr/bin/env python3
"""09.10 Мирослав (2226 частини #56/#64/#66):
— rest 208 «Я рискую десяткой»: без монети й дрібного «условия действуют…» — ці умови показано візуально по центру (шкала: эфир → +30 минут);
— rest 216 «Юра · 4 дня»: без мокапу телефона — вертикальне відео кейсу чистою карткою;
— rest 218 «Агент AI-Сайты: внутри — конвейер»: замість 8 неонових роботів — відео «офіс агента» (зелена студія з rest 10)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r208-218-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
def note(i, s): p[i]['note'] = (p[i].get('note') or '') + '\n09.10 Мирослав: ' + s

# 208
i = 55; b = p[i]['b']
T = '<p class="sl2-terms" style="margin-top:4cqh">условия действуют до конца эфира + 30 минут</p>'
assert b.count(T) == 1
b = b.replace(T, '')
b += ('<div class="r208-win sl2-a" style="--d:0.45s"><div class="r208-k">условия действуют</div>'
      '<div class="r208-bar"><div class="r208-live"><i></i>эфир</div><div class="r208-cut"><span>конец эфира</span></div>'
      '<div class="r208-plus"><b>+30</b> минут</div></div>'
      '<div class="r208-cap">до конца эфира <em>+ 30 минут</em></div></div>')
p[i]['b'] = b
p[i]['foundation']['block129']['art'] = None
note(i, 'монету й дрібний рядок прибрано; «до конца эфира + 30 минут» — шкала по центру.')

# 216 Юра
i = 63; b = p[i]['b']
OLD = ('<div class="g1001-iphone r198-phone"><i class="g1001-btn a"></i><i class="g1001-btn b"></i><i class="g1001-btn c"></i><i class="g1001-btn d"></i>'
       '<div class="g1001-iscreen"><video src="assets/video/kejsy-1409/09.mp4" poster="./assets/video/kejsy-1409/09-poster.jpg" playsinline loop preload="metadata"></video></div></div>')
assert b.count(OLD) == 1
p[i]['b'] = b.replace(OLD, '<div class="r198-card"><video src="assets/video/kejsy-1409/09.mp4" poster="./assets/video/kejsy-1409/09-poster.jpg" muted playsinline loop preload="auto"></video></div>')
note(i, 'без мокапу телефона — відео кейсу чистою карткою.')

# 218
i = 65
assert 'v6-source-61' in p[i]['b']
p[i]['b'] = ('<div class="r218"><div class="r218-eb">Первый готовый агент — ваш после блока 2</div>'
             '<div class="r218-stage"><span class="r218-lbl">Агент AI-Сайты · 8 задач внутри</span>'
             '<video src="assets/video/agent-sites/r010-studio-loop.mp4" poster="assets/video/agent-sites/r010-studio-loop-poster.jpg" autoplay muted loop playsinline '
             'aria-label="Офис агента: специалисты по очереди делают свою часть сайта"></video></div>'
             '<div class="r218-out"><span>Задача словами</span><em>→</em><b>сайт, который приводит клиентов</b></div>'
             '<p class="r218-fin">Вы ставите задачу словами. Кто за кем работает — решает агент</p></div>')
note(i, 'замість неонових роботів — відео «офіс агента» (зелена студія, як на rest 10).')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
