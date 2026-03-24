---
title: "Solution Secrets"
category: "cka-certification"
tags: ["cka-certification", "solution", "secrets"]
---

* How to create a `secret` imperatively:
```
kubectl create secret generic db-secret --from-literal=DB_Host=sql01 --from-literal=DB_User=root --from-literal=DB_Password=password123
```
* Example of a pod loading `secrets` using `envFrom`:
```
---
apiVersion: v1 
kind: Pod 
metadata:
  labels:
    name: webapp-pod
  name: webapp-pod
  namespace: default 
spec:
  containers:
  - image: kodekloud/simple-webapp-mysql
    imagePullPolicy: Always
    name: webapp
    envFrom:
    - secretRef:
        name: db-secret
```
* Then run `kubectl edit pod <pod_name>` to get the location of the temporary file where the changes are at.
* Then to recreate and delete the pod, run `kubectl replace --force -f /tmp/kubectl-edit-<numbers>.yaml`
* How many `secrets` exist in the default namespace?
```
kubectl get secrets
```
* How many secrets are defined?
	* Check under `kubectl describe secrets <secret_name>` and look for everything under `Data`
* Check the services `kubectl get svc`
* Create a `secret` --> `kubectl create secret generic <name_of_secret> --from-literal=DB_Host=sql01 --from-literal DB_User=root --from-litereal DB_Password=password123`
	* Then check with `kubectl get secret` and `kubectl describe secret <secret>`
* To add a `secret` to an already running 