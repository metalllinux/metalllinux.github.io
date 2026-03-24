---
title: "How Check For Kubernetes Errors Such As E0~"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "check", "kubernetes", "errors", "such"]
---

```
grep kubelet messages | awk '{if ($6~/E[0-9]/){print $6}}' | sort | uniq -c
```
* You then receive an output such as:
```
2136 E0825
```
