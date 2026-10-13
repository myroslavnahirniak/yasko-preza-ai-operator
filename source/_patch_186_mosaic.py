# 21.09 · слайд 186 «AI-дизайн» (Google 197, g3f9b3adf0b8_0_2903): варіант В — 3D-мозаїка з 4 груп макетів (вирізки зі скринів Google, апскейл), 6 станів. Повний текст джерела.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_2903'; D='assets/vlad-1409/dizayn/'
ITEMS=[('Коммерческие предложения','именные, под конкретную сделку'),('Рекламные объявления','десятками, чтобы было что тестировать'),('Обложки для YouTube','под каждый ролик, в одном стиле'),('Обложки Reels и TikTok','под каждую серию, пачкой')]
G=[f'<div class="s16-g s16-g1"><img class="hero" src="{D}kp-hero.webp" alt=""><img class="sm" src="{D}kp-1.webp" alt=""><img class="sm" src="{D}kp-2.webp" alt=""><img class="sm" src="{D}kp-3.webp" alt=""></div>',
   f'<div class="s16-g s16-g2"><img src="{D}creative-a.webp" alt=""><img src="{D}creative-b.webp" alt=""><img src="{D}creative-c.webp" alt=""></div>',
   f'<div class="s16-g s16-g3"><img class="hero" src="{D}yt-1.webp" alt=""><img class="sm" src="{D}yt-2.webp" alt=""><img class="sm" src="{D}yt-3.webp" alt=""></div>',
   f'<div class="s16-g s16-g4"><img src="{D}reels-1.webp" alt=""><img src="{D}reels-2.webp" alt=""><img src="{D}reels-3.webp" alt=""></div>']
cards=''.join(f'<div class="s16-card k{i+1}">{G[i]}<div class="s16-lab"><i>0{i+1}</i><div><b>{t}</b><span>{d}</span></div></div></div>' for i,(t,d) in enumerate(ITEMS))
body=('<p class="s16-sub">Что выходит из агента</p><div class="s16-scene"><div class="s16-plane">'+cards+'</div></div>'
      '<div class="s16-final"><p class="s16-concl">Всё в одном стиле — за минуты, без дизайнера и без студии</p><span class="s16-price">$250–$900 · за пакет · сложность лёгкая</span></div>')
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: варіант В — 3D-мозаїка (4 картки-групи макетів, вирізаних зі скринів Google по окремості й збільшених); крок розгортає картку майже на весь квадрат, hover — нахил за курсором; висновок і ціна в контейнері по центру.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{}); st['t']='AI-дизайн'; st['b']=body; st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'mediaBrief':'Чотири групи макетів (КП, креативи, YouTube, Reels) на 3D-площині.','animationBrief':'Огляд → кожна група розгортається на весь квадрат → висновок і ціна в контейнері.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-mosaic','eyebrow':'Услуга 2 из 7','steps':['Обзор','Коммерческие предложения','Рекламные объявления','Обложки для YouTube','Обложки Reels и TikTok','Вывод и цена']}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1)
print('patched',oid)
