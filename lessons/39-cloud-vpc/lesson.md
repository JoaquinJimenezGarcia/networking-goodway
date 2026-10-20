---
title: "39. Cloud VPCs: Subnets, Route Tables, Gateways"
---

# 39. Cloud VPCs: Subnets, Route Tables, Gateways

**Phase:** Phase 12 — Cloud, containers, and modern nets  
**Estimated time:** 2 days  
**Slug:** `39-cloud-vpc`

## Learning objectives

- Map VPC/subnet/route table/IGW/NAT
- Design public vs private subnets
- Avoid overlapping CIDRs for peering
- Read cloud route tables like `ip route`

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Mental model maps cleanly to Linux routing:

- Route table → `ip route`
- SG/NACL → host/network firewalls
- NAT gateway → SNAT egress
- IGW → public path

```bash
# From a cloud VM
ip route
curl -4 ifconfig.me
# AWS metadata example (know IMDSv2!) — prefer cloud CLI offline study if unsure
```

Always plan non-overlapping CIDRs for future peering/VPN.

## Common mistakes

- All subnets public
- Overlapping 10.0.0.0/8 everywhere
- No egress strategy for private subnets

## Exercises

Work in `exercises/39-cloud-vpc/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/39-cloud-vpc/` until after an honest attempt.**

## Self-check

1. Private subnet egress via?
2. Why non-overlapping CIDRs?
3. SG stateful meaning roughly?

## Further reading

- https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
