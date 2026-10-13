#!/usr/bin/env python3
"""09.10 · rest 109, крок 2: натюрморт праворуч — речі прокату авто замість інструментів грумінгу (з r109-chips-cars-1.png)."""
import json, os, sys, base64, subprocess, time
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.argv = [sys.argv[0]]
src = open(os.path.join(here, '_gen_openai.py'), encoding='utf-8').read(); exec(src[:src.index('FULL=')])
OUT = os.path.join(root, 'assets/gen-s2-1009'); tmp = os.path.join(OUT, 'r109-chips-cars-1.png')
P = ("Keep this image exactly as it is — the same headline, the same chips with their exact texts (including the yellow chip «прокат авто»), "
     "the same bottom text, layout, fonts, colours and dark background. Change ONLY the still life on the right: instead of the grooming tools "
     "(scissors, comb, hair clipper, towel, bottles and jars) place car rental objects in the same spot and the same warm golden low-key lighting — "
     "a glossy black premium car key fob with a leather tag lying on a black stand, and a small glossy black scale model of a premium sedan next to it. "
     "No text on the objects, no other changes.")
def run(i):
    t = time.time()
    r = subprocess.run(['curl', '-s', '-m', '400', 'https://api.openai.com/v1/images/edits', '-H', 'Authorization: Bearer ' + key(), '-F', 'model=gpt-image-2',
                        '-F', 'prompt=' + P, '-F', 'size=1024x1024', '-F', 'quality=high', '-F', 'n=1', '-F', 'image[]=@' + tmp], capture_output=True, text=True)
    try: d = json.loads(r.stdout)
    except Exception: print(i, 'BAD', r.stdout[:300]); return
    if 'data' not in d: print(i, 'ERROR', json.dumps(d.get('error', d))[:400]); return
    open(os.path.join(OUT, f'r109-cars-final-{i}.png'), 'wb').write(base64.b64decode(d['data'][0]['b64_json'])); print(i, 'ok', f'{time.time() - t:.0f}s')
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as ex: list(ex.map(run, (1, 2)))
