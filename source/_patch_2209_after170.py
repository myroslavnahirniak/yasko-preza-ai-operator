# 22.09 · Мирослав: після слайда 170 («Сотни часов и куча денег») вставити копії 7 екранів продаючої частини
# (311, 312, 313, 302, 303, 304, 305 у деці на 22.09 09:30) перед 171 («Сайт готов и опубликован»).
import json,copy
p='source/overrides.json'; o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
P=va['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
IDX=[75,76,77,66,67,68,71]  # 22.09 виправлено: були не ті (311-313,302-305), треба 337-339,328-330,333 (нумерація на 22.09 09:45)
oid='g3f9b3adf0b8_0_2950'; s=va[oid]
s.pop('presentationParts',None)  # перезапис попередньої вставки
AUTH='Мирослав 22.09.2026: після слайда 170 додати екрани 311, 312, 313, 302, 303, 304, 305 (копії з продаючої частини), далі 171.'
parts=[{'note':'Часть 1: сам слайд «Сотни часов и куча денег».\nGoogle Slides · '+oid}]
for i in IDX:
    src=P[i]
    part={k:copy.deepcopy(src[k]) for k in ('t','b','lv','k','a','mvp','foundation','salesV6Label','salesV6Source') if k in src}
    part.setdefault('k','')  # не успадковувати eyebrow батька
    part['note']='Копия экрана продающей части (part idx %d) — вставлено после слайда 170.\n'%i+(src.get('note') or '')
    parts.append(part)
s['presentationParts']={'sourceGoogleObjectId':oid,'authorization':AUTH.replace('311, 312, 313, 302, 303, 304, 305','337, 338, 339, 328, 329, 330, 333'),'allowPartTitles':True,'mediaStatus':'ready','slides':parts}
s['reason']=(s.get('reason') or '')+' | 22.09 Мирослав: після цього слайда 7 екранів з продаючої частини (AI-сайты: услуга 1/7, агент, 1000+ шаблонов; Антон Тысячник; что собирает; посчитаем; а что после).'
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('patched',len(parts)-1,'parts')
