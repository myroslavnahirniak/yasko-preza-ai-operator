#!/usr/bin/env python3
"""30.09 Мирослав: розкадровка фонового відео слайда 24 — «Живий макет»: камера пірнає в макет клініки (tilt-shift мініатюра),
   крихітні агенти вмикають 5 фізичних «станцій» (сайт-вітрина, афіша, білборд, телефон на рецепції, консьєрж), пацієнти, каса.
   k1 = sb24/live/k1 (стоматологиня ставить макет). python3 source/_gen_sb24_diorama.py [k2 …] → assets/gen-2430/sb24/diorama/kN.png"""
import os, re, subprocess, sys, concurrent.futures as cf
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(root, 'assets/gen-2430/sb24/diorama')
FACE = os.path.join(root, 'assets/photo/vlad-avatar.jpg')
BASE = ("Square 1:1 photoreal frame, real macro tilt-shift miniature photography of a handmade architectural diorama (like a real film shot on a model set), shallow depth of field, "
        "natural realistic colours, warm evening practical lights, the diorama continues the small white dental clinic model from the reference image (same tiny storefront with a tooth-shaped sign). "
        "Tiny figurines are about 2 cm tall, realistic painted miniatures; the 'agents' are tiny figures in dark hooded jackets with small warm head lamps. "
        "No holograms, no floating icons, no screens with readable UI, absolutely no readable text, no letters, no numbers, no logos, no watermark. ")
K = {
 'k2': "Macro shot inside the miniature: a small quiet night street with the dental clinic storefront, its windows dark, nobody around. Several tiny hooded agent figures with head lamps walk in from the left carrying tiny tools, ladders and light boxes, ready to start work.",
 'k3': "Macro shot gliding along the miniature street, left to right: tiny agents have just switched on five things: the clinic's large shop window now glows as a display with a clean website layout (abstract shapes only), "
       "a street light-box poster with a smiling patient photo, a billboard on the neighbouring rooftop lit up, at the reception desk inside a tiny phone glows and rings with small light rings, "
       "and at the door a tiny friendly concierge figure in a dark suit greets people. Warm lights come on one after another.",
 'k4': "Macro shot: the miniature street is now alive: tiny patient figures walk along the pavement and line up at the clinic door, the concierge leads them in, through the window the reception is busy and a tiny cash register glows warmly with a few tiny gold coins; all five installations are lit.",
 'k5': "Final composition for a presentation slide: the whole living diorama on the dark wooden table seen from the front at a slight high angle, sharp. The TOP 40% of the frame is the softly blurred dark office background with window bokeh — empty, calm. "
       "In the middle of the frame, left to right in one row, five clearly separated lit installations: the glowing website shop window, the light-box poster with a smiling patient, the rooftop billboard, the reception with the ringing phone, the door with the concierge and a queue of tiny patients. "
       "At the far right edge, out of focus, the hand of the woman dentist in a white coat rests on the table.",
 'k6lit': "The same miniature street, clinic and style as the reference frames, recomposed as a street-level frontal view for a presentation slide, camera a bit further back so the whole clinic facade fits. "
       "The TOP 32% of the frame is ONLY softly blurred city bokeh — no billboard, no objects there. Between about 36% and 72% of the frame height, the five lit installations stand LEFT TO RIGHT in this exact order, clearly separated: "
       "(1) far left: a large shop window glowing as a website display with abstract layout blocks; (2) a street light-box poster with a smiling patient; (3) in the centre a billboard mounted LOW on the edge of the roof, its top edge no higher than 36% of the frame, showing a smiling woman; "
       "(4) the reception window where a tiny desk phone glows with small light rings; (5) far right: the open entrance door with a tiny concierge in a dark suit greeting a short queue of tiny patients, a tiny cash register glowing warmly inside. "
       "The wet dark road with reflections in the bottom 25%.",
 'k6dark': "EXACTLY the same composition, camera angle and diorama as the first reference frame, but BEFORE anything is switched on: the shop window is dark, the light-box poster and the billboard are unlit and blank, the reception is dark, "
       "no concierge and no patients; only a few tiny hooded agent figures with head lamps stand next to each of the five spots, ready. Same blurred bokeh on top, same wet road.",
 'k5dark': "EXACTLY the same composition, camera angle and diorama as the reference final frame, but BEFORE the agents switched anything on: the shop window is dark, the light-box poster and the rooftop billboard are unlit and blank, "
       "the reception is dark, no concierge at the door, no patients on the street; only a few tiny hooded agent figures with head lamps stand next to each of the five spots, ready. Soft evening light, the blurred office background on top stays the same.",
}
def run(k):
    cmd = ['higgsfield', 'generate', 'create', 'gpt_image_2_5', '--prompt', BASE + K[k], '--aspect_ratio', '1:1', '--resolution', '2k', '--quality', 'xhigh', '--wait', '--wait-timeout', '20m', '--json']
    refs = {'k5dark': ['k5.png'], 'k6lit': ['draft-t116.png', 'k3.png'], 'k6dark': ['k6lit.png']}.get(k, ['k1.png'])
    for r in refs: cmd += ['--image-references', os.path.join(D, r)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r'https://[^"\s]+\.(?:png|jpg|jpeg|webp)', p.stdout)
    if not m: return k, 'FAIL ' + (p.stdout + p.stderr)[-300:]
    fn = os.path.join(D, k + '.png')
    subprocess.run(['curl', '-4', '-sS', '-L', '-m', '180', '--retry', '3', '-o', fn, m.group(0)])
    subprocess.run(['cwebp', '-quiet', '-q', '84', fn, '-o', fn[:-4] + '.webp'])
    return k, 'ok'
if __name__ == '__main__':
    ks = sys.argv[1:] or list(K)
    with cf.ThreadPoolExecutor(4) as ex:
        for k, r in ex.map(run, ks): print(k, r, flush=True)
