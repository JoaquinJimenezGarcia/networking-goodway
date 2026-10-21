# Exercise: 24. VPN Basics: IPsec, WireGuard, OpenVPN

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Contrast VPN types at a high level
- Read WireGuard quick configs conceptually
- Troubleshoot VPN DNS and routes
- Watch MTU/overhead issues

## Task

Edit `exercise.sh` and implement `vpn_often_lowers`, `modern_vpn_example`, `classic_vpn_suite`. Each function is a tiny retrieval drill for **VPN Basics: IPsec, WireGuard, OpenVPN** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/24-vpn-basics/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `vpn_often_lowers` → `MTU`; `modern_vpn_example` → `WireGuard`; `classic_vpn_suite` → `IPsec`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/24-vpn-basics/`.**
