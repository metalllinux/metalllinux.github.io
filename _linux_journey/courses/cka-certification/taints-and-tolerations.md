---
title: "Taints And Tolerations"
category: "cka-certification"
tags: ["cka-certification", "taints", "tolerations"]
---

* How you can restrict which pods are placed on certain nodes.
* A bug is intolerant to the smell of the `taint` applied to the person.
	* There are other insects that like this smell however.
	* There are two things that make a bug like a person:
		* First is the taint on the person.
		* Second is the bug's toleration level on that particular taint.
* In Kubernetes, the bug is a pod and the person is a node.
* The `scheduler` attempts to place pods on nodes and attempts to balance them across the nodes equally.
* We can prevent pods by placing a `taint` on a node.
	* For example, setting `Taint=blue` on node 1 and thus all pods are assigned to Node 2 and Node 3 instead. 
	* Can add a toleration for the `taint` to a pod. For example pods A, B and C cannot be assigned to node 1 due to `Taint=blue` being applied to the node. However pod D has a tolerance added to it for `blue`.
		* Thus the `scheduler` can assign pod `D` to `node 1`.
* `Tolerations` are set on pods.
* How to `taint` a node?
```
kubectl taint nodes node-name key=value:taint-effect
```
* For example, to assign pods that are allocated to `application blue`, the example output would be:
```
kubectl taint nodes node-name app=blue:taint-effect
```
* There are three `taint` affects that are applied to pods:
	* `NoSchedule` - pods will not be scheduled on the nodes.
	* `PreferNoSchedule` - the system will try to avoid placing a pod on a node, but it is not guaranteed.
	* `NoExecute` - new pods will not be scheduled on the nodes and existing pods on the nodes will be evicted, if they do not tolerate the `taint`. Those pods may have been scheduled on the node, before the `taint` was applied.
* An example command to `taint` `Node 1`:
```
kubectl taint node node1 app=blue:NoSchedule
```
* How to add a `toleration` to a pod?
* Firstly, open the `pod-definition.yaml` file:
```
apiVersion:
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
```
* We add the `tolerations` to the file:
```
apiVersion:
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: nginx-container
    image: nginx

  tolerations:
  - key:"app"
    operator: "Equal"
    value: "blue"
    effect: "NoSchedule"
```
* Double quotes are needed.
* When the pods are either created or updated with the above, they are either not scheduled to a node or are evicted from a node.
* Regarding the `NoExecute` `Taint`:
	* When this is applied to a node, if the appropriate `tolerance` is not set on a pod, it is killed.
* `Taints`and `Tolerations` will not further schedule pods to other nodes.
* The `Master` / `Control Plane` node does all of the management.
* The `Scheduler` does not schedule any pods on the Master Node.
	* When the cluster is first set up, an automatic `taint` is set up on the Master Node, to stop any pods from being applied.
	* To see the `taint`, run the following command:
```
kubectl describe node kubemaster | grep Taint
```