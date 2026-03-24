---
title: "Kube Controller Manager"
category: "cka-certification"
tags: ["cka-certification", "kube", "controller", "manager"]
---

* The `Controller-Manager` is like an office or main compartment in the master ship.
* Taking and monitoring necessary actions for when a new ship arrives.
* Another office can be one that manages the containers on the ships or manages the ships when they leave.
1. Continuously on the look out regarding the status of the ship.
2. Takes necessary actions to remediate the situation.
* In Kubernetes terms, the `Controller` is a process that continuously monitors the state of components within a system and works together to make sure the system is in the desired functioning state. 
	* For example, the `Node-Controller` is responsible for monitoring the status of the nodes and takes the necssary actions to keep the applications running. This is done via the `kube-apiserver`
![088538b1272565fb05a2e40dd2b3d011.png](../../_resources/088538b1272565fb05a2e40dd2b3d011.png)
* The `node-controller` checks the status of the nodes every 5 seconds.
	* That allows the `node-controller` to monitor the health of the nodes.
* If the heartbeat stops from a node, the node is marked as unreacheable.
	* This is a period of 40 seconds.
![95ec5da8a303e0efedb97d7181edc51a.png](../../_resources/95ec5da8a303e0efedb97d7181edc51a.png)
* After a node is marked as unreacheable, it is provided 5 minutes to come back up.
* If it does not, the `Node-Controller` removes the pods assigned to that node and provisions the pods onto a health node, if the pods are part of a replica set.
![beff54d76cebb890b024f683cb09a5ab.png](../../_resources/beff54d76cebb890b024f683cb09a5ab.png)
* The next controller is the `Replication-Controller`.
	* Responsible for monitoring the state of replication sets and ensures the desired number of pods are available at all times within the set.
![11cdc27dcd17cb62aa3cabfd0b8df82b.png](../../_resources/11cdc27dcd17cb62aa3cabfd0b8df82b.png)
* If a pod dies, the `Replication-Controller` creates another one.
* There are many more `Controllers` within Kubernetes.
![b7faddb002811a9c5895416e7b5a603f.png](../../_resources/b7faddb002811a9c5895416e7b5a603f.png)
* Whatever concepts we have seen so far such as deployments, services, namespaces, persistent volumes, this intelligence is built into the controllers.
* This is the brain behind a lot of things in Kubernetes.
* How can you see these controllers and where are they located in the cluster?
* They are all packaged into a single process called the `Kube-Controller-Manager`. When you install the `Kube-Controller-Manager`, the different controllers are installed as well.
* How do you install and view the `Kube-Controller-Manager`?
![e80a500ef6c5cf89ce95b37992bfc3a2.png](../../_resources/e80a500ef6c5cf89ce95b37992bfc3a2.png)
* When you install the `Kube-Controller-Manager`, the different controllers get installed as well.
* How to install the `kube-controller-manager`, which you can grab from the Kubernetes release page.
![9eb1b37d0c894a1aa3f2ff27a691693c.png](../../_resources/9eb1b37d0c894a1aa3f2ff27a691693c.png)
* Then run it as a service, which is the `kube-controller-manager.service` and you will see a list of options provided.
![41aff7ac6ec43610d2e4f4f67dcf4369.png](../../_resources/41aff7ac6ec43610d2e4f4f67dcf4369.png)
* The `node-monitor-period`, `node-monitor-grace-period` and `node-eviction-timeout` go in the `kube-controller-manager.service` configuration as options.
![55595739f82bc2e630e92f0d4d7e22d4.png](../../_resources/55595739f82bc2e630e92f0d4d7e22d4.png)
* There is an additional option called `--controllers`, where you can specify which controllers to enable.
![1e7413d82e01968d3f8ec1ad0732abcc.png](../../_resources/1e7413d82e01968d3f8ec1ad0732abcc.png)
* By default, all of the controllers are enabled, however you can choose a select few to use.
* If any of the Controllers do not work or do not exist, the following configuration would be a good starting point to look at.
![5b82309aa206fa9e6d1904515e342b04.png](../../_resources/5b82309aa206fa9e6d1904515e342b04.png)
* How do you view `kube-controller-manager` server options? - This depends on how you set up your cluster.
* If you set it up with the `kubeadm` tool, the `kube-controller-manager` is deployed as a pod in the `kube` (Kubernetes System) namespace in the Master Node.
![8796a9456a27b76f973723cab09910cc.png](../../_resources/8796a9456a27b76f973723cab09910cc.png)
* In a none `kubeadm` setup, you can see the options located in the pod definition file, which is in the `manifests` directory.
	* `/etc/kubernetes/manifests/kube-controller-manager.yaml`
![b068e78b4f42d25c8ebf04ac622c4869.png](../../_resources/b068e78b4f42d25c8ebf04ac622c4869.png)
* You can also see the running process and the effective options on the Master Node. Using something like `ps -aux | grep kube-controller-manager`
![c8bc3bb2f2028c1a457232f557eb64ca.png](../../_resources/c8bc3bb2f2028c1a457232f557eb64ca.png)