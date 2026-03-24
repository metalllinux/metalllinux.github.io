---
title: "Solution Taints And Tolerations"
category: "cka-certification"
tags: ["cka-certification", "solution", "taints", "tolerations"]
---

* How many nodes exist on the system:
```
kubectl get nodes
```
* Do any `taints` exist?
	* Use `kubectl describe node <node_name>`
* How to create a `taint` on `Node01`:
```
kubectl taint node node01 spray=mortein:NoSchedule
```
* To check help, use `kubectl taint --help` and there are multiple examples there.
	* Key is `spray`. Value is `mortein` and the Effect is `NoSchedule`
* Can then check the above under `Taints` from `kubectl describe ~`
* Create a pod with `kubectl run <pod> --image=nginx`
* Cannot specify `Toleration` Imperatively in the command line.
* Then we do the following to generate a yaml file for the pod:
```
kubectl run bee --image=nginx --dry-run=client -o yaml > bee.yaml
```
* Then edit the `bee.yaml` file with these tolerations:
```
tolerations:
       - key: spray
         value: mortein
         effect: NoSchedule
         operator: Equal
```
* Then create the image: `kubectl create -f bee.yaml`
* Check for all pods and which nodes they are assigned to with `kubectl get pods -o wide`
* To remove a `taint`:
```
kubectl taint node controlplane node-role.kubernetes.io/master:NoSchedule-
```