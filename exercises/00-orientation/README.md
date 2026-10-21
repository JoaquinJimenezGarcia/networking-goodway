# Exercise: 00. Orientation: How Networks Work and How to Practice

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain clients, servers, packets, and protocols at a beginner level
- Set up a safe practice lab (VM + localhost tools)
- Adopt attempt → struggle → solution → rewrite
- Know which tools you will use daily

## Task

Implement three helpers: `greet` (friendly hello), `daily_tool_count_min` (minimum toolkit size taught: 5), and `study_loop` (the four-step practice phrase). Comments above each function should say *when* you use the idea on-call.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/00-orientation/` | Peek only after a real attempt |

## Examples / expected behavior

`greet Net` → `Hello, Net`. `daily_tool_count_min` → `5`. `study_loop` → `attempt-struggle-solution-rewrite`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/00-orientation/`.**
