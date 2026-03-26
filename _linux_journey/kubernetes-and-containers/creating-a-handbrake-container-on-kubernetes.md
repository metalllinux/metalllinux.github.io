---
title: "Creating A Handbrake Container On Kubernetes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "creating", "handbrake", "container", "kubernetes"]
---

* Create a `docker-compose.yaml` file with the following:
```
version: '3'
services:
  handbrake:
    image: jlesage/handbrake
    ports:
      - "5800:5800"
    volumes:
      - "/docker/appdata/handbrake:/config:rw"
      - "/home/myuser:/storage:ro"
      - "/home/myuser/HandBrake/watch:/watch:rw"
      - "/home/myuser/HandBrake/output:/output:rw"
```
* Then run `kompose convert` in the same directory.
* Create the pod with:
```
kubectl apply -f handbrake-claim2-persistentvolumeclaim.yaml,handbrake-claim0-persistentvolumeclaim.yaml,handbrake-cm1-configmap.yaml,handbrake-claim3-persistentvolumeclaim.yaml,handbrake-service.yaml,handbrake-deployment.yaml
```