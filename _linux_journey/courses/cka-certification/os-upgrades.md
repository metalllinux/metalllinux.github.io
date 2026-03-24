---
title: "Os Upgrades"
category: "cka-certification"
tags: ["cka-certification", "upgrades"]
---

* What happens when one of the nodes goes down?
* If the node comes back online under 5 minutes, the `kubelet` brings the containers back up automatically.
* If the node does not come back up after 5 minutes, Kubernetes considers the node as dead.
* If the pods on the downed node are part of a replica set, they are then created on other nodes.
* The point when the pod is evicted from cluster is set by the `--pod-eviction-timeout` flag:
```
kube-controller-manager --pod-eviction-timeout=5m0s
```
* When a node goes offline, the Master Node waits for up to 5 minutes before proclaiming that the node is dead.
* When the node comes back up after the `node-eviction-timeout` has expired, it comes up blank without any containers assigned to it.
	* If `pod a` was part of a replicaset, it will have been created on another node.
	* If a pod such as `pod b` is not part of a replicaset, it is gone and won't return.
* To properly move containers from a node to another node, use the `drain <node_name>` command like so:
```
kubectl drain <node_name>
```
* The command then places any currently running containers onto other nodes instead/
* The pods are terminated on the node they were on and recreated on another node.
* The node that you run the `kubectl drain` command is then cordoned off to not allow any other containers to be assigned to it.
* To `uncordon` the node, run this command on it:
```
kubectl uncordon <node_name>
```
* The pods that moved to the other nodes however don't automatically move back to the node.
* If any new pods however are created, they would be applied to the node.
* Another command is `kubectl cordon <node_name>`
	* This makes the node unschedulable for any new containers and it does not remove or stop of the existing containers on the node.
* To mark a node as unschedulable:
```
kubectl drain <node>
```
* When running `kubectl get nodes`, you'll see the node in a `SchedulingDisabled` state.
* To bring a node out of the `SchedulingDisabled` state, we run `kubectl uncordon <node>`
* Why are the pods placed on the ControlPlane?
	* If the node has no taints placed on it, the pods will be scheduled there.
	* Check with `kubectl describe nodes <node>`
	* Usually the ControlPlane node has taints on it to stop pods being scheduled there.
* Why does `kubectl drain <node>` fail a second time?
	* When you do a drain, if there are still pods assigned to the node, it won't work .
	* ReplicaSets, Jobs, DaemonSets pods are removed much faster.
		* The ReplicaSet would then take care creating them on another node.
	* If the pod is deleted during the draining process, whatever is stored on the pod will be lost forever.
* Mark a node as scheduling disabled with `kubectl cordon <node>`