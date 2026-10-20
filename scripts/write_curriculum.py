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


def lesson_md(m: dict) -> str:
    objs = "\n".join(f"- {o}" for o in m["objectives"])
    pits = "\n".join(f"- {p}" for p in m["pitfalls"])
    checks = "\n".join(f"{i}. {c}" for i, c in enumerate(m["checks"], 1))
    reads = "\n".join(f"- {r}" for r in m["reading"])
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

{m['body'].strip()}

## Common mistakes

{pits}

## Exercises

Work in `exercises/{m['slug']}/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/{m['slug']}/` until after an honest attempt.**

## Self-check

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
  local got=$1 want=$2 msg=${{3:-}}
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


def write_exercise(slug: str, kind: str, ex_map: dict):
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
            (d / "README.md").write_text(
                "Edit `exercise.sh`, then run `./test.sh`.\n", encoding="utf-8"
            )
        else:
            (d / "README.md").write_text(
                "Reference solution — look only after attempting.\n", encoding="utf-8"
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
        write_exercise(m["slug"], m["ex_kind"], exercises.EX)

    write_readme(modules)
    write_progress(modules)
    (ROOT / "pdfs").mkdir(exist_ok=True)
    (ROOT / "pdfs" / ".gitkeep").write_text("", encoding="utf-8")
    print(f"Wrote {len(modules)} lessons + exercises/solutions")


if __name__ == "__main__":
    main()
