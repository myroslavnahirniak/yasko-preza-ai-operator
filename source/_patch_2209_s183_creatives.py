#!/usr/bin/env python3
"""22.09 Мирослав: слайд 183 (g3f9b3adf0b8_0_2921, presentationParts) — картка 03 «рекламные объявления»: замість плейсхолдера два креативи Влада (dizayn/creative-a,b)."""
import json
P='source/overrides.json'; d=json.load(open(P,encoding='utf-8'))
OLD='<div class="s16-media s16-ph"><div>рекламные объявления · визуал позже</div></div>'
NEW='<div class="s16-media s16-ads2"><img src="assets/vlad-1409/dizayn/creative-a.webp" alt="Креатив: 6 дизайнов за 20 минут"><img src="assets/vlad-1409/dizayn/creative-b.webp" alt="Креатив: контент без рутины"></div>'
hits=0
def walk(o):
    global hits
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='b' and isinstance(v,str) and OLD in v: o[k]=v.replace(OLD,NEW); hits+=1
            else: walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d)
assert hits>=1, 'плейсхолдер не знайдено'
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('patched',hits)
