---
title: "12. DNS Basics: Resolvers, Records, dig"
---

# 12. DNS Basics: Resolvers, Records, dig

**Phase:** Phase 4 — DNS  
**Estimated time:** 2 days  
**Slug:** `12-dns-basics`

## Learning objectives

- Query A/AAAA/CNAME/MX/TXT/NS
- Explain recursive vs authoritative
- Use dig/drill/nslookup
- Read TTL and caching implications

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
dig example.com A +short
dig example.com AAAA +short
dig example.com NS +short
dig example.com MX +short
dig example.com TXT +short
dig www.github.com CNAME +short

dig example.com +noall +answer
dig @1.1.1.1 example.com A
dig example.com +trace                 # walk from root (noisy)

# reverse DNS
dig -x 1.1.1.1 +short

# see full timing
dig example.com | grep -E 'Query time|SERVER'
```

```bash
# macOS/Linux alternatives
host example.com
nslookup example.com
getent hosts example.com
```

## Common mistakes

- Flushing caches randomly as first step
- Ignoring TTL when debugging 'still old IP'
- Using +trace against rate-limited networks carelessly

## Exercises

Work in `exercises/12-dns-basics/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/12-dns-basics/` until after an honest attempt.**

## Self-check

1. dig for AAAA?
2. What is +short?
3. Recursive vs authoritative?

## Further reading

- https://www.rfc-editor.org/rfc/rfc1035
