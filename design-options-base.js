/* 21.09 · спільний каркас сторінок варіантів (design-sNNN-options.html):
   таби варіантів, кроки (підслайди), replay, клавіші ←/→ (варіант) ↓/↑/Space (крок), URL ?v=A&step=2 */
(function(){
  const slide=document.getElementById('slide');
  const V=window.VARIANTS, order=window.ORDER||Object.keys(V);
  let cur=order[0], step=0;
  const q=new URLSearchParams(location.search);
  if(q.get('v')&&V[q.get('v')])cur=q.get('v');
  if(q.get('step'))step=Math.max(0,+q.get('step')||0);
  const $=s=>document.querySelector(s);
  function applyStep(animate){
    const v=V[cur]; const max=v.steps||0;
    step=Math.min(step,max);
    slide.dataset.step=step;
    slide.querySelectorAll('[data-step]').forEach(el=>{
      const n=+el.dataset.step;
      el.classList.toggle('is-future',n>step);
      el.classList.toggle('is-now',n===step);
      el.classList.toggle('is-past',n<step);
    });
    if(v.onStep)v.onStep(slide,step,animate);
    const s=$('#stepinfo');if(s)s.textContent=max?('шаг '+step+' / '+max):'';
    document.querySelectorAll('.stepbtn').forEach(b=>b.style.visibility=max?'visible':'hidden');
  }
  function render(){
    const v=V[cur];
    slide.className='slide v-'+cur+(v.cls?' '+v.cls:'');
    slide.innerHTML=typeof v.html==='function'?v.html():v.html;
    document.querySelectorAll('[data-v]').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.v===cur)));
    $('.description').textContent=v.desc||'';
    if(v.onRender)v.onRender(slide);
    applyStep(false);
    requestAnimationFrame(()=>requestAnimationFrame(()=>{slide.classList.add('play');if(v.onPlay)v.onPlay(slide);}));
    history.replaceState(null,'','?v='+cur+(step?'&step='+step:''));
  }
  window.setStep=function(n,animate){step=n;applyStep(animate!==false);history.replaceState(null,'','?v='+cur+(step?'&step='+step:''));};
  document.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>{cur=b.dataset.v;step=0;render();});
  const rp=$('#replay');if(rp)rp.onclick=()=>{step=0;render();};
  const nx=$('#next');if(nx)nx.onclick=()=>{const m=V[cur].steps||0;if(step<m)window.setStep(step+1);};
  const pv=$('#prev');if(pv)pv.onclick=()=>{if(step>0)window.setStep(step-1);};
  document.addEventListener('keydown',e=>{
    if(e.target.tagName==='INPUT')return;
    let i=order.indexOf(cur);
    if(e.key==='ArrowRight'){cur=order[(i+1)%order.length];step=0;render();}
    else if(e.key==='ArrowLeft'){cur=order[(i-1+order.length)%order.length];step=0;render();}
    else if(e.key==='ArrowDown'||e.key===' '){e.preventDefault();const m=V[cur].steps||0;if(step<m)window.setStep(step+1);}
    else if(e.key==='ArrowUp'){e.preventDefault();if(step>0)window.setStep(step-1);}
    else if(e.key==='r'){step=0;render();}
  });
  window.currentVariant=()=>cur;
  render();
})();
