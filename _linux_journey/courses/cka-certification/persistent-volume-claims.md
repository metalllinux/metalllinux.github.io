---
title: "Persistent Volume Claims"
category: "cka-certification"
tags: ["cka-certification", "persistent", "volume", "claims"]
---

* `Persistent Volume Claims` add storage to a node.
* `Persistent Volumes` and `Persistent Volume Claims` are two separate objects in the Kubernetes namespace.
* An Administrator creates `Persistent Volumes` and a user makes the `Persistent Volume Claims`.
* Once created, Kubernetes binds the set `Persistent Volume` and its `Persistent Volume Claim` together.
* Kubernetes tries to find a `Persistent Volume`, that has the right capacity asked for by the claim.
	* Kubernetes looks for the following:
		* `Sufficient Capacity`
		* `Access Modes`
		* `Volume Modes`
		* `Storage Class`
* If there are multiple `Persistent Volume Claims` aimed at one `Persistent Volume`, then you can use `labels` and `selectors` for that. For example with a `Persistent Volume`:
```
labels:
  name: my-pw
```
* For the `Persistent Volume Claim`:
```
selector:
  matchLabels:
    name: my-pv
```
* A smaller `Persistent Volume Claim`, may be bound to a larger `Persistent Volume`, if there are no better options available.
* There is a 1:1 relationship with `Persistent Volumes` and `Persistent Volume Claims`, so even if there is leftover space on a `Persistent Volume`, no other `Persistent Volume Claims` can use it.
* If there are no other `Persistent Volumes` available and a `Persistent Volume Claim` is looking for a `Persistent Volume` to bind with, that `Persistent Volume Claim` will go into a `Pending` state.
	* When newer `Persistent Volumes` are available, the `Persistent Volume Claim` can then be bound successfully.
* Example `Persistent Volume Claim` of `pvc-definition.yaml`:
```
apiVersion: v1
kind: PersistentVolumeClaim
metdata:
  name: myclaim
spec:
  accessModes:
	 - ReadWriteOnce
  resources:
     requests:
	   storage: 500Mi
```
* Create the `Persistent Volume Claim` definition file with this command:
```
kubectl create -f pvc-definition.yaml
```
* Check the `Persistent Volume Claims` with:
```
kubectl get persistentvolumeclaim
```
* When a `PVC` is created, Kubernetes looks at the volume that was made previously.
* Previously the following `Persistent Volume` was made available. Pairing this with the `Persistent Volume Claim` above will allow it to be bound (albeit wasting 500MB of storage).
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
* Running the `kubectl get persistentvolumeclaim` command again shows the following:
```
Name	STATUS	VOLUME	CAPACITY	ACCESS MODES	STORAGECLASS	AGE
myclaim	Bound	pv-vol1	1Gi			RWO			43m
```
* To delete a PVC, run the following:
```
kubectl delete persistentvolumeclaim myclaim
```
* What happens to the underlying `Persistent Volume` when the claim is deleted?
	* By default, the `persistentVolumeReclaimPolicy` is set to `Retain`
	* `persistentVolume` will remain until it is manually deleted.
	* Not available for reuse by any other claims!
* Else it can be deleted with the following:
```
persistentVolumeReclaimPolicy: Delete
```
* The above deletes the `Persistent Volume Claim` automatically.
* A third option is:
```
persistentVolumeReclaimPolicy: Recycle
```
* For the above, the data in the data volume will be scrubbed, before it is available to other claims.