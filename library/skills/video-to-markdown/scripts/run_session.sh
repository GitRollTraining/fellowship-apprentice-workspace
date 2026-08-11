#!/usr/bin/env bash
# run_session.sh SESSION_DIR VIDEO_GLOB WAV_GLOB|- TITLE [EXTRA_NOTE]
# Full pipeline for one session -> SESSION_DIR/output/{session.md,stills/,stills.json,transcript.json}
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# python resolution: $VIDEO2MD_PYTHON (the virtual environment you created — see SKILL.md
# "Install once"; library/ is read-only, so it cannot live in this directory) > system python3
PY="${VIDEO2MD_PYTHON:-python3}"
command -v "$PY" >/dev/null 2>&1 || [ -x "$PY" ] || {
  echo "python not found: $PY — set VIDEO2MD_PYTHON to your virtual environment's python (see SKILL.md)" >&2; exit 1; }
"$PY" -c "import numpy" >/dev/null 2>&1 || {
  echo "$PY cannot import numpy — create the environment and export VIDEO2MD_PYTHON (see SKILL.md 'Install once')" >&2; exit 1; }
dir="$1"; vglob="$2"; wglob="$3"; title="$4"; extra="${5:-}"

mkdir -p "$dir/output"
video="$(find "$dir" -maxdepth 1 -name "$vglob" -type f | head -1)"
[ -n "$video" ] || { echo "no video match $vglob in $dir" >&2; exit 1; }
vsrc="$(basename "$video")"
wav=""
[ "$wglob" != "-" ] && wav="$(find "$dir" -maxdepth 1 -name "$wglob" -type f | head -1)"

# damaged/unindexed containers make -ss seeks land off-target (gotcha F11): remux mkv -> mp4 first
case "$video" in
  *.mkv)
    echo "[$title] remuxing mkv -> mp4 (seek accuracy)"
    ffmpeg -y -v error -i "$video" -c copy -movflags +faststart "$dir/output/.remux.mp4" 2>/dev/null || true
    if [ -s "$dir/output/.remux.mp4" ]; then video="$dir/output/.remux.mp4"; fi
    ;;
esac

# usable duration = last readable packet pts (headers lie on truncated files)
vdur="$(ffprobe -v error -select_streams v -show_entries packet=pts_time -of csv=p=0 "$video" 2>/dev/null | tail -1)"
out="$dir/output"
mkdir -p "$out"
rm -f "$out/stills.json" "$out/transcript.json"
rm -rf "$out/stills"

echo "[$title] stills pass (vdur=${vdur}s)"
"$PY" "$HERE/extract_stills.py" "$video" "$out" --thr 0.02 --no-mask \
  --src "$vsrc" --dump-scores "$out/scores.tsv"

has_subs="$(ffprobe -v error -select_streams s -show_entries stream=index -of csv=p=0 "$video" | head -1)"
if [ -n "$has_subs" ]; then
  echo "[$title] subtitle track found — extracting (free transcript)"
  ffmpeg -y -v error -i "$video" -map 0:s:0 "$out/.subs.srt"
  "$PY" "$HERE/srt_to_transcript.py" "$out/.subs.srt" "$out/transcript.json" \
    --src "$(basename "$video")" --max-seg 15
else
  echo "[$title] transcribe video audio (ASR)"
  "$PY" "$HERE/transcribe_timed.py" "$video" "$out/transcript.json" --src "$vsrc"
fi

srcs=("$vsrc | ${vdur%.*} s | screen recording (usable packets)")
notes=()
if [ -n "$wav" ]; then
  wdur="$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$wav")"
  echo "[$title] transcribe continuation wav (offset ${vdur%.*}s)"
  "$PY" "$HERE/transcribe_timed.py" "$wav" "$out/transcript.json" \
    --src "$(basename "$wav")" --t-offset "${vdur%.*}" --append
  srcs+=("$(basename "$wav") | ${wdur%.*} s | audio-only continuation, offset +${vdur%.*} s")
  notes+=("Audio-only continuation: sections after $(printf '%02d:%02d:%02d' $((${vdur%.*}/3600)) $((${vdur%.*}%3600/60)) $((${vdur%.*}%60))) have no screen stills (wav segment).")
fi
[ -n "$extra" ] && notes+=("$extra")

args=("$out/session.md" --title "$title" --transcript "$out/transcript.json" --stills "$out/stills.json")
for s in "${srcs[@]}"; do args+=(--source "$s"); done
for n in "${notes[@]}"; do args+=(--note "$n"); done
echo "[$title] assemble"
"$PY" "$HERE/assemble.py" "${args[@]}"
echo "[$title] clean transcript"
"$PY" "$HERE/render_transcript.py" "$out"
echo "[$title] DONE -> $out"
