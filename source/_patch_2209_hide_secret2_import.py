#!/usr/bin/env python3
"""22.09 Мирослав: прибрати слайди 244–275 (імпортований Секрет 2 з v5, 32 частини на g3f9b3adf0b8_0_1774).
Частини зберігаються в source/import-secret2/parts-backup.json, сам Google-слайд → omit:true."""
import json
P='source/overrides.json'; d=json.load(open(P,encoding='utf-8'))
o=d['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_1774']
if 'presentationParts' in o:
    json.dump(o['presentationParts'],open('source/import-secret2/parts-backup.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    del o['presentationParts']
o['omit']=True
o['reason']='22.09 Мирослав: прибрати 244–275 (імпорт Секрету 2 з v5) | '+o.get('reason','')
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=2); print('ok, omit=true, parts backed up')
