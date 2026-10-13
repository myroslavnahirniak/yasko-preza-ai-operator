# 16.09 · слайд 176 «АГЕНТ» (Google 190, g3f9b3adf0b8_0_1528): чат ефіру зліва + пульт демо справа. Повний текст джерела збережено.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_1528'
s=va.get(oid) or {}
s['reason']='16.09 Мирослав: кодове слово — слово та інструкція зверху, зліва живий чат ефіру (набір «агент», повідомлення глядачів), справа скрин пульта демо із зіпки Влада з авто-прокруткою. Повний текст джерела.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='<em>АГЕНТ</em>'
st['k']='Ловите кодовое слово'
msgs=[('me',3.3,'агент'),('',4.0,'агент'),('',4.55,'Агент'),('',5.1,'агент'),('',5.65,'АГЕНТ'),('',6.2,'агент'),('',6.75,'агент'),('',7.3,'Агент')]
chat=''.join(f'<div class="s16-msg{" "+c if c else ""}" style="--d:{d:.2f}s"><i></i><span>{t}</span></div>' for c,d,t in msgs)
st['b']=('<p class="s16-sub">Пишите «агент» в чат — заберёте его в конце эфира вместе со ссылкой</p>'
 '<div class="s16-chat" aria-hidden="true"><div class="s16-msgs">'+chat+'</div>'
 '<div class="s16-input"><div class="s16-txt"><span>агент</span><b></b></div><div class="s16-send"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></div></div></div>'
 '<div class="s16-frame"><img src="assets/vlad-1409/pult/pult-7-knopok-column.png" alt="Пульт демо — от сайта до клиентов"></div>')
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'mediaBrief':'Чат ефіру зліва, пульт демо (зіпка Влада, колонка) справа.','animationBrief':'Літери слова, набір «агент» у полі, повідомлення глядачів по черзі; пульт повільно прокручується.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-codeword','eyebrow':'Ловите кодовое слово'}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched',oid)
