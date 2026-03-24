---
title: "Cluster Architecture"
category: "cka-certification"
tags: ["cka-certification", "cluster", "architecture"]
---

* Purpose of Kubernetes is to host your containers in an automated fashion, so you can deploy many instances of an application.
	* Also easily enable communication between different services in your application.
* Good analogy - cargo ships that take containers across the sea and control ships for managing and monitoring the cargo ships.
* Kubernetes cluster is a set of nodes - either physical or virtual, on-premise or on cloud, that host applications in the form of containers.
* Worker Nodes in the cluster are ships that load containers (host application as containers) - not just load, plan, store information about the ships, monitor and track the location of containers on the ships.
* The Master Node (Control Ships) relate to the Kubernetes cluster - these manage, plan, schedule and monitor nodes. Planning which containers go where, monitoring the nodes and the containers on them and more.
	* The Master Node does alll of the above, using the Control Plane components.
* On a daily basis, lots of containers are loaded and unloaded onto each ship, what time the containers were stored, which ship it was. These are stored on the `etcd` cluster.
	* `etcd` is a database that stores in formation in a key value format.
* A crane identifies which containers go on which ship - it knows this based on its size and capacity and how many containers are on which ship. In addition, any other conditions - where the ship is going, what containers the ship is allowed to carry, etc.
	* This is a `kube-scheduler` in the Kubernetes cluster.
		* Depends the right node to place a container on, based on the container's resource requirements, the worker node's capacity and any other constraints such as taints and tolerations or node affinity rules.
* There are different offices in the dock, which are assigned to different tasks or departments.
* The cargo team takes care of containers. If containers are damaged or destroyed, new ones are created.
* The services office takes care of IT and communications between different ships.
* All controllers are held together by the Controller-Manager
* Controllers are available, which take care of different areas - Node-Controller and Replication-Controller
* Node-Controllers - this takes care of the nodes, responsible for onboarding new nodes to the cluster, handling situations when nodes become unavailable or gets destroyed.
* The Replication-Controller - ensures the desired number of containers are running at all times in a replication group.
* How do all of the services communicate with each other? The kube-apiserver is the primary management component of Kubernetes - responsible for orchestrating all operations within the cluster. 
	* It also exposes the Kubernetes API to external users and this performs management operations on the cluster.
		* This connects to the Controller-Manager, etcd-cluster and kube-scheduler.
	* It monitors the state of the cluster and makes necessary changes to the cluster.
* We need everything to be Container compatible. Applications are in the form of containers.
	* DNS server can be deployed in the form of containers.
	* The software that runs the containers is the Container Runtime Engine - popular one is Docker. Docker would have to be installed on all of the nodes in the cluster.
		* This also includes the Master Nodes, if you wish to host the controlling components as containers.
* Kubernetes supports other runtime engines, such as containerd, a rkt, 
* Each ship has a captain and is responsible for managing all activities on the ships.
	* The captain tells the Master Ship that they are interested in joining the group, receiving information about the containers to be loaded on the ship and loading the appropriate containers as required, sending reports back to the Master Ship about the status of the ship and the status of the containers on the ship, etc.
* The captain of a ship is the kubelet in Kubernetes.
* A kubelet is an agent that runs on eaech node in the cluster.
	* It listens for instructions from the kube API server and deploys or destroys containers on the nodes as required.
	* The kube-api server occassionally gets reports from the kubelet to monitor the status of nodes and containers on them. 
* The applications running on the worker nodes, need to be able to communicate with each other.
	* For a example, a web server running on one container of one node and a database server running on another container from another node.
		* How would the web server reach the database server?
			* Communication between worker nodes is enabled, by a component that runs on the worker node called the kube-proxy service. 
				* The kube-proxy service allows the containers running on each worker node to reach each other.
![Screenshot_20240805_220526.png](../../_resources/Screenshot_20240805_220526.png)
