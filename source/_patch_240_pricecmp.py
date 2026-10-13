# 21.09 · 240 «И даже эти подписки — дешевле»: таблиця в стилі слайда 32 (.pricecmp.wide: логотипи, «официально» закреслено, «у нас» жовтим, чіп економії). Числа з ТЗ; % економії — арифметика з тих самих чисел.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_2936'; s=va[oid]
ROWS=[('claude','Claude Pro',20,20),('openai','ChatGPT Plus',20,9),('googlegemini','Gemini Pro',20,3.33),('perplexity','Perplexity Pro',20,2.42)]
def money(v): return '$'+(f'{v:.2f}'.rstrip('0').rstrip('.') if v!=int(v) else str(int(v)))
rows=''.join(f"<div class='pr'><span><img class='nlogo' src='assets/logo/{lg}.svg' alt=''>{nm}</span><s>{money(a)}</s><b>{money(b)}</b><em>{'—' if a==b else '−'+str(round((1-b/a)*100))+'%'}</em></div>" for lg,nm,a,b in ROWS)
table=("<div class='s239-table'><div class='pricecmp wide'><div class='pr hd'><span>Нейронка</span><u>официально</u><u>у нас</u><u>экономия</u></div>"+rows+
       "<div class='pr tot'><span>Итого в месяц</span><s>$80</s><b>$35</b><em>−56%</em></div></div></div>")
b=s['set']['b']; a=b.index("<div class=\"s239-table\">"); e=b.index("<div class=\"s239-extras\">")
s['set']['b']=b[:a]+table+b[e:]
s['reason']=(s.get('reason') or '')+' | 21.09 Мирослав: таблиця в стилі слайда 32 (логотипи, закреслені офіційні ціни, «у нас» жовтим, чіп економії, підсумковий рядок).'
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched 240')
