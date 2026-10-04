#!/usr/bin/env bash
# read_page.sh MODEL DJVU  -> full/<model>/<djvu>.txt   (MODEL = opus | codex)
set -u
m=$1 d=$2 W=$(realpath "${PM_WORK:-work}") CODEX=${CODEX:-codex}
img="$W/scan/djvu$d.jpg" out="$W/scan/full/$m/$d.txt"
mkdir -p "$W/scan/full/$m"
[[ -s $out ]] && exit 0
[[ -s $img ]] || { echo "no image $d" >&2; exit 1; }
p=$(<"$W/scan/full/prompt_full.txt")
w=$(mktemp -d)   # empty cwd: nothing else for the agent to wander into
cp "$img" "$w/page.jpg"
cd "$w" || exit 1
case $m in
  opus)  printf '%s\n' "Read only the file $w/page.jpg and nothing else. $p" | timeout 900 claude -p --model claude-opus-5-5 --allowedTools=Read > "$out.tmp" 2> "$out.err" ;;
  codex-*) e=${m#codex-}; timeout 1200 "$CODEX" exec --skip-git-repo-check -c "model_reasoning_effort=\"$e\"" "$p" -i "$w/page.jpg" > "$out.tmp" 2> "$out.err" ;;
  codexhi) timeout 1200 "$CODEX" exec --skip-git-repo-check -c 'model_reasoning_effort="high"' "$p" -i "$w/page.jpg" > "$out.tmp" 2> "$out.err" ;;
  codex) eff=(); [[ -n ${CODEX_EFFORT:-} ]] && eff=(-c "model_reasoning_effort=\"$CODEX_EFFORT\"")   # unset = server default (passing "none" is rejected)
         timeout 900 "$CODEX" exec --skip-git-repo-check "${eff[@]}" "$p" -i "$w/page.jpg" > "$out.tmp" 2> "$out.err" ;;
esac
rc=$?
[[ $rc -eq 0 && -s $out.tmp ]] && mv "$out.tmp" "$out" || echo "$m $d rc=$rc" >&2
rm -rf "$w"
