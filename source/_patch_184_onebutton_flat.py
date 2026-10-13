# 21.09 · слайд 184 «Одной кнопкой окажу услуг ещё примерно на $1500» (g409d4d20be6_0_480): Мирослав — прибрати підкроки
# (там нічого не відбувалось), усі підписи й «Итого» видно одразу; підпис «рекламное видео» піднято (CSS .s16-cap.c2 top 47.5cqh).
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(ROOT,'source/overrides.json'); o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_480'
s=va[oid]; b=s['foundation']['block129']
b.pop('steps',None); b.pop('focus',None)
s['reason']=(s.get('reason','')+' 21.09 Мирослав: підкроки прибрано — усі підписи одразу (каскад на вході); підпис «рекламное видео» піднято над планшет.').strip()
s['foundation']['animationBrief']='Підписи з’являються каскадом за секунду, далі статична композиція; кроків немає.'
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('patched',oid,'steps:',b.get('steps'))
