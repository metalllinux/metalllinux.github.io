---
title: "Solution Explore Environment"
category: "cka-certification"
tags: ["cka-certification", "solution", "explore", "environment"]
---

* How to find the interface configured for cluster connectivity:
* Run this command to see IP addresses assigned to nodes:
```
kubectl get nodes -o wide
```
* Then for network interfaces, don't over-complicate it, its `ip a`.
* Default interface for `containerd` is `cni0`
* Command to find the default gateway:
```
ip route show default
```
* How to find the port that the `kubescheduler` is running on:
```
netstat -nplt | grep scheduler
```
* An example of the `netstat` command output:
```
tcp        0      0 127.0.0.1:10259         0.0.0.0:*               LISTEN      3200/kube-scheduler
```
* Here the port that is being listened on is the third one in.
* How to find which ports the `etcd-server` is listening on:
```
netstat -anp | grep etcd | grep 2380 | wc -l 
```
* The same is also for:
```
netstat -anp | grep etcd | grep 2379 | wc -l 
81
```
* Port `2379` is the one in `etcd-server` that everything connects to.