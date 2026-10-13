#!/usr/bin/env python3
"""09.10 · rest 80/81 — прибрати грумінг, кейс прокату авто (VIP CAR).
r80: приціл над містом — у центрі прокат авто замість салону грумінгу (images/edits з s2-348-pricel.webp).
r81: «Есть разница, кому продавать» — права картинка: авто замість собаки (images/generations, у стилі фото швачки)."""
import json, os, sys, base64, subprocess, time
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
argv = sys.argv[1:]; sys.argv = [sys.argv[0]]
src = open(os.path.join(here, '_gen_openai.py'), encoding='utf-8').read(); exec(src[:src.index('FULL=')])
from PIL import Image
OUT = os.path.join(root, 'assets/gen-s2-1009')
tmp80 = os.path.join(OUT, '_r080-src.png'); Image.open(os.path.join(root, 'assets/gen-s2-1008/s2-348-pricel.webp')).convert('RGB').save(tmp80)
P80 = ("Keep this image exactly as it is: the same dark isometric night city, the same golden crosshair scope and its position, the same yellow map pins, "
       "the same camera angle, lighting and colours. Change ONLY the building in the centre of the crosshair: instead of the pet grooming shop it is a small "
       "premium car rental office — a glossy black premium sedan stands in the brightly lit glass showroom window, a car icon on the sign instead of the paw "
       "and scissors, no dog, no pets anywhere. No text, no letters.")
P81 = ("Square photo, photo-real, shot on Leica Q3 35mm, natural film grain, warm amber low-key light on a near-black background, cinematic and quiet, "
       "the same mood as a dim tailor workshop photo. A glossy black premium sedan, three-quarter front view, stands inside a small dark car rental showroom at night, "
       "warm reflections on the paint and the polished floor, a few warm ceiling lights. No people, no text, no logos, no licence plate letters.")
def call(kind, prompt, fn, image=None):
    t = time.time()
    if kind == 'edit':
        cmd = ['curl', '-s', '-m', '400', 'https://api.openai.com/v1/images/edits', '-H', 'Authorization: Bearer ' + key(), '-F', 'model=gpt-image-2',
               '-F', 'prompt=' + prompt, '-F', 'size=1536x1024', '-F', 'quality=high', '-F', 'n=1', '-F', 'image[]=@' + image]
    else:
        cmd = ['curl', '-s', '-m', '400', 'https://api.openai.com/v1/images/generations', '-H', 'Authorization: Bearer ' + key(), '-H', 'Content-Type: application/json',
               '--data-binary', json.dumps({'model': 'gpt-image-2', 'prompt': prompt, 'size': '1024x1024', 'quality': 'high', 'n': 1})]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try: d = json.loads(r.stdout)
    except Exception: print(fn, 'BAD RESPONSE', r.stdout[:300]); return
    if 'data' not in d: print(fn, 'ERROR', json.dumps(d.get('error', d))[:400]); return
    open(os.path.join(OUT, fn), 'wb').write(base64.b64decode(d['data'][0]['b64_json'])); print(fn, 'ok', f'{time.time() - t:.0f}s')
jobs = [('edit', P80, f'r080-pricel-cars-{i}.png', tmp80) for i in (1, 2)] + [('gen', P81, f'r081-car-{i}.png', None) for i in (1, 2)]
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as ex: list(ex.map(lambda j: call(*j), jobs))
