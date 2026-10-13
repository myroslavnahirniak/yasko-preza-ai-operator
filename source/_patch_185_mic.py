# 21.09 · слайд 185 «Каждая следующая услуга … одна короткая команда ртом» (Google 196, g409d4d20be6_0_49): фон — мікрофон (варіант А), без анімації. Повний текст джерела.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_49'; img='assets/gen-184-188/s185-mic.webp'
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: варіант А — фон-мікрофон із жовтою хвилею (GPT Image 2.5), текст по центру зверху, без анімації фону.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='Каждая следующая услуга, которую я сейчас буду показывать — <em>одна короткая команда ртом</em>'
st['b']=''
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'mediaBrief':'Мікрофон на темному столі, перед решіткою коротка жовта хвиля; текст зверху по центру.','animationBrief':'Лише поява тексту; фон статичний.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-statement','art':[{'src':img,'alt':'Микрофон и короткая звуковая волна'}]}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched',oid,img)
