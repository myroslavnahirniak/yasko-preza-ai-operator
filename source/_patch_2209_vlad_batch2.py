# 22.09 · правки Влада, пачка 2: Саша один сайт; доход $1.000–$1.500; убрать «А если мне 45», «Наталья, 47», Юра/Анастасия/Андрей/«Ни один из них», 4 экрана «И под каждую есть свои сотрудники»; motion.jpg в «Вам даже промт»; «7 услуг» после «Весь этот каталог — одним документом».
import json,copy
p='source/overrides.json'; o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
AUTH='Правка Влада 22.09.2026 (через Мирослава): «Вот этот слайд очень важно вставить, список этих всех услуг после этого слайда фото» (ссылка на 7 услуг, которые агенты делают целиком).'
def why(s,msg): s['reason']=(s.get('reason') or '')+' | 22.09 Влад: '+msg
# 1. Саша: один сайт
s=va['g3f9b3adf0b8_0_1838']
s['set']['t']='Сайт, который Саша <em>делает сегодня</em>'
s['set']['b']=('<p style="position:absolute;left:7cqw;right:7cqw;top:25.5cqh;margin:0;z-index:3;font:400 2.5cqw/1.4 Manrope,sans-serif;color:#c4bdb1">Обычный подросток — и сайт, за который платят взрослые бизнесы</p>'
 '<div class="s16-four" style="top:35cqh;grid-template-columns:1fr;grid-template-rows:1fr"><div class="s16-fcard"><div class="s16-media light"><img src="assets/photo/sasha-site-faino.jpg" alt="Сайт груминг-салона, который сделал Саша"></div>'
 '<div class="s16-txt"><span class="s16-n">01</span><span>Сайт груминг-салона</span></div></div></div>')
why(s,'одно фото сайта (сашасайт.png), остальные заглушки убраны; «Сайт», а не «Сайты».')
# 2. доход Саши
def fix_income(b): return b.replace('у него $1.500–$3.000 в месяц','у него выходит $1.000–$1.500 в месяц').replace('Сейчас $1.500–$3.000 в месяц','Сейчас $1.000–$1.500 в месяц').replace('сейчас $1.500–$3.000 в месяц','сейчас $1.000–$1.500 в месяц')
s=va['g3f9b3adf0b8_0_1829']; s['set']['b']=fix_income(s['set']['b']); why(s,'доход Саши — $1.000–$1.500 в месяц (без $3.000).')
sales=va['g3f9b3adf0b8_0_2226']; P=sales['presentationParts']['slides']
for part in P:
    if '$1.500–$3.000' in part.get('b',''): part['b']=fix_income(part['b'])
# 3. omit
for oid,name in [('g3f9b3adf0b8_0_1847','«А если мне 45? А если 54?»'),('g3f9b3adf0b8_0_1855','«Наталья, 47»'),('g3f9b3adf0b8_0_1881','«Юра»'),('g3f9b3adf0b8_0_1893','«Анастасия»'),('g3f9b3adf0b8_0_1904','«Андрей»'),('g3f9b3adf0b8_0_1916','«Ни один из них не стал специалистом»')]:
    s=va[oid]; s['omit']=True; why(s,'убрать слайд '+name)
# 4. сотрудники: 4 экрана из продающей части
import re
st=lambda t:re.sub('<[^>]+>','',t or '')
before=len(P); P[:]=[x for x in P if st(x.get('t')).strip()!='И под каждую есть свои сотрудники']
print('removed сотрудники parts:',before-len(P))
why(sales,'убраны 4 экрана «И под каждую есть свои сотрудники»; доход Саши $1.000–$1.500.')
# 5. motion.jpg в «Вам даже промт писать не надо»
s=va['g3f9b3adf0b8_0_1873']; b=s['set']['b']; assert '<div class="s16-phbox"><span>фото · вставлю позже</span></div>' in b
s['set']['b']=b.replace('<div class="s16-phbox"><span>фото · вставлю позже</span></div>','<div class="s16-phbox s16-photo"><img src="assets/photo/sites-base-motion.jpg" alt="База готовых сайтов под разные ниши"></div>')
why(s,'вставлено фото базы сайтов (motion.jpg) вместо заглушки.')
# 6. «7 услуг» после каталога-документа
seven=[x for x in P if st(x.get('t')).strip()=='7 услуг, которые агенты делают целиком'][0]
cat=va['g3f9b3adf0b8_0_2921']; oid='g3f9b3adf0b8_0_2921'
part2={k:copy.deepcopy(seven[k]) for k in ('t','b','lv','k','foundation') if k in seven}
part2['note']='Список всех 7 услуг (копия экрана из продающей части) — сразу после «Весь этот каталог — одним документом».\nGoogle Slides #'+str(cat['set'].get('googleNumber','')) +' · '+oid
cat['presentationParts']={'sourceGoogleObjectId':oid,'authorization':AUTH,'allowPartTitles':True,'mediaStatus':'ready','slides':[{'note':'Часть 1: каталог одним документом.\nGoogle Slides · '+oid},part2]}
why(cat,'после этого слайда — экран «7 услуг, которые агенты делают целиком».')
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('batch2 patched')
