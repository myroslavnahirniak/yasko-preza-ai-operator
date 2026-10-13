#!/usr/bin/env python3
"""09.10 · rest 91 (G359 «Биржа / ... теряет клиентов»): права половина — прокат авто замість салону грумінгу (кейс VIP CAR).
gpt-image-2 images/edits з r076-birzha-a5.webp. → assets/gen-s2-1009/r091-birzha-cars-<n>.png"""
import json, os, sys, base64, subprocess, time
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
argv = sys.argv[1:]; sys.argv = [sys.argv[0]]
src = open(os.path.join(here, '_gen_openai.py'), encoding='utf-8').read(); exec(src[:src.index('FULL=')])
N = int(argv[0]) if argv else 1
from PIL import Image
tmp = os.path.join(root, 'assets/gen-s2-1009/_r091-src.png'); Image.open(os.path.join(root, 'assets/gen-rest-1006/r076-birzha-a5.webp')).convert('RGB').save(tmp)
PROMPT = ("Keep this image exactly as it is — same composition, same split into two halves by the thin yellow vertical line, same lighting, same colours, same fonts. "
          "The LEFT half (label «БИРЖА», the laptop with the list of executors and the crowd of dark figures, and its three lines of text below) must stay completely unchanged. "
          "The three lines of text in the bottom right («— конкурентов ноль», «— сравнивать не с кем», «— вы — единственный, кто написал») must stay exactly as they are. "
          "In the RIGHT half replace the pet grooming salon with a small premium CAR RENTAL office at night: the same storefront at the same place and size, "
          "through the big lit window a glossy black premium sedan stands inside the showroom (no dog, no grooming table, no paw icon). "
          "The sign above the window reads exactly «CAR RENTAL» with a small car icon instead of the paw. "
          "Replace the vertical words on the right side of the window with exactly: «АРЕНДА», «ДОСТАВКА», «ПРЕМИУМ», «24/7». "
          "Change the yellow label at the top of the right half to exactly: «ПРОКАТ АВТО, КОТОРЫЙ ТЕРЯЕТ КЛИЕНТОВ». "
          "Keep the phone with the yellow chat notification on the dark counter in front. Russian text must be rendered exactly, letter by letter, no extra words.")
def run(i):
    t = time.time()
    cmd = ['curl', '-s', '-m', '400', 'https://api.openai.com/v1/images/edits', '-H', 'Authorization: Bearer ' + key(),
           '-F', 'model=gpt-image-2', '-F', 'prompt=' + PROMPT, '-F', 'size=1024x1024', '-F', 'quality=high', '-F', 'n=1', '-F', 'image[]=@' + tmp]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try: d = json.loads(r.stdout)
    except Exception: print(i, 'BAD RESPONSE', r.stdout[:300]); return
    if 'data' not in d: print(i, 'ERROR', json.dumps(d.get('error', d))[:400]); return
    fn = os.path.join(root, f'assets/gen-s2-1009/r091-birzha-cars-{i}.png'); open(fn, 'wb').write(base64.b64decode(d['data'][0]['b64_json']))
    print(i, 'ok', fn, f'{time.time() - t:.0f}s')
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=N) as ex: list(ex.map(run, range(1, N + 1)))
