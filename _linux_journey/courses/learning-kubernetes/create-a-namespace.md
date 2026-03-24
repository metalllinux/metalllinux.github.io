---
title: "Create A Namespace"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "create", "namespace"]
---

* Kubernetes Workspaces, allow you to isolate and organise your workloads.
* Good to create different namespaces, to organise applications and microservices.
	* For example, if you have your development and production environments running in the same Kubernetes cluster, you can separate the applications running in each environment.
	* Can separate these by deploying one into a namespace called `development` and another one for `production`.
* To get the namespaces, use the following command:
```
kubectl get namespaces
```
* This wil output something like:
```
NAME              STATUS   AGE
default           Active   11h
kube-node-lease   Active   11h
kube-public       Active   11h
kube-system       Active   11h
```
* Kubernetes manifest for a namespace:
```
---
apiVersion: v1
kind: Namespace
metadata:
  name: development
```
* The only field of importance in the above example, is the `name` field.
* To create the namespace from a manifest, we run:
```
kubectl apply -f <yaml file>
```
* We can place multiple resources in one file, by separating them with horizontal dashes.
* To add a second namespace called `production` to the file, we add:
```
---
apiVersion: v1
kind: Namespace
metadata:
  name: development
---
apiVersion: v1
kind: Namespace
metadata:
  name: production
```
* Then again run `kubectl apply -f <yaml file>`.
* Finally, to delete namespace, we run:
```
kubectl delete -f namespace.yml 
```
