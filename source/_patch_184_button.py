# 21.09 · слайд 184 «Одной кнопкой окажу услуг ещё примерно на $1500» (Google 195, g409d4d20be6_0_480): варіант Б — кнопка + 4 предмети, підписи живим текстом, 6 станів. Повний текст джерела.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_480'; img='assets/gen-184-188/s184-button.webp'
ROWS=[('AI-продавец','от $500'),('рекламное видео с моим лицом','от $250'),('рекламные объявления','от $250'),('реклама в соц сетях','от $500')]
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: варіант Б — жовта кнопка в центрі, від неї промені до чотирьох предметів (GPT Image 2.5); підписи з цінами біля предметів по кроках, підсумок під кнопкою. Суми як у джерелі.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='Одной кнопкой окажу услуг ещё примерно на <em>$1500</em>'
st['b']=''.join(f'<div class="s16-glow g{i+1}"></div>' for i in range(4))+''.join(f'<div class="s16-cap c{i+1}"><b>{r[0]}</b><i>{r[1]}</i></div>' for i,r in enumerate(ROWS))+'<div class="s16-total"><span>Итого</span><em>$1500</em></div>'
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'mediaBrief':'Кнопка «пуск» і чотири предмети (телефон з чатом, телефон на штативі, стос макетів, планшет із рупором); підписи з цінами, підсумок.','animationBrief':'Заголовок → чотири підписи по кроках (предмет підсвічується) → підсумок $1500.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-onebutton','art':[{'src':img,'alt':'Жёлтая кнопка и четыре предмета: телефон с чатом, телефон на штативе, стопка макетов, планшет с рупором'}],'steps':['Заголовок','AI-продавец','Видео с моим лицом','Рекламные объявления','Реклама в соцсетях','Итого']}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched',oid)
