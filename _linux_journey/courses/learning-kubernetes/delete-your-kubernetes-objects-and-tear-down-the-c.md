---
title: "Delete Your Kubernetes Objects And Tear Down The C"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "delete", "your", "kubernetes", "objects"]
---

* How to delete the Kubernetes resources we created. To delete the objects in the yaml files:
```
kubectl delete -f <file.yaml>
```
* The deletion looks like this:
```
myuser@myhost:~$ kubectl delete -f ./Ex_Files_Learning_Kubernetes/Exercise\ Files/04_02_Begin/deployment.yaml 
deployment.apps "pod-info-deployment" deleted
```
* In the example, we would delete:
```
busybox.yaml
deployment.yaml
quote.yaml
service.yaml
namespace.yaml
```
* To skip all of the above and just run one command, we can do the following to delete the minikube cluster:
```
minikube delete
```
* To delete all clusters, we run:
```
minikube delete --all
```