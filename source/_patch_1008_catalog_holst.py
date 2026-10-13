#!/usr/bin/env python3
"""08.10 Мирослав: каталоги rest 147/148 (2226 #15/#16):
— таблицю в кінці → картки як у Холсті (кнопки data-catalog-go, порядок і номери = кроки каталогу);
— крок 01 «AI-сайты»: живий сайт ZARMILKAS в iframe замість фото телефона;
— AI-продавец: конкуренція 3/10 (крок 07, картка) + та сама правка на rest 16 (new-g251)."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-catalog-holst-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8')); V = o['__visibleGoogleAudit']['slides']
SV = [  # n, назва, іконка Холсту, ціна, одиниця, складність, оплата, спрос, конкуренція
    (1, 'AI-сайты, которые приводят клиентов', 1, '$250–$1.200', 'за пакет', 'lo', 'разово', 9, 8),
    (2, 'AI-дизайн', 2, '$250–$900', 'за пакет', 'lo', 'разово', 8, 7),
    (3, 'Продающие AI-видео', 3, '$300–$1.200', 'за 8–12 роликов', 'lo', 'разово', 10, 5),
    (4, 'Контент-завод с AI-аватаром', 4, '$400–$1.400', 'в месяц', 'md', 'каждый месяц', 8, 6),
    (5, 'AI-таргет (платная реклама)', 6, '$300–$800', 'в месяц', 'md', 'каждый месяц', 7, 7),
    (6, 'AI-SEO (видимость в нейросетях)', 7, '$500', 'в месяц', 'md', 'каждый месяц', 7, 1),
    (7, 'AI-продавец', 5, '$500–$2.000', 'за сборку и ведение', 'md', 'сборка + ведение', 7, 3)]
def segs(v): return ''.join('<i class="on" style="--k:%d"></i>' % k if k < v else '<i style="--k:%d"></i>' % k for k in range(10))
def card(n, t, ic, pr, u, sl, py, sp, kk):
    return ('<button class="r20-c" data-catalog-go="%d" style="--i:%d"><span class="r20-ic"><img src="assets/holst-catalog/ic-%d.webp" alt=""></span>'
            '<span class="r20-nm"><span class="r20-n">%02d</span><span class="r20-t">%s</span></span><span class="r20-pr"><b>%s</b><span class="r20-u">%s</span></span>'
            '<span class="r20-sl %s"><i></i>%s</span><span class="r20-py%s">%s</span><span class="r20-sc">'
            '<span class="r20-g r20-sp"><span class="r20-l">спрос</span><span class="r20-segs">%s</span><b>%d</b></span>'
            '<span class="r20-g r20-kk"><span class="r20-l">конкуренция</span><span class="r20-segs">%s</span><b>%d</b></span></span></button>') % (
            n, n, ic, n, t, pr, u, sl, 'лёгкая' if sl == 'lo' else 'средняя', ' pm' if sl == 'md' else '', py, segs(sp), sp, segs(kk), kk)
HOLST = '<div class="co-holst r20-cat">' + ''.join(card(*s) for s in SV) + '</div>'
PHONE_OLD = '<img class="phone" src="assets/google-1008/g254-zarmilkas-phone.webp" alt="Сайт ZARMILKAS на телефоне">'
PHONE_NEW = '<div class="s16-phone" aria-label="zarmilkas-troyanda-video.vercel.app"><iframe src="assets/sites/zarmilkas/index.html" title="Сайт Zarmilkas — собран агентом" loading="lazy"></iframe></div>'
K6 = ('<div class="co-metric co-competition"><div class="co-metrichead">Конкуренция<strong>6</strong></div><div class="co-bars"><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i></div>')
K3 = ('<div class="co-metric co-competition"><div class="co-metrichead">Конкуренция<strong>3</strong></div><div class="co-bars"><i class="co-on"></i><i class="co-on"></i><i class="co-on"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i></div>')
parts = V['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
for i in (14, 15):
    b = parts[i]['b']
    assert b.count(PHONE_OLD) == 1; b = b.replace(PHONE_OLD, PHONE_NEW)
    s7 = b.index('УСЛУГА 07 / 07'); e7 = b.index('</section>', s7)
    sec = b[s7:e7]; assert sec.count(K6) == 1; b = b[:s7] + sec.replace(K6, K3) + b[e7:]
    t0 = b.index('<div class="co-table">'); t1 = b.index('<div class="co-tablehint">')
    b = b[:t0] + HOLST + b[t1:]
    parts[i]['b'] = b
    parts[i]['note'] = (parts[i].get('note') or '') + '\n08.10 Мирослав: таблиця → картки Холсту, AI-сайты — живий iframe, AI-продавец конкуренція 3.'
# rest 16 (new-g251): AI-продавец 6 → 3
x = V['new-g251']; b = x['set']['b']
i0 = b.index('<span class="r20-t">AI-продавец</span>'); i1 = b.index('</div>', i0)
seg = b[i0:i1]
old = re.search(r'<span class="r20-g r20-kk"><span class="r20-l">конкуренция</span><span class="r20-segs">.*?</span><b>6</b></span>', seg).group(0)
seg = seg.replace(old, '<span class="r20-g r20-kk"><span class="r20-l">конкуренция</span><span class="r20-segs">%s</span><b>3</b></span>' % segs(3))
x['set']['b'] = b[:i0] + seg + b[i1:]
x['reason'] += ' · 08.10 Мирослав: AI-продавец конкуренція 3'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
