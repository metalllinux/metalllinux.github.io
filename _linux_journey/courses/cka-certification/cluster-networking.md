---
title: "Cluster Networking"
category: "cka-certification"
tags: ["cka-certification", "cluster", "networking"]
---

* Each node must have at least one interface connected to the network.
* Each interface must have an address provided.
* Each host needs a unique hostname set.
	* This also includes a unique mac address.
	* Especially if VMs are created from existing ones (useful point this one).
* Some ports need to be opened as well.
	* Used by the various ports.
* For example on a Master Node:
	* `Interface` --> `eth0`
	* `Address` --> `192.168.1.10`
	* `Hostname` --> `master-01`
	* Contains the following: `kubectl`, `kube-api`, `kubelet`, `kube-scheduler`, `kube-controller-manager`, `etcd`
	* Accepts connections on port `6443` on the `kube-api` server.
	* The `kubelet` listens on port `10250`.
	* The `kube-scheduler` listens on port `10259`
	* The `kube-controller-manager` listens on port `10257`
	* The `etcd` server listens on port `2379`.
* For example on the Worker Node:
	* `Interface` --> `eth0`
	* `Address` --> `192.168.1.11`
	* `Hostname` --> `worker-01`
	* The `kubelet` listens on port `10250`
	* Exposes services for external access on ports`30000-32767`
* If you have multiple `Master` nodes, these ports need to be opened as well:
	* Need port `2380` opened on all of the Master Nodes, so that the `etcd` clients can talk to each other.
* Can check required port ranges here: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#check-required-ports
	* Good place to check if things aren't working.
* Useful `netstat` command:
```
netstat -plnt
```