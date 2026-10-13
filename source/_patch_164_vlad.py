# 16.09 · патч блоку 164–169 + матеріали Влада (відео/артефакти). Адресні правки overrides.__visibleGoogleAudit.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
R='16.09 Мирослав: блок 164–169 + матеріали Влада від 14.09 (відео, артефакти Claude). Повний текст збережено.'
G='assets/gen-164-213/'; V='assets/video/vlad-1409/'; A='assets/artifacts-1409/'
def slide(oid,t,b,layout,artv=None,eyebrow=None,extra=None):
    s=va.get(oid) or {}
    s['reason']=R; s['mediaStatus']='ready'
    rm=s.setdefault('remove',[])
    for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
        if k not in rm: rm.append(k)
    st=s.setdefault('set',{}); st['t']=t; st['b']=b
    f=s.setdefault('foundation',{})
    f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False})
    f.pop('variant',None); f.pop('layout',None)
    bl={'kind':'s16','v2':True,'layout':layout}
    if artv: bl['art']=artv
    if eyebrow: bl['eyebrow']=eyebrow
    if extra: bl.update(extra)
    f['block129']=bl; va[oid]=s
ICONS=['<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>','<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6M15 15c3 0 6 1.5 6 5"/>','<path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/>','<path d="M4 19V5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zm0 0a2 2 0 0 0 2 2h13"/>','<circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h4a1.5 1.5 0 0 1 0 3h-3a1.5 1.5 0 0 0 0 3h4"/>','<path d="M4 20h16M6 16l10-10 2 2L8 18H6z"/>','<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M8 9h8M8 13h5"/><circle cx="16" cy="14" r="1"/>','<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 9h18M8 18v3M16 18v3"/>','<rect x="3" y="5" width="13" height="10" rx="1.5"/><rect x="17" y="8" width="4" height="9" rx="1"/><path d="M6 19h7"/>','<path d="M12 16V4M7 9l5-5 5 5M4 20h16"/>','<path d="M4 6h16v12H4zM4 10h16"/><circle cx="8" cy="8" r=".8"/>','<path d="M12 3l2.5 5 5.5.8-4 3.9.9 5.5-4.9-2.6L7.1 18.2l.9-5.5-4-3.9L9.5 8z"/>','<path d="M15 10l4.5-2.5v9L15 14M4 7h11v10H4z"/>','<path d="M9 18V6l11 6z"/><path d="M3 5v14"/>','<path d="M12 21c-4 0-7-3-7-7 0-3 2-5 4-6l3-4 3 4c2 1 4 3 4 6 0 4-3 7-7 7z"/>','<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>','<path d="M4 4h16v12H4zM8 20h8M12 16v4"/>','<path d="M3 12h18M12 3v18"/><circle cx="12" cy="12" r="9"/>']
def icon(i): return '<svg viewBox="0 0 24 24" aria-hidden="true">'+ICONS[i%len(ICONS)]+'</svg>'
def iconlist(items,one=False,start=0): return '<div class="s16-list'+(' one' if one else '')+'">'+''.join('<div>'+icon(start+i)+'<span>'+x+'</span></div>' for i,x in enumerate(items))+'</div>'
def demo(name,url): return '<div class="s16-demo"><iframe src="'+A+name+'.local.html" title="Демо агента" loading="lazy"></iframe></div><p class="s16-demo-link">Живое демо · <a href="'+url+'" target="_blank" rel="noopener">'+url.replace('https://','')+'</a></p>'
def steps2(a,b,names=('Что делает агент','Живое демо агента')): return '<div class="s16-step">'+a+'</div><div class="s16-step">'+b+'</div>'
STEPS2={'steps':['Что делает агент','Живое демо агента'],'focus':'.s16-step'}
def player(src,cap,sound=True,poster=None): return '<div class="s16-player"><video src="'+src+'" playsinline preload="metadata"'+(' poster="'+poster+'"' if poster else '')+'></video></div>'+('<p class="s16-cap">'+cap+'</p>' if cap else '')
stg=[('Рецепт','изучает нишу и соседей','st-recipe'),('Замес','строит структуру, которая продаёт','st-mix'),('Сборка','пишет тексты, ставит блоки','st-assemble'),('Украшение','доводит до готовой ссылки','st-decorate')]
# 164
b='<div class="s16-vid" aria-hidden="true">'+''.join(f'<img src="{G}{f}.webp" alt="">' for _,_,f in stg)+'</div><div class="s16-stg">'+''.join(f'<div><b>{n}</b><small>{d}</small></div>' for n,d,_ in stg)+'</div><div class="s16-bottom"><p>Никто не печёт весь торт. Каждый делает свой этап и передаёт дальше</p></div>'
slide('g409d4d20be6_0_314','Разбить на этапы. На каждый — свой <em>мастер</em>',b,'s16-stages',eyebrow='Конвейер',extra={'segment':3})
# 165
lay=[('Инструкция','что делает, шаг за шагом'),('Как можно','примеры работ, на которые равняется'),('Как нельзя','ошибки, которые он уже совершил'),('Проверка','по чему понимает, что этап готов'),('Передача','что и кому отдаёт дальше')]
b='<div class="s16-lay">'+''.join(f'<div><b>{i+1:02d}</b><div><span>{n}</span><small>{d}</small></div></div>' for i,(n,d) in enumerate(lay))+'</div><div class="s16-bottom"><p>Уберите эти слои — и останется обычный чат</p></div>'
slide('g409d4d20be6_0_318','Мастера не нанимают.<br>Его <em>собирают</em>',b,'s16-layers',[{'src':G+'s165-layers.webp','alt':'Пять слоёв мастера'}],eyebrow='Что внутри одного мастера · один мастер — один этап')
# 166
b='<div class="s16-mx">'+''.join(f'<div><img src="{G}{f}.webp" alt=""><b>{n}</b>'+''.join(f'<i>{x}</i>' for x in ['инструкция','как можно','как нельзя','проверка','передача'])+'</div>' for n,_,f in stg)+'</div><div class="s16-bottom"><p>Пять слоёв × четыре этапа — и это только один торт</p><p class="s16-lead">Внутри каждого агента — часы работы и обучения на каждый этап</p></div>'
slide('g409d4d20be6_0_322','А это был всего <em>один</em> мастер',b,'s16-matrix')
# 167
slide('g3f9b3adf0b8_0_2950','Сотни часов и куча денег.<br><em>Мои, не ваши</em>','<div class="s16-bottom"><p>Один такой агент — это больше ста часов моей работы: пишешь, ломаешь, смотришь, где он ошибся, переписываешь. И так по каждому.</p><p class="s16-lead">Вам его собирать не надо. Он уже собран</p></div>','s16-vlad',[{'src':G+'s167-vlad.webp','alt':'Влад ночью за работой над агентами'}],eyebrow='Сколько это стоило')
# 168
items=[('Сайт','который продаёт','s168-site'),('Лендинг','который продаёт','s168-landing'),('Квиз','сам квалифицирует заявку','s168-quiz'),('Формы','вечер вместо недель','s168-forms'),('Аналитика','вечер вместо недель','s168-analytics'),('Домен','вечер вместо недель','s168-domain')]
b='<div class="s16-grid">'+''.join(f'<div class="s16-item"><img src="{G}{f}.webp" alt=""><b>{n}</b><small>{d}</small></div>' for n,d,f in items)+'</div><div class="s16-bottom"><span class="s16-price">$250–$1.200 · за пакет · сложность лёгкая</span><p>call-summary-landing.vercel.app — собран агентом за вечер</p></div>'
slide('g3f9b3adf0b8_0_2876','AI-сайты, которые <em>приводят клиентов</em>',b,'s16-items',eyebrow='Услуга 1 из 8',extra={'steps':[n for n,_,_ in items],'focus':'.s16-item'})
# 169 + демо агента по сайтам
it169=['Изучает конкурентов','Изучает аудиторию, кому продавать','Создаёт маркетинговую стратегию','Обучен на лучших методиках мира','Создал сайты, на которые уже было потрачено больше 100 000 долларов рекламного бюджета','Пишет продающие тексты','Создаёт интерактивные опросники','У него есть база 100+ сайтов с разным готовым дизайном','Разрабатывает сайт, адаптирует под мобильные устройства и компьютер','Размещает и публикует']
slide('g409d4d20be6_0_13','Что делает агент <em>по сайтам</em>',steps2(iconlist(it169),demo('sites','https://claude.ai/code/artifact/d511a5b9-d00f-4588-9ba0-a32a1e40addb')),'s16-icons',extra=STEPS2)
# 190 AI-дизайн
slide('g3fa86c6f413_2_0','Что делает <em>агент</em>',steps2(iconlist(['анализирует аудиторию','знает, куда ведём','вызывает сценариста','фотограф','дизайнер'],one=True,start=1),demo('design','https://claude.ai/code/artifact/25d0fb2d-1bf4-42e8-a311-4dcc8dc00155')),'s16-icons',eyebrow='AI-дизайн',extra=STEPS2)
# 194 Продающие AI-видео: картка + ролик Влада «ИИ Видео»
card='<div class="s16-list">'+''.join(f'<div><b>{n}</b>{d}</div>' for n,d in [('Товары','ролик под карточку и под рекламу'),('Одежда','модель в кадре создана нейросетью'),('Услуги и клиники','показать, как всё проходит'),('Офлайн-объекты','показать помещение, которого ещё нет')])+'</div><div class="s16-bottom"><span class="s16-price">$300–$1.200 · за пакет 8–12 роликов</span><p>В кадре не актёр. Никто не приезжал на площадку</p></div>'
slide('g409d4d20be6_0_105','Продающие <em>AI-видео</em>','<div class="s16-step">'+card+'</div><div class="s16-step">'+player(V+'ai-video-showreel-1080.mp4','Ролики, собранные AI-агентом · 42 с')+'</div>','s16-video',eyebrow='Услуга 3 из 7',extra={'steps':['Что выходит из агента','Примеры роликов'],'focus':'.s16-step','sound':True})
# 198 AI-видео агент
slide('g3fa86c6f413_2_3','Что делает <em>агент</em>',steps2(iconlist(['анализирует аудиторию','ищет лучшие идеи','пишет сценарий','раскадровка','фотограф','съёмка видео','звук','монтаж'],start=1),demo('video','https://claude.ai/code/artifact/6dd9fa9b-288a-4523-bd64-d512c7a9f537')),'s16-icons',eyebrow='AI-видео',extra=STEPS2)
# 199 Женя — відео Влада
slide('g409d4d20be6_0_112','А вот этого агента взял <em>Женя</em>',player(V+'reel-ai-agent-ru.mp4','Видео от Влада: AI-агент «Реклама недвижимости» · 1:02'),'s16-video',extra={'sound':True})
# 206 Контент-завод
slide('g3fa86c6f413_2_22','Что делает <em>агент</em>',steps2(iconlist(['ищет лучшие идеи','создаёт контент-план','подключает AI-аватара','делает Reels / Shorts / TikTok','посты в Telegram','карусели','сторис','выкладывает сам'],start=11),demo('content','https://claude.ai/code/artifact/40ca3191-8830-4a8a-9822-e9eacc46f0f4')),'s16-icons',eyebrow='Контент-завод',extra=STEPS2)
# 209 Автомонтаж — до/після
slide('g409d4d20be6_0_191','Автомонтаж старых видео <em>за 10 минут</em>','<div class="s16-pair"><div><video src="'+V+'montage-before-1080.mp4" muted playsinline loop preload="metadata"></video><span>До</span></div><div class="after"><video src="'+V+'montage-after-1080.mp4" muted playsinline loop preload="metadata"></video><span>После</span></div></div><p class="s16-cap">ИИ-агент Reelo · instagram.com/reels/DdEbBEbR7Hn</p>','s16-ba')
# 216 AI-продавец
slide('g3fa86c6f413_2_9','Что делает <em>агент</em>',steps2(iconlist(['изучает, что продаётся','знает лучшие техники продаж','пишет сценарий','живёт в мессенджерах 24/7','отвечает клиентам','умеет отправлять голосовые и видеосообщения','принимает оплату','напоминает, если клиент забыл','помнит историю каждого клиента','ведёт учёт клиентов для собственника'],start=3),demo('seller','https://claude.ai/code/artifact/8eea5290-28be-4b3f-8da4-5ca443ef5b47')),'s16-icons',eyebrow='AI-продавец',extra=STEPS2)
# 221 Реклама в Instagram — одразу демо
slide('g409d4d20be6_0_380','Реклама <em>в Instagram</em>','<div class="s16-step is-focus">'+demo('ads','https://claude.ai/code/artifact/14b143ae-adce-474c-bac0-3c1fbedef5d0')+'</div>','s16-icons')
# 225 AI-SEO · клієнти — рілс
slide('g409d4d20be6_0_501','AI-SEO · <em>Клиенты</em>',player(V+'ai-seo-reel-1080.mp4','Видео от Влада: AI-SEO — клиенты · 33 с'),'s16-video',extra={'sound':True})
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched', sum(1 for v in va.values() if v.get('reason')==R))
