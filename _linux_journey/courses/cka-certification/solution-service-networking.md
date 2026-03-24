---
title: "Solution Service Networking"
category: "cka-certification"
tags: ["cka-certification", "solution", "service", "networking"]
---

* How to check the network range the nodes in the cluster are part of:
	* Use the `ipcalc` utility.
	* Firstly find the internal IP of the nodes from the Control Plane node with: `ip a | grep eth0`.
	* Use the `ipcalc` command to see the network details. An example is below:
```
root@controlplane:~> ipcalc -b 10.33.39.8
Address:   10.33.39.8           
Netmask:   255.255.255.0 = 24   
Wildcard:  0.0.0.255            
=>
Network:   10.33.39.0/24        
HostMin:   10.33.39.1           
HostMax:   10.33.39.254         
Broadcast: 10.33.39.255         
Hosts/Net: 254                   Class A, Private Internet
```
* The answer in this case is `Network:   10.33.39.0/24`
* How to check the range of IP addresses configured for pods in the cluster?
	* Network is configured with `weave`.
	* Check the `weave` pods with `kubectl logs <weave-pod-name> weave -n kube-system`.
	* Look for `ipalloc-range`.
	* Good command to use: `kubectl logs weave-net-v28kc -n kube-system | grep ipalloc`
* Example output:
```
kubectl logs weave-net-v28kc -n kube-system | grep ipalloc
Defaulted container "weave" out of: weave, weave-npc, weave-init (init)
INFO: 2025/04/20 12:06:29.654624 Command line options: map[conn-limit:200 datapath:datapath db-prefix:/weavedb/weave-net docker-api: expect-npc:true http-addr:127.0.0.1:6784 ipalloc-init:consensus=0 ipalloc-range:10.244.0.0/16 metrics-addr:0.0.0.0:6782 name:52:4d:00:38:8e:f8 nickname:controlplane no-dns:true no-masq-local:true port:6783]
```
* How to check the IP range configured for services within the cluster?
```
cat /etc/kubernetes/manifests/kube-apiserver.yaml   | grep cluster-ip-range
```
* Example output:
```
cat /etc/kubernetes/manifests/kube-apiserver.yaml   | grep cluster-ip-range
    - --service-cluster-ip-range=10.96.0.0/12
```
* How to check the amount of `kube-proxy` pods?
* Run the following:
```
kubectl get pods -n kube-system
```
* How to find the proxy that `kube-proxy` is configured to use?
	* Check the logs of the `proxy` pods.
	* Run this command: `kubectl logs <kube-proxy-pod-name> -n kube-system`
		* Example: `kubectl logs kube-proxy-bcnwv -n kube-system`
		* `grep` for the following:
			* `userspace`, `firewalld`, `ipvs` and `iptables`.
* How does the Kubernetes cluster ensure that a `kube-proxy` pod runs on all nodes in the cluster?
	* Run `kubectl get ds -n kube-system`  to check this  