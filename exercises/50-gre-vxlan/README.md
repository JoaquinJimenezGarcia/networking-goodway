# Exercise: 50. Tunnels: GRE/VXLAN Overlay Awareness

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain overlays vs underlays
- Know VXLAN for multi-tenant/datacenter
- See Linux vxlan devices
- Relate to cloud SDN

## Task

Edit `exercise.sh` and implement `vxlan_is_an`, `vxlan_over`, `gre_is_a`. Each function is a tiny retrieval drill for **Tunnels: GRE/VXLAN Overlay Awareness** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/50-gre-vxlan/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `vxlan_is_an` → `overlay`; `vxlan_over` → `UDP`; `gre_is_a` → `tunnel`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/50-gre-vxlan/`.**
