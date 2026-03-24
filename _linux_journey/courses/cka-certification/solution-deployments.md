---
title: "Solution Deployments"
category: "cka-certification"
tags: ["cka-certification", "solution", "deployments"]
---

* Check for replicasets:
```
kubectl get rs
```
* Check for `deployments`:
```
kubectl get deployments
```
* Check pods:
```
kubectl get pods
```
* Check the image on a pod, using `kubectl describe pod <pod_name>`
* To create a deployment (useful for checking errors in your `yaml` file):
```
kubectl create -f <deployment.yaml>
```
* When using the `kind` field in a `yaml` file, the following character should be capitalised as `Deployment`
* Create an object with `kubectl create`
* Useful help command is `kubectl create deployment --help`.
* Deploy an image:
```
kubectl create deployment httpd-frontend --image=httpd:2.4-alpine --replicas=3
```
* Check `kubectl get deploy` afterwards.