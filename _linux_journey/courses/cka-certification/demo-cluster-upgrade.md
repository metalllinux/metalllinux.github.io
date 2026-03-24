---
title: "Demo Cluster Upgrade"
category: "cka-certification"
tags: ["cka-certification", "demo", "cluster", "upgrade"]
---

* Older upgrade package repositories have been deprecated. New packages are available at pkgs.k8s.io
https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/
* Separate package repository for each minor version.
* `kubeadm` needs to be upgraded first, so it can upgrade the cluster to the version it was upgraded to.
* `kubeadm` does not upgrade the `kubelet`
* Run `kubeadm upgrade apply <version>` to upgrade the cluster (aside from the `kubelet`) to version
* Must also drain Control Plane nodes as well.