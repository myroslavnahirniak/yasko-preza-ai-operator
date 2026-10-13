# 21.09 · слайди 188–191 за вибором Мирослава: 188 В (віяло, текст зверху), 189 А (КП по центру, 2 кроки), 190 C (3D-полиця + hover), 191 А (кіно-кадр, відео IMG_7847, клік — на весь слайд). Повний текст джерела.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
D='assets/vlad-1409/dizayn/'
def base(oid,reason,t,b,layout,extra=None,brief='',anim=''):
    s=va.get(oid) or {}
    s['reason']=reason; s['mediaStatus']='ready'
    rm=s.setdefault('remove',[])
    for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
        if k not in rm: rm.append(k)
    st=s.setdefault('set',{}); st['t']=t; st['b']=b; st['lv']=6
    f=s.setdefault('foundation',{})
    f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'mediaBrief':brief,'animationBrief':anim})
    f.pop('variant',None); f.pop('layout',None)
    bl={'kind':'s16','v2':True,'layout':layout}; bl.update(extra or {}); f['block129']=bl
    va[oid]=s; print('patched',oid,layout)
# 188 · На выходе — рекламные объявления (g409d4d20be6_0_68)
base('g409d4d20be6_0_68','21.09 Мирослав: варіант В — три креативи (вирізані зі скрина Google, апскейл) віялом у 3D по центру, текст зверху; hover — нахил за курсором.',
     'На выходе — <em>рекламные объявления</em>',
     '<p class="s16-caption">Реклама в Instagram и Facebook · 3 креатива для теста</p><div class="s16-fan"><div class="s16-tilt"><img class="a" src="'+D+'creative-a.webp" alt=""><img class="b" src="'+D+'creative-b.webp" alt=""><img class="c" src="'+D+'creative-c.webp" alt=""></div></div>',
     's16-fan',brief='Три креативи віялом.',anim='Поява; hover — легкий 3D-нахил.')
# 189 · Коммерческие предложения (g409d4d20be6_0_55)
base('g409d4d20be6_0_55','21.09 Мирослав: варіант А — перший слайд КП цілком і три під ним (крок 0), банери для сайту (крок 1); вирізано без рамки, по центру.',
     '<em>Коммерческие предложения</em>',
     '<div class="s16-set s0"><img class="hero" src="'+D+'kp-hero.webp" alt=""><div class="row3"><img src="'+D+'kp-1.webp" alt=""><img src="'+D+'kp-2.webp" alt=""><img src="'+D+'kp-3.webp" alt=""></div><p class="lab">Презентация клиенту</p></div>'
     '<div class="s16-set s1"><img class="b1" src="'+D+'banner-1.webp" alt=""><img class="b2" src="'+D+'banner-2.webp" alt=""><p class="lab">Баннеры для сайта</p></div>',
     's16-kpsets',{'steps':['Презентация клиенту','Баннеры для сайта']},brief='КП: перший слайд + три; банери.',anim='Два кроки.')
# 190 · Обложки YouTube, Reels и TikTok (g409d4d20be6_0_61)
base('g409d4d20be6_0_61','21.09 Мирослав: варіант C — 3D-полиця: три обкладинки YouTube верхнім рядом, три Reels/TikTok ближче до глядача; hover — нахил за курсором.',
     'Обложки YouTube, <em>Reels и TikTok</em>',
     '<div class="s16-scene"><div class="s16-tilt"><img class="y1" src="'+D+'yt-1.webp" alt=""><img class="y2" src="'+D+'yt-2.webp" alt=""><img class="y3" src="'+D+'yt-3.webp" alt=""><img class="r1" src="'+D+'reels-1.webp" alt=""><img class="r2" src="'+D+'reels-2.webp" alt=""><img class="r3" src="'+D+'reels-3.webp" alt=""></div></div><div class="s16-labs"><span>YouTube — верхний ряд</span><span>Reels и TikTok — нижний</span></div>',
     's16-shelf',brief='Шість обкладинок на 3D-полиці.',anim='Поява; hover — нахил.')
# 191 · Продающие AI-видео (g409d4d20be6_0_105)
ITEMS=[('Товары','ролик под карточку и под рекламу'),('Одежда','модель в кадре создана нейросетью'),('Услуги и клиники','показать, как всё проходит'),('Офлайн-объекты','показать помещение, которого ещё нет')]
base('g409d4d20be6_0_105','21.09 Мирослав: варіант А — відео IMG_7847 зверху (16:9, без чорних смуг, автоплей без звуку), під ним заголовок, теза, ціна і чотири типи роликів рівними рядами; клік по відео — на весь слайд зі звуком.',
     'Продающие <em>AI-видео</em>',
     '<div class="s16-player"><video src="assets/video/vlad-1409/img-7847-720.mp4" poster="./assets/video/vlad-1409/img-7847-720-poster.jpg" muted autoplay loop playsinline preload="metadata"></video><div class="hint">▶ на весь слайд</div></div>'
     '<p class="s16-claim">В кадре не актёр. Никто не приезжал на площадку</p><span class="s16-price">$300–$1.200 · за пакет 8–12 роликов · сложность лёгкая</span>'
     '<div class="s16-list">'+''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in ITEMS)+'</div>',
     's16-cine',{'eyebrow':'Услуга 3 из 7'},brief='Відео IMG_7847 зверху, текст під ним.',anim='Відео грає само; клік — на весь слайд.')
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
