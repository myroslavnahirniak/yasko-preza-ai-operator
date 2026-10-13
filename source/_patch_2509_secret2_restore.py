#!/usr/bin/env python3
"""25.09 Мирослав: повернути Секрет 2 у деку (oid g3f9b3adf0b8_0_1774, між «Переполнены биржи» і Секретом 3)
   у новому оформленні: 228–241 — iframe на secret2.html (локальний рендер), 242–259 — постери assets/gen-secret2-full/sNNN.webp."""
import json,copy
p='source/overrides.json'; o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
OID='g3f9b3adf0b8_0_1774'
pp=json.load(open('source/import-secret2/parts-backup.json',encoding='utf-8'))
data=json.load(open('js/secret2-data.js'.replace('.js','.json'),encoding='utf-8')) if False else None
# тексти v5 для alt/t беремо з бекапу частин
parts=[]
for pt in pp['slides']:
    n=pt['foundation']['importedHTML']; pt=copy.deepcopy(pt); pt.setdefault('k','')
    if n>=242:
        pt['b']=''  # текст вшитий у картинку
        pt['foundation']={'local':0,'type':'content','sourceOnly':False,'omitMedia':True,'media':[],
            'block129':{'kind':'s16','v2':True,'layout':'s16-poster','art':[{'src':f'assets/gen-secret2-full/s{n}.webp?v=20260922b','alt':pt['t']}]}}
        pt['note']='Секрет 2 · згенерований постер (GPT Image 2.5), текст вшитий у картинку; джерело source/_gen_secret2_full.py\n'+(pt.get('note') or '')
    else:
        pt['foundation']['importedLocal']=True
        pt['note']='Секрет 2 · локальний рендер secret2.html?n=%d\n'%n+(pt.get('note') or '')
    parts.append(pt)
s=va[OID]
s['presentationParts']={'sourceGoogleObjectId':OID,'allowPartTitles':True,'slides':parts,
    'authorization':'Мирослав 25.09.2026: Секрет 2 у новому оформленні (secret2.html + постери 242–259) замість імпорту v5.'}
s['omit']=False
s['reason']='25.09 Мирослав: повернути Секрет 2 (228–259) — 228–241 з secret2.html, 242–259 постерами | '+(s.get('reason') or '')
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('parts',len(parts),'iframe',sum(1 for x in parts if x['foundation'].get('importedLocal')),'poster',sum(1 for x in parts if x['foundation'].get('block129')))
