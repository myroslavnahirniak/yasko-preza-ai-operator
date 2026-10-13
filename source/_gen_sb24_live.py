#!/usr/bin/env python3
"""30.09 Мирослав: розкадровка фонового відео слайда 24 — реалістично: реальний Влад в ІНШОМУ образі (стоїть, не крісло/светр як у відео на відкритті),
   замість голограм — 5 справжніх гаджетів на столі; гроші — сповіщення на телефоні. Ніша стоматологія, один кадр ~12 с.
   python3 source/_gen_sb24_live.py [k1 …] → assets/gen-2430/sb24/live/kN.png"""
import os, re, subprocess, sys, concurrent.futures as cf
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(root, 'assets/gen-2430/sb24/live'); os.makedirs(D, exist_ok=True)
FACE = os.path.join(root, 'assets/photo/vlad-avatar.jpg')
BASE = ("Square 1:1 photoreal frame that looks like a real still from a premium commercial shot on an ARRI Alexa: natural realistic colour grading, neutral deep blacks, natural skin tones, believable practical light. "
        "A modern loft office in the evening: long dark wooden work table, a large window with soft city lights bokeh behind, a warm desk lamp; the image is NOT tinted gold or orange. "
        "No holograms, no floating icons, no glowing symbols, no coins — everything is real physical objects and real screens. "
        "The main character is the man from the reference photo — keep his exact likeness: platinum-white short hair, full light-brown beard; "
        "he wears a plain white t-shirt under an open charcoal-grey overshirt with sleeves pushed up, and he STANDS behind the table (he is not sitting, no armchair). "
        "The only other person is a young woman dentist with a dark ponytail in a white medical coat. "
        "Screens show realistic app interfaces but absolutely no readable text, no letters, no numbers, no logos, no watermark. ")
K = {
 'k1': "Over-the-shoulder shot: in the left foreground the shoulder and back of the woman dentist; she sets a small white architectural model of her dental clinic (tiny storefront with a tooth-shaped sign) on the table. "
       "The main character stands on the other side of the table, leaning on it with both hands, looking at the model with calm interest. On the table: a closed laptop and a few switched-off devices.",
 'k2': "ONE single image, not a split screen, not a collage: an extreme macro close-up of the main character's eyes filling the whole frame horizontally (eyebrows, the bridge of the nose, platinum hair edge at the top, top of the beard at the bottom), photoreal skin texture. "
       "In both irises the small white clinic model with the tooth-shaped sign is clearly reflected; a thin glint of warm lamp light crosses the eyes. Calm, focused, confident look, eyes slightly narrowed, faint smile lines — he already knows how to solve it.",
 'k3': "Medium shot: the main character taps the trackpad of an open laptop, and along the table five real devices have just lit up one after another: "
       "the laptop showing a dental clinic website with a smiling patient photo, a tablet showing a social-media ad post, a monitor showing an ad campaign dashboard with charts, "
       "a smartphone on a stand showing an incoming voice call with a sound wave, a smartphone showing a chat conversation. The woman dentist leans in, amazed.",
 'k4': "Medium shot: the main character holds his smartphone, its screen shows a stack of incoming payment notifications (light banners, no readable text), he smiles slightly. "
       "Next to him the woman dentist looks at her own phone which is filling with new appointment notifications, she smiles happily. The five lit devices stand on the table in front of them.",
 'k5': "Final wide composition for a presentation slide, the camera is further back and slightly higher, so the people are smaller in the frame. "
       "The whole TOP 42% of the frame is ONLY the large dark window with soft city-light bokeh — no heads, no people, no objects there. "
       "The man and the woman dentist stand behind the long table with their heads at about 46-50% of the frame height: the main character slightly left of centre with a relaxed confident smile and a phone in his hand, the smiling dentist on the right. "
       "On the table in front of them, between about 62% and 78% of the frame height, the five lit devices stand in ONE straight row, evenly spaced across the full width, screens facing the camera: "
       "a laptop with the clinic website, a tablet with an ad post, a monitor with an ad dashboard, a smartphone on a stand with a voice call wave, a smartphone with a chat. The small clinic model on the table. The table front edge at the bottom.",
}
def run(k):
    cmd = ['higgsfield', 'generate', 'create', 'gpt_image_2_5', '--prompt', BASE + K[k], '--aspect_ratio', '1:1', '--resolution', '2k', '--quality', 'xhigh', '--wait', '--wait-timeout', '20m', '--json']
    refs = [FACE] if k in ('k1', 'k2') else [os.path.join(D, 'k1.png'), FACE]
    for r in refs: cmd += ['--image-references', r]
    p = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r'https://[^"\s]+\.(?:png|jpg|jpeg|webp)', p.stdout)
    if not m: return k, 'FAIL ' + (p.stdout + p.stderr)[-300:]
    fn = os.path.join(D, k + '.png')
    subprocess.run(['curl', '-4', '-sS', '-L', '-m', '180', '--retry', '3', '-o', fn, m.group(0)])
    subprocess.run(['cwebp', '-quiet', '-q', '84', fn, '-o', fn[:-4] + '.webp'])
    return k, 'ok'
if __name__ == '__main__':
    ks = sys.argv[1:] or list(K)
    with cf.ThreadPoolExecutor(5) as ex:
        for k, r in ex.map(run, ks): print(k, r, flush=True)
