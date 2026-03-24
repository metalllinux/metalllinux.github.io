---
title: "Check The Health Of A Pod By Looking At The Event"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "check", "health", "pod", "looking"]
---

* Possible errors are:
	* Container image is unavailable, therefore causing an error.
	* Out of space on the worker nodes, so the pod cannot be scheduled.
	* A typo can cause the pod to start running and then suddenly stop.
* Kubernetes saves the event logs when a pod is created.
* Allows you to troubleshoot issues.
* To get information about a `pod`, we run:
```
kubectl describe pod pod-info-deployment-7587d5cc86-lkccq -n development
```
* The event logs will be at the bottom of the output.
* If the pod has been up and running for a while, you will not see any information in the event logs.
	* Kubernetes is then letting the pod do its own thing, because it is healthy.
* Most issues with pods occur within 1 minute of their lifecycle.