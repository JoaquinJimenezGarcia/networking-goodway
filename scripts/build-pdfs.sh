#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LESSONS_DIR="$ROOT/lessons"
PDFS_DIR="$ROOT/pdfs"
TEMPLATE="$ROOT/templates/lesson.yaml"
mkdir -p "$PDFS_DIR"

ENGINE=""
if command -v typst >/dev/null 2>&1; then ENGINE="typst"
elif command -v xelatex >/dev/null 2>&1; then ENGINE="xelatex"
elif command -v pdflatex >/dev/null 2>&1; then ENGINE="pdflatex"
else echo "Install typst: brew install typst" >&2; exit 1; fi
command -v pandoc >/dev/null 2>&1 || { echo "Install pandoc: brew install pandoc" >&2; exit 1; }

count=0
for lesson in "$LESSONS_DIR"/*/lesson.md; do
  [[ -f "$lesson" ]] || continue
  slug="$(basename "$(dirname "$lesson")")"
  out="$PDFS_DIR/${slug}.pdf"
  echo "Building $slug -> $out"
  pandoc "$lesson" --metadata-file="$TEMPLATE" --pdf-engine="$ENGINE" -V geometry:margin=1in -o "$out"
  count=$((count + 1))
done
echo "Built $count PDFs"
ls -1 "$PDFS_DIR" | sort
