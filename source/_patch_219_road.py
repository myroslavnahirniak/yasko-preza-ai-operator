# 21.09 · 219 (частина 1 з 4, «Как теперь ищут бизнес»): roadmap у стилі 217 — кружок → звивиста дорога → 02 → 03 (s16-road3, власна назва, бо s16-road зайнятий), крок підсвічує зупинку і підпис, на кожному кроці проявляється своя згенерована сцена (GPT Image 2.5, assets/gen-184-188/s219-*.webp).
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
part=va['g409d4d20be6_0_398']['presentationParts']['slides'][0]
D='M60 150 C220 150 330 60 500 60 S780 150 940 150'
STOPS=[(60,150),(500,60),(940,150)]
LABS=[('01','Человек спрашивает','у ChatGPT, Gemini или Perplexity: где купить, кого выбрать'),('02','Нейросеть отвечает','и называет сайт вашего клиента'),('03','Человек приходит','уже готовый, его не надо уговаривать')]
svg=f'<svg class="s16-rd" viewBox="0 0 1000 200" preserveAspectRatio="none"><path class="base" d="{D}"/><path class="lit" d="{D}" pathLength="100"/>'
for i,(x,y) in enumerate(STOPS):
    svg+=f'<g class="s16-st s{i}"><circle class="halo" cx="{x}" cy="{y}" r="18"/><circle class="ring" cx="{x}" cy="{y}" r="11"/><circle class="dot" cx="{x}" cy="{y}" r="6"/></g>'
svg+='</svg>'
labs=''.join(f'<div class="s16-lab3 l{i}" style="--x:{x/10}%"><i>{n}</i><b>{t}</b><span>{s}</span></div>' for i,((x,y),(n,t,s)) in enumerate(zip(STOPS,LABS)))
part['b']='<p class="s16-caption">Три шага — и клиент уже на сайте</p><div class="s16-roadwrap3">'+svg+labs+'</div>'
b=part['foundation']['block129']; b['layout']='s16-road3'
b['art']=[{'src':'assets/gen-184-188/s219-ask.webp','alt':'Человек спрашивает'},{'src':'assets/gen-184-188/s219-answer.webp','alt':'Нейросеть отвечает'},{'src':'assets/gen-184-188/s219-arrive.webp','alt':'Человек приходит'}]
part['note']='Частина 1 з 4: шлях людини. Roadmap: кружок → дорога → 02 → 03, крок = зупинка + сцена.\nGoogle Slides #1232 · g409d4d20be6_0_398'
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched part 0 → s16-road3')
