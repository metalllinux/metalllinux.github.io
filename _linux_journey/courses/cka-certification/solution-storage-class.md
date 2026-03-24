---
title: "Solution Storage Class"
category: "cka-certification"
tags: ["cka-certification", "solution", "storage", "class"]
---

* How to check how many `Storage Classes` there are:
```
kubectl get sc
```
* `local-storage` is the Storage Class that does not support dynamic provisioning.
* How to check the `Volume Binding Mode` that a Storage Class uses:
```
kubectl describe sc local-storage
```
* Check the `Provisioner` using this method:
```
kubectl describe sc <storage_class>
```
* Example local Persistent Volume Claim:
```
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: local-pvc
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: local-storage
  resources:
    requests:
      storage: 500Mi
```
* Useful information:
> The Storage Class called local-storage makes use of VolumeBindingMode set to WaitForFirstConsumer. This will delay the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is created.

* Example pod making use of a local PVC:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    volumeMounts:
      - name: local-persistent-storage
        mountPath: /var/www/html
  volumes:
    - name: local-persistent-storage
      persistentVolumeClaim:
        claimName: local-pvc
```
* Example of a new storage class:
```
---
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: delayed-volume-sc
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```