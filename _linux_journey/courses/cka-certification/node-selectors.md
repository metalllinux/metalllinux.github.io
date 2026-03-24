---
title: "Node Selectors"
category: "cka-certification"
tags: ["cka-certification", "node", "selectors"]
---

* For example, you have a cluster with 3 nodes (two with fewer resources).
	* Want to dedicate higher horse power jobs to the larger node.
	* In the default setup, any pods can go to any nodes.
	* To solve this, we can set a limitation on the pods to only run on certain nodes.
* There are two ways to do this:
* Node Selectors - added to the pod definition file.
* Eaxmple pod definition file:
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
```
* To limit the above pod to the larger node only, the `nodeSelector` property is added:
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
  nodeSelector:
    size: Large
```
* How does Kubernetes know which is the `Large` node?
* The Scheduler uses the above `size` labels to match the pods to the right node.
* You must first however label the nodes, prior to pod creation.
* Again, to label nodes:
```
kubectl label nodes <node-name> <label-key>=<label-value>
```
* For example:
```
kubectl label nodes node-1 size=large
```
* Then create the pod with `kubectl create -f pod-definition.yaml`
* nodeSelectors do have limitations - you cannot set them to be assigned to either a `Large or Medium size node` or any nodes that are `small` as examples.