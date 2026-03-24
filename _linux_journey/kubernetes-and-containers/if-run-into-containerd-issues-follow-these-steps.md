---
title: "If Run Into Containerd Issues Follow These Steps"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "run", "into", "containerd", "issues"]
---

```
sudo rm /etc/containerd/config.toml
sudo systemctl restart containerd
sudo kubeadm init --control-plane-endpoint=8-6-lts-master
```