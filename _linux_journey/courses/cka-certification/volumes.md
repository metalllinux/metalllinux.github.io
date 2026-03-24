---
title: "Volumes"
category: "cka-certification"
tags: ["cka-certification", "volumes"]
---

* Docker volumes are meant to be transient in nature.
	* Only last for a short period of time.
	* The data is also destroyed, along with the container.
* How does the above work with Kubernetes?
	* Pods created in Kubernetes are transient.
	* Data processed is also deleted as well.
	* Thus similarly volumes are also attached to pods.
* Simple Kubernetes volume implementation for a single node. Example pod that generates a random number:
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
* To retain the random number, a volume is generated on the pod.
* When you create a volume, you can modify the storage in many ways.
* When the pod is deleted, it still lives on in the host.
* The above `hostPath` setup is not recommended on a multinode cluster.
	* All nodes in the above example would use the `/data` directory and have the same data.
	* A better way to do storage across multiple nodes would be NFS, `GlusterFS`, `Flocker` and more.
	* Can also configure an AWS Elastic Block Store Volume.
* You would re-write the data storage part as so for AWS Elastic Block Store Volume:
```
volumes:
- name: data-volume
  awsElasticBlockStore:
	volumeID: <volume-id>
	fstype: ext4
```
* The above code block then puts the storage onto AWS EBS.
* 