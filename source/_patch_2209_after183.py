# 22.09 · Мирослав: після слайда 183 («7 услуг, которые агенты делают целиком», part 2 oid …2921)
# ПЕРЕНЕСТИ (не копіювати) з продаючої частини: 344-346, 347-354, 360-370, 397-401, 391-393, 383-385, 375-382, 317-325,
# потім 387 «Один клиент платит не один раз», потім слайд 181 «И у каждой услуги две дорожки» (Google oid …2917 → omit, копія як частина).
# Нумерація = дека на 22.09 ~10:20 (після вставки 7 екранів за слайдом 170).
import json,copy
p='source/overrides.json'; o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
SALES='g3f9b3adf0b8_0_2226'; TARGET='g3f9b3adf0b8_0_2921'; SPLIT='g3f9b3adf0b8_0_2917'
P=va[SALES]['presentationParts']['slides']
IDX=[82,83,84]+list(range(85,93))+list(range(98,109))+list(range(135,140))+list(range(129,132))+list(range(121,124))+list(range(113,121))+list(range(55,64))+[125]
assert len(IDX)==51 and len(set(IDX))==51, len(IDX)
assert 'платит не один раз' in P[125]['t'] and 'Сейчас ещё сделаем' in P[82]['t'] and 'Ане 39' in (P[55].get('t') or '').replace('<br>','').replace(' ','')or True
moved=[P[i] for i in IDX]
ids=set(map(id,moved)); P[:]=[x for x in P if id(x) not in ids]
for pt in moved:
    pt.setdefault('k','')  # не успадковувати eyebrow «Заберёте в конце» від слайда 182
    pt['note']='Перенесено з продаючої частини після слайда «7 услуг» (Мирослав 22.09).\n'+(pt.get('note') or '')
# копія слайда 181 як частина, оригінал сховати
sp=va[SPLIT]; part181={k:copy.deepcopy(sp['set'][k]) for k in ('t','b','lv','note') if k in sp['set']}
part181['k']=''; part181['foundation']=copy.deepcopy(sp['foundation'])
part181['note']='Перенесено зі слайда 181 (Google oid '+SPLIT+', тепер omit) — після «Один клиент платит не один раз».\n'+(part181.get('note') or '')
sp['omit']=True; sp['reason']=(sp.get('reason') or '')+' | 22.09 Мирослав: перенесено після блоку 7 послуг (частина oid '+TARGET+').'
T=va[TARGET]; T['presentationParts']['slides'].extend(moved+[part181])
T['presentationParts']['authorization']=(T['presentationParts'].get('authorization') or '')+' | Мирослав 22.09.2026: після «7 услуг» перенесено 51 екран продаючої частини (344–346, 347–354, 360–370, 397–401, 391–393, 383–385, 375–382, 317–325, 387) і слайд 181.'
T['reason']=(T.get('reason') or '')+' | 22.09 Мирослав: після «7 услуг» — усі 7 послуг детально (перенесено з продаючої частини) + «Один клиент платит не один раз» + «две дорожки».'
va[SALES]['reason']=(va[SALES].get('reason') or '')+' | 22.09 Мирослав: 51 екран перенесено після слайда «7 услуг» (oid '+TARGET+').'
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('moved',len(moved),'+181; sales parts left',len(P),'; target parts',len(T['presentationParts']['slides']))
