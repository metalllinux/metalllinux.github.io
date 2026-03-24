---
title: "Pods With Yaml"
category: "cka-certification"
tags: ["cka-certification", "pods", "yaml"]
---

* Kubernetes uses YAML files as the input for objects - pods, replics, deployments, services etc.
* A Kubernetes Definition File always contains 4 top level fields:
	* `apiVersion` - version of the Kubernetes API used to create the object. An example is `v1`. Others are listed below:
![54d7caa0e7ba3fdd2ce49e2b5b80716c.png](../../_resources/54d7caa0e7ba3fdd2ce49e2b5b80716c.png)
	* `kind` - type of object we are trying to create. An example is `Pod` Other possible values are `ReplicaSet`, `Deployment` or `Service`
	* `metadata` - data about the object - `name`, `labels`, `app`. The values shown are in the form of a dictionary. Everything is indented to the right, so for example `name` and `labels` are children of `metadata`. The number of spaces between the two properties does not matter. You cannot have more indents for `labels` for example, as it then becomes a child of the `name` property. The two properties also need more spaces ahead of their parent `metadata`. `name` is a string value. `labels` is a dictionary within the `metadata` dictionary. It can have any key / value pairs as required. The labels help you identify the object at a later point in time. Cannot add any old property under `metadata`.
	![6042c6e002cb0b3334ebd198a44c33ee.png](../../_resources/6042c6e002cb0b3334ebd198a44c33ee.png)
	![704030a777f60aa7a4c1718176778c01.png](../../_resources/704030a777f60aa7a4c1718176778c01.png)
	![2dcdb10a3243e676bd6e02c2463d4f30.png](../../_resources/2dcdb10a3243e676bd6e02c2463d4f30.png)
	![1e5f2885fe1b66da856fde1e585c4d44.png](../../_resources/1e5f2885fe1b66da856fde1e585c4d44.png)
	* `spec` - specifies the container / image needed in the pod. Provides additional information to Kubernetes, regarding the object. Refer to the documentation to understand the right format for each. `spec` is a dictionary. We add a property under it called `containers`. `containers` is a list / array. This is due to pods having multiple containers within them. A `-` before the word `name:` indicates the first item in the list. `name` and `image` are dictionary properties. In this case, `image` is `nginx`, which is the name of the image in the Docker repository. 
![60101dd4e8d3fda420e77003705194f7.png](../../_resources/60101dd4e8d3fda420e77003705194f7.png)
* Required fields and they must be in the configuration file.
* Once the YAML file is created, we run `kubectl create -f pod-definition.yml `
* Kubernetes then creates the pod.
* See the pods with `kubectl get pods`
* To see detailed information about the pod, run `kubectl describe pod <pod_here>`
	* Shows the following:
		* When it was created.
		* What labels are assigned to it.
		* What docker containers are part of it.
		* What are the events associated with that pod.
		* 