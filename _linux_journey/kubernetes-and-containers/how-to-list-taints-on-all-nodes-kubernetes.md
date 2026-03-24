---
title: "How to List the Taints on All Nodes in Kubernetes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "list", "taints", "all", "nodes"]
---

# How to List the Taints on All Nodes in Kubernetes

```
kubectl get nodes -o json | jq '.items[].spec'
```

