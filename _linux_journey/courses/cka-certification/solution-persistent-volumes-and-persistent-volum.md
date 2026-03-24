---
title: "Solution Persistent Volumes And Persistent Volum"
category: "cka-certification"
tags: ["cka-certification", "solution", "persistent", "volumes", "persistent"]
---

* Example of `exec`ing into a pod and running a command:
```
kubectl exec webapp -- cat /log/app.log
```
* Example steps to configure a volume:
```
kubectl get po webapp -o yaml > webapp.yaml
```
OR 
```
kubectl run --dry-run=client -o yaml
```
* Then `kubectl delete po webapp`
* Then:
```
apiVersion: v1
kind: Pod
metadata:
  name: webapp
spec:
  containers:
  - name: event-simulator
    image: kodekloud/event-simulator
    env:
    - name: LOG_HANDLERS
      value: file
    volumeMounts:
    - mountPath: /log
      name: log-volume

  volumes:
  - name: log-volume
    hostPath:
      # directory location on host
      path: /var/log/webapp
      # this field is optional
      type: Directory
```
* Then create it with:
```
kubectl create -f <file-name>.yaml
```
* Another example of `Persistent Volume`:
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-log
spec:
  persistentVolumeReclaimPolicy: Retain
  accessModes:
    - ReadWriteMany
  capacity:
    storage: 100Mi
  hostPath:
    path: /pv/log
```
* Example `Persistent Volume Claim`:
```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: claim-log-1
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Mi
```
* Updated `PersistentVolumeClaim` with better Access Modes:
```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: claim-log-1
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 50Mi
```
* Example Pod using a PersistentVolumeClaim:
```
apiVersion: v1
kind: Pod
metadata:
  name: webapp
spec:
  containers:
  - name: event-simulator
    image: kodekloud/event-simulator
    env:
    - name: LOG_HANDLERS
      value: file
    volumeMounts:
    - mountPath: /log
      name: log-volume

  volumes:
  - name: log-volume
    persistentVolumeClaim:
      claimName: claim-log-1
```
* A PVC is stuck in a `terminating` state if it is being used by a pod.
* How to forcefully delete a pod:
```
kubectl delete pod webapp --force
```