#!/usr/bin/env python3
"""08.10 дзвінок з Владом, rest 57 (new-g325, «Но следующий вопрос: «А как мне это продать?»»):
«не рівно» — текст був зашитий у постер GPT і налазив на шапку; тепер живий текст шрифтами деки по центру,
під ним гіфка «HMM…» (Tenor, Pai Mei гладить бороду) — як просив Влад («якась гіфка хмммм», у Google G325 «ХМММММ?»)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-call-r57-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8')); V = o['__visibleGoogleAudit']['slides']
y = V['new-g325']
y['foundation']['block129'].update(layout='s16-g1001', art=None)
y['set']['t'] = '<span class="g6-pre">Но следующий вопрос:</span>«А как мне это <em>продать?</em>»'
y['set']['b'] = ('<p class="r57-sub">Чтоб не напрягаться и не сидеть без денег</p>'
                 '<div class="r57-gif"><video src="assets/gif/hmm-wise-old-man.mp4" poster="assets/gif/hmm-wise-old-man-poster.jpg" '
                 'autoplay muted loop playsinline aria-label="Мудрец гладит бороду: «Хммм…»"></video></div>')
y['set']['note'] = '08.10 дзвінок з Владом: живий текст замість постера з вшитим текстом; gif «HMM…» (Tenor, hmmm-wise-old-man).'
y['reason'] += ' · 08.10 дзвінок з Владом: текст не налазить на шапку (живий текст шрифтами деки), gif «хммм» як просив Влад (Google G325 «ХМММММ?»)'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
