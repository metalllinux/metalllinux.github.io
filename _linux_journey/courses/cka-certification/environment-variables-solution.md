---
title: "Environment Variables Solution"
category: "cka-certification"
tags: ["cka-certification", "environment", "variables", "solution"]
---

Good example definition file using environment variables:
```
---
apiVersion: v1
kind: Pod
metadata:
  labels:
    name: webapp-color
  name: webapp-color
  namespace: default
spec:
  containers:
  - env:
    - name: APP_COLOR
      value: green
    image: kodekloud/webapp-color
    name: webapp-color
```
* Environment Variables are where it says `env` --> `name`
* Good example of a ConfigMap:
```
kubectl create configmap  webapp-config-map --from-literal=APP_COLOR=darkblue --from-literal=APP_OTHER=disregard
```
* A pod definition file using a configmap:
```
---
apiVersion: v1
kind: Pod
metadata:
  labels:
    name: webapp-color
  name: webapp-color
  namespace: default
spec:
  containers:
  - env:
    - name: APP_COLOR
      valueFrom:
       configMapKeyRef:
         name: webapp-config-map
         key: APP_COLOR
    image: kodekloud/webapp-color
    name: webapp-color
```
* Use `kubectl edit pod <pod-name>` to at least generate a new definition file easily (you won't be able to deply it
	* Then you can forcefully delete a pod with `kubectl replace --force -f /tmp/<pod_definition_file.yaml>`
* Short form of ConfigMap is `cm`.
* Good help command `kubectl create cm --help` - useful in the exam.
* Another good one is `kubectl create configmap webapp-config-map --from-literal=APP_COLOR=darkblue`
* Edit a pod with `kubectl edit pod <pod name>`