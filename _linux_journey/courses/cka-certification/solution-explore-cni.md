---
title: "Solution Explore Cni"
category: "cka-certification"
tags: ["cka-certification", "solution", "explore", "cni"]
---

* How to inspect the kubelet service and identify the container runtime endpoint value set for kubernetes:
* Run this command:
```
ps -aux | grep kubelet | grep --color container-runtime-endpoint
```
* In this case, the answer would be:
```
unix:///var/run/containerd/containerd.sock
```
* How to find the path configured with all binaries of the CNI supported plugins:
```
/opt/cni/bin
```
* How to identify plugins that are not available on the host:
```
ls -l /opt/cni/bin
```
* How to check the CNI plugin that is used on a cluster:
```
ls /etc/cni/net.d/
```
* An example output would be:
```
10-flannel.pluginconflist
```
* How to check the binary executable file that runs by a kubelet after its container and associated namespaces are created?
* Check the `type` field of the previously identified plugin:
```
/etc/cni/net.d/10-flannel.conflist
```
* In this case, the answer is `flannel`.