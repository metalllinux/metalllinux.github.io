---
title: "Solution Multiple Schedulers"
category: "cka-certification"
tags: ["cka-certification", "solution", "multiple", "schedulers"]
---

* To check all namespaces to find a particular pod:
```
kubectl get pods -A
```
* To describe a pod in another namespace, do:
```
kubectl describe pod <podname> -n <namespace>
```
* To check a service account in another namespace:
```
kubectl get sa my-scheduler -n kube-system
```
* How to create a `configmap`:
```
kubectl create configmap --name my-scheduler-config --from-file=/root/my-scheduler-config.yaml -n kube-system
```
* Then check the `configmap` with:
```
kubectl get configmap my-scheduler-config -n kube-system
```
* If there is a question regarding adding an image into a pod config, use `kubectl describe` on another pod to check the Image used there and then copy that over.
* To create a pod with a custom-scheduler, add the `schedulerName` field below:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  schedulerName: my-scheduler
  containers:
  - image: nginx
    name: nginx
```