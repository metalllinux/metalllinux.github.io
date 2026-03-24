---
title: "Daemonsets"
category: "cka-certification"
tags: ["cka-certification", "daemonsets"]
---

* Replicasets and Deployments allow multiple copies of the application to be available across the worker nodes.
* DaemonSets are like Replicasets - they allow you to deploy multiple instances of pods.
	* It runs one copy of the pod on every node in the cluster.
* When a Node is removed, the pod is also automatically removed.
* The DaemonSet ensures that one copy of the pod is present across all nodes in the cluster.
* Good use cases are a `Monitoring Solution` / `Logs Viewer`
	* Deploys the monitoring agent in the form of a pod on all nodes in the cluster.
* Another component that is requires on every node in the cluster is `kube-proxy`
	* DaemonSets can also be used for this purpose.
* Networking is another good idea and an agent can be deployed on every node in the cluster.
* Creating a DaemonSet is similar to the replicaset creation process.
* Example Daemon Set:
```
apiVersion: apps/v1
kind: DaemonSet
metadata:
   name: monitoring-daemon
spec:
  selector:
    matchLabels:
	  app: monitoring-agent
  template:
    metadata:
      labels:
        app: monitoring-agent
    spec:
	  containers:
	  - name: monitoring-agent
		image: monitoring-agent
```
* Exactly the same as a Replicaset definition, except `kind` is set as `DaemonSet`.
* Then create it with `kubectl create -f <yaml>`.
* View the command using `kubectl get daemonsets`
* To see more detail about a particular daemonset command, use `kubectl describe daemonsets <daemonset_name>`
* We can replace the node_name property on a pod to bypass the scheduler and place a pod on a node directly.
	* This was in version `1.12`
* From `v1.12` onwards, `NodeAffinity` and the default scheduler are used.
* 