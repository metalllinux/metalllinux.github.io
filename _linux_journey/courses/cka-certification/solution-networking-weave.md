---
title: "Solution Networking Weave"
category: "cka-certification"
tags: ["cka-certification", "solution", "networking", "weave"]
---

* Find the networking solution that is available for the cluster under `/etc/cni/net.d/`.
* How to check how many Weave Agent Peers are available:
```
kubectl get pods -n kube-system
```
* How to check which nodes have a Weave Agent Peer present:
```
kubectl get po -owide -n kube-system | grep weave
```
* How to check the bridge network / interface created by Weave on each node:
```
ip link
```
* How to check the POD IP address range created by Weave:
```
ip addr show weave
```
* How to check the default gateway configured on the PODs, scheduled on <node_here>?:
```
ssh <node_here>
ip route | grep weave
```