---
title: "Solution Rbac"
category: "cka-certification"
tags: ["cka-certification", "solution", "rbac"]
---

* Check the environment and identify the authorisation mode:
```
kubectl describe pod kube-apiserver-controlplane -n kube-system | grep "--authorization-mode"
```
* Check how many `roles` exist:
```
kubectl get roles
```
* How to check all roles in all namespaces:
```
kubectl get roles --all-namespaces
```
* How to check the resources the `kube-proxy` pod has access to:
```
kubectl describe role kube-proxy -n kube-system
```
* How to check which account the `kube-proxy` role is assigned to:
```
kubectl describe rolebinding kube-proxy -n kube-system
```
* The answer would be:
```
system:bootstrappers:kubeadm:default-node-token
```
* The output looks like this:
```
Name:         kube-proxy
Labels:       <none>
Annotations:  <none>
Role:
  Kind:  Role
  Name:  kube-proxy
Subjects:
  Kind   Name                                             Namespace
  ----   ----                                             ---------
  Group  system:bootstrappers:kubeadm:default-node-token 
```
* How to run the `get pods` command as a specific user:
```
kubectl get pods --as dev-user
```
* The `kube-proxy` rule get get details of the configmap object by `kube-proxy` only.