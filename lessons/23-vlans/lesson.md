---
title: "23. VLANs and Trunking Concepts"
---

# 23. VLANs and Trunking Concepts

**Phase:** Phase 7 — L2, switching, and local nets  
**Estimated time:** 1–2 days  
**Slug:** `23-vlans`

## Learning objectives

- Explain VLAN segmentation
- Understand access vs trunk ports
- Know 802.1Q tagging idea
- See VLAN subinterfaces on Linux

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
# Linux VLAN subinterface example (lab)
sudo ip link add link eth0 name eth0.20 type vlan id 20
sudo ip addr add 10.20.0.10/24 dev eth0.20
sudo ip link set eth0.20 up
ip -d link show eth0.20
```

VLANs split broadcast domains — security/ops boundary, not magic encryption.

## Common mistakes

- Using VLANs as only security control
- Native VLAN mismatches
- Overlapping IP plans across VLANs without routing

## Exercises

Work in `exercises/23-vlans/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/23-vlans/` until after an honest attempt.**

## Self-check

1. Access vs trunk?
2. 802.1Q does what?
3. Do VLANs encrypt?

## Further reading

- https://www.rfc-editor.org/rfc/rfc3069
