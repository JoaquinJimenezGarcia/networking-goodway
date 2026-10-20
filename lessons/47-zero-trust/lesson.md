---
title: "47. Zero Trust Networking Ideas"
---

# 47. Zero Trust Networking Ideas

**Phase:** Phase 9 — VPN, tunnels, and overlays  
**Estimated time:** 1 day  
**Slug:** `47-zero-trust`

## Learning objectives

- Move beyond flat VPN trust
- Prefer identity-aware access
- Least privilege paths
- Combine device posture + user identity

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

Zero trust: never trust network location alone. Authenticate/authorize continuously.

Practical steps: SSO, short-lived certs, mTLS/mesh, per-service policies, avoid huge flat /16 VPNs with implicit trust.

```bash
# Still verify paths explicitly
curl -I https://internal.example.com
# without VPN / with identity proxy patterns (org-specific)
```

## Common mistakes

- VPN equals secure forever
- Flat allow-all east-west
- Long-lived shared secrets

## Exercises

Work in `exercises/47-zero-trust/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/47-zero-trust/` until after an honest attempt.**

## Self-check

1. Zero trust core idea?
2. Risk of flat VPN?
3. Short-lived creds why?

## Further reading

- https://www.nist.gov/publications/zero-trust-architecture
