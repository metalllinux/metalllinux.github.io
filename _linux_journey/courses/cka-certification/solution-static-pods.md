---
title: "This checks all of the pods in all namespaces"
category: "cka-certification"
tags: ["cka-certification", "solution", "static", "pods"]
---

* How many static pod are there?
```
kubectl get pods -A
# This checks all of the pods in all namespaces
```
* Need to look at the yaml of the pod if want to know how many static pods exist in the cluster in all namespaces:
```
kubectl get pod kube-apiserver-controlplane -n kube-system -o yaml
```
* In the `ownerReferences` section of the output, you will see which node the static pod is attached to. It is listed under the `kind` field.
* What is the path of the directory holding the static pod definition files?
	* Can check the `kubelet` conf --> `/var/lib/kubelet/config.yaml`
		* There you can check the `staticPodPath` key to see the directory of where the pod manifest files are.
* To check the image of a Static Pod, check `/etc/kubernetes/manifests` and `cat` the file manifest file and check the `image` field.
* How to create a Static Pod (do not place anything after the `--command` argument):
```
kubectl run static-busybox --image=busybox --dry-run=client -o yaml --command -- sleep 1000
```
* Redirect it to a file:
```
kubectl run static-busybox --image=busybox --dry-run=client -o yaml --command -- sleep 1000 > manifest names
```
* Copy the manifest file to `/etc/kubernetes/manifests`.
* Edit an image on a Static Pod:
	* To make any changes on a Static Pod, just edit the file under `/etc/kubernetes/manifests/<POD_NAME>`
	* The pod will
	* Then verify with `kubectl get pods --watch`
* How to delete a Static Pod?
	* Cannot just use `kubectl delete pod`. This doesn't work, as it is a pod that the `kubelet` manages.
	* `ssh` into a node by running `kubectl get nodes -o wide` and then access the node using the `Internal IP` address from the command output or the node name.
	* Again, just to check where the Static Pods directory is, check `/var/lib/kubelet/config.yaml`