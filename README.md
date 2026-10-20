# Networking Goodway: Fundamentals to Proficiency

A complete, ordered networking path — twin of `linux-goodway` / `golang-goodway` — packed with **useful commands and examples**.

## Study method

1. Read the PDF and **type the commands**
2. Finish `exercises/NN-slug/` (`./test.sh`) without peeking
3. Compare `solutions/` later; rewrite next day

Track: [`curriculum/PROGRESS.md`](curriculum/PROGRESS.md)

## Lab tips

- Linux VM for `ip`, `ss`, `tcpdump`, firewalls
- macOS OK for `curl`, `dig`, `ping`, OpenSSL
- Only scan/capture systems you are allowed to test

## Layout

```
lessons/  pdfs/  exercises/  solutions/  scripts/build-pdfs.sh
```

## Build PDFs

```bash
brew install pandoc typst
./scripts/build-pdfs.sh
```

## Smoke-test solutions

```bash
./scripts/smoke_test.sh
```

## Curriculum map

| # | Title | Phase | Time | PDF |
|---|-------|-------|------|-----|
| 00 | Orientation: How Networks Work and How to Practice | Phase 0 — Orientation | 1 day | `pdfs/00-orientation.pdf` |
| 01 | OSI vs TCP/IP Models (with packet walkthrough) | Phase 1 — Models and packets | 1–2 days | `pdfs/01-osi-tcpip.pdf` |
| 02 | Encapsulation, Headers, and MTU | Phase 1 — Models and packets | 1–2 days | `pdfs/02-encapsulation.pdf` |
| 03 | Ethernet, MAC Addresses, and ARP | Phase 7 — L2, switching, and local nets | 1–2 days | `pdfs/03-ethernet-mac-arp.pdf` |
| 04 | IPv4 Basics: Addresses, Classes Myth, Private Ranges | Phase 2 — Addressing and subnets | 1–2 days | `pdfs/04-ipv4-basics.pdf` |
| 05 | Subnetting and CIDR (with practice) | Phase 2 — Addressing and subnets | 2–3 days | `pdfs/05-subnetting.pdf` |
| 06 | IPv6 Basics and Dual-Stack Commands | Phase 2 — Addressing and subnets | 1–2 days | `pdfs/06-ipv6-basics.pdf` |
| 07 | The ip Command Deep Dive (addr, link, route) | Phase 3 — Host networking toolkit | 2 days | `pdfs/07-ip-command.pdf` |
| 08 | ping, traceroute/mtr, and Path Diagnosis | Phase 3 — Host networking toolkit | 1–2 days | `pdfs/08-ping-traceroute.pdf` |
| 09 | ss, netstat, and lsof: See What Is Listening | Phase 3 — Host networking toolkit | 1–2 days | `pdfs/09-ss-netstat-lsof.pdf` |
| 10 | nc/ncat and socat: Swiss Army Networking | Phase 3 — Host networking toolkit | 1–2 days | `pdfs/10-nc-socat.pdf` |
| 11 | TCP vs UDP, Handshakes, and Reliability | Phase 1 — Models and packets | 1–2 days | `pdfs/11-tcp-udp.pdf` |
| 12 | DNS Basics: Resolvers, Records, dig | Phase 4 — DNS | 2 days | `pdfs/12-dns-basics.pdf` |
| 13 | DNS Debugging: NXDOMAIN, SERVFAIL, Split-Horizon | Phase 4 — DNS | 1–2 days | `pdfs/13-dns-debug.pdf` |
| 14 | HTTP from the CLI: curl Mastery | Phase 5 — HTTP, TLS, and APIs | 2 days | `pdfs/14-http-basics.pdf` |
| 15 | TLS, Certificates, and openssl s_client | Phase 5 — HTTP, TLS, and APIs | 2 days | `pdfs/15-tls-openssl.pdf` |
| 16 | Routing Tables and Default Gateways | Phase 6 — Routing | 1–2 days | `pdfs/16-routing-basics.pdf` |
| 17 | Static vs Dynamic Routing Concepts | Phase 6 — Routing | 1–2 days | `pdfs/17-static-dynamic-routing.pdf` |
| 18 | NAT, PAT, and Hairpinning | Phase 8 — Firewalls, NAT, and policy | 1–2 days | `pdfs/18-nat.pdf` |
| 19 | Host Firewalls: nftables, iptables, ufw | Phase 8 — Firewalls, NAT, and policy | 2 days | `pdfs/19-firewall-linux.pdf` |
| 20 | tcpdump Basics for Engineers | Phase 11 — Observability and troubleshooting | 2 days | `pdfs/20-tcpdump-basics.pdf` |
| 21 | Reading Flows: Wireshark/tshark Essentials | Phase 11 — Observability and troubleshooting | 1–2 days | `pdfs/21-wireshark-flow.pdf` |
| 22 | DHCP and Address Assignment | Phase 7 — L2, switching, and local nets | 1 day | `pdfs/22-dhcp.pdf` |
| 23 | VLANs and Trunking Concepts | Phase 7 — L2, switching, and local nets | 1–2 days | `pdfs/23-vlans.pdf` |
| 24 | VPN Basics: IPsec, WireGuard, OpenVPN | Phase 9 — VPN, tunnels, and overlays | 2 days | `pdfs/24-vpn-basics.pdf` |
| 25 | SSH Tunnels and Port Forwards | Phase 9 — VPN, tunnels, and overlays | 1–2 days | `pdfs/25-ssh-tunnels.pdf` |
| 26 | Load Balancing Concepts and Health Checks | Phase 10 — Load balancing and proxies | 1–2 days | `pdfs/26-load-balancing.pdf` |
| 27 | Reverse Proxies: TLS Termination and Headers | Phase 10 — Load balancing and proxies | 1–2 days | `pdfs/27-reverse-proxy.pdf` |
| 28 | HTTP/2, HTTP/3, and QUIC Awareness | Phase 5 — HTTP, TLS, and APIs | 1 day | `pdfs/28-http2-quic.pdf` |
| 29 | CDNs, Caching, and Cache Headers | Phase 10 — Load balancing and proxies | 1–2 days | `pdfs/29-cdn-caching.pdf` |
| 30 | Latency, Bandwidth, Loss, and QoS Basics | Phase 11 — Observability and troubleshooting | 1–2 days | `pdfs/30-qos-traffic.pdf` |
| 31 | Scanning Basics with nmap (Lab Only) | Phase 11 — Observability and troubleshooting | 1–2 days | `pdfs/31-nmap-basics.pdf` |
| 32 | How the Internet Routes: BGP at a Glance | Phase 6 — Routing | 1–2 days | `pdfs/32-bgp-internet.pdf` |
| 33 | Anycast, GeoDNS, and Global Traffic | Phase 10 — Load balancing and proxies | 1 day | `pdfs/33-anycast-dns-cdn.pdf` |
| 34 | Email Networking: MX, SPF, DKIM, DMARC | Phase 4 — DNS | 1–2 days | `pdfs/34-email-dns.pdf` |
| 35 | Time Sync and Why Networks Care | Phase 11 — Observability and troubleshooting | 1 day | `pdfs/35-ntp-time.pdf` |
| 36 | Wi-Fi Networking Essentials | Phase 7 — L2, switching, and local nets | 1 day | `pdfs/36-wireless-basics.pdf` |
| 37 | Container Networking: Bridge, CNI, localhost Traps | Phase 12 — Cloud, containers, and modern nets | 2 days | `pdfs/37-container-net.pdf` |
| 38 | Kubernetes Networking Concepts for Engineers | Phase 12 — Cloud, containers, and modern nets | 2 days | `pdfs/38-kubernetes-net.pdf` |
| 39 | Cloud VPCs: Subnets, Route Tables, Gateways | Phase 12 — Cloud, containers, and modern nets | 2 days | `pdfs/39-cloud-vpc.pdf` |
| 40 | Security Groups vs NACLs vs Host Firewalls | Phase 8 — Firewalls, NAT, and policy | 1–2 days | `pdfs/40-security-groups.pdf` |
| 41 | mTLS and Service Identity Intro | Phase 5 — HTTP, TLS, and APIs | 1–2 days | `pdfs/41-tls-mtls.pdf` |
| 42 | DNSSEC and DNS Security Awareness | Phase 4 — DNS | 1 day | `pdfs/42-dns-dnssec.pdf` |
| 43 | Network Observability: Metrics, Logs, Traces | Phase 11 — Observability and troubleshooting | 1–2 days | `pdfs/43-observability-net.pdf` |
| 44 | Networking Troubleshooting Playbook | Phase 11 — Observability and troubleshooting | 2 days | `pdfs/44-troubleshooting-playbook.pdf` |
| 45 | Host Network Performance Tuning Intro | Phase 11 — Observability and troubleshooting | 1–2 days | `pdfs/45-performance-tuning.pdf` |
| 46 | API Gateways and Edge Patterns | Phase 10 — Load balancing and proxies | 1–2 days | `pdfs/46-api-gateways.pdf` |
| 47 | Zero Trust Networking Ideas | Phase 9 — VPN, tunnels, and overlays | 1 day | `pdfs/47-zero-trust.pdf` |
| 48 | Lab: Build a Mini Network Path | Phase 0 — Orientation | 2 days | `pdfs/48-lab-packet.pdf` |
| 49 | Command Cheatsheet Consolidation Drill | Phase 3 — Host networking toolkit | 1–2 days | `pdfs/49-command-cheatsheet.pdf` |
| 50 | Tunnels: GRE/VXLAN Overlay Awareness | Phase 9 — VPN, tunnels, and overlays | 1–2 days | `pdfs/50-gre-vxlan.pdf` |
| 51 | Firewalls, Middleboxes, and Modern Protocols | Phase 8 — Firewalls, NAT, and policy | 1 day | `pdfs/51-quic-firewall.pdf` |
| 52 | Networking Interview & Oncall Drills | Phase 11 — Observability and troubleshooting | 2 days | `pdfs/52-interview-net.pdf` |
| 53 | Capstone: Multi-Host Lab Network | Phase 13 — Capstones | 3–5 days | `pdfs/53-capstone-lab-net.pdf` |
| 54 | Capstone: Broken Network Challenge | Phase 13 — Capstones | 2–4 days | `pdfs/54-capstone-debug.pdf` |
| 55 | Capstone: Secure Edge for a Small App | Phase 13 — Capstones | 4–6 days | `pdfs/55-capstone-edge.pdf` |
