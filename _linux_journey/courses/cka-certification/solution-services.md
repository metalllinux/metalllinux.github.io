---
title: "Solution Services"
category: "cka-certification"
tags: ["cka-certification", "solution", "services"]
---

* How many services exist on the system? Can check with:
```
kubectl get service / kubectl get svc
```
* Can observe the `TYPE` (usually `ClusterIP`)
* To find the `Target Port`, `Labels`, `Endpoints` use `kubectl describe services`.
* When we create a pod, it is assigned a label.
	* To create a service and direct traffic to the pods, the same labels as on the pods have traffic sent to them.
		* The `kubectl describe services` command can show 4 endpoints.
			* If `Endpoints` is zero on the `service`, that means the service has not found any pods.
* How many deployments exist in the system in the current namespace?
	* `kubectl get deployments`
* What is the image being used in the `deployment`?
	* `kubectl describe deploy <deployment_name>`
* 