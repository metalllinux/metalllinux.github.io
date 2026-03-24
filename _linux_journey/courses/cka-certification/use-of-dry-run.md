---
title: "Use Of Dry Run"
category: "cka-certification"
tags: ["cka-certification", "dry", "run"]
---

* To test what the command will do and if the resource can be created, use `--dry-run=client`
* `-o yaml` outputs the resource definition yaml to the screen.
* Create a pod manifest YAML file:
```
kubectl run nginx --image=nginx --dry-run=client -o yaml
```
* Create a deployment:
```
kubectl create deployment --image=nginx nginx
```
* Generate a deployment YAML file:
```
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml
```
* Create deployment with 4 replicas:
```
kubectl create deployment nginx --image=nginx --replicas=4
```
* Scale a deployment using `kubectl scale`:
```
kubectl scale deployment nginx --replicas=4
```
* Another way is to save the YAML definition to a file and modify it:
```
kubectl create deployment nginx --image=nginx -dry-run=client -o yaml > nginx-deployment.yaml
```
* Can then update the YAML file with the replicas or another field before creating the deployment.
* Create a service called `redis-service` of type `ClusterIP` to expose pod `redis` on port `6379`:
```
kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml
```
* The above then automatically uses the pod's labels as selectors.
* OR
```
kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml
```
* The above does not use pod labels as selectors. It assumes selectors as `app=redis`. Selectors **Cannot be passed in as option**.
* Create a service of `nginx` with type of `NodePort` to expose pod `nginx's` port `80` on port `30080` on the nodes:
```
kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml
```
* The above automatically uses the pod's labels as selectors. **Cannot specify the node port**. Must generate a definition file and add the node port manually before creating the service with the pod.
* OR
```
kubectl create service nodeport nginx --tcp=
80:80 --node-port=30080 --dry-run=client -o yaml
```
* The above does not use the pod labels as selectors.
* The better method is `kubectl expose`
* If a Node Port needs to be specified, create a definition file using the same command and manually input the nodeport before creating the service.