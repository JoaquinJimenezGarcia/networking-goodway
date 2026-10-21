# Exercise: 28. HTTP/2, HTTP/3, and QUIC Awareness

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Know why HTTP/2 multiplexes
- Understand QUIC runs on UDP
- Probe protocol with curl
- Relate to CDNs

## Task

Edit `exercise.sh` and implement `curl_http_version_writeout`, `http3_transport`, `http3_udp_port`. Each function is a tiny retrieval drill for **HTTP/2, HTTP/3, and QUIC Awareness** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/28-http2-quic/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `curl_http_version_writeout` → `%{http_version}`; `http3_transport` → `QUIC`; `http3_udp_port` → `443`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/28-http2-quic/`.**
