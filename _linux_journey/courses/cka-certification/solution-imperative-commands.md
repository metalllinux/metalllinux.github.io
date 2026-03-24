---
title: "Solution Imperative Commands"
category: "cka-certification"
tags: ["cka-certification", "solution", "imperative", "commands"]
---

* Create a pod:
```
kubectl run nginx-pod --image=nginx:alpine
```
* To add labels when creating a pod, use `--labels`
```
kubectl run redis --image=redis:alpine --labels="tier=db"
```
* Check the `help` output of `kubectl run` with `kubectl run --help`.
* To see the `--help` output when creating a `service`, run `kubectl create service --help`.
* To create the service on a specific service and expose a particular application (either an equals or a space can be used between `--name` and `--port`):
```
kubectl expose pod redis --name redis-service --port 6379
```
* Only use `kubectl create service` when you need to specify a particular NodePort. Otherwise just use `kubectl expose`.
* Then check the service with:
```
kubectl get svc redis-service
```
* The above will show you any `labels` or anything else attached to the pod.
* How to create a deployment using an image with 3 replicas:
```
kubectl create deployment webapp --image=kodekloud/webapp-color --replicas=3
```
* Check the deployment is up with:
```
kubectl get deploy
```
* Create an `nginx` pod that runs on port `8080`:
```
kubectl run custom-nginx --image=nginx --port=8080
```
* How to create a new namespace:
```
kubectl create namespace dev-ns
```
* How to create a deployment in a specific namespace:
```
kubectl create deployment redis-deploy --image=redis --replicas=2 -n dev-ns
```
* Check for the deployment in that particular namespace:
```
kubectl get deployment -n dev-ns
```
* How to create a pod and create a service with the same name and expose the port:
```
kubectl run httpd --image=httpd:alpine --port=80 --expose=true
```
* Then run `kubectl describe svc httpd` and you can see from the output the `Selector` tag and the `Endpoint` tag to know that it worked.