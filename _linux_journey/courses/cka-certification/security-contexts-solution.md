---
title: "Security Contexts Solution"
category: "cka-certification"
tags: ["cka-certification", "security", "contexts", "solution"]
---

* Example definition file for configuring a specific user:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
  namespace: default
spec:
  securityContext:
    runAsUser: 1010
  containers:
  - command:
    - sleep
    - "4800"
    image: ubuntu
    name: ubuntu-sleeper
```
* Delete the above pod first, then run `kubectl apply -f <yaml_file>`
* Example way to delete a pod quickly (don't use in Production):
```
kubectl delete pod ubuntu-sleeper --force
```
* Another example definition file to update a pod with the `root` user and adding the `SYS_TIME` and `NET_ADMIN` capabilities:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
  namespace: default
spec:
  containers:
  - command:
    - sleep
    - "4800"
    image: ubuntu
    name: ubuntu-sleeper
    securityContext:
      capabilities:
        add: ["SYS_TIME", "NET_ADMIN"]
```
