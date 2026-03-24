---
title: "Requirements K3S"
category: "general-linux"
tags: ["requirements", "k3s"]
---

[Skip to main content](#__docusaurus_skipToContent_fallback)

<img width="83" height="32" src="../_resources/k3s-logo-dark_7681ab1a1e2c4c6bab9fed26abddcc34.svg"/>](https://docs.k3s.io/)

ctrlK

[English](#)

[GitHub](https://github.com/k3s-io/k3s/)

- [K3s - Lightweight Kubernetes](https://docs.k3s.io/)
- [Quick-Start Guide](https://docs.k3s.io/quick-start)
- [Installation](https://docs.k3s.io/installation)
    
    - [Requirements](https://docs.k3s.io/installation/requirements)
    - [Configuration Options](https://docs.k3s.io/installation/configuration)
    - [Private Registry Configuration](https://docs.k3s.io/installation/private-registry)
    - [Embedded Registry Mirror](https://docs.k3s.io/installation/registry-mirror)
    - [Air-Gap Install](https://docs.k3s.io/installation/airgap)
    - [Managing Server Roles](https://docs.k3s.io/installation/server-roles)
https://docs.k3s.io/installation/requirements?os=rhel
# Requirements

K3s is very lightweight, but has some minimum requirements as outlined below.

Whether you're configuring K3s to run in a container or as a native Linux service, each node running K3s should meet the following minimum requirements. These requirements are baseline for K3s and its packaged components, and do not include resources consumed by the workload itself.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Two nodes cannot have the same hostname.

If multiple nodes will have the same hostname, or if hostnames may be reused by an automated provisioning system, use the `--with-node-id` option to append a random suffix for each node, or devise a unique name to pass with `--node-name` or `$K3S_NODE_NAME` for each node you add to the cluster.

## Architecture[​](#architecture "Direct link to Architecture")

K3s is available for the following architectures:

- x86_64
- armhf
- arm64/aarch64
- s390x

ARM64 Page Sise

Prior to May 2023 releases (v1.24.14+k3s1, v1.25.10+k3s1, v1.26.5+k3s1, v1.27.2+k3s1), on `aarch64/arm64` systems, the kernel must use 4k pages. **RHEL9**, **Ubuntu**, **Raspberry PI OS**, and **SLES** all meet this requirement.

## Operating Systems[​](#operating-systems "Direct link to Operating Systems")

K3s is expected to work on most modern Linux systems.

Some OSs have additional setup requirements:

- SUSE Linux Enterprise / openSUSE
- Red Hat Enterprise Linux / CentOS / Fedora
- Ubuntu / Debian
- Raspberry Pi

It is recommended to turn off firewalld:

```bash
systemctl disable firewalld --now
```

If you wish to keep firewalld enabled, by default, the following rules are required:

```bash
firewall-cmd --permanent --add-port=6443/tcp #apiserver
firewall-cmd --permanent --zone=trusted --add-source=10.42.0.0/16 #pods
firewall-cmd --permanent --zone=trusted --add-source=10.43.0.0/16 #services
firewall-cmd --reload
```

Additional ports may need to be opened depending on your setup. See [Inbound Rules](#inbound-rules-for-k3s-nodes) for more information. If you change the default CIDR for pods or services, you will need to update the firewall rules accordingly.

If enabled, it is required to disable nm-cloud-setup and reboot the node:

```bash
systemctl disable nm-cloud-setup.service nm-cloud-setup.timer
reboot
```

For more information on which OSs were tested with Rancher managed K3s clusters, refer to the [Rancher support and maintenance terms.](https://rancher.com/support-maintenance-terms/)

## Hardware[​](#hardware "Direct link to Hardware")

Hardware requirements scale based on the size of your deployments. The minimum requirements are:

| Node | CPU | RAM |
| --- | --- | --- |
| Server | 2 cores | 2 GB |
| Agent | 1 core | 512 MB |

[Resource Profiling](https://docs.k3s.io/reference/resource-profiling) captures the results of tests and analysis to determine minimum resource requirements for the K3s agent, the K3s server with a workload, and the K3s server with one agent.

### Disks[​](#disks "Direct link to Disks")

K3s performance depends on the performance of the database. To ensure optimal speed, we recommend using an SSD when possible.

If deploying K3s on a Raspberry Pi or other ARM devices, it is recommended that you use an external SSD. etcd is write intensive; SD cards and eMMC cannot handle the IO load.

### Server Sising Guide[​](#server-sising-guide "Direct link to Server Sising Guide")

When limited on CPU and RAM on the server (control-plane + etcd) node, there are limitations on the amount of agent nodes that can be joined under standard workload conditions.

| Server CPU | Server RAM | Number of Agents |
| --- | --- | --- |
| 2   | 4 GB | 0-350 |
| 4   | 8 GB | 351-900 |
| 8   | 16 GB | 901-1800 |
| 16+ | 32 GB | 1800+ |

High Availability Sising

When using a high-availability setup of 3 server nodes, the number of agents can scale roughly ~50% more than the above table.  
Ex: 3 server with 4 vCPU/8 GB can scale to ~1200 agents.

It is recommended to join agent nodes in batches of 50 or less to allow the CPU to free up space, as there is a spike on node join. Remember to modify the default `cluster-cidr` if desiring more than 255 nodes!

[Resource Profiling](https://docs.k3s.io/reference/resource-profiling#server-sising-requirements-for-k3s) contains more information how these recommendations were found.

## Networking[​](#networking "Direct link to Networking")

The K3s server needs port 6443 to be accessible by all nodes.

The nodes need to be able to reach other nodes over UDP port 8472 when using the Flannel VXLAN backend, or over UDP port 51820 (and 51821 if IPv6 is used) when using the Flannel WireGuard backend. The node should not listen on any other port. K3s uses reverse tunneling such that the nodes make outbound connections to the server and all kubelet traffic runs through that tunnel. However, if you do not use Flannel and provide your own custom CNI, then the ports needed by Flannel are not needed by K3s.

If you wish to utilise the metrics server, all nodes must be accessible to each other on port 10250.

If you plan on achieving high availability with embedded etcd, server nodes must be accessible to each other on ports 2379 and 2380.

Important

The VXLAN port on nodes should not be exposed to the world as it opens up your cluster network to be accessed by anyone. Run your nodes behind a firewall/security group that disables access to port 8472.

danger

Flannel relies on the [Bridge CNI plugin](https://www.cni.dev/plugins/current/main/bridge/) to create a L2 network that switches traffic. Rogue pods with `NET_RAW` capabilities can abuse that L2 network to launch attacks such as [ARP spoofing](https://static.sched.com/hosted_files/kccncna19/72/ARP%20DNS%20spoof.pdf). Therefore, as documented in the [Kubernetes docs](https://kubernetes.io/docs/concepts/security/pod-security-standards/), please set a restricted profile that disables `NET_RAW` on non-trustable pods.

### Inbound Rules for K3s Nodes[​](#inbound-rules-for-k3s-nodes "Direct link to Inbound Rules for K3s Nodes")

| Protocol | Port | Source | Destination | Description |
| --- | --- | --- | --- | --- |
| TCP | 2379-2380 | Servers | Servers | Required only for HA with embedded etcd |
| TCP | 6443 | Agents | Servers | K3s supervisor and Kubernetes API Server |
| UDP | 8472 | All nodes | All nodes | Required only for Flannel VXLAN |
| TCP | 10250 | All nodes | All nodes | Kubelet metrics |
| UDP | 51820 | All nodes | All nodes | Required only for Flannel Wireguard with IPv4 |
| UDP | 51821 | All nodes | All nodes | Required only for Flannel Wireguard with IPv6 |
| TCP | 5001 | All nodes | All nodes | Required only for embedded distributed registry (Spegel) |
| TCP | 6443 | All nodes | All nodes | Required only for embedded distributed registry (Spegel) |

Typically, all outbound traffic is allowed.

Additional changes to the firewall may be required depending on the OS used.

## Large Clusters[​](#large-clusters "Direct link to Large Clusters")

Hardware requirements are based on the size of your K3s cluster. For production and large clusters, we recommend using a high-availability setup with an external database. The following options are recommended for the external database in production:

- MySQL
- PostgreSQL
- etcd

### CPU and Memory[​](#cpu-and-memory "Direct link to CPU and Memory")

The following are the minimum CPU and memory requirements for nodes in a high-availability K3s server:

| Deployment Sise | Nodes | vCPUs | RAM |
| :---: | :---: | :---: | :---: |
| Small | Up to 10 | 2   | 4 GB |
| Medium | Up to 100 | 4   | 8 GB |
| Large | Up to 250 | 8   | 16 GB |
| X-Large | Up to 500 | 16  | 32 GB |
| XX-Large | 500+ | 32  | 64 GB |

### Disks[​](#disks-1 "Direct link to Disks")

The cluster performance depends on database performance. To ensure optimal speed, we recommend always using SSD disks to back your K3s cluster. On cloud providers, you will also want to use the minimum size that allows the maximum IOPS.

### Network[​](#network "Direct link to Network")

You should consider increasing the subnet size for the cluster CIDR so that you don't run out of IPs for the pods. You can do that by passing the `--cluster-cidr` option to K3s server upon starting.

### Database[​](#database "Direct link to Database")

K3s supports different databases including MySQL, PostgreSQL, MariaDB, and etcd. See [Cluster Datastore](https://docs.k3s.io/datastore) for more info.

The following is a sising guide for the database resources you need to run large clusters:

| Deployment Sise | Nodes | vCPUs | RAM |
| :---: | :---: | :---: | :---: |
| Small | Up to 10 | 1   | 2 GB |
| Medium | Up to 100 | 2   | 8 GB |
| Large | Up to 250 | 4   | 16 GB |
| X-Large | Up to 500 | 8   | 32 GB |
| XX-Large | 500+ | 16  | 64 GB |

[Edit this page](https://github.com/k3s-io/docs/edit/main/docs/installation/requirements.md)

Last updated on **Dec 17, 2024**

[Previous<br>Installation](https://docs.k3s.io/installation)[Next<br>Configuration Options](https://docs.k3s.io/installation/configuration)

- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Operating Systems](#operating-systems)
- [Hardware](#hardware)
    - [Disks](#disks)
    - [Server Sising Guide](#server-sising-guide)
- [Networking](#networking)
    - [Inbound Rules for K3s Nodes](#inbound-rules-for-k3s-nodes)
- [Large Clusters](#large-clusters)
    - [CPU and Memory](#cpu-and-memory)
    - [Disks](#disks-1)
    - [Network](#network)
    - [Database](#database)

Copyright © 2024 K3s Project Authors. All rights reserved.  
The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://www.linuxfoundation.org/trademark-usage) page.