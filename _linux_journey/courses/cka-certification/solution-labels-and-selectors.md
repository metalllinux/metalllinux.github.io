---
title: "Solution Labels And Selectors"
category: "cka-certification"
tags: ["cka-certification", "solution", "labels", "selectors"]
---

* How many pods are there in the `dev` environment:
```
kubectl get pods --selector env=dev
```
* It is possible to print the output of `kubectl get pods` without the header, use:
```
kubectl get pods --selector env=dev --no-headers
```
* To list all objects in a particular namespace:
```
kubectl get all -selector env=prod --no-headers
```
* Can check for multiple labels at the same time and it will show the pod that is included in all of the labels specified:
```
kubectl get all --selector env=prod,bu=finance,tier=frontend
```
* A good way to troubleshoot a bad Kubernetes file is via the `kubectl create -f <yaml_file.yaml>` and Kubernetes will tell you what the problem is.
* The example `replicaset` file is `replicaset-definition-1`:
```
apiVersion: apps/v1
kind: Replicaset
metadata:
  name: replicaset-1
spec:
  replicas: 2
  selector:
    matchLabels:
      tier: front-end
  template:
    metadata:
      labels:
        tier: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
```
* The replicaset needs the value in `tier` to match that of `template` --> `metadata=` --> `labels` --> `tier`
* What the file looks like after the changes have been made:
```
apiVersion: apps/v1
kind: Replicaset
metadata:
  name: replicaset-1
spec:
  replicas: 2
  selector:
    matchLabels:
      tier: nginx
  template:
    metadata:
      labels:
        tier: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
```