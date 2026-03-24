---
title: "Steps to Upgrade the Controlplane Node"
category: "cka-certification"
tags: ["cka-certification", "solution", "cluster", "upgrade"]
---

* How find the latest version of an upgrade available:
```
kubeadm upgrade plan
```
### Steps to Upgrade the Controlplane Node
To seamlessly transition from Kubernetes v1.30 to v1.31 and gain access to the packages specific to the desired Kubernetes minor version, follow these essential steps during the upgrade process. This ensures that your environment is appropriately configured and aligned with the features and improvements introduced in Kubernetes v1.31.

On the controlplane node:

Use any text editor you prefer to open the file that defines the Kubernetes apt repository.

vim /etc/apt/sources.list.d/kubernetes.list

Update the version in the URL to the next available minor release, i.e v1.31.

deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /

After making changes, save the file and exit from your text editor. Proceed with the next instruction.

apt update

apt-cache madison kubeadm

Based on the version information displayed by apt-cache madison, it indicates that for Kubernetes version 1.31.0, the available package version is 1.31.0-1.1. Therefore, to install kubeadm for Kubernetes v1.31.0, use the following command:

apt-get install kubeadm=1.31.0-1.1

Run the following command to upgrade the Kubernetes cluster.

kubeadm upgrade plan v1.31.0

kubeadm upgrade apply v1.31.0

    Note that the above steps can take a few minutes to complete.

Now, upgrade the Kubelet version. Also, mark the node (in this case, the "controlplane" node) as schedulable.

apt-get install kubelet=1.31.0-1.1

Run the following commands to refresh the systemd configuration and apply changes to the Kubelet service:

systemctl daemon-reload

systemctl restart kubelet

### Steps to Upgrade the Worker Node:
On the node01 node, run the following commands:

    If you are on the controlplane node, run ssh node01 to log in to the node01.

Use any text editor you prefer to open the file that defines the Kubernetes apt repository.

vim /etc/apt/sources.list.d/kubernetes.list

Update the version in the URL to the next available minor release, i.e v1.31.

deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /

After making changes, save the file and exit from your text editor. Proceed with the next instruction.

apt update

apt-cache madison kubeadm

Based on the version information displayed by apt-cache madison, it indicates that for Kubernetes version 1.31.0, the available package version is 1.31.0-1.1. Therefore, to install kubeadm for Kubernetes v1.31.0, use the following command:

apt-get install kubeadm=1.31.0-1.1

### Upgrade the Worker Node 
kubeadm upgrade node

Now, upgrade the Kubelet version.

apt-get install kubelet=1.31.0-1.1

Run the following commands to refresh the systemd configuration and apply changes to the Kubelet service:

systemctl daemon-reload

systemctl restart kubelet

    Type exit or logout or enter CTRL + d to go back to the controlplane node.

* How to check how which nodes can host applications. Check for taints:
```
kubectl describe nodes <node> | grep -i taints
```
* How to check which nodes that pods are assigned to:
```
kubectl get pods -o wide
```
* What is the latest stable version of Kubernetes that the `kubeadm` tools knows of:
```
kubeadm upgrade plan
```
* How to drain a node and mark it as unschedulable:
```
kubectl drain <node> --ignore-daemonsets
```
* Need to upgrade the `kubeadm` tool --> other controlplane nodes and then the `kubelet`.
* Can skip the CNI provider.
* Final steps are upgrading `kubectl` and `kubelet`