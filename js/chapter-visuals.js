(function () {
  'use strict';
  function esc(s) { return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
  function title(lines, tag, cls) { return '<' + tag + ' class="' + cls + '">' + lines.map(function(t){return '<span>'+t+'</span>';}).join(' ') + '</' + tag + '>'; }
  function parity(v) {
    var person = '<circle cx="65" cy="48" r="20"/><path d="M25 135v-22c0-23 18-37 40-37s40 14 40 37v22M43 135v-22M87 135v-22"/>';
    var novice = '<svg viewBox="0 0 260 170" aria-hidden="true"><g class="cv-person">' + person + '</g><path class="cv-parity-plus" d="M121 96h20M131 86v20"/><g class="cv-ai-chip"><rect class="cv-chip-fill" x="161" y="51" width="74" height="74" rx="13"/><rect x="173" y="63" width="50" height="50" rx="6"/><path d="M176 42v9M191 42v9M206 42v9M221 42v9M176 125v9M191 125v9M206 125v9M221 125v9M152 67h9M152 82h9M152 97h9M152 112h9M235 67h9M235 82h9M235 97h9M235 112h9"/><text x="198" y="95">AI</text></g></svg>';
    var expert = '<svg viewBox="0 0 260 170" aria-hidden="true"><g class="cv-person" transform="translate(58 0)">' + person + '<path d="m56 78 9 13 9-13M65 91v32"/></g><g class="cv-expert-badge"><circle cx="184" cy="110" r="19"/><path d="m175 111 6 6 12-14M173 126l-2 15 13-7 13 7-2-15"/></g></svg>';
    return '<div class="cv-parity" role="img" aria-label="' + esc(v.description) + '"><div class="cv-parity-side cv-parity-novice">' + novice + '<div class="cv-parity-label">' + esc(v.novice) + ' <em>+ AI</em></div></div><svg class="cv-parity-equal" viewBox="0 0 40 40" aria-hidden="true"><path d="M7 14h26M7 26h26"/></svg><div class="cv-parity-side cv-parity-expert">' + expert + '<div class="cv-parity-label">' + esc(v.expert) + '</div></div></div>';
  }
  function render(c) {
    var count = c.phases ? c.phases.length : 1;
    var h = '<div class="chapter-visual cv-' + esc(c.kind) + (c.presentation === 'single-screen' ? ' cv-single-screen' : '') + '" data-step="1" data-steps="' + count + '">';
    if (c.backdrop === 'circuit') h += '<svg class="cv-circuit" viewBox="0 0 100 100" fill="none" aria-hidden="true"><g stroke="currentColor" stroke-width=".12"><path d="M0 17h16l6 6v12h8M0 27h9l7 7v25l8 8h9M100 19H85l-7 7v9h-8M100 30H91l-7 7v24l-8 8h-7M0 82h18l8-8h7M100 84H85l-9-9h-7M29 100V89l8-8M68 100V90l-8-8"/><rect x="33" y="17" width="34" height="66" rx="7" opacity=".28"/></g><g fill="currentColor"><circle cx="30" cy="35" r=".45"/><circle cx="33" cy="67" r=".45"/><circle cx="70" cy="35" r=".45"/><circle cx="69" cy="69" r=".45"/><circle cx="33" cy="74" r=".45"/><circle cx="69" cy="75" r=".45"/></g></svg>';
    if (c.image) h += '<div class="cv-image"><img data-src="'+esc(c.image)+'" alt="" aria-hidden="true"></div>';
    if(c.kind === 'audiences') h += '<div class="cv-shade cv-shade-left"></div><div class="cv-shade cv-shade-right"></div>';
    if (c.kind === 'leverage') h += '<div class="cv-photo-copy">' + title(c.lines,'h1','cv-title split-done') + '<p class="cv-support">'+c.support+'</p></div>';
    else {
      if(c.lines) h += '<header class="cv-heading">'+title(c.lines,'h1','cv-title split-done')+'</header>';
      c.phases.forEach(function(p,i){
        h += '<div class="cv-phase'+(i===0?' is-current':'')+(p.visualization ? ' cv-has-parity' : '')+'" data-phase="'+(i+1)+'" aria-hidden="'+(i!==0)+'">';
        if(p.lines) h += title(p.lines,c.kind==='rules-text'&&i===0?'h1':'h2','cv-phase-title split-done');
        if(p.visualization) h += p.visualization.kind === 'agent-run' ? window.RulesMotion.render(p.visualization.description) : parity(p.visualization);
        if(p.groups) h += '<div class="cv-text-route">'+p.groups.map(function(g,i){var body=g.bodyLines?g.bodyLines.map(function(line){return '<span>'+esc(line)+'</span>';}).join(' '):esc(g.body);return '<div data-route-step="'+(i+1)+'"><strong>'+esc(g.title)+'</strong><p>'+body+'</p></div>';}).join('')+'</div>';
        if(p.paragraphs) h += '<div class="cv-body">'+p.paragraphs.map(function(t){return '<p>'+t+'</p>';}).join('')+'</div>';
        if(p.closing) h += '<p class="cv-closing">'+p.closing+'</p>';
        h += '</div>';
      });
    }
    return h+'</div>';
  }
  function stepCount(el) { return Number(el.dataset.steps)||1; }
  function setStep(el,n) {
    n=Math.max(1,Math.min(stepCount(el),n));el.dataset.step=n;
    el.querySelectorAll('[data-phase]').forEach(function(p){var on=Number(p.dataset.phase)===n;p.classList.toggle('is-current',on);p.setAttribute('aria-hidden',String(!on));});
  }
  function cue(el) { var p=el.querySelector('.cv-phase.is-current');return p?p.innerText.replace(/\s+/g,' ').trim():''; }
  window.ChapterVisuals={render:render,setStep:setStep,stepCount:stepCount,cue:cue};
})();
