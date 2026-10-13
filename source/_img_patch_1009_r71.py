#!/usr/bin/env python3
"""09.10 · rest 71 (G338, «А потом спросил… -80% от рыночной стоимости»): фон без вшитого заголовка, щоб заголовок був живим
тим самим шрифтом, що на rest 70 (layout s16-g1001 + g6-photo). Бирка на столі — «-80%», як у s2-338-minus80.
Функції erase/text/save — з _img_patch_1008.py (виконується лише частина до першого патча)."""
from pathlib import Path
src = (Path(__file__).parent / '_img_patch_1008.py').read_text(encoding='utf-8')
exec(compile(src[:src.index('# G331')], '_img_patch_1008.py', 'exec'))

im = Image.open(A / 'gen-rest-1006/r071-poster-v1.webp').convert('RGB')
im = erase(im, (0.01, 0.05, 0.99, 0.225), mode='text', thr=55, grow=9)       # заголовок угорі
im = erase(im, (0.452, 0.630, 0.508, 0.697), mode='text', thr=60, grow=4)    # «¼» на бирці
im = text(im, (855, 1158), [[('-80%', Y)]], 36, anchor='ma')
save(im, 's2-338-minus80-clean.webp')
