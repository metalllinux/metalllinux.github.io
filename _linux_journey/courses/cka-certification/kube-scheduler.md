---
title: "Kube Scheduler"
category: "cka-certification"
tags: ["cka-certification", "kube", "scheduler"]
---

* This is responsible for scheduling pods on nodes.
* It is only responsible for deciding which pod goes on which node.
![b5731a8751af2bc0c285c729f1b96f5e.png](../../_resources/b5731a8751af2bc0c285c729f1b96f5e.png)
* It doesn't do the actual pod placement on the nodes.
	* That is the job of the `kubelet`.
	* The `kubelet` is the captain of the ship and creates the pod.
* The `kube-scheduler` only decides which pod goes where.
* When there are many ships and many containers, you need to make sure the right containers ends up on the right ship.
	* For example, different sizes of ships and containers.
	* Need to make sure a ship has sufficient capacity to accommodate those containers.
	* Need to place the container on the right ship to reach the correct destination.
![52a2f692fedb5abe2ee44924a8e3efb6.png](../../_resources/52a2f692fedb5abe2ee44924a8e3efb6.png)
* The scheduler decides which nodse pods are placed on, depending on certain criteria.
* May have pods with different resource requirements. 
* Can have nodes in the cluster, dedicated to certain applications.
* How does the scheduler assign the pods?
	* The scheduler looks at each pod and trys to find the best node for it.
	* The below example pod has a set of CPU requirements. The scheduler goes through two faces, to identify the best node for the pod.
![f3f6932f271da9c409adaf5b16d8503f.png](../../_resources/f3f6932f271da9c409adaf5b16d8503f.png)
* The first phase has the Scheduler filtering out the nodes, that do not fit the profile of the pod.
	* For example, the nodes that do not have sufficient CPU and memory resources , requested by the pod.
* We are now left with two nodes, where the pod can be placed.
![040b29f1d683519220b06e2c8c0291a2.png](../../_resources/040b29f1d683519220b06e2c8c0291a2.png)
* How does the Scheduler then pick one of the above nodes?
* The second phase is where the Scheduler ranks the nodes, for the best fit for the pod.
	* It uses a priority function, to assign a score on a scale of 0-10. The scheduler calculates the amount of resources that would be free on the nodes, after placing the pod on them.
	* In the example case, the node on the right would have 6 CPUs free, when the pod is placed on it. This is four more CPU cores than the node on the left.
	* Therefore the node on the right is a better rank and therefore it wins.
![5300fd36041f6bec04a5607519e195ad.png](../../_resources/5300fd36041f6bec04a5607519e195ad.png)
* The Scheduler works at a high level and the priority can be customised and you can write your own scheduler.
* There are many further topics such as `Resources Requirements and Limits`, `Taints and Tolerations` and `Node Selectors/Affinity`
	* There is an entire section dedicated to scheduling, which will go through the above.
* How do you install the `kube-scheduler`? Download it, extract it as a binary and run it as a `kube-scheduler` service:
![de8bb7597c4b7aff18da431d5f676646.png](../../_resources/de8bb7597c4b7aff18da431d5f676646.png)
* If you set it up using the `kubeadm` tool, the `kubeadm` tools deploys the `kube-scheduler` as a pod in the `kube` system namespace on the Master Node.
* The options and pod definition file is under `/etc/kubernetes/manifests/kube-scheduler.yaml`
![257c12130a2e070f821e0dfdfaf40426.png](../../_resources/257c12130a2e070f821e0dfdfaf40426.png)
* You can also see the running process and effective options by listing the process on the Master Node, using `ps -aux | grep kube-scheduler`
![58aa6f6f165ea32d1ebc58e0d40444bc.png](../../_resources/58aa6f6f165ea32d1ebc58e0d40444bc.png)