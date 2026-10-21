# Exercise: 23. VLANs and Trunking Concepts

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Explain VLAN segmentation
- Understand access vs trunk ports
- Know 802.1Q tagging idea
- See VLAN subinterfaces on Linux

## Task

Edit `exercise.sh` and implement `vlan_tag_standard`, `multi_vlan_port`, `l2_segment_feature`. Each function is a tiny retrieval drill for **VLANs and Trunking Concepts** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/23-vlans/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `vlan_tag_standard` → `802.1Q`; `multi_vlan_port` → `trunk`; `l2_segment_feature` → `VLAN`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/23-vlans/`.**
