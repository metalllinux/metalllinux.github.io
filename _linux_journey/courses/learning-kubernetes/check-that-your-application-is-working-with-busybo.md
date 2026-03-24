---
title: "Check That Your Application Is Working With Busybo"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "check", "your", "application", "working"]
---

* How to verify that an application is working as expected? One way is to use tooling such as busybox.
* BusyBox --> Swiss Army Knife of Embedded Linux.
	* Binary that contains many UNIX tools such as `awk`, `date`, `wget` and `whoami`
	* Good tool for debugging and troubleshooting issues.
* We will use a `deployment` yaml file to create the BusyBox pod.
* This will only be deployed in the `default` namespace. It will run only 1 replica.
```
kubectl apply -f busybox.yml
```
* Then run the following to check that the pod is running: `kubectl get pods`
	* If you don't specify `-n`, `kubectl` will assume you want the `default` namespace.
* Want to use BusyBox, for an HTTP GET request to the application. Need to know the IP address of the pods, in order to accomplish that.
* Then we run:
```
kubectl get pods -n development -o wide
```
* `-o wide` shows additional information about the pods, including their IP addresses inside the Kubernetes cluster.
* Need to get inside the `busybox` pod, so we can use the `wget` tool to make an HTTP request.
* Use the `kubectl` command, `exec`
* `busybox-74b7c48b46-wzhnt`
* To `exec` into the `pod`, we use:
```
kubectl exec -it busybox-74b7c48b46-wzhnt -- /bin/sh
```
* `-it` means we want to access the pod and use an interactive terminal.
* Then we need to specify the shell with:
	* In this case, the `/bin/sh` uses the `Executable Shell`, but we can use any Shell that we like.
* If you run the `wget` command inside a container, you will receive the following:
```
Connecting to 10.244.0.7 (10.244.0.7:80)
wget: can't connect to remote host (10.244.0.7): Connection refused
/ # 
```
* Remember in the `deployment.yml` file, the pod was set up to use the port 3000.
* `wget 10.244.0.7:3000`
* You will then see pod info like so:
```
Connecting to 10.244.0.7:3000 (10.244.0.7:3000)
saving to 'index.html'
index.html           100% |******************************************************************************************************************************************************|   103  0:00:00 ETA
'index.html' saved
/ # cat index.html 
{"pod_name":"pod-info-deployment-7587d5cc86-lkccq","pod_namespace":"development","pod_ip":"10.244.0.7"}/ #
```
* Now we have verified that the application is running.
* How to check that an application is working and if the cluster is not connected to the Internet. Use BusyBox and then run the `wget` request.