---
title: "Pod Networking"
category: "cka-certification"
tags: ["cka-certification", "pod", "networking"]
---

* Configure 3 nodes.
* Create configurations for firewalls. Set up things like CNI networking as well.
	* Allow the Kubernetes Control Plane components to reach each other.
* The Control plane components have also been set up such as the `etcd server`, `kubelets` and so on. We can finally deploy the applications.
* Another crucial part is networking at the pod layer.
* The cluster will have pods and services running on it. How are the pods addressed?
	* How do they communicate with each other?
	* How do the pods interact with each other internally in the cluster?
	* Similarly how do they interact externally outside the cluster as well?
* Kubernetes does not come with a built-in solution. It expects a networking solution to solve the challenges.
	* Kubernetes does however have requirements for pod networking.
		* Every POD should have a unique IP address.
		* Every POD should be able to communicate with every other POD in the same node. This is using the same IP address.
		* Every POD should be able to communicate with every other POD on other nodes without NAT. Similarly the same IP address should also be used here.
	* Kubernetes doesn't care what the IP address is or what range or subnet it belongs to.
	* As long as a solution can be implemented to take care of IP addresses and establish connectivity between pods in a node, as well on pods in different nodes?
* How do you implement a model that solves these requirements?
	* Examples are `flannel`, `cilium`, `nsx`.
* Have a three node cluster, this includes the following nodes:
	* Node 1 - `192.168.1.11`
	* Node 2 - `192.168.1.12`
	* Node 3 - `192.168.1.13`
		* All three nodes are connected to the same LAN of `192.168.1.0`
* When containers are created in Kubernetes, it make network namespaces for them.
	* To enable communication between the nodes, we attach the namespaces to a network. Which network?
		* An example as previously discussed is `bridge` networks - created within nodes to attach namespaces.
	* Therefore, each node now has a `bridge` network set on them:
	* Node 1 - `ip link add v-net-0 type bridge`
	* Node 2 - `ip link add v-net-0 type bridge`
	* Node 3 - `ip link add v-net-0 type bridge`
	* Then each node has the interface brought up:
	* Node 1 - `ip link set dev v-net-0 up`
	* Node 2 - `ip link set dev v-net-0 up`
	* Node 3 - `ip link set dev v-net-0 up`
* Each `bridge` network needs to be on its own subnet.
	* Choose a private address range. In each node, the `bridge` would look like this:
	* Node 1 - `10.244.1.0/24`
	* Node 2 - `10.244.2.0/24`
	* Node 3 - `10.244.3.0/24`
	* Then we set the IP for the `bridge` interface:
	* Node 1 - `ip addr add 10.244.1.1/24 dev v-net-0`
	* Node 2 - `ip addr add 10.244.2.1/24 dev v-net-0`
	* Node 3 - `ip addr add 10.244.3.1/24 dev v-net-0`
* The remaining steps are performed via a scrip. This can be applied per container:
```
net-script.sh
# Create veth pair
ip link add ...

# Attach one end to the bridge
ip link set ...

# Attach one end to the container
ip link set ...

# Assign an IP address
ip -n <namespace> addr add ...

# Add a route to the default gateway
ip -n <namespace> route add ...

# Bring up the interface
ip -n <namespace> link set ...
```
* The above script is copied to other nodes and they have an IP assigned to them as well and connect to the `bridge` network within their own internal networks.
* To attach a container to a network, we need a pipe.
	* This is a virtual network cable.
* What IP do we add? We either manage it ourselves or store it inside a database.
	* The example IP to apply to a container is `10.244.1.2` - this is a free IP in the subnet.
* Now we want the pod on `Node 1` with an address of `10.244.1.2` to connect to the pod on `Node 2` at `10.244.2.2`
	* The `10.244.1.2` pod has no idea of the container on `Node 2`.
		* It will try to route to `Node 1`'s IP, as it is set as the default gateway on `192.168.1.11`
			* Therefore, add a route to `Node 2`, where the information will be routed appropriately --> `ip route add 10.244.2.2 via 192.168.1.12`
				* Once the route is added, the `blue` pod can then ping across.
					* Similarly on the other hosts, we run the above `ip route add` command so that each container is aware of where the other container is on the other hosts.
* An easier way however instead of doing the `ip route add` setup per node, is to just point all of the hosts to a Router and use that as the `default gateway`.
	* Can therefore easily manage routes to all routes on the router.
```
Network        Gateway
10.244.1.0/24  192.168.1.11
10.244.2.0/24  192.168.1.12
10.244.3.0/24  192.168.1.13
```
* With that, regarding the individual networks that were created of `10.244.1.0/24` on each node, this now forms a large network as one big `bridge` network encompassing all of the nodes. This being `10.244.0.0/16`.
* How do we run the above script automatically, when a pod is created on Kubernetes?
	* That is where CNI is used - middle man. CNI tells Kubernetes when to call a script, as soon as a container is created.
		* CNI tells us this is how your script should look like. The script needs to be modified to meet the CNI standards:
```
ADD) 
# Create veth pair
ip link add ...

# Attach one end to the bridge
ip link set ...

# Attach one end to the container
ip link set ...

# Assign an IP address
ip -n <namespace> addr add ...

# Add a route to the default gateway
ip -n <namespace> route add ...

# Bring up the interface
ip -n <namespace> link set ...
DEL)
  # Delete veth pair
  ip link del ...
```
* The `Add` section takes care of adding a container to the network.
* `DEL)` deletes the IP address and frees up the network.
* The container runtime on each node is responsible for creating containers.
* When a container is created, the container runtime looks at the CNI configuration, that being `/etc/cni/net.d/net-script.conflist` - passed as a cmdline argument when it was run.
	* Identifies the script's name.
	* Looks in the CNI's `bin` directory --> `/opt/cni/bin/net-script.sh` --> Executes the script with the `add` command `./net-script.sh add <container> <namespace>` --> The script takes care of the rest.