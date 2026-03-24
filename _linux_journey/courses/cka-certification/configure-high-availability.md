---
title: "Configure High Availability"
category: "cka-certification"
tags: ["cka-certification", "configure", "high", "availability"]
---

* If you lose the Master Node, this is not the end of the world - as long as your Worker Nodes and their applications are up and running, this is good.
	* If for example a pod on a Worker Node crashes however the replica set controller on the Master Node would need to tell the Worker Node to create a new pod.
		* However, the Master Node is not available, nor are any of the controllers and schedulers on the Master Node.
			* The kube-api server would also not be available and you could not access the cluster externally.
	* Therefore, multiple Master Nodes are needed for a high availability configuration.
* Having High Availability means you have redundancy across every component in the cluster.
	* Therefore, no single point of failure.
* Focus will be Master and Control Plane components.
* Remember, the Master Node hosts these components:
	* ETCD
	* API Server
	* Controller Manager
	* Scheduler
		* In an HA setup, the same components from above would also run on the new Master Node as well.
	* How does running multiple instances with the same components work?
		* They work on one request at a time.
		* All of the components on both Master Servers can be running at the same time.
* The Kube Controller utility talks to the API Server to have things done.
	* The Kube Control utility needs to reach the Master node at port `6443`.
		* With two Master Nodes in play, which do we point the kubectl to?
			* Should send the same request to both of them.
				* Need a load balancer configured in front of the Master Nodes, which splits traffic between the API servers.
					* We then point the Kubectl utility to that load balancer.
						* Can use HAProxy, Nginx and so on as the load balancer.
* What about the Scheduler and Controller Manager?
	* These are Controllers that watch the state of the cluster and take actions.
* The Controller Manager consists of things like the Replication Controller.
	* This watches the state of pods and takes the necessary actions.
		* Creating a new pod when one fails for example.
	* If multiple instances run in parallel, may duplicate actions and therefore create more pods than is actually required.
	* Therefore, a pair of two Master Nodes would run in a "Active" / "Standby" mode. One would be "Active" and the other would be in "Standby" mode.
		* Whom decides among the two which is active and which is passive - this is decided through a leader election process.
			* When a ControllerManager process is elected, must specify the `leader-elect` option using the below command:
```
kube-controller-manager --leader-elect true [other option]
```
* With `leader-elect` set to `true`, with this option, a `Lock` is placed on the Kube-Controller-Manager Endpoint. Whichever process updates the endpoint with its information, receive the lease and becomes the active of the two. The other becomes passive.
* There is also the `--leader-elect-lease-duration 15s` option. This is by default set to 15 seconds.
* The lease is renewed every 10 seconds. This is the `--leader-elect-renew-deadline` measure.
* Both of the processes try to become the leader every 2 seconds, which is set via the `--leader-elect-retry-period` option.
	* If one process fails due to the Master Node crashing, the other process can then acquire the Master Lock.
* Regarding ETCD.
	* There are two topologies.
		* `Stacked Control Plane Nodes Topology`
			* Requires fewer nodes.
			* Redundancy can be compromised, if Control Plane instances are lost.
		* The other is when ETCD is separated from the Control Plane nodes and ran on its own set of servers. This topology is called `External ETCD Topology`
			* Less risky - a failed Control Plane node does not affect the cluster.
				* Requires twice the amount of servers however, for the ETCD nodes.
* Check under the `/etc/systemd/system/kube-apiserver.service` and you'll see an option like `--etcd-servers=` and can then assign the ETCD server that way.
	* The API Server needs to point to the right address of the ETCD server.
		* Can read and write data through any of the available ETCD server instances.
			* That's why a list of ETCD servers is specified in the kube-api configuration.