#!/bin/zsh
# 28.09: деплой деки на yasko-preza-v5 з чистої копії (без .git, shots/, source/ крім потрібного, мастерів).
# Навіщо: vercel --prod з робочої папки падає — «File size limit exceeded (100 MB)» (CLI бере файли попри .vercelignore) і TEAM_ACCESS_REQUIRED через git-автора.
set -e
cd "$(dirname $0)/.."
S=../_deploy-preza-v5
rsync -a --delete \
 --exclude='.git' --exclude='.git-off-deploy' --exclude='shots/' --exclude='node_modules/' --exclude='*.md' --exclude='.DS_Store' --exclude='.env*' \
 --exclude='.vercelignore*' --exclude='.patched' \
 --exclude='assets/photo/gen/kie-full/' --exclude='assets/video/kejsy/' \
 --exclude='assets/gen-secret2-full/*.png' --exclude='assets/gen-secret2-full/*.jpg' --exclude='assets/gen-secret2-full/refs/' --exclude='assets/gen-secret2-full/log.json' \
 --include='source/' --include='source/audit-final-2026-09-11/' --include='source/audit-final-2026-09-11/rendered/***' \
 --include='source/google-2026-09-16/' --include='source/google-2026-09-16/media/***' \
 --include='source/design-s179-motion/' --include='source/design-s179-motion/video/***' --include='source/design-s179-motion/orbit-frames/***' \
 --include='source/import-secret2/' --include='source/import-secret2/slide.html' --include='source/import-secret2/theme.css' --include='source/import-secret2/remote-slides.json' \
 --exclude='source/**' ./ $S/
cp -R .vercel $S/
echo "staging: $(du -sh $S | cut -f1); файли >90MB:"; find $S -type f -size +90M
cd $S && vercel deploy --prod --yes
curl -s https://yasko-preza-v5.vercel.app/ | grep -o 'slides-google180.js?v=[^"]*'
