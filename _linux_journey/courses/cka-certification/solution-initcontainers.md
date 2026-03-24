---
title: "Solution Initcontainers"
category: "cka-certification"
tags: ["cka-certification", "solution", "initcontainers"]
---

* Creating an `init` container in the pod definition file:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: red
  namespace: default
spec:
  containers:
  - command:
    - sh
    - -c
    - echo The app is running! && sleep 3600
    image: busybox:1.28
    name: red-container
  initContainers:
  - image: busybox
    name: red-initcontainer
    command: 
      - "sleep"
      - "20"
```
* Get a pod definition file:
```
kubectl get pod orange -o yaml > /root/orange.yaml
```
* Identify the pods that have an initContainer by using the `kubectl describe` command.
* To `describe` all pods, just run:
```
kubectl describe pod
```
* Check the `State` also via the `describe` command.
* To check the amount of initContainers, there is no counter, just check the amount of containers listed via the `kubectl describe pod` command.
* Can have multiple initContainers chained to sleep for 30 seconds for container 1 and then for 60 seconds for container 2.
* 