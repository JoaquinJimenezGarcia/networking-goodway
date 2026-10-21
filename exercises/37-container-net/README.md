# Exercise: 37. Container Networking: Bridge, CNI, localhost Traps

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain docker bridge basics
- Publish ports correctly
- Debug DNS inside containers
- Avoid localhost confusion

## Task

Edit `exercise.sh` and implement `localhost_in_container_is`, `docker_default_network`, `container_net_plugin_model`. Each function is a tiny retrieval drill for **Container Networking: Bridge, CNI, localhost Traps** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/37-container-net/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `localhost_in_container_is` → `the-container`; `docker_default_network` → `bridge`; `container_net_plugin_model` → `CNI`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/37-container-net/`.**
