#!/usr/bin/env python3
"""09.10 · Google Влада після 08.10: rest 149 «Как это устроено» — у Google латка поверх шапки скріна платформи
(«AI Маркетолог 3.0 / VIP. Фокус-группа» — стара назва продукту) → прибираємо цей текст з постера r137-ustroeno-q2.
Темний текст на світлому екрані ноутбука: маска = темні пікселі в прямокутнику, фон — push-pull зі світлих пікселів довкола."""
import numpy as np
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]


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


def erase_dark(im, box, thr=150, grow=4, known_min=200):
    a = np.asarray(im.convert('RGB')).astype(float)
    H, W = a.shape[:2]
    x0, y0, x1, y1 = int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)
    lum = a @ [0.299, 0.587, 0.114]
    R = np.zeros((H, W), bool); R[y0:y1, x0:x1] = True
    for x in range(x0, x1):   # не чіпати рамку ноутбука: маска лише нижче першого світлого пікселя екрана в колонці
        col = np.nonzero(lum[y0 - 12:y1, x] > 200)[0]
        top = y0 - 12 + (col[0] if len(col) else y1 - y0 + 12)
        R[:min(top + 3, H), x] = False
    t = ((lum < thr) & R).astype(np.uint8) * 255
    M = np.asarray(Image.fromarray(t).filter(ImageFilter.MaxFilter(grow * 2 + 1))).astype(float) / 255 * R
    lumb = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.MinFilter(7))).astype(float)
    K = ((M < 0.5) & (lumb > known_min) & R).astype(float)
    K[~R] = 0
    # зразки беремо лише зі світлого екрана довкола (рамка прямокутника + 12 px)
    pad = np.zeros((H, W), bool); pad[max(0, y0 - 12):y1 + 12, max(0, x0 - 12):x1 + 12] = True
    K = (((M < 0.5) & (lumb > known_min) & pad)).astype(float)
    est = _fill(a, K)
    Ms = np.asarray(Image.fromarray((M * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))).astype(float) / 255
    out = a * (1 - Ms[..., None]) + est * Ms[..., None]
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


im = Image.open(ROOT / 'assets/gen-rest-1006/r137-ustroeno-q2.webp').convert('RGB')
im = erase_dark(im, (0.405, 0.236, 0.575, 0.292))
im.save(ROOT / 'assets/gen-1009/r149-ustroeno-noname.webp', quality=88)
print('→ assets/gen-1009/r149-ustroeno-noname.webp', im.size)
