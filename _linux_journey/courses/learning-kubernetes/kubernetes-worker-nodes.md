---
title: "Kubernetes Worker Nodes"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "kubernetes", "worker", "nodes"]
---

* Useful annotation on how Kubernetes Control Plane is like a Control Tower and the Worker Nodes are like Terminals:
![Screenshot from 2024-03-06 14-15-29.png](../../_resources/Screenshot%20from%202024-03-06%2014-15-29.png)
* Most Kubernetes clusters run with a minimum of 3 worker node .
* The components that take up worker nodes are:
* Pods are scheduled and run and each worker node has 3 components:
* First component is the Kubelet
	* Agent that runs on every worker node.
	* Makes sure that the containers in a pod have started running and are healthy.
	* Communicates directly with the api-server in the Control Plane.
* Next component is the Container Runtime
	* A Kublet assigned to a new pod, starts a container using Container Runtime Interface (CRI).
	* CRI enables the Kublet to create containers with the following engines: Containerd, CRI-O, Kata Containers and AWS Firecracker.
* In Kubernetes 1.24, Dockershim was removed. The Docker engine can no longer be used as container runtime. Docker Images still work in Kubernetes (Docker Images and Docker Containers are two separate things).
* Final Component is the Kube-proxy.
	* Makes sure pods and services can communicate with other pods and services on Nodes and in the Control Plane.
	* Each kube-proxy communicates directly with the Kube-apiserver
