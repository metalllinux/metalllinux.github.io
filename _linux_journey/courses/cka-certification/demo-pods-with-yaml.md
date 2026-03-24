---
title: "Demo Pods With Yaml"
category: "cka-certification"
tags: ["cka-certification", "demo", "pods", "yaml"]
---

* Will create a pod and not use the `kubectl` command.
* Will create it using a `yaml` definition file.
* The `yaml` file will have the pod specifications inside it.
* Create `pod.yaml`.
* Start with the 4 root level properties.
	* `apiVersion`
	* `kind`
	* `metadata`
	* `spec`
* We set the `apiVersion` as `v1`
* `kind` is set as `Pod`
* `metadata` is a dictionary.
	* Define the `name` of the pod (in this case `nginx`)
	* Additional `labels` can be specified.
		* `labels` is also a dictionary.
			* Can specify a label that is a key value pair, in this case `app: nginx`
			* Can add additional labels such as `tier` and set it to `frontend`
				* The `tier` label allows the pod to be grouped.
* Next, the `spec` must also be defined and this is a dictionary.
	* `spec` contains an object called `containers`.
* It is recommended not to use tabs in `yaml` files and just add two spaces for all of the children objects. Something like the below.
```
metadata:
  name: nginx
```
* A container is a list of objects.
* We give the `container` a name and this is the name of the container in the pod.
* Of course, multiple containers can be included.
```
spec:
  containers:
  - name: nginx
		image: nginx
	- name: busybox
	  image: busybox
```
* The `image` name is the Docker Hub image that we are going to create.
	* If you are using other registries aside from Docker Hub, provide the full path to the repo in the `image` line.
* Lists are defined with a `-` and then followed by the objects.
* Full file:
![8dcc535be1229071a39fbd0e0d664bad.png](../../_resources/8dcc535be1229071a39fbd0e0d664bad.png)
* `kubectl apply` or `kubectl create` work in the same fashion when creating a new object.
* We run `kubectl apply -f pod.yaml` The `-f` means `file`
* Check the status with `kubectl get pods`
* Will go from `ContainerCreating` state to `Running` state.
* To get more information about the pod, run `kubectl describe pod <name>`