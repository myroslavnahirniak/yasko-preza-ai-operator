#!/usr/bin/env python3
"""30.09 Мирослав: розкадровка фонового відео слайда 24 — ФОТОРЕАЛ з реальним Владом (не аніме), ніша стоматологія, один кадр ~12 с.
   python3 source/_gen_sb24_real.py [k1 k2 …]  → assets/gen-2430/sb24/real/kN.png"""
import os, re, subprocess, sys, concurrent.futures as cf
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(root, 'assets/gen-2430/sb24/real')
FACE = os.path.join(root, 'assets/photo/vlad-avatar.jpg')
GOLD = os.path.join(root, 'assets/photo/vlad-portrait-gold.png')
CHAIR = os.path.join(D, 'ref-hero-chair.png')
BASE = ("Square 1:1 photoreal frame that looks like a real still from a premium commercial shot on an ARRI Alexa with natural, realistic colour grading: neutral deep blacks, natural skin tones, believable light. "
        "A modern dark office at night, lit by a warm desk lamp and soft city lights through a large window; no golden haze, the image is NOT tinted gold or orange. "
        "Any holograms are subtle, semi-transparent pale warm-white light projections with only a hint of yellow, thin and elegant, like real sci-fi UI in a film — never saturated. "
        "The main character is the man from the reference photo — keep his exact likeness: platinum-white short hair, full light-brown beard, calm face; he wears a black knit sweater. "
        "The only other person is a young woman dentist with a dark ponytail in a white medical coat. "
        "Absolutely no readable text, no letters, no numbers, no logos, no watermark. ")
K = {
 'k1': "Over-the-shoulder shot: in the left foreground the shoulder and back of the woman dentist; she places on the dark desk a small realistic white architectural model of her dental clinic with tiny warm lit windows (a tiny storefront with a tooth-shaped sign). "
       "Behind the desk the main character sits in a black leather armchair, a laptop beside him, he looks up at her calmly with interest.",
 'k2': "Extreme macro close-up of the main character's eyes, filling the frame horizontally (eyebrows and bridge of the nose visible, photoreal skin texture). "
       "In his irises the tiny dental clinic model is reflected; a thin glint of warm light sweeps across the eyes. The look is calm, focused and confident, eyes slightly narrowed, faint smile lines — 'got it, here is how we solve it'. Not surprised.",
 'k3': "Medium shot: the main character at the desk raises his right hand and snaps his fingers, a tiny spark of light at his fingertips. Above and around him five translucent holographic panels unfold in a wide arc: "
       "a website page, a social-media ad post, a megaphone, a headset with sound waves, a chat with message bubbles — icons only. In each panel a tiny luminous hooded agent figure is busy working. The woman dentist at the right edge watches, amazed.",
 'k4': "Medium shot: above him hang the five subtle holographic service panels (website, ad post, megaphone, headset, chat — icons only, no faces). A few thin streams of light with a handful of realistic gold coins flow from the panels into the smartphone he holds; "
       "the phone screen lights up like an incoming payment, a few real coins land on the dark desk. The woman dentist on the right smiles; the miniature clinic on the desk lights up with tiny patient figures lining up at its door.",
 'k5': "Final composition for a presentation slide, wide shot from slightly further back: the whole TOP 40% of the frame is calm dark night office wall, completely empty — nothing there at all. "
       "The five subtle holographic panels hang LOW, in ONE straight horizontal row whose top edge is at about 42% of the frame height and bottom edge at about 56%, evenly spaced across the full width, same size, left to right: "
       "a website page, a social-media ad post, a megaphone, a headset with sound waves, a chat with message bubbles. Nothing overlaps the panels. "
       "Below the row: the main character sits relaxed in the armchair at the desk, confident slight smile, a smartphone with a lit screen in his hand, a small neat stack of real coins on the desk; "
       "the smiling woman dentist stands at the far right below the panel row (her head lower than the panels); the miniature clinic with lit windows on the desk.",
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
