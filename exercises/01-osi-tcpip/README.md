# Exercise: 01. OSI vs TCP/IP Models (with packet walkthrough)

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Map OSI layers to TCP/IP layers
- Trace a request layer-by-layer
- Identify which tool inspects which layer
- Stop mixing L2/L3/L4 terms casually

## Task

Implement `layer_for_ports`, `layer_for_mac`, `layer_for_http`, and `tls_rides_on` returning the layer labels taught in the mapping table (L4, L2, L7, TCP).

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/01-osi-tcpip/` | Peek only after a real attempt |

## Examples / expected behavior

`layer_for_ports` → `L4`; `layer_for_mac` → `L2`; `layer_for_http` → `L7`; `tls_rides_on` → `TCP`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/01-osi-tcpip/`.**
