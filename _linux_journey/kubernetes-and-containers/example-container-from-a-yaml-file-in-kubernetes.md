---
title: "Example Container From A Yaml File In Kubernetes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "example", "container", "yaml", "file"]
---

```
apiVersion: v1
kind: Pod
metadata: 
  name: redis
  labels: 
      app: redis
spec: 
  containers: 
    - name: redis 
      image: redis123
```
`kubectl create -f pod.yaml`