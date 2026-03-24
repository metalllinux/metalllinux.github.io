---
title: "To Setup A Metrics Server On Kubernetes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "setup", "metrics", "server", "kubernetes"]
---

Other Kubernetes Systems:
```
git clone https://github.com/kubernetes-incubator/metrics-server.git
```
Create the deployment:
```
kubectl create –f deploy/1.8+/
```
With MiniKube:
```
minikube addons enable metrics-server
```