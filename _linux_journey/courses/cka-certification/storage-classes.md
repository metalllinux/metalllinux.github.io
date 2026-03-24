---
title: "Storage Classes"
category: "cka-certification"
tags: ["cka-certification", "storage", "classes"]
---

* Previous Lecture --> PV is attached to a PVC, which is itself then attached to a pod definition file.
* An example of creating a `Persistent Volume` on Google Cloud:
```
gcloud beta compute disks create
      --size 1GB
      --region us-east1
      pd-disk
```
* The accompanying `Persistent Volume` would be:
```
apiVersion: v1
kind: PersistentVolume
metadata:
   name: pv-vol1
spec:
  accessModes:
      - ReadWriteOnce
  capacity:
      storage: 500Mi
  gcePersistentDisk:
     pdName: pd-disk
     fstype: ext4
```
* When an application requires storage, have to manually provision the disk on Google Cloud and then create the PV definition file.
	* This is called `Static Provisioning`.
* It is better if the volume is provisioned automatically when the application requires it.
	* This is where Storage Classes help.
* Can automatically provision storage on Google Cloud.
* Attach it to pods when a claim is made.
	* This is called `Dynamic Provisioning` of volumes.
* It is done by making a Storage Class object:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
   name: google-storage
provisioner: kubernetes.io/gce-pd
```
* Then we do not need the `PV` definition file, as the Persistent Volume will be created when the Storage Class is generated.
* For the `Persistent Volume Claim`, have to add the following `storageClassName` to the config:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
     - ReadWriteOnce
  storageClassName: google-storage
  resource:
     requests:
        storage: 500Mi
```
* The pod definition does not need to be changed:
```
apiVersion: v1
kind: Pod
metadata:
  name: random-number-generator
spec:
  containers:
  - image: alpine
    name: alpine
    command: ["/bin/sh","-c"]
	args: ["shuf -i 0-100 -n 1 >> /opt/number.out;"]

  volumes:
  - name: data-volume
	hostPath:
	   path: /data
	   type: Directory
```
* Many other provisioners available.
	* `Local`, `AzureFile`, `FlexVolume` and more.
* Another Storage Class example using a standard disk:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
   name: google-storage
provisioner: kubernetes.io/gce-pd
parameters:
   type: pd-standard
   replication-type: none
```
* A second example with an SSD:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
   name: google-storage
provisioner: kubernetes.io/gce-pd
parameters:
   type: pd-ssd
   replication-type: none
```
* A third example with an SSD and replication:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
   name: google-storage
provisioner: kubernetes.io/gce-pd
parameters:
   type: pd-ssd
   replication-type: regional-pd
```