---
title: "Cni Weave"
category: "cka-certification"
tags: ["cka-certification", "cni", "weave"]
---

* There is a particular CNI Plugin called WEAVE.
* Previously there was a CNI script that was built and implemented into the `Kubelet` through CNI.
	* Instead of the custom script, a WEAVE plugin can be integrated instead.
* The previous solution had a routing table setup - when a packet is sent from one pod to another, it goes out to the router in the network and makes its way to the node that hosts the pod.
	* This works for a small environment and in a small network.
	* Not practical for multi node and multi pod environments.
		* The routing table may not support that many entries.
* Can think of a Kubernetes cluster as a company with nodes of each office site.
	* Each department has different offices.
	* Packet needs to go from Office 1 to Office 3 - how it is transported is irrelevant.
		* Different countries and regions, the Office Boy can't do that - outsource it to a shipping company.
	* An agent is placed in each site (i.e. node) and is responsible for all shipping activities.
		* They keep talking to each other and are well-connected.
		* They all know of each other's sites, the departments, as well as the offices within them.
			* The agent intercepts a package on Node A and knows exactly the site and which Node to send it to.
				* That package is placed into a new one. It has the address as the target site's location.
			* Once the package arrives at the destination, it is intercepted by the agent on the other side.
				* That agent opens the package and delivers it to the right department.
* In the world of Kubernetes, WEAVEWORKS has an agent on each node. They communicate between each other to say what networks and pods are within each node.
* Each agent or peer stores a topology of the entire setup. They then know the pods and IPs on the other nodes.
* WEAVE creates its own bridge on the nodes and assigns an IP address to each network.
* An example command of attaching a pod to a WEAVE bridge:
```
kubectl exec busybox ip route
```
* Output:
```
default via 10.244.1.1 dev eth0
```
* WEAVE makes sure that the pod get the right route to get to the agent. The agent takes care of the other pods.
* When a packet is sent from one pod to another pod on another node. WEAVE intercepts the package and identifies it is on another network.
	* It then encapsulates the packet into a new one, with a new source and destination.
	* It sends it across the network.
	* Once on the other side, the other WEAVE agent retrieves the packet, dencapsulates it and routes the packet to the right pod.
* How do you deploy WEAVE onto a Kubernetes cluster?
	* The WEAVE daemon can be deployed on each cluster manually.
	* If Kubernetes is setup already, deploy WEAVE as pods.
* Once the base Kubernetes system is ready, with configurations set between the nodes, WEAVE can be deployed in the cluster with a single `kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"`
* If you deploy a cluster with the `kubeadm` tool and WEAVE PEERS plugin, you can see the `weave-net` pods deployed on each node.
* For troubleshooting, view the logs with `kubectl logs weave-net weave -n kube-system`