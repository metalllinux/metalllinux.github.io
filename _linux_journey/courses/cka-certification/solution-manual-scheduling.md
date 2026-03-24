---
title: "Solution Manual Scheduling"
category: "cka-certification"
tags: ["cka-certification", "solution", "manual", "scheduling"]
---

* Create the pod with `kubectl create -f nginx.yaml`.
* Why is a pod in a Pending state?
	* The Scheduler is what schedules the pod.
	* Run `kubectl describe pod nginx`
		* Check the `Node` field and it will be set to `<none>`
			* The answer then is `No Scheduler Present`
* Use `kubectl replace --force -f nginx.yaml` forcefully deletes and recreates the pod, no need to use the `kubectl delete` command.
* To continually monitor pods, use `kubectl get pods --watch`
* Cannot move one running pod from one node to another (similar to a running process on bare metal).
	* Can only delete pods on one system or node and recreate it on another.
* When you delete a pod, in the backend it has to terminate the `nginx` process.
	* It sends a kill signal to the process and it will take time to process the request and then gracefully shutdown.
* Use the `wide` option to see which node the pod is scheduled on:
```
kubectl get pods -o wide
```