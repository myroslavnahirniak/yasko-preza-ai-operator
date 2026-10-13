#!/bin/zsh
# GPT Image 2.5 with face reference. Usage: ./_gen_ref.sh <name> "<prompt>" <ref-image>
set -e
cd "$(dirname "$0")"
name="$1"; prompt="$2"; ref="$3"
out=$(higgsfield generate create gpt_image_2_5 --prompt "$prompt" --image-references "$ref" --aspect_ratio 1:1 --resolution 2k --quality xhigh --wait --wait-timeout 15m --json 2>&1)
echo "$out" > "${name}.job.json"
printf '%s\n%s\n' "$name" "$prompt (ref: $ref)" >> _prompts.log
echo "$name done"
