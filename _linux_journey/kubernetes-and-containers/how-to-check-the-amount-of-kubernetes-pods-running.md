---
title: "How To Check The Amount Of Kubernetes Pods Running"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "check", "amount", "kubernetes", "pods"]
---

`cat df | grep "/var/lib/kubelet/pods" | wc -l`