---
title: "Ways To Manage Kubernetes Pods"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "ways", "manage", "kubernetes", "pods"]
---

* One way is to create pods using the Kubernetes Deployment Object.
* There are also Daemon Sets and Jobs.
* Kubernetes Deployment is the most common way to deploy containerised applications.
	* Allows you to control the number of replicas running.
		* Kubernetes can keep the old version up and running, roll out the new version, ensure the new pods are healthy and then remove the old pods.
	* No downtime upgrade.
* Another way to deploy pods, is using a `DaemonSet`
	* One pod per node.
		* Will put one copy of a container on every node running in the cluster.
		* Can't directly control the number of replicas running.
		* Deploys containers that are usually daemons and having to run background processes.
	* Common for `DaemonSets` to run a program, that collects information from the underlying node and other pods on that node.
* The final way to deploy more than one pods at a time, is a Kubernetes Job.
	* A Job will create one or more pods and then run a container inside of them, until it has successfully completed its task.
	* Example of a Kubernetes Job, is an application you deploy in a testing cluster, that generates a batch of data for a testing framework. Only need to generate that data once in a while. Can delete the application once its done.
	* Deletes the pod afterwards.