#!/usr/bin/env python3
"""09.10 Мирослав: rest 109 «И под каждую — своя модель поиска» — чіп «стоматология» → «окна и двери»
(ніша, яку Влад виділив у списку зв'язок на G403 і з якої кейс Василия в Секреті 3). Текст стирається з чіпа (push-pull по темному
фону чіпа), новий — Manrope 500 тим самим кеглем і кольором, що сусідні чіпи. Вхід — поточний постер іншої сесії (прокат авто)."""
import numpy as np
from pathlib import Path
from PIL import Image, ImageFilter, ImageFont, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'assets/gen-s2-1009/r109-model-poiska-cars.webp'
OUT = ROOT / 'assets/gen-s2-1009/r109-model-poiska-cars-okna.webp'


def _fill(a, K):
    H, W = K.shape
    n = 1
    while n < max(H, W):
        n *= 2
    c = np.zeros((n, n, 3)); w = np.zeros((n, n))
    c[:H, :W] = a * K[..., None]; w[:H, :W] = K
    pyr = [(c, w)]
    while pyr[-1][1].shape[0] > 1:
        c, w = pyr[-1]; m = c.shape[0] // 2
        pyr.append((c.reshape(m, 2, m, 2, 3).sum((1, 3)), w.reshape(m, 2, m, 2).sum((1, 3))))
    c, w = pyr[-1]
    v = c / np.maximum(w, 1e-6)[..., None]
    for c, w in reversed(pyr[:-1]):
        up = np.repeat(np.repeat(v, 2, 0), 2, 1)
        up = (up + np.roll(up, 1, 0) + np.roll(up, -1, 0) + np.roll(up, 1, 1) + np.roll(up, -1, 1)) / 5
        al = np.minimum(w, 1.0)[..., None]
        v = al * (c / np.maximum(w, 1e-6)[..., None]) + (1 - al) * up
    return v[:H, :W]


im = Image.open(SRC).convert('RGB')
a = np.asarray(im).astype(float); H, W = a.shape[:2]
lum = a @ [0.299, 0.587, 0.114]
x0, y0, x1, y1 = 76, 318, 320, 370                     # нутро чіпа «стоматология» (рамка 60..334 × 305..382)
R = np.zeros((H, W), bool); R[y0:y1, x0:x1] = True
M = np.asarray(Image.fromarray(((lum > 70) & R).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(5))).astype(float) / 255 * R
K = ((M < 0.5) & (lum < 45)).astype(float)
K[:y0 - 6] = 0; K[y1 + 6:] = 0; K[:, :x0 - 6] = 0; K[:, x1 + 6:] = 0
est = _fill(a, K)
a = a * (1 - M[..., None]) + est * M[..., None]
im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

# колір тексту — з сусіднього чіпа «барбершоп»
ref = np.asarray(Image.open(SRC).convert('RGB'))[331:359, 415:580].reshape(-1, 3)
col = tuple(int(v) for v in ref[ref.sum(1).argmax()])
f = ImageFont.truetype(str(ROOT / 'assets/fonts/Manrope-500-cyrillic.woff2'), 28)
f.set_variation_by_axes([620])
d = ImageDraw.Draw(im)
words = ['окна', 'и', 'двери']
gap = 0.27 * 28
ws = [d.textlength(w, font=f) for w in words]
total = sum(ws) + gap * (len(words) - 1)
cx, base_mid = 197, 344.5                                 # центр чіпа і середина x-висоти сусідніх написів
bb = f.getbbox('о')                                       # x-висота: від верху «о» до низу
x = cx - total / 2
y = base_mid - (bb[1] + bb[3]) / 2
for w, ww in zip(words, ws):
    d.text((x, y), w, font=f, fill=col)
    x += ww + gap
im.save(OUT, quality=90)
print('→', OUT.name, 'колір', col, 'x-висота', bb[3] - bb[1])
