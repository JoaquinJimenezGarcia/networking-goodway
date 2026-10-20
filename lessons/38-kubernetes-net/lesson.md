---
title: "38. Kubernetes Networking Concepts for Engineers"
---

# 38. Kubernetes Networking Concepts for Engineers

**Phase:** Phase 12 — Cloud, containers, and modern nets  
**Estimated time:** 2 days  
**Slug:** `38-kubernetes-net`

## Learning objectives

- Pod/Service/ClusterIP/NodePort/Ingress ideas
- kubectl network debugging basics
- CoreDNS importance
- NetworkPolicy awareness

## Prerequisites

Complete prior lessons. Prefer a Linux VM for `ip`/`ss`/`nft` examples; macOS works for many `curl`/`dig` drills.

```bash
kubectl get svc -A
kubectl get endpoints -A | head
kubectl -n kube-system get pods -l k8s-app=kube-dns
kubectl run netshoot --rm -it --image=nicolaka/netshoot -- /bin/bash
# inside: dig kubernetes.default.svc.cluster.local; curl svcname
kubectl exec -it deploy/myapp -- ss -tulpn
```

If DNS in cluster breaks, "everything is broken". NetworkPolicies can deny silently.

## Common mistakes

- kubectl apply without understanding Services
- Using NodePort on cloud without LB
- Flat allow-all policies forever

## Exercises

Work in `exercises/38-kubernetes-net/`:

```bash
./test.sh
```

- **A:** make tests pass
- **B:** run 2–3 real commands from this lesson in your lab and note outputs
- **C:** rewrite answers from memory next day

**Do not open `solutions/38-kubernetes-net/` until after an honest attempt.**

## Self-check

1. ClusterIP purpose?
2. CoreDNS role?
3. NetworkPolicy default deny effect?

## Further reading

- https://kubernetes.io/docs/concepts/services-networking/
