---
title: "Solution Resource Limits"
category: "cka-certification"
tags: ["cka-certification", "solution", "resource", "limits"]
---

* Check pod resource limits by using `kubectl describe pod ~`
* Can check `Last State` field from the `kubectl describe pod ~` command, to see why pods are killed and go out of memory.
* How to increase the memory of a pod.
* You can see why a pod is being killed via the `kubectl describe` command.
	* Check the `Command` that it is running.
	* `Limits` in this case is set to `10Mi`.
	* However, `Requests` is set to `5Mi`.
	* That difference between the `Limits` and `Requests` fields is why the pod is going OOM.
* One way to increase the memory is by `kubectl edit` - sometimes it is not possible to change the limit in `edit`.
	* You cannot edit a running pod.
	* However, if you do change a running pod, the changes will be set to a temporary file.
* The easier way is using the `kubectl replace --force -f` command. This will delete the existing pod and recreate it.
	* `-f` is not `force` in this case.
* 