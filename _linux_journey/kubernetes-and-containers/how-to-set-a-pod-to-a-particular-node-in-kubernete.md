---
title: "How To Set A Pod To A Particular Node In Kubernete"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "pod", "particular", "node", "kubernete"]
---

Use `nodeSelector`.
```
spec:
  nodeSelector:
    hostname: <hostname_here>
```