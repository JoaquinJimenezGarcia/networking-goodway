# Exercise: 47. Zero Trust Networking Ideas

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Move beyond flat VPN trust
- Prefer identity-aware access
- Least privilege paths
- Combine device posture + user identity

## Task

Edit `exercise.sh` and implement `zero_trust_rejects`, `verify_every_request`, `prefer_identity_or_location`. Each function is a tiny retrieval drill for **Zero Trust Networking Ideas** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/47-zero-trust/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `zero_trust_rejects` → `location-only-trust`; `verify_every_request` → `yes`; `prefer_identity_or_location` → `identity`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/47-zero-trust/`.**
