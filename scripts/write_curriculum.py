#!/usr/bin/env python3
"""Generate Networking Goodway lessons, exercises, solutions, README, PROGRESS."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def exercise_readme(m: dict) -> str:
    objs = "\n".join(f"- {o}" for o in m["objectives"])
    guide = (m.get("exercise_guide") or "").strip()
    if not guide:
        guide = (
            f"Edit `exercise.sh` and implement every stub so `./test.sh` passes. "
            f"Each function encodes a fact or command pattern from **{m['title']}**."
        )
    examples = (m.get("exercise_examples") or "").strip()
    if not examples:
        examples = (
            "Use the worked command examples in the lesson (with sample outputs) as your "
            "source of truth. Your functions should return the same flags, values, or "
            "labels the lesson teaches — not guesses."
        )
    return f"""# Exercise: {m['n']:02d}. {m['title']}

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

{objs}

## Task

{guide}

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/{m['slug']}/` | Peek only after a real attempt |

## Examples / expected behavior

{examples}

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/{m['slug']}/`.**
"""


def lesson_md(m: dict) -> str:
    objs = "\n".join(f"- {o}" for o in m["objectives"])
    pits = "\n".join(f"- {p}" for p in m["pitfalls"])
    checks = "\n".join(f"{i}. {c}" for i, c in enumerate(m["checks"], 1))
    reads = "\n".join(f"- {r}" for r in m["reading"])
    guide = (m.get("exercise_guide") or "").strip()
    guide_block = f"\n### What you will build\n\n{guide}\n" if guide else ""
    return f"""---
title: "{m['n']:02d}. {m['title']}"
---

# {m['n']:02d}. {m['title']}

**Phase:** {m['phase']}  
**Estimated time:** {m['days']}  
**Slug:** `{m['slug']}`

## Learning objectives

{objs}

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.
Type every command yourself and keep a lab notes file.

{m['body'].strip()}

## Common mistakes

{pits}

## Exercises

Work in `exercises/{m['slug']}/`. Read that folder's `README.md` before coding.

```bash
cd exercises/{m['slug']}
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```
{guide_block}
### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/{m['slug']}/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

{checks}

## Further reading

{reads}
"""


HARNESS = """#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
pass=0
fail=0
assert_eq() {{
  # Assign after `local` so values like -n are not parsed as local(1) flags.
  local got want msg
  got=$1
  want=$2
  msg=${{3:-}}
  if [[ "$got" == "$want" ]]; then
    pass=$((pass + 1))
  else
    echo "FAIL $msg: got='$got' want='$want'" >&2
    fail=$((fail + 1))
  fi
}}
# shellcheck disable=SC1091
source "$ROOT/{src}"
run_tests() {{
{tests}
}}
run_tests
echo "Passed $pass failed $fail"
[[ "$fail" -eq 0 ]]
"""


def write_exercise(m: dict, ex_map: dict):
    slug = m["slug"]
    kind = m["ex_kind"]
    starter, solution, tests = ex_map[kind]
    test_lines = "\n".join(f'  assert_eq "{got}" "{want}"' for got, want in tests)
    for name, body, src in (
        ("exercises", starter, "exercise.sh"),
        ("solutions", solution, "solution.sh"),
    ):
        d = ROOT / name / slug
        d.mkdir(parents=True, exist_ok=True)
        script = "#!/usr/bin/env bash\n" + body + "\n"
        (d / src).write_text(script, encoding="utf-8")
        (d / "test.sh").write_text(
            HARNESS.format(src=src, tests=test_lines),
            encoding="utf-8",
        )
        if name == "exercises":
            (d / "README.md").write_text(exercise_readme(m), encoding="utf-8")
        else:
            (d / "README.md").write_text(
                "Reference solution — look only after attempting.\n\n"
                "Compare, then close and rewrite from memory tomorrow.\n",
                encoding="utf-8",
            )


def write_readme(modules: list[dict]):
    rows = "\n".join(
        f"| {m['n']:02d} | {m['title']} | {m['phase']} | {m['days']} | `pdfs/{m['slug']}.pdf` |"
        for m in modules
    )
    (ROOT / "README.md").write_text(
        f"""# Networking Goodway: Fundamentals to Proficiency

A complete, ordered networking path — twin of `linux-goodway` / `golang-goodway` — packed with **useful commands and examples**.

## Study method

1. Read the PDF and **type the commands**
2. Finish `exercises/NN-slug/` (`./test.sh`) without peeking
3. Compare `solutions/` later; rewrite next day

Track: [`curriculum/PROGRESS.md`](curriculum/PROGRESS.md)

## Lab tips

- Linux VM for `ip`, `ss`, `tcpdump`, firewalls
- macOS OK for `curl`, `dig`, `ping`, OpenSSL
- Only scan/capture systems you are allowed to test

## Layout

```
lessons/  pdfs/  exercises/  solutions/  scripts/build-pdfs.sh
```

## Build PDFs

```bash
brew install pandoc typst
./scripts/build-pdfs.sh
```

## Smoke-test solutions

```bash
./scripts/smoke_test.sh
```

## Curriculum map

| # | Title | Phase | Time | PDF |
|---|-------|-------|------|-----|
{rows}
""",
        encoding="utf-8",
    )


def write_progress(modules: list[dict]):
    lines = ["# Progress tracker\n", "Check boxes after PDF + exercises + rewrite.\n"]
    phase = None
    for m in modules:
        if m["phase"] != phase:
            phase = m["phase"]
            lines.append(f"\n## {phase}\n")
        lines.append(f"- [ ] `{m['slug']}` — {m['title']} ({m['days']})")
    (ROOT / "curriculum").mkdir(exist_ok=True)
    (ROOT / "curriculum" / "PROGRESS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    data = _load("curriculum_data", SCRIPTS / "curriculum_data.py")
    exercises = _load("exercises_data", SCRIPTS / "exercises_data.py")
    modules = sorted(data.MODULES, key=lambda m: m["n"])
    if len(modules) != 56:
        raise SystemExit(f"expected 56 modules, got {len(modules)}")
    miss = [m["ex_kind"] for m in modules if m["ex_kind"] not in exercises.EX]
    if miss:
        raise SystemExit(f"missing exercise kinds: {miss}")

    for m in modules:
        d = ROOT / "lessons" / m["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "lesson.md").write_text(lesson_md(m), encoding="utf-8")
        write_exercise(m, exercises.EX)

    write_readme(modules)
    write_progress(modules)
    (ROOT / "pdfs").mkdir(exist_ok=True)
    (ROOT / "pdfs" / ".gitkeep").write_text("", encoding="utf-8")
    print(f"Wrote {len(modules)} lessons + exercises/solutions")


if __name__ == "__main__":
    main()
