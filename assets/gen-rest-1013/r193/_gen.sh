#!/bin/zsh
# 13.10 rest 193 «Ремесло делает агент»: оживлення картинки Влада (Google G61) — Seedance 2.5, 3 варіанти. ./_gen.sh <name> "<prompt>"
cd "${0:A:h}"
name="$1"; prompt="$2"
out=$(higgsfield generate create seedance_2_5 --mode omni_reference --start-image start.jpg --prompt "$prompt" --aspect_ratio 1:1 --duration 6 --resolution 1080p --generate_audio false --wait --wait-timeout 25m --json 2>&1)
echo "$out" > "$name.job.json"
url=$(echo "$out" | grep -o 'https://[^"]*\.mp4' | head -1)
[ -n "$url" ] && curl -sL "$url" -o "$name.mp4" && echo "$name OK $url" || echo "$name FAIL"
