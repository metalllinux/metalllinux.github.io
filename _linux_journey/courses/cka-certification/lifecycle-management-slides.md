---
title: "Lifecycle Management Slides"
category: "cka-certification"
tags: ["cka-certification", "lifecycle", "management", "slides"]
---

[Kubernetes+-CKA-+0400+-+Application+Lifecycle+Management.pdf](../../_resources/Kubernetes+-CKA-+0400+-+Application+Lifecycle+Mana.pdf)
* Rollout command:
```
kubectl rollout status deployment/myapp-deployment
```
* Rollout history:
```
kubectl rollout history deployment/myapp-deployment
```
* `set image` command:
```
kubectl set image deployment/myapp-deployment \
nginx=nginx:1.9.1
```