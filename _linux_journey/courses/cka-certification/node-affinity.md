---
title: "Node Affinity"
category: "cka-certification"
tags: ["cka-certification", "node", "affinity"]
---

* Node Affinity ensures that a certain pod is assigned to a particular node (one with large resources for example).
* The output is more complex that with `nodeSelectors`:
```
pod-definition.yaml
apiVersion:
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: data-processor
    image: data-processor
  affinity:
   nodeAffinity;
     requiredDuringSchedulingIgnoredDuringExecution:
		 nodeSelectorTerms:
         - matchExpressions:
           - key: size
			 operator: In
			 values:
             - Large
```
* `nodeSelectorTerms:` is the array. The `key:value` pairs are underneath that.
* The `operator: In` key value, regarding `In`, that ensures the pod will be placed on a node with a value that is located in the `values:` key below that, in this case `Large`.
* To place a pod on either a large or medium node, you can also add the `Medium` value:
```
values:
- Large
- Medium
```
* You can also tel the pod to not be assigned to any nodes that are labelled as `Small`:
```
- matchExpressions:
  - key: size
	operator: NotIn
	values:
	- Small
```
* There is also the `Exists` operator, which can provide a similar result to `NotIn`. This checks if the label exists on the node and thus the `values` section is not required.
```
- matchExpressions:
  - key: size
    operator: Exists
```
* What if a Node Affinity cannot match any nodes - for example, no nodes had the label of `size`. How do we assign the pod?
* What if someone changes the label on the node at a later date.
	* This is handled by the `requiredDuringSchedulingIgnoredDuringExecution` property under `nodeAffinity`.
		* This defines the Scheduler in respect to Node Affinity and defines the lifecycle of the pod.
* There are two types of node Affinity:
```
requiredDuringSchedulingIgnoredDuringExecution
preferredDuringSchedulingIgnoredDuringExecution
```
* There is an additional Node Affinity being planned:
```
requiredDuringSchedulingRequiredDuringExecution
```
* Regarding the below two types:
```
requiredDuringSchedulingIgnoredDuringExecution
preferredDuringSchedulingIgnoredDuringExecution
```
* In a pod's lifecycle, there are two things to be aware of:
```
DuringScheduling
```
- This is when a pod does not exist and is created for the first time.
* For `requiredDuringScheduling`, the Scheduler will mandate the pod be applied with the given affinity rules.
	* If it cannot find an applicable node, the pod will not be scheduled.
* What if the pod placement is better than running the workload itself? In that case we set it to `preferredDuringScheduling`.
	* If a node is not found, the Scheduler then ignores Node Affinity rules and places the pod on any available node.
		* I.E. the Scheduler will do its best to find a matching node, but if it cannot find one, it will place it on any node.
* The other state as shown above is `DuringExecution`.
	* This is where a change is applied in the environment and affects Node Affinity - for example, the change in a label of the node.
		* In the current example, the current is `IgnoredDuringExecution`. This means that the pods will continue to run and any changes in Node Affinity will not impact them once they are scheduled.
* The upcoming one in the future only has differences in the `DuringExecution` phase. This is the `requiredDuringSchedulingRequiredDuringExecution` Affinity.
	* This will therefore automatically evict any pods that running on the nodes that do not meet the Node Affinity rules.
		* If the label `Large` is removed from a node for example, it will be affected.