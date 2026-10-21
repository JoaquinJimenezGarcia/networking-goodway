# Exercise: 27. Reverse Proxies: TLS Termination and Headers

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Terminate TLS at proxy
- Pass X-Forwarded-* carefully
- Preserve client IP with real_ip
- Log correctly

## Task

Edit `exercise.sh` and implement `xff_trust_from`, `tls_edge_role`, `proto_forward_header`. Each function is a tiny retrieval drill for **Reverse Proxies: TLS Termination and Headers** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/27-reverse-proxy/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `xff_trust_from` → `trusted-proxies-only`; `tls_edge_role` → `TLS-termination`; `proto_forward_header` → `X-Forwarded-Proto`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/27-reverse-proxy/`.**
