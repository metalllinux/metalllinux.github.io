---
title: "Install Minikube And Spin Up A Minikube Cluster"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "install", "minikube", "spin", "minikube"]
---

* You can set up a local Kubernetes cluster.
* Start minikube with:
```
minikube start 
```
* The `minikube` command creates a cluster from scratch.
* The `kubectl` allows you to interact with your cluster.
* GCP, Azure, AWS etc use their own command syntax to spin up a Kubernetes cluster. Then afterwards we use `kubectl`.
* To get information about your Kubernetes cluster, we run 
```
kubectl cluster-info
```
	* Will see where `CoreDNS` is running (this is the container network interface).
* If you see an error message saying the connection to the cluster was refused, it means you do not have `minikube` running.
* To get information on the nodes, we then run:
```
kubectl get nodes
```
* To get the namespaces that are created by default, we run:
```
kubectl get namespaces
```
* `namespaces` are a good way to isolate and manage applications.
* To list all available pods, we run:
```
kubectl get pods -A
```
* The `-A` flag hows the pods in every namespace.
* Pods are how containers are run in Kubernetes.
* Pods are also the software to run a Kubernetes cluster itself.
* To see all of the running services, we do:
```
kubectl get services -A
```
* Services act as loadbalancers within the cluster. They direct traffic to pods.
* 