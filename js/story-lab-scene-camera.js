(function(){
const L=window.StoryLab;
let scene,scenePrevious=-1;
L.register('scene',{
mount(host){scene=host;host.innerHTML=L.intro()+`<div class="scene-copy"><div class="lab-flashback">Вернёмся назад</div><h2 class="lab-title"></h2><p class="lab-body"></p></div><div class="scene-main">${L.photo('agency')}${L.photo('officeBefore')}${L.photo('officeAfter','scene-office-after')}${L.photo('car')}</div>${L.photo('team','scene-second')}<div class="scene-metric"><strong>100+</strong><span>сотрудников</span></div><div class="scene-price">$37 000</div><div class="scene-travel">${['paris','bali','newyork'].map(k=>L.photo(k)).join('')}</div><div class="scene-overview">${['agency','officeAfter','car','paris'].map(k=>L.photo(k)).join('')}</div>`;},
update(n,{animate=true}={}){const s=L.steps[n];scene.dataset.step=n;scene.dataset.travel=String(n>=5&&n<=7);scene.querySelector('.scene-copy .lab-title').innerHTML=s.title;scene.querySelector('.scene-copy .lab-body').textContent=n===3?'':s.body;scene.querySelector('.lab-flashback').hidden=n!==1;
scene.querySelectorAll('.scene-main>.lab-photo').forEach(el=>el.classList.toggle('show',el.dataset.photo===s.key||(n===3&&el.dataset.photo==='officeBefore')));scene.querySelectorAll('.scene-travel>.lab-photo').forEach(el=>el.classList.toggle('show',el.dataset.photo===s.key));
if(animate&&n!==scenePrevious&&n!==3)scene.querySelector('.scene-copy').animate([{opacity:.25,transform:'translateY(10px)'},{opacity:1,transform:'translateY(0)'}],{duration:430,easing:'ease-out'});scenePrevious=n;}
});
let camera,previous=-1;
L.register('camera',{
mount(host){camera=host;host.innerHTML=L.intro()+`<div class="camera-photos">${['agency','officeBefore','officeAfter','car','paris','bali','newyork'].map(k=>L.photo(k)).join('')}</div><div class="camera-shade"></div><div class="camera-copy"><div class="lab-flashback">Вернёмся назад</div><h2 class="lab-title"></h2><p class="lab-body"></p></div><div class="camera-badge"></div><div class="camera-indicator"><i></i><i></i><i></i></div>`;},
update(n,{animate=true}={}){const s=L.steps[n],key=n===8?'paris':s.key;camera.dataset.step=n;camera.querySelector('.camera-copy .lab-title').innerHTML=s.title;camera.querySelector('.camera-copy .lab-body').textContent=n===3?'':s.body;camera.querySelector('.lab-flashback').hidden=n!==1;camera.querySelector('.camera-badge').innerHTML=n===3?'100+<small>сотрудников</small>':n===4?'$37 000':'';camera.querySelector('.camera-indicator').hidden=n<5||n>7;camera.querySelectorAll('.camera-indicator i').forEach((e,i)=>e.classList.toggle('on',i===n-5));
camera.querySelectorAll('.camera-photos>.lab-photo').forEach(el=>{const was=el.classList.contains('current');el.classList.toggle('leaving',animate&&was&&el.dataset.photo!==key);el.classList.toggle('current',el.dataset.photo===key);});
if(animate&&n!==previous)camera.querySelector('.camera-copy').animate([{opacity:0,transform:'translateY(12px)'},{opacity:1,transform:'translateY(0)'}],{duration:600,easing:'ease-out'});previous=n;}
});
})();
