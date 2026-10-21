# Exercise: 11. TCP vs UDP, Handshakes, and Reliability

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Contrast TCP and UDP properties
- Explain three-way handshake conceptually
- Know when UDP is preferred
- Observe TCP with ss/tcpdump

## Task

Edit `exercise.sh` and implement `reliable_transport`, `datagram_transport`, `tcp_first_flag`. Each function is a tiny retrieval drill for **TCP vs UDP, Handshakes, and Reliability** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/11-tcp-udp/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `reliable_transport` → `TCP`; `datagram_transport` → `UDP`; `tcp_first_flag` → `SYN`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/11-tcp-udp/`.**
