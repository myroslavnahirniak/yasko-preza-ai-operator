#!/usr/bin/env python3
"""02.10 · сторінки (03.10: index/main = екрани 1–177, rest = 178 → «ДО СЮДА!») для перегляду на yasko-preza-1001: index (Google 1–325), part1 (Google 1–185), part2 (Google 186–325).
Беремо google180.html і після slides-google180.js вставляємо скрипт, що обрізає window.S на місці.
usage: python3 source/_parts_1001.py <out_dir>   (деплой: staging; локально для перевірки: .  → лише part1/part2.html)"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
page = (ROOT / 'google180.html').read_text(encoding='utf-8')
START2 = 'p111'                    # «Какие услуги покупают за $250–$3.000» (Секрет №1) — перший екран частини 2
END = 'g3f9b3adf0b8_0_3012'        # «Механизм работает. Вы его видели» — останній перед позначкою Влада «ДО СЮДА!»
# 03.10 Мирослав: екрани 178+ — на окрему сторінку /rest; головна (/) закінчується на «Первый — это чат. Второй — агент»
MAIN_END = 'g3fadf66108e_0_1361'   # «Первый — это чат. Второй — агент» (екран 177 на 03.10)
REST_START = 'g3fadf66108e_0_1377' # «Агент — это сотрудник, которого я обучил» (екран 178 на 03.10)
REST_FROM = 'g3f9b3adf0b8_0_2786'  # 08.10 Мирослав: /rest починається з «Напишите в чат» (екран 169), попередні — лише в головній
REST_END = '__none__'               # 06.10: «ДО СЮДА!» у Google більше нема — /rest іде до кінця деки (вся друга частина Влада)
JS = {
    'index': "var b=S.findIndex(function(x){return x.googleObjectId==='%s'});if(b>=0)S.length=b+1;" % MAIN_END,
    'main': "var b=S.findIndex(function(x){return x.googleObjectId==='%s'});if(b>=0)S.length=b+1;" % MAIN_END,  # локальна копія головної
    # 08.10 Мирослав: /rest = від «Напишите в чат» (REST_FROM; запасний старт — REST_START) до кінця деки
    'rest': ("var a=S.findIndex(function(x){return x.googleObjectId==='%s'});if(a<0)a=S.findIndex(function(x){return x.googleObjectId==='%s'});var b=S.findIndex(function(x){return x.googleObjectId==='%s'});"
             "if(a>=0){var t=S.slice(a,b>=a?b+1:S.length);S.length=0;Array.prototype.push.apply(S,t);}") % (REST_FROM, REST_START, REST_END),
    'part1': "var a=S.findIndex(function(x){return x.googleObjectId==='%s'});if(a>0)S.length=a;" % START2,
    'part2': ("var a=S.findIndex(function(x){return x.googleObjectId==='%s'}),b=S.findIndex(function(x){return x.googleObjectId==='%s'});"
              "if(a>=0&&b>=a){var t=S.slice(a,b+1);S.length=0;Array.prototype.push.apply(S,t);}") % (START2, END),
}
TITLE = {'index': 'Головна · до «Первый — это чат»', 'main': 'Головна · до «Первый — это чат»', 'rest': 'Часть 2', 'part1': 'Часть 1 · Google 1–185', 'part2': 'Часть 2 · Google 186–325'}
for name, js in JS.items():
    if name == 'index' and out.resolve() == ROOT:
        continue  # локальний index.html — робочий файл, не перезаписувати
    cut = '<script>/* %s */(function(){var S=window.S;%s})();</script>' % (TITLE[name], js)
    p, n = re.subn(r'(<script src="js/slides-google180\.js[^"]*"></script>)', lambda m: m.group(1) + '\n' + cut, page)
    assert n == 1
    p = re.sub(r'<title>[^<]*</title>', '<title>AI-Оператор · %s</title>' % TITLE[name], p, count=1)
    (out / (name + '.html')).write_text(p, encoding='utf-8')
    print('→', out / (name + '.html'))
