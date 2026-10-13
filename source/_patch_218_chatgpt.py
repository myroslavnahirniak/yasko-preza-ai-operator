# 21.09 · 218 «AI-SEO (видимость в нейросетях)»: варіант 1 (Мирослав) — живий чат ChatGPT з реального скрина (слайд 221): запит друкується, відповідь стрімиться, перший пункт «Влад Ясько — AI-Маркетолог» жовтим, крок 2 — відкривається сайт aimarketolog.site (локальна копія assets/sites/aimarketolog). Три виходи агента і ціна лишаються.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_2912'
PROMPT='Найди украинских экспертов по AI-маркетингу и AI-агентам. Только авторские курсы, не школы. Дай официальные сайты.'
LINES=[
 ('p','Отфильтровал крупные школы вроде Skillbox/GoIT и искал <b>украинских практиков с авторской программой</b>. Самое точное попадание:'),
 ('hit','<b>1. Влад Ясько — «AI-Маркетолог»</b>'),
 ('p','Авторская система бизнеса на AI-агентах: Claude Code, ChatGPT, Gemini, <b>66+ AI-сотрудников</b>, блоки по продажам, контенту и воронкам.'),
 ('link','Официальный сайт: <u>AI-Маркетолог — Влад Ясько ↗</u>'),
]
ITEMS=[('01','бизнес находят в поиске и на картах'),('02','и в ответах нейросетей, когда у них спрашивают совет'),('03','без платной рекламы — трафик не выключается')]
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: варіант 1 — живий чат ChatGPT (реальний запит і відповідь зі скрина 221), друк + стрім, перший пункт жовтим; крок 2 — сайт aimarketolog.site відкривається у вікні браузера (локальна копія).'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='AI-SEO <em>(видимость в нейросетях)</em>'
st['b']=('<div class="s16-col"><p class="s16-legend">Что собирает агент</p><div class="s16-out">'+''.join(f'<div><i>{n}</i><b>{t}</b></div>' for n,t in ITEMS)+'</div><span class="s16-price">$400–$1.800 · за пакет в месяц · сложность средняя</span></div>'
 '<div class="s16-gpt"><div class="s16-gptwin"><div class="bar"><span class="logo"></span><b>ChatGPT</b><em>веб-поиск</em></div>'
 '<div class="msgs"><div class="me"><span class="typed" data-text="'+PROMPT.replace('"','&quot;')+'"></span><i class="caret"></i></div>'
 '<div class="ai"><div class="think"><i></i><i></i><i></i></div>'+''.join(f'<p class="{c}" data-html="{h.replace(chr(34),"&quot;")}"></p>' for c,h in LINES)+'</div></div></div></div>')
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,
          'mediaBrief':'Чат ChatGPT з реальним запитом/відповіддю + сайт у вікні.','animationBrief':'Крок 1: запит друкується, відповідь стрімиться, пункт 1 жовтим, посилання пульсує. Крок 2: вікно сайту виїжджає поверх.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-chatgpt','eyebrow':'Услуга 7 из 7'}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',oid)
