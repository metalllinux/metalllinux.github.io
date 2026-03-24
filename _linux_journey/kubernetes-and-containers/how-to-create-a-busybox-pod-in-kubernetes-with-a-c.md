---
title: "How To Create A Busybox Pod In Kubernetes With A C"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "create", "busybox", "pod", "kubernetes"]
---

```
kubectl run --restart=Never --image=busybox static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml
```