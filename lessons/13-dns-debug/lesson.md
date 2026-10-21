---
title: "13. DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon"
---

# 13. DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon

**Phase:** Phase 4 — DNS  
**Estimated time:** 1–2 days  
**Slug:** `13-dns-debug`

## Learning objectives

- Differentiate NXDOMAIN vs timeout vs SERVFAIL
- Inspect /etc/resolv.conf and systemd-resolved
- Debug search domains
- Handle private DNS vs public DNS conflicts

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.
Type every command yourself and keep a lab notes file.

## Why this matters

One office gets NXDOMAIN, another gets the old A record, CI gets SERVFAIL. Split-horizon, cache poisoning of your brain (stale TTL), and upstream SERVFAIL need different fixes.

## Core concepts

What you must be able to explain:

- Differentiate NXDOMAIN vs timeout vs SERVFAIL
- Inspect /etc/resolv.conf and systemd-resolved
- Debug search domains
- Handle private DNS vs public DNS conflicts

Mental model for `13-dns-debug` (exercise kind `dns_nx`):

- Prefer **measurable** checks (exit codes, ICMP replies, DNS rcode, HTTP status, socket state) over vibes.
- Separate **reachability** (can packets flow?) from **correctness** (right service, cert, route, identity).
- Ask: *which layer's tool falsifies my current hypothesis?* Then run that tool.
- Record the exact command that proved the root cause — that becomes your playbook snippet.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
dig example.com A +short
dig example.com AAAA +short
dig example.com NS +short
```

Sample output:

```text
93.184.216.34
2606:2800:220:1:248:1893:25c8:1946
a.iana-servers.net.
```

**Interpretation:** A/AAAA/NS answers show what clients may use. Empty AAAA is not always an error on IPv4-only paths.

### Example 2

```bash
dig @1.1.1.1 example.com +noall +answer +stats
```

Sample output:

```text
example.com. 300 IN A 93.184.216.34
;; Query time: 18 msec
;; SERVER: 1.1.1.1#53
```

**Interpretation:** Pinning `@resolver` removes 'which stub resolver?' ambiguity. Query time and SERVER lines matter when comparing sites.

### Example 3

```bash
dig not-a-real-xyz.invalid A +noall +comments 2>/dev/null | head -20
```

Sample output:

```text
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: ...
```

**Interpretation:** NXDOMAIN means the name does not exist at the queried view — different from timeout or SERVFAIL.


## Mini-lab

1. Re-type every worked command for **DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon** and paste outputs into lab notes.
2. Introduce one controlled failure in the lab (wrong DNS, firewall drop, bad route) and recover using only this lesson's tools.
3. Write a 5-line playbook: symptom → first command → expected healthy output.
4. Complete the exercise stubs; then explain each function's return value without looking.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| Pointing corp laptops at 8.8.8.8 and ... | See common mistakes | Re-run lesson commands |
| Ignoring search domain appending | See common mistakes | Re-run lesson commands |
| Hardcoding IPs forever instead of fix... | See common mistakes | Re-run lesson commands |
| Timeout with no RST | Silent drop / blackhole | tcpdump + compare path |

## Study tip for DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Pointing corp laptops at 8.8.8.8 and breaking private zones
- Ignoring search domain appending
- Hardcoding IPs forever instead of fixing DNS

## Exercises

Work in `exercises/13-dns-debug/`. Read that folder's `README.md` before coding.

```bash
cd exercises/13-dns-debug
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Edit `exercise.sh` and implement `nxdomain_means`, `servfail_means`, `split_dns_name`. Each function is a tiny retrieval drill for **DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/13-dns-debug/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. NXDOMAIN meaning?
2. SERVFAIL meaning?
3. Why VPN DNS matters?

## Further reading

- https://man7.org/linux/man-pages/man5/resolv.conf.5.html
