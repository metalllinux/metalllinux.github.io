---
title: "Persistent Volumes"
category: "cka-certification"
tags: ["cka-certification", "persistent", "volumes"]
---

* One place to configure volumes is within the pod definition file.
	* In a large environment, this would then be done per pod and is not ideal.
*  Want to store this centrally. Have a central piece of storage and carve out pieces where required.
*  This is a `Persistent Volume Claim`
*  Example Persistent Volume (`pv-definition.yaml`):
```
apiVersion: v1
kind: PersistentVolume
metadata:
   name: pv-vol1
spec:
  accessModes:
	  - ReadWriteOnce
  capacity:
	  storage: 1Gi
  hostPath:
	  path: /tmp/data
```
* `accessModes` defines how a volume should be mounted on a host.
	* Supported values are:
	* `ReadOnlyMany`
	* `ReadWriteOnce`
	* `ReadWriteMany`
* `1Gi` in the above example is 1 Gigabyte.
* Volume Type in the above case is `hostPath` and uses the node's local directory.
	* `hostPath` should not be used in a production environment.
* Once done, create the volume with this command:
```
kubectl create -f pv-definition.yaml
```
* Ideally you want to replace the `hostPath` option with a supported solution like below:
```
apiVersion: v1
kind: PersistentVolume
metadata:
   name: pv-vol1
spec:
  accessModes:
	  - ReadWriteOnce
  capacity:
	  storage: 1Gi
  awsElasticBlockStore:
    volumeID: <volume-id>
	fsType: ext4
```