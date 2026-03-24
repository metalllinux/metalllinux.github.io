---
title: "Namespaces Solution"
category: "cka-certification"
tags: ["cka-certification", "namespaces", "solution"]
---

* How many `namespaces` are there on the system:
```
kubectl get namespaces
```
* To check the amount of pods in a particular `namespace`:
```
kubectl get pods --namespace=<namespace>
kubectl get pods -n=<namespace>
```
* Create a pod in a particular `namespace`:
```
kubectl run redis --image=redis -n=<namespace>
```
* To list all of the `namespaces`:
```
kubectl get ns
```
* Find a pod in a namespace, just type `kubectl get pods --all-namespaces`. The same way is to use `-A` with `kubectl get pods -A`
* How to check for a DNS name:
```
kubectl get pods -n=<namespace_name>
```
* Also check the service:
```
kubectl get svc -n=<namespace_name>
```
* If a pod and service are in the same namespace, the pod can access it.
* For a pod to access a service that is based in another namespace, it has to use the full address of the service. For example:
```
db-service.dev.svc.cluster.local
```