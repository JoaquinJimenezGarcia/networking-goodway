# Exercise: 17. Static vs Dynamic Routing Concepts

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Contrast static routes vs OSPF/BGP ideas
- Know when static is enough
- Explain convergence at a high level
- Read simple BGP/OSPF vocabulary

## Task

Edit `exercise.sh` and implement `internet_routing_protocol`, `igp_example`, `operator_routes`. Each function is a tiny retrieval drill for **Static vs Dynamic Routing Concepts** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/17-static-dynamic-routing/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `internet_routing_protocol` → `BGP`; `igp_example` → `OSPF`; `operator_routes` → `static`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/17-static-dynamic-routing/`.**
