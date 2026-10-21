---
title: "25. SSH Tunnels and Port Forwards"
---

# 25. SSH Tunnels and Port Forwards

**Phase:** Phase 9 — VPN, tunnels, and overlays  
**Estimated time:** 1–2 days  
**Slug:** `25-ssh-tunnels`

## Learning objectives

- Use local/remote/dynamic SSH forwards
- Access private admin UIs safely
- Avoid standing tunnels forever without need
- Combine with ProxyJump

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.
Type every command yourself and keep a lab notes file.

## Why this matters

Need a DB on a private host via bastion for five minutes. SSH `-L`/`-R`/`-D` is the tactical tunnel — wrong direction is the usual bug.

## Core concepts

What you must be able to explain:

- Use local/remote/dynamic SSH forwards
- Access private admin UIs safely
- Avoid standing tunnels forever without need
- Combine with ProxyJump

Mental model for `25-ssh-tunnels` (exercise kind `ssh_L`):

- Prefer **measurable** checks (exit codes, ICMP replies, DNS rcode, HTTP status, socket state) over vibes.
- Separate **reachability** (can packets flow?) from **correctness** (right service, cert, route, identity).
- Ask: *which layer's tool falsifies my current hypothesis?* Then run that tool.
- Record the exact command that proved the root cause — that becomes your playbook snippet.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
ip -br link; ip route | head
# After VPN up, compare default route and MTU
```

Sample output:

```text
wg0 UP ...
default via 10.10.0.1 dev wg0
mtu 1420
```

**Interpretation:** Tunnels add outer headers → lower effective MTU. Blackhole PMTUD is a classic VPN failure mode.

### Example 2

```bash
ping -c 2 -M do -s 1472 1.1.1.1 2>&1 | head -5 || ping -c 2 -D -s 1472 1.1.1.1 2>&1 | head -5
```

Sample output:

```text
Frag needed / Message too long / 100% loss
```

**Interpretation:** Large DF probes failing after VPN connect points to MTU/MSS issues — lower MSS/MTU or fix ICMP PTB.

### Example 3

```bash
ssh -N -L 8080:127.0.0.1:80 user@bastion  # example local forward (lab)
echo 'local forward uses -L; remote -R; dynamic -D'
```

Sample output:

```text
(ssh holds open; curl localhost:8080 hits remote :80)
```

**Interpretation:** SSH forwards are tactical tunnels. Know `-L` vs `-R` direction before debugging 'connection refused' on the wrong host.


## Mini-lab

1. Re-type every worked command for **SSH Tunnels and Port Forwards** and paste outputs into lab notes.
2. Introduce one controlled failure in the lab (wrong DNS, firewall drop, bad route) and recover using only this lesson's tools.
3. Write a 5-line playbook: symptom → first command → expected healthy output.
4. Complete the exercise stubs; then explain each function's return value without looking.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| Exposing binds on 0.0.0.0 unintention... | See common mistakes | Re-run lesson commands |
| Long-lived tunnels as permanent VPN s... | See common mistakes | Re-run lesson commands |
| Forgetting ExitOnForwardFailure | See common mistakes | Re-run lesson commands |
| Timeout with no RST | Silent drop / blackhole | tcpdump + compare path |

## Study tip for SSH Tunnels and Port Forwards

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- Exposing binds on 0.0.0.0 unintentionally
- Long-lived tunnels as permanent VPN substitute without review
- Forgetting ExitOnForwardFailure

## Exercises

Work in `exercises/25-ssh-tunnels/`. Read that folder's `README.md` before coding.

```bash
cd exercises/25-ssh-tunnels
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Edit `exercise.sh` and implement `ssh_local_forward_flag`, `ssh_remote_forward_flag`, `ssh_dynamic_flag`. Each function is a tiny retrieval drill for **SSH Tunnels and Port Forwards** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/25-ssh-tunnels/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. -L meaning?
2. -D meaning?
3. ProxyJump purpose?

## Further reading

- https://man.openbsd.org/ssh
