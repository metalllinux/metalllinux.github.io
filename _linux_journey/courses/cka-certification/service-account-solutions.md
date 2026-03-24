---
title: "Service Account Solutions"
category: "cka-certification"
tags: ["cka-certification", "service", "account", "solutions"]
---

* How to find the token of the default service account:
```
kubectl describe serviceaccount default 
```
* Find the service account by running `kubectl describe pods <pod_name> | grep -i service`
* Example of creating a new service account:
```
kubectl create serviceaccount dashboard-sa
```
* Example of creating a token:
```
kubectl create token dashboard-sa
```
* Updating a deployment to use a newly created service account:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-dashboard
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      name: web-dashboard
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        name: web-dashboard
    spec:
      serviceAccountName: dashboard-sa
      containers:
      - image: gcr.io/kodekloud/customimage/my-kubernetes-dashboard
        imagePullPolicy: Always
        name: web-dashboard
        ports:
        - containerPort: 8080
          protocol: TCP
```
* Then apply the above with `kubectl apply -f <yaml_file>`