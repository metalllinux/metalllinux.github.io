---
title: "Manual Scheduling"
category: "cka-certification"
tags: ["cka-certification", "manual", "scheduling"]
---

* How scheduling works.
	* Don't want to rely on the built-in scheduler and want to schedule the pods yourself.
* An example pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
      - containerPort: 8080
```
* Every pod has a field called `nodeName:`, which by default is not set. Kubernetes adds it automatically.
* Kubernetes goes through all of the pods that do not have `nodeName:` set. 
* The scheduling algorithm is then ran across all of the nodes.
* Once identified, it schedules the pod on the node and the `nodeName:` property to the name of the node.
	* It creates a binding object.
* What happens if there is no scheduler to monitor and schedule nodes?
	* The pods remain in a `Pending` state.
* The easiest way to schedule a pod, is to set the `nodeName:` field in the pod's manifest file, similar to the below example:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
      - containerPort: 8080
   nodeName: node02
```
* **You can only specify a node at creation time.** - Kubernetes does not allow you to modify the `nodeName` property of a pod.
	* Another way to assign a node to an existing pod, is via creating a binding object and sending a `POST` request to the pod's binding API. This mimics what the scheduler does:
```
Pod-bind-definition.yaml

apiVersion: v1
kind: Binding
metadata:
  name: nginx
target:
  apiVersion: v1
  kind: Node
  name: node02
```
* In the binding object above, you specify the name of the node to target.
* Then send a `POST` request to the binding API:
```
curl --header "Content-Type:application/json" --request POST --data '{"apiVersion":"v1","kind":"Binding" _. } http://$SERVER/api/v1/namespaces/default/pods/$PODNAME/binding
```
* Must convert the YAML file into its equivalent JSON form.