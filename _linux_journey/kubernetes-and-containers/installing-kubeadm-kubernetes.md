---
title: "Installing Kubeadm Kubernetes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "installing", "kubeadm", "kubernetes"]
---

[](https://kubernetes.io/)

- [Documentation](https://kubernetes.io/docs/)
- [Kubernetes Blog](https://kubernetes.io/blog/)
- [Training](https://kubernetes.io/training/)
- [Partners](https://kubernetes.io/partners/)
- [Community](https://kubernetes.io/community/)
- [Case Studies](https://kubernetes.io/case-studies/)
- <a id="navbarDropdown"></a>[Versions](#)
- <a id="navbarDropdownMenuLink"></a>[English](#)

- - <a id="m-docs-home"></a>[Documentation](https://kubernetes.io/docs/home/ "Kubernetes Documentation")
    - <a id="m-docs-setup"></a>[Getting started](https://kubernetes.io/docs/setup/)
        - <a id="m-docs-setup-learning-environment"></a>[Learning environment](https://kubernetes.io/docs/setup/learning-environment/)
        - <a id="m-docs-setup-production-environment"></a>[Production environment](https://kubernetes.io/docs/setup/production-environment/)
            - <a id="m-docs-setup-production-environment-container-runtimes"></a>[Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
            - <a id="m-docs-setup-production-environment-tools"></a>[Installing Kubernetes with deployment tools](https://kubernetes.io/docs/setup/production-environment/tools/)
                - <a id="m-docs-setup-production-environment-tools-kubeadm"></a>[Bootstrapping clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-install-kubeadm"></a>[Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-troubleshooting-kubeadm"></a>[Troubleshooting kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-create-cluster-kubeadm"></a>[Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-control-plane-flags"></a>[Customising components with the kubeadm API](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-ha-topology"></a>[Options for Highly Available Topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-high-availability"></a>[Creating Highly Available Clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-setup-ha-etcd-with-kubeadm"></a>[Set up a High Availability etcd Cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-kubelet-integration"></a>[Configuring each kubelet in your cluster using kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/)
                    - <a id="m-docs-setup-production-environment-tools-kubeadm-dual-stack-support"></a>[Dual-stack support with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/dual-stack-support/)
            - <a id="m-docs-setup-production-environment-turnkey-https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#check-required-ports
# Installing kubeadm

<img width="150" height="171" src="../_resources/kubeadm-stacked-color_f0170983533742b18f5d60989225.png"/> This page shows how to install the `kubeadm` toolbox. For information on how to create a cluster with kubeadm once you have performed this installation process, see the [Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) page.

This installation guide is for Kubernetes v1.32. If you want to use a different Kubernetes version, please refer to the following pages instead:

- [Installing kubeadm (Kubernetes v1.31)](https://v1-31.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Installing kubeadm (Kubernetes v1.30)](https://v1-30.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Installing kubeadm (Kubernetes v1.29)](https://v1-29.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Installing kubeadm (Kubernetes v1.28)](https://v1-28.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

## Before you begin

- A compatible Linux host. The Kubernetes project provides generic instructions for Linux distributions based on Debian and Red Hat, and those distributions without a package manager.
- 2 GB or more of RAM per machine (any less will leave little room for your apps).
- 2 CPUs or more for control plane machines.
- Full network connectivity between all machines in the cluster (public or private network is fine).
- Unique hostname, MAC address, and product_uuid for every node. See [here](#verify-mac-address) for more details.
- Certain ports are open on your machines. See [here](#check-required-ports) for more details.

#### Note:

The `kubeadm` installation is done via binaries that use dynamic linking and assumes that your target system provides `glibc`. This is a reasonable assumption on many Linux distributions (including Debian, Ubuntu, Fedora, CentOS, etc.) but it is not always the case with custom and lightweight distributions which don't include `glibc` by default, such as Alpine Linux. The expectation is that the distribution either includes `glibc` or a [compatibility layer](https://wiki.alpinelinux.org/wiki/Running_glibc_programs) that provides the expected symbols.

## Verify the MAC address and product_uuid are unique for every node

- You can get the MAC address of the network interfaces using the command `ip link` or `ifconfig -a`
- The product_uuid can be checked by using the command `sudo cat /sys/class/dmi/id/product_uuid`

It is very likely that hardware devices will have unique addresses, although some virtual machines may have identical values. Kubernetes uses these values to uniquely identify the nodes in the cluster. If these values are not unique to each node, the installation process may [fail](https://github.com/kubernetes/kubeadm/issues/31).

## Check network adapters

If you have more than one network adapter, and your Kubernetes components are not reachable on the default route, we recommend you add IP route(s) so Kubernetes cluster addresses go via the appropriate adapter.

## Check required ports

These [required ports](https://kubernetes.io/docs/reference/networking/ports-and-protocols/) need to be open in order for Kubernetes components to communicate with each other. You can use tools like [netcat](https://netcat.sourceforge.net) to check if a port is open. For example:

```
nc 127.0.0.1 6443 -zv -w 2
```

The pod network plugin you use may also require certain ports to be open. Since this differs with each pod network plugin, please see the documentation for the plugins about what port(s) those need.

## Swap configuration

The default behaviour of a kubelet is to fail to start if swap memory is detected on a node. This means that swap should either be disabled or tolerated by kubelet.

- To tolerate swap, add `failSwapOn: false` to kubelet configuration or as a command line argument. Note: even if `failSwapOn: false` is provided, workloads wouldn't have swap access by default. This can be changed by setting a `swapBehavior`, again in the kubelet configuration file. To use swap, set a `swapBehavior` other than the default `NoSwap` setting. See [Swap memory management](https://kubernetes.io/docs/concepts/architecture/nodes/#swap-memory) for more details.
- To disable swap, `sudo swapoff -a` can be used to disable swapping temporarily. To make this change persistent across reboots, make sure swap is disabled in config files like `/etc/fstab`, `systemd.swap`, depending how it was configured on your system.

## Installing a container runtime

To run containers in Pods, Kubernetes uses a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes).

By default, Kubernetes uses the [Container Runtime Interface](https://kubernetes.io/docs/concepts/architecture/cri) (CRI) to interface with your chosen container runtime.

If you don't specify a runtime, kubeadm automatically tries to detect an installed container runtime by scanning through a list of known endpoints.

If multiple or no container runtimes are detected kubeadm will throw an error and will request that you specify which one you want to use.

See [container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) for more information.

#### Note:

Docker Engine does not implement the [CRI](https://kubernetes.io/docs/concepts/architecture/cri/) which is a requirement for a container runtime to work with Kubernetes. For that reason, an additional service [cri-dockerd](https://mirantis.github.io/cri-dockerd/) has to be installed. cri-dockerd is a project based on the legacy built-in Docker Engine support that was [removed](https://kubernetes.io/dockershim) from the kubelet in version 1.24.

The tables below include the known endpoints for supported operating systems:

- [Linux](#container-runtime-0)
- [Windows](#container-runtime-1)

| Runtime | Path to Unix domain socket |
| --- | --- |
| containerd | `unix:///var/run/containerd/containerd.sock` |
| CRI-O | `unix:///var/run/crio/crio.sock` |
| Docker Engine (using cri-dockerd) | `unix:///var/run/cri-dockerd.sock` |

## Installing kubeadm, kubelet and kubectl

You will install these packages on all of your machines:

- `kubeadm`: the command to bootstrap the cluster.
    
- `kubelet`: the component that runs on all of the machines in your cluster and does things like starting pods and containers.
    
- `kubectl`: the command line util to talk to your cluster.
    

kubeadm **will not** install or manage `kubelet` or `kubectl` for you, so you will need to ensure they match the version of the Kubernetes control plane you want kubeadm to install for you. If you do not, there is a risk of a version skew occurring that can lead to unexpected, buggy behaviour. However, *one* minor version skew between the kubelet and the control plane is supported, but the kubelet version may never exceed the API server version. For example, the kubelet running 1.7.0 should be fully compatible with a 1.8.0 API server, but not vice versa.

For information about installing `kubectl`, see [Install and set up kubectl](https://kubernetes.io/docs/tasks/tools/).

#### Warning:

These instructions exclude all Kubernetes packages from any system upgrades. This is because kubeadm and Kubernetes require [special attention to upgrade](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/).

For more information on version skews, see:

- Kubernetes [version and version-skew policy](https://kubernetes.io/docs/setup/release/version-skew-policy/)
- Kubeadm-specific [version skew policy](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#version-skew-policy)

**Note:** The legacy package repositories (`apt.kubernetes.io` and `yum.kubernetes.io`) have been [deprecated and frozen starting from September 13, 2023](https://kubernetes.io/blog/2023/08/31/legacy-package-repository-deprecation/). **Using the [new package repositories hosted at `pkgs.k8s.io`](https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/) is strongly recommended and required in order to install Kubernetes versions released after September 13, 2023.** The deprecated legacy repositories, and their contents, might be removed at any time in the future and without a further notice period. The new package repositories provide downloads for Kubernetes versions starting with v1.24.0.

#### Note:

There's a dedicated package repository for each Kubernetes minor version. If you want to install a minor version other than v1.32, please see the installation guide for your desired minor version.

- [Debian-based distributions](#k8s-install-0)
- [Red Hat-based distributions](#k8s-install-1)
- [Without a package manager](#k8s-install-2)

These instructions are for Kubernetes v1.32.

1.  Update the `apt` package index and install packages needed to use the Kubernetes `apt` repository:
    
    ```
    sudo apt-get update
    # apt-transport-https may be a dummy package; if so, you can skip that package
    sudo apt-get install -y apt-transport-https ca-certificates curl gpg
    ```
    
2.  Download the public signing key for the Kubernetes package repositories. The same signing key is used for all repositories so you can disregard the version in the URL:
    
    ```
    # If the directory `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
    # sudo mkdir -p -m 755 /etc/apt/keyrings
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    ```
    

#### Note:

In releases older than Debian 12 and Ubuntu 22.04, directory `/etc/apt/keyrings` does not exist by default, and it should be created before the curl command.

3.  Add the appropriate Kubernetes `apt` repository. Please note that this repository have packages only for Kubernetes 1.32; for other Kubernetes minor versions, you need to change the Kubernetes minor version in the URL to match your desired minor version (you should also check that you are reading the documentation for the version of Kubernetes that you plan to install).
    
    ```
    # This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
    echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
    ```
    
4.  Update the `apt` package index, install kubelet, kubeadm and kubectl, and pin their version:
    
    ```
    sudo apt-get update
    sudo apt-get install -y kubelet kubeadm kubectl
    sudo apt-mark hold kubelet kubeadm kubectl
    ```
    
5.  (Optional) Enable the kubelet service before running kubeadm:
    
    ```
    sudo systemctl enable --now kubelet
    ```
    

The kubelet is now restarting every few seconds, as it waits in a crashloop for kubeadm to tell it what to do.

## Configuring a cgroup driver

Both the container runtime and the kubelet have a property called ["cgroup driver"](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#cgroup-drivers), which is important for the management of cgroups on Linux machines.

#### Warning:

Matching the container runtime and kubelet cgroup drivers is required or otherwise the kubelet process will fail.

See [Configuring a cgroup driver](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/) for more details.

## Troubleshooting

If you are running into difficulties with kubeadm, please consult our [troubleshooting docs](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/).

## What's next

- [Using kubeadm to Create a Cluster](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)

## Feedback

Was this page helpful?

Last modified March 08, 2025 at 1:56 PM PST: [Update the check for open port in install-kubeadm.md (7086544485)](https://github.com/kubernetes/website/commit/7086544485a3a02de487e9ab2c2967c1abd472ed)

[Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/setup/production-environment/tools/kubeadm/install-kubeadm.md) [Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/setup/production-environment/tools/kubeadm/install-kubeadm.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A) [Create an issue](https://github.com/kubernetes/website/issues/new?title=Installing%20kubeadm) <a id="print"></a>[Print entire section](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/_print/)

- [Before you begin](#before-you-begin)
- [Verify the MAC address and product_uuid are unique for every node](#verify-mac-address)
- [Check network adapters](#check-network-adapters)
- [Check required ports](#check-required-ports)
- [Swap configuration](#swap-configuration)
- [Installing a container runtime](#installing-runtime)
- [Installing kubeadm, kubelet and kubectl](#installing-kubeadm-kubelet-and-kubectl)
- [Configuring a cgroup driver](#configuring-a-cgroup-driver)
- [Troubleshooting](#troubleshooting)
- [What's next](#what-s-next)

© 2025 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/licence)

© 2025 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)

ICP licence: 京ICP备17074266号-3

- [](https://youtube.com/kubernetescommunity)
- [](https://discuss.kubernetes.io)
- [](https://serverfault.com/questions/tagged/kubernetes)
- [](https://www.linkedin.com/company/kubernetes/)

- [](https://k8s.dev/)
- [](https://github.com/kubernetes/kubernetes)
- [](https://slack.k8s.io)
- [](https://calendar.google.com/calendar/embed?src=calendar%40kubernetes.io)