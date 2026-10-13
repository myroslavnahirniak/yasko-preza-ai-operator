#!/bin/zsh
# 01.10: окремий лінк на деку після зуму з Владом — проєкт yasko-preza-1001 (старий прод yasko-preza-v5 не чіпаємо).
# Головна (/) = Google 1–325 до позначки Влада «ДО СЮДА!» (екрани до «Механизм работает. Вы его видели» включно);
# 03.10: / = екрани 1–177 (до «Первый — это чат»), /rest = 178 → «ДО СЮДА!» (свої номери 1–N).
# /part1 = Google 1–185 (екрани 1–145), /part2 = Google 186–325 (екрани 146–228, свої номери 1–83); повна дека — /google180.html.
# 01.10 обріз був після «Что такое AI-агент» (g3fadf66108e_0_1237), але 02.10 Влад переніс його всередину блоку.
set -e
cd "$(dirname $0)/.."
S=../_deploy-preza-1001
rsync -a --delete \
 --exclude='.git' --exclude='.git-off-deploy' --exclude='shots/' --exclude='node_modules/' --exclude='*.md' --exclude='.DS_Store' --exclude='.env*' \
 --exclude='.vercelignore*' --exclude='.patched' --exclude='.vercel/' \
 --exclude='assets/photo/gen/kie-full/' --exclude='assets/video/kejsy/' \
 --exclude='assets/gen-secret2-full/*.png' --exclude='assets/gen-secret2-full/*.jpg' --exclude='assets/gen-secret2-full/refs/' --exclude='assets/gen-secret2-full/log.json' \
 --include='source/' --include='source/audit-final-2026-09-11/' --include='source/audit-final-2026-09-11/rendered/***' \
 --include='source/google-2026-09-16/' --include='source/google-2026-09-16/media/***' \
 --include='source/design-s179-motion/' --include='source/design-s179-motion/video/***' --include='source/design-s179-motion/orbit-frames/***' \
 --include='source/import-secret2/' --include='source/import-secret2/slide.html' --include='source/import-secret2/theme.css' --include='source/import-secret2/remote-slides.json' \
 --exclude='source/**' ./ $S/
python3 source/_parts_1001.py "$S"   # index (Google 1–325) + part1 (1–185) + part2 (186–325)
echo '{"framework": null, "buildCommand": null, "outputDirectory": ".", "cleanUrls": true}' > "$S/vercel.json"
# 03.10: cleanUrls робить …/site/index.html → 308 на …/site (без слеша) — відносні шляхи сайтів в iframe ламаються (слайд 10 Рома, 2 Офис).
# Тому в цій викладці iframe-адреси assets/…/index.html → assets/…/ (папка віддає index.html одразу, 200).
python3 - "$S" <<'PY'
import sys, re, glob
s = sys.argv[1]; n = 0
for fn in glob.glob(s + '/js/*.js') + glob.glob(s + '/*.html'):
    t = open(fn, encoding='utf-8').read()
    t2, k = re.subn(r'(assets/[A-Za-z0-9_.\-/]+/)index\.html', r'\1', t)
    if k: open(fn, 'w', encoding='utf-8').write(t2); n += k
print('iframe index.html → /:', n)
PY
echo "staging: $(du -sh $S | cut -f1); файли >90MB:"; find $S -type f -size +90M
cd $S
[ -f .vercel/project.json ] || vercel link --yes --project yasko-preza-1001
vercel deploy --prod --yes
