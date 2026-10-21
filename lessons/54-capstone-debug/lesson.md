---
title: "54. Capstone: Broken Network Challenge"
---

# 54. Capstone: Broken Network Challenge

**Phase:** Phase 13 — Capstones  
**Estimated time:** 2–4 days  
**Slug:** `54-capstone-debug`

## Learning objectives

- Debug planted failures
- Produce timeline + root cause
- Fix with minimal change
- Write postmortem

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.
Type every command yourself and keep a lab notes file.

## Why this matters

Someone broke the lab on purpose. Debug with evidence only — no config archaeology until measurements demand it.

## Core concepts

What you must be able to explain:

- Debug planted failures
- Produce timeline + root cause
- Fix with minimal change
- Write postmortem

Mental model for `54-capstone-debug` (exercise kind `cap_break`):

- Prefer **measurable** checks (exit codes, ICMP replies, DNS rcode, HTTP status, socket state) over vibes.
- Separate **reachability** (can packets flow?) from **correctness** (right service, cert, route, identity).
- Ask: *which layer's tool falsifies my current hypothesis?* Then run that tool.
- Record the exact command that proved the root cause — that becomes your playbook snippet.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
ping -c 2 1.1.1.1; dig example.com +short; curl -sS -o /dev/null -w '%{http_code}\n' https://example.com; ss -tln | head
```

Sample output:

```text
icmp ok / A record / 200 / LISTEN lines
```

**Interpretation:** Playbook order: local stack → L3 → DNS → L4 listen/connect → L7. Capstones and interviews reward this sequence.

### Example 2

```bash
ip route get 1.1.1.1; traceroute -n 1.1.1.1 2>/dev/null | head -4 || true
```

Sample output:

```text
1.1.1.1 via 192.168.1.1 dev eth0 src 192.168.1.20
1 192.168.1.1
```

**Interpretation:** `ip route get` is the fastest 'which path would this host take?' check on Linux.

### Example 3

```bash
curl -sS -o /dev/null -w 'namelookup=%{time_namelookup} connect=%{time_connect} ttfb=%{time_starttransfer}\n' https://example.com
```

Sample output:

```text
namelookup=0.020 connect=0.040 ttfb=0.120
```

**Interpretation:** Percentiles beat averages for latency SLOs; single curl samples teach which phase dominates.


## Mini-lab

1. Re-type every worked command for **Capstone: Broken Network Challenge** and paste outputs into lab notes.
2. Introduce one controlled failure in the lab (wrong DNS, firewall drop, bad route) and recover using only this lesson's tools.
3. Write a 5-line playbook: symptom → first command → expected healthy output.
4. Complete the exercise stubs; then explain each function's return value without looking.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| Recreate VMs instead of debugging | See common mistakes | Re-run lesson commands |
| Changing everything | See common mistakes | Re-run lesson commands |
| No postmortem | See common mistakes | Re-run lesson commands |
| Timeout with no RST | Silent drop / blackhole | tcpdump + compare path |

## Study tip for Capstone: Broken Network Challenge

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Recreate VMs instead of debugging
- Changing everything
- No postmortem

## Exercises

Work in `exercises/54-capstone-debug/`. Read that folder's `README.md` before coding.

```bash
cd exercises/54-capstone-debug
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Edit `exercise.sh` and implement `postmortem_must_include`, `postmortem_timeline`, `postmortem_verify`. Each function is a tiny retrieval drill for **Capstone: Broken Network Challenge** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/54-capstone-debug/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. Root cause?
2. Evidence?
3. Prevention?

## Further reading

- https://sre.google/sre-book/postmortem-culture/
