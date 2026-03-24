---
title: "Practice Test Replica Solution"
category: "cka-certification"
tags: ["cka-certification", "practice", "test", "replica", "solution"]
---

* Check how many replicasets there are.
* `kubectl get replicaset`
* How to find the images that are used to create the pods in a replicaset.
* `kubectl describe replicaset <name_of_replica_set>`
	* The image is listed under `Pod Template`.
	* You can also see the amount of pods that are ready.
* To check why the pods are not in ready status, just describe one of the pods from the `kubectl describe replicaset <name_of_replica_set>` output, with `kubectl describe pod <pod_name>`.
* Delete one of the pods.
	* `kubectl delete pod <pod_name>`
* The replicaset always ensures the amount of pods are continually available, even if you delete a pod, a new pod will be created in its place.
* Can find more information by running the `kubectl explain replicaset` command, can see `apiVersion` and similar items.
* Make sure that the labels are always the same in the replicaset yaml file.
* To check for replicasets, can use `kubectl get rs`.
* To delete replicasets, can use `kubectl delete rs replicaset-here`.
* To edit a replicaset to fix an image, can run `kubectl edit rs replicaset-here`.
	* An example is changing the container image name.
* If you update an image in a replicaset, the pods are not automatically updated or recreated.
* Can delete multiple pods by using `kubectl delete pods pod1 pod2 pod3 pod4`.
* To scale a replicaset, can use the command `kubectl scale rs replicaset-here --replicas=5`.