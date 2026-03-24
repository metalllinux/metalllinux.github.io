---
title: "Solution Daemonsets"
category: "cka-certification"
tags: ["cka-certification", "solution", "daemonsets"]
---

* Good example DaemonSet:
```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: elasticsearch
  namespace: kube-system
spec:
  selector:
    matchLabels:
      name: elasticsearch
  template:
    metadata:
      labels:
        name: elasticsearch
    spec:
      containers:
      - name: elasticsearch
        image: registry.k8s.io/fluentd-elasticsearch:1.20
```
* How many DaemonSets are there in all of the namespaces:
```
kubectl get daemonsets -a
```
* How many nodes is a daemonset pod assigned to*
```
Can find this from kubectl get daemonsets -A
```
* To find more information about a particular Daemonset, this is done via `kubectl describe daemonsets <daemonset> -n <namespace_name>`
* An easier way to deploy a daemonset is to use the `dry-run` option for a Deployment and edit that.
```
kubectl create deployment elasticsearch -n kube-system --image=k8s.gcr.io/fluentd-elasticsearch:1.20 --dry-run=client -o yaml > yaml_file.yaml
```
* 