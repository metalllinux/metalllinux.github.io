---
title: "Introduction to Deployment with kubeadm"
category: "cka-certification"
tags: ["cka-certification", "introduction", "deployment", "kubeadm"]
---

# Introduction to Deployment with kubeadm

* `kubeadm` consists of the following:

* Master 
  * kube-apiserver
  * etcd
  * node-controller
  * replica-controller
* Worker 1
  * kubelet
  * container runtime (docker)
* Worker 2
  * kubelet
  * container runtime (docker)

* Installing all of the above components and setting up certificates is tedious.

* Need to install `containerd` on all of the nodes.

* Then need to install the `kubeadm` tool on all of the nodes as well.

* Kubernetes installs all of the right components on the right nodes in the right order.

* Need to initialise the Master Node.

* Once the Master Node is initialised, but before the Worker Nodes are hooked up to the cluster, Network prerequisites must be met.

    * Normal networking is not good enough, the Master Node needs a special networking solution between the Master and Worker Nodes called the POD Network.
    
* Once the POD Network is setup, the Worker Nodes join the Master Node.

* Can then deploy the application onto the Kubernetes environment.


