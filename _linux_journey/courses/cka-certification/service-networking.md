---
title: "Service Networking"
category: "cka-certification"
tags: ["cka-certification", "service", "networking"]
---

* Previously there was `pod networking`, with how bridges are created with each node, how pods get a namespace and how interfaces are attached to those namespaces.
	* Then how pods get an IP assigned to them, within the subnet assigned for that node.
	* Routes and other overlay techniques also discussed to have the pods talk to each other.
* Rarely configure pods to communicate with each other, if you want a pod to access a service on another pod, use a service for that.
* Quick recap on services:
	* For example on `Node1` you have an Orange pod with an address of `10.244.1.3`, which wants to connect to the Blue pod on `10.244.1.2`.
		* The Orange Pod makes an `orange-service` and an IP of `10.99.13.178` is assigned to it. The Blue Pod can now connect to the Orange Pod, using either the Service's IP address or its name.
	* What about if other pods want access from other nodes?
		* When a service is created, it is accessible from all pods in the cluster, irrespective of node.
	* Services are hosted across the cluster.
	* Due to the Service only being available in the Cluster, this technique is called `ClusterIP`
		* For example, if the Orange Pod holds a database application that should only be accessed within the cluster, then that is totally fine.
* Another service type is `NodePort`, this is useful if we want a pod to be accessible outside of the cluster.
	* A good example is a web application that we want accessible outside of the cluster.
		* The service that is created also receives its own IP
	* All of the other pods can also still access the same pod from within the cluster as well.
	* Another side effect is that the pod will be exposed on a particular port (for example on `30080`) on **all** nodes, not just the node that the pod is hosted on.
		* This then successfully allows external users to access the service.
* How are the services getting these IP addresses?
* How are they being made available across all nodes in the cluster?
* How is the service made on a particular port on each node?

* For example, we have the following setup that consists of three nodes.
	* Node 1 on `192.168.1.11`
	* Node 2 on `192.168.1.12`
	* Node 3 on `192.168.1.13`
* Every Kubernetes node runs a Kubelet process.
	* This is responsible for creating the pods.
* Each `Kubelet` on each node watches for changes via the `kube-apiserver`
* Every time a pod is created, it goes ahead and creates the pods!
	* CNI Plugin is then invoked to configure the network for that pod.
* Each node runs another component called `kube-proxy`.
	* `kube-proxy` watches for changes in the cluster via the `kube-api` server
		* Every time a new service is created, `kube-proxy` hops into action.
* Unlike pods, services are not created per node, they are a cluster-wide concept.
	* The services exist across all nodes in the cluster.
* In fact, services don't exist per see, there is no server or service really listening on the IP of the service.
* Regarding services - no processes, namespaces or interfaces.
	* Just a virtual object.
* How do the services get an IP address and how do we access the application on a pod through a service?
* When a service is created, it is assigned an IP address from a predefined range.
	* The `kube-proxy` component on each node gets the IP address and creates forwarding rules on each node in the cluster. For example, on Node 1, Node 2 and Node 3, you would see the following:
```
IP Address (of service): 10.99.13.178:80
Forward to (pod): 10.244.1.2
```
* Therefore, whenever another pod tries to find that particular pod's IP, it gets forwarded to the right address.
	* Of course, accessible from any node in the cluster.
* Always an IP and port configuration.
	* `kube-proxy` either creates or deletes these rules.
	* How are the rules created by `kube-proxy`. Example rules are:
		* `userspace` - listen on each port per service and proxy's connections to the pods.
		* `IPVS` - the connections are done via IPVS rules.
		* `iptables`
* `proxy-mode` is set using the `--proxy-mode` option.
	* For example, like the following: `kube-proxy --proxy-mode [userspace | iptables | ipvs]`.
		* If no option is specified, `iptables` is what is defaulted to.
* More on `kube-proxy` and `iptables`:
```
kubectl get pods -o wide
```
* The above command finds the pod with the associated IP. For example, a pod called `db` that is located on `node-1`.
* A service is created called `db-service` of type `ClusterIP` and allows the pod to be made available within the cluster.
	* When the service is created, Kubernetes assigns an IP address to it.
		* The IP that is set is `10.103.132.104`
			* The IP range that is set here is not random and is set from the `kube-api-server`, which has a range of IPs created with `service cluster IP range`:
```
kube-api-server --server-cluster-ip-range ipNet (Default: 10.0.0.0/24)
```
* Can check what the `kube-api-server` is set to with this command:
```
ps aux | grep kube-api-server
```
* You see an output similar to: `--server-cluster-ip-range=10.96.0.0/12`
	* Thus this would give the services an IP starting from `10.96.0.0` to `10.111.255.255`
	* An interesting point is pod networking - for example a pod network with a CIDR range of `10.244.0.0/16`, thus providing pods IP addresses from `10.244.0.0` to `10.244.255.255`.
	* Whatever range you specify on either the Pod or Services, these shouldn't overlap.
	* Both service and pods should have their own separate dedicated range of IP addresses.
		* A pod and a service should not be assigned the same IP address.
* Can see the `iptables` rules created by `kube-proxy`
	* You can search for the name of the service - all rules created by `kube-proxy` have a comment:
```
iptables -L -t nat | grep db-service
```
* An example output is:
```
KUBE-SVC-FJSDLFJL tcp -- anywhere 10.103.132.104 /* default/db-service: cluster IP */ tcp dpt:3306
DNAT tcp -- anywhere anywhere /* default/db-service: */ tcp to:10.244.1.2:3306
KUBE-SEP-JFDSILFJ all -- anywhere anywhere /* default/db-service: */
```
* The above  says that any traffic going to `10.103.132.104` on port `3306`, is then changed to IP `10.244.1.2:3306` (this is the IP oft he pod). This is performed by adding a `DNAT` rule
* Similarly, when you create a service of type NodePort , `kube-proxy` also creates rules to forward all traffic on all ports to all nodes.
* Can find more information in the `kube-proxy` logs from `/var/log/kube-proxy.log`.
	* It will say if it uses `iptables` and if it adds an entry for a service to the database. Search for the word `proxier`.
		* If you don't see the entries, should check the verbosity of the process.