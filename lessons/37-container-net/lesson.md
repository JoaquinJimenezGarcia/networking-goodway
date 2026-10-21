---
title: "37. Container Networking: Bridge, CNI, localhost Traps"
---

# 37. Container Networking: Bridge, CNI, localhost Traps

**Phase:** Phase 12 — Cloud, containers, and modern nets  
**Estimated time:** 2 days  
**Slug:** `37-container-net`

## Learning objectives

- Explain docker bridge basics
- Publish ports correctly
- Debug DNS inside containers
- Avoid localhost confusion

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.
Type every command yourself and keep a lab notes file.

## Why this matters

Health check to `localhost` inside a container always passes while the published port is dead. Bridge/CNI/`localhost` traps are container networking 101.

## Core concepts

What you must be able to explain:

- Explain docker bridge basics
- Publish ports correctly
- Debug DNS inside containers
- Avoid localhost confusion

Mental model for `37-container-net` (exercise kind `docker_localhost`):

- Prefer **measurable** checks (exit codes, ICMP replies, DNS rcode, HTTP status, socket state) over vibes.
- Separate **reachability** (can packets flow?) from **correctness** (right service, cert, route, identity).
- Ask: *which layer's tool falsifies my current hypothesis?* Then run that tool.
- Record the exact command that proved the root cause — that becomes your playbook snippet.

## Worked commands

Run these on a lab host. Linux VM preferred for `ip`/`ss`/`tcpdump`/`nft`; macOS is fine for many `curl`/`dig`/`ping` drills. Your addresses and timings will differ — match the *shape* of the output and the conclusion you draw.

### Example 1

```bash
docker network ls 2>/dev/null; ip -br addr | head
# kubectl get svc,ep -A 2>/dev/null | head
```

Sample output:

```text
NETWORK ID ... bridge ...
eth0 ... 10.0.0.5/24
cni0 ... 10.244.0.1/24
```

**Interpretation:** Bridge/CNI interfaces explain why `localhost` inside a container is not the host — classic false-positive health check.

### Example 2

```bash
getent hosts kubernetes.default.svc.cluster.local 2>/dev/null || echo 'CoreDNS path: svc.namespace.svc.cluster.local'
```

Sample output:

```text
10.96.0.1 kubernetes.default.svc.cluster.local
```

**Interpretation:** Cluster DNS (CoreDNS) answers service names. Wrong search domain → NXDOMAIN that works with FQDN.

### Example 3

```bash
# Cloud mental model (AWS-style)
echo 'public subnet → IGW; private subnet egress → NAT gateway; SG stateful; NACL stateless'
```

Sample output:

```text
private_subnet_egress_via=NAT-gateway
```

**Interpretation:** Route tables decide egress path. Security groups dropping return traffic look like timeouts.


## Mini-lab

1. Re-type every worked command for **Container Networking: Bridge, CNI, localhost Traps** and paste outputs into lab notes.
2. Introduce one controlled failure in the lab (wrong DNS, firewall drop, bad route) and recover using only this lesson's tools.
3. Write a 5-line playbook: symptom → first command → expected healthy output.
4. Complete the exercise stubs; then explain each function's return value without looking.

## Failure modes

| Symptom | Likely cause | Next check |
|---------|--------------|------------|
| --network host as default | See common mistakes | Re-run lesson commands |
| Assuming container DNS equals host DN... | See common mistakes | Re-run lesson commands |
| Publishing all ports broadly | See common mistakes | Re-run lesson commands |
| Timeout with no RST | Silent drop / blackhole | tcpdump + compare path |

## Study tip for Container Networking: Bridge, CNI, localhost Traps

Before each new command, write a one-line hypothesis. If the result falsifies it, update the hypothesis instead of stacking random tools. Note equivalents across OS (`ip` ↔ `ifconfig`/`route`, `ss` ↔ `netstat`). Re-run two commands from this lesson tomorrow from memory and explain the sample outputs out loud.

## Evidence habit

When pages are down, prefer evidence (`ip route get`, resolver answer, packet capture, listener list) over intuition. Document **command → output → conclusion** in a lab notebook so the same path is reusable on-call. Change one variable at a time; write a one-line hypothesis before each new tool.

## Common mistakes

- --network host as default
- Assuming container DNS equals host DNS always
- Publishing all ports broadly

## Exercises

Work in `exercises/37-container-net/`. Read that folder's `README.md` before coding.

```bash
cd exercises/37-container-net
chmod +x test.sh exercise.sh 2>/dev/null || true
./test.sh
```

### What you will build

Edit `exercise.sh` and implement `localhost_in_container_is`, `docker_default_network`, `container_net_plugin_model`. Each function is a tiny retrieval drill for **Container Networking: Bridge, CNI, localhost Traps** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

### Study loop

- **A (Drill):** make tests pass
- **B (Apply):** run 2–3 real commands from this lesson in your lab and note outputs
- **C (Challenge):** rewrite answers from memory next day

**Do not open `solutions/37-container-net/` until after an honest attempt.**

## Self-check

Answer without scrolling up:

1. localhost in container means?
2. -p 8080:80 meaning?
3. docker network ls purpose?

## Further reading

- https://docs.docker.com/network/
