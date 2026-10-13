# 21.09 · слайд 177 «Это была одна услуга из 7» (Google 191, g3f9b3adf0b8_0_1543): фон — сім вітрин (А1, GPT Image 2.5), текст зверху. Повний текст джерела збережено.
import json,sys
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_1543'
img=sys.argv[1] if len(sys.argv)>1 else 'assets/gen-164-213/s177-seven-showcases-a.webp'
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: AI-фон (сім вітрин, перша світиться — сайт, у решті предмети інших шести послуг) + текст зверху одним стовпчиком. Повний текст джерела.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='Это была <em>одна услуга из 7</em>'
st['b']='<div class="s16-text"><p>Сайт — самая понятная.</p><p>Но точно так же AI-агенты закрывают ещё 6</p><p class="s16-final">И каждую бизнес покупает отдельно</p></div>'
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'mediaBrief':'Сім вітрин у ряд, перша світиться (сайт), у решті — предмети шести інших послуг; текст зверху.','animationBrief':'Текст рядками, фон повільно наближається (Ken Burns).'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-seven','art':[{'src':img,'alt':'Семь витрин: сайт и ещё шесть услуг'}]}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched',oid,img)
