---
title: "Kubernetes 1.28 Beta Support For Using Swap On Li"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "kubernetes", "beta", "support", "swap"]
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

#### <img width="152" height="100" src="../_resources/kubecon-china-2024-white_3ec590b385a9492e9c51385f3-1.svg"/> [KubeCon + CloudNativeCon + Open Source Summit China 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-open-source-summit-ai-dev-china/)

Join us for three days of incredible opportunities to collaborate, learn and share with the cloud native community.  
[Buy your ticket now! 21 - 23 August | Hong Kong](https://events.linuxfoundation.org/kubecon-cloudnativecon-open-source-summit-ai-dev-china/register/?utm_source=kubernetes&utm_medium=all&utm_campaign=kubeconcn24&utm_content=slim-banner)

- [2024](https://kubernetes.io/blog/2024/08/20/websockets-transition/)

- [2023](https://kubernetes.io/blog/2023/12/20/contextual-logging-in-kubernetes-1-29/)

- <a id="m-blog-2023-12-20-contextual-logging-in-kubernetes-1-29"></a>[Contextual logging in Kubernetes 1.29: Better troubleshooting and enhanced logging](https://kubernetes.io/blog/2023/12/20/contextual-logging-in-kubernetes-1-29/)
- <a id="m-blog-2023-12-19-pod-ready-to-start-containers-condition-now-in-beta"></a>[Kubernetes 1.29: PodReadyToStartContainers Condition Moves to Beta](https://kubernetes.io/blog/2023/12/19/pod-ready-to-start-containers-condition-now-in-beta/)
- <a id="m-blog-2023-12-19-kubernetes-1-29-taint-eviction-controller"></a>[Kubernetes 1.29: Decoupling taint-manager from node-lifecycle-controller](https://kubernetes.io/blog/2023/12/19/kubernetes-1-29-taint-eviction-controller/)
- <a id="m-blog-2023-12-18-read-write-once-pod-access-mode-ga"></a>[Kubernetes 1.29: Single Pod Access Mode for PersistentVolumes Graduates to Stable](https://kubernetes.io/blog/2023/12/18/read-write-once-pod-access-mode-ga/)
- <a id="m-blog-2023-12-18-kubernetes-1-29-feature-loadbalancer-ip-mode-alpha"></a>[Kubernetes 1.29: New (alpha) Feature, Load Balancer IP Mode for Services](https://kubernetes.io/blog/2023/12/18/kubernetes-1-29-feature-loadbalancer-ip-mode-alpha/)
- <a id="m-blog-2023-12-15-kubernetes-1-29-volume-attributes-class"></a>[Kubernetes 1.29: VolumeAttributesClass for Volume Modification](https://kubernetes.io/blog/2023/12/15/kubernetes-1-29-volume-attributes-class/)
- <a id="m-blog-2023-12-15-csi-node-expand-secret-support-ga"></a>[Kubernetes 1.29: CSI Storage Resising Authenticated and Generally Available in v1.29](https://kubernetes.io/blog/2023/12/15/csi-node-expand-secret-support-ga/)
- <a id="m-blog-2023-12-14-cloud-provider-integration-changes"></a>[Kubernetes 1.29: Cloud Provider Integrations Are Now Separate Components](https://kubernetes.io/blog/2023/12/14/cloud-provider-integration-changes/)
- <a id="m-blog-2023-12-13-kubernetes-v1-29-release"></a>[Kubernetes v1.29: Mandala](https://kubernetes.io/blog/2023/12/13/kubernetes-v1-29-release/)
- <a id="m-blog-2023-11-28-gateway-api-ga"></a>[New Experimental Features in Gateway API v1.0](https://kubernetes.io/blog/2023/11/28/gateway-api-ga/)
- <a id="more-posts"></a>Show More Posts...

- [2022](https://kubernetes.io/blog/2022/12/30/advancements-in-kubernetes-traffic-engineering/)

- [2021](https://kubernetes.io/blog/2021/12/22/kubernetes-in-kubernetes-and-pxe-bootable-server-farm/)

- [2020](https://kubernetes.io/blog/2020/12/21/writing-crl-scheduler/)

- [2019](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-release-announcement/)

- [2018](https://kubernetes.io/blog/2018/12/12/kubernetes-federation-evolution/)

- [2017](https://kubernetes.io/blog/2017/12/Introducing-Kubeflow-Composable/)

- [2016](https://kubernetes.io/blog/2016/12/Kubernetes-Supports-Openapi/)

- [2015](https://kubernetes.io/blog/2015/12/Creating-Raspberry-Pi-Cluster-Running/)

# Kubernetes 1.28: Beta support for using swap on Linux

By **Itamar Holder (Red Hat)** | Thursday, August 24, 2023

The 1.22 release [introduced Alpha support](https://kubernetes.io/blog/2021/08/09/run-nodes-with-swap-alpha/) for configuring swap memory usage for Kubernetes workloads running on Linux on a per-node basis. Now, in release 1.28, support for swap on Linux nodes has graduated to Beta, along with many new improvements.

Prior to version 1.22, Kubernetes did not provide support for swap memory on Linux systems. This was due to the inherent difficulty in guaranteeing and accounting for pod memory utilisation when swap memory was involved. As a result, swap support was deemed out of scope in the initial design of Kubernetes, and the default behaviour of a kubelet was to fail to start if swap memory was detected on a node.

In version 1.22, the swap feature for Linux was initially introduced in its Alpha stage. This represented a significant advancement, providing Linux users with the opportunity to experiment with the swap feature for the first time. However, as an Alpha version, it was not fully developed and had several issues, including inadequate support for cgroup v2, insufficient metrics and summary API statistics, inadequate testing, and more.

Swap in Kubernetes has numerous [use cases](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2400-node-swap/README.md#user-stories) for a wide range of users. As a result, the node special interest group within the Kubernetes project has invested significant effort into supporting swap on Linux nodes for beta. Compared to the alpha, the kubelet's support for running with swap enabled is more stable and robust, more user-friendly, and addresses many known shortcomings. This graduation to beta represents a crucial step towards achieving the goal of fully supporting swap in Kubernetes.

## How do I use it?

The utilisation of swap memory on a node where it has already been provisioned can be facilitated by the activation of the `NodeSwap` feature gate on the kubelet. Additionally, you must disable the `failSwapOn` configuration setting, or the deprecated `--fail-swap-on` command line flag must be deactivated.

It is possible to configure the `memorySwap.swapBehavior` option to define the manner in which a node utilizes swap memory. For instance,

```
# this fragment goes into the kubelet's configuration file
memorySwap:

  swapBehavior: UnlimitedSwap
```

The available configuration options for `swapBehavior` are:

- `UnlimitedSwap` (default): Kubernetes workloads can use as much swap memory as they request, up to the system limit.
- `LimitedSwap`: The utilisation of swap memory by Kubernetes workloads is subject to limitations. Only Pods of [Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable) QoS are permitted to employ swap.

If configuration for `memorySwap` is not specified and the feature gate is enabled, by default the kubelet will apply the same behaviour as the `UnlimitedSwap` setting.

Note that `NodeSwap` is supported for **cgroup v2** only. For Kubernetes v1.28, using swap along with cgroup v1 is no longer supported.

## Install a swap-enabled cluster with kubeadm

### Before you begin

It is required for this demo that the kubeadm tool be installed, following the steps outlined in the [kubeadm installation guide](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm). If swap is already enabled on the node, cluster creation may proceed. If swap is not enabled, please refer to the provided instructions for enabling swap.

### Create a swap file and turn swap on

I'll demonstrate creating 4GiB of unencrypted swap.

```
dd if=/dev/zero of=/swapfile bs=128M count=32
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
swapon -s # enable the swap file only until this node is rebooted
```

To start the swap file at boot time, add line like `/swapfile swap swap defaults 0 0` to `/etc/fstab` file.

### Set up a Kubernetes cluster that uses swap-enabled nodes

To make things clearer, here is an example kubeadm configuration file `kubeadm-config.yaml` for the swap enabled cluster.

```
---
apiVersion: "kubeadm.k8s.io/v1beta3"
kind: InitConfiguration
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
failSwapOn: false
featureGates:

  NodeSwap: true
memorySwap:

  swapBehavior: LimitedSwap
```

Then create a single-node cluster using `kubeadm init --config kubeadm-config.yaml`. During init, there is a warning that swap is enabled on the node and in case the kubelet `failSwapOn` is set to true. We plan to remove this warning in a future release.

## How is the swap limit being determined with LimitedSwap?

The configuration of swap memory, including its limitations, presents a significant challenge. Not only is it prone to misconfiguration, but as a system-level property, any misconfiguration could potentially compromise the entire node rather than just a specific workload. To mitigate this risk and ensure the health of the node, we have implemented Swap in Beta with automatic configuration of limitations.

With `LimitedSwap`, Pods that do not fall under the Burstable QoS classification (i.e. `BestEffort`/`Guaranteed` Qos Pods) are prohibited from utilising swap memory. `BestEffort` QoS Pods exhibit unpredictable memory consumption patterns and lack information regarding their memory usage, making it difficult to determine a safe allocation of swap memory. Conversely, `Guaranteed` QoS Pods are typically employed for applications that rely on the precise allocation of resources specified by the workload, with memory being immediately available. To maintain the aforementioned security and node health guarantees, these Pods are not permitted to use swap memory when `LimitedSwap` is in effect.

Prior to detailing the calculation of the swap limit, it is necessary to define the following terms:

- `nodeTotalMemory`: The total amount of physical memory available on the node.
- `totalPodsSwapAvailable`: The total amount of swap memory on the node that is available for use by Pods (some swap memory may be reserved for system use).
- `containerMemoryRequest`: The container's memory request.

Swap limitation is configured as: `(containerMemoryRequest / nodeTotalMemory) × totalPodsSwapAvailable`

In other words, the amount of swap that a container is able to use is proportionate to its memory request, the node's total physical memory and the total amount of swap memory on the node that is available for use by Pods.

It is important to note that, for containers within Burstable QoS Pods, it is possible to opt-out of swap usage by specifying memory requests that are equal to memory limits. Containers configured in this manner will not have access to swap memory.

## How does it work?

There are a number of possible ways that one could envision swap use on a node. When swap is already provisioned and available on a node, SIG Node have [proposed](https://github.com/kubernetes/enhancements/blob/9d127347773ad19894ca488ee04f1cd3af5774fc/keps/sig-node/2400-node-swap/README.md#proposal) the kubelet should be able to be configured so that:

- It can start with swap on.
- It will direct the Container Runtime Interface to allocate zero swap memory to Kubernetes workloads by default.

Swap configuration on a node is exposed to a cluster admin via the [`memorySwap` in the KubeletConfiguration](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1). As a cluster administrator, you can specify the node's behaviour in the presence of swap memory by setting `memorySwap.swapBehavior`.

The kubelet [employs the CRI](https://kubernetes.io/docs/concepts/architecture/cri/) (container runtime interface) API to direct the CRI to configure specific cgroup v2 parameters (such as `memory.swap.max`) in a manner that will enable the desired swap configuration for a container. The CRI is then responsible to write these settings to the container-level cgroup.

## How can I monitor swap?

A notable deficiency in the Alpha version was the inability to monitor and introspect swap usage. This issue has been addressed in the Beta version introduced in Kubernetes 1.28, which now provides the capability to monitor swap usage through several different methods.

The beta version of kubelet now collects [node-level metric statistics](https://kubernetes.io/docs/reference/instrumentation/node-metrics/), which can be accessed at the `/metrics/resource` and `/stats/summary` kubelet HTTP endpoints. This allows clients who can directly interrogate the kubelet to monitor swap usage and remaining swap memory when using LimitedSwap. Additionally, a `machine_swap_bytes` metric has been added to cadvisor to show the total physical swap capacity of the machine.

## Caveats

Having swap available on a system reduces predictability. Swap's performance is worse than regular memory, sometimes by many orders of magnitude, which can cause unexpected performance regressions. Furthermore, swap changes a system's behaviour under memory pressure. Since enabling swap permits greater memory usage for workloads in Kubernetes that cannot be predictably accounted for, it also increases the risk of noisy neighbours and unexpected packing configurations, as the scheduler cannot account for swap memory usage.

The performance of a node with swap memory enabled depends on the underlying physical storage. When swap memory is in use, performance will be significantly worse in an I/O operations per second (IOPS) constrained environment, such as a cloud VM with I/O throttling, when compared to faster storage mediums like solid-state drives or NVMe.

As such, we do not advocate the utilisation of swap memory for workloads or environments that are subject to performance constraints. Furthermore, it is recommended to employ `LimitedSwap`, as this significantly mitigates the risks posed to the node.

Cluster administrators and developers should benchmark their nodes and applications before using swap in production scenarios, and [we need your help](#how-do-i-get-involved) with that!

### Security risk

Enabling swap on a system without encryption poses a security risk, as critical information, such as volumes that represent Kubernetes Secrets, [may be swapped out to the disk](https://kubernetes.io/docs/concepts/configuration/secret/#information-security-for-secrets). If an unauthorised individual gains access to the disk, they could potentially obtain these confidential data. To mitigate this risk, the Kubernetes project strongly recommends that you encrypt your swap space. However, handling encrypted swap is not within the scope of kubelet; rather, it is a general OS configuration concern and should be addressed at that level. It is the administrator's responsibility to provision encrypted swap to mitigate this risk.

Furthermore, as previously mentioned, with `LimitedSwap` the user has the option to completely disable swap usage for a container by specifying memory requests that are equal to memory limits. This will prevent the corresponding containers from accessing swap memory.

## Looking ahead

The Kubernetes 1.28 release introduced Beta support for swap memory on Linux nodes, and we will continue to work towards [general availability](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-stages) for this feature. I hope that this will include:

- Add the ability to set a system-reserved quantity of swap from what kubelet detects on the host.
- Adding support for controlling swap consumption at the Pod level via cgroups.
    - This point is still under discussion.
- Collecting feedback from test user cases.
    - We will consider introducing new configuration modes for swap, such as a node-wide swap limit for workloads.

## How can I learn more?

You can review the current [documentation](https://kubernetes.io/docs/concepts/architecture/nodes/#swap-memory) for using swap with Kubernetes.

For more information, and to assist with testing and provide feedback, please see [KEP-2400](https://github.com/kubernetes/enhancements/issues/4128) and its [design proposal](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2400-node-swap/README.md).

## How do I get involved?

Your feedback is always welcome! SIG Node [meets regularly](https://github.com/kubernetes/community/tree/master/sig-node#meetings) and [can be reached](https://github.com/kubernetes/community/tree/master/sig-node#contact) via [Slack](https://slack.k8s.io/) (channel **#sig-node**), or the SIG's [mailing list](https://groups.google.com/forum/#!forum/kubernetes-sig-node). A Slack channel dedicated to swap is also available at **#sig-node-swap**.

Feel free to reach out to me, Itamar Holder (**@iholder101** on Slack and GitHub) if you'd like to help or ask further questions.

- [←Previous](https://kubernetes.io/blog/2023/08/23/kubelet-podresources-api-ga/)
[Next→](https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/)

[RSS Feed](https://kubernetes.io/feed.xml)[Submit a Post](https://kubernetes.io/docs/contribute/new-content/blogs-case-studies/)[@Kubernetesio](https://twitter.com/kubernetesio)[on GitHub](https://github.com/kubernetes/kubernetes)[#kubernetes-users](http://slack.k8s.io)[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes)[Forum](https://discuss.kubernetes.io)[Kubernetes](https://kubernetes.io/docs/setup)

[Documentation](https://kubernetes.io/docs/home/) [Blog](https://kubernetes.io/blog/) [Training](https://kubernetes.io/training/) [Partners](https://kubernetes.io/partners/) [Community](https://kubernetes.io/community/) [Case Studies](https://kubernetes.io/case-studies/)

- [](https://discuss.kubernetes.io)
- [](https://twitter.com/kubernetesio)
- [](https://calendar.google.com/calendar/embed?src=calendar%40kubernetes.io)
- [](https://youtube.com/kubernetescommunity)

- [](https://github.com/kubernetes/kubernetes)
- [](https://slack.k8s.io)
- [](https://git.k8s.io/community/contributors/guide)
- [](https://stackoverflow.com/questions/tagged/kubernetes)

© 2024 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/licence)  
Copyright © 2024 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)  
ICP licence: 京ICP备17074266号-3