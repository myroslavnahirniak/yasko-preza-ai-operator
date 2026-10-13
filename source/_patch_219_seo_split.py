# 21.09 · слайд 219 «Чтобы ваш сайт советовал ChatGPT» (Google 232, g409d4d20be6_0_398) → 4 підслайди (presentationParts):
# 1 шлях людини (3D-картки по кроках, s16-path); 2–4 кроки агента з артом GPT Image 2.5 (s16-visual), 4-й з висновком і ціною.
# Запуск: python3 source/_patch_219_seo_split.py → FOUNDATION_SOURCE=google-2026-09-16/foundation-source-v2.json python3 source/_foundation_prepare.py && python3 source/_build_slides.py
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
OID='g409d4d20be6_0_398'; A='assets/gen-219/'
def fnd(layout,extra,brief,anim):
    bl={'kind':'s16','v2':True,'layout':layout}; bl.update(extra)
    return {'block129':bl,'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'layout':layout,'mediaBrief':brief,'animationBrief':anim}
def part(t,b,f,note): return {'t':t,'b':b,'lv':6,'note':note+'\nGoogle Slides #1232 · '+OID}
parts=[]
# 1 · шлях людини
s=part('Как теперь <em>ищут бизнес</em>',
 '<p class="s16-caption">Три шага — и клиент уже на сайте</p>'
 '<div class="s16-pathwrap"><div class="s16-tilt">'
 '<div class="s16-pc a"><i>01</i><b>Человек спрашивает</b><span>у ChatGPT, Gemini или Perplexity: где купить, кого выбрать</span></div>'
 '<div class="s16-pc b"><i>02</i><b>Нейросеть отвечает</b><span>и называет сайт вашего клиента</span></div>'
 '<div class="s16-pc c"><i>03</i><b>Человек приходит</b><span>уже готовый, его не надо уговаривать</span></div>'
 '</div></div>',None,'Частина 1 з 4: шлях людини.')
s['foundation']=fnd('s16-path',{'eyebrow':'Услуга 7 из 7 · AI-SEO','steps':['Человек спрашивает','Нейросеть отвечает','Человек приходит']},'Три картки шляху у 3D, з’являються по кроках.','Крок = картка; hover — нахил за курсором.')
parts.append(s)
# 2–4 · кроки агента
STEPS=[
 ('Шаг 1 из 3 · что делает агент','Видит ли сайт <em>нейросеть</em>','Очень часто сайт для неё закрыт — тогда он не попадёт в ответ никогда','s219b-gate.webp','Сайт за зачиненими воротами, око нейромережі зовні.'),
 ('Шаг 2 из 3 · что делает агент','Страницы <em>под вопросы людей</em>','Нейросеть берёт готовый ответ с первых строк, а не рассказ компании о себе','s219c-pages.webp','Дві сторінки: тьмяна «о компании» → яскрава з відповіддю у першому рядку.'),
 ('Шаг 3 из 3 · что делает агент','Каждый месяц <em>проверяет результат</em>','Задаёт нейросетям одни и те же вопросы и считает, назвали вас или нет','s219d-months.webp','Стрічка місяців із жовтими галочками, що яскравішають.'),
]
for i,(eb,t,lead,img,brief) in enumerate(STEPS):
    b='<p class="s16-lead">'+lead+'</p>'
    if i==2: b+='<div class="s16-bottom"><p class="s16-claim">Рекламу в ChatGPT купить можно. А место в самом ответе — нет</p><span class="s16-price">$500 · в месяц · сложность средняя</span></div>'
    s=part(t,b,None,'Частина %d з 4: крок агента.'%(i+2))
    s['foundation']=fnd('s16-visual',{'eyebrow':eb,'art':[{'src':A+img,'alt':''}]},brief,'Поява тексту одним рухом; арт статичний.')
    parts.append(s)
s=va.get(OID) or {}
s['reason']='21.09 Мирослав: слайд нечитабельний — розбито на 4 підслайди (шлях людини + 3 кроки агента з візуалізацією GPT Image 2.5), текст джерела збережено повністю.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
    if k not in rm: rm.append(k)
s.setdefault('set',{})
s['presentationParts']={'sourceGoogleObjectId':OID,'authorization':'Прямий запит Мирослава 21.09.2026 у сесії: «wir müssen diese Folie in Unterfolien aufteilen und lesbarer machen … З 3D візуалізацією» → «давай» на пропозицію з 4 підслайдів.','allowPartTitles':True,'mediaStatus':'ready','slides':parts}
va[OID]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched',OID,len(parts),'parts')
