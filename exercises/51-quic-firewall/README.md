# Exercise: 51. Firewalls, Middleboxes, and Modern Protocols

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Know middleboxes can break UDP/QUIC
- Test fallbacks
- Design allowlists for new protocols
- Document egress needs

## Task

Edit `exercise.sh` and implement `http3_uses_udp_port`, `broken_by_tcp_assume`, `allowlist_tcp_blocks`. Each function is a tiny retrieval drill for **Firewalls, Middleboxes, and Modern Protocols** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/51-quic-firewall/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `http3_uses_udp_port` → `443`; `broken_by_tcp_assume` → `QUIC`; `allowlist_tcp_blocks` → `UDP`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/51-quic-firewall/`.**
