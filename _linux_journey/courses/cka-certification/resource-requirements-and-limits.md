---
title: "Resource Requirements And Limits"
category: "cka-certification"
tags: ["cka-certification", "resource", "requirements", "limits"]
---

* Every pod requires a set of resources to run.
* The `kube-scheduler` decides which node and pod is assigned to.
	* Identifies the resources of the nodes and selects the best node to place the pod on.
	* If certain nodes have no sufficient resources available, the scheduler makes sure to place a pod on a node that has resources available.
	* If no nodes in the cluster have resources available, the scheduler makes sure to hold back the pod from being deployed to a node.
		* Checking the `kubectl describe pod` command, you will see if a pod cannot be scheduled at all.
* Can specify the amount of CPU and Memory to be be applied to a container - this is known as the `Resource Request`.
	* To set this in a `pod-definition` file, can add the `resources` field like the following:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
  labels:
    name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
	ports:
	  - containerPort: 8080
	resources:
	  requests:
		memory: "4Gi"
		cpu: 2
```
* When the pod is then placed on a node, it receives a guaranteed amount of resources.
* For assigning CPU resources, you can go from `1` to `0.1`. `0.1` = `100m` (the `m` stands for milli). Can go as low as `1m`, but no lower.
* `1` CPU is equivalent to `1vCPU`, IE:
```
1 AWS vCPU
1 GCP Core
1 Azure Core
1 Hyperthread
```
* For Memory you can specify `256Mi` `Mi` = `Mebibyte` or specify the same value in memory such as `268435456` or specify it as `256M`, lots of different ways.
* Useful value to bytes breakdown:
```
1 G (Gigabyte) = 1,000,000,000 bytes
1 M (Megabyte) = 1,000,000 bytes
1 K (Kilobyte) = 1,000 bytes

1 Gi (Gibibyte) = 1,073,741,824 bytes
1 Mi (Mebibyte) = 1,048,576 bytes
1 Ki (Kibibyte) = 1,024 bytes
```
* By default, a container has no limit to the resources it can consume on a node.
	* It will suffocate the native processes on the node.
* Can specify the limits of a pod and how many resources it can consume:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
  labels:
    name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
	ports:
	  - containerPort: 8080
	resources:
	  requests:
		memory: "1Gi"
		cpu: 1
      limits:
        memory: "2Gi"
		cpu: 2
```
* What happens when a pod attempts to exceed its specified limit.
	* If that happens consistently, the pod will then be terminated.
	* You'll see an OOM memory in the logs or from the `kubectl describe` command.
* By default no CPU or memory limits are set on the pods.
### CPU `requests` and `limits`
* If a `requests` is **not** set, but we have `limits`, then Kubernetes sets `requests` to be the same value as `limits`.
* If both `requests` and `limits` **are set**, that means in a scenario where two pods are assigned to a node, the Pod B should have as many resources available as Pod A.
* If `requests` is set, but `limits` is **not**, any pod can consume as many CPU cycles as available / memory as needed. **This is the best scenario**.
* Must make sure pods have `requests` set.
### Memory `requests` and `limits`
* With `requests` and `limits` not set, all of the resources are taken up by a particular pod, leaving another pod empty.
* With `requests` **not set** and `limits` set, in one example both pods would receive 3GB of memory and no more.
* Another example is `requests` being set and `limits` also being set.
* Finally `requests` is set and `limits` is **not** set.
* Memory is tricky, as you cannot throttle memory for it to be retrieved. The only way to free up memory by a pod is to `kill` it, thus freeing up its memory.
* There is a thing called `LimitRange`s. An example for CPU is below:
```
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-resource-constraint
spec:
   limits:
   - default:
	   cpu: 500m
	 defaultRequest:
       cpu: 500m
	 max:
       cpu: "1"
	 min:
	   cpu: 100m
	 type: Container
```
* A `LimitRange` can help you define default values for containers in pods, without a request or limit specified in the pod definition file. This is applicable at the `namespace` level.
* This is an object like everything else.
* In the above example, `default` is the limit, `defaultRequest` is the request, `max` is the maximum limit and `min` is the minimum limit.
* An example for Memory is here:
```
apiVersion: v1
kind: LimitRange
metadata:
  name: memory-resource-constraint
spec:
   limits:
   - default:
	   memory: 1Gi
	 defaultRequest:
       memory: 1Gi
	 max:
       memory: 1Gi
	 min:
	   memory: 500Mi
	 type: Container
```
* If you create or change a `LimitRange`, it does not affect existing pods and only affects newer pods created.
* How can you restrict the total amount of resources by all of the pods on one cluster. To do that, we create a quota at the `namespace` level.
* An example quota:
```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: my-resource-quota
spec:
  hard:
	 requests.cpu: 4
     requests.memory: 4Gi
	 limits.cpu: 10
	 limits.memory: 10Gi
```
* The above resource constraints relate to all of the pods' resource usage added together.
* Another example of a good CPU and Memory pod resource restraint combination:
```
apiVersion: v1
kind: Pod
metadata:
  name: elephant
  labels:
    name: elephant
spec:
  containers:
  - name: elephant
    image: polinux/stress
    ports:
      - containerPort: 8080
    resources:
      requests:
        memory: "20Mi"
        cpu: 1
      limits:
        memory: "20Mi"
        cpu: 2
```