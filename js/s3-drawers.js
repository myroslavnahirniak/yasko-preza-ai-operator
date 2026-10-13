(function () {
  'use strict';

  const escape = (value) => String(value == null ? '' : value).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));

  const illustrations = [
    `<svg viewBox="0 0 180 180" fill="none" aria-hidden="true">
      <path d="M31 126 87 145 151 121 95 103Z" fill="#FDD506" opacity=".07"/>
      <path d="M42 106v20c0 7 16 13 35 13s35-6 35-13v-20" fill="#211D0C" stroke="currentColor" stroke-width="2.5"/>
      <ellipse cx="77" cy="106" rx="35" ry="12" fill="#15130B" stroke="currentColor" stroke-width="2.5"/>
      <path d="M42 116c0 7 16 13 35 13s35-6 35-13" stroke="currentColor" stroke-opacity=".3" stroke-width="2"/>
      <path d="M69 76v25c0 7 16 13 35 13s35-6 35-13V76" fill="#2F280C" stroke="currentColor" stroke-width="2.5"/>
      <ellipse cx="104" cy="76" rx="35" ry="12" fill="#FDD506" stroke="currentColor" stroke-width="2.5"/>
      <path d="M69 88c0 7 16 13 35 13s35-6 35-13" stroke="currentColor" stroke-opacity=".45" stroke-width="2"/>
      <path d="M47 77V48m0 0L37 58m10-10 10 10" stroke="#F8F5E9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      <ellipse cx="104" cy="76" rx="12" ry="4" stroke="#0B0907" stroke-opacity=".7" stroke-width="2"/>
    </svg>`,
    `<svg viewBox="0 0 180 180" fill="none" aria-hidden="true">
      <path d="m35 130 52 18 61-23-52-18Z" fill="#FDD506" opacity=".07"/>
      <path d="m45 87 43 18 48-20v39l-48 19-43-18Z" fill="#221D0B" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="m88 105 48-20v39l-48 19Z" fill="#FDD506" fill-opacity=".13"/>
      <path d="m45 87 43-19 48 17-48 20Z" fill="#0B0907" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="m45 87-9-17 43-19 9 17m48 17 10-17-48-17-10 17" fill="#272210" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M88 105v38" stroke="currentColor" stroke-width="2.5"/>
      <path d="M65 74V39h45v36L88 84Z" fill="#F8F5E9" stroke="#F8F5E9" stroke-width="2" stroke-linejoin="round"/>
      <path d="M76 51h22m-22 9h14" stroke="#0B0907" stroke-width="3" stroke-linecap="round"/>
    </svg>`,
    `<svg viewBox="0 0 180 180" fill="none" aria-hidden="true">
      <path d="m30 131 57 18 65-22-57-19Z" fill="#FDD506" opacity=".07"/>
      <path d="M49 58h85v70H49z" fill="#201B0A" stroke="currentColor" stroke-opacity=".4" stroke-width="2.5"/>
      <path d="M39 48h85v70H39z" fill="#15120A" stroke="currentColor" stroke-width="2.5"/>
      <path d="M31 39h85v70H31z" fill="#FDD506" stroke="currentColor" stroke-width="2.5"/>
      <rect x="47" y="60" width="53" height="30" rx="8" fill="#0B0907"/>
      <circle cx="61" cy="75" r="4" fill="#FDD506"/>
      <circle cx="86" cy="75" r="4" fill="#FDD506"/>
      <path d="M74 60V53" stroke="#0B0907" stroke-width="3"/>
      <circle cx="74" cy="49" r="3" fill="#0B0907"/>
      <path d="m129 63 9 9 15-19" stroke="#F8F5E9" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`
  ];

  window.S3Variants = window.S3Variants || {};
  window.S3Variants.drawers = {
    render(c) {
      const header = (c.lines || []).map((line) => `<span>${line}</span>`).join('');
      const panels = (c.items || []).map((item, index) => `
        <article class="s3-drawer" data-item="${index + 1}" aria-label="${escape(item.title)} ${escape(item.detail)}">
          <div class="s3-drawer-reveal">
            <div class="s3-drawer-art">${illustrations[index] || illustrations[0]}</div>
            <div class="s3-drawer-copy"><h2>${escape(item.title)}</h2><p>${escape(item.detail)}</p></div>
          </div>
          <div class="s3-drawer-cover" aria-hidden="true"><span class="s3-drawer-number">${String(index + 1).padStart(2, '0')}</span><span class="s3-drawer-handle"></span><svg viewBox="0 0 40 40" fill="none"><path d="M11 20h18m-7-7 7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </article>`).join('');
      return `<section class="s3-design s3-drawers" data-step="1"><header class="s3-drawers-heading"><h1>${header}</h1></header><div class="s3-drawers-stack">${panels}</div><footer class="s3-drawers-closing">${escape(c.closing)}</footer></section>`;
    }
  };
})();
