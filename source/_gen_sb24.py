#!/usr/bin/env python3
"""30.09 Мирослав: розкадровка фонового відео слайда 24 («реалити-шоу AI-агентов»), аніме, один кадр 12 с, ніша — стоматологія.
   python3 source/_gen_sb24.py [k1 k2 …]  → assets/gen-2430/sb24/kN.png"""
import os, re, subprocess, sys, concurrent.futures as cf
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(root, 'assets/gen-2430/sb24')
REFS = [os.path.join(D, 'ref-anime-vlad.png'), os.path.join(D, 'ref-anime-vlad2.png'), os.path.join(D, 'ref-anime-heads.jpg')]
BASE = ("Square 1:1 frame from a high-end cinematic anime film, exactly the drawing style of the reference frames (clean cel shading, painterly backgrounds, soft cinematic light). "
        "The main character is the man from the reference frames: the same face, platinum-white swept-back hair, full dark-blond beard; here he wears a black t-shirt and black over-ear headphones around his neck. "
        "Colour palette strictly black, deep warm brown and glowing electric-yellow gold (#FDD506); night office lit by warm golden light, no blue, no purple, no green. "
        "The man has NO tattoo and NO marks on his forehead or head. The only other person is the young woman dentist with a dark ponytail in a white medical coat — never an old man, never a monk, never a copy of the main character. "
        "Absolutely no readable text, no letters, no numbers, no logos, no watermark. ")
K = {
 'k1': "Over-the-shoulder shot: in the left foreground the shoulder and back of a young woman dentist in a white medical coat with a dark ponytail; she is placing on the desk a small glowing miniature model of her dental clinic (a tiny storefront with a tooth-shaped sign). "
       "Behind the dark desk sits the main character in a black leather chair, a laptop in front of him, he looks up at her calmly. Dark night office with warm golden lamp light.",
 'k2': "Extreme close-up of the main character's eyes, classic anime eye close-up filling the frame horizontally (eyebrows and upper part of the nose visible). In his pupils the tiny glowing dental clinic miniature is reflected. "
       "A sharp golden glint flashes across the iris; the look is calm, focused and confident, eyes slightly narrowed, the corners of the eyes smiling a little: 'got it, here is how we solve it'. Not surprised.",
 'k3': "Medium shot: the main character at his desk raises his right hand and snaps his fingers, a small golden spark at his fingertips. Around and above him five translucent golden holographic panels unfold in a wide arc: "
       "a website page, a social-media ad post, a megaphone, a headset with sound waves, a chat with message bubbles. In each panel a tiny glowing hooded agent figure is busy working. The dentist stands at the right edge, amazed.",
 'k4': "Medium shot: above him hang the five golden holographic service panels (a website page, an ad post, a megaphone, a headset, a chat) — icons only, NOT portraits, no faces in the panels. Streams of glowing golden coins and light flow out of the five holographic panels and pour into a smartphone the main character holds in his hand; the phone screen glows gold like an incoming payment. "
       "Golden coins bounce onto the dark desk. The dentist on the right smiles happily; the miniature dental clinic on the desk now glows brightly with tiny patient figures lining up at its door.",
 'k5': "Final wide composition for a presentation slide: the upper 36% of the frame is calm dark night office background, completely empty (no panels, no objects there). Just below that, between 38% and 54% of the frame height, five golden holographic panels hang in ONE straight horizontal row, evenly spaced, same size, "
       "left to right: a website page, a social-media ad post, a megaphone, a headset with sound waves, a chat with message bubbles. Below them the main character sits at the desk, relaxed, confident slight smile, "
       "a smartphone glowing gold in his hand and a small neat pile of golden coins on the desk; the smiling young woman dentist with a dark ponytail in a white coat stands on the right, the glowing miniature clinic on the desk.",
}
def run(k):
    cmd = ['higgsfield', 'generate', 'create', 'gpt_image_2_5', '--prompt', BASE + K[k], '--aspect_ratio', '1:1', '--resolution', '2k', '--quality', 'xhigh', '--wait', '--wait-timeout', '20m', '--json']
    refs = REFS if k in ('k1', 'k2') else [os.path.join(D, 'k1.png'), os.path.join(D, 'ref-anime-vlad2.png')]
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
