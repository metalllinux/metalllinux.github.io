---
title: "Etcd In Kubernetes"
category: "cka-certification"
tags: ["cka-certification", "etcd", "kubernetes"]
---

* ETCD data store has the following:
	* Nodes
	* PODs
	* Configs
	* Secrets
	* Accounts
	* Roles
	* Bindings
	* Other
* Every piece of information you see when you run the `kubectl get` command is from the ETCD server.
* Every additional change you make to your cluster - adding nodes, deploying pods or replica sets are updated in the ETCD server.
	* Only once the updates are updated in the ETCD server, is the change considered to be complete.
* The practice test environments are deployed using the `kubeadm` tool. Later in the course when a cluster is set up, it is set up from scratch.
	* If you set up your cluster from scratch, you deploy ETCD by downloading the binaries yourself. This also includes configuring `ETCD` as a service on your Master Node. 
![screenshot.png](../../_resources/screenshot-4.png)
* You can pass many options such as certificates and these will be looked into further in the course.
	* There is a whole section of TLS certificates.
* You can also configure `ETCD` as a cluster - part of high availability in Kubernetes.
* The one option to note for now from the above screenshot is the `--advertise-client-urls https://${INTERNAL_IP}:2379 \\`.
	* This is the address where `ETCD` listens. This is on the IP of the server and is on port `2379`. That is the default port which `ETCD` listens on.
		* This should be configured on the `kube-api` server, when it tries to reach the `ETCD` server.
* If you cluster is using `kubeadm`, `kubeadm` will then deploy the ETCD server for you as a pod.
	* This will be in the `kube-system` namespace.
![screenshot.png](../../_resources/screenshot-5.png)
* You can explore the ETCD database, by using the etcd control utility within the `etcd-master` pod.
* To list all keys stored by Kubernetes, run the `etcd` control get command.
```
kubectl exec etcd-master -n kube-system etcdctl get / --prefix -keys-only
```
* The output looks like the below:
![screenshot.png](../../_resources/screenshot-3.png)
* Kubernetes stores data in a specific directory structure.
* The `root` directory is the registry and under that you have various Kubernetes constructs.
![screenshot.png](../../_resources/screenshot-6.png)
* ETCD in a High Availability Environment
	* You have multiple Master Nodes in the cluster. There are multiple ETCD nodes spread across the Master Nodes.
	* Make sure the `etcd` instances know about each other. Set the right parameters in the `etcd service configuration` under `etcd.service`.
![screenshot.png](../../_resources/screenshot-7.png)
* The `initial-cluster` option is where you specify the different instances of the `etcd` service. 