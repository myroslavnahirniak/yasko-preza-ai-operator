# 16.09 · 179 «И под каждую есть свои сотрудники» → 4 слайди по 2 агенти (варіант А, дві картки з результатом), 180 «Сейчас ещё сделаем несколько услуг» → 4 картки 2×2 (варіант А). Повний текст джерела збережено.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
I={'hunt':'<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4M11 8v6M8 11h6"/>','chat':'<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>','site':'<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 9h18M8 18v3M16 18v3"/>','design':'<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 12h16M12 12v8"/>','video':'<rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/>','content':'<path d="M4 20h16M6 16l10-10 2 2L8 18H6z"/>','ads':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>','seo':'<circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-4 2 2-6z"/>'}
ic=lambda k:'<svg class="s16-ico" viewBox="0 0 24 24" aria-hidden="true">'+I[k]+'</svg>'
V='assets/vlad-1409/video/'
def vid(n,fit=False):return '<div class="s16-media'+(' fit' if fit else '')+'"><video src="'+V+n+'.mp4" poster="./'+V+n+'-poster.jpg" muted playsinline loop preload="metadata"></video></div>'
def img(src,light=False,alt=''):return '<div class="s16-media'+(' light' if light else '')+'"><img src="'+src+'" alt="'+alt+'"></div>'
def fan(srcs):return '<div class="s16-media s16-fan">'+''.join('<img src="'+s+'" alt="">' for s in srcs)+'</div>'
A=[('AI-Охотник','ищет клиентов','hunt',img('assets/gen-164-213/s179-hunter-map.webp',alt='Карта с найденными клиентами')),
 ('AI-Продавец','ведёт до оплаты','chat',vid('tg-seller-voice',True)),
 ('AI-Сайты','сайты под ключ','site',fan(['assets/vlad-1409/brands/zarmilkas.webp','assets/vlad-1409/brands/maesta.webp','assets/vlad-1409/brands/bioswiss.webp'])),
 ('AI-Дизайн','КП, баннеры, макеты','design',vid('dizayn')),
 ('AI-Видео','ролики с аватаром','video',vid('avatar-1')),
 ('AI-Контент','посты и рилз','content',img('assets/vlad-1409/uslugi/kontent-dash.jpg',True,'Панель клиента')),
 ('AI-Таргет','реклама и связки','ads',img('assets/vlad-1409/uslugi/target-github.jpg',True,'Код агента-рекламщика')),
 ('AI-Видимость','выдача в нейросетях','seo',vid('ai-seo-reel'))]
def part(pi):
    a,b=A[pi*2],A[pi*2+1]
    cards=''.join('<div class="s16-tcard">'+x[3]+'<div class="s16-txt">'+ic(x[2])+'<div><b>'+x[0]+'</b><small>'+x[1]+'</small></div></div></div>' for x in (a,b))
    prog='<div class="s16-progress" aria-hidden="true">'+''.join('<i class="'+('on' if i//2==pi else 'done' if i//2<pi else '')+'"></i>' for i in range(8))+'</div>'
    body='<p class="s16-sub">Ваша команда · 8 задач · <b>'+str(pi*2+1)+'–'+str(pi*2+2)+'</b></p><div class="s16-team">'+cards+'</div>'+prog
    return {'b':body,'foundation':{'block129':{'kind':'s16','v2':True,'layout':'s16-team','eyebrow':'Пять отделов'},'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'layout':'s16-team','mediaBrief':'Слайд '+str(pi+1)+' из 4: два агента з реальним результатом (зіпка Влада: '+a[0]+' + '+b[0]+').','animationBrief':'Дві картки з’являються по черзі; відео результату грає; смужка команди показує позицію 1–8.'}}
oid='g409d4d20be6_0_43'; s=va[oid]
s['reason']='16.09 Мирослав (голосове): показати результат кожного агента; розбити на 4 слайди по 2 агенти; обрано варіант А «дві картки з результатом». Повний текст джерела (заголовок, «Ваша команда · 8 задач», 8 агентів із задачами) збережено на всіх чотирьох.'
s['mediaStatus']='ready'
s['presentationParts']={'sourceGoogleObjectId':oid,'authorization':'Прямий запит Мирослава 16.09.2026 (голосове повідомлення в сесії): розбити «И под каждую есть свои сотрудники» на 4 слайди по 2 агенти з візуалізацією результату; після сторінки варіантів обрано «179 - А варіант».','allowPartTitles':False,'mediaStatus':'ready','slides':[part(i) for i in range(4)]}
s['set']['b']=part(0)['b']
f=s.setdefault('foundation',{});f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'layout':'s16-team'});f.pop('variant',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-team','eyebrow':'Пять отделов'}
# 180
oid2='g3f9b3adf0b8_0_1536'; s2=va[oid2]
R=[('01','продавец в переписке и по телефону (AI-продавец)',vid('tg-seller-voice',True)),
 ('02','рекламное видео с моим лицом (AI-Контент)',vid('avatar-1')),
 ('03','рекламные объявления (AI-дизайнер)','<div class="s16-media s16-ph"><div>рекламные объявления · визуал позже</div></div>'),
 ('04','реклама в соц сетях (AI-таргет)',img('assets/vlad-1409/uslugi/target-github.jpg',True,'Код агента-рекламщика'))]
s2['reason']='16.09 Мирослав: візуалізувати кожен пункт (як буде виглядати); обрано варіант А «чотири картки 2×2». 01/02/04 — ассети з зіпки Влада, 03 — місце під візуал (підставить Мирослав). Повний текст джерела.'
s2['mediaStatus']='ready'
s2['set']['b']='<div class="s16-four">'+''.join('<div class="s16-fcard">'+m+'<div class="s16-txt"><span class="s16-n">'+n+'</span><span>'+t+'</span></div></div>' for n,t,m in R)+'</div>'
f2=s2.setdefault('foundation',{});f2.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'layout':'s16-four','mediaBrief':'Чотири картки з результатом: чат продавця, ролик з аватаром, місце під рекламні оголошення, код агента-рекламника.','animationBrief':'Картки з’являються по черзі; відео грають.'});f2.pop('variant',None)
f2['block129']={'kind':'s16','v2':True,'layout':'s16-four'}
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched',oid,oid2)
