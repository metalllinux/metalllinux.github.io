---
title: "Container Storage Interface (Csi)"
category: "cka-certification"
tags: ["cka-certification", "container", "storage", "interface", "csi"]
---

* In the past, Kubernetes only worked with `docker`. This was built into the Kubernetes source code.
* Other container runtimes then appeared, such as `rkt` and `cri-o`.
* CRI Standard is set how to define an orchestration solution like Kubernetes, would communicate with Container Runtimes such as `docker`.
* If a new CRI interface is created, can be easily slotted into Kubernetes without having to implement it into the Kubernetes source code.
* To extend support for different networking solutions, the Container Network Interface was introduced.
	* Networking vendors can create a plugin and make use of CSI.
	* Vendors include `Weaveworks`, `Flannel` and `Cilium`
* Storage also includes the following:
	* portworx
	* Amazon EBS
	* Azure Disk
	* DELL EMC Isilon
	* GlusterFS
	* PowerMax
	* Unity
	* XtremIO
	* NetApp
	* Nutanix
	* HPE
	* Hitachi
	* Pure Storage
* CSI, vendors can write your own drivers.
* CSI is not a Kubernetes-specific standard.
	* Meant to be a universal standard.
	* Allows any container orchestration tool to work with any storage vendor and supported plugin.
	* These vendors include:
		* Kubernetes
		* Cloud Foundry
		* Mesos
* On the Kubernetes / Cloud Foundry / Mesos side, these should do this:
	* SHOULD call to provision a new volume.
	* SHOULD call to delete a volume.
	* SHOULD call to place a workload that uses the volume onto a node.
* On the storage side of the house:
	* SHOULD provision a new volume on the storage.
	* SHOULD decommission a volume.
	* SHOULD make the volume available on a node.
* Defines a set of RPCs (Remote Procedure Calls)
	* These are called by the Container Orchestrator.
		* Must be implemented by the storage driver.
* For example. the CSI says when a pod is created, it needs a volume.
	* Therefore this calls Kubernetes and passes details such as the volume name,
	* The storage driver then needs to implement the RPC, handle the request and provision a new volume on the storage array.
	* The results of the operation are returned.
	* Similarly with the delete volume RPC
		* Storage driver should implement the code, to decommission the volume from the array.
* More information on the CSI can be found here: https://github.com/container-storage-interface/spec