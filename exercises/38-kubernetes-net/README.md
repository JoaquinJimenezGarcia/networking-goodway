# Exercise: 38. Kubernetes Networking Concepts for Engineers

## Goal

Prove you can **retrieve** the networking ideas from the lesson, not just recognize them while reading.

## Concepts from the lesson

- Pod/Service/ClusterIP/NodePort/Ingress ideas
- kubectl network debugging basics
- CoreDNS importance
- NetworkPolicy awareness

## Task

Edit `exercise.sh` and implement `k8s_cluster_dns`, `k8s_stable_vip_object`, `k8s_policy_sidecar_mesh`. Each function is a tiny retrieval drill for **Kubernetes Networking Concepts for Engineers** — return the exact tokens/flags/labels from the lesson. Keep the comment above each function describing when you would use that fact on-call. Run `./test.sh` until all 3 assertions pass.

## Files

| File | Role |
|------|------|
| `exercise.sh` | Your implementation |
| `test.sh` | Assertions — keep running until exit 0 |
| `../../solutions/38-kubernetes-net/` | Peek only after a real attempt |

## Examples / expected behavior

Expected: `k8s_cluster_dns` → `CoreDNS`; `k8s_stable_vip_object` → `Service`; `k8s_policy_sidecar_mesh` → `mesh`.

## How to work

1. Re-read the lesson sections that name the same ideas as the failing tests.
2. On your lab host, re-run 2–3 commands from the lesson and note real output.
3. Implement stubs to match lesson vocabulary (flags, record types, layer names, etc.).
4. After green: say out loud *when* you would use each idea on an on-call.

## Done when

- `./test.sh` passes
- You can redo it tomorrow without opening the solution

**Struggle first (15+ minutes) before opening `solutions/38-kubernetes-net/`.**
