#!/usr/bin/env python3
"""09.10 Мирослав (2226 #78/#80/#81):
— rest 230 «Выберите свой сценарий»: зверху gif (The Voice: тиснуть кнопку, assets/gif/voice-button-press.mp4), далі текст і кнопка; менший відступ під кнопкою; без фону з валізою;
— rest 232 «Даже половина результата…»: блок «А теперь представьте:» — по центру (CSS);
— rest 233 «Мне достаточно и одного клиента»: яскравіша картинка — рукостискання в золотому світлі (GPT Image 2.5, assets/gen-rest-1009/r233-a.webp; запасна — подарунок r233-b.webp)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r230-233-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
x = p[77]
assert 'r230-gif' not in x['b']
x['b'] = ('<div class="r230-gif"><video src="assets/gif/voice-button-press.mp4" poster="assets/gif/voice-button-press-poster.jpg" autoplay loop muted playsinline aria-label="Наставник шоу «Голос» жмёт кнопку"></video></div>' + x['b'])
x['foundation']['block129']['art'] = None
x['note'] = (x.get('note') or '') + '\n09.10 Мирослав: зверху gif — жмуть кнопку; без валізи; менший відступ під кнопкою.'
y = p[80]
y['foundation']['block129']['art'] = [{'src': 'assets/gen-rest-1009/r233-a.webp', 'alt': 'Рукопожатие в золотом свете'}]
y['note'] = (y.get('note') or '') + '\n09.10 Мирослав: яскравіша картинка — рукостискання в золотому світлі (запасна: подарунок r233-b.webp).'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
