#!/usr/bin/env python3
"""08.10 Мирослав:
rest 40 (2921 частина 30, «AI-продавец, который живёт в телефоне») — замість SVG-сцени і лендингу: ролик Telegram-чату в iPhone, автозапуск;
rest 41 (copy-g293, «УСЛУГА 07 / 07 AI-продавец») — консультант і Telegram відео з автозапуском, без червоної рамки, «Конкуренция» 3 з 10."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r40-r41-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8')); V = o['__visibleGoogleAudit']['slides']
TG = ('<video src="assets/vlad-1409/video/tg-seller-voice.mp4" poster="assets/vlad-1409/video/tg-seller-voice-poster.jpg" '
      'autoplay muted loop playsinline aria-label="AI-продавец отвечает клиенту в Telegram"></video>')
x = V['g3f9b3adf0b8_0_2921']['presentationParts']['slides'][29]
b, n = re.subn(r'<div class="s16-scene r044-scene">.*?</svg></div><div class="s16-site">.*?</div></div></div>',
    '<div class="r040-phone"><div class="g1001-iphone"><i class="g1001-btn a"></i><i class="g1001-btn b"></i><i class="g1001-btn c"></i>'
    '<i class="g1001-btn d"></i><div class="g1001-iscreen">' + TG + '</div></div></div>', x['b'], flags=re.S)
assert n == 1, n
x['b'] = b; x['reason'] = (x.get('reason') or '') + ' · 08.10 Мирослав: ролик Telegram-чату з автозапуском замість візуалізації'
y = V['copy-g293']; b = y['set']['b']
reps = [
    ('<img class="v" src="assets/video/avatar-consultant-poster.jpg" alt="Видеоконсультант онлайн">',
     '<video class="v" src="assets/video/avatar-consultant.mp4" poster="assets/video/avatar-consultant-poster.jpg" autoplay muted loop playsinline aria-label="Видеоконсультант онлайн"></video>'),
    ('<img class="v" src="assets/video/seller-voice-poster.jpg" alt="AI-продавец в переписке">', TG.replace('<video ', '<video class="v" ')),
    ('<div class="co-metric co-competition co-flag"><div class="co-metrichead">Конкуренция<strong>6</strong></div>'
     '<div class="co-bars"><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i></div>',
     '<div class="co-metric co-competition"><div class="co-metrichead">Конкуренция<strong>3</strong></div>'
     '<div class="co-bars"><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i></div>'),
]
for old, new in reps:
    assert b.count(old) == 1, old[:70]; b = b.replace(old, new)
y['set']['b'] = b; y['reason'] += ' · 08.10 Мирослав: відео з автозапуском, без червоної рамки, конкуренція 3/10'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
