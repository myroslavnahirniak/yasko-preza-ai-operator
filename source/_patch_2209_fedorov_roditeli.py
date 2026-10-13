# 22.09 · правки Влада: (1) після 59 «информационная война» — скрин переписки з Фёдоровим (2 частини); (2) після 70 «Смерть меня тогда не пугала» — фото батьків, потім відео (3 частини); (3) Секрет 02: «продать» замість «сдать».
import json,copy
p='source/overrides.json'; o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']; life=o['__lifeStory']['slides']
AUTH='Правка Влада 22.09.2026 (через Мирослава): «После слайда про информационную войну добавить скрин переписки с Федоровым»; «После этого слайда [Смерть меня тогда не пугала] нужно добавить еще слайд, где фото до родителей моих и после видоса»; «как продать, а не как сдать».'
def part(base_life,**kw):
    l=copy.deepcopy(base_life); l.update(kw); return l
# --- 59 · Фёдоров
oid='g3fadf66108e_0_441'; s=va.setdefault(oid,{}); L=life[oid]
fed=part(L,variant='portrait-pair',titleSize=3.8,quiet=True,
 photos=[{'src':'assets/photo/vlad/fedorov-chat.jpg','width':979,'height':701,'role':'evidence','fit':'contain'},
         {'src':'assets/photo/vlad/fedorov-card.jpg','width':1147,'height':863,'role':'evidence','fit':'contain'}],
 sourceMediaNotes='Скрин переписки с Михаилом Фёдоровым и карточка «кто это»; текст скринов не дублируется.')
s['presentationParts']={'sourceGoogleObjectId':oid,'authorization':AUTH,'allowPartTitles':False,'mediaStatus':'ready','slides':[
 {'note':'Часть 1: пост «Сигнал» + Россия 1.\nGoogle Slides #59 · '+oid},
 {'b':'','lifeStory':fed,'note':'Часть 2: переписка с Фёдоровым — задачи приходили напрямую. Скрин говорит сам, текст не читать.\nGoogle Slides #59 · '+oid}]}
s['reason']=(s.get('reason') or '')+' | 22.09 Влад: добавлен скрин переписки с Фёдоровым второй частью.'
# --- 70 · родители: фото → відео
oid='g3fadf66108e_0_535'; s=va.setdefault(oid,{}); L=life[oid]
foto=part(L,variant='wide',titleSize=4.2,quiet=True,quoteAccent=None,quoteNewLine=None,quoteBreakBefore=None,
 photos=[{'src':'assets/photo/vlad/roditeli.jpg','width':1280,'height':800,'role':'photo','fit':'contain'}],
 sourceMediaNotes='Свадебное фото родителей Влада.')
vid=part(L,variant='wide',titleSize=4.2,quiet=True,quoteAccent=None,quoteNewLine=None,quoteBreakBefore=None,photos=[],
 video={'src':'assets/video/roditeli.mp4','poster':'assets/video/roditeli-poster.jpg'},sourceMediaNotes='Видео родителей (12 с).')
for d in (foto,vid):
    for k in ('quoteAccent','quoteNewLine','quoteBreakBefore'): d.pop(k,None)
s['presentationParts']={'sourceGoogleObjectId':oid,'authorization':AUTH,'allowPartTitles':False,'mediaStatus':'ready','slides':[
 {'note':'Часть 1: кошелёк и таблетки.\nGoogle Slides #70 · '+oid},
 {'b':'','lifeStory':foto,'remove':['bg'],'note':'Часть 2: фото родителей.\nGoogle Slides #70 · '+oid},
 {'b':'','lifeStory':vid,'note':'Часть 3: видео родителей.\nGoogle Slides #70 · '+oid}]}
s['reason']=(s.get('reason') or '')+' | 22.09 Влад: после слайда — фото родителей, затем видео.'
# --- 135 · продать, а не сдать
oid='g3fadf66108e_0_1531'; s=va[oid]
b=s['set']['b']; assert 'Как сдать клиенту работу' in b
s['set']['b']=b.replace('Как сдать клиенту работу','Как продать клиенту работу')
s['reason']=(s.get('reason') or '')+' | 22.09 Влад: «как продать, а не как сдать».'
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('patched 3 slides')
