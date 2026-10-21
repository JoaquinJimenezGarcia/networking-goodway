# Exercise: 03. Ethernet, MAC Addresses, and ARP

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Read MAC addresses and ARP tables
- Explain ARP purpose on a LAN
- Detect basic ARP issues
- Use neighbor tables on modern Linux

## Task

Implement `arp_maps` (`IP-to-MAC`), `arp_crosses_routers` (`no`), and `linux_neigh_cmd` (`ip neigh`).

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/03-ethernet-mac-arp/` | Peek only after a real attempt |

## Examples / expected behavior

`arp_maps` → `IP-to-MAC`; `arp_crosses_routers` → `no`; `linux_neigh_cmd` → `ip neigh`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/03-ethernet-mac-arp/`.**
