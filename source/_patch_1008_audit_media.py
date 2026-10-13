#!/usr/bin/env python3
"""08.10 аудит Google: картинки, які Влад поклав поверх кадрів у Google — переносимо в деку на ті самі місця.
rest 19 (copy-g254, G254) телефон ZARMILKAS · rest 28 (copy-g266, G266) КП «Александр…» · rest 41 (copy-g293, G293) фото
консультанта + червона рамка «Конкуренция» · rest 23 (g3f9b3adf0b8_0_1528, G261) обкладинка «AI-агент, который делает сайт»
замість стрічки «агент» і робота. Позиції — з XML Google (частки слайда), перераховані в координати .co-product-scene
(x .04, y .28, w .47, h .42)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-audit-media-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8')); V = o['__visibleGoogleAudit']['slides']
def note(x, why): x['reason'] = (x.get('reason') or '') + ' · 08.10 аудит Google: ' + why
def overlay(oid, img, style, alt, why):
    x = V[oid]; b = x['set']['b']
    i = b.index('<div class="co-product-scene">'); j = b.index('</svg></div>', i) + len('</svg>')
    assert 'co-vlad' not in b
    x['set']['b'] = b[:j] + '<img class="co-vlad" src="assets/google-1008/%s" alt="%s" style="%s">' % (img, alt, style) + b[j:]
    note(x, why)
overlay('copy-g254', 'g254-zarmilkas-phone.webp', 'left:20.9%;top:-8.3%;width:57%;height:116.7%',
        'Сайт ZARMILKAS на телефоне', 'телефон ZARMILKAS поверх ілюстрації, як у Google G254')
overlay('copy-g266', 'g266-kp.webp', 'left:-.2%;top:5.5%;width:101%;height:75.5%',
        'Коммерческие предложения — именные, под конкретную сделку', 'скрин КП поверх ілюстрації, як у Google G266')
overlay('copy-g293', 'g293-consultant.webp', 'left:4.5%;top:4.5%;width:51.3%;height:83.1%',
        'Видеоконсультант онлайн', 'фото консультанта поверх ілюстрації, як у Google G293')
x = V['copy-g293']; b = x['set']['b']
assert b.count('<div class="co-metric co-competition">') == 1
x['set']['b'] = b.replace('<div class="co-metric co-competition">', '<div class="co-metric co-competition co-flag">')
note(x, 'червона рамка навколо «Конкуренция», як у Google G293')
# rest 23 · G261
x = V['g3f9b3adf0b8_0_1528']; b = x['set']['b']
i = b.index('<div class="s16-msgs">'); j = b.index('<div class="s16-input">')
b = b[:i] + b[j:]
b = b.replace('<img class="r27-robot" src="assets/google-1001/g031-robot-look.webp" alt="">',
              '<img class="r23-cover" src="assets/google-1008/g261-agent-cover.webp" alt="AI-агент, который делает сайт — собирает сайт клиники сам и показывает каждый шаг работы">')
assert 'r23-cover' in b and 's16-msgs' not in b
x['set']['b'] = b
note(x, 'обкладинка «AI-агент, который делает сайт» замість стрічки «агент» і робота, як у Google G261')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
