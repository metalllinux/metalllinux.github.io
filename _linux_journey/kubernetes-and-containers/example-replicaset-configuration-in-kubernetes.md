---
title: "Example Replicaset Configuration In Kubernetes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "example", "replicaset", "configuration", "kubernetes"]
---

```
apiVersion: apps/v1
kind: ReplicaSet
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
        tier: front-end
     spec:
       containers:
       - name: nginx
         image: nginx 
```