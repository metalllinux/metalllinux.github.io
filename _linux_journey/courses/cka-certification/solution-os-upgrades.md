---
title: "Solution Os Upgrades"
category: "cka-certification"
tags: ["cka-certification", "solution", "upgrades"]
---

* How to quickly show which nodes certain pods are assigned to:
```
kubectl get pods -o wide
```
* When draining a node of pods, if you get a warning related to a daemonset, run this command:
```
kubectl drain node01 --ignore-daemonsets
```